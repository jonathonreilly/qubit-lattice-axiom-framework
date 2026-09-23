from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
coldpath=r/'drain8163-cold-confirmation-v4.json';cold=json.loads(coldpath.read_text());assert cold['tree']=='b0a6014e85334e890cda852da411cccb0827b273'
assert cold['verdict']=='PASS STAGED COLD SOURCE CONFIRMATION'
pre=json.loads((r/'drain8163-author-cheap-v4.json').read_text());assert pre['mechanical_status']=='ok' and not pre['cache_checked']
planpath=r/'drain8163-capture-plan-v2.json';assert sha(planpath)=='a979f2f9cb89d5e4b73473c1fe5e0f2f0eff5b5b033a4552ad22e7b381059aa5';plan=json.loads(planpath.read_text())['order'];assert len(plan)==6
for x in plan:
 assert x['json_output']=='logs/runner-cache/'+Path(x['runner']).with_suffix('.json').name
 assert x['timeout_seconds']==180 and x['process_tree_rss_limit_bytes']==768*1048576
 assert sha(r/'review-meta-slot'/x['runner'])==x['source_sha256']
s=(r/'drain8159-capture.py').read_text().replace('review-draft-slot','review-meta-slot').replace('drain8159','drain8163').replace('author-unit-draft-v1','author-unit-draft-v4').replace('author-cheap-v1','author-cheap-v4').replace('cold-confirmation-v1','cold-confirmation-v4').replace('ba0ef06b15272b36d374c388afa5d4010d6571b6cb8768ab240a80a65a16e457',sha(coldpath)).replace("cold['status']=='COLD SOURCE CONFIRMED; ELIGIBLE FOR DECLARED BOUNDED CAPTURES; PARTIAL SALVAGE ONLY'","cold['status']=="+repr(cold['verdict']))
rows=[(Path(x['runner']).stem,x['runner'],x['timeout_seconds'],x['process_tree_rss_limit_bytes']) for x in plan]
start=s.index('for _,runner,_,_ in ');stop=s.index('\n verify();receipt=',start)
s=s[:start]+"for _,runner,_,_ in "+repr(rows)+":assert not (w/'logs/runner-cache'/Path(runner).with_suffix('.json').name).exists(),runner\nfor pr,primary,cap_seconds,cap_bytes in "+repr(rows)+":"+s[stop:]
s=s.replace("cold['status']", "cold['verdict']")
p=r/'drain8163-capture.py';assert not p.exists();compile(s,str(p),'exec');p.write_text(s);print(sha(p))
