import mpmath as mp,json,time
mp.mp.dps=90

def data(b,L):
 delta=mp.exp(-L);E=-4*(1+b)-delta;den=mp.sqrt(E*E-16*(1-b)**2);g=-2*mp.ellipk(64*b/(den*den))/(mp.pi*den)
 def integrals(x):
  u=mp.cos(x);A=-E-4*u;s=mp.sqrt(A*A-16*b*b)
  return (1-u)/s,(1-mp.cos(2*x))/s,u/(4*b)+(1-u*A/(4*b))/s
 cuts=[0,mp.sqrt(delta),mp.mpf('.001'),mp.mpf('.1'),1,mp.pi];cuts=sorted(set(cuts))
 D=[mp.quad(lambda x:integrals(x)[j],cuts)/mp.pi for j in range(3)];dx,dxx,dxy=D;dy=(1+delta*g-4*dx)/(4*b)
 # recurrence for g02, converted to differences
 dyy=(-E*dy-4*dxy+delta*g)/(2*b)
 G=mp.matrix([[dxx-4*dx-2*dx*dx/g,2*dxy-2*dx-2*dy-2*dx*dy/g],[2*dxy-2*dx-2*dy-2*dx*dy/g,dyy-4*dy-2*dy*dy/g]])
 sigma=(E+mp.sqrt(E*E-16))/2
 M=sigma*G;mu=(M[0,0]+M[1,1]+mp.sqrt((M[0,0]-M[1,1])**2+4*M[0,1]**2))/2
 return mu,G,sigma
def run_roots():
 rows=[];bc=mp.mpf('.23475690092702978')
 for bs in ['.1','.15','.18','.2','.21','.22']:
  b=mp.mpf(bs);guess=mp.mpf('.9531128274')/(bc-b)
  L=mp.findroot(lambda x:data(b,x)[0]-1,(max(1,guess-3),guess+3),tol=mp.mpf('1e-55'),maxsteps=30)
  residual=abs(data(b,L)[0]-1);assert residual<mp.mpf('1e-45')
  rows.append(dict(b=bs,log_inverse_gap=mp.nstr(L,60),gap=mp.nstr(mp.exp(-L),60),scaled_log=mp.nstr((bc-b)*L,40),Birman_residual=mp.nstr(residual,10)))
 return rows
