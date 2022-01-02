import socket

'''
    Socket oluşturup
    bind methodu ile server adresini localhost(sebebi ise lokal bir ortamda çalışıyoruz) ve portunu sunucuya veriyoruz.
    Artık sunucumuzun adresi ve portu belli
    .listen() metodu ile sunucumuza gelen bağlantıları dinliyoruz.
'''

routerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
routerSocket.bind(("localhost", 8300))

routerSocket.listen(10)

'''
   Sonsuz döngüye alarak gelen bağlantıları dinliyoruz.
   Bağlantı düzgün ise gelen bağlantıdan .recv() metodu ile mesajı alıyoruz. 
'''
while True:
    connection, address = routerSocket.accept()

    if connection is not None:
        receivedMessage = connection.recv(1024)

        '''
            Aldığımız mesajı boş olup olmadığını kontrol edip gelen meajı UTF-8 olarak dönüştürüyoruz.
            Sonra mesajı ekrana yazdırıyoruz.
        '''

        if receivedMessage != b'':
            decodeMessage = receivedMessage.decode("UTF-8")
            print("Mesaj Geldi!")
            print("Mesaj: ", decodeMessage)
            print()

            '''
                Burda geçici bir soket oluşturup diğer yönlendiricimize bağlanıyoruz.
                Bağlandıktan sonra mesajımızı byte olarak gönderip bağlantımızı kapatıyoruz.
                try except ile bir sorun var mı diye kontrol edip ekrana hata bastırıyoruz.
            '''

            try:
                routerSend = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                routerSend.connect(("localhost", 8400))
                routerSend.send(bytes(decodeMessage, "UTF-8"))
                routerSend.close()
            except:
                print("Mesaj gönderilirken hata oluştu!")


