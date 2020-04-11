from sklearn.externals import joblib
model = joblib.load("salary_model.pk1")
print("Input the years of experience: ", end='')
exp = float(input())
print("Predicted Salary: ", model.predict([[exp]])[0])