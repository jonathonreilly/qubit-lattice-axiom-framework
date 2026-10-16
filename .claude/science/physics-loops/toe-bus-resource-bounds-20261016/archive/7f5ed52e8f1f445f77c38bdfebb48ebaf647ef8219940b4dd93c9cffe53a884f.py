"""New exposed finite check; does not import an author or historical checker."""
from pathlib import Path
import itertools, json, math, platform, sys
import numpy as np
import scipy
from scipy.linalg import qr, eigh

OUT=Path(sys.argv[1]).resolve()
N=6
size=2**N
I=np.eye(2); n=np.diag([0.,1.]); sm=np.array([[0.,1.],[0.,0.]])
sp=sm.T; X=sp+sm; Z=I-2*n
def tensor(*items):
    out=np.array([[1.]])
    for x in items: out=np.kron(out,x)
    return out
def local(ops): return tensor(*(ops.get(j,I) for j in range(N)))
def norm(a): return float(np.linalg.norm(a,2))
def check(v,msg):
    if not v: raise AssertionError(msg)
def span(a):
    u,s,_=np.linalg.svd(a,full_matrices=True)
    rank=int(np.sum(s>1e-9))
    return u[:,:rank],u[:,rank:],rank
def pin_zero(x,msg,tol=2e-9):check(x<tol,f'{msg}: {x}')

# Integer computational-basis construction of every supplied source operator.
D=np.zeros((size,N+1))
for x in range(size):D[x,x.bit_count()]=1
Jsource=D/np.sqrt(np.sum(D*D,axis=0))
Nop=sum(local({j:n}) for j in range(N))
swaps=[]
for j in range(N-1):
    U=np.zeros((size,size))
    mask1=1<<(N-1-j); mask2=1<<(N-2-j)
    for x in range(size):
        y=x if bool(x&mask1)==bool(x&mask2) else x^mask1^mask2
        U[y,x]=1
    swaps.append(U)
L=sum(np.eye(size)-U for U in swaps)
C=sum(local({j:n,j+1:n}) for j in range(N-1))
site_sm=local({0:sm}); site_sp=site_sm.T

columns=[D]
for r in (1,2):
    for sites in itertools.combinations(range(N),r):
        for choices in itertools.product((n,sm,sp),repeat=r):
            columns.append(local(dict(zip(sites,choices)))@D)
    raw=np.concatenate(columns,axis=1)
    u,perp,rank=span(raw)
    if r==1:U1,U1perp,rank1,raw1=u,perp,rank,raw.copy()
    else:U2,U2perp,rank2,raw2=u,perp,rank,raw.copy()
P1=U1@U1.T;P2=U2@U2.T
source_report={'N':N,'physical_dimension':size,'code_dimension':N+1,
    'one_action_dimension':rank1,'two_action_dimension':rank2,
    'one_action_columns':raw1.shape[1],'two_action_columns':raw2.shape[1]}
check(rank1<size and rank2<size and rank2>rank1,'proper nested envelopes required')
source_report['one_action_in_two']=norm((np.eye(size)-P2)@U1)
source_report['L_invariance_one']=norm((np.eye(size)-P1)@L@U1)
source_report['L_invariance_two']=norm((np.eye(size)-P2)@L@U2)
source_report['number_invariance_two']=norm((np.eye(size)-P2)@Nop@U2)
source_report['swap_invariance_two']=max(norm((np.eye(size)-P2)@U@U2) for U in swaps)
source_report['lowering_one_to_two']=norm((np.eye(size)-P2)@site_sm@U1)
source_report['raising_one_to_two']=norm((np.eye(size)-P2)@site_sp@U1)
source_report['counterterm_leak_outside_one']=norm((np.eye(size)-P1)@C@Jsource)
source_report['counterterm_leak_outside_two']=norm((np.eye(size)-P2)@C@Jsource)
for k,v in source_report.items():
    if k.endswith(('in_two','invariance_one','invariance_two','one_to_two','outside_two')):pin_zero(v,k)
check(source_report['counterterm_leak_outside_one']>1e-3,'one-envelope counterterm truncation must be rejected')

# Deterministic finite fixture design: choose the outside-G2 eigenvalue farthest
# from the G2 spectrum. This is declared adaptive fixture selection, not sampling.
a2=eigh(U2.T@L@U2,eigvals_only=True)
aout=eigh(U2perp.T@L@U2perp,eigvals_only=True)
separations=np.array([np.min(np.abs(a2-a)) for a in aout])
pick=int(np.argmax(separations));alpha=float(aout[pick]);c=-alpha
check(separations[pick]>1e-3,'fixture requires an isolated outside-G2 pole')
compressed=U1.T@(L+c*np.eye(size))@U1
T1=U1@np.linalg.inv(compressed)@U1.T
hole=np.flatnonzero(np.diag(Nop)==N-1)
Rh=np.linalg.inv((L+c*np.eye(size))[np.ix_(hole,hole)])
chiN=(np.eye(size)-Jsource@Jsource.T)@site_sm@Jsource[:,N]
bN=N/(N-1)*(chiN[hole]@Rh@chiN[hole])
predicted=np.array([k*(N-k+1)/(N*N*c)+bN*k*(k-1)/(N*N) for k in range(N+1)])
actual=Jsource.T@site_sp@T1@site_sm@Jsource
resolvent_report={'outside_G2_eigenvalues':aout.tolist(),'selected_index':pick,
    'alpha':alpha,'c':c,'distance_from_G2_spectrum':float(separations[pick]),
    'full_source_min_singular_value':float(np.linalg.svd(L+c*np.eye(size),compute_uv=False)[-1]),
    'restricted_source_min_singular_value':float(np.linalg.svd(compressed,compute_uv=False)[-1]),
    'one_hole_b_N':float(bN),'self_energy_formula_error':norm(actual-np.diag(predicted)),
    'wrong_symmetric_only_formula_error':norm(actual-np.diag([k*(N-k+1)/(N*N*c) for k in range(N+1)])),
    'reached_inverse_residual':norm((L+c*np.eye(size))@T1@site_sm@Jsource-site_sm@Jsource)}
pin_zero(resolvent_report['self_energy_formula_error'],'compressed source formula')
pin_zero(resolvent_report['reached_inverse_residual'],'inverse on reached vectors')
check(resolvent_report['full_source_min_singular_value']<1e-10,'outside pole should be visible')
check(resolvent_report['wrong_symmetric_only_formula_error']>1e-3,'omitted multiplicity term must fail')

# The gap coefficient estimate is checked against the actual adjacent-swap chain.
all_source=eigh(L,eigvals_only=True);positive=all_source[all_source>1e-8]
ell=N*(N-1)//2
gap_report={'ell':ell,'proposed_lower_bound':1/(ell*ell),'actual_positive_gap':float(positive[0]),
    'operator_inequality_min_eigenvalue':float(eigh(L-(np.eye(size)-Jsource@Jsource.T)/(ell*ell),eigvals_only=True)[0])}
check(gap_report['operator_inequality_min_eigenvalue']>-1e-9,'source gap inequality')

# Full actual finite matrices: one old qubit, one bus qubit, one length-six source.
# This deliberately tests the envelope lemma, not the complete routed geometry.
omega=20.; lam=omega-alpha; vp=.7; r=.9
check(lam>0,'positive bus field')
H=omega*n
K0=tensor(H,I,np.eye(size))+tensor(I,lam*n,np.eye(size))+tensor(I,I,omega*Nop+L)
V=vp*tensor(X+.3*Z,X,np.eye(size))+r*(tensor(I,sp,site_sm)+tensor(I,sm,site_sp))
A=-r*r/c;B=-r*r*bN;u=-A/N;v=-(B-A)/N
A2=tensor(I,I,u*Nop+v*C)
J=tensor(I,np.array([[1.],[0.]]),Jsource)
F=J.T@K0@J;energies=np.diag(F)
H1=tensor(I,I,U1);H2=tensor(I,I,U2)
P2full=H2@H2.T;P=J@J.T
Jc=H2.T@J;complete,_=qr(Jc,mode='full')
Qbasis=H2@complete[:,J.shape[1]:]
eq,Wq=eigh(Qbasis.T@K0@Qbasis);Uq=Qbasis@Wq
den=eq[:,None]-energies[None,:]
delta=float(np.min(np.abs(den)));check(delta>1e-3,'restricted Q/P separation')
Z1=Uq@(-(Uq.T@V@J)/den)
M=J.T@(V@Z1+A2@J)
diff=energies[:,None]-energies[None,:]
secular=np.abs(diff)<1e-8
Dcode=np.where(secular,M,0.)
rhs=J@Dcode-V@Z1-A2@J
pp=J.T@rhs;zp=np.zeros_like(pp);np.divide(pp,diff,out=zp,where=~secular)
Z2=Uq@((Uq.T@rhs)/den)+J@zp
R3=V@Z2+A2@Z1-Z1@Dcode;R4=A2@Z2-Z2@Dcode
full_identity=norm(K0@Z1-Z1@F+V@J)+norm(K0@Z2-Z2@F-rhs)
pin_zero(full_identity,'two full-space Sylvester identities',2e-8)
pin_zero(norm(Dcode-Dcode.T),'Hermitian secular D')
pin_zero(norm(F@Dcode-Dcode@F),'D commutes with F')
parent_bound=2*(norm(Z1)+norm(Z2))+(.3+.1)*(norm(R3)+norm(R4))
outside3=norm((np.eye(len(K0))-P2full)@R3)
corrector={'full_dimension':len(K0),'H1_dimension':H1.shape[1],'H2_dimension':H2.shape[1],
    'code_dimension':J.shape[1],'bus_field':lam,'source_frequency':omega,
    'restricted_gap':delta,'full_sylvester_error':full_identity,
    'VJ_outside_H1':norm((np.eye(len(K0))-H1@H1.T)@V@J),
    'VH1_outside_H2':norm((np.eye(len(K0))-P2full)@V@H1),
    'A2J_outside_H2':norm((np.eye(len(K0))-P2full)@A2@J),
    'A2J_outside_H1':norm((np.eye(len(K0))-H1@H1.T)@A2@J),
    'R3_outside_H2':outside3,'perturbation_not_H2_invariant':norm((np.eye(len(K0))-P2full)@V@H2),
    'Z1_norm':norm(Z1),'Z2_norm':norm(Z2),'R3_norm':norm(R3),'R4_norm':norm(R4),
    'C_corr_tstar_point3_window_point1':parent_bound,'time_checks':[]}
for key in ('VJ_outside_H1','VH1_outside_H2','A2J_outside_H2'):pin_zero(corrector[key],key)
check(corrector['A2J_outside_H1']>1e-4,'actual counterterm must require second envelope')
check(outside3>1e-5,'fixture must exercise charged leakage beyond H2')
for xi in (.02,.01,.005):
    K=K0+xi*V+xi*xi*A2;Fxi=F+xi*xi*Dcode;ZZ=J+xi*Z1+xi*xi*Z2
    e,Q=eigh(K);f,R=eigh(Fxi);t=.3/(xi*xi)+.1
    out=Q@(np.exp(-1j*t*e)[:,None]*(Q.T@J))
    target=J@R@(np.exp(-1j*t*f)[:,None]*R.T)
    err=norm(out-target)
    res=norm(K@ZZ-ZZ@Fxi-xi**3*R3-xi**4*R4)
    bound=2*xi*norm(Z1)+2*xi*xi*norm(Z2)+t*(xi**3*norm(R3)+xi**4*norm(R4))
    pin_zero(res,'full residual identity',3e-8);check(err<=bound+1e-8,'full-output Duhamel estimate')
    corrector['time_checks'].append({'xi':xi,'t':t,'full_output_isometry_error':err,'direct_Duhamel_bound':bound,'residual_identity_error':res})

report={'scope':'Finite floating-point check of actual adjacent-swap source and full-space corrector; not a routed-bus simulation or theorem proof.',
    'exposure':'Root proposal and 3-level fixture read before design; new N=6 construction and code, same model, no historical checker imports.',
    'fixture_selection':'Outside-G2 source eigenvalue maximizing computed separation; selected adaptively by declared deterministic rule.',
    'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
    'source':source_report,'compressed_resolvent':resolvent_report,'permutation_gap':gap_report,'full_corrector':corrector}
(OUT/'CHECK_RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
