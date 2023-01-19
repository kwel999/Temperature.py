
print("\t\033[1;32m     Made by \033[1;36mKWEL999#1155 \n\n")
print("""_______________________________
      𝘐𝘧 𝘺𝘰𝘶 𝘴𝘦𝘭𝘦𝘤𝘵 (1) 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘧𝘪𝘯𝘥 𝘤𝘦𝘭𝘴𝘪𝘶𝘴 𝘵𝘰 𝘧𝘢𝘩𝘳𝘦𝘯𝘩𝘦𝘪𝘵 
                    𝘣𝘶𝘵 𝘪𝘧 𝘺𝘰𝘶 𝘴𝘦𝘭𝘦𝘤𝘵 (2) 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘧𝘪𝘯𝘥 𝘧𝘢𝘩𝘳𝘦𝘯𝘩𝘦𝘪𝘵 𝘵𝘰 𝘤𝘦𝘭𝘴𝘪𝘶𝘴
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
