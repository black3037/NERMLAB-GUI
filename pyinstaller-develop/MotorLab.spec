# -*- mode: python -*-

block_cipher = None

import os
#'C:\\Users\\Derek\\Desktop\\pyinstaller-develop'
path_to_spec = str(os.path.dirname(os.path.realpath('MotorLab.spec')))

path_to_motorlab_py = os.path.normpath(os.getcwd() + os.sep + os.pardir)
path_to_resources = path_to_motorlab_py + '\Resources'
path_to_motorlab_py = path_to_motorlab_py + '\MotorLab.py'

path_to_splash = path_to_resources + '\splash_loading.png'
path_to_icon_1 = path_to_resources + '\motorlabicon.png'
path_to_icon_2 = path_to_resources + '\motorlabicon.ico'


a = Analysis([path_to_motorlab_py],
             pathex=[path_to_spec],
             binaries=[],
             datas=[(path_to_splash,'Data'),(path_to_icon_1,'Data')],
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
          name='MotorLab',
          debug=False,
          strip=False,
          upx=True,
          console=False , 
		  icon=path_to_icon_2)
