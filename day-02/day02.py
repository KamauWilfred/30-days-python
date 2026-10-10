print("========USER PROFILE========")
name = input("name")
Birth_year = input("Birth_year")
Age = int(input("Age"))
if(Age>=18):
    print("Youre an adult")
else:
    print("Youre a minor")
Fav_lang = (input("Fav_lang"))
Username = name.replace(" ", "") + Birth_year.strip()
if(len(Username)<8):
    print("Username is too short")
else:
    print("Username", Username)
print("Username lengh:", len(Username))
print("==============================")

