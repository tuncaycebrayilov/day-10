import sys

f = open("main.txt", "a")

try:
    if sys.argv[1] == 'add':
        name = input("Enter series name: ")
        director = input("Enter director name: ")
        seasons = input("Enter Number of seasons: ")
        episodes = input("Enter Number of episodes: ")
        genre = input("Enter Genre: ")

        f.write(f'Series Name: {name}')
        f.write('\n')
        f.write(f'Director: {director}')
        f.write('\n')
        f.write(f'Seasons: {seasons}')
        f.write('\n')
        f.write(f'Episodes: {episodes}')
        f.write('\n')
        f.write(f'Genre: {genre}')
        f.write('\n')
        f.write('\n')


        print("Added Succesfully")

except:
    print("Wrong input")



a = open('main.txt', 'r')
if sys.argv[1] == "All" and sys.argv[2] == "series":
    print(a.read())