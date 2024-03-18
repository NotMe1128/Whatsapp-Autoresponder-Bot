
import json

from flask import Flask, request, jsonify

#import socket

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])

def handle_webhook():

    try:

        # receive json

        data = request.get_json()
        print(data)
        sender = data['query']['sender']

        message = data['query']['message']

        
        #server_ip = socket.gethostbyname(socket.gethostname())

        # Process the request (you can customize this logic)

        reply1 = "Example reply 1"

        reply2 = "Example reply 2"

    

        response_data = {

            "replies": [{"message": reply1}, {"message": reply2}]    

        }

     
        #print(f"Server IP address: {server_ip}")

        return jsonify(response_data), 200

    except Exception as e:
        print(e)
        return str(e), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=2574,debug=True)
    
    
    
