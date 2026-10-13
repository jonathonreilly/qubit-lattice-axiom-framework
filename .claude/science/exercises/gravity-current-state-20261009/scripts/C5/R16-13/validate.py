"""R16-13 validation: (1) Dirac Xi_F evaluator vs R10-5's 8-comp control (sin k, (1-cos k)/2) at m=0.3: Xi_F = -0.004195,
alpha_F = +0.03588 (r105_tt_paired.out); (2) strain mu_E^s for the NN scalar at m=1 vs V3 +1.97038864e-3."""
import numpy as np, time
from dirac import dirac_xi, strain_mu, Fn
t0=time.time()
ctrl = Fn(np.sin, np.cos, lambda k: -np.sin(k), lambda k: 0.5*(1-np.cos(k)), lambda k: 0.5*np.sin(k), lambda k: 0.5*np.cos(k))
for N in (96, 160):
    r = dirac_xi(ctrl, 0.3, N, pol='T2g', Nc=8, kind='CF')
    print('8-comp control m=0.3 N=%d T2g: alpha_F %+.5f  beta_F %+.6f  Xi_F %+.6f   (R10-5: alpha_F +0.03588, Xi_F -0.004195)' % (N, r['alpha'], r['beta'], r['Xi']), flush=True)
# closed form of R10-5 Theorem PT for the fermion alone: Xi_F = <g(|c'|^2-1)/E^3> - <s_x s_y A_zz/E^5>
N=160; k=(np.arange(N)+0.5)*2*np.pi/N-np.pi
S=np.sin(k); W=0.5*(1-np.cos(k)); v=S*S+W*W; cp2=np.cos(k)**2+0.25*np.sin(k)**2
vpp=2*(np.cos(k)**2 - np.sin(k)**2) + 2*(0.25*np.sin(k)**2 + W*0.5*np.cos(k)); A=vpp/2-1
X,Y,Z=np.meshgrid(np.arange(N),np.arange(N),np.arange(N),indexing='ij'); m=0.3
E=np.sqrt(m*m+v[X]+v[Y]+v[Z]); sx=S[X]**2; sy=S[Y]**2
for pol in ('T2g','Eg'):
    w = 4*sx*sy if pol=='T2g' else (sx-sy)**2
    cf = np.mean(0.25*(sx+sy)*(cp2[Z]-1)/E**3) - np.mean(0.25*w*A[Z]/E**5)
    r = dirac_xi(ctrl, 0.3, N, pol=pol, Nc=8, kind='CF')
    print('closed form (PT, fermion alone) %s: %+.6f   evaluator %+.6f' % (pol, cf, r['Xi']), flush=True)
# scalar strain calibration
nn = Fn(lambda k: 2*np.sin(k/2), lambda k: np.cos(k/2), lambda k: -0.5*np.sin(k/2), lambda k: 0*k, lambda k: 0*k, lambda k: 0*k)
for N in (64, 96):
    muE, muT = strain_mu(nn, 1.0, N, kind='sep')
    print('NN scalar m=1 N=%d: mu_E^s %+.10e (V3 +1.97038864e-3)  mu_T2^s %+.2e' % (N, muE, muT), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
