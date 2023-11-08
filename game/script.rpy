define j = Character("James")
define jv = Character("James (Inside Voice)")
define c = Character("Clara")
define uf = Character("Unknown Figure")
define dr = Character("Doctor")

label start:
    show screen settings_button
    scene bg_beach_night_1

    jv "A gentle breeze causes the palm fronds overhead to rustle, sounding like nature's own bamboo wind chimes. This is a popular retreat for couples in the summer. The tropical trees provide a lush green canopy, far out of sight of teachers and fellow students. But now, in the late dry season, it feels like I'm standing under a pile of kindling. I breathe into my cupped hands and rub them together furiously to prevent them from numbing in this evening chill."

    j "Just how long am I expected to wait out here, anyway? I'm sure the note said 7:00 PM."

    jv "Ah yes... the note... slipped in my bag while I wasn't looking. As far as clichés go, I'm more a fan of the late text message, but at least this way shows a bit of initiative. As I ponder the meaning of the note, the dusk gradually deepens. The fireflies silently lighting up the darkening sky are the only sign of time passing in this stagnant world. Their slow dance upon the quiet beach makes it seem like time has slowed to a crawl. As I gaze into the night sky, the rustling of dry sand nearby startles me, interrupting the quiet mood. Someone is approaching me from behind."

    jv "???"

    uf "Hi... James? You came?"

    jv "She asks something so quietly, I can barely hear it. It's dark, but I can see her outline. That soft voice? I'd know it anywhere.  I feel my heart skip a beat. It's her—the one I've always listened to from afar. My heart beats faster as I turn to see her…"

    scene bg_beach_night_2

    j "Clara? I got a note telling me to wait here... it was yours?"

    jv "Dammit. I spent all afternoon trying to come up with a good line and that was the result. Pathetic."

    c "Ahmm... yes. I asked a friend to give you that note... I'm so glad you got it."

    jv "A shy, joyous smile that makes me so tense I couldn't move a single muscle even if I tried. My heart is pounding now, as if it were trying to burst out from my chest and claim this girl for itself."

    j "So... ah... here we are. Out in the cool evening..."

    jv "Once again, the wind stirs up the palm fronds. The rhythmic noise is music to my ears. Clara flinches ever so softly against the gust of wind. As it passes, she rights herself, as if supported by some new confidence. Her eyes lock with mine and she lazily twirls her long, dark hair around her finger. All the while, the anxious beating of my heart grows louder. My throat is tight; I doubt I could even force a word out if I tried."

    menu:
        c "You see... ...I wanted to know... ...if you'd go out with me..."

        "Sure why not!":
            pass

        "I'd love to":
            pass
    
    jv "I stand there, motionless, save for my pounding heart. I want to say something in reply, but my vocal cords feel like they've been stretched beyond the breaking point."

    c "... James?"

    jv "I reach up to try to massage my throat, but this only sends spikes of blinding pain along my arms."

    c "... James?"

    jv "My body seizes up, every muscle constricting, and my eyes squeeze shut against a surge of pain, sending me tumbling to the ground."

    scene bg_beach_night_3

    c "... James?"

    jv "The beating in my chest suddenly stops, and I go weak at the knees. The world around me - the canopy of palm fronds, the darkening evening sky, Clara running towards me - all these fade to black. The last things I remember before slipping away are the sounds of Clara screaming for help and the incessant rustle of the palm fronds above..."

    "Time Skip"

    scene bg_hospital_1

    jv "3 months since my heart attack, confined to a hospital room, I've had time to reflect on my condition, arrhythmia. It's a rare, potentially fatal heart disorder. They said it was a miracle I'd lived so long without symptoms. My parents were devastated, even willing to sell our house for a cure that doesn't exist."

    jv "Hospital life is monotonous. Initially, there were visitors and get-well gifts, but they dwindled. Only my parents visited regularly. Clara, the last friend to stop visiting, never mentioned the incident that led to my hospitalization."

    scene bg_beach_night_3
    with dissolve
    pause 1.5

    scene bg_hospital_1
    with dissolve

    jv "The hospital staff, always in a hurry, felt impersonal. I stopped watching TV and started reading, losing track of time."

    scene bg_hospital_2

    jv  "Then, one day, my nurse brought in a chess set. 'It's good for the mind,' she said. I was skeptical at first, but with nothing else to do, I started to play."

    scene bg_hospital_3

    jv "One day, the doctor, with my parents present, announced I could go home. The list of lifelong medications was overwhelming. Then came the bombshell - I couldn't return to my old school."

    dr "Your parents have decided to transfer your treatment to their hometown, Iloilo City. They have several great heart centers there that can manage your condition. Better living conditions and a slow paced life might be good for you!"

    jv "I was shocked. What am I going to do with my ???. My parents have arranged a transfer to Central Iloilo University, an ordinary university with low barriers of entry. Apparently, they accept anybody there."

    jv "I felt insulted. An ordinary school. This is such a downgrade from my previous school De La Soleil University! However, I had no choice. I’m just happy to be alive. I had to accept my new reality. A clean slate isn't a bad thing. It's a fresh start, and my life isn't over. And who knows, maybe they have a chess club."

    return