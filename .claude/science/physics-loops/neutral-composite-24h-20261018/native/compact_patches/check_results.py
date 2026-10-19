"""Author consistency checks; no independent review or size-selection verdict."""
from pathlib import Path
import json
import numpy as np
P=Path(__file__).resolve().parent
load=lambda f:json.loads((P/f).read_text())
assert max(x['max_error'] for x in load('mpo_check.json'))==0
assert load('moment_control.json')['max_error']<1e-10
assert load('fusion_control.json')['all_pass'] and load('volume_algebra.json')['all_pass']
rows=load('sheet_fixed_characters.json')['rows'];poles=[]
for r in rows:
 weights=np.array(r['lowest_eigen_probe_overlaps']);inds=[i for i in range(1,4) if max(weights[:,i])>1e-8 and r['lowest_eigen_residuals'][i]<1e-8]
 assert inds
 k=inds[0];gap=r['lowest_sector_energies'][k]-r['ground_energy']
 last=r['levels'][-1];visible=[i for i,en in enumerate(last['energies']) if max(row[i] for row in last['probe_overlaps'])>1e-8 and last['residuals'][i]<1e-4]
 assert visible and min(abs(last['energies'][i]-gap) for i in visible)<1e-7
 poles.append(dict(shape=r['shape'],gap=gap,eigen_residual=r['lowest_eigen_residuals'][k],normalized_source_weights=weights[:,k].tolist()))
assert abs(poles[1]['gap']-poles[2]['gap'])<1e-9
for f in ['patch_response_32.json','boundary_response_32.json','volume_response_32.json','patch_response_128.json']:
 if not (P/f).exists():continue
 for r in load(f)['rows']:
  G=np.array(r['centered_gram']);K=np.array(r['centered_H']);Q=np.array(r['centered_H2'])
  assert max(np.max(abs(M-M.T)) for M in [G,K,Q])<1e-8
  assert np.linalg.eigvalsh(G).min()>-1e-8 and np.linalg.eigvalsh(Q).min()>-1e-6
baseline=load('patch_response_32.json')['rows'][1]['ritz_energies'][0]
dressed=load('boundary_response_32.json')['rows'][0]['ritz_energies'][0]
assert dressed<=baseline+1e-8
cube=load('exact_periodic_cube.json');pole=load('pole_analysis.json')['first_returned_source_visible_group']
assert cube['ground_residual']<1e-8 and pole['max_residual']<1e-8
assert abs(cube['raw_energies'][1]-2*cube['raw_energies'][0])<1e-8
out=dict(periodic_cube_source_visible_group=pole,sheet_source_visible_modes=poles,three_dimensional_variational_energy_reduction=baseline-dressed,scope='Dense/tensor and representation/solver checks by root; no stable finite size established; thresholds are exposed numerical diagnostics')
(P/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
