# gpt3-persona-bot
a simple bot that allows you to chat with various personas

You will need a key. 

## how to run the cli

    harper@ {~/openai/bot}$ pip3 install -r requirements.txt
    ...
    ...
    harper@ {~/openai/bot}$ export OPENAI_API_KEY=sk-KEYKEYKEYKEYKEYKEYKEYKEY

    harper@ {~/openai/bot}$ python3 cli.py        07/22/20  5:45PM
    _   _                                        ____
    | \ | | _____      __      __ _  __ _  ___   / ___|_   _ _ __ _   _
    |  \| |/ _ \ \ /\ / /____ / _` |/ _` |/ _ \ | |  _| | | | '__| | | |
    | |\  |  __/\ V  V /_____| (_| | (_| |  __/ | |_| | |_| | |  | |_| |
    |_| \_|\___| \_/\_/       \__,_|\__, |\___|  \____|\__,_|_|   \__,_|
                                    |___/

    You are chatting with the persona named: New-age Guru

    This persona is inspired by Conversations with Chris Holmes
    This persona is designed by Chris Holmes and Harper Reed

    type `quit` to quit
    ========================================================================

    Please ask me a question

    Q: Why are humans so full of pain?
    A: Because it is our most powerful energy

you can change which persona it is using by passing the `-p` argument

    $ python3 cli.py -p space
    ____                          ____  __
    / ___| _ __   __ _  ___ ___   / /  \/  | ___   ___  _ __
    \___ \| '_ \ / _` |/ __/ _ \ / /| |\/| |/ _ \ / _ \| '_ \
    ___) | |_) | (_| | (_|  __// / | |  | | (_) | (_) | | | |
    |____/| .__/ \__,_|\___\___/_/  |_|  |_|\___/ \___/|_| |_|
          |_|

    You are chatting with the persona named: Space/Moon

    This persona is inspired by Space and Moon law
    This persona is designed by @Angeliki Kapoglou and Harper Reed

    type `quit` to quit
    ========================================================================

    Please ask me a question

    Q: what jurisdiction is the  moon in?
    A: According to the 1967 Outer Space Treaty, the Moon and other celestial 
    bodies are “not subject to national appropriation by claim of sovereignty, 
    by means of use or occupation, or by any other means.” No entity (national 
    or otherwise) can claim ownership of the Moon.

## how to run the web interface

Same as the cli: 

`python3 web.py`

or if you want to specify a persona use

`python3 web.py -p space`

Works super well with `ngrok` or the like.  

**This is not meant to be a public facing product. If you want to make it public, please be responsible. Also remember to talk to openAI before you deploy anything into "production".**

# yay

## Lot's of TODOs here.

* Better handling when there isn't a good response.
* Better handling of repeating responses
* More personas
  * Doctor?
  * Dungeon master
  * More politicians?
  * Plato? lol
  
  
---

# thanks 

Thanks to [@gdb](https://github.com/gdb) and team for the awesome API. It is really amazing and has been loads of fun. 

Can't wait to see how it turns out
