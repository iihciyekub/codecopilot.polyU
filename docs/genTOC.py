import os 

# 更改项目目录为 docs
os.chdir("./docs")
# 遍历 path 目录下的所有 md 后缀的文件,并返回路径给我

def get_md_file(path):

    md_list = []
    t = ""
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.md':
                file_path = os.path.join(root, file)
                # 读取 md 文件的内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    a = f.readlines(1)
                a = a[0].replace("# ","")
                a = a.replace("\n","")
                a = a.strip()
                t += f"- [{a}]({file_path})\n"
                md_list.append(file_path)

    print(t)
    return t

t = get_md_file("weeks")
with open('_sidebar.md', 'w', encoding='utf-8') as f:
    f.write(t)


#  