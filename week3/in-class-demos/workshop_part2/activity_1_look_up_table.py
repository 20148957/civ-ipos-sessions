# We sometimes want to use the nested loops to created multidimensional structure
# create a lookup table where each product code is associated
# with a tuple containing the product name and its price.

# Define the function that creates the product lookup table
def create_product_lookup_table(product_codes, product_info):
    # TODO Initialise an empty dictionary to store the lookup table


    # TODO Iterate over the rows of the product codes list

        # TODO Iterate over the elements in each row

            # TODO Use the product code as the key for the dictionary

            # TODO Use the corresponding product info as the value for the dictionary

            # TODO Add the key-value pair to the lookup table



    # Return the completed lookup table
    return look_up_table

# Create two 2D lists for product codes and product info
product_codes = [['P1001', 'P1002'], ['P1003', 'P1004']]
product_info = [[('Apple', 1.20), ('Banana', 0.50)], [('Cherry', 0.75), ('Date', 1.50)]]

# Call the function with the product codes and product info lists
product_lookup_table = create_product_lookup_table(product_codes, product_info)

# Print the resulting product lookup table
print(product_lookup_table)

# Generated result {'P1001': ('Apple', 1.2), 'P1002': ('Banana', 0.5), 'P1003': ('Cherry', 0.75), 'P1004': ('Date',
# 1.5)}

