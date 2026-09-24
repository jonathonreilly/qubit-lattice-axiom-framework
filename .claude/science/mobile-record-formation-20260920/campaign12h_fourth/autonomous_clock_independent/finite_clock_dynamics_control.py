#!/usr/bin/env python3
"""Direct autonomous finite-Hamiltonian control, with independent reductions.
No supplied campaign implementation is imported. The non-phase-covariant jump
sqrt(gamma)|+><0| tests the free-H counterphase on full input channel matrices.
"""
from pathlib import Path
from itertools import product
import json,time
import numpy as np
from scipy.linalg import expm
from scipy.sparse import coo_matrix,diags,bmat,eye,kron
from scipy.sparse.linalg import expm_multiply
from scipy.stats import binom
HERE=Path(__file__).resolve().parent
T=1.2;omega=.83;gamma=.7
H=np.diag([0.,omega]).astype(complex)
Lop=np.sqrt(gamma)*np.array([[1,0],[1,0]],complex)/np.sqrt(2)
G=-1j*(np.kron(np.eye(2),H)-np.kron(H.T,np.eye(2)))
GG=Lop.conj().T@Lop
G+=np.kron(Lop.conj(),Lop)-.5*(np.kron(np.eye(2),GG)+np.kron(GG.T,np.eye(2)))
def trace_norm_hermitian(A):return float(np.sum(np.abs(np.linalg.eigvalsh((A+A.conj().T)/2))))
def choi_from_super(S):
 J=np.zeros((4,4),complex)
 for r in range(2):
  for q in range(2):
   block=S[:,r+2*q].reshape(2,2,order='F')
   for a in range(2):
    for b in range(2):J[2*a+r,2*b+q]=block[a,b]
 return J
def choi_from_columns(A):
 # A has axes output system, discarded environment, input system.
 return np.einsum('aer,bes->arbs',A,A.conj()).reshape(4,4)
def rotate_choi(J,elapsed):
 p=np.repeat(np.exp(-1j*np.array([0.,omega])*elapsed),2)
 return p[:,None]*J*p[None,:].conj()
def local_collision(dt):
 assert gamma*dt<=.5+1e-14
 z=np.zeros(4,complex);z[0]=1
 w=np.zeros(4,complex);w[1]=w[3]=1/np.sqrt(2)
 c=np.sqrt(1-gamma*dt);ss=np.sqrt(gamma*dt)
 R=np.eye(4)+(c-1)*(np.outer(z,z)+np.outer(w,w))+ss*(np.outer(w,z)-np.outer(z,w))
 U=np.repeat(np.exp(-1j*np.array([0.,omega])*dt),2)[:,None]*R
 assert np.linalg.norm(U.conj().T@U-np.eye(4))<2e-14
 ks=[U[np.ix_([f,2+f],[0,2])] for f in (0,1)]
 expected=[expm(-1j*dt*H)@np.diag([np.sqrt(1-gamma*dt),1]),expm(-1j*dt*H)@Lop*np.sqrt(dt)]
 assert max(np.linalg.norm(a-b) for a,b in zip(ks,expected))<2e-14
 return U,ks

def model(N,width):
 B=width+2;flags=2**N;words=tuple(product(range(2),range(B),range(flags)))
 index={q:i for i,q in enumerate(words)};D=len(words)
 labels=np.array([system+n for system,n,f in words]);energies=omega*labels
 grid=(2*T/np.pi)*np.arcsin(np.sqrt(np.arange(N+1)/N));durations=np.diff(grid)
 nu=np.pi/T
 hc=np.eye(N+1)*nu*N/2
 gates=[];corrected=[];ideal_prefix=[np.eye(4,dtype=complex)]
 for bit,dt in enumerate(durations):
  U,ks=local_collision(dt);rr=[];cc=[];values=[]
  for col,(system,n,f) in enumerate(words):
   m=system+n
   if not 1<=m<=width+1:rr.append(col);cc.append(col);values.append(1);continue
   inp=2*system+((f>>bit)&1)
   for out in range(4):
    amp=U[out,inp]
    if abs(amp)<1e-15:continue
    sout,fout=divmod(out,2);dest=index[sout,m-sout,(f&~(1<<bit))|(fout<<bit)]
    rr.append(dest);cc.append(col);values.append(amp)
  V=coo_matrix((values,(rr,cc)),shape=(D,D)).tocsr()
  unit=V.conj().T@V-eye(D,format='csr')
  assert not unit.nnz or max(abs(unit.data))<4e-14
  comm=diags(energies)@V-V@diags(energies)
  assert not comm.nnz or max(abs(comm.data))<2e-14
  gates.append(V);corrected.append(diags(np.exp(1j*dt*energies))@V)
  step=sum(np.kron(k.conj(),k) for k in ks);ideal_prefix.append(step@ideal_prefix[-1])
 for j in range(1,N+1):hc[j,j-1]=hc[j-1,j]=nu*np.sqrt(j*(N+1-j))/2
 blocks=[[None]*(N+1) for _ in range(N+1)]
 for j in range(N+1):blocks[j][j]=eye(D,format='csr')*nu*N/2
 for j,W in enumerate(corrected,1):
  coeff=nu*np.sqrt(j*(N+1-j))/2
  blocks[j][j-1]=coeff*W;blocks[j-1][j]=coeff*W.conj().T
 program=bmat(blocks,format='csr');qfull=np.tile(energies,N+1)
 Htot=program+diags(qfull)
 commute=Htot@diags(qfull)-diags(qfull)@Htot
 assert not commute.nnz or max(abs(commute.data))<1e-12
 beta=np.zeros(B);beta[1:width+1]=np.sqrt(2/(width+1))*np.sin(np.pi*np.arange(1,width+1)/(width+1))
 work_input=np.zeros((D,2),complex)
 for system in (0,1):
  for n,amp in enumerate(beta):work_input[index[system,n,0],system]=amp
 assert np.linalg.norm(work_input.conj().T@work_input-np.eye(2))<2e-14
 actual_prefix=[work_input]
 for V in gates:actual_prefix.append(V@actual_prefix[-1])
 prefix_choi=[choi_from_columns(a.reshape(2,B*flags,2)) for a in actual_prefix]
 initial=np.zeros(((N+1)*D,2),complex);initial[:D]=work_input
 times=np.linspace(0,T,17)
 trajectory=expm_multiply(-1j*Htot,initial,start=0,stop=T,num=len(times),endpoint=True,traceA=-1j*float(np.real(Htot.diagonal().sum())))
 test_input=np.array([np.sqrt(.4),np.sqrt(.6)*np.exp(.37j)])
 expected_free=omega*(.6+(width+1)/2)
 eta=min(2.,8*np.sin(np.pi/(2*(width+1))))
 c_bound=7*gamma**2+4*omega*gamma
 uniform_bound=min(2.,eta+(T*T*c_bound+np.sqrt(2)*gamma*T)/np.sqrt(N))
 rows=[]
 for t,embed in zip(times,trajectory):
  arr=embed.reshape(N+1,2,B,flags,2).transpose(1,0,2,3,4).reshape(2,(N+1)*B*flags,2)
  full=choi_from_columns(arr)
  p=np.sin(np.pi*t/(2*T))**2
  weights=binom.pmf(np.arange(N+1),N,p)
  mixture=sum(prob*rotate_choi(J,t-tj) for prob,J,tj in zip(weights,prefix_choi,grid))
  residual=np.max(abs(full-mixture))
  assert residual<4e-11
  assert np.linalg.norm(embed.conj().T@embed-np.eye(2))<4e-11
  target=choi_from_super(expm(t*G));norm=trace_norm_hermitian(full-target)
  assert norm/2<=uniform_bound+4e-11
  vector=embed@test_input
  free_energy=float(np.vdot(vector,qfull*vector).real)
  clock_energy=float(np.vdot(vector.reshape(N+1,D),hc@vector.reshape(N+1,D)).real)
  programmed_energy=float(np.vdot(vector,program@vector).real)
  assert abs(free_energy-expected_free)<2e-10
  assert abs(programmed_energy-nu*N/2)<2e-10
  assert clock_energy>=-2e-10
  nvals=np.array([n for system,n,f in words]);svals=np.array([system for system,n,f in words])
  system_energy=float(np.vdot(vector,np.tile(omega*svals,N+1)*vector).real)
  battery_energy=float(np.vdot(vector,np.tile(omega*nvals,N+1)*vector).real)
  rows.append({'t':float(t),'full_H_versus_history_channel_max_entry_residual':float(residual),'reference_input_trace_error':norm/2,'diamond_upper_from_unnormalized_Choi':min(2.,norm),'system_mean_energy':system_energy,'battery_mean_energy':battery_energy,'free_energy_balance_residual':abs(free_energy-expected_free),'bare_positive_clock_mean':clock_energy,'interaction_mean':programmed_energy-clock_energy,'clock_plus_interaction_conservation_residual':abs(programmed_energy-nu*N/2)})
 return {'N':N,'battery_width':width,'clock_dimension':N+1,'battery_dimension':B,'blank_pure_flags':N,'total_flag_dimension':flags,'full_dimension':(N+1)*D,'time_grid':grid.tolist(),'max_collision_duration':float(max(durations)),'prepared_clock_mean':nu*N/2,'prepared_clock_variance':nu**2*N/4,'interaction_norm_upper_bound':nu*N,'prepared_battery_mean':omega*(width+1)/2,'analytic_uniform_channel_bound':uniform_bound,'max_full_H_history_residual':max(r['full_H_versus_history_channel_max_entry_residual'] for r in rows),'max_reference_input_trace_error':max(r['reference_input_trace_error'] for r in rows),'rows':rows}
start=time.monotonic()
results=[model(N,width) for N,width in [(2,5),(4,9),(6,17)]]
packet={'scientific_role':'Direct evolution under one finite time-independent Hamiltonian; synthetic non-phase-covariant two-level GKLS control, not an imported campaign model','parameters':{'T':T,'omega':omega,'gamma':gamma,'jump':'sqrt(gamma)|+><0|'},'cases':results,'wall_seconds':time.monotonic()-start,'limits':'Finite examples corroborate the exact construction. The analytic theorem supplies arbitrary-input/reference and uniform-time scope; no multitime or event-time instrument inferred.'}
(HERE/'FINITE_CLOCK_DYNAMICS_RESULTS.json').write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps({'parameters':packet['parameters'],'wall_seconds':packet['wall_seconds'],'summaries':[{k:r[k] for k in ('N','battery_width','full_dimension','max_full_H_history_residual','max_reference_input_trace_error','prepared_clock_mean','interaction_norm_upper_bound')} for r in results]},indent=2))
