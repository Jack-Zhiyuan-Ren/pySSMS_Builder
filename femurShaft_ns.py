import numpy as np
from operator import add

def femurShaft_ns(dataModel, femur_start, answerLeg, rightbone, femurMuscle_start, markerFemur_start, wrapLocations):


    if answerLeg == rightbone:
        SEL = np.divide([-28.5309, 5.3055, -3.3018], 1000)
        SEL_epi = np.divide([-1.799, -19.7590, -418.0754], 1000)
        HC = np.divide([-0.1583, -0.2439, 0.0038],1000)
        ISTHMUS = np.divide([-17.2534, 4.2462, -14.4892],1000)
    else:
        SEL = np.divide([28.5309, 5.3055, -3.3018],1000)
        SEL_epi = np.divide([1.799, -19.7590, -418.0754],1000)
        HC = np.divide([0.1583, -0.2439, 0.0038],1000)
        ISTHMUS = np.divide([17.2534, 4.2462, -14.4892],1000)

    point1 = SEL
    point2 = SEL_epi
    t = np.arange(0, 1, 0.001)
    C = np.tile(point1, (len(t), 1)).T + np.outer((point2 - point1), t)
    SEL_point = C[:, 111]

    translationDis = np.array([0, 0, 0]) - SEL_point
    #print(translationDis)

    # the bone
    femurShaftLoc = []
    # print('femur_start.T')
    # print(femur_start)
    for i in femur_start: ##Didn't need the transpose
        # print("i")
        # print(i)
        # print("translationDis")
        # print(translationDis)
        femurShaftLoc.append(i + translationDis)

    SEL_epiShaft = SEL_epi + translationDis
    SEL_pointShaft = SEL_point + translationDis
    headShaft = HC + translationDis
    isthmusShaft = ISTHMUS + translationDis

    # the muscle attachments
    #femurShaftLocMA = np.array([(map(add,i , translationDis)) for i in np.transpose(femurMuscle_start)])
    femurShaftLocMA = []
    for j in femurMuscle_start: ## Didn't need the transpose
        femurShaftLocMA.append(j + translationDis)
    

    # the markers
    femurShaftLocMarkers = markerFemur_start + translationDis
    # print('femurShaftLocMarkers')
    # print(femurShaftLocMarkers)
    aZY = np.array([SEL_epiShaft[1],SEL_epiShaft[2]]) - np.array([0, 0])
    bZY = np.array([0, -0.4]) - np.array([0, 0])
    angleZY = np.arccos(np.dot(aZY, bZY) / (np.linalg.norm(aZY) * np.linalg.norm(bZY)))
    Rx = np.array([[1, 0, 0], [0, np.cos(angleZY), -np.sin(angleZY)], [0, np.sin(angleZY), np.cos(angleZY)]])

    aZX = np.array([SEL_epiShaft[0],SEL_epiShaft[2]]) - np.array([0, 0])
    bZX = np.array([0, 0.4]) - np.array([0, 0])
    angleZX = np.pi - np.arccos(np.dot(aZX, bZX) / (np.linalg.norm(aZX) * np.linalg.norm(bZX)))

    if answerLeg == rightbone:  # right leg
        Ry = np.array([[np.cos(angleZX), 0, np.sin(angleZX)], [0, 1, 0], [-np.sin(angleZX), 0, np.cos(angleZX)]])
    else:
        # This is for the left femur
        Ry = np.array([[np.cos(-angleZX), 0, np.sin(-angleZX)], [0, 1, 0], [-np.sin(-angleZX), 0, np.cos(-angleZX)]])

    R_transfer = np.dot(Ry, Rx)
    # print(R_transfer)

    tmp = np.dot(R_transfer, (headShaft - isthmusShaft).T).T
    aXY = [tmp[0],tmp[1]]

    if answerLeg == rightbone:  # right leg
        bXY = np.array([0.4, 0])
        angleXY = np.arccos(np.dot(aXY, bXY) / (np.linalg.norm(aXY) * np.linalg.norm(bXY)))
        Rz = np.array([[np.cos(angleXY), -np.sin(angleXY), 0], [np.sin(angleXY), np.cos(angleXY), 0], [0, 0, 1]])
    else:
        bXY = np.array([-0.4, 0])
        angleXY = np.arccos(np.dot(aXY, bXY) / (np.linalg.norm(aXY) * np.linalg.norm(bXY)))
        Rz = np.array([[np.cos(-angleXY), -np.sin(-angleXY), 0], [np.sin(-angleXY), np.cos(-angleXY), 0], [0, 0, 1]])

    R_transfer = np.dot(Rz, np.dot(Ry, Rx))

    femurShaftLocRot = np.transpose(np.dot(R_transfer, np.transpose(femurShaftLoc)))

    wrapLocationsRot = np.dot(R_transfer, wrapLocations.T).T

    print('in_femurShaft')
    print('wrapLocationRot')
    print(wrapLocationsRot)
    

    SEL_epiShaftRot = np.dot(R_transfer, SEL_epiShaft.T).T
    SEL_pointShaftRot = np.dot(R_transfer, SEL_pointShaft.T).T
    headShaftRot = np.dot(R_transfer, headShaft.T).T
    isthmusShaftRot = np.dot(R_transfer, isthmusShaft.T).T

    femurShaftLocRotMA = np.transpose(np.dot(R_transfer, np.transpose(femurShaftLocMA)))

    femurShaftLocRotMarkers = []
    # print('R_Transfer')
    # print(R_transfer)
    # print('markerFemur_start')
    # print(markerFemur_start)

    for i in range(markerFemur_start.shape[0]):
        item = np.transpose(np.matmul(R_transfer, femurShaftLocMarkers[i]))
        # print("R_transfer")
        # print(R_transfer)
        # print("markerFemur_start[i]")
        # print(np.transpose(markerFemur_start)[i])
        # print("item")
        # print(item)
        femurShaftLocRotMarkers.append(item)

    femurShaftLocRotMarkers = np.array(femurShaftLocRotMarkers)

    HeadNeck = []
    LesserTroc = []
    Shaft = []
    Condylar = []
    FemurShaftAxis = SEL_epiShaftRot - SEL_pointShaftRot  # vector from bottom to top
    magn_FemurShaftAxis = np.linalg.norm(FemurShaftAxis)

    for i in range(femurShaftLocRot.shape[0]):
        itemVector = femurShaftLocRot[i, :] - SEL_pointShaftRot  # vector from each point to the max point
        # the projection of vector each vector on the largest vector
        item = np.dot(itemVector, FemurShaftAxis) / magn_FemurShaftAxis
        if item <= 0.12 * (magn_FemurShaftAxis / 16):
            HeadNeck.append(femurShaftLocRot[i, :])
        elif item < 1.45 * (magn_FemurShaftAxis / 16) and item > 0.12 * (magn_FemurShaftAxis / 16):
            LesserTroc.append(femurShaftLocRot[i, :])
        elif item < 14 * (magn_FemurShaftAxis / 16) and item > 1 * (magn_FemurShaftAxis / 16):
            Shaft.append(femurShaftLocRot[i, :])
        else:
            Condylar.append(femurShaftLocRot[i, :])
    # print("shaft")
    # print(Shaft[0] - [0.1, 0, 0])

    # Divide the shaft into proximal and distalt part
    ShaftProx = []
    ShaftDist = []
    FemurShaftAxis = SEL_epiShaftRot - SEL_pointShaftRot  # vector from bottom to top
    magn_FemurShaftAxis = np.linalg.norm(FemurShaftAxis)
    for i in range(len(Shaft)):
        itemVector = Shaft[i] - SEL_pointShaftRot  # vector from each point to the max point
        # the projection of vector each vector on the largest vector
        item = np.dot(itemVector, FemurShaftAxis) / magn_FemurShaftAxis
        if item <= 0.5 * (magn_FemurShaftAxis / 2):
            ShaftProx.append(Shaft[i])
        else:
            ShaftDist.append(Shaft[i])
            

    HeadNeckMA = []
    LesserTrocMA = []
    ShaftMA = []
    CondylarMA = []

    FemurShaftAxisMA = SEL_epiShaftRot - SEL_pointShaftRot  # vector from bottom to top
    magn_FemurShaftAxisMA = np.linalg.norm(FemurShaftAxisMA)

    for i in range(femurShaftLocRotMA.shape[0]):
        itemVector = femurShaftLocRotMA[i, :] - SEL_pointShaftRot  # vector from each point to the max point
        item = np.dot(itemVector, FemurShaftAxisMA) / magn_FemurShaftAxisMA  # the projection of vector each vector on the largest vector
        
        if item <= 0.12 * (magn_FemurShaftAxisMA / 16):
            HeadNeckMA.append(femurShaftLocRotMA[i, :])
        elif item < 1.45 * (magn_FemurShaftAxisMA / 16) and item > 0.12 * (magn_FemurShaftAxisMA / 16):
            LesserTrocMA.append(femurShaftLocRotMA[i, :])
        elif item < 14 * (magn_FemurShaftAxisMA / 16) and item > (magn_FemurShaftAxisMA / 16):  # limit for the shaft %0.395
            ShaftMA.append(femurShaftLocRotMA[i, :])
        else:
            CondylarMA.append(femurShaftLocRotMA[i, :])

    ShaftProxMA = []
    ShaftDistMA = []

    FemurShaftAxisMA = SEL_epiShaftRot - SEL_pointShaftRot  # vector from bottom to top
    magn_FemurShaftAxisMA = np.linalg.norm(FemurShaftAxisMA)

    for i in range(len(ShaftMA)):
        itemVector = ShaftMA[i] - SEL_pointShaftRot  # vector from each point to the max point
        item = np.dot(itemVector, FemurShaftAxisMA) / magn_FemurShaftAxisMA  # the projection of vector each vector on the largest vector
        
        if item <= 0.5 * (magn_FemurShaftAxisMA / 2):
            ShaftProxMA.append(ShaftMA[i])
        else:
            ShaftDistMA.append(ShaftMA[i])
            
            
    HeadNeckMarkers = []
    LesserTrocMarkers = []
    ShaftMarkers = []
    CondylarMarkers = []

    FemurShaftAxisMarkers = SEL_epiShaftRot - SEL_pointShaftRot  # vector from bottom to top
    magn_FemurShaftAxisMarkers = np.linalg.norm(FemurShaftAxisMarkers)
    
    # print('femurShaftLocRotMarkers')
    # print(femurShaftLocRotMarkers)
    
    for i in range(femurShaftLocRotMarkers.shape[0]):
        itemVector = femurShaftLocRotMarkers[i, :] - SEL_pointShaftRot  # vector from each point to the max point
        item = np.dot(itemVector, FemurShaftAxisMarkers) / magn_FemurShaftAxisMarkers  # the projection of vector each vector on the largest vector
        
        if item <= 0.12 * (magn_FemurShaftAxisMarkers / 16):
            HeadNeckMarkers.append(femurShaftLocRotMarkers[i, :])
        elif item < 1.45 * (magn_FemurShaftAxisMarkers / 16) and item > 0.12 * (magn_FemurShaftAxisMarkers / 16):
            LesserTrocMarkers.append(femurShaftLocRotMarkers[i])
        elif item < 14 * (magn_FemurShaftAxisMarkers / 16) and item > (magn_FemurShaftAxisMarkers / 16):  # limit for the shaft
            ShaftMarkers.append(femurShaftLocRotMarkers[i, :])
        else:
            CondylarMarkers.append(femurShaftLocRotMarkers[i, :])
            
            
    ShaftProxMarkers = []
    ShaftDistMarkers = []

    FemurShaftAxisMarkers = SEL_epiShaftRot - SEL_pointShaftRot  # vector from bottom to top
    magn_FemurShaftAxisMarkers = np.linalg.norm(FemurShaftAxisMarkers)

    for i in range(len(ShaftMarkers)):
        itemVector = ShaftMarkers[i, :] - SEL_pointShaftRot  # vector from each point to the max point
        item = np.dot(itemVector, FemurShaftAxisMarkers) / magn_FemurShaftAxisMarkers  # the projection of vector each vector on the largest vector
        
        if item <= 0.5 * (magn_FemurShaftAxisMarkers / 2):
            ShaftProxMarkers.append(ShaftMarkers[i, :])
        else:
            ShaftDistMarkers.append(ShaftMarkers[i, :])
            
            
    innerBox = HeadNeck
    innerBoxMA = HeadNeckMA  # the top part of the femur (femoral head and greater SEL_point)
    innerBoxMarker = HeadNeckMarkers
    middleBox = np.concatenate((LesserTroc, ShaftProx), axis=0)  # the lesser SEL_point and proximal part of the femur
    middleBoxMA = np.concatenate((LesserTrocMA, ShaftProxMA), axis=0)
    # print('LesserTrocMarkers')
    # print(LesserTrocMarkers)
    # print('ShaftProxMA')
    # print(ShaftProxMA)
    middleBoxMarker = np.concatenate((LesserTrocMA, ShaftProxMA), axis=0) ## Why middle Box MA is the same as middleBoxMarker
    outerBox = np.concatenate((HeadNeck, LesserTroc, Shaft), axis=0)  # everything except for the condylar
    outerBox_less = np.concatenate((ShaftDist, Condylar), axis=0)  # everything apart from inner and middle box
    
    # print('middleboxmarker')
    # print(middleBoxMarker)

    # print("wrapLocation_NewAxis femurshaft_ns")
    # print(wrapLocationsRot)
    # print(innerBox, middleBox, innerBoxMA, innerBoxMarker, middleBoxMA, middleBoxMarker,femurShaftLocRot, headShaftRot, \
    # angleZX, angleZY,angleXY,translationDis, femurShaftLocRotMA, femurShaftLocRotMarkers, \
    # Condylar,ShaftProx,ShaftDist, CondylarMA,ShaftDistMA,CondylarMarkers, ShaftMarkers, wrapLocationsRot)
    # print("femurShaftLocRot")
    # print(femurShaftLocRot)

    return  innerBox, middleBox, innerBoxMA, innerBoxMarker, middleBoxMA, middleBoxMarker,femurShaftLocRot, headShaftRot, \
    angleZX, angleZY,angleXY,translationDis, femurShaftLocRotMA, femurShaftLocRotMarkers, \
    Condylar,ShaftProx,ShaftDist, CondylarMA,ShaftDistMA,CondylarMarkers, ShaftMarkers, wrapLocationsRot




    

