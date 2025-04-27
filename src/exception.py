import sys
import logging

def error_message(error,error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    filename = exe_tb.tb_frame.f_code.co_filename
    message = "Error in python script [{0}] line number [{1}] error message [{2}]".format(
    filename, exe_tb.tb_lineno, str(error))
    return message
    

class CustomException(Exception):
    def __init__(self,message,error_detail:sys):
        super().__init__(message)
        self.message = error_message(message,error_detail = error_detail)

    def __str__(self):
        return self.message
    