import openai
import pathlib
import logging
import json

class persona_bot:

    engine = "davinci"
    stop_sequence = "\n\n"
    restart_sequence = "\n\nQ: " #TBD
    start_sequence = "\nA: "
    temperature = 0.6
    max_tokens = 100
    top_p = 1
    persona_path = "./personas/"
    
    

    def __init__(self, openai_key=None, persona_name="guru", log_level=logging.WARN):
        self.openai = openai
        logging.basicConfig(level=log_level)
        self.logger = logging.getLogger(__name__)
        if openai_key:
            self.openai_key = openai_key
        self.persona_name = persona_name
        root = pathlib.Path(__file__).parent.resolve()
        self.persona_path = root / "personas"

        self.load_persona()

    def load_persona(self):
        self.logger.info("Loading prompt")
        prompt_filename = self.persona_path / str(self.persona_name + ".json")
        self.logger.debug("Promp filename: " + str(prompt_filename))

        if (prompt_filename.exists()):
            with open(prompt_filename) as f:
                prompt_text = f.read()
                persona = json.loads(prompt_text)
                
                self.prompt = self.build_prompt(persona['qa_pairs'])
                del  persona['qa_pairs']
                self.persona = persona
        else:
            raise Exception('Persona not available')

    def build_prompt(self, qa_pairs):
        prompt = ""
        
        for qa in qa_pairs:
            prompt = prompt + "Q: "+ qa["q"]  + "\n"
            prompt = prompt + "A: "+ qa["a"] + "\n\n"
        prompt = prompt + "Q: "
        return prompt

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
        self.logger.debug("Answer: " + str_result)
        return str_result
        

    def ask(self, question):
        self.logger.debug("Question: " + question)
        prompt = self.merge_question(question)
        return self.completion(prompt)

    




if __name__ == "__main__":
    persona = "space"
    bot = persona_bot(persona_name=persona, log_level=logging.INFO)
    print 
    response = bot.ask("Are my feelings real?")
    print(response)
    print(bot.persona)
