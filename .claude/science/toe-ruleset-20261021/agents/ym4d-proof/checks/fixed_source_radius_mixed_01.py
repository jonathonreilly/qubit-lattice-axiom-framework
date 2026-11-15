import os,sys,re,time,json,resource,subprocess,math,itertools
from pathlib import Path
START=time.monotonic();gates=[];rows=[]
def gate(label):
    s=subprocess.check_output(['/usr/bin/memory_pressure','-Q'],text=True)
    q={'stage':label,'free_percent':int(re.search(r'free percentage:\s*(\d+)%',s).group(1)),'load':os.getloadavg(),'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'seconds':time.monotonic()-START};gates.append(q)
    assert q['free_percent']>=50 and max(q['load'])<20 and q['rss_bytes']<2_000_000_000 and q['seconds']<60,q
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    for n in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:assert os.environ[n]=='1'
def ck(n,b,v=None,control=False):rows.append({'name':n,'pass':bool(b),'value':str(v),'control':control})
gate('before_import')
import sympy as s
import mpmath as mp
mp.mp.dps=65
root=Path(__file__).resolve().parents[6];lock=json.loads((root/'logs/physics_worker_lock.json').read_text())
x=s.symbols('x0:3');poly=0;dist=[]
for k in range(7):
    for l0 in range(k+1):
        for l1 in range(k-l0+1):
            ls=(l0,l1,k-l0-l1)
            multin=s.factorial(k)/s.prod(s.factorial(t) for t in ls)
            moments=s.prod(s.factorial(t+(i==0)) for i,t in enumerate(ls))
            coeff=multin*moments/s.factorial(k)
            dist.append(coeff==l0+1)
            poly+=coeff*s.prod(x[i]**ls[i] for i in range(3))
ck('all_coordinate_child_cancellations',all(dist),len(dist))
t=s.symbols('t');gen=1/((1-t*x[0])**2*(1-t*x[1])*(1-t*x[2]))
expected=s.expand(s.series(gen,t,0,7).removeO().subs(t,1))
ck('object_generating_function',s.expand(expected-poly)==0)
ck('missing_incoming_leg_rejected',poly.coeff(x[0],1).subs({x[1]:0,x[2]:0})!=1,control=True)
lam,e,p,m2,m4=s.symbols('lam e p m2 m4');xx=s.symbols('w1:4')
a=-lam*xx[0]**2*xx[1]**2/p**4;v=-e*xx[1]*xx[2]
def avg(poly):
    result=0
    for powers,c in s.Poly(s.expand(poly),*xx).terms():
        if any(n%2 for n in powers):continue
        if any(n>4 for n in powers):continue
        result+=c*s.prod({0:1,2:m2,4:m4}[n] for n in powers)
    return s.expand(result)
Z=avg(sum((a+v)**k/s.factorial(k) for k in range(4)))
def coeff_log(z):return s.expand(sum((-1)**(k+1)*(z-1)**k/k for k in range(1,4))).coeff(lam,1).coeff(e,2)
direct=s.factor(coeff_log(Z));want=-m2**2*(m4-m2**2)/(2*p**4)
A=avg(a);G=avg(v*v/2);attached=avg(a*v*v/2)
forest=s.expand(attached-A*G).coeff(lam,1).coeff(e,2)
ck('direct_mixed_log',s.simplify(direct-want)==0,direct)
ck('object_forest_mixed_log',s.simplify(forest-want)==0,forest)
ck('wrong_compatibility_rejected',s.simplify(coeff_log(Z+A*G)-want)!=0,coeff_log(Z+A*G),True)
ck('missing_attachment_rejected',s.simplify(coeff_log(1+A+G)-want)!=0,coeff_log(1+A+G),True)
pp=mp.mpf(2);zp=mp.erf(pp/mp.sqrt(2));phi=lambda w:mp.exp(-w*w/2)/mp.sqrt(2*mp.pi)
mu2=mp.quad(lambda w:w*w*phi(w),[-pp,0,pp])/zp;mu4=mp.quad(lambda w:w**4*phi(w),[-pp,0,pp])/zp
num=s.lambdify((m2,m4,p),direct,'mpmath')(mu2,mu4,pp)
form=-mu2**2*(mu4-mu2**2)/(2*pp**4)
# Integrate the finite series' connected coefficient, factored into independent 1D moments.
integrated=(-mp.quad(lambda w:w*w*phi(w),[-pp,0,pp])**2*mp.quad(lambda w:w**4*phi(w),[-pp,0,pp])/zp**3+mu2**4)/(2*pp**4)
ck('actual_truncated_gaussian_mixed_coefficient',num<0 and abs(num)>mp.mpf('1e-8') and abs(num-form)<mp.mpf('1e-45') and abs(num-integrated)<mp.mpf('1e-45'),num)
gate('complete')
r={'passed':sum(x['pass'] for x in rows),'total':len(rows),'controls':sum(x['control'] for x in rows),'failed':[x['name'] for x in rows if not x['pass']],'checks':rows,'gates':gates,'lock_read_only':lock,'scope':'Post-first-run, preregistered exact mixed-object algebra. Not a uniform theorem certification.'}
print(json.dumps(r,indent=2));assert not r['failed'],r['failed']
