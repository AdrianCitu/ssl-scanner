try:
    import zipfile
    import os
except ImportError as e:
    print e
    print "Failed to load dependencies. This issue maybe caused by using an unstable Jython version."


newZip = zipfile.ZipFile('../ssl-scanner.bapp', 'w')
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        fullPath = os.path.join(root, name)
        print(fullPath)
        newZip.write(fullPath, compress_type=zipfile.ZIP_DEFLATED)

newZip.close()
