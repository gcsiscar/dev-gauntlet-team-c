init python:

    g = Gallery()

    g.button("CG1_Button")
    g.unlock_image("CG1")


    g.button("CG2_Button")
    g.unlock_image("CG2")

    g.button("CG3_Button")
    g.unlock_image("CG3")

    g.transition = dissolve

screen gallery():
    tag menu

    add gui.game_menu_background

    vbox xalign 0.0 yalign 0.0:
        imagebutton idle "gui/button/back_idle.png" action Return()
    
    vbox xalign 1.0 yalign 1.0:
        imagebutton idle "gui/button/settings_idle.png" action ShowMenu("preferences")

    grid 3 3:
        xfill True
        yfill True

        add g.make_button("CG1_Button", locked="cg_locked.png", unlocked="cg_unlocked.png", xalign=0.5, yalign=0.5)
        add g.make_button("CG2_Button", locked="cg_locked.png", unlocked="cg_unlocked.png", xalign=0.5, yalign=0.5)
        add g.make_button("CG3_Button", locked="cg_locked.png", unlocked="cg_unlocked.png", xalign=0.5, yalign=0.5)

        
        add g.make_button("CG1_Button", locked="cg_locked.png", unlocked="cg_unlocked.png", xalign=0.5, yalign=0.5)
        add g.make_button("CG2_Button", locked="cg_locked.png", unlocked="cg_unlocked.png", xalign=0.5, yalign=0.5)
        add g.make_button("CG3_Button", locked="cg_locked.png", unlocked="cg_unlocked.png", xalign=0.5, yalign=0.5)