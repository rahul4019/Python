from random import choice

capital = "Topeka"

bird = 'Western Meadowlark'

flower = 'Sunflower'

song = 'Home on the range'

def randomFunfact():
    funFacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")

    print(funFacts[int(index)])

# only runs if the this is the main file
if __name__ == "__main__":
    randomFunfact()
