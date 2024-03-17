### Electronic Store Management System

#### Overview:
This project comprises several Python files that together form an Electronic Store Management System. The system allows customers to purchase items from the store, updates the store's inventory, and generates invoices for customers' purchases.

#### Files:
1. **BILL GENERATION PROGRAM.py**: 
    - This is the main script that runs the Electronic Store Management System.
    - It orchestrates the shopping process by importing modules and executing functions for purchasing items and generating invoices.

2. **read.py**:
    - Contains a function `read_file()` to read information about available products from a file named "products.txt". It parses the data and prints the available products to the console.
    
3. **purchase.py**:
    - Defines a function `purchase()` that facilitates the purchasing process for customers.
    - It interacts with customers, validates their input, calculates the total cost of purchases, applies discounts if applicable, and generates invoices.

4. **write.py**:
    - Contains a function `over_write()` to update the inventory after customer purchases.
    - It updates the quantity of products in the stock file and prints the remaining stock products.

5. **products.txt**:
    - Contains information about available products in the store, including product name, price, and quantity.

#### Functionality:
- **Customer Interaction**: Customers are prompted to enter their name and select products for purchase.
- **Inventory Management**: The system maintains an inventory of available products and updates it after each customer purchase.
- **Purchase Processing**: It calculates the total cost of purchases, applies discounts based on the total amount, and generates invoices for customers.
- **Invoice Generation**: Invoices are generated for each customer's purchase, containing details of the purchased items, discounts applied, and total payable amount.

#### Usage:
1. Users run `BILL GENERATION PROGRAM.py` to initiate the Electronic Store Management System.
2. Upon execution, the system reads available products from the "products.txt" file and prompts customers to make purchases.
3. After each purchase, the inventory is updated, and an invoice is generated for the customer's purchase.
4. Invoices are generated in text file format, providing customers with a record of their purchases.

#### Conclusion:
This Electronic Store Management System provides a convenient way for customers to shop for items, manage inventory, and generate invoices. It offers a streamlined shopping experience and efficient inventory management for store owners.
