students = [
    {"name":"zaki","grades":[100,50,25]},
    {"name":"shady","grades":[70,20,35]},
    {"name":"mona","grades":[19,73,15]},
]
avg = {student["name"]:sum(student["grades"])/3 for student in students}
for k,v in avg.items():
    print(f'name: {k}, avg: {v:.2f}')