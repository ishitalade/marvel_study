# %%
pip install requests

# %%
pip install pandas as pd

# %%
#setting env and requesting API, parameters- marvel website, timestamp-5, hash-using ts, pvt key and public key
import pandas as pd
import requests
import json

# %%
# Activity 2- fetching characters
url = 'http://gateway.marvel.com/v1/public/characters?ts=5&apikey=dc614452a50241427e8f3cdec8a7b9b3&hash=2802d6fc5306949520459230887777e1'
limit = 100
COLUMN_NAMES = ['Character Name','Number of Event appearances','Number of Series appearances','Number of Stories appearances','Number of comics appearances', 'Character_id']
df = pd.DataFrame(columns = COLUMN_NAMES)
a = "%" #Instead of going through every character, we can use % to get all charecters
for nameStartsWith in a:
    print(nameStartsWith)
    final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}'
    output = requests.get(final_url)
    o = output.json()
    for i in range(o["data"]["count"]):
        char_list = o["data"]["results"]
        df2 = pd.DataFrame({
                'Character Name':char_list[i]["name"],
                'Number of Event appearances': char_list[i]["events"]["available"],
                'Number of Series appearances': char_list[i]["series"]["available"],
                'Number of Stories appearances': char_list[i]["stories"]["available"],
                'Number of Comics appearances': char_list[i]["comics"]["available"],
                'Character_id': char_list[i]["id"]
        },index = [i])
        df = pd.concat([df,df2])
    print(f'Before entering loop, df.shape[0] = {df.shape[0]}\n')
    n = o['data']['total']
    print(f'total characters = {n}')
    temp_n = n
    offset = 0
    while temp_n > limit:
        temp_n -= limit
        offset += limit
        final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}&offset={offset}'
        output = requests.get(final_url)
        o = output.json()
        for i in range(o["data"]["count"]):
            char_list = o["data"]["results"]
            df2 = pd.DataFrame({
                    'Character Name':char_list[i]["name"],
                    'Number of Event appearances': char_list[i]["events"]["available"],
                    'Number of Series appearances': char_list[i]["series"]["available"],
                    'Number of Stories appearances': char_list[i]["stories"]["available"],
                    'Number of Comics appearances': char_list[i]["comics"]["available"],
                    'Character_id': char_list[i]["id"]
            },index = [i+offset])
            df = pd.concat([df,df2])

df

# %%
# Activity 3- Function to generate dataframe with api inputs
def df_fun(hash, api, nameStartsWith):
    limit = 100
    COLUMN_NAMES = ['Character Name','Number of Event appearances','Number of Series appearances','Number of Stories appearances','Number of comics appearances', 'Character_id']
    df = pd.DataFrame(columns = COLUMN_NAMES)
    final_url = f'http://gateway.marvel.com/v1/public/characters?ts=5&apikey={api}&hash={hash}&nameStartsWith={nameStartsWith}&limit={limit}'
    output = requests.get(final_url)
    o = output.json()
    for i in range(o["data"]["count"]):
        char_list = o["data"]["results"]
        df2 = pd.DataFrame({
                'Character Name':char_list[i]["name"],
                'Number of Event appearances': char_list[i]["events"]["available"],
                'Number of Series appearances': char_list[i]["series"]["available"],
                'Number of Stories appearances': char_list[i]["stories"]["available"],
                'Number of Comics appearances': char_list[i]["comics"]["available"],
                'Character_id': char_list[i]["id"]
        },index = [i])
        df = pd.concat([df,df2])
    print(f'Before entering loop, df.shape[0] = {df.shape[0]}\n')
    n = o['data']['total']
    print(f'total characters = {n}')
    temp_n = n
    offset = 0
    while temp_n > limit:
        temp_n -= limit
        offset += limit
        final_url = f'{url}&nameStartsWith={nameStartsWith}&limit={limit}&offset={offset}'
        output = requests.get(final_url)
        o = output.json()
        for i in range(o["data"]["count"]):
            char_list = o["data"]["results"]
            df2 = pd.DataFrame({
                    'Character Name':char_list[i]["name"],
                    'Number of Event appearances': char_list[i]["events"]["available"],
                    'Number of Series appearances': char_list[i]["series"]["available"],
                    'Number of Stories appearances': char_list[i]["stories"]["available"],
                    'Number of Comics appearances': char_list[i]["comics"]["available"],
                    'Character_id': char_list[i]["id"]
            },index = [i+offset])
            df = pd.concat([df,df2])
    print(df)

df_fun('2802d6fc5306949520459230887777e1', 'dc614452a50241427e8f3cdec8a7b9b3', 'A')

# %%
# Activity 4- Function to filter characters based on conditions
def char_filter(df1, col, filter_condition):
    df1.columns = [column.replace(" ", "_") for column in df1.columns]
    col = col.replace(" ", "_")
    total_condition = col+ filter_condition
    res = df1.query(total_condition)
    return res

result = char_filter(df1 = df, col = 'Character Name',filter_condition = '.str.startswith("3")')
result

# %%
# Activity 5
apikey= input("Input the apikey:")
hash= input("Input the hash key:")
nameStartsWith=(input("Input the starting letter:")).upper()
df=df_fun(hash,apikey, nameStartsWith)
print(df)
df_ac5= char_filter(df1=df, col='Character Name', filter_condition='.str.startswith("a")')


