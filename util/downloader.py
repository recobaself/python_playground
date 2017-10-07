#!/usr/bin/python
import urllib.request
import sys

def parseFile(path):
    urls = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line[:4] == 'http':
                urls.append(line)
    return urls


def download(arr):
    for url in arr:
        try:
            file_name = url.split('/')[-1]
            urllib.request.urlretrieve(url, file_name)
            print(u"\u2713" + "   " + file_name + " downloaded ...")
        except:
            print("!!  Failed to download from " + url)
    print("Download completed!")

if __name__ == '__main__':
    # print('Hello World')
    p = sys.argv[1]
    # print(p)
    download(parseFile(p))
