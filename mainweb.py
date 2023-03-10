# -*- coding: UTF-8 -*-
import streamlit as st
import pandas as pd
import numpy as np 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
tab2, tab3 = st.tabs([ "Student mark prediction", "VARK"])

def load_Student_data():
    return pd.read_excel('Student.xlsx')

def save_model(model):
    joblib.dump(model, 'model_student.joblib')

def load_model():
    return joblib.load('model_student.joblib')


with tab2:

    st.subheader('Student mark prediction') 
    col1,col2 = st.columns(2)
    #Creating Button
    Start = col1.button('ทำการสร้างข้อมูล')
    Load = col2.button('ทำการแสดงผลข้อมูล')
    Train = col1.button('ทำการฝึกฝนข้อมูล')
    Predict = col2.button('ทำการคาดคะเนข้อมูล')

    #input data
    courses = st.slider('คุณลงวิชาเรียนไปทั้งหมดกี่วิชา',0,10,5)
    Mark = st.number_input("กรุณาระบุคะแนนเฉลี่ยของคุณ")
    
    #Generating model(Create model)
    if Start:
        data = pd.read_csv('Student_Marks.csv')
        df = pd.DataFrame(data)
        df.to_excel('Student.xlsx') 
    
    #Loading model
    if Load:
        load_data = load_Student_data()
        pd.DataFrame(load_data)
        load_data=load_data.drop(columns="Unnamed: 0",axis=1)
        # st.markdown(load_data.keys())
        st.write(load_data.head(10))

    #Training model
    if Train:
        data = pd.read_csv('Student_Marks.csv')
        df = pd.DataFrame(data)
        X = df.drop(columns= 'time_study',axis= 1)
        y = df['time_study']
        x_train,x_test,y_train,y_test = train_test_split(X,y,test_size= 0.2)
        model = LinearRegression()
        model.fit(x_train,y_train) 
        save_model(model)  

    #prediction model
    if Predict: 
        model = load_model()
        input_data = (courses,Mark)
        array_data = np.asarray(input_data)
        c = array_data.reshape(1,-1)
        predict_result = model.predict(c) 
        result = int(predict_result[0]) 
        st.info(f'เวลาที่คุณควรใช้ในการเรียนคือ : {result}') 
        
        st.success(f'คุณต้องใช้เวลาประมาณ {int(result)/int(courses)} ต่อหนึ่งคาบ')


with tab3:
    st.info('Fleming, N.D. and Mills, C. (1992) แบ่งสไตล์การเรียนรู้ตามความความชอบหรือความถนัดในการรับข้อมูลไว้ 4 กลุ่ม โดย เรียกชื่อการแบ่งกลุ่มนี้ว่า VARK Model หรือ VARK Learning Styles')
    
    V,A,R,K = st.columns(4)
    
    V_B = V.button('V')
    A_B = A.button('A')
    R_B = R.button('R')
    K_B = K.button('K')
    
    
    if V_B:
        st.text('V = Visual รูปแบบการเรียนรู้ที่สื่อด้วยภาพและสัญลักษณ์')
        st.info('ไม่เพียงแต่ภาพเท่านั้นที่คนรักการเรียนรู้รูปแบบนี้ชื่นชอบ แต่พวกเขายังสามารถมองเห็นข้อมูลต่างๆ ในรูปแบบแผนที่ แผนผัง แผนภาพ กราฟ แผนภูมิ และลูกศรสัญลักษณ์ต่างๆ อีกด้วย และสิ่งเหล่านี้ ก็ดีกว่าการบอกเล่าเป็นคำพูดหรือลายลักษณ์อักษร')
        st.text('ชอบทำงานหรืออ่านหนังสือในบรรยากาศที่เงียบสงบ \nชอบวางแผนก่อนลงมือทำ\nอ่านและทำความเข้าใจกับแผนที่ แผนภูมิ และภาษาสัญลักษณ์ได้ดี\nชอบเห็นภาพรวมก่อนที่จะเจาะลึกลงในรายละเอียด\nชอบสีสันและสามารถจำแนกแยกแยะสิ่งต่างๆ จากรูปลักษณ์และสีสัน\nสามารถจำลองเรื่องราว ลำดับเหตุการณ์ และขั้นตอนต่างๆ ที่ได้เห็น เป็นภาพหรือแผนภาพในสมอง') 
    if A_B:
        st.text('A = Aural / Auditory รูปแบบการเรียนรู้ที่สื่อด้วยเสียง')
        st.info('รูปแบบที่รับรู้ข้อมูลผ่านโสตประสาท หรือผ่านการได้ยินได้ฟัง ผู้ที่มีสไตล์การเรียนรู้แบบนี้จะชื่นชอบการฟังบรรยาย ฟังเทป การสนทนากลุ่มย่อย การพูดคุยทางโทรศัพท์ แม้แต่การพูดคุยกับตัวเอง หรือคิดออกมาดังๆ เพื่อเรียบเรียงความคิด และหาคำตอบให้กับเรื่องที่ครุ่นคิดอยู่ขณะนั้น ดังนั้น จึงไม่ใช่เรื่องแปลกที่จะเห็นคนกลุ่มนี้พูดคนเดียว หรือพูดกับหนังสือในมือ เพราะกำลังใช้ความคิดผ่านการพูด')
        st.text('ชอบอ่านออกเสียงดัง ๆ\nไม่อายที่จะพูดต่อสาธารณชน\nชอบฟังคำอธิบาย และชอบอธิบาย\nจดจำชื่อคนและสิ่งต่างๆ ได้ดี\nได้ยินและระบุเสียงประกอบฉากที่ได้ยินในภาพยนตร์ได้\nชอบฟังดนตรี\nเรียนภาษาที่สองหรือภาษาต่างประเทศได้ดี\nอ่านช้า ๆ\nอยู่เงียบๆ ไม่ได้นาน\nชอบขึ้นแสดงบนเวที เช่น ละคร ทอล์คโชว์\nปฏิบัติตามคำบอกได้ดี') 
    if R_B:
        st.text('R = Read / write รูปแบบการเรียนรู้ที่สื่อด้วยอักษร')
        st.info('สไตล์การเรียนรู้รูปแบบนี้ชื่นชอบข้อมูลที่เป็นลายลักษณ์อักษร จึงไม่น่าแปลกใจที่นักวิชาการทั้งหลายจะมีลักษณะการเรียนรู้รูปแบบนี้โดดเด่นมาก เพราะเป็นรูปแบบการเรียนรู้ที่เน้นการรับและส่งข้อมูลผ่านการอ่านและการเขียน เห็นได้ชัดว่า ผู้ที่ชื่นชอบสไตล์นี้มักจะพกพาพจนานุกรม, dictionary, power point เอกสารต่างๆ ติดตัวไว้เสมอ และเป็นผู้ใช้อินเตอร์เน็ตตัวเอง')
        st.text('ชอบอ่านทุกสิ่งทุกอย่าง\nพกสมุดโน้ต และปากกาติดตัว (หรือเครื่องบันทึกอื่นๆ เช่น tablet notebook)\nค้นหาข้อมูลบนอินเตอร์เนตเป็นประจำ\nมีพจนานุกรม dictionary อยู่ใกล้ตัวเสมอ\nชอบเล่นกับตัวอักษร เช่น crossword, scrabble\nเขียน diary, logbook หรือ รายการสิ่งที่กระทำในแต่ละวัน\nสะสมตำรา เช่น ตำราทำอาหาร ตำราการออกกายบริหาร ตำราพัฒนาบุคลิกภาพ ฯลฯ\nปฏิบัติตามคำสั่งที่เป็นลายลักษณ์อักษรได้ดี\nชอบเขียนบทความ ความคิดเห็น เรื่องแต่ง สารคดี ฯลฯ')
    if K_B:
        st.text('Kinesthetic รูปแบบการเรียนรู้ที่สื่อด้วยสัมผัสและการกระทำ') 
        st.info('คำจำกัดความของรูปแบบการเรียนรู้รูปแบบนี้คือ การใช้ประสบการณ์และการลงมือปฏิบัติ ไม่ว่าจะเป็นในสถานการณ์จำลองหรือสถานการจริงก็ตาม ถึงแม้ว่าประสบการณ์จะมีผลกระตุ้นการเรียนรู้ทุกรูปแบบก็ตาม แต่สำหรับผู้ที่ชื่นชอบสไตล์การเรียนรู้แบบนี้จะต้องเชื่อมโยงกับความเป็นจริง ไม่ว่าจะเป็นประสบการณ์ตรงส่วนตัว ตัวอย่าง แบบจำลอง การลงมือปฏิบัติ หรือสถานการณ์จำลอง ทั้งนี้รวมถึง การสาธิต การจำลองสถานการณ์ด้วยภาพยนตร์ ละคร หรือกรณีศึกษา')
        st.text('สนุกสนานกับการค้นคว้า ทดลอง ลงมือปฎิบัติ การสาธิต และทัศนศึกษา\nจดจำได้ดีเมื่อมีการใช้อุปกรณ์ สร้างแบบจำลอง และจับต้องสิ่งที่กำลังเรียนรู้\nนั่งอยู่เฉย ๆ นาน ๆ ไม่ได้ ชอบเดินไปมา และเปลี่ยนอิริยาบถบ่อย ๆ\nมีแนวโน้มเป็นนักสะสม\nพูดเร็ว และชอบแสดงท่าทางประกอบ\nชอบเล่นกีฬาหรือเครื่องดนตรี\nชอบเข้าร่วมกิจกรรมต่างๆ มากกว่าเป็นผู้สังเกตการณ์\nปฏิบัติตามการสาธิตได้ดี')