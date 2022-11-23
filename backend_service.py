from flask import Flask, request, Response
import json
import mariadb

app = Flask(__name__)

# part 1
# url: http://127.0.0.1:5000/prime_number?number=31
'''
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
'''
# part 2
# url: http://127.0.0.1:5000/airport/EFHK

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game2',
    user='root',
    password='root123'
)


@app.route('/airport/<string:icao>')
def get_airport(icao):
    try:
        sql = "SELECT name, municipality from airport where ident = '" + icao + "'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        response = {
            "ICAO": icao,
            "Name:": result[0][0],
            "Location": result[0][1]
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
