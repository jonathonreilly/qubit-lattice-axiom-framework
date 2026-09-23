#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations
import json,time
import numpy as np
from model import *


def norm2(v):return float(sum(abs(a)**2 for a in v.values()))

def main():
 start=time.perf_counter();edges=CUBE_EDGES;AA=CUBE_A
 phase0=[0]*12;phasei=[int(e in CUBE_CHORDS) for e in edges]
 rows=[]
 for pop in [4,6,8]:
  for phases in [phase0,phasei]:
   bases,M,C0,C1,H4,Hplain,Z=rotor_coefficients(8,AA,edges,pop,4,phases)
   assert np.array_equal(M,C0)
   assert np.max(abs(C1),initial=0)==0
   assert np.array_equal(H4,-.5*Z.conj().T@Z)
   assert np.max(abs(Hplain),initial=0)==0
   row={'population':pop,'phase_powers':phases,'grade_dimensions':list(map(len,bases)),'C1_norm':float(np.linalg.norm(C1)),'gated_H4_norm':float(np.linalg.norm(H4)),'ungated_H4_norm':float(np.linalg.norm(Hplain))}
   if pop==6:
    target=words(8,AA,8,4,0)
    bs=[B_matrix(bases[0],target,e,c,AA,edges,phases) for e in range(12) for c in [-1,1]]
    gamma=sum(b.conj().T@b for b in bs)
    vals=np.linalg.eigvalsh(gamma)
    row['second_loss_spectrum']=vals.tolist();row['second_loss_trace']=float(np.trace(gamma).real)
   rows.append(row)
 # Verify the local-pair formula also when distant A centers are present.
 for n,es,As,pop in [(8,tuple((i,i+1) for i in range(7)),frozenset((0,2,4,6)),4),(8,tuple((i,i+1) for i in range(7)),frozenset((0,2,4,6)),6)]:
  bases,M,C0,C1,H4,Hplain,Z=rotor_coefficients(n,As,es,pop,4,[0]*len(es))
  expected=np.zeros_like(H4)
  for a,c in combinations(sorted(As),2):
   if not set(neighbors(a,es)).intersection(neighbors(c,es)):continue
   f0=F_matrix(bases[0],bases[1],a,es,[0]*len(es))
   f1=F_matrix(bases[1],bases[2],c,es,[0]*len(es))
   fcfa=f1@f0;expected-=2*fcfa.conj().T@fcfa
  assert np.array_equal(H4,expected) and np.max(abs(Hplain),initial=0)==0
  rows.append({'graph':'eight-site path','population':pop,'C1_norm':float(np.linalg.norm(C1)),'local_pair_formula_exact':True,'ungated_H4_norm':float(np.linalg.norm(Hplain))})
 q0=tuple(int(v in AA) for v in range(8));s0=(q0,(0,)*12);v0={s0:1}
 Hout=defaultdict(complex)
 for a,c in combinations(sorted(AA),2):
  v=v0
  for center,adj in [(a,False),(c,False),(c,True),(a,True)]:
   v=apply_paths(v,lambda s,center=center,adj=adj:F_paths(s,center,edges,adjoint=adj))
  for s,amp in v.items():Hout[s]+=-2*amp
 assert Hout[s0]==-84 and len(Hout)==13
 loop_terms=[]
 for s,amp in Hout.items():
  assert s[0]==q0 and gauss(*s,AA,edges)
  if s!=s0:
   assert amp==-2 and sum(abs(x) for x in s[1])==4
   loop_terms.append(s[1])
 # A concrete pair of marked births; interference retained at full field level.
 first=edges.index((0,1));second=edges.index((4,5))
 b1=effective_birth(s0,first,1,AA,edges)
 b2b1=apply_paths(b1,lambda s:effective_birth(s,second,-1,AA,edges).items())
 assert norm2(b1)==2 and norm2(b2b1)==1 and len(b2b1)==1
 final_state=next(iter(b2b1));assert gauss(*final_state,AA,edges)
 assert final_state[0]==(1,-1,1,1,-1,1,1,1)
 coherent1=effective_birth(s0,first,None,AA,edges)
 coherent2=apply_paths(coherent1,lambda s:effective_birth(s,second,None,AA,edges).items())
 assert norm2(coherent1)==4 and norm2(coherent2)==4
 total2=[]
 for name,vec in [('resolved_first',b1),('coherent_first',coherent1)]:
  marked=[]
  for e in range(12):
   for c in [-1,1]:
    out=apply_paths(vec,lambda s,e=e,c=c:effective_birth(s,e,c,AA,edges).items())
    marked.append(norm2(out)/norm2(vec))
  total2.append({'first':name,'instantaneous_total_second_rate_over_kappa':sum(marked),'resolved_mark_rates_over_kappa':marked})
 # One initially occupied field delta produces genuine nonconstant field motion.
 mean=Hout[s0].real;variance=norm2(Hout)-mean**2
 assert variance==48
 return {'exact_gaussian_integer_fiber_controls':rows,'cube_initial_H4':{'diagonal':-84,'oriented_loop_amplitudes':[-2]*12,'integer_loop_shifts':loop_terms,'variance_on_zero_flux_delta':variance},'two_formation_witness':{'first_mark':{'edge':(0,1),'charge_at_low_endpoint':1},'second_mark':{'edge':(4,5),'charge_at_low_endpoint':-1},'first_output_norm_squared':norm2(b1),'ordered_output_norm_squared':norm2(b2b1),'final_q':final_state[0],'final_E':final_state[1],'second_mark_rate_over_kappa_given_first':norm2(b2b1)/norm2(b1),'coherent_first_norm_squared':norm2(coherent1),'coherent_ordered_norm_squared':norm2(coherent2),'total_second_rate_controls':total2},'scope':'Exact unit-rotor path and Gaussian-integer matrix controls; fiber loss spectra numerical; no all-state completion assertion','elapsed_seconds':time.perf_counter()-start}

if __name__=='__main__':print(json.dumps(main(),indent=2))
