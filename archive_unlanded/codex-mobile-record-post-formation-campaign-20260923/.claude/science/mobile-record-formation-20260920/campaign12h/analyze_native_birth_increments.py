#!/usr/bin/env python3
"""Exploratory paired birth-increment analysis, added after the fixed screen.

This subtracts each trajectory's own initial quadrupole. It does not replace
the original preselected full-field comparisons or change any simulation.
"""
from pathlib import Path
import json,hashlib
import numpy as np
H=Path(__file__).resolve().parent;D=H/'admissibility_wave_screen'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
original=json.loads((D/'CONTINUUM_ANALYSIS.json').read_text());rows=[]
for item in original:
 name=item['case'];raw=D/(name+'.npz');assert sha(raw)==item['identities']['raw_sha256']
 with np.load(raw) as f:
  fields=f['fields']/np.sqrt(item['side']**3)
  delta=(fields[:,-1,0,4]-fields[:,0,0,4]).real
  # At j=0 the signed birth content has mean zero, independent of its total count.
  density_increment=(fields[:,-1,0,0]-fields[:,0,0,0]).real
  initial=fields[:,0,0,4].real;final=fields[:,-1,0,4].real
 seed=int.from_bytes(hashlib.sha256(name.encode()).digest()[:4],'little')
 rng=np.random.default_rng(np.random.SeedSequence([2026092233,seed]))
 weights=rng.multinomial(len(delta),np.full(len(delta),1/len(delta)),4000)/len(delta)
 draws=weights@delta;ci=np.quantile(draws,[.025,.975])
 with np.load(D/(name+'_continuum_analysis.npz')) as a:target=float((a['target'][-1,0,4]-a['target'][0,0,4]).real)
 variance_pred=(2/3)*density_increment.mean()/(item['side']**3)
 row=dict(case=name,j=item['j'],side=item['side'],trajectories=len(delta),raw_sha256=sha(raw),
   initial_quadrupole_mean=float(initial.mean()),final_quadrupole_mean=float(final.mean()),
   paired_birth_quadrupole_mean=float(delta.mean()),pointwise_95_bootstrap_interval=ci.tolist(),
   paired_sampling_standard_error=float(delta.std(ddof=1)/np.sqrt(len(delta))),
   target_continuum_increment=target,
   uniform_birth_variance_control=None if item['j'] else dict(predicted_per_path_variance=float(variance_pred),observed_per_path_variance=float(delta.var(ddof=1))),
   base_seed=2026092233,name_seed=seed)
 rows.append(row);print(json.dumps(row),flush=True)
result=dict(source_sha256=sha(Path(__file__)),analysis_status='Exploratory analysis chosen after viewing the fixed screen results. All nine cases retained; no simulation parameters or original targets changed.',
 scope='Paired final-minus-initial global quadrupole increments. Intervals are pointwise Monte Carlo sampling uncertainty; no multiplicity, finite-size or physical inference is included.',cases=rows)
(H/'NATIVE_BIRTH_INCREMENT_ANALYSIS.json').write_text(json.dumps(result,indent=2)+'\n')
