#!/usr/bin/env python3
"""Independent reviewer controls, fixed before author runner inspection.
Bounded diagnostics, not proofs of infinite-volume or continuum statements.
Runtime cap: 120 seconds. Only writes JSON to stdout.
"""
import itertools, json, math, platform, time
from fractions import Fraction as F
import numpy as np
import scipy
from scipy.special import roots_jacobi, eval_chebyu, iv
from numpy.polynomial.legendre import leggauss

start=time.monotonic()
rows=[]
def check(name, condition, **evidence):
    rows.append(dict(name=name,passed=bool(condition),**evidence))
def mul(q,p):
    a,b,c,d=q; e,f,g,h=p
    return np.array([a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e])
def dag(q): return q*np.array([1,-1,-1,-1])
def product(qs):
    q=np.array([1.,0,0,0])
    for p in qs:q=mul(q,p)
    return q
def unit(rng):
    q=rng.normal(size=4);return q/np.linalg.norm(q)
def small(rng):
    q=np.r_[1.,rng.normal(size=3)*.18];return q/np.linalg.norm(q)
rng=np.random.default_rng(29101450)

# Actual 3^3 spatial torus, independent link fields on two time slices.
n=3; sites=list(itertools.product(range(n),repeat=3))
def shift(x,d):
    y=list(x);y[d]=(y[d]+1)%n;return tuple(y)
U={(x,d):unit(rng) for x in sites for d in range(3)}
V={(x,d):unit(rng) for x in sites for d in range(3)}
h={x:unit(rng) for x in sites}
g={x:unit(rng) for x in sites};j={x:unit(rng) for x in sites}
def psum(A):
    return sum(product([A[x,d],A[shift(x,d),e],dag(A[shift(x,e),d]),dag(A[x,e])])[0]
               for x in sites for d in range(3) for e in range(d+1,3))
def tloops(A,B,H):
    return [product([A[x,d],H[shift(x,d)],dag(B[x,d]),dag(H[x])])[0] for x in sites for d in range(3)]
def projected_integrand(A,B,H):
    return [mul(A[x,d],dag(product([H[x],B[x,d],dag(H[shift(x,d)])])))[0] for x in sites for d in range(3)]
tv=tloops(U,V,h); kv=projected_integrand(U,V,h)
check('temporal_slab_orientation',np.max(np.abs(np.array(tv)-kv))<3e-15,max_error=float(np.max(np.abs(np.array(tv)-kv))),links=len(tv))
beta=.73; ne=len(U); npq=len(sites)*3
logwilson=-beta*(sum(1-x for x in tv)+(2*npq-psum(U)-psum(V))/2)
logkernel=-beta*(npq-psum(U))/2+beta*sum(kv)-beta*(npq-psum(V))/2-beta*ne
check('actual_slab_half_spatial_action',abs(logwilson-logkernel)<1e-12,error=logwilson-logkernel)
check('negative_omit_spatial_factor',abs(logwilson-(beta*sum(kv)-beta*ne))>1.,error=logwilson-(beta*sum(kv)-beta*ne))
Ug={(x,d):product([g[x],U[x,d],dag(g[shift(x,d)])]) for x,d in U}
Vj={(x,d):product([j[x],V[x,d],dag(j[shift(x,d)])]) for x,d in V}
hgj={x:product([g[x],h[x],dag(j[x])]) for x in sites}
check('independent_two_slice_gauge_covariance',np.max(np.abs(np.array(tloops(Ug,Vj,hgj))-tv))<3e-15 and abs(psum(Ug)-psum(U))<1e-12)
check('negative_wrong_temporal_vertex',max(abs(product([U[x,d],h[x],dag(V[x,d]),dag(h[shift(x,d)])])[0]-tv[i]) for i,(x,d) in enumerate(U))>.1)

# Gauge-invariant one spatial square, exact character reduction; coefficients
# are obtained by independent Haar Gauss-Jacobi integration, NOT Bessel formula.
x,wt=roots_jacobi(96,.5,.5);wt=wt/(math.pi/2)
chars=np.array([eval_chebyu(k,x) for k in range(14)])
for beta in [.1,.7,2.,5.]:
    raw=chars@(wt*np.exp(beta*x)); eig=raw/np.arange(1,15)
    K=(chars.T*(eig**4))@chars
    A=np.exp(-beta*(1-x)/2)
    T=(np.sqrt(wt)*A)[:,None]*K*(np.sqrt(wt)*A)[None,:]
    vals,vec=np.linalg.eigh(T);lam=vals[-1];psi=vec[:,-1]/np.sqrt(wt)
    if sum(psi)<0:psi=-psi
    ratio=vals[-2]/lam
    nu=wt*A*psi;nu/=sum(nu)
    P=K*nu[None,:];P/=P.sum(axis=1)[:,None]
    pi=wt*psi**2;pi/=sum(pi)
    check('wilson_square_transfer_beta_'+str(beta),0<ratio<1 and 1-ratio>math.exp(-8*beta) and vals[0]>-1e-10,
          top=float(lam),ratio=float(ratio),minorization=math.exp(-8*beta),min_truncated_eigenvalue=float(vals[0]))
    check('wilson_square_doob_beta_'+str(beta),np.max(np.abs(pi@P-pi))<1e-12 and np.min(P/nu[None,:])>=math.exp(-8*beta)-1e-10,
          stationary_error=float(np.max(np.abs(pi@P-pi))),min_density=float(np.min(P/nu[None,:])))
    if beta==.7:
        wrongK=(chars.T*(raw**4))@chars
        wrongT=(np.sqrt(wt)*A)[:,None]*wrongK*(np.sqrt(wt)*A)[None,:]
        wrongvals=np.linalg.eigvalsh(wrongT)
        check('negative_character_dimension_divisor',abs(wrongvals[-2]/wrongvals[-1]-ratio)>1e-4)
        wrongK2=(chars.T*(eig**1))@chars
        check('negative_one_temporal_link_for_square',np.max(np.abs(wrongK2-K))>.1)
        wrong=(A[:,None]*K*A[None,:])@wt/lam
        check('negative_constant_vacuum',np.max(np.abs(wrong-1))>.1,maximum_row_error=float(np.max(np.abs(wrong-1))))
# beta=0 exactly rank one in analytic character coefficients.
check('haar_endpoint_rank_one',np.max(np.abs(chars@wt-np.r_[1.,np.zeros(13)]))<2e-13)
neg=chars@(wt*np.exp(-.7*x))
check('negative_beta_positivity_excluded',neg[1]<0,fundamental_character_coefficient=float(neg[1]))

# Haar integration using Hopf coordinates: t~U[0,1], independent circles.
u,uw=leggauss(24);u=(u+1)/2;uw/=2
ph=2*math.pi*np.arange(40)/40
q=[];qw=[]
for t,w in zip(u,uw):
    for p in ph:
        for s in ph:q.append([math.sqrt(t)*math.cos(p),math.sqrt(t)*math.sin(p),math.sqrt(1-t)*math.cos(s),math.sqrt(1-t)*math.sin(s)]);qw.append(w/1600)
q=np.array(q);qw=np.array(qw)
means=[np.zeros(4),np.array([.2,-.3,.4,.1]),np.array([0.,0.,0.,1.])]
for m in means:
    r=float(np.linalg.norm(m))
    for lam in [0.,.35,2.6,.4+.3j]:
        un=qw*np.exp(lam*(q@m));norm=sum(un);avg=(un@q)/norm
        b=iv(2,lam*r)/iv(1,lam*r) if lam*r!=0 else 0
        target=b*m/r if r else np.zeros(4)
        check('hopf_mean_'+str(m.tolist())+'_'+str(lam),np.max(np.abs(avg-target))<2e-13,max_error=float(np.max(np.abs(avg-target))))
        if r and lam==.4+.3j:
            negavg=(un@(q*np.array([1,-1,-1,-1])))/norm
            analytic=b*dag(m)/r
            check('complex_negative_orientation',np.max(np.abs(negavg-analytic))<2e-13)
            check('negative_conjugate_lambda',np.max(np.abs(negavg-np.conjugate(target)*np.array([1,-1,-1,-1])))>.05)
        if 0<r<1 and lam==2.6:
            wrong=b*dag(m)/(r**3)
            check('negative_nonunit_mean_inverse',np.max(np.abs((un@(q*np.array([1,-1,-1,-1])))/norm-wrong))>.1)
check('repeated_link_haar_second_moment',abs(sum(qw*q[:,0]**2)-.25)<2e-14)
check('negative_normalizer_omission',abs((qw*np.exp(2.6*q[:,0]))@q[:,0]-iv(2,2.6)/iv(1,2.6))>.2)

# Exact rational sphere moments by integration recurrence E x^(2n)=(2n-1)/(2n+2) E x^(2n-2).
mom=[F(1)]
for k in range(1,7):mom.append(mom[-1]*F(2*k-1,2*k+2))
z={2*k:mom[k]/math.factorial(2*k) for k in range(7)}
a={j:(j+1)*z.get(j+1,F(0)) for j in range(12)};b={}
for j in range(11):b[j]=a[j]-sum(z[k]*b.get(j-k,F(0)) for k in z if 0<k<=j)
check('sphere_integral_normalized_series',b[1]==F(1,4) and b[3]==F(-1,96) and b[5]==F(1,1536),coefficients=[str(b[j]) for j in [1,3,5]])

# Actual paired S4' paths, L=3 in d=4. Lazy fine fields on 12^4 torus.
L=3;ns=12;d=4;fields={};orders=list(itertools.permutations(range(d)))
def forward(v,mu):
    v=list(v);v[mu]=(v[mu]+1)%ns;return tuple(v)
def move_path(a,b,order):
    out=[];a=list(a)
    for mu in order:
        while a[mu]!=b[mu]:
            delta=b[mu]-a[mu]
            # Axial paths only within a block, so there is no ambiguity.
            if delta>0:out.append((tuple(a),mu,1));a[mu]+=1
            else:a[mu]-=1;out.append((tuple(a),mu,-1))
    return out

def contour(X,mu,y,order):
    root=tuple(L*x+1 for x in X);rootY=list(root);rootY[mu]+=L
    dest=list(y);dest[mu]+=L
    p=move_path(root,y,order);s=list(y)
    for k in range(L):p.append((tuple(s),mu,1));s[mu]+=1
    tail=move_path(tuple(rootY),tuple(dest),order)
    return p+[(v,e,-o) for v,e,o in tail[::-1]]
def fine(v,e):
    key=(tuple(t%ns for t in v),e)
    if key not in fields:fields[key]=small(rng)
    return fields[key]
def path_value(path,getter):return product([getter(v,e) if o==1 else dag(getter(v,e)) for v,e,o in path])
def mean_link(X,mu,getter):
    val=np.zeros(4)
    for local in itertools.product(range(L),repeat=d):
        y=tuple(L*x+t for x,t in zip(X,local))
        for order in orders:val+=path_value(contour(X,mu,y,order),getter)
    return val/(len(orders)*L**d)
X=(0,0,0,0);Y=(0,0,0,2)
def loop_edges(X):
    a=list(X);a[0]+=1;b=list(X);b[1]+=1
    return [(X,0,1),(tuple(a),1,1),(tuple(b),0,-1),(X,1,-1)]
edges=loop_edges(X)+loop_edges(Y);Ms=[mean_link(v,e,fine) for v,e,o in edges]
check('actual_s4_path_mean_domain',all(np.linalg.norm(m)<=1+1e-14 for m in Ms),radii=[float(np.linalg.norm(m)) for m in Ms],fine_links_read=len(fields),contours_per_edge=len(orders)*L**d)
# Degree-four coefficient by 4096 complete finite sums. +/- quaternion basis
# is a degree-two Haar cubature, exactly sufficient for the lambda^4 term.
basis=np.r_[np.eye(4),-np.eye(4)]
def coeff4(ms,orient):
    total=0.
    for ind in itertools.product(range(8),repeat=4):
        vs=[basis[i] for i in ind]
        trace=product([v if o==1 else dag(v) for v,o in zip(vs,orient)])[0]
        total+=trace*math.prod(float(v@m) for v,m in zip(vs,ms))
    return total/8**4
cf=[]
for k in [0,4]:
    orient=[o for _,_,o in edges[k:k+4]];ms=Ms[k:k+4]
    got=coeff4(ms,orient);expect=product([m if o==1 else dag(m) for m,o in zip(ms,orient)])[0]/4**4
    cf.append(got)
    check('actual_s4_haar_tensor_coefficient_'+str(k),abs(got-expect)<2e-17,coefficient=got)
    inv=product([m if o==1 else dag(m)/(m@m) for m,o in zip(ms,orient)])[0]/4**4
    check('negative_inverse_in_loop_'+str(k),abs(inv-got)>1e-4)
check('degree_eight_tensor_scale',abs((4**4)**-2-4**-8)==0,coefficient_product=cf[0]*cf[1],scope='Pointwise conditional tensor identity; no sampling claim about the Wilson covariance.')
# A noncentral coarse background lifted to all fine block faces.
coarse={}
def coarse_get(X,e):
    key=(tuple(t%4 for t in X),e)
    if key not in coarse:coarse[key]=unit(rng)
    return coarse[key]
def lift(v,e):
    if v[e]%L==L-1:return coarse_get(tuple(t//L for t in v),e)
    return np.array([1.,0,0,0])
for v,e,o in edges[:2]:
    m=mean_link(v,e,lift);target=coarse_get(v,e)
    check('actual_s4_noncentral_face_lift_'+str(e),np.max(np.abs(m-target))<6e-14,max_error=float(np.max(np.abs(m-target))))

# Actual one-plaquette Wilson fine measure after tree gauge: SU(2) Haar
# class density exp(beta x), tested independently via the Hopf rule.
beta=1.4;x0=q[:,0];p=qw*np.exp(beta*x0);Z=sum(p);p/=Z
Fv=x0;Gv=x0**2;cov=float(p@(Fv*Gv)-(p@Fv)*(p@Gv))
def logsource(t,s):return math.log(float(qw@np.exp(beta*x0+t*Fv+s*Gv)))
eps=1e-3
fd=(logsource(eps,eps)-logsource(eps,-eps)-logsource(-eps,eps)+logsource(-eps,-eps))/(4*eps**2)
check('haar_coarse_source_log_retains_actual_wilson_covariance',abs(fd-cov)<2e-8 and abs(cov)>1e-3,covariance=cov,mixed_source_finite_difference=fd)
check('negative_drop_source_only_log',abs(cov)>1e-3,incorrect_value=0.)
# Total covariance at positive noise via fully normalized joint quadrature.
# Coarse scalar class variable z follows exp(lambda*z*x) (finite model only).
x1,w1=roots_jacobi(40,.5,.5);w1/=math.pi/2
fine=w1*np.exp(beta*x1);fine/=sum(fine)
noise=np.exp(1.8*np.outer(x1,x1))*w1[None,:];noise/=noise.sum(axis=1)[:,None]
joint=fine[:,None]*noise;coarsep=joint.sum(axis=0);reverse=joint/coarsep[None,:]
f=x1;g=x1**2;ef=f@reverse;eg=g@reverse
term1=float(coarsep@(ef*eg)-(coarsep@ef)*(coarsep@eg));term2=float(coarsep@((f*g)@reverse-ef*eg));total=float(fine@(f*g)-(fine@f)*(fine@g))
check('total_covariance_normalized_joint',abs(term1+term2-total)<3e-15,coarse_term=term1,conditional_term=term2,total=total,scope='Finite normalized scalar conditional control; not an S4 RG theorem.')
check('negative_discard_conditional_covariance',abs(term2)>.01)
print(json.dumps({'reviewer_control':'Independent constructions before inspecting author runner','runtime':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'elapsed_seconds':time.monotonic()-start,'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows),'checks':rows},indent=2))
raise SystemExit(any(not x['passed'] for x in rows))
