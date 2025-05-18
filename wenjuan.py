import streamlit as st
import qrcode
from io import BytesIO

st.title("调查问卷示例")

st.write("请填写以下问卷：")

name = st.text_input("1. 你的姓名：")
age = st.number_input("2. 你的年龄：", min_value=1, max_value=120, step=1)
gender = st.radio("3. 你的性别：", ["男", "女", "其他"])
hobby = st.multiselect("4. 你的兴趣爱好：", ["阅读", "运动", "音乐", "旅行", "美食", "其他"])
feedback = st.text_area("5. 你对本问卷的建议：")

if st.button("提交"):
    st.success("感谢你的填写！")
    st.write("你的答卷：")
    st.write(f"姓名：{name}")
    st.write(f"年龄：{age}")
    st.write(f"性别：{gender}")
    st.write(f"兴趣爱好：{', '.join(hobby)}")
    st.write(f"建议：{feedback}")

# 生成二维码
st.divider()
st.subheader("手机扫码填写问卷")
qr_url = "https://xxxx.ngrok.io"  # 用ngrok生成的公网地址
qr = qrcode.make(qr_url)
buf = BytesIO()
qr.save(buf)
st.image(buf.getvalue(), caption="问卷二维码，手机扫码填写", width=200)