import json

from ndex_datamodels import NetworkN

def expand(cx1, cx2):
    network1 = NetworkN(cx1)
    network2 = NetworkN(cx2)
    network1.expand(network2)
    return network1.to_CX()

if __name__ == "__main__":
    print 'alignment'
    network1 = NetworkN()
    network1.add_node('B')
    network1.add_node('X')
    network1.add_node('Q')
    network1.add_node('C')
    network1.add_edge('B', 'X')
    network1.add_edge('X', 'Q')
    network1.add_edge('Q', 'C')

    network2 = NetworkN()
    network2.add_node('A')
    network2.add_node('B')
    network2.add_node('C')
    network2.add_node('E')
    network2.add_node('F')
    network2.add_node('G')
    network2.add_node('H')
    network2.add_edge('A', 'B')
    network2.add_edge('B', 'C')
    network2.add_edge('A', 'C')
    network2.add_edge('B', 'E')
    network2.add_edge('E', 'F')
    network2.add_edge('E', 'H')
    network2.add_edge('F', 'G')

    print json.dumps( network1.to_CX())
    print json.dumps( network2.to_CX())

    cx = expand(network1.to_CX(), network2.to_CX())
