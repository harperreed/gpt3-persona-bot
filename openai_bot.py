import openai
import pathlib

class openai_bot:

    engine = "davinci"
    stop_sequence = "↵"
    restart_sequence = "↵↵Q:"
    start_sequence = "↵A:"
    temperature = 0.0
    max_tokens = 100
    top_p = 1
    persona_path = "./personas/"
    
    

    def __init__(self, openai_key, persona):
        self.openai = openai
        self.persona = persona
        root = pathlib.Path(__file__).parent.resolve()
        self.persona_path = root / "personas"
        self.load_prompt()

    def load_prompt(self):
        prompt_filename = self.persona_path / str(self.persona + ".md")
        print(prompt_filename)
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
            prompt=self.prompt,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            stop=self.stop_sequence
            )
        print(completion_result['choices'])

    def ask(self, question):
        prompt = self.merge_question(question)
        
        self.completion(prompt)

        return "answer"

if __name__ == "__main__":
    persona = "guru"
    bot = openai_bot(key, persona)
    
    response = bot.ask("Why are we here?")
    print(response)
