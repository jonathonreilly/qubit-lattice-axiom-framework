from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
coldpath=r/'drain8164-cold-confirmation-v1.json';assert sha(coldpath)=='e5e212d19a44ef433f82ef6c2dafd37d2f1300c9dbbfda96ddbd20953b965c24'
cold=json.loads(coldpath.read_text());assert cold['verdict']=='SOURCE_COLD_PASS_BOUNDED_CAPTURE_ELIGIBLE_AFTER_CHEAP_PREFLIGHT' and cold['tree']=='a61c1aa27111156ac99ba6346a58ed184aa689aa'
pre=json.loads((r/'drain8164-author-cheap-v1.json').read_text());assert pre['mechanical_status']=='ok' and not pre['cache_checked']
planpath=r/'drain8164-capture-plan-v1.json';assert sha(planpath)=='7dccfebda94ab69352854bc5854fd7f559a58c7939b5ad6ece3b5dbf299c6049'
plan=json.loads(planpath.read_text())['programs'];assert len(plan)==8
for x in plan:
 assert x['json_destination']=='logs/runner-cache/'+Path(x['runner']).with_suffix('.json').name
 assert sha(r/'drain-author-slot'/x['runner'])==x['source_sha256']
s=(r/'drain8163-capture.py').read_text().replace('review-meta-slot','drain-author-slot').replace('drain8163','drain8164').replace('draft-v4','draft-v1').replace('cheap-v4','cheap-v1').replace('confirmation-v4','confirmation-v1').replace('9f543c83c7bc51f299e60b64e822bd90e74b6d0a66b7bfad90913006f1e040e6',sha(coldpath)).replace('PASS STAGED COLD SOURCE CONFIRMATION',cold['verdict'])
rows=[(Path(x['runner']).stem,x['runner'],x['timeout_seconds'],x['process_tree_rss_cap_bytes']) for x in plan]
start=s.index('for _,runner,_,_ in ');stop=s.index('\n verify();receipt=',start)
s=s[:start]+'for _,runner,_,_ in '+repr(rows)+":assert not (w/'logs/runner-cache'/Path(runner).with_suffix('.json').name).exists(),runner\nfor pr,primary,cap_seconds,cap_bytes in "+repr(rows)+':'+s[stop:]
p=r/'drain8164-capture.py';assert not p.exists();compile(s,str(p),'exec');p.write_text(s);print(sha(p))
