"""Exact charge-diagonal and coherent sign-matrix check from saved physical paths."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
x=json.loads((HERE/'DECISIVE_RESULTS.json').read_text())['physical_charge_control']
branches=x['actual_birth_branches'];n=x['n'];M=n+2;count=len(branches)
assert count==10
coherent=[[F(1,count) for j in range(count)] for i in range(count)]
mixed=[[F(1,count) if branches[i]['sigma']==branches[j]['sigma'] else F(0) for j in range(count)] for i in range(count)]
assert [coherent[i][i] for i in range(count)]==[mixed[i][i] for i in range(count)]
def purity(rho):return sum(rho[i][j]*rho[j][i] for i in range(count) for j in range(count))
assert purity(coherent)==1 and purity(mixed)==F(1,2)
cross=[(i,j) for i in range(count) for j in range(count) if branches[i]['sigma']!=branches[j]['sigma']]
assert len(cross)==50 and all(coherent[i][j]==F(1,10) and mixed[i][j]==0 for i,j in cross)
def diag_moments(rho):
 m=sum(rho[i][i]*branches[i]['total_B_charge'] for i in range(count))
 s=sum(rho[i][i]*branches[i]['total_B_charge']**2 for i in range(count))
 return [str(m),str(s),str(s-m*m)]
assert diag_moments(coherent)==diag_moments(mixed)==['1','2','1']
uniform=x['uniform_minus_Gauss_rows'];a=tuple(x['emitter']);b=tuple(x['marked_B'])
pa=F(sum(tuple(r['minus_site'])==a for r in uniform),M)
pb=F(sum(tuple(r['minus_site'])==b for r in uniform),M)
assert pa==pb==F(1,M)
# These are physical diagonal-projector bounds, independent of field dressing.
trace_bounds={'each_fixed_resolved_sign_vs_uniform_minus':str(1-pa),
              'fixed_edge_coherent_vs_uniform_minus':str(1-pa-pb)}
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'physical_paths_input_sha256':hashlib.sha256((HERE/'DECISIVE_RESULTS.json').read_bytes()).hexdigest(),
 'coherent_density_matrix':[[str(v) for v in row] for row in coherent],
 'equal_resolved_sign_mixture':[[str(v) for v in row] for row in mixed],
 'purities':[str(purity(coherent)),str(purity(mixed))],
 'cross_sign_entries_preserved_by_coherent_output':len(cross),
 'coherent_and_mixture_B_moments':diag_moments(coherent),
 'uniform_minus_projector_probabilities':{'minus_at_a':str(pa),'minus_at_b':str(pb)},
 'trace_distance_lower_bounds':trace_bounds,
 'scope':'Field-electric branch vectors are distinct physical basis states at the declared finite-electric input. Equal diagonal charge laws do not justify replacing coherent output by the sign mixture. Bounds use D_tr=one half trace norm.'}
with (HERE/'CHARGE_COHERENCE_RESULTS.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
