#!/usr/bin/python3

import webapp


class urlaleat(webapp.webApp):
    def process(self, parsedRequest):
        """Process the relevant elements of the request."""
        import random
        numero = random.randint(1, 1000000)
        return ("200 OK", "<html><body><a href ="
                + str(numero) + ">Dame mas</a></body></html>")

if __name__ == "__main__":
    testWebApp = urlaleat("localhost", 1234)
sumando1, sumando2 = recurso.split('+')
