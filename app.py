import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)



# 앱 제목
st.title("나만의 레시피를 소개합니다")

# 재료 입력 받기
food = st.text_input("어떤 재료를 가지고 계십니까?")

# 재료 출력
if st.button("레시피 생성하기"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": food,
            },
            {
                "role": "system",
                "content": "입력받은 재료로 할 수 있는 맛있는 요리 레시피를 알려줘" 
            }
        ],
        model ="gpt-4o",
    )
    result = chat_completion.choices[0].message.content

    st.write(result)
