#!/usr/bin/env python

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        html = """
<!DOCTYPE html>
<html>
<head><title>Enable CORS Testpage</title></head>
<body>
<h1>Enable CORS</h1>
<p>See <a href="http://enable-cors.org/">Enabling CORS</a> for more details</p>
</body>
</html>
        """
        self.response.write(html)
        
application = webapp2.WSGIApplication([
                                        ("/", MainPage),
                                      ], debug=True)
