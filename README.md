# gpt3-persona-bot
a simple bot that allows you to chat with various personas

You will need a key. 

## how to run

    harper@ {~/openai/bot}$ pip3 install -r requirements.txt
    harper@ {~/openai/bot}$ export OPENAI_API_KEY=
    harper@ {~/openai/bot}$ python3 persona_bot.py
    You are speaking to the persona named: space

    type `quit` to quit
    ========================================================================
    Please ask me a question

    Q: Do you think we will settle on mars?
    A: I think we will settle on the Moon, but I’m not sure we’ll be able to settle on
    Mars. We’ll certainly send people to Mars, and we’ll probably find out a lot about
    Mars that will be of interest to us, but the challenges are so great that I don’t 
    think we’ll be able to stay. I’m not sure that we will be able to settle the Moon, 
    either


# yay

## Lot's of TODOs here. 

* Better handling when there isn't a good response.
* Better handling of repeating responses
* Break the prompts into JSON Q/A pairs and then merge in prompt building
  * Allows for some meta data and source data in persona generation
  * Can have "names" 
  * can put model tweaks directly in personas
* Maybe some easier hooks into various chat apps
* More personas
  * Doctor?
  * Dungeon master
  * More politicians?
  * Plato? lol
  
