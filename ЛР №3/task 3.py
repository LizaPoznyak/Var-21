# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.

with open("subjects.txt", "r", encoding='utf-8') as file:
    subjects = file.readlines()

subject_dict = {}
for subject in subjects:
    subject_info = subject.split(" - ")
    subject_name = subject_info[0]
    lesson_info = subject_info[1].split(" ")
    total_lessons = 0
    for lesson in lesson_info:
        lesson_details = lesson.split("(")
        total_lessons += int(lesson_details[0])
    subject_dict[subject_name] = total_lessons

for subject, total_lessons in subject_dict.items():
    print(f"{subject}: {total_lessons}")
