from flask import Flask, render_template, request
from joblib import load
import pandas as pd
import warnings 
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    Total_Stops = int(request.form.get('Total_Stops'))
    Route_1 = str(request.form.get('Route_1'))
    Route_2 = str(request.form.get('Route_2'))
    Route_3 = str(request.form.get('Route_3'))
    Route_4 = str(request.form.get('Route_4'))
    Route_5 = str(request.form.get('Route_5'))
    Air_India = int(request.form.get('Air_India'))
    GoAir = int(request.form.get('GoAir'))
    IndiGo = int(request.form.get('IndiGo'))
    Jet_Airways = int(request.form.get('Jet_Airways'))
    Jet_Airways_Business = int(request.form.get('Jet_Airways_Business'))
    Multiple_carriers = int(request.form.get('Multiple_carriers'))
    Multiple_carriers_Premium_economy = int(request.form.get('Multiple_carriers_Premium_economy'))
    SpiceJet = int(request.form.get('SpiceJet'))
    Vistara = int(request.form.get('Vistara'))
    Vistara_Premium_economy = int(request.form.get('Vistara_Premium_economy'))
    source_Kolkata = int(request.form.get('source_Kolkata'))
    source_Mumbai = int(request.form.get('source_Mumbai'))
    dest_Kolkata = int(request.form.get('dest_Kolkata'))
    dest_New_Delhi = int(request.form.get('dest_New_Delhi'))
    Journey_day = int(request.form.get('Journey_day'))
    Journey_month = int(request.form.get('Journey_month'))
    Dep_Time_hour = int(request.form.get('Dep_Time_hour'))
    Dep_Time_minute = int(request.form.get('Dep_Time_minute'))
    Arrival_Time_hour = int(request.form.get('Arrival_Time_hour'))
    Arrival_Time_minute = int(request.form.get('Arrival_Time_minute'))
    Duration_hours = int(request.form.get('Duration_hours'))
    Duration_mins = int(request.form.get('Duration_mins'))
    df_sample = pd.DataFrame({'Total_Stops': [Total_Stops], 'Route_1': [Route_1], 'Route_2': [Route_2], 'Route_3': [Route_3], 'Route_4': [Route_4],
                              'Route_5': [Route_5], 'Air India': [Air_India], 'GoAir': [GoAir],'IndiGo': [IndiGo], 'Jet Airways': [Jet_Airways],
                              'Jet Airways Business': [Jet_Airways_Business], 'Multiple carriers': [Multiple_carriers], 'Multiple carriers Premium economy': [Multiple_carriers_Premium_economy],'SpiceJet': [SpiceJet], 'Vistara': [Vistara],
                              'Vistara Premium economy': [Vistara_Premium_economy], 'source_Kolkata': [source_Kolkata], 'source_Mumbai': [source_Mumbai],'dest_Kolkata': [dest_Kolkata],
                              'dest_New Delhi': [dest_New_Delhi], 'Journey_day': [Journey_day], 'Journey_month': [Journey_month],'Dep_Time_hour': [Dep_Time_hour],
                              'Dep_Time_minute': [Dep_Time_minute], 'Arrival_Time_hour': [Arrival_Time_hour], 'Arrival_Time_minute': [Arrival_Time_minute],'Duration_hours': [Duration_hours], 'Duration_mins': [Duration_mins]})
    df_sample['Route_1'] = encoder_1.transform(df_sample['Route_1'])
    df_sample['Route_2'] = encoder_2.transform(df_sample['Route_2'])
    df_sample['Route_3'] = encoder_3.transform(df_sample['Route_3'])
    df_sample['Route_4'] = encoder_4.transform(df_sample['Route_4'])
    df_sample['Route_5'] = encoder_5.transform(df_sample['Route_5'])
    df_sample = df_sample.reindex(columns=col_names)
    output = round(float(model.predict(df_sample)[0]), 2)
    return render_template('predict.html', output= output)

if __name__  ==  '__main__':
    model = load('model.pkl')
    encoder_1 = load('encoder_1.pkl')
    encoder_2 = load('encoder_2.pkl')
    encoder_3 = load('encoder_3.pkl')
    encoder_4 = load('encoder_4.pkl')
    encoder_5 = load('encoder_5.pkl')
    col_names = load('column_names.pkl')
    app.run(debug=True)

