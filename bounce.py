import ndex.client as nc
from networkn import NdexGraph
import thread
import copy

def update_network(thread_name, G, network_id):
    ndex_dev = nc.Ndex("http://dev.ndexbio.org", username="drh", password="drh")
    # ndex_dev.set_debug_mode(True)
    G = copy.deepcopy(G)
    G.set_name('RAS: ' + network_id)
    for i in range(1000):
        # print i, thread_name, network_id
        ndex_dev.update_cx_network(G.to_CX_stream(), network_id)
        # print 'done with', i, thread_name, network_id

def get_edges(thread_name, G, network_id):
    ndex_dev = nc.Ndex("http://dev.ndexbio.org", username="drh", password="drh")
    # ndex_dev.set_debug_mode(True)
    route = "/network/%s/edge/asNetwork/0/500" % (network_id)
    for i in range(50000):
        ndex_dev.get(route)

ndex = nc.Ndex("http://public.ndexbio.org", username="test", password="test")
# ndex_dev = nc.Ndex("http://dev.ndexbio.org", username="drh", password="drh")
#
noi_id = '50e3dff7-133e-11e6-a039-06603eb7f303'

noi_cx = ndex.get_network_as_cx_stream(noi_id).json()
noi = NdexGraph(noi_cx)

print 'start'
try:
    thread.start_new_thread(update_network, ('thread-1', noi, '4499f87f-278a-11e6-8cb7-06832d634f41'))
    thread.start_new_thread(update_network, ('thread-2', noi, '4aacfe71-278a-11e6-8cb7-06832d634f41'))
    thread.start_new_thread(update_network, ('thread-3', noi, '51553f82-278a-11e6-8cb7-06832d634f41'))

    thread.start_new_thread(get_edges, ('thread-4', noi, '4499f87f-278a-11e6-8cb7-06832d634f41'))
    thread.start_new_thread(get_edges, ('thread-5', noi, '4aacfe71-278a-11e6-8cb7-06832d634f41'))
    thread.start_new_thread(get_edges, ('thread-6', noi, '51553f82-278a-11e6-8cb7-06832d634f41'))
except:
    print 'Error: Unable to launch threads'

print 'Done launching threads.'

while 1:
   pass



#
# for i in range(1000):
#     print i
#     ndex_dev.update_cx_network(noi.to_CX_stream(), noi_id)


# noi.set_name("1. RAS machine")
# ndex_dev.save_cx_stream_as_new_network(noi.to_CX_stream())
#
# noi.set_name("2. RAS machine")
# ndex_dev.save_cx_stream_as_new_network(noi.to_CX_stream())
#
# noi.set_name("3. RAS machine")
# ndex_dev.save_cx_stream_as_new_network(noi.to_CX_stream())





