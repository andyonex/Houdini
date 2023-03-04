# Use it to quickly preview variouse stage of animation
# Script will create objectMerge node and put selected node to input parameter
# ObjectMerge node will be connected to the null node called "QUICK_PREVIEW" with DisplayFlag on it
# For example: put BoneDeform setup between objectMerge and "Preview"

import hou

if hou.selectedNodes():

    # Get the currently selected node
    selected_node = hou.selectedNodes()[0]

    # Get the parent of the selected node
    parent_node = selected_node.parent()

    # Look for the "QUICK_preview" node in the same location as the selected node        
    if parent_node.node("QUICK_PREVIEW"):
        preview_node = parent_node.node("QUICK_PREVIEW")    
    else:
        # Create "QUICK_preview" since it doesn't exist
        preview_node = parent_node.createNode("null", "QUICK_PREVIEW")

    # Look for the "merge" in the same location as the selected node    
    if parent_node.node("QUICK_PREVIEW_INPUT"):
        merge_node = parent_node.node("QUICK_PREVIEW_INPUT")

    else:
        # Create "QUICK_preview" since it doesn't exist
        merge_node = parent_node.createNode("object_merge", "QUICK_PREVIEW_INPUT")
        # connect preview node with merge
        preview_node.setNextInput(merge_node)

    # Apply selected node to merge node parameter
    merge_node.parm("objpath1").set(selected_node.path())

    # Set display flag on preview node
    preview_node.setDisplayFlag(True)

else:
    # Get the current network editor
    editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

    # Get the current path
    path = editor.pwd().path()

    # if Preview exists set the display flag to it
    if hou.node(path+"/QUICK_PREVIEW"):
        hou.node(path+"/QUICK_PREVIEW").setDisplayFlag(True)


        
