def start(): 
    print('Приветсвую, пользователь!', end = '\n') 
 
    ansver_users = input('Хотите узнать свое любимое блюдо? Напишите "+", если согласны ') 
    match ansver_users: 
        case '+': 
            startQuestion(massiv_b, massiv, massiv_ingrediens) 
 
        case _: 
            print('Отключение') 
 
def startQuestion(ms_b, ms, ms_i): 
    question = [] 
 
    for i in range(len(ms_i) - 1): 
        for j in ms_i[i]: 
            if j not in question: 
                question.append(j) 
     
    print(question) 
 
     
     
    k = 0 
    i = 0 
    while True: 
        i -= k 
        print(k) 
        print(i) 
        grade_user = int(input(f"Насколько вы любите: {question[i]}, От 1 до 5 \n")) 
        value = question[i] 
        match grade_user: 
             
            case 5: 
                procent = 20 
            case 4: 
                procent = 15 
            case 3: 
                procent = 10 
            case 2: 
                procent = 5 
            case 1: 
                procent = 0 
        sek = [] 
        for i in range(len(ms_b)): 
            for key in ms_b: 
                if ms_b[key][i] == value: 
                    sek.append(key) 
        for i in range(len(sek)): 
            ms_b[sek[i]][-1] += procent 
         
        print(grade_user) 
        if grade_user < 1 or grade_user > 5: 
            print('Неверная оценка!') 
            k = 1 
        else: 
            k = 0 
            i += 1 
            if question[i] == question[-1]: 
                break 
            else: 
                i += 1 
 
 
 
         
 
                 
 
             
 
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