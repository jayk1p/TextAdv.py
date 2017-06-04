#Text based Adventure - Drunk Night

print """
    You go to your mansion and have to sneak in b/c you spent the
    night at your best friend's place from high school and got so drunk that
    you don't remember a single thing.
    Which way do you enter? Front or back?
    """


door = raw_input("> ")

if door == "front":
    print """You made the entrance too obvious and you have been caught
    by your wife. You run out of the house while her chasing after your ass with a
    extra large broom stick"""




elif door == "back":
    print """
    You've successfully entered the mansion without having your
    wife notice you
    """

    print """
    You're starting to get very thirsty. The kitchen is just a few feet away
    while your room is another 50 feet away. Which way do you go?"""


    thirsty = raw_input("> ")

    if thirsty == "kitchen":
        print """
        You've screwed up you jackass. You're wife is right there"""

    elif thirsty == "room":
        print """
        Success! You've made it back to your room and you fell asleep
        in your bed as if nothing had happened. """


else:
    print "Goodbye"
