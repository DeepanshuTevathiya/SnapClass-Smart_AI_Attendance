from src.Database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def check_teacher_exist(username):
    response = supabase.table("teacher").select("username").eq("username",username).execute()
    return len(response.data)>0

def create_teacher(username, name, password):
    data = {"username":username, "name":name, "password": hash_pass(password)}
    response = supabase.table("teacher").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teacher").select("*").eq("username",username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None


def get_all_students():
    response = supabase.table("student").select("*").execute()
    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {'name':new_name, 'face_embedding':face_embedding, 'voice_embedding':voice_embedding}
    response = supabase.table('student').insert(data).execute()
    return response.data

def create_subject(subject_code, subject_name, section, teacher_id):
    data = {'subject_code':subject_code, 'subject_name':subject_name, 'section':section, 'teacher_id':teacher_id}
    response = supabase.table('subjects').insert(data).execute()
    return response.data

def get_teacher_subjects(teacher_id):
    response = supabase.table('subjects').select("*, subject_student(count), attendance(timestamp)").eq('teacher_id',teacher_id).execute()
    subjects =  response.data

    for sub in subjects:
        sub['total_students'] = sub.get('subject_student', [{}])[0].get('count', 0) if sub.get('subject_student') else 0
        attendance = sub.get('attendance', [])
        unique_session = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_session

        sub.pop('subject_student', None)
        sub.pop('attendance', None)
    return subjects