import sys,json,importlib.util,hashlib
from pathlib import Path
r=Path('/private/tmp/review-drain-20260915');w=r/'review-meta-slot';sys.path[:0]=[str(w/'scripts'),str(w/'docs/audit/scripts')]
import build_citation_graph as g, runner_cache as c, audit_packet_script_deps as p
j=json.loads((r/'drain8150-original-inventory.json').read_text());out=[]
for u in j:
 n=u['number'];root=r/'drain8150-originals'/str(n); runner=next(root/x['path'] for x in u['original_paths'] if x['path'].startswith('scripts/'));note=next(root/x['path'] for x in u['original_paths']if x['path'].startswith('docs/')and x['path'].endswith('.md'))
 p.SCRIPTS_DIR=root/'scripts'
 inputs=c.declared_input_paths(runner);bound=[]
 for name in inputs:
  f=root/name if (root/name).exists()else w/name
  bound.append({'path':name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'source':str(f),'role':'own note'if f==note else 'current repository premise/read input'})
 out.append({'pr':n,'claim_type':g.extract_claim_type_hint(note.read_text()),'timeout':c.declared_timeout_for(runner),'graph_helpers':g.resolve_helper_runner_paths(str(runner)),'packet_helpers':sorted(p.transitive_helpers(runner.stem)),'inputs':bound,'canonical_source_conflicts':[x['path']for x in u['original_paths']if (x['path'].startswith('scripts/')or (x['path'].startswith('docs/')and x['path'].endswith('.md')))and (w/x['path']).exists()]})
(r/'drain8150-original-discovery.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
