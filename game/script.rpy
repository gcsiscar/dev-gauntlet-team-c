define s = Character('SYLVIE', color="#eaaad3")
define m = Character('Me', color="#c8c8ff")

default book = False

screen back_button():
    imagebutton:
        align (0.0, 0.0)
        idle "gui/button/back_idle.png" action MainMenu()

label start:

    scene default_background
    show screen back_button
    with fade

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile:
        xalign 0.8

    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    menu:
        s "Sure, but what's a \"visual novel?\""
        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book


label game:

    m "It's a kind of videogame you can play on your computer or a console."

    jump marry

label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    jump marry

label marry:

    "And so, we become a visual novel creating duo."

    jump ending

