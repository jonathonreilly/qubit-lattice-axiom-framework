#!/usr/bin/env python3
"""Author finite checks, not an infinite-volume computation.

Independent routes: actual clock links and positive image sums; Gaussian
quadrature of the positive auxiliary current representation. Exact rational
cochains challenge the intervening identities. Only NumPy/SciPy/SymPy.
"""
import itertools as it
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.special import roots_hermitenorm


def cube3():
    cells = []
    for degree in range(4):
        seq = []
        for dirs in it.combinations(range(3), degree):
            for base in it.product(range(2), repeat=3):
                if all(base[d] == 0 for d in dirs):
                    seq.append((base, dirs))
        cells.append(seq)
    ds = []
    for degree in range(3):
        lookup = {x: i for i, x in enumerate(cells[degree])}
        mat = sp.zeros(len(cells[degree + 1]), len(cells[degree]))
        for row, (base, dirs) in enumerate(cells[degree + 1]):
            for k, axis in enumerate(dirs):
                lower = tuple(d for d in dirs if d != axis)
                upper_base = list(base)
                upper_base[axis] += 1
                mat[row, lookup[(tuple(upper_base), lower)]] += (-1) ** k
                mat[row, lookup[(base, lower)]] -= (-1) ** k
        ds.append(mat)
    return cells, ds


def positive_theta(x, b, c, cutoff=12):
    period = 2 * np.pi / b
    reduced = np.remainder(x + period / 2, period) - period / 2
    vals = reduced[..., None] - period * np.arange(-cutoff, cutoff + 1)
    return np.sqrt(2 * np.pi) / (b * np.sqrt(c)) * np.exp(
        -vals**2 / (2 * c)
    ).sum(axis=-1)


def clock_data(cells, D, beta, N, cutoff):
    # A genuine spanning-tree gauge of the cube, independent of the face
    # coordinates used to enumerate auxiliary conserved currents.
    vertices = cells[0]
    parent = list(range(len(vertices)))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    vertex_lookup = {b: i for i, (b, _) in enumerate(vertices)}
    chords = []
    for k, (base, (axis,)) in enumerate(cells[1]):
        other = list(base)
        other[axis] += 1
        i, j = root(vertex_lookup[base]), root(vertex_lookup[tuple(other)])
        if i == j:
            chords.append(k)
        else:
            parent[i] = j
    assert len(chords) == 5
    angles = np.zeros((N**5, len(cells[1])))
    angles[:, chords] = np.array(list(it.product(range(N), repeat=5))) * (2*np.pi/N)
    curvature = angles @ D.T
    images = np.arange(-cutoff, cutoff+1)
    X = np.sqrt(beta) * (curvature[..., None] - 2*np.pi*images)
    weights = np.exp(-X**2 / 2)
    localZ = weights.sum(axis=-1)
    conditional = weights / localZ[..., None]
    law = localZ.prod(axis=1)
    law /= law.sum()
    means = (conditional*X).sum(axis=-1)
    centered = X-means[..., None]
    var = (conditional*centered**2).sum(axis=-1)
    third = (conditional*centered**3).sum(axis=-1)
    fourth_cumulant = (conditional*centered**4).sum(axis=-1)-3*var**2
    covariance = np.einsum('n,ni,nj->ij', law, means, means)
    covariance += np.diag(law @ var)
    mean = law @ means
    covariance -= np.outer(mean, mean)

    def char(h):
        factors = (conditional*np.exp(1j*X*h[None,:,None])).sum(axis=-1)
        return law @ factors.prod(axis=1)

    def moments(v):
        m = means @ v
        v2 = var @ (v**2)
        k3 = third @ (v**3)
        k4 = fourth_cumulant @ (v**4)
        raw = [1., law@m, law@(m*m+v2), law@(m**3+3*m*v2+k3),
               law@(m**4+6*m*m*v2+3*v2*v2+4*m*k3+k4)]
        return np.array(raw)
    return char, moments, covariance, N**5


def aux_data(B, P, R, beta, N, cutoff, order):
    b = 2*np.pi*np.sqrt(beta)
    g = N/np.sqrt(beta)
    c = 1/32
    A0 = 1/6-c
    T = 1/(1-6*c)
    eta, quadrature = roots_hermitenorm(order)
    eta = eta*np.sqrt(A0)
    quadrature = quadrature/np.sqrt(2*np.pi)
    # Any five cube faces form a primitive integral cycle basis under D*.
    S = np.zeros(((2*cutoff+1)**5, 6))
    S[:, :5] = np.array(list(it.product(range(-cutoff, cutoff+1), repeat=5)))
    PS = S @ P
    energies = np.einsum('ni,ni->n', PS, PS)
    weights = np.exp(-g*g*energies/2)
    residue = np.remainder(np.rint(S@B).astype(int), 6)
    theta = positive_theta(eta[None,:]-g*np.arange(6)[:,None]/6, b, c)
    H0 = theta@quadrature
    J0 = np.bincount(residue, weights, minlength=6)
    norm = J0@H0
    jvec = -g*PS
    bvec = -T*B
    H1 = theta@(quadrature*eta)
    H2 = theta@(quadrature*eta**2)
    J1 = np.array([np.bincount(residue, weights*jvec[:,k], minlength=6)
                   for k in range(6)]).T
    mean = (J1.T@H0+bvec*(J0@H1))/norm
    covariance = np.zeros((6,6))
    for i in range(6):
        for j in range(6):
            Jij = np.bincount(residue, weights*jvec[:,i]*jvec[:,j], minlength=6)
            covariance[i,j] = (Jij@H0 + bvec[i]*(J1[:,j]@H1)
                                + bvec[j]*(J1[:,i]@H1)
                                + bvec[i]*bvec[j]*(J0@H2))/norm-mean[i]*mean[j]

    def char(h):
        Jh = np.bincount(residue, weights*np.exp(jvec@h), minlength=6)
        Hh = theta@(quadrature*np.exp((bvec@h)*eta))
        return np.exp(-h@R@h/2)*(Jh@Hh)/norm

    def moments(v):
        out = []
        jv = jvec@v
        bv = bvec@v
        for n in range(5):
            total = 0.
            for k in range(n+1):
                Jk = np.bincount(residue, weights*jv**k, minlength=6)
                Hnk = theta@(quadrature*(bv*eta)**(n-k))
                total += math.comb(n,k)*(Jk@Hnk)
            out.append(total/norm)
        return np.array(out)
    return char, moments, covariance, norm


def fourth_cumulant(raw):
    _, m1, m2, m3, m4 = raw
    return m4-4*m1*m3-3*m2*m2+12*m1*m1*m2-6*m1**4


def dual_lattice_data(B, beta, N, cutoff):
    # L_N=N Z^6+B* Z on the free three-cube. The coefficient of B*
    # is reduced modulo N, giving a unique integer parametrization.
    m=np.array(list(it.product(range(-cutoff,cutoff+1),repeat=6)),dtype=float)
    Z=np.concatenate([(N*m+k*B)/np.sqrt(beta) for k in range(N)])
    weights=np.exp(-np.einsum('ni,ni->n',Z,Z)/2)
    weights/=weights.sum()
    mean=weights@Z
    covariance=np.einsum('n,ni,nj->ij',weights,Z,Z)-np.outer(mean,mean)
    def mgf(h):
        return weights@np.exp(Z@h)
    def k4(v):
        scalar=Z@v
        raw=np.array([weights@(scalar**k) for k in range(5)])
        return fourth_cumulant(raw)
    return mgf,covariance,k4


def exact_and_regulator():
    cells, (d0,D,B) = cube3()
    assert D*d0 == sp.zeros(6,8) and B*D == sp.zeros(1,12)
    assert D.rank() == 5 and (D.T[:, :5]).rank() == 5
    # Its primitive index is one: the omitted face can be eliminated from
    # any filling using the cube boundary whose six coefficients are +/-1.
    assert all(abs(x)==1 for x in B)
    P = sp.eye(6)-B.T*B/6
    c = sp.Rational(1,32)
    A0 = sp.Rational(1,6)-c
    T = 1/(1-6*c)
    R = sp.eye(6)+c*B.T*T*B
    assert R == (sp.eye(6)-c*B.T*B).inv()
    assert B.T*T*A0*T*B == R-P
    assert R*P == P and A0*T == sp.Rational(1,6)
    S = sp.Matrix([1,0,-1,2,0,0])
    U = 3*B.T
    assert D.T*U == sp.zeros(12,1)
    assert P*(S+U) == P*S
    assert (B*U)[0]/6 == 3
    # Evaluate the completed-square exponent and the maximizing point
    # by different scalar formulas for several actual cube fillings.
    records = []
    for entries in ([1,0,0,0,0,0], [1,-1,2,0,1,0], list(B)):
        S = sp.Matrix(entries)
        E = (S.T*P*S)[0]
        area = (S.T*R*S)[0]
        a = (T*B*S)[0]
        uq = a*a*A0
        assert area == E+uq
        for k in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(9,10)]:
            g = sp.Rational(3)
            eta = g*A0*a/k
            direct = -g*g*area/2+g*a*eta-k*eta**2/(2*A0)
            predicted = g*g*((1/k-1)*uq-E)/2
            assert sp.simplify(direct-predicted)==0
            records.append({'E':str(E),'U':str(uq),'kappa':str(k),
                            'exponent_without_half_factor':str(predicted)})
    return cells, D, B, P, R, records


def planar_fourier_check():
    # Discretization only, with periodic zero mode omitted. Not an
    # enclosure of the infinite Green integral or a free-boundary check.
    rows=[]
    for M in [24,32,48]:
        p=2*np.pi*np.arange(M)/M
        q=4*np.sin(p/2)**2
        s=(q[:,None]+q[None,:]).reshape(-1)
        # Sum the two transverse momenta; at zero/zero use zero.
        kernel=np.zeros_like(s)
        for start in range(0,len(s),128):
            top=s[start:start+128,None]
            den=top+s[None,:]
            kernel[start:start+128]=np.divide(top,den,out=np.zeros_like(den),
                                             where=den>0).mean(axis=1)
        kernel=kernel.reshape(M,M)
        for L in [1,2,4,8,12]:
            geometric=np.exp(1j*p[:,None]*np.arange(L)[None,:]).sum(axis=1)
            amp=abs(geometric)**2
            E=float((kernel*amp[:,None]*amp[None,:]).mean())
            if L==1:
                assert abs(E-(1-M**-4)/2)<2e-14
            assert E <= math.sqrt(3)*math.pi*L/2+1e-10
            rows.append({'grid':M,'side':L,'energy_sample':E,'area':L*L,
                         'proved_infinite_upper':math.sqrt(3)*math.pi*L/2})
    return rows


def main():
    cells,D,B,P,R,regulator=exact_and_regulator()
    Dn=np.array(D,dtype=float)
    Bn=np.array(B,dtype=float).ravel()
    Pn=np.array(P,dtype=float)
    Rn=np.array(R,dtype=float)
    rng=np.random.default_rng(621509)
    directions=[Pn[:,0], (np.eye(6)-Pn)[:,0], rng.normal(size=6)]
    directions=[v/np.linalg.norm(v) for v in directions]
    sources=[s*v for v in directions for s in [.2,.55,1.1]]
    cases=[]
    for beta,N in [(.25,2),(.5,3),(.8,4)]:
        dchar,dmom,dcov,count=clock_data(cells,Dn,beta,N,10)
        dchar8,_,_,_=clock_data(cells,Dn,beta,N,8)
        achar,amom,acov,norm=aux_data(Bn,Pn,Rn,beta,N,4,160)
        achar3,amom3,acov3,_=aux_data(Bn,Pn,Rn,beta,N,3,120)
        srcerr=max(abs(dchar(h)-achar(h)) for h in sources)
        srccut=max(abs(achar(h)-achar3(h)) for h in sources)
        imgcut=max(abs(dchar(h)-dchar8(h)) for h in sources)
        coverr=float(abs(dcov-(Rn-acov)).max())
        moments=[]
        for v in directions:
            dx=dmom(v);dy=amom(v)
            kx=fourth_cumulant(dx);ky=fourth_cumulant(dy)
            moments.append({'X_variance':float(dx[2]-dx[1]**2),
                            'Y_variance':float(dy[2]-dy[1]**2),
                            'X_fourth_cumulant':float(kx),
                            'Y_fourth_cumulant':float(ky),
                            'fourth_gap':float(abs(kx-ky))})
        case={'beta':beta,'N':N,'actual_clock_configurations':count,
              'source_error':float(srcerr),'aux_cutoff_comparison':float(srccut),
              'image_cutoff_comparison':float(imgcut),'covariance_error':coverr,
              'aux_covariance_cutoff_gap':float(abs(acov-acov3).max()),
              'aux_normalization':float(norm),'directions':moments}
        wrong_prefactor=max(abs(achar(h)*(np.exp(h@(Rn-Pn)@h/2)-1))
                            for h in sources)
        case['rejected_prefactor_P_gap']=float(wrong_prefactor)
        case['rejected_prefactor_I_covariance_gap']=float(abs(dcov-(np.eye(6)-acov)).max())
        assert wrong_prefactor>1e-3
        print(json.dumps(case),flush=True)
        assert srcerr<2e-10 and coverr<2e-10
        assert max(x['fourth_gap'] for x in moments)<2e-9
        assert srccut<2e-9 and imgcut<1e-14
        dual_mgf,dual_cov,dual_k4=dual_lattice_data(Bn,beta,N,3)
        dual_mgf2,dual_cov2,_=dual_lattice_data(Bn,beta,N,2)
        Cnoise=Rn-np.eye(6)
        K=np.linalg.inv(Rn)
        noise_identity_error=float(abs(acov-(dual_cov+Cnoise)).max())
        poisson_error=max(abs(dchar(h)-np.exp(-h@h/2)*dual_mgf(-h)) for h in sources)
        dual_cutoff=max(abs(dual_mgf(h)-dual_mgf2(h)) for h in sources)
        fourth_noise_error=max(abs(dual_k4(v)-fourth_cumulant(amom(v)))
                               for v in directions)
        error_cov=(K-np.eye(6))@dual_cov@(K-np.eye(6))+K@Cnoise@K
        coupling_margin=float(np.linalg.eigvalsh(np.eye(6)-K-error_cov).min())
        case['dual_lattice_source_error']=float(poisson_error)
        case['dual_lattice_cutoff_gap']=float(dual_cutoff)
        case['independent_noise_covariance_error']=noise_identity_error
        case['independent_noise_fourth_cumulant_error']=float(fourth_noise_error)
        case['smoothing_coupling_matrix_margin']=coupling_margin
        assert noise_identity_error<2e-10 and poisson_error<2e-10
        assert fourth_noise_error<2e-9 and dual_cutoff<2e-9
        assert coupling_margin>-2e-14
        cases.append(case)
    # A real-space theta sum checks the integer-filling periodicity
    # separately from the rational phase argument.
    beta=.5
    b=2*np.pi*np.sqrt(beta)
    eta=np.linspace(-1.7,2.1,19)
    filling_gaps=[]
    for N in [3,3.5]:
        g=N/np.sqrt(beta)
        gap=float(abs(positive_theta(eta,b,1/32)
                      -positive_theta(eta-3*g,b,1/32)).max())
        filling_gaps.append({'N':N,'theta_shift_gap':gap})
        if N==3: assert gap<1e-13
        else: assert gap>.1
    # Exact normalized non-Gaussian probability with the scalar source
    # self-duality relation. No numerical fit to a gauge field.
    z,t=sp.symbols('z t',real=True)
    He4=z**4-6*z*z+3
    eps=sp.Rational(1,16)
    assert sp.expand(He4+6-(z*z-3)**2)==0
    M=sp.exp(t*t/4)*(1+eps*t**4/4)
    chi=sp.exp(-t*t/4)*(1+eps*t**4/4)
    assert sp.simplify(chi-sp.exp(-t*t/2)*M)==0
    k4=sp.diff(sp.log(M),t,4).subs(t,0)
    assert k4==sp.Rational(3,8)
    result={'status':'finite_author_checks_only','cube_cases':cases,
            'integer_filling_periodicity_controls':filling_gaps,
            'exact_regulator_checks':regulator,
            'planar_fourier_discretizations':planar_fourier_check(),
            'non_gaussian_self_duality_fourth_cumulant':str(k4),
            'limits':['no interval-certified quadrature or image tails',
                      'Fourier samples do not execute an infinite lattice proof',
                      'free-box exhaustion is an analytic argument',
                      'no full coupled-field summation or independent review']}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print('per_element: exact cochain, resolvent and filling-change identities checked')
    print('per_site: actual cube clock/image law compared with a positive auxiliary integral')
    print('per_mode: fifteen finite Fourier discretizations challenge the planar estimate')
    print('per_block: source, covariance and fourth-cumulant identities checked on three cubes')
    print('lattice_wide: uniform regulator failure uses a written planar/exhaustion proof; not executed')


if __name__=='__main__':
    main()
