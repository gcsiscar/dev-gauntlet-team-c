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

style something: 
    size 32
    font "fonts/BoldFont.ttf" 
    color gui.my_color 
    background "#B3B8CD"

screen character_details(name="???", char_image="cg_unlocked", stats=DEFAULT_STATS):
    # add "character_unlocked_idle":
    #     align (0.8, 0.2)

    # add char_image:
    #     align (0.784, 0.236)
    #     offset (-4, 2.8)


    # add "character_details_background":
    #     align (1.0, 0.50)

    frame:
        background Image("images/character_details_background.png")
        xalign 0.5
        # yalign 0.5
        xoffset 610
        yoffset 145
        xsize 543
        ysize 777

        frame:
            background None
            ymargin 24
            xmargin 24

            vbox:
                spacing 24

                # $ logo_pathname = "squares/" + char_image if not None else "cg_unlocked"
                # imagebutton:
                #     auto logo_pathname + "_%s.png"
                #     # ypos
                #     at transform:
                #         zoom 0.5

                vbox:
                    text "Character Name" font "fonts/BoldFont.ttf" color gui.my_color
                    text "[name]" font "fonts/Roboto-Regular.ttf" xoffset 8 color gui.my_color
                    add "small_text_container" offset(0,-32)

                vbox:
                    text "Friendship Level" yoffset -16 font "fonts/BoldFont.ttf" color gui.my_color
                    hbox:
                        for i in range(0, 5):
                            add "blue_heart":
                                size (40, 40)
                                yoffset -12

                hbox:
                    spacing 8
                    text "ELO":
                        font "fonts/BoldFont.ttf" 
                        color gui.my_color 
                        yalign 0.5
                    frame:
                        background "small_text_container"
                        text "{value}".format(value=stats["elo"]):
                            font "fonts/BoldFont.ttf" 
                            color gui.my_color
                            xalign 0.5
                            yalign 0.5

                hbox:
                    spacing 8
                    text "DEPTH":
                        font "fonts/BoldFont.ttf" 
                        color gui.my_color 
                        yalign 0.5
                    frame:
                        background "small_text_container"
                        text "{value}".format(value=stats["depth"]):
                            font "fonts/BoldFont.ttf" 
                            color gui.my_color 
                            yalign 0.5

                hbox:
                    spacing 8
                    text "MOVETIME":
                        font "fonts/BoldFont.ttf" 
                        color gui.my_color 
                        yalign 0.5

                    frame:
                        background "small_text_container"
                        text "{value}".format(value=stats["movetime"]):
                            font "fonts/BoldFont.ttf" 
                            color gui.my_color 
                            yalign 0.5
                    
                hbox:
                    textbutton "Challenge":
                        action [Hide("character_details"), Jump("freeplay_chess_game")]

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
        # xysize(50, 50)
        # scrollbars "vertical"

        # Since we have scrollbars, this positions the side, rather than
        # the vpgrid.
        # xalign 0.5

        $ characters = [
            {
                "name": "Clara",
                "unlocked": True,
                "square": "clara_square",
                "stats": {
                    "elo": "1143",
                    "depth": "1",
                    "movetime": "800",
                }
            },
            {
                "name": "Ava",
                "unlocked": True,
                "square": "ava_square",
                "stats": {
                    "elo": "1743",
                    "depth": "1",
                    "movetime": "4000",
                }
            },
            {
                "name": "Elara",
                "unlocked": True,
                "square": "elara_square",
                "stats": {
                    "elo": "1573",
                    "depth": "1",
                    "movetime": "3000",
                }
            },
            {
                "name": "Ria",
                "unlocked": True,
                "square": "ria_square",
                "stats": {
                    "elo": "1623",
                    "depth": "1",
                    "movetime": "1500",
                }
            },
            {
                "name": "???",
                "unlocked": False,
                "square": None
            },
            {
                "name": "???",
                "unlocked": False,
                "square": None
            },
        ]

        for idx, c in enumerate(characters):
            $ name = c["name"]
            $ is_unlocked = c["unlocked"]
            fixed:
                fit_first True
                if is_unlocked:
                    # $ logo_pathname = "squares/" + c["square"] if not None else "character_unlocked"
                    $ logo_pathname = "squares/" + c["square"] + "_idle.png"
                    imagebutton:
                        auto "character_unlocked_%s.png" 
                        selected_idle "character_unlocked_hover"
                        action [
                            SetVariable("char_selected_loc", idx),
                            SelectedIf(char_selected_loc == idx),
                            Show(
                                "character_details",
                                name=name,
                                char_image=c["square"],
                                stats=c["stats"]
                            )
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