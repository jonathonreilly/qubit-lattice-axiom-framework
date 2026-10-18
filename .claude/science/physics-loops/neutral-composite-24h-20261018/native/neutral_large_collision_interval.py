import mpmath as mp,json
iv=mp.iv;iv.dps=40
from neutral_threshold_interval import run_certificate
run_certificate()
b=iv.mpf(['.2347569009270','.2347569009271']);one=iv.mpf(1);two=iv.mpf(2);rt2=iv.sqrt(two);E=-4*(1+b);sig=(E+iv.sqrt(E*E-16))/2
Dx=iv.atan2(1,iv.sqrt(b))/(2*iv.pi);Dy=iv.atan2(iv.sqrt(b),1)/(2*iv.pi*b);Dxy=1/(2*iv.pi*iv.sqrt(b));Dxx=2*(1+b)*Dx-2*b*Dxy;Gxx=Dxx-4*Dx;Gxy=2*Dxy-2*Dx-2*Dy
ratio=sig*Gxy/(1-sig*Gxx);vy=1/iv.sqrt(1+ratio**2);vx=ratio*vy
A=-rt2*sig*(vx*Dx+vy*Dy);assert (vy/b).a>vx.b
M=-sig/(2*rt2)*vy/b
s=iv.sqrt(1-b*b);c=1+b-s;t=iv.sqrt(1-c*c)
hp=sig/(2*rt2)*(vx*(1-c)+vy)/(1-c+b)
h0=sig/(2*rt2)*vy/b;h2=sig/(2*rt2)*(vx*(1-c*c)+vy)/(1-c*c+b)
j=iv.mpc(0,1);signs=[1,-1,1,-1];total=iv.mpc(0)
for axis in [0,1]:
 for direction in [-1,1]:
  fd=vx/rt2 if axis==0 else vy/rt2*(b+j*direction*s)
  phases=[c-j*direction*sg*t if axis==0 else s+j*direction*b for sg in signs]
  for ia in range(4):
   for ib in range(4):
    if ia==ib:continue
    ic,ie=[k for k in range(4) if k not in [ia,ib]]
    hsum=h0 if signs[ic]+signs[ie]==0 else h2
    total+=4*phases[ib]*((hp-fd*phases[ic])*(hp-fd*phases[ie])-2*A*hsum+fd**2*phases[ic]*phases[ie])
C=total.real;lower=C-96*(1+b)*M*A
assert float(lower.a)>2.58
print(json.dumps({k:str(v) for k,v in dict(b=b,vx=vx,vy=vy,A=A,M=M,C=C,lower=lower,imaginary=total.imag).items()},indent=2))
