
print("\t\033[1;32m     Made by \033[1;36mKWEL999#1155 \n\n")
print("""_______________________________
      ππ§ πΊπ°πΆ π΄π¦π­π¦π€π΅ (1) πΊπ°πΆ π€π’π― π§πͺπ―π₯ π€π¦π­π΄πͺπΆπ΄ π΅π° π§π’π©π³π¦π―π©π¦πͺπ΅ 
                    π£πΆπ΅ πͺπ§ πΊπ°πΆ π΄π¦π­π¦π€π΅ (2) πΊπ°πΆ π€π’π― π§πͺπ―π₯ π§π’π©π³π¦π―π©π¦πͺπ΅ π΅π° π€π¦π­π΄πͺπΆπ΄
___________________________________"""'')

def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(str(fahrenheit )+ " degree Fahrenheit")

def fahrenheit_to_celsius():
 	fahrenheit = float(input("Enter temperature in fahrenheit: "))
 	celsius = (fahrenheit - 32)/1.8
 	print(str(celsius) + " degree Celsius" )


select = input("Select:\n1-celsius_to_fahrenheit\n2-fahrenheit_to_celsius\nSelect:")

if select=="1":
	celsius_to_fahrenheit()
elif select=="2":
 	fahrenheit_to_celsius()
else:print("Select number")
