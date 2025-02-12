import streamlit as st
from PIL import Image
from transformers import pipeline
from ultralytics import YOLO

tab1, tab2, tab3 = st.tabs(["โรคของทุเรียน", "ตรวจหาโรคของทุเรียน", "AI"])

with tab1:
    # Introduction section
    st.header("เกี่ยวกับทุเรียน")
    st.write("""
    ทุเรียน (Durian) เป็นผลไม้ที่มีชื่อเสียงของไทยและประเทศในภูมิภาคเอเชียตะวันออกเฉียงใต้ โดยมีเนื้อผลที่หวานมัน และมีกลิ่นเฉพาะตัว
    อย่างไรก็ตาม ทุเรียนสามารถประสบกับโรคต่างๆ ที่อาจส่งผลกระทบต่อการเจริญเติบโตและผลผลิตได้
    """)

    # Disease section
    st.header("โรคของทุเรียน")

    # Disease for Leaves
    st.subheader("โรคที่เกิดกับใบ")
    st.write("""
    1. **โรคจุดใบจากสาหร่าย (Algal Leaf Spot)**
    - อาการ: จุดที่เกิดบนใบจะมีลักษณะเป็นสีเขียวหรือสีน้ำตาล
    - การรักษา: ใช้สารเคมี fungicides ลดความชื้น ควบคุมการระบาด

    2. **โรคใบไหม้ (Leaf Blight)**
    - อาการ: ใบเริ่มเน่าเปื่อยจากขอบใบ, แผลเปียกชื้น
    - การรักษา: ใช้สารเคมี fungicides ควบคุมการให้น้ำ ปรับปรุงการระบายอากาศ

    3. **โรคใบลาย (Leaf Spot)**
    - อาการ: ใบมีจุดสีเหลืองหรือสีน้ำตาล ปรากฏเป็นลาย
    - การรักษา: ใช้สารเคมี fungicides ตัดแต่งใบที่ติดเชื้อ และรักษาความสะอาดของสวน
    """)

    # Disease for Tree
    st.subheader("โรคที่เกิดกับต้น")
    st.write("""
    1. **โรคเน่าของต้น (Root Rot Disease)**
    - อาการ: ต้นไม่เจริญเติบโต รากเน่า และใบเริ่มเหี่ยว
    - การรักษา: ใช้สารเคมีที่ช่วยฆ่าเชื้อราในดิน

    2. **โรคต้นเน่า (Trunk Rot)**
    - อาการ: ต้นเริ่มผุเน่าและมีการปล่อยกลิ่นเหม็น
    - การรักษา: ตัดต้นที่ติดเชื้อ และทำการพ่นสารเคมีเพื่อฆ่าเชื้อรา

    3. **โรคใบฝ่อ (Canker Disease)**
    - อาการ: ต้นมีแผลที่เปลือก ต้นฝ่อและแห้ง
    - การรักษา: ใช้สารเคมีที่เหมาะสม และตัดแผลที่ติดเชื้อ
    """)

    # Disease for Root
    st.subheader("โรคที่เกิดกับราก")
    st.write("""
    1. **โรครากเน่า (Root Rot)**
    - อาการ: รากเริ่มเน่าและไม่สามารถดูดน้ำและสารอาหารได้
    - การรักษา: รักษาความสะอาดของดิน และใช้สารเคมีฆ่าเชื้อรา

    2. **โรคดินแข็ง (Soil Compaction)**
    - อาการ: รากไม่สามารถเจริญเติบโตได้ เนื่องจากดินแน่น
    - การรักษา: ปรับสภาพดินให้ร่วนซุย และเพิ่มการระบายน้ำ
    """)

    # Additional diseases
    st.subheader("โรคอื่นๆ")
    st.write("""
    1. **โรคไวรัส (Virus Disease)**
    - อาการ: ใบและผลมีการเปลี่ยนสี มีลายที่ไม่ปกติ
    - การรักษา: ตัดต้นที่ติดเชื้อ และควบคุมการแพร่กระจายของแมลงที่เป็นพาหะ

    2. **โรคที่เกิดจากแมลงศัตรูพืช**
    - อาการ: ใบและต้นเสียหายจากการกินของแมลง
    - การรักษา: ใช้สารกำจัดแมลงและเพิ่มการควบคุมศัตรูพืช
    """)

    # Conclusion
    st.header("สรุป")
    st.write("""
    โรคต่างๆ ที่พบในทุเรียนสามารถป้องกันและรักษาได้ด้วยการใช้สารเคมีที่เหมาะสม การรักษาความสะอาดของสวน และการปรับสภาพดินที่เหมาะสม
    การเฝ้าระวังและตรวจสอบอย่างสม่ำเสมอเป็นสิ่งสำคัญในการป้องกันไม่ให้โรคแพร่กระจาย
    """)


with tab2:
    st.header("Detect Durian ตรวจหาโรคของทุเรียน")
    st.subheader("วิธีการใช้งาน")
    st.write("1. อัปโหลดภาพ (ใบทุเรียน , ต้นทุเรียน , อื่นๆ)")
    st.write("2. รอให้ Model ประมวลผลและทำนาย")
    st.write("3. Model จะแสดงภาพที่ท่านอัปโหลด และทำนายว่ามีสิ่งผิดปกติใดเกิดขึ้น พร้อมสาเหตุและวิธีแก้ไข")

    ## load Model
    model = YOLO("test_leaf_durian.pt")
    def predict_image(image):
        results = model(image)
        return results

    disease_info = {
        'Algal Leaf Spot': {
            'cause': 'เกิดจากเชื้อรา Algae (สาหร่าย)',
            'symptoms': 'จุดที่เกิดบนใบจะมีลักษณะเป็นสีเขียวหรือสีน้ำตาล',
            'prevention': 'ใช้สารเคมี fungicides, ลดความชื้น, ควบคุมการระบาด',
        },
        'Leaf Blight': {
            'cause': 'เกิดจากเชื้อรา Phytophthora หรือ Alternaria',
            'symptoms': 'ใบเริ่มเน่าเปื่อยจากขอบใบ, แผลเปียกชื้น',
            'prevention': 'ใช้สารเคมี fungicides, ควบคุมการให้น้ำ, ปรับปรุงการระบายอากาศ',
        },
        'Leaf Spot': {
            'cause': 'เกิดจากเชื้อรา Septoria, Alternaria, Cercospora',
            'symptoms': 'จุดบนใบที่มีสีเหลือง, น้ำตาล, หรือดำ',
            'prevention': 'ใช้สารเคมี fungicides, ตัดแต่งใบที่ติดเชื้อ',
        },
        'No Disease': {
            'cause': 'ไม่มีโรคหรือปัญหาสุขภาพ',
            'symptoms': 'ไม่มีอาการผิดปกติ',
            'prevention': 'รักษาความสะอาดและสภาพแวดล้อมที่ดี',
        }
    }
    
    ## uploaded file
    uploaded_file = st.file_uploader("อัปโหลดรูปภาพ", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        ##st.image(image, caption="Uploaded Image", use_container_width=True)

        ## Prediction durian disease
        results = predict_image(image)
        st.subheader("Prediction results:")
        st.image(results[0].plot(), caption="Predicted Image", use_container_width=True)
        
        boxes = results[0].boxes  
        class_names = results[0].names 
        confidences = boxes.conf
        max_confidence_idx = confidences.argmax()  
        max_confidence_class = class_names[int(boxes.cls[max_confidence_idx])] 
        max_confidence_value = confidences[max_confidence_idx]

        st.write(f"โรคที่ตรวจพบคือ:  **{max_confidence_class}**")
        st.write(f"ความมั่นใจในการทำนาย:  **{max_confidence_value*100:.2f}%**")

        if max_confidence_class in disease_info:
            st.write(f"**สาเหตุ:** {disease_info[max_confidence_class]['cause']}")
            st.write(f"**อาการ:** {disease_info[max_confidence_class]['symptoms']}")
            st.write(f"**การป้องกันและการรักษา:** {disease_info[max_confidence_class]['prevention']}")
        
with tab3:
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

    st.title("💬 AI Chatbot (No API)")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = generator(prompt, max_length=500000000, num_return_sequences=1)

        msg = response[0]['generated_text']

        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)