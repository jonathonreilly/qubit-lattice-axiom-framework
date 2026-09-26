"""Adaptive global/local covariance comparison; no phase or coverage claim."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import io
import json
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'gauss_worm_z1_followup'/'winding_analysis'
OUT.mkdir(exist_ok=True)
sha = lambda b: hashlib.sha256(b).hexdigest()
manifest_path = ROOT/'gauss_worm_z1_followup'/'analysis'/'RAW_IDENTITIES.json'
manifest = json.loads(manifest_path.read_bytes())
source_hash = sha(Path(__file__).read_bytes())
seal = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'plan_sha256': sha((ROOT/'GAUSS_WINDING_STIFFNESS_FOLLOWUP_PLAN.md').read_bytes()),
    'source_sha256': source_hash,
    'raw_manifest_sha256': sha(manifest_path.read_bytes()),
    'block_size': 1024,
    'bootstrap_replicates': 2000,
    'seed': 202609211100,
    'new_analysis_adaptive': True,
}
(OUT/'PRE_ANALYSIS_SEAL.json').write_text(json.dumps(seal, indent=2)+'\n')
cases = []
for case_id, record in enumerate(sorted(manifest['files'], key=lambda r:r['path'])):
    path = Path(record['path'])
    raw = path.read_bytes()
    assert len(raw) == record['bytes'] and sha(raw) == record['sha256']
    meta_path = path.with_suffix('.json')
    meta_raw = meta_path.read_bytes()
    assert sha(meta_raw) == record['metadata_sha256']
    meta = json.loads(meta_raw)
    L = meta['L']; V = L**3
    a = np.loadtxt(io.StringIO(raw.decode()), delimiter=',', skiprows=1)
    assert a.shape == (meta['samples'],10) and np.isfinite(a).all()
    assert np.array_equal(a[:,0],np.arange(len(a)))
    assert np.all(np.diff(a[:,1])>0)
    assert np.max(np.abs(a[:,7:10]/L-np.rint(a[:,7:10]/L))) < 1e-9
    y = np.column_stack([a[:,2:7], a[:,7:10]**2/V, a[:,7:10]/np.sqrt(V)])
    count = len(y)//1024
    b = y[:count*1024].reshape(count,1024,11).mean(axis=1)
    block_path = OUT/(path.stem+'_blocks.csv')
    np.savetxt(block_path,b,delimiter=',',header='rho,S_x1,S_x2,S_xy1,S_xy2,Fx2_per_V,Fy2_per_V,Fz2_per_V,Fx_per_sqrtV,Fy_per_sqrtV,Fz_per_sqrtV',comments='')
    # First five columns reproduce the earlier full compact reduction.
    old = np.loadtxt(ROOT/'gauss_worm_z1_followup'/'analysis'/(path.stem+'_blocks.csv'),delimiter=',',skiprows=1)
    old_grouped = old[:count*8,1:6].reshape(count,8,5).mean(axis=1)
    assert np.allclose(b[:,:5],old_grouped,rtol=1e-11,atol=1e-12)
    local = b[:,1:5].mean(axis=1)
    global_ = b[:,5:8].mean(axis=1)
    pair = np.column_stack([local,global_])
    mean = pair.mean(axis=0)
    estimate = mean[1]/mean[0]
    rng = np.random.default_rng(202609211100+case_id)
    draws = pair[rng.integers(0,count,size=(2000,count))].mean(axis=1)
    ratios = draws[:,1]/draws[:,0]
    interval = np.quantile(ratios,[.025,.975]).tolist() if count>=16 else None
    def lag(x):
        u=x[:-1];v=x[1:]
        if min(np.std(u),np.std(v))<=1e-13:return None
        return float(np.corrcoef(u,v)[0,1])
    lags = [lag(pair[:,i]) for i in range(2)]
    half = count//2
    # Quantized winding benchmark, separate from inference about this chain.
    cutoff = int(np.ceil(10*np.sqrt(L*mean[0])))+10
    w = np.arange(-cutoff,cutoff+1,dtype=float)
    weights = np.exp(-w*w/(2*L*mean[0]))
    correction = float((weights*w*w).sum()/weights.sum()/(L*mean[0]))
    flags = []
    if count<16:flags.append('fewer_than_16_complete_blocks')
    if any(x is not None and abs(x)>.2 for x in lags):flags.append('material_lag1_block_dependence')
    result = {
        'tag':path.stem,'L':L,'initialization':meta['initialization'],
        'raw_sha256_recomputed':record['sha256'],'samples':len(y),
        'blocks':count,'discarded_tail':len(y)-1024*count,
        'local_four_mode_average':float(mean[0]),
        'global_three_flux_variance_average':float(mean[1]),
        'global_over_local':float(estimate),'descriptive_interval':interval,
        'individual_flux_second_moments_per_V':b[:,5:8].mean(axis=0).tolist(),
        'individual_flux_means_per_sqrtV':b[:,8:11].mean(axis=0).tolist(),
        'lag1_local_global':lags,
        'first_half_local_global':pair[:half].mean(axis=0).tolist(),
        'last_half_local_global':pair[-half:].mean(axis=0).tolist(),
        'quantized_gaussian_variance_over_continuum':correction,
        'gaussian_winding_cutoff':cutoff,'flags':flags,
        'blocks_sha256':sha(block_path.read_bytes()),
        'earlier_spectral_block_reduction_agrees':True,
    }
    cases.append(result)
    print(path.stem,'blocks',count,'global/local',estimate,'interval',interval,'flags',flags,flush=True)
assert len(cases)==8
output = {
    'created_utc':datetime.now(timezone.utc).isoformat(),
    'preanalysis_seal_sha256':sha((OUT/'PRE_ANALYSIS_SEAL.json').read_bytes()),
    'source_sha256':source_hash,'cases':cases,
    'raw_bytes_rehashed':sum(r['bytes'] for r in manifest['files']),
    'scope':'Adaptive descriptive global/local covariance check. Supplied Gaussian benchmark, not derived effective action. No quantitative mixing, coverage, infinite-volume phase, quantum-vacuum or formation-state result.',
}
(OUT/'WINDING_ANALYSIS.json').write_text(json.dumps(output,indent=2,allow_nan=False)+'\n')
