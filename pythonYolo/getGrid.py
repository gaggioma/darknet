import cv2
import numpy as np

image  = cv2.imread("C:\\Users\\magaggio\\Desktop\\NumberDataset\\imgTest\\sudoku.jpg")
#cv2.imshow("Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray", gray)

blur = cv2.GaussianBlur(gray, (5,5), 0)
#cv2.imshow("blur", blur)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imshow("thresh", thresh)

contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_area = 0
c = 0
for i in contours:
        area = cv2.contourArea(i)
        if area > 1000:
                if area > max_area:
                    max_area = area
                    best_cnt = i
                    image = cv2.drawContours(image, contours, c, (0, 255, 0), 3)
        c+=1

mask = np.zeros((gray.shape),np.uint8)
cv2.drawContours(mask,[best_cnt],0,255,-1)
cv2.drawContours(mask,[best_cnt],0,0,2)
#cv2.imshow("mask", mask)

out = np.zeros_like(gray)
out[mask == 255] = gray[mask == 255]
#cv2.imshow("New image", out)

blur = cv2.GaussianBlur(out, (5,5), 0)
#cv2.imshow("blur1", blur)

thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
#cv2.imshow("thresh1", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


c = 0
font = cv2.FONT_HERSHEY_COMPLEX  
for i in contours:

        area = cv2.contourArea(i)
        if area > 200:
            cv2.drawContours(image, contours, c, (0, 255, 0), 3)

            # Used to flatted the array containing 
            # the co-ordinates of the vertices. 
            approx = cv2.approxPolyDP(i, 0.009 * cv2.arcLength(i, True), True)
            n = approx.ravel()  
            i = 0
            for j in n : 
                if(i % 2 == 0): 
                    x = n[i] 
                    y = n[i + 1] 
        
                    # String containing the co-ordinates. 
                    string = str(x) + " " + str(y)  
        
                    if(i == 0): 
                        # text on topmost co-ordinate. 
                        cv2.putText(image, "P", (x, y), 
                                        font, 0.5, (255, 0, 0))  
                    #else: 
                        # text on remaining co-ordinates. 
                        #cv2.putText(image, string, (x, y), font, 0.5, (0, 255, 0))  
                i = i + 1

cv2.imshow("Final Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()