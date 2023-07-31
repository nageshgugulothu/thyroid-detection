
from pymongo import MongoClient

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        try:
            data = CustomData(
                 age=float(request.form.get('age')),
                TSH=float(request.form.get('TSH')),
                T3=float(request.form.get('T3')),
                TT4=float(request.form.get('TT4')),
                T4U=float(request.form.get('T4U')),
                FTI=float(request.form.get('FTI')),
                sex=request.form.get('sex'),
                on_thyroxine=request.form.get('on_thyroxine'),
                query_on_thyroxine=request.form.get('query_on_thyroxine'),
                on_antithyroid_medication=request.form.get('on_antithyroid_medication'),
                sick=request.form.get('sick'),
                pregnant=request.form.get('pregnant'),
                thyroid_surgery=request.form.get('thyroid_surgery'),
                I131_treatment=request.form.get('I131_treatment'),
                query_hypothyroid=request.form.get('query_hypothyroid'),
                query_hyperthyroid=request.form.get('query_hyperthyroid'),
                lithium=request.form.get('lithium'),
                goitre=request.form.get('goitre'),
                tumor=request.form.get('tumor'),
                hypopituitary=request.form.get('hypopituitary'),
                psych=request.form.get('psych')
            )

            # Connect to MongoDB and retrieve data
            client = MongoClient("<YOUR_MONGODB_URI>")
            db = client["your_database_name"]
            collection = db["your_collection_name"]
            data_from_mongo = collection.find()

            # Process the data from MongoDB as needed
            # For example, you can convert it to a DataFrame
            df = pd.DataFrame(data_from_mongo)


        except Exception as e:
            raise CustomException(e, sys)
