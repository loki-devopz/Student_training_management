class InvalidMarksError(Exception):
    """Raised when student marks are invalid."""
    pass


class StudentNotFoundError(Exception):
    """Raised when a student does not exist."""
    pass