import logging

def setting_logging(name, fileName, level= logging.DEBUG):
    
    """Creating custom logging configuration and ensuring only one handler is added"""
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    formater = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    
   
    file_handler = logging.FileHandler(fileName)
    file_handler.setFormatter(formater)
    
    
    console_handling = logging.StreamHandler()
    console_handling.setFormatter(formater)
    
    
    if not logger.handlers:
     logger.addHandler(file_handler)
     logger.addHandler(console_handling)
     
    return logger
    