import API

@API.API.route('/', methods=['GET'])
def home():
    return "Welcome to the Home Page!"  


