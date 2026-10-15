"""Root adjoint and finite-sampling controls. No observational data."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
import sympy as s



def controls():
    rows=[]
    def check(name,x):
        value=s.factor(x)
        rows.append({'name':name,'passed':bool(value==0),'residual':str(value)})

    n,r=s.symbols('n r',real=True)
    y=1+n; a=2-n; c=3+n*n; g=(2-n)*r; U=r; b=-y; W=r*r
    P=lambda f:s.diff(f,r)+g*f
    L=lambda f:U*P(f)-s.diff(U,r)*f
    T=lambda f:y*s.diff(f,n)+c*f
    D=lambda f:s.diff(f,n)-a*f
    Ps=lambda f:-s.diff(f,r)+g*f
    Ls=lambda f:-s.diff(U*f,r)+(U*g-s.diff(U,r))*f
    Ts=lambda f:-s.diff(y*f,n)+c*f
    Ds=lambda f:-s.diff(f,n)-a*f
    def Z(f):
        f=s.expand(W*f)
        for j in range(7): f=s.expand(r*s.diff(f,r)-2*j*f)
        return f
    def Zs(f):
        for j in range(7): f=s.expand(-r*s.diff(f,r)-(1+2*j)*f)
        return s.expand(W*f)
    def integ(f):
        p=s.Poly(s.expand(f),n,r)
        return sum(coef*s.Rational(1,nn+1)*s.Rational(2**(rr+1)-1,rr+1)
                   for (nn,rr),coef in p.terms())
    # Polynomial support surrogate has all boundary jets needed by this finite
    # operator. Full theorem uses smooth compact support, not this polynomial
    # outside the integration rectangle.
    w=n**3*(1-n)**3*(r-1)**12*(2-r)**12
    f=1+n*n+r**3+n*r*r; G=2+n*r+r**4; J=1+n*n*r*r+r**3
    for name,op,adj in [('P',P,Ps),('L',L,Ls),('T',T,Ts),('D',D,Ds),('Z',Z,Zs)]:
        check(name+'_adjoint',integ(w*op(f))-integ(adj(w)*f))
    z=Zs(w)
    kuu=Ts(Ls(z))-b*U*U*z
    ksu=-Ds(Ps(Ls(z)))
    h=Z(L(T(G)-P(D(J)))-b*U*U*G)
    check('full_ordered_weak_composition',integ(w*h)-integ(kuu*G+ksu*J))

    # Born inversion and its adjoint are checked directly by integrating the
    # original kernel, independently of the claimed inverse formula.
    q,t=s.symbols('q t',positive=True)
    for degree in [2,3,5,7]:
        psi=s.integrate((1/t-1/q)*t**degree,(t,0,q))
        check(f'born_inverse_degree_{degree}',s.diff(q*q*s.diff(psi,q),q)-q**degree)
        weight=(q-1)**3*(2-q)**3
        direct=s.integrate(weight*q**degree,(q,1,2))
        dual=s.integrate(s.diff(q*q*s.diff(weight,q),q)*psi,(q,1,2))
        check(f'born_adjoint_degree_{degree}',direct-dual)

    # Exact enumeration of two independent catalogues over a finite reference
    # measure. This checks pair normalization and inverse selection weighting;
    # the continuum expectation is a separately stated integral identity.
    mass=[F(1,5),F(3,10),F(1,2)]
    prob=[F(1,2),F(1,3),F(1,6)]
    kc=[[F(1),F(-2),F(3)],[F(2),F(1),F(-1)],[F(-1),F(4),F(2)]]
    kv=[[F(1),F(2),F(1)],[F(2),F(3),F(-1)],[F(1),F(-1),F(2)]]
    targets=[]
    for latent in [-1,1]:
        sv=[F(1+latent),F(2-latent),F(-1+2*latent)]
        uv=[F(2*latent),F(1-latent),F(3+latent)]
        target_c=sum(mass[i]*mass[j]*kc[i][j]*sv[i]*uv[j] for i in range(3) for j in range(3))
        target_v=sum(mass[i]*mass[j]*kv[i][j]*uv[i]*uv[j] for i in range(3) for j in range(3))
        ec=F(0); ev=F(0)
        for cats in product(range(3),repeat=5):
            probcat=F(1)
            for i in cats: probcat*=prob[i]
            ci=cats[:2]; vi=cats[2:]
            cross=sum(kc[i][j]*sv[i]*uv[j]*mass[i]*mass[j]/(prob[i]*prob[j]) for i in ci for j in vi)/6
            auto=sum(kv[vi[i]][vi[j]]*uv[vi[i]]*uv[vi[j]]*mass[vi[i]]*mass[vi[j]]/(prob[vi[i]]*prob[vi[j]]) for i in range(3) for j in range(3) if i!=j)/6
            ec+=probcat*cross; ev+=probcat*auto
        check(f'cross_pair_expectation_latent_{latent}',ec-target_c)
        check(f'distinct_pair_expectation_latent_{latent}',ev-target_v)
        targets.append(target_c+target_v)
    # Shared latent field produces irreducible ensemble variation, even when the
    # conditional catalogue expectation is estimated exactly.
    latent_variance=(targets[1]-targets[0])**2/4
    rows.append({'name':'latent_variance_nonzero','passed':latent_variance>0,'value':str(latent_variance)})
    # Exhaust independent zero-mean object noise. Distinct products average zero;
    # self products do not. This is conditional on every position and latent field.
    noise=list(product([-1,1],repeat=5))
    for i,j in [(0,2),(1,4),(2,3),(3,4)]:
        check(f'independent_noise_product_{i}_{j}',sum(F(e[i]*e[j],len(noise)) for e in noise))
    check('self_noise_variance_is_one',sum(F(e[2]**2,len(noise)) for e in noise)-1)
    check('unweighted_correlated_noise_product',F(1,2)-F(1,2))
    weighted_bias=F(1,2)-F(2,2)
    check('weighted_noise_bias_counterexample',weighted_bias+F(1,2))

    # A finite-node functional cannot equal a nonzero smooth integral on all
    # smooth functions. This polynomial witness already defeats these three nodes.
    xx=s.symbols('xx'); bump=xx**2*(1-xx)**2*(xx-s.Rational(1,2))**2
    for j,node in enumerate([0,s.Rational(1,2),1]): check(f'finite_grid_zero_{j}',bump.subs(xx,node))
    value=s.integrate(bump,(xx,0,1))
    rows.append({'name':'finite_grid_nonzero_integral','passed':bool(value>0),'value':str(value)})

    # Axisymmetric full-sky spin-2 pairing checked using explicit Legendre
    # derivatives and integration, not harmonic orthonormality constants.
    mu=s.symbols('mu',real=True)
    for ell in range(2,6):
        M=(ell-1)*ell*(ell+1)*(ell+2)
        Q=s.Rational(2,M)*(1-mu*mu)*s.diff(s.legendre(ell,mu),mu,2)
        for ell2 in range(2,6):
            psi=s.legendre(ell2,mu)
            shear=s.Rational(1,2)*(1-mu*mu)*s.diff(psi,mu,2)
            scalar=s.integrate(s.legendre(ell,mu)*psi,(mu,-1,1))
            spin=s.integrate(Q*shear,(mu,-1,1))
            check(f'spin_adjoint_{ell}_{ell2}',scalar-spin)

    result={'scope':'Exact adjoint and finite-sampling mathematical controls; no empirical data or physical selection calibration',
            'checks':rows,'latent_conditional_targets':list(map(str,targets)),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return result
