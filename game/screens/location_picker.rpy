define locations = [
    { "name": "Molo Church", "img":"molo_church_thumbnail" }, 
    { "name": "Molo Mansion", "img": "brick_pavement_thumbnail" }, 
    { "name": "Esplanade 4", "img": "esplanade_4_thumbnail" },
    { "name": "Medical City", "img": "esplanade_medical_city_thumbnail" }, 
    { "name": "Provincial Capitol", "img": "esplanade_provincial_capitol_thumbnail" }, { "name": "Riverside", "img": "riverside_thumbnail" }]


screen location_picker(hero_name=None, hero_img=None):
    tag menu

    add gui.game_menu_background

    text "Locations":
        xalign 0.5
        yalign 0.1
        font "fonts/BoldFont.ttf" 
        color "#ebabd4" 
        outlines [ (absolute(8), "#fff", absolute(0), absolute(0)) ]
        size 48

    vpgrid:
            align (0.5, 0.5)
            cols 3
            spacing 50

            for location in locations:
                $ loc = "images/locations/{val}_%s.png".format(val=location["img"])
                $ name = location["name"]
                fixed:
                    fit_first True
                    imagebutton: 
                        auto loc
                        action [PauseAudio("music", value=True), Call("freeplay_chess_game", background=location["img"], hero_name=hero_name,hero_img=hero_img)]
                    text "[name]":
                        align (0.5, 0.5)
                        font "fonts/BoldFont.ttf"
                        outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
                        size 40
                    
