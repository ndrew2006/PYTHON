#print ("Hello \nWorld!")
#name = "Андрей"
#age = 39
#print ("Привет, " + name)
#print ("Тебе - " + str(age) + " лет!")

#name = input ("Введите свое имя: ")
#print ("Ваше имя: " + name)

#import math

#a = 5.65

#print( math.ceil (a) )

i = 1000
while i > 100:
    print (i)
    i /= 2

for j in "Hello World":
    if j=="a":
        #continue # Пропускает одну итерацию (если встречается W то ее не выводит)
        break # Выход из цикла
    print(j*2, end="") # end="" - выводит все в одну строку.
else:
    print ("Буквы \"а\" нету в слове")