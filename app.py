from flask import Flask, jsonify,request
from flask import Flask, jsonify, render_template, request
#from preprocess import cleaning
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_two_nums',methods = ["POST"])
def add_two_nums():

    #Get x,y from the posted data
    dataDict = request.get_json()
    #Add z = x+y
    x = dataDict["x"]
    y = dataDict["y"]
    z = x+y
    #Prepare a JSON, "z":z
    retJSON = {
	"z" :z
	}
    #return jsonify(map_prepared)
    return jsonify(retJSON),200
    
# Model world
import pickle
#now we weill load the saved model
with open('mysaved_md_svc_smote', 'rb') as file:
    loaded_model = pickle.load(file)
    
#to make sure things work
#input_text = ['क्रान्तिसम्बन्धी विभिन्न लेख र अनुसन्धानमा भनिएको छ– माओवादीको दसवर्षे संघर्षले ‘सामाजिक क्रान्ति’ ल्याएन, राजनीतिक क्रान्तिचाहिँ ल्यायो । सामाजिक क्रान्ति तब मात्र भन्न मिल्छ, जब त्यस परिवर्तनले राज्य र समाजका सारा पुराना संरचना भत्काई नयाँ संरचना निर्माण गर्छ । राजनीतिक क्रान्तिले भने राजनीतिक व्यवस्थामा केही परिवर्तन ल्याउँछ तर सामाजिक संरचनामा खासै परिवर्तन ल्याउँदैन ।']

@app.route("/predict", methods=["POST"])
def makeprediction():
    string_input = request.form.get("string_input", "")
    prediction = loaded_model.predict([string_input]);
    return render_template("result.html",result =prediction[0])

if __name__ == '__main__':
     app.run(port=9000, debug=True)


