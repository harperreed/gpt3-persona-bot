import openai
import pathlib

class openai_bot:

    engine = "davinci"
    stop_sequence = "\n\n"
    restart_sequence = "\n\nQ: " #TBD
    start_sequence = "\nA: "
    temperature = 0.6
    max_tokens = 100
    top_p = 1
    persona_path = "./personas/"
    
    

    def __init__(self, openai_key=None, persona="guru"):
        self.openai = openai
        if openai_key:
            self.openai_key = openai_key
        self.persona = persona
        root = pathlib.Path(__file__).parent.resolve()
        self.persona_path = root / "personas"
        self.load_prompt()

    def load_prompt(self):
        prompt_filename = self.persona_path / str(self.persona + ".md")

        if (prompt_filename.exists()):
            with open(prompt_filename) as f:
                self.prompt = f.read()
        else:
            raise Exception('Persona not available')

    def merge_question(self, question):
        return self.prompt + question

    def completion(self, prompt):
        completion_result = self.openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            stop=self.stop_sequence
            )
        
        return self.clean_result(completion_result)
    
    def clean_result(self, result):
        str_result = result['choices'][0]['text'].replace(self.start_sequence,"")
        return str_result
        

    def ask(self, question):
        prompt = self.merge_question(question)
        return self.completion(prompt)

    def chat(self):
        # Largely from: https://github.com/jezhiggins/eliza.py
        print()
        print("You are speaking to the persona named:", self.persona )
        print()
        print("type `quit` to quit")
        print('='*72)
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
                break
            response = self.ask(s)
            print("A:", response)
            print()



if __name__ == "__main__":
    persona = "space"

    bot = openai_bot(persona=persona)
    bot.chat()
    
    #response = bot.ask("Where are the bananas?")
    #print(response)
