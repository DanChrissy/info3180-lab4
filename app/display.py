import os

rootdir = os.getcwdu()
f = []
def get_uploaded_images():
    for subdir, files in os.walk(rootdir + '/app/static/uploads'):
        for file in files:
            f.append(os.path.join(subdir,file))
    return f
    