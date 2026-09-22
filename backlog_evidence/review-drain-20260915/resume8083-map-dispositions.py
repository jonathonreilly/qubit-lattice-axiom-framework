from pathlib import Path
import json,subprocess,hashlib,gzip,collections
r=Path('/private/tmp/review-drain-20260915');repo=r/'resume-author8083';units=json.loads((r/'resume8083-original-deltas.json').read_text());out=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
gitblob=lambda b:hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
for u in units:
 n=u['pr'];ap=Path(f'docs/work_history/repo/review_feedback/pr{n}-evidence/archive-manifest.json');man=json.loads((repo/ap).read_text());am={x['original_path']:x for x in man['entries']}
 for row in u['rows']:
  p=row['path'];entry=dict(pr=n,head=u['head'],base=u['base'],**row)
  if p in am:
   e=am[p];q=ap.parent/e['stored_path'];b=(repo/q).read_bytes();raw=gzip.decompress(b)if e['encoding']=='gzip'else b
   assert sha(b)==e['stored_sha256'] and sha(raw)==e['raw_sha256'] and gitblob(raw)==row['after_blob']==e['git_blob'] and row['after_mode']==e['original_mode']
   entry.update(disposition='accepted unchanged as historical source/evidence',final_path=str(q),final_sha256=sha(b),raw_sha256=sha(raw),final_blob=gitblob(b),reason='Exact original source or historical record preserved; historical labels confer no current verdict.')
  elif p=='docs/audit/data/citation_graph_manifest.json':
   entry.update(disposition='superseded',final_path=p,reason='Original generated topology acknowledgement is not scientific evidence; regenerate for final integrated source topology. Original Git head/blob is exact recovery location.')
  elif p.startswith(('docs/','scripts/')):
   b=(repo/p).read_bytes();entry.update(disposition='narrowed',final_path=p,final_sha256=sha(b),final_blob=gitblob(b),reason='Current portable canonical publication/compact evidence wrapper; original scientific body preserved with historical/current authority separated. Source verdict pending final correction.')
  else:raise RuntimeError(p)
  out.append(entry)
result=dict(scope='Draft-bound complete original constituent path dispositions; does not confer semantic PASS',candidate_base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip(),candidate_staged_tree=subprocess.check_output(['git','write-tree'],cwd=repo,text=True).strip(),entries=out,counts=dict(collections.Counter(x['disposition']for x in out)))
(r/'resume8083-draft-dispositions.json').write_text(json.dumps(result,indent=2)+'\n');print(len(out),result['counts']);print('sha256',sha((r/'resume8083-draft-dispositions.json').read_bytes()))
