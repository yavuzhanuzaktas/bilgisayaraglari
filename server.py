import socket

'''
    Socket oluşturup
    bind methodu ile server adresini localhost(sebebi ise lokal bir ortamda çalışıyoruz) ve portunu sunucuya veriyoruz.
    Artık sunucumuzun adresi ve portu belli
    .listen() metodu ile dışarıdan gelen bağlantıların hepsini dinliyoruz.
'''

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("localhost", 8000))
serverSocket.listen(10)

'''
    Yukarıda gelen bağlantıları dinliyorduk.
    .accept() metodu ile gelen bağlantıları kabul ediyoruz.
    
    Sonra aldığımız veriyi connection(bağlantı) ve address(adres bilgileri) olarak ikiye ayırıyoruz.
'''
connection, address = serverSocket.accept()

'''
    Burda sınırsız döngüye alarak bağlantı geçerli olana kadar bağlantı bekliyoruz
'''
while True:
    if connection is not None:
        break

'''
    Burdaki sınırsız döngümüz ise bağlantı geldiğinde çalışıp kullanıcıdan mesaj alıyor.
'''

while True:
    print("Bağlantı sağlandı!")
    getMessage = input("Göndermek istediğiniz mesaj: ")

    '''
        .send() metodu ile gelen bağlantıya mesaj gönderiyoruz.
        Gönderirken byte olarak gönderiyoruz.
        try except ile bir sorun olursa ekrana hata bastırıyoruz.
    '''
    try:
        connection.send(bytes(getMessage, "UTF-8"))
    except:
        print("Mesaj gönderilirken hata oluştu!")