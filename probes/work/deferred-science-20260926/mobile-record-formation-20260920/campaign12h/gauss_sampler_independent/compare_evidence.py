#!/usr/bin/env python3
"""Source comparison, exact receipt authentication, and selective raw reductions.

No production replay. Large raw CSV hashes are recorded claims, not recomputed;
all compact blocks and metadata are authenticated, and small raw windows tested.
"""
from pathlib import Path
from io import StringIO
import hashlib,json,re
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
identities={}
def read(p):
 p=Path(p);raw=p.read_bytes();identities[str(p)]={'bytes':len(raw),'sha256':sha(raw)};return raw
def load(p):return json.loads(read(p))
def close(a,b):return bool(np.allclose(a,b,rtol=1e-10,atol=2e-8,equal_nan=False))
def lag_columns(a):
 out=[]
 for x in a.T:
  u=x[:-1];v=x[1:]
  if len(x)<=2 or min(np.std(u),np.std(v))<=1e-13:out.append(None)
  else:
   u=u-u.mean();v=v-v.mean();out.append(float((u@v)/np.sqrt((u@u)*(v@v))))
 return out

def compare_lags(actual,expected):
 assert len(actual)==len(expected)
 for a,b in zip(actual,expected):
  assert (a is None)==(b is None)
  if a is not None:assert abs(a-b)<1e-10

pre=load(HERE/'PRE_COMPARISON_SEAL.json')
for item in pre['sources']+pre['artifacts']:
 raw=Path(item['path']).read_bytes();assert sha(raw)==item['sha256'] and len(raw)==item['bytes']
first=read(ROOT/'gauss_worm_screen.cpp').decode();follow=read(ROOT/'gauss_worm_z1_followup.cpp').decode()
assert first.replace('for(int L:{9,13,17})for(double z:{.2,1.,4.}){','for(int L:{17,25,33,49})for(double z:{1.}){').replace('20260921300ULL','20260921400ULL')==follow
for checker,result,log in [('gauss_worm_trace_check.py','GAUSS_WORM_TRACE_RESULTS.json','GAUSS_WORM_TRACE_RUN.log'),('centered_gauss_staggered_check.py','CENTERED_GAUSS_STAGGERED_RESULTS.json','CENTERED_GAUSS_STAGGERED_RUN.log')]:
 code=read(ROOT/checker);r=load(ROOT/result);text=read(ROOT/log).decode()
 assert r['source_sha256']==sha(code) and all(x['passed'] for x in r['checks'])
 assert text.count('PASS: ')==len(r['checks']) and 'FAIL' not in text

read(ROOT/'CENTERED_GAUSS_STAGGERED_SECTORS_AND_ADJOINT_ESCAPE.md')
reducer=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-20/worm_block_reduce.cpp')
reducer_hash=sha(read(reducer))
read(Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-20/worm_block_reduce'))
for path in ['GAUSS_WORM_SCREEN_PLAN.md','GAUSS_WORM_Z1_FOLLOWUP_PLAN.md','GAUSS_WORM_SCREEN_RUN.log','GAUSS_WORM_Z1_FOLLOWUP_RUN.log','GAUSS_WORM_ANALYSIS_RUN.log','GAUSS_WORM_Z1_ANALYSIS_RUN.log','gauss_worm_z1_followup/SOURCE_CHANGE.diff']:
 read(ROOT/path)
rows=[];raw_total_bytes=0;raw_window_bytes=0;compact_block_bytes=0
for folder,analysis_name,analysis_script,Ls,zs,burn,production,seedbase in [
 ('gauss_worm_screen','SCREEN_ANALYSIS.json','analyze_gauss_worm_screen.py',[9,13,17],[.2,1.,4.],5000000,25000000,20260921300),
 ('gauss_worm_z1_followup','FOLLOWUP_ANALYSIS.json','analyze_gauss_worm_z1_followup.py',[17,25,33,49],[1.],100000000,1000000000,20260921400)]:
 rawdir=ROOT/folder;out=rawdir/'analysis'
 production_seal=load(rawdir/'PRE_PRODUCTION_SEAL.json')
 assert production_seal['parameters']=={'burn':burn,'production':production,'threads':8}
 for row in production_seal['files']:
  body=read(Path(row['path']));assert sha(body)==row['sha256'] and len(body)==row['bytes']
 source=read(ROOT/analysis_script)
 analysis=load(out/analysis_name)
 assert analysis.get('analysis_source_sha256',analysis.get('source_sha256'))==sha(source)
 manifest_raw=read(out/'RAW_IDENTITIES.json');manifest=json.loads(manifest_raw)
 assert analysis['raw_identities_sha256']==sha(manifest_raw)
 assert manifest['reducer_source_sha256']==reducer_hash
 expected={f'L{L}_z{int(z*10)}_init{initial}':(L,z,initial,seedbase+2*idx+initial)
           for idx,(L,z) in enumerate((L,z) for L in Ls for z in zs) for initial in (0,1)}
 assert {c['tag'] for c in analysis['cases']}==set(expected)
 claimed={Path(r['path']).stem:r for r in manifest['files']}
 assert set(claimed)==set(expected)
 for c in analysis['cases']:
  tag=c['tag'];L,z,initial,seed=expected[tag]
  meta_raw=read(rawdir/(tag+'.json'));meta=json.loads(meta_raw)
  summary=load(out/(tag+'_summary.json'))
  reduce_log=read(out/(tag+'_reduce.log')).decode()
  assert c['metadata']==meta and c['summary']==summary
  assert meta['L']==L and meta['z']==z and meta['initialization']==initial and meta['seed']==seed
  assert meta['burn_attempts']==burn and meta['production_attempts']==production
  assert meta['accepted']==meta['creations']+meta['removals']
  assert meta['final_occupied']==initial*L**3+meta['creations']-meta['removals']
  assert 0<=meta['final_occupied']<=L**3
  stride=1024 if z<.5 else 1
  assert meta['closed_trace_stride']==stride and meta['samples']==meta['production_closed_visits']//stride
  n=meta['samples'];nb=n//128;tail=n%128
  assert summary['samples']==n and summary['blocks']==nb and summary['discarded_tail']==tail
  assert f'{n} samples, {summary["observable_changes"]} observable changes, {summary["flux_changes"]} flux changes' in reduce_log
  assert 0<=summary['flux_changes']<=summary['observable_changes']<n
  assert 1<=summary['maximum_identical_observable_run']<=n
  rawpath=Path(claimed[tag]['path']);assert rawpath==rawdir/(tag+'.csv')
  assert rawpath.stat().st_size==claimed[tag]['bytes']
  assert sha(meta_raw)==claimed[tag]['metadata_sha256']
  assert re.fullmatch('[0-9a-f]{64}',claimed[tag]['sha256'])
  raw_total_bytes+=rawpath.stat().st_size
  block_raw=read(out/(tag+'_blocks.csv'));compact_block_bytes+=len(block_raw)
  block=np.loadtxt(StringIO(block_raw.decode()),delimiter=',',skiprows=1,ndmin=2)
  assert block.shape==(nb,9) and np.array_equal(block[:,0],np.arange(nb))
  b=block[:,1:];assert np.isfinite(b).all()
  # Read only first 256 rows plus at most 65,536 tail bytes of each raw CSV.
  with rawpath.open('rb') as f:
   header=f.readline();prefix=b''.join(f.readline() for _ in range(256))
   f.seek(max(0,rawpath.stat().st_size-65536));tail_bytes=f.read()
  raw_window_bytes+=len(header)+len(prefix)+len(tail_bytes)
  begin=np.loadtxt(StringIO(prefix.decode()),delimiter=',',ndmin=2)
  assert np.array_equal(begin[:,0],np.arange(256))
  # Discard the potentially partial leading line from the random-access tail.
  end=np.loadtxt(StringIO(tail_bytes.decode().split('\n',1)[1]),delimiter=',',ndmin=2)
  assert int(end[-1,0])==n-1 and np.array_equal(np.diff(end[:,0]),np.ones(len(end)-1))
  assert np.all(np.diff(begin[:,1])>0) and np.all(np.diff(end[:,1])>0)
  assert 1<=begin[0,1] and end[-1,1]<=production
  assert close(begin[:128,2:].mean(axis=0),b[0])
  assert close(begin[128:256,2:].mean(axis=0),b[1])
  last_block=end[(end[:,0]>=(nb-1)*128)&(end[:,0]<nb*128)]
  assert len(last_block)==128 and close(last_block[:,2:].mean(axis=0),b[-1])
  leftover=end[end[:,0]>=nb*128,2:]
  assert len(leftover)==tail
  reconstructed=(128*b.sum(axis=0)+leftover.sum(axis=0))/n
  assert close(reconstructed,summary['mean'])
  assert close(begin[0,2:],summary['first']) and close(end[-1,2:],summary['last'])
  windows=np.vstack((begin[:,2:],end[:,2:]))
  assert np.all(windows>=np.array(summary['minimum'])-1e-10)
  assert np.all(windows<=np.array(summary['maximum'])+1e-10)
  assert np.max(np.abs(windows[:,0]*L**3-np.rint(windows[:,0]*L**3)))<1e-8
  assert np.max(np.abs(windows[:,5:]/L-np.rint(windows[:,5:]/L)))<1e-8
  if 'profiles' in c:
   for profile in c['profiles']:
    size=profile['block_size'];group=size//128;count=len(b)//group
    x=b[:count*group].reshape(count,group,8).mean(axis=1);mean=x.mean(axis=0);half=count//2
    assert profile['blocks']==count and profile['discarded_samples']==n-count*size
    assert close(profile['first_half_mean'],x[:half].mean(axis=0))
    assert close(profile['last_half_mean'],x[-half:].mean(axis=0))
    lags=lag_columns(x);compare_lags(lags,profile['lag1_block_correlation'])
    estimates=list(mean[:5])+[mean[1]/mean[2],mean[3]/mean[4]]
    for key,estimate in zip(['rho','S_x1','S_x2','S_xy1','S_xy2','ratio_axis','ratio_diagonal'],estimates):
     val=profile['values'][key];assert close(val['estimate'],estimate)
     assert (val['interval'] is None)==(count<16)
     if val['interval'] is not None:assert np.isfinite(val['interval']).all() and val['interval'][0]<=val['interval'][1]
    flags=[]
    if count<16:flags.append('fewer_than_16_complete_blocks')
    if any(a is not None and abs(a)>.2 for a in lags):flags.append('material_lag1_block_dependence')
    if summary['maximum_identical_observable_run']>size:flags.append('identical_run_exceeds_block_size')
    assert flags==profile['flags']
  else:
   half=len(b)//2
   assert close(c['first_half_block_mean'],b[:half].mean(axis=0)) and close(c['last_half_block_mean'],b[-half:].mean(axis=0))
   lags=lag_columns(b);compare_lags(lags,c['block_lag1_correlation'])
   for kind,a,d in [('axis',1,2),('diagonal',3,4)]:
    val=c['ratios'][kind]
    if b[:,d].mean()<1e-15:assert val['estimate'] is None and val['interval'] is None
    else:
     assert close(val['estimate'],b[:,a].mean()/b[:,d].mean())
     assert (val['interval'] is None)==(nb<16)
   flags=[]
   if nb<16:flags.append('insufficient_prespecified_block_count')
   if summary['flux_changes']==0:flags.append('no_observed_winding_change')
   if summary['observable_changes']==0:flags.append('all_observed_states_identical_in_saved_observables')
   if summary['maximum_identical_observable_run']>128:flags.append('identical_run_exceeds_block_length')
   if any(a is not None and abs(a)>.2 for a in lags):flags.append('material_lag1_block_dependence')
   assert flags==c['flags']
  rows.append({'folder':folder,'tag':tag,'raw_recorded_sha256':claimed[tag]['sha256'],
   'full_raw_hash_independently_recomputed':False,'raw_bytes':claimed[tag]['bytes'],
   'raw_prefix_payload_sha256':sha(prefix),'raw_tail_payload_sha256':sha(tail_bytes),
   'raw_rows_checked':len(begin)+len(end),'blocks_fully_read':nb,
   'independent_reduction_comparisons_passed':True,
   'full_summary_mean_reconstructed_from_all_block_means_and_actual_tail':reconstructed.tolist(),
   'limitation':'No complete raw min/max/change-count or raw checksum recomputation; bootstrap intervals inspected but not regenerated.'})

receipt=load(ROOT/'gauss_worm_screen/analysis/development/FIX_RECEIPT.json')
old=read(ROOT/'gauss_worm_screen/analysis/development/analyze_gauss_worm_screen_attempt01.py')
assert sha(old)==receipt['before_sha256']
assert sha(read(ROOT/'analyze_gauss_worm_screen.py'))==receipt['after_sha256']
read(ROOT/'gauss_worm_screen/analysis/development/SCREEN_ANALYSIS_attempt01.json')
read(ROOT/'gauss_worm_screen/analysis/development/ANALYSIS_attempt01.log')
for path,item in identities.items():assert sha(Path(path).read_bytes())==item['sha256'],path
result={'scope':'Post-seal source and compact-data comparison; no production rerun or complete raw-data verification.',
 'source_identities':identities,'cases':rows,'raw_total_bytes':raw_total_bytes,
 'raw_window_bytes_read':raw_window_bytes,'compact_block_bytes_read':compact_block_bytes,
 'exact_precomparison_check_source_sha256':sha((HERE/'independent_check.py').read_bytes()),
 'followup_diff_is_only_two_declared_lines':True,'all_checks_passed':True}
(HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'cases_checked':len(rows),'all_checks_passed':True,'sources_authenticated':len(identities),
 'raw_total_bytes':raw_total_bytes,'raw_window_bytes_read':raw_window_bytes,
 'compact_block_bytes_read':compact_block_bytes,'full_raw_hashes_recomputed':0,
 'production_executions':0,'bootstrap_reexecutions':0},indent=2))
