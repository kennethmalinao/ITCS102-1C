print("WELCOME TO THE FREE ANIME ADD LIST")


anime_list = []

while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")
    if anime == "exit":
        break
    anime_list.append(anime)
    print(anime, "has been added to your anime list.")

print("\nYou have exited the anime program.")
print("Your anime list includes:")
for a in anime_list:
    print("-", a)