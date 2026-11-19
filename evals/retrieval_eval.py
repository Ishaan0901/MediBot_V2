from app.answer import retriever
import json

with open(r'evals/test_set.json','r',encoding='utf-8') as file:
    data=json.load(file)

match_count=0
total_ques=0
missed_ids=[]


for d in data:
    que=d.get('question')
    source_file=d.get('source_file')        #source file for that particular question as mentioned in json file
    loader_page=d.get('loader_page')        #page number for that particular question as mentioned in json file
    que_type=d.get('type')
    json_tup=(source_file,loader_page)

    if que_type=='answerable' or que_type=='trap':

        total_ques+=1
        check_list=[]

        context=retriever.invoke(que)
        for c in context:
            source=c.metadata.get('source').replace('data/','')
            page=c.metadata.get('page')
            check_list.append((source,page))

        if json_tup in check_list:
            print(f"FOUND for (id:{d.get('id')})")
            match_count+=1
        else :
            print(f"NOT FOUND for (id:{d.get('id')})")
            missed_ids.append(d.get('id'))

