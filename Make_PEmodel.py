import os
import numpy as np
from xml2struct import xml2struct
import xml.etree.ElementTree as ET
from femur_ns import femur_ns
import re 
import shutil


def make_PEmodel_FemurOnly(answerModel, deformed_model, answerMarkerSet, deform_bone, which_leg, angle, angle_NS, geometryFolder):
    place = os.path.join(os.getcwd(), 'DEFORMED_MODEL')
    
    
    # print(answerModel)
    if which_leg == 'R' and deform_bone == 'F':
        answerModel_tmp = answerModel
        answerMarkerSet_tmp = answerMarkerSet
    else:
        answerModel_tmp = place + answerModel
        answerMarkerSet_tmp = place + answerMarkerSet

    
    dataModel = xml2struct(answerModel)
    
    if not os.path.exists("DEFORMED_MODEL\Geometry"):
        os.mkdir("DEFORMED_MODEL\Geometry")
        
    if deform_bone == 'F' and which_leg == 'R':
        for i in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"])):
            if 'attached_geometry' in dataModel["Model"]["BodySet"]["objects"]["Body"][i] and \
               'Mesh' in dataModel["Model"]["BodySet"]["objects"]["Body"][i]["attached_geometry"]:
                if len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["attached_geometry"]["Mesh"]) > 1:
                    for j in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["attached_geometry"]["Mesh"])):
                        try:
                            vtp_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["attached_geometry"]["Mesh"][j]["mesh_file"]["Text"]
                            shutil.copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
                        except:
                            pass
                else:
                    try:
                        vtp_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["attached_geometry"]["Mesh"]["mesh_file.Text"]
                        shutil.copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
                    except:
                        pass
            else:
                try:
                    if len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"]) > 1:
                        for j in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"])):
                            try:
                                vtp_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"][j]["geometry_file"]["Text"]
                                shutil.copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
                            except:
                                pass
                    else:
                        try:
                            vtp_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["VisibleObject"]["GeometrySet"]["objects"]["DisplayGeometry"]["geometry_file"]["Text"]
                            shutil.copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
                        except:
                            pass
                except:
                    pass

            if 'components' in dataModel["Model"]["BodySet"]["objects"]["Body"][i] and \
               'PhysicalOffsetFrame' in dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]:
                if 'attached_geometry' in dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]["PhysicalOffsetFrame"] and \
                   'Mesh' in dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]["PhysicalOffsetFrame"]["attached_geometry"]:
                    if len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]["PhysicalOffsetFrame"]["attached_geometry"]["Mesh"]) > 1:
                        for j in range(len(dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]["PhysicalOffsetFrame"]["attached_geometry"]["Mesh"])):
                            try:
                                vtp_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]["PhysicalOffsetFrame"]["attached_geometry"]["Mesh"][j]["mesh_file"]["Text"]
                                shutil.copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
                            except:
                                pass
                    else:
                        try:
                            vtp_filename = dataModel["Model"]["BodySet"]["objects"]["Body"][i]["components"]["PhysicalOffsetFrame"]["attached_geometry"]["Mesh"]["mesh_file"]["Text"]
                            shutil.copyfile(os.path.join(geometryFolder, vtp_filename), os.path.join(place, 'Geometry', vtp_filename))
                        except:
                            pass
                            
    
    answerNameModel = deformed_model

    # the marker set for this model.
    markerset = xml2struct(answerMarkerSet_tmp)
    answerLegFemur = which_leg
    answerDegFemur = angle
    
    if which_leg == 'R': 
        femur_filename = 'r_femur.vtp'
    else:
        femur_filename = 'l_femur.vtp'
        
                                  
    if answerLegFemur == 'R':  # Rotation of the right foot
    # FA_preAngle = 17.6
    # NS_preAngle = 123.3
    # The added anteversion angle is defined
        angleCorrection = answerDegFemur  # - FA_preAngle
        FA_angle = -(angleCorrection * (np.pi / 180))
        NS_angle = -((angle_NS) * (np.pi / 180))
        # print('FA_angle Make PE')
        # print(FA_angle)
        # print("NS_angle")
        # print(NS_angle)

        # The geometry of the right femur is imported
        dataFemur = xml2struct(os.path.join(geometryFolder, femur_filename))
    else:  # Rotation of the left foot
        # FA_preAngle = 17.6
        # NS_preAngle = 123.3
        # The added anteversion angle is defined
        angleCorrection = answerDegFemur  # - FA_preAngle
        FA_angle = angleCorrection * (np.pi / 180)
        NS_angle = ((angle_NS) * (np.pi / 180))
        # The geometry of the left femur is imported
        dataFemur = xml2struct(os.path.join(geometryFolder, femur_filename))
    #print(dataFemur)
    femur_ns(dataModel, markerset, answerLegFemur, 'R', FA_angle, NS_angle,
         answerNameModel, answerMarkerSet, dataFemur, place)
         
         
    file_path = f"DEFORMED_MODEL/{answerNameModel}.osim"

    with open(file_path, 'r') as f:
        filetext = f.read()

    geometry_path_starts = [match.start() for match in re.finditer(r'<GeometryPath', filetext)]
    geometry_path_ends = [match.end() for match in re.finditer(r'</GeometryPath>', filetext)]

    newFileText = filetext
    
    for i in range(len(geometry_path_starts)):
        section = filetext[geometry_path_starts[i]:geometry_path_ends[i]]
        i1 = section.find('<objects')
        i2 = section.find('</objects')
        if i2 != -1:
            section = section[i1:i2]
            name_idx = [m.start() for m in re.finditer('name=', section)]
            abs_start = 0
            abs_end = 0
            names = []
            full_text = []
            for j in range(len(name_idx)):
                sep = section[name_idx[j] + 5]
                sep2 = section[name_idx[j] + 6:].find(se)
                sep2 = sep2 + name_idx[j] + 6
                names.append(section[name_idx[j] + 6: sep2])
                tmp1 = section[name_idx[j] - 25:].find('<')
                tmp1 = name_idx[j] - 25 + tmp1
                obj_type = section[tmp1:name_idx[j] - 2]
                end_idx = section[tmp1:].find('</' + obj_type)
                end_idx = tmp1 + end_idx
                section[tmp1 - 1:end_idx + len(obj_type) + 1]
                full_text.append(section[tmp1 - 1:end_idx + len(obj_type) + 1])
                if j == 0:
                    abs_start = tmp1 - 1
                if j == len(name_idx) - 1:
                    abs_end = end_idx + len(obj_type) + 1
            order = sorted(range(len(names)), key=lambda k: names[k])
            section_new_order = ''
            for j in order:
                section_new_order += full_text[j]
            newFileText = newFileText.replace(section[abs_start:abs_end], section_new_order)
            
            
    with open('DEFORMED_MODEL/' + answerNameModel + '.osim', 'w') as fid:
        fid.write(newFileText)

         
 


