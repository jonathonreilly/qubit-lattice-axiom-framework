from pathlib import Path
import json,subprocess,hashlib
w=Path('/private/tmp/review-drain-20260915/author-pool/author-backlog');o=Path('/private/tmp/review-drain-20260915');plan=json.loads((o/'8061-author-archive-plan.json').read_text());allout={}
for c in plan:
 pr=c['pr'];dest=w/f'docs/work_history/repo/review_feedback/pr{pr}-evidence';cmd=['python3',str(w/'docs/ai_methodology/skills/review-loop/scripts/review_workspace.py'),'archive','--repo',str(w),'--revision',c['head'],'--prefix',c['prefix'],'--destination',str(dest),'--namespace',f'pr{pr}']
 for k in c['keep_raw']:cmd+=['--keep',k]
 result=subprocess.check_output(cmd);(o/f'{pr}-archive-author-receipt.json').write_bytes(result);m=json.loads((dest/'archive-manifest.json').read_text());assert len(m['entries'])==c['original_history_count']
 allout[str(pr)]={'head':c['head'],'prefix':c['prefix'],'manifest_path':str(dest/'archive-manifest.json'),'manifest_sha256':hashlib.sha256((dest/'archive-manifest.json').read_bytes()).hexdigest(),'count':len(m['entries']),'keep_raw':c['keep_raw'],'mapping':{x['original_path']:str((dest/x['stored_path']).relative_to(w)) for x in m['entries']}}
(o/'8061-archive-anchor.json').write_text(json.dumps(allout,indent=2)+'\n');print({k:v['count'] for k,v in allout.items()})
