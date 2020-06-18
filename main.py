import cv2 as cv
import os
import settings

bread_path = os.path.join(os.getcwd(), settings.ORGIN_IMG_PATH)
breads = os.listdir(bread_path)

new_bread_path = os.path.join(os.getcwd(), settings.DESTINATION_IMG_PATH)

for bread in breads:
  img_path = os.path.join(bread_path, bread)
  imgs_name = os.listdir(img_path)
  for img_name in imgs_name:
    try:
      img = (os.path.join(img_path, img_name)).replace('\\','/')
      src_img = cv.imread(img, cv.IMREAD_COLOR)
      dst_img = cv.resize(src_img, (128, 128), interpolation=cv.INTER_NEAREST)

    except Exception as e:
      print(str(e), e)
    dst_bread_dir = os.path.join(new_bread_path, bread)
    dst_file_path = os.path.join(new_bread_path, bread, img_name)
    print('-----------------------')
    print(dst_file_path)
    
    if not os.path.isdir(dst_bread_dir):
      try:
        os.makedirs(dst_bread_dir)
      except FileExistsError:
        print("檔案已經存在")
    cv.imwrite(dst_file_path, dst_img)
