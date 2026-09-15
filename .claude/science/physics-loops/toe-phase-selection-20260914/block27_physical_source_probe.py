#!/usr/bin/env python3
"""Direct clock/image versus coupled-defect sources and full Hodge pair checks."""
import itertools
import json
import math

import numpy as np


def cube():
    dimension = 3
    cells = {}
    for p in range(4):
        cells[p] = [(x, ori) for ori in itertools.combinations(range(dimension), p)
                    for x in itertools.product(range(2), repeat=dimension)
                    if all(x[j] == 0 for j in ori)]
    incidence = {}
    for p in [0, 1, 2]:
        lookup = {c:i for i,c in enumerate(cells[p])}
        mat = np.zeros((len(cells[p+1]),len(cells[p])))
        for row,(x,ori) in enumerate(cells[p+1]):
            for pos,j in enumerate(ori):
                sub = tuple(i for i in ori if i != j)
                xp = list(x)
                xp[j] += 1
                mat[row,lookup[(tuple(xp),sub)]] += (-1)**pos
                mat[row,lookup[(x,sub)]] -= (-1)**pos
        incidence[p]=mat
    parent = list(range(len(cells[0])))
    def root(i):
        while parent[i] != i:
            i=parent[i]
        return i
    chords=[]
    for edge,row in enumerate(incidence[0]):
        left,right=np.flatnonzero(row)
        a,b=root(left),root(right)
        if a == b:
            chords.append(edge)
        else:
            parent[a]=b
    D=incidence[1][:,chords]
    B=incidence[2][0]
    assert D.shape == (6,5) and np.max(abs(B@D)) == 0
    assert np.linalg.matrix_rank(D) == 5
    return D,B


def physical_sources():
    D,B=cube()
    Qinv=np.linalg.inv(D.T@D)
    P=D@Qinv@D.T
    n0=np.zeros(6)
    n0[0]=B[0]
    y0=B/6
    assert np.max(abs((np.eye(6)-P)@n0-y0)) < 1e-14
    integer=np.array(list(itertools.product(range(-5,6),repeat=5)),dtype=float)
    q=np.arange(-6,7,dtype=float)
    images=np.arange(-6,7,dtype=float)
    tests=[np.array([.23,-.31,.17,.4,-.22,.13]),
           np.array([-.7,.2,.33,-.1,.42,.61])]
    rows=[]
    for N,beta in [(2,.8),(3,1.1),(4,1.1)]:
        angles=2*math.pi/N*np.array(list(itertools.product(range(N),repeat=5)))
        raw=angles@D.T
        F=raw[:,:,None]-2*math.pi*images
        image_weights=np.exp(-beta*F**2/2)
        direct_norm=np.prod(np.sum(image_weights,axis=2),axis=1).sum()
        electric=N*(integer@Qinv@D.T)
        electric_weight=np.exp(-N*N*np.einsum('ni,ij,nj->n',integer,Qinv,integer)/(2*beta))
        magnetic_weight=np.exp(-2*math.pi**2*beta*q*q/6)
        phase=2*math.pi*N*(integer@Qinv@D.T@n0)
        weight=(electric_weight[:,None]*magnetic_weight[None,:]
                *np.exp(1j*phase[:,None]*q[None,:]))
        coupled_norm=weight.sum()
        assert abs(coupled_norm.imag) < 1e-13 and coupled_norm.real > 0
        for h in tests:
            local=np.sum(image_weights*np.exp(1j*math.sqrt(beta)*F*h[None,:,None]),axis=2)
            direct=np.prod(local,axis=1).sum()/direct_norm
            ue=electric@h/math.sqrt(beta)
            vm=2*math.pi*math.sqrt(beta)*q*(y0@h)
            factor=np.exp(-h@P@h/2)
            coupled=factor*np.sum(weight*np.exp(-ue[:,None]-1j*vm[None,:]))/coupled_norm
            both_reversed=factor*np.sum(weight*np.exp(ue[:,None]+1j*vm[None,:]))/coupled_norm
            wrong_relative=factor*np.sum(weight*np.exp(ue[:,None]-1j*vm[None,:]))/coupled_norm
            omitted_electric=factor*np.sum(weight*np.exp(-1j*vm[None,:]))/coupled_norm
            error=float(abs(direct-coupled))
            fault=float(abs(direct-wrong_relative))
            omit=float(abs(direct-omitted_electric))
            assert error < 3e-12 and abs(direct-both_reversed) < 3e-12
            assert omit > 1e-6
            if N % 3:
                assert fault > 1e-6
            else:
                # On this particular three-cube, I-B*B/3 preserves M_N
                # when3 divides N. Relative-source reversal is then a true
                # symmetry and cannot be used as a rejected fault.
                assert fault < 3e-12
            rows.append(dict(N=N,beta=beta,direct_characteristic=[direct.real,direct.imag],
                             coupled_error=error,both_source_reversal_error=float(abs(direct-both_reversed)),
                             single_source_sign_change_residual=fault,
                             sign_change_status=('rejected' if N%3 else 'arithmetic_symmetry_control'),
                             omitted_electric_source_fault=omit))
    # Independently check the lattice reflection using exact integer
    # arithmetic for a finite generating family, not the source sum.
    lattice_reflections=[]
    for N in [3,6]:
        twice_generators=np.concatenate([np.rint(D).astype(int).T,N*np.eye(6,dtype=int)])
        for m in twice_generators:
            bm=int(B@m)
            assert bm%3 == 0
            reflected=m-(bm//3)*B.astype(int)
            assert int(B@reflected)%N == 0
            assert int(reflected@reflected) == int(m@m)
        lattice_reflections.append(N)
    return dict(rows=rows,lattice_reflection_generator_controls=lattice_reflections,
                integer_current_cutoff=5,magnetic_cutoff=6,image_cutoff=6,
                scope='Finite three-cube identity; finite Gaussian sums are not interval-certified tails.')


def physical_pair():
    rows=[]
    for theta,u,v in [(.6,.2,-.3),(1.2,-.4,.7),(2.1,.6,.1)]:
        joint=sum(np.exp(-a*u-1j*b*v+1j*a*b*theta)
                  for a,b in itertools.product([-1,1],repeat=2))
        source_free=sum(np.exp(1j*a*b*theta)
                        for a,b in itertools.product([-1,1],repeat=2))
        connected=joint-4*math.cosh(u)*math.cos(v)-(source_free-4)
        expected=4*((math.cos(theta)-1)*(math.cosh(u)*math.cos(v)-1)
                    -math.sin(theta)*math.sinh(u)*math.sin(v))
        error=float(abs(connected-expected))
        wrong=4*((math.cos(theta)-1)*(math.cosh(u)*math.cos(v)-1)
                 +math.sin(theta)*math.sinh(u)*math.sin(v))
        assert error < 1e-13 and abs(connected-wrong) > .01
        rows.append(dict(parameters=[theta,u,v],error=error,
                         wrong_physical_cross_sign=float(abs(connected-wrong))))
    return rows


def row_symbol(delta, pair, other, denominator):
    first=np.zeros(4,dtype=object)
    second=np.zeros(4,dtype=object)
    i,j=pair
    k,l=other
    first[i],first[j]=-delta[j],delta[i]
    second[k],second[l]=-delta[l],delta[k]
    numerator=sum(first[n]*np.conjugate(second[n]) for n in range(4))
    return np.divide(numerator,denominator,out=np.zeros_like(denominator,dtype=complex),
                     where=denominator>0)


def full_projection_pairs():
    pairs=list(itertools.combinations(range(4),2))
    rows=[]
    N=3
    c=2*math.pi*N
    for length in [8,12,16,24]:
        vector=np.exp(2j*math.pi*np.arange(length)/length)-1
        delta=[vector.reshape(tuple(length if j==i else 1 for j in range(4)))
               for i in range(4)]
        denominator=sum(abs(x)**2 for x in delta)
        mode=(1,2,1,0)
        Rmode=np.zeros((6,6),complex)
        Rzero=np.zeros((6,6),complex)
        Pmode=np.zeros((6,6),complex)
        Crows=[]
        square_rows=[]
        max_imag=0.
        for i,p in enumerate(pairs):
            csum=0.
            squared=0.
            for j,q in enumerate(pairs):
                symbol=row_symbol(delta,p,q,denominator)
                raw=np.fft.ifftn(symbol)
                max_imag=max(max_imag,float(np.max(abs(raw.imag))))
                kernel=raw.real
                squared+=float(np.sum(kernel**2))
                csum+=float(np.sum(np.cos(c*kernel)-1))
                R=np.sin(c*kernel)-c*kernel
                transform=np.fft.fftn(R)
                Rmode[i,j]=transform[mode]
                Rzero[i,j]=transform.flat[0]
                Pmode[i,j]=symbol[mode]
            Crows.append(csum)
            square_rows.append(squared)
        diag=(1-length**(-4))/2
        assert max(abs(x-diag) for x in square_rows) < 2e-13
        assert max(Crows)-min(Crows) < 2e-11
        r=float(np.trace(Rzero).real/6)
        assert np.max(abs(Rzero-r*np.eye(6))) < 3e-12
        Qmode=np.eye(6)-Pmode
        assert np.max(abs(Pmode@Qmode)) < 1e-13
        mixed=np.linalg.norm(Pmode@Rmode@Qmode,ord=2)
        assert mixed <= np.linalg.norm(Rmode-r*np.eye(6),ord=2)+1e-11
        rows.append(dict(length=length,all_orientation_square_sum=square_rows[0],
                         periodic_projection_diagonal=diag,A_N_finite=Crows[0],
                         A_N_orientation_spread=max(Crows)-min(Crows),
                         remainder_zero_scalar=r,zero_scalar_error=float(np.max(abs(Rzero-r*np.eye(6)))),
                         leading_cross_cancellation=float(np.max(abs(Pmode@Qmode))),
                         remaining_cross_mode_norm=float(mixed),real_kernel_error=max_imag))
    return dict(N=N,rows=rows,
                scope='All six orientations, finite torus harmonic correction retained; no continuum rate inferred.')


if __name__ == '__main__':
    print(json.dumps(dict(status='finite_checks_passed',physical_sources=physical_sources(),
                         physical_pair=physical_pair(),full_projection_pairs=full_projection_pairs()),indent=2))
