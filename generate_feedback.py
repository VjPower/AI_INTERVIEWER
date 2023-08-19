#USGAE


#python generate_feedback.py <file name> 


import openai
from dotenv import load_dotenv
import os 
import sys
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
file_name=sys.argv[1]

def get_chat_completion(iContent):
    conv_list=[{"role":"system", "content":f'''You are the world's best interviewer. The model will be given an interview transcript between interviewer and candidate. Based on job profile given in the title, evaluate candidate and rate the candidate on communications ,technical skills, practical skills and attitude. Give the answer in points and describe each point with the rating. For eg:

Attitude: Rating out of 10
Confidence: Rating out of 10
Technical Skills:  Rating out of 10
Practical skills: Rating out of 10

Give Overall rating and verdict for if the candidate has to be considered for next round along with above ratings \n
                {iContent}'''}]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conv_list,
        temperature=0,  
        # max_tokens=50,    
        # frequency_penalty=0.5,  
        # presence_penalty=0.2,  
    )
    return response['choices'][0]['message']['content'].strip()


if __name__=="__main__":
    with open(f"{file_name}","r") as file:
        iContent=file.read()
        file_name= file_name.replace('.txt','')
    answer= get_chat_completion(iContent)
    with open(f'{file_name}_REVIEW.txt','w') as file:
        file.write(answer)
