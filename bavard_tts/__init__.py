from waitress import serve
from pyramid.config import Configurator

def main(global_config=None, **settings):
    config = Configurator(settings=settings)
    
    # Include static assets
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'bavard_tts:static')
    
    # Configure templates
    config.add_jinja2_renderer('.jinja2')
    config.add_jinja2_search_path('bavard_tts:templates')
    
    # Add routes
    config.include('.routes')
    
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)