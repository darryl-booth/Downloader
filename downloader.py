import urllib.request  # Needed to request web resource
from os import path
import traceback


def get_filename(url):
    fragment_removed = url.split("#")[0]  # keep to left of first #
    query_string_removed = fragment_removed.split("?")[0]
    scheme_removed = query_string_removed.split("://")[-1].split(":")[-1]
    if scheme_removed.find("/") == -1:
        return ""
    return path.basename(scheme_removed)


# Using readlines()
file = open("list.txt", "r")
lines = file.readlines()

count = 0
# Strips the newline character
for line in lines:
    count += 1
    print("Downloading {}: {}".format(count, line.strip()))

    try:
        response = urllib.request.urlopen(line.strip())
        file = open("downloaded/" + get_filename(line.strip()), "wb")
        file.write(response.read())
        file.close()
    except:
        print("*** Error on " + line.strip() + " ***")
        traceback.print_exc()
