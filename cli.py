from persona_bot import persona_bot

if __name__ == "__main__":
    persona = "benhuh"

    bot = persona_bot(persona_name=persona)
    bot.chat()
    
    #response = bot.ask("Where are the bananas?")
    #print(response)
