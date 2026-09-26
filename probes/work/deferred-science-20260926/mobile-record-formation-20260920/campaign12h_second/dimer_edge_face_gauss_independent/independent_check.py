#!/usr/bin/env python3
"""Independent incidence and squeezed finite-block controls, before author code."""
from pathlib import Path
from itertools import product,permutations
import json,math
import numpy as np
import sympy as s
from scipy import sparse
from scipy.sparse.linalg import expm_multiply
from scipy.linalg import eigh
HERE=Path(__file__).resolve().parent

def matrices(L):
    pts=list(product(range(L),repeat=3));ix={x:i for i,x in enumerate(pts)};V=len(pts)
    D=[]
    for j in range(3):
        r=[];c=[];v=[]
        for x in pts:
            y=list(x);y[j]=(y[j]+1)%L
            r.extend([ix[x],ix[x]]);c.extend([ix[tuple(y)],ix[x]]);v.extend([1,-1])
        D.append(sparse.csr_matrix((v,(r,c)),shape=(V,V),dtype=int))
    blocks=[[None]*3 for _ in range(3)]
    Z=sparse.csr_matrix((V,V),dtype=int)
    for i,k in product(range(3),repeat=2):
        blocks[i][k]=sum((int(s.LeviCivita(i,j,k))*D[j] for j in range(3)),Z.copy())
    C=sparse.bmat(blocks,format='csr');d0=sparse.vstack(D,format='csr');d2=sparse.hstack(D,format='csr')
    return pts,ix,d0,C,d2

def covariance(pts,ix,d0,C,d2,L):
    V=len(pts);count=0
    for p in permutations(range(3)):
        for signs in product([-1,1],repeat=3):
            R=np.zeros((3,3),int)
            for i in range(3):R[p[i],i]=signs[i]
            if round(np.linalg.det(R))!=1:continue
            er=[];ec=[];ev=[];fr=[];fc=[];fv=[];vr=[];vc=[];cr=[];cc=[]
            for x in pts:
                rx=R@np.array(x);vr.append(ix[tuple(rx%L)]);vc.append(ix[x])
                cube=rx.copy()
                for a in range(3):
                    if signs[a]<0:cube[p[a]]-=1
                cr.append(ix[tuple(cube%L)]);cc.append(ix[x])
                for a in range(3):
                    edge=rx.copy()
                    if signs[a]<0:edge[p[a]]-=1
                    er.append(p[a]*V+ix[tuple(edge%L)]);ec.append(a*V+ix[x]);ev.append(signs[a])
                    face=rx.copy()
                    for b in range(3):
                        if b!=a and signs[b]<0:face[p[b]]-=1
                    fr.append(p[a]*V+ix[tuple(face%L)]);fc.append(a*V+ix[x]);fv.append(signs[a])
            RE=sparse.csr_matrix((ev,(er,ec)),shape=C.shape);RF=sparse.csr_matrix((fv,(fr,fc)),shape=C.shape)
            R0=sparse.csr_matrix((np.ones(V,int),(vr,vc)),shape=(V,V));R3=sparse.csr_matrix((np.ones(V,int),(cr,cc)),shape=(V,V))
            assert (d0@R0-RE@d0).nnz==0
            assert (C@RE-RF@C).nnz==0
            assert (d2@RF-R3@d2).nnz==0
            count+=1
    return count

def incidence_controls():
    rows=[]
    for L in [3,4]:
        pts,ix,d0,C,d2=matrices(L);V=L**3
        assert (C@d0).nnz==0 and (d2@C).nnz==0
        assert np.all(np.asarray(abs(C).sum(axis=1)).ravel()==4)
        rc=s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix(C.toarray())).rank()
        r0=s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix(d0.toarray())).rank()
        r2=s.polys.matrices.DomainMatrix.from_Matrix(s.Matrix(d2.toarray())).rank()
        assert (rc,r0,r2)==(2*V-2,V-1,V-1)
        cov=covariance(pts,ix,d0,C,d2,L)
        lam={};maxres=0.
        for q in product(range(L),repeat=3):
            k=2*np.pi*np.array(q)/L;d=np.exp(1j*k)-1
            X=np.array([[0,-d[2],d[1]],[d[2],0,-d[0]],[-d[1],d[0],0]])
            value=float(np.vdot(d,d).real);res=np.linalg.norm(X.conj().T@X-(value*np.eye(3)-np.outer(d,d.conj())))
            maxres=max(maxres,float(res));assert res<1e-13
            z=s.simplify(sum(4*s.sin(s.pi*s.Rational(a,L))**2 for a in q));lam[str(z)]=lam.get(str(z),0)+1
        assert lam['0']==1
        wrong=(C-C.T)@C;coo=wrong.tocoo();assert coo.nnz
        u,v,val=int(coo.row[0]),int(coo.col[0]),int(coo.data[0])
        # E=e_u, Q=e_v: the wrongly unadjointed electric law changes energy by val.
        assert int(((C.T-C.T)@C)[u,v])==0
        rows.append(dict(side=L,vertices=V,curl_rank=rc,gradient_rank=r0,divergence_rank=r2,
                         real_transverse_modes=rc,gauge_modes=3*V-rc,proper_cubical_chain_map_controls=cov,
                         squared_frequency_inventory=lam,max_symbol_Gram_residual=maxres,
                         wrong_adjoint_energy_countercontrol=dict(E_edge=u,Q_edge=v,wrong_energy_derivative=val),
                         sufficient_HK_norm_constant_times_K=f'{17*3*V}/4 * K'))
    return rows

def local_spin():
    rows=[]
    for K in [1,2,3,4]:
        a=s.zeros(K+1)
        for n in range(1,K+1):a[n-1,n]=s.sqrt(s.Rational(n*(K-n+1),K))
        Q=(a+a.T)/s.sqrt(2);P=s.I*(a.T-a)/s.sqrt(2);N=s.diag(*range(K+1))
        assert a*a.T-a.T*a==s.eye(K+1)-2*N/K
        eig=Q.eigenvals();assert max(s.simplify(v*v) for v in eig)==s.Rational(K,2)
        rows.append(dict(K=K,exact_Q_norm_squared=str(s.Rational(K,2)),exact_finite_CCR=True))
    # A two-edge incidence row C=(1,-1), d0=(1,1), witnesses the finite-K defect.
    K=1;a=s.Matrix([[0,1],[0,0]]);Q=(a+a.T)/s.sqrt(2);P=s.I*(a.T-a)/s.sqrt(2);I=s.eye(2)
    P0=s.kronecker_product(P,I);P1=s.kronecker_product(I,P);B=s.kronecker_product(Q,I)-s.kronecker_product(I,Q)
    H=(P0*P0+P1*P1+B*B)/2;G=P0+P1;comm=H*G-G*H
    norm2=s.simplify(s.trace(comm.conjugate().T*comm));assert norm2>0
    return dict(spin_norm_rows=rows,two_edge_finite_Gauss_commutator_Frobenius_squared=str(norm2))

def squeezed_moments(mu):
    return [1,mu,3*mu**2+2*mu,15*mu**3+18*mu**2+4*mu,105*mu**4+180*mu**3+84*mu**2+8*mu]

def state_and_hamiltonian(K):
    eps=K**(-1/6);omega=math.sqrt(2);rT=(1-omega)/(1+omega);rZ=(1-eps*eps)/(1+eps*eps)
    diag=(rT+rZ)/2;off=(rZ-rT)/2;coeff=np.zeros((K+1,K+1));coeff[0,0]=((1-rT*rT)*(1-rZ*rZ))**.25
    for m in range(2,K+1,2):coeff[0,m]=diag*math.sqrt((m-1)/m)*coeff[0,m-2]
    for n in range(1,K+1):
        for m in range(K+1):
            coeff[n,m]=((diag*math.sqrt(n-1)*coeff[n-2,m] if n>=2 else 0)+(off*math.sqrt(m)*coeff[n-1,m-1] if m>=1 else 0))/math.sqrt(n)
    alpha=np.linalg.norm(coeff);assert alpha<=1+1e-14;phi=coeff.ravel()/alpha
    low=sparse.diags([math.sqrt(n*(1-(n-1)/K)) for n in range(1,K+1)],1,shape=(K+1,K+1),format='csr')
    Q=(low+low.T)/math.sqrt(2);P=1j*(low.T-low)/math.sqrt(2);I=sparse.eye(K+1,format='csr')
    P0=sparse.kron(P,I,format='csr');P1=sparse.kron(I,P,format='csr');B=sparse.kron(Q,I,format='csr')-sparse.kron(I,Q,format='csr')
    H=(P0@P0+P1@P1+B@B)/2;G=(P0+P1)/math.sqrt(2)
    assert (H-H.getH()).nnz==0
    muT=(omega+1/omega-2)/4;muZ=(eps**2+eps**-2-2)/4;mT=squeezed_moments(muT);mZ=squeezed_moments(muZ)
    total=[sum(math.comb(n,j)*mT[j]*mZ[n-j] for j in range(n+1)) for n in range(5)]
    weighted=math.sqrt(sum(math.comb(4,j)*total[j] for j in range(5)))
    tail=math.sqrt(max(0,1-alpha**2));bound=weighted/K**2
    assert tail<=bound+1e-13
    energy=float(np.vdot(phi,H@phi).real);ET=omega/2;data=[]
    ep,UP=eigh(P.toarray())
    for t in [0.,.5,1.]:
        evolved=expm_multiply(-1j*t*H,phi);et=float(np.vdot(evolved,H@evolved).real)
        assert abs(et-energy)<2e-12
        gauss=float(np.vdot(G@evolved,G@evolved).real)
        transverse_e=(P0-P1)/math.sqrt(2)
        transverse=float(np.vdot(transverse_e@evolved,transverse_e@evolved).real)
        magnetic=float(np.vdot(B@evolved,B@evolved).real)
        assert abs((transverse+magnetic+gauss)/2-et)<2e-12
        chars=[]
        for z in [.25,1.,3.]:
            w=UP@np.diag(np.exp(-1j*z*ep/math.sqrt(2)))@UP.conj().T
            transformed=w@evolved.reshape((K+1,K+1))@w.T
            chi=np.vdot(evolved,transformed.ravel())
            chars.append(dict(z=z,characteristic_real=float(chi.real),characteristic_imag=float(chi.imag),distance_from_reduced_value=float(abs(chi-1))))
        data.append(dict(time=t,energy=et,gauge_mean_square=gauss,K_one_sixth_scaled_gauge=K**(1/6)*gauss,Gauss_characteristics=chars))
    return dict(K=K,epsilon=eps,physical_dimension=(K+1)**2,projection_norm=alpha,projection_tail_norm=tail,
                Markov_tail_bound=bound,weighted_number_norm=weighted,epsilon_four_scaled_number_norm=eps**4*weighted,
                canonical_energy=ET+eps**2/4,transverse_energy=ET,initial_physical_energy=energy,
                K_one_third_scaled_energy_error=K**(1/3)*abs(energy-ET),evolutions=data)

def main():
    result=dict(incidence=incidence_controls(),spin=local_spin(),two_edge_squeezed_controls=[])
    print(json.dumps(result,indent=2),flush=True)
    for K in [2,4,8,16,32,64]:
        row=state_and_hamiltonian(K);result['two_edge_squeezed_controls'].append(row);print(json.dumps(row),flush=True)
    result['two_edge_scope']='C=(1,-1), one transverse and one gauge coordinate. This is an independent finite-dimensional state/projection/Hamiltonian control, not the full cubic lattice simulation. Its Gaussian Fock coefficients have analytic infinite-space normalization; no canonical evolution cutoff is used.'
    result['weak_convergence_countercontrol']='X_R=R with probability R^-2 and zero otherwise has characteristic function converging uniformly to 1, while E X_R^2=1. Thus characteristic convergence or bounded energy alone would not replace the addendum target-energy argument.'
    (HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
