# Creating a anime recommendation
print("Welcome to anime recommendators")
print("Choose a genre you wamt")
print("1. Action")
print("2. Romance")
print("3. Comedy")
genre_choice = input("Enter genre choice (1/2/3): ")

if genre_choice == "1":
    genre = "Action"
    print("\nYou selected: ",genre)
    print("Pick era you want: 2000s/2010s")
    
    era_chose1 = input("Choose one (1/2): ")
    if era_chose1 == "1":
        print("Here are the recommendations")
        print(":NARUTO")
        print(":BLEACH")
        print(":Fullmetal Alchemist")
        print(":Black Butler")
    if era_chose1 == "2":
        print("Here are the recommendations")
        print(":Demon Slayer")
        print(":My Hero Academia")
        print(":Over Lord")
        print(":Fate Stay Night")
        
if genre_choice == "2":
    genre = "Romance"
    print("\nYou selected: ",genre)
    print("Pick era you want: 2000s/2010s")
        
    era_chose2 = input("Choose one (1/2): ")
    if era_chose2 == "1":
        print("Here are the recommendations")
        print(":From me to you")
        print(":Nana")
        print(":Spice and Wolf")
        print(":Lovely Comflex")
        
    if era_chose2 == "2":
        print("Here are the recommendations")
        print(":Your Lie in April")
        print(":After the rain")
        print(":Fruit Basket")
        print(":Violet Overgarden")     
        
if genre_choice == "3":
    genre = "Comedy"
    print("\nYou selected: ",genre)
    print("Pick era you want: 2000s/2010s")  
    
    era_chose3 = input("Choose one (1/2): ")
    if era_chose3 == "1":
        print("Here are the recommendations")
        print(":Gintama")
        print(":FLCL")
        print(":Toradora")
        print(":To-Loveru")
        
    if era_chose3 == "2":
        print("Here are the recommendations")
        print(":Oreimo")
        print(":Beka and Test")
        print(":Bakuman")

        print(":The Tatami Galaxy")
