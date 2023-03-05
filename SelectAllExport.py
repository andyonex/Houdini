# Select all nodes in current path with the name "Export_*"

import hou

# Get the current network editor
editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

# Get the current path
path = editor.pwd().path()

# List all nodes in current path
current_nodes = hou.node(path + "/").children()

# List all ndoes with "Export_" in its name
export_nodes = [node for node in current_nodes if "Export_" in node.name()]

# Select all nodes from the export list
for node in export_nodes:
    node.setSelected(True)
