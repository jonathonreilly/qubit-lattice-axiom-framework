from pathlib import Path
import hashlib
import json
import subprocess
import sys

N=Path(__file__).resolve().parents[1]
W=N.parent/'correlation_worktree'
O=N/'two_body_integration'
path=W/'docs/audit/data/citation_graph_manifest.json'
before=path.read_bytes()
(O/'BASE_GRAPH_MANIFEST.json').write_bytes(before)
old=json.loads(before)
for label,script in [('graph_build','docs/audit/scripts/run_citation_graph_build.py'),('graph_manifest','docs/audit/scripts/write_citation_graph_manifest.py')]:
    proc=subprocess.run([sys.executable,script],cwd=W,capture_output=True)
    (O/(label+'.stdout')).write_bytes(proc.stdout)
    (O/(label+'.stderr')).write_bytes(proc.stderr)
    if proc.returncode:
        print(proc.stdout.decode());print(proc.stderr.decode());raise SystemExit(proc.returncode)
new=json.loads(path.read_text())
added=sorted(set(new['nodes'])-set(old['nodes']))
removed=sorted(set(old['nodes'])-set(new['nodes']))
rewired=[k for k in old['nodes'] if k in new['nodes'] and old['nodes'][k]!=new['nodes'][k]]
expected='two_body_autonomous_halt_bounded_theorem_note_2026-10-17'
assert added==[expected],added
assert not removed and not rewired,(removed,rewired)
graph=json.loads((W/'docs/audit/data/citation_graph.json').read_text())
nodes=graph['nodes']
node=nodes[expected] if isinstance(nodes,dict) else next(x for x in nodes if x.get('id')==expected or x.get('claim_id')==expected)
edges=[e for e in graph['edges'] if expected in str(e)]
record={'old_counts':{k:old[k] for k in ('node_count','edge_count')},'new_counts':{k:new[k] for k in ('node_count','edge_count')},'added':added,'removed':removed,'rewired':rewired,'new_node':node,'new_edges':edges,'manifest_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Only the intended new note and its citation links; prior-result context is not a new mathematical import. Old topology preserved. Generated graph JSON is validation residue and will not be committed.'}
(O/'GRAPH_VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
