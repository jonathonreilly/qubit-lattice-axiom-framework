#!/usr/bin/env python3
"""Post-seal selective comparison. Executes only extracted pure author functions.
Never imports the author module (whose top level creates an output directory).
"""
from pathlib import Path
from collections import deque,Counter
import ast,hashlib,importlib.util,itertools,json,sys
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;R=O.parent
if (O/'COMPARISON_RESULTS.json').exists():raise SystemExit('comparison evidence already preserved')
spec=importlib.util.spec_from_file_location('independent_geometry',O/'independent_check.py')
i=importlib.util.module_from_spec(spec);spec.loader.exec_module(i)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pre=json.loads((O/'PRE_COMPARISON_SEAL.json').read_text())
for row in pre['sources']+pre['artifacts']+pre['prior_sealed_evidence_reused']+pre['procedures_reused']:
    assert sha(Path(row['path']))==row['sha256'],row['path']
p=R/'geometric_general_graph_check.py';assert sha(p)==pre['author_runner_unread_identity']['sha256']
author=json.loads((R/'geometric_general_graph_checks/RESULTS.json').read_text())
for name,digest in author['sources_sha256'].items():assert sha(R/name)==digest,name
log=(R/'GEOMETRIC_GENERAL_GRAPH_RUN.log').read_text();lines=log.splitlines()
logged=[json.loads(s) for s in lines if s.startswith('{"name"')]
assert logged==author['rows']
assert not (R/'GEOMETRIC_GENERAL_GRAPH_RUN.stderr').read_bytes()
own=json.loads((O/'RESULTS.json').read_text())
for a,b in zip(author['rows'][0]['rows'],own['exhaustive_labeled_small_graphs']['rows']):
    assert a['vertices']==b['n'] and a['graphs']==b['connected_graphs_with_perfect_matching'] and a['near_states']==b['near_states_checked']

# Alternative incidence count: fix a representative directed slide and its near matching,
# then enumerate graph completions of its required edges, rather than graph/state pairs.
template_counts=[]
for n,required,mult in [(4,{(0,1),(1,2)},24),(6,{(0,1),(1,2),(3,4)},360)]:
    remaining=[e for e in itertools.combinations(range(n),2) if e not in required];allowed=0
    for mask in range(1<<len(remaining)):
        edges=required|{e for j,e in enumerate(remaining) if mask>>j&1}
        if i.connected(n,edges) and i.matchings(n,edges,n//2):allowed+=1
    total=allowed*mult;expected=next(x['directed_slide_channels'] for x in author['rows'][0]['rows'] if x['vertices']==n)
    assert total==expected
    template_counts.append({'n':n,'graph_completions_per_slide_template':allowed,'slide_templates':mult,'total_directed_channels':total})

# Freeze the exact source function AST; supply independent edge/partner helpers.
names={'simple_graph','move','complete_virtually','relocate','connect','near_components'}
tree=ast.parse(p.read_text());body=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in names]
assert {x.name for x in body}==names
namespace={'deque':deque,'edge':i.edge,'partners':lambda m:{u:v for a,b in m for u,v in [(a,b),(b,a)]}}
exec(compile(ast.Module(body=body,type_ignores=[]),str(p)+' [pure selected functions]','exec'),namespace)
replays=[]
for name,data in own['named_graph_definitions'].items():
    n=data['n'];es={tuple(e) for e in data['edges']};full=i.matchings(n,es,n//2);near=i.matchings(n,es,n//2-1)
    G=namespace['simple_graph'](n,es)
    pairs=[(near[0],near[-1]),(near[len(near)//2],near[0]),(near[-1],near[len(near)//2])]
    for start,target in pairs:
        ops,cycles=namespace['connect'](frozenset(start),frozenset(target),frozenset(full[0]),G)
        tracked=i.Tracked(n,i.neighbors(n,es),start)
        for a,b,c in ops:tracked.slide((c,b,a))
        assert tracked.m==target
        for a,b,c in reversed(ops):tracked.slide((a,b,c))
        assert tracked.m==start
        assert len(ops)<=(n//2)**2+4*(n//2)
        replays.append({'graph':name,'steps':len(ops),'cycles':cycles,'independent_marked_forward_and_reverse_replay':True})
# Reconstruct the author's disconnected two-square diagnostic independently.
es={i.edge(off+j,off+(j+1)%4) for off in [0,4] for j in range(4)}
near=i.matchings(8,es,3);full=i.matchings(8,es,4);graph=i.slide_graph(8,es,near)
assert i.components(graph)==author['rows'][3]['component_sizes'] and len(full)==4
unseen=set(range(len(near)));exit_counts=[]
while unseen:
    comp=set(i.distances(graph,min(unseen)));unseen-=comp;exits=set()
    for q in comp:
        M=near[q];holes=[u for u,v in enumerate(i.partner(8,M)) if v<0]
        if i.edge(*holes) in es:exits.add(i.canonical((*M,i.edge(*holes))))
    exit_counts.append(len(exits))
assert exit_counts==author['rows'][3]['reachable_full_counts']
# Verify bounds/schema of all author random/periodic controls without claiming to replay them.
assert len(author['rows'][1]['rows'])==80==author['rows'][1]['cases']
assert len(author['rows'][2]['rows'])==8
for x in author['rows'][1]['rows']:
    k=x['vertices']//2;assert 0<=x['events']<=k*k+4*k and 0<=x['cycle_changes']<=k//2
for x in author['rows'][2]['rows']:
    k=x['N']**3//2;assert 0<=x['events']<=k*k+4*k and 0<=x['cycles']<=k//2
result={'scope':'Post-preseal source and selective control comparison, not a full author-suite rerun.',
        'precomparison_artifacts_unchanged':len(pre['artifacts']),'author_source_identities_authenticated':author['sources_sha256'],
        'author_log_rows_equal_result_rows':True,'author_stderr_empty':True,'exhaustive_graph_and_state_counts_independently_equal':True,
        'alternative_directed_channel_counts':template_counts,'selected_author_function_paths_independently_replayed':replays,
        'disconnected_two_square_exit_counts':exit_counts,'all_author_random_and_periodic_summary_rows_read_and_bounds_checked':True,
        'author_random_and_large_periodic_runs_not_reexecuted':True,'unresolved_findings':[]}
(O/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
