# -*- mode: python -*-

block_cipher = None


a = Analysis(['openweather.py'],
             pathex=['/Users/alicia/Documents/Websites/ITsimplified/1startbootstrap-landing-page-gh-pages/posts'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='openweather',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='openweather.ico')
app = BUNDLE(exe,
             name='openweather.app',
             icon='openweather.ico',
             bundle_identifier=None)
