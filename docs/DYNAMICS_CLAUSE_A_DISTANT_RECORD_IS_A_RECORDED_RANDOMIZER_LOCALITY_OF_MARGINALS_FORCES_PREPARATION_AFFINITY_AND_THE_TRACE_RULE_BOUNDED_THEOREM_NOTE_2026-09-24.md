---
claim_id: dynamics_clause_a_distant_record_is_a_recorded_randomizer_locality_of_marginals_forces_preparation_affinity_and_the_trace_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted. The Hilbert-space kinematics that the dynamics clause of open PR 9040 brings with it: qubit density operators, tensor-product composition and purifications (the axioms fix no cross-site composition law). The compression update of open PR 9041 with its distant part (D-perm): a record projects the joint state and the unrecorded parts take their conditional states. A site's law is a function of its own conditional state (D-tr). Locality of marginals at equal time (D-loc): at the moment a distant record forms, a site's marginal record distribution does not depend on whether, or along which axis, it forms. Results. (i) The clause carries purifications: the Heisenberg bond at J t = pi is the swap up to phase, and partial swaps prepare every reduced Bloch length. (ii) A record on a purifying partner realizes every two-point pure decomposition of a qubit state (200 random chords, deviation 1e-15). (iii) So D-loc makes the law affine on the Bloch ball; with a normalized antipodal menu it is (1 + lambda r.m)/2. Given D-perm's distant update, D-loc and affinity are equivalent: the distant record is the autonomous randomizer the landed affine/Born note asks for, and D-loc restates affinity as a locality reading. (iv) D-perm's support condition (the compression must exist whenever q can form) forces lambda = 1 and E_q = P_q for any two-outcome effect. (v) A tanh deformation of the landed exp(k n.m) counterkernel and a cubic deformation, which pass the landed note's conditions, shift the site's marginal by 0.06 to 0.2 with the distant record and its axis. (vi) With the partner's weights from the same law, D-loc passes only lambda = 1 and lambda = 0, and the support condition removes lambda = 0. (vii) The distant update carries the argument: under a replacement update that keeps only the lock, anti-Born and tanh laws pass D-loc, differing from the trace rule by up to 0.93 and 0.15. (viii) D-loc holds at equal time only: in a four-site Heisenberg chain a record at distance 3 shifts site 0's later Bloch vector, growing as t^3. This is the standard no-signalling route to the trace rule inside supplied quantum kinematics. No derivation of the kinematics, D-perm, D-tr, D-loc, the menu or the formation rate is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_a_distant_record_is_a_recorded_randomizer_2026_09_24.py
---

# A distant record is a recorded randomizer

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a consistency derivation of preparation affinity inside supplied
quantum kinematics, with finite certificates; unaudited.

## Result

The landed
`ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`
finds that the Born law's missing rung is **preparation affinity**: the law
must be affine when the condition it depends on is itself a physical
mixture. Covariance, endpoint normalization and exclusion do not force this.
Nonlinear kernels such as `exp(k n·m)` survive all of them. The landed
note's first obligation asks for "an autonomous recorded randomizer" that
proves affinity.

Inside the kinematics that the dynamics clause brings with it, a distant
record is such a randomizer:
- **Carrying.** The clause can move an entangled partner of a condition
  qubit to any distance, one bond at a time, with each bond evolved to a
  swap.
- **Steering.** Under the compression update, recording that partner
  leaves the condition qubit at either end of any chord through its state,
  with the chord's weights.
- **Locality of marginals.** Read locality as saying that, at the moment a
  distant record forms, the site's marginal record distribution cannot
  depend on whether or how it forms (D-loc). Then the law agrees with its
  chord averages everywhere, so it is affine.
- **The trace rule.** An affine law on an antipodal menu is
  `(1 + λ r·m)/2`.
- **Orientation.** The compressed state must exist whenever a record can
  form. That sets `λ = 1`, and for any two-outcome effect it forces
  `E_q = P_q`. This is the Born law: neither anti-Born nor a weaker
  contrast.

A deformed law, in contrast, lets the distant party signal.

**What this is and is not.** It is the standard no-signalling route to the
trace rule, placed in the framework. The quantum kinematics, the distant
update and the premise that the law sees the site's conditional state are
all supplied. Given the distant update, D-loc and affinity are equivalent.
So D-loc *restates* affinity as a locality reading ("an unrecorded partner
acts like a recorded-then-forgotten one"); it does not reduce it to
something weaker. What the framework gains is an autonomous randomizer, and
one reading that also constrains the dynamics (open PR 9084).

## Setting and decision points

- **Kinematics (supplied with the clause, open PR 9040; D-dyn).** Qubit
  density operators, tensor-product composition and purifications. The
  Qubit axiom gives each site `M₂(C)`. The four axioms fix no cross-site
  composition law (landed
  `COMPOSITION_LAW_SELECTION_GRADED_ZEROS_ORDER_BLIND_RULES_BOUNDED_THEOREM_NOTE_2026-09-13.md`).
  The tensor product comes with the clause, which acts on it.
- **Compression updates (open PR 9041; D-perm).** A record `q` projects
  the joint state: the recorded site ends in `P_q` (the lock), and the
  unrecorded parts take their conditional states (the distant update). The
  compressed state must exist whenever `q` can form (the support
  condition).
- **The law sees the conditional state (D-tr).** The law `P(+m | r)` is a
  function of a condition state with Bloch vector `r`. That can be the
  site's own state or a neighbour's. It is normalized over the antipodal
  menu `{+m, −m}` (D-menu).
- **Locality of marginals at equal time (D-loc).** At the moment a distant
  record forms, a site's marginal record distribution does not depend on
  whether, or along which axis, it forms.
  - This is how this note reads the Lattice axiom's physical locality
    together with Admissibility's neighbour determination.
  - It is recorded as a decision point, not derived from the axiom text.
  - It is an equal-time statement. Later, the dynamics carries influence
    from the record's site to others (Theorem 7). That is causal
    propagation, not signalling by the record.

None is adopted.

## Theorem 1 — the clause carries purifications

The Heisenberg bond `J s·s = J(SWAP/2 − 1/4)` evolved for `Jt = π` is the
swap, up to a phase. A chain of such steps moves a qubit's entangled
partner as far as needed, with the bonds switched one at a time. The
antiferromagnetic pair ground state of open PR 9043 is a singlet. Partial
swaps `e^{−iθ SWAP}` acting on `|↑↓⟩` prepare every reduced Bloch length
from 1 down to 0. So every qubit state has a purification whose partner the
clause can place at any distance.

## Theorem 2 — a distant record steers every chord

Let `ρ = p ψ₁ + (1 − p) ψ₂` be any chord through a qubit state. Its
endpoints are pure, and `p` is fixed by where `ρ` sits.

Purify it as `√p |ψ₁⟩|0⟩ + √(1 − p) |ψ₂⟩|1⟩`. Under the compression update,
recording the partner in `{|0⟩, |1⟩}` leaves the qubit in `ψ₁` with
probability `p` and in `ψ₂` with probability `1 − p`.

Any such purification is related to one the clause can distribute by a
unitary on the partner, and that unitary only changes which basis the
record uses. ∎

## Theorem 3 — locality of marginals forces affinity

Let the site's law be `P(+m | ρ)`, a function of a condition state `ρ`.

**Two ways to compute the marginal at the moment the partner records.**
- If the distant partner forms no record, the site sees the reduced
  state `ρ`, and its marginal is `P(ρ)`.
- If the partner records, the site sees `ψ_b` with probability `p_b`, and
  its marginal is `Σ_b p_b P(ψ_b)`.

D-loc makes these equal on every chord (Theorem 2). A function on the Bloch
ball that equals its chord interpolation everywhere is linear along every
chord, and hence affine.
- With the menu normalized, `P(+m | r) = (1 + λ r·m)/2`.
- Covariance rules out other affine forms, as in the landed note's
  `q = c + b n·m`.
- Conversely, an affine law passes D-loc on every chord. So, given the
  distant update, D-loc and affinity are equivalent. ∎

## Theorem 4 — the support condition fixes the orientation

Under D-perm, a record `q` leaves the state `P_q ρ P_q / Tr(P_q ρ)`. That
state must exist whenever `q` can form. So `P(q | ρ) > 0` requires
`Tr(P_q ρ) > 0`.
- **The menu law.** At the antipodal pure state `ρ = P_{−q}`,
  `Tr(P_q ρ) = 0`, so `P(q | −q) = (1 − λ)/2` must vanish. Hence `λ = 1`.
- **Any two-outcome effect.** Take `E_q` and `E_{−q} = I − E_q`. The
  requirement forces `Tr(E_q P_{−q}) = 0` and `Tr(E_{−q} P_q) = 0`, so
  `E_q = P_q`. ∎

The orientation comes from this support condition, not from the lock. A
record that simply leaves its site in `P_q`, whatever the prior state, is
compatible with anti-Born odds (Theorem 6).

If the condition is a whole neighbourhood, the same argument applies on its
state space. An affine law there is `Tr(E ρ)` for an effect `E`.

## Theorem 5 — the partner's weights need not be assumed

Theorem 3 used Born weights for the partner's record. Instead, give the
partner the same law as the site.
- A random pure site–partner state.
- The partner records along `n`, with weights from its own reduced state.
- The site's conditional states come from projecting the partner.

D-loc compares the site's marginal with and without that record. The
largest shifts over 400 draws are:

| Law | Largest shift |
|---|---|
| Born (`λ = 1`) | 2e-16 |
| trivial (`λ = 0`) | 0 |
| `λ = 0.5` | 0.10 |
| anti-Born (`λ = −1`) | 0.73 |
| cubic | 0.069 |

So self-consistently D-loc leaves only `λ = 1` and `λ = 0`, and the
support condition (Theorem 4) removes `λ = 0`.

For affinity in general, use partner axes perpendicular to its Bloch
vector. There the menu forces weights of 1/2 for any law, so D-loc gives
Jensen's midpoint equation on chords through the site's state. The
independent check confirms this catches every nonlinear law tested. ∎

## Theorem 6 — the distant update carries the argument

Replace D-perm by a replacement update: a record at the partner sets the
partner to `P_q` and leaves the rest alone, so the site keeps its reduced
state. The lock holds by construction. D-loc also holds, for every law,
because the site's state never changes with the partner's record. So the
anti-Born law and the tanh law both pass. On random reduced states they
differ from the trace rule by up to 0.93 and 0.15.

So the Born law here needs the distant update of D-perm, and its support
condition. It does not follow from D-loc and the lock alone. ∎

## Theorem 7 — D-loc is an equal-time reading

Take a four-site Heisenberg chain in a random pure state. Record site 3
along `z` without selecting the outcome, and compare site 0 with and
without that record as the chain evolves:

| Time | Shift of site 0's Bloch vector |
|---|---|
| 0 | 0 |
| 0.01 | 1.9e-8 |
| 0.05 | 2.4e-6 |
| 0.1 | 1.9e-5 |

The shift grows as `t³` (fitted exponent 3.00), which is the order at which
the dynamics first connects the two sites. At equal time it is zero. So
D-loc holds at equal time, or for records whose sites the dynamics does not
connect. ∎

## What deformed laws do

Two nonlinear laws were tested, both with the Born endpoints:
- the landed counterkernel `exp(k n·m)`, normalized over the menu and
  rescaled, `(1 + tanh(k r·m)/tanh k)/2` with `k = 2`;
- a cubic deformation, `(1 + x + ε(x³ − x))/2` with `ε = 0.3`.

The landed note shows that such laws pass its conditions. Under the
compression update, both let a distant party signal:
- **Record or not.** Whether the partner is recorded shifts the site's
  marginal by up to 0.201 (tanh) and 0.062 (cubic).
- **Which axis.** The choice of recording axis shifts it by up to 0.166
  (tanh) and 0.057 (cubic).

The shift grows with the deformation: 2.5e-3, 2.3e-2 and 6.2e-2 at
`ε = 0.01, 0.1, 0.3`. It vanishes only at `ε = 0`.

## The landed gate's four obligations

| Obligation (landed note) | Status under the supplied setting |
|---|---|
| 1. An autonomous recorded randomizer or coarse-graining that proves affinity | The distant record is an autonomous randomizer. Given D-perm's distant update, affinity is equivalent to D-loc, so D-loc restates it as a locality reading. |
| 2. The normalized probability identified with the one-neighbour transition density | Replaced, not met: the antipodal menu gives a normalized law directly (D-menu), for a law on the site's quantum state. |
| 3. A repeatability experiment that orients Born rather than anti-Born | Settled by D-perm's support condition (Theorem 4), for a law on the site's quantum state rather than on neighbour possibilities. |
| 4. An autonomous reset or repeat process for stable frequencies | Open PR 9052: frequencies follow the one-shot odds exactly when correlations cluster. |

So the Born law here rests on:
- the supplied kinematics;
- D-perm, with its distant update and support condition;
- D-tr, the law as a function of the site's conditional state;
- D-loc at equal time;
- the antipodal menu.

## Prior art

No-signalling arguments for linear quantum rules are standard (Gisin 1990;
Simon, Bužek and Gisin 2001). With Hilbert-space kinematics given, the
measurement postulates are close to fixed (Masanes, Galley and Müller
2019). These are cited as prior art, not as premises.

## Checks

The runner has 9 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| Purifications | `|U − phase·SWAP|` 3.4e-16 at `Jt = π`. Partial swaps give reduced Bloch lengths 1.0, 0.966, 0.866, 0.707, 0.5, 0.259, 0. |
| Steering | 200 random chords, largest deviation 1.1e-15. |
| Trace rule | Largest steered-average discrepancy over 300 chords 1.1e-16. |
| Deformed laws signal | Record-or-not shift: tanh 0.201, cubic 0.062. Axis shift: tanh 0.166, cubic 0.057. |
| Affinity forced | Chord violation 2.2e-16 at `ε = 0`; then 2.5e-3, 2.3e-2 and 6.2e-2. |
| Orientation from the support condition | On a 21-point grid only `λ = 1` passes. Among 13,529 random effects, only `E_q = P_q` has zero violation. The sampled ratio of `|E_q − P_q|` to the violation reached 4.31; this is a sample, not a bound. |
| Self-consistent weights | Only `λ = 1` and `λ = 0` pass. `λ = 0.5`, anti-Born and cubic shift by 0.10, 0.73 and 0.069. |
| The distant update carries it | Replacement update: anti-Born and tanh pass D-loc (shift 1e-16), with gaps 0.93 and 0.15 to the trace rule. |
| Equal time | Shift 0 at `t = 0`; 1.9e-8, 2.4e-6, 1.9e-5 at `t = 0.01, 0.05, 0.1`; exponent 3.00. |

## Independent checks

A separate checker wrote its own code without reading this runner. A later
adversarial review of the whole chain ran its own checks.
- **Confirmed.**
  - The swap at `Jt = π`, the partial-swap lengths and steering on 2000
    chords.
  - Chord affinity.
  - The deformed laws' exact largest shifts: tanh 0.2065, and cubic `ε/4`.
  - Orientation from the support condition.
  - That D-loc is a new constraint relative to the landed note, whose
    conditions the deformed laws pass.
- **Flagged, now addressed.**
  - The partner's Born weights were an input. Theorem 5 now removes them.
  - The first obligation is restated as D-loc, not discharged outright.
  - The 4.31 ratio is a sample.
  - Moving a partner needs bonds switched one at a time.
  - The kinematics, the distant update and D-tr were used but not listed.
    They are now listed, and Theorem 6 shows the distant update is
    load-bearing.
  - D-loc fails for later times. It is now scoped to equal time
    (Theorem 7).
  - The lock alone does not orient the law; the support condition does.

## What this does not do

- It adopts no decision point. The kinematics, D-perm, D-tr and D-loc are
  supplied and recorded, not derived from the axiom text.
- It does not derive the menu, the relaxation profile (which fixes the
  state, not the law) or the formation rate.
- Its steering uses qubit chords and two-outcome records. The neighbourhood
  version is argued, not computed.
