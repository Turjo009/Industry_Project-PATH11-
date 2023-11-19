##Find run these commands in terminal:
#pip install networkx
#pip install pyvis
## then run this python file to create a html file which demonstrates the graph.

import networkx as nx
from pyvis.network import Network

# Create a directed graph
G = nx.DiGraph()

# Input your data here.
# You should replace this with your complete data.
data = [
    {
    "Plant Item": "CLEAN101",
    "Connect from": "ELEVATOR_SWICTH_1",
    "Connect to": "DISTRIBUTOR1"
  },
  {
    "Plant Item": "CLEAN102",
    "Connect from": "ELEVATOR_SWICTH_2",
    "Connect to": "DISTRIBUTOR2"
  },
  {
    "Plant Item": "CLEAN103",
    "Connect from": "ELEVATOR_SWICTH_3",
    "Connect to": "SCREEN2"
  },
  {
    "Plant Item": "CLEAN104",
    "Connect from": "ELEVATOR_SWICTH_4",
    "Connect to": "DIVERTER3"
  },
  {
    "Plant Item": "PRESSURE106",
    "Connect from": "SOURCE_6",
    "Connect to": "CONVEYOR6"
  },
  {
    "Plant Item": "PRESSURE107",
    "Connect from": "SOURCE_7",
    "Connect to": "CONVEYOR7"
  },
  {
    "Plant Item": "PRESSURE108",
    "Connect from": "SOURCE_8",
    "Connect to": "DIVERTER8"
  },
  {
    "Plant Item": "CALIBRATE111",
    "Connect from": "FLOW6",
    "Connect to": "PVC"
  },
  {
    "Plant Item": "CALIBRATE111",
    "Connect from": "SOURCE_11",
    "Connect to": "PVC"
  },
  {
    "Plant Item": "CONVEYOR1",
    "Connect from": "SOURCE_1",
    "Connect to": "LINK1"
  },
  {
    "Plant Item": "CONVEYOR2",
    "Connect from": "LINK1",
    "Connect to": "WEIGHT2"
  },
  {
    "Plant Item": "WEIGHT2",
    "Connect from": "CONVEYOR2",
    "Connect to": "SEPARATOR2"
  },
  {
    "Plant Item": "PROCESSOR2",
    "Connect from": "DRIVE2",
    "Connect to": "SPLITTER1"
  },
  {
    "Plant Item": "CONVEYOR3",
    "Connect from": "LINK2",
    "Connect to": "WEIGHT3"
  },
  {
    "Plant Item": "WEIGHT3",
    "Connect from": "CONVEYOR3",
    "Connect to": "SEPARATOR3"
  },
  {
    "Plant Item": "PROCESSOR3",
    "Connect from": "SEPARATOR3",
    "Connect to": "DIVERTER7"
  },
  {
    "Plant Item": "CONVEYOR4",
    "Connect from": "DISTRIBUTOR2",
    "Connect to": "PRESS1"
  },
  {
    "Plant Item": "CONVEYOR4",
    "Connect from": "DISTRIBUTOR1",
    "Connect to": "PRESS1"
  },
  {
    "Plant Item": "CONVEYOR5",
    "Connect from": "DISTRIBUTOR1",
    "Connect to": "PRESS1"
  },
  {
    "Plant Item": "CONVEYOR5",
    "Connect from": "DISTRIBUTOR2",
    "Connect to": "PRESS1"
  },
  {
    "Plant Item": "CONVEYOR6",
    "Connect from": "PRESSURE106",
    "Connect to": "WEIGHT6"
  },
  {
    "Plant Item": "CONVEYOR6",
    "Connect from": "DIVERTER8",
    "Connect to": "WEIGHT6"
  },
  {
    "Plant Item": "WEIGHT6",
    "Connect from": "CONVEYOR6",
    "Connect to": "DUST6"
  },
  {
    "Plant Item": "DUST6",
    "Connect from": "WEIGHT6",
    "Connect to": "PROCESSOR6"
  },
  {
    "Plant Item": "PROCESSOR6",
    "Connect from": "DUST6",
    "Connect to": "DIVERTER1"
  },
  {
    "Plant Item": "CONVEYOR7",
    "Connect from": "PRESSURE107",
    "Connect to": "WEIGHT7"
  },
  {
    "Plant Item": "WEIGHT7",
    "Connect from": "CONVEYOR7",
    "Connect to": "DUST7"
  },
  {
    "Plant Item": "DUST7",
    "Connect from": "WEIGHT7",
    "Connect to": "PROCESSOR7"
  },
  {
    "Plant Item": "PROCESSOR7",
    "Connect from": "DUST7",
    "Connect to": "DIVERTER2"
  },
  {
    "Plant Item": "CONVEYOR8",
    "Connect from": "MAIN_WEIGHTER2",
    "Connect to": "WEIGHT8"
  },
  {
    "Plant Item": "WEIGHT8",
    "Connect from": "CONVEYOR8",
    "Connect to": "CONVEYOR9"
  },
  {
    "Plant Item": "CONVEYOR9",
    "Connect from": "WEIGHT8",
    "Connect to": "SEPARATOR1"
  },
  {
    "Plant Item": "CONVEYOR10",
    "Connect from": "DRIVE1",
    "Connect to": "WEIGHT10"
  },
  {
    "Plant Item": "WEIGHT10",
    "Connect from": "CONVEYOR10",
    "Connect to": "CONVEYOR11"
  },
  {
    "Plant Item": "CONVEYOR11",
    "Connect from": "WEIGHT10",
    "Connect to": "LINK6"
  },
  {
    "Plant Item": "CONVEYOR12",
    "Connect from": "LINK8",
    "Connect to": "WEIGHT12"
  },
  {
    "Plant Item": "WEIGHT12",
    "Connect from": "CONVEYOR12",
    "Connect to": "DEST_LOAD"
  },
  {
    "Plant Item": "CONVEYOR14",
    "Connect from": "DIVERTER8",
    "Connect to": "WEIGHT14"
  },
  {
    "Plant Item": "WEIGHT14",
    "Connect from": "CONVEYOR14",
    "Connect to": "LINK5"
  },
  {
    "Plant Item": "DEST1",
    "Connect from": "DISTRIBUTOR2",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST1",
    "Connect from": "DISTRIBUTOR1",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST6",
    "Connect from": "DISTRIBUTOR2",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST6",
    "Connect from": "DISTRIBUTOR1",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST11",
    "Connect from": "PVC",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST_CLEAN",
    "Connect from": "LINK6",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST4",
    "Connect from": "TRIPPER1",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST5",
    "Connect from": "TRIPPER2",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST14",
    "Connect from": "CHUTE1",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST_LOAD",
    "Connect from": "WEIGHT12",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST_WEIGH",
    "Connect from": "SCREEN1",
    "Connect to": ""
  },
  {
    "Plant Item": "DEST_WEIGH",
    "Connect from": "SCREEN2",
    "Connect to": ""
  },
  {
    "Plant Item": "LINK1",
    "Connect from": "CONVEYOR1",
    "Connect to": "CONVEYOR2"
  },
  {
    "Plant Item": "LINK2",
    "Connect from": "SOURCE_3",
    "Connect to": "CONVEYOR3"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "DIVERTER7",
    "Connect to": "ELEVATOR2"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "DIVERTER7",
    "Connect to": "ELEVATOR1"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "SPLITTER1",
    "Connect to": "SPLITTER1A"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "SPLITTER1",
    "Connect to": "SPLITTER1B"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "DIVERTER3",
    "Connect to": "ELEVATOR1"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "SPLITTER2",
    "Connect to": "SPLITTER2A"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "SPLITTER2",
    "Connect to": "SPLITTER2B"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "SPLITTER3",
    "Connect to": "SPLITTER3A"
  },
  {
    "Plant Item": "LINK3",
    "Connect from": "SPLITTER3",
    "Connect to": "SPLITTER3B"
  },
  {
    "Plant Item": "LINK4",
    "Connect from": "SPLITTER4",
    "Connect to": "SPLITTER4A"
  },
  {
    "Plant Item": "LINK4",
    "Connect from": "SPLITTER4",
    "Connect to": "SPLITTER4B"
  },
  {
    "Plant Item": "LINK4",
    "Connect from": "SPLITTER5",
    "Connect to": "SPLITTER5A"
  },
  {
    "Plant Item": "LINK4",
    "Connect from": "SPLITTER5",
    "Connect to": "SPLITTER3B"
  },
  {
    "Plant Item": "LINK5",
    "Connect from": "WEIGHT14",
    "Connect to": "CHUTE1"
  },
  {
    "Plant Item": "LINK6",
    "Connect from": "CONVEYOR11",
    "Connect to": "LOAD1"
  },
  {
    "Plant Item": "LINK6",
    "Connect from": "CONVEYOR11",
    "Connect to": "DEST_CLEAN"
  },
  {
    "Plant Item": "LINK7",
    "Connect from": "LOAD1",
    "Connect to": "LINK8"
  },
  {
    "Plant Item": "LINK8",
    "Connect from": "LINK7",
    "Connect to": "CONVEYOR12"
  },
  {
    "Plant Item": "DIVERTER1",
    "Connect from": "PROCESSOR6",
    "Connect to": "SPLITTER4"
  },
  {
    "Plant Item": "DIVERTER1",
    "Connect from": "PROCESSOR6",
    "Connect to": "SPLITTER2"
  },
  {
    "Plant Item": "DIVERTER2",
    "Connect from": "PROCESSOR7",
    "Connect to": "SPLITTER3"
  },
  {
    "Plant Item": "DIVERTER2",
    "Connect from": "PROCESSOR7",
    "Connect to": "SPLITTER5"
  },
  {
    "Plant Item": "DIVERTER3",
    "Connect from": "CLEAN104",
    "Connect to": "LINK3"
  },
  {
    "Plant Item": "DIVERTER3",
    "Connect from": "CLEAN104",
    "Connect to": "SCREEN1"
  },
  {
    "Plant Item": "DIVERTER6",
    "Connect from": "FLOW5",
    "Connect to": "MAIN_WEIGHTER2"
  },
  {
    "Plant Item": "DIVERTER7",
    "Connect from": "PROCESSOR3",
    "Connect to": "LINK3"
  },
  {
    "Plant Item": "DIVERTER8",
    "Connect from": "PRESSURE108",
    "Connect to": "CONVEYOR14"
  },
  {
    "Plant Item": "DIVERTER8",
    "Connect from": "PRESSURE108",
    "Connect to": "CONVEYOR6"
  },
  {
    "Plant Item": "ELEVATOR_PATH_1",
    "Connect from": "ELEVATOR1",
    "Connect to": "ELEVATOR_SWICTH_1"
  },
  {
    "Plant Item": "ELEVATOR_PATH_2",
    "Connect from": "ELEVATOR2",
    "Connect to": "ELEVATOR_SWICTH_2"
  },
  {
    "Plant Item": "ELEVATOR_PATH_3",
    "Connect from": "ELEVATOR3",
    "Connect to": "ELEVATOR_SWICTH_3"
  },
  {
    "Plant Item": "ELEVATOR_PATH_4",
    "Connect from": "ELEVATOR4",
    "Connect to": "ELEVATOR_SWICTH_4"
  },
  {
    "Plant Item": "ELEVATOR1",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR_PATH_1"
  },
  {
    "Plant Item": "ELEVATOR1",
    "Connect from": "SPLITTER1B",
    "Connect to": "ELEVATOR_PATH_1"
  },
  {
    "Plant Item": "ELEVATOR1",
    "Connect from": "SPLITTER2A",
    "Connect to": "ELEVATOR_PATH_1"
  },
  {
    "Plant Item": "ELEVATOR1",
    "Connect from": "SPLITTER3A",
    "Connect to": "ELEVATOR_PATH_1"
  },
  {
    "Plant Item": "ELEVATOR_SWICTH_1",
    "Connect from": "ELEVATOR_PATH_1",
    "Connect to": "CLEAN101"
  },
  {
    "Plant Item": "ELEVATOR2",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR_PATH_2"
  },
  {
    "Plant Item": "ELEVATOR2",
    "Connect from": "SPLITTER1A",
    "Connect to": "ELEVATOR_PATH_2"
  },
  {
    "Plant Item": "ELEVATOR2",
    "Connect from": "SPLITTER2B",
    "Connect to": "ELEVATOR_PATH_2"
  },
  {
    "Plant Item": "ELEVATOR2",
    "Connect from": "SPLITTER3B",
    "Connect to": "ELEVATOR_PATH_2"
  },
  {
    "Plant Item": "ELEVATOR_SWICTH_2",
    "Connect from": "ELEVATOR_PATH_2",
    "Connect to": "CLEAN102"
  },
  {
    "Plant Item": "ELEVATOR3",
    "Connect from": "SPLITTER4A",
    "Connect to": "ELEVATOR_PATH_3"
  },
  {
    "Plant Item": "ELEVATOR3",
    "Connect from": "SPLITTER5A",
    "Connect to": "ELEVATOR_PATH_3"
  },
  {
    "Plant Item": "ELEVATOR_SWICTH_3",
    "Connect from": "ELEVATOR_PATH_3",
    "Connect to": "CLEAN103"
  },
  {
    "Plant Item": "ELEVATOR4",
    "Connect from": "FLOW7",
    "Connect to": "ELEVATOR_PATH_4"
  },
  {
    "Plant Item": "ELEVATOR4",
    "Connect from": "SPLITTER4B",
    "Connect to": "ELEVATOR_PATH_4"
  },
  {
    "Plant Item": "ELEVATOR4",
    "Connect from": "SPLITTER3B",
    "Connect to": "ELEVATOR_PATH_4"
  },
  {
    "Plant Item": "ELEVATOR_SWICTH_4",
    "Connect from": "ELEVATOR_PATH_4",
    "Connect to": "CLEAN104"
  },
  {
    "Plant Item": "FLOW5",
    "Connect from": "MAIN_WEIGHTER1",
    "Connect to": "DIVERTER6"
  },
  {
    "Plant Item": "FLOW6",
    "Connect from": "MAIN_WEIGHTER2",
    "Connect to": "CALIBRATE111"
  },
  {
    "Plant Item": "FLOW7",
    "Connect from": "PVC",
    "Connect to": "ELEVATOR4"
  },
  {
    "Plant Item": "PRESS1",
    "Connect from": "CONVEYOR5",
    "Connect to": "TRIPPER2"
  },
  {
    "Plant Item": "PRESS1",
    "Connect from": "CONVEYOR4",
    "Connect to": "TRIPPER1"
  },
  {
    "Plant Item": "CHUTE1",
    "Connect from": "LINK5",
    "Connect to": "DEST14"
  },
  {
    "Plant Item": "SEPARATOR1",
    "Connect from": "CONVEYOR9",
    "Connect to": "DRIVE1"
  },
  {
    "Plant Item": "SEPARATOR2",
    "Connect from": "WEIGHT2",
    "Connect to": "DRIVE2"
  },
  {
    "Plant Item": "SEPARATOR3",
    "Connect from": "WEIGHT3",
    "Connect to": "DRIVE3"
  },
  {
    "Plant Item": "DRIVE1",
    "Connect from": "SEPARATOR1",
    "Connect to": "CONVEYOR10"
  },
  {
    "Plant Item": "DRIVE2",
    "Connect from": "SEPARATOR2",
    "Connect to": "PROCESSOR2"
  },
  {
    "Plant Item": "DRIVE3",
    "Connect from": "SEPARATOR3",
    "Connect to": "PROCESSOR3"
  },
  {
    "Plant Item": "PVC",
    "Connect from": "CALIBRATE111",
    "Connect to": "DEST11"
  },
  {
    "Plant Item": "PVC",
    "Connect from": "CALIBRATE111",
    "Connect to": "FLOW7"
  },
  {
    "Plant Item": "DISTRIBUTOR1",
    "Connect from": "CLEAN101",
    "Connect to": "DEST6"
  },
  {
    "Plant Item": "DISTRIBUTOR1",
    "Connect from": "CLEAN101",
    "Connect to": "CONVEYOR5"
  },
  {
    "Plant Item": "DISTRIBUTOR1",
    "Connect from": "CLEAN101",
    "Connect to": "DEST1"
  },
  {
    "Plant Item": "DISTRIBUTOR1",
    "Connect from": "CLEAN101",
    "Connect to": "CONVEYOR4"
  },
  {
    "Plant Item": "DISTRIBUTOR2",
    "Connect from": "CLEAN102",
    "Connect to": "DEST6"
  },
  {
    "Plant Item": "DISTRIBUTOR2",
    "Connect from": "CLEAN102",
    "Connect to": "CONVEYOR5"
  },
  {
    "Plant Item": "DISTRIBUTOR2",
    "Connect from": "CLEAN102",
    "Connect to": "DEST1"
  },
  {
    "Plant Item": "DISTRIBUTOR2",
    "Connect from": "CLEAN102",
    "Connect to": "CONVEYOR4"
  },
  {
    "Plant Item": "SCREEN1",
    "Connect from": "DIVERTER3",
    "Connect to": "DEST_WEIGH"
  },
  {
    "Plant Item": "SCREEN1",
    "Connect from": "DIVERTER3",
    "Connect to": "MAIN_WEIGHTER1"
  },
  {
    "Plant Item": "SCREEN2",
    "Connect from": "CLEAN103",
    "Connect to": "MAIN_WEIGHTER1"
  },
  {
    "Plant Item": "SCREEN2",
    "Connect from": "CLEAN103",
    "Connect to": "DEST_WEIGH"
  },
  {
    "Plant Item": "LOAD1",
    "Connect from": "LINK6",
    "Connect to": "LINK7"
  },
  {
    "Plant Item": "SOURCE_11",
    "Connect from": "",
    "Connect to": "CALIBRATE111"
  },
  {
    "Plant Item": "SOURCE_1",
    "Connect from": "",
    "Connect to": "CONVEYOR1"
  },
  {
    "Plant Item": "SOURCE_3",
    "Connect from": "",
    "Connect to": "LINK2"
  },
  {
    "Plant Item": "SOURCE_6",
    "Connect from": "",
    "Connect to": "PRESSURE106"
  },
  {
    "Plant Item": "SOURCE_7",
    "Connect from": "",
    "Connect to": "PRESSURE107"
  },
  {
    "Plant Item": "SOURCE_8",
    "Connect from": "",
    "Connect to": "PRESSURE108"
  },
  {
    "Plant Item": "SOURCE_WEIGH",
    "Connect from": "",
    "Connect to": "MAIN_WEIGHTER1"
  },
  {
    "Plant Item": "SPLITTER1",
    "Connect from": "PROCESSOR2",
    "Connect to": "LINK3"
  },
  {
    "Plant Item": "SPLITTER1A",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR2"
  },
  {
    "Plant Item": "SPLITTER1B",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR1"
  },
  {
    "Plant Item": "SPLITTER2",
    "Connect from": "DIVERTER1",
    "Connect to": "LINK3"
  },
  {
    "Plant Item": "SPLITTER2A",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR1"
  },
  {
    "Plant Item": "SPLITTER2B",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR2"
  },
  {
    "Plant Item": "SPLITTER3",
    "Connect from": "DIVERTER2",
    "Connect to": "LINK3"
  },
  {
    "Plant Item": "SPLITTER3A",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR1"
  },
  {
    "Plant Item": "SPLITTER3B",
    "Connect from": "LINK3",
    "Connect to": "ELEVATOR2"
  },
  {
    "Plant Item": "SPLITTER3B",
    "Connect from": "LINK4",
    "Connect to": "ELEVATOR4"
  },
  {
    "Plant Item": "SPLITTER4",
    "Connect from": "DIVERTER1",
    "Connect to": "LINK4"
  },
  {
    "Plant Item": "SPLITTER4A",
    "Connect from": "LINK4",
    "Connect to": "ELEVATOR3"
  },
  {
    "Plant Item": "SPLITTER4B",
    "Connect from": "LINK4",
    "Connect to": "ELEVATOR4"
  },
  {
    "Plant Item": "SPLITTER5",
    "Connect from": "DIVERTER2",
    "Connect to": "LINK4"
  },
  {
    "Plant Item": "SPLITTER5A",
    "Connect from": "LINK4",
    "Connect to": "ELEVATOR3"
  },
  {
    "Plant Item": "TRIPPER1",
    "Connect from": "PRESS1",
    "Connect to": "DEST4"
  },
  {
    "Plant Item": "TRIPPER2",
    "Connect from": "PRESS1",
    "Connect to": "DEST5"
  },
  {
    "Plant Item": "MAIN_WEIGHTER1",
    "Connect from": "SCREEN2",
    "Connect to": "FLOW5"
  },
  {
    "Plant Item": "MAIN_WEIGHTER1",
    "Connect from": "SCREEN1",
    "Connect to": "FLOW5"
  },
  {
    "Plant Item": "MAIN_WEIGHTER1",
    "Connect from": "SOURCE_WEIGH",
    "Connect to": "FLOW5"
  },
  {
    "Plant Item": "MAIN_WEIGHTER2",
    "Connect from": "DIVERTER6",
    "Connect to": "FLOW6"
  },
  {
    "Plant Item": "MAIN_WEIGHTER2",
    "Connect from": "DIVERTER6",
    "Connect to": "CONVEYOR8"
  }
]



# Add edges based on the data
for item in data:
    if item["Connect from"]:
        G.add_edge(item["Connect from"], item["Plant Item"])
    if item["Connect to"]:
        G.add_edge(item["Plant Item"], item["Connect to"])

# Now, instead of using matplotlib, we'll use pyvis for visualization
nt = Network(notebook=True)
nt.from_nx(G)


# Adjusting edge settings to make arrows more prominent
for edge in nt.edges:
    edge['arrows'] = 'to'
    edge['arrowStrikethrough'] = True

# Adjusting node settings for label inside the node
for node in nt.nodes:
    node['font'] = {'color': 'black', 'size': 15}
    node['shapeProperties'] = {'useBorderWithImage': True}
    node['value'] = 60 

    # Check label and set color
    if 'source' in node['label'].lower():
        node['color'] = 'green'
    elif 'dest' in node['label'].lower():
        node['color'] = 'red'

nt.show("network_with_arrows.html")

#nt.show("network.html")
