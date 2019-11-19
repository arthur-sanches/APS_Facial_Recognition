import cv2

def show_webcam(mirror=False):
    """Starts a available webcam and waits for an user input to take a picture or stop"""
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == 32:
            img_name = "aps/user_image.png"
            cv2.imwrite(img_name, img)
            break  # spacebar to take picture and quit
        if cv2.waitKey(2) == 27: 
            break  # esc to quit
    cam.release()
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()