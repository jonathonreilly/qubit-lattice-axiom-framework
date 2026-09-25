"""Genuinely read-only: read source/evidence, recompute arithmetic, print JSON.

Imports no local/author scientific program and has no write/open/exec API.
This verifies all saved coefficients/certificates/charge rows. It distinguishes
own primitive cross-check evidence from a new complete primitive rerun.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product,permutations
from pathlib import Path
import hashlib,json,math
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
pins=json.loads((HERE/'SOURCE_PINS.json').read_text())
for item in pins['sources']:
 p=HERE/item['frozen_path'];assert sha(p.read_bytes())==item['sha256'] and p.stat().st_size==item['bytes']
 if item['origin'].startswith('/'):
  assert Path(item['origin']).read_bytes()==p.read_bytes()
executions=[]
for tag in ['freeze','exploration','supersolution','decisive','charge_coherence']:
 r=json.loads((HERE/f'{tag}.execution.json').read_text())
 assert sha(Path(r['command'][1]).read_bytes())==r['source_sha256']
 for stream in ['stdout','stderr']:
  b=(HERE/f'{tag}.{stream}.txt').read_bytes();assert sha(b)==r[f'{stream}_sha256'] and len(b)==r[f'{stream}_bytes']
 assert r['exit_code']==0 and r['stderr_bytes']==0
 executions.append({'tag':tag,'source_sha256':r['source_sha256'],'exit_code':0,'stderr_bytes':0})
data=json.loads((HERE/'DECISIVE_RESULTS.json').read_text());cert=data['supersolution']
assert data['source_sha256']==sha((HERE/'decisive_threshold_and_charge_control.py').read_bytes())
assert data['helper_sha256']==sha((HERE/'primitive_kernel.py').read_bytes())
assert data['search_artifact_sha256']==sha((HERE/'SUPERSOLUTION_EXPLORATION.json').read_bytes())
single={tuple(k):v for k,v in data['single_algebraic_kernel']['complete_column']}
steps=[tuple(s if j==axis else 0 for j in range(3)) for axis in range(3) for s in [-1,1]]
walk2=Counter(tuple(a+b for a,b in zip(u,v)) for u in steps for v in steps)
P=walk2.copy();P[(0,0,0)]-=6
P={k:v for k,v in P.items() if v};square=Counter()
for a,u in P.items():
 for b,v in P.items():square[tuple(x+y for x,y in zip(a,b))]+=u*v
polynomial=Counter({k:2*v for k,v in square.items()})
for k,v in P.items():polynomial[k]+=188*v
polynomial[(0,0,0)]-=1392
assert single=={k:v for k,v in polynomial.items() if v}
assert sum(single.values())==6048 and cert['threshold']==12096
assert 2*36**2+164*36-2448==6048
assert 2*0**2+164*0-2448==-2448
DEN=cert['denominator'];corr={tuple(k):v for k,v in cert['corrections_numerators']}
h=lambda t:DEN+corr.get(tuple(t),0)
assert DEN==10**9 and min([DEN]+[DEN+v for v in corr.values()])==934634416
raw=json.loads((HERE/'UNWRAPPED_PRIMITIVE_COLUMNS.json').read_text())
assert len(raw)==len(cert['complete_unwrapped_type_rows'])==37
expected=sorted({tuple(sorted(t)) for t in product(range(11),repeat=3) if 0<sum(t)<=10 and sum(t)%2==0})
assert [tuple(r['separation']) for r in raw]==expected
row_min=[];entries=0;type_rows=[]
for rawrow,row in zip(raw,cert['complete_unwrapped_type_rows']):
 assert rawrow['separation']==row['separation']
 assert sha(json.dumps(rawrow['complete_column'],separators=(',',':')).encode())==row['raw_column_sha256']
 agg=Counter();keys=set()
 for points,v in rawrow['complete_column']:
  key=tuple(map(tuple,points));assert key not in keys and key[0]!=key[1];keys.add(key)
  assert type(v) is int
  if key!=tuple(sorted(((0,0,0),tuple(row['separation'])))):assert v>0
  typ=tuple(sorted(abs(a-b) for a,b in zip(*points)));agg[typ]+=v;entries+=1
 assert [[list(k),v] for k,v in sorted(agg.items()) if v]==row['grouped_column']
 residual=sum(v*h(k) for k,v in agg.items())-12096*h(row['separation'])
 assert residual==row['residual_numerator']<0
 assert sum(agg.values())==row['row_sum']
 row_min.append(residual)
 type_rows.append({'separation':row['separation'],'residual_numerator':residual,'complete_column_entries':len(keys)})
assert max(row_min)==-607772==cert['maximum_unwrapped_residual_numerator']
# Finite quotients: exact weights, all entries, shift positivity, rational
# Collatz intervals, constant vector averages and strict threshold bounds.
finite=[];total_finite_entries=0
for table in data['finite_tori']:
 L,n=table['L'],table['n'];assert n==L**3//2
 classes=Counter(tuple(sorted(min(v,(-v)%L) for v in x)) for x in product(range(L),repeat=3) if sum(x)%2==0 and any(x))
 types=[tuple(t) for t in table['types']];assert types==sorted(classes)
 assert [classes[t] for t in types]==table['relative_class_weights']
 rows=[dict(row) for row in table['matrix_rows']];v=table['positive_integer_test_vector'];shift=table['nonnegative_shift']
 assert len(v)==len(rows)==len(types) and all(type(x) is int and x>0 for x in v)
 ratios=[];residuals=[]
 for i,row in enumerate(rows):
  assert len(row)==len(table['matrix_rows'][i])
  for j,x in row.items():
   assert type(x) is int and x+(shift if i==j else 0)>=0
   assert classes[types[i]]*x==classes[types[j]]*rows[j].get(i,0)
   total_finite_entries+=1
  ratios.append(F(sum(x*v[j] for j,x in row.items()),v[i]))
  residuals.append(sum(x*h(types[j]) for j,x in row.items())-12096*h(types[i]))
 lo,hi=min(ratios),max(ratios);assert [str(lo),str(hi)]==table['exact_Perron_interval'] and hi<12096
 assert table['supersolution_residual_numerators']==residuals
 assert table['same_local_supersolution_valid']==(max(residuals)<=0)
 average=F(sum(classes[types[i]]*sum(row.values()) for i,row in enumerate(rows)),n-1)
 assert str(average)==table['constant_trial_exact'] and average==12096-F(1548,n-1)
 finite.append({'L':L,'dimension':len(rows),'exact_interval':[str(lo),str(hi)],'constant_trial':str(average),'shared_h_max_residual':max(residuals)})
# The parent near-row count has a strictly negative total defect; compute its
# exact sum from the new primitive output, not the parent's numeric table.
def orbit(t):
 return {tuple(s*x for s,x in zip(signs,p)) for p in set(permutations(t)) for signs in product([-1,1],repeat=3)}
defect=sum(len(orbit(tuple(r['separation'])))*(r['row_sum']-12096) for r in cert['complete_unwrapped_type_rows'] if sum(r['separation'])<=4)
assert defect==-1548

# Independently assemble the incidence matrix for every saved physical charge
# row, using only the finite graph and sparse flows; no state-builder import.
q=data['physical_charge_control'];L=q['L'];vertices=list(product(range(L),repeat=3));ix={x:i for i,x in enumerate(vertices)}
A={x for x in vertices if sum(x)%2==0};B=set(vertices)-A
def nearby(x):return sorted({tuple((a+b)%L for a,b in zip(x,u)) for u in steps})
edges=[(a,b) for a in sorted(A) for b in nearby(a)]
base=[int(x in A) for x in vertices];n=len(A);M=n+2
allrows=q['actual_birth_branches']+q['uniform_minus_Gauss_rows'];charge_count=0
for row in allrows:
 charge=row['charge_word'];flow=row.get('electric_shift',row.get('one_integer_Gauss_flow'))
 divergence=[0]*len(vertices)
 for e,v in flow:
  a,b=edges[e];divergence[ix[a]]+=v;divergence[ix[b]]-=v
 assert divergence==[v-b for v,b in zip(charge,base)]
 assert sum(charge)==n and sum(v!=0 for v in charge)==M and sum(v==-1 for v in charge)==1
 assert all(charge[ix[a]]!=0 for a in A)
 assert sum(charge[ix[b]] for b in B)==row['total_B_charge']
 assert sum(charge[ix[a]]-1 for a in A)==row['total_A_defect']
 charge_count+=1
for sign in [-1,1]:
 rows=[r for r in q['actual_birth_branches'] if r['sigma']==sign];assert len(rows)==5
 for row in rows:
  emitter=tuple(q['emitter']);marked=tuple(q['marked_B']);moved=tuple(row['moved_neighbor'])
  assert moved!=marked and moved in nearby(emitter) and marked in nearby(emitter)
  assert row['charge_word'][ix[emitter]]==sign and row['charge_word'][ix[marked]]==-sign and row['charge_word'][ix[moved]]==1
  assert row['total_B_charge']==1-sign
u=q['uniform_minus_Gauss_rows'];assert len(u)==M
assert F(sum(r['total_B_charge'] for r in u),M)==F(2*n,M)
assert F(sum(r['total_B_charge']**2 for r in u),M)-F(2*n,M)**2==F(8*n,M*M)
coh=json.loads((HERE/'CHARGE_COHERENCE_RESULTS.json').read_text())
assert coh['physical_paths_input_sha256']==sha((HERE/'DECISIVE_RESULTS.json').read_bytes())
assert coh['source_sha256']==sha((HERE/'charge_coherence_control.py').read_bytes())
rho=[[F(v) for v in row] for row in coh['coherent_density_matrix']];mix=[[F(v) for v in row] for row in coh['equal_resolved_sign_mixture']]
assert len(rho)==len(mix)==10 and all(len(row)==10 for row in rho+mix)
assert all(rho[i][j]==F(1,10) for i in range(10) for j in range(10))
for i in range(10):
 for j in range(10):assert mix[i][j]==(F(1,10) if q['actual_birth_branches'][i]['sigma']==q['actual_birth_branches'][j]['sigma'] else 0)
assert sum(rho[i][j]*rho[j][i] for i in range(10) for j in range(10))==1
assert sum(mix[i][j]*mix[j][i] for i in range(10) for j in range(10))==F(1,2)
assert sum(rho[i][j]!=mix[i][j] for i in range(10) for j in range(10))==50
assert coh['trace_distance_lower_bounds']=={'each_fixed_resolved_sign_vs_uniform_minus':str(F(M-1,M)),'fixed_edge_coherent_vs_uniform_minus':str(F(M-2,M))}

# Explicit discriminators: omitted factor two changes the kernel/threshold;
# dropping a saved positive contact coefficient breaks a row equality; a wrong
# charge sign violates the saved Gauss vector, and dephasing loses 50 entries.
clean=dict((tuple(k),v) for k,v in cert['complete_unwrapped_type_rows'][0]['grouped_column'])
damaged=clean.copy();chosen_key=next(k for k,v in clean.items() if v>0);damaged[chosen_key]-=1
sample=q['actual_birth_branches'][0];bad=sample['charge_word'].copy();bad[ix[tuple(q['emitter'])]]*=-1
sample_divergence=[0]*len(vertices)
for edge,value in sample['electric_shift']:
 a,b=edges[edge];sample_divergence[ix[a]]+=value;sample_divergence[ix[b]]-=value
discriminators={'half_Gram_factor_rejected':{k:v//2 for k,v in single.items()}!=dict(polynomial),
 'one_contact_entry_drop_breaks_saved_raw_grouping':damaged!=clean,
 'wrong_emitter_charge_breaks_Gauss':sample_divergence!=[v-b for v,b in zip(bad,base)],
 'dephasing_changes_50_cross_sign_entries':sum(rho[i][j]!=mix[i][j] for i in range(10) for j in range(10))==50}
assert all(discriminators.values())
report={'source_pins_verified':len(pins['sources']),'execution_bindings':executions,'single_kernel_polynomial':'K=2P^2+188P-1392 I =2 A^4+164 A^2-2448 I on B, P=A^2-6 I',
 'single_spectral_interval':[-2448,6048],'separated_upper_threshold':12096,
 'unwrapped_complete_entries':entries,'all_unwrapped_rows':type_rows,'finite_quotients':finite,'all_finite_entries':total_finite_entries,
 'summed_near_row_defect':defect,'physical_Gauss_charge_rows':charge_count,'coherent_charge_result_sha256':sha((HERE/'CHARGE_COHERENCE_RESULTS.json').read_bytes()),
 'discriminators':discriminators,'own_scientific_programs_imported_or_executed':False,'filesystem_mutation_by_verifier':False,
 'scope':'Complete stored-certificate arithmetic and independent polynomial/Gauss reconstruction. The primary also compared 13 near-shell columns using separate ordered four-hop enumeration. No author outputs imported.','all_checks_completed':True}
print(json.dumps(report,indent=2))
