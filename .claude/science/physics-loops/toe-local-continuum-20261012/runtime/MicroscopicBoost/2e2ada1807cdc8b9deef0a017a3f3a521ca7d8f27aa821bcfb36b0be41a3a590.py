"""Compact polynomial test data and transparent quadrature; no boost import."""
import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.legendre import leggauss
from scipy.special import beta, hyp0f1

class Packet:
    def __init__(self,center,radius,coeff,power=6,name='packet'):
        self.center=float(center);self.radius=float(radius)
        self.coeff=np.asarray(coeff,dtype=float);self.power=power;self.name=name
        self.poly=[Polynomial([*row])*Polynomial([1,0,-1])**power for row in coeff]
    def value(self,x,order=0):
        x=np.asarray(x,dtype=float);y=(x-self.center)/self.radius
        inside=np.abs(y)<1
        return np.stack([np.where(inside,p.deriv(order)(y)/self.radius**order,0.) for p in self.poly],axis=-1)
    def integral(self,left,right):
        lo=np.clip((np.asarray(left)-self.center)/self.radius,-1,1)
        hi=np.clip((np.asarray(right)-self.center)/self.radius,-1,1)
        return self.radius*np.stack([p.integ()(hi)-p.integ()(lo) for p in self.poly],axis=-1)
    def quadrature(self,n=96):
        z,w=leggauss(n)
        return self.center+self.radius*z,self.radius*w
    def norms(self,n=96):
        x,w=self.quadrature(n)
        out={}
        for k in range(3):
            val=self.value(x,k)
            out[f'f{k}']=float(np.sqrt(np.sum(w[:,None]*val**2)))
            if k:out[f'xf{k}']=float(np.sqrt(np.sum(w[:,None]*(x[:,None]*val)**2)))
        return out
    def fourier(self,q):
        """Closed Fourier integral; independently checked against x quadrature."""
        q=np.asarray(q);k=q*self.radius;p=self.power
        b=beta(.5,p+1)
        base=b*hyp0f1(p+1.5,-k*k/4)
        deriv=-b*k/(2*p+3)*hyp0f1(p+2.5,-k*k/4)
        ans=np.stack([row[0]*base+1j*row[1]*deriv for row in self.coeff],axis=-1)
        return self.radius*np.exp(-1j*q*self.center)[:,None]*ans/np.sqrt(2*np.pi)

PACKETS=[
    Packet(.17,1.13,[[1.,.2],[-.3,.7]],name='off_grid'),
    Packet(-1.4,.61,[[.2,1.],[-.8,-.1]],name='negative_shift'),
    Packet(8.,.35,[[1.,.3],[.1,-.5]],name='narrow_distant'),
    Packet(200.,20.,[[.7,.1],[.2,-.6]],name='broad_distant'),
]
FLOW_PACKET=Packet(.23,1.05,[[1.,.2],[-.35,.7]],name='flow_compact_C5')

def independent_cells(packet,indices,a,n=48,order=0,boost=False,m=.8,v=1.3):
    """Split integration at packet boundaries; no polynomial antiderivative."""
    z,w=leggauss(n);out=[]
    for site in indices:
        lo=max(a*site,packet.center-packet.radius)
        hi=min(a*(site+1),packet.center+packet.radius)
        if hi<=lo:out.append(np.zeros(2,dtype=complex if boost else float));continue
        x=(lo+hi)/2+(hi-lo)*z/2
        if boost:
            f=packet.value(x);fp=packet.value(x,1)
            vals=1j*np.stack([v*(x*fp[:,1]+f[:,1]/2)+m*x*f[:,1],
                              v*(x*fp[:,0]+f[:,0]/2)-m*x*f[:,0]],axis=-1)
        else: vals=packet.value(x,order)
        out.append((hi-lo)/2*np.sum(w[:,None]*vals,axis=0)/np.sqrt(a))
    return np.asarray(out)
