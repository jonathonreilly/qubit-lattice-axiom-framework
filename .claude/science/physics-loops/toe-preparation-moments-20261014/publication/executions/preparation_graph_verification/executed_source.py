import json,shutil
from common import N,W,pin,read_json,write_json,run,now
D=N/'publication_integration/preparation';c=read_json(N/'preparation_moment_publication_components/INPUTS.json')
g=read_json(W/'docs/audit/data/citation_graph.json');old=read_json(D/'base_graph.json');claim=c['claim_id'];parent=c['parent']['claim_id']
assert set(g['nodes'])==set(old['nodes'])|{claim}
assert all(g['nodes'][k]==v for k,v in old['nodes'].items())
assert g['nodes'][claim]['deps']==[parent] and g['nodes'][claim]['path']==c['note'] and g['nodes'][claim]['runner_path']==c['helper']
key=lambda x:json.dumps(x,sort_keys=True)
assert sorted(map(key,g['edges']))==sorted(list(map(key,old['edges']))+[key({'from':claim,'to':parent})])
assert g['roots']==old['roots']
run(D,'write_graph_manifest',['python3','docs/audit/scripts/write_citation_graph_manifest.py'])
m=read_json(W/'docs/audit/data/citation_graph_manifest.json');prior=read_json(D/'base_graph_manifest.json')
assert all(m['nodes'][k]==v for k,v in prior['nodes'].items())
assert m['node_count']==len(g['nodes']) and m['edge_count']==len(g['edges'])
shutil.copyfile(W/'docs/audit/data/citation_graph.json',D/'after_graph.json')
shutil.copyfile(W/'docs/audit/data/citation_graph_manifest.json',D/'after_graph_manifest.json')
r={'utc':now().isoformat(),'complete_old_nodes_preserved':len(old['nodes']),'complete_old_edges_preserved':len(old['edges']),'roots_unchanged':True,'new_node':g['nodes'][claim],'new_edge':{'from':claim,'to':parent},'graph':pin(D/'after_graph.json'),'manifest':pin(D/'after_graph_manifest.json'),'scope':'Full graph object equality plus exact one-node/one-edge addition; no audit status change.'}
write_json(D/'GRAPH_VERIFICATION.json',r);print(r)
