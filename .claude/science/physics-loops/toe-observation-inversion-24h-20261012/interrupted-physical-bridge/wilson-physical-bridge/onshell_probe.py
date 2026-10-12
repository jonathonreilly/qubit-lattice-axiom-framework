import numpy as np
from numpy.polynomial.legendre import leggauss
from itertools import product
import json,time

def nodes(m,n):
    z,w=leggauss(n);u=(z+1)/2;wu=w/2
    nr=max(2*n,48);zr,wr=leggauss(nr)
    # Linear inner ball-sector and logarithmic outer radial scale, both exact cube sectors.
    t1=m*(zr+1)/2;wt1=m*wr/2
    L=np.log(np.pi/m);t2=m*np.exp(L*(zr+1)/2);wt2=t2*L*wr/2
    for t,wt in [(t1,wt1),(t2,wt2)]:
      tt,uu,vv=np.meshgrid(t,u,u,indexing='ij')
      ww=(wt[:,None,None]*wu[None,:,None]*wu[None,None,:]*tt**2).ravel()/(2*np.pi)**3
      base=np.stack([tt.ravel(),(tt*uu).ravel(),(tt*vv).ravel()],axis=1)
      for imax in range(3):
       b=np.roll(base,imax,axis=1)
       for signs in product([-1,1],repeat=3):yield b*np.array(signs),ww

def parts(k,p,m,gauge):
    sp=np.sin(p);cp=np.cos(p);Mp=m+np.sum(1-cp);Ep=np.sqrt(sp@sp+Mp*Mp);npv=np.r_[sp,Mp]/Ep
    q=p-k;sq=np.sin(q);Mq=m+np.sum(2*np.sin(q/2)**2,axis=1);Eq=np.sqrt(np.sum(sq*sq,axis=1)+Mq*Mq)
    nq=np.column_stack([sq,Mq])/Eq[:,None];dot=nq@npv
    hk=2*np.sin(k/2);om=np.sqrt(np.sum(hk*hk,axis=1));kh=hk/om[:,None]
    ca=np.cos(p-k/2);sa=np.sin(p-k/2)
    bp=ca*npv[:3]+sa*npv[3];bq=ca*nq[:,:3]+sa*nq[:,3,None]
    if gauge=='feynman':
      splus=2-4*dot+2*np.sum(bp*bq,axis=1);sminus=4-splus
      sea=np.sum(-npv[:3]*sp+npv[3]*cp)/(4*om)
      coul=0
    else:
      c=np.sum(ca*ca*(1-kh*kh),axis=1)+np.sum(sa*sa,axis=1)-np.sum(sa*kh,axis=1)**2
      bpbq=np.sum(bp*bq,axis=1)-np.sum(bp*kh,axis=1)*np.sum(bq*kh,axis=1)
      splus=c*(1-dot)+2*bpbq;sminus=2*c-splus
      sea=np.sum((1-kh*kh)*(-npv[:3]*sp+npv[3]*cp),axis=1)/(4*om)
      coul=(nq@npv)/(2*om*om)
    den=Ep-Eq-om
    if np.max(den)>=0:raise ValueError('Nonnegative emission denominator; stable-branch probe invalid')
    exchange=(splus/den+sminus/(Ep+Eq+om))/(4*om)
    return sea,coul,exchange,Ep,Mp

def evaluate(m,x,n,gauge):
 p=np.array([m*x,0.,0.]);zero=np.zeros(3);acc=np.zeros(3);rest=np.zeros(3);diff=0.
 for k,w in nodes(m,n):
  a=parts(k,p,m,gauge);b=parts(k,zero,m,gauge)
  for j in range(3):acc[j]+=np.sum(w*a[j]);rest[j]+=np.sum(w*b[j])
  integrand=sum(a[:3])*a[3]-sum(b[:3])*a[4]
  diff+=np.sum(w*integrand)/(p@p)
 return {'m':m,'x':x,'n':n,'gauge':gauge,'on_shell_shift_parts':acc.tolist(),'rest_shift_parts':rest.tolist(),'kinetic_after_rest_calibration':diff}

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=16);ap.add_argument('--mass',type=float,default=.001);ap.add_argument('--x',type=float,default=2);ap.add_argument('--out',required=True);a=ap.parse_args();t=time.time()
 out=[evaluate(a.mass,a.x,a.n,g) for g in ['feynman','coulomb']]
 with open(a.out,'w') as f:json.dump({'results':out,'elapsed':time.time()-t},f,indent=2)
 print(json.dumps({'results':out,'elapsed':time.time()-t}))
