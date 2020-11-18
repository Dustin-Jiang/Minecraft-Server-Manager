import os
import time
os.chdir(r"C:\MCServer\1.12.2")
Path = r"xcopy /E .\world .\Backups\worldbackup-"
Path = Path + time.strftime("%Y-%m-%d", time.localtime())
Path = Path + "\\"
os.system(Path)