"""Extract only model configuration, usage counters and task times; never message bodies."""
from pathlib import Path
import collections,datetime,hashlib,json,sqlite3
B=Path(__file__).resolve().parent
conn=sqlite3.connect('file:/Users/jonBridger/.codex/state_5.sqlite?mode=ro',uri=True);conn.row_factory=sqlite3.Row
rates=json.loads((B/'pricing.json').read_text())['standard_credits_per_million']
for label,path,model,effort in [('reviewer-a','/root/sol_max_matched_8158','gpt-6-sol','max'),('reviewer-b','/root/astra_low_matched_8158','gpt-6-astra','low')]:
 meta=dict(conn.execute('select id,rollout_path,model,reasoning_effort,agent_path from threads where agent_path=? order by created_at desc',(path,)).fetchone())
 assert (meta['model'],meta['reasoning_effort'])==(model,effort)
 records=[];starts=[];ends=[];configs=[];last_total=None;seen=set()
 for line in Path(meta['rollout_path']).read_text().splitlines():
  e=json.loads(line);v=e.get('payload',{});kind=e.get('type')
  if kind=='turn_context':configs.append({k:v.get(k) for k in ['model','effort','service_tier']})
  if kind=='event_msg':
   if v.get('type')=='task_started':starts.append(e['timestamp'])
   if v.get('type') in ['task_complete','task_completed']:ends.append(e['timestamp'])
   if v.get('type')=='token_count' and v.get('info'):last_total=v['info']['total_token_usage']
  if kind=='token_usage_record':
   rid=v['response_id'];assert rid not in seen;seen.add(rid)
   records.append(dict(timestamp=e['timestamp'],response_id=rid,usage=v['usage']))
 assert len(starts)==len(ends)==1,(label,'review task not complete',starts,ends)
 assert (B/label/'review.json').is_file() and (B/label/'review.md').is_file()
 total=dict(sum((collections.Counter(x['usage']) for x in records),collections.Counter()))
 assert all(total.get(k,0)==v for k,v in last_total.items()),(label,'counter mismatch')
 assert all(c['model']==model and c['effort']==effort for c in configs),configs
 it=total['input_tokens'];ct=total['cached_input_tokens'];ot=total['output_tokens'];assert 0<=ct<=it
 p=rates[model];cost=((it-ct)*p['uncached_input']+ct*p['cached_input']+ot*p['output'])/1e6
 parse=lambda t:datetime.datetime.fromisoformat(t.replace('Z','+00:00'))
 report={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [(B/label/'review.json'),(B/label/'review.md')]}
 result=dict(session=meta,actual_configurations=configs,task_start=starts[0],task_end=ends[0],active_task_seconds=(parse(ends[0])-parse(starts[0])).total_seconds(),request_count=len(records),total_token_usage=total,request_usage_records=records,modeled_standard_credits=cost,modeled_fast_credits=2.5*cost,report_hashes=report,pricing_reference='pricing.json',boundary='Observed reviewer request tokens and active task time; setup/coordinator/scoring work excluded. Reasoning tokens are included in output, not added again. Credits are modeled, not a billing receipt; service tier only asserted if observed.')
 out=B/(label+'-usage.json');assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n')
 print(label,model,effort,result['active_task_seconds'],total,cost)
