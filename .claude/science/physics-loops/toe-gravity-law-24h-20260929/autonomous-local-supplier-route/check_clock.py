"""Small module controls. The two-level matrix is a clock/ledger fixture,
not a replacement for the original rotor law in the analytic construction.
"""
import time,resource,json,math
from pathlib import Path
from fractions import Fraction
import numpy as np
OUT=Path(__file__).resolve().parent
start=time.monotonic();cpu=time.process_time()
X=np.array([[0.,1.],[1.,0.]])
G=np.eye(2)-X # positive log-like local drive, norm2; does not commute with h.
h=np.diag([0.,2.]);T=.6;k0=2

def fixture(K):
 d=2*K+1
 shift=np.diag(np.ones(d-1),-1)
 f=.5*np.eye(d)-.25*(shift+shift.T) # compression of (1-cos x)/2 >=0
 pc=np.diag(np.arange(d,dtype=float))
 hs=np.kron(np.eye(d),h);hc=np.kron(pc,np.eye(2));inter=np.kron(f,G)
 H=hs+hc+inter
 assert np.linalg.eigvalsh(f)[0]>=-1e-13
 ev,Q=np.linalg.eigh(H);assert ev[0]>=-1e-13
 psi=np.zeros(2*d,dtype=complex)
 for j in range(-k0,k0+1):psi[2*(j+K)]=1/math.sqrt(2*k0+1)
 out=Q@(np.exp(-1j*T*ev)*(Q.conj().T@psi))
 energy=lambda A,v:float(np.vdot(v,A@v).real)
 changes={name:energy(A,out)-energy(A,psi) for name,A in [('system',hs),('clock',hc),('interaction',inter),('total',H)]}
 assert abs(changes['total'])<1e-10
 assert changes['system']>1e-5
 assert abs(changes['system']+changes['clock'])>1e-5 # deleting controller interaction fails.
 # The unshifted clock convention permits vector comparison across cutoffs.
 out*=np.exp(1j*K*T)
 return out,changes,float(ev[0])
ref,_,_=fixture(32)
rows=[]
for K in (6,8,10):
 vec,ledger,ground=fixture(K)
 pad=np.zeros_like(ref);pad[2*(32-K):2*(32+K+1)]=vec
 err=np.linalg.norm(pad-ref)
 k=K-k0+1;x=2*T
 tail=sum(x**n/math.factorial(n) for n in range(k,100))
 assert err<=2*tail+1e-12
 rows.append({'K':K,'dimension':2*(2*K+1),'joint_vector_error_vs_K32':float(err),'proved_vector_tail_upper':2*tail,'energy_changes':ledger,'minimum_total_energy':ground})

# Exact Gaussian-integer interaction-picture words with the true nonwrapping
# shifts. All intermediate magnitudes here are below 2^53.
def act(vec,tick,K=None):
 out={}
 roots=(1,1j,-1,-1j)
 for (m,s),v in vec.items():
  for dm,c in ((0,2),(-1,-1),(1,-1)):
   for sp,sgn in ((s,1),(1-s,-1)):
    mp=m+dm
    if K is not None and abs(mp)>K:continue
    phase=roots[(tick*((mp+2*sp)-(m+2*s)))%4]
    key=mp,sp;out[key]=out.get(key,0)+c*sgn*phase*v
 return {k:v for k,v in out.items() if v}
words=0
for K in range(3,9):
 for n in range(K-k0+1):
  full=cut={(m,0):1 for m in range(-k0,k0+1)}
  for j in range(n):
   full=act(full,2*j+1);cut=act(cut,2*j+1,K)
  assert full==cut
  assert all(z.real.is_integer() and z.imag.is_integer() for z in map(complex,full.values()))
  words+=1
K=4;d=2*K+1
S=np.diag(np.ones(d-1),-1);P=np.diag(np.arange(-K,K+1))
assert np.array_equal(P@S-S@P,S)
wrap=S.copy();wrap[0,-1]=1
wrap_def=P@wrap-wrap@P-wrap
assert wrap_def[0,-1]==-(2*K+1)

# Matched-record code: conjugated copying preserves it at every partial pulse,
# not merely at the completed collision. Exact integer matrices suffice.
dF=3
copy=np.zeros((dF*dF,dF*dF),dtype=int)
for f0 in range(dF):
 for e0 in range(dF):copy[f0*dF+(e0+f0)%dF,f0*dF+e0]=1
gf=np.eye(dF,dtype=int);gf[0,1]=gf[1,0]=-1
gfe=copy@np.kron(gf,np.eye(dF,dtype=int))@copy.T
code=np.diag([int(f0==e0) for f0 in range(dF) for e0 in range(dF)])
assert np.array_equal(copy.T@copy,np.eye(dF*dF,dtype=int))
assert np.array_equal(gfe@code,code@gfe)
assert gfe[0,dF+1]==-1 # a genuine offdiagonal matched-label transition
assert all(gfe[row,col]==0 for row in range(dF*dF) for col in range(dF*dF)
           if code[row,row] != code[col,col])

# Literal cubic-star original B maps: coherence kept within each chosen mark.
# This checks label/field/grade premises, not an apparatus Hilbert matrix.
from itertools import product
source_words=0
for qa in (-1,1):
 for bs in product((-1,0,1),repeat=6):
  for b in range(6):
   for sigma in (-1,1):
    for dest in range(6):
     if dest==b or bs[b] or bs[dest]:continue
     final=list(bs);final[b]=-sigma;final[dest]=qa
     ee=[0]*6;ee[b]=sigma;ee[dest]=-qa
     assert sum(v!=0 for v in final)==sum(v!=0 for v in bs)+2
     assert sum(ee)==sigma-qa
     assert all(-ee[i]==final[i]-bs[i] for i in range(6))
     source_words+=1
assert source_words==9720

r={'clock_module_matrix_rows':rows,'exact_interaction_picture_word_cases':words,
 'cyclic_wrap_wrong_clock_commutator_detected':int(wrap_def[0,-1]),
 'exact_matched_record_code_preserved':True,
 'original_cubic_star_B_words':source_words,
 'scope':'Matrix engine is only a clock/interaction-ledger module fixture. Original law remains the full sourced cubic h and B in the proof; no matrix substitution is made.',
 'wall_seconds':time.monotonic()-start,'cpu_seconds':time.process_time()-cpu,
 'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(OUT/'clock_results.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2));print('PASS 6 groups; FAIL 0')
