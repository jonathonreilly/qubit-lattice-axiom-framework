"""Exact finite supplied-kernel identities; no quadrature error estimate or broad exclusion."""
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json,sys
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['archive/chirality_exact_review_2026_10_18/MANIFEST.json', 'archive/chirality_exact_review_2026_10_18/original-recovery.tar.gz', 'docs/CHIRALITY_CONSTRUCTIVE_FINITE_ALGEBRA_NOTE_2026-10-18.md', 'docs/CHIRALITY_FINITE_REFLECTION_KERNELS_NOTE_2026-10-18.md', 'docs/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md', 'outputs/chirality_exact_review_2026_10_18/PROVENANCE.json', 'outputs/chirality_exact_review_2026_10_18/README.md', 'outputs/chirality_exact_review_2026_10_18/proofs/bare_scalar_integral.md', 'outputs/chirality_exact_review_2026_10_18/proofs/boundary_row_wilson_mode.md', 'outputs/chirality_exact_review_2026_10_18/proofs/cubic_invariant_spaces.md', 'outputs/chirality_exact_review_2026_10_18/proofs/filtered_corner_algebra.md', 'outputs/chirality_exact_review_2026_10_18/proofs/finite_reflection_kernels.md', 'outputs/chirality_exact_review_2026_10_18/proofs/free_overlap_and_rational_projectors.md', 'outputs/chirality_exact_review_2026_10_18/proofs/majorana_square_conventions.md', 'outputs/chirality_exact_review_2026_10_18/proofs/marker_su3.md', 'outputs/chirality_exact_review_2026_10_18/proofs/one_loop_covariance.md', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_count.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_labels.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/OBS3/scripts/obs3_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/OBS3/scripts/univ.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/QMC1/scripts/x2model.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/BLEAK1/b1_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/BLEAK1/b1_semi.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_tokens_z1_full.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_tokens_z1_links.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_z3.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_z3_lowmem.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/parse_lemma.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/su3common.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/K2/k2t1_free_transfer_4d.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/o12.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/t22lib.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v2_exact_witness.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v2b_exact_vector.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v3_o12_exact.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/common.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/kramers_fams.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/p6_fierz_lambda1_zero.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/pair_kramers_u1c.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/X2/x2_cert.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/X3/tx3_overlap_transfer.py.source', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']

def box(z,widths):
 n=len(widths);factor=1
 for j in range(1,n):factor*=j
 return sum((prod(e)*max(F(0),z+sum((s*w for s,w in zip(e,widths)),F(0))/2)**(n-1)/factor for e in product([-1,1],repeat=n)),F(0))

def congruence(matrix):
 # Symmetric Schur complements: A = L D L^T, with exact rational entries.
 n=len(matrix);a=[r[:] for r in matrix];L=[[F(i==j) for j in range(n)] for i in range(n)];piv=[]
 for k in range(n):
  d=a[k][k]
  if not d:raise ArithmeticError('Zero pivot requires a different congruence; not silently classified')
  piv.append(d)
  for i in range(k+1,n):L[i][k]=a[i][k]/d
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]-=L[i][k]*d*L[j][k]
 reconstructed=[[sum((L[i][k]*piv[k]*L[j][k] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]
 if reconstructed!=matrix:raise AssertionError('Exact LDL reconstruction failed')
 return piv

def strip_kernel(f1,f2,d):
 cuts={-d,d}
 for z in [-3*d,-d,d,3*d]:
  cuts.add(max(-d,min(d,f1+z)));cuts.add(max(-d,min(d,-f2+z)))
 cuts=sorted(cuts);total=F(0)
 for lo,hi in zip(cuts,cuts[1:]):
  samples=[lo+(hi-lo)*j/4 for j in range(5)]
  values=[box(f1-e,[2*d]*3)*box(f2+e,[2*d]*3) for e in samples]
  total+=(hi-lo)*sum((w*v for w,v in zip([7,32,12,32,7],values)),F(0))/90
 return total

def main():
 if sys.flags.optimize:raise RuntimeError('Assertions must remain enabled')
 rows=[]
 for d in [F(3,10),F(3,5),F(3,4)]:
  cfg=list(product([F(0),d/12],[-11*d/12,F(0),11*d/12]));c=[F(1),F(-9,5),F(1),F(-1),F(9,5),F(-1)]
  K=[[box(s-t,[2*d-abs(x-y)]*2+[2*d]*2) for y,t in cfg] for x,s in cfg]
  q=sum((c[i]*K[i][j]*c[j] for i in range(6) for j in range(6)),F(0));piv=congruence(K)
  assert q==-d**3/100 and sum(x>0 for x in piv)==5 and sum(x<0 for x in piv)==1
  for x,s in cfg:
   links=[x,F(0),s+x,-s,F(0),F(0),F(0),F(0)]
   a,b,c_,e,f,g,h,i=links;plaquettes=[a+h-c_-f,b+f-e-h,c_+i-a-g,e+g-b-i]
   assert plaquettes==[-s,s,s,-s] and max(map(abs,plaquettes))<=11*d/12
  rows.append({'delta':str(d),'matrix':[[str(x) for x in r] for r in K],'LDL_pivots':list(map(str,piv)),'quadratic_value_without_Haar':str(q),'Haar_factor':'(2*pi)^-3','inertia':[5,1,0]})
  print('[PASS] T22 exact fixture delta='+str(d)+' quadratic='+str(q)+' inertia=5,1,0',flush=True)
 print('T22_RESULT',json.dumps(rows),flush=True)
 d=F(3,5);axis=[F(-11,20),F(-11,60),F(11,60),F(11,20)];cfg=list(product(axis,repeat=2));K=[[strip_kernel(x-u,y-v,d) for u,v in cfg] for x,y in cfg];piv=congruence(K)
 assert sum(x>0 for x in piv)==15 and sum(x<0 for x in piv)==1
 assert all(max(map(abs,p))<=d-F(1,20) for p in cfg)
 print('[PASS] O12 exact delta=3/5 sixteen-point inertia=15,1,0',flush=True)
 print('O12_RESULT',json.dumps({'delta':str(d),'configurations':[[str(x) for x in p] for p in cfg],'matrix':[[str(x) for x in r] for r in K],'LDL_pivots':list(map(str,piv)),'inertia':[15,1,0],'Haar_factor':'(2*pi)^-5'}),flush=True)
 print('per_element: Exact rational box-convolution entries and piecewise polynomial integrals are evaluated, without floating quadrature tolerances.')
 print('per_site: All six T22 configurations and sixteen O12 plaquette pairs satisfy the explicit strict admissibility margins.')
 print('per_mode: Exact congruence reconstruction certifies the stated finite matrix inertias; no arbitrary geometry spectrum is inferred.')
 print('per_block: The specified six-entry quadratic vector and both complete matrices are printed with their positive Haar normalizations.')
 print('lattice_wide: Only the supplied finite two-slice geometries and stated delta domains are covered; other weights and infinite volume are untested.')
 print('Count unit: three exact T22 fixtures and one exact O12 fixture, each including all its identities.')
 print('TOTAL: PASS=4 FAIL=0')
def _deadline(signum, frame):
    raise TimeoutError('Declared scientific runtime cap exceeded; partial stdout retained')

if __name__=='__main__':
    import signal
    import sys
    if sys.flags.optimize:
        raise RuntimeError('Assertions must remain enabled')
    signal.signal(signal.SIGALRM, _deadline)
    signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC)
    try:
        main()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
