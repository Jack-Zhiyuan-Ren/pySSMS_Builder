from pathlib import Path
import os, shutil
from xml2struct import xml2struct

from Make_PEmodel import make_PEmodel_FemurOnly

    
    


pathstr = Path.cwd()
os.chdir(pathstr)

folder = 'C:/Users/jackr/OneDrive/Documents/GitHub/Ren_Femur_Twist_Python-copy/DEFROMED_MODEL'
#deleteing the files that was in folder
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        
# mfile_name = mfilename('fullpath');
# [pathstr,name,ext] = fileparts(mfile_name);
# cd(pathstr);
# try
    # delete('DEFORMED_MODEL/*');
# end
# addpath(genpath(pwd))

##values for Rajagopal as base model

model = 'Rajagopal/Rajagopal2015.osim'
GeometryFolder = 'Rajagopal/Geometry'
applyTibiaTorsionToJointOffset = 1
default_Anteversion = 21
default_NeckShaftAngle = 121
default_TibiaTorsion = 24

markerset = 'MarkerSet.xml'

deform_bone = 'F'
which_leg = 'R'
angle_AV_right = 15.7 #right anteversion angle (in degrees) 
angle_NS_right = 180  # right neck-shaft angle (in degrees) 

deformed_model = 'rightNSA'+  str(angle_NS_right) + '_rightAVA' + str(angle_AV_right)


make_PEmodel_FemurOnly(model, deformed_model, markerset, deform_bone, which_leg, angle_AV_right, angle_NS_right, GeometryFolder,)

# model = deformed_model + '.osim'
# markerset = deformed_model + '_' + markerset
# deform_bone = 'F'
# which_leg = 'L'
# angle_AV_left = 12.5
# angle_NS_left = 129.5
# deformed_model = deformed_model = 'leftNSA' + str(angle_NS_left) + '_leftAVA' + str(angle_AV_left)
# make_PEmodel_FemurOnly( model, deformed_model, markerset, deform_bone, which_leg, angle_AV_left - default_Anteversion, angle_NS_left - default_NeckShaftAngle, GeometryFolder)
