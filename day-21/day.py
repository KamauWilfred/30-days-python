import re

reg = input(f"\nEnter registration number: ")

digits = re.findall(r"\d+", reg)
capital = re.findall(r"[A-Z]", reg)
replace = re.sub(r"\d+", "#", reg)

print(f"\nDigits: ",digits)
print("Capital letters: ", capital)
print("Modified reg: ",replace)

if re.fullmatch(r"[A-Z]{2}\d{3}[A-Z]{2}\d{2}", reg):
    print(f"\nValid registration number!")

else:
    print(f"\nInvalid registration number!")
