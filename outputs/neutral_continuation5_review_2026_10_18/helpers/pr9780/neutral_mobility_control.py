import mpmath as mp
from neutral_threshold_highprecision import data
mp.mp.dps=65
bc=mp.mpf('.23475690092702978')
def solve(b):
 guess=mp.mpf('.9531128274')/(bc-b)
 L=mp.findroot(lambda x:data(b,x)[0]-1,(max(1,guess-3),guess+3),tol=mp.mpf('1e-38'),maxsteps=30)
 return -4*(1+b)-mp.exp(-L),L
def run_checks():
 rows=[]
 for bs in ['.05','.1','.15','.18','.2']:
  b=mp.mpf(bs);E,L=solve(b);h=mp.mpf('0.00001');Em,_=solve(b-h);Ep,_=solve(b+h);Eb=(Ep-Em)/(2*h);Ebb=(Ep-2*E+Em)/(h*h)
  mu,G,sigma=data(b,L);M=sigma*G;v=mp.matrix([M[0,1],1-M[0,0]]);v/=mp.sqrt((v.T*v)[0]);dh=mp.mpf('0.00001');Gp=data(b,L+dh)[1];Gm=data(b,L-dh)[1];GE=(Gp-Gm)/(2*dh*mp.exp(-L));Delta=mp.sqrt(E*E-16);sigE=(1+E/Delta)/2;den=sigma*sigma*(v.T*(-GE)*v)[0]-sigE;u2=1/den
  Ec=-8/Delta*u2;Exx=-(E-b*Eb-Ec)/4;Eyy=(1-b*b)/4*Ebb-b/4*Eb;Ezz=2/Delta*u2;W=(-v[0]+b*v[1])**2*u2
  row={k:float(x) for k,x in dict(b=b,gap=mp.exp(-L),E=E,curvature_x=Exx,curvature_y=Eyy,curvature_z=Ezz,source_weight_over_lambda2=W,curvature_weight_ratio=Ezz/W).items()};rows.append(row)
 return rows
