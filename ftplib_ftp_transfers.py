# FTP - FileTransferProtocol- transfer files to/from servers
# not most secured way (ssh-encripting everything, sftp)

from ftplib import FTP

ftp = FTP('domainname.com')                                     #domainname translates to an IP address
ftp.login(user='username',passwd='password')

ftp.cwd('/specificdomain-or-location/')                         #change current working dir

#grabbing file from the remote server
def grabFile():
    fileName = 'fileName.txt'
    localFile = open(fileName, 'wb')
    ftp.retrbinary('RETR' + fileName, localFile.write, 1024)    #retrieve remote file to local file, buffer size

    ftp.quit()
    localFile.close()

def placeFile():
    fileName = 'fileName.txt'
    ftp.storbinary('STOR' + fileName, open(fileName, 'rb'))    #store binary
    ftp.quit()




