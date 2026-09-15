"""Exact checks of the Borel escape and its failure of tightness.

The all-profile continuous-support proof is analytic. A shared covariance
helper is used only for the earlier word part, with provenance explicit.
"""
import itertools
import json
from pathlib import Path
import sympy as s
from block5_algebra_naturality_check import I,A,B,E12,E21,zero,real_vector,real_action,covariance,algebra_rank


def inverse_corner(p,q,t):
    if t==zero:return zero
    entries=s.symbols('c0:4')
    c=s.Matrix(2,2,entries)
    equations=list(c-q*c*p)+list(t*c-p)+list(c*t-q)
    solution=s.linsolve(equations,entries)
    assert len(solution)==1
    values=next(iter(solution))
    assert not set(entries)&set().union(*(v.free_symbols for v in values))
    result=s.Matrix(2,2,values).applyfunc(s.simplify)
    assert s.simplify(result-q*result*p)==zero
    assert s.simplify(t*result-p)==zero and s.simplify(result*t-q)==zero
    return result


def inverse_features(profile):
    features=[]
    for i,a in enumerate(profile):
        eigenvalues=list(a.eigenvals())
        if len(eigenvalues)!=2:continue
        for lam,mu in [eigenvalues,eigenvalues[::-1]]:
            p=((a-mu*I)/(lam-mu)).applyfunc(s.simplify);q=I-p
            for j,b in enumerate(profile):
                if i==j:continue
                t=(p*b*q).applyfunc(s.simplify)
                if t!=zero:features.append(inverse_corner(p,q,t))
    return features


def enhanced_covariance(profile):
    out=covariance(profile)
    for matrix in inverse_features(profile):
        v,w=real_vector(matrix),real_vector(s.I*matrix)
        out+=(v*v.T+w*w.T)/2
    return out.applyfunc(s.simplify)


def main():
    assert inverse_corner(s.diag(1,0),s.diag(0,1),2*E12)==E21/2
    profiles={'empty':[],'scalar':[I,2*I],'commuting':[A,2*A+I],
              'nilpotent_commuting':[E12,2*E12],
              'upper_triangular':[A,E12],'lower_triangular':[A,E21],
              'two_nilpotents':[E12,E21],'full_pair':[A,B]}
    results=[];equivariance=0
    transformations=[I+E12,s.diag(2,s.Rational(1,2)),s.Matrix([[1,s.I],[0,1]])]
    for name,profile in profiles.items():
        commutes=all(x*y==y*x for x,y in itertools.combinations(profile,2))
        arank=algebra_rank(profile)
        q=enhanced_covariance(profile)
        assert q.rank()==2*arank if commutes else q.rank()==8
        for g in transformations:
            for conjugate in [False,True]:
                transform=lambda x:g*(s.conjugate(x) if conjugate else x)*g.inv()
                action=real_action(g,conjugate)
                delta=enhanced_covariance(list(map(transform,profile)))-action*q*action.T
                assert s.simplify(delta)==s.zeros(8)
                equivariance+=1
        results.append(dict(profile=name,complex_word_algebra_dimension=arank,
                            inverse_feature_count=len(inverse_features(profile)),
                            enhanced_real_covariance_rank=q.rank()))
    # Exact path to a degenerate profile. The explicit probability formula
    # comes from a circular complex normal, not from a variance-only inference.
    degeneration=[]
    for t in [s.Rational(1),s.Rational(1,2),s.Rational(1,4),s.Rational(1,16)]:
        features=inverse_features([A,t*E12])
        assert features==[E21/t]
        q=enhanced_covariance([A,t*E12])
        variance=s.simplify(q[2,2]+q[6,6])
        assert variance==1/t**2
        degeneration.append(dict(t=str(t),variance_21=str(variance),
                                 exact_probability_unit_disk=str(1-s.exp(-t*t))))
    assert enhanced_covariance([A,zero]).rank()==4
    # Coordinate-level proof control: preserving a common line is essential.
    a,b,c=s.symbols('a b c')
    nilpotent=s.Matrix([[a,b],[c,-a]])
    commutator=E12*nilpotent-nilpotent*E12
    assert commutator==s.Matrix([[c,-2*a],[0,-c]])
    assert commutator.charpoly().all_coeffs()==[1,0,-c*c]
    result=dict(status='exact_author_checks_passed',independent_review=False,
                support_profiles=results,automorphism_covariance_cases=equivariance,
                degeneration=degeneration,
                continuous_limit_word_covariance_rank=4,
                analytic_non_tightness='P(abs(output21)<=R)=1-exp(-R^2*t^2) tends to0',
                limitations=['initial structural polynomial equality failure is preserved under review/',
                             'continuous maximal-support and global-existence assertions use analytic proofs',
                             'Borel inverse-corner law is discontinuous at specified degeneracies',
                             'common-fiber identification and matrix-label process remain supplied',
                             'word covariance helper shared with earlier exact runner',
                             'no matter kinetic, Born or all-foundation conclusion'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('per_element: checked intrinsic partial-inverse equations and covariance under real algebra automorphisms')
    print('per_site: checked exact maximal support ranks on central, commuting, triangular and full-algebra profiles')
    print('per_mode: checked and not executed — these are probability kernels, not kinetic or quantum modes')
    print('per_block: checked a degenerating two-record profile and its exact non-tight Gaussian probability')
    print('lattice_wide: checked and not executed — append-support monotonicity and global existence use the written proof')


if __name__=='__main__':main()
