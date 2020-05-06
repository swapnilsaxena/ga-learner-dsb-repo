# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 

# code starts here
bank=pd.read_csv(path)

categorical_var=bank.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank.select_dtypes(include='number')
print(numerical_var)





# code ends here


# --------------
# code starts here
banks = bank.drop(columns = 'Loan_ID')

print(banks.isnull().sum())

bank_mode=banks.mode().iloc[0]

banks.fillna(bank_mode, inplace = True) 

banks.isnull().sum()
#code ends here


# --------------
# Code starts here

 #pd.pivot_table(df, values='D', index=['A', 'B'],columns=['C'], aggfunc=np.sum)
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed']
,values = 'LoanAmount',aggfunc=np.mean)

print(avg_loan_amount)
# code ends here



# --------------
# code starts here
#df[df['Legendary']==True]['Type 1'].value_counts().idxmax()

loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

loan_approved_nse = banks.loc[(banks.Self_Employed =='No') & (banks.Loan_Status == 'Y'),['Loan_Status']].count()
print(loan_approved_nse)

percentage_se = (loan_approved_se * 100/614)
percentage_se = percentage_se[0]
print(percentage_se)

percentage_nse = (loan_approved_nse * 100/614)
percentage_nse = percentage_nse[0]
print(percentage_nse)
# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)

#print(loan_term)

big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

#loan_groupby.head()

loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]

mean_values = loan_groupby.agg(np.mean)

#pokemon_stats_legendary=pokemon_stats.groupby(['Generation','Name'])[['Attack']].agg(np.mean).idxmax()[0]

# code ends here


