#!/usr/bin/env python3
"""Finite challenges for the proposed fixed-coupling Haar Villain score limit.

The general Gaussianity, thermodynamic, spectral and continuum arguments
are written proofs awaiting independent review. These finite checks do not
execute them. The layered quadratic environment is a comparison model.
No repository scientific input or package integrity file is read.
"""
AUDIT_TIMEOUT_SEC = 180

import itertools
import json
import math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import quad
from scipy.sparse import coo_matrix, eye, block_diag, vstack
from scipy.sparse.linalg import splu
from numpy.polynomial.hermite import hermgauss

def complex_box(d,L,periodic=False):
 side=2*(L+1);levels=[]
 for r in range(d+1):
  lev=[]
  for I in itertools.combinations(range(d),r):
   sizes=[side if periodic else (L if j in I else L+1) for j in range(d)]
   lev.extend((x,I) for x in itertools.product(*(range(n) for n in sizes)))
  levels.append(lev)
 ds=[]
 for r in range(d):
  ids={c:i for i,c in enumerate(levels[r])};rows=[];cols=[];vals=[]
  for a,(x,J) in enumerate(levels[r+1]):
   for j,mu in enumerate(J):
    I=J[:j]+J[j+1:];y=list(x);y[mu]+=1
    if periodic:y[mu]%=side
    rows.extend([a,a]);cols.extend([ids[(tuple(y),I)],ids[(x,I)]]);vals.extend([(-1)**j,-(-1)**j])
  ds.append(coo_matrix((vals,(rows,cols)),shape=(len(levels[r+1]),len(levels[r])),dtype=np.int64).tocsr())
 return levels,ds


def extensions(free,per,d,L):
 N=L+1;ext=[]
 for r in range(d+1):
  ids={c:i for i,c in enumerate(free[r])};rows=[];cols=[];vals=[]
  for a,(x,I) in enumerate(per[r]):
   y=[];sgn=1
   for j,t in enumerate(x):
    if j not in I:y.append(t if t<N else 2*N-1-t)
    else:
     if t in [N-1,2*N-1]:sgn=0;break
     if t<N-1:y.append(t)
     else:y.append(2*N-2-t);sgn*=-1
   if sgn:rows.append(a);cols.append(ids[(tuple(y),I)]);vals.append(sgn)
  ext.append(coo_matrix((vals,(rows,cols)),shape=(len(per[r]),len(free[r])),dtype=np.int64).tocsr())
 return ext


def zero(A):
 A.eliminate_zeros();return A.nnz==0


def reflection():
 rows=[]
 for d,L in [(1,1),(1,2),(1,3),(1,7),(2,1),(2,3),(3,1),(3,2),(4,1),(4,2)]:
  f,df=complex_box(d,L);p,dp=complex_box(d,L,True);E=extensions(f,p,d,L)
  for r in range(d+1):
   assert zero(E[r].T@E[r]-(2**d)*eye(len(f[r]),dtype=np.int64))
   assert np.max(np.diff(E[r].indptr),initial=0)<=1
   if r:assert np.max(abs(np.asarray(E[r].sum(axis=0))),initial=0)==0
   if r<d:
    assert zero(dp[r]@E[r]-E[r+1]@df[r])
    assert zero(dp[r].T@E[r+1]-E[r]@df[r].T)
  # Wrong even extension in an edge direction violates the derivative identity.
  bad=E[1].copy();bad.data=abs(bad.data)
  defect=dp[0]@E[0]-bad@df[0];assert not zero(defect)
  rows.append(dict(d=d,L=L,period=2*(L+1),free_dimensions=list(map(len,f)),periodic_dimensions=list(map(len,p)),both_derivatives_exact=True,norm_multiplicity=2**d,wrong_edge_parity_defect_entries=defect.nnz))
 return rows


def nested_projection():
 # Hodge inverse and zero-extension identities are distinct constructions.
 import sympy as s
 small,ds=complex_box(4,1);large,dl=complex_box(4,2)
 ext=[]
 for r in range(5):
  ids={cell:i for i,cell in enumerate(large[r])}
  rows=[ids[cell] for cell in small[r]]
  ext.append(coo_matrix((np.ones(len(rows),dtype=np.int64),(rows,np.arange(len(rows)))),shape=(len(large[r]),len(small[r]))).tocsr())
 assert zero(dl[2].T@ext[3]-ext[2]@ds[2].T)
 assert zero(dl[1].T@ext[2]@ds[2].T)
 Dsmall=s.Matrix(np.vstack([ds[2].T.toarray(),ds[3].toarray()]))
 Hsmall=Dsmall.T*Dsmall;Psmall=Dsmall*Hsmall.inv()*Dsmall.T
 assert Psmall*Psmall==Psmall
 assert Psmall[24:25,24:25]==s.eye(1)
 assert Psmall[:24,24:25]==s.zeros(24,1)
 assert s.Matrix(ds[1].T.toarray())*Psmall[:24,:24]==s.zeros(len(small[1]),24)
 Dlarge=vstack([dl[2].T,dl[3]]).astype(float).tocsr()
 Hlarge=(Dlarge.T@Dlarge).tocsc()
 Plarge=Dlarge@splu(Hlarge).solve(Dlarge.T.toarray())
 E=block_diag([ext[2],ext[4]]).toarray()
 embedded=E@np.array(Psmall,dtype=float)@E.T
 nesting=np.linalg.norm(Plarge@embedded-embedded)
 minimum=float(np.linalg.eigvalsh(Plarge-embedded).min())
 assert nesting<2e-12 and minimum>-2e-12
 # Closed free-box three-charges do NOT obey the analogous zero-extension
 # rule. The two opposite 012 faces form a closed relative charge here.
 q=np.zeros(len(small[3]),dtype=np.int64);q[:2]=1
 assert np.max(abs(ds[3]@q))==0
 wrong=dl[3]@ext[3]@q
 assert np.max(abs(wrong))>0
 return dict(small_projection_rank=int(s.trace(Psmall)),large_projection_rank=int(round(np.trace(Plarge))),exact_codifferential_extension=True,nesting_error=float(nesting),minimum_projection_order_eigenvalue=minimum,wrong_closed_charge_extension_defect=wrong.tolist())


def positive_integrals(order=60):
 # A non-coordinate two-dimensional subspace inside R3, non-diagonal K,
 # and several overlapping rank-one interactions.
 V=np.array([[1.,1.],[-1.,1.],[0.,-2.]])
 Q,_=np.linalg.qr(V);eigen=np.array([.7,1.1]);S=Q@np.diag(np.sqrt(eigen));K=S@S.T
 U=np.array([[1.,-1.,0.],[0.,1.,1.],[1.,0.,-1.],[1.,1.,0.]])
 coeff=np.array([.006,-.004,.005,.003]);absu=abs(U);u1=absu.sum(axis=1)
 delta=float(np.max((abs(coeff)*u1)@absu));M3=float(np.max((abs(coeff)*u1*u1)@absu))
 k=float(np.max(abs(K).sum(axis=1)));assert k*delta<1
 C=k/(1-k*delta)
 x,w=hermgauss(order);grid=np.array(list(itertools.product(x,x)));wg=np.outer(w,w).ravel()/np.pi
 points=np.sqrt(2)*grid@S.T;interaction=np.cos(points@U.T)@coeff
 rows=[]
 directions=[np.array([.3,-.2,.1]),np.array([-.2,.15,.45]),np.array([.1,.1,-.2])]
 for tilt in [np.array([0.,0.,0.]),np.array([.2,-.3,.1]),np.array([-.4,.1,.3])]:
  exponent=interaction+points@tilt;weights=wg*np.exp(exponent);norm=weights.sum();weights/=norm
  for a,b,c in [(directions[0],directions[0],directions[0]),tuple(directions)]:
   obs=[points@v for v in [a,b,c]];center=[v-weights@v for v in obs]
   third=float(weights@(center[0]*center[1]*center[2]))
   bound=M3*C**3*math.prod(float(np.linalg.norm(v,ord=3)) for v in [a,b,c])
   assert abs(third)<=bound+2e-12
   rows.append(dict(tilt=tilt.tolist(),third_cumulant=third,derived_bound=bound))
 # Taylor remainder for the exact positive finite measure at zero tilt.
 w0=wg*np.exp(interaction);z0=w0.sum();w0/=z0;a=directions[0]
 covariance=points.T@(w0[:,None]*points)
 lower=K@np.linalg.inv(np.eye(3)+delta*K)
 upper=K@np.linalg.inv(np.eye(3)-delta*K)
 lower_margin=float(np.linalg.eigvalsh(Q.T@(covariance-lower)@Q).min())
 upper_margin=float(np.linalg.eigvalsh(Q.T@(upper-covariance)@Q).min())
 assert lower_margin>=-3e-12 and upper_margin>=-3e-12
 mean=float(w0@(points@a));var=float(w0@((points@a-mean)**2))
 for t in [.1,.3,1.,2.]:
  exact=math.log(float(np.sum(wg*np.exp(interaction+t*(points@a))))/z0)
  rem=abs(exact-t*mean-t*t*var/2);bound=M3*C**3*float(np.linalg.norm(t*a,ord=3))**3/6
  assert rem<=bound+3e-13
  rows.append(dict(source_scale=t,log_mgf_remainder=rem,derived_bound=bound))
 return dict(order=order,k_schur=k,delta=delta,M3=M3,contraction=k*delta,cramer_rao_lower_margin=lower_margin,convexity_upper_margin=upper_margin,cases=rows)


def collective_control():
 # Exact one-dimensional reduction preserves a non-Gaussian fourth cumulant
 # at every ambient dimension. Gauss-Hermite integration is deterministic.
 x,w=hermgauss(100);z=np.sqrt(2)*x;zeta=.4;weights=w*np.exp(zeta*np.cos(z));weights/=weights.sum()
 var=float(weights@(z*z));fourth=float(weights@(z**4))-3*var*var
 assert abs(fourth)>.01
 cases=[]
 for n in [1,4,16,64,256,1024]:
  norm3cubed=n**(-.5);M3=zeta*math.sqrt(n)
  assert abs(M3*norm3cubed-zeta)<1e-14
  cases.append(dict(dimension=n,source_ell3_cubed=norm3cubed,third_influence_bound=M3,product=M3*norm3cubed))
 return dict(variance=var,fourth_cumulant=fourth,dimension_independent_non_gaussian=True,cases=cases)


def theta_upper_hypothesis_control():
 x,w=hermgauss(100);z=np.sqrt(2)*x
 weights=w*np.exp(-.2*np.cos(z));weights/=weights.sum()
 variance=float(weights@(z*z))
 assert variance>1.05
 return dict(variance=variance,reference_variance=1.,hessian_perturbation_bound=.2,qualification='A uniformly convex small cosine perturbation need not have covariance below its Gaussian reference. The actual theta MGF domination is a separate structural input.')

def cube(d):
    cells, ds = complex_box(d, 1)
    return cells, [sp.Matrix(matrix.toarray()) for matrix in ds]


def exact_hodge():
 rows=[]
 for d in [3,4]:
  cells,ds=cube(d);B=ds[2];H=B*B.T
  if d>3:H+=ds[3].T*ds[3]
  G=H.inv();I=sp.eye(H.rows);c=sp.Rational(1,32);T=(I-c*H).inv()
  H1=ds[0]*ds[0].T+ds[1].T*ds[1]
  P=ds[1]*H1.inv()*ds[1].T;R=B.T*G*B
  assert P+R==sp.eye(B.cols) and P*R==sp.zeros(B.cols)
  assert G*T==G+c*T
  for beta in [sp.Rational(1,5),sp.Rational(3,2)]:
   A=beta*(G-c*I);h=sp.Matrix([sp.Rational((i*7)%11-5,17) for i in range(B.cols)])
   source=-sp.sqrt(beta)*G*B*h;j=A.inv()*source
   assert sp.simplify(j+T*B*h/sp.sqrt(beta))==sp.zeros(B.rows,1)
   assert sp.simplify((h.T*P*h+source.T*A.inv()*source)[0]-(h.T*h+c*h.T*B.T*T*B*h)[0])==0
   # Distinct covariance decompositions for arbitrary positive charge covariance.
   seed=sp.Matrix([[((i+2)*(j+3))%7-3 for j in range(3)] for i in range(B.rows)])
   V=seed*seed.T/sp.Integer(100000)
   Cphi=A-4*sp.pi**2*A*V*A
   Cx=sp.eye(B.cols)+c*B.T*T*B-B.T*T*Cphi*T*B/beta
   expected=P+4*sp.pi**2*beta*B.T*G*V*G*B
   assert sp.simplify(Cx-expected)==sp.zeros(B.cols)
  rows.append(dict(d=d,plaquettes=B.cols,three_cells=B.rows,hodge_spectrum={str(v):m for v,m in H.eigenvals().items()},exact_identities=True))
 return rows


def three_cube():
 # Positive Gaussian quadrature of the auxiliary phi density versus independent
 # magnetic and Poisson-comb formulae for the original full lifted flux.
 _,ds=cube(3);b=np.array(ds[2],dtype=float).ravel();P=np.eye(6)-np.outer(b,b)/6
 c=1/32;rows=[]
 for beta in [.1,.4,1.,3.]:
  A=beta*(1/6-c);T=1/(1-6*c)
  n=np.arange(-80,81,dtype=float);w=np.exp(-2*np.pi**2*beta*n*n/6);w/=w.sum()
  varq=float(w@(n*n))
  def theta(x):
   ls=np.arange(math.floor(x)-12,math.ceil(x)+13,dtype=float)
   return np.exp(-(x-ls)**2/(2*beta*c)).sum()/math.sqrt(2*np.pi*beta*c)
  # Integrate in standard-Gaussian coordinates, bounded interval has omitted
  # standard tail below 4e-33; shifted tilt checks keep the quadratic maximum
  # within this range. Repeat with width14 to challenge the truncation.
  def integral(j=0,power=0,width=12):
   return quad(lambda z: ((math.sqrt(A)*z)**power)*math.exp(-z*z/2+j*math.sqrt(A)*z)*theta(math.sqrt(A)*z)/math.sqrt(2*math.pi),-width,width,epsabs=2e-12,epsrel=2e-12,limit=400)[0]
  norm=integral();varphi=integral(power=2)/norm
  varexpected=A-4*np.pi**2*A*A*varq
  assert abs(varphi-varexpected)<2e-12
  for index,h in enumerate([np.array([.2,-.1,.3,.05,-.4,.15]),b*.11,P@np.array([.3,.4,-.2,.1,.15,.25])]):
   bh=float(b@h);s=-math.sqrt(beta)*bh/6;j=-T*bh/math.sqrt(beta)
   magnetic=math.exp(-float(h@P@h)/2)*float(w@np.cos(2*np.pi*n*s))
   comb=np.exp(-.5*np.sum((h[None,:]+n[:,None]*b[None,:]/math.sqrt(beta))**2,axis=1)).sum()/np.exp(-3*n*n/beta).sum()
   pref=math.exp(-float(h@h)/2-c*T*bh*bh/2)
   aux=pref*integral(j=j)/norm
   aux14=pref*integral(j=j,width=14)/integral(width=14)
   assert max(abs(magnetic-comb),abs(magnetic-aux),abs(aux-aux14))<4e-12
   wrong_sign=pref*quad(lambda z:math.cos(j*math.sqrt(A)*z)*math.exp(-z*z/2)*theta(math.sqrt(A)*z)/math.sqrt(2*math.pi),-12,12,epsabs=1e-12,limit=400)[0]/norm
   if index<2:assert abs(wrong_sign-aux)>1e-4
   rows.append(dict(beta=beta,source=index,magnetic=magnetic,poisson_comb=float(comb),positive_auxiliary_quad=aux,maximum_error=float(max(abs(magnetic-comb),abs(magnetic-aux))),cutoff_error=abs(aux-aux14),wrong_characteristic_instead_of_mgf_error=abs(wrong_sign-aux),aux_covariance_error=abs(varphi-varexpected)))
 return rows


def wedge_symmetry():
 # Every invariant real symmetric quadratic form on Lambda^2(R4) is scalar
 # under the full signed-permutation group. Test via exact linear constraints.
 pairs=list(itertools.combinations(range(4),2));basis=[]
 for i in range(6):
  for j in range(i,6):
   E=sp.zeros(6);E[i,j]=E[j,i]=1;basis.append(E)
 generators=[]
 for r in range(4):
  generators.append(sp.diag(*[(-1 if r in I else 1) for I in pairs]))
 for r in range(3):
  perm=list(range(4));perm[r],perm[r+1]=perm[r+1],perm[r];U=sp.zeros(6)
  for j,I in enumerate(pairs):
   image=tuple(perm[i] for i in I);K=tuple(sorted(image));U[pairs.index(K),j]=1 if image==K else -1
  generators.append(U)
 eq=[]
 for U in generators:
  mats=[U.T*E*U-E for E in basis]
  eq.extend([[m[i,j] for m in mats] for i in range(6) for j in range(6)])
 ker=sp.Matrix(eq).nullspace();assert len(ker)==1
 invariant=sum((ker[0][k]*E for k,E in enumerate(basis)),sp.zeros(6))
 assert invariant==invariant[0,0]*sp.eye(6) and invariant[0,0]!=0
 return dict(generators=len(generators),symmetric_parameters=len(basis),invariant_dimension=len(ker),scope='Quadratic-form algebra only; no homogenized energy existence or identification follows.')

D = 4
C = 1 / 32
BASES = [list(itertools.combinations(range(D), r)) for r in range(D + 1)]


def wedge(deltas, r):
    n = deltas[0].shape[0]
    result = np.zeros((len(BASES[r + 1]) * n, len(BASES[r]) * n), complex)
    ids = {I: i for i, I in enumerate(BASES[r])}
    for row, J in enumerate(BASES[r + 1]):
        for j, mu in enumerate(J):
            col = ids[J[:j] + J[j + 1:]]
            result[row*n:(row+1)*n, col*n:(col+1)*n] += (-1)**j * deltas[mu]
    return result


def preconditioner(deltas, local_c=C):
    d2, d3 = wedge(deltas, 2), wedge(deltas, 3)
    assert np.linalg.norm(d3 @ d2) < 2e-13
    derivative = np.vstack([d2.conj().T, d3])
    laplacian = derivative.conj().T @ derivative
    return derivative @ np.linalg.solve(laplacian, derivative.conj().T) - local_c * derivative @ derivative.conj().T


def multiplier(k):
    return preconditioner([np.array([[np.expm1(1j*t)]]) for t in k])


def continuum(p):
    return preconditioner([np.array([[1j*t]]) for t in p], local_c=0)


def gaussian_covariance(K, A):
    # Direct integration of a proper Gaussian density on range(K):
    # inverse of its precision in orthonormal compatible coordinates.
    eigen, vectors = np.linalg.eigh(K)
    V, positive = vectors[:, eigen > 1e-10], eigen[eigen > 1e-10]
    precision = np.diag(1 / positive) - V.conj().T @ A @ V
    assert np.min(np.linalg.eigvalsh(precision)) > .5
    return V @ np.linalg.solve(precision, V.conj().T)


def layered_checks():
    alpha, eta = -.12, .09
    first = np.diag([1.] * 6 + [0.])
    avg, difference = alpha * first, eta * first
    phase_A = np.diag([alpha + eta, alpha - eta])
    A = np.kron(first, phase_A)
    e0 = np.array([[1.], [1.]]) / np.sqrt(2)
    e1 = np.array([[1.], [-1.]]) / np.sqrt(2)
    embed = np.kron(np.eye(7), e0)
    U = np.hstack([embed, np.kron(np.eye(7), e1)])
    pi_shift = np.array([np.pi, 0., 0., 0.])
    Kenv = multiplier(pi_shift)
    effective = avg + difference @ np.linalg.solve(np.eye(7) - Kenv @ avg, Kenv @ difference)
    shortcut_defect = np.linalg.norm(effective - avg)
    assert shortcut_defect > .005
    rows, fiber_errors, precision_errors = [], [], []
    for p in [np.array([1., 2., -1., .5]), np.array([1., 0., 0., 0.]), np.array([0., 1., 0., 0.])]:
        K0 = continuum(p)
        limiting = np.linalg.solve(np.eye(7) - K0 @ effective, K0)
        wrong = np.linalg.solve(np.eye(7) - K0 @ avg, K0)
        errors = []
        for a in [1/8, 1/16, 1/32, 1/64, 1/128, 1/256]:
            k = a * p
            shift = np.array([[0., 1.], [1., 0.]])
            deltas = [np.exp(1j*k[0]) * shift - np.eye(2)]
            deltas += [np.expm1(1j*k[j]) * np.eye(2) for j in range(1, 4)]
            K = preconditioner(deltas)
            blocks = np.zeros((14, 14), complex)
            blocks[:7, :7], blocks[7:, 7:] = multiplier(k), multiplier(k + pi_shift)
            ferr = np.linalg.norm(U.conj().T @ K @ U - blocks)
            fiber_errors.append(float(ferr))
            assert ferr < 2e-9
            covariance = gaussian_covariance(K, A)
            response = np.linalg.solve(np.eye(14) - K @ A, K)
            perr = np.linalg.norm(covariance - response)
            precision_errors.append(float(perr))
            assert perr < 2e-10
            projected = embed.conj().T @ covariance @ embed
            errors.append(float(np.linalg.norm(projected - limiting)))
        assert errors[-1] < errors[0] / 20
        rows.append(dict(direction=p.tolist(),mesh=[1/8,1/16,1/32,1/64,1/128,1/256],limit_errors=errors,mean_hessian_shortcut_limit_error=float(np.linalg.norm(wrong-limiting))))
    assert max(row['mean_hessian_shortcut_limit_error'] for row in rows) > .005
    return dict(alpha=alpha,eta=eta,effective_diagonal=np.real(np.diag(effective)).tolist(),mean_hessian_shortcut_matrix_error=float(shortcut_defect),maximum_fiber_identity_error=max(fiber_errors),maximum_precision_response_error=max(precision_errors),cases=rows)


def symmetry_commutant():
    # General (not assumed symmetric) two-form matrices commuting with all
    # coordinate reflections and adjacent swaps have only one free parameter.
    import sympy as s
    pairs = BASES[2]
    generators = []
    for mu in range(4):
        generators.append(s.diag(*[-1 if mu in I else 1 for I in pairs]))
    for mu in range(3):
        perm = list(range(4))
        perm[mu], perm[mu+1] = perm[mu+1], perm[mu]
        G = s.zeros(6)
        for col, I in enumerate(pairs):
            J = [perm[i] for i in I]
            sign = 1 if J[0] < J[1] else -1
            G[pairs.index(tuple(sorted(J))), col] = sign
        generators.append(G)
    variables = s.symbols('b:36')
    B = s.Matrix(6, 6, variables)
    equations = [entry for G in generators for entry in B*G-G*B]
    matrix, _ = s.linear_eq_to_matrix(equations, variables)
    null = matrix.nullspace()
    assert len(null) == 1
    candidate = s.Matrix(6, 6, null[0])
    assert candidate == candidate[0, 0] * s.eye(6)
    return dict(unknown_entries=36,generators=7,commutant_dimension=1,antisymmetric_component_excluded=True)


def invariant_mixture_control():
    # Average four rotated layered Gaussian environments. The global layer
    # orientation is a translation-invariant random label. Cubic symmetry
    # of the average does not make this environment spatially ergodic.
    alpha, eta = -.12, .09
    first = np.diag([1.] * 6 + [0.])
    avg, diff = alpha * first, eta * first
    p = np.array([0., 0., 0., 1.])
    K0 = continuum(p)
    test = np.zeros(7)
    test[BASES[2].index((0, 1))] = 1
    variances = []
    for mu in range(4):
        k = np.zeros(4)
        k[mu] = np.pi
        Km = multiplier(k)
        effective = avg + diff @ np.linalg.solve(np.eye(7)-Km@avg, Km@diff)
        covariance = np.linalg.solve(np.eye(7)-K0@effective, K0)
        variances.append(float(np.real(test @ covariance @ test)))
    # A mixture of centered Gaussians has fourth cumulant 3 Var(variance).
    fourth = 3 * float(np.var(variances))
    assert fourth > 1e-6
    return dict(component_variances=variances,mixture_fourth_cumulant=fourth,translation_invariant_global_label=True,qualification='Comparison model only; not a counterexample to the actual small-carrier Villain law or its uniform third-influence hypotheses.')


def image_score_and_reflection():
    # Positive image moments versus derivatives of the independently summed
    # Villain weight. High precision differences challenge the sqrt(beta)
    # normalization and the conditional-variance subtraction.
    mp.mp.dps = 60
    rows = []
    for beta in [2, 5, 20]:
        b = mp.mpf(beta)
        for u in [mp.mpf('0'), mp.mpf('.3'), mp.pi-mp.mpf('.1'), mp.pi]:
            def weight(x, cutoff=20):
                return sum(mp.exp(-b*(x-2*mp.pi*k)**2/2) for k in range(-cutoff,cutoff+1))
            values = [mp.sqrt(b)*(u-2*mp.pi*k) for k in range(-20,21)]
            weights = [mp.exp(-x*x/2) for x in values]
            z = sum(weights)
            mean = sum(w*x for w,x in zip(weights,values))/z
            variance = sum(w*(x-mean)**2 for w,x in zip(weights,values))/z
            step = mp.mpf('1e-12')
            derivative = -(mp.log(weight(u+step))-mp.log(weight(u-step)))/(2*step*mp.sqrt(b))
            second = -(mp.log(weight(u+step))-2*mp.log(weight(u))+mp.log(weight(u-step)))/(step**2*mp.sqrt(b))
            assert variance > 0
            assert abs(mean-derivative) < mp.mpf('1e-18')
            assert abs(second-mp.sqrt(b)*(1-variance)) < mp.mpf('1e-17')
            cutoff_error = abs(weight(u,14)/z-1)
            assert cutoff_error < mp.mpf('1e-50')
            rows.append(dict(beta=beta,angle=float(u),score=float(mean),image_variance=float(variance),score_derivative_error=float(abs(mean-derivative)),score_curvature_error=float(abs(second-mp.sqrt(b)*(1-variance))),cutoff_relative_error=float(cutoff_error)))
    reflection = []
    for p in [sp.Matrix([1,0,0]),sp.Matrix([1,2,2]),sp.Matrix([2,-3,6])]:
        w = sp.sqrt((p.T*p)[0])
        conserved = sp.zeros(4,3)
        conserved[0,:] = -sp.I*p.T/w
        conserved[1:4,:] = sp.eye(3)
        metric = sp.diag(-1,1,1,1)
        reflected = sp.simplify(conserved.conjugate().T*metric*conserved)
        transverse = sp.eye(3)-p*p.T/(p.T*p)[0]
        assert reflected == transverse
        assert transverse*transverse == transverse and transverse.rank() == 2
        # Ignoring conservation leaves a negative time-component direction.
        assert metric[0,0] < 0
        reflection.append(dict(momentum=list(map(int,p)),energy=str(w),rank=transverse.rank(),conserved_reflection_form_exact=True))
    return dict(image_cases=rows,reflection=reflection)


def run():
    low, high = positive_integrals(40), positive_integrals(60)
    comparison = max(abs(a.get('third_cumulant',a.get('log_mgf_remainder'))-b.get('third_cumulant',b.get('log_mgf_remainder'))) for a,b in zip(low['cases'],high['cases']))
    assert comparison < 3e-12
    return dict(
        free_reflection=reflection(), nested_hodge_projection=nested_projection(),
        positive_integral_cumulants=high, quadrature_order_comparison=comparison,
        collective_non_gaussian_control=collective_control(),
        theta_upper_hypothesis_control=theta_upper_hypothesis_control(),
        exact_flux_hodge=exact_hodge(), actual_three_cube_flux=three_cube(),
        symmetric_form_commutant=wedge_symmetry(), layered_response=layered_checks(),
        general_form_commutant=symmetry_commutant(), invariant_mixture_control=invariant_mixture_control(),
        physical_score_and_reflection=image_score_and_reflection())


if __name__ == '__main__':
    results = run()
    print(json.dumps(results, indent=2))
    print('per_element: executed exact integer cochain reflection and Hodge identities, plus scalar image-score and conditional-variance normalization challenges.')
    print('per_site: executed a wrong closed-charge zero-extension control and fixed-site image kernels; uniform carrier tails are checked and not executed, using the written mass bounds.')
    print('per_mode: executed Bloch-fiber versus real-space matrices, independent Gaussian precision inversion, exact signed-permutation commutants and rank-two conserved reflection forms.')
    print('per_block: executed positive finite-measure cumulants, real auxiliary MGF versus original magnetic and Poisson sums, and collective/nonergodic comparison controls.')
    print('lattice_wide: checked and not executed: the all-box Riesz bound, noise-factor state matching, two-replica concentration, spectral limit and fixed-beta full-score continuum theorem depend on the written analytic proofs, awaiting independent review.')
    print(f'TOTAL: PASS={len(results)} FAIL=0')
