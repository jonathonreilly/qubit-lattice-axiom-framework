"""Literal finite spin Q and matrix conjugation, separate from candidate B."""
import numpy as np
from scipy.linalg import expm
from reporting import arguments,Book

def kron_all(ms):
    out=np.array([[1.+0j]])
    for m in ms:out=np.kron(out,m)
    return out

def matrices(L,R,a,g,J):
    eye=np.eye(2,dtype=complex)
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1.])
    N=R-L+1
    site=lambda p,n:kron_all([p if j==n-L else eye for j in range(N)])
    xs=[site(X,n) for n in range(L,R+1)]
    ys=[site(Y,n) for n in range(L,R+1)]
    zs=[site(Z,n) for n in range(L,R+1)]
    Q=np.zeros((2**N,2**N),complex)
    for j,n in enumerate(range(L,R)):
        Q+=a*n*(-J*xs[j]@xs[j+1]-(g/2)*(zs[j]+zs[j+1]))
    gammas=[];tail=np.eye(2**N,dtype=complex)
    for j in range(N):
        gammas.extend([tail@xs[j],tail@ys[j]])
        tail=tail@zs[j]
    return Q,gammas

def field(gs,f):return sum((z*g for z,g in zip(f,gs)),np.zeros_like(gs[0]))

def main():
    args,c=arguments();b=Book('actual_spin',args)
    a=.31;m=.8;v=1.3
    # Reference couplings independently solve g-J=m/2 and 4gJ=v²/a².
    J=(np.sqrt(m*m+4*v*v/(a*a))-m)/4;g=J+m/2
    cg,cJ=c.couplings(a,m,v)
    b.check('supplied_family',abs(cg-g)+abs(cJ-J),2e-14)
    for L,R in [(-2,2),(1,5)]:
        Q,gs=matrices(L,R,a,g,J);N=R-L+1;dim=2**N
        # Actual Hermitian coefficient matrix is i times row action of i[Q,gamma].
        actual=np.empty((2*N,2*N),complex)
        for j,gj in enumerate(gs):
            deriv=1j*(Q@gj-gj@Q)
            actual[j,:]=[1j*np.trace(gk@deriv)/dim for gk in gs]
        indices=np.arange(L,R+1)
        pred=c.boost_matrix(indices,a,g,J,finite_open=True).toarray()
        raw=c.boost_matrix(indices,a,g,J,finite_open=False).toarray()
        b.check('literal_full_matrix',np.linalg.norm(pred-actual),2e-11,L=L,R=R)
        b.check('padded_interior_matrix',np.linalg.norm(raw[2:-2,2:-2]-actual[2:-2,2:-2]),2e-11,L=L,R=R)
        b.check('self_adjoint_matrix',np.linalg.norm(pred-pred.conj().T),2e-11,L=L,R=R)
        for s in [-.27,.19]:
            f=np.zeros(2*N);h=np.zeros(2*N);f[2:6]=[.7,-.1,.4,.2];h[4:8]=[-.2,.8,.1,-.3]
            obs=field(gs,f)@field(gs,h)
            unit=expm(-1j*s*Q)
            actual_obs=unit@obs@unit.conj().T
            of=expm(c.BOOST_SIGN*1j*s*pred)@f
            oh=expm(c.BOOST_SIGN*1j*s*pred)@h
            proposed_obs=field(gs,of)@field(gs,oh)
            b.check('actual_even_flow',np.linalg.norm(proposed_obs-actual_obs),3e-10,L=L,R=R,s=s)
    # One-site reference fixes the sign without a lattice continuum comparison.
    n=2;g=1.1;a=.4;s=.3
    _,gs=matrices(n,n,a,g,0.)
    X,Y=gs;Z=-1j*X@Y
    Q=-a*g*(n-.5)*Z
    actual=expm(-1j*s*Q)@X@expm(1j*s*Q)
    mat=c.boost_matrix([n],a,g,0.,finite_open=False).toarray()
    predicted=field(gs,expm(c.BOOST_SIGN*1j*s*mat)@np.array([1.,0.]))
    b.check('onsite_clock',np.linalg.norm(actual-predicted),2e-13)
    # Independent endpoint embedding: old two-site matrices versus new three-site.
    _,old=matrices(0,1,1.,1.,0.)
    _,new=matrices(-1,1,1.,1.,0.)
    for degree in [1,2,3,4]:
        before=np.eye(4,dtype=complex);after=np.eye(8,dtype=complex)
        for j in range(degree):before=before@old[j];after=after@new[j+2]
        error=np.linalg.norm(after-np.kron(np.eye(2),before),ord=2)
        if degree%2==0:b.check('even_endpoint_independence',error,1e-13,degree=degree)
        else:b.check('odd_endpoint_nonlocal_witness',abs(error-2),1e-13,degree=degree,witness=error)
    b.finish('Reference uses literal finite Pauli Q, commutators/traces, and full spin exponential. Padded rows alone do not test endpoint corrections. Frobenius residuals dominate operator norm. Odd fields are only reference matrices; tested odd endpoint mismatch is a limitation, not a local spin identification.')

if __name__=='__main__':main()
