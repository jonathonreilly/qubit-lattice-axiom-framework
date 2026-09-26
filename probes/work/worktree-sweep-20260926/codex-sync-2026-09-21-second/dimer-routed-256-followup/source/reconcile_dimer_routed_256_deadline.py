#!/usr/bin/env python3
"""Preserve and reconcile every frozen declaration after the original wrapper exits."""
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess

def ident(p):
 p=Path(p);h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(2**20),b''):h.update(b)
 return dict(path=str(p.resolve()),bytes=p.stat().st_size,sha256=h.hexdigest())
def check(x):assert ident(x['path'])==x,x['path']
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')

def main(root,pid):
 out=root/'RECOVERY_SUMMARY.json';assert not out.exists()
 process=subprocess.run(['ps','-p',str(pid),'-o','args='],capture_output=True,text=True)
 assert 'dimer_routed_256_run.py' not in process.stdout,'Original wrapper is still active'
 now=datetime.datetime.now(datetime.timezone.utc);deadline=datetime.datetime.fromisoformat('2026-09-22T00:25:55+00:00')
 assert now>=deadline or (root/'SUMMARY.json').exists(),'No early administrative closure'
 mp=root/'MANIFEST.json';dp=root/'DISPATCH.json';m=json.loads(mp.read_text());d=json.loads(dp.read_text())
 check(d['manifest']);assert d['manifest']==ident(mp);check(d['wrapper']);check(m['binary'])
 for x in d['source_snapshots']:check(x['snapshot']);assert x['snapshot']['sha256']==x['original']['sha256']
 for x in m['geometry']:check(x['file'])
 jobs={(j['N'],j['kind'],j['replicate']):j for j in m['jobs']};assert len(jobs)==16
 progress=json.loads((root/'PROGRESS.json').read_text());assert progress['completed']==progress['total']==16
 normalized={}
 for row in progress['results']:
  ref=row.get('job',row);key=(ref['N'],ref['kind'],ref['replicate']);assert key in jobs and key not in normalized
  job=jobs[key];assert ref['seed']==job['seed'];path=Path(job['output']);status=row['status'];evidence=[]
  if 'receipt' in row:
   check(row['receipt']);receipt=json.loads(Path(row['receipt']['path']).read_text());assert receipt['job']==job and receipt['status']==status
   for x in receipt['outputs']:check(x);evidence.append(x)
   if status=='complete_verified_receipt':assert receipt['returncode']==0
   else:assert receipt['returncode']!=0
  elif status=='not_started_deadline':
   assert now>=deadline and row['job']==job
   assert not any(Path(str(path)+s).exists() for s in ['', '.state','.stdout','.stderr','.receipt.json'])
  else:
   assert status=='wrapper_failure',status
   evidence=[ident(Path(str(path)+s)) for s in ['', '.state','.stdout','.stderr','.receipt.json'] if Path(str(path)+s).exists()]
  normalized[key]=dict(N=key[0],kind=key[1],replicate=key[2],seed=job['seed'],job=job,status=status,original_progress_row=row,receipt=row.get('receipt'),preserved_output_bindings=evidence)
 assert set(normalized)==set(jobs)
 statuses={s:sum(x['status']==s for x in normalized.values()) for s in sorted({x['status'] for x in normalized.values()})}
 original=root/'SUMMARY.json';source_status='original_summary_present' if original.exists() else 'original_summary_missing_after_wrapper_exit'
 if original.exists():
  old=json.loads(original.read_text());assert old['statuses']==statuses
 logroot=Path(__file__).resolve().parent
 logs=[ident(logroot/f'DIMER_ROUTED_256_PRODUCTION_RUN.{s}') for s in ['log','stderr']]
 result=dict(created_utc=now.isoformat(),status='reconciled_all_declarations',source_status=source_status,
  reason='Frozen wrapper gives not-started rows a nested job shape while its final sort expects flat identifiers; original logs and PROGRESS are preserved.',
  reconciler=ident(__file__),manifest=ident(mp),dispatch=ident(dp),progress=ident(root/'PROGRESS.json'),original_summary=ident(original) if original.exists() else None,
  wrapper_process_check=dict(pid=pid,returncode=process.returncode,args=process.stdout.strip()),original_wrapper_logs=logs,statuses=statuses,rows=[normalized[k] for k in sorted(normalized)],
  scientific_scope='No seeds, execution order, stopping rule, failed data, or sampling decisions changed. No observable was used for reconciliation.')
 save(out,result);print(json.dumps(dict(statuses=statuses,summary=ident(out)),indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--wrapper-pid',type=int,required=True);a=p.parse_args();main(a.root.resolve(),a.wrapper_pid)
