import socket

'''
    Socket oluşturup
    bind methodu ile server adresini localhost(sebebi ise lokal bir ortamda çalışıyoruz) ve portunu sunucuya veriyoruz.
    Artık sunucumuzun adresi ve portu belli
    .connect() metodu ile sunucumuza bağlanıp aktif olduğumuzun bilgisini veriyoruz.
    Bundan dolayı sunucumuz bağlantı geldiğini ve bu bağlantıyı kullanarak mesaj atabilceğini anlıyor.
'''

routerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
routerSocket.bind(("localhost", 8100))

routerSocket.connect(("localhost", 8000))

'''
   Sonsuz döngüye alarak gelen mesajı dinliyoruz.
   Soketten mesajı .recv() fonksiyonu ile alıyoruz. 
'''
while True:
    receivedMessage = routerSocket.recv(1024)

    '''
        Gelen mesajı boş olup olmadığı kontrol ettikten sonra decode metodu ile UTF-8 formatına çeviriyoruz.
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

            routerSend.connect(("localhost", 8200))
            routerSend.send(bytes(decodeMessage, "UTF-8"))
            routerSend.close()
        except:
            print("Mesaj gönderilirken hata oluştu!")

