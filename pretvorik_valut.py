import bottle
import model 
from model import currencies, history, Convert
 

@bottle.get("/")
def login_get(): 
    return bottle.template('zacetna-stran.html', error='')

@bottle.post('/')
def login_post():
    return bottle.redirect("/convert/")


@bottle.get('/convert/')
def converted_get():
    return bottle.template("pretvornik.html", currencies = currencies, value=None, curr1=None,curr2=None,res=None,history=history)

@bottle.post('/convert/')
def converted_post():
    value = float(bottle.request.forms["value"])
    curr1 = bottle.request.forms["curr1"]
    curr2 = bottle.request.forms["curr2"]
    if  value is not None and curr1 is not None  and curr2 is not None:
        res = Convert(value,curr1,curr2).converted()
        return bottle.template("pretvornik.html", currencies = currencies, value=value,curr1= curr1, curr2 = curr2,res=res, history=history)
    else:
        return bottle.redirect("/convert/")
    

bottle.run(debug=True, reloader=True)







