import excel_read
from names import Student

menu = 'Choose an option:\n' \
       '1.\tAdd new student\n' \
       '2.\tGenerate CSV\n' \
       '3.\tGet Student List:\n' \
       '0.\tQuit\n'


grade_values = {
    '0': 'Kindergarten',
    '1': 'First Grade',
    '2': 'Second Grade',
    '3': 'Third Grade',
    '4': 'Fourth Grade',
    '5': 'Fifth Grade',
    '6': 'Sixth Grade',
    '7': 'Seventh Grade',
    '8': 'Eighth Grade'
}

csv_values = {
    'Kindergarten': '/Students/Kindergarten',
    'First Grade': '/Students/1st Grade',
    'Second Grade': '/Students/2nd Grade',
    'Third Grade': '/Students/3rd Grade',
    'Fourth Grade': '/Students/4th Grade',
    'Fifth Grade': '/Students/5th Grade',
    'Sixth Grade': '/Students/6th Grade',
    'Seventh Grade': '/Students/7th Grade',
    'Eighth Grade': '/Students/8th Grade'
}


if __name__ == '__main__':
    while True:
        file_name = input('Copy and paste the excel\'s file path here: ')
        file_name = file_name.replace('\"', '')
        try:
            school = excel_read.main(file_name)
            break
        except Exception as e:
            error = 'In file explorer navigate to where excel file is\n' \
                    'While holding down shift key, right click on the excel file and click \'Copy As Path\'' \
                    'In here use \'Ctrl V\' to paste file path here'
            print(e)
            print(error)
    for class_ in school:
        class_.sort(key=lambda student_method: student_method.first_name)
    for class_ in school:
        print(class_)
    while True:
        user_choice = input(menu)
        if user_choice == '0':
            break
        elif user_choice == '1':
            first_name = input('Enter Student\'s first name: ')
            last_name = input('Enter Student\'s last name (Don\'t include Jr., ii, etc.): ')
            class_level = (input('Enter Student\'s class level ((0 for Kindergarten),1,2,etc.): '))[0:1]
            domain = input('Enter Domain(standard is \'@elsbaltimore.org\'): ')
            new_student = Student(first_name, last_name, domain, grade_values[class_level])
            print(new_student)
            school[int(class_level)].append(new_student)
            for class_ in school:
                print(class_)
        elif user_choice == '2':
            password = input('Enter Student\'s Password:')
            path = input('Enter file path for the new csv file:')
            file_name = "{0}\\users.csv".format(path)
            with open(file_name, 'w') as file:
                file.write('First name,Last name,Email address,Password,Org Unit Path,'
                           'Change Password at Next Sign-In\n')
                for class_ in school:
                    for student in class_:
                        file.write(f'{student.first_name},{student.last_name},{student.email},{password},'
                                   f'{csv_values[student.class_level]},TRUE\n')
        elif user_choice == '3':
            path = input('Enter file path for the new csv file:')
            file_name = "{0}\\student_list.csv".format(path)
            with open(file_name, 'w') as list_:
                for class_ in school:
                    for student in class_:
                        list_.write(f'{student.first_name},{student.last_name},{student.email},{student.class_level}\n')
                    list_.write('\n')
        else:
            print('Invalid Input')
