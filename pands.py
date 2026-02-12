# text="madam"
# if text==text[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
import pandas as pd

df = pd.read_csv(r"C:\Users\nanic\Downloads\Cars_Data.csv")

df['valuable'] = "no"

df.loc[
    (df['wheel-base'] > 100) & (df['length'] > 100),
    'valuable'
] = "yes"


print(df.tail())
