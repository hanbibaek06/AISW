import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)



# 앱 제목
st.title("오늘의 노래를 들어봐요🎧🎶")

# 재료 입력 받기
song = st.text_input("오늘 당신의 기분은 어떠한가요?")

feeling = st.select_slider(
    "그 기분의 정도를 알려주세요!",
    options=[
        f"아주 조금 {song}함",
        f"조금 {song}함",
        f"적당히 {song}함",
        f"매우 {song}함"
    ],
)
st.write("지금 내 기분의 정도는", feeling)
        
        

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
                "content": "위에서 입력받은 기분에 어울리는 노래를 5개 찾아주고, 해당 뮤직비디오나 노래영상을 각각 하나씩 나타내줘"
            }
        ],
        model ="gpt-4o",
    )
    response = client.images.generate(
        model="dall-e-3",
        prompt=song,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    
    result = chat_completion.choices[0].message.content
    st.write(result)





