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


def check_student_exist(username):
    response = supabase.table("student").select("username").eq("username",username).execute()
    return len(response.data)>0

def create_student(username, name, password):
    data = {"username":username, "name":name, "password":hash_pass(password)}
    response = supabase.table("student").insert(data).execute()
    return response.data

def student_login(username, password):
    response = supabase.table("student").select("*").eq("username",username).execute()
    if response.data:
        student = response.data[0]
        if check_pass(password, student["password"]):
            return student
    return None