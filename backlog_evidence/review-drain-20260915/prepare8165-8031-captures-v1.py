from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
configs=[('8165','author-draft-slot','drain8165-cold-source-confirmation-v1.json','23e5ef3bdb74b24bea00fc587066a78e30540959328430351439fd39278de292','PASS_COLD_SOURCE_WITH_BOUNDED_CLAIMS','tree','72c562ec6ce768dab8c86385fe87345aeebada911e2cbc1836e40946f0e73a76'),('8031','review-draft-slot','drain8031-cold-confirmation-v1.json','2e002d0b440b23ec69f5eaa2272105e6ce95a7a23ac2c122b5aa366c65772c2f','SOURCE_CONFIRMED_FOR_BOUNDED_CAPTURE','staged_tree','e79ba1f9d17ca5942c6bc0cfef4159f9f6f37b85764930d513d2284d6aabe5fb')]
for unit,slot,coldname,coldhash,verdict,tree_key,planhash in configs:
 coldpath=r/coldname;assert sha(coldpath)==coldhash;cold=json.loads(coldpath.read_text());assert cold['verdict']==verdict
 draft=json.loads((r/f'drain{unit}-author-unit-draft-v1.json').read_text());assert cold[tree_key]==draft['source']['tree']
 pre=json.loads((r/f'drain{unit}-author-cheap-v1.json').read_text());assert pre['mechanical_status']=='ok' and not pre['cache_checked']
 planpath=r/f'drain{unit}-capture-plan-v1.json';assert sha(planpath)==planhash;plan=json.loads(planpath.read_text())
 entries=plan['order'] if unit=='8165' else [plan];assert len(entries)==(3 if unit=='8165' else 1)
 rows=[]
 for x in entries:
  assert (x['json_output'] if unit=='8165' else x['json_destination'])=='logs/runner-cache/'+Path(x['runner']).with_suffix('.json').name
  assert sha(r/slot/x['runner'])==x['source_sha256']
  rows.append((Path(x['runner']).stem,x['runner'],x['timeout_seconds'],x['process_tree_rss_limit_bytes'] if unit=='8165' else x['rss_limit_MiB']*1048576))
 s=(r/'drain8163-capture.py').read_text().replace('review-meta-slot',slot).replace('drain8163','drain'+unit).replace('draft-v4','draft-v1').replace('cheap-v4','cheap-v1').replace(f'drain{unit}-cold-confirmation-v4.json',coldname).replace('9f543c83c7bc51f299e60b64e822bd90e74b6d0a66b7bfad90913006f1e040e6',coldhash).replace('PASS STAGED COLD SOURCE CONFIRMATION',verdict).replace("cold['tree']",f"cold[{tree_key!r}]")
 start=s.index('for _,runner,_,_ in ');stop=s.index('\n verify();receipt=',start)
 s=s[:start]+'for _,runner,_,_ in '+repr(rows)+":assert not (w/'logs/runner-cache'/Path(runner).with_suffix('.json').name).exists(),runner\nfor pr,primary,cap_seconds,cap_bytes in "+repr(rows)+':'+s[stop:]
 p=r/f'drain{unit}-capture.py';assert not p.exists();compile(s,str(p),'exec');p.write_text(s);print(unit,sha(p))
