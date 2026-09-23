"""Charged exchange potential: exact finite-spin-sector Hessian and cubic geometry.
This tests a finite-box potential band, not the full kinetic phase diagram.
"""
from pathlib import Path
from itertools import combinations,product
from datetime import datetime,timezone
import hashlib,json,math
import sympy as s
import numpy as np
from scipy.linalg import eigh,eigvalsh

HERE=Path(__file__).resolve().parent

def finite_graph(n,edges,theta,phi):
    words=[tuple(1 if i in up else -1 for i in range(n))
           for up in combinations(range(n),n//2)]
    idx={w:i for i,w in enumerate(words)};dim=len(words)
    H0=s.zeros(dim);H1=s.zeros(dim);H2=s.zeros(dim)
    D=s.zeros(len(edges),n)
    for e,(a,c) in enumerate(edges):
        D[e,a]=-1;D[e,c]=1
        X=theta[e]+phi[e]/2;Y=-theta[e]+phi[e]/2
        R0=s.zeros(dim);R1=s.zeros(dim);R2=s.zeros(dim)
        for col,w in enumerate(words):
            target=list(w);target[a],target[c]=target[c],target[a]
            row=idx[tuple(target)]
            phase=w[a]*X+w[c]*Y
            R0[row,col]=1;R1[row,col]=-s.I*phase;R2[row,col]=-phase**2
        H0-=R0+R0.T;H1-=R1+s.conjugate(R1.T);H2-=R2+R2.T
    u=s.ones(dim,1)/s.sqrt(dim);E0=-2*len(edges)
    assert H0*u==E0*u and s.simplify((u.T*H1*u)[0])==0
    qvec=s.Matrix(words)
    assert s.simplify(H1*u-2*s.I*qvec*D.T*s.Matrix(theta)/s.sqrt(dim))==s.zeros(dim,1)
    gap=H0-E0*s.eye(dim);P=u*u.T
    # The connected exchange graph makes this fixed-content kernel one-dimensional.
    assert gap.rank()==dim-1
    inv=(gap+P).inv()-P
    exact=s.simplify((u.T*H2*u)[0]-2*(s.conjugate((H1*u).T)*inv*(H1*u))[0])
    L=D.T*D;one=s.ones(n,n)/n;Lp=(L+one).inv()-one
    th=s.Matrix(theta);ph=s.Matrix(phi)
    predicted=s.simplify(s.Rational(n-2,n-1)*(ph.T*ph)[0]+
                        s.Rational(4*n,n-1)*(th.T*(s.eye(len(edges))-D*Lp*D.T)*th)[0])
    assert exact==predicted and exact>=0
    # Direct independent finite-angle diagonalization, without Taylor matrices.
    samples=[]
    def energy(tau):
        ham=np.zeros((dim,dim),dtype=complex)
        for e,(a,c) in enumerate(edges):
            R=np.zeros((dim,dim),dtype=complex)
            for col,w in enumerate(words):
                target=list(w);target[a],target[c]=target[c],target[a]
                phase=float(w[a]*(theta[e]+phi[e]/2)+w[c]*(-theta[e]+phi[e]/2))
                R[idx[tuple(target)],col]=np.exp(-1j*tau*phase)
            ham-=R+R.conj().T
        return float(eigvalsh(ham,subset_by_index=[0,0])[0])
    for tau in (.04,.02,.01):
        curvature=(energy(tau)+energy(-tau)-2*E0)/tau**2
        samples.append({'step':tau,'symmetric_ground_curvature':curvature,
                        'difference_from_exact':curvature-float(exact)})
    assert abs(samples[-1]['difference_from_exact'])<.002
    return {'sites':n,'edges':edges,'fixed_charge':0,'spin_sector_dimension':dim,
            'theta':list(map(str,theta)),'phi':list(map(str,phi)),
            'ground_energy':E0,'exact_fixed_sector_kernel_dimension':1,
            'exact_second_derivative':str(exact),'predicted_second_derivative':str(predicted),
            'H1_ground_one_magnon_identity':True,'direct_finite_angle_controls':samples}

def cubic(d,L):
    vv=list(product(range(L),repeat=d));vi={x:i for i,x in enumerate(vv)};V=len(vv)
    def sh(x,j):
        y=list(x);y[j]=(y[j]+1)%L;return tuple(y)
    ee=[(x,j) for x in vv for j in range(d)];ei={e:i for i,e in enumerate(ee)}
    ff=[(x,i,j) for x in vv for i in range(d) for j in range(i+1,d)]
    av=[x for x in vv if sum(x)%2==0];ai={x:i for i,x in enumerate(av)};n=len(av)
    G=np.zeros((len(ee),V),dtype=np.int64)
    C=np.zeros((len(ff),len(ee)),dtype=np.int64)
    Th2=np.zeros_like(C);D=np.zeros((len(ff),n),dtype=np.int64)
    for row,(x,i) in enumerate(ee):G[row,vi[x]]=-1;G[row,vi[sh(x,i)]]=1
    for row,(x,i,j) in enumerate(ff):
        ids=[ei[x,i],ei[sh(x,i),j],ei[sh(x,j),i],ei[x,j]]
        C[row,ids]=[1,1,-1,-1]
        if sum(x)%2==0:
            a=x;c=sh(sh(x,i),j);Th2[row,ids]=[1,1,1,1]
        else:
            a=sh(x,i);c=sh(x,j);Th2[row,ids]=[-1,1,-1,1]
        D[row,ai[a]]=-1;D[row,ai[c]]=1
    restrict=np.zeros((n,V),dtype=np.int64)
    for x,i in ai.items():restrict[i,vi[x]]=1
    assert np.array_equal(C@G,np.zeros((len(ff),V),dtype=np.int64))
    assert np.array_equal(Th2@G,2*D@restrict)
    Lmat=(D.T@D).astype(float);val,vec=eigh(Lmat)
    assert val[1]>1e-8 and abs(val[0])<1e-8
    Lp=(vec[:,1:]/val[1:])@vec[:,1:].T
    Th=Th2/2
    transverse=Th-D@(Lp@(D.T@Th))
    hess=(n-2)/(n-1)*(C.T@C)+4*n/(n-1)*(Th.T@transverse)
    assert np.max(np.abs(hess-hess.T))<1e-10
    gauge_error=float(np.max(np.abs(hess@G)))
    assert gauge_error<1e-9
    ev=eigvalsh(hess);zero=np.count_nonzero(np.abs(ev)<1e-8)
    assert zero==V-1 and ev[0]>-1e-8
    constants=[]
    predicted_mass=4*n/(n-1)*(d-1)
    for direction in range(d):
        a=np.array([float(j==direction) for x,j in ee])
        residual=float(np.linalg.norm(hess@a-predicted_mass*a)/np.linalg.norm(a))
        assert residual<1e-9
        assert np.max(np.abs(D.T@(Th@a)))<1e-10
        assert abs(np.linalg.norm(Th@a)**2-(d-1)*np.linalg.norm(a)**2)<1e-9
        constants.append({'direction':direction,'normalized_curvature':float(a@hess@a/(a@a)),
                          'predicted_curvature':predicted_mass,
                          'constant_mode_eigenvector_residual':residual})
    # Fixed low wave number, transverse polarization. Checkerboard folding can
    # mix this test vector with its staggered partner, so report Ritz pairs.
    kk=2*np.pi/L
    mode_pairs=[]
    for direction in range(1,d):
        vectors=[]
        for stagger in (0,1):
            a=np.array([np.exp(1j*kk*x[0])*(-1)**(stagger*sum(x))
                        if j==direction else 0j for x,j in ee])
            # Orthogonal projection away from the full vertex-gradient space.
            if np.linalg.norm(G.T@a)>1e-10:
                gl,gv=eigh((G.T@G).astype(float))
                a-=G@((gv[:,1:]/gl[1:])@(gv[:,1:].T@(G.T@a)))
            vectors.append(a)
        q,_=np.linalg.qr(np.column_stack(vectors))
        block=q.conj().T@hess@q
        leakage=float(np.linalg.norm(hess@q-q@block))
        mode_pairs.append({'wave_number':kk,'polarization':direction,
                           'projected_two_mode_Ritz_values':eigvalsh(block).tolist(),
                           'two_mode_subspace_leakage':leakage})
    return {'dimension':d,'period':L,'vertices':V,'A_records':n,'links':len(ee),
            'plaquettes':len(ff),'charge_exchange_graph_gap':float(val[1]),
            'exact_incidence_identities':True,'Hessian_gauge_residual':gauge_error,
            'Hessian_nullity':int(zero),'expected_vertex_gauge_nullity':V-1,
            'positive_Hessian_minimum':float(ev[V-1]),'Hessian_maximum':float(ev[-1]),
            'uniform_connection_controls':constants,'low_mode_controls':mode_pairs,
            'scope':'Finite-box lowest matter-potential band Hessian at zero angle. Not the complete quantum Hamiltonian gap or a thermodynamic Higgs theorem.'}

def main():
    examples=[]
    for n in (4,6):
        edges=[(i,(i+1)%n) for i in range(n)]
        if n==6:edges += [(0,3),(1,4),(2,5)]
        theta=[s.Rational((i*3)%7-3,7) for i in range(len(edges))]
        phi=[s.Rational((i*2)%5-2,5) for i in range(len(edges))]
        examples.append(finite_graph(n,edges,theta,phi))
        sitephase=[s.Rational(i*i,11) for i in range(n)]
        examples.append(finite_graph(n,edges,[sitephase[c]-sitephase[a] for a,c in edges],
                                     [s.Integer(0)]*len(edges)))
    b=Path(__file__).read_bytes()
    out={'created_utc':datetime.now(timezone.utc).isoformat(),
         'source':{'path':str(Path(__file__).resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()},
         'exact_finite_graph_controls':examples,
         'cubic_controls':[cubic(d,L) for d,L in [(2,4),(2,6),(2,8),(3,4),(3,6)]],
         'status':'Author controls; independent reconstruction pending.',
         'limits':'The exact finite-spin-sector calculation checks the potential-band Hessian. Cubic matrix spectra are floating corroboration, not interval enclosures or a full matter-field phase proof.'}
    text=json.dumps(out,indent=2)+'\n';(HERE/'CHARGED_RECORD_POTENTIAL_HESSIAN_RESULTS.json').write_text(text)
    print(text,end='')
if __name__=='__main__':main()
