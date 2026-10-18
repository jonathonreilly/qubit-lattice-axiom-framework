import mpmath as m,json
m.mp.dps=45
S=[(0,0),(1,0),(0,1),(1,1),(0,-1),(1,-1)];V=m.matrix(6)
for i,j in [(0,2),(0,4),(1,3),(1,5)]:V[i,j]=V[j,i]=2

def green(eps):
 z=eps+1j*eps*m.mpf('1e-12');a=4-z;g=2/(m.pi*a)*m.ellipk(16/a**2);cut=m.acos(1-eps/2)
 def f(x):
  b=a-2*m.cos(x);d=m.sqrt(b*b-4);root=(b-d)/2
  return (1-m.cos(x)*root)/d
 A11=m.quad(f,[0,cut,2*cut,m.pi])/m.pi
 G10=(a*g-1)/4;G11=g-A11;G20=a*G10-g-2*G11;G12=(a*G11-2*G10)/2
 vals={(0,0):g,(0,1):G10,(1,1):G11,(0,2):G20,(1,2):G12}
 G=m.matrix([[vals[tuple(sorted((abs(x-u),abs(y-v))))] for u,v in S] for x,y in S])
 return G,g

def plane(eps,axis=0):
 k=m.acos(1-eps/2)
 return m.matrix([m.exp(1j*k*((x-m.mpf('.5')) if axis==0 else y)) for x,y in S])
def cp(z):return [float(m.re(z)),float(m.im(z))]
def inner(a,b):return (a.transpose_conj()*b)[0]
gc=(m.pi**2-8)/(12*m.pi**2-32*m.pi)
rows=[]
for st in ['.001','.00001','.0000001']:
 ef=m.mpf(st);E=2*ef;G,g=green(ef);pi=plane(E);pf=plane(ef)
 form=inner(pf,V*m.lu_solve(m.eye(6)+G*V,pi));pred=1/(g-gc)
 rows.append(dict(ef=float(ef),incoming_energy=float(E),formfactor=cp(form),asymptotic=cp(pred),relative_error=float(abs(form/pred-1)),scaled=cp(m.log(1/ef)*form)))
# Exact rotated two-channel finite-rank T matrix. Thresholds are shifted to 0,d;
# choose h/d before rotation via theta, keeping the physical threshold gap fixed.
E=m.mpf('.1');d=m.mpf('.03');G0,_=green(E);Ge,_=green(E-d);G=m.matrix(12)
for i in range(6):
 for j in range(6):G[i,j]=G0[i,j];G[i+6,j+6]=Ge[i,j]
pi,pf=plane(E),plane(E-d)
first=inner(pf,V*m.lu_solve(m.eye(6)+Ge*V,pi));conv=[]
for st in ['.03','.01','.003']:
 c=m.mpf(st);th=m.atan(2*c)/2;s,a=m.sin(th),m.cos(th);B=m.matrix([[s*s,s*a],[s*a,a*a]]);W=m.matrix(12)
 for aa in range(2):
  for bb in range(2):
   for i in range(6):
    for j in range(6):W[aa*6+i,bb*6+j]=B[aa,bb]*V[i,j]
 incoming=m.matrix(list(pi)+[0]*6);solution=m.lu_solve(m.eye(12)+G*W,incoming);scattered=W*solution
 exact=inner(pf,m.matrix(list(scattered)[6:]));conv.append(dict(c=float(c),relative_born_error=float(abs(exact/(c*first)-1)),amplitude=cp(exact)))
assert rows[-1]['relative_error']<1e-5
assert conv[-1]['relative_born_error']<1e-4
print(json.dumps(dict(gc=float(gc),scaled_limit=float(4*m.pi),threshold_rows=rows,exact_twochannel_control=conv,scope='Pinned coefficient model, first order in c then threshold; no native emission rate'),indent=2))
