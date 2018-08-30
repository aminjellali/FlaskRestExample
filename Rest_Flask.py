''' This is a Rest Api Exemple  '''
''' A small Rest Api developed using Flask that serves the purpose of calculating the price including VAT from a list of objects '''
from flask import Flask,request
from flask_restful import Api, Resource



app = Flask(__name__)
api = Api(app)

items =  [{
'name':'Cola' ,
'price':3 ,
'TVA':30
}]
data = []

class Price (Resource):
    def get (self,name):
        itemSearch = next(iter(filter(lambda x: x['name']==name,items)),None)
        if itemSearch == None :
            return {'message':'no such item!'} , 400
        else :
            return {'name':name ,
            'price including TVA': itemSearch['price'] * (1+itemSearch['TVA']/100)
            } , 200

    def post (self,name):
        requestData = request.get_json()
        itemSearch = next(iter(filter(lambda x: x['name']==name ,items)),None)
        if itemSearch is not None :
            return {'message' : 'Item already exists'} , 400
        else :
            item = {'name':name,
            'price':requestData['price'],
            'TVA':requestData['TVA']}
            items.append(item)
            return {'item' : items}


class ItemsList(Resource):
    def get(self):
        list = []
        for item in items:
            list.append({
            'name' : item['name'],
            'price including TVA': item['price'] * (1+item['TVA']/100)
            })
        return {'Items' : list }


api.add_resource(Price,'/price/<string:name>')
api.add_resource(ItemsList,'/list')

app.run(port=9909,debug=True)
