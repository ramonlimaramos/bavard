# bavard_tts/views.py

from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return ''

@view_config(route_name='generate_speech', renderer='templates/generate_speech.jinja2')
def generate_speech(request):
    # Add logic to generate speech here
    return {'message': 'Generating speech...'}

@view_config(route_name='upload_model', renderer='templates/upload_model.jinja2')
def upload_model(request):
    # Add logic to handle model upload here
    return {'message': 'Uploading model...'}
