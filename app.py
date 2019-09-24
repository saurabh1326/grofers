from flask import Flask,request, jsonify,Response
app = Flask(__name__)
from Get_Set_Grofers.models.db import store
import redis

red = redis.StrictRedis()
def event_stream():
    pubsub = red.pubsub()
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        print message
        yield 'data: %s\n\n' % message['data']

@app.route('/get/<string:key>' , methods = ['GET'])
def get(key):
    val  = store.get(key)
    print ("val",val)
    res = {
            "status" : "success",
            "msg" : "'{}' key not found".format(key)
        }
    if val is None:
        return jsonify(res)
    else:
        return jsonify({
            "status":"success",
            "key" : key,
            "val"  : val
        })

def validate_request(req):
    if 'key' in req and 'val' in req:
        return True
    return False


@app.route('/stream')
def stream():
    return Response(event_stream(),
                          mimetype="text/event-stream")

@app.route('/set' , methods = ['POST'])
def post():
    req =  request.get_json()
    if not validate_request(req):
        return {
            "status":"Faliure",
            "msg" : "Invalid Request"
        },400
    store[req['key']]=req['val']

    return {
        "status":"Success",
        "msg":"Set Successful"
    }

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
