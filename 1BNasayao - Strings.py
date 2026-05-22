#This project is a hazard word scanner that checks Safety Data Sheet (SDS) warnings for dangerous keywords.
#As a first year ChE Student, reading and understanding chemical safety protocols is a crucial part of laboratory work.

inyou = input('Hello! Please state your name: ')
inSDS = input('Enter the SDS warning phrase to scan: ')
#input variables
#inyou is a variable that defines the user's name
#inSDS is a variable that holds the safety warning text typed by the user

print("Hello", inyou, "! Scanning the SDS text...")

#string manipulation functions and calculations
inSDS_upper = inSDS.upper()
#The .upper() method from Chapter 6 converts the text into all uppercase letters so the scanner is case-insensitive.

#The output will show if the inputted SDS warning phrase contains specific hazardous keywords.
print("\n--- Scanning Report for", inyou, "---")
print("Original Text:", inSDS)

#The 'in' operator checks if a specific word is hidden anywhere inside the user's text.
if "FLAMMABLE" in inSDS_upper:
    print("ALERT: FLAMMABLE chemical detected. Keep away from open flames and heat sources.")

if "TOXIC" in inSDS_upper:
    print("ALERT: TOXIC chemical detected. Ensure proper ventilation and wear appropriate PPE.")

if "FLAMMABLE" not in inSDS_upper and "TOXIC" not in inSDS_upper:
    print("Notice: No 'flammable' or 'toxic' keywords detected in this phrase.")