"""Bounded falsifiers for the conditional soft-spin2 and lattice-source theorem.

No file inputs; native scattering and an interacting gravity phase are not derived.
"""
AUDIT_TIMEOUT_SEC = 90
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import numpy as np
import sympy as sp
from scipy.linalg import svdvals


def cross_constraint(velocities):
    """Linear equations for arbitrary gradient values F_i, independently of E."""
    v=np.asarray(velocities,float);n,d=v.shape;rows=[]
    for i,j in combinations(range(n),2):
        z=v[i]-v[j]
        if np.linalg.norm(z)<1e-14:continue
        for a,b in combinations(range(d),2):
            row=np.zeros((n,d));row[i,a]+=z[b];row[j,a]-=z[b]
            row[i,b]-=z[a];row[j,b]+=z[a];rows.append(row.ravel())
    return np.array(rows)


def collision_geometry():
    rng=np.random.default_rng(813);rows=[]
    for d in (2,3,4):
        p=rng.normal(size=(7,d))
        cases={'quadratic':p,'massive':p/np.sqrt(1+(p*p).sum(1))[:,None],
               'massless':p/np.linalg.norm(p,axis=1)[:,None]}
        for label,v in cases.items():
            C=cross_constraint(v);s=svdvals(C);rank=np.count_nonzero(s>1e-10)
            basis=np.column_stack([v.ravel()]+[np.tile(np.eye(d)[a],len(v)) for a in range(d)])
            assert np.max(abs(C@basis))<1e-12
            assert len(v)*d-rank==d+1
            bad=basis[:,0].copy();bad[0]+=0.25
            assert np.linalg.norm(C@bad)>0.01
            rows.append({'d':d,'velocity_image':label,'gradient_nullity':int(len(v)*d-rank)})
    # In a collinear image transverse components can be constant but each
    # longitudinal gradient is unrestricted; it violates the key hypothesis.
    v=np.column_stack([np.arange(6),np.zeros((6,2))]);C=cross_constraint(v)
    assert 18-np.linalg.matrix_rank(C)==8
    # Local normal-collision tangent constraint for a nonquadratic energy.
    p=np.array([.2,.3,.4]);q=np.array([-.1,.35,-.2]);mass=.7
    def energy(x):return np.sqrt(mass**2+np.sum(np.sin(x)**2))
    def velocity(x):return np.sin(2*x)/(2*energy(x))
    n=velocity(p)-velocity(q);delta=np.cross(n,[.3,.5,.7]);delta/=np.linalg.norm(delta)
    assert abs(n@delta)<1e-14
    beta=.73;gamma=np.array([.2,-.5,.4])
    assert abs(((beta*velocity(p)+gamma)-(beta*velocity(q)+gamma))@delta)<1e-14
    return rows


def cubic_and_integrability():
    rotations=[]
    for perm in permutations(range(3)):
        for sign in product((-1,1),repeat=3):
            R=np.eye(3,dtype=int)[list(perm)]*np.array(sign)[:,None]
            if round(np.linalg.det(R))==1:rotations.append(R)
    assert len(rotations)==24
    assert np.linalg.matrix_rank(np.vstack([R-np.eye(3) for R in rotations]))==3
    C=np.vstack([np.kron(np.eye(3),R)-np.kron(R.T,np.eye(3)) for R in rotations])
    assert 9-np.linalg.matrix_rank(C)==1
    # Solve the antisymmetric integrability equation for arbitrary b+beta and A-A^T.
    velocities=[sp.Matrix([1,0,0]),sp.Matrix([0,1,0]),sp.Matrix([0,0,1])]
    u=sp.Matrix(sp.symbols('u0:3'));a01,a02,a12=sp.symbols('a01 a02 a12')
    anti={(0,1):a01,(0,2):a02,(1,2):a12};equations=[]
    for v in velocities:
        equations += [u[j]*v[i]-u[i]*v[j]-anti[i,j] for i,j in combinations(range(3),2)]
    assert sp.linsolve(equations,(*u,a01,a02,a12))==sp.FiniteSet((0,0,0,0,0,0))
    # Anisotropic tilted quadratic shell BEFORE hard-graviton alignment.
    p=sp.Matrix(sp.symbols('p0:3',real=True));k=sp.Rational(3,2)
    b=sp.Matrix([sp.Rational(1,5),sp.Rational(-1,7),sp.Rational(1,9)])
    Q=sp.Rational(2,3);A=sp.diag(2,3,4);a=sp.Matrix([1,-2,3]);B=11
    L=b.dot(p)+Q;rad=L**2+k*(p.dot(A*p)+2*a.dot(p)+B)
    E=(-L+sp.sqrt(rad))/k
    v=sp.Matrix([sp.diff(E,x) for x in p]);f0=k*E+b.dot(p)+Q
    assert all(sp.simplify(z)==0 for z in f0*v-(-b*E+A*p+a))
    # After a hard isotropic gapless graviton fixes b=0, A=k*c^2 I.
    c=sp.Rational(5,4);K=sp.Matrix([sp.Rational(1,3),sp.Rational(-1,2),sp.Rational(1,7)])
    mu=sp.Rational(7,5);eps=sp.sqrt(mu**2+c*c*(p-K).dot(p-K));E=eps-Q/k
    v=sp.Matrix([sp.diff(E,x) for x in p]);zeta=sp.Matrix([E,*(E*v)])
    g=k+Q/E;target=k*sp.Matrix([eps,*(c*c*(p-K))])
    assert all(sp.simplify(z)==0 for z in g*zeta-target)
    return {'proper_cubic_rotations':24,'fixed_vectors':0,'matrix_commutant_dimension':1,
            'general_affine_shell_gradient':'exact','shifted_common_shell':'exact'}


def modular_rank(rows,prime=1000003):
    a=[[int(x.numerator%prime)*pow(int(x.denominator%prime),-1,prime)%prime for x in row] for row in rows]
    rank=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank];inv=pow(a[rank][j],-1,prime)
        a[rank]=[(x*inv)%prime for x in a[rank]]
        for i in range(rank+1,len(a)):
            scale=a[i][j]
            if scale:a[i]=[(x-scale*y)%prime for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank


def soft_pole_check():
    # Exactly on-shell m=1 momenta from a rational boost of two COM directions.
    p=[[F(25,16),F(3,4),F(0),F(15,16)],
       [F(25,16),F(-3,4),F(0),F(15,16)],
       [F(25,16),F(0),F(3,4),F(15,16)],
       [F(25,16),F(0),F(-3,4),F(15,16)]]
    eta=[-1,-1,1,1];pairs=list(combinations(range(4),2));sym=[(i,j) for i in range(4) for j in range(i,4)]
    assert all(v[0]**2-sum(x*x for x in v[1:])==1 for v in p)
    assert all(sum(eta[a]*p[a][i] for a in range(4))==0 for i in range(4))
    rows=[]
    for u,v in product(range(-3,4),repeat=2):
        # Rational stereographic soft directions. Every denominator is nonzero.
        den=1+u*u+v*v;n=[F(2*u,den),F(2*v,den),F(1-u*u-v*v,den)];q=[F(1),*(-x for x in n)]
        assert sum(x*x for x in n)==1
        denom=[sum(x*y for x,y in zip(q,z)) for z in p];assert all(denom)
        for nu in range(4):
            rows.append([eta[a]*(q[i]*int(j==nu)+q[j]*int(i==nu and i!=j))/denom[a]
                         for a in range(4) for i,j in sym])
    expected=[p[a][i]*p[a][j] for a in range(4) for i,j in sym]
    assert all(sum(x*y for x,y in zip(row,expected))==0 for row in rows)
    rank=modular_rank(rows);assert rank==39
    # The exact nonzero kernel gives rank<=39, modular minor gives rank>=39.
    numerical=np.array(rows,float);values=svdvals(numerical)
    assert values[-1]<1e-12 and values[-2]>.01
    # Changing one symmetric residue coefficient must violate real-soft Ward tests.
    bad=expected.copy();bad[0]+=F(1,7)
    assert any(sum(x*y for x,y in zip(row,bad))!=0 for row in rows)
    # Nonzero trace terms are not silently treated as an all-parameter Ward completion.
    trace=[F(0)]*40
    for i,j in sym:
        if i==j:trace[sym.index((i,j))]=F(1 if i==0 else -1)
    assert any(sum(x*y for x,y in zip(row,trace))!=0 for row in rows)
    null_p=[[F(1),F(1),F(0),F(0)],[F(1),F(-1),F(0),F(0)],
            [F(1),F(0),F(1),F(0)],[F(1),F(0),F(-1),F(0)]]
    null_rows=[];directions=0
    for u,v in product(range(-3,4),repeat=2):
        den=1+u*u+v*v;q=[F(1),-F(2*u,den),-F(2*v,den),-F(1-u*u-v*v,den)]
        denom=[sum(x*y for x,y in zip(q,z)) for z in null_p]
        if not all(denom):continue
        directions+=1
        for nu in range(4):
            null_rows.append([eta[a]*(q[i]*int(j==nu)+q[j]*int(i==nu and i!=j))/denom[a]
                              for a in range(4) for i,j in sym])
    null_expected=[null_p[a][i]*null_p[a][j] for a in range(4) for i,j in sym]
    assert all(sum(x*y for x,y in zip(row,null_expected))==0 for row in null_rows)
    assert modular_rank(null_rows)==39
    # The tangent null divisor's two conjugate components together span the
    # full hyperplane, and these three points avoid every other real hard pole.
    qs=[sp.Matrix([1,-1,0,0]),sp.Matrix([1,-1,sp.I,1]),sp.Matrix([1,-1,-sp.I,1])]
    assert sp.Matrix.hstack(*qs).rank()==3
    for q in qs:
        assert q[0]**2-sum(x*x for x in q[1:])==0
        assert q.dot(sp.Matrix(null_p[0]))==0
        assert all(q.dot(sp.Matrix(z))!=0 for z in null_p[1:])
    return {'hard_legs':4,'real_soft_directions':49,'symmetric_unknowns':40,
            'exact_rank':rank,'exact_nullity':1,'smallest_nonzero_numeric_singular_value':float(values[-2]),
            'null_hard_leg_soft_directions':directions,'null_hard_leg_exact_rank':39,'null_divisor_span':3}


def dirac_band_collision():
    I=np.eye(2);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
    alpha=[np.kron(X,s) for s in [X,Y,Z]];beta=np.kron(Z,I);gamma=alpha+[beta]
    for i,j in product(range(4),repeat=2):
        assert np.max(abs(gamma[i]@gamma[j]+gamma[j]@gamma[i]-2*np.eye(4)*(i==j)))<1e-14
    out=[]
    for m,k in product((.4,1,2),(.05,.1,.2,.5)):
        Ek=np.sqrt(m*m+np.sin(k)**2);Eh=(Ek+m)/2
        y2=Eh*Eh-m*m-np.sin(k/2)**2;assert 0<y2<1;y=np.arcsin(np.sqrt(y2))
        ps=np.array([[k,0,0],[0,0,0],[k/2,y,0],[k/2,-y,0]])
        energies=[];currents=[]
        for p in ps:
            h=m*beta+sum(np.sin(p[i])*alpha[i] for i in range(3))
            e=np.sqrt(m*m+np.sum(np.sin(p)**2));energies.append(e)
            assert np.max(abs(np.linalg.eigvalsh(h)-np.array([-e,-e,e,e])))<1e-12
            # Hellmann-Feynman group velocity from the full positive-band projector.
            P=(np.eye(4)+h/e)/2;velocity=np.array([np.trace(P@alpha[i]*np.cos(p[i])).real/2 for i in range(3)])
            assert np.max(abs(velocity-np.sin(2*p)/(2*e)))<1e-12
            currents.append(e*velocity)
        eta=np.array([-1,-1,1,1]);assert np.max(abs(eta@ps))<1e-14
        assert abs(eta@energies)<1e-12
        defect=eta@currents;A=np.sin(k)-np.sin(2*k)/2
        assert abs(defect[0]-A)<1e-12 and np.max(abs(defect[1:]))<1e-12
        assert defect[0]>0
        bound=2/3*sum(np.linalg.norm(p)**3 for p in ps)
        assert np.linalg.norm(defect)<=bound
        out.append({'m':m,'k':k,'y':float(y),'ward_defect':float(defect[0]),'bound':float(bound)})
    # Exact series coefficient for every m>0 rules out a single charge shift Q.
    k,m=sp.symbols('k m',positive=True);Ek=sp.sqrt(m*m+sp.sin(k)**2);Eh=(Ek+m)/2
    A=sp.sin(k)-sp.sin(2*k)/2;B=sp.sin(k)/Eh-sp.sin(2*k)/(2*Ek)
    aser=sp.series(A,k,0,6).removeO();bser=sp.series(B,k,0,6).removeO()
    ratio=sp.series(bser/aser,k,0,3).removeO().expand()
    assert sp.simplify(ratio.coeff(k,0)-(1/m+1/(2*m**3)))==0
    assert sp.simplify(ratio.coeff(k,2)+5/(8*m**3)+1/(2*m**5))==0
    return out


def improved_derivatives():
    x=sp.Symbol('x',real=True);out=[]
    for R in range(1,6):
        coeff=[sp.Rational(2*(-1)**(r+1),r)*sp.factorial(R)**2/(sp.factorial(R-r)*sp.factorial(R+r)) for r in range(1,R+1)]
        for j in range(R):
            assert sum(coeff[r-1]*r**(2*j+1) for r in range(1,R+1))==int(j==0)
        C=sp.factorial(R)**2/sp.factorial(2*R+1)
        leading=(-1)**R*sum(coeff[r-1]*r**(2*R+1) for r in range(1,R+1))/sp.factorial(2*R+1)
        assert leading==-C
        derivative=sum(coeff[r-1]*sp.sin(r*x) for r in range(1,R+1))
        current=sp.series(derivative*sp.diff(derivative,x),x,0,2*R+2).removeO()
        assert sp.simplify(current-x+(2*R+2)*C*x**(2*R+1))==0
        numerical=np.array([float(c) for c in coeff]);rr=np.arange(1,R+1)
        A1=float(np.dot(abs(numerical),rr));moment=float(np.dot(abs(numerical),rr**(2*R+1)))
        constant=moment*(A1/float(sp.factorial(2*R+1))+1/float(sp.factorial(2*R)))
        for z in [.1,.2,.4]:
            d=np.dot(numerical,np.sin(rr*z));dp=np.dot(numerical*rr,np.cos(rr*z))
            assert abs(d*dp-z)<=constant*abs(z)**(2*R+1)+1e-15
        out.append({'range':R,'coefficients':list(map(str,coeff)),'leading_derivative_error':str(-C),
                    'current_error_order':2*R+1,'uniform_Taylor_bound_constant':constant})
    return out


def reaction_offsets_and_native_band():
    R=sp.Matrix([[-2,2,0],[0,-2,2],[-2,0,2]])
    K=sp.Matrix([sp.Rational(1,2),sp.Rational(-1,2),sp.Rational(3,2)])
    G=sp.Matrix([-2,4,2]) # Units of pi.
    assert R*K==G and R.rank()==R.row_join(G).rank()==2
    z=sp.Matrix([-1,-1,1]);assert z.T*R==sp.zeros(1,3) and (z.T*G)[0]==0
    bad=sp.Matrix([-2,4,0]);assert (z.T*bad)[0]==-2
    assert R.row_join(bad).rank()==3
    assert sp.zeros(1,1).row_join(sp.Matrix([2])).rank()==1
    # The supplied two-orbital Wilson symbol has a tangent direction with
    # an exact sine dispersion; this follows directly from its full matrix.
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
    records=[]
    for zeta,q in product((.3,.7,.95),(.1,.3,.6)):
        p=np.array([0.,q,np.arccos(zeta)])
        h=np.sin(p[0])*X+np.sin(p[1])*Y+(2+zeta-np.cos(p).sum())*Z
        e=np.linalg.eigvalsh(h)[1];expected=4*np.sin(q/2)**2
        assert abs(e*e-expected)<1e-13 and expected<q*q
        records.append({'zeta':zeta,'tangent_momentum':q,'cone_squared_defect':float(e*e-q*q)})
    x,m,e=sp.symbols('x m e',real=True)
    # Reconstruct the full Dirac characteristic polynomial before substituting
    # an exactly quadratic trial energy; crossings do not select an eigenvector.
    Xs=sp.Matrix([[0,1],[1,0]]);Zs=sp.diag(1,-1)
    hs=m*sp.kronecker_product(Zs,sp.eye(2))+sp.sin(x)*sp.kronecker_product(Xs,Xs)
    characteristic=sp.factor((e*sp.eye(4)-hs).det())
    assert sp.expand(characteristic-(e*e-m*m-sp.sin(x)**2)**2)==0
    det=sp.simplify(characteristic.subs(e,sp.sqrt(m*m+x*x)))
    assert sp.simplify(det-(x*x-sp.sin(x)**2)**2)==0
    assert sp.series(det,x,0,10).removeO()==x**8/9
    return {'consistent_valley_offsets_pi':list(map(str,K)),
            'closed_menu_bad_residual_pi':-2,'native_tangent_band':records,
            'Dirac_trial_shell_determinant_leading':'x^8/9'}


def lattice_causal_tails():
    from scipy.linalg import expm
    import mpmath as mp
    N=7;J=.7;t=.12;dim=1<<N
    H=np.zeros((dim,dim))
    for b in range(dim):
        for x in range(N-1):
            if ((b>>x)^(b>>(x+1)))&1:H[b^(1<<x)^(1<<(x+1)),b]=-J
    one=np.array([1<<x for x in range(N)]);h=H[np.ix_(one,one)]
    assert np.array_equal(h,np.diag([-J]*(N-1),1)+np.diag([-J]*(N-1),-1))
    U=expm(-1j*t*H);u=expm(-1j*t*h)
    assert np.max(abs(U[np.ix_(one,one)]-u))<1e-14
    assert U[0,0]==1 and np.max(abs(U[1:,0]))==0
    exact=sp.zeros(N)
    for x in range(N-1):exact[x,x+1]=exact[x+1,x]=-1
    for r in range(1,N):
        for n in range(r):assert (exact**n)[r,0]==0
        assert (exact**r)[r,0]==(-1)**r
        assert (exact**(r+1))[r,0]==0
        assert abs(U[1<<r,1])>0
    # Independent infinite-chain Fourier sum and Bessel evaluation.
    q=np.arange(512)*2*np.pi/512
    amplitudes=[]
    for r in range(7):
        quadrature=np.mean(np.exp(1j*q*r+2j*J*t*np.cos(q)))
        bessel=1j**r*complex(mp.besselj(r,2*J*t))
        assert abs(quadrature-bessel)<1e-15
        amplitudes.append(float(abs(U[1<<r,1])**2))
    mp.mp.dps=60;bounds=[]
    R=mp.mpf(2);ct=mp.mpf(1)
    rate=R*mp.acosh(R/ct)-mp.sqrt(R*R-ct*ct);assert rate>0
    for inva in (4,8,16,32):
        r=int(R*inva);value=abs(mp.besselj(r,ct*inva));bound=mp.exp(-rate*inva)
        assert 0<value<bound
        bounds.append({'inverse_spacing':inva,'distance_sites':r,'amplitude':float(value),'bound':float(bound)})
    return {'qubit_chain_sites':N,'nonzero_remote_occupation_probabilities':amplitudes,
            'continuum_outside_axis_front':bounds}


def preferred_frame_quadratic():
    w,k=sp.symbols('w k',nonzero=True,real=True)
    c1,c2,c3,c4=sp.symbols('c1 c2 c3 c4',real=True)
    eta=sp.diag(1,-1,-1,-1);d=sp.Matrix([w,0,0,k])
    def action(H,V):
        Hu=eta*H*eta;tr=sp.trace(eta*H);d2=(d.T*eta*d)[0];div=Hu*d
        eh=sp.expand((d2*(sum(H[i,j]*Hu[i,j] for i in range(4) for j in range(4))-tr**2)
                      -2*(div.T*eta*div)[0]+2*d.dot(div)*tr)/4)
        D=sp.zeros(4)
        for a in range(4):
            for m in range(4):
                D[a,m]=d[a]*V[m]+sum(eta[m,z]*(d[a]*H[z,0]+w*H[z,a]-d[z]*H[a,0])/2 for z in range(4))
        ae=-c1*sum(eta[a,a]*eta[m,m]*D[a,m]**2 for a in range(4) for m in range(4))
        ae-=c2*sp.trace(D)**2+c3*sp.trace(D*D)+c4*sum(eta[m,m]*D[0,m]**2 for m in range(4))
        return sp.expand(eh+ae),D
    t,h,v,n,b,l=sp.symbols('t h v n b l',real=True)
    c13=c1+c3;c14=c1+c4;c123=c1+c2+c3
    LT,_=action(sp.diag(0,t,-t,0),sp.zeros(4,1))
    assert sp.simplify(LT-((1-c13)*w*w-k*k)*t*t/2)==0
    H=sp.zeros(4);H[1,3]=H[3,1]=h
    LV,_=action(H,sp.Matrix([0,v,0,0]))
    expected=(1-c13)*w*w*h*h/2+c14*w*w*v*v-c1*k*k*v*v+c13*w*k*h*v
    assert sp.simplify(LV-expected)==0
    LVred=sp.factor(LV.subs(h,-c13*k*v/((1-c13)*w)))
    expected=(c14*w*w-(2*c1-c1*c1+c3*c3)*k*k/(2*(1-c13)))*v*v
    assert sp.simplify(LVred-expected)==0
    LS,_=action(sp.diag(n,b,b,l),sp.Matrix([-n/2,0,0,0]))
    LSred=sp.factor(LS.subs({n:2*b/c14,l:-2*(1+c2)*b/c123}))
    expected=((1-c13)*(2+c13+3*c2)*w*w/(2*c123)-(2-c14)*k*k/(2*c14))*b*b
    assert sp.simplify(LSred-expected)==0
    # Build the UNFIXED full Hessian, so fixing h0i and longitudinal v has not
    # silently discarded a metric or aether constraint.
    pairs=[(i,j) for i in range(4) for j in range(i,4)]
    hs=sp.symbols('h0:10');vs=sp.symbols('v1:4');H=sp.zeros(4)
    for z,(i,j) in zip(hs,pairs):H[i,j]=H[j,i]=z
    V=sp.Matrix([-H[0,0]/2,*vs]);full,D=action(H,V);variables=(*hs,*vs)
    Hess=sp.hessian(full,variables)
    gauge=[]
    for mu in range(4):
        xi=sp.eye(4)[:,mu];xil=eta*xi;Hg=d*xil.T+xil*d.T;Vg=-w*xi
        vector=sp.Matrix([Hg[i,j] for i,j in pairs]+list(Vg[1:]))
        assert all(sp.simplify(x)==0 for x in Hess*vector)
        _,Dg=action(Hg,Vg);assert Dg==sp.zeros(4)
        gauge.append(vector)
    # Derive the complete source variation, including the transforming vector.
    ts=sp.symbols('T0:10');T=sp.zeros(4)
    for z,(i,j) in zip(ts,pairs):T[i,j]=T[j,i]=z
    J=sp.Matrix(sp.symbols('J0:4'));xi=sp.Matrix(sp.symbols('xi0:4'))
    xil=eta*xi;Hg=d*xil.T+xil*d.T;Vg=-w*xi
    variation=sum(Hg[i,j]*T[i,j] for i in range(4) for j in range(4))/2+Vg.dot(J)
    mixed=(T*d-w*eta*J).dot(xil)
    assert sp.expand(variation-mixed)==0
    assert sp.expand(variation-sum(Hg[i,j]*T[i,j] for i in range(4) for j in range(4))/2+w*xi.dot(J))==0
    params={c1:sp.Rational(1,10),c2:sp.Rational(1,10),c3:0,c4:0,k:1}
    squared=[sp.Rational(10,9),sp.Rational(19,18),sp.Rational(95,54)]
    counts=[]
    for speed2,physical in zip(squared,[2,2,1]):
        K=np.array(Hess.subs(params).subs(w,sp.sqrt(speed2)),float)
        values=svdvals(K);nullity=int(np.count_nonzero(values<1e-11))
        assert nullity==4+physical
        counts.append({'speed_squared':str(speed2),'gauge_nullity':4,'additional_mode_nullity':physical})
    K=np.array(Hess.subs(params).subs(w,2),float)
    assert 13-np.linalg.matrix_rank(K)==4
    # Exact full-equation and positive pole-weight checks for one representative
    # of each polarization. Tensor/vector partners follow spatial rotation.
    mode_vectors=[];mode_weights=[]
    for label,speed2 in zip(['tensor','vector','scalar'],squared):
        values={z:sp.S.Zero for z in variables}
        if label=='tensor':values.update({H[1,1]:1,H[2,2]:-1})
        elif label=='vector':values.update({vs[0]:1,H[1,3]:-c13*k/((1-c13)*w)})
        else:values.update({H[0,0]:2/c14,H[1,1]:1,H[2,2]:1,H[3,3]:-2*(1+c2)/c123})
        mode=sp.Matrix([sp.sympify(values[z]) for z in variables]).subs(params).subs(w,sp.sqrt(speed2))
        matrix=Hess.subs(params).subs(w,sp.sqrt(speed2))
        assert all(sp.simplify(x)==0 for x in matrix*mode)
        weight=sp.simplify((mode.T*sp.diff(Hess,w).subs(params).subs(w,sp.sqrt(speed2))*mode)[0]/(2*sp.sqrt(speed2)))
        assert weight>0;mode_weights.append(str(weight));mode_vectors.append(mode)
    assert mode_weights==['9/10','1/5','54/5']
    # A k!=0 gauge section h03=h13=h23=h33=0 gives a complete 9-field symbol.
    # Its exact determinant checks the entire finite-frequency mode census.
    removed={pairs.index(pair) for pair in [(0,3),(1,3),(2,3),(3,3)]}
    kept=[i for i in range(13) if i not in removed]
    determinant=sp.factor(Hess.subs(params).extract(kept,kept).det())
    polynomial=sp.prod((w*w-speed2)**multiplicity for speed2,multiplicity in zip(squared,[2,2,1]))
    factor=sp.simplify(determinant/polynomial)
    assert factor!=0 and not factor.has(w)
    # All reduced kinetic and spatial gradient coefficients are positive here.
    coefficients=[(1-c13)/2,sp.Rational(1,2),c14,(2*c1-c1*c1+c3*c3)/(2*(1-c13)),
                  (1-c13)*(2+c13+3*c2)/(2*c123),(2-c14)/(2*c14)]
    coeff=[sp.simplify(x.subs(params)) for x in coefficients]
    assert all(x>0 for x in coeff)
    return {'unfixed_fields':13,'quadratic_gauge_directions':4,'mode_counts':counts,
            'positive_reduced_kinetic_and_gradient_coefficients':list(map(str,coeff)),
            'exact_full_equation_pole_weights':mode_weights,'gauge_section_determinant':str(determinant),
            'metric_only_Ward_assumed':False}


if __name__=='__main__':
    for f in [collision_geometry,cubic_and_integrability,soft_pole_check,dirac_band_collision,
              improved_derivatives,reaction_offsets_and_native_band,lattice_causal_tails,
              preferred_frame_quadratic]:
        print('PASS',f.__name__,json.dumps(f(),sort_keys=True))
    print('TOTAL: 8 substantive scientific check families passed; author evidence only.')
    print('per_element: exact residue, action, characteristic and stencil identities are checked in their declared conventions.')
    print('per_site: the full seven-qubit nearest-neighbor XY Hamiltonian and occupation response are constructed and compared.')
    print('per_mode: actual Dirac/Wilson eigenmodes and the complete thirteen-field aether quadratic symbol are checked.')
    print('per_block: exact four-leg collision kernels, reaction menus and a gauge-section determinant provide finite falsifiers.')
    print('lattice_wide: checked and not executed — quantified family claims use the written proofs; no interacting gravity phase is established.')
