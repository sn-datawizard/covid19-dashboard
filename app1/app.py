import requests
import pandas as pd
from google.cloud import storage


url = 'https://api.corona-zahlen.org/vaccinations/states'
response = requests.get(url)
result = response.json()['data']

df = pd.DataFrame.from_dict(result, orient='index')
l_index = df.index.values.tolist()

l_total = []

l_vacc1_total = []
l_vacc1_biontech = []
l_vacc1_moderna = []
l_vacc1_astraZeneca = []
l_vacc1_janssen = []
l_vacc1_novavax = []

l_vacc2_total = []
l_vacc2_biontech = []
l_vacc2_moderna = []
l_vacc2_astraZeneca = []
l_vacc2_janssen = []
l_vacc2_novavax = []

l_vacc3_total = []
l_vacc3_biontech = []
l_vacc3_moderna = []
l_vacc3_astraZeneca = []
l_vacc3_janssen = []
l_vacc3_novavax = []

l_vacc4_total = []
l_vacc4_biontech = []
l_vacc4_moderna = []
l_vacc4_astraZeneca = []
l_vacc4_janssen = []
l_vacc4_novavax = []

for state in l_index:
    l_total.append(result[state]['administeredVaccinations'])
    
    l_vacc1_total.append(result[state]['vaccinated'])
    l_vacc1_biontech.append(result[state]['vaccination']['biontech'])
    l_vacc1_moderna.append(result[state]['vaccination']['moderna'])
    l_vacc1_astraZeneca.append(result[state]['vaccination']['astraZeneca'])
    l_vacc1_janssen.append(result[state]['vaccination']['janssen'])
    l_vacc1_novavax.append(result[state]['vaccination']['novavax'])

    l_vacc2_total.append(result[state]['secondVaccination']['vaccinated'])
    l_vacc2_biontech.append(result[state]['secondVaccination']['vaccination']['biontech'])
    l_vacc2_moderna.append(result[state]['secondVaccination']['vaccination']['moderna'])
    l_vacc2_astraZeneca.append(result[state]['secondVaccination']['vaccination']['astraZeneca'])
    l_vacc2_janssen.append(result[state]['secondVaccination']['vaccination']['janssen'])
    l_vacc2_novavax.append(result[state]['secondVaccination']['vaccination']['novavax'])

    l_vacc3_total.append(result[state]['boosterVaccination']['vaccinated'])
    l_vacc3_biontech.append(result[state]['boosterVaccination']['vaccination']['biontech'])
    l_vacc3_moderna.append(result[state]['boosterVaccination']['vaccination']['moderna'])
    l_vacc3_astraZeneca.append(result[state]['boosterVaccination']['vaccination']['astraZeneca'])
    l_vacc3_janssen.append(result[state]['boosterVaccination']['vaccination']['janssen'])
    l_vacc3_novavax.append(result[state]['boosterVaccination']['vaccination']['novavax'])

    l_vacc4_total.append(result[state]['2ndBoosterVaccination']['vaccinated'])
    l_vacc4_biontech.append(result[state]['2ndBoosterVaccination']['vaccination']['biontech'])
    l_vacc4_moderna.append(result[state]['2ndBoosterVaccination']['vaccination']['moderna'])
    l_vacc4_astraZeneca.append(result[state]['2ndBoosterVaccination']['vaccination']['astraZeneca'])
    l_vacc4_janssen.append(result[state]['2ndBoosterVaccination']['vaccination']['janssen'])
    l_vacc4_novavax.append(result[state]['2ndBoosterVaccination']['vaccination']['novavax'])


mydf = pd.DataFrame(list(zip(l_index, l_total,l_vacc1_total,l_vacc1_biontech,l_vacc1_moderna,l_vacc1_astraZeneca,l_vacc1_janssen,l_vacc1_novavax,l_vacc2_total,l_vacc2_biontech,l_vacc2_moderna,l_vacc2_astraZeneca,l_vacc2_janssen,l_vacc2_novavax,l_vacc3_total,l_vacc3_biontech,l_vacc3_moderna,l_vacc3_astraZeneca,l_vacc3_janssen,l_vacc3_novavax,l_vacc4_total,l_vacc4_biontech,l_vacc4_moderna,l_vacc4_astraZeneca,l_vacc4_janssen,l_vacc4_novavax)), columns = ['State','Total','Total1','Biontech1','Moderna1','AstraZeneca1','Janssen1','Novavax1','Total2','Biontech2','Moderna2','AstraZeneca2','Janssen2','Novavax2','Total3','Biontech3','Moderna3','AstraZeneca3','Janssen3','Novavax3','Total4','Biontech4','Moderna4','AstraZeneca4','Janssen4','Novavax4'])
#mydf['AstraZeneca4'] = mydf['AstraZeneca4'].fillna('0').astype('int64')
print(mydf)
mydf.to_csv('./data.csv', sep=';', index=False)

client = storage.Client.from_service_account_json('./sns-covid-gcp-b6475c6924f9.json')
#buckets_list = list(client.list_buckets())
#print(buckets_list)
bucket = client.get_bucket('covid-gcp-bucket1')

blob = bucket.blob('data') #Target path
blob.upload_from_filename('./data.csv') #Source path

print(blob.public_url)
print('Upload successfull')