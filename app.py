from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json

app = Flask(__name__)

# Setup Google Sheets connection
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_json = json.loads(os.environ['GOOGLE_CREDENTIALS_JSON'])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
client = gspread.authorize(creds)

# Open the sheet by name
sheet = client.open("Wren OI Waitlist").sheet1

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/waitlist', methods=['GET', 'POST'])
def waitlist():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Append to Google Sheet
        sheet.append_row([name, email, timestamp])

        return render_template('waitlist.html', success=True)

    return render_template('waitlist.html')

if __name__ == '__main__':
    app.run(debug=True)
