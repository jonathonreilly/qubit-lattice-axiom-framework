"""Capture and adapt the exact current static publication machinery, metadata only."""
from pathlib import Path
import ast,hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent
B=N/'commuting_static_edge_qualified_publication_draft'
sha=lambda b:hashlib.sha256(b).hexdigest()
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
def put(p,b):
 p.parent.mkdir(parents=True,exist_ok=True);assert not p.exists(),p;p.write_bytes(b)
f=(B/'FINAL_FREEZE.json').read_bytes();index={r['path']:r for r in json.loads(f)['members']};rows=[]
def cp(rel,dest):
 b=(B/rel).read_bytes();assert ident(b)=={k:index[rel][k] for k in ['bytes','sha256']}
 put(D/dest,b);rows.append({'source':str(B/rel),'recovery_path':dest,**ident(b)})
put(D/'machinery_reference/FINAL_FREEZE.json',f)
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 cp(name,'machinery_reference/'+name)
for mode in ['build','inspection','seal']:
 for p in sorted((B/'metadata_runs'/mode).iterdir()):
  if p.is_file():cp(str(p.relative_to(B)),'machinery_reference/evidence/'+mode+'/'+p.name)
for name in ['AGENTS.md','SCIENCE_WORKFLOW.md','build_citation_graph.py']:cp('methodology/'+name,'methodology/'+name)
cp('MACHINERY_SOURCE_PINS.json','methodology/BASELINE_SOURCE_PINS.json')
put(D/'MACHINERY_SOURCE_PINS.json',(json.dumps({'baseline':str(B),'baseline_freeze':ident(f),'sources':rows,
 'procedure_authority_ref':'56c5c0ab64f532c5784e895b2f9aa6894fa334e0','procedure_capture_ref':'5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2',
 'current_instruction_reuse_authorized_by_root':True,'new_git_commands':0,'selected_only':True,
 'no_recursive_publication_archive':True,'new_scientific_executions':0},indent=2)+'\n').encode())
print(json.dumps({'captured_selected_files':len(rows),'baseline_freeze':ident(f),'science_executions':0},indent=2))
