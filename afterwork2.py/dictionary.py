student_data = {
    "id1":{"name":"jordan","class":"V","Subject_intigrestion":"english, math, science"},
    "id2":{"name":"jordan","class":"V","Subject_intigrestion":"english, math, science"},
    "id3":{"name":"micheal","class":"V","Subject_intigrestion":"english, math, science"},
    "id4":{"name":"priyansh","class":"V","Subject_intigrestion":"english, math, science"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_keys = (details["name"],details["class"], details["Subject_intigrestion"])
    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id] = details
    
for k, v in result.items():
    print(k, " : ",v)


