import mpmath as m,itertools,json,hashlib,pathlib
m.mp.dps=70
out=[]
for c in map(m.mpf,['0.03','0.3','1','3','30']):
 K=int(m.ceil(m.sqrt(180/c)));ks=range(-K,K+1);Z=sum(m.exp(-c*k*k) for k in ks);v=sum(k*k*m.exp(-c*k*k) for k in ks)/Z;mu=sum(k**4*m.exp(-c*k*k) for k in ks)/Z
 assert mu<=224*(v+v*v)
 for h in [m.mpf('.1'),m.mpf('.7'),m.pi]:
  # Poisson positive alias sum independently compared with product.
  L=int(m.ceil(m.sqrt(180*c)/m.pi))+3;la=sum(m.exp(-m.pi**2*(k+h/(2*m.pi))**2/c) for k in range(-L,L+1))/sum(m.exp(-m.pi**2*k*k/c) for k in range(-L,L+1))
  prod=m.mpf(1)
  for j in range(1,int(m.ceil(100/c))+1):
   q=m.exp(-c*(2*j-1));prod*=1-4*q/(1+q)**2*m.sin(h/2)**2
  assert abs(m.log(prod)-m.log(la))<m.mpf('1e-55')
  assert -m.log(la)>=2*v*h*h/m.pi**2*(1-m.mpf('1e-55'))
 out.append({'c':str(c),'fourth_ratio':str(mu/(v+v*v))})
# Independent exact modular Gauss enumeration and oriented hopping closure.
for N in [3,4,5]:
 for j in range(4):
  charge=[int(i==j)-int(i==0) for i in range(4)]
  actual={e for e in itertools.product(range(N),repeat=4) if all((e[i]-e[(i-1)%4]-charge[i])%N==0 for i in range(4))}
  expected={tuple((n-int(e<j))%N for e in range(4)) for n in range(N)}
  assert actual==expected and len(actual)==N
  for e in actual:
   nxt=list(e);nxt[j]=(nxt[j]-1)%N;j2=(j+1)%4
   assert all((nxt[i]-nxt[(i-1)%4]-(int(i==j2)-int(i==0)))%N==0 for i in range(4))
# Scalar approximation controls challenge both resolvent endpoints and product bound.
for n in [1,2,7,100]:
 for k in range(1001):
  l=m.mpf(k)/1000;assert abs(l**n-m.exp(-n*(1-l)))<=m.mpf(2)/n
for delta in map(m.mpf,['.1','.001']):
 for l in map(m.mpf,['1e-60','.001','.2','.5','.99','1']):
  x=(1-l)/delta;z=-m.log(l)/delta;assert 0<=1/(1+x)-1/(1+z)<=2*delta
p=pathlib.Path(__file__);print(json.dumps({'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'PASS','checks':['high precision independent Poisson versus Jacobi product and floor','fourth moment bound','exhaustive N3/4/5 charged modular Gauss spaces and hopping','scalar product and logarithmic-resolvent endpoints'],'rows':out},indent=2))
