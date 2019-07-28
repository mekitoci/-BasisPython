#格式化的三種方式
name = input("name:")
age = input("age:")
job = input("job:")
school = input("School:")

info = ''' 
---------------info of %s ---------------
name: %s
age: %s
job: %s 
school: %s 
''' % (name,name,age,job,school)

info2 = ''' 
---------------info of {_name} ---------------
name: _name
age: _age
job: _job
school: _school 
'''  .format(_name=name,_age=age,_job=job,_school=school)

info3 =''' 
---------------info of {0} ---------------
name: {0}
age: {1}
job: {2}
school: {3} 
'''  .format(_name=name,_age=age,_job=job,_school=school)

print(info)
