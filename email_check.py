b = []

grade_numbers = {
    'Kindergarten': 0,
    'First Grade': 1,
    'Second Grade': 2,
    'Third Grade': 3,
    'Fourth Grade': 4,
    'Fifth Grade': 5,
    'Sixth Grade': 6,
    'Seventh Grade': 7,
    'Eighth Grade': 8
}


def check(f, s, count):
    global b
    one = f[0:count]
    two = s[0:count]
    if one == two:
        check(f, s, count + 1)
        b.append([one, two])
    else:
        b.append([one, two])


def find_duplicate(s, c):
    global b
    for student in c:
        if student.email == s.email and s.first_name != student.first_name:
            check(student.first_name, s.first_name, 1)
            s.email = (b[0][1] + s.last_name + s.domain).lower()
            student.email = (b[0][0] + student.last_name + student.domain).lower()
            break
        elif student.email == s.email and s.first_name == student.first_name:
            s.email = (s.first_name[0:1] + s.last_name + str(grade_numbers[s.class_level]) + s.domain).lower()
    b = []


def main(student_list):
    emails = set()
    for class_list in student_list:
        for student in class_list:
            length = len(emails)
            emails.add(student.email)
            if len(emails) == length:
                find_duplicate(student, class_list)


if __name__ == '__main__':
    print('hi')
