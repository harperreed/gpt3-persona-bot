from persona_bot import persona_bot
import argparse
import pyfiglet
import sys

def main():

    def chat(bot):
            # Largely from: https://github.com/jezhiggins/eliza.py
            print(pyfiglet.figlet_format(bot.persona['name']))
            print("You are chatting with the persona named:", bot.persona['name'] )
            print()
            print("This persona is inspired by", bot.persona['inspired_by'] )
            print("This persona is designed by", bot.persona['designed_by'] )
            print()
            print("type `quit` to quit")
            print('='*72)
            print()
            print('Please ask me a question')
            print()

            s = ''
            while s != 'quit':
                try:
                    s = input('Q: ')
                except EOFError:
                    s = 'quit'
                    print(s)
                if (s=='quit' or s==''):
                    raise Exception('Exiting chat. Thank you for chattign with the '+ bot.persona['name'] + ' persona')
                    break
                response = bot.ask(s)
                print("A:", response)
                print()

    

    parser = argparse.ArgumentParser(description=None)

    parser.add_argument("-p", "--persona", default="guru")
    args = parser.parse_args()
    persona = args.persona
    bot = persona_bot(persona_name=persona)
    chat(bot)



if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as  e:
        print(e)

