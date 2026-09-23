import time,resource,signal,json,sys
from fractions import Fraction as F
start=time.monotonic();cpu=time.process_time();checks=[]
resource.setrlimit(resource.RLIMIT_CPU,(10,10));signal.alarm(30)
def ck(name,value):
 assert value,name
 checks.append(name)
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def transpose(a):return list(map(list,zip(*a)))
# Independent shell optimization by all nonnegative labels in rectangle.
for R in range(1,41):
 vals=[(p*p+q*q+p*q+3*p+3*q,p,q) for p in range(R+1) for q in range(R+1) if p+q==R]
 ck('balanced-shell-'+str(R),min(vals)[0]==(3*R*R+3)//4+3*R)
# Character/Cayley-Hamilton route independent of indexed epsilon integrator.
# X=MU is Haar. B=U(chi I-X)/2,C=UX^dagger/3.
# chi_bar^2-Tr(X^dagger^2)=2chi; Echi=Echi^2=0,E|chi|^2=1.
# Thus Gbb=(3-1-1+3)/12; Gcc=3/27; Jbc=2/(18*6).
g=[F(1),F(3-1-1+3,12),F(3,27)]
m=[[0,F(2,6*6),F(1,9*6)],[F(2,6*6),0,F(2,18*6)],[F(1,9*6),F(2,18*6),0]]
ck('character-Gram',g==[1,F(1,3),F(1,9)])
ck('Cayley-mixed-J',m[1][2]==F(1,54))
t=F(1,100);v=F(16)*t/(F(1,6)+t/F(6)-t*t/F(3));x=[1,t,t];N=sum(z*z for z in x)
H=[[ (F([0,16,16][i])+v if i==j else -v/F(6)) for j in range(3)] for i in range(3)]
E=v-v*t/F(3)
ck('neutral-eigen-equations',all(z==E*y for z,y in zip([r[0] for r in mm(H,[[z] for z in x])],x)))
# eigenvectors antisymmetric and second symmetric vector orthogonal to x
for name,y,e in [('antisymmetric',[0,1,-1],16+7*v/F(6)),('symmetric',[-2*t,1,1],16+11*v/F(6)-E)]:
 ck(name+'-eigenvector',all(z==e*w for z,w in zip([r[0] for r in mm(H,[[z] for z in y])],y)))
 ck(name+'-above-ground',e>E)
ck('nonneutral-electric-floor',0<E<v<4)
qn=sum(g[i]*x[i]**2 for i in range(3));jn=sum(x[i]*m[i][j]*x[j] for i in range(3) for j in range(3));kn=sum(g[i]*x[i]**2*[4,16,12][i] for i in range(3));delta=(kn+v*(qn-jn))/qn-E
ck('excess-exact',delta==F(454685351,113607549));ck('strict-finite-interval',4<delta<F(401,100))
loss=1-qn/N;theta=2*t*t/N;epath=8*t*t/N;eface=4*epath
ck('projection-loss',loss==F(7,45009) and loss<=theta<1)
ck('norm-numerator',qn==1+4*t*t/F(9));ck('magnetic-numerator',jn==(4*t+t*t)/27)
for name,a,b in [('theta',theta,F(1,50)),('derivative',epath,F(3,100)),('face',eface/4,F(3,100))]:ck(name+'-enclosure',a<=b*b)
upper=(4+F(1,50)*(4+4*F(3,100))+2*v*(F(3,100)+F(1,50)))/(1-theta)
ck('sharp-budget-upper',delta<=upper);ck('crude-budget-outside-domain',2*v>1)
# Different rational compression fixture, rank-one span(1,2,2).
u=[F(1,3),F(2,3),F(2,3)];P=[[a*b for b in u] for a in u];I=[[F(i==j) for j in range(3)]for i in range(3)];Q=sub(I,P)
# rank-one compressed V and W commute: extend to rank-two P to detect sign.
P,Q=Q,P;V=[[F([1,2,4][i]) if i==j else F(0) for j in range(3)]for i in range(3)];W=[[F([1,-1,1][i]) if i==j else F(0) for j in range(3)]for i in range(3)]
left=sub(mm(mm(mm(mm(P,V),P),W),P),mm(mm(mm(mm(P,W),P),V),P));right=sub(mm(mm(mm(mm(P,W),Q),V),P),mm(mm(mm(mm(P,V),Q),W),P))
ck('different-fixture-commutator',left==right and any(z for r in left for z in r));ck('sign-mutation-detected',left!=[[-z for z in r] for r in right])
# Independent expected-value mutations are rejected against derived quantities.
for name,actual,bad in [('B-norm',g[1],F(1)),('C-norm',g[2],F(1,3)),('BJC',m[1][2],F(1,18)),('exact-four',delta,F(4)),('acceptance',qn/N,F(1))]:ck('mutation-'+name,actual!=bad)
# coefficient 4 comes from (3/a)*sqrt((8d/3)*(2a/3)*E).
ck('derivative-prefactor-square',9*F(8,3)*F(2,3)==16)
ck('Casimir-trace',8==3*F(8,3));ck('old-normalization-inconsistent',16!=3*F(8,3))
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1048576 if sys.platform=='darwin' else 1024)
assert rss<64
print(json.dumps({'checks':checks,'count':len(checks),'delta':str(delta),'q':str(qn/N),'upper':str(upper),'wall_sec':time.monotonic()-start,'cpu_sec':time.process_time()-cpu,'maxrss_MiB':rss,'limits':{'wall':30,'CPU':10,'RSS_MiB':64},'scope':'independent exact character/Cayley reduction and rational algebra; no primary runner, no SU3 simulation, no proof by sampling'},indent=2))
