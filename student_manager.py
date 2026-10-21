from fastapi import FastAPI, HTTPException

app = FastAPI()

class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名；{self.name}，语文成绩：{self.chinese}，数学成绩：{self.math}，英语成绩：{self.english}，总成绩：{self.total_score()}"

    def update_score(self, subject, score):
        if subject == "chinese":
            self.chinese = score
        elif subject == "math":
            self.math = score
        elif subject == "english":
            self.english = score
        else:
            print("无效的科目名称。")

    def total_score(self):
        return self.chinese + self.math + self.english

    def to_dict(self):
        return {
            "name": self.name,
            "chinese": self.chinese,
            "math": self.math,
            "english": self.english,
            "total_score": self.total_score()
        }
students = []

@app.get("/students")
def get_students():
    return [student.to_dict() for student in students]

@app.post("/students")
def add_student(data:dict):
    name = data.get("name")

    if not name:
        raise  HTTPException(status_code=400,detail="缺少学生姓名")
    for s in students:
        if s.name == name:
            raise   HTTPException(status_code=400,detail="学生已存在")
    try:
        chinese = int(data["chinese"])    
        math = int(data["math"])   
        english = int(data["english"])
    except (KeyError,ValueError):
        raise HTTPException(status_code=400,detail="学生成绩必须是整数")
    if not (0<=chinese<=100 and 0<=math<=100 and 0<=english<=100):
        raise HTTPException(status_code=400,detail="学生成绩必须在0到100区间内")
    students.append(students(name,chinese,math,english))
    return{"message":"添加成功","student":name}

@app.delete("/students/{name}")
def remove_student(name: str):
    for s in students:
        if s.name == name:
            students.remove(s)
            return {"message": "删除成功", "student": name}

    raise HTTPException(status_code=404, detail="未找到该学生")