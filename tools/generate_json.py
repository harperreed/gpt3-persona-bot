import json

interview_text_filename = "example_interview.txt"
interview_file_name = interview_text_filename.replace(".txt",".json")

with open(interview_text_filename) as f:
    md = f.read()

md = md.split("\n\n")
qas =[]

for e in md:
    qat = e.replace("Q: ","").split("\nA: ")
    qa = {}
    qa['q']=qat[0]
    qa['a']=qat[1]
    qas.append(qa)


persona = {
    "name": "OpenAI Q&A ",
    "inspired_by": "",
    "sources":["http://beta.openai.com"],
    "tune":{
        "temperature": 0.9,
        "top_p": 0
    },
    "qa_pairs": qas
}


with open(interview_file_name, "w" ) as f:
   f.write(json.dumps(persona))