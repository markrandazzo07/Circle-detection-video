# import the necessary packages
import cv2
import numpy as np
import cv2 as cv

def circleDetection(cap):
    while True:
        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray_blurred = cv2.blur(gray, (3, 3))
        detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 100, minRadius=240, maxRadius=700)
        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                # Draw the circumference of the circle.
                cv2.circle(frame, (a, b), r, (255, 0, 0), 10)

                # Draw a middle dot to show the center.
                cv2.circle(frame, (a, b), 1, (34, 167, 255), 10)
                cv2.imshow("Detected Circle", frame)
                cv2.waitKey(1)

    cap.release()
    cv.destroyAllWindows()
