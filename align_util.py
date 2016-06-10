import idmapper


def create_node_id_to_gene_map(G):
    ids = G._get_candidate_ids()
    genes = idmapper.get_gene_id_mapping(ids)
    input_to_gene_map = make_input_to_gene_map(genes)
    return make_node_id_to_gene_map(G, input_to_gene_map)


def make_input_to_gene_map(response):
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


def make_node_id_to_gene_map(G, input_to_gene_map):
    node_id_to_gene_map = {}

    for n, attr in G.nodes_iter(data=True):
        if 'represents' in attr:
            represents = attr['represents']
            if isinstance(represents, basestring):
                represents = represents.split(':')[-1]
                if represents in input_to_gene_map:
                    gene_symbol = input_to_gene_map[represents]
                    if gene_symbol:
                        node_id_to_gene_map[n] = gene_symbol
                        continue
        if 'alias' in attr:
            aliases = attr['alias']
            if type(aliases) is list:
                for alias in aliases:
                    if isinstance(alias, basestring):
                        alias = alias.split(':')[-1]
                        if alias in input_to_gene_map:
                            gene_symbol = input_to_gene_map[alias]
                            if gene_symbol:
                                node_id_to_gene_map[n] = gene_symbol
                                continue
        if 'name' in attr:
            name = attr['name']
            if isinstance(name, basestring):
                name = name.split(':')[-1]
                if name in input_to_gene_map:
                    gene_symbol = input_to_gene_map[name]
                    if gene_symbol:
                        node_id_to_gene_map[n] = gene_symbol

    return node_id_to_gene_map
