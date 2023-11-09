## Character screen ##############################################################
##
## The character screen is a graphical user interface component that presents essential 
## information about the player's in-game character. 
##
##
define char_selected_loc = -1

screen character_details(name="???",char_image="cg_unlocked"):
    add "character_details_background":
        align (1.0, 0.51)

    add "character_unlocked_idle":
        align (0.8, 0.2)
    
    add char_image:
        align (0.784, 0.236)
        offset (-4, 2.8)

    frame:
        background None
        align (1.0, 0.5)
        offset (-83, -35)

        vbox:
            spacing 16
            vbox:
                xalign 1.0
                text "Character Name" font "fonts/BoldFont.ttf" color gui.my_color
                text "[name]" font "fonts/Roboto-Regular.ttf" xoffset 8 color gui.my_color
                add "small_text_container":
                    offset(0,-32)
                text "Friendship Level" yoffset -16 font "fonts/BoldFont.ttf" color gui.my_color
                hbox:
                    for i in range(0, 5):
                        add "blue_heart":
                            size (40, 40)
                            yoffset -12
            
            vbox:
                yoffset 20
                spacing 24
                for i in ["Likes", "Dislikes", "Notes"]:
                    vbox:
                        text "[i]" font "fonts/BoldFont.ttf" color gui.my_color
                        add "large_text_container"

screen character_screen():
    tag menu

    add gui.game_menu_background

    text "Characters" align (0.5, 0.06) size 48 color "#ebabd4" font "fonts/BoldFont.ttf"

    vbox xalign 0.0 yalign 0.0:
        imagebutton idle "gui/button/back_idle.png" action [Return(), Hide("character_details")]
    
    vbox xalign 1.0 yalign 1.0:
        imagebutton idle "gui/button/settings_idle.png" action ShowMenu("preferences")
    
    add "character_sheet_background.png":
        align (0.18, 0.52)

    vpgrid:
        align (0.23, 0.52)
        cols 4
        rows 4
        xspacing 5
        yspacing 40
        draggable True
        mousewheel True
        ysize 750
        # xysize(50, 50)
        # scrollbars "vertical"

        # Since we have scrollbars, this positions the side, rather than
        # the vpgrid.
        # xalign 0.5
        $ characters = [
            { "name": "Rosalyn", "unlocked": True },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False },
            { "name": "???", "unlocked": False }
        ]
        for idx, c in enumerate(characters):
            $ name = c["name"]
            $ is_unlocked = c["unlocked"]
            fixed:
                fit_first True
                if is_unlocked:
                    imagebutton:
                        auto "character_unlocked_%s.png" 
                        selected_idle "character_unlocked_hover"
                        action [SetVariable("char_selected_loc", idx), SelectedIf(char_selected_loc == idx), Hide("character_details"), Show("character_details", name=name)]
                    text "[name]" align (0.5, 1.0) yoffset 24 font "fonts/BoldFont.ttf" color gui.my_color
                    add "cg_unlocked":
                        align (0.5, 0.5)
                        yoffset 5
                else:
                    imagebutton idle "character_locked_background.png" action NullAction()
                    text "???" align (0.5, 1.0) yoffset 24 font "fonts/BoldFont.ttf" color gui.my_color
                    add "cg_locked":
                        align (0.5, 0.5)
                        yoffset 5