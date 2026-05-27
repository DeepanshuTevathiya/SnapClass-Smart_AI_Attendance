# 📸 SnapClass — Smart AI Attendance System

An AI-powered attendance system that reduces attendance-taking from **5–10 minutes to just 5–10 seconds**.  
Click a photo of the class → AI recognizes every student → attendance marked. Done.

> 🎥 **Demo Video** — *(https://github.com/user-attachments/assets/7416dd80-f2d4-45a1-9b25-c5cf62721cca)*

---

## How It Works

**Teacher:** Take a photo of the class → face recognition identifies students → attendance marked instantly. Alternatively, use voice roll-call. Export records as CSV anytime.

**Student:** Register with a face photo + optional voice sample → enroll in subjects via QR code or URL → track attendance % on personal dashboard.

---

## Project Structure

```
SnapClass/
├── src/
│   ├── components/       # Reusable UI components
│   ├── Database/         # Supabase DB interactions
│   ├── pipelines/        # Face & voice recognition pipelines
│   ├── screens/          # App screens (Teacher, Student views)
│   └── ui/               # Styling and layout
├── .streamlit/           # Streamlit config
├── app.py                # Entry point
└── requirements.txt
```

---

## Tech Stack

| Layer | Tech |
|---|---|
| Frontend | Streamlit |
| Backend / DB | Supabase |
| Face Recognition | Dlib + face_recognition |
| Face Classifier | SVM (retrained on each new registration) |
| Voice Recognition | Resemblyzer + Librosa |
| QR Enrollment | Segno |
| Auth | Bcrypt |

---

## Supabase Setup

### 1. Create a Supabase project at [supabase.com](https://supabase.com)

### 2. Create the following tables manually in your Supabase Table Editor:

**`teacher`**
| Column | Type |
|---|---|
| teacher_id | int8 (PK) |
| username | text |
| name | text |
| password | text |

**`student`**
| Column | Type |
|---|---|
| student_id | int8 (PK) |
| name | text |
| face_embedding | jsonb |
| voice_embedding | jsonb |

**`subjects`**
| Column | Type |
|---|---|
| subject_id | int8 (PK) |
| subject_code | text |
| subject_name | text |
| section | text |

**`subject_student`** *(enrollment junction table)*
| Column | Type |
|---|---|
| subject_id | int8 (PK, FK → subjects) |
| student_id | int8 (PK, FK → student) |

**`attendance`**
| Column | Type |
|---|---|
| id | int8 (PK) |
| timestamp | timestamptz |
| subject_id | int8 (FK → subjects) |
| student_id | int8 (FK → student) |
| is_present | bool |

### 3. Add your credentials in a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

---

## Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/DeepanshuTevathiya/SnapClass-Smart_AI_Attendance
cd SnapClass-Smart_AI_Attendance

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your .env file with Supabase credentials

# 5. Run the app
streamlit run app.py
```

---

## Try It Out

🌐 **App:** [snapclass-deepminds.streamlit.app](https://snapclass-deepminds.streamlit.app)  
🖥️ **Landing Page:** [snap-class-landing-page-green.vercel.app](https://snap-class-landing-page-green.vercel.app/)

---

## Author

**Deepanshu Tevathiya** — AI / ML Enthusiast

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/deepanshu-tevathiya/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/DeepanshuTevathiya)
