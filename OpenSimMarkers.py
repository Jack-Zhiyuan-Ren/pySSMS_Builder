from xml2struct import xml2struct

def OpenSimMarkers(markerset, answerLeg, rightbone):
    markerSize = len(markerset["MarkerSet"]["objects"]["Marker"])
    markerCalcn = []
    markerTibia = []
    markerCalcnNR = []
    markerTibiaNR = []
    markerFemur = []
    markerFemurNR = []

    if answerLeg == rightbone:
        for i in range(markerSize):
            try:
                bonepart = markerset["MarkerSet"]["objects"]["Marker"][i]["body"]
            except Exception as e:
                if 'body' in str(e):
                    bonepart = markerset["MarkerSet"]["objects"]["Marker"][i]["body"]
                else:
                    raise Exception('Unknown Error in OpenSimMarkers regarding bonepart, check try-catch blocks')
            
            if 'femur_r' in bonepart:
                a = markerset["MarkerSet"]["objects"]["Marker"][i]["location"].strip().split()
                for j in  range(len(a)): 
                    a[j] = float(a[j])
                markerFemur.append(a)
                markerFemurNR.append(i)
    else:
        for i in range(markerSize):
            try:
                bonepart = markerset["MarkerSet"]["objects"]["Marker"][i]
            except Exception as e:
                if 'body' in str(e):
                    bonepart = markerset["MarkerSet"]["objects"]["Marker"][i]
                else:
                    raise Exception('Unknown Error in OpenSimMarkers regarding bonepart, check try-catch blocks')
            
          
            if 'femur_l' in bonepart:
                a = markerset["MarkerSet"]["objects"]["Marker"][i]["location"].strip().split()
                for j in  range(len(a)): 
                    a[j] = float(a[j])
                markerFemur.append(a)
                markerFemurNR.append(i)
                
    return markerCalcn, markerTibia, markerCalcnNR, markerTibiaNR, markerFemur, markerFemurNR
