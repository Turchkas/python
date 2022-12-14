from random import choice

world_list = ['Автомобиль', 'Баклажан', 'Свекла', 'Мандарин', 'Апельсин', 'Хурма', 'Скрупулезность', 'Педантичность', 'Гомеостаз', 'Инбридинг', 'Сногсшибательность', 'Фрустрация', 'Напыщенность', 'Кропотливость', 
'Гидрокарбонат', 'Поясница', 'Болтушка', 'Скарабей', 'Калабалык', 'Уныние', 'Талия', 'Стамеска', 'Клозет', 'Толерантность', 'Эксгумация', 'Либерализм', 'Экспонат', 'Пышность', 'Скабрёзность', 'Шаловливость', 
'Экспозиция', 'Индульгенция', 'Контрацептив', 'Шкворень', 'Эпиграф', 'Эпитафия', 'Барбекю', 'Жульен', 'Энцефалопатия', 'Парашютист', 'Импозантность', 'Индифферент', 'Демультипликатор', 'Педикулёз', 'Выхухоль', 
'Россомаха', 'Сущность', 'Поэтапность', 'Напыщенность', 'Возвышенность', 'Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель', 'Знак', 'Фильтр', 'Башня', 'Кондитер', 'Омар', 'Чан', 'Пламя', 'Банк', 'Тетерев',
'Муж', 'Камбала', 'Груз', 'Кино', 'Лаваш', 'Калач', 'Геолог', 'Бальзам', 'Бревно', 'Жердь', 'Борец', 'Самовар', 'Карабин', 'Подлокотник', 'Барак', 'Мотор', 'Шарж', 'Сустав', 'Амфитеатр', 'Скворечник', 'Подлодка', 
'Затычка', 'Ресница', 'Спичка', 'Кабан', 'Муфта', 'Синоптик', 'Характер', 'Мафиози', 'Фундамент', 'Бумажник', 'Библиофил', 'Дрожжи', 'Казино', 'Конечность', 'Пробор', 'Дуст', 'Комбинация', 'Мешковина', 'Процессор',
'Крышка', 'Сфинкс', 'Пассатижи', 'Фунт', 'Кружево', 'Агитатор', 'Формуляр', 'Прокол', 'Абзац', 'Караван', 'Леденец', 'Кашпо', 'Баркас', 'Кардан', 'Вращение', 'Метрдотель', 'Клавиатура', 'Радиатор', 'Сегмент', 
'Обещание', 'Магнитофон', 'Кордебалет', 'Заварушка']

print('Давайте играть в угадайку слов!')

def get_world(world_list):
    return choice(world_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play():
    word = get_world(world_list)
    tries = 6 
    guessed_words = []
    word_completion = '_' * len(word) 
    print(display_hangman(tries))
    print(word_completion)
    print('Введите букву')
    while '_' in word_completion and tries!=0:
      c = input().upper()
      if c in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
         if c in word:
            if c not in guessed_words:
               guessed_words.append(c)
               for i in range(len(word)):
                  if c==word[i]:
                     word_completion = word_completion[:i] + c + word_completion[i+1:]
                     if '_' not in word_completion:
                        print('Поздравляем, вы угадали слово! Вы победили!')
            else:
               print('Ты уже пробовал эту букву')
         else:
            if c not in guessed_words:
               guessed_words.append(c)
               tries -= 1
               print(display_hangman(tries))
            else:
               print('Ты уже пробовал эту букву')
            if tries==0:
                  print('Ты проиграл, загаданное слово -', word)
      else:
         print('Вводи ТОЛЬКО русские буквы')
      print(word_completion)

flag = True
while flag==True:
   play()
   print('\nЗакончим на этом? Вводи да/нет, yes/no, y/n в любом регистре')
   s = input() 
   while s.lower() not in ('no', 'нет', 'n'):
      if s.lower() in ('да', 'yes', 'y'):
         flag = False
         break
      else:
         print('Повтори?')
         s = input()


