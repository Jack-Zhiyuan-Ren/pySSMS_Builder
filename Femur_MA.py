import numpy as np

# def femur_MA(dataModel, answerLeg, rightbone):
#     # Find the muscles in the model
#     muscleType = list(dataModel["Model"]["ForceSet"]["objects"].keys())
#     #muscles = dataModel["Model"]["ForceSet"]["objects"]["muscleType]

# # Identify the left and right leg
#     if answerLeg == rightbone:
#         femurMA = 'femur_r'
#     else:
#         femurMA = 'femur_l'

#     femurMuscle = []
#     femurPlace1 = []
#     femurNR = []
#     femurMuscleType = []

#     muscleTypes = list(dataModel["Model"]["ForceSet"]["objects"].keys())
    
#     for k in range(len(muscleTypes)):
#         muscleType = muscleTypes[k]
#         muscles = dataModel["Model"]["ForceSet"]["objects"].get(muscleType)
        
#     print(muscles)

#     for i in range(len(muscles)):
#         if 'GeometryPath' in muscles[i]:
#             AttachmentSize = list(dataModel["Model"]["ForceSet"]["objects"]["muscleType"][i]['GeometryPath']['PathPointSet']['objects'].keys())
#         else:
#             AttachmentSize = []

#         for j in range(len(AttachmentSize)):
#             MuscleAttachments = muscles[i]['GeometryPath']['PathPointSet']['objects'][AttachmentSize[j]]

#             if len(MuscleAttachments) == 1:  # only one PathPoint of this kind in this muscle
#                 try:
#                     CompareStrings1_femur = femurMA == MuscleAttachments['body']['Text']
#                 except KeyError as e:
#                     if 'body' in str(e):
#                         CompareStrings1_femur = femurMA == re.sub('/bodyset/', '', MuscleAttachments['socket_parent_frame']['Text'])
#                     else:
#                         raise ValueError('Unknown Error in femur_MA check try-catch blocks')

#                 if CompareStrings1_femur:
#                     try:
#                         femurMuscle.append(list(map(float, MuscleAttachments['location']['Text'].split())))
#                     except KeyError:
#                         femurMuscle.append(list(map(float, MuscleAttachments['socket_parent_frame']['Text'].split())))
#                     femurMuscleType.append(muscleType)
#                     femurNR.append(i)
#                     place1 = AttachmentSize[j]
#                     femurPlace1.append(place1)
#             else:  # more of a kind - we need to add {1,%d} after the type
#                 for ii in range(len(MuscleAttachments)):
#                     try:
#                         CompareStrings1_femur = femurMA == MuscleAttachments[ii]['body']['Text']
#                     except KeyError as e:
#                         if 'body' in str(e):
#                             CompareStrings1_femur = femurMA == re.sub('/bodyset/', '', MuscleAttachments[ii]['socket_parent_frame']['Text'])
#                         else:
#                             raise ValueError('Unknown Error in femur_MA check try-catch blocks')

#                     if CompareStrings1_femur:
#                         try:
#                             femurMuscle.append(list(map(float, MuscleAttachments[ii]['location']['Text'].split())))
#                         except KeyError:
#                             femurMuscle.append(list(map(float, MuscleAttachments[ii]['socket_parent_frame']['Text'].split())))
#                         femurMuscleType.append(muscleType)
#                         femurNR.append(i)
#                         place1 = f"{AttachmentSize[j]}{{1,{ii}}}"
#                         femurPlace1.append(place1)
#     print(femurMuscle, femurPlace1, femurNR, femurMuscleType)
#     return femurMuscle, femurPlace1, femurNR, femurMuscleType


## Version 2
## This function finds all the muscle that is related to the femur


def femur_MA(dataModel, answerLeg, rightbone):
    # Find the muscles in the model
    # muscleType = list(dataModel["Model"]["ForceSet"]["objects"].keys())
    # muscles = dataModel.OpenSimDocument.Model.ForceSet.objects[muscleType]
    
    # Identify the left and right leg
    if answerLeg == rightbone:
        femurMA = 'femur_r'
    else:
        femurMA = 'femur_l'
    
    femurMuscle = []
    femurPlace1 = []
    femurNR = []
    femurMuscleType = []
    
    muscleTypes = list(dataModel["Model"]["ForceSet"]["objects"].keys())

    for muscleType in muscleTypes:
        muscles = dataModel["Model"]["ForceSet"]["objects"][muscleType]
       
        for i in range(len(muscles)):
            if 'GeometryPath' in dataModel["Model"]["ForceSet"]["objects"][muscleType][i] and isinstance(dataModel["Model"]["ForceSet"]["objects"][muscleType][i]['GeometryPath'], dict):
                AttachmentSize = dataModel["Model"]["ForceSet"]["objects"][muscleType][i]['GeometryPath']['PathPointSet']['objects']['PathPoint']
            else:
                AttachmentSize = []
            
            for j in range(len(AttachmentSize)):
                MuscleAttachments = AttachmentSize[j]
                if len(MuscleAttachments) == 1:  # only one PathPoint of this kind in this muscle
                    CompareStrings1_femur = femurMA == MuscleAttachments['body']
                    if CompareStrings1_femur:
                        try:
                            femurMuscle.append(np.array(MuscleAttachments['location'].split()).astype(float))
                        except KeyError:
                            femurMuscle.append(float(MuscleAttachments['socket_parent_frame']['Text']))
                        
                        femurMuscleType.append(muscleType)
                        femurNR.append(i)
                        place1 = AttachmentSize[j]
                        femurPlace1.append(place1)
                
                else:  # more of a kind - we need to add {1,%d} after the type
                    CompareStrings1_femur = femurMA == MuscleAttachments['body']
                    if CompareStrings1_femur:
                        try:
                            femurMuscle.append(np.array(MuscleAttachments['location'].split()).astype(float))
                        except KeyError:
                            femurMuscle.append(float(MuscleAttachments['socket_parent_frame']['Text']))
            
                        femurMuscleType.append(muscleType)
                        femurNR.append(i)
                        place1 = f"PathPoint{1,{j}}"
                        femurPlace1.append(place1)
    # print(femurMuscle)
    # print(femurPlace1)
    # print(femurNR)
    # print(femurMuscleType)
    return femurMuscle, femurPlace1, femurNR, femurMuscleType   
