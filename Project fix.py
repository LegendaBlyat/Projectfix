tasks=[]
def add_tasks():
        print('Ваш выбор: 1',
              '\nВведите текст задачи: ')
        add_task=input()
        tasks.append(add_task)
        print('Задача успешно добавлена!')
def view_tasks():
        print('Ваш выбор: 2',
              '\nСписок задач: ')
        for i, item in enumerate(tasks):
            print(i+1, item)
def delete_tasks():
    while True:
        print('Ваш выбор: 3',
            '\nВыберите номер задачи для удаления: ')
        for i, item in enumerate(tasks):
            print(i + 1, item)
        delete=int(input())
        if delete>i+1 or delete==0:
                print('Такого номера задачи не существует')
                continue

        else:
            tasks.pop(delete-1)
        print('Задача успешно удалена!')
        break

def main():
    while True:
        main = int(input('Выберите действие: '
                     '\n 1. Добавить задачу'
                     '\n 2. Просмотреть список задач '
                     '\n 3. Удалить задачу'
                     '\n 4. Выйти из программы'))
        if main==1:
            add_tasks()
        if main==2:
            view_tasks()
        if main==3:
            delete_tasks()
        if main==4:
            print('Программа завершена')
            quit()
main()



