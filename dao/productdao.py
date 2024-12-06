from model.models import Product


class ProductDAO:
    def __init__(self):
        """
        Initializes the ProductDAO with a sample collection of products.
        """
        self.products = [
            Product(1, "Royal Oak", "Audemars Piguet", 36000, "Luxury", 'Automatic', 'Steel', 'Steel', 'Double-fold clasp', 'Steel', '41 mm', 'Steel', '5 ATM', 'Steel', 'Sapphire crystal', 'black', '60 h', 'Audemars_Piquet_Royal_Oak.webp', "Original Royal Oak in Steel. This piece highlights the real strength of the Royal Oak, which was originally designed and conceived to highlight the beauty and strength of steel for high-end timepieces.This example comes on the traditional steel band, features a black dial, and the date window at the five o'clock position.", 2),
            Product(2, "Seamaster Diver 300M", "Omega", 4728, "Sport", 'Automatic', 'Steel', 'Steel', 'Fold clasp', 'Steel', '42 mm','Steel', '30 ATM', 'Ceramic', 'Sapphire crystal', 'black', '55 h', 'Omega_SM_D.webp', "The OMEGA Seamaster Professional Diver 300M is a renowned luxury diver's watch, in production since 1993. Designed for 300m underwater use, it features a 42mm stainless steel case and bracelet, a green ceramic bezel with a white enamel diving scale, and a green ceramic dial with laser-engraved waves and a date window. Rhodium-plated hands and indexes are coated with white Super-LumiNova for low-light visibility. Its self-winding OMEGA Master Chronometer Calibre 8800 movement, certified for accuracy and reliability, is visible through the sapphire crystal caseback. It includes a helium escape valve and an adjustable stainless steel bracelet with a diver extension.", 1),
            Product(3, "Speedmaster Date", "Omega", 1495, "Sport", 'Automatic', 'Steel', 'Steel', 'Fold clasp', 'Steel', '39 x 13.5 mm', 'Steel', '5 ATM', 'Steel', 'Sapphire crystal', 'black', '44 h', 'Omega_Speedmaster.jpg', "This Omega Speedmaster Date 3513.50.00 has a black baton dial and a bracelet strap. This Omega has undergone a thorough inspection of accuracy, functionality and condition at our Omega certified service centre to determine the level of reconditioning required to meet our strict standards. It has also been checked against our records to ensure authenticity. All our watches have a 24-month warranty for your peace of mind.", 3 ),
            Product(4, "Datejust 36", "Rolex", 4950, "Luxury", 'Automatic', 'Gold/Steel', 'Gold/Steel', 'Fold clasp', 'Steel','36 mm', 'Gold/Steel', '10 ATM', 'Yellow Gold', 'Plexiglass', 'Gold', '42 h', 'Rolex_Datejust36.webp',"This genuine vintage Rolex is in Excellent condition vintage watch of it's age. Watch has received a full movement service and case/bracelet overhaul by on staff SC&L watchmaking team. This reference is now out of production. Watch comes with all original box, paperwork, and warranty certificate, not commonly included with a vintage watch from this era. Tritium Superluminova dial has patina'd consistently with the age of this watch.",4),
            Product(5, "Daytona", "Rolex", 41150, "Luxury", 'Automatic', 'Rose Gold', 'Gold', 'Fold clasp', 'Rose Gold', '40 mm', 'Rose Gold', '10 ATM', 'Rose Gold', 'Sapphire crystal', 'Rose Gold', '72h','Rolex_Dytona.webp',"This Rolex Daytona 116523 has a steel baton dial and a bracelet strap. This Rolex has undergone a thorough inspection of water resistance, accuracy, functionality and condition to determine the level of reconditioning required to meet our strict standards. It has also been referenced against technical documents and manufacturer records where available to ensure authenticity and a clean history. All our watches have a 24-month warranty for your peace of mind. One of our skilled polishing technicians has removed marks on the case and bracelet of this watch, brought about by daily wear and tear, which is why this watch does not come with the remaining manufacturer’s warranty.", 3),
            Product(6, "Submariner Date", "Rolex", 12000, "Luxury", 'Automatic', 'Yellow Gold', 'Gold', 'Fold clasp','Gold', '40 mm', 'Yellow Gold', '5 ATM', 'Yellow Gold', 'Sapphire crystal', 'Gold', '55 h', 'Rolex_SM_Date.webp',"This Rolex Submariner 16610 has a black dial and a bracelet strap. This Rolex has undergone a thorough inspection of water resistance, accuracy, functionality and condition to determine the level of reconditioning required to meet our strict standards. It has also been referenced against technical documents and manufacturer records where available to ensure authenticity and a clean history. ", 7),
            Product(7, "Perpetual Calendar", "Patek Philippe", 26000, "Luxury", 'Automatic', 'Leather', 'Black', 'Fold clasp', 'White Gold','37 mm', 'White Gold', '5 ATM', 'White gold', 'Sapphire crystal', 'White Gold', '40 h', 'PP_PC.webp',"Ultra-thin self-winding 31-260 PS QL caliber featuring a triple-patented additional module displays the day, date and month through a large single 12 o’clock aperture, complemented by two round apertures for the leap-year cycle and day/night indication and a moon-phase display.", 5),
            Product(8, "Calatrava", "Patek Philippe", 5000, "Luxury", 'Manual winding', 'Leather', 'Black','Fold clasp', 'Gold','33 mm', 'Gold', '5 ATM', 'Gold', 'Sapphire crystal', 'Black', '35 h', "PP_Calatrava.webp","Supremely elegant, the Calatrava charms each new genereation of watch lovers by its timeless understated perfection.", 5
                    )
        ]

    def get_all_products(self):
        """
        Retrieves all products in the catalog.
        """
        return self.products

    def get_product_by_id(self, product_id):
        """
        Retrieves a single product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            Product: The product with the given ID, or None if not found.
        """
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None  # Product not found


# Example usage of ProductDAO
def main_with_dao():
    product_dao = ProductDAO()

    print("All Products:")
    for product in product_dao.get_all_products():
        print(product)

    print("\nFetching Product by ID (ID: 2):")
    product = product_dao.get_product_by_id(2)
    if product:
        print(product)
    else:
        print("Product not found.")


if __name__ == "__main__":
    main_with_dao()
