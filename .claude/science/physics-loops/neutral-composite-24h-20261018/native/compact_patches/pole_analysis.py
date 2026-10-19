from pathlib import Path
import json
import numpy as np
P=Path(__file__).resolve().parent;r=json.loads((P/'exact_cube_poles.json').read_text());E=np.array(r['lowest_energies'])-r['ground_energy'];W=np.array(r['normalized_probe_weights']);groups=[]
for i,e in enumerate(E):
 if not groups or abs(e-groups[-1]['gap'])>1e-8:groups.append(dict(gap=float(e),indices=[]))
 groups[-1]['indices'].append(i)
for g in groups:
 ids=g['indices'];g['captured_normalized_source_weights']=W[:,ids].sum(axis=1).tolist();g['max_residual']=max(r['eigen_residuals'][i] for i in ids);g['touches_eigensolver_cutoff']=max(ids)==len(E)-1
visible=[g for g in groups if g['gap']>1e-8 and max(g['captured_normalized_source_weights'])>1e-8]
assert visible and visible[0]['max_residual']<1e-8
out=dict(first_returned_source_visible_group=visible[0],groups=groups,scope='Weights summed over returned eigenvectors at each energy; full degeneracy completeness not certified. Finite selected-sector periodic cube, no internal-size or scalar-irrep certificate.')
(P/'pole_analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(out['first_returned_source_visible_group'])
