"""Serialized governed graph build, then manifest; inspect only intended delta."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

D=Path(__file__).resolve().parent
W=D.parents[1]/'correlation_worktree'
p=W/'docs/audit/data/citation_graph_manifest.json'
before=(D/'BASE_GRAPH_MANIFEST.json').read_bytes()
assert p.read_bytes()==before,'Timeout must not have changed the original topology manifest.'
old=json.loads(before); runs=[]
for label,script,cap in [('graph_build','docs/audit/scripts/run_citation_graph_build.py',180),('graph_manifest','docs/audit/scripts/write_citation_graph_manifest.py',60)]:
    started=datetime.datetime.now(datetime.timezone.utc).isoformat(); clock=time.monotonic()
    try:
        proc=subprocess.run([sys.executable,script],cwd=W,capture_output=True,timeout=cap)
        stdout,stderr,code=proc.stdout,proc.stderr,proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout,stderr,code=exc.stdout or b'',exc.stderr or b'',None
    (D/(label+'.stdout')).write_bytes(stdout); (D/(label+'.stderr')).write_bytes(stderr)
    runs.append({'script':script,'started_utc':started,'elapsed_seconds':time.monotonic()-clock,'wall_cap_seconds':cap,'exit_code':code,'script_sha256':hashlib.sha256((W/script).read_bytes()).hexdigest()})
    (D/'GRAPH_EXECUTIONS.json').write_text(json.dumps(runs,indent=2)+'\n')
    assert code==0,(label,code)
new=json.loads(p.read_text())
added=sorted(set(new['nodes'])-set(old['nodes']))
removed=sorted(set(old['nodes'])-set(new['nodes']))
rewired=[k for k in old['nodes'] if k in new['nodes'] and old['nodes'][k]!=new['nodes'][k]]
expected='structural_coefficient_box_bounded_theorem_note_2026-10-17'
graph=json.loads((W/'docs/audit/data/citation_graph.json').read_text())
node=graph['nodes'][expected]
edges=[e for e in graph['edges'] if e.get('from')==expected or e.get('to')==expected]
record={'old_counts':{k:old[k] for k in ('node_count','edge_count')},'new_counts':{k:new[k] for k in ('node_count','edge_count')},
        'added':added,'removed':removed,'rewired':rewired,'new_node':node,'new_edges':edges,
        'manifest_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'executions':runs,
        'scope':'New structural note and its explicit citation only. Generated citation_graph.json is validation residue, not publication source.'}
(D/'GRAPH_VERIFICATION.json').write_text(json.dumps(record,indent=2)+'\n')
assert added==[expected] and not removed and not rewired,(added,removed,rewired)
assert len(edges)==1 and edges[0]['from']==expected and edges[0]['to']=='two_body_autonomous_halt_bounded_theorem_note_2026-10-17',edges
print(json.dumps(record,indent=2))
