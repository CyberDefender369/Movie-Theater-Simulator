#dictionary for movies
movies =  {"The Marvels": [13, 3],
           "The Exorcist: Believer": [17, 3],
           "PAW Patrol: The Mighty Movie": [5, 3],
           "Five Nights at Freddy's": [13, 3],
           "Freelance": [17, 3],
           "A Million Miles Away": [5, 3]
           }

#getting customers movie choice, checking age, and seeing if there are enough seats
while True:
    choice = input("What movie would you like to watch?: ").strip().title()
    
    if choice in movies:
        age = int(input("How old are you?: ").strip())
        
        if age >= movies[choice][0]:
            
            if movies[choice][1] > 0:
                print("Enjoy your movie!")
                movies[choice][1] -= 1
            else:
                print("Sorry, there are no more seats.")
                
        else:
            print("Sorry, you are not old enough.")
            
    else:
        print("Sorry, we are currently not showing that movie.")