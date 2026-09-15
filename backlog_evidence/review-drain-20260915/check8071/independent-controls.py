from pathlib import Path
import sympy as s,itertools,json,time
start=time.monotonic();out=[]
def ck(name,yes):
 assert yes,name
 out.append(name)
Q=s.Rational;n=6
def skew(offset):
 z=s.zeros(n)
 for i in range(n):
  for j in range(i+1,n):z[i,j]=Q(((i*3+j*2+offset)%7)-3,40);z[j,i]=-z[i,j]
 return z
za,zc=skew(1),skew(3)
def pf(z,idx):
 if not idx:return s.Integer(1)
 return sum((-1)**(k+1)*z[idx[0],idx[k]]*pf(z,idx[1:k]+idx[k+1:]) for k in range(1,len(idx)))
def state(z):return {sum(1<<i for i in ii):pf(z,list(ii)) for k in range(0,n+1,2) for ii in itertools.combinations(range(n),k)}
va,vc=state(za),state(zc);dot=lambda a,b:sum(x*b.get(i,0) for i,x in a.items());ov=dot(va,vc)
ck('six-mode Pfaffian overlap determinant',ov>0 and ov**2==(s.eye(n)-za*zc).det())
def act(v,j,create):
 return {i^(1<<j):(-1)**((i&((1<<j)-1)).bit_count())*x for i,x in v.items() if bool(i&(1<<j))!=create}
A=(s.eye(n)-zc*za).inv();F=-A*zc;B=za*A;C=-za*A*zc
for cr1,cr2,mat in [(False,False,F),(False,True,A),(True,False,C),(True,True,B)]:ck('six-mode ordered block '+str((cr1,cr2)),all(dot(va,act(act(vc,j,cr2),i,cr1))==ov*mat[i,j] for i in range(n) for j in range(n)))
ck('transpose CAR contacts',A+C.T==s.eye(n) and F.T==-F and B.T==-B)
r=Q(99,100);q=r*r;ck('fixed degree constants',((1+r)/(1-r),3*((1+r)/(1-r))**2)==(199,118803));ck('2048-term tail strict',q**2048/(1-q)<Q(1,10**15))
E=s.Matrix([[Q(1,5),Q(2,9)],[0,Q(-1,7)]]);M=s.eye(2)-E;S=sum((E**i for i in range(7)),s.zeros(2));ck('nonnormal fresh residual exact',s.eye(2)-M*S==E**7 and M.inv()-S==M.inv()*E**7)
# An odd row permutation must be restored in determinant reconstruction.
P=s.Matrix([[0,1],[1,0]]);BB=P*M;ck('permutation sign cannot be dropped',BB.det()==-M.det() and M.det()>0)
z=Q(1,5);lo=2*sum(z**(2*j+1)/s.Integer(2*j+1) for j in range(12));tail=2*z**25/(25*(1-z*z));ck('scalar log enclosure independent high precision',bool(s.N(s.log(Q(3,2))-lo,60)>0) and bool(s.N(lo+tail-s.log(Q(3,2)),60)>0))
# The Riccati parent disk margin is independent of stationary spectral gaps.
ck('parent disk strict margin',2*r-99*(1-r*r)==Q(99,10000))
a={'pass_count':len(out),'controls':out,'elapsed_seconds':time.monotonic()-start,'scope':'Different six-mode Pfaffian coefficients and rational nonnormal residual/sign controls; no primary/helper or native physical execution.'};p=Path(__file__).with_name('independent-controls-result.json');assert not p.exists();p.write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a,indent=2))
