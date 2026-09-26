"""Independent compact arithmetic and selected raw-window check; no full raw rehash."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, io, json
import numpy as np
import mpmath as mp
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent
OUT=ROOT/'gauss_worm_z1_followup/winding_analysis'
OLD=ROOT/'gauss_worm_z1_followup/analysis'
sha=lambda b:hashlib.sha256(b).hexdigest()
ident=lambda p:{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())}
sources={}
def source(p):
    sources[str(p)]=ident(p); return p
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
for rec in [pre['source'],pre['dependency']]+pre['artifacts']:
    assert ident(Path(rec['path']))==rec
source(HERE/'PRE_COMPARISON_SEAL.json')
plan=source(ROOT/'GAUSS_WINDING_STIFFNESS_FOLLOWUP_PLAN.md')
script=source(ROOT/'gauss_winding_stiffness_analysis.py')
manifest_path=source(OLD/'RAW_IDENTITIES.json'); manifest=json.loads(manifest_path.read_text())
author_seal_path=source(OUT/'PRE_ANALYSIS_SEAL.json'); seal=json.loads(author_seal_path.read_text())
results_path=source(OUT/'WINDING_ANALYSIS.json'); results=json.loads(results_path.read_text())
assert seal['plan_sha256']==ident(plan)['sha256']
assert seal['source_sha256']==results['source_sha256']==ident(script)['sha256']
assert seal['raw_manifest_sha256']==ident(manifest_path)['sha256']
assert results['preanalysis_seal_sha256']==ident(author_seal_path)['sha256']
assert (seal['block_size'],seal['bootstrap_replicates'],seal['seed'])==(1024,2000,202609211100)
assert seal['new_analysis_adaptive'] is True
records=sorted(manifest['files'],key=lambda r:r['path'])
assert len(records)==len(results['cases'])==8
cases=[]; selected_bytes=0; mp.mp.dps=90
for case_id,(rec,res) in enumerate(zip(records,results['cases'])):
    raw=Path(rec['path']); assert raw.stat().st_size==rec['bytes']
    meta_path=source(raw.with_suffix('.json')); assert ident(meta_path)['sha256']==rec['metadata_sha256']
    meta=json.loads(meta_path.read_text()); L=meta['L']; V=L**3
    assert L%2==1 and L>=7 and res['tag']==raw.stem
    bpath=source(OUT/(raw.stem+'_blocks.csv'))
    assert ident(bpath)['sha256']==res['blocks_sha256']
    b=np.loadtxt(bpath,delimiter=',',skiprows=1)
    oldpath=source(OLD/(raw.stem+'_blocks.csv'))
    old=np.loadtxt(oldpath,delimiter=',',skiprows=1)
    n=meta['samples']; nb=n//1024
    assert b.shape==(nb,11) and np.isfinite(b).all()
    assert (n,nb,n%1024)==(res['samples'],res['blocks'],res['discarded_tail'])
    np.testing.assert_allclose(b[:,:5],old[:nb*8,1:6].reshape(nb,8,5).mean(1),rtol=1e-11,atol=1e-12)
    local=b[:,1:5].sum(1)/4; glob=b[:,5:8].sum(1)/3
    pair=np.stack((local,glob),axis=1); means=pair.mean(0)
    np.testing.assert_allclose(means,[res['local_four_mode_average'],res['global_three_flux_variance_average']],rtol=1e-13)
    np.testing.assert_allclose(means[1]/means[0],res['global_over_local'],rtol=1e-13)
    np.testing.assert_allclose(b[:,5:8].mean(0),res['individual_flux_second_moments_per_V'],rtol=1e-13)
    np.testing.assert_allclose(b[:,8:11].mean(0),res['individual_flux_means_per_sqrtV'],rtol=1e-13,atol=1e-15)
    lags=[np.corrcoef(pair[:-1,j],pair[1:,j])[0,1] for j in range(2)]
    np.testing.assert_allclose(lags,res['lag1_local_global'],rtol=1e-12,atol=1e-14)
    half=nb//2
    np.testing.assert_allclose(pair[:half].mean(0),res['first_half_local_global'],rtol=1e-13)
    np.testing.assert_allclose(pair[-half:].mean(0),res['last_half_local_global'],rtol=1e-13)
    # Same declared draws, independently compute ratios with scalar dot products of multiplicities.
    rng=np.random.default_rng(seal['seed']+case_id)
    rr=[]
    for _ in range(2000):
        multiplicities=np.bincount(rng.integers(0,nb,size=nb),minlength=nb)
        rr.append(np.dot(multiplicities,glob)/np.dot(multiplicities,local))
    interval=np.quantile(rr,[.025,.975]); np.testing.assert_allclose(interval,res['descriptive_interval'],rtol=1e-13)
    flags=[]
    if nb<16: flags.append('fewer_than_16_complete_blocks')
    if any(abs(x)>.2 for x in lags):flags.append('material_lag1_block_dependence')
    assert flags==res['flags']
    # First raw block: square each Fi before averaging. Last complete block: independently selected tail.
    with raw.open('rb') as f:
        header=f.readline(); prefix=b''.join(f.readline() for _ in range(1024))
        f.seek(max(0,raw.stat().st_size-524288)); tail=f.read()
    first=np.loadtxt(io.BytesIO(prefix),delimiter=',')
    complete_tail=tail.split(b'\n',1)[1]
    last=np.loadtxt(io.BytesIO(complete_tail),delimiter=',')
    selected_bytes+=len(header)+len(prefix)+len(tail)
    assert np.array_equal(first[:,0],np.arange(1024))
    assert last[-1,0]==n-1 and np.all(np.diff(last[:,0])==1)
    cut=last[(last[:,0]>=(nb-1)*1024)&(last[:,0]<nb*1024)]
    assert cut.shape==(1024,10)
    for a,index in [(first,0),(cut,-1)]:
        assert np.max(abs(a[:,7:10]/L-np.rint(a[:,7:10]/L)))<1e-9
        vals=np.column_stack((a[:,2:7],a[:,7:10]**2/V,a[:,7:10]/np.sqrt(V))).mean(0)
        np.testing.assert_allclose(vals,b[index],rtol=2e-12,atol=2e-13)
    sigma2=mp.mpf(str(L))*mp.mpf(str(means[0])); r=mp.exp(-2*mp.pi**2*sigma2)
    upper=8*mp.pi**2*sigma2*r*(1+r)/(1-r)**3
    cutoff=int(np.ceil(10*np.sqrt(float(sigma2))))+10
    assert cutoff==res['gaussian_winding_cutoff']
    # Discrete correction is strictly below one, but at these scales double precision rounds to one.
    assert abs(res['quantized_gaussian_variance_over_continuum']-1)<1e-14
    cases.append({'tag':raw.stem,'blocks':nb,'ratio':float(means[1]/means[0]),'interval':interval.tolist(),
        'lags':lags,'flags':flags,'sigma_squared':str(sigma2),'gaussian_one_minus_ratio_upper_bound':mp.nstr(upper,20),
        'selected_prefix_bytes':len(header)+len(prefix),'selected_tail_bytes':len(tail),
        'prefix_sha256':sha(header+prefix),'tail_sha256':sha(tail),
        'first_and_last_complete_raw_blocks_agree':True,'raw_recorded_sha256_not_recomputed':rec['sha256']})
assert results['raw_bytes_rehashed']==sum(r['bytes'] for r in records)==150150494
result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'all assertions passed',
    'cases':cases,'independently_read_raw_bytes':selected_bytes,'independent_full_raw_rehash':False,
    'author_reported_full_raw_rehash_bytes':results['raw_bytes_rehashed'],'sources':list(sources.values()),
    'scope':'Full compact-table and seeded paired arithmetic; first/last raw blocks only. No simulation rerun, full raw hash, mixing or coverage claim.'}
(HERE/'COMPACT_RESULTS.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='sources'},indent=2,allow_nan=False))
