
class ProductAlreadyExistsError(Exception):
    """Raised when a product with the same product_id already exists in the inventory."""
    pass

class InsufficientStockError(Exception):
    """Raised when attempting to sell more of a product than the available stock."""
    pass

class InvalidProductDataError(Exception):
    """Raised when there is invalid data while loading product data."""
    pass
