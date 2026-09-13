"""Exact arbitrary-function commutators and finite Fourier challenges.

The Wilson norm estimate is proved in the paired note. This runner tests
finite instances; it does not compute a continuum gravitational algebra.
"""
from pathlib import Path
from itertools import product
import hashlib,json,math,time
import numpy as np
import sympy as s
from scipy import sparse

HERE=Path(__file__).resolve().parent


def run():
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
    # Four-component mass cancellation, with a genuinely arbitrary mass.
    mass=s.symbols('mass',real=True)
    alpha=[s.kronecker_product(sig[0],z) for z in sig]
    beta=s.kronecker_product(sig[2],identity)
    psi4=s.Matrix([s.Function('p'+str(i))(*y) for i in range(4)])
    def h4(f,m): return -s.I*sum((alpha[i]*f.diff(y[i]) for i in range(3)),s.zeros(4,1))+m*beta*f
    def H4(n,f,m): return (n*h4(f,m)+h4(n*f,m))/2
    eq('arbitrary_Dirac_mass_cancels_normal_commutator',
       H4(N,H4(M,psi4,mass),mass)-H4(M,H4(N,psi4,mass),mass),
       H4(N,H4(M,psi4,0),0)-H4(M,H4(N,psi4,0),0))

    # A finite Fourier regulator contains every intermediate support, so no
    # projected product is substituted for the actual product on the test band.
    modes=list(product(range(-3,4),repeat=3))
    index={k:i for i,k in enumerate(modes)}
    initial=[index[k] for k in product(range(-1,2),repeat=3)]
    columns=np.array([2*i+j for i in initial for j in range(2)])
    sig_np=[np.array(z,complex) for z in sig]
    ident2=np.eye(2)
    def multiplication(coefs):
        rows=[];cols=[];vals=[]
        for k,ik in index.items():
            for q,c in coefs.items():
                target=tuple(k[i]+q[i] for i in range(3))
                if target in index:
                    rows.append(index[target]);cols.append(ik);vals.append(c)
        one=sparse.csr_matrix((vals,(rows,cols)),shape=(len(modes),len(modes)))
        return sparse.kron(one,ident2,format='csr')
    ns={(0,0,0):1,(1,0,0):.1,(-1,0,0):.1,(0,1,0):-.05j,(0,-1,0):.05j}
    ms={(0,0,0):1,(1,1,0):.15,(-1,-1,0):.15,(0,0,1):-.1j,(0,0,-1):.1j}
    mn,mm=multiplication(ns),multiplication(ms)
    nbound=sum(abs(v) for v in ns.values())
    mbound=sum(abs(v) for v in ms.values())
    K0=math.sqrt(3);B=math.sqrt(2);P=K0+2*B
    zeta=.5;v=math.sqrt(1-zeta*zeta);pstar=math.acos(zeta)
    points=np.array(modes,float)
    rows=[]
    for w in(-1,1):
        linear=points*np.array([1,1,w*v])
        h0=sparse.block_diag([sum(d*mat for d,mat in zip(vec,sig_np)) for vec in linear],format='csr')
        hn0=(mn@h0+h0@mn)/2;hm0=(mm@h0+h0@mm)/2
        target=(1j*(hn0@hm0-hm0@hn0))[:,columns].toarray()
        for spacing in(.16,.08,.04,.02):
            check('separated_node_support_'+str(w)+'_'+str(spacing),spacing*P<pstar)
            k=spacing*points+np.array([0,0,w*pstar])
            d=np.array([np.sin(k[:,0]),np.sin(k[:,1]),2.5-np.cos(k[:,0])-np.cos(k[:,1])-np.cos(k[:,2])]).T/spacing
            actual=sparse.block_diag([sum(z*mat for z,mat in zip(vec,sig_np)) for vec in d],format='csr')
            hn=(mn@actual+actual@mn)/2;hm=(mm@actual+actual@mm)/2
            difference=(1j*(hn@hm-hm@hn))[:,columns].toarray()-target
            error=float(np.linalg.norm(difference,2))
            delta=spacing*P*P/2+spacing*spacing*P**3/6
            bound=nbound*mbound*(4*P*delta+2*delta**2)
            check('actual_low_band_commutator_bound_'+str(w)+'_'+str(spacing),error<bound,error=error,bound=bound)
            rows.append(dict(node=w,spacing=spacing,error=error,bound=bound))
        check('lattice_error_is_exercised_'+str(w),rows[-1]['error']>.0001)
        check('lattice_errors_shrink_'+str(w),all(rows[-j]['error']<rows[-j-1]['error'] for j in range(1,4)))

    # Actual finite two-band projector and lapse matrices check the sea scalar.
    periodic=list(product(range(3),repeat=3))
    pin={k:i for i,k in enumerate(periodic)}
    points=2*np.pi*np.array(periodic)/3
    ds=np.array([np.sin(points[:,0]),np.sin(points[:,1]),2.5-np.cos(points[:,0])-np.cos(points[:,1])-np.cos(points[:,2])]).T
    hdiag=sparse.block_diag([sum(z*mat for z,mat in zip(vec,sig_np)) for vec in ds]).toarray()
    e,u=np.linalg.eigh(hdiag)
    p0=u[:,e<0]@u[:,e<0].conj().T
    rng=np.random.default_rng(60913)
    positions=np.array(periodic)
    fourier=np.exp(1j*positions@points.T)/math.sqrt(27)
    matrices=[]
    for j in range(2):
        lapse=1+.2*rng.normal(size=27)
        mult=np.kron(fourier.conj().T@np.diag(lapse)@fourier,ident2)
        matrices.append((mult@hdiag+hdiag@mult)/2)
    comm=matrices[0]@matrices[1]-matrices[1]@matrices[0]
    near('finite_filled_band_normal_order_scalar_zero',np.trace(p0@comm),0,tol=2e-10)
    check('finite_lapse_commutator_nonzero',np.linalg.norm(comm)>1)
    out=dict(status='PASS',checks=len(checks),details=checks,finite_fourier_probes=rows,
             elapsed_seconds=time.monotonic()-start,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Arbitrary-function algebra and finite free native Fourier challenges. No interacting or complete gravitational constraint algebra.')
    (HERE/'BLOCK06_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='details'},indent=2))

if __name__=='__main__': run()
