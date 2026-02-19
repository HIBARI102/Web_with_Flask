StayFix/
├── app/                        # โฟลเดอร์หลักของโปรแกรม
│   ├── __init__.py             # จุดเริ่มต้นโปรแกรม (App Factory)
│   ├── models.py               # นิยามฐานข้อมูล (Table ต่างๆ)
│   ├── static/                 # เก็บ CSS, JS, Images
│   │   └── css/
│   │       └── style.css       # ไฟล์ Tailwind/Custom CSS
│   ├── templates/              # เก็บไฟล์ HTML (แบ่งหมวดหมู่ย่อย)
│   │   ├── base.html           # โครงหลัก (Navbar/Footer)
│   │   ├── partials/           # ส่วนประกอบย่อย (เช่น _sidebar.html)
│   │   ├── main/               # (กลุ่ม 1) หน้าทั่วไป: Dashboard, About
│   │   ├── tickets/            # (กลุ่ม 2) หน้าจัดการแจ้งซ่อม: Add, List, Detail, Edit, History
│   │   └── rooms/              # (กลุ่ม 3) หน้าจัดการห้องพัก: Room List, Assign Tech
│   └── routes/                 # เก็บ Logic การทำงาน (Blueprints)
│       ├── main.py             # เส้นทางของหน้า Dashboard, About
│       ├── tickets.py          # เส้นทางของหน้าแจ้งซ่อมทั้งหมด
│       └── rooms.py            # เส้นทางของหน้าจัดการห้อง
├── instance/                   # เก็บไฟล์ database.db (SQLite)
├── .gitignore                  # ระบุไฟล์ที่ไม่ต้องเอาลง Git (เช่น venv/)
├── requirements.txt            # รายชื่อ Library ที่ใช้
└── run.py                      # ไฟล์สำหรับสั่งรันโปรแกรม
