# Independent check: proper-cubic pair covariance and cubic color information

The exact representation identity and the specified finite drift witness
are correct. No source correction or unresolved step was identified within
this bounded check. The two conclusions have different hypotheses: covariance
with the fixed U=1 direct-sum R forces cubic-moment blindness; the drift
contradiction additionally needs a nonzero readable Z12 observable and the
preparation domain used in the witness.

This is raw compatibility evidence for the stated representation and
affine encoding. It is not a general quantum no-go, publication disposition,
formal audit or retained-status judgment.

## Representation and positive example

For proper signed permutations, chi(b)=b1b2b3 transforms by
a(R)=sign(sigma), where sigma is the underlying coordinate permutation.
Consequently T=sum_b chi(b)rho_b must obey U T U^dagger=a(R)T.

There is a short independent proof that T=0. Proper two-coordinate sign
flips force every singlet-triplet off-diagonal vector and off-diagonal
triplet matrix entry to vanish. A coordinate three-cycle makes the three
remaining triplet diagonal entries equal. A proper rotation with an odd
coordinate permutation leaves this scalar block form unchanged but has
a=-1, forcing the entire operator to zero. Thus no alternating component
occurs in the full complex operator space. An independent exact sum over
all 24 rotations also gives zero in every entry of the 16-by-16 character
projection. Only proper rotations and the supplied U are used.

Affine mixtures therefore lose the perturbation delta p_b=delta_w chi(b)/8.
This identity is independent of the chosen positive covariant state family.
It does not classify larger blocks, other representations or nonlinear
preparation assignments.

For the explicit family, the corner triplet block has perpendicular and
parallel eigenvalues 5/32 and 3/16. Its singlet Schur complement is 71/144;
the axis Schur complement is 61/128. These prove strict positivity, along
with the positive triplet blocks. All matrices are Hermitian and trace one.
The independent code also checks all 56 leading principal minors and all
336 state-covariance relations exactly. The (1,2) triplet entry gives

    Tr[rho(p) Q12]=2 kappa Z12=Z12/48.

A constant covariant encoding rho_a=I/4 is an important countercontrol:
it also loses w but has no nonzero readable Z12. The representation identity
alone cannot give the asserted drift contradiction. The source retains
this observability condition correctly.

## Exact microscopic drift

The two independently drawn color preparations have D_i=1/7,
X=(0,1/28,0), Y=Z=0; only the second has
w(x)=cos(pi x/3)/16. Their minimum probability is 3/56. Cubic blindness
gives identical local densities, and independence of encoded pairs gives
identical complete product density operators. This is stronger than mere
equality of local marginals for arbitrary correlated preparations.

In the actual four-context rate k0/2+h/4, the context contraction is
S_delta(p_l+p_r)_a=gamma delta.[X cross b_a]. The endpoint mu terms vanish
because Y=0. The symmetric current part vanishes because Z12=0. Using
sum p_b b1b2 b=(Y2,Y1,w) gives the exact current

    J_(delta,Z12)(x)=gamma/4 *delta.[X cross e3]
                                      [w(x)+w(q_delta x)].

Only the nonfixed delta=-e1 contributes. Its displacement is -2e1, so
incoming minus outgoing at x=1 is

    dot Z12=-(gamma A/4)[w(3)-w(-1)]
           =3 gamma A eta/8=3/3584.

The baseline derivative is zero. Hence the Q12 derivative difference is
1/57344, and the local density derivative difference has entries (1,2)
and (2,1) equal to 1/114688. These are unaccelerated microscopic-time
identities, with gamma=1,k0=11/10,N=12; no continuum limit or later product
evolution is used.

The independent checker forms full fourteen-entry currents by directly
summing the actual rate on all 14^4 contexts for twenty incoming/outgoing
cases, before taking the Z12 projection. Integer common denominators and
a checked accumulation bound make this exact. It separately checks the
contracted formula, all twelve preparation phases, a two-pair tensor
equality, and the observable trace. Full product equality follows by
factorization; its exponentially large matrix is not materialized.

## Source-bound review and controls

The complete primary note was read at SHA-256
`7cfff2132cf070ee69c5dd80bd868e6a2568bed6343dc99dbf5d388a770c4cf8`.
The actual rate/current premises and the preceding independent operational
scope were reused at the identities in PRE_SOURCES.json. The full independent
derivation and controls were sealed before new author code/results access:
PRE_COMPARISON_SEAL.json SHA-256
`387e46f74ee1e1814f9fe42555bceb50b9bbbf82a824cc766c989cee248078fa`
(four sources, seven artifacts).

The complete final author checker, complete results, both streams and
receipt were subsequently read and authenticated. Checker SHA-256 is
`df54440ecf138348ece9aefda505634db3be394e0e2597a6730a3f03617a43f7`;
result SHA-256 is
`d11926fd793bed41bdb495e89dbd1fd3cc1455c004d529bc300b1c92238e5a23`.
Every supplied and embedded source binding agrees. The selective comparison
checks all 24 reported matrices/characters, the zero projection and rank-two
trivial projection, all 56 minors, twelve directional derivative rows, and
the final exact fractions against the independently sealed calculations.
No consequential prose/code drift was found. The author suite was not
rerun or imported; authentication is distinguished from the independent
mathematics and exact recomputations.

Both independent and comparison executions succeeded on their first runs,
with empty stderr; no failed attempt was discarded. Full sources, outputs,
logs and command receipts are retained. FINAL_SEAL.json authenticates this
packet and preserves the pre-comparison evidence unchanged.

## Boundaries

Equal complete encoded inputs cannot receive the two different Q12
assignments from a single density-operator evolution with identical settings
and no extra preparation information. A fixed basis or endpoint convention
change applied consistently preserves that equality. Input-correlated
environments, retained classical labels, count conditioning or other
nonproduct preparations can change the full inputs; they are outside this
comparison. Larger blocks, a different U, extra readable state information,
restricted preparation domains and different generators remain open.

This check neither supplies quantum dynamics nor excludes the separate
positive quantum constructions. It establishes no general impossibility,
physical-emergence result, native formation law or broad no-go completion.
No primary source, Git state, PR, publication or audit status was changed.
No further research was added after this packet.
