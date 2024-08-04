import random
import json

def startQuestion(massivIngrediens):
    question = []

    for item in massivIngrediens:
        ingredients = item[1]
        for ingredient in ingredients:
            if ingredient not in question:
                question.append(ingredient)

    while question:
        random_ingredient = random.choice(question)
        question.remove(random_ingredient)

        def ingidient(random_ingredient):
            ingridientsNumber = input(f"На сколько от 1 до 5, вам нравится данный ингредиент: {random_ingredient}\n")

            # Проверяем, что введенное значение в допустимом диапазоне
            if ingridientsNumber.isdigit() and 1 <= int(ingridientsNumber) <= 5:
                return searchIngidient(int(ingridientsNumber), random_ingredient)
            else:
                print("Пожалуйста, введите число от 1 до 5.")
                return ingidient(random_ingredient)
        
        def searchIngidient(ingridientsNumber, random_ingredient):
            total_occurrences = check_ingredient(ingridientsNumber, random_ingredient, massivIngrediens)  # Инвертируем оценку
            print(f"Ингредиент '{random_ingredient}' найден {total_occurrences} раз(а) в списке.")
            for dish in massivIngrediens:
                if dish[2] > 80.0:
                    print(f"Блюдо '{dish[0]}' набрало более 80 процентов.")
                    return True  # Завершаем цикл
            return False  # Продолжаем цикл

        def check_ingredient(ingridientsNumber, ingredient, data):
            total_count = 0
            for dish in data:
                if ingredient in dish[1]:
                    # Рассчитываем процентное соотношение
                    percent_value = (100 / len(dish[1])) / 5 * ingridientsNumber
                    dish[2] += percent_value
                    print(dish[0], dish[2])
                    total_count += 1
            return total_count

        if ingidient(random_ingredient):
            break

    if not question:
        print('Вы тот, кому ничего не нравится.')
        return

def start():
    # Открытие и чтение JSON-файла
    with open('c:/Users/N_OFFICE_5/Desktop/react/py/product.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Преобразование данных обратно в список списков
        massivIngrediens = [[item['name'], item['ingredients'], item['count']] for item in data]


    print('Приветсвую, пользователь!', end='\n') 
    ansverUsers = input('Хотите узнать свое любимое блюдо? Напишите "+": ') 

    if(ansverUsers == '+'):
        startQuestion(massivIngrediens)
    else: 
        return print('Отключение')

start()