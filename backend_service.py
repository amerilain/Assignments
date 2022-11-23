from flask import Flask, request

app = Flask(__name__)


@app.route('/prime_number')
def prime_number():
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


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
