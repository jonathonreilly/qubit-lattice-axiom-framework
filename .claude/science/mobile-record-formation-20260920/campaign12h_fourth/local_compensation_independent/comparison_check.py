#!/usr/bin/env python3
"""New post-PRE controls for author additions; only own builders are imported."""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
import json,time
import numpy as np
import sympy as sp
from model import *
from finite_spin_check import cycle_states
base=Path(__file__).resolve().parent;D4=base.parent

def plus(v,w,scale=1):
 out=defaultdict(complex,v)
 for s,a in w.items():out[s]+=scale*a
 return {s:a for s,a in out.items() if a}

def moment_polynomial(v):
 out=defaultdict(int)
 for (q,E),a in v.items():
  assert complex(a).imag==0 and a==int(complex(a).real)
  for (q2,E2),b in v.items():
   if q!=q2:continue
   assert complex(b).imag==0 and b==int(complex(b).real)
   out[tuple(x-y for x,y in zip(E,E2))]+=int(complex(a).real)*int(complex(b).real)
 return dict(out)

def all_mark_control():
 edges=CUBE_EDGES;A=CUBE_A;zero=(0,)*12;q0=tuple(int(x in A) for x in range(8));seed=(q0,zero)
 rows=[];marked={};aggregate_polys=[]
 for first_coh in [False,True]:
  for second_coh in [False,True]:
   total=defaultdict(int);nonzero=0;firstnorm=0
   for e in range(12):
    for sign in [None] if first_coh else [-1,1]:
     v=effective_birth(seed,e,sign,A,edges)
     n=4 if first_coh else 2
     assert moment_polynomial(v)=={zero:n};firstnorm+=n
     g=defaultdict(int)
     for f in range(12):
      for charge in [None] if second_coh else [-1,1]:
       out=apply_paths(v,lambda s:effective_birth(s,f,charge,A,edges).items())
       if out:nonzero+=1
       for shift,amp in moment_polynomial(out).items():g[shift]+=amp;total[shift]+=amp
     assert g[zero]==8*n and len(g)==3
     loops={s for s in g if s!=zero}
     assert all(g[s]==n for s in loops) and len(loops)==2
     if not second_coh:marked[(first_coh,edges[e],sign)]=(n,loops)
   assert firstnorm==48 and total[zero]==384 and len(total)==13
   assert all(v==8 for s,v in total.items() if s!=zero)
   aggregate_polys.append(dict(total))
   rows.append({'coherent_first':first_coh,'coherent_second':second_coh,'first_total':firstnorm,'two_mark_zero_flux_norm_squared':total[zero],'small_time_population8_coefficient_over_kappa_squared':total[zero]//2,'nonzero_two_mark_channels':nonzero})
 assert all(g==aggregate_polys[0] for g in aggregate_polys)
 authored=json.loads((D4/'local_compensation_author/LOCAL_COMPENSATION_CONTROLS.json').read_text())['actual_two_birth_controls']
 for a,b in zip(authored,rows):
  assert a['summed_two_birth_norm_squared']==b['two_mark_zero_flux_norm_squared']
  assert a['nonzero_two_mark_channels']==b['nonzero_two_mark_channels']
 authored_marks=json.loads((D4/'local_compensation_author/MECHANISM_CONTROLS.json').read_text())['all_first_mark_exact_rotor_rate_polynomials']
 assert len(authored_marks)==len(marked)==36
 for r in authored_marks:
  key=(r['coherent_first'],tuple(r['first_edge']),None if r['coherent_first'] else r['first_signs'][0]);n,loops=marked[key]
  p=r['normalized_second_rate_over_kappa'];assert n==r['first_Gram'] and tuple(p['loop']) in loops
  assert p['identity']==8 and p['loop_coefficient']==p['adjoint_coefficient']==1
 return {'all_instrument_combinations':rows,'all_36_author_first_mark_polynomials_independently_matched':True,'total_Gram_terms':[{'shift':s,'coefficient':v} for s,v in sorted(aggregate_polys[0].items())],'total_Gram_identity':'384 I + 8 sum_six_faces(W_p+W_p^dagger)','coefficient_bounds_over_kappa_squared':[144,240]}

def sum_squares_control():
 A=frozenset((0,2));edges,states=cycle_states(4,A,1);ix={s:i for i,s in enumerate(states)};d=len(states)
 Fs=[];hs=[];W=sp.zeros(d)
 for a in sorted(A):
  F=sp.zeros(d)
  for col,s in enumerate(states):
   for out,amp in F_paths(s,a,edges,1):
    assert amp==1;F[ix[out],col]+=1
  h=sp.diag(*[int(s[0][a]==0) for s in states]);W+=h;Fs.append(F);hs.append(h)
  assert F*F==sp.zeros(d) and h*F==F and F*h==sp.zeros(d)
 for a in range(2):
  for c in range(2):
   if a!=c:assert Fs[a]*Fs[c]==Fs[c]*Fs[a] and hs[a]*Fs[c]==Fs[c]*hs[a]
 eps=sp.Rational(2,5);I=sp.eye(d);J=I
 for F in Fs:J=J*(I+eps*F)
 P=sp.diag(*[int(all(s[0][a] for a in A)) for s in states])
 H=W-eps*sum((F+F.T for F in Fs),sp.zeros(d))+eps**2*sum((F.T*F for F in Fs),sp.zeros(d))
 squares=sum(((h-eps*F).T*(h-eps*F) for h,F in zip(hs,Fs)),sp.zeros(d))
 assert H==squares and P*J*P==P and H*J*P==sp.zeros(d)
 for h,F in zip(hs,Fs):assert (h-eps*F)*J==J*h
 assert J.det()==1
 p_rank=P.rank();kernel=d-H.rank();assert p_rank==kernel==9
 return {'geometry':'complete physical four-cycle, spin 1, total charge 2, populations 2 and 4','dimension':d,'epsilon':str(eps),'sum_of_squares_exact':True,'full_similarity_constraint_identity_exact':True,'dressing_determinant':str(J.det()),'P_rank':p_rank,'exact_H_kernel_dimension':kernel,'all_physical_P_vectors_checked':True}

def general_graph_control():
 n=9;A=frozenset((0,2,5,8));edges=tuple(sorted(tuple(sorted(e)) for e in [(0,1),(0,3),(0,4),(2,1),(2,3),(2,4),(2,6),(5,4),(5,6),(8,7)]))
 q0=tuple(int(x in A) for x in range(n));seed=(q0,(0,)*len(edges));v0={seed:1}
 def T(v,w):
  out={}
  for a in A:
   for adj in [False,True]:
    term=apply_paths(v,lambda s:F_paths(s,a,edges,adjoint=adj))
    out=plus(out,{s:x for s,x in term.items() if sum(s[0][c]==0 for c in A)==w},-1)
  return out
 def M(v):return T(T(v,1),0)
 def C(v):
  out={}
  for a in A:
   gated={s:x for s,x in v.items() if gate(s[0],a,A,edges)}
   term=apply_paths(apply_paths(gated,lambda s:F_paths(s,a,edges)),lambda s:F_paths(s,a,edges,adjoint=True))
   out=plus(out,term)
  return out
 def canonical(v):
  out=M(M(v));out=plus(out,M(C(v)),-.5);out=plus(out,C(M(v)),-.5);out=plus(out,T(C(T(v,1)),0))
  z=v
  for w in [1,2,1,0]:z=T(z,w)
  return plus(out,z,-.5)
 direct=canonical(v0);expected={};scalar=0;squares=0
 for a,c in combinations(sorted(A),2):
  common=set(neighbors(a,edges)).intersection(neighbors(c,edges))
  if not common:continue
  scalar-=2*(len(neighbors(a,edges))*len(neighbors(c,edges))-len(common))
  for b,d in combinations(sorted(common),2):
   squares+=1;cycle=[a,b,c,d];E=[0]*len(edges)
   for x,y in zip(cycle,cycle[1:]+cycle[:1]):E[edges.index(tuple(sorted((x,y))))]+=1 if x<y else -1
   for sign in [-1,1]:expected[(q0,tuple(sign*x for x in E))]=-2
 expected[seed]=scalar
 assert direct==expected and scalar==-40 and squares==4
 old_scalar=sum(len(neighbors(a,edges))**2 for a in A)+sum(len(neighbors(b,edges))*(len(neighbors(b,edges))-1) for b in range(n) if b not in A)
 z=v0
 for w in [1,2,1,0]:z=T(z,w)
 old=plus(M(M(v0)),z,-.5)
 assert old==plus(expected,v0,old_scalar-scalar) and old_scalar==42
 # New, physical post-first seeds also probe the local pair identity.
 e=edges.index((0,1));v=effective_birth(seed,e,1,A,edges);local={}
 for a,c in combinations(sorted(A),2):
  if not set(neighbors(a,edges)).intersection(neighbors(c,edges)):continue
  term=v
  for center,adj in [(a,False),(c,False),(c,True),(a,True)]:term=apply_paths(term,lambda s,center=center,adj=adj:F_paths(s,center,edges,adjoint=adj))
  local=plus(local,term,-2)
 assert canonical(v)==local
 return {'vertices':n,'A':sorted(A),'edges':edges,'scope':'Irregular disconnected graph; one A pair has three common neighbors and another has two','square_count':squares,'compensated_scalar':scalar,'original_scalar':old_scalar,'exact_initial_operator_action_terms':len(direct),'canonical_and_cycle_formula_exact':True,'post_first_local_pair_identity_exact':True}

def detuning_control():
 A=CUBE_A;edges=CUBE_EDGES;q0=tuple(int(x in A) for x in range(8));first=effective_birth((q0,(0,)*12),0,1,A,edges);seed=sorted(first)[0]
 out={}
 for a in A:
  term=apply_paths(apply_paths({seed:1},lambda s:F_paths(s,a,edges)),lambda s:F_paths(s,a,edges,adjoint=True))
  out=plus(out,term)
 mean=out.get(seed,0).real;norm=sum(abs(a)**2 for a in out.values());variance=norm-mean**2
 assert gauss(*seed,A,edges) and variance>0
 return {'state':'One physical basis component of the actual first (0,1), plus-at-zero output','q':seed[0],'E':seed[1],'mean_M':mean,'norm_squared_Mpsi':norm,'variance_M':variance,'interpretation':'M is non-scalar already on a permitted fixed-N physical block. A fixed fractional compensation error therefore violates the stated all-state uniform-at-zero criterion.'}

def main():
 started=time.perf_counter()
 return {'scope':'Post-source independent additions; PRE controls are unchanged. No author builder imported or run.','sum_of_squares':sum_squares_control(),'all_mark_second_event':all_mark_control(),'general_graph_first_sector':general_graph_control(),'detuning_non_scalar_countercontrol':detuning_control(),'elapsed_seconds':time.perf_counter()-started}
if __name__=='__main__':print(json.dumps(main(),indent=2))
