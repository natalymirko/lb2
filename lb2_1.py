try:
    file_read = open('auto.txt', 'r')
    contents = file_read.readlines()
    file_read.close()
    print('Всі автомобілі з файлу auto.txt:\n----------------------------------------')
    fin=[]
    for i in contents:
        fin.append(i.split(' '))
        print (i)
    print('----------------------------------------')
    rikn=int(input("Введіть початок діапазону (рік випуска) ->"))
    rikk=int(input("Введіть кінець діапазону (рік випуска) ->"))
    virobnik=input("Введіть частину назви виробника ->")
    print('----------------------------------------')     
    fout=[]
    for j in fin:
        if int(j[3])>=rikn and int(j[3])<=rikk and j[1].find(virobnik)>=0:
            fout.append(' '.join(j))
    file_write = open('auto_rez.txt','w')
    for j in fout:
        file_write.write(j)
    print("Результат пошуку знаходиться у файлі auto_rez.txt")
    file_write.close()
except:
    print("Помилка при відкриті файлу")
