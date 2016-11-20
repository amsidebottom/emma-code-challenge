import urllib2

def link_verification(link_list):
    responses = {
        300: ('Multiple Choices',
              'Object has several resources -- see URI list'),
        301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
        302: ('Found', 'Object moved temporarily -- see URI list'),
        303: ('See Other', 'Object moved -- see Method and URL list'),
        304: ('Not Modified',
              'Document has not changed since given time'),
        305: ('Use Proxy',
              'You must use proxy specified in Location to access this '
              'resource.'),
        307: ('Temporary Redirect',
              'Object moved temporarily -- see URI list'),
    
        400: ('Bad Request',
              'Bad request syntax or unsupported method'),
        401: ('Unauthorized',
              'No permission -- see authorization schemes'),
        402: ('Payment Required',
              'No payment -- see charging schemes'),
        403: ('Forbidden',
              'Request forbidden -- authorization will not help'),
        404: ('Not Found', 'Nothing matches the given URI'),
        405: ('Method Not Allowed',
              'Specified method is invalid for this server.'),
        406: ('Not Acceptable', 'URI not available in preferred format.'),
        407: ('Proxy Authentication Required', 'You must authenticate with '
              'this proxy before proceeding.'),
        408: ('Request Timeout', 'Request timed out; try again later.'),
        409: ('Conflict', 'Request conflict.'),
        410: ('Gone',
              'URI no longer exists and has been permanently removed.'),
        411: ('Length Required', 'Client must specify Content-Length.'),
        412: ('Precondition Failed', 'Precondition in headers is false.'),
        413: ('Request Entity Too Large', 'Entity is too large.'),
        414: ('Request-URI Too Long', 'URI is too long.'),
        415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
        416: ('Requested Range Not Satisfiable',
              'Cannot satisfy request range.'),
        417: ('Expectation Failed',
              'Expect condition could not be satisfied.'),
    
        500: ('Internal Server Error', 'Server got itself in trouble'),
        501: ('Not Implemented',
              'Server does not support this operation'),
        502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
        503: ('Service Unavailable',
              'The server cannot process the request due to a high load'),
        504: ('Gateway Timeout',
              'The gateway server did not receive a timely response'),
        505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
        }    
    
    failed_links = []
    for link in link_list:
        req = urllib2.Request(link)
        try:
            resp = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            if e.code >= 300:
                failed_links.append(link + " failed. Reason: " + str(e.code) + str(responses[e.code]))
        except urllib2.URLError as e:
                failed_links.append(link + " failed. Reason: " + str(e.reason))
    return failed_links



# Could the function be improved if the same list of links is being passed in many times, and what are the tradeoffs?
     # As links are passed through, the link and its status (success or error code) could be stored in a dictionary. When a link is passed through, the function could check to see if it has been passed through previously. If so, it would return the links' associated status. If not, it could go through the verification process, then add the link and its status to the dictionary. The tradeoff is that this adds another step to the function which could result in slower runtime.

# How might this function be exposed as an HTTP API to be used by a front-end application?
     # An HTML form could be used to get the user's input, which would be a list of links to verify. This function could store all links seperated by a " " or "," into a list of links. After the verification process, the function could print the list of links that were unsuccessful and why.
