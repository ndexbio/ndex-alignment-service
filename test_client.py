from networkn import NdexGraph
import idmapper
import align_util as util

noi = NdexGraph(server='http://public.ndexbio.org', uuid='4a5bc352-9243-11e5-b435-06603eb7f303')
rn = NdexGraph(server='http://public.ndexbio.org', uuid='19f2fc35-1235-11e6-a039-06603eb7f303')

noi_node_id_to_gene_map = util.create_node_id_to_gene_map(noi)
rn_node_id_to_gene_map = util.create_node_id_to_gene_map(rn)

noi.show_stats()
rn.show_stats()

for node_id, merge_id in noi_node_id_to_gene_map.iteritems():
    noi.set_node_attribute(node_id, 'expand_id', merge_id)

for node_id, merge_id in rn_node_id_to_gene_map.iteritems():
    rn.set_node_attribute(node_id, 'expand_id', merge_id)

noi.expand(rn, attribute='expand_id')
noi.show_stats()

noi.set_name("Ravasi expanded with bindingdb all compounds mouse")

noi.write_to("ravasi.cx")

noi.upload_to("http://dev2.ndexbio.org", username="rudipillich", password="rudipillich")


