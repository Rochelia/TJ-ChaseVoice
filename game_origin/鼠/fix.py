name=input()
cnt=1
with open(f"C:\\Users\\86150\\PycharmProjects\\PythonProject\\text.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    with open(f"te.txt", 'a', encoding='utf-8') as f:
        f.write(f"{name}_"+str(cnt)+".mp3|"+line)
        cnt+=1