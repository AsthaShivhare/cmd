import urllib
import os
# downloading executable file
exefile="eclipse-win64.exe"
# specifying the path of file where it is to be downloaded
location = input("Enter the path at which you want to download file \n In quotes : ")
path=location+ exefile

urllib.urlretrieve("https://www.python.org/ftp/python/2.7.14/python-2.7.14.amd64.msi", path)
print "\n Executable file downloaded!!!!!!\n   "
print  "Path of the file is : \n" , path




#checking if the downloaded file is zipped

if path.endswith(".zip"):
    zip_ref = zipfile.ZipFile(path,'r')
    #extracting file at given directory
    zip_ref.extractal(location)
    print (" File unzipped Successfully!!!!")

    zip_ref.close() 
else:
    print ("File is not zipped")



