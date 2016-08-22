#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from caesar import encrypt

rot13_header= """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar</title>
    </head>
    <body>
        <h1>Rotate Text</h1>
    </body>
</html>
"""

class Rot13(webapp2.RequestHandler):
    def get(self):

        rot13_form="""
        <form method="post">
            <label>
                Rotate by:
                <input type="text" name="rotate-by"/>
            </label>
            <br>
            <textarea name ="text" style='height: 100px; width: 400px;'>type here</textarea>
            <br>
            <input type="submit">
        </form>
        """
        response = rot13_header + rot13_form
        self.response.write(response)
    def post(self):
        rotate_by= self.request.get("rotate-by")
        num=int(rotate_by)

        text = self.request.get('text')
        newtext = encrypt(text, num)

        rot13_form2="""
        <form method="post">
            <label>
                Rotate by:
                <input type="text" name="rotate-by" value=%s >
            </label>
            <br>
            <textarea name ="text" style='height: 100px; width: 400px;'>%s</textarea>
            <br>
            <input type="submit">
        </form>
        """ % (num, newtext)
        response = rot13_header + rot13_form2
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', Rot13)
], debug=True)
