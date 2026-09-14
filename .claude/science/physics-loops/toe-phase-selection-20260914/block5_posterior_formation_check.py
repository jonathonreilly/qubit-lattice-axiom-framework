#!/usr/bin/env python3
"""A local permanent observation process whose full precision has moral edges.

This is a supplied protocol with initial control records. Its attractive
Gaussian field is a posterior conditional law, not its unconditional root law.
"""
import itertools
import json
from pathlib import Path
import sympy as s


def main():
    mass=s.Rational(1)
    kappa=s.Rational(1)
    incidence=s.Matrix([[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[1,0,0,-1]])
    prior=s.eye(4)/mass**2
    noise=s.eye(4)/kappa
    transfer=s.eye(8)
    transfer[4:,:4]=incidence
    joint_cov=transfer*s.diag(prior,noise)*transfer.T
    joint_precision=joint_cov.inv()
    target=mass**2*s.eye(4)+kappa*incidence.T*incidence
    observed=joint_cov[4:,4:]
    gain=joint_cov[:4,4:]*observed.inv()
    posterior=joint_cov[:4,:4]-gain*joint_cov[4:,:4]
    assert posterior==target.inv()
    assert joint_precision[:4,:4]==target
    assert joint_cov[:4,:4]==prior and prior!=posterior
    assert gain==kappa*posterior*incidence.T

    roots=[(0,0,0),(2,0,0),(2,2,0),(0,2,0)]
    observations=[(1,0,0),(2,1,0),(1,2,0),(0,1,0)]
    controls=[(x,y,1) for x,y,z in roots]
    assert len(set(roots+observations+controls))==12
    l1=lambda x,y:sum(abs(a-b) for a,b in zip(x,y))
    for j in range(4):
        assert l1(controls[j],roots[j])==1
        for i in range(4):
            if incidence[j,i]:
                assert l1(observations[j],roots[i])==1
    # Formation reads nearest parents. Static precision contains root-root
    # terms at distance two, so the two locality statements are distinct.
    moral=[]
    for i in range(4):
        for j in range(i+1,4):
            if joint_precision[i,j] and l1(roots[i],roots[j])>1:
                moral.append(dict(left=i,right=j,distance=l1(roots[i],roots[j]),
                                  precision=str(joint_precision[i,j])))
    assert len(moral)==4

    # A local closed-support scalar M2 codec, without the earlier nonlinear
    # full-payload chart: M=(8r+i x)I+(R(1,2,3)).sigma.
    pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    vector=s.Matrix([1,2,3])
    rotations=[]
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1,1),repeat=3):
            r=s.zeros(3)
            for i in range(3):
                r[i,permutation[i]]=signs[i]
            if r.det()==1:
                rotations.append(r)
    assert len({tuple(r*vector) for r in rotations})==24
    for r in rotations:
        payload=s.Rational(2,7)
        role=5
        m=(8*role+s.I*payload)*s.eye(2)
        rv=r*vector
        for i in range(3):
            m+=rv[i]*pauli[i]
        assert s.re(s.trace(m))/16==role
        assert s.im(s.trace(m))/2==payload
        recovered=s.Matrix([s.trace(m*p)/2 for p in pauli])
        assert recovered.applyfunc(s.simplify)==rv

    # Conditional Gaussian shifts give a controlled positive-window version.
    metric=kappa**2*incidence*posterior*incidence.T
    assert all(ev<=kappa for ev in metric.eigenvals())
    epsilon=s.Rational(1,100)
    window_kl_bound=kappa*4*epsilon**2/2
    # Check every box corner against the quadratic KL expression, independently
    # of the operator-norm inequality used for the uniform bound.
    for signs in itertools.product((-1,1),repeat=4):
        y=epsilon*s.Matrix(signs)
        exact_kl=(y.T*gain.T*posterior.inv()*gain*y)[0]/2
        assert exact_kl<window_kl_bound
    result=dict(precision=[[str(x) for x in target.row(j)] for j in range(4)],
                posterior_covariance=[[str(x) for x in posterior.row(j)] for j in range(4)],
                unconditional_root_covariance='identity; differs from posterior',
                formation_edges_nearest=True,initial_controls=controls,
                roots=roots,observation_sites=observations,
                nonnearest_static_precision_entries=moral,
                scalar_matrix_codec_frames=24,
                observation_covariance_determinant=str(observed.det()),
                positive_window_epsilon=str(epsilon),
                posterior_kl_upper_bound=str(window_kl_bound),
                posterior_tv_upper_bound=str(s.sqrt(window_kl_bound/2)),
                scope='supplied local permanent protocol; target field is conditional on later observations, not the unconditional formed root field')
    Path(__file__).with_name('BLOCK5_POSTERIOR_FORMATION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
