## Character screen ##############################################################
##
## The character screen is a graphical user interface component that presents essential
## information about the player's in-game character.
##
##
define char_selected_loc = -1

define DEFAULT_STATS = {
    "elo": None,
    "depth": None,
    "movetime": None,
}

style details_text:
    offset (8, -33)
    font "fonts/BoldFont.ttf"
    outlines [(absolute(2), "#fff", absolute(0), absolute(0))]
    color "#ebaad4"

# screen character_details(name="???", char_image="cg_unlocked", avatar="cg_unlocked", stats=DEFAULT_STATS, backstory="???"):
#     $ elo = stats["elo"]
#     $ depth = stats["depth"]
#     $ movetime = stats["movetime"]

screen character_stat(stat_label="", stat_value=""):
    hbox:
        spacing 8
        text stat_label:
            font "fonts/BoldFont.ttf" 
            color gui.my_color 
            yalign 0.5
        frame:
            background "small_text_container"
            text "{value}".format(value=stat_value):
                font "fonts/BoldFont.ttf" 
                color gui.my_color
                xalign 0.5
                yalign 0.5


screen character_details(name="???", img={}, stats=DEFAULT_STATS, backstory="???"):
    $ elo = stats["elo"]
    $ depth = stats["depth"]
    $ movetime = stats["movetime"]
    $ full_img = img["full"]
    frame:
        background "character_details_background"
        xalign 0.5
        # yalign 0.5
        # xoffset 585
        xoffset 600
        yoffset 145
        # xsize 543
        # ysize 777
        # ypadding 20

        vbox:
            offset (20, 20)
            vbox:
                offset (5, 20)
                xalign 1.0
                text "Character Name" font "fonts/BoldFont.ttf" color gui.my_color
                add "small_text_container"
                text "[name]" style "details_text"
                text "Friendship Level" yoffset -10 font "fonts/BoldFont.ttf" color gui.my_color
                hbox:
                    for i in range(0, 5):
                        add "blue_heart":
                            size (40, 40)
                            yoffset -12
                text "ELO" font "fonts/BoldFont.ttf" color gui.my_color
                add "small_text_container"
                text "[elo]" style "details_text"

                text "Depth" font "fonts/BoldFont.ttf" color gui.my_color
                add "small_text_container"
                text "[depth]" style "details_text"

                text "Movetime" font "fonts/BoldFont.ttf" color gui.my_color
                add "small_text_container"
                text "[movetime]" style "details_text"
                
            vbox:
                yoffset 20
                spacing 24
                vbox:
                    text "Backstory" font "fonts/BoldFont.ttf" color gui.my_color
                    add "large_text_container"
                    text "[backstory]" style "details_text" yoffset -80 font "fonts/Roboto-Bold.ttf"
                vbox:
                    yoffset -120
                    xalign 1.0
                    imagebutton:
                        auto "gui/button/red_btn_%s.png"
                        action [Hide("character_details"), Jump("freeplay_chess_game")]
                    text "Challenge" font "fonts/BoldFont.ttf" xalign 0.5 yoffset -90

                # use character_stat(stat_label="ELO", stat_value=stats["elo"])

                # use character_stat(stat_label="DEPTH", stat_value=stats["depth"])

                # use character_stat(stat_label="MOVETIME", stat_value=stats["movetime"])

    vbox:
        align (0.8, 0.2)
        add full_img:
            xalign 0.5
            yoffset 50


screen character_screen():
    tag menu

    add gui.game_menu_background

    text "Characters" align (0.5, 0.06) size 48 color "#ebabd4" font "fonts/BoldFont.ttf"

    vbox xalign 0.0 yalign 0.0:
        imagebutton idle "gui/button/back_idle.png" action [Return(), Hide("character_details")]

    use settings_button()

    add "character_sheet_background.png":
        align (0.18, 0.52)

    vpgrid:
        align (0.23, 0.52)
        cols 4
        rows 4
        xspacing 5
        yspacing 40
        # draggable True
        # mousewheel True
        ysize 750

        $ characters = [
            {
                "name": "Clara",
                "backstory": "A mysterious old flame reappears\nagain....for a game of chess?!",
                "img": {
                    "square": "clara_square",
                    "full": "clara_full"
                },
                "stats": {
                    "elo": "1143",
                    "depth": "1",
                    "movetime": "800",
                },
                "unlocked": True
            },
            {
                "name": "Ava",
                "backstory": "The quiet thinker, whose world center\non patterns and calculated moves.",
                "img": {
                    "square": "ava_square",
                    "full": "ava_full"
                },
                "stats": {
                    "elo": "1743",
                    "depth": "1",
                    "movetime": "4000",
                },
                "unlocked": True
            },
            {
                "name": "Elara",
                "backstory": "Her chess prowess honed in grand\nlibraries, a beacon of wisdom.",
                "img": {
                    "square": "elara_square",
                    "full": "elara_full"
                },
                "stats": {
                    "elo": "1573",
                    "depth": "1",
                    "movetime": "3000",
                },
                "unlocked": True
            },
            {
                "name": "Ria",
                "backstory": "For Ria, chess is not just a game;\nit's a way of life.",
                "img": {
                    "square": "ria_square",
                    "full": "ria_full"
                },
                "stats": {
                    "elo": "1623",
                    "depth": "1",
                    "movetime": "1500",
                },
                "unlocked": True
            },
            {
                "name": "???",
                "unlocked": False,
            },
            {
                "name": "???",
                "unlocked": False,
            },
        ]

        for idx, c in enumerate(characters):
            $ name = c["name"]
            $ is_unlocked = c["unlocked"]
            fixed:
                fit_first True
                if is_unlocked:
                    # $ logo_pathname = "squares/" + c["square"] if not None else "character_unlocked"
                    $ logo_pathname = "squares/" + c["img"]["square"] + "_idle.png"
                    $ img = c["img"]
                    imagebutton:
                        auto "character_unlocked_%s.png" 
                        selected_idle "character_unlocked_hover"
                        style "button_sound_click"
                        action [
                            SetVariable("char_selected_loc", idx),
                            SelectedIf(char_selected_loc == idx),
                            Show(
                                "character_details",
                                name=name,
                                stats=c["stats"],
                                img=img,
                                backstory=c["backstory"]
                            ),
                        ]
                    add logo_pathname: 
                        align (0.5, 0.5)

                    text "[name]" align (0.5, 1.0) yoffset 24 font "fonts/BoldFont.ttf" color gui.my_color
                else:
                    imagebutton idle "character_locked_background.png" action NullAction()
                    text "???" align (0.5, 1.0) yoffset 24 font "fonts/BoldFont.ttf" color gui.my_color
                    add "cg_locked":
                        align (0.5, 0.5)
                        yoffset 5
