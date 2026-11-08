# Independent Haar check of the two-square patch

Source: main `f5af11cd0102cfd0b51aef0911f600130bf5beb1`; raw specification
`CHECKER_SPEC.md`, SHA-256
`a6dd198b4655cdc66e6d3db21eef18b64f8130d495d11bd3092e687383dfa3e7`.
The checker is a separate restricted-input context of the same model family,
retaining the inherited configured model and effort. No primary worktree,
primary implementation, output, or conclusions have been inspected. The host
does not expose a more specific model/effort receipt in this subagent context.
This is a bounded research check, not an audit or a retained-status decision.

## Current checkpoint

The analytic derivation below was written before any primary comparison.
It closes the sector, matrix, commutator, and exchange questions within the
specified seven-link model. The final executable Haar certificate completed
with 19 successful software/consistency checks, two rejected scientific-input
mutations, and a rejected missing-term tamper. Its exact values agree with the
derivation. Both numerical leases were released. No primary comparison has
been performed, and no physics premise is derived from the repository's axioms.

The decisive route is SU(2) fusion at each of six vertices followed by Haar
index contractions, not five-state local-matrix sparse action. The prospective
failure points are all-six-vertex Gauss constraints, loop orientation,
trace-plus-adjoint normalization, and the dimension factor in the common-link
integral. A contradiction in any of those checks would reopen the matrices.

## Input, boundary conditions, and normalization

Write the seven group variables as

`a=g_AB, b=g_BC, d=g_DE, e=g_EF, u=g_AD, v=g_BE, w=g_CF`.

Every one of A,B,C,D,E,F has an independent SU(2) gauge transformation. There
are no matter charges and no external links. In particular, Gauss law is not
omitted at the boundary. The link Hilbert space is the orthogonal sum of the
constant representation and the four matrix coefficients of spin one-half.
The latter is one `V_(1/2) tensor V_(1/2)^*` under the two endpoint actions,
not four independent representation labels.

Normalized Haar measure is uniform on the unit three-sphere in the supplied
coordinates. Sign symmetry and coordinate symmetry give

`integral x_mu = 0`, `integral x_mu x_nu = delta_(mu,nu)/4`,
`integral x_mu x_nu x_rho = 0`.

Thus `<2 x_mu, x_nu * 1> = delta_(mu,nu)/2`. Projection of multiplication
by `x_mu` has exactly the two matrix elements `1/2` connecting the constant
and `2 x_mu`; its matrix elements within the four nonconstant states vanish.
This derives the supplied `P_mu` normalization directly from Haar moments.

Let `P` be the tensor product projection onto the seven retained link spaces.
For a simple loop, every edge occurs once. Therefore contraction of the color
indices commutes with these separate link projections, and its projected
trace is `P M_W P`, where `M_W` is ordinary multiplication by the classical
Wilson trace. Every SU(2) Wilson trace is real, so the specified magnetic
operator is `B_p=2 P M_(W_p) P`. The factor two is essential: it is the
trace plus adjoint, with no division by two. The link projection is invariant
under both endpoint actions, so these operators preserve the Gauss sector.

## Complete Gauss sector

For a given choice of retained link representation, count the occupied
(spin-one-half) links at each vertex. A vertex with zero occupied links has
one invariant. One or three spin-one-halves has no singlet, while two have
one singlet. This follows directly from
`1/2 tensor 1/2 = 0 direct-sum 1` and the fact that an odd number of
half-integral spins has no integral-spin singlet. All vertices here have
degree at most three, so every admissible occupied subgraph has even degree
and its intertwiner multiplicity is one.

The four admissible edge sets are:

| State | Occupied links | Number |
|---|---|---:|
| `empty` | none | 0 |
| `L` | AB,BE,DE,AD | 4 |
| `R` | BC,CF,EF,BE | 4 |
| `O` | AB,BC,CF,EF,DE,AD | 6 |

Completeness can also be counted as the binary cycle-space dimension
`7-6+1=2`, hence four even subgraphs on this connected graph. There is no
fifth state with all seven links occupied: B and E would each carry three
spin-one-halves and violate Gauss law. Different spin assignments are
orthogonal summands, and each of the four surviving intertwiner spaces is
one-dimensional, so the full gauge-invariant patch Hilbert space has
dimension four, not merely a four-state subspace.

Choose the real wavefunctions

```
empty = 1
L = tr(u^-1 d^-1 v a)
R = tr(v^-1 e^-1 w b)
O = tr(u^-1 d^-1 e^-1 w b a).
```

These use precisely the specified `F_n ... F_1` multiplication order.
They are in the retained tensor product and obey all six Gauss laws. Each
nonempty loop has norm one: integrate all but one loop variable using Haar
invariance, leaving `integral [tr(g)]^2 = 4 integral x_4^2 = 1`.
Different states have an edge present in just one of them, whose single
fundamental matrix coefficient integrates to zero. This is an orthonormal
basis. `|empty>` is an empty-flux reference, not a selected physical vacuum.

## The shared-link integral and all matrix elements

Set `A=a u^-1 d^-1` and `D=e^-1 w b`. By cyclicity,
`L=tr(v A)`, `R=tr(v^-1 D)`, and `O=tr(A D)`.
The exact fundamental Haar contraction is

```
integral dv v_ij (v^-1)_kl = (1/2) delta_il delta_jk,
integral dv tr(v A) tr(v^-1 D) = (1/2) tr(A D).
```

The sign is positive. It is the ordinary matrix/dual-matrix contraction;
no epsilon tensor sign is inserted. Consequently
`integral L R O = (1/2) integral O^2 = 1/2`.

Every magnetic matrix element is `2 integral W_i W_p W_j`.
An edge occurring in an odd number of the three functions gives zero by
`g -> -g`; hence the only allowed transitions toggle the corresponding
cycle's edge set. The nonzero overlaps are
`<L|B_L|empty>=2`, `<O|B_L|R>=1`,
`<R|B_R|empty>=2`, `<O|B_R|L>=1`, and their adjoints.
In the declared order `(empty,L,R,O)`, the exact matrices are

```
B_L = [0 2 0 0]     B_R = [0 0 2 0]
      [2 0 0 0]           [0 0 0 1]
      [0 0 0 1]           [2 0 0 0]
      [0 0 1 0]           [0 1 0 0]

E = sum_links E_link^2 = diag(0,3,3,9/2).
```

The electric eigenvalues are the occupied-link counts times `3/4`.
The commutator is

```
C = [B_L,B_R] = 3 (|L><R| - |R><L|)
  = [0  0 0 0]
    [0  0 3 0]
    [0 -3 0 0]
    [0  0 0 0].
```

It annihilates `|empty>` and `|O>`, but is nonzero on the full Gauss sector.
Testing it only on the empty-flux reference would miss noncommutativity.

These signs are tied to the explicit Wilson-trace basis. If another basis
uses phases `|i>'=s_i |i>`, every operator and the exchange map must transform
as `M'_(ij)=s_i^* M_(ij) s_j`. A sign difference is reconciled by that same
diagonal conjugation on all operators, not by comparing entries in isolation.
Reversing a loop's traversal does not itself introduce a sign, because
`tr(g^-1)=tr(g)` for SU(2). The product of the four transition coefficients
around `empty -> L -> O -> R -> empty` is the phase-independent positive
number `4`; changing just one transition sign cannot be removed by rephasing.

## Exact spatial exchange being tested

Reflect the patch in `x=1`: A exchanges with C, D with F, and B,E stay fixed.
The oriented links transform as
`AB <-> BC^-1`, `DE <-> EF^-1`, `AD <-> CF`, with BE fixed.
The geometric reflection reverses both square-loop orientations. Reality
of the SU(2) trace gives the unitary involution

```
X|empty>=|empty>, X|L>=|R>, X|R>=|L>, X|O>=|O>.
X B_L X = B_R,  X B_R X = B_L,  X E X = E,  X C X = -C.
```

This tests one reflection exchanging the two squares of this finite planar
patch. It is not a representation or a test of the full three-dimensional
cubic group, nor a construction of a homogeneous three-dimensional update.

## Update choices

Use equal real step parameter `t` and the unitary sign convention
`exp(-i t B)`. At fixed couplings, exchange symmetry means `X U X = U`.
Changing the Hamiltonian sign only changes the corresponding odd Taylor
coefficients, not the symmetry conclusions.

1. Ordered product `U_LR(t)=exp(-it B_L) exp(-it B_R)`.
   Exchange sends it to `U_RL(t)`, and
   `U_LR-U_RL = -t^2 C + O(t^3)`. It is therefore not exchange invariant
   for all t. A fully exact witness at `t=pi/2` is
   `U_LR|L>=-|R>` but `U_RL|L>=i|O>`.
   This is a generic small-step failure, not a statement that every nonzero
   step fails: at `t=n*pi` both single-square exponentials are diagonal in
   this basis and the ordered products commute.

2. Left-centered Strang product
   `S_L(t)=exp(-it B_L/2) exp(-it B_R) exp(-it B_L/2)`.
   Exchange gives the right-centered `S_R(t)`, not the same word.
   Direct expansion through order three gives
   `S_L-S_R = -(i t^3/8)[B_L+B_R,C] + O(t^4)`.
   Its leading action on the empty-flux reference is
   `(3i/4)t^3 (|L>-|R>)`. Thus time symmetry of a palindrome does not
   establish spatial exchange symmetry. An exact witness is
   `S_L(pi)=diag(1,-1,1,-1)` and
   `S_R(pi)=diag(1,1,-1,-1)`.
   Strang is exchange invariant through second order, and has accidental
   equalities such as `t=2n*pi`, where both sides are identity.

3. Joint exponential `J(t)=exp[-it(B_L+B_R)]`.
   Its generator commutes with X, so it commutes with X for every real t,
   exactly. The same proof covers
   `exp[-it(kappa E + beta(B_L+B_R))]` for real kappa,beta.
   With unequal fixed square coefficients, the generator is exchange
   invariant only when those coefficients coincide; exchanging the
   coefficients as well describes covariance of a family, a different
   statement. At isolated times even a noninvariant generator can have an
   invariant exponential, so the generator test is a statement about the
   entire one-parameter family.

The finite-patch exchange test supplies neither a unique physical update nor
a physical-law selector. All matrices above follow conditionally from the
specified projected-Haar model and its boundary Gauss laws. No vacuum,
continuum, mass-gap, or three-dimensional claim follows.

## Machinery provenance and search

The source of the general spin-network organization is the standard compact
group representation construction; John C. Baez's *Spin Network States in
Gauge Theory*, [arXiv:gr-qc/9411007](https://arxiv.org/abs/gr-qc/9411007),
was found by the targeted query `SU(2) lattice gauge theory spin network
basis Haar measure orthogonality fundamental representation arxiv` on
2026-11-07. The search result describes a fixed-graph orthonormal basis.
Only that bibliographic/abstract statement was inspected; no coefficient or
patch calculation was imported. The needed special case is fully derived
above from singlet fusion and elementary Haar moments. The supervisor owns
campaign-wide repository/open-PR search provenance; this checker deliberately
did not inspect primary or related result artifacts before its derivation.

Applicable operating sources were the checkout's `AGENTS.md`,
`SCIENCE_WORKFLOW.md`, freshness procedure, `workhorse/SKILL.md`, relevant
Lab Operation rules, and `lab_ops.py`. The installed workhorse copy differs
from the checkout; the repository copy at the pinned revision controls this
check. No instruction file was edited.

## Execution and mutation evidence

The executable is
`scripts/gb1_cf_two_plaquette_haar_check_2026_11_07.py`, final SHA-256
`daa78235e9f850c486eba543cde39df04240ec6095f3db1998931874e80dfa66`.
Full preflight, lease, and runner output is preserved in
`logs/runner-cache/gb1_cf_two_plaquette_haar_check_2026_11_07.txt`.
The final run exited zero, used 25,509,888 peak RSS bytes and 0.122056 seconds
of measured runner time, and recorded 19 successful software/consistency
checks with no failed checks. Preflight allowed the job; its memory-cap
probe was unavailable, so the runner used an 85-second alarm and RSS checks.
All six math-thread environment variables were one. The unique
`gb1cf-haar-checker-20261107-run2` lease was held during execution and released
afterward. The earlier run is retained in the same log and is identified by
its different source hash; only run 2 certifies the final source.

The runner expands ordinary 2x2 color traces through the quaternion basis
`e_0=I, e_j=i sigma_j`, where
`e_j e_k=-delta_jk I-epsilon_jkl e_l`. It retains 64 monomials per square
trace and 1,024 for the outer trace. Shared coordinate indices are contracted
with `delta_mu,nu/4`; it never constructs the seven-link five-state action.
All decisive values use `Fraction` arithmetic; exact complex witnesses use
pairs of rational matrices. The five-state projected-coordinate matrix is
computed separately only to check the local normalization against the raw
specification, and never feeds the loop matrix calculation.

The demonstrated rejection paths are:

| Probe | Derived value | Proposed defect | Observed behavior |
|---|---|---|---|
| Local projected coordinate | `1/2` | replace by `1` | raises `RejectedCandidate` |
| Shared-link color contraction | `(1/2) O` | replace by `O` | raises `RejectedCandidate`; all-scalar monomial is `1`, proposed `2` |
| Missing contraction term | all-scalar coefficient `1` | omit that key, giving `0` | raises `RejectedCandidate` |

These test the exact candidate-validation path, not just a favorable final
number. Full matrices and Taylor coefficients are emitted separately from
check counts. The symmetry failures are computed findings, not mandatory
scientific outcomes asserted by a PASS counter.

There is no unresolved calculation inside the declared bounded patch scope.
The remaining handoff is the supervisor's comparison against the primary's
frozen artifacts, including a common-basis sign reconciliation if needed.
Same-family shared model biases, shared raw premises, and the absence of a
different-provider check remain independence limitations. No audit grade,
retained status, or broader physical conclusion is claimed.
