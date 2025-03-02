import os
path=os.getcwd()
folder=os.listdir(path)
for item in folder:
    if os.path.isdir(item):
        with open(f"{os.path.join(path,item)}\\text.txt", 'r',encoding='utf-8') as f:
            line = f.readlines()
        cnt=0
        os.remove(f"{os.path.join(path,item)}\\text.txt")
        files=os.listdir(os.path.join(path,item))
        files.sort()
        for file in files:
            if file.endswith(".mp3")or file.endswith(".wav"):
                with open (f'{os.path.join(path,item)}\\text.txt', 'a',encoding='utf-8') as f:
                    f.write(f"{file}|{line[cnt]}")
                cnt=cnt+1



