import random
import json

def startQuestion(massivIngrediens):
    question = []

    for item in massivIngrediens:
        ingredients = item[1]
        for ingredient in ingredients:
            if ingredient not in question:
                question.append(ingredient)

    while True:
        random_ingredient = random.choice(question)

        def ingidient(random_ingredient):
            ingridientsNumber = input(f"На сколько от 1 до 5, вам нравиться данный ингредиент: {random_ingredient}\n")

            # Проверяем, что введенное значение в допустимом диапазоне
            if ingridientsNumber.isdigit() and 1 <= int(ingridientsNumber) <= 5:
                searchIngidient(ingridientsNumber, random_ingredient)
            else:
                print("Пожалуйста, введите число от 1 до 5.")
                ingidient(random_ingredient)
        
        def searchIngidient(ingridientsNumber, random_ingredient):
            print(f"Вы ввели данное значение: {ingridientsNumber}")
            total_occurrences = check_ingredient(random_ingredient, massivIngrediens)
            
            print(f"Ингредиент '{random_ingredient}' найден {total_occurrences} раз(а) в списке.")


        def check_ingredient(ingredient, data):
            total_count = 0
            for dish in data:
                count = dish[1].count(ingredient)
                dish[2] += count
                total_count += count
            return total_count

        ingidient(random_ingredient)
        break
        
 
def start():
    print('Приветсвую, пользователь!', end = '\n') 
 
    # ansverUsers = input('Хотите узнать свое любимое блюдо? Напишите "+", если согласны ') 

    # Открытие и чтение JSON-файла
    with open('product.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Преобразование данных обратно в список списков
        massivIngrediens = [[item['name'], item['ingredients'], item['count']] for item in data]

        # Печать результата
        print(massivIngrediens)

    # if(ansverUsers != '+'):
    #         return print('Отключение')

    # startQuestion(massivIngrediens) 

start()