Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your weight in kilograms: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("Your Body Mass Index is: ", BMI)
if(BMI>0):
	if(BMI<=16):
		print("You are severly underweight")
	elif(BMI<=18.5):
		print("You are underweight")
	elif(BMI<=25):
		print("You are a healthy weight")
	elif(BMI<=30):
		print("You are overweight")
	else: print("You are obese")
else:("Enter valid details")