# Receipt Generator Code
from pyscript import display, document


def generate_receipt(e): 
    product1 = document.getElementById("item1")
    product2 = document.getElementById("item2")
    product3 = document.getElementById("item3")
    product4 = document.getElementById("item4")
    product5 = document.getElementById("item5")

    sub_total = 0

    # Add the price of each selected product to the subtotal
    if product1.checked:
        sub_total = sub_total + 100

    if product2.checked:
        sub_total = sub_total + 80

    if product3.checked:
        sub_total = sub_total + 120

    if product4.checked:
        sub_total = sub_total + 50

    if product5.checked:
        sub_total = sub_total + 20

    # Calculates the VAT by multiplying the sub total by 0.12 (12%)
    vat = sub_total * 0.12

    # Calculates the total amount
    total_amount = sub_total + vat

    # Displays the receipt
    document.getElementById("receipt").innerHTML = f"""
        <p>Subtotal: ₱{sub_total:.2f}</p>
        <p>VAT: ₱{vat:.2f}</p>
        <p>Total Amount: ₱{total_amount:.2f}</p>
    """