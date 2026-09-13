"""Author checks for a specified common-frame native Weyl coupling.

The paired note proves uniform node preservation and a slowly varying
operator bound. Finite challenges do not establish dynamical gravity.
External scientific data reads: none. Integrity reads: this source for
its self hash; the paired note is bound by the canonical cache envelope.
"""
from pathlib import Path
from itertools import product
from collections import deque
import hashlib,json,math,time
import numpy as np
import scipy.linalg as la
import sympy as s

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    'docs/NATIVE_COMMON_FRAME_SPIN_CONNECTION_BOUNDED_THEOREM_NOTE_2026-09-13.md',
)
ROOT=Path(__file__).resolve().parents[1]
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
I2=s.eye(2)
SIG=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
EPS=np.zeros((3,3,3))
for a,b,c in product(range(3),repeat=3):
    EPS[a,b,c]=(a-b)*(b-c)*(c-a)/2

def run_flat_spin():
    start=time.monotonic()
    checks=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    def eq(name,a,b):
        delta=a-b
        entries=list(delta) if isinstance(delta,s.MatrixBase) else [delta]
        check(name,all(s.expand(z)==0 for z in entries))
    def near(name,a,b,tol=3e-11):
        residue=float(np.max(abs(np.asarray(a)-np.asarray(b))))
        check(name,residue<tol,residual=residue,tolerance=tol)
    y=s.symbols('x y z',real=True)
    sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    identity=s.eye(2)
    N=s.Function('N')(*y)
    M=s.Function('M')(*y)
    psi=s.Matrix([s.Function('u')(*y),s.Function('v')(*y)])
    aa=s.Matrix([s.Function('a'+str(i))(*y) for i in range(3)])
    bb=s.Matrix([s.Function('b'+str(i))(*y) for i in range(3)])
    def grad(f): return s.Matrix([s.diff(f,x) for x in y])
    def div(v): return sum(s.diff(v[i],y[i]) for i in range(3))
    def curl(v): return s.Matrix([s.diff(v[2],y[1])-s.diff(v[1],y[2]),
                                  s.diff(v[0],y[2])-s.diff(v[2],y[0]),
                                  s.diff(v[1],y[0])-s.diff(v[0],y[1])])
    def pauli(v): return sum((sig[i]*v[i] for i in range(3)),s.zeros(2))
    def h(f): return -s.I*sum((sig[i]*f.diff(y[i]) for i in range(3)),s.zeros(2,1))
    def H(n,f): return (n*h(f)+h(n*f))/2
    def shift(v,f):
        return -s.I*(sum((v[i]*f.diff(y[i]) for i in range(3)),s.zeros(2,1))
                     +div(v)*f/2)+pauli(curl(v))*f/4
    def strain(v):
        j=v.jacobian(y)
        return (j+j.T)/2
    def K(matrix,f):
        return -s.I*sum((sig[j]*(matrix[i,j]*f.diff(y[i])
                              +s.diff(matrix[i,j],y[i])*f/2)
                        for i in range(3) for j in range(3)),s.zeros(2,1))
    drift=N*grad(M)-M*grad(N)
    eq('arbitrary_function_normal_normal_operator',s.I*(H(N,H(M,psi))-H(M,H(N,psi))),shift(drift,psi))
    eq('arbitrary_function_shift_free_Hamiltonian',s.I*(shift(aa,h(psi))-h(shift(aa,psi))),-K(strain(aa),psi))
    eq('arbitrary_function_shift_lapse_residual',
       s.I*(shift(aa,H(N,psi))-H(N,shift(aa,psi))),
       H((aa.dot(grad(N))),psi)-(N*K(strain(aa),psi)+K(strain(aa),N*psi))/2)
    bracket=bb.jacobian(y)*aa-aa.jacobian(y)*bb
    commstrain=strain(aa)*strain(bb)-strain(bb)*strain(aa)
    rotation=s.Matrix([sum(s.LeviCivita(k,i,j)*commstrain[j,i] for i in range(3) for j in range(3)) for k in range(3)])
    eq('arbitrary_function_shift_shift_strain',
       s.I*(shift(aa,shift(bb,psi))-shift(bb,shift(aa,psi)))-shift(bracket,psi),pauli(rotation)*psi/4)
    a0=s.Matrix([y[0],0,0]);b0=s.Matrix([y[1],y[0],0])
    br0=b0.jacobian(y)*a0-a0.jacobian(y)*b0
    eq('exact_noncommuting_strain_witness',
       s.I*(shift(a0,shift(b0,psi))-shift(b0,shift(a0,psi)))-shift(br0,psi),-sig[2]*psi/2)
    omega=s.Matrix(s.symbols('wx wy wz',real=True))
    rotation_field=omega.cross(s.Matrix(y))
    eq('rigid_rotation_has_spin_half',pauli(curl(rotation_field))/4,pauli(omega)/2)
    eq('rigid_rotation_has_no_strain',strain(rotation_field),s.zeros(3))
    eq('dilation_residual',s.I*(shift(s.Matrix(y),h(psi))-h(shift(s.Matrix(y),psi))),-h(psi))
    return dict(status='PASS',checks=len(checks),details=checks)

def run_common_frame():
    start=time.monotonic();checks=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    def eq(name,a,b):
        z=a-b
        vals=list(z) if isinstance(z,s.MatrixBase) else [z]
        check(name,all(s.trigsimp(s.expand_complex(x))==0 for x in vals))
    k=s.symbols('kx ky kz',real=True)
    theta=s.symbols('theta',real=True)
    zeta=s.cos(theta);v=s.sin(theta)
    F=s.Matrix(3,3,s.symbols('f0:9',real=True))
    F0=s.diag(1,1,v);ff=F-F0
    b=zeta-s.cos(k[2]);r=2-s.cos(k[0])-s.cos(k[1])
    d=s.Matrix([s.sin(k[0]),s.sin(k[1]),r+b])
    vertices=s.Matrix([[s.sin(k[0]),s.sin(k[1]),b*s.sin(k[2])/v**2],
                       [s.sin(k[0]),s.sin(k[1]),b*s.sin(k[2])/v**2],
                       [s.sin(k[2])*s.sin(k[0])/v,s.sin(k[2])*s.sin(k[1])/v,b/v]])
    deformed=d+s.Matrix([sum(ff[a,j]*vertices[a,j] for j in range(3)) for a in range(3)])
    naive=F*s.Matrix([s.sin(k[0]),s.sin(k[1]),b/v])+s.Matrix([0,0,r])
    for w in(-1,1):
        sub={k[0]:0,k[1]:0,k[2]:w*theta}
        R=s.diag(1,1,w)
        eq('all_frame_values_preserve_node_'+str(w),deformed.subs(sub),s.zeros(3,1))
        eq('exact_common_frame_tangent_'+str(w),deformed.jacobian(k).subs(sub),R*F)
        eq('exact_naive_frame_tangent_'+str(w),naive.jacobian(k).subs(sub),F*R)
        eq('common_principal_metric_'+str(w),(R*F).T*(R*F),F.T*F)
    t=s.symbols('t',real=True)
    shear=s.Matrix([[1,0,t],[0,1,0],[t,0,v]])
    gp=shear.T*shear
    gm=s.diag(1,1,-1)*gp*s.diag(1,1,-1)
    eq('naive_metric_shear_difference',gp[0,2]-gm[0,2],2*t*(1+v))
    check('shear_witness_is_nonzero',(gp[0,2]-gm[0,2]).subs({t:s.Rational(1,10),theta:s.pi/3})!=0)

    # Separate finite Laurent coefficient construction, as actual directed
    # hopping displacements rather than differentiating the supplied vertices.
    def vec(j,n=1):
        q=[0,0,0];q[j]=n;return tuple(q)
    def sincoeff(j,scale=1,step=1):
        return {vec(j,step):scale/(2*s.I),vec(j,-step):-scale/(2*s.I)}
    laurent={}
    for a in range(3):
        for j in range(3):
            if a<2 and j<2: co=sincoeff(j)
            elif a<2:
                co=sincoeff(2,zeta/v**2)
                co.update(sincoeff(2,-1/(2*v**2),2))
            elif j<2:
                co={}
                for sj,sz in product((-1,1),repeat=2):
                    q=[0,0,sz];q[j]=sj
                    co[tuple(q)]=-sj*sz/(4*v)
            else:
                co={(0,0,0):zeta/v,vec(2):-1/(2*v),vec(2,-1):-1/(2*v)}
            laurent[a,j]=co
            for w in(-1,1):
                zero=sum(c*s.exp(s.I*q[2]*w*theta) for q,c in co.items())
                eq('Laurent_node_'+str((a,j,w)),zero,0)
                for ell in range(3):
                    jet=sum(s.I*q[ell]*c*s.exp(s.I*q[2]*w*theta) for q,c in co.items())
                    eq('Laurent_jet_'+str((a,j,w,ell)),jet,(w if a==2 else 1)*int(j==ell))

    # Direct absolute Laurent second moments check the Taylor constants;
    # these are not estimated from the variable-frame operator error.
    for zz in(s.Rational(1,2),s.Rational(3,4),s.Rational(99,100)):
        substitution={theta:s.acos(zz)};vv=s.sqrt(1-zz**2)
        for (a,j),co in laurent.items():
            actual=sum(s.Abs(c.subs(substitution))*sum(x*x for x in r)/2 for r,c in co.items())
            if a<2 and j<2:expected=s.Rational(1,2)
            elif a<2:expected=(zz+2)/(2*vv**2)
            elif j<2:expected=1/vv
            else:expected=1/(2*vv)
            eq('Laurent_Taylor_constant_'+str((zz,a,j)),actual,expected)

    # Literal shortest protected paths on open virtual boxes, including thin
    # x boxes where detours at a boundary must use the other direction.
    sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    routed=0;maxlen=0;route_groups={}
    for shape in((3,3,3),(1,3,3),(2,2,3)):
        cells=list(product(*(range(n) for n in shape)))
        cellset=set(cells)
        nodes={(2*x[0]+rr,x[1],x[2]) for x in cells for rr in(0,1)}
        def protected(a,b):
            if a[1]!=b[1]:
                tail=min(a,b)
                return (tail[0]+tail[1])%2==0
            return True
        def path(a,b):
            todo=deque([(a,0)]);seen={a}
            while todo:
                here,dist=todo.popleft()
                if here==b:return dist
                if dist==4:continue
                for j,sgn in product(range(3),(-1,1)):
                    there=list(here);there[j]+=sgn;there=tuple(there)
                    if there in nodes and there not in seen and protected(here,there):
                        seen.add(there);todo.append((there,dist+1))
            return None
        for (a,j),co in laurent.items():
            for displacement in co:
                for x in cells:
                    target=tuple(x[i]+displacement[i] for i in range(3))
                    if target not in cellset:continue
                    for r0,r1 in product((0,1),repeat=2):
                        if sig[a][r0,r1]==0:continue
                        p0=(2*x[0]+r0,x[1],x[2]);p1=(2*target[0]+r1,target[1],target[2])
                        length=path(p0,p1)
                        assert length is not None and length<=4,('protected_path',shape,a,j,x,target,r0,r1)
                        route_groups.setdefault((shape,a,j),[]).append(length)
                        maxlen=max(maxlen,length);routed+=1
    for (shape,a,j),lengths in route_groups.items():
        check('protected_frame_family_'+str((shape,a,j)),all(x<=4 for x in lengths),
              routes=len(lengths),max_length=max(lengths))
    check('four_edge_route_is_exercised',maxlen==4)

    # The proof's global relative bound is challenged away from the nodes,
    # near each node and at trigonometric corners, for three fixed zetas.
    rng=np.random.default_rng(60613)
    fixed=rng.normal(size=(3,3));fixed=(fixed+fixed.T)/2;fixed/=np.linalg.norm(fixed)
    reports=[]
    for zz in(.5,.8,.99):
        vv=math.sqrt(1-zz*zz);star=math.acos(zz)
        deltaF=fixed*vv**2/(4*math.sqrt(10))
        sample=rng.uniform(-math.pi,math.pi,(600,3))
        corners=np.array(list(product((0.,math.pi),repeat=3)))
        near_nodes=np.vstack([np.array([0,0,w*star])+1e-4*rng.normal(size=(30,3)) for w in(-1,1)])
        sample=np.vstack([sample,corners,near_nodes])
        sx,sy,sz=np.sin(sample).T;cx,cy,cz=np.cos(sample).T
        dd=np.array([sx,sy,2+zz-cx-cy-cz]).T
        norm=np.linalg.norm(dd,axis=1)
        vertex=np.empty((len(sample),3,3))
        vertex[:,0,:]=vertex[:,1,:]=np.array([sx,sy,(zz-cz)*sz/vv**2]).T
        vertex[:,2,:]=np.array([sz*sx/vv,sz*sy/vv,(zz-cz)/vv]).T
        perturb=np.einsum('aj,naj->na',deltaF,vertex)
        error=np.linalg.norm(perturb,axis=1)
        check('global_relative_bound_challenge_'+str(zz),np.max(error/norm)<.25,
              max_ratio=float(np.max(error/norm)),proved_upper=.25)
        check('two_node_preservation_lower_bound_challenge_'+str(zz),
              np.min(np.linalg.norm(dd+perturb,axis=1)/norm)>.75)
        reports.append(dict(zeta=zz,samples=len(sample),max_relative=float(np.max(error/norm))))
    out=dict(status='PASS',checks=len(checks),details=checks,routed_hoppings=routed,max_path_length=maxlen,
             numerical_challenges=reports,elapsed_seconds=time.monotonic()-start,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Exact symbolic node/metric identities and literal finite protected routes; global preservation is the analytical relative-bound theorem, not inferred from samples.')
    return out

def run_spin_connection():
    start=time.monotonic();checks=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    def eq(name,a,b):
        z=a-b
        vals=list(z) if isinstance(z,s.MatrixBase) else [z]
        check(name,all(s.expand(x)==0 or s.simplify(x)==0 for x in vals))
    def scalar(F,jets):
        inv=F.inv()
        return -sum(s.LeviCivita(a,b,c)*F[a,i]*jets[i][b,j]*inv[j,c]
                    for a,b,c,i,j in product(range(3),repeat=5))/4
    def geometric(F,jets,label):
        # Compute the metric and Christoffel symbols directly; do not use
        # the compact scalar formula to construct the full operator.
        G=F.T*F;g=G.inv()
        dg=[-g*(dF.T*F+F.T*dF)*g for dF in jets]
        Gamma=[[[sum(G[n,l]*(dg[i][l,j]+dg[j][l,i]-dg[l][i,j])
                            for l in range(3))/2 for j in range(3)]
                            for i in range(3)] for n in range(3)]
        omega=[]
        for i in range(3):
            wi=s.Matrix(3,3,lambda b,c:sum(F[b,m]*g[m,n]*(jets[i][c,n]+
                sum(Gamma[n][i][j]*F[c,j] for j in range(3)))
                for m,n in product(range(3),repeat=2)))
            eq(label+'_connection_antisymmetric_'+str(i),wi+wi.T,s.zeros(3))
            omega.append(wi)
        for w in(-1,1):
            tau=[sig[0],sig[1],w*sig[2]]
            gamma=[sum((tau[a]*F[a,j] for a in range(3)),s.zeros(2)) for j in range(3)]
            A=[sum((omega[i][b,c]*tau[b]*tau[c]/4 for b,c in product(range(3),repeat=2)),s.zeros(2)) for i in range(3)]
            for i,j in product(range(3),repeat=2):
                compat=sum((tau[a]*jets[i][a,j] for a in range(3)),s.zeros(2))
                compat+=sum((Gamma[j][i][k]*gamma[k] for k in range(3)),s.zeros(2))
                compat+=A[i]*gamma[j]-gamma[j]*A[i]
                eq(label+'_Clifford_compatibility_'+str((w,i,j)),compat,s.zeros(2))
            full=sum((-s.I*gamma[i]*(A[i]-I2*sum(Gamma[k][k][i] for k in range(3))/2) for i in range(3)),s.zeros(2))
            sympart=-s.I*sum((tau[a]*jets[i][a,i]/2 for a,i in product(range(3),repeat=2)),s.zeros(2))
            eq(label+'_full_half_density_connection_'+str(w),full,sympart+w*scalar(F,jets)*I2)
            # Build the commutator of two first-order differential operators
            # from their value/first jets. Derivatives of the zeroth-order
            # connection cancel, so no second frame jet is assumed zero.
            N=s.Rational(7,5);M=s.Rational(9,7)
            dN=s.Matrix([s.Rational(2,3),-s.Rational(3,5),s.Rational(4,7)])
            dM=s.Matrix([-s.Rational(1,2),s.Rational(5,6),s.Rational(3,8)])
            ddN=s.Matrix([[1,2,-1],[2,-3,4],[-1,4,2]])/7
            ddM=s.Matrix([[2,-1,3],[-1,1,-2],[3,-2,4]])/9
            hA=[-s.I*x for x in gamma]
            dhA=[[-s.I*sum((tau[a]*jets[i][a,j] for a in range(3)),s.zeros(2)) for j in range(3)] for i in range(3)]
            NA=[N*x for x in hA];MA=[M*x for x in hA]
            NB=N*full+sum((hA[j]*dN[j]/2 for j in range(3)),s.zeros(2))
            MB=M*full+sum((hA[j]*dM[j]/2 for j in range(3)),s.zeros(2))
            covector=N*dM-M*dN
            drift=G*covector
            dG=[dF.T*F+F.T*dF for dF in jets]
            ddrift=[dG[i]*covector+G*(dN[i]*dM+N*ddM[:,i]-dM[i]*dN-M*ddN[:,i]) for i in range(3)]
            for j in range(3):
                coeff=sum((NA[i]*(dM[i]*hA[j]+M*dhA[i][j])-MA[i]*(dN[i]*hA[j]+N*dhA[i][j]) for i in range(3)),s.zeros(2))
                coeff+=NB*MA[j]-MB*NA[j]+NA[j]*MB-MA[j]*NB
                eq(label+'_curved_normal_commutator_drift_'+str((w,j)),s.I*coeff,-s.I*drift[j]*I2)
            zero=NB*MB-MB*NB
            for i in range(3):
                dNB=dN[i]*full+sum((dhA[i][j]*dN[j]/2+hA[j]*ddN[j,i]/2 for j in range(3)),s.zeros(2))
                dMB=dM[i]*full+sum((dhA[i][j]*dM[j]/2+hA[j]*ddM[j,i]/2 for j in range(3)),s.zeros(2))
                zero+=NA[i]*dMB-MA[i]*dNB
            target=-s.I*sum(ddrift[i][i] for i in range(3))*I2/2
            target+=-s.I*sum((drift[i]*A[i] for i in range(3)),s.zeros(2))
            target+=-s.I*sum((gamma[i]*gamma[j]*(dN[i]*dM[j]-dM[i]*dN[j])/4 for i,j in product(range(3),repeat=2)),s.zeros(2))
            eq(label+'_curved_normal_commutator_spin_'+str(w),s.I*zero,target)
        return scalar(F,jets)

    rng=np.random.default_rng(671313)
    for n in range(4):
        M=s.Matrix(rng.integers(-2,3,(3,3)).tolist())
        F=s.eye(3)+(M.T*M)/10
        if n==3:F=s.Matrix([[1,s.Rational(1,3),0],[0,1,s.Rational(1,5)],[0,0,1]])*F
        jets=[s.Matrix(rng.integers(-3,4,(3,3)).tolist())/10 for _ in range(3)]
        if n<3:jets=[(j+j.T)/2 for j in jets]
        val=geometric(F,jets,'rational_jet_'+str(n))
        if n<3:check('nonzero_scalar_on_positive_frame_'+str(n),val!=0,value=str(val))

    # An exact moving orthonormal frame: matrix conjugation provides a
    # separate sign check independent of metric and Koszul calculations.
    z=s.symbols('z',real=True);theta=s.Function('theta',real=True)(z)
    F=s.Matrix([[s.cos(theta),s.sin(theta),0],[-s.sin(theta),s.cos(theta),0],[0,0,1]])
    jets=[s.zeros(3),s.zeros(3),F.diff(z)]
    eq('rotating_frame_scalar_sign',scalar(F,jets),-s.diff(theta,z)/2)
    U=s.diag(s.exp(s.I*theta/2),s.exp(-s.I*theta/2))
    eq('unitary_conjugation_scalar_sign',-s.I*U*sig[2]*U.H.diff(z),-s.diff(theta,z)*I2/2)
    A,B,D=s.symbols('A B D',real=True);Ap,Bp,Dp,c=s.symbols('Ap Bp Dp c',real=True)
    F=s.Matrix([[A,B,0],[B,D,0],[0,0,c]])
    jets=[s.zeros(3),s.zeros(3),s.Matrix([[Ap,Bp,0],[Bp,Dp,0],[0,0,0]])]
    eq('nonuniform_positive_frame_formula',scalar(F,jets),-c*((A-D)*Bp+B*(Dp-Ap))/(4*(A*D-B**2)))
    check('positive_frame_scalar_witness',scalar(F,jets).subs({A:2,B:0,D:1,Ap:0,Bp:1,Dp:0,c:1})==-s.Rational(1,8))
    symjets=[s.Matrix([[s.Symbol('s'+str(i)+str(min(a,b))+str(max(a,b)),real=True) for b in range(3)] for a in range(3)]) for i in range(3)]
    eq('flat_symmetric_first_variation_zero',scalar(s.eye(3),symjets),0)

    # Exact linearized Sylvester equation, with independent generic vector
    # gradient matrices and all noncommuting symmetric strain components.
    Ja=s.Matrix(3,3,s.symbols('a0:9',real=True));Jb=s.Matrix(3,3,s.symbols('b0:9',real=True))
    Sa=(Ja+Ja.T)/2;Sb=(Jb+Jb.T)/2;Aa=(Ja-Ja.T)/2;Ab=(Jb-Jb.T)/2
    dOab=(Jb*Sa-Sa*Jb.T-Sa*Ab-Ab*Sa)/2
    dOba=(Ja*Sb-Sb*Ja.T-Sb*Aa-Aa*Sb)/2
    eq('polar_rotation_metric_derivative',dOab,(Sb*Sa-Sa*Sb)/2)
    eq('polar_rotation_antisymmetrized_derivative',dOab-dOba,-(Sa*Sb-Sb*Sa))
    K=Sa*Sb-Sb*Sa
    R=sum((sig[k]*s.LeviCivita(k,i,j)*K[j,i]/4 for k,i,j in product(range(3),repeat=3)),s.zeros(2))
    spinvar=sum(((dOab-dOba)[a,b]*sig[a]*sig[b]/4 for a,b in product(range(3),repeat=2)),s.zeros(2))
    eq('field_rotation_cancels_frozen_spin_residual',spinvar,s.I*R)

    # Finite matrix polar composition and first variations away from E=I.
    # This probes the nonlinear polar map, not only a Taylor formula.
    def positive_root(X):
        vals,vec=np.linalg.eigh(X)
        assert vals.min()>0
        return (vec*np.sqrt(vals))@vec.T
    def polar(E,J):
        out=positive_root(J@E@E@J.T)
        return out,np.linalg.solve(out,J@E)
    for n in range(5):
        X=rng.normal(size=(3,3));E=np.eye(3)+X.T@X/4
        Ja=rng.normal(size=(3,3))/3;Jb=rng.normal(size=(3,3))/3
        J1=la.expm(Ja);J2=la.expm(Jb)
        E1,O1=polar(E,J1);E2,O2=polar(E1,J2);E12,O12=polar(E,J2@J1)
        check('finite_polar_frame_composition_'+str(n),np.linalg.norm(E2-E12)<2e-12)
        check('finite_polar_rotation_cocycle_'+str(n),np.linalg.norm(O2@O1-O12)<2e-12)
        check('finite_polar_SO3_'+str(n),np.linalg.norm(O12@O12.T-np.eye(3))<2e-12 and abs(np.linalg.det(O12)-1)<2e-12)
        Om=la.solve_sylvester(E,E,Ja@E-E@Ja.T)
        deltaE=Ja@E-E@Om
        eps=1e-5
        Ep,Op=polar(E,np.eye(3)+eps*Ja);Em,Omn=polar(E,np.eye(3)-eps*Ja)
        errE=np.linalg.norm((Ep-Em)/(2*eps)-deltaE)
        errO=np.linalg.norm((Op-Omn)/(2*eps)-Om)
        check('nonflat_polar_frame_derivative_'+str(n),errE<3e-9,error=errE)
        check('nonflat_polar_rotation_derivative_'+str(n),errO<3e-9,error=errO)
    out=dict(status='PASS',checks=len(checks),details=checks,elapsed_seconds=time.monotonic()-start,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Exact connection comparisons on rational frame jets, generic symbolic strain cancellation, explicit nonuniform frames, and finite polar-map challenges. Author checks, not independent review or dynamical gravity.')
    return out

def run_variable_frame():
    start=time.monotonic();checks=[];reports=[]
    def check(name,ok,**details):
        assert bool(ok),(name,details)
        checks.append(dict(name=name,**details))
    zz=.5;v=math.sqrt(1-zz*zz);star=math.acos(zz)
    F0=np.diag([1,1,v]);inv0=np.diag([1,1,1/v])
    px,py=.7,-.4;K=math.sqrt(px*px+py*py+1)
    grid=128;x=2*math.pi*np.arange(grid)/grid
    pz=np.fft.fftfreq(grid,1/grid)
    psi=np.zeros((grid,2,6),complex)
    for j,q in enumerate((-1,0,1)):
        for orb in(0,1):psi[:,orb,2*j+orb]=np.exp(1j*q*x)
    def mul_symbol(symbol,u):
        return np.fft.ifft(np.einsum('nab,nbc->nac',symbol,np.fft.fft(u,axis=0)),axis=0)
    def opnorm(u):return float(np.linalg.norm(u.reshape(grid*2,6)/math.sqrt(grid),2))
    def neumann(F,m):
        X=np.einsum('ab,nbc->nac',inv0,F-F0)
        power=np.broadcast_to(np.eye(3),(len(F),3,3)).copy();total=power.copy()
        for _ in range(m):
            power=-np.einsum('nab,nbc->nac',power,X);total+=power
        return np.einsum('nab,bc->nac',total,inv0)
    def connection(F,deriv,Q):
        # Only spatial derivative i=3 is nonzero in these examples.
        return -np.einsum('abc,na,nbj,njc->n',EPS,F[:,:,2],deriv,Q)/4
    for family in('xy_shear','all_shears'):
        t,b,c,d=(.025,.015,0.,0.) if family=='xy_shear' else(.025,.015,.01,.008)
        def field(z):
            f=np.zeros((len(z),3,3));f[:,0,0]=t
            if family=='all_shears':f[:,1,1]=-t/2
            f[:,0,1]=f[:,1,0]=b*np.sin(z)
            f[:,0,2]=f[:,2,0]=c*np.cos(z)
            f[:,1,2]=f[:,2,1]=d*np.sin(z)
            return F0+f
        F=field(x);f=F-F0
        derivative=np.zeros_like(F)
        derivative[:,0,1]=derivative[:,1,0]=b*np.cos(x)
        derivative[:,0,2]=derivative[:,2,0]=-c*np.sin(x)
        derivative[:,1,2]=derivative[:,2,1]=d*np.cos(x)
        q=np.array([[t,b,c],[b,t/2 if family=='all_shears' else 0,d],[c,d,0]])
        fbound=float(np.linalg.norm(q));rho=fbound/v;M0=1+fbound
        M1=M3=math.sqrt(2*(b*b+c*c+d*d))
        check(family+'_small_frame_preserves_constant_symbols',fbound<v*v/math.sqrt(10))
        check(family+'_Neumann_rho',rho<1)
        Cexact=connection(F,derivative,np.linalg.inv(F))
        mref=20;Cref=connection(F,derivative,neumann(F,mref))
        etaref=1.5*M0*M1*rho**(mref+1)/(v*(1-rho))
        check(family+'_nonzero_connection',np.max(np.abs(Cexact))>1e-5,amplitude=float(np.max(np.abs(Cexact))))
        check(family+'_reference_connection',np.max(np.abs(Cref-Cexact))<1e-15,
              analytical_tail_bound=etaref)
        if family=='xy_shear':
            expected=-v*t*b*np.cos(x)/(4*(1+t-b*b*np.sin(x)**2))
            check('exact_xy_connection_formula',np.max(np.abs(expected-Cexact))<1e-15)
        for m in(0,2,4):
            Q=neumann(F,m)
            bound=rho**(m+1)/(v*(1-rho))
            residual=float(np.max(np.linalg.norm(Q-np.linalg.inv(F),axis=(1,2))))
            # Frobenius can exceed operator norm; use actual singular values.
            residual=float(np.max(np.linalg.svd(Q-np.linalg.inv(F),compute_uv=False)[:,0]))
            check(family+'_inverse_remainder_'+str(m),residual<=bound+1e-14,error=residual,bound=bound)
        L=np.array([[.5,.5,(zz+2)/(2*v*v)],[.5,.5,(zz+2)/(2*v*v)],[1/v,1/v,1/(2*v)]])
        for w in(-1,1):
            R=np.array([1,1,w]);p=np.array([np.full(grid,px),np.full(grid,py),pz]).T
            tangent=p*np.array([1,1,w*v])
            hlin=np.einsum('na,aij->nij',tangent,SIG)
            continuum=mul_symbol(hlin,psi)
            for a,j in product(range(3),repeat=2):
                V=np.einsum('n,ij->nij',R[a]*p[:,j],SIG[a])
                continuum+=(f[:,a,j,None,None]*mul_symbol(V,psi)+mul_symbol(V,f[:,a,j,None,None]*psi))/2
            continuum+=w*Cref[:,None,None]*psi
            results=[]
            for aa in(.12,.06,.03,.015,1e-6):
                m=6 if aa==1e-6 else 4
                P=K+(m+2)
                check(family+'_separated_bands_'+str((w,aa)),aa*P<star)
                k=np.array([np.full(grid,aa*px),np.full(grid,aa*py),w*star+aa*pz]).T
                sk=np.sin(k);ck=np.cos(k)
                ds=np.array([sk[:,0],sk[:,1],2+zz-ck.sum(axis=1)]).T
                native=mul_symbol(np.einsum('na,aij->nij',ds/aa,SIG),psi)
                vertices=np.empty((grid,3,3))
                vertices[:,0,:]=vertices[:,1,:]=np.array([sk[:,0],sk[:,1],(zz-ck[:,2])*sk[:,2]/(v*v)]).T
                vertices[:,2,:]=np.array([sk[:,2]*sk[:,0]/v,sk[:,2]*sk[:,1]/v,(zz-ck[:,2])/v]).T
                for a,j in product(range(3),repeat=2):
                    V=np.einsum('n,ij->nij',vertices[:,a,j]/aa,SIG[a])
                    native+=(f[:,a,j,None,None]*mul_symbol(V,psi)+mul_symbol(V,f[:,a,j,None,None]*psi))/2
                no_connection=native.copy()
                central=(field(x+aa)-field(x-aa))/(2*aa)
                Q=neumann(F,m);Cm=connection(F,central,Q)
                eta=1.5*M0*M1*rho**(m+1)/(v*(1-rho))+aa*aa*M0*M3/(4*v*(1-rho))
                check(family+'_local_connection_bound_'+str((w,aa)),np.max(np.abs(Cm-Cexact))<=eta+1e-13)
                Bsym=np.einsum('n,ij->nij',sk[:,2]/v,np.eye(2))
                native+=(Cm[:,None,None]*mul_symbol(Bsym,psi)+mul_symbol(Bsym,Cm[:,None,None]*psi))/2
                error=opnorm(native-continuum)
                cm=1.5*M0*(M1+aa*aa*M3/6)/(v*(1-rho))
                bound=aa*P*P/2+aa*aa*P**3/6+aa*P*P*np.sum(q*L)+cm*aa*P/v+eta
                check(family+'_operator_bound_'+str((w,aa)),error+etaref<bound,
                      error=error,analytical_bound=bound,reference_tail=etaref)
                # The polynomial reference has degree <=mref+2; 128-point
                # Parseval is exact for its norm matrix (roundoff excepted).
                check(family+'_Parseval_degree_'+str((w,aa)),2*(mref+3)<grid)
                results.append(dict(spacing=aa,m=m,error=error,bound=bound))
                if aa==1e-6:
                    omitted=opnorm(no_connection-continuum)
                    check(family+'_omitted_connection_has_nonzero_limit_'+str(w),omitted>2e-5 and error<3e-6,
                          omitted_error=omitted,completed_error=error)
            check(family+'_resolved_convergence_'+str(w),all(results[i+1]['error']<results[i]['error'] for i in range(len(results)-1)))
            reports.append(dict(frame=family,node=w,values=results))
    out=dict(status='PASS',checks=len(checks),details=checks,reports=reports,elapsed_seconds=time.monotonic()-start,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Finite Fourier operator challenges on variable frames. Exact continuum connection is enclosed by an analytical Neumann tail; no sampled proof of the general theorem or long-time claim.')
    return out

def run_native_paths():
    checks=[];n=5;size=1<<n
    def check(name,ok):
        assert bool(ok),name
        checks.append(dict(name=name))
    cs=[]
    for j in range(n):
        c=np.zeros((size,size),complex)
        for state in range(size):
            if (state>>j)&1:
                sign=(-1)**((state&((1<<j)-1)).bit_count())
                c[state^(1<<j),state]=sign
        cs.append(c)
    gamma=[c+c.conj().T for c in cs]
    B=[np.eye(size)-2*c.conj().T@c for c in cs]
    for length in range(1,5):
        Ap=(1j)**(length-1)*np.eye(size)
        for j in range(length):Ap=Ap@(-1j*gamma[j]@gamma[j+1])
        check('native_path_endpoint_'+str(length),np.max(abs(Ap+1j*gamma[0]@gamma[length]))<1e-13)
        T=1j*Ap@(B[0]-B[length])/2
        J=-Ap@(np.eye(size)-B[0]@B[length])/2
        hop=cs[0].conj().T@cs[length]
        check('native_real_hopping_'+str(length),np.max(abs(T-hop-hop.conj().T))<1e-13)
        check('native_imaginary_hopping_'+str(length),np.max(abs(J-1j*(hop-hop.conj().T)))<1e-13)
    return dict(status='PASS',checks=len(checks),details=checks)


def main():
    start=time.monotonic()
    families=dict(flat_spin=run_flat_spin(),common_frame=run_common_frame(),
                  spin_connection=run_spin_connection(),variable_frame=run_variable_frame(),
                  native_paths=run_native_paths())
    for label,result in families.items():
        names=[row['name'] for row in result['details']]
        assert len(names)==len(set(names)),('duplicate_check_name',label)
    out=dict(status='PASS',checks=sum(x['checks'] for x in families.values()),families=families,
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             elapsed_seconds=time.monotonic()-start,
             scope='Specified free native frame construction, exact local algebra and finite operator challenges. No metric selection, interacting frame theorem, long-time control or full gravitational constraint algebra.')
    target=ROOT/'outputs/native_common_frame_spin_connection_2026_09_13.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS common native frame and spin connection:',out['checks'],'checks')
    for label,result in families.items():print(label+':',result['checks'],'PASS')
    print('per_element: Exact symbolic vertex jets and Clifford identities are checked; no physical parameter is fitted.')
    print('per_site: Local rational frame jets and the central frame stencil are checked in their stated finite examples.')
    print('per_mode: Both native nodes, the shear metric and finite Fourier operator errors are explicitly challenged.')
    print('per_block: Protected hopping routes on three open boxes and five-mode even CAR paths are enumerated.')
    print('lattice_wide: The note proves the uniform zero-set and slow-band bounds; the runner does not simulate an infinite system or prove gravity dynamics.')
    print('Source SHA-256:',out['source_sha256'])
    print('Elapsed seconds:',out['elapsed_seconds'])

if __name__=='__main__':main()
