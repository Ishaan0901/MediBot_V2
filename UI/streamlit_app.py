import streamlit as st
from app.answer import ask_question

not_found_variants = [
    "not found in sources",
    "not found in the sources",
    "not found in source",
    "the answer is not found in the sources",
]

st.title("MediBot 2.0")
st.subheader('Scope:')
st.markdown(''' 
MediBot answers only from these 4 PDFs: WHO Guideline for the pharmacological treatment of hypertension in adults (2021), MSF Clinical Guidelines, MSF Essential Drugs, and Hesperian “Where There Is No Doctor” (2009 edition). Topics include high blood pressure treatment, diarrhoea, snakebite, tetanus, rabies, some drug doses, and basic home care. If the answer is not in these documents, it replies “Not found in sources.”
''')
st.subheader('Example Questions:')
st.markdown('''
1. At what blood pressure does WHO say drug treatment should start?
2. What daily salt intake does WHO recommend for people with hypertension?
3. How is acute diarrhoea defined in the MSF clinical guidelines?
4. Do tourniquets and cutting or sucking the wound help after a snake bite?
5. How much clean water is one ORS sachet mixed into?
''')
st.error('Disclaimer : For Educational Purpose only, not medical advice.')

que=st.chat_input('enter the question here...')
if que: 
    response=ask_question(que)

    answer=response.get('answer')

    st.subheader('Question:')
    st.markdown(que)

    st.subheader('answer:')
    st.markdown(answer)


    if answer.lower().strip('. \n') not in not_found_variants:
    
        st.subheader('Content Retrieved from :')
        sources_list=response.get('sources')
        for s in sources_list:
            source=s.get('source')
            page=s.get('page_number')

            # st.markdown(f'Source:{source}... Page Number: {page}')