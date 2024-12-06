from dao.productdao import ProductDAO
class ProductService:
    def __init__(self):
        """
        Service class for handling product-related operations.
        """
        self.product_dao = ProductDAO()

    def get_all_products(self):
        """
        Retrieves a list of all products from the DAO.
        Returns: List[Product]: A list of all products available in the DAO.
        """
        return self.product_dao.get_all_products()

    def get_product_details(self, product_id):
        """
        Retrieves detailed information of a specific product by its ID.
        Args: product_id (int): The unique identifier of the product.
        Returns: Product: The product details for the specified product ID.

        """
        return self.product_dao.get_product_by_id(product_id)
