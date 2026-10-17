#!/usr/bin/env python3
"""Exact residual replay plus analytic, non-grid interval certificate.

The fixed rational input is read from the frozen old-cap certificate, never
from a binary64 optimizer. mpmath proposes matrices; Fraction arithmetic and
the inequalities proved in CANDIDATE.md certify them. This is a source-exposed
author calculation, not an independent review or an infinite-chain simulation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
import numpy as np
import mpmath as mp

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 90
started = time.monotonic()
for row in json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())['sources']:
    b = Path(row['snapshot_path']).read_bytes()
    assert len(b) == row['bytes']
    assert hashlib.sha256(b).hexdigest() == row['sha256']
frozen = json.loads((ROOT/'inputs/rational_point_certificate.json').read_text())
par = {k:F(v) for k,v in frozen['exact_parameters'].items()}
J, cos0, sin0 = (par[k] for k in ('J','cos_k','sin_k'))
eps = par['epsilon']
gA,gB,h,la,lb,u,dA,dB,mu0,mu1,nu = (par[k] for k in
    ('gA','gB','t','lambdaA','lambdaB','u','DeltaA','DeltaB','mu0','mu1','scalar_reserve'))
assert cos0*cos0+sin0*sin0 == 1 and cos0>0 and sin0>0
assert eps == 2*J*(1-cos0)
assert nu == -mu1 > 0 and mu0 >= 0
assert min(dA,dB,h,la,lb,u,gA,gB)>0 and max(gA,gB)<=1

DEN = 10**55
def rounded(x): return F(int(mp.nint(x*DEN)),DEN)
def mpq(x): return mp.mpf(x.numerator)/x.denominator
def zeros(n,m=None): return np.full((n,n if m is None else m),F(0),dtype=object)
def eye(n):
    a=zeros(n)
    for i in range(n): a[i,i]=F(1)
    return a
def norm(a): return max(sum(abs(v) for v in row) for row in a)
def cnorm(ar,ai):
    return max(sum(abs(x)+abs(y) for x,y in zip(r,s)) for r,s in zip(ar,ai))
def cmatrix_product(ar,ai,br,bi): return ar@br-ai@bi, ar@bi+ai@br
def packed(q): return {'rational':str(q),'display_float':float(q)}
def serial(a): return [[str(v) for v in row] for row in a]
def cadd(a,b): return a[0]+b[0], a[1]+b[1]
def cneg(a): return -a[0],-a[1]
def cmul(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def cscale(q,a): return q*a[0],q*a[1]
def cpow(a,n):
    r=(F(1),F(0))
    for _ in range(n): r=cmul(r,a)
    return r

I2,I4,I8,I16 = (eye(n) for n in (2,4,8,16))
X=zeros(2); X[0,1]=X[1,0]=F(1)
Z=np.diag([F(1),F(-1)])
nA=np.diag([F(0),F(0),F(1),F(1)])
nB=np.diag([F(0),F(1),F(0),F(1)])
hop=zeros(4); hop[1,2]=hop[2,1]=F(1)
XA,XB=np.kron(X,I2),np.kron(I2,X)
VA=la*np.kron(I4+XA,I2)+mu0*I8
VB=lb*np.kron(I4+XB,I2)+mu1*I8
Cbare=dA*nA+dB*nB+h*(nA+nB-hop)+u*nA@nB
K4=2*I4+np.kron(Z,Z)
Bfull=np.kron(I4,K4)+np.kron(Cbare,I4)
Bfull+=gA*np.kron(nA,I4+np.kron(X,I2))
Bfull+=gB*np.kron(nB,I4+np.kron(I2,X))
Pfull=np.kron(I4,np.kron(X,X))
assert np.array_equal(Bfull,Bfull.T)
assert np.array_equal(Bfull@Pfull,Pfull@Bfull)
assert np.array_equal(Bfull[:4,:4],K4)
assert np.array_equal(Bfull[4:,:4],zeros(12,4))

channels=[]; witnesses=[]; rapp={}; rerr={}
for p in (1,-1):
    C=(dA+gA)*nA+(dB+gB)*nB+h*(nA+nB-hop)+u*nA@nB
    G=gA*nA+p*gB*nB
    B=np.kron(I4,2*I2+Z)+np.kron(C,I2)+np.kron(G,X)
    # Unnormalized exact Bell columns avoid any eigenvector/rounding premise.
    Uold=np.array([[F(1),F(0)],[F(0),F(p)],
                  [F(0),F(1)],[F(p),F(0)]],dtype=object)
    U=np.kron(I4,Uold)
    assert np.array_equal(U.T@U,2*I8)
    assert np.array_equal(U.T@Bfull@U,2*B)
    assert np.array_equal(B[:2,:2],2*I2+Z)
    assert np.array_equal(B[2:,:2],zeros(6,2))
    for s in (1,-1):
        iss=0 if s==1 else 1
        E=2+s+eps
        D=B[2:,2:]+(2*J-E)*eye(6)
        dl=1+min(dA,dB)+2*J-E
        assert dl>2*J
        A=D@D-4*J*J*eye(6)
        dm=mp.matrix([[mpq(v) for v in row] for row in D])
        ev,V=mp.eigsy(dm)
        Sm=V*mp.diag([mp.sqrt(v*v-4*mpq(J)**2) for v in ev])*V.T
        S=np.array([[rounded(Sm[i,j]) for j in range(6)] for i in range(6)],dtype=object)
        assert np.array_equal(S,S.T)
        root_res=norm(S@S-A)
        candidate_lower=dl-norm(S-D)
        true_lower=dl-2*J
        assert candidate_lower>0
        root_error=root_res/(candidate_lower+true_lower)
        source_F_error=F(3,2)*root_error
        Do=(2-s)+2*J-E
        assert abs(Do)>2*J
        So=rounded(mp.sqrt(mpq(Do*Do-4*J*J)))
        other_F_error=abs(So*So-(Do*Do-4*J*J))/(So+abs(Do)-2*J)/2
        Fr=zeros(8); Fi=zeros(8)
        Fr[iss,iss]=-J*cos0; Fi[iss,iss]=J*sin0
        Fr[1-iss,1-iss]=-(Do+(1 if Do>0 else -1)*So)/2
        Fr[2:,2:]=-(D+S)/2
        Mr=zeros(16); Mi=zeros(16)
        Mr[:8,:8]=(E-2*J)*I8-B-VA
        Mr[:8,8:]=J*I8; Mr[8:,:8]=J*I8
        Mr[8:,8:]=Fr-VB; Mi[8:,8:]=Fi
        assert np.array_equal(Mr,Mr.T) and np.array_equal(Mi,Mi.T)
        mm=mp.matrix([[mpq(Mr[i,j])+mp.j*mpq(Mi[i,j]) for j in range(16)] for i in range(16)])
        inv=mm**-1
        Nr=np.array([[rounded(mp.re(inv[i,j])) for j in range(16)] for i in range(16)],dtype=object)
        Ni=np.array([[rounded(mp.im(inv[i,j])) for j in range(16)] for i in range(16)],dtype=object)
        rr,ri=cmatrix_product(Mr,Mi,Nr,Ni)
        inverse_res=cnorm(I16-rr,-ri)
        assert inverse_res<1
        approx_inverse_bound=cnorm(Nr,Ni)/(1-inverse_res)
        deltaM=max(source_F_error,other_F_error)
        assert approx_inverse_bound*deltaM<1
        inverse_bound=approx_inverse_bound/(1-approx_inverse_bound*deltaM)
        assert inverse_bound<164
        br=zeros(16,1); bi=zeros(16,1); bi[8+iss,0]=2*J*sin0
        xm=inv*mp.matrix([mpq(br[i,0])+mp.j*mpq(bi[i,0]) for i in range(16)])
        xr=np.array([[rounded(mp.re(v))] for v in xm],dtype=object)
        xi=np.array([[rounded(mp.im(v))] for v in xm],dtype=object)
        axr,axi=cmatrix_product(Mr,Mi,xr,xi)
        state_res=cnorm(axr-br,axi-bi)
        state_error=inverse_bound*(state_res+deltaM*cnorm(xr,xi))
        rapp[s,p]=(xr[8+iss,0]-1,xi[8+iss,0]); rerr[s,p]=state_error
        channels.append({'s':s,'p':p,'inverse_infinity_upper':packed(inverse_bound),
            'root_error':packed(root_error),'inverse_residual':packed(inverse_res),
            'matrix_error':packed(deltaM),'state_residual':packed(state_res),
            'reflection_error':packed(state_error),
            'reflection_approximation':[str(v) for v in rapp[s,p]]})
        witnesses.append({'s':s,'p':p,'sqrt_source':serial(S),'sqrt_other':str(So),
            'inverse_real':serial(Nr),'inverse_imag':serial(Ni),
            'state_real':serial(xr),'state_imag':serial(xi)})

alpha=rapp[-1,-1]; alpha_error=rerr[-1,-1]
central=[]
for s in (1,-1):
    for p in (1,-1):
        w=(F(-7,25),F(24,25)) if p==1 else (F(1),F(0))
        target=cmul(w,alpha)
        chord=sum(abs(x-y) for x,y in zip(rapp[s,p],target))+rerr[s,p]+alpha_error
        central.append({'s':s,'p':p,'bound':packed(chord)})
central_bound=max(F(row['bound']['rational']) for row in central)
central_contract=F(176,10**15)
assert central_bound<central_contract
assert F(frozen['certified_point_isometry_error']['rational'])<central_contract

# Exact algebra confirms the site-1 free coefficient and phase conversion.
z0=(cos0,sin0); zi=(cos0,-sin0)
x0=cadd(z0,cneg(cpow(z0,3)))
x1=cadd((F(1),F(0)),cneg(cpow(z0,4)))
row0=cadd(cscale(-2*J*cos0,x0),cscale(J,x1))
row1=cadd(cscale(J,x0),cscale(-J,cmul(zi,x1)))
assert row0==(0,0) and row1==(0,2*J*sin0)
zeta_approx=cneg(cmul(cpow(zi,4),alpha))
r0_abs=cneg(cpow(z0,2))
assert cmul(r0_abs,zeta_approx)==cmul(cpow(zi,2),alpha)

# Entire interval, using only exact rational inequalities and Lipschitz bounds.
width=F(1,1000)
assert sin0>width
epsilon_low=eps-2*J*width; epsilon_high=eps+2*J*width
assert 0<epsilon_low<epsilon_high<4*J
source_gap=min(dA,dB)-2-epsilon_high
old_gap=2-4*J
g=F(9,50)
assert min(source_gap,old_gap)>g
kappa=F(1,7)
assert 2+g/J>kappa+1/kappa
Q1=2*kappa*kappa/(1-kappa*kappa)
assert Q1==F(1,24)
M16prime=2*J/(1-kappa*kappa)
neumann=164*M16prime*width
assert neumann<1
M16inverse=F(164)/(1-neumann)
assert M16inverse<166
M24inverse=F(332)+1/J
assert M24inverse<366
nu24=F(1,366)
LM24=F(11,100)
assert J*J*(9+4/(1-kappa*kappa)**2)<LM24*LM24
assert 2*J*J/nu24**2<16**2
X1upper=(F(9,4)*J+LM24*16)/nu24
assert X1upper<700
X0=F(16); X1=F(700)
C0sq=2*(X0+2)**2+X0*X0/(1-kappa*kappa)
assert C0sq<31**2
assert (2*X1)**2+(2*X1+2)**2<1982**2
assert 1/(1-kappa*kappa)<F(1011,1000)**2
assert (1+kappa*kappa)/(1-kappa*kappa)**3<F(21,20)**2
C1upper=F(1982)+X1*F(1011,1000)+X0*Q1*F(21,20)
assert C1upper<2700
v=F(1,40)
velocity_lower=2*J*(sin0-width)
assert velocity_lower>v and 2*J/v<F(5,2)

# Explicit supplied packet and finite resource example. No huge state is built.
sigma=F(1,10**6)
F0,F1=F(1,750),F(2000)
assert 15*sigma/9<F0*F0 and F(15)/(4*sigma)<F1*F1
CA=CB=F(2001)
assert F1+F(5,2)*F0<CA
assert F1+(X1+F(5,2))*F0<CB
Dj=F1*31+F0*2700+F(5,2)*F0*31
Dpacket=F(88000)
assert Dj<62004 and 2*Dj*Dj<Dpacket*Dpacket
Delta=central_contract+(X1+2)*sigma
T=10**13
sqrt_lower=F(866000)
# pi>3, sqrt(2pi)>12/5; every final resource assertion is rational.
assert sqrt_lower**2<3*v*T
delta_in=CB/sqrt_lower+Dpacket/(F(12,5)*v*T)
assert v*T>=1 and delta_in<F(1,4) and CA/sqrt_lower<F(1,4)
joint=Delta+2*(CA+CB)/sqrt_lower+3*Dpacket/(F(12,5)*v*T)
eta_p=F(1,1000)
N=22*10**12
d=N-2*J*T
assert d>=max(F(1),2*J*T,16*(F1+F0)**2/(3*eta_p**2))
assert joint+eta_p<F(11,1000)
point_amplitude=2*delta_in+eta_p
assert point_amplitude<F(5622,10**6)
bmax_bound=3+dA+dB+2*h+u+2*gA+2*gB
assert bmax_bound<20
Vmax=max(2*la+mu0,abs(mu1),abs(2*lb+mu1))
rho=F(18)
assert 2*J+F(19,2)+Vmax<rho
Tobs=4*T; M=9*10**14; dM=M-N+1; zeta=F(1,1000)
e_upper=sum(F(1,math.factorial(k)) for k in range(5))+F(1,120)/(1-F(1,6))
assert e_upper<F(11,4)
assert (F(11,4)-F(4,11))/2<F(6,5)
assert 1-F(3,8)>F(3,5)
assert 4/(F(3,5)*zeta)<F(8,3)**9
assert dM>rho*Tobs*F(6,5)+9
assert joint+eta_p+zeta<F(12,1000)

report={
 'status':'Certified exact fixed-point replay and analytic interval inequalities; wavepacket conclusion conditional on separately reviewed bridge',
 'exact_parameters':{k:str(v) for k,v in par.items()},
 'central_channels':channels,'central_comparison':central,
 'central_bound':packed(central_bound),'retained_central_contract':str(central_contract),
 'phase':{'absolute_reflection':'r_abs(k)=exp(-2ik) r_site1(k)',
          'free_site1':'-exp(4ik)','free_absolute':'-exp(2ik)',
          'single_scalar':'zeta=-exp(-4ik0)*alpha; alpha=exact r_site1_(-1,-1)(k0)',
          'zeta_approximation':[str(v) for v in zeta_approx],
          'zeta_approximation_error':packed(alpha_error),
          'physical_scalar':'exp(-i nu t)','nu':str(nu),
          'exact_free_boundary_and_scalar_algebra':True},
 'interval':{'center':'k0=2 arctan(1/q), q='+str(par['tan_half_complement']),
             'half_width':str(width),'epsilon_lower':packed(epsilon_low),
             'epsilon_upper':packed(epsilon_high),'source_gap_lower':packed(source_gap),
             'old_band_gap_lower':packed(old_gap),'chosen_closed_gap':str(g),
             'kappa_upper':str(kappa),'closed_root_derivative_upper':str(Q1),
             'velocity_lower':packed(velocity_lower),'chosen_velocity_lower':str(v)},
 'matching':{'point_M16_inverse_2_upper':164,'M16_derivative_2_upper':packed(M16prime),
             'Neumann_parameter_upper':packed(neumann),'interval_M16_inverse_2_upper':packed(M16inverse),
             'chosen_M16_inverse_2_upper':166,'M24_inverse_2_upper':packed(M24inverse),
             'chosen_M24_inverse_2_upper':366,'M24_sigma_min_lower':str(nu24),
             'M24_derivative_upper':str(LM24),'X0':16,'X1_and_L':700,
             'C0':31,'C1':2700,'numerical_eigenvectors_used_in_norm_conversion':False},
 'packet':{'half_width':str(sigma),'F0_upper':str(F0),'F1_upper':str(F1),
           'CA':str(CA),'CB':str(CB),'Dj_upper':packed(Dj),'D_grouped_upper':str(Dpacket),
           'Delta_upper':packed(Delta),'T':T,'all_future_from_elapsed_time':2*T,
           'delta_in_upper':packed(delta_in),'infinite_untruncated_isometry_upper':packed(joint),
           'eta_p':str(eta_p),'support_sites':N,
           'infinite_finite_preparation_isometry_upper':packed(joint+eta_p),
           'infinite_bound_state_amplitude_upper':packed(point_amplitude),
           'approximate_preparation_error_assumed':0,
           'preparation_scope':'Specified normalized finite vector of Fourier integrals; no native generator supplied'},
 'finite_horizon':{'B_spectral_lower':1,'B_spectral_upper':20,
                   'positive_block_B_upper':packed(bmax_bound),'Vmax':packed(Vmax),
                   'rho_upper':str(rho),'Tobs':Tobs,'mu':1,'clock_sites':M,
                   'first_omitted_site_path_distance':dM,'finite_boundary_tolerance':str(zeta),
                   'complete_isometry_upper':packed(joint+eta_p+zeta),
                   'complete_unhalved_trace_upper':packed(2*(joint+eta_p+zeta))},
 'checks':{'physical_B_exact_block_reduction':True,'vacuum_B_equals_K':True,
           'parity_reducing':True,'old_added_cap_2':True,'momentum_grid_used':False,
           'all_source_channels_included':True},
 'runtime':{'python':sys.version,'executable':sys.executable,'numpy':np.__version__,
            'mpmath':mp.__version__,'mpmath_dps':mp.mp.dps,'platform':platform.platform(),
            'largest_executed_matrix_dimension':16,'square_root_dimension':6,
            'theorem_matching_dimension':24,'cpu_seconds_cap':60,
            'elapsed_seconds_after_import':time.monotonic()-started},
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
(ROOT/'POINT_WITNESSES.json').write_text(json.dumps(witnesses,indent=2)+'\n')
(ROOT/'CERTIFICATE.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
