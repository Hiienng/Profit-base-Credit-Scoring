import pandas as pd

# Đọc file .xlsx
df = pd.read_csv(r'C:\Users\hiennpd3\OneDrive - VPBank\AA Team\Mô hình Scorecard\hien-main\01. data\input\final_input.csv')
for col in df.columns:
    df[col] = df[col].astype(str)

# Define mapping rules

stream_7 = {
    '1. MC2': 'e',
    '2. Titanium' :'k',
    '3. Platinum':'q',
    '4. World':'t',
    '5. Visa Platinum':'h',
    '6. Visa Signature':'e',
    '7. Visa Gold':'r'

}

stream_9 = {
    'DIGITAL CARD': 1,
    'HHB CARD': 2,
    'JARVIS CARD': 3,
    'JARVIS CUSTOMER CARD': 4,
    'ONLINE CARD': 5,
    'RETAIL CARD': 6,
    'TIMO CARD': 7
}

stream_11 = {
    'ADDITIONAL CARD 247': 'a',
    'ADDITIONAL CARD FLG': 'b',
    'ADDITIONAL CARD PMC': 'c',
    'AUM': 'd',
    'CARD FOR CARD': 'e',
    'CARD FOR CARD FLG': 'f',
    'CASA': 'g',
    'HIGH LEVEL': 'h',
    'HOUSE OWNER': 'i',
    'INSURANCE': 'j',
    'LENDING HHB - CROSS SELL': 'k',
    'LENDING SECURED - BUNDLE': 'l',
    'LENDING SECURED - CROSS SELL': 'm',
    'LENDING UPL - CROSS SELL': 'n',
    'MOBILE CAMPAIGN - MOBIFONE': 'o',
    'MOBILE CAMPAIGN - TRUSTING SOCIAL': 'p',
    'NONE': 'q',
    'NORMAL SALARY': 'r',
    'OPEN MARKET': 's',
    'OTHER': 't',
    'PAYROLL': 'u',
    'PCB SURROGATE': 'v',
    'PERSONAL IMPROVEMENT': 'w',
    'PERSONAL IMPROVEMENT FLG': 'x',
    'SALARY GOV': 'y',
    'SHOPEE': 'z',
    'STAFF': 'aa',
    'TD': 'bb',
    'TEACHER': 'cc',
    'TRAVEL': 'dd',
    'VNA': 'ee'
}

stream_13 = {
    '1.<5M': 'a',
    '2.5M-10M': 'b',
    '3.10M-15M': 'c',
    '4.15M-40M': 'd',
    '5.40M-150M': 'e',
    '6.>=150M': 'f',
    'UNKNOWN': 'g'
}

stream_14 = {'FEMALE': 'a', 'MALE': 'b', 'OTHER': 'c'}

stream_15 = {
    'Divorced': 'a',
    'Married': 'b',
    'Other': 'c',
    'Single': 'd'
}

stream_16 = {
    'Intermediate/High school': 'a',
    'Junior college': 'b',
    'Others': 'c',
    'Postgraduate': 'd',
    'University': 'e',
    'Unknown': 'f'
}

stream_17 = {
    'An Giang': 'a',
    'Ba Ria - Vung Tau': 'b',
    'Bac Giang': 'c',
    'Bac Kan': 'd',
    'Bac Lieu': 'e',
    'Bac Ninh': 'f',
    'Ben Tre': 'g',
    'Binh Dinh': 'h',
    'Binh Duong': 'i',
    'Binh Phuoc': 'j',
    'Binh Thuan': 'k',
    'Ca Mau': 'l',
    'Can Tho': 'm',
    'Cao Bang': 'n',
    'Da Nang': 'o',
    'Dak Lak': 'p',
    'Dak Nong': 'q',
    'Dien Bien': 'r',
    'Dong Nai': 's',
    'Dong Thap': 't',
    'Gia Lai': 'u',
    'H': 'v',
    'HA GIANG': 'w',
    'Ha Nam': 'x',
    'Ha Noi': 'y',
    'Ha Tinh': 'z',
    'Hai Duong': 'aa',
    'Hai Phong': 'ab',
    'Hau Giang': 'ac',
    'Hoa Binh': 'ad',
    'Hung Yen': 'ae',
    'Khanh Hoa': 'af',
    'Kien Giang': 'ag',
    'Kon Tum': 'ah',
    'Lai Chau': 'ai',
    'Lam Dong': 'aj',
    'Lang Son': 'ak',
    'Lao Cai': 'al',
    'Long An': 'am',
    'N': 'an',
    'Nam Dinh': 'ao',
    'Nghe An': 'ap',
    'Ninh Binh': 'aq',
    'Ninh Thuan': 'ar',
    'Phu Tho': 'as',
    'Phu Yen': 'at',
    'Quang Binh': 'au',
    'Quang Nam': 'av',
    'Quang Ngai': 'aw',
    'Quang Ninh': 'ax',
    'Quang Tri': 'ay',
    'Soc Trang': 'az',
    'Son La': 'ba',
    'Tay Ninh': 'bb',
    'Thai Binh': 'bc',
    'Thai Nguyen': 'bd',
    'Thanh Hoa': 'be',
    'THI XA HONG LINH': 'bf',
    'Thua Thien - Hue': 'bg',
    'Tien Giang': 'bh',
    'TP Ho Chi Minh': 'bi',
    'Tra Vinh': 'bj',
    'Tuyen Quang': 'bk',
    'Vinh Long': 'bl',
    'Vinh Phuc': 'bm',
    'VN': 'bn',
    'Yen Bai': 'bo'
}

stream_19 = {'MASS': 'ab', 'MASS AF' :'at', 'PRIORITY': 'ag'}

stream_26 = {'Revolver':'qw', 'Spender':'tr'}

# Apply mapping rules
df['7'] = df['7'].map(stream_7)
df['9'] = df['9'].map(stream_9)
df['11'] = df['11'].map(stream_11)
df['13'] = df['13'].map(stream_13)
df['14'] = df['14'].map(stream_14)
df['15'] = df['15'].map(stream_15)
df['16'] = df['16'].map(stream_16)
df['17'] = df['17'].map(stream_17)
df['19'] = df['19'].map(stream_19)
df['26'] = df['26'].map(stream_26)

# Define the function to transform numbers to words and replace characters
def transform_value(value):
    num_to_word = {
        '0': 'a', '1': 'r', '2': 'b', '3': 'v', '4': 's',
        '5': 't', '6': 'l', '7': 'y', '8': 'm', '9': 'k'
    }
    return ''.join(num_to_word.get(digit, digit) for digit in value).replace('.', '/').replace(',', ')')

# Apply the transformation to all other columns
for col in df.columns:
    if col not in ['7','9', '11', '13', '14', '15', '16', '17', '19', '26']:
        df[col] = df[col].apply(transform_value)
df.to_json(r'C:\Users\hiennpd3\OneDrive - VPBank\AA Team\Mô hình Scorecard\hien-main\01. data\input\modified_data.json.gz', orient='records', compression='gzip')
##########################################################




cif	contract_number	acnt_contract_oid	issue_month	issue_date_ctr	unlock_date	product_group	contract_limit	bi_card_type	liab_limit	campaign_group	cus_income	income_tier	gender	marital_status	edu_level	province_city	age	cus_class	ovd_days	ovd_days_6m	ovd_days_12m	ovd_days_24m	ovd_days_36m	nhom_no_cic	revolver_group	nii_24m	nfi_24m	toi_24m	provision_24m	bad_flag
