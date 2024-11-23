def includeme(config):
    config.add_route('home', '/')
    config.add_route('generate_speech', '/generate')
    config.add_route('upload_model', '/upload')
    
    config.scan('.views') 