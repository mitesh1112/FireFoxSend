import firefoxsend

if __name__ == '__main__':
    ffs = firefoxsend.FireFoxSend()
    #url = ffs.upload('D:\\mitesh\\all.txt')
    url = ffs.upload('D:\\mitesh\\Fonts.zip')
    print(url)