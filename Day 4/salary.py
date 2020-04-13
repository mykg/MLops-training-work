from sklearn.externals import joblib
model = joblib.load("salary_model.pk1")

print("\n")
print("\t\t Welcome to future tools!")
print("\t\t ------------------------")
print("\n")

while True:
	print("Press 1: to predict salary")
	print("Press 2: exit")
	print("Enter your choice: ",end='')
	ch = input()

	if int(ch) == 1:

		print("Input the years of experience: ", end='')
		exp = float(input())
		print("Predicted Salary: ", model.predict([[exp]])[0])

	elif int(ch) == 2:
		exit()

	else:
		print("Option not supported yet!")