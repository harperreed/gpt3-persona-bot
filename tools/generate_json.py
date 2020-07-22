import json
import argparse
import pathlib
import sys


def main():
    

    parser = argparse.ArgumentParser(description=None)

    parser.add_argument("-f", "--interview_file",  required=True)

    args = parser.parse_args()



    interview_text_filename = pathlib.Path(args.interview_file)
    if not interview_text_filename.exists ():
        raise Exception('Interview file not available: ' + str(interview_text_filename)) 

    interview_file_name = pathlib.Path(str(interview_text_filename).replace(".txt",".json"))

    if interview_file_name.exists ():
        raise Exception('Destination Interview file already exists: ' + str(interview_file_name)) 

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
        "designed_by": "",
        "sources":["http://beta.openai.com"],
        "tune":{
            "temperature": 0.9,
            "top_p": 0
        },
        "qa_pairs": qas
    }


    with open(interview_file_name, "w" ) as f:
        f.write(json.dumps(persona, sort_keys=True,  indent=4))



if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as  e:
        print(e)
