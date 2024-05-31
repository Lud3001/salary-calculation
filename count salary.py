#file = open('file.txt' , 'r')
try:
    file = open('file.txt' , 'r')
except FileNotFoundError: 
    dict_count = {}
    print("Error, the file didn't open")
else:
    dict_count = {}
    for i in file: 
        month = i.split(' :') #  k[0] = month;
        dict_count[month[0]] = {} 
        w_s = month[1].split(' ;') # w_s ---- worker-salary
        for p in w_s:
            worker_id = p.split(' - ')
            try:
                worker_id[1] = float(worker_id[1])
            except ValueError:
                print(f'the salary data is input incoerrectly. It must be number, not string Check salaries: {worker_id}')
            else:
                dict_count[month[0]][worker_id[0]] = worker_id[1]

         

dict_people = {}

if len(dict_count) != 0:
    print(dict_count)
else:
    print('the form is empty')



# 1 - добавлять новых сотрудников
# 2 - рассчет средней зарплаты
months = ('January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December')
count = 0
while True:
    flag = True
    while flag:
        act = input('choose what you want to do: 1 is for filling the form; 2 is for giving the salary: ')
        try:
            act = int(act)
        except ValueError:
            print('not correct type, input number')
        else:
            flag = False
    if act == 1:
        flag_fill = True
        while flag_fill:
            month = input('write the month you work with: ').title()
            if month not in months:
                print('you input month wrong')
                continue
            worker = input("input the worker's name and surname: ").title()
            flag_salary = True
            while flag_salary:
                worker_salary = input("input worker's salary: ")
                try:
                    worker_salary = float(worker_salary)
                except ValueError:
                    print('not correct type, input number')
                else:
                    flag_salary = False
            if month not in dict_count:
                dict_count[month] = {worker : worker_salary}
            else:
                dict_count[month][worker] = worker_salary
            cont = input('would you like to continue? input "yes" or "no": ')
            if cont == 'no':
               print(dict_count)
               flag_fill = False    
    elif act == 2:
        
        
        for i in dict_count:
            for j in dict_count[i]:
                try:
                    dict_count[i][j] = float(dict_count[i][j])
                except ValueError:
                    print(f'Error: data input incorrectly, check {i} and {j}')
                else:
                    if j not in dict_people:
                        dict_people[j] = [dict_count[i][j]]
                        print(dict_people)       
                    else:
                        dict_people[j].append(dict_count[i][j])
    
    continue_cicle = input('would you like to cintinue? input "yes" or "stop"')
    if continue_cicle == 'yes':
        continue
    elif continue_cicle == 'stop':
        break
    
             


        
 

with open('file.txt' , 'w' , encoding='UTF-8') as accounant_file:
    for k in dict_count:
        accounant_file.write(k)
        accounant_file.write(' : ')
        for kk in dict_count[k]:
            accounant_file.write(kk)
            accounant_file.write(' - ')
            accounant_file.write(str(dict_count[k][kk]))
            accounant_file.write(' ; ')
        accounant_file.write('\n')


