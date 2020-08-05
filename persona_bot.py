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
        root = pathlib.Path(__file__).parent.resolve()

        self.logger.info("Setting persona to "+ persona_name)
        self.persona_path = root / "personas"

        self.load_persona(persona_name)

    def load_persona(self,  persona):
        self.logger.info("Loading prompt")
        prompt_filename = self.persona_path / str(persona+ ".json")
        self.logger.debug("Promp filename: " + str(prompt_filename))

        if (prompt_filename.exists()):
            with open(prompt_filename) as f:
                prompt_text = f.read()
                persona = json.loads(prompt_text)
                
                self.prompt = self.build_prompt(persona['qa_pairs'])
                
                del  persona['qa_pairs']
                self.persona = persona
                self.temperature = self.persona['tune']['temperature']
                self.top_p = self.persona['tune']['top_p']
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

    def change_persona(self, persona):
        self.load_persona(persona)
    




if __name__ == "__main__":
    persona = "space"
    bot = persona_bot(persona_name=persona, log_level=logging.DEBUG)
    print(bot.persona)
    response = bot.ask("Are their laws for the moon??")
    print(response)
    bot.change_persona("guru")
    print(bot.persona)
    response = bot.ask("Why are humans like this?")
    print(response)
    
