from chalice import Chalice, BadRequestError
from chalicelib.password_strength import compute_strength
import logging

app = Chalice(app_name='password-strength-checker')
app.log.setLevel(logging.DEBUG)

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/password/compute-strength', methods=['POST'],
           content_types=['application/json'])
def password_compute_strength():
    request_body = app.current_request.json_body
    password = request_body.get('password')
    if password is None:
        raise BadRequestError('Password not provided')
    app.log.debug(f'Got password {password}')
    return {
        'strength': compute_strength(password)
    }
