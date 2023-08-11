import os
import shutil
import exiftool

paths = {
    "main camera": "G:\\PRIVATE\\M4ROOT\\CLIP",
    "hupa camera": "D:\\PRIVATE\\M4ROOT\\CLIP",
    "drone": "H:\\DCIM\\100MEDIA",
    "sound": "F:\\MUSIC"
}


def move_files(origin_path, dest_path):
    os.chdir(origin_path)
    counter = 0
    for file in os.listdir():
        # if file.contains(".XML"):
        #    continue
        shutil.copy2(file, dest_path)
        counter += 1
    print(str(counter) + " files have copied to " + dest_path)


print("Enter the name of the bride:")
bride = input()
print("Enter the name of the groom:")
groom = input()
print("Enter the date DDMMYY:")
date = input()
nameOfCouple = bride + " and " + groom + " " + date
# curren_path = "C:\\Users\\danie\\Desktop\\moveToHdd"
curren_path = "C:\\Users\\danie\\OneDrive - Technion\\work\\trying_to_upload"
os.makedirs(os.path.join(curren_path, nameOfCouple))
curren_path += "\\" + nameOfCouple
# os.chdir(curren_path)

for subdir, origin_path in paths.items():
    os.makedirs(os.path.join(curren_path, subdir))
    dest_path = os.path.join(curren_path, subdir)
    try:
        move_files(origin_path, dest_path)
    except OSError:
        print("Missing", subdir)
        os.rmdir(dest_path)



# os.makedirs("main camera")
# os.makedirs("sound")
# os.makedirs("drone")
# os.makedirs("hupa camera")
# origin_path = MAIN_CAMERA_PATH
# dest_path = curren_path + "\\main camera"
# try:
#     move_files(origin_path, dest_path)
# except OSError:
#     print("missing main camera")
#     os.rmdir(dest_path)
# origin_path = DRONE_PATH
# dest_path = curren_path + "\\drone"
# try:
#     move_files(origin_path, dest_path)
# except OSError:
#     print("missing drone")
#     os.rmdir(dest_path)
#
# origin_path = HUPA_CAMERA_PATH
# dest_path = curren_path + "\\hupa camera"
# try:
#     move_files(origin_path, dest_path)
# except OSError:
#     print("missing hupa camera")
#     os.rmdir(dest_path)
#
# origin_path = SOUND_PATH
# dest_path = curren_path + "\\sound"
# try:
#     move_files(origin_path, dest_path)
# except OSError:
#     print("missing sound")
#     os.rmdir(dest_path)
