from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt




path = "/Users/ilkedelandcaglar/Downloads/udentıfy/microsoft_try/demo_resimler/isi1_deneme.png"


def find_where_is_everyone(path):
    img = Image.open ( f"{path}" )
    img1 = cv2.imread ( path )
    print('real size')
    print(img1.shape)
    y_distance = float((img1.shape[0]))
    x_distance = (float(img1.shape[1])) ##ikincisi x ilki y
    orta_x = x_distance /2
    orta_y = y_distance/2
    middle_point = orta_y, orta_x

    print('orta nokto y ____ x')
    print(middle_point)




    img1=cv2.imread(path,1)

    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    #lower red
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])


    #upper red
    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(img1,img1, mask= mask)


    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    res2 = cv2.bitwise_and(img1,img1, mask= mask2)

    img3 = res+res2
    img4 = cv2.add(res,res2)         ##en iyi calisani
    img5 = cv2.addWeighted(res,0.5,res2,0.5,0)


    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    smoothed2 = cv2.filter2D(img3,-1,kernel)





    #cv2.imshow('Original',img1)
    #cv2.imshow('Averaging',smoothed)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('mask2',mask2)
    #cv2.imshow('res2',res2)
    #cv2.imshow('res3',img3)


    #cv2.imshow('res4',img4) ## asil olan



    #cv2.imshow('res5',img5)
    #cv2.imshow('smooth2',smoothed2)





    image_copy = img4.copy()

    black_pixels_mask = np.all(img4 == [0, 0, 0], axis=-1)

    non_black_pixels_mask = np.any(img4 != [0, 0, 0], axis=-1)
    # or non_black_pixels_mask = ~black_pixels_mask

    image_copy[black_pixels_mask] = [255, 255, 255]
    image_copy[non_black_pixels_mask] = [0, 0, 0]

    #plt.imshow(image_copy)           #____________debugging icin
    #plt.show()

    width, height = img.size[:2]
    px = np.array(image_copy)

    yukari = float(0)
    sag = float(0)
    sol = float(0)
    asagi = float(0)

    sag_ust =[]
    sol_ust= []
    sag_alt = []
    sol_alt = []

    for i in range(height):
       for j in range(width):
          if(px[i,j,0] == 0 & px[i,j,1] == 0 & px[i,j,2] == 0):
              #print(i,j,px[i,j])   #____________debugging icin
              if i > orta_x and j > orta_y:
                  sag_alt.append("elma")
              if i < orta_x and j > orta_y:
                sol_alt.append ( "elma" )
              if i > orta_x and j < orta_y:
                  sag_ust.append("elma")
              if i < orta_x and j < orta_y:
                  sol_ust.append ( "elma" )

    print("uzunliklar______")
    print ( "sag_ust" )
    print(len(sag_ust))
    print ( "sol_ust" )
    print(len(sol_ust))
    print ( "sag_alt" )
    print(len(sag_alt))
    print ( "sol_alt" )
    print(len(sol_alt))
    print('_______________')


    sayi_sag_ust = float(len(sag_ust))
    sayi_sol_ust = float(len(sol_ust))
    sayi_sag_alt = float(len(sag_alt))
    sayi_sol_alt = float(len(sol_alt))




    if sayi_sag_ust > max(sayi_sol_ust, sayi_sag_alt, sayi_sol_alt):
        print(f"sag ust")
        return (f"sag ust")
    elif sayi_sol_ust > max ( sayi_sag_ust, sayi_sag_alt, sayi_sol_alt ):
        print(f"sol ust")
        return (f"sol ust")
    elif sayi_sag_alt > max ( sayi_sol_ust, sayi_sag_ust, sayi_sol_alt ):
        print(f"sag alt")
        return (f"sag alt")
    elif sayi_sol_alt > max ( sayi_sol_ust, sayi_sag_alt, sayi_sag_ust ):
        print(f"sol alt")
        return (f"sol alt")



    #cv2.waitKey(0)  #kontrol icin
    cv2.destroyAllWindows()

#find_where_is_everyone(path) #____________debugging icin

