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


# screen character_details(character={}):
    # $ name, _img, stats, _unlocked = character.values()

screen character_details(name="???", char_image="cg_unlocked", img={}, stats=DEFAULT_STATS):
    frame:
        background "character_details_background"
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

                # TODO: Display character logo here

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

                use character_stat(stat_label="ELO", stat_value=stats["elo"])

                use character_stat(stat_label="DEPTH", stat_value=stats["depth"])

                use character_stat(stat_label="MOVETIME", stat_value=stats["movetime"])

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
                "img": {
                    "square": "clara_square",
                    "full": "clara_full"
                },
                "stats": {
                    "elo": "1143",
                    "depth": "1",
                    "movetime": "800",
                },
                "unlocked": True,
            },
            {
                "name": "Ava",
                "img": {
                    "square": "ava_square",
                    "full": "ava_full"
                },
                "stats": {
                    "elo": "1743",
                    "depth": "1",
                    "movetime": "4000",
                },
                "unlocked": True,
            },
            {
                "name": "Elara",
                "img": {
                    "square": "elara_square",
                    "full": "elara_full"
                },
                "stats": {
                    "elo": "1573",
                    "depth": "1",
                    "movetime": "3000",
                },
                "unlocked": True,
            },
            {
                "name": "Ria",
                "img": {
                    "square": "ria_square",
                    "full": "ria_full"
                },
                "stats": {
                    "elo": "1623",
                    "depth": "1",
                    "movetime": "1500",
                },
                "unlocked": True,
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
                    $ img = c["img"]

                    $ logo_pathname = "squares/" + img["square"] if not None else "character_unlocked"
                    imagebutton:
                        auto logo_pathname + "_%s.png"
                        action [
                            SetVariable("char_selected_loc", idx),
                            SelectedIf(char_selected_loc == idx),
                            Show(
                                "character_details",
                                name=name,
                                char_image=img["square"],
                                img=img,
                                stats=c["stats"]
                            ),
                            # Show("character_details", c),
                        ]
                        at transform:
                            zoom 0.5

                    text "[name]" align (0.5, 1.0) yoffset 24 font "fonts/BoldFont.ttf" color gui.my_color
                else:
                    imagebutton idle "character_locked_background.png" action NullAction()
                    text "???" align (0.5, 1.0) yoffset 24 font "fonts/BoldFont.ttf" color gui.my_color
                    add "cg_locked":
                        align (0.5, 0.5)
                        yoffset 5
