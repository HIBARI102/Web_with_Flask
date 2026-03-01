# 🏨 StayFix - Hotel Maintenance System

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.2-black?style=for-the-badge&logo=flask)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css)
![SQLite](https://img.shields.io/badge/SQLite-3.0-003B57?style=for-the-badge&logo=sqlite)

**StayFix** คือระบบบริหารจัดการงานซ่อมบำรุงภายในโรงแรม พัฒนาด้วย Python Flask และ Tailwind CSS ออกแบบมาเพื่อให้เจ้าหน้าที่โรงแรมสามารถติดตามสถานะการแจ้งซ่อมได้อย่างรวดเร็วและแม่นยำ

---

## ✨ Features (คุณสมบัติเด่น)

* **🎫 Ticket Management**: สร้าง, แก้ไข และลบตั๋วแจ้งซ่อม พร้อมระบบ Priority (Low, Normal, High)
* **🏢 Room Management**: จัดการข้อมูลห้องพัก และเชื่อมโยงตั๋วแจ้งซ่อมเข้ากับหมายเลขห้อง
* **🌓 Dark Mode Support**: รองรับการใช้งานทั้งโหมดสว่างและโหมดมืด (Dark Mode) อย่างสมบูรณ์
* **🌐 Multilingual**: ระบบสลับภาษา ไทย (TH) และ อังกฤษ (EN) ทั่วทั้งแอปพลิเคชัน
* **📊 Dashboard**: สรุปภาพรวมสถานะตั๋วแจ้งซ่อมที่ยังค้างอยู่ในระบบ

---

## 🛠️ Tech Stack (เครื่องมือที่ใช้)

| ส่วนงาน | เทคโนโลยีที่ใช้ |
| :--- | :--- |
| **Backend** | Python 3.13 / Flask Framework |
| **Database** | SQLite + SQLAlchemy (ORM) |
| **Auth** | Flask-Login |
| **Frontend** | Tailwind CSS + Jinja2 Templates |
| **Icons** | Heroicons / Unicode Emojis |


---

## 🚀 Getting Started (วิธีการติดตั้งและรัน)

### 1. เตรียมสภาพแวดล้อม (Environment)
```bash
# สร้างและเปิดใช้งาน Virtual Environment
python -m venv .venv
.\.venv\Scripts\activate
```
2. ติดตั้ง Library และ Database
```bash
pip install -r requirements.txt
flask init-db
```
3. เริ่มใช้งานโปรแกรม
```bash
python run.py
```
เข้าใช้งานผ่าน URL: http://127.0.0.1:5000




