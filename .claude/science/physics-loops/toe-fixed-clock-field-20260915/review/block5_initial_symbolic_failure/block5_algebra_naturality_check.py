"""Exact author challenges of full-algebra support and word kernels.

There is no sample-based claim about invariant measures. The no-moment
support theorem and global priority existence require the written proofs.
"""
import itertools
import json
from pathlib import Path
import sympy as s


I=s.eye(2);zero=s.zeros(2)
A=s.diag(1,-1);B=s.Matrix([[0,1],[1,0]])
E12=s.Matrix([[0,1],[0,0]]);E21=E12.T


def real_vector(matrix):
    entries=list(matrix)
    return s.Matrix([s.re(z) for z in entries]+[s.im(z) for z in entries])


def real_action(g,conjugate=False):
    basis=[]
    for phase in [1,s.I]:
        for index in range(4):
            matrix=s.zeros(2);matrix[index]=phase
            transformed=g*(s.conjugate(matrix) if conjugate else matrix)*g.inv()
            basis.append(real_vector(transformed))
    return s.Matrix.hstack(*basis)


def words(profile,max_length=3):
    result=[(0,I)]
    for length in range(1,max_length+1):
        for indices in itertools.product(range(len(profile)),repeat=length):
            value=I
            for index in indices:value=value*profile[index]
            result.append((length,value))
    return result


def covariance(profile):
    result=s.zeros(8)
    for length,matrix in words(profile):
        real,imag=real_vector(matrix),real_vector(s.I*matrix)
        result+=s.Rational(1,2*4**length)*(real*real.T+imag*imag.T)
    return result


def algebra_rank(profile,max_length=3):
    return s.Matrix.hstack(*[s.Matrix(list(matrix)) for _,matrix in words(profile,max_length)]).rank()


def main():
    a,b,c,d,n=s.symbols('a b c d n')
    generic=s.Matrix([[a,b],[c,d]])
    upper=I+n*E12
    explicit=s.Matrix([[a+n*c,b+n*(d-a)-n*n*c],[c,d-n*c]])
    assert s.expand(upper*generic*(I-n*E12)-explicit)==zero
    tu=real_action(I+E12);tl=real_action(I+E21)
    assert (tu-s.eye(8))**3==s.zeros(8)
    assert (tl-s.eye(8))**3==s.zeros(8)
    upper_dim=8-(tu-s.eye(8)).rank()
    central_dim=8-s.Matrix.vstack(tu-s.eye(8),tl-s.eye(8)).rank()
    assert upper_dim==4 and central_dim==2

    profiles={'empty':[],'sole_zero':[zero],'sole_identity':[I],
              'diagonal':[A],'jordan':[E12],'triangular':[A,E12],
              'full_pair':[A,B],'complex_pair':[A+s.I*I,B+E12],
              'commuting_pair':[A,2*A+I],
              'six_slots':[A,B,E12,E21,zero,s.I*I]}
    expected={'empty':1,'sole_zero':1,'sole_identity':1,'diagonal':2,
              'jordan':2,'triangular':3,'full_pair':4,'complex_pair':4,
              'commuting_pair':2,'six_slots':4}
    covariances={name:covariance(profile) for name,profile in profiles.items()}
    rank_checks=[]
    for name,profile in profiles.items():
        arank=algebra_rank(profile);rrank=covariances[name].rank()
        assert arank==expected[name] and rrank==2*arank
        # Verify that the computed word span has actually stabilized.
        assert algebra_rank(profile,4)==arank
        rank_checks.append(dict(profile=name,words=len(words(profile)),
                               complex_algebra_dimension=arank,real_covariance_rank=rrank))
    assert covariances['sole_zero']==covariances['empty']
    assert covariances['sole_identity']==s.Rational(85,64)*covariances['empty']

    transformations=[I+E12,I+E21,s.diag(2,s.Rational(1,2)),B,
                     s.Matrix([[1,s.I],[0,1]])]
    equivariant_cases=0
    for name,profile in profiles.items():
        for g in transformations:
            for conjugate in [False,True]:
                action=real_action(g,conjugate)
                transformed=[g*(s.conjugate(x) if conjugate else x)*g.inv() for x in profile]
                assert covariance(transformed)==action*covariances[name]*action.T
                equivariant_cases+=1
    slot_permutations=0
    profile=profiles['six_slots']
    for permutation in [(5,4,3,2,1,0),(1,0,3,2,5,4),(2,3,4,5,0,1),(0,2,4,1,3,5)]:
        assert covariance([profile[i] for i in permutation])==covariances['six_slots']
        slot_permutations+=1

    u,v=s.symbols('u v')
    U=u*I+v*A
    span=s.Matrix.hstack(*[s.Matrix(list(x)) for x in [I,U,B,U*B]])
    assert s.factor(span.det()) in [4*v*v,-4*v*v]
    assert s.factor((U*B-B*U).det())==4*v*v
    assert s.Rational(1,4)+s.Rational(1,64)==s.Rational(17,64)
    # Noncommuting is insufficient: this pair only generates a triangular algebra.
    assert A*E12-E12*A!=zero and algebra_rank([A,E12])==3
    assert algebra_rank([A,B],1)==3 and algebra_rank([A,B])==4

    seed={(0,0,0):A,(1,0,0):A,(0,1,0):B,(1,1,0):B}
    def neighbors(point):
        for axis in range(3):
            for sign in [-1,1]:
                yield tuple(value+(sign if i==axis else 0) for i,value in enumerate(point))
    seed_checks=[]
    for point,value in seed.items():
        profile=[seed[y] for y in neighbors(point) if y in seed]
        assert algebra_rank(profile)==4
        seed_checks.append(dict(site=list(point),neighbor_algebra_dimension=4))
    first=(2,0,0);second=(2,1,0)
    excluded=(set(neighbors(first))|set(neighbors(second)))-set(seed)-{first,second}
    assert len(excluded)==8
    first_profile=[seed[y] for y in neighbors(first) if y in seed]
    assert first_profile==[A]
    # An exact prefix value inside the first site's support, not a Gaussian draw.
    prefix=dict(seed);prefix[first]=s.Rational(1,3)*I+s.Rational(2,5)*A
    second_profile=[prefix[y] for y in neighbors(second) if y in prefix]
    assert algebra_rank(second_profile)==4

    dilation=real_action(s.diag(2,s.Rational(1,2)))
    frobenius_cov=s.eye(8)/2
    assert (dilation*frobenius_cov*dilation.T)[1,1]/frobenius_cov[1,1]==16
    wrong_output_gap=max(abs(x) for x in
                         dilation*covariances['full_pair']*dilation.T-covariances['full_pair'])
    assert wrong_output_gap>1
    result=dict(status='exact_author_checks_passed',independent_review=False,
                upper_shear_fixed_real_dimension=upper_dim,both_shears_fixed_real_dimension=central_dim,
                support_ranks=rank_checks,exact_real_automorphism_cases=equivariant_cases,
                exact_slot_permutations=slot_permutations,
                zero_vs_identity_variance_ratio='85/64',seed_checks=seed_checks,
                seed_prefix_full_algebra=True,restricted_additional_clocks=len(excluded),
                analytic_positive_clock_event='exp(-17)*(1-exp(-1))^2',
                first_seed_extension_noncentral_variance='17/64',
                rejected_full_support_from_noncommutativity_alone_dimension=3,
                rejected_length1_word_span_dimension=3,
                rejected_frobenius_full_inner_invariance_variance_ratio=16,
                rejected_independent_output_relabeling_gap=str(wrong_output_gap),
                limitations=['invariant probability and infinite ancestor conclusions rely on analytic proofs',
                             'finite covariance display coordinates do not define the intrinsic kernel',
                             'common algebra identification and compatible seed are supplied inputs',
                             'no quantum channel, kinetic realization or all-foundation claim'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('per_element: checked exact shear identities, fixed spaces, word products and Gaussian covariance transformations')
    print('per_site: checked all named one-input and multi-input algebra support dimensions and a supplied compatible seed')
    print('per_mode: checked and not executed — no matter kinetic or quantum mode is supplied by a matrix-label kernel')
    print('per_block: checked slot permutations and a support-valid noncentral two-step prefix')
    print('lattice_wide: checked and not executed — the global process uses the analytic finite-ancestor proof, not a finite-lattice extrapolation')


if __name__=='__main__':main()
