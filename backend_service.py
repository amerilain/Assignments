from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/prime_number')
def prime_number():
    try:
        args = request.args
        number = int(args.get("number"))

        if number > 2:
            for n in range(2, number):
                if (number % n) == 0:
                    answer = 'false'
                    break
            else:
                answer = 'true'
        else:
            answer = 'false'
        response = {
            "number": number,
            "isPrime": answer
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as entered",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
