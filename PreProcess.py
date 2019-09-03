from PIL import Image, ImageFilter, ImageEnhance

#this jacks up the image and makes it greyscale, because
#I think it will make it easier to work with
def PrepareImage(pathToFile):
  im = Image.open(pathToFile)
  im.load()
  im = im.convert('L')
  # im.show()
  im = im.filter(ImageFilter.SHARPEN)
  im = im.point(lambda i: i * 3.5)
  enh = ImageEnhance.Contrast(im)
  enh.enhance(3).save("temp/processed.png")



