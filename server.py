
import json
import fun 
import searcher
import randfacts
import random
import database

from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])

def handle_webhook():

    try:
        data = request.get_json()
        #print(data)
        sender = data['query']['sender']
        message = data['query']['message']
        #print(message)
        if message[0:5]=="!calc":
        	reply1=fun.calculate_expression(message)
        elif message[0:6]=="!8ball":
        	reply1=fun.a8ball()
        elif message[0:6]=="!kinky":
            if message.endswith("!kinky"):
                user=sender
            else:
                words = message.split()
                user = words[1]
                print(user)
            reply1=fun.kinky(user)
        elif message[0:5]=="!fact":
            reply1=randfacts.get_fact(only_unsafe=False)
        elif message[0:7]=="!google":
            reply1=searcher.process_input(message)     
        elif message[0:7]=="!uptime":
            reply1=fun.uptime()
        elif message[0:9]=="!db query":
            reply1=database.process_request(message,sender)
        elif message[0:5] in ["!roll","!dice"]:
            reply1=fun.roll_dice(message[5:])
        else:
        	reply1 = "Unknown command. Type !help for a list of commmands."

  

    

        response_data = {

            "replies": [{"message": reply1}]    

        }

        return jsonify(response_data), 200

    except Exception as e:
        print(e)
        return str(e), 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=6563,debug=True)
    
    
    
