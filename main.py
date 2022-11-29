from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

class DemoApiEndpoint(Resource):
    def __init__(self):
        self.post_args = reqparse.RequestParser()
        self.post_args.add_argument("name",
                                    type=str,
                                    help="You must include a name string with this post request.",
                                    required=True)
    def get(self):
        return {
            "message": "This is a response from a GET request."
        }

    def post(self):
        args = self.post_args.parse_args()
        name = args['name']
        return {
            "message": f'Nice to meet you, {name}!'
        }

api.add_resource(DemoApiEndpoint, "/api/DemoApiEndpoint")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)