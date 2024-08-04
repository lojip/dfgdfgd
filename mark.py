def start():
    print('Приветсвую, пользователь!', end = '\n')

    ansver_users = input('Хотите узнать свое любимое блюдо? Напишите "+", если согласны ')
    match ansver_users:
        case '+':
            startQuestion(massiv_borsh, massiv_pizza, massiv_salat, massiv_sup, massiv_b, massiv, massiv_ingrediens)

        case _:
            print('Отключение')

def startQuestion(ms_bo, ms_p, ms_s, ms_su, ms_b, ms, ms_i):
    question = []

    for i in range(len(ms_i) - 1):
        for j in ms_i[i]:
            if j not in question:
                question.append(j)
    

    
    
    k = 0
    ing = 0
    s = 0
    procent = 0
    bl_80procent = []
    while s == 0:
        print(question)
        ing -= k
        grade_user = int(input(f"Насколько вы любите: {question[ing]}, От 1 до 5 \n"))
        # if grade_user < 1 or grade_user > 5:
        #     print('Неверная оценка!')
        #     k = 1
        #     s = 1
        #     break
        # else:
        #     k = 0
        #     if question[ing] == question[-1]:
        #         break
        #     else:
        #         ing += 1

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
        massiv_slovar = [ms_bo, ms_p, ms_s, ms_su]
        # for slovar in massiv_slovar:
        #     procenti.append(slovar['procent'])


        for i in massiv_slovar:
            for j in range(len(i)):
                if i['ingridiens'][j] == value:
                    bl = i['name']
                    sek.append(bl)
            for key_2 in range(len(sek)):
                for i in massiv_slovar:
                    if i['name'] == sek[key_2]:
                        procenti = i['procent']
                        procenti += procent
                        i['procent'] = procenti
        
        for pr in massiv_slovar:
            if pr['procent'] >= 80 and question == []:
                bl_80procent.append(pr['name'])
                s = 1
                break

    print(bl_80procent)

    if len(bl_80procent) == 1:
        print(f'Вы любите блюдо: {bl_80procent[0]}')




        # for i in range(len(ms_b)):
        #     for key in ms_b:
        #         if ms_b[key][i] == value:
        #             sek.append(key)
        # for i in range(len(sek)):
        #     ms_b[sek[i]][-1] += procent
        



        

                

            

massiv = ['Пицца', 'Салат', 'Суп', 'Борщ']
massiv_ingrediens = [
    ['Сыр', 'Колбаса', 'Майонез', 'Лук', 'Грибы'], 
    ['Капуста', 'Помидоры', 'Огурцы', 'Майонез'], 
    ['Картошка', 'Лук', 'Марковка', 'Мясо'], 
    ['Свекла', 'Картошка', 'Зелень', 'Марковка']
]

massiv_b = {'Пицца': ['Сыр', 'Колбаса', 'Майонез', 'Лук', 'Грибы', 0], 
            'Салат': ['Капуста', 'Помидоры', 'Огурцы', 'Майонез', 0], 
            'Суп': ['Картошка', 'Лук', 'Марковка', 'Мясо', 0],
            'Борщ': ['Свекла', 'Картошка', 'Зелень', 'Марковка', 0]}

massiv_pizza = {
    'name': 'Пицца', 
    'ingridiens': ['Сыр', 'Колбаса', 'Майонез', 'Лук', 'Грибы'],
    'procent': 0 
}

massiv_salat = {
    'name': 'Салат', 
    'ingridiens': ['Капуста', 'Помидоры', 'Огурцы', 'Майонез'],
    'procent': 0 
}

massiv_sup = {
    'name': 'Суп', 
    'ingridiens': ['Картошка', 'Лук', 'Марковка', 'Мясо'],
    'procent': 0 
}

massiv_borsh = {
    'name': 'Борщ', 
    'ingridiens': ['Свекла', 'Картошка', 'Зелень', 'Марковка'],
    'procent': 0 
}

start()