import logging
import requests
from datetime import datetime
import queryLogs
import main
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
api_logger1 = logging.getLogger('api_logger1')
api_logger1.setLevel(logging.DEBUG)
api_file_handler1 = logging.FileHandler('log1.log')
api_file_handler1.setLevel(logging.DEBUG)
api_logger1.addHandler(api_file_handler1)
api_logger2 = logging.getLogger('api_logger2')
api_logger2.setLevel(logging.DEBUG)
api_file_handler2= logging.FileHandler('log2.log')
api_file_handler2.setLevel(logging.DEBUG)
api_logger2.addHandler(api_file_handler2)
api_logger3 = logging.getLogger('api_logger3')
api_logger3.setLevel(logging.DEBUG)
api_file_handler3= logging.FileHandler('log3.log')
api_file_handler3.setLevel(logging.DEBUG)
api_logger3.addHandler(api_file_handler3)
l1=[]
l2=[]
l3=[]
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        data = response.json()
        for i in data:
            if i["metadata"]["source"]=='log1.log':
                l1.append(i)
            
            elif i["metadata"]["source"]=='log2.log':
                l2.append(i)    
            elif i["metadata"]["source"]=='log3.log':
                l3.append(i)
        print(l1)
        print(l2)        
        print(l3)        

        api_logger1.info(l1)
        api_logger2.info(l2)
        api_logger3.info(l3)                
        return data
    except Exception as e:
        print("exception in fetch")
# Function to process data
def process_data(data):
    try:
        logging.info('Processing data...')
        # Simulate processing by printing data
        print(queryLogs.filter_log_file(main.source,main.log_string,main.timestamp,main.level))
        logging.info('Data processing completed successfully.')
    except Exception as e:
        logging.error('Error processing data: %s', str(e))

def main():
    # API URL
    api_url = 'http://127.0.0.1:5000/generate_logs'

    # Fetch data
    data = fetch_data(api_url)
    # process_data(data)
if __name__ == "__main__":
    main()
