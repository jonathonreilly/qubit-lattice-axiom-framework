#!/usr/bin/env python3
"""Exact Gaussian normalization, archive reconstruction, and a defined-point/undefined-bootstrap control."""
from pathlib import Path
from fractions import Fraction
import importlib.util,json,sys
import numpy as np
sys.dont_write_bytecode=True
EVIDENCE=Path(__file__).resolve().parent
OUT=EVIDENCE
if len(sys.argv)==3 and sys.argv[1]=='--output':
    OUT=Path(sys.argv[2]).resolve()
    assert OUT.is_relative_to(EVIDENCE) and OUT!=EVIDENCE
    OUT.mkdir(parents=True,exist_ok=False)
elif len(sys.argv)!=1:
    raise SystemExit('usage: ancillary_controls.py [--output NEW_EVIDENCE_SUBDIRECTORY]')
elif (OUT/'ANCILLARY_RESULTS.json').exists():
    raise SystemExit('preserved results exist; use --output with a new evidence subdirectory')
spec=importlib.util.spec_from_file_location('independent_control',EVIDENCE/'independent_check.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.OUT=OUT

# For independent standard real Gaussians, E[X^2]=1 and E[X^4]=3.
# Q=(sum_{i=1}^r X_i^2)/r has E[Q^2]=(3r+r(r-1))/r^2.
ratios={}
for name,r,target in [('single_two_complex_polarizations',4,Fraction(3,2)),('three_mode_average',12,Fraction(7,6)),('three_real_windings',3,Fraction(5,3))]:
    ratio=Fraction(3*r+r*(r-1),r*r)
    assert ratio==target;ratios[name]={'independent_real_Gaussians':r,'ratio':str(ratio)}
archives=[]
for backup in sorted((EVIDENCE/'toy_runs').glob('*.original.state.txt')):
    prefix=str(backup).replace('.original.state.txt','');cert=json.loads(Path(prefix+'.verification.json').read_text())
    with np.load(prefix+'.state.npz') as a:
        arrays=[a[k] for k in ['partner','identity','births_at_site']]
        body='\n'.join(cert['ASCII_headers'])+'\n'+''.join(f'{i} {int(arrays[0][i])} {int(arrays[1][i])} {int(arrays[2][i])}\n' for i in range(len(arrays[0])))
    assert body.encode()==backup.read_bytes()
    archives.append({'prefix':prefix,'sha256':c.sha(backup),'reconstructed_ASCII_is_byte_identical':True})

# A nonzero empirical mean W does not prevent all-zero W bootstrap resamples.
# The two rows are synthetic statistical fixtures, never represented as physical runs.
folder=OUT/'synthetic_mixed_zero_winding_input';a=c.synthetic_input(folder,'baseline')
summary=json.loads((folder/'SUMMARY.json').read_text());row=summary['results'][0];name=row['name']
dp=folder/(name+'.json');vp=folder/(name+'.verification.json');rp=folder/(name+'.receipt.json')
d=json.loads(dp.read_text());v=json.loads(vp.read_text());receipt=json.loads(rp.read_text())
d['winding']=[0,0,0];v['winding_power_per_component']=0.;row['winding_power_per_component']=0.
c.write(dp,d);c.write(vp,v)
receipt['files'][dp.name]=c.sha(dp);receipt['files'][vp.name]=c.sha(vp);c.write(rp,receipt);c.write(folder/'SUMMARY.json',summary)
proc=c.logrun('synthetic_mixed_zero_winding_analysis',[sys.executable,c.SRC/'analyze_geometric_fixed_rate_followup.py',folder,OUT/'synthetic_mixed_zero_winding_analysis'],ok=1)
assert 'AssertionError' in proc.stderr
result={'conditional_Gaussian_exact_moments':ratios,'archive_reconstruction':archives,
        'mixed_zero_winding':{'empirical_mean_W_positive':True,'probability_of_zero_W_mean_in_one_two_row_bootstrap_resample':'1/4','analyzer_exit_code':proc.returncode,'failure_is_preserved':True},
        'production_outputs_read':False}
c.write(OUT/'ANCILLARY_RESULTS.json',result)
print(json.dumps(result,indent=2))
