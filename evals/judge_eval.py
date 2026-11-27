from app.models import judge
import time
import json


with open(r'evals/test_set.json','r',encoding='utf-8') as file:
    data=json.load(file)

with open(r'evals/answers.json','r',encoding='utf-8') as file:
    llm_data=json.load(file)


actual_data=[]
llm_answers=[]
reviews=[]

for d in data:
    que_type=d.get('type')
    question=d.get('question')
    actual_answer=d.get('answer')
    que_id=d.get('id')

    actual_data.append([que_type,question,actual_answer,que_id])

for l in llm_data:
    generated_answer=l.get('answer').get('answer')

    llm_answers.append(generated_answer)

for i in range(len(actual_data)):

    if actual_data[i][0]!='not_in_docs':

        current_data=actual_data[i]
        current_answer=llm_answers[i]

        prompt=f'''You are a strict grader for a medical question answering system.

                    Question: {current_data[1]}
                    Correct answer: {current_data[2]}
                    Bot answer: {current_answer}

                    Rules:
                    - Mark CORRECT only if the bot answer means the same as the correct answer.
                    - All numbers, doses and units must match exactly. A changed or missing number is INCORRECT.
                    - Different wording is fine.
                    - If the bot answer says "Not found in sources", mark INCORRECT, because the answer exists in the documents.
                    - Extra detail is fine, but extra wrong detail that changes the meaning is INCORRECT.

                    Write one short reason. On the last line write only CORRECT or INCORRECT.'''

        review=judge.invoke(prompt).content
        reviews.append((current_data[3],review))

        print(f'{current_data[3]}-->{review}')
        time.sleep(20)

        with open("evals/judgement.json", "w", encoding="utf-8") as file:
            json.dump(reviews, file, indent=4, ensure_ascii=False)