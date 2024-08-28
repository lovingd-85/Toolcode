def test_videotoimg(videoPath,svPath):
    videoPath_list = glob.glob(videoPath + "*.avi")
    # videoPath_list = videoPath_list[0:100]
    numFrame = 0
    for Path in videoPath_list:
        cap = cv2.VideoCapture(Path)
        while True:
            if cap.grab():
                flag, img = cap.retrieve()
                if not flag:
                    continue
                else:
                    numFrame += 1
                    newPath = svPath + str(numFrame).zfill(8) + ".jpg"
                    cv2.imencode('.jpg', img)[1].tofile(newPath)
            else:
                break
    print("Picture:{}".format(numFrame))
