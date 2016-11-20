# Emma Code Challenge
This function accepts a list of URLs and returns a subset of those links that are either written incorrectly or do not return a success status code, along with the status code received to indicate the reason for the error.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Python (download: https://www.python.org/downloads/) 
  - Note: Python version 2.7.10 was used to write this function
- **urllib2** module must be imported. This step is included in the EmmaCodeChallengeFinal.py file

### Instructions for Running Code

1. Download the **EmmaCodeChallengeFinal.py** file found in this repository
2. Open the file in the IDE of your choice
3. In the shell, input your list of links to verify and store them in the variable **link_list**
   - Example:
   
 ```
link_list=["http://www.google.com", "http://www.facebook.com", "http://www.fake-server.org", "http://www.mssidebottom.com/fakepage"]
 ```
4. Now, call the function **link_verification** with the argument **link_list**:
```
link_verification(link_list)
```

The function will return a list of invalid URLs, as well as the reason/status code for their failure. The example link_list given above will return the following failed_list:
```
['http://www.fake-server.org failed. Reason: [Errno 8] nodename nor servname provided, or not known', "http://www.mssidebottom.com/fakepage failed. Reason: 404('Not Found', 'Nothing matches the given URI')"]
```


## Testing the Function

To test the function, create **link_list** such that it contains links that should succeed, and links that should fail for varying reasons.
The link_list example above contains the following:

1. http://www.google.com - This link is anticpated to be successful, as it should link to Google. Therefore, it should not be returned in the failed_links list
2. http://facebook.com - Same as above -- this link is anticipated to be successful and therefore not returned
3. http://fake-server.org - This website does not exist, so it is expected that we will receive an error that there was no server found for this site.
4. http://mssidebottom.com/fakepage - I created the website mssidebottom.com for my classroom, but there is not page called "fakepage". therefore this link should be returned with a 404 error.

You can test the function with any links you would like. To test a link:

1. Include it in **link_list** and run **link_verification(link_list)**
2. If the link is not contained in the returned list, the function found it to be a successful URL. If the link is contained in the returned list, it was not found to be a successful URL due to the provided reason.

## Author

* **Alyssa Sidebottom** 
