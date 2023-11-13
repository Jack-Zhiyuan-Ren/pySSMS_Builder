# Torsion_Tool_Python
<div align="center">
  <img src=".github/Finsihed_Femur.png" width="500" >
</div>
<div align="center">
  <em>Transformed Femur</em>
</div>

$~$

Torsion_Tool_Python is a Python-based program that generates subject-specific musculoskeletal OpenSim models. The program requires two input angles, the Neck Shaft Angle(NSA) and the Anteversion Angle(AVA), which can be measured from the patient's CT scan.

## Why Musculoskeletal Models?
<div align="center">
  <img src=".github/SSMS.png" width="300" >
</div>
Subject-specific musculoskeletal (SSMS) models provide an accurate way to evaluate human movements that is non-invasive and ethical. In a study that investigates patients with motor disabilities such as Cerebral Palsy, the gait analysis of the SSMS determined the patient’s excessive internally rotated gaited is mainly caused by his abnormally anteverted femur, not by the short hamstrings and adductors that the researchers previously assumed (Delp et al., 2002). In such studies, the subject-specific musculoskeletal models are generated from magnetic resonance imaging (MRI) and/or Computed Tomography (CT) Scans (Veerkamp et al., 2021).  The developing process is time-consuming and requires a high level of expertise, which makes patient-specific studies nearly impossible for doctors to operate by 
themselves (Modenese et al., 2018). To streamline this process, the Subject-specific models can be generated by modifying a few characteristics geometries, such as the tibia torsion, femoral neck-shaft angle (NSA), and anteversion angle (AVA), of generic OpenSim (Delp et al., 1990) models. However, currently, there is no open-source tool with a free license available to generate such models. 

## What are NSA and AVA?

<div align="center">
  <img src=".github/NSAandAVA.png" width="300" >
</div>

The neck shaft angle (NSA) is defined as the angle between the neck axis and the shaft axis. The anteversion angle (AVA) is the angle between the neck axis and the medial-lateral axis through the epicondyles in a plane perpendicular to the shaft axis. The NSA and AVA of the generic femur were calculated to be 123 and 17◦, respectively (Veerkamp et al., 2021). NSA and AVA are the most important aspect of the proximal femoral geometry because they have the highest impact on muscle-tendon moment arms and joint contact forces (Kainz et al,. 2020)

## Workflow of this Program
<div align="center">
  <img src=".github/Flow.png" width="400" >
</div>


The diagram above demonstrates the basic workflow of the program TorsionTool_Python.Once these values are obtained from the subject’s CT scan, two rotation angles are calculated by finding the difference between the subject’s AVA and NSA angles and the generic model’s AVA and NSA angles (Offset Method). After that, the 
generic bone is sectioned into three parts (shown in 
the figure below) and the transformation will 
be performed separately. The vertices in the inner box
rotate first through an offset angle corresponding to 
the change in anteversion. Then the middlebox rotates 
through an angle that is decreased linearly as a 
function of superior-inferior distance along the axis. 
In the final step, the outer box that contains the entire 
femur is translated to restore the position of the 
femoral head. After the program finishes running, 
A new subject-specific OpenSim model is generated 
with updated geometries.

<div align="center">
  <img src=".github/boxes.png" width="200" >
</div> 

## Installation

1. On GitHub.com, navigate to the main page of the repository.
2. Above the list of files, click  Code.

<div align="center">
  <img src=".github/code-button.png" width="300" >
</div> 

3. Click Download ZIP.
4. Extract all the files to a designated folder
<div align="center">
  <img src=".github/Extract.png" width="300" >
</div> 


## Instructions
0. Before running the program. Make sure to install [numpy](https://numpy.org/install/), [scipy](https://scipy.org/install/), and [matplotlib](https://stackoverflow.com/questions/37661119/python-mpl-toolkits-installation-issue) modules
1. In the the "Ren_Femur_Twist_Python-copy-main" folder, create a new folder called "DEFORMED_MODEL".
2. Fix the folder file path to your own current directory path and keep the "/DEFORMED_MODEL"
<div align="left">
  <img src=".github/Direction2.png" width="400" >
</div> 

2. Go to Main_FemurTorsionTool.
3. Enter the AVA and NSA measured from the CT scan.
For Mac users if the following error is encountered.
<div align="left">
  <img src=".github/File_not_found_error.png" width="400" >
</div> 
Go to "Make_PEmodel" file, change the "/" to "\" as shown in the following image.
<div align="left">
  <img src=".github/fix.png" width="400" >
</div> 
# If error "Rajagoal/Rajagopal2015.osim not found" pops up, make sure to open the folder in the VScode explorer.

## References
<div align="left">
  <img src=".github/Reference.png" width="400" >
</div> 


