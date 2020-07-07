import sys

sys.path.append(".")

import streamlit as st
import SessionState

from models.lstm_model import LSTMModel

st.title("LSTM for sentiment analysis")

reviews = []

lstmModel = LSTMModel()

# x_train, x_test = lstmModel.importData([],[])
state = SessionState.get(key=0)

email = st.text_input("Enter your email here")

text1 = st.empty()
text2 = st.empty()
text3 = st.empty()
text4 = st.empty()
text5 = st.empty()

value = ''
if st.button('Reset', key="s2"):
    state.key += 1
    val = 'o'
    
r1 = text1.text_area("here's my text", value='p', key="t1")
r2 = text2.text_area("Here's my text2", value=value, key="t2")
r3 = text3.text_area("Here's my text3", value=value, key="t3")
r4 = text4.text_area("Here's my text4", value='', key="t4")
r5 = text5.text_area("Here's my text5", value='', key="t5")

if st.button("Submit", key="s2"):
    
    if r1 and r1 != "deafult value" and reviews.count(r1) == 0:
        reviews.append(r1)
    
    if r2 and r2 != "deafult value" and reviews.count(r2) == 0:
        reviews.append(r2)
    
    if r3 and r3 != "deafult value" and reviews.count(r3) == 0:
        reviews.append(r3)
    
    if r4 and r4 != "deafult value" and reviews.count(r4) == 0:
        reviews.append(r4)
    
    if r5 and r5 != "deafult value" and reviews.count(r5) == 0:
        reviews.append(r5)
    value = ""

st.write(reviews)

#userReview = st.text_area("Enter your review here to detect emotion of it")
#st.slider("Rate your review", 0.0, 1.0, 0.5)
# userReview = "great movie"

if email and reviews:

    from dbops.operations import *
    with app.app_context():
        data = get_review_details(email, reviews)
        st.write(data)
    
    
    # reviews.append(userReview)
    # max_features = 47000
    # max_doc_len = 220
    # temp = []
    # model = lstmModel.loadModel()
    # temp, reviews = lstmModel.preProcessData(temp, reviews)
    # temp, reviews = lstmModel.encodeData(max_features, max_doc_len, temp, reviews)
    # result = lstmModel.predict(model, reviews)
    # print(result)
    # st.write("Emotion is ", result)

    
