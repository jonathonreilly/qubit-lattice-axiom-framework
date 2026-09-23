import resource,signal,time,json
from fractions import Fraction as Q
from itertools import product
resource.setrlimit(resource.RLIMIT_CPU,(15,15));signal.alarm(20)
n=0
for p,q,r in product([Q(1,10),Q(1),Q(2),Q(7)],repeat=3):
 # Differentiate numerator/denominator polynomial coefficient arrays using quotient rule.
 arr=[([q**3+4*r**3],[q**3+4*r**3,0,0,1]),([4*r**3,q*q],[4*r**3,q*q,q]),([q*q+r*q+2*r*r,r],[q*q+r*q+2*r*r,r,1])]
 val=[]
 for N,D in arr:
  ev=lambda a:sum(c*p**k for k,c in enumerate(a))
  de=lambda a:sum(k*c*p**(k-1) for k,c in enumerate(a) if k)
  val.append(ev(N)/ev(D));assert (de(N)*ev(D)-ev(N)*de(D))/ev(D)**2<0
 A=p**3+q**3+4*r**3;B=p*q*(p+q)+4*r**3
 assert val[1]-val[0]==p*p*(p-q)*(q*q*(p+q)+4*r**3)/(A*B)
 if p>=q:assert val[0]<=val[1]
 n+=1
for v in [Q(1),Q(11,10),Q(4,3),Q(149,100)]:
 x=(v-1)/v**3;U=v**3;D=v*v/(1-3*x*v*v);F=v**3*(1+3*x*D)
 assert min(U,D,F)>=1
 assert U==(1+x*U)**3 and D==(1+x*U)**2*(1+3*x*D) and F==(1+x*U)**3*(1+3*x*D)
print(json.dumps({'positive_weight_grid':n,'quotient_derivative_signs':3*n,'factorization_checks':n,'positive_fixed_points':4,'all_pass':True}))
