from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    # Create a Twilio VoiceResponse object
    response = VoiceResponse()
    # Say a message when the call is received
    response.say("Hello, this is your Flask app responding to Twilio!")
    # Return the TwiML as XML
    return Response(str(response), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
