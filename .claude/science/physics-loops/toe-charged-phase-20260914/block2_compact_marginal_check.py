"""Actual one-face massive determinant: periodization and cube-sector marginals.

The exact one-face curvature bound sharpens the general loop bound for this
finite diagnostic. It does not test a compact thermodynamic phase.
"""
from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad

M=8.;t=1.;c=M**4-4*M*M*t*t+2*t**4;b=2*t**4
eta=2*b/(c-b);assert c>2*b
out=[]
for beta in [.1,.5,2.,20.]:
    assert beta>eta
    W=lambda F:((c-b*np.cos(F))/c)**2
    gaussian_expect=lambda shift,var:1+(b/c)**2/2-2*(b/c)*np.exp(-var/2)*np.cos(shift)+(b/c)**2/2*np.exp(-2*var)*np.cos(2*shift)
    cutoff=12
    compact=quad(lambda phi:W(phi)*sum(np.exp(-beta*(phi+2*np.pi*n)**2/2) for n in range(-cutoff,cutoff+1)),-np.pi,np.pi,epsabs=1e-11)[0]/(2*np.pi)
    unfolded=math.sqrt(2*np.pi/beta)*gaussian_expect(0,1/beta)/(2*np.pi)
    radius=(2*cutoff+1)*np.pi
    tail=(1+b/c)**2*math.sqrt(2*np.pi/beta)*math.erfc(radius*math.sqrt(beta/2))/(2*np.pi)
    assert abs(compact-unfolded)<tail+1e-11
    # One cube has six oriented faces and one integer three-cell charge.
    # Its normalized incidence vector has entries +/-1/sqrt(6). Projection
    # onto its five-dimensional exact-flux plane gives variance 5/(6 beta)
    # for the selected face coordinate. y_m has squared norm (2pi m)^2/6.
    sigma2=5/(6*beta);normal=gaussian_expect(0,sigma2);sectors=[]
    def logratio(m):
        y2=(2*np.pi*m)**2/6;shift=2*np.pi*m/6
        return -beta*y2/2+np.log(gaussian_expect(shift,sigma2)/normal)
    for m in [0,1,2,3,5]:
        y2=(2*np.pi*m)**2/6;shift=2*np.pi*m/6
        integral=quad(lambda z:np.exp(-z*z/2)*W(np.sqrt(sigma2)*z+shift)/np.sqrt(2*np.pi),-np.inf,np.inf,epsabs=1e-11)[0]
        assert abs(integral-gaussian_expect(shift,sigma2))<1e-10
        lr=logratio(m)
        assert -(beta+eta)*y2/2-1e-12<=lr<=-(beta-eta)*y2/2+1e-12
        sectors.append({'m':m,'log_sector_ratio':lr,'lower_log_bound':-(beta+eta)*y2/2,'upper_log_bound':-(beta-eta)*y2/2,'gaussian_marginal_integral':integral})
    a=(beta-eta)*np.pi**2/6;ms=np.arange(-40,41);weights=np.exp([logratio(int(m)) for m in ms]);density=float(np.dot(ms*ms,weights)/sum(weights))
    theta_bound=4*np.exp(-a/2)/(a*(1-np.exp(-3*a/2)))
    nextm=41;r=np.exp(-a*(2*nextm+1));rt=((nextm+1)/nextm)**2*r;assert rt<1
    ztail=2*np.exp(-a*nextm**2)/(1-r);qtail=2*nextm**2*np.exp(-a*nextm**2)/(1-rt)
    density_error=qtail+density*ztail
    assert density+density_error<=theta_bound+1e-14
    out.append({'beta':beta,'exact_one_face_Hessian_bound':eta,'compact_partition':compact,'unfolded_partition':unfolded,'periodization_tail_bound':tail,'sector_cases':sectors,'current_squared_density':density,'density_truncation_error_upper':density_error,'proved_density_upper':theta_bound})
    print(out[-1],flush=True)
# Noninteger charge is not periodic in the same 2pi gauge convention.
assert abs(((c-b*np.cos(.5*2*np.pi))/c)**2-((c-b)/c)**2)>1e-4
Path(__file__).with_name('BLOCK2_COMPACT_MARGINAL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
