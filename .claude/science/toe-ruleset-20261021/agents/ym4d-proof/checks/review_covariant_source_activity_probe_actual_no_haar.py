"""Actual SU2 crossing-link conditional fibre; no imports of author/reviewer checkers."""
import itertools, json, math, time
import numpy as np
import mpmath as mp
from collections import Counter
mp.mp.dps = 55
start=time.monotonic(); checks={}; diagnostics={}
def check(name,condition):
    checks[name]=bool(condition)
    if not condition: raise AssertionError(name)
I=np.eye(2,dtype=complex)
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
def group(theta,n): return np.cos(theta)*I+1j*np.sin(theta)*np.einsum('i,ijk->jk',n,pauli)
V=[group(.55,[1,0,0]),group(.11,[0,1,0]),I,I]
Pc=V[0]@V[1]@V[0].conj().T@V[1].conj().T
pvec=np.array([(np.trace(Pc@x)/(2j)).real for x in pauli]); axis=pvec/np.linalg.norm(pvec)
L=3; period=9; origin=(1,1,0,0); edge=(origin,0)
def canonical(x): return tuple(int(t)%period for t in x)
def add(x,mu,n):
    y=list(x);y[mu]+=n;return tuple(y)
def path(x,y,perm):
    z=tuple(x); out=[]
    for mu in perm:
        while z[mu]!=y[mu]:
            sign=1 if z[mu]<y[mu] else -1
            base=z if sign>0 else add(z,mu,-1)
            out.append((canonical(base),mu,sign));z=add(z,mu,sign)
    assert z==tuple(y)
    return out
perms=list(itertools.permutations(range(4)))
def words(X,mu):
    Y=add(X,mu,L)
    for r in itertools.product(range(-1,2),repeat=4):
        x=tuple(X[i]+r[i] for i in range(4)); y=add(x,mu,L)
        for perm in perms:
            left=path(X,x,perm); mid=path(x,y,[mu]); right=path(Y,y,perm)
            yield left+mid+[(p,d,-s) for p,d,s in reversed(right)]
def link(x,mu,a):
    # The centered block interval is [-1,1]; residue 1 is its positive face.
    base=V[mu] if (x[mu]+1)%L==L-1 else I
    if (canonical(x),mu)==edge: return group(a,axis)@base
    return base
def product(word,a):
    z=I.copy()
    for x,mu,s in word:
        w=link(x,mu,a);z=z@(w if s>0 else w.conj().T)
    return z
main=list(words((0,0,0,0),0))
counts=Counter(sum(s for x,mu,s in w if (x,mu)==edge) for w in main)
check('S4_1944_words',len(main)==1944)
check('S4_crossing_weight_72_over_1944',counts==Counter({0:1872,1:72}))
check('S4_lift_exact_V0',max(np.linalg.norm(product(w,0)-V[0]) for w in main)<2e-12)
# Every kernel with either endpoint block in the two blocks of the edge.
blocks=[(0,0,0,0),(3,0,0,0)]; coarse=set()
for X in blocks:
    for mu in range(4): coarse.add((X,mu));coarse.add((add(X,mu,-3),mu))
other_occurrences=0; other_words=0
for X,mu in coarse:
    if X==(0,0,0,0) and mu==0:continue
    for w in words(X,mu):
        other_words+=1;other_occurrences+=sum((x,d)==edge for x,d,s in w)
check('all_other_endpoint_kernels_do_not_read_edge',other_occurrences==0)
for a in [-.13,.07,.21]:
    M=sum((product(w,a) for w in main),start=np.zeros((2,2),complex))/len(main)
    expected=((1-1/27)*I+group(a,axis)/27)@V[0]
    check('actual_mean_'+str(a),np.linalg.norm(M-expected)<2e-12)
def plaquette(x,mu,nu,a):
    return link(x,mu,a)@link(add(x,mu,1),nu,a)@link(add(x,nu,1),mu,a).conj().T@link(x,nu,a).conj().T
q=float(np.trace(Pc).real/2); sn=float(np.linalg.norm(pvec))
for a in [-.13,.07,.21]:
    Ps=[plaquette(x,0,nu,a) for nu in [1,2,3] for x in [origin,add(origin,nu,-1)]]
    actual=sum(1-np.trace(P).real/2 for P in Ps)
    exact=5*(1-np.cos(a))+1-q*np.cos(a)+sn*np.sin(a)
    check('six_actual_plaquettes_'+str(a),abs(actual-exact)<2e-12)
    check('source_actual_curved_plaquette_'+str(a),abs(1-np.trace(Ps[0]).real/2-(1-q*np.cos(a)+sn*np.sin(a)))<2e-12)
check('noncommuting_coarse_holonomies',np.linalg.norm(V[0]@V[1]-V[1]@V[0])>.1)
delta=np.linalg.norm(I-Pc,2)
check('exact_commutator_curvature',abs(delta-2*math.sin(.55)*math.sin(.11))<2e-12)
df=eta=delta/(2*(L*L+4))
check('strong_good_empty_necessary_margin',abs((L*L*df+4*eta)/delta-.5)<2e-12)
# Arbitrarily small coarse curvature with one large coarse link/holonomy.
for d in [1e-3,1e-7,1e-11]:
    beta=math.asin(d/(2*math.sin(.7)))
    X=group(.7,[0,0,1]);Y=group(beta,[1,0,0]);P=X@Y@X.conj().T@Y.conj().T
    check('arbitrarily_small_curvature_'+str(d),abs(np.linalg.norm(I-P,2)/d-1)<2e-5)
check('holonomy_not_a_small_link_assumption',np.linalg.norm(I,2)==1 and np.linalg.norm(I-group(.7,[0,0,1]),2)>.6)
# Full finite-u conditional density, including the one field-dependent normalizer
# and all three colours in the Haar chart density. Other frozen factors cancel.
u=mp.mpf(20);t=mp.mpf('1.3')*u; frac=mp.mpf(1)/27
qmp=1-2*mp.sin(mp.mpf('.55'))**2*mp.sin(mp.mpf('.11'))**2
smp=mp.sqrt(1-qmp*qmp); eps=mp.mpc('.02','.015'); p=mp.mpf('1.25')
def radius(a): return mp.sqrt((1-frac+frac*mp.cos(a))**2+(frac*mp.sin(a))**2)
def z0(z): return 2*mp.besseli(1,z)/z if z else mp.mpf(1)
def logj(a): return 2*mp.log(mp.sin(a)/a) if a else mp.mpf(0)
def source(a): return 1-qmp*mp.cos(a)+smp*mp.sin(a)
def phase(a,e=0):
    return u*(5*(1-mp.cos(a))+source(a)+e*source(a))+mp.log(z0(t*radius(a)))-t*(1-frac+frac*mp.cos(a))
a0=mp.findroot(lambda a:mp.diff(lambda x:phase(x),a),(-mp.mpf('.03'),mp.mpf(0)))
a1=mp.findroot(lambda a:mp.diff(lambda x:phase(x,eps),a),a0)
k0=mp.diff(lambda x:phase(x),a0,2); k1=mp.diff(lambda x:phase(x,eps),a1,2)
c0=1/mp.sqrt(k0); c1=1/mp.sqrt(k1)
check('finite_u_real_critical_point',abs(mp.diff(lambda x:phase(x),a0))<mp.mpf('1e-45') and k0>0)
check('original_complex_source_critical_point',abs(mp.diff(lambda x:phase(x,eps),a1))<mp.mpf('1e-45') and abs(mp.im(a1))>mp.mpf('1e-8'))
for j,a in enumerate([mp.mpf(0),mp.mpf('.11'),a1]):
    z=t*radius(a); direct=2/mp.pi*mp.quad(lambda th:mp.sin(th)**2*mp.exp(z*mp.cos(th)),[0,mp.pi])
    check('normalized_SU2_group_integral_'+str(j),abs(direct/z0(z)-1)<mp.mpf('1e-35'))
haar_axis=1/(4*mp.pi**2)
f=lambda a:mp.exp(-phase(a,eps))
J0=haar_axis*mp.quad(f,[a0-c0*p,a0,a0+c0*p])
base=phase(a0)
M=phase(a0,eps)-base
R=lambda w:phase(a0+c0*w)-base-w*w/2
S=lambda w:u*eps*(source(a0+c0*w)-source(a0))
Zg=mp.quad(lambda w:mp.exp(-w*w/2-R(w)-S(w)),[-p,0,p])
Jfixed=haar_axis*c0*mp.exp(-base-M)*Zg
check('exact_fixed_reference_full_factors',abs(Jfixed/J0-1)<mp.mpf('1e-30'))
# Independent review assertion: direct normalized Haar moment, not phase(z).
review_den=mp.quad(lambda th:mp.sin(th)**2*mp.exp(t*mp.cos(th)),[0,mp.pi])
review_num=mp.quad(lambda th:mp.sin(th)**2*mp.cos(th)*mp.exp(t*mp.cos(th)),[0,mp.pi])
review_expected=u*(5+qmp)+t*frac-t*(review_num/review_den)*frac*(1-frac)+mp.mpf(2)/3
review_actual=mp.diff(lambda a:phase(a),0,2)
review_error=abs(review_actual-review_expected)/max(1,abs(review_expected))
print(json.dumps({'author_prefix_checks':checks,'review_expected_hessian':str(review_expected),'review_actual_hessian':str(review_actual),'review_error':str(review_error)}))
assert review_error<mp.mpf('1e-30'),'actual_density_zero_hessian'
