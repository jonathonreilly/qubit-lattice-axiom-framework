"""Independent compact packet arithmetic and spacetime-coordinate oracle."""
import numpy as np
from numpy.polynomial import Polynomial as Poly
from scipy.special import roots_legendre

def quadrature(n,lo,hi):
    x,w=roots_legendre(n)
    return (lo+hi)/2+(hi-lo)/2*x,(hi-lo)/2*w

class Packet:
    """(1-u^2)^6 times two real affine functions, zero outside |u|<1."""
    def __init__(self,center,radius,coefficients):
        self.center=center;self.radius=radius
        base=(Poly([1,0,-1]))**6
        self.polys=[base*Poly(c) for c in coefficients]
        norm=sum((p*p).integ()(1)-(p*p).integ()(-1) for p in self.polys)*radius
        self.polys=[p/np.sqrt(norm) for p in self.polys]
        self.norm=1.
    def value(self,x):
        u=(np.asarray(x)-self.center)/self.radius
        return np.stack([p(u)*(np.abs(u)<1) for p in self.polys],axis=-1)
    def integral(self,left,right):
        l=np.clip((np.asarray(left)-self.center)/self.radius,-1,1)
        r=np.clip((np.asarray(right)-self.center)/self.radius,-1,1)
        return self.radius*np.stack([p.integ()(r)-p.integ()(l) for p in self.polys],axis=-1)
    def cells(self,indices,a):
        return (self.integral(a*indices,a*(indices+1))/np.sqrt(a)).reshape(-1)
    def fourier(self,q,nodes):
        x,w=quadrature(nodes,self.center-self.radius,self.center+self.radius)
        q=np.asarray(q);flat=q.reshape(-1)
        result=np.exp(-1j*flat[:,None]*x[None,:])@(w[:,None]*self.value(x))/np.sqrt(2*np.pi)
        return result.reshape(q.shape+(2,))

def packets():
    return [Packet(c,r,cs) for c,r,cs in [
        (-.40,.95,[[1,.2],[.25,-.1]]),(.10,.90,[[.15,.1],[1,-.15]]),
        (.55,.85,[[.8,-.2],[-.4,.25]]),(-.15,1.05,[[.4,.15],[.9,.1]]),
        (.30,.90,[[-.3,.2],[1,.1]]),(-.55,.85,[[1,-.1],[.6,.2]])]]

def frame(q,m,v):
    theta=np.arctan2(v*np.asarray(q),m)
    return np.stack([np.exp(.5j*theta),-1j*np.exp(-.5j*theta)],axis=-1)/np.sqrt(2)

def initial_positive(packet,q,m,v,nodes):
    return np.sum(frame(q,m,v).conj()*packet.fourier(q,nodes),axis=-1)

def compose_coordinates(word,v):
    """g=(translation a, boost eta); compose a1+Lambda_eta1 a2."""
    eta=0.;tau=0.;ell=0.
    for kind,p in word:
        if kind=='b':eta+=v*p
        else:
            dt,dx=(-p,0.) if kind=='t' else (0.,p)
            old_eta=eta
            tau+=np.cosh(old_eta)*dt+np.sinh(old_eta)*dx/v
            ell+=v*np.sinh(old_eta)*dt+np.cosh(old_eta)*dx
    return eta,tau,ell

def reference_positive(packet,q,word,m,v,nodes):
    eta,tau,ell=compose_coordinates(word,v)
    q=np.asarray(q);E=np.hypot(m,v*q)
    moved=q*np.cosh(eta)+E*np.sinh(eta)/v
    jac=np.sqrt(np.hypot(m,v*moved)/E)
    return np.exp(-1j*(tau*E+ell*q))*jac*initial_positive(packet,moved,m,v,nodes)

def continuum_cells(positive,q,w,indices,a,m,v):
    # Reality reconstructs the negative band, giving twice the real part.
    phase=np.exp(1j*a*(np.asarray(indices)[:,None]+.5)*q[None,:])
    phase*=np.sinc(a*q[None,:]/(2*np.pi))
    return (2*np.sqrt(a/(2*np.pi))*np.real(phase@((w*positive)[:,None]*frame(q,m,v)))).reshape(-1)

def words():
    return [ [('b',.17),('t',.19),('x',.31)],
             [('t',-.21),('b',-.13),('x',-.27)],
             [('b',-.11),('t',.16),('b',.09),('x',.23)] ]
