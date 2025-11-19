import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)



# 앱 제목
st.title("맛집 홍보 포스터 제작")

# 재료 입력 받기
food = st.text_input("어떤 음식을 홍보하고 싶으신가요?")

# 재료 출력
if st.button("홍보문구 및 포스터 제작"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": food,
            },
            {
                "role": "system",
                "content": "위에서 입력받은 음식의 홍보 문구를 간략하게 작성해줘"
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
    
    
    result = chat_completion.choices[0].message.content
    image_url = response.data[0].url
    
    st.write(result)
    st.image(image_url)
