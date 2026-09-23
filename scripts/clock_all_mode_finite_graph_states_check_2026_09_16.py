#!/usr/bin/env python3
"""Theta-product coercivity and an exact charged-ring transfer diagnostic.

All finite tails and eigensystems are floating diagnostics, not interval proofs.
The charged ring has one mobile particle and one static opposite charge at0.
"""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS = ['docs/CLOCK_VARIANCE_CALIBRATED_JOINT_ROTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/CLOCK_ALL_MODE_COERCIVITY_FINITE_GRAPH_STATES_BOUNDED_THEOREM_NOTE_2026-09-16.md']
import hashlib,json,math,time
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_INPUT_TEXT = {p: (_REPO_ROOT / p).read_text() for p in AUDIT_INPUT_PATHS}
assert 'clock_variance_calibrated_joint_rotor_transfer_bounded_theorem_note_2026-09-16' in _INPUT_TEXT['docs/CLOCK_VARIANCE_CALIBRATED_JOINT_ROTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-16.md']
assert 'clock_all_mode_coercivity_finite_graph_states_bounded_theorem_note_2026-09-16' in _INPUT_TEXT['docs/CLOCK_ALL_MODE_COERCIVITY_FINITE_GRAPH_STATES_BOUNDED_THEOREM_NOTE_2026-09-16.md']
assert 'v(c)=delta g² N²/(4pi²)' in _INPUT_TEXT['docs/CLOCK_VARIANCE_CALIBRATED_JOINT_ROTOR_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-16.md']
assert 'I-T=(I-M^2)+M(I-Q)M' in _INPUT_TEXT['docs/CLOCK_ALL_MODE_COERCIVITY_FINITE_GRAPH_STATES_BOUNDED_THEOREM_NOTE_2026-09-16.md']
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.special import logsumexp


def product_data(c):
    m=np.arange(1,max(3,math.ceil(32/c))+1,dtype=float)
    q=np.exp(-c*(2*m-1));a=4*q/(1+q)**2
    return a,float(a.sum()/2)


def jump_data(c):
    k=np.arange(-max(3,math.ceil(math.sqrt(60/c))),max(3,math.ceil(math.sqrt(60/c)))+1,dtype=float)
    p=np.exp(-c*k*k);p/=p.sum()
    return k,p,float(p@(k*k))


def log_character(c,h):
    a,_=product_data(c)
    return float(np.log1p(-a*np.sin(h/2)**2).sum())


def calibrate(delta,N,g):
    target=delta*g*g*N*N/(4*math.pi**2)
    lo=min(1.,1/(4*target));hi=max(1.,1/target)
    c=math.exp(brentq(lambda z:product_data(math.exp(z))[1]-target,math.log(lo),math.log(hi),xtol=2e-14))
    assert abs(jump_data(c)[2]/target-1)<3e-12
    return c


def theta_checks():
    rows=[]
    for c in [.003,.03,.3,1.,3.,10.,30.]:
        a,vp=product_data(c);k,p,vs=jump_data(c)
        assert abs(vp/vs-1)<2e-13
        for h in [.001,.1,.7,2.,math.pi]:
            lp=log_character(c,h)
            m=np.arange(-max(4,math.ceil(math.sqrt(60*c)/math.pi)),max(4,math.ceil(math.sqrt(60*c)/math.pi))+1,dtype=float)
            ld=float(logsumexp(-math.pi**2*(m+h/(2*math.pi))**2/c)-logsumexp(-math.pi**2*m*m/c))
            assert abs(lp-ld)<2e-8
            floor=2*vs*h*h/math.pi**2
            assert -lp>=floor*(1-2e-13)
            rows.append({'c':c,'h':h,'minus_log_character':-lp,'floor':floor,'product_vs_poisson_error':abs(lp-ld),'variance_relative_difference':abs(vp/vs-1)})
    for N in [4,5,16,17,64,65]:
        for power in [1,2,3]:
            delta=N**(-power);g=.7;c=calibrate(delta,N,g)
            for r in range(-N//2+(N%2),N//2+1):
                energy=-log_character(c,2*math.pi*r/N)/delta
                assert energy>=(2*g*g/math.pi**2)*r*r*(1-3e-12)
    return rows


def matter_matrix(phi,hop):
    h=np.eye(4,dtype=complex)*2*hop
    for j in range(3):h[j+1,j]=h[j,j+1]=-hop
    h[0,3]=-hop*np.exp(-1j*phi);h[3,0]=h[0,3].conjugate()
    assert eigh(h,eigvals_only=True).min()>-2e-14
    return h


def charged_transfer(N,delta,g,hop):
    c=calibrate(delta,N,g);theta=2*math.pi*np.arange(N)/N
    k,p,_=jump_data(c)
    # Direct integer jump sum, independent of the product eigenvalue formula.
    lam=np.array([p@np.cos(2*math.pi*r*k/N) for r in range(N)])
    direct=np.array([math.exp(log_character(c,2*math.pi*r/N)) for r in range(N)])
    assert max(abs(lam-direct))<2e-13
    qdiag=np.array([lam[(n-1)%N]**j*lam[n]**(4-j) for n in range(N) for j in range(4)])
    y=delta/(2*g*g);images=np.arange(-8,9);w=y**(images*images)
    b=np.cos(theta[:,None]*images)@w/w.sum()
    Mangle=np.zeros((4*N,4*N),dtype=complex)
    for s,phi in enumerate(theta):
        ev,u=eigh(matter_matrix(phi,hop));Mangle[4*s:4*s+4,4*s:4*s+4]=math.sqrt(b[s])*(u*np.exp(-delta*ev/2))@u.conj().T
    U=np.exp(2j*math.pi*np.outer(np.arange(N),np.arange(N))/N)/math.sqrt(N)
    F=np.kron(U,np.eye(4));M=F.conj().T@Mangle@F
    T=(M*qdiag[None,:])@M
    assert np.linalg.norm(T-T.conj().T)<2e-12
    # Noncommuting physical factors: this is not exp of their summed logarithms.
    comm=float(np.linalg.norm(M*qdiag[None,:]-qdiag[:,None]*M))
    # Resolve noncommutation above a norm-scaled roundoff threshold. Its size
    # tends to zero with delta and has no universal unit lower coefficient.
    assert comm>1000*np.finfo(float).eps*np.linalg.norm(M)*np.linalg.norm(qdiag)
    return T,comm


def full_physical_check(N,g,hop,delta):
    coords=np.indices((N,)*4).reshape(4,-1).T
    theta=2*math.pi*coords/N;total=theta.sum(axis=1);d=len(coords)
    basis=np.zeros((d,4,4*N),complex)
    for n in range(N):
        for j in range(4):
            basis[:,j,4*n+j]=np.exp(1j*(n*total-theta[:,:j].sum(axis=1)))/math.sqrt(d)
    flat=basis.reshape(4*d,4*N)
    assert np.linalg.norm(flat.conj().T@flat-np.eye(4*N))<2e-12
    y=delta/(2*g*g);images=np.arange(-8,9);w=y**(images*images)
    b=np.cos(total[:,None]*images)@w/w.sum()
    mult=np.empty((d,4,4),complex)
    for s,angles in enumerate(theta):
        h=np.eye(4,dtype=complex)*2*hop
        for j in range(4):
            h[(j+1)%4,j]=-hop*np.exp(-1j*angles[j]);h[j,(j+1)%4]=h[(j+1)%4,j].conjugate()
        ev,u=eigh(h);mult[s]=math.sqrt(b[s])*(u*np.exp(-delta*ev/2))@u.conj().T
    weighted=np.einsum('sij,sja->sia',mult,basis).reshape((N,)*4+(4,4*N))
    freq=np.fft.fftn(weighted,axes=(0,1,2,3),norm='ortho')
    c=calibrate(delta,N,g);k,p,_=jump_data(c)
    lam=np.array([p@np.cos(2*math.pi*r*k/N) for r in range(N)])
    diag=np.prod(lam[coords],axis=1).reshape((N,)*4)
    back=np.fft.ifftn(freq*diag[...,None,None],axes=(0,1,2,3),norm='ortho').reshape(d,4,4*N)
    actual=flat.conj().T@np.einsum('sij,sja->sia',mult,back).reshape(4*d,4*N)
    expected,_=charged_transfer(N,delta,g,hop)
    err=float(np.linalg.norm(actual-expected));assert err<3e-12
    # Integer-Gauss witness on every reduced basis label, not just dimension.
    for n in range(N):
        for j in range(4):
            electric=np.array([n-int(e<j) for e in range(4)])
            div=electric-np.roll(electric,1);charge=np.eye(4,dtype=int)[j]-np.eye(4,dtype=int)[0]
            assert np.array_equal(div,charge)
    return {'N':N,'full_dimension':4*d,'physical_dimension':4*N,'full_vs_reduced_transfer_error':err}


def rotor(Ncut,g,hop):
    ns=np.arange(-Ncut,Ncut+1);d=4*len(ns);H=np.zeros((d,d))
    def ix(n,j):return 4*(n+Ncut)+j
    for n in ns:
        for j in range(4):
            a=ix(n,j);H[a,a]=g*g/2*(j*(n-1)**2+(4-j)*n*n)+1/(g*g)+2*hop
            if n<Ncut:
                b=ix(n+1,j);H[a,b]=H[b,a]=-1/(2*g*g)
            if j<3:
                b=ix(n,j+1);H[a,b]=H[b,a]=-hop
            elif n>-Ncut:
                b=ix(n-1,0);H[a,b]=H[b,a]=-hop
    return H


def thermal(ev,u,t):
    w=np.exp(-t*ev);return (u*w)@u.conj().T,float(w.sum())


def charged_paths():
    g=.7;hop=.23;t=.8;cut=40
    H=rotor(cut,g,hop);ee,vv=eigh(H);ee2,vv2=eigh(rotor(cut+8,g,hop))
    assert np.max(abs(ee[:12]-ee2[:12]))<2e-12
    ref,Z=thermal(ee,vv,t);ref2,Z2=thermal(ee2,vv2,t)
    assert abs(Z-Z2)<2e-12
    rows=[]
    for power in [1,2,3]:
        errors=[]
        for N in [8,16,32,48,64]:
            delta=(.4 if power==1 else 2.)/N**power
            T,comm=charged_transfer(N,delta,g,hop);lam,u=eigh(T)
            assert lam.min()>-2e-13 and lam.max()<1+1e-13
            order=np.argsort(lam)[::-1];lam=lam[order];u=u[:,order]
            energy=-np.log(np.clip(lam,1e-300,1))/delta
            assert np.max(abs(energy[:8]-ee[:8]))<2.
            signed=np.where(np.arange(N)<N/2,np.arange(N),np.arange(N)-N)
            embed=np.zeros((4*(2*cut+1),4*N),complex)
            for r,n in enumerate(signed):
                for j in range(4):embed[4*(n+cut)+j,4*r+j]=1
            finite,z=thermal(energy,u,t);actual=embed@finite@embed.conj().T
            trace_error=float(np.abs(eigh(actual/z-ref/Z,eigvals_only=True)).sum())
            ground=embed@u[:,0];ground_overlap=float(abs(np.vdot(vv[:,0],ground))**2)
            errors.append(trace_error)
            rows.append({'power':power,'N':N,'delta':delta,'noncommuting_factor_norm':comm,'first_eight_energy_errors':(energy[:8]-ee[:8]).tolist(),'ground_overlap_squared':ground_overlap,'partition_function_error':z-Z,'gibbs_trace_norm_error':trace_error,'rotor_ground_gap':float(ee[1]-ee[0])})
        assert errors[-1]<errors[0]/6
        assert errors[-1]<.003
    return rows


def run():
    start=time.time();theta=theta_checks();physical=[full_physical_check(N,.7,.23,.03) for N in [3,4]];states=charged_paths()
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'theta_product_checks':theta,'full_physical_checks':physical,'charged_ring_states':states,'seconds':time.time()-start},indent=2))
    print("TOTAL: PASS=3 FAIL=0")
    print("N5 per_element: finite integer-Gaussian and Fourier-character values checked; see JSON parameter rows")
    print("N5 per_site: finite four-link ring configurations and explicit Gauss labels checked")
    print("N5 per_mode: only the finite sampled mode sets checked; analytical all-mode bounds are not executed")
    print("N5 per_block: finite mode/parameter families completed; see JSON rows")
    print("N5 lattice_wide: analytical joint-limit proof not executed; floating cutoffs are diagnostics")


if __name__=='__main__':run()
