"""Independent small complete-output discriminator; no parent checker imports."""
from pathlib import Path
import json,sys,platform
import numpy as np
import scipy
from scipy.linalg import expm
O=Path(sys.argv[1]);I=np.eye(2);X=np.array([[0.,1.],[1.,0.]])
Y=np.array([[0.,-1j],[1j,0.]]);Z=np.diag([1.,-1.]);n=np.diag([0.,1.])
def kron(*xs):
 out=np.array([[1.]])
 for x in xs:out=np.kron(out,x)
 return out
def norm(a):return float(np.linalg.norm(a,2))
def gate(phi):return expm(-1j*np.pi/4*(I+np.cos(phi)*Y-np.sin(phi)*X))
H=.36*X+.27*Z+.23*I;omega=.9;nu=1.7;JF=.4;reserve=2.3
S=np.array([[1.,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1.]])
A0=nu*kron(n,I,I)+omega*(kron(I,n,I)+kron(I,I,n))+JF*kron(I,np.eye(4)-S)
C0=reserve+nu+2*omega+2*JF
ron=.8;roff=1.2;ts=1.1;tp=1.3;alphaon=ron/2;alphaoff=roff/2;tau=ron+ts+tp+roff
phi=.37;tilde=phi+omega*alphaoff
Au=ts+tp+alphaon+alphaoff;Phi=C0*Au+reserve*(alphaon+alphaoff)+np.pi*2/4
IdC=np.eye(8);IdE=np.eye(8)
ready=np.zeros((8,1));ready[0,0]=1
J=kron(np.eye(16),ready)
swap=np.zeros((128,128))
for d in range(2):
 for c in range(8):
  for e in range(8):swap[(d*8+e)*8+c,(d*8+c)*8+e]=1
Uon=kron(expm(-1j*ron*H),expm(-1j*alphaon*A0),IdE)*np.exp(-1j*(reserve+C0)*alphaon)
Uoff=kron(expm(-1j*roff*H),expm(-1j*alphaoff*A0),IdE)*np.exp(-1j*(reserve+C0)*alphaoff)
Us=kron(expm(-1j*ts*H),IdC,IdE)@swap*np.exp(-1j*C0*ts)
def full(rotation_angle):
 Up=kron(expm(-1j*tp*H),kron(I,gate(rotation_angle),gate(rotation_angle)),IdE)*np.exp(-1j*C0*tp)
 return Uoff@Up@Us@Uon@J
alpha=np.array([[1.],[np.exp(1j*phi)]])/np.sqrt(2)
Omega=kron(np.array([[1.],[0.]]),alpha,alpha)
append=kron(I,Omega,IdE)
UE=expm(-1j*alphaon*A0);UD=expm(-1j*tau*H)
target=np.exp(-1j*Phi)*append@kron(UD,UE)
actual=full(tilde)
literal_memory=np.exp(-1j*Phi)*append@kron(UD,IdE)
without_reserve_phase=np.exp(-1j*(Phi-reserve*(alphaon+alphaoff)))*append@kron(UD,UE)
K=kron(H,IdC,IdE)+kron(I,A0+reserve*IdC,IdE)
report={'scope':'Floating-point complete isometry discriminator at xi=0. This is the exact commuting zero-weak-coupling boundary, not a positive-xi runtime bus or numerical integration of an arbitrary waveform.',
 'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
 'qubits':{'old':1,'bus':1,'source':2,'memory':3},'physical_dimension':128,'input_dimension':16,
 'parameters':{'ron':ron,'roff':roff,'ts':ts,'tp':tp,'tau':tau,'alpha_on':alphaon,'alpha_off':alphaoff,'omega':omega,'C0':C0,'R':reserve,'phi_release':phi,'phi_gate':tilde,'Phi':Phi},
 'complete_isometry_error':norm(actual-target),
 'wrong_literal_memory_isometry_error':norm(actual-literal_memory),
 'wrong_off_ramp_phase_sign_isometry_error':norm(full(phi-omega*alphaoff)-target),
 'wrong_unshifted_gate_phase_isometry_error':norm(full(phi)-target),
 'missing_R_ramp_phase_isometry_error':norm(actual-without_reserve_phase),
 'mean_compression_difference_for_different_memory_outputs':norm(target.conj().T@K@target-literal_memory.conj().T@K@literal_memory),
 'second_compression_difference_for_different_memory_outputs':norm(target.conj().T@K@K@target-literal_memory.conj().T@K@K@literal_memory)}
assert report['complete_isometry_error']<2e-12
for key in ('wrong_literal_memory_isometry_error','wrong_off_ramp_phase_sign_isometry_error','wrong_unshifted_gate_phase_isometry_error','missing_R_ramp_phase_isometry_error'):assert report[key]>.1
for key in ('mean_compression_difference_for_different_memory_outputs','second_compression_difference_for_different_memory_outputs'):assert report[key]<2e-11
# A single global phase cannot repair the memory comparator: use all source/old
# input columns and find a phase-invariant Gram test rather than one state.
overlap=target.conj().T@literal_memory
report['memory_overlap_nonscalar_norm']=norm(overlap-np.trace(overlap)/16*np.eye(16))
assert report['memory_overlap_nonscalar_norm']>.1
(O/'CHECK_RESULT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
