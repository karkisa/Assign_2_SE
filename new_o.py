# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

hostName = "0.0.0.0"
serverPort = 3000
mocjk_wea= {"coord":{"lon":-123.262,"lat":44.5646},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"base":"stations","main":{"temp":281.19,"feels_like":280.52,"temp_min":279.51,"temp_max":282.9,"pressure":1027,"humidity":79},"visibility":10000,"wind":{"speed":1.54,"deg":270},"clouds":{"all":20},"dt":1642209311,"sys":{"type":2,"id":2040223,"country":"US","sunrise":1642175199,"sunset":1642208235},"timezone":-28800,"id":5720727,"name":"Corvallis","cod":200}
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data/2.5/weather':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps(mocjk_wea).encode('utf-8'))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


# http://127.0.0.1:8080/data/2.5/weather
# https://api.openweathermap.org/data/2.5/weather?q=corvallis&appid=741d8bb9e490bcecbc0c3c56b458fcbd

# http://3.82.127.138:3000/data/2.5/weather
#http://ec2-3-82-127-138.compute-1.amazonaws.com:3000/data/2.5/weather

