import xlrd
from names import Student
import email_check

grade_names = {
    'kindergarten': 'Kindergarten',
    'grade1': 'First Grade',
    'grade2': 'Second Grade',
    'grade3': 'Third Grade',
    'grade4': 'Fourth Grade',
    'grade5': 'Fifth Grade',
    'grade6': 'Sixth Grade',
    'grade7': 'Seventh Grade',
    'grade8': 'Eighth Grade'
}


roman_numerals = {
    'grade i': 'grade1',
    'grade ii': 'grade2',
    'grade iii': 'grade3',
    'grade iv': 'grade4',
    'grade v': 'grade5',
    'grade vi': 'grade6',
    'grade vii': 'grade7',
    'grade viii': 'grade8'
}

titles = [' jr.', ' jr', ' sr.', ' sr', 'iii', ' ii', ' iv', ' Jr.', ' Jr',
          ' Sr.', ' Sr', ' III', ' II', ' IV']


def get_grade_number(roman_numeral):
    return roman_numerals[roman_numeral]


def sort_students(students):
    new_students = [[], [], [], [], [], [], [], [], []]
    for class_list in students:
        num = email_check.grade_numbers[class_list[0].class_level]
        new_students[num] = class_list
    return new_students


def delete_spaces(value):
    if ',' in str(value):
        for title in titles:
            if title in value:
                value = value.replace(title, '')
        value = value.replace(' ', '')
        value = value.replace('*', '')
        return value
    else:
        return str(value)


def main(location):
    global grade_names
    global roman_numerals
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)
    text = []
    with open('names.txt', 'w') as values:
        for col in range(10):
            for row in range(100):
                try:
                    value = sheet.cell_value(row, col)
                    if value == '':
                        pass
                    else:
                        values.write(str(value) + '\n')
                        text.append(value)
                except IndexError:
                    break
    in_class = False
    class_name = ''
    students = []
    class_list = []
    count = 0
    for name in text:
        value = delete_spaces(name)
        lower_value = value.lower()
        if lower_value in roman_numerals:
            lower_value = roman_numerals[lower_value]
        if lower_value in grade_names:
            in_class = True
            class_name = grade_names[lower_value]
        elif in_class:
            if ',' in value:
                f_name = value[value.index(',') + 1:]
                l_name = value[0:value.index(',')]
                new_student = Student(f_name, l_name, '@elsbaltimore.org', class_name)
                class_list.append(new_student)
            else:
                in_class = False
                students.append(class_list)
                class_list = []
                count += 1
    students = sort_students(students)
    email_check.main(students)
    return students


if __name__ == '__main__':
    s = main('C:/Users/markv/Documents/Emmanuel/School/Mark.xlsx')
