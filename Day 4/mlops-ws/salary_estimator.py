from sklearn.externals import joblib
salary_model=joblib.load("salary_model.pk1")


print("\t\t\tWelcome to future tools")
print("\t\t\t------------------------")
print()


while True:
	print("Press 1: salary predict")
	print("Press 2: predict new requirement")
	print("Press 3: cal score for current emp")
	print("Press 4: classfy score for current emp")
	print("Press 5: to exit")

	print("Enter your choice: " , end='')
	ch = input()


	if int(ch) == 1:
		print("Enter year Exp : " , end='')
		exp = input()
		exp = float(exp)
		print( "predicted salary : " , salary_model.predict(exp)[0] )

	elif int(ch) == 2:
		print("search new requirement")

	elif int(ch) == 3:
		print("cal")

	elif int(ch) == 4:
		print("cal")

	elif int(ch) == 5:
		exit()

	else:
		print("option not supported")

