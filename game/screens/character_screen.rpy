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
    # offset (8, -33)
    font "fonts/BoldFont.ttf"
    outlines [(absolute(2), "#fff", absolute(0), absolute(0))]
    color "#ebaad4"

screen character_stat(stat_label="", stat_value=""):
    vbox:
        style_prefix "character_stat"
        text "[stat_label]" font "fonts/BoldFont.ttf" color gui.my_color
        frame:
            background "small_text_container"
            text "[stat_value]" style "details_text"

screen friendship_level(level=0):
    vbox:
        spacing 10
        text "Friendship Level" font "fonts/BoldFont.ttf" color gui.my_color
        hbox:
            for i in range(0, 5):
                if level > i:
                    add "pink_heart":
                        size (40, 40)
                        yoffset -12
                else:
                    add "blue_heart":
                        size (40, 40)
                        yoffset -12


screen character_details(name="???", img={}, stats=DEFAULT_STATS, backstory="???"):
    $ elo = stats["elo"]
    $ depth = stats["depth"]
    $ movetime = stats["movetime"]
    $ full_img = img["full"]
    $ bg_char = img["bg"]
    frame:
        background "character_details_background"
        xalign 0.5
        xoffset 600
        yoffset 145

        vbox:
            offset (20, 30)
            vbox:
                offset (5, 20)
                xalign 1.0
                spacing 20
                use character_stat("Character Name", name)
                use friendship_level(2)
                use character_stat("ELO", elo)
                use character_stat("Depth", depth)
                use character_stat("Movetime", movetime)
                
            vbox:
                yoffset 40
                spacing 24
                vbox:
                    text "Backstory" font "fonts/BoldFont.ttf" color gui.my_color
                    add "large_text_container"
                    text "[backstory]" style "details_text" xoffset 10 yoffset -80 font "fonts/Roboto-Bold.ttf"
                vbox:
                    yoffset -120
                    xalign 1.0
                    imagebutton:
                        auto "gui/button/red_btn_%s.png"
                        action [Hide("character_details"), Show("location_picker",hero_name=name,hero_img=bg_char)]
                    text "Challenge" font "fonts/BoldFont.ttf" xalign 0.5 yoffset -90

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
                    "full": "clara_full",
                    "bg": "clara"
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
                    "full": "ava_full",
                    "bg": "ava"
                },
                "stats": {
                    "elo": "1743",
                    "depth": "4",
                    "movetime": "4000",
                },
                "unlocked": True
            },
            {
                "name": "Elara",
                "backstory": "Her chess prowess honed in grand\nlibraries, a beacon of wisdom.",
                "img": {
                    "square": "elara_square",
                    "full": "elara_full",
                    "bg": "elara"
                },
                "stats": {
                    "elo": "1573",
                    "depth": "2",
                    "movetime": "3000",
                },
                "unlocked": True
            },
            {
                "name": "Ria",
                "backstory": "For Ria, chess is not just a game;\nit's a way of life.",
                "img": {
                    "square": "ria_square",
                    "full": "ria_full",
                    "bg": "ria"
                },
                "stats": {
                    "elo": "1623",
                    "depth": "3",
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
                    $ stats = c["stats"]
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
                                stats=stats,
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
