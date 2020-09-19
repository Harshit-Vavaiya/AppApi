from flask import Flask
from flask_restful import Api, Resource

students = {
    '142':{
        'name':"john Doe",
        'class': 'IT'
    }
}

app = Flask(__name__)

@app.route("/")
def home():
    return "Hellow world"
# api = Api(app)
# class Hello(Resource):
#     def get(self,id):
#         return students[id]
    
# api.add_resource(Hello,'/hello/<string:id>')
# if __name__ == "__main__":
#     app.run(debug=True)