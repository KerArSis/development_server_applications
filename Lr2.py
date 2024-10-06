# Создаем классы для иерархии овощей
class Vegetable:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

class Root(Vegetable):
    pass

class Leafy(Vegetable):
    pass

class Fruit(Vegetable):
    pass

# Создаем экземпляры овощей
carrot = Root("Carrot", 50)
potato = Root("Potato", 77)
spinach = Leafy("Spinach", 23)
tomato = Fruit("Tomato", 18)
cucumber = Fruit("Cucumber", 16)

# Создаем салат и добавляем овощи
salad = [carrot, potato, spinach, tomato, cucumber]

# Функция для подсчета общей калорийности салата
def calculate_salad_calories(salad):
    total_calories = 0
    for vegetable in salad:
        total_calories += vegetable.calories
    return total_calories

# Функция для сортировки овощей в салате по калорийности
def sort_salad_by_calories(salad):
    salad.sort(key=lambda x: x.calories)
    return salad

# Функция для поиска овощей в заданном диапазоне калорийности
def find_vegetables_in_calorie_range(salad, min_calories, max_calories):
    return [vegetable for vegetable in salad if min_calories <= vegetable.calories <= max_calories]

# Пример использования
print("Салат:")
for vegetable in salad:
    print(f"- {vegetable.name} ({vegetable.calories} калорий)")

print(f"\nОбщая калорийность салата: {calculate_salad_calories(salad)} калорий")

print("\nСалат, отсортированный по калорийности:")
sorted_salad = sort_salad_by_calories(salad)
for vegetable in sorted_salad:
    print(f"- {vegetable.name} ({vegetable.calories} калорий)")

print("\nОвощи в салате, калорийность которых находится в диапазоне от 20 до 60 калорий:")
vegetables_in_range = find_vegetables_in_calorie_range(salad, 20, 60)
for vegetable in vegetables_in_range:
    print(f"- {vegetable.name} ({vegetable.calories} калорий)")
