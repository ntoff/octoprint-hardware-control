#####
#This script is just for testing
#####

import requests

apiKey = 'y0ur4p1k3yg03sh323' #put your octoprint api key here
url = 'http://127.0.0.1:5000/api/job'
### Uncomment only ONE command
command = {'command': 'cancel'} #start a print
#command = {'command': 'start'} #cancel a print

r = requests.post(url=url, headers={'X-Api-Key': apiKey}, json=command)