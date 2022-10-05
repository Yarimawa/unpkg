class BaseErrorClass:
    pass

class PackageError(BaseException, BaseErrorClass):
    """Package name omitted."""