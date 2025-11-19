import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)



# 앱 제목
st.title("기분에 맞는 노래를 들어봐요🎧🎶")

# 재료 입력 받기
song = st.text_input("오늘 당신의 기분은 어떠한가요?")

# 재료 출력
if st.button("어울리는 노래 찾기"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": song,
            },
            {
                "role": "system",
                "content": "위에서 입력받은 기분에 어울리는 노래를 찾아줘"
            }
        ],
        model ="gpt-4o",
    )
    response = client.images.generate(
        model="dall-e-3",
        prompt=food,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    # 재료 입력 받기
number = st.text_input("듣고 싶은 노래의 번호를 적어주세요.")

# 재료 출력
if st.button("확인"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": number,
            },
            {
                "role": "system",
                "content": "위에서 입력받은 번호에 해당하는 노래를 찾아서 뮤직비디오를 보여줘"
            }
        ],
        model ="gpt-4o",
    )
    response = client.images.generate(
        model="dall-e-3",
        prompt=number,
        size="1024x1024",
        quality="standard",
        n=1,
    )
     
    
    result = chat_completion.choices[0].message.content
    st.write(result)
