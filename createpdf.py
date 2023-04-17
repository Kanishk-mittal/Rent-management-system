from fpdf import FPDF
from tkinter import *
import fitz  # PyMuPDF library

# Define the PDF object
def generate_invoice(tenant_name,date,rent,internet_charges,last_unit,current_unit,last_balance=0):
    global root
    pdf = FPDF()

    # Add a page to the PDF
    pdf.add_page()

    # Set the font for the PDF
    pdf.set_font("Arial", size=12)

    # Add the invoice header
    pdf.cell(200, 10, txt="Invoice", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Tenant Name: {tenant_name}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Invoice Date: {date}", ln=1, align="L")

    # Add the table header
    pdf.cell(140, 10, txt="Item", border=1, ln=0, align="C")
    pdf.cell(40, 10, txt="Price", border=1, ln=1, align="C")

    pdf.cell(140, 10, txt="Rent", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(rent), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Internet Charges", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(internet_charges), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Last unit", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(last_unit), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Current unit", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(current_unit), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Electricity Units difference", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(float(current_unit)-float(last_unit)), border=1, ln=1, align="R")

    pdf.cell(140,10,txt="Per unit charge",border=1,ln=0,align="L")
    pdf.cell(40, 10, txt="7.5", border=1, ln=1, align="R")

    pdf.cell(140, 10, "total electricity charge", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str((float(current_unit)-float(last_unit))*7.5), border=1, ln=1, align="R")

    pdf.cell(140, 10, "Last Balance", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(last_balance), border=1, ln=1, align="R")

    # Add the total row
    total =last_balance+ rent + internet_charges + (float(current_unit)-float(last_unit))*7.5

    pdf.cell(100, 10, txt="", border=0, ln=0)
    pdf.cell(40, 10, txt="Total", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(total), border=1, ln=0, align="R")
    pdf.output(f"D:\\rent_invoice\\invoice_{tenant_name}_{date}.pdf")

    root = Tk()

    # Open the PDF file using PyMuPDF
    doc = fitz.open(f"D:\\rent_invoice\\invoice_{tenant_name}_{date}.pdf")

    # Get the number of pages in the PDF
    num_pages = doc.page_count

    # Create a canvas to display the PDF
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()

    # Loop through each page in the PDF and render it on the canvas
    for page_num in range(num_pages):
        # Get the page object for the current page
        page = doc[page_num]

        # Get the dimensions of the page
        page_width = page.rect.width
        page_height = page.rect.height

        # Create an image of the current page
        pix = page.get_pixmap(alpha=False)

        # Convert the image to a format that can be displayed in Tkinter
        img = PhotoImage(data=pix.tobytes())

        # Add the image to the canvas
        canvas.create_image(0, 0, anchor='nw', image=img)

    # Start the Tkinter mainloop to display the PDF
    root.mainloop()

def new_tenant_recipt(tenant_name,date,rent,internet_charges,police_verification,Rent_agreement,balance=0):
    global root
    pdf = FPDF()

    # Add a page to the PDF
    pdf.add_page()

    # Set the font for the PDF
    pdf.set_font("Arial", size=12)

    # Add the invoice header
    pdf.cell(200, 10, txt="Invoice", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Tenant Name: {tenant_name}", ln=1, align="L")
    pdf.cell(200, 10, txt=f"Invoice Date: {date}", ln=1, align="L")

    # Add the table header
    pdf.cell(140, 10, txt="Item", border=1, ln=0, align="C")
    pdf.cell(40, 10, txt="Price", border=1, ln=1, align="C")

    # Add the table rows
    #rent = 1000
    #internet_charges = 50
    #electricity_units_consumed = 100
    #charge_per_unit_electricity = 10
    #total_electricity_charge = electricity_units_consumed * charge_per_unit_electricity

    pdf.cell(140, 10, txt="Rent", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(rent), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Internet Charges", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(internet_charges), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Security deposit", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(rent), border=1, ln=1, align="R")

    pdf.cell(140, 10, txt="Police verification", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(police_verification), border=1, ln=1, align="R")

    pdf.cell(140, 10, "Rent agreement charges", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(Rent_agreement), border=1, ln=1, align="R")

    pdf.cell(140, 10, "Balance", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(balance), border=1, ln=1, align="R")

    # Add the total row
    total =rent*2+internet_charges+police_verification+Rent_agreement+balance

    pdf.cell(100, 10, txt="", border=0, ln=0)
    pdf.cell(40, 10, txt="Total", border=1, ln=0, align="L")
    pdf.cell(40, 10, txt=str(total), border=1, ln=0, align="R")
    pdf.output(f"D:\\rent_invoice\\invoice_{tenant_name}_{date}.pdf")

    root = Tk()

    # Open the PDF file using PyMuPDF
    doc = fitz.open(f"D:\\rent_invoice\\invoice_{tenant_name}_{date}.pdf")

    # Get the number of pages in the PDF
    num_pages = doc.page_count

    # Create a canvas to display the PDF
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()

    # Loop through each page in the PDF and render it on the canvas
    for page_num in range(num_pages):
        # Get the page object for the current page
        page = doc[page_num]

        # Get the dimensions of the page
        page_width = page.rect.width
        page_height = page.rect.height

        # Create an image of the current page
        pix = page.get_pixmap(alpha=False)

        # Convert the image to a format that can be displayed in Tkinter
        img = PhotoImage(data=pix.tobytes())

        # Add the image to the canvas
        canvas.create_image(0, 0, anchor='nw', image=img)

    # Start the Tkinter mainloop to display the PDF
    root.mainloop()
