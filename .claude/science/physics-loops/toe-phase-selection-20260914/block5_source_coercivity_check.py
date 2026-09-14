#!/usr/bin/env python3
"""Check the source-specific uniform Hodge margin by independent row algebra.

The margin proof is local and analytical. Finite fixtures challenge pinning,
antiperiodic folds, signs, width and mass; they do not prove a physical phase.
"""
from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np
import sympy as s

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'scripts'))
import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as source


def main():
    vmin,vmax=s.Rational(5,6),s.Rational(13,6)
    smax=s.Rational(3,5)
    gamma=(vmin+1/vmax+2*vmin/(1+smax))/4
    Gamma=(vmax+1/vmin+2*vmax/(1-smax))/4
    assert gamma==s.Rational(243,416) and gamma>s.Rational(1,2)
    rows=[]
    cases=[(12,4,None,s.Rational(1),s.Rational(3,5),s.Rational(0)),
           (16,4,(vmin,)*4,s.Rational(1,10),-smax,smax),
           (12,8,(vmax,vmin)*4,s.Rational(7),smax,-smax)]
    for cover,width,pattern,mass,sigma,record in cases:
        fixture=source.Fixture(width,cover_t=cover,pattern=pattern,tag='block5-coercivity')
        q=fixture.q({source.RECORD_CELL:record},mass=mass,sigma=sigma,
                    sx=s.Rational(7,5),st=-s.Rational(2,3))
        S=s.expand((q+q.H)/2)
        h=S/mass
        margins=[];upper=[]
        for i in range(h.rows):
            off=sum(s.Abs(h[i,j]) for j in range(h.cols) if i!=j)
            margins.append(s.cancel(h[i,i]-off))
            upper.append(s.cancel(h[i,i]+off))
        assert min(margins)>=gamma and max(upper)<=Gamma
        # The anti-Hermitian connection contributes no Hermitian part.
        kinetic=fixture.q({source.RECORD_CELL:record},mass=0,sigma=sigma,
                         sx=s.Rational(7,5),st=-s.Rational(2,3))
        assert s.expand(kinetic+kinetic.H)==s.zeros(h.rows)
        assert s.expand(q-kinetic-mass*h)==s.zeros(h.rows)
        # Rebuild the cover quadratic forms before the half-fold. This uses
        # the full sparse construction, not the already-quotiented q matrix.
        substitutions=fixture.substitution(sigma,{source.RECORD_CELL:record},
                                          s.Rational(7,5),-s.Rational(2,3),mass)
        pinned=source.ssubs(fixture.fx.H_free,source.region_pin(fixture.fx,(fixture.c-1,fixture.c)))
        full_h=source.dense(source.ssubs(pinned,substitutions),fixture.fx.SIZE,fixture.fx.SIZE)
        full_d=source.dense(source.ssubs(fixture.fx.edge_d[(0,0)],substitutions),fixture.fx.SIZE,fixture.fx.SIZE)
        half=fixture.N
        compress=lambda A:(A[:half,:half]+A[half:,half:]-A[:half,half:]-A[half:,:half])/2
        assert full_h[:half,:half]==full_h[half:,half:]
        assert full_h[:half,half:]==full_h[half:,:half]
        assert compress(full_h)==h
        full_k=s.I*(full_h*full_d+full_d.H*full_h)
        assert s.expand(compress(full_k)-kinetic)==s.zeros(half)
        c=mass/2
        edges=source.edge_union((S,))
        B,residuals=source.signed_edge_factor(S,c,edges)
        assert min(residuals)>=mass*(gamma-s.Rational(1,2))
        assert s.expand(B*B.H+c*s.eye(h.rows)-S)==s.zeros(h.rows)
        qn=np.array(q.evalf(),dtype=complex)
        bn=np.array(B.evalf(),dtype=complex)
        n,k=bn.shape
        inverse=np.linalg.inv(qn)
        W=(inverse+inverse.conj().T)/2
        D=inverse@bn
        C=np.block([[W,D],[D.conj().T,np.eye(k)]])
        uniform_lower=mass*gamma/(1+mass*gamma)
        L=np.block([[qn,-bn],[np.zeros((k,n)),np.eye(k)]])
        N=np.diag([float(c)]*n+[1.]*k)
        Q=L.conj().T@np.linalg.solve(N,L)
        assert np.linalg.norm(Q@C-np.eye(n+k),ord=2)<1e-9
        assert np.linalg.norm(W-D@D.conj().T-float(c)*inverse@inverse.conj().T,ord=2)<1e-10
        actual_min=float(np.linalg.eigvalsh(Q)[0])
        assert actual_min>float(uniform_lower)
        rows.append(dict(cover_t=cover,width=width,pattern=None if pattern is None else list(map(str,pattern)),
                         mass=str(mass),background_shear=str(sigma),record_shear=str(record),
                         dimension=n+k,smallest_hodge_row_margin=str(min(margins)),
                         largest_hodge_row_sum=str(max(upper)),smallest_gram_residual=str(min(residuals)),
                         uniform_precision_lower_bound=str(uniform_lower),numeric_precision_minimum=actual_min))
    outside=source.Fixture(4,cover_t=10,tag="odd-half-cover-challenge")
    outside_k=outside.q(mass=0,st=s.Rational(2,3))
    hermitian_entries=sum(value!=0 for value in s.expand(outside_k+outside_k.H))
    assert hermitian_entries==16
    result=dict(outside_domain_odd_half_cover_hermitian_entries=hermitian_entries,
                hodge_lower_bound=str(gamma),hodge_upper_bound=str(Gamma),
                source_sha256=sha256(Path(source.__file__).read_bytes()).hexdigest(),
                domain='Temporal cover divisible by four, even width, v in [5/6,13/6], |shear|<=3/5, same local Hodge/fold/pinning definitions; mass>0, c=mass/2 or mass/3',
                claim='Analytical dimension-independent coercivity of this supplied Gaussian family; no massless estimate or native phase selection',
                finite_challenges=rows)
    Path(__file__).with_name('BLOCK5_SOURCE_COERCIVITY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
