"""Capture bounded prior machinery/current procedure; no science execution."""
from pathlib import Path
import hashlib,json,subprocess
D=Path(__file__).resolve().parent;N=D.parent
B=N/'endpoint_target_compilation_qualified_publication_draft'
W=N.parent/'correlation_worktree'
REF='5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2'
sha=lambda b:hashlib.sha256(b).hexdigest()
def pin(b):return {'bytes':len(b),'sha256':sha(b)}
f=(B/'FINAL_FREEZE.json').read_bytes()
assert sha(f)=='d8d497c515fa8f1eebf4f336a55435557cc3c8b60384f4a17a5ce2d40a8c37d7'
index={r['path']:r for r in json.loads(f)['members']};rows=[]
def cp(rel,dest):
 b=(B/rel).read_bytes();assert pin(b)=={k:index[rel][k] for k in ['bytes','sha256']}
 p=D/dest;p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists();p.write_bytes(b)
 rows.append({'source':str(B/rel),'recovery_path':dest,**pin(b)})
(D/'machinery_reference').mkdir(exist_ok=False)
(D/'machinery_reference/FINAL_FREEZE.json').write_bytes(f)
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 cp(name,'machinery_reference/'+name)
for mode in ['build','inspection','seal']:
 for p in sorted((B/'metadata_runs'/mode).iterdir()):
  if p.is_file():cp(str(p.relative_to(B)),'machinery_reference/evidence/'+mode+'/'+p.name)
commands=[]
for path in ['docs/ai_methodology/SCIENCE_WORKFLOW.md','AGENTS.md','docs/audit/scripts/build_citation_graph.py']:
 argv=['git','-C',str(W),'show',REF+':'+path]
 r=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=10)
 assert r.returncode==0,(path,r.stderr)
 dest=D/'methodology'/Path(path).name;dest.parent.mkdir(exist_ok=True);dest.write_bytes(r.stdout)
 commands.append({'argv':argv,'exit_code':r.returncode,'stdout_recovery':str(dest.relative_to(D)),
                  'stdout':pin(r.stdout),'stderr':r.stderr.decode()})
(D/'MACHINERY_SOURCE_PINS.json').write_text(json.dumps({'baseline_freeze':pin(f),'selected_only':True,
 'no_recursive_publication_archives':True,'sources':rows,'current_procedure_ref':REF,'read_only_commands':commands},indent=2)+'\n')
print(json.dumps({'selected_machinery_and_evidence_files':len(rows),'current_procedure_files':len(commands),'scientific_executions':0}))
