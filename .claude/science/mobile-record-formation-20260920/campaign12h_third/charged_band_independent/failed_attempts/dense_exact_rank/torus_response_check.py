"""Independent cubic incidence, relaxed response, and harmonic/axis-mode controls."""
from pathlib import Path
from itertools import product,combinations
from datetime import datetime,timezone
import hashlib,json
import numpy as np
import sympy as s
from scipy.linalg import null_space
HERE=Path(__file__).resolve().parent
OUT=HERE/'TORUS_RESPONSE_RESULTS.json';assert not OUT.exists()

def geometry(d,L):
    vertices=list(product(range(L),repeat=d));vid={x:i for i,x in enumerate(vertices)}
    def plus(x,i):
        y=list(x);y[i]=(y[i]+1)%L;return tuple(y)
    edges=[(x,i) for x in vertices for i in range(d)];ei={e:k for k,e in enumerate(edges)}
    As=[x for x in vertices if sum(x)%2==0];ai={x:i for i,x in enumerate(As)}
    plaquettes=[(x,i,j) for x in vertices for i,j in combinations(range(d),2)]
    B=np.zeros((len(vertices),len(edges)),int)
    for k,(x,i) in enumerate(edges):B[vid[x],k]=1;B[vid[plus(x,i)],k]=-1
    curl=np.zeros((len(plaquettes),len(edges)),int)
    two=np.zeros_like(curl);diag=np.zeros((len(As),len(plaquettes)),int)
    for p,(x,i,j) in enumerate(plaquettes):
        cycle=[x,plus(x,i),plus(plus(x,i),j),plus(x,j)]
        legs=[(ei[(x,i)],1),(ei[(plus(x,i),j)],1),(ei[(plus(x,j),i)],-1),(ei[(x,j)],-1)]
        for e,sg in legs:curl[p,e]=sg
        if sum(x)%2:
            cycle=cycle[1:]+cycle[:1];legs=legs[1:]+legs[:1]
        a,c=cycle[0],cycle[2]
        diag[ai[a],p]=1;diag[ai[c],p]=-1
        for k,(e,sg) in enumerate(legs):two[p,e]=sg*(1 if k<2 else -1)
    select=np.zeros((len(As),len(vertices)),int)
    for x,k in ai.items():select[k,vid[x]]=1
    assert np.array_equal(curl@B.T,np.zeros((len(plaquettes),len(vertices)),int))
    assert np.array_equal(two@B.T,2*diag.T@select)
    return vertices,edges,As,B,curl,two,diag

all_results=[]
for d,L in [(2,6),(3,6)]:
    vertices,edges,As,B,curl,two,diag=geometry(d,L)
    n=len(As);pe=(n-2)/(2*(n-1));po=n/(2*(n-1))
    reduced=diag[:-1,:];inv=np.linalg.inv(reduced@reduced.T)
    projection=np.eye(len(curl))-reduced.T@inv@reduced
    Q=pe*curl.T@curl+po*two.T@projection@two
    assert np.max(np.abs(Q-Q.T))<1e-12
    gauge_error=float(np.max(np.abs(Q@B.T)))
    assert gauge_error<5e-12
    harmonics=[]
    for i in range(d):
        f=np.array([1 if axis==i else 0 for x,axis in edges],float)
        expected=4*po*(d-1)
        assert np.max(np.abs(diag@two@f))<1e-12
        err=float(np.max(np.abs(Q@f-expected*f)))
        assert err<5e-12
        harmonics.append({'direction':i,'quadratic_eigenvalue':expected,'residual':err})
    modes=[]
    for mode in (1,2,3):
        k=2*np.pi*mode/L
        f=np.array([np.exp(1j*k*x[0]) if axis==1 else 0 for x,axis in edges])
        expected=4*(po*(d-1)-np.sin(k/2)**2/(n-1))
        err=float(np.max(np.abs(Q@f-expected*f)))
        assert err<8e-12
        assert np.max(np.abs(B@f))<1e-12
        assert np.max(np.abs(diag@two@f))<1e-12
        modes.append({'wavevector':[mode]+[0]*(d-1),'polarization':1,'quadratic_eigenvalue':expected,
                      'frequency_over_omega0':float(2*np.sqrt(expected)),'residual':err})
    entry={'dimension':d,'period':L,'vertices':len(vertices),'links':len(edges),'A_sites':n,
           'plaquettes':len(curl),'gauge_and_two_path_incidence_identities_exact_integer':True,
           'p_equal':str(s.Rational(n-2,2*(n-1))),'p_opposite':str(s.Rational(n,2*(n-1))),
           'gauge_response_residual':gauge_error,'harmonic_controls':harmonics,'axis_mode_controls':modes}
    if d==2:
        Bs=s.Matrix(B);Cs=s.Matrix(curl);Ts=s.Matrix(two);Ds=s.Matrix(diag)
        Dr=Ds[:-1,:]
        Pis=s.eye(len(curl))-Dr.T*(Dr*Dr.T).inv()*Dr
        Qs=s.Rational(n-2,2*(n-1))*Cs.T*Cs+s.Rational(n,2*(n-1))*Ts.T*Pis*Ts
        assert Qs*Bs.T==s.zeros(len(edges),len(vertices))
        assert Qs.rank()==len(edges)-len(vertices)+1
        assert Ds.rank()==n-1 and Cs.rank()==len(edges)-len(vertices)+1-d
        for i in range(d):
            f=s.Matrix([1 if axis==i else 0 for x,axis in edges])
            assert Qs*f==s.Rational(2*n*(d-1),n-1)*f
        roots=[s.Integer(1),s.Rational(1,2)+s.I*s.sqrt(3)/2,-s.Rational(1,2)+s.I*s.sqrt(3)/2,
               -s.Integer(1),-s.Rational(1,2)-s.I*s.sqrt(3)/2,s.Rational(1,2)-s.I*s.sqrt(3)/2]
        exact_modes=[]
        for mode in (1,2,3):
            f=s.Matrix([roots[(mode*x[0])%L] if axis==1 else 0 for x,axis in edges])
            expected=s.Rational(2*n*(d-1),n-1)-4*s.sin(s.pi*mode/L)**2/(n-1)
            assert (Qs*f-expected*f).applyfunc(s.simplify)==s.zeros(len(edges),1)
            exact_modes.append(str(s.simplify(expected)))
        ortho=null_space(B.astype(float))
        eig=np.linalg.eigvalsh(ortho.T@Q@ortho)
        assert np.min(eig)>0
        # A selected neutral charge vector tests the exact orthogonal electric decomposition.
        q=np.zeros(len(vertices));
        for i,x in enumerate(As):q[vertices.index(x)]=1 if i<n//2 else -1
        electric=B.T@np.linalg.pinv(B@B.T)@q
        coulomb=float(q@np.linalg.pinv(B@B.T)@q)
        assert np.max(np.abs(B@electric-q))<1e-12
        assert abs(electric@electric-coulomb)<1e-12
        entry.update({'exact_A_graph_rank':n-1,'exact_curl_rank':len(edges)-len(vertices)+1-d,
                      'exact_Q_rank':len(edges)-len(vertices)+1,'exact_harmonic_eigenvalue':str(s.Rational(2*n*(d-1),n-1)),
                      'exact_axis_eigenvalues':exact_modes,
                      'numeric_physical_eigenvalues':[float(x) for x in eig],
                      'selected_charge_Coulomb_energy':coulomb,'Gauss_minimal_electric_residual':float(np.max(np.abs(B@electric-q)))})
    else:
        entry['scope']='Integer incidence identities and numerical harmonic/axis-mode residuals; no symbolic 648x648 rank computation.'
    all_results.append(entry)
out={'created_utc':datetime.now(timezone.utc).isoformat(),'source':{'path':str(Path(__file__).resolve()),
 'sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},'controls':all_results,
 'convention':'Q is the coefficient of angle squared in the relaxed energy; the real Hessian is 2Q. Frequencies are 2 omega0 sqrt(eigenvalue(Q)).',
 'scope':'Physical quotient response matrices on allowed cubic tori. No all-neutral-configurations diagonalization or thermodynamic conclusion.'}
OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
