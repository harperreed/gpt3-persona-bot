# Persona Generator

This will take a interview and turn it into a persona with a bit less work than doing it manually

You can take an interview in this format:

`example_interview.txt`

    Q: What is human life expectancy in the United States?
    A: Human life expectancy in the United States is 78 years.

    Q: Who was president of the United States in 1955?
    A: Dwight D. Eisenhower was president of the United States in 1955.

    Q: What party did he belong to?
    A: He belonged to the Republican Party.

    Q: Who was president of the United States before George W. Bush?
    A: Bill Clinton was president of the United States before George W. Bush.

    Q: Who won the World Series in 1995?
    A: The Atlanta Braves won the World Series in 1995.

and turn it into this: 

`example_interview.json`

    {
        "designed_by": "",
        "inspired_by": "",
        "name": "OpenAI Q&A ",
        "qa_pairs": [
            {
                "a": "Human life expectancy in the United States is 78 years.",
                "q": "What is human life expectancy in the United States?"
            },
            {
                "a": "Dwight D. Eisenhower was president of the United States in 1955.",
                "q": "Who was president of the United States in 1955?"
            },
            {
                "a": "He belonged to the Republican Party.",
                "q": "What party did he belong to?"
            },
            {
                "a": "Bill Clinton was president of the United States before George W. Bush.",
                "q": "Who was president of the United States before George W. Bush?"
            },
            {
                "a": "The Atlanta Braves won the World Series in 1995.\n",
                "q": "Who won the World Series in 1995?"
            }
        ],
        "sources": [
            "http://beta.openai.com"
        ],
        "tune": {
            "temperature": 0.9,
            "top_p": 0
        }
    }


It isn't flawless, but it largely works. 

`python3 generate_json.py -f harper-reed.txt`