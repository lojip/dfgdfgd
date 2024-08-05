import random
import json

PROCENT_MAX = 80.0
PROCENT_AVERAGE = 70.0
PROCENT_MIN = 60.0

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
            
            scores = {}
            for dish in massivIngrediens:
                score = dish[2]
                if score in scores:
                    scores[score].append(dish[0])
                else:
                    scores[score] = [dish[0]]
            remaining_ingredients = [ingredient for dish in massivIngrediens if dish[2] == score for ingredient in dish[1] if ingredient in question]          
            print(remaining_ingredients)
            
            for dish in massivIngrediens:
                if dish[2] >= PROCENT_MAX:
                    for score, dishes in scores.items():
                        if len(dishes) == 1:
                            print(f"Скорее всего ваше любимое блюдо: '{dish[0]}'.")
                            return True
                        else: 
                            remaining_ingredients = [ingredient for dish in massivIngrediens if dish[2] == score for ingredient in dish[1] if ingredient in question]
                            handle_duplicate(remaining_ingredients, dishes)
                            return False

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
        
        def handle_duplicate(score, dishes):
            while score:
                random_ingredient = random.choice(question)
                question.remove(random_ingredient)

                def ingidientDouble(random_ingredient):
                    ingridientsNumber = input(f"На сколько от 1 до 5, вам нравится данный ингредиент: {random_ingredient}\n")

                    # Проверяем, что введенное значение в допустимом диапазоне
                    if ingridientsNumber.isdigit() and 1 <= int(ingridientsNumber) <= 5:
                        return searchIngidientDouble(random_ingredient)
                    else:
                        print("Пожалуйста, введите число от 1 до 5.")
                        return ingidientDouble(random_ingredient)
                    
                def searchIngidientDouble(ingredient):
                    for dish in massivIngrediens:
                        if ingredient in dish[1]:
                            return print(f"Скорее всего ваше любимое блюдо: '{dish[0]}'.")
                        else: 
                            return print("Возникла Ошибка")
                
                if ingidientDouble(random_ingredient):
                    break

        if ingidient(random_ingredient):
            break

    if not question:
        massivIngrediens.sort(key=lambda x: x[2], reverse=True)
        for dish in massivIngrediens:
            if dish[2] >= PROCENT_AVERAGE:
                return print(f"Наверное ваше любимое блюдо: '{dish[0]}'.")
            elif dish[2] >= PROCENT_MIN:
                return print(f"Мы полностью не уверены, но может это ваше любимое блюдо: '{dish[0]}'.")
            else:
                return print(f"Вы тот, кому ничего не нравиться :(")
            
def start():
    # Открытие и чтение JSON-файла
    with open('C:/Users/N_OFFICE_5/Desktop/Новая папка/Новая папка (2)/Новая папка/react/py/product.json', 'r', encoding='utf-8') as file:
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