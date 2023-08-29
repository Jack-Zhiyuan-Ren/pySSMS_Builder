from pathlib import Path
import os, shutil
import numpy as np
from xml2struct import xml2struct
from coordinatesCorrection import coordinatesCorrection
from operator import add
from Femur_MA import femur_MA
from xml2dict import xml2dict
    
    


pathstr = Path.cwd()
os.chdir(pathstr)
model = 'Rajagopal/Rajagopal2015.osim'
geometryFolder = 'Rajagopal/Geometry'
dataModel = xml2struct(model)
dataModel2 = xml2dict(model)

markerset = 'MarkerSet.xml'
markers = xml2struct(markerset)


# print(dataModel2["OpenSimDocument"]["Model"])
#dataModel.OpenSimDocument.Model.BodySet.objects.Body
#len(dataModel.OpenSimDocument.Model.BodySet.objects.Body)

# for i in range(len(dataModel.OpenSimDocument.Model.BodySet.objects.Body)):
#     if 'attached_geometry' in dataModel.OpenSimDocument.Model.BodySet.objects.Body[i] and \
#         'Mesh' in dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].attached_geometry:
#         if len(dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].attached_geometry.Mesh) > 1:
#             for j in range(len(dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].attached_geometry.Mesh)):
#                 try:
#                     vtp_filename = dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].attached_geometry.Mesh[j].mesh_file.Text
#                     copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
#                 except:
#                     pass
#         else:
#             try:
#                 vtp_filename = dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].attached_geometry.Mesh.mesh_file.Text
#                 copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
#             except:
#                 pass
#     else:
#         try:
#             if len(dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].VisibleObject.GeometrySet.objects.DisplayGeometry) > 1:
#                 for j in range(len(dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].VisibleObject.GeometrySet.objects.DisplayGeometry)):
#                     try:
#                         vtp_filename = dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].VisibleObject.GeometrySet.objects.DisplayGeometry[j].geometry_file.Text
#                         copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
#                     except:
#                         pass
#             else:
#                 try:
#                     vtp_filename = dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].VisibleObject.GeometrySet.objects.DisplayGeometry.geometry_file.Text
#                     copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
#                 except:
#                     pass
#         except:
#             pass

#     if 'components' in dataModel.OpenSimDocument.Model.BodySet.objects.Body[i] and \
#         'PhysicalOffsetFrame' in dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components:
#         if 'attached_geometry' in dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components.PhysicalOffsetFrame and \
#             'Mesh' in dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components.PhysicalOffsetFrame.attached_geometry:
#             if len(dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components.PhysicalOffsetFrame.attached_geometry.Mesh) > 1:
#                 for j in range(len(dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components.PhysicalOffsetFrame.attached_geometry.Mesh)):
#                     try:
#                         vtp_filename = dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components.PhysicalOffsetFrame.attached_geometry.Mesh[j].mesh_file.Text
#                         copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
#                     except:
#                         pass
#             else:
#                 try:
#                     vtp_filename = dataModel.OpenSimDocument.Model.BodySet.objects.Body[i].components.PhysicalOffsetFrame.attached_geometry.Mesh.mesh_file.Text
#                     copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
#                 except:
#                     pass


# print(dataModel["Model"]["BodySet"]["objects"]["Body"][4]["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"]["geometry_file"])
#["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"][1]["geometry_file"]



# for i in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"])):
#     print(dataModel["Model"]["BodySet"]["objects"]["Body"][i])
answerLeg = 'R'

# print(dataModel["Model"]["BodySet"]["objects"]["Body"][10]["Joint"]["CustomJoint"]["parent_body"])
# if 'femur_' + answerLeg.lower() == dataModel["Model"]["BodySet"]["objects"]["Body"][3]["Joint"]["CustomJoint"]["parent_body"]:
#     print("yes")
    
# else:
#     print("no")

# =============================================================================
# print(dataModel["Model"]["BodySet"]["objects"]["Body"][3]["WrapObjectSet"]["objects"]["WrapCylinder"][2])
# 
# wrapCnt = 0
# wrapLocations = []
# wrapRotations = []
# wrapIndizes = []
# wrapObjectTypes = dataModel["Model"]["BodySet"]["objects"]["Body"][3]["WrapObjectSet"]["objects"]["WrapCylinder"]
# i = 3
# for j in range(len(wrapObjectTypes)):
#     wrapRotations.append(list(map(float, dataModel["Model"]["BodySet"]["objects"]["Body"][i]["WrapObjectSet"]["objects"]["WrapCylinder"][j]["xyz_body_rotation"].split())))
#     wrapLocations.append(list(map(float, dataModel["Model"]["BodySet"]["objects"]["Body"][i]["WrapObjectSet"]["objects"]["WrapCylinder"][j]["xyz_body_rotation"].split())))
#     for k in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["WrapObjectSet"]["objects"]["WrapCylinder"][j])):
#         wrapCnt += 1
#         wrapIndizes.append([i, j, k])
# print(wrapLocations)
# print(wrapRotations)
# print(wrapIndizes)
# =============================================================================
# =============================================================================
which_leg = 'R'
# print(f'{which_leg.lower()}_femur')
    
# for i in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"])):
#     if f'{which_leg.lower()}_femur' in dataModel["Model"]["BodySet"]["objects"]["Body"][i]:
#         if 'attached_geometry' in dataModel["Model"]["BodySet"]["objects"]["Body"][i]:
#             femur_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["attached_geometry"]["Mesh"]["mesh_file"]["Text"]
#             print(femur_filename + "if")
#         else:
#             femur_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"][i]["geometry_file"]
#             print(femur_filename + "else")
            
#     else:
#         print('False')

# =============================================================================


if which_leg == 'R': 
    femur_filename = 'r_femur.vtp'
else:
    femur_filename = 'l_femur.vtp'



# dataFemur = xml2struct(os.path.join(geometryFolder, femur_filename))
# Femur = np.array(dataFemur["PolyData"]["Piece"]["Points"]["DataArray"].split()).astype(float)
# print(Femur[0])
# Femur_2 = [Femur[i:i+3] for i in range(0, len(Femur), 3)]
# print(coordinatesCorrection(Femur_2))


#polyText = dataFemur.VTKFile.PolyData.Piece.Polys.DataArray[0][0].Text
# print(type(dataFemur["PolyData"]["Piece"]["Polys"]["DataArray"][0]))

# muscleType = list(dataModel["Model"]["ForceSet"]["objects"].keys())
# print(dataModel["Model"]["ForceSet"]["objects"].get('CoordinateActuator'))

# print(markers["MarkerSet"]["objects"]["Marker"][1]["location"])
# print(markers["MarkerSet"]["objects"]["Marker"][1]["location"].strip().split())
# a = markers["MarkerSet"]["objects"]["Marker"][1]["location"].strip().split()

# for i  in  range(len(a)): 
#     a[i] = float(a[i])
# print(type(a[0]))


#markerset.OpenSimDocument.MarkerSet.objects.Marker

# SEL = [-28.5309, 5.3055, -3.3018] / 1000
# =============================================================================
# print(np.divide( [-28.5309, 5.3055, -3.3018], 1000))
# =============================================================================

# =============================================================================
# a = [1, 2, 3]
# b = [4, 5, 6]
# 
# 
# print(list(map(add,a,b)))
# =============================================================================


# =============================================================================
# SEL = np.divide([-28.5309, 5.3055, -3.3018], 1000)
# SEL_epi = np.divide([1.799, -19.7590, -418.0754],1000)
# HC = np.divide([-0.1583, -0.2439, 0.0038],1000)
# ISTHMUS = np.divide([-17.2534, 4.2462, -14.4892],1000)
# 
# point1 = SEL
# point2 = SEL_epi
# t = np.arange(0, 1, 0.001)
# C = np.tile(point1, (len(t), 1)).T + np.outer((point2 - point1), t)
# SEL_point = C[:, 111]
# 
# translationDis = np.array([0, 0, 0]) - SEL_point
# =============================================================================

# print(translationDis)

# =============================================================================
# SEL_epiShaft = SEL_epi + translationDis
# SEL_pointShaft = SEL_point + translationDis
# headShaft = HC + translationDis
# isthmusShaft = ISTHMUS + translationDis
# =============================================================================


# print((headShaft-isthmusShaft).T)
# =============================================================================
femur_filename = 'r_femur.vtp'
dataFemur = xml2struct(os.path.join(geometryFolder, femur_filename))
# femur = np.array(dataFemur["PolyData"]["Piece"]["Points"]["DataArray"].split()).astype(float)
# femur_2 = [femur[i:i+3] for i in range(0, len(femur), 3)]
# femur_start = coordinatesCorrection(femur_2)
# 
# 
# femurShaftLoc = [list(map(add,i , translationDis)) for i in np.transpose(femur_start)]
# =============================================================================
# print(femurShaftLoc)

# aZY = SEL_epiShaft[0, 1:3] - np.array([0, 0])


# femurShaftLoc = []
# for i in femur_start.T:
#     femurShaftLoc.append(i + translationDis)
# # print(femurShaftLoc)


#Fmeur MA testing section
muscleTypes = list(dataModel["Model"]["ForceSet"]["objects"].keys())
# print(muscleTypes)

# print(dataModel2["OpenSimDocument"]["Model"]["ForceSet"]["objects"]["Millard2012EquilibriumMuscle"][0]["@name"])
a = dataModel["Model"]["ForceSet"]["objects"]["Millard2012EquilibriumMuscle"][0]["GeometryPath"]['PathPointSet']['objects']["PathPoint"][0]["location"]
b = np.array(a.split()).astype(float)
# print(b)
# print(len(b))
# for muscleType in muscleTypes:
#     muscles = dataModel["Model"]["ForceSet"]["objects"][muscleType]
#     print(muscleType)
#     print(len(muscles))
# rightbone = 'R'
# femurMuscle, femurPlace1, femurNR, femurMuscleType = femur_MA(dataModel, answerLeg, rightbone)
# print(femurPlace1)


AttachmentSize = dataModel["Model"]["ForceSet"]["objects"]["Millard2012EquilibriumMuscle"][1]['GeometryPath']['PathPointSet']['objects']['PathPoint']
# print(AttachmentSize)
MuscleAttachments = AttachmentSize[0]
c = np.array(MuscleAttachments['location'].split()).astype(float)
# print(c)

polyText = dataFemur["PolyData"]["Piece"]["Polys"]["DataArray"][0]
polysplit = polyText.split('\n')
# print(polysplit)
#====
poly3 = []
for i in range(len(polysplit)):
    poly3.append(np.array(polysplit[i].split()).astype(float))
polys = []
for i in range(1,len(poly3) - 1):
    polys.append(poly3[i] + 1)
polys = np.array(polys)
#====
print(polys)
