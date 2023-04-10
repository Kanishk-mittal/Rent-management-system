from reportlab.pdfgen import canvas

# Create a new PDF document
pdf = canvas.Canvas('receipt.pdf')

# Set the font for the document
pdf.setFont('Helvetica', 12)

# Set the receipt data
tenant_name = 'John Doe'
rent_amount = 1000.00
receipt_number = 12345

# Set the coordinates for the receipt data
x = 50
y = 750

# Add the tenant name to the receipt
pdf.drawString(x, y, 'Tenant Name: {}'.format(tenant_name))

# Add the rent amount to the receipt
y -= 20
pdf.drawString(x, y, 'Rent Amount: ${}'.format(rent_amount))

# Add the receipt number to the receipt
y -= 20
pdf.drawString(x, y, 'Receipt Number: {}'.format(receipt_number))

# Save the PDF document
pdf.save()
