import mpmath as m,json
m.mp.dps=45
S=[(0,0),(1,0),(0,1),(1,1),(0,-1),(1,-1)]
V=m.matrix(6)
for i,j in [(0,2),(0,4),(1,3),(1,5)]:V[i,j]=V[j,i]=2
r=(4-m.pi)/(4-2*m.pi)
def pair(z):return [float(m.re(z)),float(m.im(z))]
def run(st):
 eps=m.mpf(st);z=eps+1j*eps*m.mpf('1e-12');a=4-z;g=2/(m.pi*a)*m.ellipk(16/a**2)
 cut=m.acos(1-eps/2)
 def f(x):
  b=a-2*m.cos(x);d=m.sqrt(b*b-4);root=(b-d)/2
  return (1-m.cos(x)*root)/d
 A11=m.quad(f,[0,cut,2*cut,m.pi])/m.pi
 G10=(a*g-1)/4;G11=g-A11;G20=a*G10-g-2*G11;G12=(a*G11-2*G10)/2
 def green(dx,dy):
  q=tuple(sorted((abs(dx),abs(dy))))
  return {(0,0):g,(0,1):G10,(1,1):G11,(0,2):G20,(1,2):G12}[q]
 G=m.matrix([[green(x-u,y-v) for u,v in S] for x,y in S]);phi=m.matrix([m.exp(1j*cut*(x-m.mpf(1)/2)) for x,y in S]);u=m.lu_solve(m.eye(6)+G*V,phi);src=u[0]+u[1]
 pred=2*r/(8*g*(1+r)-1-4*r/m.pi)
 return dict(eps=float(eps),g=pair(g),source=pair(src),pred=pair(pred),relative_error=float(abs(src/pred-1)),scaled_source=pair(src*m.log(1/eps)),A11=pair(A11))
print(json.dumps(dict(rows=[run(x) for x in ['.001','.00001','.0000001']],limit=float(m.pi*r/(1+r))),indent=2))
