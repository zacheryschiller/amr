#!/usr/bin/env python

'''
This program is used to download a set of files from the FOIA
server, based on a json list of files returned from the site
'''

import os
import urllib2


def main():
    fname = "/Users/zschiller/Downloads/h.json"
    fin = open(fname, 'r')
    data = fin.readline()
    data = data.split('subject')
    docNames = []
    for line in data:
        text = line.split('"')
        try:
            if text[10][-4:] == ".pdf":
                docNames.append(text[10])
        except:
            print None
    print len(docNames)

    # download_file("https://foia.state.gov/searchapp/"
    # + docNames[0], docNames[0])
    for i in xrange(len(docNames)):
        print "Getting", i, "of", len(docNames)
        download_file(
            "https://foia.state.gov/searchapp/" + docNames[i], docNames[i])

    #    dirs = docNames[i].split('/')
    #    print dirs
    #
    # dirName = "/users/zschiller/Desktop/hillary/"
    # if not os.path.exists(dirName):
    #    os.makedirs(dirName)
    fin.close()


def download_file(download_url, docName):
    dirs = docName.split('/')
    dirName = "/users/zschiller/Desktop/hillary/" + \
        dirs[1] + '/' + dirs[2] + '/' + dirs[3] + '/'
    print dirName
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    newFileName = dirName + dirs[4]
    response = urllib2.urlopen(download_url)
    fin = open(newFileName, 'w')
    fin.write(response.read())
    fin.close()
    print("Completed")

# Run the main program
if __name__ == '__main__':
    main()
