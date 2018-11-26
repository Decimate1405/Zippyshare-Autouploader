from math import ceil
import os


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

def localdirsize_dividedby_n(folder, n):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            fpath = os.path.join(dirpath, f)
            fsize = os.path.getsize(fpath)
            total_size += fsize
    localDirGB = total_size/1073741824
    return ceil(localDirGB/n)


def getBasePath(folder):
    # format folder
    cwd = os.getcwd()
    if "\\" in cwd:
        if folder[-1] != "\\":
            folder = folder+"\\"
    if "/" in cwd:
        if folder[-1] != "/":
            folder = folder+"/"
    count0 = 0
    foldertrigger = False
    for x in folder[::-1]:
        count0 -= 1
        if x == "\\" or x == "/":
            if foldertrigger:
                break
            foldertrigger = True
    index = count0+len(folder)
    folder_basename = folder[index:].replace("\\", "/")
    return folder_basename