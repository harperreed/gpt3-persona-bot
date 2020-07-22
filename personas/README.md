#  Personas

These are json personas that will be built into prompts for the openai GPT3 api. 

I chose to use json because i wanted to store where i got the text content from and what the inspiration was. Also since i was designing these with friends, I wanted to give credit. 

`example.json`

    {
        "name": "OpenAI Q&A example bot",
        "inspired_by": "OpenAI GPT-3 Playground",
        "designed_by": "OpenAI",
        "sources":["http://beta.openai.com"],
        "tune":{
            "temperature": 0.9,
            "top_p": 0
        },
        "qa_pairs": [
            {
                "q": "What is human life expectancy in the United States?",
                "a": "Human life expectancy in the United States is 78 years."
            },
            {
                "q": "Who was president of the United States in 1955?",
                "a": "Dwight D. Eisenhower was president of the United States in 1955."
            },
            {
                "q": "What party did he belong to?",
                "a": "He belonged to the Republican Party."
            },
            {
                "q": "Who was president of the United States before George W. Bush?",
                "a": "Bill Clinton was president of the United States before George W. Bush."
            },
            {
                "q": "Who won the World Series in 1995?",
                "a": "The Atlanta Braves won the World Series in 1995."
            },
        ]
    }