class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print("為學員%s辦理註冊手續！"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("雇用新員工%s 。。。"%staff_obj.name)


class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        --------Info of Teacher: %s-----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
         ------------------------------------
         ''' %(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))


class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        -------Info of Student: %s-------
        Name:%s
        Age:%s
        Sex:%s
        ID:%s
        Grade:%s
         ------------------------------------
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tuition for $%s" %(self.name,amount))


school = School("金門高中","金門縣金城鎮光前路94號")

t1 = Teacher("謝尚衛",45,"男",81000,"物理")
t2 = Teacher("許淵智",40,"男",75000,"數學")

s1 = Student("陳雋洋",18,"男",510087,"中原大學")
s2 = Student("Jax",18,"男",510088,"台灣大學")

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students[1].stu_id) #s2.stu_id
print(school.staffs[0].salary) #t1.salary
school.staffs[0].teach()

for paid in school.students:
    paid.pay_tuition(5000)

