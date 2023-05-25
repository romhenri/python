import qrcode

myLink = input("Cole o Link aqui: ")

myQrCode = qrcode.make(myLink)

myQrCode.save("arquivo.png")
myQrCode.show()
