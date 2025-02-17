# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

transform bounce:
    alpha 0.0
    xoffset 0.0
    yoffset 10.0
    linear 0.2 alpha 1.0 xoffset 0.0 yoffset 0.0
    linear 0.2 alpha 1.0 xoffset 0.0 yoffset -10.0
    linear 0.2 alpha 1.0 xoffset 0.0 yoffset 0.0

define s = Character("Saki")

define r = Character("Rin")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show saki normal at right with dissolve

    show rin normal at left with dissolve

    # These display lines of dialogue.
    
    s "It's already so late... I can't believe we re still out here after that meeting." with dissolve
    
    r "I know, right? The boss was unbearable today. I swear, it’s like he doesn’t know the meaning of 'work-life balance.'" with bounce

    s "Tell me about it. I thought I was going to lose it when he threw more tasks on my plate. Like, don't we already have a full workload?"

    r "Honestly, I think he’s trying to see how far he can push us. And I’m not sure if he even cares about our health. It’s just ‘do more, faster, better’ every single time."

    s "Exactly! And he’s got this attitude like if you don’t stay late, you’re slacking off. But I’ve been working non-stop for the last month. It’s exhausting."

    r "He always says, 'It’s for the company’s success.' But at what cost, Saki? We’re barely managing to keep up, and he's acting like we have unlimited energy."

    s "And have you noticed how he keeps piling on tasks without ever acknowledging how much we’re already doing? It’s like he thinks we’re robots."

    r "Ugh, don’t even get me started on the emails. The guy sends them at 10 PM and expects immediate responses. Who does that?"

    s "I’m starting to think we’re his personal 24/7 help desk. It's not even about productivity anymore—it's just pure micromanaging."

    r "I’ve been staying up late just to meet deadlines. But, honestly, I don’t even know if it's worth it anymore. The rewards don't match the effort."

    s "Yeah, I used to be so motivated, but now it feels like I’m just surviving, not thriving. Every day is just more stress, more tasks. Where’s the light at the end of the tunnel?"

    r "There isn't one, at least not with this boss. Every time I think I’ve crossed the finish line, he just throws another hurdle in front of me."

    s "It’s crazy. I used to love coming to work—working with the team, collaborating, learning new things. Now it feels like I’m just trying to avoid burnout."

    r "Burnout? I'm already there. I don’t even remember the last time I had a day off without checking work emails every couple of hours."

    s "Same here. It’s like there’s no escape. I think... I think it’s time to look for something else. Somewhere where I can actually breathe again."

    r "I was thinking the same thing. I’m all for putting in the effort, but I need a break. I’m tired of working under someone who doesn’t even care about our well-being."

    s "I mean, we both deserve better, right? It’s not like we’re asking for a vacation every week—just reasonable expectations and respect for our time."

    r "Exactly. It’s not too much to ask. We’re doing our best, and honestly, that should be enough."

    s "I don’t know... maybe it’s time we both start looking for something else. Somewhere that values us more."

    r "Yeah... I’ve got a few companies in mind already. I’ll start updating my resume tomorrow."

    s "Same here. I’ve been thinking about it for a while, but today, after the endless overtime, I’m convinced. It's time for a change."

    r "I’m glad we’re on the same page. If we both leave, maybe he’ll finally understand how much we were carrying the team."

    s "I’m not sure he’d care, honestly. But at least we’ll be free."

    r "You know what? You’re right. Let’s leave all this behind and take our skills to a place where we’re respected."

    s "Deal. We’ll make it through this together, Rin. We’ve got this."

    r "We do. Together, we can handle anything."

    s "how"
    
    # This ends the game.

    return
