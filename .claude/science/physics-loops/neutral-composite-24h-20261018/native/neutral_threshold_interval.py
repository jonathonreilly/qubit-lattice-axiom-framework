import mpmath as mp,json
iv=mp.iv;iv.dps=40

def data(b):
 root=iv.sqrt(b);dx=iv.atan2(1,root)/(2*iv.pi);dy=iv.atan2(root,1)/(2*iv.pi*b);dxy=1/(2*iv.pi*root)
 dxx=2*(1+b)*dx-2*b*dxy;dyy=2*(1+b)/b*dy-2/b*dxy
 Gxx=dxx-4*dx;Gyy=dyy-4*dy;Gxy=2*dxy-2*dx-2*dy;E=-4*(1+b);sig=(E+iv.sqrt(E*E-16))/2
 A=sig*Gxx;D=sig*Gyy;B=sig*Gxy;mu=(A+D+iv.sqrt((A-D)**2+4*B**2))/2
 return mu,B/(1-A),[dx,dy,dxy],sig
def run_certificate():
 lo='0.2347569009270';hi='0.2347569009271'
 l=data(iv.mpf(lo))[0];h=data(iv.mpf(hi))[0]
 assert l.a>1 and h.b<1
 mu,r,D,s=data(iv.mpf([lo,hi]));assert r.a>iv.mpf(hi).b
 b=iv.mpf([lo,hi]);dx,dy,dxy=D
 A=s*(2*(1+b)*dx-2*b*dxy-4*dx);B=s*(2*dxy-2*dx-2*dy)
 assert B.a>0 and (1-A).a>0
 return dict(bracket=[lo,hi],lower_mu=str(l),upper_mu=str(h),source_ratio=str(r),source_nonzero=True)
