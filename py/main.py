import random

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
                searchIngidient(random_ingredient)
            else:
                print("Пожалуйста, введите число от 1 до 5.")
                ingidient(random_ingredient)
        
        def searchIngidient(random_ingredient):
            print(f"Вы ввели данное значение: {random_ingredient}")


        ingidient(random_ingredient)
        break
        
 
def start():
    print('Приветсвую, пользователь!', end = '\n') 
 
    ansverUsers = input('Хотите узнать свое любимое блюдо? Напишите "+", если согласны ') 
    massivIngrediens = [
        ['Пицца', ['Сыр', 'Колбаса', 'Майонез', 'Лук', 'Грибы'], 0],  
        ['Салат', ['Капуста', 'Помидоры', 'Огурцы', 'Майонез'], 0],  
        ['Суп', ['Картошка', 'Лук', 'Марковка', 'Мясо'], 0], 
        ['Борщ', ['Свекла', 'Картошка', 'Зелень', 'Марковка'], 0]
    ]

    if(ansverUsers != '+'):
        return print('Отключение')

    startQuestion(massivIngrediens) 

start()