from revChatGPT.V1 import Chatbot
from dotenv import load_dotenv
import os
from flask import *
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/login',methods=['GET', 'POST']) 
def login():  
    load_dotenv()

    OPENAI_EMAIL=os.getenv("OPENAI_EMAIL")
    OPENAI_PASSWORD=os.getenv("OPENAI_PASSWORD")

    chatbot = Chatbot(config={
        "email": OPENAI_EMAIL,
        "password": OPENAI_PASSWORD
    })

    prompt = request.form("prompt")
    response = ""

    for data in chatbot.ask(
        prompt
    ):
        response = data["message"]

    return render_template('getinput.html', prompt=prompt)
  
if __name__ =='__main__':  
    app.run(debug = True)