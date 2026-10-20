class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名；{self.name}，语文成绩：{self.chinese}，数学成绩：{self.math}，英语成绩：{self.english}，总成绩：{self.chinese + self.math + self.english}"

    def update_score(self, subject, score):
        if subject == "chinese":
            self.chinese = score
        elif subject == "math":
            self.math = score
        elif subject == "english":
            self.english = score
        else:
            print("无效的科目名称。")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("请输入学生姓名：")

        for s in self.students:
            if s.name == name:
                print("学生已存在，无法添加。")
                return

        try:
            chinese = int(input("请输入语文成绩："))
            math = int(input("请输入数学成绩："))
            english = int(input("请输入英语成绩："))
        except ValueError:
            print("成绩必须是数字，添加失败。")
            return

        if not (0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100):
            print("成绩必须在0到100之间，学生添加失败。")
            return

        self.students.append(Student(name, chinese, math, english))
        print("学生添加成功。")

    def update_student(self):
        name = input("请输入要修改成绩的学生姓名：")
        for student in self.students:
            if student.name == name:
                subject = input("请输入要修改的科目（chinese, math, english）：")
                score = int(input("请输入新的成绩："))
                if 0 <= score <= 100:
                    student.update_score(subject, score)
                    print("成绩修改成功。")
                else:
                    print("成绩必须在0到100之间，修改失败。")
                return
        print("未找到该学生，无法修改成绩。")

    def remove_student(self):
        name = input("请输入要删除的学生姓名：")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("学生删除成功。")
                return
        print("未找到该学生，无法删除。")

    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for student in self.students:
            if student.name == name:
                print(student)
                return
        print("未找到该学生。")
    def display_all_students(self):
        if not self.students:
            print("没有学生信息。")
            return
        for student in self.students:
            print(student)
    def run(self):
        while True:
            print("\n学生管理系统")
            print("1. 添加学生")
            print("2. 修改学生成绩")
            print("3. 删除学生")
            print("4. 查询学生信息")
            print("5. 显示所有学生信息")
            print("6. 退出系统")
            choice = input("请输入操作编号：")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.remove_student()
            elif choice == "4":
                self.query_student()
            elif choice == "5":
                self.display_all_students()
            elif choice == "6":
                print("退出教务系统。")
                break
            else:
                print("无效的操作编号，请重新输入。")

if __name__ == "__main__":
    manager = StudentManager()
    manager.run()