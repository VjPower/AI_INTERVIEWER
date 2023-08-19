#USAGE 

#1st line: Job Profile For Eg. (Backend Engineer on Django, Python)
#2nd line: <Years of Experience>

import openai
from dotenv import load_dotenv
import os 

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_chat_completion(conv_list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conv_list,
        temperature=1.3,  
        # max_tokens=50,    
        # frequency_penalty=0.5,  
        # presence_penalty=0.2,  
    )
    return response['choices'][0]['message']['content'].strip()


if __name__=="__main__":
    yoe=int
    difficulty=str
    mapping={"1":"EASY","2":"MEDIUM","3":"UPPER MEDIUM","4":"HARD","5":"VERY HARD"}

    while True:
        print("Enter Job profile ")
        prompt=input("Job Profile: ")
        yoe=input("Enter years of experience: ")
        if int(yoe)<6:
            difficulty=mapping[str(yoe)]
        else:
            difficulty="EXTREMELY HARD"
        conv_list=[{"role":"system", "content":f"Your job is to generate technical interview questions based on a job requirement. These questions will be of difficulty: {difficulty}. Recommend questions based on these details. "}]
        conv_list.append({"role":"user","content":str(prompt)})
        answer= get_chat_completion(conv_list)
        print(answer)