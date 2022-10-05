class BaseErrorClass:
    pass

class PackageError(BaseException, BaseErrorClass):
    """Package name omitted."""
    def __init__(self, *args: object):
        if args:
            print(args[0])
