import os
from dotenv import load_dotenv

load_dotenv()
environment = os.environ.get('ENV')
print(environment)
host = ''
if(environment.lower() == 'sqa'):
    host = 'acs-platform-o2c-cp-kafka-2:9092'
elif(environment.lower() == 'val'):
    host = 'acs-platform-qc-cp-kafka-0:9092'   
    #host = 'acs-platform-val-cp-kafka-0:9092'
elif(environment.lower() == 'prod'):
    host = 'acs-platform-ldt-kafka:9092'
else:
    print(f'wrong bootsrap value')

def produce_ivd_result_event():
    print(host)
    return {"Results":"Success"}
