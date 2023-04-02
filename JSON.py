from distutils.file_util import write_file
import os
import json
from urllib import response


with open("vlan_details.json", "w") as w:
    json.dump(response, w)

print(response)