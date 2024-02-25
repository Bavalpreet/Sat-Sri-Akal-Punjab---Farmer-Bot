from flask import Flask, request
from flask_restful import Resource, Api
import requests
import json
from googletrans import Translator

# global variables

## greeting examples
greetings_list = [
"hey",
"hello",
"hi",
"hii",
"hlo",
"hello there",
"good morning",
"good evening",
"moin",
"hey there",
"let's go",
"hey dude",
"goodmorning",
"goodevening",
"good afternoon",
]

## goodbye examples
good_bye_list = [
"cu",
"good by",
"cee you later",
"good night",
"bye",
"goodbye",
"have a nice day",
"see you around",
"bye bye",
"see you later",
"thank you",
"tq",
"thanku",
]

## could not understand template
could_not_understand = [
    {
        "recipient_id": "",
        "text": "I couldn't understand. Can you please rephrase it?",
        "buttons": [
                {
                    "payload": "",
                    "title": ""
            }
        ]
    }
]

## for storing the last sent message of user
last_query = ""

## bot endpoints dict
bot_urls_dict = {
    "chilli" : "http://localhost:5006/webhooks/rest/webhook",
    "chilli_pun" : "http://localhost:5007/webhooks/rest/webhook",
    "citrus" : "http://localhost:5008/webhooks/rest/webhook",
    "citrus_pun" : "http://localhost:5009/webhooks/rest/webhook",
    "garlic" : "http://localhost:5010/webhooks/rest/webhook",
    "garlic_pun" : "http://localhost:5011/webhooks/rest/webhook",
    "guava" : "http://localhost:5012/webhooks/rest/webhook",
    "guava_pun" : "http://localhost:5013/webhooks/rest/webhook",
    "pea" : "http://localhost:5014/webhooks/rest/webhook",
    "pea_pun" : "http://localhost:5015/webhooks/rest/webhook",
    "rice" : "http://localhost:5016/webhooks/rest/webhook",
    "rice_pun" : "http://localhost:5017/webhooks/rest/webhook",
    "wheat" : "http://localhost:5018/webhooks/rest/webhook",
    "wheat_pun" : "http://localhost:5019/webhooks/rest/webhook",
}

def send_request_to_bot(sender, query, bot_name):
    """
    This function is used to first create a payload using the `sender` and `query` arguments.
    Which are then sent as a post request to the bot_url of the concerned crop.
    Finally the response of the bot is returned.
    """
    payload = json.dumps(dict(sender=sender, message=query))
    r = requests.post( url=bot_urls_dict[bot_name], data=payload)
    # json_object = json.loads(r.json())
    print("\n\nUser query is -> ", query, "\n")
    print(bot_name)
    print(payload)
    print(bot_urls_dict[bot_name])
    # print(json.dumps(r.json(), indent=1))
    print(r.json())
    print("Bot response -> ", r.json()[0]["text"])
    print("*"*20)
    print(f"Bot Name: {bot_name}")
    # print(r.json()[0]['recipient_id'])
    response = r.json()
    response[0]["recipient_id"] = int(response[0]["recipient_id"]) 
    return response

def ask_query(query, sender):
    print("#"*10 + "Enterd the ask_query function\n")
    if "paddy" in query or "rice" in query or "basmati" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="rice")
        return response
    
    elif "ਚੌਲਾਂ" in query or "ਬਾਸਮਤੀ" in query or "ਝੋਨਾ" in query or "ਝੋਨੇ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="rice_pun")
        return response
    
    elif "wheat" in query:
        print("------------------wheat--------------------")
        response = send_request_to_bot(sender=sender, query=query, bot_name="wheat")
        return response
    
    elif "ਕਣਕ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="wheat_pun")
        return response
    
    elif "chili" in query or "chilly" in query or "chilli" in query or "chllie" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="chilli")
        return response
    
    elif "ਮਿਰਚ" in query or "ਮਿਰਚਾਂ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="chilli_pun")
        return response
    
    elif "citrus" in query or "kinnow" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="citrus") 
        return response
    
    elif "ਕਿੰਨੂ" in query or "ਨਿੰਬੂ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="citrus_pun") 
        return response
    
    elif "garlic" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="garlic") 
        return response
    
    elif "ਲਸਣ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="garlic_pun") 
        return response
    
    elif "guava" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="guava") 
        return response
    
    elif "ਅਮਰੂਦ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="guava_pun") 
        return response
    
    elif "pea" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="pea") 
        return response
    
    elif "ਮਟਰ" in query:
        response = send_request_to_bot(sender=sender, query=query, bot_name="pea_pun") 
        return response
    
    else:
        translator = Translator()
        lang = translator.detect(query)
        print("")
        if lang.lang=="en":
            buttons = [
                        {
                            "recipient_id": int(sender),
                            "text": "Please confirm for which crop you are asking the query",
                            "buttons": [
                                        {
                                            "payload": "Rice",
                                            "title": "Rice"
                                        },
                                        {
                                            "payload": "Wheat",
                                            "title": "Wheat"
                                        },
                                        {
                                            "payload": "Chilli",
                                            "title": "Chilli"
                                        },
                                        {
                                            "payload": "Guava",
                                            "title": "Guava"
                                        },
                                        {
                                            "payload": "Citrus",
                                            "title": "Citrus"
                                        },
                                        {
                                            "payload": "Pea",
                                            "title": "Pea"
                                        },
                                        {
                                            "payload": "Garlic",
                                            "title": "Garlic"
                                        }
                                    ]
                        }
                    ]
        elif lang.lang == "pa":
            buttons = [
                        {
                            "recipient_id": int(sender),
                            "text": "ਕਿਰਪਾ ਕਰਕੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਤੁਸੀਂ ਕਿਸ ਫਸਲ ਲਈ ਪੁੱਛਗਿੱਛ ਕਰ ਰਹੇ ਹੋ",
                            "buttons": [
                                        {
                                            "payload": "ਚੌਲ",
                                            "title": "ਚੌਲ"
                                        },
                                        {
                                            "payload": "ਕਣਕ",
                                            "title": "ਕਣਕ"
                                        },
                                        {
                                            "payload": "ਮਿਰਚ",
                                            "title": "ਮਿਰਚ"
                                        },
                                        {
                                            "payload": "ਅਮਰੂਦ",
                                            "title": "ਅਮਰੂਦ"
                                        },
                                        {
                                            "payload": "ਖੱਟੇ",
                                            "title": "ਖੱਟੇ"
                                        },
                                        {
                                            "payload": "ਮਟਰ",
                                            "title": "ਮਟਰ"
                                        },
                                        {
                                            "payload": "ਲਸਣ",
                                            "title": "ਲਸਣ"
                                        }
                                    ]
                        }
                    ]
        return buttons

app = Flask(__name__)
api = Api(app)

class Bot(Resource):
    def post(self):
        data = request.json
        print(data.keys())
        print(data)
        try:
            global last_query
            # print(data.keys())
            print(data["message"].lower())
            print("*"*5 + "if for greetings")
            if "message" in data.keys():
                if data["message"].lower() in greetings_list:
                    print("inside greetings if condition")
                    payload = json.dumps(dict(sender = int(data['sender']), message = data["message"]))
                    for bot_name in bot_urls_dict.keys():
                        _r1 = requests.post(url=bot_urls_dict[bot_name], data=payload)
                    response = _r1.json()
                    response[0]["recipient_id"] = int(response[0]["recipient_id"])
                    response[0]["text"] = "Hi! Welcome to Farmerapp. You can ask queries related to crop diseases, fertilizers, etc"
                    return response
                if data["message"].lower() in good_bye_list:
                    print("inside googbye if condition")
                    response = [
                        {
                            "recipient_id": int(data['sender']),
                            "text": "Do you have any more questions?",
                            "buttons": [
                                {
                                    "payload": "/ok_yes_for_goodbe",
                                    "title": "YES"
                                },
                                {
                                    "payload": "/ok_no_for_goodby",
                                    "title": "NO"
                                }
                            ]
                        }
                    ]
                    return response
                if "/ok_yes_for_goodbe" in data["message"]:
                    print("*"*5 + "if for /ok_yes_for_goodbe")
                    response = [
                        {
                            "recipient_id": int(data['sender']),
                            "text": "Please type your questions in the chat.",
                            "buttons": [
                                {
                                    "payload": "",
                                    "title": ""
                                }
                            ]
                        }
                    ]
                    return response

                if "/ok_no_for_goodby" in data["message"]:
                    print("*"*5 + "if for /ok_no_for_goodby")
                    response = [
                        {
                            "recipient_id": int(data['sender']),
                            "text": "bye",
                            "buttons": [
                                {
                                    "payload": "",
                                    "title": ""
                                }
                            ]
                        }
                    ]
                    return response
                
                if "/ok" in data["message"]:
                    print("*"*5 + "if for /ok")
                    payload = json.dumps(dict(sender = int(data['sender']), message = data["message"]))
                    for bot_name in bot_urls_dict.keys():
                        _r1 = requests.post(url=bot_urls_dict[bot_name], data=payload)
                    response = _r1.json()
                    response[0]["recipient_id"] = int(response[0]["recipient_id"])
                    return response
                
                if len(data["message"].split()) < 5:
                    print("*"*5 + "if for sentence length < 5")
                    raise Exception("message length is less than 5 words")
            if "crop_name" in data.keys():
                # if crop name is there in the payload sent by client then we append the crop name on the end of the last query sent by user
                print("* "*5+"Crop_name: ", data["crop_name"] + " *"*5)
                query = last_query.strip() + " " + data["crop_name"].lower().strip()
                print("Query after adding crop name: ", query)
                response = ask_query(query, int(data["sender"]))
                print(type(response))
                return response
            response = ask_query(data['message'], int(data["sender"]))
            print(type(response))

            # using globle variable to store last message
            last_query = data['message']
            print("*"*20)
            print("The current message stored message is: ",last_query)
            print("*"*20)
            return response
        except Exception as e:
            print("Exception: ", e)
            could_not_understand[0]["recipient_id"] = int(data["sender"])
            return could_not_understand

api.add_resource(Bot, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
