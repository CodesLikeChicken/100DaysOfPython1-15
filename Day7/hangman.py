import random

def print_hangman():
    global goal_word
    global guessed_letters

    hint_display = ""

    for letter in goal_word:
        if(letter in guessed_letters):
            hint_display += letter
        else:
            hint_display += "_"
    
    print (hint_display)

def solved():
    global goal_word
    global guessed_letters

    for letter in goal_word:
        if not letter in guessed_letters:
            return False

    return True

random_words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]
random_word_index = random.randint(0, len(random_words) - 1)
goal_word = random_words[random_word_index]
guessed_letters = []

guesses = 10
while (guesses > 0):
    print_hangman()
    guessed_letter = input(f"Guess a letter ({guesses} remaining): ").lower()

    if len(guessed_letter) > 1:
        print("Woah now, only one letter at a time!")
        continue

    guessed_letters.append(guessed_letter)

    if solved():
        break

    guesses -= 1

print (f'The word was "{goal_word}"')

if (guesses > 0):
    print("You are a winner!")
else:
    print("You lose!")


