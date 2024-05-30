from barcode import Code128
from barcode.writer import ImageWriter
import os

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        try:
            # Define a valid path to save the barcode image
            file_name = f"barcode_{product_code}.png"
            file_path = os.path.join(os.getcwd(), file_name)
            
            # Create barcode object
            tag = Code128(product_code, writer=ImageWriter())
            
            # Save the barcode image
            tag.save(file_path)
            
            return file_path
        except Exception as e:
            print(f"Error creating barcode: {e}")
            raise e

# Test the BarcodeHandler independently
if __name__ == "__main__":
    handler = BarcodeHandler()
    product_code = "123456789012"
    result = handler.create_barcode(product_code)
    print(f"Barcode saved at: {result}")
