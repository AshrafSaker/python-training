salaries = [2000, 1800, 3100, 4400, 1500]
#bonus = int(input("write bounce to add: "))
bonus = 10
salaries = list(map(lambda x: x+ bonus , salaries))
# تستخدم map كمعادلة سريعة ل اجراء حسابي  كل index  في ال list 
print(salaries)

#filter تعمل  هذه الوظيفة في فصل القيم المحدده بشرط معين 
salaries = [2000, 1800, 3100, 4400, 1500]

res = list(filter(lambda x: x > 3000 , salaries))#
# تم عمل فلتر في القائمة للقيم اكبر من 3000
print(res)
