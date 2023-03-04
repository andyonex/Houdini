# Add a parameter with noise expression to the selected node
import hou
import random

# Get the selected node
node = hou.selectedNodes()[0]

# Get all parameters on the node
all_parms = node.parms()

# Create a new list containing only parameters with names that contain "my_"
my_parms = [parm for parm in all_parms if "my_" in parm.name()]

# Get the amount of my_ parameters
index = str(len(my_parms))

# Create parm group
parm_group = node.parmTemplateGroup()


# Set the seed value
random.seed(float(index))

# Generate a random float value between 0 and 1 using the seed
rnd = random.uniform(0, 10)

# Create a new float parameters
parm_noiseAmpl = hou.FloatParmTemplate("m_noise_ampl" + index, "Ampl", 1, join_with_next=True, default_value=(0.4,))
parm_noiseFreq = hou.FloatParmTemplate("m_noise_freq" + index, "Freq", 1, join_with_next=True, default_value=(3.0,))
parm_noiseVal = hou.FloatParmTemplate("my_noise_value" + index, "Noise " + index, 1, default_value=(0.0,))
parm_noiseOffset = hou.FloatParmTemplate("m_noise_offset" + index, "Offset", 1, join_with_next=True, default_value=(rnd,))


# Add folder
folder = hou.FolderParmTemplate("folder" + index, "Noise " + index)

# Define folder type
folder.setFolderType(hou.folderType.Collapsible)

# Add parameters to the folder 
folder.addParmTemplate(parm_noiseVal)
folder.addParmTemplate(parm_noiseAmpl)
folder.addParmTemplate(parm_noiseFreq)
folder.addParmTemplate(parm_noiseOffset)

# Define parameter group used to collect folder/s
group = node.parmTemplateGroup()

# Add folder to group and group to node
group.append(folder)

# Apply group to node interface
node.setParmTemplateGroup(group)

# Get parameter to apply expression to
parm = node.parm("my_noise_value"+index)

# Expresson for frequency
freq = f"$T*ch(\"m_noise_freq{index}\")+ch(\"m_noise_offset{index}\")"

# Final expression for the node 
ex = f"noise({freq},{freq},{freq})*ch(\"m_noise_ampl{index}\")"

# Apply expression to the parameter
parm.setExpression(ex)


