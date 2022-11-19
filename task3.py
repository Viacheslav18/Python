def most_frequent(List): #Створюємо функцію most_frequent.
    cnt = 0
    word = "" #змінна word, де зберігаються слова.
    for i in List: #Цикл for.
        cur = List.count(i) #count() = повертає кількість елементів із вказаним значенням.
        if(cur > cnt) and (len(i) > 3): #Виводить слова, які мають більше 3 символів.
            cnt = cur
            word = i

    for i in range(List.count(word)): #count()повертає кількість елементів із вказаним значенням.
        mText.remove(word) #remove()видаляє вказаний елемент.
    return word, cnt #return полягає в тому, щоб вийти з функції та повернути значення.

while True: #Цикл While:

    program = input("\n [1] Топ 5 повторюваних слів\n [2] Словник\n [3] Топ 5 найдовших\n [→] Виберіть дію: ") #Просить вибрати, що виконає код.
    mText = input("\n [→] Введіть текст: ").split() #split() = Розбиває рядок на список.

    if program.lower() == "1": #Якщо користувач вводить 1, тоді спрацьовує цей код.
        print("\n Топ 5 повторюваних слів [↓]\n")
        for i in range(5): #Цикл for для range.
            p1, p2 = most_frequent(mText) #Використовується функція most_frequent.
            print(p1, p2) #Виводить топ 5 повторюваних слів.

    elif program.lower() == "2": #Якщо користувач вводить 2, тоді спрацьовує цей код.
        mText = set(mText) #set() = зберігає в собі елементи і не дає їм повторюватись.
        mText = list(mText) #list() = використовуються для зберігання кількох елементів в одній змінній.
        mText.sort() #sort() = сортує елементи списку в порядку зростання або спадання.
        print("\n Словник [↓]\n")
        for i in range(len(mText)): #Цикл for для range.
            if len(mText[i]) > 3: #Виводить слова, які мають більше 3 символів.
                print(mText[i]) #Виводить словник.

    elif program.lower() == "3": #Якщо користувач вводить 3, тоді спрацьовує цей код.
        mText = set(mText) #set() = зберігає в собі елементи і не дає їм повторюватись.
        mText = list(mText) #list() = використовуються для зберігання кількох елементів в одній змінній.
        mText.sort(reverse = True, key = len) #len() = повертає кількість елементів в об’єкті. Якщо об’єкт є рядком, len()функція повертає кількість символів у рядку.
        print("\n Топ 5 найдовших слів [↓]\n")
        for i in range(5): #Цикл for для range.
            print(mText[i], len(mText[i])) #Виводить топ 5 найдовших слів.

    else: #else
        print("\n [✘] Ви вибрали не правильну дію!") #Якщо жодна з дій не була вибрана, відображає це повідомлення.