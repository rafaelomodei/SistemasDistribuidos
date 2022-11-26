class FunctionUtils:
    def __init__(self):
        self = self

    def message_return(self, message='', status=0, error=''):
        if ((message or error) and status):
            return {
                "response": message,
                "status": status,
                "error": error
            }
