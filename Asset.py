import hashlib
import jinja2



asset_template = '''<net.rptools.maptool.model.Asset>
  <id>
    <id>24026be7ee6033968a928584be4503e1</id>
  </id>
  <name>BasicMap</name>
  <extension>png</extension>
  <image/>
</net.rptools.maptool.model.Asset>
'''.strip()


class Asset(object):
    def __init__(self, name, ext, contents, md5=None):
        self.contents = contents
        self.name = name
        self.ext = ext
        if md5 is None:
            md5 = hashlib.md5(contents).hexdigest()
        self.md5 = md5

    def asset_xml(self):
        return jinja2.Template(asset_template).render(asset=self)

    def __repr__(self):
        return '<Asset {}.{}>'.format(self.name, self.ext)
