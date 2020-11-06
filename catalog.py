from flask import Flask
from flask_restful import Api, Resource



app = Flask(__name__)
api = Api(app)
books = [["How-to-get-a-good-grade-in-DOS-in-20-minutes-a-day" , "distributed systems" , "20" , "7","1"],["RPCs for Dummies","distributed systems","25","4","2"],["Xen and the Art of Surviving Graduate School","graduate school","10","8", "3"],["Cooking for the Impatient Graduate Student","graduate school","40","3", "4"]]


class search(Resource):
    def get(self, type):

        s=""
        for p in range(4):
            if books[p][1]==type:
               s=s+"title : "+ books[p][0]+" , "
               s=s+"id : " +books[p][4]+" , "


        return{"books":s}
class lookup(Resource):
    def get(self, id):
        s=""
        for p in range(4):
            if books[p][4]==str(id):
                s = s + "title : " + books[p][0] + " , "
                s = s + "stock : " + books[p][3] + " , "
                s = s + "price : " + books[p][2] + " , "
        return {"books": s}
api.add_resource(search, "/search/<string:type>")
api.add_resource(lookup,"/lookup/<int:id>")
if __name__ == "__main__":
    app.run(debug=True)
