import streamlit as st
import qrcode
from io import BytesIO
import pandas as pd

st.set_page_config(
    page_title="调查问卷",
    page_icon="icon.jpg",
    layout="wide"
)
st.title("五四运动对新时代中国青年的影响调研")

st.header("一、基础认知类")
q1 = st.radio("1. 您是否了解五四运动的具体发生时间和主要历史事件？", ["是", "否"], index=None)
q2 = st.radio("2. 您认为五四运动的核心精神内涵（爱国、进步、民主、科学）在当下社会是否依然重要？", ["是", "否"], index=None)
q3 = st.multiselect(
    "3. 您通过哪些渠道了解五四运动相关知识？（可多选）",
    ["学校历史课程", "网络媒体（短视频、文章等）", "红色影视作品", "纪念馆、博物馆参观", "长辈讲述", "其他"]
)

st.header("二、精神传承类")
q4 = st.radio(
    "4. 在您看来，新时代中国青年传承五四精神最需要做到哪一点？",
    ["坚定的爱国情怀", "追求进步与创新", "积极参与社会事务", "崇尚科学与理性", "其他"],
    index=None
)
q5 = st.radio(
    "5. 您是否曾参与过与五四精神相关的主题活动（如主题演讲、志愿服务等）？",
    ["经常参与", "偶尔参与", "从未参与"],
    index=None
)
q6 = st.radio(
    "6. 您认为当前学校或社会开展的五四精神宣传教育活动效果如何？",
    ["非常有效，印象深刻", "效果一般，流于形式", "几乎没有作用"],
    index=None
)

st.header("三、行为影响类")
q7 = st.radio(
    "7. 当国家利益或民族尊严受到损害时，您会采取什么行动？",
    ["在网络上发声，表达立场", "参与相关主题活动，如签名声援等", "从自身做起，做好本职工作来贡献力量", "不太关注，觉得与自己无关"],
    index=None
)
q8 = st.multiselect(
    "8. 在学习或工作中遇到困难时，五四精神中的哪些理念会激励您克服困难？（可多选）",
    ["不畏艰难、勇往直前", "敢于突破传统、创新思维", "团结协作、共同奋斗", "其他"]
)
q9 = st.radio(
    "9. 您是否愿意为社会公益事业或志愿服务贡献自己的时间和精力？",
    ["非常愿意，经常参与", "愿意，但时间有限", "不太愿意"],
    index=None
)
q10 = st.radio(
    "10. 您在职业规划中，是否会考虑将个人发展与国家发展需求相结合？",
    ["会，这是重要考量因素", "偶尔会考虑", "不会考虑"],
    index=None
)

st.header("四、社会环境类")
q11 = st.radio(
    "11. 您认为当前社会氛围对五四精神的弘扬起到了怎样的作用？",
    ["大力推动，营造了良好氛围", "作用一般，重视程度不足", "几乎没有促进作用"],
    index=None
)
q12 = st.radio(
    "12. 您身边的同龄人对五四精神的关注和传承情况如何？",
    ["普遍很重视，积极践行", "部分人重视，存在差异", "很少有人关注"],
    index=None
)
q13 = st.radio(
    "13. 您认为媒体在传播五四精神方面做得怎么样？",
    ["宣传形式丰富，效果显著", "宣传内容单一，缺乏吸引力", "很少进行相关宣传"],
    index=None
)

st.header("五、自我反思类")
q14 = st.radio(
    "14. 您觉得自己在传承五四精神方面做得如何？",
    ["做得很好，积极践行", "一般，还有提升空间", "做得较差，有待加强"],
    index=None
)
q15 = st.multiselect(
    "15. 您认为阻碍自己更好传承五四精神的因素有哪些？（可多选）",
    ["学业/工作压力大，无暇顾及", "缺乏相关实践机会", "对五四精神理解不够深入", "社会环境影响", "其他"]
)
q16 = st.multiselect(
    "16. 您希望通过哪些方式加深对五四精神的理解和传承？（可多选）",
    ["参加主题讲座、培训", "实地参观红色教育基地", "开展主题实践活动", "阅读相关书籍、文献", "其他"]
)

q17 = st.radio(
    "17. 您认为五四精神在未来 5 - 10 年对中国青年的影响力会如何变化?",
    ["影响力持续增强", "保持现状", "影响力逐渐减弱"],
    index=None
)

q18 = st.multiselect(
    "18. 您希望新时代中国青年以怎样的方式传承和发扬五四精神？（可多选）",
    ["立足本职，在工作学习中践行", "积极参与社会变革与发展", "加强文化传播，让更多人了解", "其他"]
)
q19 = st.radio(
    "19. 您是否愿意成为五四精神的传播者和践行者，带动身边人共同传承？",
    ["非常愿意", "视情况而定", "不愿意"],
    index=None
)
q20 = st.text_area(
    "20. 对于如何更好地发挥五四运动精神对新时代中国青年的引领作用，您还有哪些建议？"
)

# 提交时写入 CSV 文件
if st.button("提交"):
    data = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5, "q6": q6, "q7": q7, "q8": q8, "q9": q9, "q10": q10,
            "q11": q11, "q12": q12, "q13": q13, "q14": q14, "q15": q15, "q16": q16, "q17": q17, "q18": q18, "q19": q19, "q20": q20}
    try:
        df = pd.read_csv('survey.csv')
        new_df = pd.DataFrame([data])
        df = pd.concat([df, new_df], ignore_index=True)
    except FileNotFoundError:
        df = pd.DataFrame([data])
    df.to_csv('survey.csv', index=False)
    st.success("感谢您的填写！")

# 显示历史内容（表格形式）
try:
    df = pd.read_csv('survey.csv')
    st.info(f"num:{len(df)}")
    st.dataframe(df)
except FileNotFoundError:
    st.write("暂无历史填写内容。")

# 生成二维码
st.divider()
st.subheader("手机扫码填写问卷")
qr_url = "https://wenjuan-olbeuwobukyaqevjnfwfup.streamlit.app/"
qr = qrcode.make(qr_url)
buf = BytesIO()
qr.save(buf)
st.image(buf.getvalue(), caption="问卷二维码，手机扫码填写", width=200)


