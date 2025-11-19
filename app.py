import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)



# 앱 제목
st.title("오늘의 노래를 들어봐요🎧🎶")

song = st.text_input("오늘 당신의 기분은 어떠한가요?")

if song:
    feeling = st.select_slider(
    "그 기분의 정도를 알려주세요!",
    options=[
        f"아주 조금 {song}",
        f"조금 {song}",
        f"적당히 {song}",
        f"조금 많이 {song}"
        f"매우 {song}"
    ],
)
st.write("지금 내 기분의 정도는", feeling)

        
if st.button("어울리는 노래 찾기"):
     user_prompt = f"나의 기분은 '{song}'이고, 그 정도는 '{feeling}'이야. 이 감정 상태에 딱 어울리는 노래 5곡을 추천해주고, 유튜브 링크도 함께 줘."
     chat_completion = client.chat.completions.create(
        model ="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "당신은 음악 추천 전문가입니다. 사용자의 기분과 그 강도에 맞춰 상세하게 노래를 추천해주세요."
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
    )

    response = client.images.generate(
                model="dall-e-3",
                prompt=f"{feeling}한 기분을 표현하는 추상적인 앨범 커버 아트", # 프롬프트 구체화
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            # 결과 출력
            image_url = response.data[0].url
            result = chat_completion.choices[0].message.content
            
            st.image(image_url, caption=feeling)
            st.write(result)


