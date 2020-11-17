def path(students):
    students = sorted(students, key=lambda vector: (int(vector[2]), vector[1]))
    return students

def input_q2693(forms):
    output = []
    
    for i in range(len(forms)):
        if len(forms[i]) < 2:
            line = []
            gap = i + int(forms[i]) + 1
            for j in range(i+1, gap):
                line.append(forms[j].split())
            line = path(line)
            for word in line:
                output.append(word[0])

    return '\n'.join(output)