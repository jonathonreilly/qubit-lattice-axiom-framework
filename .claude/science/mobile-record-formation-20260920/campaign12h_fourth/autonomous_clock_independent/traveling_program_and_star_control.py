#!/usr/bin/env python3
"""Independent reconstruction of the traveling program and original-star rows.
The only campaign matrix input is this worker's previously sealed local
construction. No root model, root clock helper, or PRE executable is imported.
"""
from pathlib import Path
from itertools import product
import json,math
import numpy as np
from scipy.linalg import expm
from scipy.sparse import bmat,eye,diags,block_diag,kron
from scipy.sparse.linalg import expm_multiply
from scipy.fft import dst,idst
HERE=Path(__file__).resolve().parent
SNAP=HERE/'comparison_sources'
def tn(A):return float(np.sum(np.linalg.svd(A,compute_uv=False)))
def clock_spectral(w,n,T):
 dt=T/n;theta=np.pi/(w+1);J=1/(2*dt*np.cos(theta));a=2*J*T;R=math.ceil(8*a)
 x=np.arange(-w-R,n+R+1);M=len(x);z=np.pi/(M+1)
 ev=2*J*(np.cos(z)-np.cos(z*np.arange(1,M+1)))
 chi=np.zeros(M,complex);mask=(x>=-w)&(x<0)
 chi[mask]=(1j)**x[mask]*np.sqrt(2/(w+1))*np.sin(theta*(x[mask]+w+1))
 assert abs(np.vdot(chi,chi)-1)<2e-14
 coeff=dst(chi,type=1,norm='ortho')
 def evolve(t):return idst(np.exp(-1j*t*ev)*coeff,type=1,norm='ortho')
 return x,chi,J,R,ev,evolve

def choi_columns(columns,nclock,nwork_env):
 # Work order is (system,battery,all flags). Input has two system columns.
 A=columns.reshape(nclock,2,nwork_env,2).transpose(1,0,2,3).reshape(2,nclock*nwork_env,2)
 return np.einsum('aer,bes->arbs',A,A.conj()).reshape(4,4)
def choi_super(S):
 J=np.zeros((4,4),complex)
 for r in (0,1):
  for q in (0,1):
   A=S[:,r+2*q].reshape(2,2,order='F')
   for a in (0,1):
    for b in (0,1):J[2*a+r,2*b+q]=A[a,b]
 return J

def full_program():
 n=3;w=3;width=2;T=.3;dt=T/n;omega=np.sqrt(2);gamma=.4;B=width+2;f=2**n
 words=tuple(product(range(2),range(B),range(f)));ix={p:i for i,p in enumerate(words)};D=len(words)
 hs=np.array([omega*s for s,b,flags in words]);hb=np.array([omega*b for s,b,flags in words]);q=hs+hb
 # Coherent jump not covariant under H: sqrt(gamma)|+><0|.
 z=np.array([1.,0.,0.,0.]);v=np.array([0.,1.,0.,1.])/np.sqrt(2)
 c=np.sqrt(1-gamma*dt);ss=np.sqrt(gamma*dt)
 rot=np.eye(4)+(c-1)*(np.outer(z,z)+np.outer(v,v))+ss*(np.outer(v,z)-np.outer(z,v))
 local=np.repeat(np.exp(-1j*np.array([0.,omega])*dt),2)[:,None]*rot
 assert np.linalg.norm(local.conj().T@local-np.eye(4))<2e-14
 gates=[];prefix=[np.eye(D,dtype=complex)];gs=[prefix[0]];gq=[prefix[0]];ws=[];wq=[]
 for bit in range(n):
  V=np.zeros((D,D),complex)
  for col,(system,b,flags) in enumerate(words):
   label=system+b
   if not 1<=label<=width+1:V[col,col]=1;continue
   a=2*system+((flags>>bit)&1)
   for out in range(4):
    sout,fout=divmod(out,2);row=ix[sout,label-sout,(flags&~(1<<bit))|(fout<<bit)]
    V[row,col]=local[out,a]
  assert np.linalg.norm(V.conj().T@V-np.eye(D))<2e-13
  assert np.max(abs((q[:,None]-q[None,:])*V))<2e-14
  gates.append(V);prefix.append(V@prefix[-1]);k=bit+1
  ws.append(np.exp(1j*k*dt*hs)[:,None]*V*np.exp(-1j*(k-1)*dt*hs)[None,:])
  wq.append(np.exp(1j*dt*q)[:,None]*V)
  gs.append(np.exp(1j*k*dt*hs)[:,None]*prefix[-1]);gq.append(np.exp(1j*k*dt*q)[:,None]*prefix[-1])
  assert np.linalg.norm(ws[-1]@gs[-2]-gs[-1])<3e-13
  assert np.linalg.norm(wq[-1]@gq[-2]-gq[-1])<3e-13
  assert np.linalg.norm(gq[-1]-np.exp(1j*k*dt*hb)[:,None]*gs[-1])<3e-13
 xs,chi,J,R,ev,evolve=clock_spectral(w,n,T);M=len(xs);clip=np.clip(xs,0,n);center=2*J*np.cos(np.pi/(M+1))
 HC=diags([-J*np.ones(M-1),center*np.ones(M),-J*np.ones(M-1)],[-1,0,1],format='csr')
 def compile_direct(steps):
  pieces=[[None]*M for _ in range(M)]
  for a in range(M):pieces[a][a]=eye(D,format='csr')*center
  for a in range(M-1):
   k0,k1=clip[a:a+2]
   link=np.eye(D) if k0==k1 else steps[k1-1]
   pieces[a+1][a]=-J*link;pieces[a][a+1]=-J*link.conj().T
  return bmat(pieces,format='csr')
 hist_s=compile_direct(ws);hist_q=compile_direct(wq)
 gauge=block_diag([gs[k] for k in clip],format='csr')
 defect=hist_s-gauge@kron(HC,eye(D),format='csr')@gauge.conj().T
 assert max(abs(defect.data),default=0)<3e-13
 battery_phase=np.concatenate([np.exp(1j*k*dt*hb) for k in clip])
 cb=diags(battery_phase)
 defect2=hist_q-cb@hist_s@cb.conj().T
 assert max(abs(defect2.data),default=0)<3e-13
 Q=diags(np.tile(q,M));total_s=Q+hist_s;total_q=Q+hist_q
 for h in (hist_s,hist_q):
  comm=h@Q-Q@h
  assert max(abs(comm.data),default=0)<3e-13
 beta=np.zeros(B);beta[1:width+1]=np.sqrt(2/(width+1))*np.sin(np.pi*np.arange(1,width+1)/(width+1))
 inp=np.zeros((D,2),complex)
 for system in (0,1):
  for b in range(B):inp[ix[system,b,0],system]=beta[b]
 initial=(chi[:,None,None]*inp[None,:,:]).reshape(M*D,2)
 assert np.linalg.norm(gauge.conj().T@initial-initial)<2e-14
 bare=kron(HC,eye(D),format='csr')
 assert np.linalg.norm((hist_s-bare)@initial)<3e-13
 assert np.linalg.norm((hist_q-bare)@initial)<3e-13
 # Direct initial derivative on all input matrix units, including a reference.
 Y=total_s@initial
 Xarr=initial.reshape(M,2,B*f,2).transpose(1,0,2,3).reshape(2,M*B*f,2)
 Yarr=Y.reshape(M,2,B*f,2).transpose(1,0,2,3).reshape(2,M*B*f,2)
 derivative=-1j*(np.einsum('aer,bes->arbs',Yarr,Xarr.conj())-np.einsum('aer,bes->arbs',Xarr,Yarr.conj())).reshape(4,4)
 hs2=np.diag([0.,omega]);A=-1j*(np.kron(np.eye(2),hs2)-np.kron(hs2.T,np.eye(2)))
 assert np.max(abs(derivative-choi_super(A)))<2e-12
 Sobs=diags(np.tile(hs,M));ground=initial[:,0]
 initial_power=float((1j*np.vdot(ground,(total_s@Sobs-Sobs@total_s)@ground)).real)
 assert abs(initial_power)<2e-12
 rows=[]
 for t in (0.,.13,T):
  direct=expm_multiply(-1j*t*total_s,initial);directq=expm_multiply(-1j*t*total_q,initial)
  cp=evolve(t)
  expected=np.stack([cp[a]*gs[k]@inp for a,k in enumerate(clip)])
  expected*=np.exp(-1j*t*q)[None,:,None];expected=expected.reshape(M*D,2)
  mismatch=np.linalg.norm(direct-expected)
  assert mismatch<2e-11
  assert np.linalg.norm(directq-battery_phase[:,None]*direct)<2e-11
  rho=choi_columns(direct,M,B*f);rhoq=choi_columns(directq,M,B*f)
  assert np.max(abs(rho-rhoq))<2e-12
  qmean=float(np.trace(direct.conj().T@(Q@direct)).real/2)
  ec=float(np.trace(direct.conj().T@(hist_s@direct)).real/2)
  assert abs(qmean-(omega/2+omega*(width+1)/2))<2e-11
  assert abs(ec-center)<2e-11
  rows.append({'t':t,'direct_H_vs_spectral_clock_isometry_error':float(mismatch),'system_vs_full_Q_counterphase_reduced_Choi_error':float(np.max(abs(rho-rhoq))),'free_energy_balance_error':abs(qmean-(omega/2+omega*(width+1)/2)),'clock_program_energy':ec})
 return {'system_jump':'sqrt(gamma)|+><0|; not H-covariant','clock_dimension':M,'total_dimension':M*D,'rows':rows,'initial_reduced_derivative_equals_A':True,'initial_system_power':initial_power,'original_GKLS_initial_ground_power':omega*gamma/2,'initial_interaction_action_zero_on_product_preparation':True,'counterphase_difference':'Controlled battery-only phase; full states differ, reduced system/reference channels agree.'}

# Rebuild the actual star from the worker's source-blind local-matrix data.
# No root execution code or clock helper is imported.
def star_rows():
 data=json.loads((SNAP/'microscopic_electric_robustness_independent/EXACT_STAR_MATRIX_RESULTS.json').read_text())
 d=data['dimension'];basis=[tuple(a['q']) for a in data['basis']]
 def mat(rows):
  A=np.zeros((d,d),complex)
  for r in rows:A[r['row'],r['column']]=float(r['value'])
  return A
 F=mat(data['operators']['F']);W=mat(data['operators']['W']);TT=mat(data['operators']['T']);CC=mat(data['operators']['C_original'])
 epsilon=1/np.sqrt(6);kappa=.1;T=.1
 H=(W+epsilon*TT+epsilon**2*CC)/epsilon**4
 psi=np.zeros(d,complex);psi[basis.index((1,0,0,0))]=1;psi=(psi+epsilon*F@psi)/np.sqrt(1+3*epsilon**2)
 assert np.linalg.norm(H@psi)<3e-12
 eig,V=np.linalg.eigh(H);levels=np.array([0.,36.,54.]);labels=np.argmin(abs(eig[:,None]-levels[None,:]),axis=1)
 assert max(abs(eig-levels[labels]))<3e-12
 energies=levels[labels];energy_delta=energies[:,None]-energies[None,:]
 initial=V.conj().T@np.outer(psi,psi.conj())@V
 assert np.linalg.norm(initial*(labels[:,None]+labels[None,:]))<2e-12
 jumps={(b,c):mat(data['operators']['resolved_j'][str((b,c))]) for b in (1,2,3) for c in (-1,1)}
 authors=json.loads((SNAP/'autonomous_clock_author/ORIGINAL_STAR_CLOCK_RESULTS.json').read_text())['rows']
 keyed={(r['instrument'],r['steps'],r['t']):r for r in authors};results=[]
 for kind in ('resolved','coherent'):
  raw=list(jumps.values()) if kind=='resolved' else [jumps[b,1]+jumps[b,-1] for b in (1,2,3)]
  ls=[np.sqrt(kappa)/epsilon*j for j in raw];gamma=sum(l.conj().T@l for l in ls);g=float(np.linalg.norm(gamma,2));h=float(max(energies));I=np.eye(d)
  generator=-1j*(np.kron(I,H)-np.kron(H.T,I))
  for l in ls:
   ll=l.conj().T@l;generator+=np.kron(l.conj(),l)-.5*(np.kron(I,ll)+np.kron(ll.T,I))
  rho0=np.outer(psi,psi.conj()).reshape(-1,order='F');exact=expm_multiply(generator,rho0,start=0,stop=T,num=5,endpoint=True)
  for n,w,L in ((256,8,31),(1024,16,127)):
   dt=T/n;vv,rr=np.linalg.eigh(gamma);K0=(rr*np.sqrt(1-dt*vv))@rr.conj().T
   free=expm(-1j*dt*H);ks=[V.conj().T@free@K0@V]+[np.sqrt(dt)*V.conj().T@free@l@V for l in ls]
   prefix=[initial]
   for k in range(n):prefix.append(sum(a@prefix[-1]@a.conj().T for a in ks))
   prefix=np.asarray(prefix)
   # Explicit translated finite battery vectors give the final-energy Gram
   # matrix for the whole stationary-input prefix; no per-step battery reset.
   beta=np.zeros(L+2);beta[1:L+1]=np.sqrt(2/(L+1))*np.sin(np.pi*np.arange(1,L+1)/(L+1))
   down=np.r_[beta[1:],0.]
   translates=[np.kron(beta,beta),np.kron(down,beta),np.kron(beta,down)]
   gram=np.array([[np.vdot(b,a) for b in translates] for a in translates]).real
   assert np.max(abs(np.diag(gram)-1))<2e-14
   factor=gram[labels[:,None],labels[None,:]]
   finite_prefix=prefix*factor[None,:,:]
   xs,chi,J,R,clock_eig,evolve=clock_spectral(w,n,T);M=len(xs);theta=np.pi/(w+1)
   eta=min(2.,8*np.sin(np.pi/(2*(L+1))));collision=T*dt*(7*g*g+4*h*g);clock_time=2*g*(dt*w+T*np.tan(theta)/np.sqrt(w+1))
   a=2*J*T;logtail=np.log(4)+a+R*np.log(a)-math.lgamma(R+1);boundary=min(2.,np.exp(max(logtail,np.log(np.finfo(float).tiny))))
   bound=min(2.,eta+collision+clock_time+boundary)
   for t,target in zip(np.linspace(0,T,5),exact):
    pt=evolve(t);weights=np.bincount(np.clip(xs,0,n),weights=abs(pt)**2,minlength=n+1)
    phase=np.exp(1j*(np.arange(n+1)*dt-t)[:,None,None]*energy_delta[None,:,:])
    actual=np.einsum('k,kab->ab',weights,phase*finite_prefix)
    target=V.conj().T@target.reshape(d,d,order='F')@V
    row={'instrument':kind,'steps':n,'t':float(t),'state_trace_norm_error':tn(actual-target),'autonomous_system_energy':float(np.dot(energies,np.diag(actual).real)),'original_GKLS_system_energy':float(np.dot(energies,np.diag(target).real)),'clock_dimension':M,'clock_program_energy_above_ground':2*J*np.cos(np.pi/(M+1)),'proved_uniform_diamond_bound':bound}
    old=keyed[kind,n,float(t)]
    fields=('state_trace_norm_error','autonomous_system_energy','original_GKLS_system_energy','clock_program_energy_above_ground','proved_uniform_diamond_bound')
    differences={k:abs(row[k]-old[k]) for k in fields}
    assert max(differences.values())<2e-8,(kind,n,t,differences)
    assert row['clock_dimension']==old['clock_dimension']
    assert abs(np.trace(actual)-1)<5e-11
    row['author_field_differences']=differences;results.append(row)
 assert len(results)==len(authors)
 return {'independent_origin':'Frozen source-blind local operator matrix data; independent spectral DST clock propagation and explicit finite battery translation Gram matrix','comparison_rows':results,'max_author_field_difference':max(max(r['author_field_differences'].values()) for r in results),'row_count':len(results),'scope':'Actual lambda=0 stationary dressed star, both original instruments; no assertion that this input-specific Gram reduction holds for arbitrary nonstationary input.'}
result={'complete_non_covariant_program':full_program(),'original_star_comparison':star_rows(),'author_implementation_imported':False,'scientific_discrepancies':[]}
(HERE/'TRAVELING_PROGRAM_AND_STAR_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'complete_non_covariant_program':result['complete_non_covariant_program'],'original_star_summary':{k:result['original_star_comparison'][k] for k in ('max_author_field_difference','row_count','scope')},'scientific_discrepancies':[]},indent=2))
