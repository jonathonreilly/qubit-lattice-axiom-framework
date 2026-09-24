#!/usr/bin/env python3
"""Author controls: exact clock moments and complete autonomous matrices.

The complete matrix example is a two-level raising channel, not a substitute
for the original physical star. A separate control treats that star.
"""
from pathlib import Path
import json, math, sys
sys.dont_write_bytecode = True
import numpy as np
import sympy as sy
from scipy.linalg import expm
from scipy.sparse import block_diag, diags, eye, kron
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent


def trace_norm(a):
    return float(np.sum(np.linalg.svd(a, compute_uv=False)))


def exact_moments():
    rows = []
    for w in (2, 3, 5):
        theta = sy.pi / (w + 1)
        xs = list(range(-w - 3, 4))
        p = sy.zeros(len(xs), 1)
        for j, x in enumerate(xs):
            if -w <= x <= -1:
                p[j] = sy.I**x * sy.sqrt(sy.Rational(2, w + 1)) * sy.sin(theta * (x + w + 1))
        T = sy.zeros(len(xs))
        for j in range(len(xs)-1):
            T[j+1, j] = 1
        V = sy.I * (T - T.T)  # J=1
        X = sy.diag(*xs)
        meanv = sy.simplify((p.conjugate().T * V * p)[0])
        varv = sy.simplify((p.conjugate().T * V**2 * p)[0] - meanv**2)
        meanx = sy.simplify((p.conjugate().T * X * p)[0])
        assert sy.simplify((p.conjugate().T*p)[0]-1) == 0
        assert sy.simplify(meanv-2*sy.cos(theta)) == 0
        assert sy.simplify(varv-4*sy.sin(theta)**2/(w+1)) == 0
        assert meanx == -sy.Rational(w+1, 2)
        rows.append({'width':w, 'mean_X':str(meanx), 'mean_velocity_at_J1':str(meanv),
                     'variance_velocity_at_J1':str(varv), 'arithmetic':'exact SymPy'})
    return rows


def clock(w, n, horizon):
    tau = horizon/n
    theta = np.pi/(w+1)
    J = 1/(2*tau*np.cos(theta))
    a = 2*J*horizon
    R = int(np.ceil(8*a))
    xs = np.arange(-w-R, n+R+1)
    M = len(xs)
    e0 = 2*J*(1-np.cos(np.pi/(M+1)))
    K = diags((-J*np.ones(M-1), (2*J-e0)*np.ones(M), -J*np.ones(M-1)), (-1,0,1), format='csr')
    p = np.zeros(M, complex)
    support = (xs>=-w)&(xs<=-1)
    p[support] = (1j)**xs[support]*np.sqrt(2/(w+1))*np.sin(theta*(xs[support]+w+1))
    assert abs(np.linalg.norm(p)-1)<1e-13
    logtail = np.log(4)+a+R*np.log(a)-math.lgamma(R+1)
    # Round an unrepresentably small positive analytical bound UP to the
    # smallest normal float. Reporting zero would suggest exact truncation.
    boundary = min(2., np.exp(max(logtail, np.log(np.finfo(float).tiny))))
    assert logtail <= np.log(4)-7*a+1e-10
    return xs,K,p,J,R,boundary,e0


def position_controls():
    rows = []
    for w,n in ((4,64),(8,256),(16,256)):
        horizon=1.;tau=horizon/n
        xs,K,p,J,R,b,e0=clock(w,n,horizon)
        evolved=expm_multiply(-1j*K,p,start=0,stop=horizon,num=5,endpoint=True)
        for t,pt in zip(np.linspace(0,horizon,5),evolved):
            prob=abs(pt)**2
            assert abs(prob.sum()-1)<3e-11
            mean=float(np.dot(xs,prob))
            expected=-(w+1)/2+t/tau
            assert abs(mean-expected)<3e-8
            mismatch=float(np.dot(abs(tau*np.clip(xs,0,n)-t),prob))
            bound=tau*w+horizon*np.tan(np.pi/(w+1))/np.sqrt(w+1)
            assert mismatch <= bound+3e-11
            energy=float(np.vdot(pt,K@pt).real)
            assert abs(energy-(2*J-e0))<3e-8
            rows.append({'width':w,'steps':n,'t':float(t),'clock_dimension':len(xs),
                         'mean_position_error':abs(mean-expected),'mean_time_mismatch':mismatch,
                         'proved_uniform_time_bound':float(bound),'clock_energy_above_ground':energy,
                         'proved_boundary_trace_bound':float(b),'boundary_buffer':R})
    return rows


def embed_gate(U, which, n):
    nf=2**n;out=np.zeros((2*nf,2*nf),complex)
    mask=1<<(n-1-which)
    for col in range(2*nf):
        s,f=divmod(col,nf);bit=int(bool(f&mask))
        for ss in (0,1):
            for ff in (0,1):
                newf=(f&~mask)|(ff*mask)
                out[ss*nf+newf,col]=U[2*ss+ff,2*s+bit]
    assert np.linalg.norm(out.conj().T@out-np.eye(2*nf))<1e-12
    return out


def finite_lift(U, nf, L):
    d=len(U);nb=L+2;labels=np.repeat((0,1),nf)
    V=np.zeros((d*nb,d*nb),complex)
    for b in range(d):
        for r in range(nb):
            q=r+labels[b];col=b*nb+r
            if 1<=q<=L+1:
                for a in range(d):
                    rr=q-labels[a]
                    V[a*nb+rr,col]=U[a,b]
            else:
                V[col,col]=1
    assert np.linalg.norm(V.conj().T@V-np.eye(len(V)))<1e-12
    return V


def reduced_choi(columns, nc, nf, nb):
    # Columns correspond to two system inputs. Initial reference is normalized.
    p=columns.reshape(nc,2,nf,nb,2).transpose(0,2,3,1,4).reshape(-1,4)
    return p.T@p.conj()/2


def complete_autonomous_control():
    n=3;nf=2**n;L=2;nb=L+2;w=3;horizon=.3;tau=horizon/n
    omega=np.sqrt(2);gamma=.4
    H=np.diag((0.,omega));jump=np.array([[0.,0.],[np.sqrt(gamma),0.]])
    k1=np.sqrt(tau)*jump
    k0=np.diag((np.sqrt(1-tau*gamma),1.))
    kright=np.diag((1.,np.sqrt(1-tau*gamma)))
    Uflag=np.block([[k0,-k1.conj().T],[k1,kright]])
    order=[0,2,1,3]
    Ulocal=Uflag[np.ix_(order,order)]
    Ulocal=np.kron(expm(-1j*H*tau),np.eye(2))@Ulocal
    assert np.linalg.norm(Ulocal.conj().T@Ulocal-np.eye(4))<1e-13
    E=np.repeat((0.,omega),nf*nb)
    ER=np.tile(omega*np.arange(nb),2*nf)
    Hfree=E+ER
    db=len(E)
    beta=np.zeros(nb);beta[1:L+1]=np.sqrt(2/(L+1))*np.sin(np.pi*np.arange(1,L+1)/(L+1))
    Jin=np.zeros((db,2),complex)
    for s in (0,1):
        Jin[s*nf*nb:s*nf*nb+nb,s]=beta
    Vprod=np.eye(db,dtype=complex);G=[Vprod.copy()];old=G[0]
    prefix_errors=[]
    for k in range(1,n+1):
        U=embed_gate(Ulocal,k-1,n);V=finite_lift(U,nf,L)
        assert np.linalg.norm((Hfree[:,None]-Hfree[None,:])*V)<1e-12
        Vprod=V@Vprod
        current=np.exp(1j*E*k*tau)[:,None]*Vprod
        W=np.exp(1j*E*k*tau)[:,None]*V*np.exp(-1j*E*(k-1)*tau)[None,:]
        prefix_errors.append(float(np.linalg.norm(W@old-current)))
        assert prefix_errors[-1]<2e-12
        G.append(current);old=current
    naive=np.exp(-1j*E*horizon)[:,None]*(Vprod@Jin)
    correct=np.exp(-1j*E*horizon)[:,None]*(G[-1]@Jin)
    assert np.linalg.norm(correct-Vprod@Jin)<1e-12
    double_count_difference=float(np.linalg.norm(naive-correct))
    assert double_count_difference>.1
    xs,K,chi,J,R,boundary,e0=clock(w,n,horizon)
    choices=np.clip(xs,0,n)
    Gauge=block_diag([G[k] for k in choices],format='csr')
    Hhist=Gauge@kron(K,eye(db,format='csr'),format='csr')@Gauge.conj().T
    HF=diags(np.tile(Hfree,len(xs)),format='csr')
    Htotal=Hhist+HF
    hermitian=Htotal-Htotal.conj().T
    comm=Hhist@HF-HF@Hhist
    hermerr=float(np.max(abs(hermitian.data),initial=0))
    commerr=float(np.max(abs(comm.data),initial=0))
    assert hermerr<2e-12 and commerr<2e-12
    init=(chi[:,None,None]*Jin[None,:,:]).reshape(-1,2)
    assert np.linalg.norm(Gauge.conj().T@init-init)<1e-13
    Es0=float(np.trace(init.conj().T@(diags(np.tile(E,len(xs)))@init)).real/2)
    ER0=float(np.trace(init.conj().T@(diags(np.tile(ER,len(xs)))@init)).real/2)
    Ec0=float(np.trace(init.conj().T@(Hhist@init)).real/2)
    assert abs(ER0-omega*(L+1)/2)<1e-12
    assert abs(Ec0-(2*J-e0))<1e-12
    rows=[]
    for t in (0.,.13,horizon):
        direct=expm_multiply(-1j*t*Htotal,init)
        cp=expm_multiply(-1j*t*K,chi)
        formula=np.stack([cp[a]*G[k]@Jin for a,k in enumerate(choices)])
        formula*=np.exp(-1j*Hfree*t)[None,:,None]
        formula=formula.reshape(-1,2)
        residual=float(np.linalg.norm(direct-formula))
        assert residual<2e-11
        rho=reduced_choi(direct,len(xs),nf,nb)
        assert abs(np.trace(rho)-1)<1e-12
        assert min(np.linalg.eigvalsh(rho))>-1e-12
        Es=float(np.trace(direct.conj().T@(diags(np.tile(E,len(xs)))@direct)).real/2)
        Er=float(np.trace(direct.conj().T@(diags(np.tile(ER,len(xs)))@direct)).real/2)
        Ec=float(np.trace(direct.conj().T@(Hhist@direct)).real/2)
        balance=abs(Es+Er-Es0-ER0)
        assert balance<2e-11 and abs(Ec-Ec0)<2e-11
        rows.append({'t':t,'direct_full_exponential_vs_gauge_isometry_error':residual,
                     'system_energy':Es,'battery_energy':Er,'clock_program_energy':Ec,
                     'free_energy_balance_residual':balance,'clock_program_energy_change':abs(Ec-Ec0)})
    return {'scope':'Complete finite qubit, three flags, one battery, and clock; two input columns include a reference-uniform isometry comparison',
            'joint_dimension':Htotal.shape[0],'clock_dimension':len(xs),'battery_dimension':nb,
            'Hermiticity_residual':hermerr,'free_energy_commutator_residual':commerr,
            'prefix_telescoping_residuals':prefix_errors,'naive_double_counting_isometry_defect':double_count_difference,
            'initial_resource_energies':{'battery':ER0,'clock_program_above_ground':Ec0},'rows':rows,
            'positivity_basis':'Exact unitary gauge of a positive path Hamiltonian plus nonnegative diagonal free energy; no numerical eigenvalue assertion substitutes for this argument'}


if __name__=='__main__':
    result={'exact_clock_moments':exact_moments(),'physical_time_position_controls':position_controls(),
            'complete_autonomous_matrix_control':complete_autonomous_control(),
            'all_assertions_passed':True,'independence':'Author consistency controls, not independent evidence'}
    (HERE/'CLOCK_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
