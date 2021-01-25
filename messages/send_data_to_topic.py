from time import sleep
from json import dumps
from kafka import KafkaProducer
import pandas as pd
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

local_path = 'C:\\Users\\hanna\\Desktop\\data\\ScadaData.txt'
scada_data = pd.read_csv(local_path, delimiter='\t',  parse_dates=True)
scada_data['dtTimeStamp'] = pd.to_datetime(scada_data['dtTimeStamp'])
start_index = 0
turbine_names = scada_data['intObjectId'].unique()[0:2]
filtered = scada_data[scada_data['intObjectId'].isin(turbine_names)]
number_of_turbines = len(turbine_names)
for e in range(0,int(len(scada_data)/number_of_turbines)):
    df_slice = filtered[start_index:start_index+number_of_turbines]
    df_slice.set_index('intObjectId', inplace=True)
    start_index += number_of_turbines  
    result = df_slice.to_json(orient="index", date_format='iso')
    data = json.loads(result)     
    producer.send('SMARTStop', value=data)
    sleep(20)
