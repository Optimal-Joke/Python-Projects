letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letters_to_points = {letter: points for letter, points in zip(letters, points)}
player_info = {}

### Game Setup ###

print("""
                                  Welcome to
        ███████╗ ██████╗██████╗  █████╗ ██████╗ ██████╗ ██╗     ███████╗
        ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝
        ███████╗██║     ██████╔╝███████║██████╔╝██████╔╝██║     █████╗  
        ╚════██║██║     ██╔══██╗██╔══██║██╔══██╗██╔══██╗██║     ██╔══╝  
        ███████║╚██████╗██║  ██║██║  ██║██████╔╝██████╔╝███████╗███████╗
        ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝
                   ███████╗ ██████╗ ██████╗ ██████╗ ███████╗
                   ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
                   ███████╗██║     ██║   ██║██████╔╝█████╗  
                   ╚════██║██║     ██║   ██║██╔══██╗██╔══╝  
                   ███████║╚██████╗╚██████╔╝██║  ██║███████╗
                   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
           ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
           ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
              ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
              ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
              ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
              ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                           Created by Hunter Holland
    
    """)
while True:
    num = input("Number of players in game : ")
    try:
        num_players = int(num)
        break
    except ValueError:
        print(
            f"""
            You can't have \"{num}\" players, silly. Please enter a valid number.
            """)

### Initialize Player Entry in Game Dictionary ###
for i in range(1, num_players+1):
    player_name = input(f"Player {i} Name : ")
    player_info[i] = {}
    player_info[i]["name"] = player_name.title()
    player_info[i]["words played"] = []
    player_info[i]["score"] = 0

### Start Prompt ###

while True:
    start_command = input("\nType \"Y\" to begin. ")
    if start_command.upper() == "Y":
        break
    else:
        print("""
            That was not a "Y". Are you testing me, or did you just goof?""")
print("""
                                Have fun!
        """)

### End Game Setup ###
### Game functions ###


def play_word(i, word):
    player_info[i]["words played"].append(word)


def score_word(word, double_letters="", triple_letters="", num_double_word=0, num_triple_word=0):
    point_total = 0
    for letter in word.upper():
        if letters_to_points.get(letter):
            point_total += letters_to_points[letter]
        else:
            point_total += 0
    for letter in double_letters.upper():
        point_total += letters_to_points[letter]
    for letter in triple_letters.upper():
        point_total += 2 * letters_to_points[letter]
    if (num_double_word != 0) & (num_double_word != ""):
        point_total *= 2 ** int(num_double_word)
    if (num_triple_word != 0) & (num_triple_word != ""):
        point_total *= 3 ** int(num_triple_word)
    return point_total


def fetch_word_info(word):
    double_letters = input("Type each Double Letter : ")
    triple_letters = input("Type each Triple Letter : ")
    double_word = input("Number of Double Word Score tiles covered : ")
    triple_word = input("Number of Triple Word Score tiles covered : ")
    return word, double_letters, triple_letters, double_word, triple_word


def update_point_totals(i, word_score):
    player_info[i]["score"] += word_score


### End Game Functions ###
### Game begins ###

in_game = True
turn_number = 0
while in_game:
    turn_number += 1
    for i in range(1, num_players+1):
        player_name = player_info[i]["name"]
        print(f"{player_name}, Turn {turn_number} ———")
        word = input("Word Played (to end game, type \"END GAME\") : ")
        if word.upper() == "END GAME":
            in_game = False
            break
        word, double_letters, triple_letters, double_word, triple_word = fetch_word_info(
            word)
        word_score = score_word(
            word.upper(), double_letters, triple_letters, double_word, triple_word)
        play_word(i, word)
        update_point_totals(i, word_score)
        print(f"WORD SCORE: {word_score} \n")
    

### Game ends ###
### Begin Subtracting Players' Hand Tiles from Their Final Score ###

print("""
                          You have ended the game! 
            Type out your remaining letters in the fields that follow. 
            As per official Scrabble rules, their point values will be 
                      deducted from your final score.
    """)

for i in range(1, num_players+1):
    player_name = player_info[i]["name"]
    letters_in_hand = input(f"{player_name}, Leftover Letters : ")
    score_deduction = score_word(letters_in_hand)
    player_info[i]["score"] -= score_deduction


### Print Final Scores ###


print("\nFINAL SCORES:")
for i in range(1, num_players+1):
    player_name = player_info[i]["name"]
    player_score = player_info[i]["score"]
    print(f"{player_name} : {player_score}")


### Subtract Hand From Score ###


request_words = input(
    "\nWould you like to see the words each player played? (Y/N)  ")

print("")
if request_words.upper() == "Y":
    for i in range(1, num_players+1):
        name = player_info[i]["name"]
        words = player_info[i]["words played"]
        print(f"{name}: {words}")

print("\nThank you for using Hunter Holland's Scrabble Score Tracker! Have a great day.\n")
