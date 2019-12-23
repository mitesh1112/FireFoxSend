import firefoxsend

if __name__ == '__main__':
    ffs = firefoxsend.FireFoxSend()
    #url = ffs.upload('D:\\mitesh\\all.txt')
    #url = ffs.upload('D:\\mitesh\\Fonts.zip')
    url = ffs.upload('D:\\mitesh\\temp\\Ausord_backup_2019_12_19_233002_3755087.bak')
    print(url)