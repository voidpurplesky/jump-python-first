from os import listdir, path

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
    
search("c:/")