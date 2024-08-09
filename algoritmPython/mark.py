# Функция, которая приветсвует пользователя
# Передает блюда во вторую функцию и запускает ее

def start():
    print('Приветсвую, пользователь!', end = '\n')
    ansver_users = input('Хотите узнать свое любимое блюдо? Напишите "+", если согласны ')
    match ansver_users:
        case '+':
            startQuestion(massiv_dishes)
        case _:
            print('Отключение')

# Функция, которая начинает опрос и считает проценты
def startQuestion(ms_dishes):
    question = []
    for i in ms_dishes:
        for j in i['ingridiens']:
            if j not in question:
                question.append(j)

    k = 0
    ing = 0
    s = 0
    procent = 0
    bl_80procent = []
    massiv_dish = []
    massiv_slovar = []
    for i in ms_dishes:
        massiv_slovar.append(i)
    while question != []:
        ing -= k
        grade_user = int(input(f"Насколько вы любите: {question[ing]}, От 1 до 5 \n"))
        for slov in massiv_slovar:
            if question[ing] == slov['ingridiens']:
                massiv_dish.append(slov['name'])

        match grade_user:
            case 5:
                procent = 20
                value = question[ing]
                question.pop(ing)
            case 4:
                procent = 15
                value = question[ing]
                question.pop(ing)
            case 3:
                procent = 10
                value = question[ing]
                question.pop(ing)
            case 2:
                procent = 5
                value = question[ing]
                question.pop(ing)
            case 1:
                procent = 0
                value = question[ing]
                question.pop(ing)
            case _:
                print('Неверная оценка!')
                value = ''

        sek = []
        procenti = 0
        for i in massiv_slovar:
            for j in range(len(i)):
                if j >= len(i):
                    j = -1
                if i['ingridiens'][j] == value:
                    bl = i['name']
                    sek.append(bl)

        while sek != []:
            for i in massiv_slovar:
                print(i)
                if i['name'] == sek[0]:
                    procenti = i['procent']
                    procent = (100 / len(i['ingridiens'])) / 5 * grade_user
                    print(len(i['ingridiens']), procent)
                    procenti += procent
                    i['procent'] = procenti
                    print(massiv_dishes)
            sek.pop(0)

        for pr in massiv_slovar:
            if pr['procent'] >= 80 and question == [] and pr['name'] not in bl_80procent:
                bl_80procent.append(pr['name'])

    if len(bl_80procent) == 0:
        print('Вы не любите ни одно из блюд')
        print(massiv_dishes)
    else:
        print(massiv_dishes)
        if len(bl_80procent) == 1:
            print(f'Вы любите блюдо: {bl_80procent[0]}')
        else:
            name_first = bl_80procent[0]
            double_procent = []

            for i in massiv_dishes:
                if i['name'] == name_first:
                    double_procent.append[i['procent']]
                    
            if double_procent == 2:
                if double_procent[0] > double_procent[1]:
                    print(f'Вы любите блюдо: {bl_80procent[0]}')
                else:
                    maks = double_procent[0]
                    for i in double_procent:
                        if i > maks:
                            maks = i
                        if i == maks:
                            print('Вам могут понравится несколько блюд:', *bl_80procent)
            

massiv_dishes = [
    {
        'name': 'Пицца', 
        'ingridiens': ['Сыр', 'Колбаса', 'Майонез', 'Лук', 'Грибы'],'procent': 0 
    },
    {
        'name': 'Салат', 
        'ingridiens': ['Капуста', 'Помидоры', 'Огурцы', 'Майонез'],
        'procent': 0 
    },
    {
        'name': 'Суп', 
        'ingridiens': ['Картошка', 'Лук', 'Марковка', 'Мясо'],
        'procent': 0 
    },
    {
        'name': 'Борщ', 
        'ingridiens': ['Свекла', 'Картошка', 'Зелень', 'Марковка'],
        'procent': 0 
    },
    {
      "name": "Омлет",
      "ingridiens": ["Яйца", "Молоко", "Сыр", "Помидоры"],
      "procent": 0
    },
    {
      "name": "Картофель фри",
      "ingridiens": ["Картошка", "Соль", "Масло"],
      "procent": 0
    }
]

start()