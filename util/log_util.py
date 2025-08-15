from abc import ABC, abstractmethod
import time
from functools import wraps
from typing import Callable, Any


# 1. Logger interface (abstraction)
class LoggerInterface(ABC):
    @abstractmethod
    def debug(self, message: str):
        pass

    @abstractmethod
    def info(self, message: str):
        pass

    @abstractmethod
    def warning(self, message: str):
        pass

    @abstractmethod
    def error(self, message: str, exc_info: bool = False):
        pass


# 2. Default implementation using Python's logging module
class StdLogger(LoggerInterface):
    def __init__(self, name: str):
        import logging
        self.logger = logging.getLogger(name)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str, exc_info: bool = False):
        self.logger.error(message, exc_info=exc_info)


# 3. Log aspect implementation
class LogAspect:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def log_method(self, description: str = ""):
        """Decorator for method logging"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                # Get method info
                class_name = args[0].__class__.__name__ if args else "UnknownClass"
                method_name = func.__name__
                full_desc = description if description else f"{class_name}.{method_name}"

                # Pre-execution log (Before advice)
                self.logger.info(f"[START] {full_desc} - Args: {args[1:]}, Kwargs: {kwargs}")
                start_time = time.time()

                try:
                    # Execute the target method
                    result = func(*args, **kwargs)
                    
                    # Post-execution log (After returning advice)
                    elapsed = (time.time() - start_time) * 1000
                    self.logger.info(
                        f"[SUCCESS] {full_desc} - Completed in {elapsed:.2f}ms - Result: {str(result)[:200]}"
                    )
                    return result

                except Exception as e:
                    # Exception log (After throwing advice)
                    elapsed = (time.time() - start_time) * 1000
                    self.logger.error(
                        f"[FAILED] {full_desc} - Failed in {elapsed:.2f}ms - Error: {str(e)}",
                        exc_info=True
                    )
                    raise  # Re-throw the exception to not affect business logic

            return wrapper
        return decorator


# 4. Logger factory (for easy replacement of logging implementations)
class LoggerFactory:
    @staticmethod
    def get_logger(name: str) -> LoggerInterface:
        # To replace logging library, just change the implementation here
        # e.g. return LoguruLogger(name) or StructLogger(name)
        return StdLogger(name)

    @staticmethod
    def get_log_aspect(name: str) -> LogAspect:
        logger = LoggerFactory.get_logger(name)
        return LogAspect(logger)
    