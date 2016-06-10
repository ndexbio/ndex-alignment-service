import json
import ndex.client as nc
import idmapper
import networkx as nx
import align_util as util

from networkn import NdexGraph

def make_label_map(response):
    label_map = {}
    for match in response.get('matched'):
        species = match.get('species')
        if species and species == 'human':
            id = match.get('in')
            matches = match.get('matches')
            if id and matches:
                sym = matches.get("Symbol")
                if sym:
                    label_map[id] = sym
    return label_map

def node_to_gene_map(network, label_map):
    node_to_gene_map = {}

    G = network

    for node_id, node_identifier in nx.get_node_attributes(G, 'name').iteritems():
        # print("  id = " + node_identifier)
        gene_symbol = label_map.get(node_identifier)

        if gene_symbol:
            #print("  sym = " + gene_symbol)
            node_to_gene_map[node_id] = gene_symbol

    return node_to_gene_map

def gene_to_node_map(network, label_map):
    gene_to_node_map = {}

    G = network
    for node_id, node_identifier in nx.get_node_attributes(G, 'name').iteritems():
            gene_symbol = label_map.get(node_identifier)
            if gene_symbol:
                gene_to_node_map[gene_symbol] = node_id
    return gene_to_node_map


def expand(primaryCX, secondaryCX):
    primary = NdexGraph(primaryCX)
    secondary = NdexGraph(secondaryCX)

    primary_node_id_to_gene_map = util.create_node_id_to_gene_map(primary)
    secondary_node_id_to_gene_map = util.create_node_id_to_gene_map(secondary)

    primary.show_stats()
    secondary.show_stats()

    for node_id, merge_id in primary_node_id_to_gene_map.iteritems():
        primary.set_node_attribute(node_id, 'expand_id', merge_id)

    for node_id, merge_id in secondary_node_id_to_gene_map.iteritems():
        secondary.set_node_attribute(node_id, 'expand_id', merge_id)

    primary.expand(secondary, attribute_key='expand_id')
    primary.show_stats()

    return primary.to_cx()

if __name__ == "__main__":
    pass

