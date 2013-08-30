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
# Add the library location to the path
import sys
sys.path.insert(0, 'lib')

from attachmentproxy.handler import ATTACHMENT_PROXY_ROUTES
from main_handler import MAIN_ROUTES
from notify.handler import NOTIFY_ROUTES
from oauth.handler import OAUTH_ROUTES
from signout.handler import SIGNOUT_ROUTES
from simplepage.handler import SIMPLEPAGE_ROUTES
from upload.handler import UPLOAD_ROUTES


ROUTES = (
    ATTACHMENT_PROXY_ROUTES + MAIN_ROUTES + NOTIFY_ROUTES + OAUTH_ROUTES +
    SIGNOUT_ROUTES + SIMPLEPAGE_ROUTES + UPLOAD_ROUTES)


app = webapp2.WSGIApplication(ROUTES)

'''class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('I live to make you coffee')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)'''