# Adiciona colunas e seus valores em um arquivo CSV
# Atualiza os values de uma coluna em um arquivo CSV

import pandas as pd

# EXTRACT
csv_file_name = 'bootcamp_santander_1.csv'
df = pd.read_csv(csv_file_name, sep = ';')

# TRANSFORM - Adiciona colunas e seus valores em um arquivo CSV
# Recebe um arquivo CSV com as colunas e valores a serem adicionados
def add_column_csv_file(filename, df_add_columns):
  df_new_columns = pd.read_csv(filename, sep = ';')
  new_columns = df_new_columns.columns.tolist()

  for column in new_columns:
    col_values = df_new_columns[f'{column}'].tolist()
    df_add_columns[f'{column}'] = col_values
  
  # LOAD
  df_add_columns.to_csv(csv_file_name, index=False, sep = ';')

add_column_csv_file('investment_balance.csv', df)

# TRANSFORM - Atualiza os valores em um arquivo CSV
# Recebe um arquivo CSV com as colunas e valores a serem atualizados
def update_csv_column(filename, df_upate_col_values):
  df_new_col_values = pd.read_csv(filename, sep = ';')
  columns_name = df_new_col_values.columns.tolist()
   
  user_id_col_name = columns_name[0]
  users_id = df_new_col_values[f'{user_id_col_name}'].tolist()

  for i in range(1, len(columns_name)):
    col_name = columns_name[i]
    new_values = df_new_col_values[f'{col_name}'].tolist()
    j = 0
    for user in users_id:
      user_indice = df[df[f'{user_id_col_name}'] == user].index
      df.loc[user_indice, col_name] = new_values[j]
      j += 1

  #LOAD
  df_upate_col_values.to_csv(csv_file_name, index=False, sep = ';')


add_column_csv_file('investment_balance.csv', df)

update_csv_column('new_balances.csv', df)
