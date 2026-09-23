#!/usr/bin/env python3
"""Bounded post-PRE comparison.  Imports only the frozen independent builder."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import hashlib,json,time
import numpy as np
import sympy as sp
from cube_point_check import EDGES,TREE,CHORDS,A_SITES,state_space,legal_hops,physical_field,chord_part,add,ZERO
HERE=Path(__file__).resolve().parent;AUTHOR=HERE.parent/'cube_point_spectrum_author'
PRE_HASH='8c29f173d14a983a0c6273560712c32685d48429d7482c5dcff152e426d05c0a'
AUTHOR_HASH='b99a0a0b243c9ecfaade581acbb2450d4e3d53d95967bb7096ed9388558f2665'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def authenticate(path,expected):
 assert sha(path)==expected
 s=json.loads(path.read_text());counts={}
 for group in ['sources','artifacts']:
  for row in s[group]:
   q=Path(row['path']);assert len(q.read_bytes())==row['bytes'] and sha(q)==row['sha256']
  counts[group]=len(s[group])
 return s,counts
pre,pre_counts=authenticate(HERE/'PRE_COMPARISON_SEAL.json',PRE_HASH)
seal,author_counts=authenticate(AUTHOR/'AUTHOR_SEAL.json',AUTHOR_HASH)
saved=json.loads((AUTHOR/'CUBE_POINT_SPECTRUM_RESULTS.json').read_text())
controls=json.loads((AUTHOR/'CUBE_CERTIFICATE_CONTROLS.json').read_text())
assert saved['source_sha256']==sha(AUTHOR/'cube_fiber_polynomials.py')
assert controls['source_sha256']==sha(AUTHOR/'cube_certificate_check.py')
assert controls['input_sha256']==sha(AUTHOR/'CUBE_POINT_SPECTRUM_RESULTS.json')
P,Q=state_space(0),state_space(1);qi={q:i for i,q in enumerate(Q)}
assert saved['edges']==[list(e) for e in EDGES]
assert saved['tree']==[list(e) for e in EDGES if e in TREE]
assert saved['chords']==[list(e) for e in CHORDS]
assert saved['P_words']==[list(q) for q in sorted(P)]
assert saved['W1_words']==[list(q) for q in sorted(Q)]
physical_checks=0
for q in P:
 for out,d,_ in legal_hops(q):
  df=chord_part(d)
  for f in [ZERO]+[tuple(int(k==j) for k in range(5)) for j in range(5)]:
   assert add(physical_field(q,f),d)==physical_field(out,add(f,df));physical_checks+=1
assert physical_checks==controls['physical_hop_gauss_checks']==1296
assert controls['legal_P_to_Q_hops']==216
assert controls['tree_incidence_determinant']=='1'
x=sp.Symbol('x');rows=[];polys=[];cumulative=None
for number,entry in enumerate(saved['exact_rows']):
 turns=entry['quarter_turns'];A=sp.zeros(len(Q),len(P))
 for col,q in enumerate(P):
  for out,d,amp in legal_hops(q):
   A[qi[out],col]+=amp*sp.I**sum(a*b for a,b in zip(turns,chord_part(d)))
 H=-A.conjugate().T*A
 assert H==H.conjugate().T
 poly=sp.Poly(H.charpoly(x).as_expr(),x,domain=sp.ZZ)
 assert [str(c) for c in poly.all_coeffs()]==entry['characteristic_coefficients']
 assert sp.Poly(sp.sympify(entry['characteristic_polynomial_factorization']),x)==poly
 polys.append(poly);cumulative=poly if cumulative is None else sp.gcd(cumulative,poly).monic()
 assert sp.expand(cumulative.as_expr()-sp.sympify(entry['cumulative_gcd']))==0
 assert cumulative.degree()==entry['gcd_degree']
 item={'quarter_turns':turns,'all_37_characteristic_coefficients_equal':True,
       'factorization_and_gcd_equal':True,'gcd_degree':cumulative.degree(),
       'trace_H':str(sp.trace(H)),'trace_H_squared':str(sp.expand(sp.trace(H*H)))}
 if number<3:
  ctl=controls['rows'][number];assert ctl['quarter_turns']==turns
  for value,key in [(-2,'p_minus2'),(-5,'p_minus5'),(-6,'p_minus6')]:
   assert str(poly.eval(value))==ctl[key];item[key]=str(poly.eval(value))
  assert sp.expand(cumulative.as_expr()-sp.sympify(ctl['gcd']))==0
  assert sp.expand(sp.trace(H)-sp.sympify(ctl['H_trace']))==0
  assert sp.expand(sp.trace(H*H)-sp.sympify(ctl['H2_trace']))==0
  assert all(poly.eval(v)!=0 for v in [-2,-5,-6])==ctl['determinant_nonzero_surviving_roots']
 rows.append(item)
assert saved['final_gcd']=='1' and saved['final_gcd_degree']==0
assert sp.gcd(sp.gcd(polys[0],polys[1]),polys[2]).as_expr()==1
assert sp.gcd(polys[0],polys[4]).as_expr()==1
own=json.loads((HERE/'CUBE_POINT_RESULTS.json').read_text())
assert own['fibers'][0]['charpoly_coefficients']==saved['exact_rows'][0]['characteristic_coefficients']
assert own['fibers'][1]['charpoly_coefficients']==saved['exact_rows'][4]['characteristic_coefficients']
numeric=[]
for entry in saved['numeric_fibers']:
 theta=entry['chord_angles'];A=np.zeros((len(Q),len(P)),complex)
 for col,q in enumerate(P):
  for out,d,amp in legal_hops(q):A[qi[out],col]+=amp*np.exp(1j*np.dot(theta,chord_part(d)))
 H=-A.conj().T@A;ev=np.linalg.eigvalsh(H)
 eig_error=float(np.max(np.abs(ev-entry['H2_eigenvalues'])))
 distance=float(np.min(np.abs(ev+6)));distance_error=abs(distance-entry['distance_to_diagonal_energy_minus6'])
 determinant=float(np.linalg.det(H+6*np.eye(36)).real)
 det_scaled_error=abs(determinant-entry['determinant_H2_plus6'])/(1+abs(determinant))
 assert eig_error<1e-12 and distance_error<1e-12 and det_scaled_error<1e-10
 numeric.append({'chord_angles':theta,'maximum_eigenvalue_error':eig_error,'minus6_distance_error':distance_error,'determinant_scaled_error':det_scaled_error})
# Parse every JSON object in the complete author stdout, including its repeated rows.
decoder=json.JSONDecoder();remaining=(AUTHOR/'PROBE.stdout.log').read_text();objects=[]
while remaining.strip():
 remaining=remaining.lstrip();obj,end=decoder.raw_decode(remaining);objects.append(obj);remaining=remaining[end:]
assert len(objects)==6 and objects[:-1]==saved['exact_rows'] and objects[-1]==saved
assert (AUTHOR/'CERTIFICATE.stdout.log').read_bytes()==(AUTHOR/'CUBE_CERTIFICATE_CONTROLS.json').read_bytes()
assert not (AUTHOR/'PROBE.stderr.log').read_bytes() and not (AUTHOR/'CERTIFICATE.stderr.log').read_bytes()
receipts=[]
for name,script in [('PROBE_RUN_RECEIPT.json','cube_fiber_polynomials.py'),('CERTIFICATE_RUN_RECEIPT.json','cube_certificate_check.py')]:
 r=json.loads((AUTHOR/name).read_text());assert r['exit_code']==0 and r['source_sha256']==sha(AUTHOR/script)
 receipts.append({'receipt':name,'source_and_exit_verified':True,'has_command_array':'command' in r})
print(json.dumps({'pre_sha256':PRE_HASH,'pre_bindings_preserved':pre_counts,
 'author_seal_sha256':AUTHOR_HASH,'author_bindings_verified':author_counts,
 'new_builder_used':'Frozen independent cube_point_check.py; no author builder imported or executed.',
 'complete_matter_bases_and_tree_chords_equal':True,'physical_gauss_checks_rebuilt':physical_checks,
 'exact_fibers':rows,'numeric_fibers':numeric,
 'author_three_fiber_gcd':'1','independent_two_fiber_gcd':'1',
 'independent_PRE_polynomials_match_author_zero_and_all_i_controls':True,
 'full_author_stdout_json_objects_verified':len(objects),'author_receipts':receipts,
 'required_mathematical_corrections':[],'scope':'P-space physical point spectrum. No new conclusion about dynamics, other sectors, or other geometries.'},indent=2))
