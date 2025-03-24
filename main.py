import pandas as pd

from modules.driver import quit_driver, setup_driver
from modules.login import login

df = pd.read_excel('company_list.xlsx')
driver = setup_driver()
i = 0
df['STATUS'] = ''

for index, row in df.iterrows():

    nif = row['NIF']
    password = row['PASSWORD']

    print(f'Tentando login para NIF: {nif}')
    status = login(driver, nif, password)
    df.at[index, 'STATUS'] = status
    i += 1
    if i % 10 == 0:
        df.to_excel('company_list_output.xlsx', index=False)

df.to_excel('company_list_output.xlsx', index=False)
print('Processo concluído. Status salvo no Excel.')
quit_driver(driver)
