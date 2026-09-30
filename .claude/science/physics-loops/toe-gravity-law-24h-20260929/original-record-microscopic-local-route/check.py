"""Actual two-leaf compensated star; finite controls, not a volume proof."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k]='1'
import itertools,json,math,time,resource,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import expm
started=time.process_time();here=Path(__file__).resolve().parent
words=[(1,0,0),(0,1,0),(0,0,1),(-1,1,1),(1,-1,1),(1,1,-1)]
assert set(words)=={q for q in itertools.product((-1,0,1),repeat=3) if sum(q)==1}
idx={q:i for i,q in enumerate(words)};dim=len(words)
F=np.zeros((dim,dim),complex);jres=[]
for q,i in idx.items():
    if q[0]:
        for b in (1,2):
            if q[b]==0:
                r=list(q);r[b]=q[0];r[0]=0;F[idx[tuple(r)],i]+=1
for b in (1,2):
    for sign in (-1,1):
        j=np.zeros((dim,dim),complex)
        for q,i in idx.items():
            if q[0]==q[b]==0:
                r=list(q);r[0]=sign;r[b]=-sign;j[idx[tuple(r)],i]=1
        jres.append(j)
W=np.diag([int(q[0]==0) for q in words]).astype(complex)
T=-F-F.conj().T;C=F.conj().T@F;D2=F@F.conj().T
P=np.eye(dim)-W
comm=lambda A,B:A@B-B@A
norm=lambda A:float(np.linalg.norm(A,2))
adj=lambda A:A.conj().T
for j in jres:
    assert norm(comm(W,j)+j)==0 and norm(j@P)==0
assert norm(C-2*np.diag([1,0,0,0,0,0]))==0
assert norm(sum(adj(j)@j for j in jres)-2*W)==0
assert norm(P@(C-D2+C*0-F.conj().T@F)@P)==0
# The compensation, not a removed birth channel, cancels the low second order.
assert norm(P@(C-adj(F)@F)@P)==0
w=np.real(np.diag(W));grade=w[:,None]-w[None,:]
avg=lambda A:np.where(grade==0,A,0)
off=lambda A:A-avg(A)
def invgrade(A):
    out=np.zeros_like(A);nz=grade!=0;out[nz]=A[nz]/grade[nz];return out

def dissipator(Js,A):
    return sum((adj(j)@A@j-(adj(j)@j@A+A@adj(j)@j)/2 for j in Js),np.zeros_like(A))

rows=[]
for instrument,js in [('resolved',jres),('coherent',[jres[0]+jres[1],jres[2]+jres[3]])]:
    assert norm(sum(adj(j)@j for j in js)-2*W)==0
    B=[j@F@P for j in js]
    assert norm(sum(adj(b)@b for b in B)-4*np.diag([1,0,0,0,0,0]))==0
    for S in (4,8,16,32):
        delta=K=1.;kappa=.7;e=math.sqrt(delta/(K*S*(S+1)));d=math.sqrt(1+2*e*e)
        Y=np.eye(dim,dtype=complex);Y[0,0]=1/d
        Y[0,1:3]=e/d;Y[1:3,0]=-e/d
        Y[1:3,1:3]=np.eye(2)+(1/d-1)*np.ones((2,2))/2
        h=W+e*T+e*e*C
        rotation_residual=norm(Y@h@adj(Y)-(W+e*e*D2))
        assert norm(Y@adj(Y)-np.eye(dim))<2e-14 and rotation_residual<2e-14
        Js=[Y@j@adj(Y) for j in js]
        for j in Js:assert norm(np.where(grade>0,j,0))<1e-15
        Ae=kappa/e**2*dissipator(Js,W);R=off(Ae)
        Be=lambda A:1j*delta/e**2*comm(D2,A)+kappa/e**2*dissipator(Js,A)
        full=lambda A:1j*delta/e**4*comm(W,A)+Be(A)
        K1=1j*e**4/delta*invgrade(R)
        K2=1j*e**4/delta*invgrade(off(Be(K1)))
        X=W+K1+K2
        Dminus=kappa/e**2*sum((adj(np.where(grade==-1,j,0))@np.where(grade==-1,j,0) for j in Js),np.zeros_like(W))
        residual=full(X)+Dminus
        expected=avg(Be(K1))+Be(K2)
        exact_identity_error=norm(residual-expected)
        assert exact_identity_error<2e-9
        # Analytic constants: ||R||<=sqrt2*kappa/e; ||Be||<=b/e²;
        # ||Be-e^-2 B_-2||<=32sqrt2*kappa/e on this complete star.
        b=4*delta+8*kappa
        cK1=math.sqrt(2)*kappa/delta
        cK2=math.pi*b*cK1/delta
        cResidual=64*kappa*kappa/delta+b*cK2
        assert norm(K1)<=cK1*e**3*(1+1e-12)
        assert norm(K2)<=cK2*e**5*(1+1e-12)
        assert norm(expected)<=cResidual*e**2
        wrong_sign=norm(full(W-K1)+Dminus)
        assert wrong_sign>10*norm(expected)
        # Direct ACTUAL no-event propagation, with all original output vectors.
        H=delta/e**4*h;A_no=-1j*H-kappa/e**2*W
        initial=np.zeros(dim,complex);initial[0]=1
        times=sorted(set([0.,.01,.05,.1,.25]+[r*e**4 for r in (math.pi/4,math.pi/2,math.pi,2*math.pi)]))
        evolution=[]
        for t in times:
            psi=expm(t*A_no)@initial
            survival=float(np.vdot(psi,psi).real)
            holes=float(np.vdot(psi,W@psi).real)
            target_survival=math.exp(-4*kappa*t)
            noerr=np.outer(psi,psi.conj())-target_survival*np.outer(initial,initial.conj())
            joint_error=float(np.sum(abs(np.linalg.eigvalsh(noerr))))+abs(survival-target_survival)
            # Each original mark has vector B_m Omega; no sign dephasing is inserted.
            output_trace=sum((1-survival)/4*float(np.vdot(bm@initial,bm@initial).real) for bm in B)
            assert abs(output_trace-(1-survival))<1e-12 and -1e-10<=survival<=1+1e-10
            rotation_holes=float(np.vdot(Y@initial,W@(Y@initial)).real)
            assert abs(rotation_holes-2*e*e/(1+2*e*e))<1e-14
            cK=cK1+cK2/16
            physical_bound=e*e*(8+4*cK*e+2*cResidual*t)
            assert holes<=physical_bound+1e-10
            evolution.append({'t':t,'holes':holes,'holes_over_epsilon2':holes/e**2,'actual_total_intensity':2*kappa/e**2*holes,'target_intensity_unconditional':4*kappa*target_survival,'mark_joint_trace_error':joint_error,'survival':survival,'target_survival':target_survival})
        rows.append({'instrument':instrument,'S':S,'epsilon':e,'rotation_residual':rotation_residual,'D8_identity_error':exact_identity_error,'K1_norm_over_epsilon3':norm(K1)/e**3,'K2_norm_over_epsilon5':norm(K2)/e**5,'corrected_residual_norm_over_epsilon2':norm(expected)/e**2,'analytic_residual_constant':cResidual,'wrong_K1_sign_residual_norm':wrong_sign,'without_K2_off_residual_over_epsilon':norm(off(Be(K1)))/e,'evolution':evolution})
result={'model':'complete actual supplied two-leaf star, Gauss E_Ab=-q_b; no fitted proxy','words':words,'complete_dimension':dim,'rows':rows,'role':'Local algebra/normal-form and actual marked-output control; no numerical proof of cubic-volume convergence.','cpu_seconds':time.process_time()-started,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'bindings':{n:hashlib.sha256((here/n).read_bytes()).hexdigest() for n in ('check.py','CONTRACT.md','RUN_CONTRACT.md','SOURCE_IDENTITIES.json')}}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'complete_dimension':dim,'rows':len(rows),'max_D8_identity_error':max(r['D8_identity_error'] for r in rows),'max_corrected_residual_over_epsilon2':max(r['corrected_residual_norm_over_epsilon2'] for r in rows),'cpu_seconds':result['cpu_seconds'],'peak_rss_bytes':result['peak_rss_bytes'],'mark_output_coherence_preserved':True},indent=2))
