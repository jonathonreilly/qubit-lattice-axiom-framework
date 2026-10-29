"""Registered finite diagnostics; no predecessor program imported."""
import os,sys,re,time,json,resource,subprocess,itertools
from pathlib import Path
from fractions import Fraction as F
START=time.monotonic(); rows=[]; gates=[]
def gate(stage):
    s=subprocess.check_output(['/usr/bin/memory_pressure','-Q'],text=True)
    g={'stage':stage,'free_percent':int(re.search(r'free percentage:\s*(\d+)%',s).group(1)),
       'load':os.getloadavg(),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'seconds':time.monotonic()-START}
    gates.append(g)
    assert g['free_percent']>=50 and max(g['load'])<20 and g['rss_bytes']<2_000_000_000 and g['seconds']<60,g
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    for x in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:assert os.environ[x]=='1'
def out(x):
    if isinstance(x,(list,tuple)):return [out(y) for y in x]
    if isinstance(x,dict):return {str(k):out(v) for k,v in x.items()}
    if isinstance(x,(str,int,float,bool)) or x is None:return x
    return str(x)
def check(name,condition,value=None,control=False):
    rows.append({'name':name,'pass':bool(condition),'value':out(value),'control':control})
gate('before_import')
import mpmath as mp
mp.mp.dps=65
root=Path(__file__).resolve().parents[6]
lock=json.loads((root/'logs/physics_worker_lock.json').read_text())
# Monomial coefficients of the forest identity, independently integrated by order.
for ns in [(1,1,1),(2,1,3),(4,2,1)]:
    probabilities=[]; wrong=[]
    for k in range(3):
        a,b=[ns[i] for i in range(3) if i!=k];c=ns[k];n=a+b+c
        probabilities.append(F(a*b,n)*(F(1,b+c)+F(1,a+c)))
        wrong.append(F(a*b,n)*(F(1,b)+F(1,a)))
    check('forest_probability_'+str(ns),sum(probabilities)==1,probabilities)
    check('max_bottleneck_rejected_'+str(ns),sum(wrong)!=1,sum(wrong),True)
    check('missing_tree_rejected_'+str(ns),sum(probabilities[:-1])!=1,sum(probabilities[:-1]),True)
phi=lambda z:mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
zp=lambda p:mp.erf(p/mp.sqrt(2))
q=mp.mpc('1.02','.01');t=mp.mpc('.02','.015'); scalar=[]
for p in map(mp.mpf,[2,4,8,12]):
    h=t*p; f=lambda z:mp.exp(-q*z*z/2)/mp.sqrt(2*mp.pi)
    shifted=mp.quad(lambda w:f(w-h),[-p,0,p])
    main=mp.quad(f,[-p,0,p])
    left=mp.quad(f,[-p-h,-p]);right=mp.quad(f,[p,p-h])
    check('scalar_oriented_contours_'+str(p),abs((main+left+right)/shifted-1)<mp.mpf('1e-40'),abs((main+left+right)/shifted-1))
    cutoff=mp.log(shifted/zp(p))+mp.log(q)/2
    detfactor=mp.exp(-mp.log(q)/2+cutoff)*zp(p)
    check('scalar_full_cut_normalization_'+str(p),abs(detfactor/shifted-1)<mp.mpf('1e-40'))
    if p==2:
        check('missing_end_rejected',abs((main+left)/shifted-1)>mp.mpf('1e-8'),abs(right/shifted),True)
        check('wrong_end_rejected',abs((main+left-right)/shifted-1)>mp.mpf('1e-8'),2*abs(right/shifted),True)
    if p==8:
        tilted=mp.quad(lambda w:mp.exp(-q*w*w/2+q*h*w)/mp.sqrt(2*mp.pi),[-p,0,p])
        check('critical_vacuum_identity',abs(mp.exp(q*h*h/2)*shifted/tilted-1)<mp.mpf('1e-40'))
        check('omitted_vacuum_rejected',abs(shifted/tilted-1)>mp.mpf('1e-3'),abs(shifted/tilted-1),True)
    scalar.append({'p':p,'quadratic_cube_sup':abs(q-1)*p*p/2,'cutoff':cutoff,'end_moduli':[abs(left),abs(right)]})
check('growing_sup_decreasing_cutoff',scalar[-1]['quadratic_cube_sup']>scalar[0]['quadratic_cube_sup'] and abs(scalar[-1]['cutoff'])<abs(scalar[0]['cutoff'])/1000,scalar)
gate('after_scalar')
q1=mp.mpc(1,'.02');q2=mp.mpc('.99','.015');e=mp.mpc('.015','-.01');t1=mp.mpc('.012','.008');t2=mp.mpc('-.01','.006')
def inner(q,b,lo,hi):
    return mp.sqrt(mp.pi/(2*q))*mp.exp(b*b/(2*q))*(mp.erf(mp.sqrt(q/2)*(hi+b/q))-mp.erf(mp.sqrt(q/2)*(lo+b/q)))
def matrix_integral(p,lam=0):
    h1,h2=t1*p,t2*p
    return mp.quad(lambda w:mp.exp(-q1*(w-h1)**2/2)*inner(q2+2*lam*(w-h1)**2/p**4,e*(w-h1),-p-h2,p-h2),[-p,0,p])/(2*mp.pi)
mat=[]
for p in map(mp.mpf,[2,4,8]):
    z=matrix_integral(p);cut=mp.log(z/zp(p)**2)+mp.log(q1*q2-e*e)/2
    check('matrix_cutoff_bound_'+str(p),abs(cut)<10*mp.exp(-p*p/8),[cut,10*mp.exp(-p*p/8)])
    mat.append([p,cut])
p=mp.mpf(2)
moment=mp.quad(lambda x:(x*x-1)*phi(x),[-p,0,p])/zp(p)
coeff=-moment*moment;boundary=-4*p*p*phi(p)**2/zp(p)**2
check('mixed_mean_edge_boundary_coefficient',abs(coeff/boundary-1)<mp.mpf('1e-45'),[coeff,boundary])
check('deleted_cutoff_coefficient_rejected',abs(coeff)>mp.mpf('1e-8'),control=True)
edge_support=set(range(9));mean1_support=set(range(-3,1));mean2_support=set(range(8,12))
reader=edge_support|mean1_support|mean2_support
check('full_original_reader',reader==set(range(-3,12)))
check('endpoint_only_reader_rejected',not reader.issubset({0,8}),sorted(reader-{0,8}),True)
# A bounded two-site decoration: recurrence moments versus precision derivatives.
h1,h2=t1*p,t2*p;lo,hi=-p-h2,p-h2
Z=matrix_integral(p)
def moments_inner(b):
    v=[inner(q2,b,lo,hi)];flo=mp.exp(-q2*lo*lo/2-b*lo);fhi=mp.exp(-q2*hi*hi/2-b*hi)
    v.append((-b*v[0]-fhi+flo)/q2)
    for k in range(2,5):v.append(((k-1)*v[k-2]-b*v[k-1]-hi**(k-1)*fhi+lo**(k-1)*flo)/q2)
    return v
mom=[];via=[]
for k in [1,2]:
    m=mp.quad(lambda w:mp.exp(-q1*(w-h1)**2/2)*(w-h1)**(2*k)*moments_inner(e*(w-h1))[2*k]/p**(4*k),[-p,0,p])/(2*mp.pi)
    d=mp.quad(lambda w:mp.exp(-q1*(w-h1)**2/2)*(2*(w-h1)**2/p**4)**k*mp.diff(lambda qq:inner(qq,e*(w-h1),lo,hi),q2,k)/mp.factorial(k),[-p,0,p])/(2*mp.pi)
    mom.append(m/Z);via.append(d/Z)
    check('decoration_coefficient_'+str(k),abs(via[-1]-(-1)**k*mom[-1]/mp.factorial(k))<mp.mpf('1e-40'))
connected2=(mom[1]-mom[0]**2)/2
check('connected_subtraction_rejected',abs(connected2-mom[1]/2)>mp.mpf('1e-8'),[connected2,mom[1]/2],True)
gate('after_matrix_and_decoration')
# Actual reviewed crossing fibre; retain its finite-u normalizer and Haar term.
f=mp.mpf(1)/27;eps=mp.mpc('.02','.01');kap=mp.mpf('1.3');fib=[]
for u in map(mp.mpf,[1000,100000,10000000]):
    p=mp.sqrt(mp.log(u));delta=mp.mpf('.1')*p/mp.sqrt(u);qc=1-delta*delta/2;sc=mp.sqrt(1-qc*qc);tt=kap*u
    def rad(a):return mp.sqrt(1-2*f*(1-f)*(1-mp.cos(a)))
    def logz(z):return mp.log(2*mp.besseli(1,z)/z)
    vac=logz(tt)-tt
    def src(a):return 1-qc*mp.cos(a)+sc*mp.sin(a)
    def lj(a):return 2*mp.log(mp.sinc(a))
    def phase(a,ep=0):
        return u*(5*(1-mp.cos(a))+(1+ep)*src(a))+logz(tt*rad(a))-logz(tt)-tt*f*(mp.cos(a)-1)-lj(a)
    a0=mp.findroot(lambda a:mp.diff(lambda x:phase(x),a),(-delta/4,0))
    a1=mp.findroot(lambda a:mp.diff(lambda x:phase(x,eps),a),a0)
    k0=mp.diff(lambda x:phase(x),a0,2);k1=mp.diff(lambda x:phase(x,eps),a1,2);c0=1/mp.sqrt(k0)
    h=(a1-a0)/c0;Q=k1/k0
    check('actual_stationarity_'+str(u),max(abs(mp.diff(lambda x:phase(x),a0)),abs(mp.diff(lambda x:phase(x,eps),a1)))/u<mp.mpf('1e-40'))
    cn=mp.besseli(2,tt)/mp.besseli(1,tt)
    expected=u*(5+qc)+tt*f-tt*f*(1-f)*cn+mp.mpf(2)/3
    actual0=mp.diff(lambda x:phase(x),0,2)
    check('actual_finite_u_zero_hessian_'+str(u),abs(actual0/expected-1)<mp.mpf('1e-40'))
    check('actual_fixed_source_scaled_shift_'+str(u),abs(h)/p<mp.mpf('.01') and abs(Q-1)<mp.mpf('.02'),[h/p,Q-1])
    z=mp.mpc('.3','.2');R=phase(a1+c0*z,eps)-phase(a1,eps)-Q*z*z/2
    # Distinct evaluation in original fixed white coordinates, retaining critical vacuum.
    w=z+h;lhs=phase(a0+c0*w,eps)-phase(a0,0)
    rhs=phase(a1,eps)-phase(a0,0)+Q*(w-h)**2/2+R
    check('actual_critical_taylor_identity_'+str(u),abs(lhs-rhs)<mp.mpf('1e-40'),abs(lhs-rhs))
    if u==1000:
        check('normalizer_hessian_omission_rejected',abs(tt*f*(1-f)*cn)>mp.mpf('1e-8'),tt*f*(1-f)*cn,True)
        check('Haar_hessian_omission_rejected',mp.mpf(2)/3>mp.mpf('1e-8'),mp.mpf(2)/3,True)
    fib.append({'u':u,'p':p,'delta':delta,'epsilon':eps,'h_over_p':h/p,'Q_minus_I':Q-1,'critical_source_vacuum':phase(a1,eps)-phase(a0,0),'common_kernel_vacuum':vac,'remainder':R})
gate('complete')
result={'passed':sum(x['pass'] for x in rows),'total':len(rows),'controls':sum(x['control'] for x in rows),'failed':[x['name'] for x in rows if not x['pass']],'checks':rows,'scalar':out(scalar),'matrix':out(mat),'actual_fibre':out(fib),'gates':gates,'lock_read_only':lock,'scope':'Finite registered diagnostics; actual fibre uses reviewed contour counts and freezes other coordinates. No uniform-theorem or full-transform certification.'}
print(json.dumps(out(result),indent=2))
assert not result['failed'],result['failed']
