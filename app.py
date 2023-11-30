import mikrotik, guess
from flask import Flask, request
from constant import SKILL_ID

app = Flask(__name__)


@app.route('/', methods=['POST'])
def res():
    post_req = request.json
    print(post_req)
    match post_req.get('session').get('skill_id'):
        case SKILL_ID:
            command = post_req.get('request')
            response_text = False, 'Команда недоступна'
            if not command.get('command'):
                response_text = mikrotik.connect()
            else:
                response_text = guess.guesser(command.get('command'))
            print(response_text)
            response = {
                'response': {
                'text': response_text[1],
                'end_session': True
                },
                'version': '1.0'
            }
            return response


if __name__ == '__main__':
    context = ('ECC-cert.pem', 'ECC-privkey.key')
    app.run('0.0.0.0', port=5000, ssl_context=context, debug=True)