"""Dispersion-coordinate construction, with material control switches."""
import numpy as np
JACOBIAN_POWER = .5
CELL_PHASE_SIGN = -1

def w(a,p):return np.sqrt(1-a*a*np.asarray(p)**2/4)
def qa(a,p):return 2*np.arcsin(a*np.asarray(p)/2)/a
def pa(a,q):return 2*np.sin(a*np.asarray(q)/2)/a
def frame(a,q):
    sig=np.sqrt(.25+1/a**2);g=sig/2+.25;j=sig/2-.25
    theta=np.angle(g-j*np.exp(-1j*a*np.asarray(q)))
    if np.ndim(theta):raise ValueError('frame takes scalar q')
    return np.diag([np.exp(-.5j*theta),np.exp(.5j*theta)])
def transfer(b,a,p):
    factor=w(b,p)**(1-JACOBIAN_POWER)*w(a,p)**(-JACOBIAN_POWER)
    return factor*frame(b,qa(b,p)).conj().T@frame(a,qa(a,p))
def delta_density(a,p):
    return a/(2*np.pi)*w(a,p)**(-2*JACOBIAN_POWER)
def aliases(a,q,fhat):
    ell=np.arange(-8,9);freq=q+2*np.pi*ell/a
    return np.sum(np.exp(CELL_PHASE_SIGN*.5j*a*freq)*np.sinc(a*freq/(2*np.pi))*fhat(freq))
def compact_hat(p):
    p=np.asarray(p);return np.sqrt(3003/2048)*np.maximum(1-p*p,0)**3
def geometric_hat(a,p):
    p=np.asarray(p);q=qa(a,p)
    sig=np.sqrt(.25+1/a**2);g=sig/2+.25;j=sig/2-.25
    theta_a=np.angle(g-j*np.exp(-1j*a*q));theta=np.arctan(p)
    return np.exp(.5j*(theta-theta_a))*w(a,p)**(-JACOBIAN_POWER)*np.exp(CELL_PHASE_SIGN*.5j*a*q)*np.sinc(a*q/(2*np.pi))*compact_hat(q)
