from fractions import Fraction as F
import json,time,resource
start=time.process_time()
# Independent exact tuple enumeration of the bilinear transport commutator.
n=7
wrap=lambda k:(k+3)%7-3
value=F(0)
terms=[]
for beta in [-3,3]:
 for gamma in [-1,1]:
  for delta in [-3,3]:
   if (beta+gamma+delta)%7==0:
    coefficient=-gamma*(wrap(beta+gamma)-wrap(gamma)-beta)
    value+=F(coefficient,8);terms.append([beta,gamma,delta,str(F(coefficient,8))])
assert value==F(7,4)
# Conformal constants reconstructed directly from the ball estimates.
r=F(1,128);R=1+r;d=2-R**5;A=R+R**6/d;L=1+6*R**5/d+5*R**10/d**2
assert F(1,1600)*F(9,8)*A<=r/2
assert F(1,1600)*F(9,8)*L<=F(1,2)
assert 3*(R**4-1)<F(1,8)
# Flat trace-free family: no source implementation imported.
a=F(13,10);lam=F(2,5);b=F(1,100)
for cosine in [F(-1),F(0),F(1),F(2,3)]:
 momenta=[lam+b*cosine,lam-b*cosine,lam]
 grav=a*(sum(x*x for x in momenta)-sum(momenta)**2/2)
 w2=3*a*lam**2-4*a*b*b*cosine**2
 assert grav+w2/2==0 and w2>0
# Homogeneous diagonal H=a/w [sum(g_i p_i)^2 - (sum g_i p_i)^2/2]+w/2.
# Each partial derivative at g_i=c, p_i=lam/c is respectively
# dH/dp_i=-a*lam*c/w and dH/dg_i=-a*lam**2/(c*w).
for c in [F(1,2),F(1),F(3)]:
 gp=[lam]*3
 assert a*(2*gp[0]-sum(gp))*c==-a*lam*c
 assert a*(2*gp[0]-sum(gp))*lam/c==-a*lam**2/c
print(json.dumps({'alias_value':str(value),'alias_terms':terms,'conformal_mapping':str(F(1,1600)*F(9,8)*A),'conformal_lipschitz':str(F(1,1600)*F(9,8)*L),'compatible_and_homogeneous_exact':True,'cpu_seconds':time.process_time()-start,'rss_raw':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},indent=2))
