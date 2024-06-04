import pandas as pd

df = pd.read_csv(r'C:\Users\hiennpd3\OneDrive - VPBank\AA Team\Mô hình Scorecard\hien-main\01. data\input\final_input.csv')
for col in df.columns:
    df[col] = df[col].astype(str)
num_to_word = {
    '0': 'u', '1': 'g', '2': 'h', '3': 'r', '4': 'a',
    '5': 'y', '6': 'd', '7': 'seven', '8': 'c', '9': '*','.': '/'
}
word_to_num = {v: k for k, v in num_to_word.items()}
for col in df.columns:
    df[col] = df[col].apply(lambda x: ''.join(num_to_word.get(digit, digit) for digit in x))
    df[col] = df[col].apply(lambda x: ''.join(word_to_num.get(word, word) for word in x.lower().split()))
df.to_json('modified_data.json', orient='records')
