from chalice import Chalice
from chalicelib.password_strength import compute_strength
import logging

app = Chalice(app_name='password-strength-checker')
app.log.setLevel(logging.DEBUG)

@app.route('/')
def index():
    return {'hello': 'world'}

#TODO: Handle invalid input, return BAD_REQUEST
@app.route('/password/compute-strength', methods=['POST'],
           content_types=['application/json'])
def password_compute_strength():
    request_body = app.current_request.json_body
    password = request_body.get('password')
    app.log.debug(f'Got password {password}')
    return {
        'strength': compute_strength(password)
    }
