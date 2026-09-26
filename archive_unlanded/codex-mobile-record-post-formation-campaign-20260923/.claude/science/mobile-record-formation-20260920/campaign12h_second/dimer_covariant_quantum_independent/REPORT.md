# Mixed two-qubit encoding and conditional curl-energy review

No actionable mathematical defect or required source correction was found.
The supplied positive encoding, its finite-family product-state Weyl limit,
and the two conditional bracket/energy calculations reconstruct. This is a
bounded scientific check, not a native quantum-dynamics construction, an
audit verdict, or a phase claim.

## Sources and independence boundary

The complete primary note was read at SHA-256
`5b53badd77e2a61b100eb8a3b048986895e78f9904f12d5b79b41dbb25b2a91a`.
The independently written derivation and controls were sealed before the
author checker or results in `PRE_COMPARISON_SEAL.json`, SHA-256
`b4dcfe9a8f9b0558482a3bf2c877ab68bdee96dab82c7216fa93872598e7088b`
(14 artifacts and 10 source/dependency bindings).

After that seal, the complete author checker
`dimer_covariant_quantum_encoding_check.py`, SHA-256
`371256d50f196b3e35bc3872feed93024b227373860931e95d9ffbe02eaf4a72`,
and its complete result file, SHA-256
`c694f17850f26562349be83b76317eacf459ae9885ee7ccf62f5704f37dda344`,
were read and compared. The three separate group files equal their embedded
results, the run log names the three completed groups, and stderr is empty.
No author code was executed.

The previous antipodal-product encoding review and corrected routed theorem
were reused only at their recorded identities. The new encoding is distinct
from the original pure antipodal record interpretation. The separately
queued finite-qubit construction was not opened during this review.

## Positive encoding and six observables

For `rho=[[q,w^dagger],[w,rI]]`, trace one and strict positivity follow from
q+3r=1, q,r>0 and `||w||^2<qr`. The two supplied orbits give squared norms
lambda_A^2 and 3lambda_B^2, exactly as used in the maximum condition. The
rational example's Schur complements are 13/32 and 55/128. At equality the
state can become singular; beyond it the matrix can have a negative
eigenvalue. These boundaries were checked explicitly.

The singlet/triplet basis gives the stated proper-cubic covariance and
endpoint-swap reversal. Direct multiplication verifies both Pauli identities,
including the minus sign in `B_i=-(sigma_1 cross sigma_2)_i/2`. The means are
`2lambda_A e_i` and `2lambda_B b_i`. The population tangent image has exactly
six dimensions. Different orbit-isotropic weights have the same average
rho_0, and remaining color statistics are not reconstructed. Six accessible
means do not imply single-copy discrimination of fourteen full-rank states.

The symmetrized covariance and CCR form are

`V=(q+r)I_6`, `Sigma=2(q-r)J`.

The quantum Gram matrix `V+iSigma/2` has eigenvalues 2q and 2r, each threefold.
For q!=r this gives three canonical pairs in the fluctuation limit. At
q=r=1/4 the limiting form vanishes even though the finite-block observables
do not commute. At the rational example, the averaged centered commutator
has exact mean-square variance 20/(9K).

The independent checker verifies all fourteen states, 336 proper-rotation
state identities, endpoint swap, all six physical Pauli expressions, the
population rank and symbolic covariance spectrum. These are changed
encoding/preparation premises, as the note explicitly states.

## Product-state Weyl limit

The claimed ordered product factorization is exact for independent blocks.
For fixed tests z_j, write Z_j=z_j.O and M=sum_j ||Z_j||. The one-block factor
is `1+b/K+r_K`, with

`b=-1/2 z_sum^T V z_sum - i/2 sum_(j<l) z_j^T Sigma z_l`.

The matrix exponential series gives
`|r_K|<=exp(M/sqrt(K)) M^3/(6K^(3/2))`. With
`R=exp(M)M^3/6` and `D=M^2/2+R`, for K>=2D the logarithmic remainder obeys
`|K log(1+b/K+r_K)-b|<=R/sqrt(K)+D^2/K`. This supplies a direct proof for
each fixed finite word, independently of any general interacting quantum
central-limit theorem.

The ordering phase matters. An independently selected group-commutator word
`A_1,B_1,-A_1,-B_1` has limit `exp(-2i/3)` in the rational example. Matrix
controls for K=16 through 4096 approach that sign and remain separated from
its complex conjugate. A different three-test rational word was expanded
exactly through second order. A two-block tensor calculation also verifies
the factorization directly.

For bounded spatial test arrays the same expansion is uniform block by
block. The limit uses their limiting empirical inner product. In the intended
uniform torus/Riemann-sum setting this yields the stated onsite spatial delta
kernel. Merely assuming convergence of arbitrary array inner products does
not select a different prescribed continuum measure or prove convergence in
an infinite-dimensional field topology. The source's finite-family scope is
the operative theorem.

## Conditional normalization and energy signs

The field scaling gives coefficients `a lambda_A/lambda_B` and
`b lambda_B/lambda_A`. The ratio `lambda_B/lambda_A=sqrt(a/b)` makes both
equal sqrt(ab), and a common reduction of the lambdas meets positivity.
The equal-fourteen-color example correctly gives speed 2gamma/7.

The new quantum covariance is preserved by the proposed linear flow. This
does not transfer the classical stochastic generator or its Euler theorem
to the new quantum states; the note correctly labels the drift hypothetical.

For onsite Sigma=s0J, s0=2(q-r)!=0, the exact full-helicity curl drift uniquely
fixes the quadratic Hessian to `(c/s0)diag(C,C)`, C=i[Q cross]. At Q!=0 the
signature is two positive, two negative and two zero directions. A real
transverse helix `(cos z,sin z,0)` has curl equal to minus itself, so the
negative direction is not an artifact of treating Q and -Q independently.
Transverse restriction removes zero directions but retains both signs.
Changing s0's sign exchanges the signs rather than curing indefiniteness.

A positive conserved norm is not automatically the Hamiltonian generating
this flow: with the onsite bracket its identity Hessian generates onsite
rotations. The note limits this conclusion to the specified bracket, full
transverse space and exact drift, and preserves the possibilities of an
excited-state linearization, different brackets or extra degrees of freedom.

## Derivative-bracket construction and limits

For canonical (Qpot,P), E=-P and B=CQpot have linear map
`T=[[0,-I],[C,0]]`. Direct calculation gives
`T J T^dagger=[[0,C],[-C,0]]` and the positive semidefinite canonical Hessian
`diag(C^2,I)=T^dagger T`. Hamilton's equations then give
Edot=C B and Bdot=-C E with the source's signs. At nonzero Q the derivative
bracket has rank four. The map T has rank five: B is transverse, while E
still needs a separately selected electric Gauss constraint. Longitudinal
Qpot is unobservable in this map.

On a periodic box B=curl Qpot also has zero spatial mean. Arbitrary harmonic
magnetic sectors require extra data. The note presents an explicit example
rather than claiming this parametrizes every periodic Maxwell state, so this
is a scope clarification rather than a correction request. The new bracket
is supplied continuum Gaussian field theory; no microscopic identification,
formation coupling or electric-Gauss preparation has been established here.

## Evidence comparison and limits

`compare_author.py` authenticates all source/output bindings and all fourteen
sealed precomparison artifacts. It compares the fourteen exact color rows
and four exact Fourier Hessian spectra. It recomputes all 25 author finite-K
Weyl values with the closed rank-two exponential

`exp(iZ/sqrt(K)) = I + (cos(theta)-1)Z^2/||z||^2
                     + i sin(theta)Z/||z||`,
`theta=||z||/sqrt(K)`,

instead of importing the author implementation or calling its matrix
exponential routine. The maximum discrepancy is about 2.84e-13; Gaussian
targets agree to the recorded precision. Numerical corroboration is kept
separate from the bounded-series proof.

One independent helper assertion initially compared unsimplified symbolic
Gram matrices structurally. Its exact simplified difference is zero and its
eigenvalues already matched. The initial script, stdout/stderr, receipt and
diagnostic are preserved under `failed_attempts/`; only that equality test
was changed. The corrected full independent run and postcomparison run pass.

Attempts to access the two contextual literature links failed in the web
tool and are recorded in `EXTERNAL_ACCESS_RECEIPT.json`. Their contents and
bibliographic details were not independently authenticated in this review.
Neither is a theorem import: the finite product expansion and canonical
Hamiltonian calculation above supply the required arguments directly.

To reproduce the blind matrix controls, copy `independent_check.py` to a
fresh empty directory and run it with Python, NumPy, SciPy and SymPy. It
refuses to overwrite an existing result file. Full logs, receipts and exact
source identities accompany this report. No primary source, prior sealed
packet, Git state, publication or audit status was changed.
