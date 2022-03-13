import hashlib
import sys
import os
from os.path import exists



def check_len():
    if len(sys.argv) == 3:
        return True
    else:
        return False



def check_file_existence():
    if '/' in sys.argv[1] or '\\' in sys.argv[1]:
        _path = sys.argv[1]
    else:
        _path = os.getcwd()+'/'+sys.argv[1]
    if exists(_path):
        return True
    return False


if check_len():
    if check_file_existence():
        

        if '/' in sys.argv[1] or '\\' in sys.argv[1]:
            _path = sys.argv[1]

        else:
            _path = os.getcwd()+'/'+sys.argv[1]
        with open(_path,'r') as file:
            for line in file.readlines():
                hash_ob=hashlib.md5(line.strip().encode())
                hashed_pass=hash_ob.hexdigest()
                
                if hashed_pass==sys.argv[2]:
                    
                    print("Found cleartext password :"+line.strip())
                    break
                   
        
    else:
        print("File doesn't exists")
else:
    print("Provide correct argument of file and valid text")
    print(f"{sys.argv[0]} file.txt text")
    sys.exit(1)

