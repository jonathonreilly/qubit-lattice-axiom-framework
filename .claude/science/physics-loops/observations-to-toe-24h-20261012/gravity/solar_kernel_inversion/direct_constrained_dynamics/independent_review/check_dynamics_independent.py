#!/usr/bin/env python3
"""Small independent proof controls, without importing the author runner."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import sys
sys.dont_write_bytecode=True
import hashlib,json,math,resource,time
from datetime import datetime,timezone
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import mpmath as mp
import sympy as s
from scipy.optimize import brentq

HERE=Path(__file__).resolve().parent
RT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def guard():
    assert time.time()<json.loads((RT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RT/n).exists() for n in ('STOP_REQUESTED.json','USER_STOP_REQUESTED.json','STOP_REQUESTED','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'))
def atanh_bounds(z,n):
    lo=sum((z**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
    return lo,lo+z**(2*n+1)/((2*n+1)*(1-z*z))
def mpq(q):return mp.mpf(q.numerator)/q.denominator
def serial(q):return {'fraction':str(q),'approximate':mp.nstr(mpq(q),45)}

def discrete_energy(weights):
    # Solve constant constitutive flux and endpoint compatibility directly;
    # no multi-variable minimizer and no author energy function.
    w=np.array([float(x) for x in weights])
    knots=10.**(-3+np.arange(21)/4)  # Acceleration scaled by 1e-10.
    step=math.log(10)/4
    Nmax=1+sum(w)
    def response(g):
        return 1+np.clip(np.log(knots[1:]/np.maximum(np.abs(g)[:,None],1e-300))/step,0,1)@w
    def inverse_flux(p):
        low=np.minimum(p,0); high=np.maximum(p,0)
        for _ in range(66):
            mid=(low+high)/2
            below=response(mid)*mid<p
            low=np.where(below,mid,low); high=np.where(below,high,mid)
        return (low+high)/2
    x=np.arange(65)/64
    phi=np.sin(np.pi*x)+.13*np.sin(2*np.pi*x);phi[[0,-1]]=0
    gp=64*np.diff(phi)
    shift=brentq(lambda q:sum(inverse_flux(gp+q)), -max(gp),-min(gp),xtol=1e-14)
    g=inverse_flux(gp+shift)
    A=np.abs(g)
    # Integrate 2a N(a) over successive whole/partial ramp intervals.
    F=Nmax*np.minimum(A,knots[0])**2
    for j in range(20):
        lo=knots[j]; hi=np.minimum(A,knots[j+1]);mask=hi>lo
        beta=w[j]/step
        alpha=1+sum(w[j+1:])+beta*np.log(knots[j+1])
        primitive=lambda t:t*t*(alpha-beta*np.log(t)+beta/2)
        F[mask]+=primitive(hi[mask])-primitive(lo)
    F+=np.maximum(0,A*A-knots[-1]**2)
    J=float(np.mean(2*gp*g-F));p2=float(np.mean(gp*gp))
    residual=float(np.max(np.abs(response(g)*g-gp-shift)))
    closure=float(np.mean(g))
    assert residual<2e-14 and abs(closure)<2e-14
    assert p2/Nmax<J<p2
    return {'J':J,'lower':p2/Nmax,'upper':p2,'constant_flux':float(shift),
            'max_flux_residual':residual,'endpoint_closure':closure}

def run():
    start=time.perf_counter();guard();mp.mp.dps=90
    records=[]
    for name in ('snapshot_manifest_v1.json','diagnostic_snapshot_v1.json','diagnostic_version_change.json'):
        records.extend(json.loads((HERE/name).read_text())['sources'])
    for r in records:assert sha(r['original'])==sha(r['snapshot'])==r['sha256']
    frozen=json.loads((HERE/'snapshot_FROZEN_TRANSFER_INPUT.json').read_text(),parse_float=Decimal)
    author1=json.loads((HERE/'snapshot_author_RESULTS_v1.json').read_text())
    author2=json.loads((HERE/'snapshot_author_RESULTS_v2.json').read_text())
    assert author1['identities']['direct_dynamics_check.py']==sha(HERE/'snapshot_author_runner_v1.py')
    assert author2['identities']['direct_dynamics_check.py']==sha(HERE/'snapshot_direct_dynamics_check.py')
    for name in ('PROTOCOL.md','DIRECT_DYNAMICS.md','FROZEN_TRANSFER_INPUT.json'):
        assert author1['identities'][name]==author2['identities'][name]==sha(HERE/('snapshot_'+name))
    for old,new in zip(author1['candidates'],author2['candidates']):
        assert all(new[k]==v for k,v in old.items())
        assert set(new)-set(old)=={'min_D_binary64_lower_exact','min_D_binary64_lower_float'}

    # Different log identity: ln(10)/4 = atanh(1/2) + atanh(1/19)/2.
    lo2,hi2=atanh_bounds(Q(1,2),120);lo19,hi19=atanh_bounds(Q(1,19),40)
    dlo,dhi=lo2+lo19/2,hi2+hi19/2
    d=mp.log(10)/4
    assert mpq(dlo)<d<mpq(dhi)
    alo=Q(author1['log_step_enclosure']['lower_exact']);ahi=Q(author1['log_step_enclosure']['upper_exact'])
    assert alo<=dlo<dhi<=ahi
    candidate_checks=[]
    for name,tokens in frozen['candidates'].items():
        weights=[Q(str(x)) for x in tokens]
        binary=[Q.from_float(float(x)) for x in tokens]
        rows=[]
        for j,w in enumerate(weights):
            N=1+sum(weights[j+1:]); dl=N-w/dlo;dh=N-w/dhi
            assert 0<dl<=dh<=N
            D=mpq(N)-mpq(w)/d;NN=mpq(N)
            # Maximize by all critical m and endpoints, rather than choosing the author's branch formula.
            critical=[D,NN]
            peak=3*NN*D/(2*(NN+D))
            if D<peak<NN:critical.append(peak)
            speeds=[mp.sqrt(((NN+D)*m-NN*D)/m**3) for m in critical]
            vmax=max(speeds)
            author=next(c for c in author2['candidates'] if c['name']==name)['rows'][j]
            assert abs(float(vmax)-author['group_max_over_cs'])<3e-14
            assert abs(float(D)-author['D_upper'])<2e-15
            rows.append({'j':j,'N':serial(N),'D_interval':[serial(dl),serial(dh)],'D_approximate':mp.nstr(D,50),'group_max_over_cs':mp.nstr(vmax,50)})
        exact_min=min(Q(row['D_interval'][0]['fraction']) for row in rows)
        binary_min=min([Q(1)]+[1+sum(binary[j+1:])-binary[j]/dlo for j in range(20)])
        author=next(c for c in author2['candidates'] if c['name']==name)
        assert 0<Q(author['min_D_lower_exact'])<=exact_min
        assert 0<Q(author['min_D_binary64_lower_exact'])<=binary_min
        safe_lower=Q(5676,10000) if name=='original_D_joint' else Q(2336,10000)
        assert min(exact_min,binary_min)>safe_lower
        worst=max(rows,key=lambda row:mp.mpf(row['group_max_over_cs']))
        assert worst['j']==author['worst_group_row']['ramp']
        E=mp.mpf('1.4915242022774435e-10')
        knots=[mp.power(10,mp.mpf(-13)+mp.mpf(j)/4) for j in range(21)]
        cell=next(j for j in range(20) if knots[j]<E<knots[j+1])
        assert weights[cell]==0
        left=right=cell
        while left>0 and weights[left-1]==0:left-=1
        while right<19 and weights[right+1]==0:right+=1
        external_N=1+sum(weights[right+1:])
        assert abs(float(external_N)-author['external_N'])<1e-15
        energy=discrete_energy(weights)
        assert abs(energy['J']-author['nonlinear_Dirichlet_diagnostic']['J'])<2e-12
        candidate_checks.append({'name':name,'rows':rows,'D_strict_safe_lower':str(safe_lower),
            'decimal_min_D_lower':serial(exact_min),'binary64_min_D_lower':serial(binary_min),'worst_ramp':worst['j'],
            'max_group_over_cs':worst['group_max_over_cs'],'external_N_equals_D':serial(external_N),
            'external_plateau':[mp.nstr(knots[left],40),mp.nstr(knots[right+1],40)],
            'external_phase_over_cs':mp.nstr(1/mp.sqrt(mpq(external_N)),45),'external_tail':0,
            'independent_Dirichlet':energy})

    # General radial-composition Laplacian identity, avoiding four Cartesian differentiations.
    N,D,z=s.symbols('N D z',positive=True)
    H=s.diag(1/N,1/N,1/D)
    x=s.Matrix([0,0,z]);r=(x.T*H*x)[0];R=(x.T*H**2*x)[0];V=(x.T*H**3*x)[0]
    T=s.trace(H);U=s.trace(H**2)
    bilap=(3*T*T+6*U)*r**s.Rational(-5,2)-(30*T*R+60*V)*r**s.Rational(-7,2)+105*R*R*r**s.Rational(-9,2)
    kernel=s.factor(-bilap/(4*s.pi*N*s.sqrt(D)))
    target=-6*(N-D)**2/(s.pi*N**3*z**5)
    assert s.simplify(kernel-target)==0
    assert s.simplify(kernel.subs(D,N))==0
    force_tail=s.factor(-s.diff(kernel,z))
    assert s.simplify(force_tail+30*(N-D)**2/(s.pi*N**3*z**6))==0
    m=s.symbols('m',positive=True)
    group_squared=((N+D)*m-N*D)/m**3
    assert s.simplify(s.diff(group_squared,m)+(2*D*m-3*D*N+2*N*m)/m**4)==0
    interior_squared=s.simplify(group_squared.subs(m,3*N*D/(2*(N+D))))
    assert s.simplify(interior_squared-4*(N+D)**3/(27*N**2*D**2))==0
    assert s.limit(D*s.sqrt(interior_squared),D,0,dir='+')==2*s.sqrt(3)*s.sqrt(N)/9
    c=s.symbols('c',positive=True)
    derivative=s.factor(s.diff(s.log(4*(2*N-c)**3/(27*N*N*(N-c)**2)),N))
    assert s.simplify(derivative+2*(N*N-N*c+c*c)/(N*(N-c)*(2*N-c)))==0

    # Exact non-polynomial witness by restriction to a plane: division leaves a nonzero remainder.
    kx,kz=s.symbols('kx kz',real=True)
    remainder=s.rem((kx*kx+kz*kz)**2,2*kx*kx+kz*kz/2,kx)
    assert s.simplify(remainder-s.Rational(9,16)*kz**4)==0
    assert s.rem((kx*kx+kz*kz)**2,2*(kx*kx+kz*kz),kx)==0
    p,q,r,lam,ap=s.symbols('p q r lambda a_phi',nonzero=True,real=True)
    vv=p/(q+r*p)
    reduced_kin=s.factor(lam*ap*ap*(1+r*vv)**2)
    reduced_space=s.factor(-2*p*vv+q*vv**2)
    omega2=s.factor(-reduced_space/reduced_kin)
    assert s.simplify(omega2-p*p/(lam*ap*ap*(q+2*r*p)))==0
    S=s.Matrix([[0,-p],[-p,q]]);a=s.Matrix([ap,r*ap]);w2=s.symbols('omega2')
    assert s.expand((S+w2*lam*a*a.T).det()+p*p-lam*w2*ap*ap*(q+2*r*p))==0
    # k!=0 spatial form has one sign of each; positive K cannot remove it by congruence.
    for kinetic in (np.eye(2),np.array([[2.,.3],[.3,1.]])):
        kval,kvec=np.linalg.eigh(kinetic);invroot=(kvec/np.sqrt(kval))@kvec.T
        frequencies=np.linalg.eigvalsh(-invroot@np.array([[0.,-1.],[-1.,2.]])@invroot)
        assert frequencies[0]<0<frequencies[1]

    # Small normalized C-infinity radial bump convolved away from its support.
    # The continuity argument is the proof; quadrature illustrates the witness.
    rr,rw=np.polynomial.legendre.leggauss(16);rr=(rr+1)/2;rw=rw/2
    mu,mw=np.polynomial.legendre.leggauss(12);phi=2*np.pi*np.arange(16)/16
    pts=np.array([[rad*np.sqrt(1-cc*cc)*np.cos(ph),rad*np.sqrt(1-cc*cc)*np.sin(ph),rad*cc]
                  for rad in rr for cc in mu for ph in phi])
    weights=np.array([wr*rad*rad*np.exp(-1/(1-rad*rad))*wc*2*np.pi/16
                      for rad,wr in zip(rr,rw) for cc,wc in zip(mu,mw) for ph in phi])
    weights/=sum(weights)
    def eval_kernel(points):
        h=np.array([.5,.5,2.]);T=sum(h);U=sum(h*h)
        ss=(points*points)@h;RR=(points*points)@(h*h);VV=(points*points)@(h*h*h)
        lap2=(3*T*T+6*U)*ss**(-2.5)-(30*T*RR+60*VV)*ss**(-3.5)+105*RR*RR*ss**(-4.5)
        return -lap2/(4*np.pi*2*np.sqrt(.5))
    exact_axis=float(target.subs({N:2,D:s.Rational(1,2),z:2}))
    bump=[]
    for radius in (.2,.1,.05):
        points=np.array([0,0,2.])-radius*pts
        samples=eval_kernel(points)
        assert np.max(samples)<0
        value=float(weights@samples)
        dz=np.array([0,0,1e-4])
        force=float(-weights@(eval_kernel(points+dz)-eval_kernel(points-dz))/(2e-4))
        assert force<0
        bump.append({'radius':radius,'acceleration_tail':value,'force_acceleration_tail':force,'relative_axis_error':abs(value/exact_axis-1)})
    assert bump[-1]['relative_axis_error']<bump[0]['relative_axis_error']
    guard()
    for rec in records:assert sha(rec['original'])==sha(rec['snapshot'])==rec['sha256']
    output={'at':datetime.now(timezone.utc).isoformat(),'status':'SCOPED_PROOF_AND_CONTROLS_CONSISTENT',
        'source_records':records,'reviewer_script_sha256':sha(__file__),
        'independent_log_step':[serial(dlo),serial(dhi)],'candidate_checks':candidate_checks,
        'axis_kernel_cs1':str(kernel),'force_acceleration_kernel_cs1':str(force_tail),
        'rank_one_reduced_kinetic':str(reduced_kin),'rank_one_reduced_spatial':str(reduced_space),
        'rank_one_frequency':str(omega2),'anisotropic_polynomial_remainder':str(remainder),
        'small_bump_controls':bump,'source_version_change':'v2 preserves all v1 candidate fields and adds exact binary64-weight positivity bounds; wording now separates certification from approximate infimum.',
        'limits':'Same static response is supplied. Zero-boundary nonlinear energy and homogeneous whole-space compact physical-data propagation are different domains. No matter-plus-field positivity, nonlinear existence, quasistatic transfer, empirical signaling or full gravity classification proved.',
        'elapsed_seconds':time.perf_counter()-start,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with (HERE/'independent_dynamics_checks_v1.json').open('x') as f:json.dump(output,f,indent=2)
    print(json.dumps({'status':output['status'],'candidates':[{'name':c['name'],'D_safe_lower':c['D_strict_safe_lower'],'vmax_over_cs':c['max_group_over_cs'],'Dirichlet_J':c['independent_Dirichlet']['J']} for c in candidate_checks], 'elapsed_seconds':output['elapsed_seconds'],'max_rss_bytes':output['max_rss_bytes']},indent=2))

if __name__=='__main__':run()
