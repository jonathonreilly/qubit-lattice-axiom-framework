"""Finite challenges for logarithmic clock scaling, not a universal phase proof."""
AUDIT_TIMEOUT_SEC = 180
import itertools
import json
import math
import numpy as np
from scipy.special import logsumexp
from scipy.stats import binom


def close(a,b,tol=2e-10):
    assert np.allclose(a,b,atol=tol,rtol=tol),(np.asarray(a),np.asarray(b))


def form(L,k,dtype=float):
    return {I:np.zeros((L,)*4,dtype=dtype) for I in itertools.combinations(range(4),k)}


def d(f,L,k):
    out=form(L,k+1,np.result_type(*[v.dtype for v in f.values()]))
    for I in out:
        for n,j in enumerate(I):
            v=f[I[:n]+I[n+1:]];out[I]+=(-1)**n*(np.roll(v,-1,axis=j)-v)
    return out


def ds(f,L,k):
    out=form(L,k-1,np.result_type(*[v.dtype for v in f.values()]))
    for I,v in f.items():
        for n,j in enumerate(I):out[I[:n]+I[n+1:]]+=(-1)**n*(np.roll(v,1,axis=j)-v)
    return out


def green(f,L):
    grid=np.indices((L,)*4);lam=sum(4*np.sin(np.pi*grid[j]/L)**2 for j in range(4));inv=np.divide(1.,lam,out=np.zeros_like(lam),where=lam>1e-12)
    return {I:np.fft.ifftn(np.fft.fftn(v)*inv).real for I,v in f.items()}


def dot(f,g):return sum(float(np.sum(f[I]*g[I])) for I in f)


def theta(u,cut=12):return 1+2*sum(math.exp(-u*n*n) for n in range(1,cut+1))


def cochain_quantization():
    out=[]
    for L in [4,6]:
        V=L**4;cubes=[];faces=[];edge_supports=[]
        for base in itertools.product(range(0,L,2),repeat=4):
            cube=form(L,3,np.int64);cube[(0,1,2)][base]=1
            boundary=ds(cube,L,3)
            support={(I,tuple(x)) for I,v in boundary.items() for x in np.argwhere(v)}
            assert len(support)==6 and dot(boundary,boundary)==6
            assert not any(support&s for s in cubes);cubes.append(support)
            face=form(L,2,np.int64);face[(0,1)][base]=1
            edge=ds(face,L,2)
            e={(I,tuple(x)) for I,v in edge.items() for x in np.argwhere(v)}
            assert len(e)==4 and not any(e&s for s in edge_supports)
            edge_supports.append(e);faces.append(face)
        assert len(cubes)==V//16
        # Quantization checked from independent angle and integer image data.
        rng=np.random.default_rng(2026091412+L);N=8;beta=.7
        a={I:rng.integers(0,N,size=(L,)*4) for I in form(L,1)}
        curl=d(a,L,1);k={I:rng.integers(-2,3,size=(L,)*4) for I in curl}
        X={I:2*np.pi*np.sqrt(beta)*(curl[I]/N-k[I]) for I in curl}
        dx=d(X,L,2);dk=d(k,L,2)
        for I in dx:close(dx[I],-2*np.pi*np.sqrt(beta)*dk[I])
        # A closed but non-exact integer flux defeats dropping the harmonic test.
        flux=form(L,2,np.int64);flux[(0,1)][L-1,L-1,:,:]=1
        assert all(not v.any() for v in d(flux,L,2).values())
        h=form(L,2);h[(0,1)][:]=L**-2
        close(dot(flux,h),1);close(dot(h,h),1)
        # A non-exact arbitrary integer cochain need NOT have integral harmonic mean.
        spike=faces[0];close(dot(spike,h),L**-2)
        out.append(dict(L=L,cube_count=len(cubes),cube_squared_boundary_norm=6,harmonic_period=dot(flux,h),nonclosed_spike_harmonic=dot(spike,h)))
    return out


def image_atoms_and_cube_law():
    rows=[]
    for beta in [.03,.1,.4,1.]:
        q=math.exp(-2*math.pi**2*beta);bound=1/(1+q)
        maxmass=0
        for t in np.linspace(-2.5,2.5,61):
            n=np.arange(-40,41);logs=-2*np.pi**2*beta*(n-t)**2;p=np.exp(logs-logsumexp(logs));mode=int(n[np.argmax(p)])
            toward=mode+(1 if t>=mode else -1)
            ratio=math.exp(-2*math.pi**2*beta*((toward-t)**2-(mode-t)**2))
            assert ratio>=q*(1-2e-12)
            assert p.max()<=bound+2e-14;maxmass=max(maxmass,float(p.max()))
        rows.append(dict(beta=beta,max_atom=maxmass,uniform_atom_bound=bound,minimum_defect_probability=q/(1+q)))
    # Exact five-link gauge-fixed single cube: positive lift lattice consists
    # of six integers with oriented sum divisible by N. Convolution does not
    # enumerate the clock angles and follows a different calculation path.
    cube=[]
    for N,beta in [(2,.08),(3,.2),(4,.4),(5,.6)]:
        sigma=N*N/(4*np.pi**2*beta);R=25;n=np.arange(-R,R+1);weights=np.exp(-n*n/(2*sigma));conv=np.array([1.])
        for _ in range(6):conv=np.convolve(conv,weights)
        sums=np.arange(-6*R,6*R+1);mask=sums%N==0;Z=conv[mask].sum();pclosed=conv[6*R]/Z
        localupper=min(1.,2*math.exp(-math.pi**2*beta/3));atomupper=1/(1+math.exp(-2*math.pi**2*beta))
        assert 1-pclosed<=localupper+1e-13 and pclosed<=atomupper+1e-13
        # Independently compute the modular normalizer by root-of-unity filtering.
        modZ=sum((np.sum(weights*np.exp(2j*np.pi*j*n/N)))**6 for j in range(N))/N
        close(Z,modZ.real,2e-9);assert abs(modZ.imag)<2e-9
        # Independent finite clock angle sum uses beta directly, not sigma.
        angles=2*np.pi*np.arange(N)/N;image=np.arange(-25,26)
        phi=np.exp(-beta*(angles[:,None]-2*np.pi*image[None,:])**2/2).sum(axis=1)
        configurations=np.array(list(itertools.product(range(N),repeat=5)))
        last=(-configurations.sum(axis=1))%N
        clockZ=float((np.prod(phi[configurations],axis=1)*phi[last]).sum())
        close(Z,clockZ,2e-9)
        cube.append(dict(N=N,beta=beta,sigma=sigma,p_closed=float(pclosed),defect_upper=localupper,closed_upper=atomupper,omitted_one_axis_gaussian_bound=2*math.exp(-(R+1)**2/(2*sigma))/(1-math.exp(-(2*R+3)/(2*sigma)))))
    return dict(atoms=rows,single_cube=cube)


def integer_current_map_and_theta():
    L=4;rng=np.random.default_rng(12);rows=[]
    locations=[(0,0,0,0),(2,0,0,0),(0,2,0,0)]
    projected=[]
    for p in locations:
        f=form(L,2);f[(0,1)][p]=1;a=ds(f,L,2);w=d(green(a,L),L,1)
        for I,v in ds(w,L,2).items():close(v,a[I])
        projected.append(w)
    gram=np.array([[dot(w,v) for v in projected] for w in projected]);assert np.linalg.eigvalsh(gram).min()>0
    coefficient=np.array(list(itertools.product([-1,0,1],repeat=3)))
    energy=np.einsum('ni,ij,nj->n',coefficient,gram,coefficient)
    assert np.all(energy<=np.sum(coefficient**2,axis=1)+1e-12)
    for u in [.1,.5,1.]:
        finite=float(np.exp(-u*energy).sum());product=(1+2*math.exp(-u))**3
        assert finite>=product-1e-11;rows.append(dict(u=u,projected_finite_theta=finite,unprojected_product=product))
    # Source pairing compares face projection with integer edge-current map.
    for _ in range(5):
        f={I:rng.integers(-2,3,size=(L,)*4).astype(float) for I in form(L,2)}
        a=ds(f,L,2);w=d(green(a,L),L,1)
        source={I:rng.normal(size=(L,)*4) for I in f};psi=green(ds(source,L,2),L)
        close(dot(w,source),dot(a,psi));assert dot(a,a)<=16*dot(w,w)+1e-9
        B=max(float(abs(v).max()) for v in psi.values());assert abs(dot(a,psi))<=B*sum(float(abs(v).sum()) for v in a.values())+1e-8
    for u in [1.,1.2,2.,4.,10.]:
        close(theta(u),math.sqrt(math.pi/u)*theta(math.pi**2/u),2e-12)
        tail=theta(u)-1;assert tail<=2*math.exp(-u)/(1-math.exp(-3*u))+1e-15;assert tail<=3*math.exp(-u)+1e-15
    # Highest Fourier mode saturates ||d_1||=4 and the source potential bound.
    checker=(-1.)**np.indices((L,)*4).sum(axis=0);a=form(L,1);a[(0,)][:]=checker;a[(1,)][:]=-checker
    assert all(np.max(abs(v))<1e-12 for v in ds(a,L,1).values())
    w=d(green(a,L),L,1);close(dot(a,a),16*dot(w,w))
    sigma=2.;B=math.pi*math.sqrt(sigma)/32;psi={I:B*v for I,v in a.items()};h=d(psi,L,1)
    exponent=-2*math.pi**2*sigma*dot(w,w)+2*math.pi*math.sqrt(sigma)*dot(w,h)
    target=-math.pi**2*sigma*dot(a,a)/16
    close(exponent,target);assert target<0
    return dict(gram_eigenvalues=np.linalg.eigvalsh(gram).tolist(),projected_theta_lower_bounds=rows,source_pairing_cases=5,saturated_source_exponent=exponent,saturated_integer_bound=target)


def affine_source_relative():
    basis=np.array([[1.,0.],[0.,1.],[-1.,-1.]]);gram=basis.T@basis;dual=basis@np.linalg.inv(gram)
    Z=np.array(list(itertools.product(range(-20,21),repeat=2)));W=Z@dual.T;nonzero=np.any(Z!=0,axis=1)
    rows=[]
    for sigma in [.2,.5,1.,3.]:
        b=basis@np.array([.27,-.19]);h=np.array([.25,-.15,.1]);he=basis@np.linalg.solve(gram,basis.T@h);z=Z@basis.T+b
        weights=np.exp(-np.sum(z*z,axis=1)/(2*sigma));C=np.sum(weights*np.exp(1j*z@h/np.sqrt(sigma)))/weights.sum();G=math.exp(-he@he/2)
        tail=np.exp(-2*np.pi**2*sigma*np.sum(W*W,axis=1));phase=np.exp(2j*np.pi*W@b)
        numerator=np.sum(tail*np.exp(2*np.pi*np.sqrt(sigma)*(W@he))*phase);denom=np.sum(tail*phase)
        close(C/G,numerator/denom)
        eta=float(np.sum(np.exp(-np.pi**2*sigma*np.sum(W[nonzero]**2,axis=1))))
        radius=math.pi*math.sqrt(sigma)/8
        if np.linalg.norm(he)<=radius and eta<1:assert abs(C/G-1)<=2*eta/(1-eta)+1e-13
        rows.append(dict(sigma=sigma,source_norm=float(np.linalg.norm(he)),source_radius=radius,relative_characteristic=[float((C/G).real),float((C/G).imag)],theta_half_tail=eta))
    return rows


def loop_potential_refinement():
    rows=[]
    for m in [2,4,6,8]:
        L=4*m;S=form(L,2);S[(0,1)][:m,:m,0,0]=1;j=ds(S,L,2);psi=green(j,L);PeS=d(psi,L,1)
        beta=math.ceil(4*math.log(2*L**4));sigma=16*beta/math.pi**2
        energy=dot(PeS,PeS);close(energy,dot(j,psi));assert dot(j,j)==4*m
        assert energy>=dot(j,j)/16-1e-11
        potential=max(float(abs(v).max()) for v in psi.values());assert potential<1
        # Compare all scalar-kernel sites with a heat-kernel-shaped envelope.
        delta=form(L,0);delta[()][0,0,0,0]=1;G=green(delta,L)[()];close(float(G.mean()),0,1e-13);grid=np.indices((L,)*4);dist2=sum(np.minimum(grid[i],L-grid[i])**2 for i in range(4));envelope=1/(1+dist2)+L**-2
        ratio=float(np.max(abs(G)/envelope));assert ratio<1
        rows.append(dict(inverse_mesh=m,L=L,source_norm=math.sqrt(dot(S,S)),projected_source_norm=math.sqrt(energy),potential_sup=potential,source_l2_radius=math.pi*math.sqrt(sigma)/8,potential_radius=math.pi*math.sqrt(sigma)/32,green_envelope_ratio=ratio))
    # The q=N single-plaquette character is exactly one: it is outside(B).
    L=4;V=L**4;beta=math.ceil(4*math.log(2*V));N=8*beta;sigma=16*beta/math.pi**2
    S=form(L,2);S[(0,1)][0,0,0,0]=1;j=ds(S,L,2);psi=green(j,L)
    q=N;B=q/math.sqrt(beta)*max(float(abs(v).max()) for v in psi.values())
    radius=math.pi*math.sqrt(sigma)/32;G=math.exp(-q*q*dot(j,psi)/(2*beta))
    assert B>radius and G<1e-10
    assert all(abs(np.exp(2j*np.pi*q*r/N)-1)<1e-11 for r in range(N))
    return dict(refinements=rows,alias_control=dict(q=q,N=N,potential_sup=B,allowed_radius=radius,gaussian_characteristic=G,clock_characteristic=1))


def logarithmic_rates_and_moment_boundary():
    rows=[]
    for L in [4,8,16,64,256,1024]:
        V=L**4;beta=math.ceil(4*math.log(2*V));N=8*beta;sigma=N*N/(4*math.pi**2*beta);tau=math.pi**2*sigma/16;close(tau,beta)
        logtheta=math.log1p(2*sum(math.exp(-tau*n*n) for n in range(1,8)))
        eta=math.expm1(4*V*logtheta);eta_bound=math.expm1(12*V*math.exp(-beta));simple=math.expm1(.75/V**3)
        assert eta<=eta_bound*(1+1e-12) and eta_bound<=simple*(1+1e-12)
        bad=8*V*math.exp(-math.pi**2*beta/3)+12*math.exp(-2*math.pi**2*beta)
        logwrap=math.log(12*V)-math.pi**2*beta/2
        # Exponent of V in the all-wrap Holder bound; k=19 is not certified.
        exponents={k:(k+1)/2-math.pi**2 for k in [2,18,19,40]}
        assert exponents[18]<0<exponents[19]
        rows.append(dict(L=L,beta=beta,N=N,sigma=sigma,theta_tail_bound=eta_bound,defect_upper=bad,log_wrap_upper=logwrap))
    return dict(family=rows,principal_holder_exponents=exponents,score_all_moments_from_conditional_jensen=True)


def conditional_defect_count():
    eta=.07;n=8;successes=[np.linspace(eta,.5,n),np.linspace(.25,.9,n)];pmfs=[]
    for probabilities in successes:
        p=np.array([1.])
        for q in probabilities:p=np.convolve(p,[1-q,q])
        assert np.all(np.cumsum(p)<=binom.cdf(np.arange(n+1),n,eta)+1e-14);pmfs.append(p)
    mixture=.4*pmfs[0]+.6*pmfs[1];assert np.all(np.cumsum(mixture)<=binom.cdf(np.arange(n+1),n,eta)+1e-14)
    # Uniformly valid conditional domination does not imply unconditional independence.
    p0=.1;p1=.8;mean=(p0+p1)/2;joint=(p0*p0+p1*p1)/2
    assert joint>mean*mean
    beta=.1;q=math.exp(-2*math.pi**2*beta);m=1/(1+q)
    volume_upper=[m**(L**4//16) for L in [4,6,8,10]];assert all(b<a for a,b in zip(volume_upper,volume_upper[1:]))
    return dict(conditional_cases=2,mixture_mean=float(np.arange(n+1)@mixture),unconditional_covariance=joint-mean*mean,fixed_beta=beta,global_closed_upper=volume_upper)


def main():
    data=dict(cochain_quantization=cochain_quantization(),image_atoms_and_cube_law=image_atoms_and_cube_law(),integer_current_map_and_theta=integer_current_map_and_theta(),affine_source_relative=affine_source_relative(),loop_potential_refinement=loop_potential_refinement(),logarithmic_rates_and_moment_boundary=logarithmic_rates_and_moment_boundary(),conditional_defect_count=conditional_defect_count())
    print(json.dumps(data,indent=2))
    print('per_element: executed scalar image probabilities and shifted theta characteristics on explicit finite sums; their truncations are not universal tail certificates.')
    print('per_site: executed oriented cube boundaries, disjoint even-sublattice supports and integer harmonic periods on side-four and side-six four-tori.')
    print('per_mode: executed Fourier current potentials and Hodge energy identities on finite four-tori through side thirty-two, retaining the zero-mode subtraction.')
    print('per_block: executed single-cube lifted laws, loop refinements, logarithmic parameter members and conditional-mixture defect counts on declared finite domains.')
    print('lattice_wide: checked and not executed; logarithmic Maxwell and Wilson limits and global defect bounds depend on the written proof and await independent review.')

if __name__=='__main__':main()
