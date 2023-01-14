from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('data/loan_sanction_train.csv')
urban_loan_amount_male = df.loc[df['Property_Area'] == 'Urban'].loc[df['Gender'] == 'Male']['LoanAmount'].sum()
urban_loan_amount_female = df.loc[df['Property_Area'] == 'Urban'].loc[df['Gender'] == 'Female']['LoanAmount'].sum()
rural_loan_amount_male = df.loc[df['Property_Area'] == 'Rural'].loc[df['Gender'] == 'Male']['LoanAmount'].sum()
rural_loan_amount_female = df.loc[df['Property_Area'] == 'Rural'].loc[df['Gender'] == 'Female']['LoanAmount'].sum()
semiurban_loan_amount_male = df.loc[df['Property_Area'] == 'Semiurban'].loc[df['Gender'] == 'Male']['LoanAmount'].sum()
semiurban_loan_amount_female = df.loc[df['Property_Area'] == 'Semiurban'].loc[df['Gender'] == 'Female']['LoanAmount'].sum()

graduate_income = df.loc[df['Education'] == 'Graduate']['CoapplicantIncome'].sum()
non_graduate_income = df.loc[df['Education'] == 'Not Graduate']['CoapplicantIncome'].sum()
total_income = graduate_income + non_graduate_income

labels = ['Graduate', 'Not Graduate']

sizes = [graduate_income,non_graduate_income]


names = ['Urban Male', 'Urban Female', 'Rural Male', 'Rural Female', 'Semi Male', 'Semi Female']
loan_amount = [urban_loan_amount_male, urban_loan_amount_female, rural_loan_amount_male, rural_loan_amount_female, semiurban_loan_amount_male, semiurban_loan_amount_female]

plt.figure(figsize=(10, 10))
plt.subplot(211)
plt.bar(names, loan_amount)
plt.suptitle('Loan Amount Male vs Female')
plt.subplot(212)
plt.bar(labels, sizes)
plt.suptitle('Loan Amount Male vs Female')
# plt.savefig('img/loan-analysis.png', dpi=300)

plt.show()

print(df)