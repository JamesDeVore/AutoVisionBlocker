import base64
import hashlib
import io
import os
import uuid
import zipfile

import jinja2
from PIL import Image
from six import iteritems
from Asset import Asset

from process import ProcessImage
from ReAnalyze import CreateSquares
from Analyze import analyzeImage

properties_xml = '''
<map>
  <entry>
    <string>campaignVersion</string>
    <string>1.4.1</string>
  </entry>
  <entry>
    <string>version</string>
    <string>1.5.3</string>
  </entry>
</map>
'''

with open('templates/content.xml') as f:
    content_template = jinja2.Template(f.read())

class Map(object):
    def __init__(self, image, VBCoords = None, **kwargs):
        assert isinstance(image, Asset)
        self.image = image
        self.id = base64.encodestring(uuid.uuid4().bytes).strip()
        self.VBBoxes = VBCoords


    def _add_asset(self, f, asset):
        f.writestr('assets/{}'.format(asset.md5), asset.asset_xml())
        f.writestr('assets/{}.{}'.format(asset.md5, asset.ext), asset.contents)

    def content_xml(self):
        return content_template.render(m=self)

    def make_file(self, file, mode='w', compressed=True):
        c = zipfile.ZIP_DEFLATED if compressed else zipfile.ZIP_STORED
        with zipfile.ZipFile(file, mode=mode, compression=c) as f:
            f.writestr('content.xml', self.content_xml())
            f.writestr('properties.xml', properties_xml)
            self._add_asset(f, self.image)


def makeMap(pathToOriginalImg,name):
  imgFile = io.open(pathToOriginalImg, mode='rb').read()
  img = Asset("asset",'png',imgFile)
  #lets get the image coords array
  #first you need to pre process
  # countedArray = analyzeImage(pathToOriginalImg, 5)
  raw_array = ProcessImage(pathToOriginalImg, 3)
  countedArray = CreateSquares(raw_array, 3)
  thisMap = Map(image=img, VBCoords = countedArray)
  thisMap.make_file('output/ ' + name + '.zip')
  thisMap.make_file('output/ ' + name + '.rpmap')

makeMap("samples/dungeon3.png",'newMap')
