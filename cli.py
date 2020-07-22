from persona_bot import persona_bot

if __name__ == "__main__":
    persona = "space"

    bot = persona_bot(persona=persona)
    bot.chat()
    
    #response = bot.ask("Where are the bananas?")
    #print(response)
