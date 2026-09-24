---
claim_id: cube_actual_formation_local_density_limit_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical diagnostics alone do not prove the analytic limits or select physical dynamics."
upstream_dependencies:
  - minimal_axioms
  - cube_six_record_rotor_point_spectrum_bounded_theorem_note_2026-09-24
  - finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24
  - cube_two_mark_loop_readout_bounded_theorem_note_2026-09-24
runner: scripts/cube_actual_formation_local_density_limit_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The source argument below comes from the frozen submission, with the narrow corrections identified in the combined review receipt. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. The Hamiltonians, quantum state spaces, instruments, backgrounds and preparations are supplied model assumptions. Fresh canonical controls are distinguished from archived diagnostics; no numerical scan substitutes for the displayed proofs.

# Actual formation on the cube: local density in the joint-spin limit

Root theorem candidate, September 23, 2026. Provisional dependency: the cube
point-spectrum packet is frozen but its independent reconstruction is pending.
The argument below has not yet received a selective independent check.

The time-smearing/commuting-positive-density insight originated in the
independent ring consequence reconstruction, PRE
ba8907a8da440ad8832f86ff42b33b7c90d99082d181d215af43a8b89c11f37c,
whose complete report root read before writing this cube extension. This is
an explicitly source-informed extension, not a claim to have independently
rediscovered that mechanism. The uniform-input version and the time-dependent
cube first-source argument below are new root obligations.

## 1. Statement, supplied premises and embedding

Use the oriented cube with A={0,3,5,6}, the hard-core charge values 0,+1,-1,
total charge four, normalized integer spins, Gauss div E=q-1_A, and the
Hamiltonian and formation instrument of the checked parent effective-target
theorem. Let K,delta,kappa>0 be fixed and

    C=S(S+1), eta=K C=delta/epsilon^2.

The physical P sector has every A occupied. Its record numbers are N=4,6,8.
Use the same five chord fields as in the cube spectrum note, so that

    H_N = l2(Z^5) tensor C^(d_N),  d_4=1, d_6=36, d_8=28.

The finite-spin spaces are their complete physical subspaces with every link
field in [-S,S], not a common small field cutoff. Let Pi_R be projection onto
all these P charge words with max_e |E_e|<=R. R is fixed independently of S;
Pi_R is finite rank and increases strongly to the identity. Microscopic
windows may also include W>0 charge words, whose population vanishes by the
parent target approximation.

Initialize N=4, all A plus and all B vacant, with any fixed normalizable
field density rho_0 of trace one. Use trace-norm convergent physical spin
approximants, such as normalized projections onto the full spin boxes. No
uniform high-field moment condition is required for the asserted strong
semigroup extension. The zero-field vector is a particular allowed input.

The proposed compact ordinary-time conclusion is

    Pi_R rho_S(t) Pi_R -> Pi_R rho_4(t) Pi_R

in trace norm, uniformly for t in [0,T], where

    rho_4(t)=exp(-48 kappa t) exp(-it h_4) rho_0 exp(it h_4),
    h_4=K sum_e E_e^2 + delta H4_(4,rotor).             (1)

All finite-window six- and eight-record densities tend to zero. The trace of
the common local limit is exp(-48 kappa t). Thus for each t>0, the normalized
full densities have no trace-norm convergent subsequence in this embedding.
This is a finite-graph, fixed-scaling and specified-initial-sector theorem;
it does not determine the total six/eight-record probabilities or exclude a
description at growing electric scales. It is not an inconsistency of the
finite-spin model or a statement about all possible theories.

The exact cube point-spectrum result used here is the absence of any
normalizable eigenvectors of H2 on H6. Its proof is the three-fiber polynomial
certificate and finite-Laurent determinant argument, not numerical band
sampling. Treat the conclusion below as dependent on that packet until its
check is complete.

## 2. Uniform bounds and convergence on the six-record core

Write A_S=Pi_1 T_S P on this record sector. In the physical charge/field
basis, each P column has at most six legal outward hops. Each Pi_1 row has
at most three inverse hops returning its one vacant A site to P. Every
normalized integer-spin shift has absolute amplitude at most one. The
row/column bound therefore gives

    ||A_S|| <= sqrt(18),  ||H2_S||<=18.

The Pi_1-to-Pi_2 hopping block has at most three entries per column and six
per row, so its norm is also at most sqrt(18). Consequently ||Z_S||<=18 and

    ||H4_S||=|| (A_S^* A_S)^2 - Z_S^* Z_S/2 || <=486.   (2)

A Pi_1 word has exactly two holes, one on A and one on B. There is at most
one edge joining them. Summing the two resolved newborn orientations gives
sum j^*j<=2I on Pi_1. Their cross-Gram is zero on a fixed edge, including at
finite S. Thus coherent and resolved total losses coincide and

    0<=Gamma_(6,S)=kappa sum B_(e,sigma,S)^*B_(e,sigma,S)
       <=2 kappa A_S^*A_S <=36 kappa I.                (3)

No ring-specific diagonal-loss formula is being used on the cube. Its
different old-hop paths can interfere.

Extend the finite-spin H2,H4 and loss by zero off their reducing physical
spin spaces. They are uniformly bounded; on a finite-field finite-support
core their coefficients converge to the rotor coefficients. Thus H2_S and
H2_S^* converge strongly to H2 and H2^*. The boundedness then gives

    [H2_S,L] -> [H2,L] in operator norm                (4)

for each finite-rank L, first for finite-field vectors and then by density.
These core facts do not require an expansion of the electric correction on
states whose field scale grows with S.

## 3. Uniform time-averaged local escape lemma

Let V_S(t) be the six-record no-event contraction generated by

    -i eta H2_S -i delta H4_S -Gamma_(6,S)/2.

For every fixed finite-rank projection Pi and T<infinity,

    sup_(rho>=0,tr rho<=1, rho physical at S)
       integral_0^T tr[Pi V_S(t)rho V_S(t)^*]dt ->0.    (5)

This is uniform in the initial density, but is time averaged. It asserts no
pointwise escape after a sharp externally imposed six-record restart.

Proof: allow an arbitrary sequence of such rho_S and set
sigma_S(t)=V_S(t)rho_S V_S(t)^*. For any fixed nonnegative C^1 weight w on
[0,T], the positive trace-class operators

    R_S=integral w(t) sigma_S(t)dt

have uniformly bounded trace. Extract a subsequence converging against every
compact operator. One can construct it by a countable physical basis and
diagonal extraction; positivity and bounded finite diagonal sums give a
positive trace-class limit R. This avoids replacing the limit by a singular
non-normal functional on all bounded operators.

Test the no-event equation with a finite-rank finite-field L, multiply by w,
and integrate by parts. After division by eta, the boundary and derivative
terms are bounded by ||L||(2||w||_infinity+||w'||_1)/eta. The H4 and loss
terms are bounded by a constant times ||L||||w||_1/eta using (2)--(3).
It follows that tr([H2_S,L] R_S)->0. Equation (4) implies

    tr([H2,L] R)=0

for all finite-rank L, hence [R,H2]=0. If a positive compact R commuting
with bounded self-adjoint H2 were nonzero, one of its positive eigenspaces
would be nonzero and finite dimensional. It would be invariant under H2;
diagonalizing H2 on that space would give a normalizable H2 eigenvector.
The cube spectral certificate excludes this. Hence R=0.

Every subsequential compact-test limit is zero, so tr(Pi R_S)->0 for the
whole sequence. Taking w=1 proves the integral version directly; more general
L1 weights follow by approximation and the trace bound. If the supremum in
(5) did not tend to zero, a sequence of approximate maximizing densities
would contradict exactly the argument just given. This proves uniformity.

The loss bound also gives tr sigma_S(t)>=exp(-36 kappa t) for trace-one
inputs. Thus the vanishing local time average cannot be explained solely
by depletion into the next record sector. For any fixed Pi,

    liminf integral_0^T tr[(I-Pi)sigma_S(t)]dt
       >= (1-exp(-36 kappa T))/(36 kappa).              (6)

This is a statement about probability outside each fixed field window, not
an assertion of a limiting rescaled field distribution.

## 4. The four-record field and first source

In H4 the unique matter word is q=1_A, and Gauss has zero divergence.
Every oriented A-to-B hop on edge e changes E_e by k_e=+1 or -1. The exact
normalized squared amplitude is

    1-E_e(E_e+k_e)/C

on the physical interval, including the zero amplitude at a forbidden
outward spin-boundary hop. Returning from Pi_1 to P can only undo that hop.
Therefore

    H2_(4,S)=-12I + C^(-1) sum_e E_e(E_e+k_e).

Since k_e=-(1_A(u)-1_A(v)) on oriented u<v, the linear sum equals
-sum_(a in A) div E(a)=0. After removing the irrelevant scalar phase,

    eta(H2_(4,S)+12I)=K sum_e E_e^2                    (7)

exactly on the entire physical spin space.

H4_(4,S) is uniformly bounded and converges strongly on the common field
space to the rotor H4. The latter is a finite sum of shifts. Explicit cube
path enumeration gives

    H4_(4,rotor)=60I-2 sum_(six cube faces p)(W_p+W_p^*). (8)

Indeed there are twelve first hops, and 42 unordered pairs of outward hops
with distinct A sources and B destinations. The diagonal Z^*Z coefficient
is 42 times four, so H4 has diagonal 144-84=60. The alternative pairings
around each of the six faces give the displayed coefficient -2 in each
direction. Formula (1) can instead use the unexpanded exact parent H4;
the convergence proof does not depend on introducing six independent face
variables. There are only five independent circulations.

For a fixed resolved first edge/orientation, there are two legal old-record
destinations. Their final charge words differ, and each unit-rotor path has
unit amplitude. For each channel its Gram is 2I on H4. There are 24 such
channels. For a coherent edge the two orientations have orthogonal output
ranges, so its Gram is 4I. Thus, for either instrument,

    Gamma_(4,rotor)=48 kappa I.                        (9)

At finite S, 0<=Gamma_(4,S)<=48 kappa I and it converges strongly to (9).
The first loss generally depends on field at finite S; an exact finite-S
exponential clock is not asserted on the cube.

Let V=K sum E_e^2, a self-adjoint diagonal multiplication operator with
finite-support core. On the full H4 extend the spin generators as
-i V-i delta H4_(4,S)-Gamma_(4,S)/2. Their spin boxes reduce them and contain
the intended physical evolution. The remaining bounded perturbations are
uniformly bounded and converge strongly. The Duhamel identity, applied to
the compact set of vectors traversed by the limiting semigroup on [0,T],
gives strong convergence uniformly on [0,T]. Bounded-perturbation expansion
also supplies the semigroups without assuming a field-moment bound on the
initial vector. The limiting loss is scalar, yielding (1). Finite-rank and
trace-class approximation prove the density assertion for rho_0.

The first jump maps B_(4->6,j,S) are uniformly bounded and converge strongly
to their rotor versions. Hence the positive source densities

    F_S(t)=kappa sum_j B_(j,S) rho_(4,S)(t) B_(j,S)^*

converge in trace norm, uniformly on compact times, to a continuous F(t).
This follows first for finite-rank initial densities and then by uniform
boundedness/trace approximation. The argument includes the time dependence
of the pre-first-formation quantum field; it does not replace it by a fixed
zero-field source.

## 5. Triangular composition and the actual local limit

The full target has only upward number transitions. Thus

    rho_(6,S)(t)=integral_0^t V_S(r) F_S(t-r) V_S(r)^*dr. (10)

For a fixed finite-field projection Pi, replacing F_S by F changes its
compressed density trace norm by at most T sup_[0,T]||F_S-F||_1. Approximate
the compact continuous positive family F(s) in trace norm by a finite list
of positive source densities F_l. For each t, use a piecewise selection of
that list to approximate F(t-r). The local integral is then bounded by a
finite sum of integrals over [0,T] for constant F_l. Each tends to zero by
(5). The trace approximation error is uniform in t. Positivity gives

    sup_(0<=t<=T) ||Pi rho_(6,S)(t) Pi||_1 ->0.          (11)

After the second formation every site is occupied, so the target Hamiltonian
and later jumps vanish. Therefore

    rho_(8,S)(t)=kappa sum_j integral_0^t
                   B_(6->8,j,S)rho_(6,S)(s)B_(6->8,j,S)^* ds.

For each fixed output window R, a two-link hop/birth path can only enter it
from a fixed enlarged input window, for example R+2. The bounded path count
therefore bounds its window trace by a fixed constant times the input
window trace integrated over time. Equation (11) proves that every fixed
eight-record window tends uniformly to zero as well. No high-field return
through the finite-range endpoint jump is omitted.

Together with (1), this proves the claimed local limit. Its trace is
exp(-48 kappa t). A trace-norm convergent subsequence of the normalized full
densities at t>0 would have exactly these finite matrix elements, hence would
equal rho_4(t). Trace continuity contradicts its trace deficit. The parent
uniform-S deterministic microscopic-to-target estimate is O(epsilon) and
transfers the local limits and this subsequence contradiction to the bare
microscopic densities with the same deterministic initialization.

No normalized microscopic random-stop restart is used. The proof composes
the full target density and its explicitly controlled first source.

## 6. Boundaries, alternatives and remaining work

The result does not specify the six/eight probability split, field values
of order S, semiclassical trajectories, or a limit of unbounded electric
observables. Other scalings, extra local interactions, finite-S dynamics,
and field coordinates that grow with S are not excluded. It also does not
remove the ring's prepared or ordinary finite-window results. The fixed
cube geometry and its absence of point spectrum are load-bearing.

Independent checking is required for the exact cube spectral premise,
uniform-input compactness argument, first-source convergence and composition.
Exact path controls for (2)--(3) and (7)--(9), source-bound receipts and a
written scope stress test must accompany any publication. Until then this
is a coherent provisional extension with those dependencies explicit.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the stated graph, sector, preparation, observation topology and order of limits.
- **N2 — Alternatives:** other laws, preparations, graphs and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not repository axioms.
- **N4 — Dependencies:** companion arguments retain their explicit hypotheses and confer no audit grade.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate proofs; floating computations are not interval enclosures. Archived diagnostic tables remain historical observations.
- **N6 — Resolution:** fixed-time, shrinking-time, fixed-index, growing-index and volume statements must not be interchanged.
- **N7 — Remaining work:** native model selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** this source applies no audit verdict or retained grade.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied quantum model.
- [cube_six_record_rotor_point_spectrum_bounded_theorem_note_2026-09-24](CUBE_SIX_RECORD_ROTOR_POINT_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.
- [finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24](FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.
- [cube_two_mark_loop_readout_bounded_theorem_note_2026-09-24](CUBE_TWO_MARK_LOOP_READOUT_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.

## Source and verification

Source PR #8839, frozen head `8ccef7097deb77fe79f0d9406eef7d5c6e4962bd`. Complete original path dispositions and recovery branches are retained in the combined receipt. Review and affected-fix confirmation use the same primary session without subagents; no formal audit is claimed.

```bash
python3 scripts/cube_actual_formation_local_density_limit_2026_09_24.py
```

The runner executes selected controls in a fresh temporary directory and includes generated result JSON in its authenticated stdout. Source history and deferred diagnostics remain recoverable from the original branch.
