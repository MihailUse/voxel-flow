import cv2

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
video = cv2.VideoWriter('video.mp4', fourcc, 20.0, (640, 360))

for i in range(1014, 1515):
    img = cv2.imread('baseball_{0:05d}.png'.format(i))
    img = cv2.resize(img, (640,360))
    video.write(img)

video.release()
