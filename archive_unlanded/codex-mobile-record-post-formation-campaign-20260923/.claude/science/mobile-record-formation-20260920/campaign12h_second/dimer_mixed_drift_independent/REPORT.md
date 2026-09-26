# Independent check: mixed-encoding initial-drift ambiguity

The specified finite witness is correct. I found no required source correction.
At the same complete product density operator, the two classical preparations
assign different initial derivatives to the same pair observable:

| Quantity at black site (1,1,0) | Preparation p | Preparation p' | Difference p' minus p |
|---|---:|---:|---:|
| D_2 | 1/7 | 5/28 | 1/28 |
| microscopic dot X_2 | -3/224 | -15/896 | -3/896 |
| microscopic dot mean(A_2) | -3/896 | -15/3584 | -3/3584 |

This is a compatibility failure for the fixed six-moment mixed encoding,
with both preparations in its domain and no additional preparation
information. It is not a general quantum no-go, a claim against other
encodings, or an audit/retention verdict.

## Exact reconstruction

The encoding parameters q=1/2,r=1/6,lambda_A=1/8,lambda_B=1/12 give positive
axis/corner Schur complements 13/32 and 3/8. All fourteen matrices are
strictly positive and normalized. Their mixture depends only on
w=lambda_A X+i lambda_B Y. Both preparations have X=0 and
Y=(0,0,cos(pi x/3)/8); transferring equal mass between the two signs of
A_1 and A_2 changes D_2 but not w. Both profiles are normalized and strictly
positive, with minimum probability 3/56 across all their sampled values.

Independent color draws and product preparation imply

    E[tensor_u rho_(a_u)] = tensor_u E[rho_(a_u)].

Thus equality of each local mixed density gives equality of the entire
864-pair encoded density operator on the N=12 torus. This conclusion uses
the product preparation premise; equal marginals alone would not suffice
for arbitrary correlated inputs.

For the actual rate k0/2+h/4, direct averaging over the four distinct
contexts gives, since every X vanishes and D_2 is spatially constant,

    J_(delta,X2)(x)
       =gamma D_2/4 * delta.[e_2 cross (Y_l+Y_r)].

The symmetric k0 part vanishes for X_2, and the factor 1/4 retains the
supplied half-rate convention. Only delta=-e_1 contributes; its route
displacement is -2e_1. With c_x=cos(pi x/3),

    J_-(x)=-gamma D_2 A[c_(x+2)+c_(x-4)]/4
          =-gamma D_2 A c_(x+2)/2,
    dot X_2(x)=J_-(x+2)-J_-(x)
              =gamma D_2 A[c_(x+2)-c_(x+4)]/2.

At x=1 the cosine difference is -3/2, giving the table. The observable
A_2=|0><2|+|2><0| has mean 2lambda_A X_2=X_2/4. The encoded local density
derivatives differ in entries (0,2) and (2,0) by -3/7168, with all other
entries of their difference zero. Euler acceleration multiplies the
observable difference by N=12, giving -9/896; it is unnecessary here.

## Independent evidence and failure preservation

Before any new author checker/results access, the independent script
enumerated all 14^4 context assignments for each of five nonfixed
directions, twelve first coordinates, and both preparations. Those 120
channel cases give 4,609,920 exact weighted assignments. Probabilities have
common denominator 896, and the actual rate is (22+5hn)/40 with integer
hn. A checked upper bound keeps every accumulation inside int64; the
current calculation uses no numerical tolerance. All complete fourteen-entry
currents agree with a separately contracted formula, sum to zero, and give
the stated incoming-minus-outgoing derivatives. All rates are between
1/20 and 21/20. Exact matrix checks verify local density equality,
observable normalization, the local density derivative difference and a
two-pair tensor product. Full product equality follows algebraically;
the exponentially large total density matrix was not materialized.

The first run reached output serialization after all mathematical assertions
passed, then failed on NumPy integer coordinates in its JSON context list.
The complete original source, partial output, empty log, traceback and
receipt remain under failed_attempts/numpy_json. The sole repair converts
those coordinates to Python integers. No formula, assertion, grid or
threshold changed. The corrected run succeeded with empty stderr.

INDEPENDENT_DERIVATION.md gives the complete pre-comparison reasoning.
PRE_COMPARISON_SEAL.json binds four sources and thirteen artifacts at
SHA-256 `0bb97a1123d58603376f6e98c4768d9d45a06b50d6016ef39059c4cd65373790`.
The reviewed witness source is
`114b380b061072193712bf46a9ca3a935488994e310076e6cf08b034b6b5222a`;
the complete prerequisite source identities are in PRE_SOURCES.json.

After that seal, the complete author checker, complete result and both run
streams were read and authenticated. Checker SHA-256 is
`c6dfe27f6d0b09e8f505dc2da488904858c157e456d83a4967ae5ad5170786e7`;
result SHA-256 is
`ef373d0981c92419e7a7a6c53bbf5106890f171dabb935b3310aeb6a6d247736`.
All reported exact values agree with the independently sealed direct-rate
enumeration. Both embedded source identities and the log's JSON agree;
stderr is empty. There is no separate author command receipt, and none is
claimed. The author runner uses the contracted current formula; this review
independently checked that formula against actual four-context rates.
No consequential prose/code drift was found. The author suite was not
rerun for a success count. COMPARISON_RESULTS.json records the bounded
comparison, and FINAL_SEAL.json binds the complete packet while preserving
the pre-comparison seal and failed serialization attempt unchanged.

## Operational scope

A single quantum experiment with identical full input density operators,
identical settings and input-independent ancillas cannot give different
expectations of the same observable. The assignments therefore cannot both
factor through this density encoding. No Hamiltonian, Markov, locality,
hydrodynamic or long-time assumption is required for that test.

Retaining a classical label, conditioning on color counts, or using
preparation-correlated purifications/environments may change the full
physical inputs; those are different interfaces. A fixed basis/phase change
or consistent pair-orientation convention applied to both preparations
preserves their equality and conjugates the same observable, so it does
not evade this witness. Restricting the preparation domain, encoding more
moments, enlarging the physical block, or changing the generator remains
open. The original pure-projector record interpretation is not silently
identified with the changed mixed-state representation.

Only the exact initial derivative is tested. No later product evolution,
native formation result, general impossibility, physical-emergence conclusion,
or completed broad no-go gate follows. No primary source, Git state,
publication or audit status was changed.
