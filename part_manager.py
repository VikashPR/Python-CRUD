from tkinter import *

# Create a window Object
app = Tk()

# Part
part_text = StringVar()
part_lable = Label(app, text="Part Name", font=('Poppins', 14), pady=30)
part_lable.grid(row=0, column=0, padx=4, pady=4)
part_entry = Entry(app, textvariable=part_text, font=('Poppins', 14))
part_entry.grid(row=0, column=1)

# Customer
customer_text = StringVar()
customer_lable = Label(app, text="Customer", font=('Poppins', 14))
customer_lable.grid(row=0, column=2, padx=4, pady=4)
customer_entry = Entry(app, textvariable=customer_text, font=('Poppins', 14))
customer_entry.grid(row=0, column=3)

# Retailer
retailer_text = StringVar()
retailer_lable = Label(app, text="retailer Name", font=('Poppins', 14))
retailer_lable.grid(row=1, column=0, padx=4, pady=4)
retailer_entry = Entry(app, textvariable=retailer_text, font=('Poppins', 14))
retailer_entry.grid(row=1, column=1)

# Price
price_text = StringVar()
price_lable = Label(app, text="price", font=('Poppins', 14))
price_lable.grid(row=1, column=2, padx=4, pady=4)
price_entry = Entry(app, textvariable=price_text, font=('Poppins', 14))
price_entry.grid(row=1, column=3)


# App title
app.title("Part Manager")
# App Dimensions
app.geometry('700x350')

# Running the app
app.mainloop()
