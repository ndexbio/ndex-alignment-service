from networkn import NdexGraph
import align_util as util

def align_test_helper(noi, rn, output_name):
    noi_node_id_to_gene_map = util.create_node_id_to_gene_map(noi)
    rn_node_id_to_gene_map = util.create_node_id_to_gene_map(rn)

    noi.show_stats()
    rn.show_stats()

    for node_id, merge_id in noi_node_id_to_gene_map.iteritems():
        noi.set_node_attribute(node_id, 'expand_id', merge_id)

    for node_id, merge_id in rn_node_id_to_gene_map.iteritems():
        rn.set_node_attribute(node_id, 'expand_id', merge_id)

    noi.expand(rn, attribute_key='expand_id')
    noi.show_stats()

    noi.set_name(output_name)

    noi.write_to(output_name + ".cx")

    noi.upload_to("http://test.ndexbio.org", username="alignment", password="alignment")


def test1():
    noi = NdexGraph(server='http://test.ndexbio.org', username='alignment', password='alignment', uuid='10fbdf00-2ebc-11e6-a3d4-028f28cd6a5b')
    rn = NdexGraph(server='http://public.ndexbio.org', uuid='fa3b2d50-1229-11e6-a039-06603eb7f303')
    align_test_helper(noi, rn, 'EGFR_output')

def test2():
    noi = NdexGraph(server='http://test.ndexbio.org', username='alignment', password='alignment', uuid='f37b5c59-2ecd-11e6-a3d4-028f28cd6a5b')
    rn = NdexGraph(server='http://public.ndexbio.org', uuid='fa3b2d50-1229-11e6-a039-06603eb7f303')
    align_test_helper(noi, rn, 'Two EGFR_output')

test2()