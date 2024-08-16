import qrcode

# img = qrcode.make('https://www.youtube.com/')
# img.save('youtube_qrcode.png')

daraz_img = qrcode.make("https://www.daraz.pk/")
daraz_img.save('daraz_qrcode.png')

