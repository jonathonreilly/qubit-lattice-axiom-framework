from pathlib import Path
import json,subprocess,hashlib
w=Path('/private/tmp/review-drain-20260915/author-pool/author-backlog');o=Path('/private/tmp/review-drain-20260915');inv=json.loads((o/'check8058/inventory.json').read_text());allout={}
for c in inv['constituents']:
 pr=c['pr'];paths=[x['path'] for x in c['paths'] if x['path'].startswith('.claude/')];prefix=paths[0].split('/')[0:5];prefix='/'.join(prefix)+'/'
 # Prefix is .claude/science/physics-loops/PACKET (four components).
 prefix='/'.join(paths[0].split('/')[:4])+'/'
 keeps=['HANDOFF.md']
 for n in ('ROOT_CANONICAL_REVIEW.md','independent-canonical-review/REVIEW.md','TRACE_GATE.md'):
  if prefix+n in paths:keeps.append(n)
 if pr==8058:keeps+=['evidence/native-l4-third-vertex-post-review/INPUTS.json','evidence/native-l4-third-vertex-run-1085/RESULT.json','evidence/native-l4-third-vertex-run-1085/SOLVE_VECTORS.json']
 dest=w/f'docs/work_history/repo/review_feedback/pr{pr}-evidence'
 cmd=['python3',str(w/'docs/ai_methodology/skills/review-loop/scripts/review_workspace.py'),'archive','--repo',str(w),'--revision',c['head'],'--prefix',prefix,'--destination',str(dest),'--namespace',f'pr{pr}']
 for k in keeps:cmd+=['--keep',k]
 result=subprocess.check_output(cmd);(o/f'{pr}-archive-author-receipt.json').write_bytes(result)
 m=json.loads((dest/'archive-manifest.json').read_text());assert {x['original_path']:x['raw_sha256'] for x in m['entries']}=={x['path']:x['sha256'] for x in c['paths'] if x['path'].startswith(prefix)}
 allout[str(pr)]={'head':c['head'],'prefix':prefix,'manifest_path':str(dest/'archive-manifest.json'),'manifest_sha256':hashlib.sha256((dest/'archive-manifest.json').read_bytes()).hexdigest(),'count':len(m['entries']),'keep_raw':keeps,'mapping':{x['original_path']:str((dest/x['stored_path']).relative_to(w)) for x in m['entries']}}
(o/'8058-archive-anchor.json').write_text(json.dumps(allout,indent=2)+'\n');print({k:v['count'] for k,v in allout.items()})
