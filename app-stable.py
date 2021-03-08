from flask import Flask, jsonify,request
from flask import Flask, jsonify, render_template, request
#from preprocess import cleaning
app = Flask(__name__)

#import sql python package
from flask_mysqldb import MySQL


#configure the database
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ".?Eh_YV'E2abuBs+"
app.config['MYSQL_DB'] = 'majorproject'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

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
    ground_truth = request.form.get("ground_truth", "")
    prediction = loaded_model.predict([string_input]);

    # store info in db for later use
    # inserting into the database
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO nepali_news (ground_truth, news_text, predicted) VALUES (%s,%s,%s)", (ground_truth, string_input,prediction[0]))
    mysql.connection.commit()
    cur.close()
    return render_template("result.html",result =prediction[0])

@app.route("/news", methods=["GET"])
def news():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM nepali_news where ground_truth=predicted")
    news = cur.fetchall()
    badge_color_map = {
        'health': 'badge-success',
        'literature': 'badge-secondary',
        'sports': 'badge-info',
        'entertainment': 'badge-primary',
        'opinion': 'badge-warning',
        'politics': 'badge-danger'
    }
    return render_template("news.html",news= news, badge_color_map=badge_color_map)


if __name__ == '__main__':
    app.run(port=5000, host= '0.0.0.0')
