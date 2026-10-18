import sys,json,mpmath as m
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from neutral_mobility_control import solve
from neutral_threshold_highprecision import data
m.mp.dps=55
W0=m.mpf('.025744944098352')
def resolvent(b,delta,s,eta):
 z=-4*(1+b)+delta*(s+1j*eta)
 den=m.sqrt(z*z-16*(1-b)**2);g=-2*m.ellipk(64*b/den**2)/(m.pi*den)
 def ff(x):
  u=m.cos(x);a=z+4*u;root=m.sqrt(a-4*b)*m.sqrt(a+4*b)
  return (u-1)/root,(m.cos(2*x)-1)/root,u*(1-a/root)/(4*b)-1/root
 x0=m.sqrt(delta*max(s,1)/2);cuts=sorted(set([m.mpf(0),x0/2,x0,x0*2,m.mpf('.001'),m.mpf('.1'),m.mpf(1),m.pi]))
 dx,dxx,dxy=[m.quad(lambda x:ff(x)[j],cuts)/m.pi for j in range(3)]
 dy=(1-(z+4+4*b)*g-4*dx)/(4*b);dyy=(-z*dy-4*dxy-(z+4+4*b)*g)/(2*b)
 D=m.matrix([dx,dy]);M=m.matrix([[dxx-4*dx,2*dxy-2*dx-2*dy],[2*dxy-2*dx-2*dy,dyy-4*dy]])
 sig=(z+m.sqrt(z*z-16))/2;A=m.eye(2)/sig-M;G=M-2*D*D.T/g;T=(m.eye(2)/sig-G)**-1;f=m.matrix([-1,b])
 R=(G**-1-sig*m.eye(2))**-1
 direct=(f.T*R*f)[0];q=2*(D.T*(A**-1)*D)[0];num=2/sig**2*(f.T*(A**-1)*D)[0]**2
 form=(f.T*(A**-1)*f)[0]/sig**2-(f.T*f)[0]/sig-num/(g+q)
 assert abs(direct-form)<m.mpf('1e-35')*max(1,abs(direct))
 return direct
rows=[]
for bs in ['.1','.15','.18','.2']:
 b=m.mpf(bs);E,L=solve(b);delta=m.exp(-L);mu,G,sig=data(b,L);mat=sig*G;v=m.matrix([mat[0,1],1-mat[0,0]]);v/=m.sqrt((v.T*v)[0]);h=m.mpf('1e-7');GE=(data(b,L+h)[1]-data(b,L-h)[1])/(2*h*delta);se=(1+E/m.sqrt(E*E-16))/2;u2=1/(sig**2*(v.T*(-GE)*v)[0]-se);Z=(-v[0]+b*v[1])**2*u2
 for ss in ['.25','1','4']:
  s=m.mpf(ss);eta=m.mpf('.2');raw=resolvent(b,delta,s,eta);scaled=delta*raw/Z;target=-1/m.log(-s-1j*eta)
  rows.append(dict(b=float(b),s=float(s),gap=float(delta),bound_weight=float(Z),bound_critical_ratio=float(Z/(W0*delta*L**2)),scaled_imag=float(scaled.imag),target_imag=float(target.imag),imag_relative_error=float(abs((scaled.imag-target.imag)/target.imag)),critical_transform=[float((raw/(W0*L**2)).real),float((raw/(W0*L**2)).imag)]));print(json.dumps(rows[-1]),flush=True)
assert max(r['imag_relative_error'] for r in rows if r['b']==.2)<1e-5
for i in range(3):assert rows[3+i]['imag_relative_error']>rows[6+i]['imag_relative_error']>rows[9+i]['imag_relative_error']
