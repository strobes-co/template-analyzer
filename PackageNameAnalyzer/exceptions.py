# Write your custom exceptions here for handling exceptions
# in this project
# example:

class InvalidJsonExtension(Exception):
    def __str__(self):
        return 'Output extension is not json'