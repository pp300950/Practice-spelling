import random
from termcolor import colored

words =  [
    ("aggressive", "แอ็ก-เกรส-ซิฟ"),
    ("refrigerator", "รี-ฟริ-เจอ-เร-เทอร์"),
    ("community", "คอ-มิว-นิ-ที"),
    ("neighborhood", "เน-ยิบ-เบอร์-ฮูด"),
    ("ingredient", "อิน-เกร-เดียน-ท"),
    ("intelligent", "อิน-เทล-ลิ-เจ้น-ท"),
    ("expensive", "อิค-สเพน-ซิฟ"),
    ("firefighter", "ไฟ-เยอร์-ไฟ-เทอร์"),
    ("knowledge", "โน-เลจ"),
    ("celebrate", "เซ-เล-เบรต"),
    ("delicious", "ดิ-ลิ-เชียส"),
    ("foreigner", "ฟอร์-เนอ"),
    ("information", "อิน-ฟอร์-เม-ชัน"),
    ("seatbelt", "ซี-ท-เบลท์"),
    ("inheritance", "อิน-เฮ-ริ-เทน-ส"),
    ("pharmacist", "ฟาร์-แม-ซิส-ท"),
    ("pharmacy", "ฟาร์-แม-ซี"),
    ("engineer", "อิน-จี-เนียร์"),
    ("accountant", "เเอคเคาท์ทึนท"),
    ("archaeologist", "อาร์-ชา-โอ-โล-จิส"),
    ("architect", "อาร์-คิ-เทค-ท"),
    ("announcement", "แอ-นาวน์-เมน-ท"),
    ("achievement", "แอ-ชีฟ-เมน-ท"),
    ("confusion", "คอน-ฟิว-ชั่น"),
    ("biologist", "ไบ-อ็อล-อะ-จิส"),
    ("advertisement", "แอด-เวอร์-ไท-ซเมน-ท"),
    ("search", "เซิร์ช"),
    ("ceremony", "เซ-เร-โม-นี"),
    ("discussion", "ดิ-สคัด-ชัน"),
    ("expensive", "อิค-สเพน-ซิฟ"),
    ("decorator", "ดี-เคอ-เร-เทอร์"),
    ("scholarship", "ชอ-ลา-ชิพ"),
    ("receptionist", "รี-เซป-ชั่น-นิสต์"),
    ("detective", "ดิ-เทก-ทิฟ"),
    ("education", "อิ-ดึ-เค-ชัน"),
    ("garland", "แกร์-แลนด์"),
    ("palace", "พา-เลซ"),
    ("sponge", "สปั๊น-จ"),
    ("competition", "คอม-เพ็ท-ทิ-ชัน"),
    ("retreat", "รี-ทรีต"),
    ("excellent", "เอ็กซ์-เซล-เลนต์"),
    ("memory", "เมม-โม-รี"),
    ("persuade", "เพอร์-สเวด"),
    ("dangerous", "แด็น-เจอ-รัส"),
    ("secretary", "ซี-เค-เร-เทรี"),
    ("interpreter", "อิน-เทอร์-พรี-เทอร์"),
    ("journalist", "เจอร์-นัล-ลิสต์"),
    ("influence", "อิน-ฟลู-เอน-ซ"),
    ("concentrate", "คอน-เซ็น-เทรท"),
    ("merchant", "เมอร์-แชนท์"),
    ("invite", "อิน-ไวท"),
    ("treasure", "เทร-เชอร์"),
    ("president", "ปรี-เซ-เด้นท์"),
    ("messenger", "เมส-เซน-เจอ"),
    ("photographer", "ฟอ-โท-กรา-ฟอร์"),
    ("bartender", "บาร์-เทน-ดอร์"),
    ("cashier", "แคช-เชียร์"),
    ("scientist", "ไซ-เอ็น-ทิส"),
    ("dressmaker", "เดรส-เมก-เคอร์"),
    ("population", "ปอ-พู-เล-ชัน"),
]
A=60
B=0
# ประกาศตัวแปรสำหรับเก็บคำที่ถูกต้อง
correct_words = []

# ประกาศตัวแปรสำหรับเก็บคะแนน
score = 0

# วนลูปเพื่อสุ่มคำ
while True:
    # สุ่มคำศัพท์ออกมาหนึ่งคำ
    word, reading = random.choice(words)

    # ตรวจสอบว่าคำศัพท์นั้นเคยถูกพิมพ์มาแล้วหรือไม่
    if word in correct_words:
        continue

    # พิมพ์คำศัพท์และคำอ่านออกมาให้ผู้ใช้g
    
    print("  คำอ่าน: " + reading)
    B = B + 1
    # รับคำตอบจากผู้ใช้
    answer = input("  คำศัพท์: ")

    # ตรวจสอบคำตอบ
    if answer.lower() == word:
        # คำตอบถูก
        correct_words.append(word)
        print(colored("  ถูกต้อง", 'green'))
        score += 1
        A = A - 1
    else:
        # คำตอบผิด
        print(colored(f"  ผิด คำศัพท์ถูกต้องคือ: {word}", 'red'),"     ")

    # แสดงคะแนน
    print("  ตอบถูก: " + str(score),"เหลืออีก:"+str(A)," คำ" ,"ตอบ: "+str(B)+" ครััง")
print("**********************")
print("  ตอบผิดทั้งหมด",B-59)