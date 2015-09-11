import statsmodels.api as sm
import pandas as pd
from patsy import dmatrices

df = pd.DataFrame().from_csv("marketing_data.csv")

y, X = dmatrices('open_rate ~ email_address + first_last_name + formal_casual_subject + name_present + subject_line + time_of_day', data=df, return_type='dataframe')

lm = sm.OLS(y,X)
result = lm.fit()
print result.summary()
