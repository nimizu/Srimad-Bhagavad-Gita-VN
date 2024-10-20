define K = Character("Lord Krishna", color="#ffcccc")
define A = Character("Arjun", color="#ffcccc")

# Declare images with zoom
image field:
    "images/thebgfield.jpg"
    zoom 5

image SriKrishna:
    "images/SriKrishna.png"
    zoom 1.25

image Arjun:
    "images/Arjun.png"
    zoom 1.25

# Full script for Chapter 3
label start:
    scene field

    # Verse 1
    show Arjun

    window auto hide
    show Arjun:
        subpixel True ypos 1.1 
        xpos 0.2 
        linear 0.03 xpos 0.3 
    with Pause(0.13)
    show Arjun:
        pos (0.3, 1.1) 
    window auto show

    play sound "sound/Chap3/1.ogg"
    A "O Janardan, if You consider knowledge superior to action, then why do You ask me to wage this terrible war? My intellect is bewildered by Your ambiguous advice. Please tell me decisively the one path by which I may attain the highest good."
    "BG 3.3"
    stop sound

    # Verse 2
    hide Arjun
    show SriKrishna

    show SriKrishna:
        subpixel True pos (0.8, 1.2) 


    play sound "sound/Chap3/2.ogg"
    K "O sinless one, the two paths leading to enlightenment were previously explained by Me: the path of knowledge, for those inclined toward contemplation, and the path of work for those inclined toward action."
    "BG 3.4"
    stop sound

    # Verse 3
    play sound "sound/Chap3/3.ogg"
    K "One cannot achieve freedom from karmic reactions by merely abstaining from work, nor can one attain perfection of knowledge by mere physical renunciation."
    "BG 3.5"
    stop sound

    # Verse 4
    play sound "sound/Chap3/4.ogg"
    K "There is no one who can remain without action even for a moment. Indeed, all beings are compelled to act by their qualities born of material nature (the three guṇas)."
    "BG 3.6"
    stop sound

    # Verse 5
    play sound "sound/Chap3/5.ogg"
    K "Those who restrain the external organs of action, while continuing to dwell on sense objects in the mind, certainly delude themselves and are to be called hypocrites."
    "BG 3.7"
    stop sound

    # Verse 6
    play sound "sound/Chap3/6.ogg"
    K "But those karm yogis who control their knowledge senses with the mind, O Arjun, and engage the working senses in working without attachment, are certainly superior."
    "BG 3.8"
    stop sound

    # Verse 7
    play sound "sound/Chap3/7.ogg"
    K "You should thus perform your prescribed Vedic duties, since action is superior to inaction. By ceasing activity, even your bodily maintenance will not be possible."
    "BG 3.9"
    stop sound

    # Verse 8
    play sound "sound/Chap3/8.ogg"
    K "Work must be done as a yajna to the Supreme Lord; otherwise, work causes bondage in this material world. Therefore, O son of Kunti, for the satisfaction of God, perform your prescribed duties, without being attached to the results."
    "BG 3.10"
    stop sound

    # Verse 9
    play sound "sound/Chap3/9.ogg"
    K "In the beginning of creation, Brahma created humankind along with duties, and said, 'Prosper in the performance of these yajñas (sacrifices), for they shall bestow upon you all you wish to achieve.'"
    "BG 3.11"
    stop sound

    # Verse 10
    play sound "sound/Chap3/10.ogg"
    K "By your sacrifices, the celestial gods will be pleased, and by cooperation between humans and the celestial gods, great prosperity will reign for all."
    "BG 3.12"
    stop sound

    # Verse 11
    play sound "sound/Chap3/11.ogg"
    K "The celestial gods, being satisfied by the performance of sacrifice, will grant you all the desired necessities of life. But those who enjoy what is given to them, without making offerings in return, are verily thieves."
    "BG 3.13"
    stop sound

    # Verse 12
    play sound "sound/Chap3/12.ogg"
    K "The spiritually-minded, who eat food that is first offered in sacrifice, are released from all kinds of sin. Others, who cook food for their own enjoyment, verily eat only sin."
    "BG 3.14"
    stop sound

    # Verse 13
    play sound "sound/Chap3/13.ogg"
    K "All living beings subsist on food, and food is produced by rains. Rains come from the performance of sacrifice, and sacrifice is produced by the performance of prescribed duties."
    "BG 3.15"
    stop sound

    # Verse 14
    play sound "sound/Chap3/14.ogg"
    K "The duties for human beings are described in the Vedas, and the Vedas are manifested by God Himself. Therefore, the all-pervading Lord is eternally present in acts of sacrifice."
    "BG 3.16"
    stop sound

    # Verse 15
    play sound "sound/Chap3/15.ogg"
    K "O Parth, those who do not accept their responsibility in the cycle of sacrifice established by the Vedas are sinful. They live only for the delight of their senses; indeed, their lives are in vain."
    "BG 3.17"
    stop sound

    # Verse 16
    play sound "sound/Chap3/16.ogg"
    K "But those who rejoice in the self, who are illumined and fully satisfied in the self, for them, there is no duty."
    "BG 3.18"
    stop sound

    # Verse 17
    play sound "sound/Chap3/17.ogg"
    K "Such self-realized souls have nothing to gain or lose either in discharging or renouncing their duties. Nor do they need to depend on other living beings to fulfill their self-interest."
    "BG 3.19"
    stop sound

    # Verse 18
    play sound "sound/Chap3/18.ogg"
    K "Therefore, giving up attachment, perform actions as a matter of duty because by working without being attached to the fruits, one attains the Supreme."
    "BG 3.20 – 3.21"
    stop sound

    # Verse 19
    play sound "sound/Chap3/19.ogg"
    K "By performing their prescribed duties, King Janak and others attained perfection. You should also perform your duties to set an example for the good of the world."
    "BG 3.22"
    stop sound

    # Verse 20
    play sound "sound/Chap3/20.ogg"
    K "Whatever actions great persons perform, common people follow. Whatever standards they set, all the world pursues."
    "BG 3.23"
    stop sound

    # Verse 21
    play sound "sound/Chap3/21.ogg"
    K "There is no duty for Me to do in all the three worlds, O Parth, nor do I have anything to gain or attain. Yet, I am engaged in prescribed duties."
    "BG 3.24"
    stop sound

    # Verse 22
    play sound "sound/Chap3/22.ogg"
    K "For if I did not carefully perform the prescribed duties, O Parth, all men would follow My path in all respects."
    "BG 3.25"
    stop sound

    # Verse 23
    play sound "sound/Chap3/23.ogg"
    K "If I ceased to perform prescribed actions, all these worlds would perish. I would be responsible for the pandemonium that would prevail, and would thereby destroy the peace of the human race."
    "BG 3.26"
    stop sound

    # Verse 24
    play sound "sound/Chap3/24.ogg"
    K "As ignorant people perform their duties with attachment to the results, O scion of Bharat, so should the wise act without attachment, for the sake of leading people on the right path."
    "BG 3.27"
    stop sound

    # Verse 25
    play sound "sound/Chap3/25.ogg"
    K "The wise should not create discord in the intellects of ignorant people, who are attached to fruitive actions, by inducing them to stop work."
    "BG 3.28"
    stop sound

    # Verse 26
    play sound "sound/Chap3/26.ogg"
    K "Rather, by performing their duties in an enlightened manner, they should inspire the ignorant also to do their prescribed duties."
    "BG 3.29"
    stop sound

    # Verse 27
    play sound "sound/Chap3/27.ogg"
    K "All activities are carried out by the three modes of material nature. But in ignorance, the soul, deluded by false identification with the body, thinks of itself as the doer."
    "BG 3.30"
    stop sound

    # Verse 28
    play sound "sound/Chap3/28.ogg"
    K "O mighty armed Arjun, one who is in the knowledge of the truth, who knows that the soul is eternal and beyond the three modes of material nature, is not entangled in the dualities of this world."
    "BG 3.31"
    stop sound

    # Verse 29
    play sound "sound/Chap3/29.ogg"
    K "One who is free from attachment and is a well-wisher of all living entities, and who has no desires for material gain, is certainly not affected by sinful actions, just as a lotus flower is untouched by water."
    "BG 3.32"
    stop sound

    # Verse 30
    play sound "sound/Chap3/30.ogg"
    K "Therefore, surrender all your works unto Me, the Supreme Personality of Godhead. In full knowledge of Me, without desires for gain, and without false ego, fight."
    "BG 3.33"
    stop sound

    # Verse 31
    play sound "sound/Chap3/31.ogg"
    K "Those who, having faith, follow this teaching of Mine, with their minds and senses fully engaged in My devotion, are certainly liberated from the bondage of material actions."
    "BG 3.34"
    stop sound

    # Verse 32
    play sound "sound/Chap3/32.ogg"
    K "But those who, being envious of My teaching, do not listen to My words, are to be considered as foolish and ignorant, and are bound by the material nature."
    "BG 3.35"
    stop sound

    # Verse 33
    play sound "sound/Chap3/33.ogg"
    K "Even the wise man acts according to his own nature; for everyone follows their own nature. What can repression accomplish?"
    "BG 3.36"
    stop sound

    # Verse 34
    play sound "sound/Chap3/34.ogg"
    K "It is better to engage in one’s own duty, even if it is imperfectly performed, than to perform another’s duty perfectly. It is better to die in one’s own duty than to live by the duty of another."
    "BG 3.37"
    stop sound

    # Verse 35
    play sound "sound/Chap3/35.ogg"
    K "Surrender to the Supreme Lord. Only then will you be free from sin, and you will be promoted to the higher planets."
    "BG 3.38"
    stop sound

    # Verse 36
    play sound "sound/Chap3/36.ogg"
    K "O Arjun, what is that force that compels a person to sin even against their own wishes?"
    "BG 3.39"
    stop sound

    # Verse 37
    play sound "sound/Chap3/37.ogg"
    K "It is lust which is born of contact with the material mode of passion and is the greatest enemy of the conditioned soul."
    "BG 3.40"
    stop sound

    # Verse 38
    play sound "sound/Chap3/38.ogg"
    K "As fire is covered by smoke, as a mirror is covered by dust, and as an embryo is covered by the womb, the eternal soul is covered by this lust."
    "BG 3.41"
    stop sound

    # Verse 39
    play sound "sound/Chap3/39.ogg"
    K "Therefore, O Arjun, one must first control the senses and then the mind, then one can attain real knowledge."
    "BG 3.42"
    stop sound

    # Verse 40
    play sound "sound/Chap3/40.ogg"
    K "Thus knowing the soul to be superior to the material intellect, O mighty armed Arjun, subdue the lower self (senses, mind, and intellect) by the higher self (strength of the soul), and kill this formidable enemy called lust."
    "BG 3.43"
    stop sound

    return