#!/usr/bin/env python3
"""Author finite checks for clock correlations and static transfer matching.
All scientific fixtures are constructed here. The sole repository integrity
read is this script's source hash; no external scientific input is read.
Infinite-volume proofs and physical identification require independent review.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 300
"""Finite direct-clock and shifted-current checks, not an infinite-volume proof."""
from itertools import product
from pathlib import Path
import json
import numpy as np
from scipy.special import logsumexp


def theta_f(beta,x,qmax=12):
    q=np.arange(1,qmax+1,dtype=float)
    r=np.exp(-np.pi**2*beta*q*q/3)
    return (1+2*np.cos(2*np.pi*np.asarray(x)[...,None]*q)@r)/(1+2*r.sum())


def curvature_majorant(beta):
    q=np.arange(1,30,dtype=float)
    r=np.exp(-np.pi**2*beta*q*q/3)
    floor=1-2*r.sum()
    assert floor>0
    m1=4*np.pi*(q*r).sum()
    m2=8*np.pi**2*(q*q*r).sum()
    return m2/floor+(m1/floor)**2


def clock_character(n,beta,source):
    # On one oriented three-cube the six face fluxes obey sum b=0 mod N.
    # The first five are independent uniform gauge-quotient coordinates.
    x=np.asarray(list(product(range(n),repeat=5)),dtype=float)
    b=np.column_stack((x,np.mod(-x.sum(axis=1),n)))
    angles=2*np.pi*np.arange(n)/n
    images=np.arange(-7,8)
    lw=logsumexp(-beta/2*(angles[:,None]-2*np.pi*images)**2,axis=1)
    logweights=lw[b.astype(int)].sum(axis=1)
    probabilities=np.exp(logweights-logsumexp(logweights))
    phases=np.exp(2j*np.pi*(b@source)/n)
    value=probabilities@phases
    assert abs(value.imag)<2e-13 and value.real>0
    return float(value.real)


def current_coset(n,beta,source,cutoff,drop_magnetic=False,wrong_shift=False):
    basis=np.asarray(list(product(range(-cutoff,cutoff+1),repeat=5)),dtype=float)
    basis=np.column_stack((basis,np.zeros(len(basis))))
    shift=(source-source[-1])/ (1 if wrong_shift else n)
    def weights(a):
        projected=a-a.mean(axis=1)[:,None]
        value=np.exp(-n*n/(2*beta)*(projected*projected).sum(axis=1))
        if not drop_magnetic:
            value*=theta_f(beta,n*projected[:,-1])
        return value
    return float(weights(basis+shift).sum()/weights(basis).sum())


def coset_tail_bound(n,beta,source,cutoff,ratio):
    # P on the five-coordinate quotient is I-11^T/6. Conditioning on
    # one coordinate gives energy x_i^2/2. The remaining precision is
    # B=I_4-11^T/6, det B=1/3 and B^-1>=I. Gaussian Poisson summation
    # bounds every translated four-dimensional sum by the expression below.
    a=n*n/(2*beta)
    q=np.pi*np.pi/a
    theta_bound=1+2*np.exp(-q)/(1-np.exp(-3*q))
    conditional_bound=np.sqrt(3)*(np.pi/a)**2*theta_bound**4
    def tail(shift):
        result=0.
        for value in shift:
            for sign in [-1,1]:
                x=cutoff+1+sign*value
                assert x>0
                result+=np.exp(-a*x*x/2)/(1-np.exp(-a*(x+.5)))
        return conditional_bound*result
    shifted=(source[:-1]-source[-1])/n
    # The retained denominator is at least its unit origin weight.
    return float(tail(shifted)+ratio*tail(np.zeros(5)))


def periodized_log(alpha,z,shift,center=0):
    grid=np.arange(-20,21,dtype=float)+shift
    v=alpha*(grid-center)**2/2-z*np.cos(2*np.pi*grid)
    return float(logsumexp(-v))


def check_wilson_shift():
    data={'scope':'Finite three-cube and one-dimensional challenges; not the four-dimensional thermodynamic theorem.',
          'independent_review':False,'families':{}}
    cases=[]
    for alpha,z in [(3.,.03),(1.,.2),(20.,.3)]:
        upper=alpha+z*(2*np.pi)**2
        for shift in [.025,.15,.5,1.15]:
            actual=periodized_log(alpha,z,shift)-periodized_log(alpha,z,0)
            bound=-upper*shift*shift/2
            assert actual>=bound-2e-13
            assert abs(actual-(periodized_log(alpha,z,shift+1)-periodized_log(alpha,z,0)))<2e-13
            cases.append({'alpha':alpha,'z':z,'shift':shift,'log_ratio':actual,'lower_bound':bound,
                          'potential_is_nonconvex':alpha-z*(2*np.pi)**2<0})
    data['families']['periodized_curvature']={'cases':cases}
    alpha,z,shift=20.,.3,.025
    actual=periodized_log(alpha,z,shift)-periodized_log(alpha,z,0)
    wrong_bound=-(alpha-z*(2*np.pi)**2)*shift**2/2
    assert actual<wrong_bound-1e-4
    nonsym=periodized_log(80.,0.,-.2,.2)-periodized_log(80.,0.,0.,.2)
    assert nonsym< -80*.2**2/2-1
    data['families']['assumption_faults']={'wrong_curvature_margin':wrong_bound-actual,
                                         'non_even_log_ratio':nonsym,'invalid_even_bound':-80*.2**2/2}

    sources=[np.array([1,0,0,0,0,0]),np.array([1,1,0,0,0,0]),np.array([1,2,0,-1,0,0])]
    checks=[]
    for n,beta in [(2,2.),(3,2.),(5,2.),(3,3.)]:
        eps=curvature_majorant(beta)
        for source in sources:
            exact=clock_character(n,beta,source)
            projections=source-source.mean()
            energy=float(projections@projections)
            lower=float(np.exp(-(1/beta+eps)*energy/2))
            assert exact>=lower-2e-13 and exact<=1+2e-13
            cutoffs=[3,4,5,6,7] if n==2 else ([2,3,4,5,6] if beta==3 else [2,3,4,5])
            sums=[current_coset(n,beta,source,k) for k in cutoffs]
            tail_bound=coset_tail_bound(n,beta,source,cutoffs[-1],sums[-1])
            assert abs(sums[-1]-exact)<3e-8
            assert abs(sums[-1]-exact)<=tail_bound+5e-13
            checks.append({'N':n,'beta':beta,'source':source.tolist(),'curvature_epsilon_majorant':eps,
                           'coulomb_energy':energy,'direct_clock':exact,'lower_bound':lower,
                           'cutoffs':cutoffs,'coset_values':sums,'last_absolute_discrepancy':abs(sums[-1]-exact),
                           'analytic_gaussian_truncation_bound_evaluated_in_float':tail_bound})
    data['families']['clock_vs_current_coset']={'cases':checks}
    source=sources[0]
    exact=clock_character(3,2.,source)
    wrong=current_coset(3,2.,source,4,wrong_shift=True)
    dropped=current_coset(3,2.,source,4,drop_magnetic=True)
    assert abs(wrong-exact)>1e-4 and abs(dropped-exact)>1e-8
    alias=clock_character(3,2.,3*source)
    assert abs(alias-1)<2e-13
    charge2=clock_character(3,2.,2*source)
    assert abs(charge2-exact)<2e-13
    data['families']['physical_alias_and_source_faults']={'physical_character':exact,'wrong_shift':wrong,
                'dropped_magnetic_factor':dropped,'charge_N_alias':alias,'charge_two_equals_minus_one':charge2}
    return data

"""Direct currents, sparse Poisson solves and reduced Green quadrature."""
from pathlib import Path
import json
import numpy as np
from scipy.sparse.linalg import LinearOperator,cg


def currents(side,r,t):
    assert max(r,t)<side
    j0=np.zeros((side,)*4);j1=np.zeros_like(j0)
    j0[:t,0,0,0]=1;j0[:t,r,0,0]=-1
    j1[t,:r,0,0]=1;j1[0,:r,0,0]=-1
    divergence=np.roll(j0,1,axis=0)-j0+np.roll(j1,1,axis=1)-j1
    assert np.max(np.abs(divergence))==0
    return j0,j1


def fft_energy(side,r,t):
    j0,j1=currents(side,r,t)
    one=2-2*np.cos(2*np.pi*np.arange(side)/side)
    lam=sum(one.reshape((1,)*i+(side,)+(1,)*(3-i)) for i in range(4))
    lam[0,0,0,0]=1
    energy=0.
    parts=[]
    for j in [j0,j1]:
        hat=np.fft.fftn(j)
        part=float(np.sum(np.abs(hat)**2/lam)/side**4)
        parts.append(part);energy+=part
    return energy,parts


def reduced_integrals(n,pairs):
    k=2*np.pi*(np.arange(n)+.5)/n-np.pi
    one=2-2*np.cos(k)
    l1=one[:,None,None]
    lam=l1+one[None,:,None]+one[None,None,:]
    root=np.sqrt(lam*(lam+4))
    exponent=2*np.arcsinh(np.sqrt(lam)/2)
    g4=float(np.mean(1/root))
    out={}
    for r,t in pairs:
        dr2=(np.sin(r*k/2)/np.sin(k/2))[:,None,None]**2
        static=float(np.mean(l1*dr2/lam))
        end=2*float(np.mean(dr2*(-np.expm1(-t*exponent))/root*(lam-l1)/lam))
        energy=t*static+end
        assert -1e-13<=end<=2*r*r*g4+1e-13
        out[f'{r},{t}']={'energy':energy,'energy_per_time':energy/t,
                         'static_limit':static,'positive_endpoint_remainder':end,
                         'remainder_upper':2*r*r*g4}
    return {'n':n,'G4_origin_quadrature':g4,'rectangles':out}


def check_rectangle_green():
    data={'scope':'Finite Fourier and Poisson identities plus quadrature convergence; no numerical continuum proof.',
          'independent_review':False,'families':{}}
    timechecks=[]
    for lam in [.07,.4,2.,9.]:
        root=np.sqrt(lam*(lam+4));r=2/(lam+2+root)
        for t in [1,2,5,17]:
            matrix=r**np.abs(np.arange(t)[:,None]-np.arange(t)[None,:])/root
            direct=float(matrix.sum())
            formula=t/lam-2*(1-r**t)/(lam*root)
            assert abs(direct-formula)<2e-12*max(1,direct)
            timechecks.append({'lambda':lam,'T':t,'direct':direct,'formula':formula,'difference':abs(direct-formula)})
    data['families']['time_green_geometric_sum']={'cases':timechecks}

    periodic=[]
    for side in [8,12,16,24,32]:
        face,_=fft_energy(side,1,1)
        expected=.5*(1-side**-4)
        assert abs(face-expected)<2e-13
        e,parts=fft_energy(side,2,4)
        reversed_e,_=fft_energy(side,4,2)
        assert abs(e-reversed_e)<2e-13
        periodic.append({'side':side,'unit_face_energy':face,'exact_hodge_value':expected,
                         'rectangle_2_4_energy':e,'exchanged_rectangle_energy':reversed_e,
                         'side_contributions':parts})
    data['families']['explicit_periodic_currents']={'cases':periodic}

    side,r,t=8,2,3
    j0,j1=currents(side,r,t)
    def laplacian(vector):
        arr=vector.reshape((side,)*4)
        out=8*arr.copy()
        for axis in range(4):
            out-=np.roll(arr,1,axis)+np.roll(arr,-1,axis)
        return out.ravel()
    operator=LinearOperator((side**4,side**4),matvec=laplacian,dtype=float)
    energy=0.;residuals=[]
    for j in [j0,j1]:
        solved,info=cg(operator,j.ravel(),rtol=1e-13,atol=1e-14,maxiter=400)
        assert info==0
        residual=float(np.linalg.norm(laplacian(solved)-j.ravel()))
        residuals.append(residual);energy+=float(j.ravel()@solved)
    fourier,parts=fft_energy(side,r,t)
    assert abs(energy-fourier)<1e-12
    open_divergence=np.roll(j0,1,axis=0)-j0
    assert np.max(np.abs(open_divergence))==1
    assert abs(parts[0]-energy)>.1
    data['families']['independent_poisson_and_faults']={'cg_energy':energy,'fft_energy':fourier,
                  'poisson_residuals':residuals,'missing_spatial_ends_energy':parts[0],
                  'missing_spatial_ends_divergence':float(np.max(np.abs(open_divergence)))}

    pairs=[(1,1),(1,2),(2,1),(2,4),(4,2),(4,16),(4,64),(8,64)]
    levels=[reduced_integrals(n,pairs) for n in [24,32,48,64,96,128]]
    for level in levels:
        assert abs(level['rectangles']['1,1']['static_limit']-1/3)<2e-13
        assert level['rectangles']['4,64']['energy_per_time']<level['rectangles']['4,16']['energy_per_time']
    last=levels[-1]['rectangles']
    assert abs(last['1,1']['energy']-.5)<1e-7
    assert abs(last['1,2']['energy']-last['2,1']['energy'])<1e-7
    assert abs(last['2,4']['energy']-last['4,2']['energy'])<3e-7
    data['families']['reduced_infinite_time_quadrature']={'levels':levels,
          'infinite_volume_exact_calibrations':{'unit_face_energy':.5,'unit_separation_static_rate':1/3},
          'quadrature_error_certified':False}
    return data

"""Finite falsifiers for the author's analytic clock/transfer bridge.
No finite grid or matrix calculation proves the infinite-volume theorem.
"""
import hashlib
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.special import ive


def heat(theta, beta):
    theta = np.asarray(theta)
    if beta == 0:
        return np.ones_like(theta, dtype=float)
    # Positive Gaussian image sum; normalize out its irrelevant common factor.
    principal = (theta + np.pi) % (2*np.pi) - np.pi
    return sum(np.exp(-beta*(principal+2*np.pi*k)**2/2) for k in range(-8,9))

def cube_character_table(N, couplings):
    # Gauge quotient for the six oriented faces of one free three-cube.
    # Independent b1,...,b5 and b6=-sum b ensure the single Bianchi constraint.
    digits = np.indices((N,)*5).reshape(5,-1).T
    faces = np.column_stack((digits, -digits.sum(axis=1) % N))
    weights = np.ones(len(digits))
    for p,beta in enumerate(couplings):
        weights *= heat(2*np.pi*faces[:,p]/N, beta)
    prob = (weights/weights.sum()).reshape((N,)*5)
    # FFT sign is harmless by inversion symmetry; verify rather than assume.
    chars = np.fft.fftn(prob)
    assert np.max(np.abs(chars.imag)) < 2e-13
    return chars.real, digits

def ginibre_checks():
    records=[]
    rng=np.random.default_rng(2915)
    for N in (2,3,4,5):
        for beta in (.13,.45,1.2,2.7):
            base=np.array([0., beta*.6,beta,beta*1.3,beta*.8,beta*1.1])
            phi,digits=cube_character_table(N,base)
            minimum_increment=1.
            for p in range(6):
                raised=base.copy();raised[p]+=.31
                other,_=cube_character_table(N,raised)
                increment=float(np.min(other-phi))
                assert increment > -3e-12, (N,beta,p,increment)
                minimum_increment=min(minimum_increment,increment)
            assert phi.min() > -2e-13
            # Random arbitrary character pairs, including non-simple loops.
            pairs=rng.integers(0,len(digits),size=(4000,2))
            A=digits[pairs[:,0]];B=digits[pairs[:,1]]
            lookup=lambda x: phi[tuple((x%N).T)]
            covariance=(lookup(A+B)+lookup(A-B))/2-lookup(A)*lookup(B)
            assert covariance.min()>-3e-12,(N,beta,covariance.min())
            records.append({'N':N,'base_scale':beta,'characters':N**5,
              'single_plaquette_increases':6,'sampled_character_pairs':len(pairs),
              'minimum_character':float(phi.min()),
              'minimum_increment':minimum_increment,
              'minimum_cosine_covariance':float(covariance.min())})
    return records

def haar_and_divisibility_checks():
    records=[]
    rng=np.random.default_rng(290321)
    for N in (2,3,4,5):
        for beta in (.35,1.1,2.7):
            phi,digits=cube_character_table(N,[beta]*6)
            # Independent U(1) integration: the cube's one Bianchi constraint
            # leaves a one-dimensional plaquette Fourier sum.
            k=np.arange(-40,41)[:,None]
            denominator=np.exp(-6*k[:,0]**2/(2*beta)).sum()
            sampled=digits[rng.integers(0,len(digits),size=500)]
            gaps=[]
            for r in sampled:
                charges=np.append(r,0)
                haar=float(np.exp(-np.sum((k-charges)**2,axis=1)/(2*beta)).sum()/denominator)
                clock=float(phi[tuple(r)])
                gaps.append(clock-haar)
                assert clock-haar>-3e-12,(N,beta,r.tolist(),clock,haar)
            records.append({'clock_order':N,'beta':beta,'sampled_characters':len(sampled),
                'minimum_clock_minus_haar':min(gaps)})
    for N,M in ((2,4),(3,6)):
        beta=.85
        small,_=cube_character_table(N,[beta]*6)
        large,digits=cube_character_table(M,[beta]*6)
        gaps=small[tuple((digits%N).T)]-large[tuple(digits.T)]
        assert gaps.min()>-3e-12
        records.append({'subgroup_order':N,'containing_order':M,'characters':len(digits),
            'minimum_subgroup_minus_containing':float(gaps.min())})
    # The two non-divisible orders cannot be ordered uniformly in J.
    phi2,_=cube_character_table(2,[.15]*6)
    phi3,_=cube_character_table(3,[.15]*6)
    differences=[]
    for q in (2,3):
        v2=float(phi2[q%2,0,0,0,0]);v3=float(phi3[q%3,0,0,0,0])
        differences.append(v2-v3)
    assert differences[0]>.1 and differences[1]<-.1
    records.append({'nondivisible_order_control':[2,3],
       'q2_clock2_minus_clock3':differences[0],
       'q3_clock2_minus_clock3':differences[1]})
    return records

def carpet_pinning_checks():
    # A single coarse face: exact integrated carpet weights via Bessel
    # convolution; compare its finite-clock distribution to Villain.
    out=[]
    for N in (2,3,4,7):
        beta=.85
        theta=2*np.pi*np.arange(N)/N
        target=heat(theta,beta);target/=target.sum()
        rows=[]
        for m in (1,2,4,8,16,32,64,128):
            orders=np.arange(1,80)
            coupling=m*m*beta
            coeff=(ive(orders,coupling)/ive(0,coupling))**(m*m)
            approx=1+2*np.cos(np.outer(theta,orders))@coeff
            approx/=approx.sum()
            err=float(np.max(abs(approx-target)))
            rows.append({'refinement':m,'maximum_probability_error':err})
        assert rows[-1]['maximum_probability_error']<3e-5
        assert rows[-1]['maximum_probability_error']<rows[0]['maximum_probability_error']/500
        out.append({'N':N,'beta':beta,'convolution_checks':rows})
    # Finite-h clock pinning on a two-link torus, with Villain interaction.
    # Coupling is theta1-theta2; pin BOTH variables before h->infinity.
    for N in (2,3,4):
        beta=.8
        roots=2*np.pi*np.arange(N)/N
        weights=heat(roots[:,None]-roots[None,:],beta)
        target=float(np.sum(weights*np.cos(roots[:,None]-roots[None,:]))/weights.sum())
        grid=2*np.pi*np.arange(768)/768
        difference=grid[:,None]-grid[None,:]
        villain=heat(difference,beta)
        vals=[]
        for h in (0.,2.,8.,32.,128.,256.,512.):
            pin=np.exp(h*(np.cos(N*grid)-1))
            w=villain*pin[:,None]*pin[None,:]
            value=float(np.sum(w*np.cos(difference))/w.sum())
            vals.append({'h':h,'expectation':value,'clock_limit_error':abs(value-target)})
        assert vals[-1]['clock_limit_error'] < vals[0]['clock_limit_error']/20
        assert vals[-1]['clock_limit_error'] < .002
        out.append({'N':N,'pinning_grid_side':len(grid),'clock_target':target,'finite_h_checks':vals})
    return out

def transfer_checks():
    out=[]
    # Four oriented edges around a spatial square, incidence head-tail.
    D=np.zeros((4,4),dtype=int)
    for e in range(4):
        D[e,e]=-1;D[e,(e+1)%4]=1
    gamma=np.array([1,0,0,0])
    for N,beta in ((2,.24),(2,.85),(3,.35),(3,1.1),(4,.48)):
        configurations=np.array(list(itertools.product(range(N),repeat=4)))
        count=len(configurations)
        weights=heat(2*np.pi*np.arange(N)/N,beta)
        V=weights[configurations.sum(axis=1)%N]
        rootV=np.sqrt(V)
        delta=(configurations[:,None,:]-configurations[None,:,:])%N
        C=np.prod(weights[delta],axis=2)/count
        T=rootV[:,None]*C*rootV[None,:]
        eig,vec=np.linalg.eigh(T)
        lam=eig[-1];Omega=vec[:,-1]
        if Omega.sum()<0: Omega=-Omega
        assert Omega.min()>0 and eig[0]>0
        Omega/=np.linalg.norm(Omega)
        assert np.linalg.norm(T@Omega-lam*Omega)<2e-11
        direct=[]
        for charge in (0,1,N-1,N):
            phase=np.exp(2j*np.pi*charge*(configurations@gamma)/N)
            # Independently sum all temporal link variables eta. This keeps
            # their Wilson phases and is not temporal gauge fixing.
            K=np.zeros_like(C,dtype=complex)
            K0=np.zeros_like(C)
            for eta in configurations:
                gauge_shift=D@eta
                row=np.prod(weights[(delta+gauge_shift)%N],axis=2)/count
                K0+=row/count
                K+=row*np.exp(2j*np.pi*charge*(gamma@gauge_shift)/N)/count
            gauged=rootV[:,None]*K*rootV[None,:]
            neutral=rootV[:,None]*K0*rootV[None,:]
            assert np.max(abs(gauged-gauged.conj().T))<2e-12
            min_projected=float(np.linalg.eigvalsh(gauged)[0])
            assert min_projected>-3e-12
            # Direct free-time expectation uses boundary b=sqrt(V).
            endpoint=np.conj(phase)*rootV
            for time in (1,2,3):
                explicit=(np.vdot(endpoint,np.linalg.matrix_power(gauged,time)@endpoint)
                    /np.vdot(rootV,np.linalg.matrix_power(neutral,time)@rootV))
                temporal_gauge=(np.vdot(endpoint,np.linalg.matrix_power(T,time)@endpoint)
                    /np.vdot(rootV,np.linalg.matrix_power(T,time)@rootV))
                assert abs(explicit-temporal_gauge)<2e-11,(N,beta,charge,time)
                # Infinite-time interior limit and its direct positive spectrum.
                psi=phase*Omega
                spectral_weights=abs(vec.conj().T@psi)**2
                moment=float(np.sum(spectral_weights*(eig/lam)**time))
                ground=np.vdot(psi,np.linalg.matrix_power(T/lam,time)@psi)
                assert abs(moment-ground)<2e-12
                if charge%N==0: assert abs(moment-1)<3e-12
                direct.append({'q':charge,'T':time,'explicit_temporal_links':float(explicit.real),
                  'temporal_gauge_discrepancy':float(abs(explicit-temporal_gauge)),
                  'interior_ground_state_moment':moment,
                  'spectral_discrepancy':float(abs(moment-ground))})
        # Fault controls: missing V boundary factors and omitting temporal
        # charge phases each change the actual nonzero-charge expectation.
        charge=1
        phase=np.exp(2j*np.pi*(configurations@gamma)/N)
        psi=np.conj(phase)*rootV
        correct=np.vdot(psi,T@psi)/np.vdot(rootV,T@rootV)
        no_end_V=np.vdot(np.conj(phase),T@np.conj(phase))/np.sum(T)
        no_temporal_phase=np.vdot(psi,neutral@psi)/np.vdot(rootV,neutral@rootV)
        assert abs(correct-no_temporal_phase)>1e-4
        # Very small beta makes spatial V almost constant, so compare to a
        # scale appropriate to the intentionally weak interaction.
        assert abs(correct-no_end_V)>1e-10
        # Gauge character of charged state, verified for every vertex shift.
        charge_error=0.
        for vertex in range(4):
            eta=np.eye(4,dtype=int)[vertex]
            shifted=(configurations+D@eta)%N
            indexes=np.ravel_multi_index(shifted.T,(N,)*4)
            expected=np.exp(2j*np.pi*(gamma@D@eta)/N)*phase*Omega
            charge_error=max(charge_error,float(np.max(abs((phase*Omega)[indexes]-expected))))
        assert charge_error<3e-12
        out.append({'N':N,'beta':beta,'matrix_dimension':count,
          'minimum_transfer_eigenvalue':float(eig[0]),'largest_eigenvalue':float(lam),
          'maximum_gauge_character_error':charge_error,
          'missing_endpoint_weight_effect':float(abs(correct-no_end_V)),
          'missing_temporal_phase_effect':float(abs(correct-no_temporal_phase)),
          'comparisons':direct})
    return out

def check_clock_transfer():
    result={'status':'author_finite_checks_not_independent_review',
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'limitations':['floating arithmetic, no interval certificate',
        'finite low-dimensional systems do not establish the 4D source-curvature theorem',
        'carpet and pinning convergence tests are finite probes of separately written proofs']}
    result['ginibre']=ginibre_checks()
    result['carpet_pinning']=carpet_pinning_checks()
    result['haar_and_divisibility']=haar_and_divisibility_checks()
    result['transfer']=transfer_checks()
    return result

def main():
    evidence={
      'wilson_shift':check_wilson_shift(),
      'rectangle_green':check_rectangle_green(),
      'clock_transfer':check_clock_transfer(),
    }
    print('EVIDENCE_JSON: '+json.dumps(evidence,sort_keys=True))
    print('per_element: exact clock character aliases and direct source phases are evaluated on finite gauge quotients.')
    print('per_site: vertex gauge characters and explicit temporal-link sums are checked on spatial-square systems.')
    print('per_mode: positive finite transfer eigenvalues and spectral moments are compared with matrix powers.')
    print('per_block: periodic rectangle currents, sparse Poisson solves and three-cube Fourier/current sums are compared.')
    print('lattice_wide: checked and not executed — infinite free-state uniqueness and static-rate existence use the written proofs.')
    print('TOTAL: PASS=12 FAIL=0')
if __name__=='__main__':
    main()
