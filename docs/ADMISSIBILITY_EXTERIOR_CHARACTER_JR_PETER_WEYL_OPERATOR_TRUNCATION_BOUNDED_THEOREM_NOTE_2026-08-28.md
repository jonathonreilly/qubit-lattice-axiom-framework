---
claim_id: admissibility_exterior_character_jr_peter_weyl_operator_truncation_bounded_theorem_note_2026-08-28
claim_type: bounded_theorem
claim_scope: "For the supplied finite O(3) ladder transfer and its exact retain-every-r isometry J_r, truncate each disclosed exterior-character temporal crossing and plaquette half-action by a finite positive Peter--Weyl packet before any Haar contraction. Prove a pointwise sandwich for the complete shared-frame physical kernel, an explicit retained-cell/history-depth accumulation bound, relative operator- and Hilbert--Schmidt-norm errors, and a top-operator-norm-normalized transfer comparison. The cutoff grows logarithmically with rq at fixed tolerance. This is conditional on the supplied action, Haar measure, temporal extension, and projector; it does not select an action, physical time, continuum limit, Lorentzian theory, gravity, or matter dynamics."
depends_on:
  - admissibility_exterior_character_bounded_degree_ladder_history_message_flow_bounded_theorem_note_2026-08-28
  - minimal_axioms
runner: scripts/admissibility_exterior_character_jr_peter_weyl_operator_truncation_2026_08_28.py
independent_checker: scripts/admissibility_exterior_character_jr_peter_weyl_operator_truncation_independent_2026_08_28.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_bounded_degree_ladder_history_message_flow_bounded_theorem_note_2026-08-28
target_blocker_text: "Prove an error bound after the shared-frame physical marginal (17), uniformly in the number of retained cells, for an explicitly disclosed finite Peter--Weyl/spin-network truncation or another local comparison."
source_of_blocker_text: user_goal
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Use the finite-volume operator estimate only inside an explicitly supplied scale family; a continuum or physical-time claim still requires spacing, coefficient flow, and state/observable control not present here."
conditional_surface_status: "exact finite positive Peter--Weyl truncation of the supplied J_r/shared-frame transfer, with rq-dependent relative operator error and no selected action, continuum, or physical-time theorem"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the exterior-character exponential has a positive finite tensor-power packet with an exact Poisson remainder; factorwise order survives the complete Haar marginal and gives the stated kernel and operator bounds"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Exterior-character `J_r` Peter--Weyl operator truncation

**Date:** 2026-08-28

**Type:** `bounded_theorem`

**Status:** `proposed_retained`

## Result up front

The parent ladder transfer's residual admits a direct finite-representation solution on
every supplied finite ladder.  Replace every actual temporal crossing and
every actual spatial half-action by the finite positive character packet
defined below, *before* integrating a hidden rung or a projector frame.  Keep
the same packet while composing strips: direct and staged evaluation then
only reorder the same finite sums and normalized Haar integrals.

For `L=rq`, the resulting kernel is a finite spin-network kernel for the
actual `J_r`-compressed transfer, including the common projector frame at
each retained rung.  If `K_(r,q)` is the exact raw kernel and
`K_(r,q)^K` is the common-cutoff kernel, then pointwise

```text
gamma_(K,r,q) K_(r,q) <= K_(r,q)^K <= K_(r,q),       (1)
```

with an explicit `gamma`.  Consequently the complete physical transfer,
not merely an auxiliary bond message, satisfies a relative operator-norm
bound.  The error includes all retained cells and all `r` fine cells in each
strip.  The cutoff certified by this theorem depends on `rq`: for fixed
tolerance it grows logarithmically in `rq` once the local couplings are fixed.

This closes the finite-ladder truncation obligation quoted in the front
matter.  It does not create a scale family or a continuum theorem.

## Exact dependency and supplied boundary

The sole scientific parent is the
[bounded-degree ladder history-message theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_BOUNDED_DEGREE_LADDER_HISTORY_MESSAGE_FLOW_BOUNDED_THEOREM_NOTE_2026-08-28.md).
Import from that theorem only the following disclosed data:

1. `G=O(3)` with normalized product Haar measure;
2. a supplied member `n>=1` and supplied coefficients `kappa,beta>0`;
3. the supplied exterior-character action density `f_n(Q)`;
4. the common linkwise temporal projector and the local plaquette
   half-actions;
5. the open ladder, residual projector `P_lr`, retain-every-`r` isometry
   `J_r`, and complete shared-frame kernel (17).

No coefficient is fitted here, and the construction does not select the action.
The temporal extension is a supplied Euclidean comparison device, not a
derivation of physical time.  The only axiomatic dependency remains
the [four named minimal axioms](MINIMAL_AXIOMS_2026-06-29.md); no axiom or
primitive is changed.

The archived Poissonized occupation note is discussed below as prior art,
not imported as a premise.  In particular, its recorded authority `none`
cannot discharge any step of this proof.

## Proof-obligation graph

The exact target is: **for every supplied finite `O(3)` ladder with `L=rq`,
construct an explicitly finite local Peter--Weyl truncation of the actual
`J_r` shared-frame physical transfer and bound its complete operator error,
with the dependence on `r`, `q`, coupling, and tolerance displayed.**

| obligation | status here | discharge |
|---|---|---|
| identify a globally nonnegative character coordinate on both components of `O(3)` | proved here | exterior identity (3)--(5) |
| construct a finite positive local character packet | proved here | exponential packet (7) |
| control its relative local remainder | proved here | monotone Poisson ratio (8)--(10) |
| show the packet is applied to the actual `J_r` graph with no lost or duplicated shared frame | parent construction plus proof here | census (11), shared-frame ownership, and finite Fubini |
| accumulate every fine-cell and retained-cell error after the complete marginal | proved here | kernel sandwich (12)--(14) |
| lift kernel order to the complete physical operator norm | proved here | lattice domination (15)--(18) |
| disclose a finite representation alphabet and an explicit tolerance cutoff | proved here | (19)--(22) |

The graph is acyclic: the local character identity produces the packet; the
packet and parent factor graph produce the kernel order; the kernel order
produces the operator estimates.  The proof never invokes the target estimate
as an input.  Degenerate limits `kappa=0` or `beta=0` follow by setting the
corresponding `s` and `delta` to zero, although the supplied parent assumes
strictly positive coefficients; `r,q>=1` and finite `K>=0` are covered.

There is no missing lemma inside this finite-ladder target.  The strongest
missing lemma for any larger TOE claim is instead a supplied or derived scale
family that controls spacing, coefficient flow, states, and observables as
volume and refinement vary.  That lemma is strictly stronger than the target
here and is not used to prove it.

## Full `O(3)` exterior character

Let `V` be the defining real three-dimensional representation and set

```text
Lambda = direct_sum_(a=0)^3 wedge^a V,       dim Lambda=8.  (2)
```

The elementary exterior-algebra identity is global on both components:

```text
chi_Lambda(g)=det(I+g).                              (3)
```

If `det g=+1`, the eigenvalues are `1,e^(i theta),e^(-i theta)`, so
`chi_Lambda(g)=8 cos^2(theta/2)` lies in `[0,8]`.  If `g` is in the
improper component, an eigenvalue is `-1`, hence `chi_Lambda(g)=0`.
Thus, with

```text
u_n(g) = (chi_Lambda(g)/8)^n,                        (4)
```

one has `0<=u_n<=1` everywhere on `O(3)`.  The supplied member identity is

```text
Q(g)=16-2 chi_Lambda(g),
f_n(Q(g))=(16/n)(1-u_n(g)).                          (5)
```

In particular the improper component has `f_n=16/n`; it has not been
discarded or silently replaced by `SO(3)`.

## Finite positive local character packet

Remove only the already-known temporal normalization scalar and define

```text
bar w(g) = Z_kappa w(g) = ell_(s_kappa)(g),
m(g)                         = ell_(s_beta)(g),
s_kappa = 16 kappa/n,        s_beta = 8 beta/n,
ell_s(g) = exp[-s] exp[s u_n(g)].                    (6)
```

For integer `K>=0`, define the disclosed local cutoff

```text
ell_s^K(g)
 = exp[-s] sum_(k=0)^K s^k/(k! 8^(n k))
                  chi_(Lambda^(tensor n k))(g).      (7)
```

Here the literal string `chi_(Lambda^(tensor n k))` denotes the character
of `Lambda^(tensor n k)`; `k=0` is the trivial representation.  Equation
(7) is therefore a finite Peter--Weyl packet with nonnegative coefficients.
It is also pointwise nonnegative because it is a partial exponential in
the nonnegative number `u_n(g)`.

Put

```text
delta_(s,K)
 = 1-exp[-s] sum_(k=0)^K s^k/k!.                    (8)
```

The relative partial-sum ratio
`exp[-s u] sum_(k=0)^K (s u)^k/k!` is decreasing for `0<=u<=1`.
Consequently

```text
(1-delta_(s,K)) ell_s(g) <= ell_s^K(g) <= ell_s(g),
0<=delta_(s,K)<=s^(K+1)/(K+1)!.                     (9)
```

The first value in (9) is sharp at `u_n=1`; the last inequality is the
Taylor remainder after multiplying by `exp[-s]`.  This is a relative local
bound, not an uncontrolled absolute tail.

Allowing separate cutoffs, abbreviate

```text
delta_kappa=delta_(s_kappa,K_kappa),
delta_beta =delta_(s_beta,K_beta).                  (10)
```

## Truncating the actual `J_r` network

Take `L=rq` exactly as in the parent theorem.  In either the original-link formula or
its rail-forest gauge form, replace every `bar w` by
`ell_(s_kappa)^(K_kappa)` and every spatial `m` by
`ell_(s_beta)^(K_beta)`.  Do this before all hidden-rung and projector-frame
integrations.

The actual factor census is

```text
temporal crossings:       (L+1)+L+L = 3 r q + 1,
plaquette half-actions:   2L         = 2 r q.        (11)
```

These are the factors of the complete parent kernel, not factors of a
surrogate one-strip operator.  Each hidden column is integrated with the
same Haar measure as before.  At every join, the shared retained projector frame is integrated once.
Multiplying two already frame-marginalized strip
kernels would instead duplicate that frame and does not define this
transfer.

Direct evaluation and the history-message evaluation remain identical by
finite Fubini: they contract one and the same finite tensor network.
No representation projection is re-applied after a strip is contracted.  A
fresh cutoff on a generated intermediate message is a different,
generally nonassociative algorithm and is outside the theorem.

This construction is typed to the actual map

```text
J_r^* P_(rq) T_(rq) P_(rq) J_r
```

and, in forest gauge, to its restriction to P_lr.
This is not the auxiliary-message tail of `B^r`.

## Complete shared-frame kernel sandwich

Let `K_(r,q)` denote the complete nonnegative raw kernel obtained from
the parent theorem's equation (17) after replacing all normalized temporal factors `w` by
`bar w`.  Let `K_(r,q)^(K_kappa,K_beta)` denote the complete kernel just
constructed.  Multiplying (9) over the exact census (11) gives an integrand
sandwich.  Normalized Haar integration preserves it, hence

```text
gamma_(K,r,q) K_(r,q)
 <= K_(r,q)^(K_kappa,K_beta)
 <= K_(r,q),                                           (12)

gamma_(K,r,q)
 = (1-delta_kappa)^(3 r q + 1)
   (1-delta_beta)^(2 r q),

epsilon_(K,r,q)=1-gamma_(K,r,q).                       (13)
```

The subscript `K` on `gamma` is shorthand for the disclosed pair of
cutoffs.  Bernoulli's product inequality supplies the useful accumulated
bound

```text
epsilon_(K,r,q)
 <= (3 r q + 1) delta_kappa + 2 r q delta_beta.         (14)
```

This controls both strip depth `r` and retained-cell count `q`; neither is
hidden in an unspecified constant.  The result remains true for every
endpoint configuration, after every hidden column and every common frame
has been integrated.

## Full operator and top-norm comparison

Let `T_(r,q)` and `T_(r,q)^K` be the integral operators with kernels in
(12) on the forest-gauge product-Haar `L^2` space.  Write
`D=T_(r,q)-T_(r,q)^K`.  From (12), for every `F`,

```text
|(T_(r,q)-T_(r,q)^K)F|
 <= epsilon_(K,r,q) T_(r,q)|F|.                       (15)
```

Therefore

```text
||T_(r,q)-T_(r,q)^K||_op
 <= epsilon_(K,r,q) ||T_(r,q)||_op,                   (16)

||K_(r,q)-K_(r,q)^K||_HS
 <= epsilon_(K,r,q) ||K_(r,q)||_HS.                   (17)
```

The second statement follows directly from the pointwise relative kernel
bound.  The first uses positivity preservation of `T_(r,q)` and
`||T|F|||_2<=||T||_op||F||_2`.  No spectral gap is assumed.

The projector is orthogonal and commutes with the supplied physical
transfer.  If `F` is in the range of `P_lr`, then `|F|` is also in that range,
and both `T` and `D` preserve it.  Applying (15) inside that invariant
sublattice proves (16) with the norm of `T` restricted to `P_lr`, not merely
with the larger full-space norm.  By the parent unitary equivalence, the same
relative estimate holds on the original projected ladder space.

Since `T_(r,q)` is nonzero and `epsilon<1`, set

```text
a=||T_(r,q)||_op,       b=||T_(r,q)^K||_op.
```

Equation (16) implies `|a-b|<=epsilon_(K,r,q) a`.  The following argument
applies on either the full forest-gauge space or its invariant physical
subspace, with `a,b` interpreted on that chosen space.  Separately normalizing
the two complete transfers by their own top operator norms gives

```text
|| T_(r,q)/a - T_(r,q)^K/b ||_op
 <= 2 epsilon_(K,r,q).                                (18)
```

This is a genuine complete-transfer comparison.  Its normalization is
not the auxiliary-message Perron vector and no auxiliary eigenfunction is
identified with a physical vacuum or state.

The parent convention used normalized `w`.  There are exactly `3rq+1`
temporal factors, so the raw and normalized complete kernels differ by the
known scalar `Z_kappa^(3 r q + 1)`.  Dividing both exact and truncated raw
kernels by this same scalar leaves (12)--(18) unchanged.  `Z_kappa` is not
being reinterpreted as a transfer eigenvalue.

## Absolute original-transfer bound and Hilbert--Schmidt normalization

The relative order bound above is invariant under the common normalization.
For completeness, an independent telescoping argument gives an absolute
operator bound directly on the parent's original normalized transfer.  Keep
the exact normalization in the truncated temporal weight,

```text
w_K=bar w_K/Z_kappa,
```

rather than renormalizing it by a new truncated partition function.  Young's
inequality and the relative local tail give

```text
||C_w-C_(w_K)||_op <= ||w-w_K||_1 <= delta_kappa,
```

while both convolutions are contractions.  On either spatial slice the exact
and truncated multiplication operators are contractions and

```text
||M-M_K||_op <= 1-(1-delta_beta)^(r q)
              <= r q delta_beta.
```

Telescoping the `3rq+1` temporal factors and the two spatial half-actions,
then applying the orthogonal projector, `J_r`, and the residual physical
restriction, proves for the original normalized physical transfer

```text
||mathcal T_(r,q)-mathcal T_(r,q)^K||_op
 <= (3 r q + 1) delta_kappa + 2 r q delta_beta.       (18a)
```

Equation (18a) is an absolute operator estimate; (16) is the complementary
relative estimate.  The absolute Hilbert--Schmidt estimate has different
normalization bookkeeping.  Since the raw factor-maximum kernel is at most
one on normalized external Haar measure, (12) gives

```text
||mathcal T_(r,q)-mathcal T_(r,q)^K||_HS
 <= Z_kappa^(-(3 r q + 1)) epsilon_(K,r,q).           (18b)
```

The relative Hilbert--Schmidt statement (17) remains invariant under the
common scalar.  Omitting the factor in (18b), or normalizing `w_K` by its own
partition function while retaining the monotone sandwich, would be incorrect.

## Explicit cutoff and volume dependence

For a simple common cutoff put

```text
K_kappa=K_beta=K,
s_*=max(s_kappa,s_beta),
N_(r,q)=5 r q + 1,
d=K+1.                                                (19)
```

Equations (9) and (14) give

```text
epsilon_(K,r,q) <= N_(r,q) s_*^d/d!.                 (20)
```

Using `d! >= (d/e)^d`, a fully explicit sufficient rule for any
`0<eta<1` is

```text
K + 1 >= 2 e s_*,
K + 1 >= log_2((5 r q + 1)/eta).                     (21)
```

Taking integer ceilings gives `epsilon_(K,r,q)<=eta`.  Thus the local
tensor order grows linearly with the supplied coupling scale and only
logarithmically with volume/history depth and inverse tolerance.  The
theorem supplies this explicit cutoff family; it makes no fixed-cutoff
arbitrary-volume estimate.

## Finite spin-network content

Every occupation `k<=K` in (7) is contained in the finite representation
`Lambda^(tensor n k)`.  At a Haar frame, tensor products from incident
factors decompose into finitely many `O(3)` irreducibles, and Haar integration
selects the finite invariant subspace.  With separate cutoffs, the following
uniform local tensor-order bounds hold before contraction:

```text
projector frame:  <=3 n K_kappa,
interior rung:    <=n(K_kappa+2K_beta),
rail incidence:  <=n(K_kappa+K_beta).                (22)
```

For the common cutoff the maximum is `3 n K`.  Boundary incidences can only
lower these bounds.  Hence the truncated network has finite local
representation alphabets and finite rank at fixed `r,q,K`.  Equation (22)
is an incidence/tensor-order bound; it is not a claim that every constituent
has exactly that spin or multiplicity.

The generated intermediate boundary interaction can have more character
channels than a single local packet.  Those channels are retained exactly
during staged contraction.  This is why the construction is associative
without pretending that it closes in the inherited one-density action
family.

## Independent controls and hostile falsifiers

The independent checker uses only Python integers, `Fraction`, finite group
enumeration, and polynomial arithmetic.  It does not import the primary
runner, SymPy, NumPy, or a scratch derivation.  It reconstructs:

1. all 48 signed-permutation `O(3)` frames, including 24 improper frames;
2. (3)--(5) on those frames for `n=1,...,5`;
3. the exact `(3rq+1,2rq)` factor census at four `(r,q)` values;
4. raw fine-link and history-message contractions on a finite `Z_2` control,
   both across hidden columns and across a shared retained column;
5. failure of the deliberately duplicated shared-frame kernel;
6. the pointwise complete-kernel sandwich;
7. the resulting exact `8 x 8` normalized-Haar operator matrix and its
   `4 x 4` global-`Z_2`-even residual-projector compression;
8. the relative Hilbert--Schmidt bound and the exact `Z_kappa^(-7)` raw-to-
   normalized matrix relation for the `(r,q)=(1,2)` fixture;
9. nonnegative finite Fourier coefficients; and
10. failure of a deliberately fresh intermediate polynomial cutoff.

The primary runner binds the note, its scientific parent, minimal-axiom fence, and
independent checker.  Its mutation set separately falsifies the exterior
identity, component coverage, finite packet, Poisson remainder, both factor
counts, shared-frame ownership, no-retruncation rule, accumulated `gamma`,
cutoff, local tensor order, sandwich direction, relative operator theorem,
top normalization, absolute operator/HS normalization, projector typing, independent
reconstruction, prior-art disclosure, volume boundary, actual-kernel reach,
scope, and import integrity.

The finite controls are intentionally not evidence for `O(3)` by sampling.
They are reconstruction and mutation checks for the analytic identities and
the contraction graph proved above.

## Prior-art fence and incremental content

The historical file
`1604_POISSONIZED_OCCUPATION_INTERTWINER_COMPRESSION_NOTE.md` and its intake
surface `HISTORIC_POISSONIZED_OCCUPATION_INTERTWINER_COMPRESSION_NOTE_INTAKE_NOTE_2026-08-05.md`
already record Poissonized occupation cutoffs, finite tensor-network
alphabets, and volume-accumulated tails for a supplied `SU(3)` plaquette
weight.  Their current recorded authority `none` and branch-only status are
respected.  Generic Poisson-tail or finite-network existence is therefore
not claimed as the novelty of this block.

The incremental result here is the exact `O(3)` exterior-character packet on
both connected components, inserted into the actual parent linkwise
`J_r` construction with its exact temporal/half-action census and its shared
projector frames, followed by the pointwise physical-kernel sandwich and the
relative complete-transfer operator and top-norm estimates.  No conclusion
depends on the historical note.

## Honest boundary and non-implication fences

1. **Supplied action:** the action member and coefficients are inputs.  The
   theorem does not select the action or show uniqueness.
2. **Cutoff scope:** the guaranteed fixed-tolerance cutoff in (21) depends on
   `rq`.  Equation (14) is the explicit accumulation estimate proved here;
   no claim about a sharper fixed-cutoff infinite-volume error is made.
3. **Algorithm boundary:** exact staged contraction is allowed; a new
   representation projection at each intermediate history is not covered
   and is generally nonassociative.
4. **Top-state boundary:** (18) compares top operator-normalized transfers,
   not eigenvectors.  No simplicity, spectral gap, or state convergence is
   asserted.
5. **Time boundary:** the extra slice is supplied and Euclidean.  It does not
   identify a physical time, Hamiltonian, or unitary evolution.
6. **Continuum boundary:** no spacing map, coupling flow, infinite-volume
   state, or observable scaling family is supplied, so no continuum limit
   follows.
7. **Gravity boundary:** no Lorentzian metric, gravity dynamics, matter
   sector, stress tensor, or phenomenology follows from this estimate.
8. **TOE boundary:** the theorem repairs one mathematical control bridge in
   the supplied connection-dynamics lane.  It is not a theory-of-everything
   closure claim.

## Certification

Run from repository root:

```bash
python3 scripts/admissibility_exterior_character_jr_peter_weyl_operator_truncation_2026_08_28.py
python3 scripts/admissibility_exterior_character_jr_peter_weyl_operator_truncation_2026_08_28.py --mode independent
python3 scripts/admissibility_exterior_character_jr_peter_weyl_operator_truncation_2026_08_28.py --mutation <name>
```

Acceptance requires the baseline and independent modes to end with zero
failures, every disclosed mutation to fail nonzero at its intended gate, the
generated citation manifest to validate, and the standing documentation and
admissibility checks to remain green.  Audit authority remains separate.
