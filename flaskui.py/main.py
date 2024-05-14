from flask import Flask,render_template,request
from datetime import datetime,timedelta,timezone
import queryLogs
import random
app=Flask(__name__)
    
current_datetime = datetime.now(timezone.utc)
three_months_ago = current_datetime - timedelta(days=3*30) 
timestamp = three_months_ago.isoformat() + 'Z'
@app.get('/generate_logs')
async def generate_logs():
    logs = []
    for _ in range(100):
        log_data = {
            "level": random.choice(["info", "error", "success"]),
            "log_string": random.choice(["Inside the Search API","Failed to connect"]),
            "timestamp":timestamp,
            "metadata": {
                "source": random.choice(["log1.log","log2.log","log3.log"])
            }
        }
        logs.append(log_data)
    return logs
@app.route('/home')
def home():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    source = request.form['source']
    log_string = request.form['log_string']
    timestamp = request.form['timestamp']
    level = request.form['level']
    l= queryLogs.filter_log_file(source,log_string,timestamp,level)
    print(f"Source: {source}")
    print(f"Log String: {log_string}")
    print(f"Timestamp: {timestamp}")
    print(f"Level: {level}")
    return l


if __name__=='__main__':
    # print(queryLogs.filter_log_file('log2.log','Failed to connect','2024-02-14T06:14:16.737960+00:00Z','success'))
    app.run(debug=True)