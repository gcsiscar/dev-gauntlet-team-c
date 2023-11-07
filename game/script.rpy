# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

# THIS_PATH is defined in chess_displayable.rpy
# define THIS_PATH = '00-chess-engine/'
init python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')

# The game starts here.

# label start:
#     scene bg room
#     e "Welcome to the Ren'Py Chess Game!"


define e = Character("Eileen")

# define the song titles and their files
init python:
    # must be persistent to be able to record the scores
    # after adding new songs, please remember to delete the persistent data

    rhythm_game_songs = [
    Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt'),
    Song('Positivity', 'audio/Positivity.mp3', 'audio/Positivity.beatmap.txt'),
    Song('Pearlescent', 'audio/Pearlescent.mp3', 'audio/Pearlescent.beatmap.txt'),
    Song('Pearlescent - trimmed', 'audio/Pearlescent - trimmed.mp3', 'audio/Pearlescent - trimmed.beatmap.txt'), # 22 sec, easy to test 
    Song('Thoughts', 'audio/Thoughts.mp3', 'audio/Thoughts.beatmap.txt')
    ]

    # # init
    # if persistent.rhythm_game_high_scores:
    #     for song in songs:
    #         if not song in persistent.rhythm_game_high_scores:
    #             persistent.rhythm_game_high_scores[song] = (0, 0)

# map song name to high scores
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}

# the song that the player chooses to play, set in `choose_song_screen` below
default selected_song = None
define s = Character('SYLVIE', color="#eaaad3")
define m = Character('Me', color="#c8c8ff")

default persistent.rosalyn_unlocked = False

screen next_button():
    imagebutton:
        align (0.96, 0.76)
        idle "gui/button/next_button_idle.png" action renpy.curry(renpy.end_interaction)(True)

screen settings():
    imagebutton:
        align (1.0, 1.0)
        idle "gui/button/settings_idle.png" action ShowMenu()

screen back_button():
    imagebutton:
        align (0.0, 0.0)
        idle "gui/button/back_idle.png" action MainMenu()

label start:
    scene default_background
    show screen back_button
    show screen settings
    show screen next_button
    with fade

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show heroine_happy:
        xalign 0.8

    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    hide screen next_button
    menu:
        s "Sure, but what's a \"visual novel?\""
        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book


label game:
    show screen next_button
    $ persistent.rosalyn_unlocked = True
    hide screen next_button
    window hide
    call rhythm_game_entry_label
    m "It's a kind of videogame you can play on your computer or a console."
    jump marry

label book:
    show screen next_button
    $ persistent.rosalyn_unlocked = True
    m "It's like an interactive book that you can read on a computer or a console."
    jump chess_game
    # jump marry

label marry:
    show screen next_button
    "And so, we become a visual novel creating duo."
    jump ending


label chess_game:
    # board notation
    $ fen = STARTING_FEN
    $ STOCKFISH_ENGINE = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)

    menu:
        "Please select the game mode."

        "Player vs. Player":
            $ player_color = None # None for Player vs. Player
            $ depth = None

        "Player vs. Computer":
            # initialize other variables used by the stockfish engine in stockfish.go()
            menu:
                "Please select a difficulty level"

                "Easy":
                    $ depth = 2

                "Medium":
                    $ depth = 6

                "Hard":
                    $ depth = 12

            menu:
                "Please select Player color"

                "White":
                    $ player_color = chess.WHITE # this constant is defined in chess_displayable.rpy 

                "Black":
                    # board view flipped so that the player's color is at the bottom of the screen
                    $ player_color = chess.BLACK

    window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    # disable Esc key menu to prevent the player from saving the game
    $ _game_menu_screen = None

    call screen chess(fen, player_color, depth)

    # re-enable the Esc key menu
    $ _game_menu_screen = 'save'

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    # kill stockfish engine
    $ quit_stockfish()

    $ quick_menu = True
    window show

    if _return == DRAW:
        e "The game ended in a draw."
    else: # RESIGN or CHECKMATE
        $ winner = "White" if _return == chess.WHITE else "Black"
        e "The winner is [winner]."
        if player_color is not None: # PvC
            if _return == player_color:
                e "Congratulations, player!"
            else:
                e "Better luck next time, player."

    menu:
        "Would you like to play another game?"

        "Yes":
            jump chess_game

        "No":
            pass

    return