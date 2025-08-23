import requests
from config import HTTP_TIMEOUT
import logging

logger = logging.getLogger(__name__)

def generate_header(token):
    """
    Generate the Authorization header for the request.
    
    :param token: The token to be included in the header.
    :return: A dictionary containing the Authorization header.
    """
    return {
        "Authorization": f"Bearer {token}"
    }

def get(url, params=None, headers=None, timeout=HTTP_TIMEOUT):
    """
    Make a GET request to the specified URL with optional parameters and headers.
    
    :param url: The URL to send the GET request to.
    :param params: Optional dictionary of query parameters to include in the request.
    :param headers: Optional dictionary of headers to include in the request.
    :return: The response object from the GET request.
    """
    
    logger.debug("Making GET request to %s with params: %s and headers: %s", url, params, headers)
    response = requests.get(url, params=params, headers=headers,timeout=timeout)
    
    logger.debug("Response status code: %s, headers: %s, content: %s", response.status_code, response.headers, response.content)
    
    return response

def post(url, data=None, headers=None, timeout=HTTP_TIMEOUT):
    """
    Make a POST request to the specified URL with optional data and headers.
    
    :param url: The URL to send the POST request to.
    :param data: Optional dictionary of data to include in the request body.
    :param headers: Optional dictionary of headers to include in the request.
    :return: The response object from the POST request.
    """
    
    logger.debug("Making POST request to %s with data: %s and headers: %s", url, data, headers)
    
    response = requests.post(url, json=data, headers=headers, timeout=timeout)
    
    logger.debug("Response status code: %s, headers: %s, content: %s", response.status_code, response.headers, response.content)
    
    return response 

def put(url, data=None, headers=None, timeout=HTTP_TIMEOUT):
    """
    Make a PUT request to the specified URL with optional data and headers.
    
    :param url: The URL to send the PUT request to.
    :param data: Optional dictionary of data to include in the request body.
    :param headers: Optional dictionary of headers to include in the request.
    :return: The response object from the PUT request.
    """
    
    logger.debug("Making PUT request to %s with data: %s and headers: %s", url, data, headers)
    
    response = requests.put(url, json=data, headers=headers, timeout=timeout)
    
    logger.debug("Response status code: %s, headers: %s, content: %s", response.status_code, response.headers, response.content)
    
    return response 

def delete(url, headers=None, timeout=HTTP_TIMEOUT):
    """
    Make a DELETE request to the specified URL with optional headers.
    
    :param url: The URL to send the DELETE request to.
    :param headers: Optional dictionary of headers to include in the request.
    :return: The response object from the DELETE request.
    """
    
    logger.debug("Making DELETE request to %s with headers: %s", url, headers)
    
    response = requests.delete(url, headers=headers, timeout=timeout)
    
    logger.debug("Response status code: %s, headers: %s, content: %s", response.status_code, response.headers, response.content)
    
    return response 