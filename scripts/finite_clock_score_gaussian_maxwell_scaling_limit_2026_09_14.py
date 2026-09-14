"""Finite challenges of the conditional finite-clock Gaussian scaling proof.

No repository scientific input is read. The arbitrary-volume affine-curl
bound is an explicit unreviewed premise of the note, not verified here.
The three-face incidence model below checks algebra, not a four-torus phase.
"""
AUDIT_TIMEOUT_SEC = 180

import itertools
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import logsumexp


def close(a,b,tol=2e-10):
    assert np.allclose(a,b,atol=tol,rtol=tol), (np.asarray(a),np.asarray(b))


def discrete_moments(points,sigma):
    points=np.asarray(points,dtype=float)
    logw=-np.sum(points*points,axis=1)/(2*sigma)
    logZ=logsumexp(logw)
    weights=np.exp(logw-logZ)
    mean=weights@points
    cov=(points.T*weights)@points-np.outer(mean,mean)
    return logZ,weights,mean,cov


def clock_lift_and_score():
    # Integer incidence of a three-edge cycle, not a four-dimensional torus.
    d=np.array([[1,-1,0],[0,1,-1],[-1,0,1]])
    records=[]
    for N,beta in [(2,.18),(4,.65),(6,1.4)]:
        sigma=N*N/(4*np.pi*np.pi*beta)
        clocks=np.array(list(itertools.product(range(N),repeat=3)))
        da=clocks@d.T
        residues=da%N
        counts={tuple(x):0 for x in residues}
        for x in residues:counts[tuple(x)]+=1
        expected={x for x in itertools.product(range(N),repeat=3) if sum(x)%N==0}
        assert set(counts)==expected
        assert set(counts.values())=={N}
        # Each image sum includes all integers within six of its local center.
        m=np.arange(-6,7)
        u=2*np.pi*da/N
        displacement=u[:,:,None]-2*np.pi*m[None,None,:]
        image=np.exp(-beta*displacement**2/2)
        localZ=image.sum(axis=2)
        conditional=image/localZ[:,:,None]
        x=math.sqrt(beta)*displacement
        mean=(conditional*x).sum(axis=2)
        var=(conditional*x*x).sum(axis=2)-mean*mean
        config=localZ.prod(axis=1);total=config.sum();config/=total
        # The independent Fourier series computes the physical score.
        n=np.arange(-20,21)
        fourier=np.exp(-n*n/(2*beta))
        phi=np.cos(u[:,:,None]*n)@fourier
        derivative=(-np.sin(u[:,:,None]*n)*n)@fourier
        score=derivative/phi
        Y=-score/math.sqrt(beta)
        close(Y,mean)
        if N==2:close(Y,0)
        # Enumerate the full-rank image lattice through its congruence.
        cutoff=math.ceil(math.sqrt(2*sigma*50))+2
        raw=np.array(list(itertools.product(range(-cutoff,cutoff+1),repeat=3)))
        z=raw[raw.sum(axis=1)%N==0]
        logZ,w,zmean,cov=discrete_moments(z,sigma)
        close(total,N*math.exp(logZ))
        close(zmean,0)
        CX=cov/sigma
        from_conditioning=(mean.T*config)@mean+np.diag(config@var)
        close(CX,from_conditioning)
        h=np.array([.7,-.9,.4])
        CY=(Y.T*config)@Y
        noise=float(h@(CX-CY)@h)
        independent_noise=float(config@(var@(h*h)))
        close(noise,independent_noise)
        epsilon=(8*np.pi*np.pi*beta+16)*math.exp(-np.pi*np.pi*beta/2)
        assert noise<=epsilon*float(h@h)+1e-12
        # Reconstruct primal L_N={n: all coordinates congruent mod N}.
        cut_n=math.ceil(math.sqrt(2*beta*50))+2
        primal=np.array(list(itertools.product(range(-cut_n,cut_n+1),repeat=3)))
        primal=primal[np.all((primal-primal[:,[0]])%N==0,axis=1)]
        _,_,_,cn=discrete_moments(primal,beta)
        close(cn/beta+CX,np.eye(3))
        records.append(dict(N=N,beta=beta,beta_d=sigma,
                            constant_lift_fiber=N,lattice_points=len(z),
                            source_noise=noise,score_variance=float(h@CY@h),
                            covariance_duality_error=float(abs(cn/beta+CX-np.eye(3)).max())))
    return records


def centered_theta_and_affine_control():
    basis=np.array([[2.,1.],[0.,3.]])
    grid=np.array(list(itertools.product(range(-15,16),repeat=2)))
    z=grid@basis.T;sigma=1.7
    logZ,w,mean,cov=discrete_moments(z,sigma)
    close(mean,0)
    rng=np.random.default_rng(20260914)
    ratios=[]
    for h in rng.normal(size=(25,2)):
        logmgf=logsumexp(-np.sum(z*z,axis=1)/(2*sigma)+z@h/math.sqrt(sigma))-logZ
        shifted=logsumexp(-np.sum((z-math.sqrt(sigma)*h)**2,axis=1)/(2*sigma))-logZ
        close(logmgf,float(h@h)/2+shifted)
        assert logmgf<=float(h@h)/2+2e-12
        ratios.append(math.exp(shifted))
    # This same lattice shifted halfway is NOT subject to a covariance cap.
    sigma_shift=.05
    odd=(2*np.arange(-10,11)+1).reshape(-1,1)
    _,w,mean,cov=discrete_moments(odd,sigma_shift)
    assert cov[0,0]>19*sigma_shift
    h=.1
    affine_logmgf=logsumexp(-odd[:,0]**2/(2*sigma_shift)
                            +h*(odd[:,0]-mean[0])/math.sqrt(sigma_shift))
    affine_logmgf-=logsumexp(-odd[:,0]**2/(2*sigma_shift))
    assert affine_logmgf>h*h/2
    return dict(centered_theta_ratios=ratios,affine_variance=float(cov[0,0]),
                affine_sigma=sigma_shift,affine_log_mgf=float(affine_logmgf))


def exact_plane_gaussian_approach():
    records=[];h=np.array([1.,-1.,0.])/math.sqrt(2)
    errors=[]
    for j in range(1,6):
        sigma=j/4;N=8*j
        cutoff=math.ceil(9*math.sqrt(sigma)+N/3)
        pairs=np.array(list(itertools.product(range(-cutoff,cutoff+1),repeat=2)))
        z=np.concatenate([np.column_stack((pairs,N*k-pairs.sum(axis=1))) for k in (-1,0,1)])
        logZ,w,mean,cov=discrete_moments(z,sigma)
        source=z@h/math.sqrt(sigma)
        logmgf=float(logsumexp(-np.sum(z*z,axis=1)/(2*sigma)+.8*source)-logZ)
        variance=float(w@(source*source))
        fourth=float(w@(source**4))
        error=abs(logmgf-.8**2/2)
        errors.append(error)
        assert logmgf<=.8**2/2+1e-12
        records.append(dict(beta_d=sigma,N=N,variance=variance,fourth=fourth,
                            log_mgf=logmgf,gaussian_log_mgf=.8**2/2))
    assert all(b<a for a,b in zip(errors,errors[1:]))
    assert errors[-1]<1e-5 and abs(records[-1]['fourth']-3)<1e-3
    # Rademacher has the same variance and a centered sub-Gaussian MGF,
    # but does not have the required lower squeeze or Gaussian fourth moment.
    rad=np.array([-1.,1.]);weights=np.array([.5,.5])
    close(weights@(rad*rad),1)
    assert weights@(rad**4)==1
    assert math.log(math.cosh(1))<.5
    return dict(three_face_lattice_sequence=records,rademacher_fourth=1)


def tilted_coset_total_covariance():
    N=3;sigma=2.;cutoff=17
    raw=np.array(list(itertools.product(range(-cutoff,cutoff+1),repeat=3)))
    raw=raw[raw.sum(axis=1)%N==0]
    labels=raw.sum(axis=1)//N;X=raw/math.sqrt(sigma)
    h=np.array([.7,-.5,.9]);source=X@h
    base=-np.sum(raw*raw,axis=1)/(2*sigma)
    Pe=np.eye(3)-np.ones((3,3))/3;records=[]
    for tilt in [-1.2,-.2,.9]:
        exponent=base+tilt*source;logZ=logsumexp(exponent)
        w=np.exp(exponent-logZ);mean=w@X
        cov=(X.T*w)@X-np.outer(mean,mean)
        within=np.zeros((3,3));mean_second=np.zeros((3,3));smallest=1.
        for label in np.unique(labels):
            mask=labels==label;mass=float(w[mask].sum())
            if mass<1e-16:continue
            conditional=w[mask]/mass;local=X[mask];cm=conditional@local
            cc=(local.T*conditional)@local-np.outer(cm,cm)
            within+=mass*cc
            mean_second+=mass*np.outer(cm,cm)
            smallest=min(smallest,float(np.linalg.eigvalsh(cc+.999*(np.eye(3)-Pe)).min()))
        between=mean_second-np.outer(mean,mean)
        close(cov,within+between)
        assert np.trace(between)>.5
        assert np.linalg.eigvalsh(cov-.998*Pe).min()>-1e-10
        assert smallest>.998
        eps=2e-4
        hessian=(logsumexp(base+(tilt+eps)*source)-2*logZ
                 +logsumexp(base+(tilt-eps)*source))/(eps*eps)
        gradient=(logsumexp(base+(tilt+eps)*source)
                  -logsumexp(base+(tilt-eps)*source))/(2*eps)
        close(gradient,float(h@mean),tol=1e-7)
        close(hessian,float(h@cov@h),tol=1e-7)
        records.append(dict(tilt=tilt,between_coset_covariance_trace=float(np.trace(between)),
                            source_gradient=float(gradient),direct_mean=float(h@mean),
                            source_hessian=float(hessian),direct_variance=float(h@cov@h)))
    return records


ORIENTATIONS=list(itertools.combinations(range(4),2))


def exterior_one(p):
    p=np.asarray(p)
    matrix=np.zeros((6,4),dtype=np.result_type(p,complex))
    for row,(mu,nu) in enumerate(ORIENTATIONS):
        matrix[row,nu]=p[mu];matrix[row,mu]=-p[nu]
    return matrix


def twoform_projection(p):
    D=exterior_one(p)
    return D@D.conj().T/float(np.vdot(p,p).real)


def midpoint_and_cell_average():
    L=6;ell=3.;a=ell/L
    modes=np.array([1,0,-1,1]);k=2*np.pi*modes/L;p=k/a
    q=np.exp(1j*k)-1
    xi=2*np.sin(k/2)
    edge_phase=np.diag(np.exp(1j*k/2))
    face_phase=np.diag([np.exp(1j*(k[mu]+k[nu])/2) for mu,nu in ORIENTATIONS])
    close(exterior_one(q)@edge_phase,face_phase@(1j*exterior_one(xi)))
    close(twoform_projection(q),face_phase@twoform_projection(xi)@face_phase.conj().T)
    v=np.array([1+1j,2,-1j,.3,-.7,.2j]);v/=np.linalg.norm(v)
    sinc=float(np.prod(np.sinc(k/(2*np.pi))))
    nodes,weights=np.polynomial.legendre.leggauss(12)
    direct_cell=1+0j
    for component in p:
        direct_cell*=a/2*np.sum(weights*np.exp(1j*component*a*nodes/2))
    close(direct_cell,a**4*sinc)
    grid=np.indices((L,)*4)
    source=np.empty((6,L,L,L,L),complex)
    for o,(mu,nu) in enumerate(ORIENTATIONS):
        phase=sum(k[c]*grid[c] for c in range(4))+(k[mu]+k[nu])/2
        source[o]=a*a/(ell*ell)*sinc*v[o]*np.exp(1j*phase)
    coeff=np.fft.fftn(source,axes=(1,2,3,4),norm='ortho')
    index=tuple(modes%L)
    selected=coeff[(slice(None),)+index]
    close(selected,sinc*face_phase@v)
    close(np.sum(abs(coeff)**2),sinc*sinc)
    close(source.reshape(6,-1).sum(axis=1),0)
    pair=float(np.vdot(selected,twoform_projection(q)@selected).real)
    close(pair,sinc*sinc*np.vdot(v,twoform_projection(xi)@v).real)
    assert sinc*sinc<=1
    errors=[];momentum=np.array([.7,1.2,-.8,.4])
    continuum=twoform_projection(momentum)
    for step in [.5,.25,.125,.0625]:
        lattice=twoform_projection(2*np.sin(step*momentum/2))
        error=float(np.linalg.norm(lattice-continuum))
        errors.append(error)
        assert error<step*step
    assert all(b<a/3.9 for a,b in zip(errors,errors[1:]))
    # The harmonic piece cannot be discarded for an arbitrary norm-one source.
    harmonic=np.full(6*L**4,1/math.sqrt(6*L**4))
    close(harmonic@harmonic,1)
    harmonic_local=1/L**4
    assert harmonic_local>0
    return dict(cell_average_norm=sinc*sinc,projected_pairing=pair,
                centered_symbol_errors=errors,harmonic_unit_source_norm=1,
                one_plaquette_harmonic_norm_squared=harmonic_local)


def cross_matrix(p):
    x,y,z=p
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0]],float)


def os_electric_magnetic_reconstruction():
    records=[]
    # Orientation order is 01,02,03,12,13,23; B=(23,-13,12).
    change=np.zeros((6,6));change[:3,:3]=np.eye(3)
    change[3,5]=1;change[4,4]=-1;change[5,3]=1
    for p in [np.array([.7,-.4,1.2]),np.array([0.,0.,2.]),np.array([1.,2.,-3.])]:
        r=float(np.linalg.norm(p));PT=np.eye(3)-np.outer(p,p)/(r*r);C=cross_matrix(p)
        close(C@C,-r*r*PT)
        for p0 in [.3,1.1,-.8]:
            full=change@twoform_projection(np.r_[p0,p])@change.T
            denominator=p0*p0+r*r
            expected=np.block([[(p0*p0*np.eye(3)+np.outer(p,p))/denominator,-p0*C/denominator],
                               [p0*C/denominator,r*r*PT/denominator]])
            close(full,expected)
            close(np.linalg.eigvalsh(full),[0,0,0,1,1,1])
        u=.73
        i0=quad(lambda k:1/(k*k+r*r),0,np.inf,weight='cos',wvar=u,epsabs=1e-12)[0]/np.pi
        i1=-1j*quad(lambda k:k/(k*k+r*r),0,np.inf,weight='sin',wvar=u,epsabs=1e-12)[0]/np.pi
        close(i0,math.exp(-r*u)/(2*r))
        close(i1,-1j*math.exp(-r*u)/2)
        # Subtract the EE contact term before integrating at u>0.
        noncontact=np.block([[-r*r*PT*i0,-C*i1],[C*i1,r*r*PT*i0]])
        reflection=np.diag([-1,-1,-1,1,1,1])
        kernel=reflection@noncontact
        M=-1j*C/r
        gram=np.block([[PT,M],[M,PT]])
        close(kernel,r/2*math.exp(-r*u)*gram)
        close(gram,gram.conj().T)
        T=np.column_stack((PT,M))
        close(gram,T.conj().T@T)
        eigen=np.linalg.eigvalsh(gram)
        close(eigen,[0,0,0,0,2,2])
        assert np.linalg.eigvalsh(noncontact[:3,:3]).min()<0
        # Removing cross blocks changes the physical mode count to four.
        uncoupled=np.block([[PT,np.zeros((3,3))],[np.zeros((3,3)),PT]])
        assert np.count_nonzero(np.linalg.eigvalsh(uncoupled)>1e-8)==4
        for t in [.1,.7,2.3]:
            spectral=math.exp(-t*r)
            close(-math.log(spectral)/t,r)
        records.append(dict(spatial_momentum=p.tolist(),gram_eigenvalues=eigen.tolist(),
                            reflected_kernel_error=float(abs(kernel-r/2*math.exp(-r*u)*gram).max())))
    return records


def bianchi_and_contact():
    p=np.array([.3,.7,-1.1,2.]);D=exterior_one(p);P=twoform_projection(p)
    triples=list(itertools.combinations(range(4),3));d2=np.zeros((4,6))
    for row,(a,b,c) in enumerate(triples):
        d2[row,ORIENTATIONS.index((b,c))]=p[a]
        d2[row,ORIENTATIONS.index((a,c))]=-p[b]
        d2[row,ORIENTATIONS.index((a,b))]=p[c]
    close(d2@D,0);close(d2@P,0)
    contact=D.conj().T@P@D
    close(contact,float(p@p)*np.eye(4)-np.outer(p,p))
    assert np.linalg.norm(contact)>1
    # Shared conditional noise would defeat (4.1), even with correct marginals.
    h=np.array([1.,1.,1.]);shared_variance=float(h.sum()**2)
    independent_variance=float(h@h)
    assert shared_variance==9 and independent_variance==3
    return dict(bianchi_error=float(abs(d2@P).max()),euclidean_divergence_covariance_norm=float(np.linalg.norm(contact)),
                shared_noise_variance=shared_variance,independent_noise_variance=independent_variance)


def tail_constants_and_scaling():
    # Independent numerical integration of the sub-Gaussian tail majorant.
    records=[]
    for beta in [.1,.8,2.,5.]:
        threshold=np.pi*math.sqrt(beta)
        integrated=4*(2*threshold**2*math.exp(-threshold**2/2)
                       +quad(lambda x:4*x*math.exp(-x*x/2),threshold,np.inf,epsabs=1e-13)[0])
        epsilon=(8*np.pi*np.pi*beta+16)*math.exp(-np.pi*np.pi*beta/2)
        close(integrated,epsilon)
        records.append(dict(beta=beta,noise_bound=epsilon))
    beta1=(107*math.log(3)+math.log(4))/(4*np.pi*np.pi)
    deltas=[]
    for sigma in [2000.,2100.,2200.]:
        a=sigma/384-beta1;q=math.exp(-2*np.pi*np.pi*a)
        S5=q*(1+26*q+66*q*q+26*q**3+q**4)/(1-q)**6
        S6=q*(1+57*q+302*q*q+302*q**3+57*q**4+q**5)/(1-q)**7
        delta=sigma*(8503056*S6+262144*S5)/(a*math.e)
        assert 0<delta<1e-3;deltas.append(delta)
    assert all(b<a for a,b in zip(deltas,deltas[1:]))
    sequence=[]
    for j in [2,10,100,1000]:
        beta=2000+j;N=8*beta;spacing=1/j;L=2*j*j
        dual=N*N/(4*np.pi*np.pi*beta)
        close(dual,16*beta/(np.pi*np.pi));close(spacing*L,2*j)
        assert L%2==0 and N%8==0 and dual>beta
        sequence.append(dict(j=j,beta=beta,N=N,beta_d=dual,physical_side=spacing*L))
    return dict(tail_integrals=records,affine_input_delta_values=deltas,supplied_scaling_sequence=sequence)


def main():
    families=[('positive_clock_lift_score_and_duality',clock_lift_and_score),
              ('centered_theta_and_shifted_counterexample',centered_theta_and_affine_control),
              ('finite_exact_plane_gaussian_approach',exact_plane_gaussian_approach),
              ('tilted_coset_total_covariance',tilted_coset_total_covariance),
              ('midpoint_symbol_and_cell_average',midpoint_and_cell_average),
              ('electric_magnetic_os_reconstruction',os_electric_magnetic_reconstruction),
              ('bianchi_contact_and_conditional_noise',bianchi_and_contact),
              ('tail_constants_and_explicit_scaling',tail_constants_and_scaling)]
    records={}
    for name,check in families:
        records[name]=check();print('finite_check_completed: '+name,flush=True)
    print(json.dumps(records,indent=2,sort_keys=True))
    print('per_element: scalar Gaussian lifts, score derivatives, centered theta sources and tail integrals are checked with explicit finite cutoffs.')
    print('per_site: the three-face incidence toy checks clock fibers and conditional plaquette noise; it is not a four-dimensional phase computation.')
    print('per_mode: midpoint Fourier phases, continuum projector symbols, electric-magnetic contact signs and the rank-two reflected Gram matrix are checked.')
    print('per_block: composite orders two, four and six, a finite exact-plane lattice sequence and an even side-six Fourier block are checked personally.')
    print('lattice_wide: checked and not executed — arbitrary-volume affine covariance, distributional convergence and full Fock reconstruction rest on the stated conditional derivation.')
    print(f'TOTAL: PASS={len(families)} FAIL=0')
    print('scope: finite mathematical challenges only; the all-shift input and the new continuum theorem await independent proof review and formal audit.')


if __name__=='__main__':main()
