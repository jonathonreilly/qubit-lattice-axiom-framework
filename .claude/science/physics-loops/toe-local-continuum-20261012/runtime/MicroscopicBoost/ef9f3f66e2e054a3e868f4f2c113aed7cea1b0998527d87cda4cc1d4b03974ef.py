"""Literal finite-open flow versus an independent tilted-Cauchy integral."""
import hashlib
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.sparse.linalg import expm_multiply
from fixtures import FLOW_PACKET as packet
from reporting import arguments,Book

class TiltedSolution:
    def __init__(self,m,v,Q,nq,nx):
        z,w=leggauss(nq);self.q=Q*z;self.weights=Q*w/np.sqrt(2*np.pi)
        self.m=m;self.v=v;self.nx=nx
        self.E=np.sqrt(m*m+v*v*self.q*self.q)
        fh=packet.fourier(self.q)
        dh=np.stack([(-v*self.q+1j*m)*fh[:,1],(-v*self.q-1j*m)*fh[:,0]],axis=1)
        self.bands=[(fh+dh/self.E[:,None])/2,(fh-dh/self.E[:,None])/2]
    def terms(self,s):
        eta=self.v*s;ch=np.cosh(eta);sh=np.sinh(eta)
        # Z(s)=U_(-vs): the outside spin matrix is exp(+eta sigma_x/2).
        spin=np.array([[np.cosh(eta/2),np.sinh(eta/2)],
                       [np.sinh(eta/2),np.cosh(eta/2)]])
        return [(self.q*ch-sign*self.E/self.v*sh,band@spin.T)
                for sign,band in zip([1,-1],self.bands)]
    def value(self,x,s,order=0):
        out=np.zeros((len(x),2),complex)
        for k,amplitude in self.terms(s):
            weighted=(self.weights*(1j*k)**order)[:,None]*amplitude
            out+=np.exp(1j*np.outer(x,k))@weighted
        return out
    def cells(self,indices,a,s):
        out=np.zeros((len(indices),2),complex);centers=a*(indices+.5)
        for k,amplitude in self.terms(s):
            weighted=(self.weights*np.sinc(a*k/(2*np.pi)))[:,None]*amplitude
            out+=np.sqrt(a)*(np.exp(1j*np.outer(centers,k))@weighted)
        return out
    def norms(self,s):
        radius=(abs(packet.center)+packet.radius)*np.exp(abs(self.v*s))
        z,w=leggauss(self.nx);x=radius*z;w=radius*w
        out={}
        for p in range(3):
            val=self.value(x,s,p)
            out[f'f{p}']=float(np.sqrt(np.sum(w[:,None]*np.abs(val)**2)))
            if p:out[f'xf{p}']=float(np.sqrt(np.sum(w[:,None]*np.abs(x[:,None]*val)**2)))
        return out

def extras(p):p.add_argument('--resolution',choices=['coarse','fine'],default='coarse')

def main():
    args,c=arguments(extras);book=Book('whole_boost_flow',args)
    m=.8;v=1.3
    settings={'coarse':(40.,1024,320,6.),'fine':(96.,2816,640,10.)}
    Q,nq,nx,box=settings[args.resolution]
    continuum=TiltedSolution(m,v,Q,nq,nx)
    norms0=packet.norms();norm0=norms0['f0']
    # Check the closed initial Fourier formula with direct physical quadrature.
    qcheck=np.array([-47.,-8.4,-.03,0.,.03,2.7,39.])
    x,w=packet.quadrature(256)
    numerical=np.exp(-1j*np.outer(qcheck,x))@(w[:,None]*packet.value(x))/np.sqrt(2*np.pi)
    book.check('initial_Fourier_integral',np.linalg.norm(numerical-packet.fourier(qcheck)),2e-12)
    stored={}
    for s in [-.27,.27]:
        norms_end=continuum.norms(s)
        book.check('continuum_flux_norm',abs(norms_end['f0']-norm0),2e-7,s=s)
        outside=np.array([-3.,-2.4,2.4,3.])
        vals=continuum.value(outside,s)
        book.check('continuum_outside_support',np.linalg.norm(vals),2e-7,s=s)
        probe=continuum.value(np.linspace(-2,2,97),s)
        book.check('continuum_reality',np.linalg.norm(probe.imag),2e-11,s=s)
        # Independent weighted physical derivative norms on the entire compact orbit.
        zt,wt=leggauss(10)
        times=np.sign(s)*abs(s)*(zt+1)/2
        orbit=[continuum.norms(t) for t in times]
        for a in [.4,.2,.1,.05,.025]:
            L=int(np.floor(-box/a));R=int(np.ceil(box/a))
            indices=np.arange(L,R+1)
            J=(np.sqrt(m*m+4*v*v/a**2)-m)/4;g=J+m/2
            B=c.boost_matrix(indices,a,g,J,finite_open=True)
            initial=c.cell_average(packet,indices,a).ravel()
            evolved=expm_multiply(c.BOOST_SIGN*1j*s*B,initial,traceA=0.)
            comparison=continuum.cells(indices,a,s).ravel()
            # Cell step embedding has unit norm; continuum Z preserves ||f||.
            error2=float(np.vdot(evolved,evolved).real+norm0**2-2*np.vdot(evolved,comparison).real)
            book.check('comparison_squared_nonnegative',max(-error2,0),2e-9,a=a,s=s,error_squared=error2)
            error=float(np.sqrt(max(error2,0)))
            integrated_R=abs(s)/2*sum(w*c.bound_R(n,a,m,v) for w,n in zip(wt,orbit))
            limit=a*(norms_end['f1']+integrated_R)
            book.check('D2_whole_wavefunction',error,limit+2e-7,a=a,s=s,ratio=error/limit,
                       norm_derivative_end=norms_end['f1'],integrated_R=float(integrated_R),box=box,Q=Q,nq=nq,nx=nx)
            book.check('finite_flow_norm',abs(np.linalg.norm(evolved)-np.linalg.norm(initial)),2e-10,a=a,s=s)
            book.check('finite_flow_reality',np.linalg.norm(evolved.imag),2e-11,a=a,s=s)
            # Save full complex vectors for resolution/box comparison, not just errors.
            key=f'a{a}_s{s}'
            stored[key+'_indices']=indices
            stored[key+'_evolved']=evolved
            stored[key+'_continuum_cells']=comparison
    datafile=Path(args.output).with_suffix('.vectors.npz')
    np.savez(datafile,**stored)
    book.finish({'settings':{'Q':Q,'nq':nq,'nx':nx,'box':box},
       'vectors_file':str(datafile),'vectors_sha256':hashlib.sha256(datafile.read_bytes()).hexdigest(),
       'limits':'The literal finite-open weighted flow approximates the infinite group only diagnostically. Fourier and physical quadrature are floating approximations without a certified total error. The two planned resolutions/boxes must be compared. Compact C5 polynomial data are used for diagnostics; theorem uses compact smooth vectors. Formula D2 is an analytic proof, not inferred from these rows.'})

if __name__=='__main__':main()
