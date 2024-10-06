class Abiturient:
    def __init__(self, id, surname, name, patronymic, address, phone, grades):
        """ Конструктор класса Abiturient """
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.phone = phone
        self.grades = grades
    
    def get_grades(self):
        """ Геттер для получения оценок """
        return self.grades
    
    def set_grades(self, grades):
        """ Сеттер для установки оценок """
        self.grades = grades
    
    def get_id(self):
        """ Геттер для ID """
        return self.id

    def __str__(self):
        """ Переопределение метода toString для вывода информации об абитуриенте """
        return f"{self.id} | {self.surname} {self.name} {self.patronymic} | Адрес: {self.address} | Телефон: {self.phone} | Оценки: {self.grades}"
    
    def __hash__(self):
        """ Переопределение метода hashCode для уникальной хэш-функции """
        return hash((self.id, self.surname, self.name, self.patronymic, self.address, self.phone, tuple(self.grades)))

def abiturients_with_unsatisfactory(grads, unsatisfactory_grade=3):
    """ Получает список абитуриентов с неудовлетворительными оценками """
    return [abiturient for abiturient in grads if any(grade < unsatisfactory_grade for grade in abiturient.get_grades())]

def abiturients_above_score(grads, threshold):
    """ Получает список абитуриентов с суммой баллов выше заданной """
    return [abiturient for abiturient in grads if sum(abiturient.get_grades()) > threshold]

def abiturients_with_highest_sum(grads, num):
    """ Получает список абитуриентов с самой высокой суммой баллов, а также дает полный список с полупроходной суммой """
    sorted_abiturients = sorted(grads, key=lambda abiturient: sum(abiturient.get_grades()), reverse=True)
    highest_abiturients = sorted_abiturients[:num]
    
    # Вычисление полупроходной суммы (например, минимальная сумма среди высоких)
    passing_score = sum(highest_abiturients[-1].get_grades())
    
    # Получение всех абитуриентов с полупроходной суммой
    passing_abiturients = [abiturient for abiturient in grads if sum(abiturient.get_grades()) >= passing_score]
    
    return highest_abiturients, passing_abiturients

# Пример использования
if __name__ == "__main__":
    # Создание массива абитуриентов
    abiturients = [
        Abiturient(1, "Иванов", "Иван", "Иванович", "Москва, ул. Ленина", "123456789", [3, 5, 4, 2]),
        Abiturient(2, "Петров", "Петр", "Петрович", "Москва, ул. Пушкина", "987654321", [5, 5, 4, 4]),
        Abiturient(3, "Сидоров", "Сидор", "Сидорович", "Москва, ул. Гоголя", "123123123", [2, 2, 3, 3]),
        Abiturient(4, "Федоров", "Федор", "Федорович", "Москва, ул. Чехова", "321321321", [5, 5, 5, 4])
    ]

    # a) Список абитуриентов, имеющих неудовлетворительные оценки
    unsatisfactory = abiturients_with_unsatisfactory(abiturients)
    print("Абитуриенты с неудовлетворительными оценками:")
    for abiturient in unsatisfactory:
        print(abiturient)

    # b) Список абитуриентов, у которых сумма баллов выше заданной
    threshold = 12
    above_threshold = abiturients_above_score(abiturients, threshold)
    print(f"\nАбитуриенты с суммой баллов выше {threshold}:")
    for abiturient in above_threshold:
        print(abiturient)

    # c) Заданное число абитуриентов, имеющих самую высокую сумму баллов, и полный список с полупроходной суммой
    num = 2
    highest_abiturients, passing_abiturients = abiturients_with_highest_sum(abiturients, num)

    print(f"\nТоп {num} абитуриентов с самой высокой суммой баллов:")
    for abiturient in highest_abiturients:
        print(abiturient)

    print("\nАбитуриенты с полупроходной суммой:")
    for abiturient in passing_abiturients:
        print(abiturient)
