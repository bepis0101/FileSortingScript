import os
import shutil

def create_path(dirr, file):
    return os.path.join(dirr, file)


def fix_path(path: str):
    path = path.split(':')[1:][0]
    new_path = path.replace('\\', '/')
    return new_path

main_directory = input('Podaj sciezke ktora chcesz uporzadkowac: ')

main_directory = fix_path(main_directory)

os.chdir(main_directory)

pictures = [
    'jpeg',
    'jpg',
    'heic',
    'png',
]

src = [
    'cpp',
    'c',
    'py',
    'html',
    'css',
    'js',
]

movies = [
    'mp4',
    'mov',
    'wmv',
    'avi',
]

documents = [
    'pdf',
    'docx',
    'txt',
    'odt',
]


def match(extension):
    for item in pictures:
        if item == extension:
            return 'pictures/'
    for item in src:
        if item == extension:
            return 'code/'
    for item in movies:
        if item == extension:
            return 'movies/'
    for item in documents:
        if item == extension:
            return 'documents/'
    return 0


for file in os.listdir():
    extension = os.path.splitext(file)[-1][1:]
    extension = extension.lower()
    directory = match(extension)
    # print(extension)
    if directory:
        target_dir = create_path(main_directory, directory)
        # print(target_dir)
        if os.path.exists(target_dir):
            shutil.move(create_path(main_directory, file), target_dir)
            # print((create_path(main_directory, file), target_dir))
            
        else:
            os.mkdir(target_dir)
            shutil.move(create_path(main_directory, file), target_dir)
            # print((create_path(main_directory, file), target_dir))