# -*- coding: utf-8 -*-
'''
此程序读取videoPath文件目录下的4个视频文件，并显示出来
'''

import cv2
import numpy as np
import os


def showVideo(videoPath):
	files = os.listdir(videoPath)
	num = len(files)
	cap = []
	for i in range(num):
		print('第%d个视频：' % i, files[i])
		# cap.append(cv2.VideoCapture(0))
		cap.append(cv2.VideoCapture(videoPath + '/' + files[i]))

	print('size:', cap[1].read()[1].shape)

	while True:
		faces1, frame1=cap[0].read()
		faces2, frame2=cap[1].read()
		faces3, frame3=cap[2].read()
		faces4, frame4=cap[3].read()

		frameLeft=cv2.resize(frame1, (480, 360), interpolation=cv2.INTER_CUBIC)
		frame11=cv2.resize(frame1, (240, 180), interpolation=cv2.INTER_CUBIC)
		frame12=cv2.resize(frame2, (240, 180), interpolation=cv2.INTER_CUBIC)
		frame13=cv2.resize(frame3, (240, 180), interpolation=cv2.INTER_CUBIC)
		frame14=cv2.resize(frame4, (240, 180), interpolation=cv2.INTER_CUBIC)
		frame_1=np.hstack([frame11, frame12])
		frame_2=np.hstack([frame13, frame14])
		frameRight=np.vstack([frame_1, frame_2])
		frame=np.hstack([frameLeft, frameRight])

		cv2.imshow('video', frame)
		c=cv2.waitKey(1)
		if c == 27:
			break

	for i in range(num):
		cap[i].release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	videoPath='./video'
	showVideo(videoPath)


'''
import cv2
cap = cv2.VideoCapture(0)
while True:
	ret, frame = cap.read()
	c = waitKey(1)
	if c == 27:
		break;
cap.release()
cv2.destroyAllWindows()

1、cap = cv2.VideoCapture(0)
VideoCapture()中参数是0，表示打开笔记本的内置摄像头，
参数是视频文件路径则打开视频，如cap = cv2.VideoCapture("../test.avi")

2、ret,frame = cap.read()
 cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。
其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。

3、cv2.waitKey(1)，waitKey（）方法本身表示等待键盘输入，
参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停,；
参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿。
c得到的是键盘输入的ASCII码，esc键对应的ASCII码是27，即当按esc键是if条件句成立

4、调用release()释放摄像头，调用destroyAllWindows()关闭所有图像窗口。
'''
