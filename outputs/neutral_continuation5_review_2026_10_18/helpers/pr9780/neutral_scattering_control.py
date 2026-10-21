import sys,json,mpmath as m
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_mobility_control import solve
m.mp.dps=55

def calc(b,delta,s=1,eta=m.mpf('.05')):
 z=-4*(1+b)+delta*(s+1j*eta)
 den=m.sqrt(z*z-16*(1-b)**2);g=-2*m.ellipk(64*b/den**2)/(m.pi*den)
 def f(x):
  u=m.cos(x);a=z+4*u;root=m.sqrt(a-4*b)*m.sqrt(a+4*b)
  return (u-1)/root,(m.cos(2*x)-1)/root,u*(1-a/root)/(4*b)-1/root
 x0=m.sqrt(delta*max(s,1)/2);cuts=sorted(set([m.mpf(0),x0/2,x0,x0*2,m.mpf('.001'),m.mpf('.1'),m.mpf(1),m.pi]))
 dx,dxx,dxy=[m.quad(lambda x:f(x)[j],cuts)/m.pi for j in range(3)]
 dy=(1-(z+4+4*b)*g-4*dx)/(4*b)
 # recurrence z*gy+4*gxy+2b*(g0+g2y)=0
 dyy=(-z*dy-4*dxy-(z+4+4*b)*g)/(2*b)
 D=m.matrix([dx,dy]);M=m.matrix([[dxx-4*dx,2*dxy-2*dx-2*dy],[2*dxy-2*dx-2*dy,dyy-4*dy]])
 sig=(z+m.sqrt(z*z-16))/2
 A=m.eye(2)/sig-M;G=M-2*D*D.T/g;T=(m.eye(2)/sig-G)**-1
 # x-oriented real incoming momentum at real energy
 k=m.acos(1-s*delta/4);h=m.sqrt(2)*m.matrix([m.cos(k)-1-dx/g,-dy/g])
 t=-1/g+(h.T*T*h)[0]
 q=2*(D.T*(A**-1)*D)[0];red=-1/(g+q)
 c=1/(8*m.pi*m.sqrt(b));target=-1/(c*m.log(-s-1j*eta))
 return dict(b=float(b),delta=float(delta),t=[float(t.real),float(t.imag)],target=[float(target.real),float(target.imag)],relative_error=float(abs(t-target)/abs(target)),rank_reduction_error=float(abs(t-red)))
rows=[]
for bs in ['.1','.15','.18']:
 b=m.mpf(bs);E,L=solve(b);d=m.exp(-L)
 for s in [m.mpf('.25'),m.mpf(1),m.mpf(4)]:
  row=calc(b,d,s);rows.append(row);print(json.dumps(row),flush=True)
assert max(r['relative_error'] for r in rows if r['b']==.18)<2e-5
for sindex in range(3):
 assert rows[sindex]['relative_error']>rows[sindex+3]['relative_error']>rows[sindex+6]['relative_error']
