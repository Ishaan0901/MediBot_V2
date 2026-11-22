from app.answer import ask_question
import json

not_found_variants = [
    "not found in sources",
    "not found in the sources",
    "not found in source",
    "the answer is not found in the sources",
]

with open(r'evals/test_set.json','r',encoding='utf-8') as file:
    data=json.load(file)

count=0
total=0
for d in data:
    que_type=d.get('type')
    que=d.get('question')
    

    if que_type=='not_in_docs':
        answer=ask_question(que).get('answer')
        check_ans=answer.lower().strip('. ')

        total+=1

        if check_ans in not_found_variants:
            print(f'{que} -> not found')
            count+=1
        else:
            print(f'{que}--->{answer}')
per=(count/total)*100

print(f'\n============Total not found:{count}===============')
print(f'===============percentage:{per}===========')