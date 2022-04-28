import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

model1 = pickle.load(open('models/crop.pkl', 'rb'))
model2 = pickle.load(open('models/fertilizer.pkl', 'rb'))
model3 = pickle.load(open('models/life.pkl', 'rb'))
model4 = pickle.load(open('models/stroke.pkl', 'rb'))
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

#CROP RECOMMENDATION
@app.route("/crop", methods = ['GET'])
def crop():
    return render_template('crop.html')

@app.route('/croppredict', methods=['POST'])
def croppredict():
    if request.method == "POST":
        int_features = [float(x) for x in request.form.values ()]
        final_features = [np.array(int_features)]
        prediction = model1.predict(final_features)
        output = prediction[0]

        return render_template ('result.html', prediction_text=' The Recommended Crop to grow is {}'.format (output))

    else:
        return render_template('crop.html')

#FERTILIZER RECOMMENDATION
@app.route("/fertilizer", methods = ['GET'])
def fertilizer():
    return render_template('fertilizer.html')

@app.route('/fertilizerpredict', methods=['POST'])
def fertilizerpredict():
    temp_array = list ()
    if request.method == "POST":
        temp = int(request.form['Temparature'])
        humid = int(request.form['Humidity'])
        mois = int(request.form['Moisture'])
        nit = int(request.form['Nitrogen'])

        pho = int(request.form['Phosphorous'])
        temp_array = temp_array + [temp, humid, mois, nit, pho]

        soil_type = request.form['Soil-Type']
        if soil_type == 'Soil Type_Black':
            temp_array = temp_array + [1, 0, 0, 0, 0]
        elif soil_type == 'Soil Type_Clayey':
            temp_array = temp_array + [0, 1, 0, 0, 0]
        elif soil_type == 'Soil Type_Loamy':
            temp_array = temp_array + [0, 0, 1, 0, 0]
        elif soil_type == 'Soil Type_Red':
            temp_array = temp_array + [0, 0, 0, 1, 0]
        elif soil_type == 'Soil Type_Sandy':
            temp_array = temp_array + [0, 0, 0, 0, 1]

        crop_type = request.form['Crop-Type']
        if crop_type == 'Crop Type_Barley':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Cotton':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Ground Nuts':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Maize':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Millets':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Oil seeds':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Paddy':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif crop_type == 'Crop Type_Pulses':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif crop_type == 'Crop Type_Sugarcane':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif crop_type == 'Crop Type_Tobacco':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif crop_type == 'Crop Type_Wheat':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


        final_features = np.array([temp_array])
        prediction = model2.predict( final_features )
        output = prediction[0]

        return render_template ('result.html', prediction_text=' Recommended Fertilizer is {}'.format(output))
    else:
        return render_template('fertilizer.html')

#LIFE EXPECTANCY
@app.route("/life", methods = ['GET'])
def life():
    return render_template('life.html')

@app.route('/lifepredict', methods=['POST'])
def lifepredict():
    int_features = list ()
    if request.method == "POST":
        features = [int (x) for x in request.form.values()]
        final_features = np.array ([features] )
        prediction = model3.predict ( final_features )
        output = round (prediction[0], 2)

        return render_template ('result.html', prediction_text=' Your Life Expectancy is {}'.format (output))

    else:
        return render_template ('life.html')

#STROKE PREDICTION
@app.route("/stroke", methods = ['GET'])
def stroke():
    return render_template('stroke.html')

@app.route('/strokepredict', methods=['POST'])
def strokepredict():
    temp_array =list()
    if request.method== 'POST':
        age =int(request.form['age'])
        hype = int(request.form['hypertension'])
        heart = int(request.form['heart_disease'])
        glevel = int(request.form['avg_glucose_level'])
        bmi = int(request.form['bmi'])

        gender = request.form['Gender']
        if gender =='Female':
            temp_array= temp_array+[1,0]
        else:
            temp_array = temp_array + [0 , 1]

        marr = request.form['Martial Status']
        if marr=='Not Married':
            temp_array = temp_array + [1, 0]
        else:
            temp_array = temp_array + [0 , 1]

        govt = request.form['Work Type']
        if govt == 'Govt Job':
            temp_array = temp_array + [1,0,0,0,0]
        elif govt == 'Never Worked':
            temp_array = temp_array + [0, 1, 0, 0, 0]
        elif govt == 'Private Job':
            temp_array = temp_array + [0, 0, 1, 0, 0]
        elif govt == 'Self Employed':
            temp_array = temp_array + [0, 0, 0, 1, 0]
        elif govt == 'Student/Children':
            temp_array = temp_array + [0, 0, 0, 0, 1]


        rt = request.form['Residence Type']
        if rt=='Rural':
            temp_array = temp_array + [1, 0]
        else:
            temp_array = temp_array + [0 , 1]

        smk = request.form['Smoking Status']
        if smk == 'Dont want to Disclose':
            temp_array = temp_array + [1,0,0,0]
        elif smk == 'Formerly Smoked':
            temp_array = temp_array + [0, 1, 0, 0]
        elif smk == 'Never Smoked':
            temp_array = temp_array + [0, 0, 1, 0 ]
        elif smk == 'Smokes':
            temp_array = temp_array + [0, 0, 0, 1]


        temp_array = temp_array + [age , hype , heart , glevel , bmi]

        final_features = np.array([temp_array])
        prediction = model4.predict( final_features )
        output = prediction[0]

        if output == 0:
            output = 'You are less likely to get stroke'
        else:
            output = 'You are likely to get stroke'

        return render_template ( 'result.html', prediction_text='  {}'.format( output ) )

    else:
        return render_template ('stroke.html') 

if __name__ == "__main__":
    app.run(debug=True)