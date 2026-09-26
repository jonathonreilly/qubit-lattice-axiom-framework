#!/usr/bin/env python3
"""Descriptive completed-subset adapter; preserves every frozen declaration."""
from pathlib import Path
import argparse,datetime,json,math
import numpy as np
import analyze_dimer_routed_256 as base
from reconcile_dimer_routed_256_deadline import ident,check,save
HERE=Path(__file__).resolve().parent

def aggregate(x):
 return dict(mean=x.mean(axis=0).tolist(),standard_error=(x.std(axis=0,ddof=1)/math.sqrt(len(x))).tolist() if len(x)>1 else None)

def controls(path):
 assert not path.exists();r=base.exact_controls();r.update(adapter=ident(__file__),deadline_plan=ident(HERE/'DIMER_ROUTED_256_DEADLINE_ANALYSIS_PLAN.md'))
 save(path,r);print('Original exact observable controls and adapter identities sealed before aggregate access.')

def analyze(root,out,control_path):
 assert not out.exists();control=json.loads(control_path.read_text());assert control['analyzer']==ident(base.__file__) and control['adapter']==ident(__file__)
 check(control['deadline_plan']);mp=root/'MANIFEST.json';dp=root/'DISPATCH.json';rp=root/'RECOVERY_SUMMARY.json'
 m=json.loads(mp.read_text());d=json.loads(dp.read_text());recovery=json.loads(rp.read_text())
 assert recovery['status']=='reconciled_all_declarations' and recovery['manifest']==ident(mp)==d['manifest'] and recovery['dispatch']==ident(dp)
 check(recovery['reconciler']);check(recovery['progress']);check(d['wrapper']);check(m['binary'])
 for x in d['source_snapshots']:check(x['snapshot']);assert x['snapshot']['sha256']==x['original']['sha256']
 for x in m['geometry']:check(x['file'])
 jobs={(j['N'],j['kind'],j['replicate']):j for j in m['jobs']};assert len(jobs)==len(recovery['rows'])==16
 seen=set();cells={};declarations=[];audit=[];file_count=file_bytes=0
 for row in recovery['rows']:
  key=(row['N'],row['kind'],row['replicate']);assert key in jobs and key not in seen;seen.add(key);job=jobs[key]
  assert row['job']==job and row['seed']==job['seed'];declarations.append({k:row[k] for k in ['N','kind','replicate','seed','status']})
  for x in row['preserved_output_bindings']:check(x)
  if row['status']!='complete_verified_receipt':continue
  check(row['receipt']);receipt=json.loads(Path(row['receipt']['path']).read_text());assert receipt['job']==job and receipt['returncode']==0 and receipt['status']=='complete_verified_receipt'
  assert {x['path'] for x in receipt['outputs']}=={job['output']+s for s in ['', '.state','.stdout','.stderr']}
  for x in receipt['outputs']:check(x);file_count+=1;file_bytes+=x['bytes']
  value=json.loads(Path(job['output']).read_text());K=job['N']**3//2
  assert (value['N'],value['seed'],value['mode'])==(job['N'],job['seed'],'production')
  assert value['geometry']==job['command'][2] and value['pairs']==K and value['channels']==5*K
  assert value['minimum_nontrivial_cycle']>=job['N']//2 and value['key_permutation_verified'] and value['counts_verified']
  assert len(value['color_counts'])==14 and sum(value['color_counts'])==K
  assert 0<=value['color_changes']<=value['accepted']<=value['attempts'] and value['gamma']==1 and value['k0']==1.1
  assert [x['t'] for x in value['snapshots']]==base.TIMES.tolist() and not Path(job['output']+'.stderr').read_bytes()
  raw=np.asarray([x['fields'] for x in value['snapshots']],dtype=float);assert raw.shape==(5,3,6,2) and np.isfinite(raw).all()
  fields=(raw[...,0]+1j*raw[...,1])*np.array([math.sqrt(7)]*3+[math.sqrt(7)/2]*3)
  cells.setdefault(key[:2],[]).append((job,value,fields));audit.append(dict(N=key[0],kind=key[1],replicate=key[2],receipt=row['receipt']))
 assert seen==set(jobs)
 results=[];per=[];rng=np.random.default_rng(base.SEED)
 for N,kind in sorted({key[:2] for key in jobs}):
  entries=sorted(cells.get((N,kind),[]),key=lambda x:x[0]['replicate']);R=len(entries)
  declared=[x for x in declarations if (x['N'],x['kind'])==(N,kind)]
  cell=dict(N=N,kind=kind,declared_histories=len(declared),completed_histories=R,histories=R,declared_outcomes=declared,
   interval_scope='Descriptive conditional completed-subset intervals; administrative completion can depend on trajectory runtime. No censoring correction or unbiased-study claim.')
  if not R:cell.update(status='no_completed_histories',by_mode=None,mode_average=None);results.append(cell);continue
  fields=np.stack([x[2] for x in entries]);values=np.empty((R,5,3,4))
  for it,t in enumerate(base.TIMES):
   for axis in range(3):values[:,it,axis]=base.observables(fields[:,0,axis],fields[:,it,axis],axis,float(t))
  assert np.max(abs(values[:,0,:,0]))<1e-25
  average=values.mean(axis=2);flat=average.reshape(R,-1);mean=aggregate(average)
  if R>=2:
   boot=np.empty((base.BOOTSTRAPS,flat.shape[1]))
   for start in range(0,base.BOOTSTRAPS,500):
    end=min(start+500,base.BOOTSTRAPS);counts=rng.multinomial(R,np.ones(R)/R,size=end-start);boot[start:end]=(counts@flat)/R
   low,high=np.quantile(boot,[.025,.975],axis=0);mean.update(bootstrap95_low=low.reshape(5,4).tolist(),bootstrap95_high=high.reshape(5,4).tolist())
  else:mean.update(bootstrap95_low=None,bootstrap95_high=None)
  cell.update(status='complete_geometry_cohort' if R==8 else 'incomplete_geometry_cohort',times=base.TIMES.tolist(),metrics=list(base.METRICS),replicates=[x[0]['replicate'] for x in entries],
   by_mode=aggregate(values),mode_average=mean,normalized_component_variances=aggregate(abs(fields)**2),
   **{name:aggregate(np.array([x[1][name] for x in entries],dtype=float)) for name in ['attempts','accepted','color_changes','wall_seconds']})
  results.append(cell)
  for i,(job,value,_) in enumerate(entries):per.append(dict(N=N,kind=kind,replicate=job['replicate'],seed=job['seed'],by_time_mode_metric=values[i].tolist(),**{name:value[name] for name in ['attempts','accepted','color_changes','wall_seconds']}))
 out.mkdir(parents=True)
 save(out/'PER_HISTORY.json',dict(metric_order=list(base.METRICS),times=base.TIMES.tolist(),mode_order=['x','y','z'],rows=per))
 save(out/'AUTHENTICATION.json',dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),manifest=ident(mp),dispatch=ident(dp),reconciled_summary=ident(rp),history_receipts=audit,
  all_declarations=declarations,authenticated_completed_output_files=file_count,authenticated_completed_output_bytes=file_bytes,
  scope='All completed output bytes and preserved incomplete receipt outputs authenticated. Endpoint payloads hashed here; selected decoding is separate. All sixteen declarations retained.'))
 report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='complete_declared_study' if len(per)==16 else 'incomplete_declared_study_descriptive_completed_subset',
  adapter=ident(__file__),original_analyzer=ident(base.__file__),sign_controls=ident(control_path),manifest=ident(mp),reconciled_summary=ident(rp),
  per_history=ident(out/'PER_HISTORY.json'),authentication=ident(out/'AUTHENTICATION.json'),declared=16,completed=len(per),missing=16-len(per),all_declarations=declarations,
  bootstrap=dict(draws=base.BOOTSTRAPS,seed=base.SEED,unit='Whole independent history; directions/times/components retained together',interval='Pointwise percentile95 for the completed subset; unavailable when R<2; not simultaneous or censoring-adjusted'),
  expected_mode_average=[[0,float(np.cos(4*np.pi*t/7)),float(np.sin(4*np.pi*t/7)),1] for t in base.TIMES],cells=results,
  scope='Follow-up selected after the earlier N<=128 study. No pooling, fitted exponent, damping fit, representative-subset guarantee, or complete-study claim when censored.')
 save(out/'RESULTS.json',report);print(json.dumps(dict(completed=len(per),declared=16,results=ident(out/'RESULTS.json')),indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--controls-only',type=Path);p.add_argument('--root',type=Path);p.add_argument('--output',type=Path);p.add_argument('--controls',type=Path);a=p.parse_args()
 if a.controls_only:controls(a.controls_only)
 else:assert a.root and a.output and a.controls;analyze(a.root.resolve(),a.output.resolve(),a.controls.resolve())
