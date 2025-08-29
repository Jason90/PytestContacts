import os
import time
import inspect
from functools import wraps
from typing import Callable, Any
from abc import ABC, abstractmethod
from util import re_util


# 1. Logger interface (abstraction)
class LoggerInterface(ABC):
    @abstractmethod
    def debug(self, message: str, *args: Any): 
        pass

    @abstractmethod
    def info(self, message: str, *args: Any):
        pass

    @abstractmethod
    def warning(self, message: str, *args: Any):
        pass

    @abstractmethod
    def error(self, message: str, *args: Any, exc_info: bool = False): 
        pass


# 2. Default implementation using Python's logging module
class StdLogger(LoggerInterface):
    def __init__(self, name: str):
        import logging
        self.logger = logging.getLogger(name)

    def debug(self, message: str, *args: Any):
        formatted_msg = message % args if args and "%" in message else message
        cleaned_msg = re_util.clean_invalid_chars(formatted_msg)
        self.logger.debug(cleaned_msg)

    def info(self, message: str, *args: Any):
        formatted_msg = message % args if args and "%" in message else message
        cleaned_msg = re_util.clean_invalid_chars(formatted_msg)
        self.logger.info(cleaned_msg)

    def warning(self, message: str, *args: Any):
        formatted_msg = message % args if args and "%" in message else message
        cleaned_msg = re_util.clean_invalid_chars(formatted_msg)
        self.logger.warning(cleaned_msg)

    def error(self, message: str, *args: Any, exc_info: bool = False):
        formatted_msg = message % args if args and "%" in message else message
        cleaned_msg = re_util.clean_invalid_chars(formatted_msg)
        self.logger.error(cleaned_msg, exc_info=exc_info)


# 3. Log aspect implementation
class LogAspect:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def log_method(self, description: str = ""):
        """Decorator for method logging"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                # Get method/function info - improved version
                if args:
                    # For class methods: get class name from first argument (self/cls)
                    class_name = args[0].__class__.__name__
                else:
                    # For top-level functions: use module name instead of class name
                    module_name = func.__module__
                    class_name = module_name.split('.')[-1]  # Get last part of module name
                    
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
    def get_log_aspect(name: str = None) -> LogAspect:
        if name is None:
            # Obtain the file name of the caller (without extension)
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            if module and hasattr(module, '__file__'):
                # Get the root directory (assuming there is a pytest.ini file in the root directory)
                file_path = os.path.abspath(module.__file__)
                current = file_path
                while True:
                    parent = os.path.dirname(current)
                    if os.path.exists(os.path.join(parent, "pytest.ini")):
                        name = os.path.basename(parent)
                        break
                    if parent == current:
                        name = "unknown"
                        break
                    current = parent
            else:
                name = "unknown"
        logger = LoggerFactory.get_logger(name)
        return LogAspect(logger)
    
#default logger    
log=LoggerFactory.get_log_aspect()