#api.open-notify.org/astros.json
#pip --version
#if not exist, i uninstalled python and reinstalled it with admin privileges and checked the PATH being set as well
#pip is used to install any package from python package index
#python package index or pypi is the 3rd party software repo for python (similar to nuget packages)

#pip3 install requests
#or pip
#mac may be different where it doesn't need install, but windows needs it

#open-notify.org has info on the api we will be using
#json is stored as a dictionary

#virutal environments for packages incase the depencies on the version are different.
#documentation on python venv
#pip install virtualenv
#py -m venv myenv
#myenv/Scripts/activate
#note, this is windows, different on different OS's

#deactivate to get of a venv

import requests #this is from pip

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

for person in json['people']:
    print(person['name'])