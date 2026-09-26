#!/usr/bin/env python3
"""Post-seal comparison; uses a closed rank-two exponential, no author import."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as s
import independent_check as own

OUT=Path(__file__).resolve().parent;RAW=OUT.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
pre=load(OUT/'PRE_COMPARISON_SEAL.json')
for r in pre['artifacts']:
 p=OUT/r['path'];assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256']
for r in pre['sources']:
 p=Path(r['path']);assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256']
folder=RAW/'dimer_covariant_quantum_encoding_checks';result=load(folder/'RESULTS.json');sources={}
def bind(p):sources[str(p.resolve())]={'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)}
bind(folder/'RESULTS.json')
for name,digest in result['sources_sha256'].items():assert sha(RAW/name)==digest;bind(RAW/name)
for name,group in result['groups'].items():p=folder/(name+'.json');assert load(p)==group;bind(p)
log=RAW/'DIMER_COVARIANT_QUANTUM_ENCODING_RUN.log';err=RAW/'DIMER_COVARIANT_QUANTUM_ENCODING_RUN.stderr'
assert log.read_text().splitlines()==[name+' PASS' for name in result['groups']] and not err.read_bytes();bind(log);bind(err)
q=s.Rational(1,2);r=s.Rational(1,6);la=s.Rational(1,8);lb=s.Rational(1,16);base=s.diag(q,r,r,r)
local=result['groups']['local_encoding_and_moments']
for row in local['exact_states']:
 e=s.Matrix(row['e']);b=s.Matrix(row['b']);R=own.rho(q,r,la,lb,e,b);w=R[1:,0]
 assert s.Rational(row['schur'])==q-(w.H*w)[0]/r
 assert row['means']==[str(s.simplify(s.trace(R*O))) for O in own.O]
assert local['population_tangent_rank']==6 and local['rotation_state_equalities']==336
base_np=np.array(base.tolist(),dtype=complex);ops=[np.array(x.tolist(),dtype=complex) for x in own.O]
sigma=np.array((2*(q-r)*own.J).tolist(),dtype=float);V=float(q+r)*np.eye(6)
max_value_error=0.;max_target_error=0.;row_count=0
for sequence in result['groups']['finite_quantum_fluctuations']['finite_product_Weyl_rows']:
 zs=np.asarray(sequence['z'],dtype=float);total=np.sum(zs,axis=0)
 phase=sum(zs[i]@sigma@zs[j] for i in range(len(zs)) for j in range(i+1,len(zs)))
 target=np.exp(-.5*total@V@total-.5j*phase)
 max_target_error=max(max_target_error,abs(target-complex(sequence['target_real'],sequence['target_imag'])))
 for row in sequence['rows']:
  K=row['K'];word=np.eye(4,dtype=complex)
  for z in zs:
   Z=sum((z[i]*ops[i] for i in range(6)),np.zeros((4,4),dtype=complex));length=np.linalg.norm(z)
   if length:
    angle=length/math.sqrt(K)
    E=np.eye(4)+(math.cos(angle)-1)*(Z@Z)/(length*length)+1j*math.sin(angle)*Z/length
   else:E=np.eye(4)
   word=word@E
  actual=np.trace(base_np@word)**K;recorded=complex(row['real'],row['imag'])
  error=abs(actual-recorded);max_value_error=max(max_value_error,error);row_count+=1
  assert error<3e-11 and abs(abs(actual-target)-row['absolute_error'])<3e-11
assert max_target_error<1e-14 and row_count==25
energy=result['groups']['Hamiltonian_and_derivative_escape']
for row in energy['exact_Fourier_rows']:
 Q=s.Matrix(row['Q']);C=s.I*own.cross(Q);H=s.Rational(3,7)*s.diag(C,C)
 reported={s.sympify(k):v for k,v in row['onsite_generator_energy_eigenvalues'].items()};assert reported==H.eigenvals()
 Hplus=s.diag(C*C,s.eye(3));assert {s.sympify(k):v for k,v in row['positive_potential_energy_eigenvalues'].items()}==Hplus.eigenvals()
assert energy['normalization_c']=='2/7'
answer={'created_utc':datetime.now(timezone.utc).isoformat(),'precomparison_artifacts_unchanged':len(pre['artifacts']),
 'complete_author_source_sha256':sha(RAW/'dimer_covariant_quantum_encoding_check.py'),
 'completed_groups':3,'exact_color_rows_compared':14,'finite_Weyl_rows_recomputed_with_closed_rank_two_exponential':row_count,
 'maximum_Weyl_value_discrepancy':max_value_error,'maximum_Gaussian_target_discrepancy':max_target_error,
 'exact_Hessian_spectra_compared':4,'all_embedded_and_separate_groups_identical':True,'no_author_code_executed':True}
(OUT/'AUTHOR_COMPARISON.json').write_text(json.dumps(answer,indent=2)+'\n')
(OUT/'POST_COMPARISON_SOURCES.json').write_text(json.dumps({'sources':list(sources.values())},indent=2)+'\n')
print(json.dumps(answer,indent=2))
