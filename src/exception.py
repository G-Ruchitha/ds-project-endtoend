'''
This code defines a custom exception class in Python 
along with a function to generate detailed error messages. 
'''

import sys

'''
Imports the sys module which provides access to system-specific 
parameters and functions, including sys.exc_info() 
used for obtaining information about the exception.
'''
def error_message_detail(error,error_detail:sys):

    '''
    Defines a function error_message_detail that takes two parameters: error 
    (the exception object) and error_detail (which is expected to be of type sys).
    '''
    _,_,exc_tb = error_detail.exc_info()

    '''
    Retrieves the exception details using exc_info() from the sys 
    module. exc_info() returns a tuple containing the exception type, value, and traceback object. 
    Here, only the traceback object (exc_tb) is captured, 
    and the other values are ignored (using _).
    '''
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    '''
    Extracts the filename of the script where the exception occurred from the traceback object. 
    tb_frame provides the current stack frame, 
    and f_code.co_filename gives the name of the file.
    '''

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    '''
    file_name: the name of the file where the error occurred.
    exc_tb.tb_lineno: the line number where the exception was raised.
    str(error): the string representation of the exception message.
    '''
    return error_message

'''
Custom Exception Class
'''
class CustomException(Exception):
    '''
    Defines a custom exception class named CustomException that 
    inherits from the built-in Exception class.
    '''
    def __init__(self,error_message,error_detail:sys):
        '''
        Initializes the custom exception. The constructor takes error_message 
        (the message for the exception) and error_detail (providing traceback information).
        '''
        super().__init__(error_message)
        '''
        Calls the constructor of the base Exception class with error_message
        to correctly call the parent class's initializer.
        '''
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        '''
        Sets the error_message attribute of the CustomException instance using the 
        error_message_detail function. It formats the error message with details 
        provided by the traceback object.
        '''
      
    def __str__(self):
        '''
        Defines the __str__ method. This method is called when the CustomException 
        instance is converted to a string (e.g., when printing the exception).
        '''
        return self.error_message

