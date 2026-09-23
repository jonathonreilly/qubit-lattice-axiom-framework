from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
coldpath=r/'drain8167-cold-review-v1.json';assert sha(coldpath)=='c875e4ee4fe7d99e64d821f19f3a9c1f3f912e4c6dfe4bc9d881c9b0190ed287';cold=json.loads(coldpath.read_text());assert cold['verdict']=='PASS_WITH_BOUNDED_CLAIMS_SOURCE_ONLY'
pre=json.loads((r/'drain8167-author-cheap-v1.json').read_text());assert pre['mechanical_status']=='ok' and not pre['cache_checked']
planpath=r/'drain8167-capture-plan-v2.json';assert sha(planpath)=='bc0fcd6e6dba3aa773109ad8d2b53e6b18ab81763f588df7c16b48ed3f79e851';plan=json.loads(planpath.read_text())['order'];assert len(plan)==2
for x in plan:
 assert x['json_output']=='logs/runner-cache/'+Path(x['runner']).with_suffix('.json').name
 assert sha(r/'review-meta-slot'/x['runner'])==x['source_sha256']
s=(r/'drain8163-capture.py').read_text().replace('drain8163','drain8167').replace('draft-v4','draft-v1').replace('cheap-v4','cheap-v1').replace('drain8167-cold-confirmation-v4.json',coldpath.name).replace('9f543c83c7bc51f299e60b64e822bd90e74b6d0a66b7bfad90913006f1e040e6',sha(coldpath)).replace('PASS STAGED COLD SOURCE CONFIRMATION',cold['verdict'])
rows=[(Path(x['runner']).stem,x['runner'],x['timeout_seconds'],x['process_tree_rss_limit_bytes']) for x in plan]
start=s.index('for _,runner,_,_ in ');stop=s.index('\n verify();receipt=',start)
s=s[:start]+'for _,runner,_,_ in '+repr(rows)+":assert not (w/'logs/runner-cache'/Path(runner).with_suffix('.json').name).exists(),runner\nfor pr,primary,cap_seconds,cap_bytes in "+repr(rows)+':'+s[stop:]
p=r/'drain8167-capture.py';assert not p.exists();compile(s,str(p),'exec');p.write_text(s);print(sha(p))
