from os import listdir, path, walk

def search(dirname):
    try:
        filenames = listdir(dirname)
        for filename in filenames:
            full_filename = path.join(dirname, filename)
            #print(full_filename)

            if path.isdir(full_filename):
                search(full_filename)
            else:
                ext = path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

#search("c:/")

for (p, dir, files) in walk("d:/"):
    for filename in files:
        ext = path.splitext