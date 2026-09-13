"""Independent local-connection and polar-action challenges for BLOCK06."""
from pathlib import Path
from itertools import product
import hashlib,json,time
import numpy as np
import scipy.linalg as la
import sympy as s

HERE=Path(__file__).resolve().parent
sig=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
I2=s.eye(2)

def run():
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
    (HERE/'BLOCK06_SPIN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='details'},indent=2))

if __name__=='__main__':run()
