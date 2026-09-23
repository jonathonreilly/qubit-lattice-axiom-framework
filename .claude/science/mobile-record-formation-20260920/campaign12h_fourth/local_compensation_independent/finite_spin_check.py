#!/usr/bin/env python3
"""Complete physical sectors, finite-spin compensation and full P recycling."""
from itertools import product
import json,time
import numpy as np
import scipy
from scipy.sparse import csc_matrix,eye,kron
from scipy.sparse.linalg import expm_multiply
from model import *


def path_states(n,A):
 out=[]
 for q in product((-1,0,1),repeat=n):
  if sum(q)!=len(A):continue
  E=[];flux=0
  for v in range(n-1):
   flux+=q[v]-int(v in A);E.append(flux)
  assert flux+q[-1]-int(n-1 in A)==0
  out.append((q,tuple(E)))
 return out

def cycle_states(n,A,S):
 edges=tuple((i,i+1) for i in range(n-1))+((0,n-1),)
 out=[]
 for E in product(range(-S,S+1),repeat=n):
  div=[0]*n
  for (x,y),v in zip(edges,E):div[x]+=v;div[y]-=v
  q=tuple(div[x]+int(x in A) for x in range(n))
  if all(abs(c)<=1 for c in q):out.append((q,E))
 return edges,out

def construct(states,A,edges,S):
 n=len(states);ix={s:i for i,s in enumerate(states)};zero=np.zeros((n,n))
 Fs=[]
 for a in sorted(A):
  F=zero.copy()
  for col,s in enumerate(states):
   for out,amp in F_paths(s,a,edges,S):
    assert out in ix and gauss(*out,A,edges)
    F[ix[out],col]+=amp
  Fs.append(F)
 T=-sum(F+F.T for F in Fs)
 W=np.array([sum(s[0][a]==0 for a in A) for s in states])
 N=np.array([sum(c!=0 for c in s[0]) for s in states])
 C=zero.copy();electric=np.zeros(n)
 for a,F in zip(sorted(A),Fs):
  M=F.T@F;D=np.diag(M)
  Dinfty=np.array([int(s[0][a]!=0)*sum(s[0][b]==0 for b in neighbors(a,edges)) for s in states])
  Q=np.array([int(gate(s[0],a,A,edges)) for s in states])
  term=M+np.diag(Dinfty-D)
  assert np.max(abs(term*Q[None,:]-term*Q[:,None]),initial=0)<1e-12
  C+=term*Q[None,:]
  for i,(q,E) in enumerate(states):
   if not q[a]:continue
   for b in neighbors(a,edges):
    if q[b]:continue
    e=edges.index(tuple(sorted((a,b))));direction=1 if a<b else -1
    electric[i]+=E[e]**2-direction*q[a]*E[e]
 assert np.max(abs(C-C.T),initial=0)<1e-12
 assert np.max(abs(C*(W[:,None]-W[None,:])),initial=0)<1e-12
 assert np.max(abs(C*(N[:,None]-N[None,:])),initial=0)<1e-12
 P=np.where(W==0)[0];Q1=np.where(W==1)[0];Q2=np.where(W==2)[0]
 hop=T[np.ix_(Q1,P)];M=hop.T@hop;Z=T[np.ix_(Q2,Q1)]@hop
 C0=C[np.ix_(P,P)];C1=C[np.ix_(Q1,Q1)]
 K2=C0-M;expected=np.zeros_like(K2) if S is None else np.diag(electric[P]/(S*(S+1)))
 identity_error=float(np.max(abs(K2-expected),initial=0));assert identity_error<1e-12
 K4=M@M-.5*Z.T@Z+hop.T@C1@hop-.5*(M@C0+C0@M)
 jumps=[]
 for e in range(len(edges)):
  for charge in [-1,1]:
   J=zero.copy()
   for col,s in enumerate(states):
    for out,amp in birth_paths(s,e,charge,edges,S):
     assert out in ix and gauss(*out,A,edges)
     J[ix[out],col]+=amp
   assert np.max(abs(J*(W[:,None]-W[None,:]+1)),initial=0)<1e-12
   assert np.max(abs(J*(N[:,None]-N[None,:]-2)),initial=0)<1e-12
   jumps.append(-J[np.ix_(P,Q1)]@hop)
 return {'states':states,'P':P,'K2':K2,'K4':K4,'jumps':jumps,'electric':electric[P],'identity_error':identity_error,'C_norm':float(np.linalg.norm(C,2)),'C_min_eigenvalue':float(np.linalg.eigvalsh(C)[0]),'C1_norm':float(np.linalg.norm(C1)),'grade_counts':{str(k):int(sum(W==k)) for k in sorted(set(W))},'number_counts':{str(k):int(sum(N[P]==k)) for k in sorted(set(N[P]))}}

def generator(H,bs,kappa):
 n=len(H);I=eye(n,format='csc');H=csc_matrix(H)
 L=-1j*(kron(I,H)-kron(H.T,I))
 for b in bs:
  b=csc_matrix(b);loss=b.getH()@b
  L+=kappa*(kron(b.conjugate(),b)-.5*kron(I,loss)-.5*kron(loss.T,I))
 return L.tocsc()

def main():
 start=time.perf_counter();cyclic=[]
 for S in [1,2]:
  A=frozenset((0,2));edges,states=cycle_states(4,A,S);m=construct(states,A,edges,S)
  cyclic.append({'S':S,'complete_physical_dimension':len(states),'P_dimension':len(m['P']),'grade_counts':m['grade_counts'],'P_number_counts':m['number_counts'],'K2_diagonal_identity_max_error':m['identity_error'],'C_operator_norm':m['C_norm'],'C_min_eigenvalue':m['C_min_eigenvalue'],'C1_norm':m['C1_norm']})
 A=frozenset((0,2,4,6));edges=tuple((i,i+1) for i in range(7));states=path_states(8,A)
 rotor=construct(states,A,edges,None);assert len(states)==266 and len(rotor['P'])==65
 assert np.max(abs(rotor['K2']))<1e-12
 delta=.7;K=.4;kappa=.2;times=[0,.2,.6]
 init=(tuple(int(v in A) for v in range(8)),(0,)*7)
 ip=list(rotor['P']).index(states.index(init));rho0=np.zeros((65,65),complex);rho0[ip,ip]=1
 H=K*np.diag(rotor['electric'])+delta*rotor['K4'];L=generator(H,rotor['jumps'],kappa)
 target=[expm_multiply(t*L,rho0.reshape(-1,order='F')).reshape((65,65),order='F') for t in times]
 rows=[]
 for S in [4,8,16,32]:
  finite=construct(states,A,edges,S);HS=K*np.diag(finite['electric'])+delta*finite['K4'];LS=generator(HS,finite['jumps'],kappa)
  errors=[]
  for t,reference in zip(times,target):
   rho=expm_multiply(t*LS,rho0.reshape(-1,order='F')).reshape((65,65),order='F')
   assert abs(np.trace(rho)-1)<2e-12 and np.linalg.eigvalsh((rho+rho.conj().T)/2)[0]>-2e-12
   errors.append(float(sum(abs(np.linalg.eigvalsh((rho-reference+rho.conj().T-reference.conj().T)/2)))))
  rows.append({'S':S,'epsilon':float(np.sqrt(delta/(K*S*(S+1)))),'K2_diagonal_identity_max_error':finite['identity_error'],'C1_norm':finite['C1_norm'],'H4_operator_norm_error':float(np.linalg.norm(finite['K4']-rotor['K4'],2)),'maximum_jump_operator_norm_error':max(float(np.linalg.norm(b-c,2)) for b,c in zip(finite['jumps'],rotor['jumps'])),'full_target_density_trace_errors':errors})
 assert all(rows[i+1]['full_target_density_trace_errors'][-1]<rows[i]['full_target_density_trace_errors'][-1] for i in range(3))
 final=target[-1];N=np.array([sum(c!=0 for c in states[i][0]) for i in rotor['P']]);pop={str(n):float(np.trace(final[np.ix_(N==n,N==n)]).real) for n in [4,6,8]}
 assert pop['8']>0
 return {'environment':{'numpy':np.__version__,'scipy':scipy.__version__},'complete_cyclic_controls':cyclic,'eight_site_tree_recycling_control':{'complete_physical_dimension':len(states),'P_dimension':65,'grade_counts':rotor['grade_counts'],'P_number_counts':rotor['number_counts'],'maximum_physical_link_absolute_value':max(abs(e) for q,E in states for e in E),'rotor_C1_norm':rotor['C1_norm'],'parameters':{'delta':delta,'K':K,'kappa':kappa,'times':times},'spin_rows':rows,'rotor_number_probabilities_at_final_time':pop},'scope':'Finite floating full-target checks with all reachable numbers; not a microscopic-generator replay or proof of convergence rate. Analytic identities and general target theorem supply the proof.','elapsed_seconds':time.perf_counter()-start}

if __name__=='__main__':print(json.dumps(main(),indent=2))
