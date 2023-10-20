from random import choice


def get_random_word(words: list):
    return choice(words)


names = ["Maria", "Nikolay", "Stefan", "Yordan"]
places = ["Sofia", "Varna", "Bourgas", "Sozopol"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
noons = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "in the car"]

while True:
    print("This is your random sentence")
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noon = get_random_word(noons)
    random_adverb = get_random_word(adverbs)
    random_details = get_random_word(details)
    print("\033[1;37;40m", end="")
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noon} {random_details}")
    print("\033[1;33;40m", end="")
    command = input("Click [Enter] to generate a new one or type [exit] and click [Enter] for exit")
    if command == "exit":
        break
