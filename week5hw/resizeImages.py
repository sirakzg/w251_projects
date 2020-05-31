import cv2
import glob

root_folder = "flower_photos/*"


for file in glob.glob(root_folder):
	img = cv2.imread(file)
	resized = cv2.resize(img, (299,299), interpolation = cv2.INTER_NEAREST)
	cv2.imwrite(file, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 95])