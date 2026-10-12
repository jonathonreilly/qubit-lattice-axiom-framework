"""Independent physical integration and Taylor-remainder diagnostics for D1."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from fixtures import PACKETS,independent_cells
from reporting import arguments,Book

def weighted_remainder(packet,a,sign,n=64):
    lo=packet.center-packet.radius-a;hi=packet.center+packet.radius+a
    knots=sorted(set([lo,hi,packet.center-packet.radius,packet.center+packet.radius,
                      packet.center-packet.radius-sign*a,packet.center+packet.radius-sign*a]))
    z,w=leggauss(n);total=0.
    for l,r in zip(knots[:-1],knots[1:]):
        x=(l+r)/2+(r-l)*z/2
        diff=(packet.value(x+sign*a)-packet.value(x))/(sign*a)-packet.value(x,1)
        total+=(r-l)/2*np.sum(w[:,None]*(x[:,None]*diff)**2)
    return float(np.sqrt(total))

def main():
    args,c=arguments();b=Book('weighted_cells',args);m=.8;v=1.3
    for packet in PACKETS:
        norms=packet.norms()
        for a in [.4,.2,.1,.05,.025]:
            indices=np.arange(int(np.floor((packet.center-packet.radius)/a))-2,
                              int(np.ceil((packet.center+packet.radius)/a))+2)
            # Reference couplings are reconstructed from the two supplied constraints.
            J=(np.sqrt(m*m+4*v*v/a**2)-m)/4;g=J+m/2
            cells=c.cell_average(packet,indices,a)
            reference=independent_cells(packet,indices,a)
            ctx={'packet':packet.name,'a':a}
            b.check('physical_cell_integral',np.linalg.norm(cells-reference),2e-10,**ctx)
            b.check('cell_contraction',np.linalg.norm(cells),norms['f0']+2e-11,**ctx)
            B=c.boost_matrix(indices,a,g,J)
            actual=B@cells.ravel()
            expected=independent_cells(packet,indices,a,boost=True,m=m,v=v).ravel()
            residual=np.linalg.norm(actual-expected)
            bound=a*c.bound_R(norms,a,m,v)
            b.check('D1',residual,bound+3e-10,**ctx,ratio=float(residual/bound),norms=norms)
            for sign in [-1,1]:
                rem=weighted_remainder(packet,a,sign)
                limit=a/2*norms['xf2']+a*a/6*norms['f2']
                b.check('weighted_Taylor',rem,limit+3e-9,**ctx,sign=sign)
            # Actual C_a of a cell-constant unit vector must return that vector.
            right_inverse=a**c.CELL_POWER*a/np.sqrt(a)
            b.check('cell_right_inverse',abs(right_inverse-1),2e-14,**ctx)
    b.finish('Reference continuum B is evaluated from analytic physical derivatives under split Gauss integration; candidate cells use polynomial antiderivatives. Norm integrals are polynomial quadratures, with floating tolerances and no interval-arithmetic certificate. The compact polynomial fixtures are C5 (H² weighted), not C_c-infinity. Full rows retain all loose-bound survivors.')

if __name__=='__main__':main()
