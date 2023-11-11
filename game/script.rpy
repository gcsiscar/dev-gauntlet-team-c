init python:
    # for importing libraries
    import_dir = os.path.join(renpy.config.gamedir, THIS_PATH, 'python-packages')

define text_light = "#7FA8D5"

image ctc_blink:
    "gui/button/next_button_idle.png"
    xalign 1.0 
    yalign 1.0
    yoffset -30
    xoffset -80
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

style char_name:
    color "#ffffff"
    font "fonts/BoldFont.ttf"
    size 50
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

style clara_char_name is char_name:
    color "#eaaad3"

style dr_char_name is char_name:
    color text_light
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]


define j = Character("James", who_style="char_name", ctc="ctc_blink", ctc_position="fixed")
define jv = Character("James (Inside Voice)", who_style="char_name",ctc="ctc_blink", ctc_position="fixed")
define c = Character("Clara", who_style="clara_char_name", ctc="ctc_blink", ctc_position="fixed")
define uf = Character("Unknown Figure", ctc="ctc_blink", ctc_position="fixed")
define dr = Character("Doctor", who_style="dr_char_name", ctc="ctc_blink", ctc_position="fixed")

screen splash():
    add Solid("#fff")
    vbox:
        align (0.5, 0.4)
        add "splash_logo":
            size (600, 600)
        text "Team C" size 72 font "fonts/BoldFont.ttf" color "#000" xalign 0.5

label splashscreen:
    scene black
    with Pause(1)

    show screen splash with dissolve
    with Pause(2)

    hide screen splash with dissolve
    with Pause(1)

    return 

label start:
    play music "beach.ogg" fadeout 1.0 fadein 1.0 
    show screen intro with dissolve
    pause 3
    
    scene bg_beach_night_1
    hide screen intro with dissolve
    show screen settings_button(xalign=1.0, yalign=0.0)

    jv "A gentle breeze causes the palm fronds overhead to rustle, sounding like nature's own bamboo wind chimes. This is a popular retreat for couples in the summer."

    jv "The tropical trees provide a lush green canopy, far out of sight of teachers and fellow students. But now, in the late dry season, it feels like I'm standing under a pile of kindling."
    
    jv "I breathe into my cupped hands and rub them together furiously to prevent them from numbing in this evening chill."

    j "Just how long am I expected to wait out here, anyway? I'm sure the note said 7:00 PM."

    jv "Ah yes... the note... slipped in my bag while I wasn't looking. As far as clichés go, I'm more a fan of the late text message, but at least this way shows a bit of initiative."

    jv "As I ponder the meaning of the note, the dusk gradually deepens. The fireflies silently lighting up the darkening sky are the only sign of time passing in this stagnant world."
    
    jv "Their slow dance upon the quiet beach makes it seem like time has slowed to a crawl. As I gaze into the night sky, the rustling of dry sand nearby startles me, interrupting the quiet mood. Someone is approaching me from behind."

    play sound "footsteps_in_water.ogg" volume 0.5

    jv "???"

    stop sound 

    uf "Hi... James? You came?"

    jv "She asks something so quietly, I can barely hear it. It's dark, but I can see her outline. That soft voice? I'd know it anywhere."
    
    jv "I feel my heart skip a beat. It's her—the one I've always listened to from afar. My heart beats faster as I turn to see her…"

    scene bg_beach_night_2

    j "Clara? I got a note telling me to wait here... it was yours?"

    jv "Dammit. I spent all afternoon trying to come up with a good line and that was the result. Pathetic."

    c "Ahmm... yes. I asked a friend to give you that note... I'm so glad you got it."

    jv "A shy, joyous smile that makes me so tense I couldn't move a single muscle even if I tried. My heart is pounding now, as if it were trying to burst out from my chest and claim this girl for itself."

    j "So... ah... here we are. Out in the cool evening..."

    jv "Once again, the wind stirs up the palm fronds. The rhythmic noise is music to my ears. Clara flinches ever so softly against the gust of wind."
    
    jv "As it passes, she rights herself, as if supported by some new confidence. Her eyes lock with mine and she lazily twirls her long, dark hair around her finger."

    jv "All the while, the anxious beating of my heart grows louder. My throat is tight; I doubt I could even force a word out if I tried."

    menu:
        c "You see... ...I wanted to know... ...if you'd go out with me..."

        "Sure why not!":
            pass

        "I'd love to":
            pass
    
    scene black
    stop music 

    # play audio ["ear_ring.mp3", "heart-beat.ogg"]
    play music "ear_ring.mp3" volume 0.3 loop 
    play sound "heart-beat.ogg" loop

    pause 2.0
    scene bg_beach_night_4 with dissolve
    
    jv "I stand there, motionless, save for my pounding heart. I want to say something in reply, but my vocal cords feel like they've been stretched beyond the breaking point."

    c "... James?"

    jv "I reach up to try to massage my throat, but this only sends spikes of blinding pain along my arms."

    c "... James?"

    jv "My body seizes up, every muscle constricting, and my eyes squeeze shut against a surge of pain, sending me tumbling to the ground."

    stop music
    stop sound

    scene bg_beach_night_3

    c "... James?"

    jv "The beating in my chest suddenly stops, and I go weak at the knees. The world around me - the canopy of palm fronds, the darkening evening sky, Clara running towards me - all these fade to black."

    jv "The last things I remember before slipping away are the sounds of Clara screaming for help and the incessant rustle of the palm fronds above..."

    # Time Skip
    show screen time_skip with dissolve
    pause 1.5
    
    scene bg_hospital_1
    hide screen time_skip with dissolve

    pause 1.5
    jv "3 months since my heart attack, confined to a hospital room, I've had time to reflect on my condition, arrhythmia. It's a rare, potentially fatal heart disorder."
    
    jv "They said it was a miracle I'd lived so long without symptoms. My parents were devastated, even willing to sell our house for a cure that doesn't exist."

    jv "Hospital life is monotonous. Initially, there were visitors and get-well gifts, but they dwindled. Only my parents visited regularly."
    
    jv "Clara, the last friend to stop visiting, never mentioned the incident that led to my hospitalization."

    scene bg_beach_night_3
    with dissolve
    pause 1.5

    scene bg_hospital_1
    with dissolve

    jv "The hospital staff, always in a hurry, felt impersonal. I stopped watching TV and started reading, losing track of time."

    scene bg_hospital_2

    jv  "Then, one day, my nurse brought in a chess set. 'It's good for the mind,' she said. I was skeptical at first, but with nothing else to do, I started to play."

    jump intro_chess_game



label intro_chess_game:
    # board notation
    $ fen = STARTING_FEN

    if config.developer:
        call screen intro_chess(fen, player_color=None, depth=0)
    
    else:
        $ STOCKFISH_ENGINE = chess.engine.SimpleEngine.popen_uci(STOCKFISH, startupinfo=STARTUPINFO)
        # window hide
        $ quick_menu = False

        # avoid rolling back and losing chess game state
        $ renpy.block_rollback()

        # # disable Esc key menu to prevent the player from saving the game
        $ _game_menu_screen = None

        # call screen chess(fen, player_color=chess.WHITE, depth=-1)
        call screen intro_chess(fen, player_color=chess.WHITE, depth=0)

        # re-enable the Esc key menu
        $ _game_menu_screen = 'save'

        # avoid rolling back and entering the chess game again
        $ renpy.block_rollback()

        # restore rollback from this point on
        $ renpy.checkpoint()

        # kill stockfish engine
        $ quit_stockfish()

        # window show
        $ quick_menu = True
        

    scene bg_hospital_3

    jv "At first, I was just moving the pieces without any strategy."
    
    jv "But as days turned into weeks, I began to see patterns, strategies."
    
    jv "I read books about chess, learned famous moves. The game became a new world for me, a world where I could control the outcome."
    
    jv "It was a small thing, but it gave me a sense of control that was missing from my life."

    # Time Skip
    show screen time_skip_hospital with dissolve
    pause 1.5
    
    scene bg_hospital_1
    hide screen time_skip_hospital with dissolve

    pause 1.5

    jv "One day, the doctor, with my parents present, announced I could go home. The list of lifelong medications was overwhelming."

    jv "Then came the bombshell - I couldn't return to my old school."

    scene bg_hospital_4

    dr "Your parents have decided to transfer your treatment to their hometown, Iloilo City."
    
    dr "They have several great heart centers there that can manage your condition. Better living conditions and a slow paced life might be good for you!"

    jv "I was shocked. What am I going to do without the relentless pulse of the city, the neon-lit nights, and the symphony of urban chaos that I've grown to love?"
    
    jv "My parents have arranged a transfer to Central Iloilo University, an ordinary university with low barriers of entry. Apparently, they accept anybody there."

    jv "I felt insulted. An ordinary school. This is such a downgrade from my previous school De La Soleil University!"

    jv "However, I had no choice. I’m just happy to be alive. I had to accept my new reality. A clean slate isn't a bad thing. It's a fresh start, and my life isn't over."

    jv "And who knows, maybe they have a chess club."

    hide screen settings_button with dissolve

    scene black
    show screen end_intro with dissolve
    pause 1.5

    hide screen end_intro with dissolve
    pause 1.5

    return

label freeplay_chess_game:
    # board notation
    $ fen = STARTING_FEN

    call screen intro_chess(fen, player_color=None, depth=0, background="bg_freeplay_1")

    call screen main_menu

screen intro_chess(fen, player_color, depth, background="bg_hospital_3"):
    modal True

    default hover_displayable = HoverDisplayable()
    default chess_displayable = ChessDisplayable(
        fen=fen, 
        player_color=player_color, 
        depth=depth
    )
    
    add background

    # center bottom
    fixed xpos 600 ypos 920:
        hbox:
            spacing 40
            hbox spacing 5:
                text 'Resign' color COLOR_WHITE yalign 0.5
                textbutton '⚐':
                    action [
                        Confirm(
                            'Would you like to resign?', 
                            yes=[
                                Play('sound', AUDIO_DRAW),
                                # if the current player resigns, the winner will be the opposite side
                                Return(not chess_displayable.whose_turn)
                            ]
                        )
                    ]
                    style 'control_button' yalign 0.5

            hbox spacing 5:
                text 'Undo move' color COLOR_WHITE yalign 0.5
                textbutton '⟲':
                    action [Function(chess_displayable.undo_move)]
                    style 'control_button' yalign 0.5

            hbox spacing 5:
                text 'Flip board view' color COLOR_WHITE yalign 0.5
                textbutton '↑↓':
                    action [Play('sound', AUDIO_FLIP_BOARD),
                    ToggleField(chess_displayable, 'bottom_color'),
                    SetField(chess_displayable, 'has_flipped_board', True)]
                    style 'control_button' yalign 0.5

    # middle panel for chess displayable
    fixed xpos 600 ypos 180:
        add Image(IMG_CHESSBOARD)
        add chess_displayable
        add hover_displayable # hover loc over chesspieces
        if chess_displayable.game_status == CHECKMATE:
            # use a timer so the player can see the screen once again
            timer 4.0 action [
            Return(chess_displayable.winner)
            ]
        elif chess_displayable.game_status == STALEMATE:
            timer 4.0 action [
            Return(DRAW)
            ]
    

    # right panel for promotion selection
    showif chess_displayable.show_promotion_ui:
        text 'Select promotion piece type' xpos 1010 ypos 180 color COLOR_WHITE size 18
        vbox xalign 0.9 yalign 0.5 spacing 20:
            null height 40
            textbutton '♜':
                action SetField(chess_displayable, 'promotion', 'r') style 'promotion_piece'
            textbutton '♝':
                action SetField(chess_displayable, 'promotion', 'b') style 'promotion_piece'
            textbutton '♞':
                action SetField(chess_displayable, 'promotion', 'n') style 'promotion_piece'
            textbutton '♛':
                action SetField(chess_displayable, 'promotion', 'q') style 'promotion_piece'

screen time_skip():
    add Solid("#000")
    text "3 Months Later":
        align (0.5, 0.5)
        font "fonts/BoldFont.ttf"
        size 80


screen time_skip_hospital():
    add Solid("#000")
    text "A few days later":
        align (0.5, 0.5)
        font "fonts/BoldFont.ttf"
        size 80

screen intro():
    add Solid("#000")
    vbox:
        align (0.5, 0.5)
        spacing 10
        text "- Introduction -":
            align (0.5, 0.5)
            font "fonts/BoldFont.ttf"
            size 24
        text "Whispers on the twilight shores":
            align (0.5, 0.5)
            font "fonts/BoldFont.ttf"
            size 60

screen end_intro():
    add Solid("#000")
    vbox:
        align (0.5, 0.5)
        spacing 10
        text "- End -":
            align (0.5, 0.5)
            font "fonts/BoldFont.ttf"
            size 24
        text "To be continued":
            align (0.5, 0.5)
            font "fonts/BoldFont.ttf"
            size 60