import pandas as pd

df = pd.read_csv('test_data_has_null.CSV', encoding='cp949')
    
df.fillna("NULL", inplace=True)
new_df = df[df['나이'] != "NULL"] 
average = new_df['나이'].mean()
new_df['difference'] = abs(new_df['나이'] - average)
df = new_df.sort_values(by='difference')
nearest_10_rows = df.head(10)

# data = nearest_10_rows.to_dict('records')
# return JsonResponse({'dat': data})
