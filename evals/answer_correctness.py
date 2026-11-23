from app.answer import ask_question
import json

with open(r'evals/test_set.json','r',encoding='utf-8') as file:
    data=json.load(file)

complete_list=[]

for d in data:
    que=d.get('question')
    q_id=d.get('id')

    answer=ask_question(que)
    check_data={'id':q_id,
        'question':que,
        'answer':answer
        }
    complete_list.append(check_data)
    print(f'question {q_id} completed....')


with open("./evals/answers.json", "w",encoding='utf-8') as file:
    json.dump(complete_list,file,indent=4)
