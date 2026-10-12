"""Exterior determinant and Fourier-projector route; no author imports."""
import json,itertools,sys
import numpy as np
from scipy.integrate import quad

TOL=2e-12
rows=[]
def emit(name,ok,**data):
    row=dict(name=name,ok=bool(ok),**data);rows.append(row);print(json.dumps(row),flush=True)
def annih(N,j):
    A=np.zeros((1<<N,1<<N),complex)
    for b in range(1<<N):
        if (b>>j)&1:A[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
    return A
def exterior(U):
    N=len(U);d=1<<N;F=np.zeros((d,d),complex);F[0,0]=1
    subsets=[tuple(j for j in range(N) if (b>>j)&1) for b in range(d)]
    for b,J in enumerate(subsets):
        if not J:continue
        for a,I in enumerate(subsets):
            if len(I)==len(J):F[a,b]=np.linalg.det(U[np.ix_(I,J)])
    return F
def nrm(A):return float(np.linalg.norm(A,ord=2))
for Nc in (2,3):
    N=2*Nc;d=1<<Nc;D=d*d
    U=np.zeros((N,N))
    for j in range(Nc):
        U[2*j,j]=U[2*j+1,j]=1/np.sqrt(2)
        U[2*j,Nc+j]=1/np.sqrt(2);U[2*j+1,Nc+j]=-1/np.sqrt(2)
    F=exterior(U)
    emit('exterior_unitarity',nrm(F.conj().T@F-np.eye(D))<TOL,coarse_sites=Nc,residual=nrm(F.conj().T@F-np.eye(D)))
    def embed(A):return F@np.kron(np.eye(d),A)@F.conj().T
    Ks=[F.conj().T[q*d:(q+1)*d,:]/np.sqrt(d) for q in range(d)]
    def channel(A):return sum((K@A@K.conj().T for K in Ks),np.zeros((d,d),complex))
    def bad_channel(A):return sum((A[q*d:(q+1)*d,q*d:(q+1)*d] for q in range(d)),np.zeros((d,d),complex))/d
    e=[]
    for j in range(Nc):
        a=annih(Nc,j)
        e.append(nrm(embed(a)-(annih(N,2*j)+annih(N,2*j+1))/np.sqrt(2)))
    emit('exterior_vs_retained_annihilator',max(e)<TOL,coarse_sites=Nc,max_residual=max(e))
    errors=[];baderrors=[];unnormalized=[]
    for p in range(d):
        for q in range(d):
            A=np.zeros((d,d));A[p,q]=1;B=embed(A)
            errors.append(nrm(channel(B)-A));baderrors.append(nrm(bad_channel(B)-A));unnormalized.append(nrm(d*channel(B)-A))
    emit('trace_left_inverse_all_matrix_units',max(errors)<TOL,coarse_sites=Nc,count=d*d,max_residual=max(errors))
    emit('mutation_wrong_trace_basis_detected',max(baderrors)>0.1,coarse_sites=Nc,max_residual=max(baderrors))
    emit('mutation_unnormalized_trace_detected',max(unnormalized)>0.1,coarse_sites=Nc,max_residual=max(unnormalized))
    unit=nrm(sum((K@K.conj().T for K in Ks),np.zeros((d,d),complex))-np.eye(d))
    emit('kraus_unitality',unit<TOL,coarse_sites=Nc,residual=unit)
    parity_f=np.diag([(-1)**b.bit_count() for b in range(D)])
    parity_c=np.diag([(-1)**b.bit_count() for b in range(d)])
    test=np.diag(np.arange(D,dtype=float)/D)+0.3*(annih(N,0).conj().T@annih(N,N-1)+annih(N,N-1).conj().T@annih(N,0))
    out=channel(test)
    emit('even_parity_preserved',nrm(out@parity_c-parity_c@out)<TOL,coarse_sites=Nc,residual=nrm(out@parity_c-parity_c@out))
    b0=sum(U[j,Nc]*annih(N,j) for j in range(N));b1=sum(U[j,Nc+1]*annih(N,j) for j in range(N))
    C=(b0+b0.conj().T)@(b1+b1.conj().T)
    emit('complement_nonmultiplicativity',nrm(channel(C))<TOL and nrm(channel(C@C)+np.eye(d))<TOL,coarse_sites=Nc,image_norm=nrm(channel(C)),square_image_plus_identity=nrm(channel(C@C)+np.eye(d)))
    if Nc==2:
        # Choi from Kraus vectors, independently also compare block reconstruction.
        Ch=np.zeros((D*d,D*d),complex)
        for K in Ks:
            vec=K.T.reshape(-1);Ch+=np.outer(vec,vec.conj())
        lo=float(np.linalg.eigvalsh(Ch).min())
        direct=np.zeros_like(Ch)
        for p in range(D):
            for q in range(D):
                A=np.zeros((D,D));A[p,q]=1
                direct[p*d:(p+1)*d,q*d:(q+1)*d]=channel(A)
        emit('choi_positive_and_formula_matches',lo>-TOL and nrm(Ch-direct)<TOL,min_eigenvalue=lo,block_residual=nrm(Ch-direct))

def params(m,v,a):
    sigma=np.sqrt(m*m/4+v*v/(a*a));return sigma/2+m/4,sigma/2-m/4
def integral_projector(g,J,weighted):
    k=2*np.pi*np.arange(32768)/32768-np.pi
    off=2j*(g-J*np.exp(-1j*k));E=np.abs(off)
    P12=off/(2*E)
    child=(1+np.exp(-1j*k))/np.sqrt(2) if weighted else np.ones_like(k)
    return complex(np.mean(-1j*np.conj(child)*2*P12*child))
def scalar_quad(g,J,weighted):
    r=J/g
    f=lambda k:((1+np.cos(k)) if weighted else 1)*(1-r*np.cos(k))/np.sqrt(1-2*r*np.cos(k)+r*r)
    value,error=quad(f,-np.pi,np.pi,epsabs=2e-13,epsrel=2e-13,limit=250)
    return value/(2*np.pi),error/(2*np.pi)
for m,v,a in [(6,2,1),(1,1,1),(3,2,.7),(6,0,1)]:
    g,J=params(m,v,a);gf,Jf=params(m,v,a/2)
    coarse=integral_projector(g,J,False);fine=integral_projector(gf,Jf,True)
    cquad,ce=scalar_quad(g,J,False);fquad,fe=scalar_quad(gf,Jf,True)
    err=max(abs(coarse-cquad),abs(fine-fquad))
    emit('Fourier_projector_vs_scalar_quadrature',err<TOL,m=m,v=v,a=a,coarse=coarse.real,fine=fine.real,imaginary=max(abs(coarse.imag),abs(fine.imag)),max_difference=err,quad_error_max=max(ce,fe))
    emit('fixed_refinement_state_discrepancy' if v else 'degenerate_v_zero_survivor',(fine.real<coarse.real-1e-5) if v else abs(fine-coarse)<TOL,m=m,v=v,a=a,coarse_minus_fine=coarse.real-fine.real)
    wrong_negative=-fine.real
    wrong_weight=integral_projector(gf,Jf,False).real
    emit('wrong_projector_fails_moment_equality',abs(wrong_negative-fine.real)>0.1,m=m,v=v,a=a,residual=abs(wrong_negative-fine.real))
    if v:
        emit('wrong_weight_fails_moment_equality',abs(wrong_weight-fine.real)>1e-5,m=m,v=v,a=a,residual=abs(wrong_weight-fine.real))
        emit('weak_inequality_survives_wrong_weight',wrong_weight<coarse.real,m=m,v=v,a=a,reason='A strict state inequality alone does not verify the child filter.')
emit('all_numerical_predicates',all(x['ok'] for x in rows),predicate_count=len(rows),tolerance=TOL)
raise SystemExit(0 if all(x['ok'] for x in rows) else 1)
