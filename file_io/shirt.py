from PIL import Image, ImageOps
import sys

if len(sys.argv)<3:
    sys.exit("Too few")
elif len(sys.argv)>3:
    sys.exit("Too many")
elif sys.argv[1][-3:].lower() != "jpg" and sys.argv[1][-3:].lower() != "jpeg" and sys.argv[1][-3:].lower() != "png":
    sys.exit("Not right format")
elif sys.argv[1][-3:].lower() != sys.argv[2][-3:].lower():
    sys.exit("Not matching")
else:
    face = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
    face_conv = ImageOps.fit(face,shirt.size)
    face_conv.paste(shirt,mask=shirt)
    face_conv.save(sys.argv[2])
