import json
def filter_log_file(source,log_string,timestamp,level):
    l=[]
    print(type(source),source,log_string,timestamp,level)
    try:
        with open(source, 'r') as file:
            print(f"Contents of {source}:")
            for line in file:
                log_entry=eval(line)
                # Check if log entry matches the provided timestamp or log string
                for i in log_entry:
                    print(i)
                    if i['timestamp'] == timestamp and i['log_string'] == log_string and i['level']==level:
                        l.append(i)               
    except FileNotFoundError:
        print(f"Error: {source} not found")
    return l
# # Example usage
source='log2.log'
log_string='Failed to connect'
timestamp='2024-02-14T06:14:16.737960+00:00Z'
level='success'
print(filter_log_file(source,log_string,timestamp,level))
