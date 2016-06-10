from networkn import NdexGraph

def create_two_egfr():
    G = NdexGraph()

    n1 = G.add_named_node('EGFR')
    n2 = G.add_named_node('X1')
    n3 = G.add_named_node('X2')

    G.add_edge_between(n1,n2)
    G.add_edge_between(n1,n3)

    n4 = G.add_named_node('EGFR')
    n5 = G.add_named_node('Y1')
    n6 = G.add_named_node('Y2')

    G.add_edge_between(n4, n5)
    G.add_edge_between(n4, n6)

    G.add_edge_between(n2, n5)

    G.set_name('Two Symbol: EGFR')

    G.upload_to('http://test.ndexbio.org', 'alignment', 'alignment')

def create_egfr():
    G = NdexGraph()

    n1 = G.add_named_node('EGFR')
    n2 = G.add_named_node('X1')
    n3 = G.add_named_node('X2')

    G.add_edge_between(n1,n2)
    G.add_edge_between(n1,n3)

    G.set_name('Symbol: EGFR')

    G.upload_to('http://test.ndexbio.org', 'alignment', 'alignment')

create_two_egfr()