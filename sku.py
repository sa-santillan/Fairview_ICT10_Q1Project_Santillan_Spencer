# SKU Generator
from pyscript import document, display


# Gets user input
def generate_sku(e):

    # Clears the div content 
    document.getElementById('results').innerHTML = " "

    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("stock").value

    # Creates the SKU by using the first 3 letters of the category and first 4 letts of the product
    sku = category[:3].upper() + "-" + product[:4].upper() + "-" + str(stock)

    # Displays the SKU
    display("SKU: ", sku, target="results")