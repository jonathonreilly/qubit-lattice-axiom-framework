"""Actual 4D paired S4' incidences and a one-link SU(2) Haar slice.
The slice fixes other interior links; it is not the full cube integral.
"""
from itertools import product, permutations, combinations
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, math, time
import mpmath as mp
import sympy as sp
started=time.monotonic(); checks={}; controls={}
def ck(n,v,control=False):
    (controls if control else checks)[n]=bool(v)
    assert v,n

d=4; L=3; m=1; pL=5*L-4; orders=list(permutations(range(d)))
zero=(0,)*d

def add(x,y):return tuple(a+b for a,b in zip(x,y))
def e(mu,k=1):return tuple(k if j==mu else 0 for j in range(d))
def axis_word(start,finish,order):
    x=list(start); word=[]
    for mu in order:
        sg=1 if finish[mu]>=x[mu] else -1
        for _ in range(abs(finish[mu]-x[mu])):
            if sg<0:x[mu]-=1
            word.append(((tuple(x),mu),sg))
            if sg>0:x[mu]+=1
    assert tuple(x)==finish
    return word

def word(mu,y,order):
    first=axis_word(zero,y,order)
    middle=[((add(y,e(mu,j)),mu),1) for j in range(L)]
    last=axis_word(e(mu,L),add(y,e(mu,L)),order)
    return first+middle+[(edge,-sg) for edge,sg in reversed(last)]

base={mu:[word(mu,y,o) for y in product(range(-m,m+1),repeat=d) for o in orders] for mu in range(d)}
ck('actual_contour_count',all(len(a)==math.factorial(d)*L**d for a in base.values()))
ck('actual_contour_length',all(len(w)<=pL for a in base.values() for w in a))
ck('one_edge_occurs_at_most_twice_per_contour',all(max(Counter(edge for edge,sg in w).values(),default=0)<=2 for a in base.values() for w in a))

def block_of(x,T):return tuple(((v+m)//L)%T for v in x)
def modpos(x,M):return tuple(v%M for v in x)
# Full small periodic torus, including the duplicated endpoint geometry T=2.
T=2; M=T*L; blocks=list(product(range(T),repeat=d)); sites=list(product(range(M),repeat=d))
interior={}; all_links=[]
for x in sites:
    for mu in range(d):
        edge=(x,mu); all_links.append(edge)
        bx=block_of(x,T); by=block_of(add(x,e(mu)),T)
        if bx==by:interior[edge]=bx
n_l=4*L**3*(L-1); nP=6*n_l
ck('actual_interior_link_count_each_block',all(sum(v==B for v in interior.values())==n_l for B in blocks))
plaquette_reads=defaultdict(set); link_degrees=Counter()
for x in sites:
    for mu,nu in combinations(range(d),2):
        P=(x,mu,nu)
        edges=((x,mu),(modpos(add(x,e(mu)),M),nu),(modpos(add(x,e(nu)),M),mu),(x,nu))
        for edge in edges:
            link_degrees[edge]+=1
            if edge in interior:plaquette_reads[interior[edge]].add(P)
ck('six_plaquettes_per_fine_link',all(link_degrees[edge]==6 for edge in all_links))
ck('actual_PY_per_cube_count',all(len(plaquette_reads[B])<=nP for B in blocks))
readers=defaultdict(set); endpoints_ok=True
for B in blocks:
    shift=tuple(L*v for v in B)
    for mu in range(d):
        C=(B,mu); B2=tuple((B[j]+(j==mu))%T for j in range(d)); endpoints={B,B2}
        for w in base[mu]:
            for (x,nu),sg in w:
                xx=modpos(add(x,shift),M); yy=modpos(add(xx,e(nu)),M)
                endpoints_ok &= block_of(xx,T) in endpoints and block_of(yy,T) in endpoints
                readers[xx,nu].add(C)
ck('paired_contours_stay_in_two_endpoint_blocks',endpoints_ok)
ck('interior_link_reads_at_most_eight_coarse_kernels',all(len(readers[edge])<=8 for edge in interior))
ck('interblock_link_reads_one_coarse_kernel',all(len(readers[edge])<=1 for edge in all_links if edge not in interior))
ck('omitting_kernel_endpoint_collar_rejected',max(len(readers[edge]) for edge in interior)>1,True)

# One central fine link b=(0,e_0), with every other fine link I. Exact
# contour words are U^k. Keep all 8 coarse kernels with an endpoint at B=0.
central=(zero,0); distributions={}
for mu in range(d):
    for incoming in (False,True):
        shift=e(mu,-L) if incoming else zero
        cnt=Counter()
        for w in base[mu]:
            k=sum(sg for (x,nu),sg in w if (add(x,shift),nu)==central)
            cnt[k]+=1
        distributions[(mu,incoming)]=cnt
norm=math.factorial(d)*L**d
ck('eight_actual_kernel_means_normalized',len(distributions)==8 and all(sum(c.values())==norm for c in distributions.values()))
ck('central_link_nontrivial_in_all_eight_means',all(any(k and n for k,n in c.items()) for c in distributions.values()))
# A coarse kernel outside the endpoint blocks must be constant in this link.
ck('nonendpoint_contours_do_not_read_central_link',all(
    all((add(x,(3,3,3,3)),nu)!=central for (x,nu),sg in w) for a in base.values() for w in a))

# Exact noncommuting SU(2) trace check at rational unit quaternions.
I=sp.I; eye=sp.eye(2)
sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-I],[I,0]]); sz=sp.diag(1,-1)
axis=(sp.Rational(2,3),sp.Rational(2,3),sp.Rational(1,3))
U=sp.Rational(3,5)*eye+I*sp.Rational(4,5)*(axis[0]*sx+axis[1]*sy+axis[2]*sz)
VX=sp.Rational(5,13)*eye+I*sp.Rational(12,13)*sx
VY=sp.Rational(8,17)*eye+I*sp.Rational(15,17)*sy
ck('actual_SU2_unitarity_and_noncommuting_coarse_data',sp.simplify(U.det())==1 and sp.simplify(U.H*U-eye)==sp.zeros(2) and VX*VY!=VY*VX)
trace_ok=True
for cl,cnt in distributions.items():
    Mat=sp.zeros(2)
    for k,n in cnt.items():Mat+=sp.Rational(n,norm)*(U**k)
    a=sp.simplify(sp.trace(Mat)/2)
    b=sp.simplify(sp.trace((axis[0]*sx+axis[1]*sy+axis[2]*sz)*Mat)/(2*I))
    for V,cc,ss,j in [(VX,sp.Rational(5,13),sp.Rational(12,13),0),(VY,sp.Rational(8,17),sp.Rational(15,17),1)]:
        actual=sp.simplify(sp.trace(V.inv()*Mat)/2)
        trace_ok &= sp.simplify(actual-(a*cc+b*ss*axis[j]))==0
ck('actual_matrix_trace_matches_quaternion_kernel',trace_ok)
ck('coarse_noncommutativity_control',(VX*VY-VY*VX)!=sp.zeros(2),True)
# SU(2) Haar moments from beta integrals versus the Bessel power series.
ck('Haar_Bessel_coefficients_ten_orders',all(
    sp.simplify(sp.gamma(n+sp.Rational(1,2))/(sp.sqrt(sp.pi)*sp.gamma(n+2))/sp.factorial(2*n)
                -1/(4**n*sp.factorial(n)*sp.factorial(n+1)))==0 for n in range(10)))

mp.mp.dps=65; tol=mp.mpf('1e-45')
u=mp.mpf(5)/4; kappa=mp.mpf(4)/5; t=u*kappa
source=mp.mpc(1,2)/50; cut=mp.mpf(1)/2
xcut=1-cut**2/2; thcut=2*mp.asin(cut/2)
clist=list(distributions)
angles={cl:mp.mpf(0) for cl in clist}; angles[(0,False)]=mp.mpf(1)/5;angles[(1,False)]=mp.mpf(1)/7
axes={cl:0 for cl in clist};axes[(1,False)]=1

def H(q):return 1 if q==0 else 2*mp.besseli(1,q)/q

def sinhc(q):return 1 if q==0 else mp.sinh(q)/q

def angle_kernel(theta,omit_normalizer=False,collapse_axes=False):
    s=mp.mpf(0); h=[mp.mpf(0)]*3; den=mp.mpf(1)
    for cl,cnt in distributions.items():
        a=sum(mp.mpf(n)*mp.cos(k*theta) for k,n in cnt.items())/norm
        b=sum(mp.mpf(n)*mp.sin(k*theta) for k,n in cnt.items())/norm
        ang=angles[cl]; s+=t*a*mp.cos(ang)
        j=0 if collapse_axes else axes[cl];h[j]+=t*b*mp.sin(ang)
        den*=H(t*mp.sqrt(a*a+b*b))
    return mp.exp(s)*sinhc(mp.sqrt(sum(x*x for x in h)))/(1 if omit_normalizer else den)

def wt(theta,eps=0,omit_normalizer=False):
    return 2/mp.pi*mp.sin(theta)**2*mp.exp(-6*u*(1+eps)*(1-mp.cos(theta)))*angle_kernel(theta,omit_normalizer)

# Independent quaternion-scalar coordinate x=Re tr U/2. Chebyshev
# recurrences avoid acos/cos in every original contour factor.
def chebT(n,x):
    if n==0:return mp.mpf(1)
    a,b=mp.mpf(1),x
    for _ in range(1,n):a,b=b,2*x*b-a
    return b

def chebU(n,x):
    if n==0:return mp.mpf(1)
    a,b=mp.mpf(1),2*x
    for _ in range(1,n):a,b=b,2*x*b-a
    return b

def wx(x,eps=0):
    rr=1-x*x; s=mp.mpf(0); vec=[mp.mpf(0)]*3;den=mp.mpf(1)
    for cl,cnt in distributions.items():
        a=sum(mp.mpf(n)*chebT(abs(k),x) for k,n in cnt.items())/norm
        beta=sum(mp.mpf(n)*(1 if k>0 else -1)*chebU(abs(k)-1,x) for k,n in cnt.items() if k)/norm
        ang=angles[cl];s+=t*a*mp.cos(ang);vec[axes[cl]]+=t*beta*mp.sin(ang)
        den*=H(t*mp.sqrt(a*a+rr*beta*beta))
    return 2/mp.pi*mp.sqrt(max(mp.mpf(0),rr))*mp.exp(-6*u*(1+eps)*(1-x))*mp.exp(s)*sinhc(mp.sqrt(max(mp.mpf(0),rr)*sum(v*v for v in vec)))/den

Herrors=[abs(H(q)-2/mp.pi*mp.quad(lambda th:mp.sin(th)**2*mp.exp(q*mp.cos(th)),[0,mp.pi])) for q in [mp.mpf(1)/3,mp.mpf(7)/5]]
ck('actual_kernel_normalizer_Haar_integral',max(Herrors)<tol)
D0=mp.quad(lambda th:wt(th),[0,thcut]);N0=mp.quad(lambda th:wt(th),[thcut,1,2,mp.pi])
De=mp.quad(lambda th:wt(th,source),[0,thcut]);Ne=mp.quad(lambda th:wt(th,source),[thcut,1,2,mp.pi])
Dx=mp.quad(lambda x:wx(x,source),[xcut,1]);Nx=mp.quad(lambda x:wx(x,source),[-1,0,xcut])
whole_x=mp.quad(lambda x:wx(x,source),[-1,0,xcut,1])
ck('actual_cut_Haar_reference_positive',D0>0 and N0>0)
ck('angle_and_quaternion_good_integrals_agree',abs(De-Dx)<tol)
ck('angle_and_quaternion_bad_integrals_agree',abs(Ne-Nx)<tol)
# Integrate the source compensation directly over the cut reference.
returned=mp.quad(lambda th:wt(th)*mp.exp(-6*u*source*(1-mp.cos(th)))*(1+mp.exp(6*u*source*(1-mp.cos(th)))*Ne/D0),[0,thcut])/D0
ck('actual_Haar_slice_compensation_identity',abs(returned-whole_x/D0)<tol)
wrong=mp.quad(lambda th:wt(th,source)*(1+Ne/D0),[0,thcut])/D0
ck('actual_Haar_drop_compensator_control',abs(wrong-whole_x/D0)>mp.mpf('1e-8'),True)
wrongN=mp.quad(lambda th:wt(th,source,True),[thcut,1,2,mp.pi])
ck('actual_Haar_omit_kernel_normalizer_control',abs(wrongN-Ne)>mp.mpf('1e-8'),True)
ck('wrong_nonlinear_cut_boundary_control',abs(mp.quad(lambda th:wt(th,source),[0,cut])-De)>mp.mpf('1e-8'),True)
ck('collapse_noncommuting_coarse_axes_control',abs(angle_kernel(mp.mpf(2)/3,False,True)-angle_kernel(mp.mpf(2)/3))>mp.mpf('1e-8'),True)

# Actual conditional stress: all 8 incident coarse matrices -I, kappa=10.
# Keep every Haar normalizer. This checks the explicit H20b scope guard.
ps={cl:sum(F(n,norm) for k,n in cnt.items() if k) for cl,cnt in distributions.items()}
expected_p={(mu,inc):(F(4,27) if mu==0 and not inc else F(1,9) if mu==0 else F(10,81)) for mu in range(4) for inc in (False,True)}
ck('stress_actual_contour_probabilities',ps==expected_p and sum(ps.values())==1)
r0=F(1,10); epscut=F(1,2); stress_kappa=10
margin=stress_kappa*(2-r0*r0/2-epscut*epscut)-12
ck('stress_exponent_positive_exact',margin==F(109,20))
central_blocks={zero}|{tuple((1 if j==mu else 0) for j in range(4)) for mu in range(4)}
diagonal=(1,1,1,1)
ck('rough_diagonal_collar_is_outside_all_eight_kernel_endpoints',diagonal not in central_blocks and all(abs(x)<=1 for x in diagonal))
cross_edge=((1,3,3,3),0)
rough_corners=[(1,3,3,3),(2,3,3,3),(1,4,3,3),(2,4,3,3)]
central_coarse={(zero,mu) for mu in range(4)}|{(tuple(1 if j==mu else 0 for j in range(4)),mu) for mu in range(4)}
ck('rough_interblock_link_preserves_all_interior_cuts',cross_edge not in interior and len({block_of(x,T) for x in rough_corners})==2)
ck('rough_interblock_link_leaves_central_conditional_density_unchanged',not(readers[cross_edge]&central_coarse))
rough_P=(-eye)*eye*eye*eye
ck('fixed_rough_collar_forces_completion_failure',eye-rough_P==2*eye and F(2)>epscut/4)
stress_u=mp.mpf(20); stress_t=10*stress_u

def stress_log(th):
    val=-6*stress_u*(1-mp.cos(th))
    for cl,cnt in distributions.items():
        aa=sum(mp.mpf(n)*mp.cos(k*th) for k,n in cnt.items())/norm
        bb=sum(mp.mpf(n)*mp.sin(k*th) for k,n in cnt.items())/norm
        val+=-stress_t*aa-mp.log(H(stress_t*mp.sqrt(aa*aa+bb*bb)))
    return val
shift=stress_log(mp.pi)
def stress_w(th):return mp.sin(th)**2*mp.exp(stress_log(th)-shift)
SG=mp.quad(stress_w,[0,thcut]);SB=mp.quad(stress_w,[thcut,1,2,mp.pi])
stress_bad=SB/(SG+SB)
ck('actual_conditional_cut_failure_near_one',stress_bad>mp.mpf('0.99'))
# A successful-return selector cannot be substituted for this failed collar.
ck('dropping_completion_selector_stress_control',SG<SB/100,True)

out={'schema':'source-history-author-su2-v1','scope':'Actual S4 contour geometry and a one-link SU2 Haar slice with every other fine link fixed to I; not the full cube denominator or a weak-coupling proof',
     'checks':checks,'negative_controls':controls,'counts':{'checks':len(checks),'negative_controls':len(controls)},
     'T':T,'L':L,'D':3,'fine_links':len(all_links),'interior_links_per_block':n_l,
     'max_PY_single_cube':max(map(len,plaquette_reads.values())),
     'contour_word_powers':{str(k):dict(v) for k,v in distributions.items()},
     'quadrature':{'decimal_digits':mp.mp.dps,'tolerance':str(tol),'interval_certified':False,
       'u':str(u),'kappa':str(kappa),'source':str(source),'cut':str(cut),'D0':mp.nstr(D0,30),'N0':mp.nstr(N0,30),
       'good_error':mp.nstr(abs(De-Dx),8),'bad_error':mp.nstr(abs(Ne-Nx),8),
       'return_error':mp.nstr(abs(returned-whole_x/D0),8),'drop_compensator_error':mp.nstr(abs(wrong-whole_x/D0),12)},
     'stress':{'scope':'One-link conditional SU2 slice, not the full cube integral or unconditional Wilson measure','u':str(stress_u),'kappa':10,'exact_margin':str(margin),'log10_good_probability':mp.nstr(mp.log10(SG/(SG+SB)),18),'bad_probability_exceeds_0.99':bool(stress_bad>mp.mpf('0.99'))},
     'versions':{'mpmath':mp.__version__,'sympy':sp.__version__},
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'elapsed_seconds':time.monotonic()-started,'all_pass':True}
print(json.dumps(out,indent=2))
