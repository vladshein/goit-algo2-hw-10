# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"Teacher(name='{self.first_name} {self.last_name}', age={self.age}, email='{self.email}', subjects={self.can_teach_subjects})"


def create_schedule(subjects: set, teachers: list):
    uncovered_subjects = set(subjects)
    assigned_teachers = []

    while uncovered_subjects:
        candidates = []
        for teacher in teachers:
            teachable = teacher.can_teach_subjects & uncovered_subjects
            if teachable:
                candidates.append((len(teachable), teacher.age, teacher, teachable))

        if not candidates:
            break

        # Сортування викладачів за віком
        candidates.sort(key=lambda x: x[1])

        # Сортування викладачів за кількістю предметів
        candidates.sort(key=lambda x: x[0], reverse=True)
        print(candidates)
        _, _, selected_teacher, assigned_subjects = candidates[0]

        print(f"Candidates are: {candidates}")
        print("====================")
        selected_teacher.assigned_subjects = assigned_subjects
        uncovered_subjects -= assigned_subjects
        teachers.remove(selected_teacher)
        assigned_teachers.append(selected_teacher)

    return assigned_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)
    print(schedule)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
