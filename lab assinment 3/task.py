# Electricity Bill Calculation Program
customer_type = input("Type of Customer   : ")
PU = int(input("Previous Units (PU): "))
CU = int(input("Current Units (CU) : "))

# Calculate Units Consumed
units = CU - PU

# Charges (for Domestic type)
if customer_type.lower() == "domestic":
    rate = 2.47             # per unit energy charge
    EC = units * rate
    FC = 50.00
    CC = 70.00
    # Adjusted duty to match real bill (6.3%)
    ED = (EC + FC + CC) * 0.06303
else:
    rate = 4.00
    EC = units * rate
    FC = 100.00
    CC = 100.00
    ED = (EC + FC + CC) * 0.05

# Total Bill
bill_amount = EC + FC + CC + ED
bill_amount = round(bill_amount, 2)

# Output
print("\n---------------------------------------")
print("     TGNPDCL Electricity Bill")
print("---------------------------------------")
print(f"Type of Customer   : {customer_type}")
print(f"Previous Units (PU): {PU}")
print(f"Current Units (CU) : {CU}")
print(f"Units Consumed     : {units}")
print("---------------------------------------")
print(f"Energy Charges (EC): ₹{EC:.2f}")
print(f"Fixed Charges (FC) : ₹{FC:.2f}")
print(f"Customer Charges(CC): ₹{CC:.2f}")
print(f"Electricity Duty(ED): ₹{ED:.2f}")
print("---------------------------------------")
print(f"Total Bill Amount  : ₹{bill_amount:.2f}")
print("---------------------------------------")
