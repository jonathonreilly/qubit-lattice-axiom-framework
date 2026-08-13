---
claim_id: os0_is_a_primitive_cut_not_lattice_hypothetical_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "The Euclidean OS0 quadratic Q_E=(k4^{2}+k^{2})/4 is independent of the linear Wick parameter a. Speed-preservation on Q_E selects a^{2}=1; the displayed unadopted lopsided cut Q_lopsided=(4 k4^{2}+k^{2})/4 selects a^{2}=1/4. Current Lattice names Z^{3}, nearest-neighbor adjacency, and proper cubic rotations, and does not name a Euclidean tick or c_t. The kinetic-isotropy primitive supplies c_t=c_s rather than deriving it. The clock extra therefore lives in that primitive cut, not in Lattice. Q_lopsided is displayed only; OS0 is not dropped; a=1 is not installed."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/os0_is_a_primitive_cut_not_lattice_hypothetical_2026_08_13.py
---

# OS0 Euclidean Isotropy Is a Primitive Cut, Not Lattice Content

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact Fraction algebra on two displayed Euclidean quadratic
cuts and a textual location reading of current Lattice versus the
kinetic-isotropy primitive.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/os0_is_a_primitive_cut_not_lattice_hypothetical_2026_08_13.py`](../scripts/os0_is_a_primitive_cut_not_lattice_hypothetical_2026_08_13.py)
**Parents on origin/main:**
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
and the current axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

This is a hypothetical bounded theorem about *where* Euclidean isotropy
lives. It is not a Wick `a=1` install. It is not an `a`-family listing.
No axiom is edited. No primitive is edited.

## Result Up Front

A friction-audit candidate can ask whether the OS0 equality `c_t=c_s`
already sits inside Lattice, because Lattice already forces equal spatial
spacings. The Euclidean quadratic and the current wording say no.

Reconstruct the OS0 Euclidean form

```text
Q_E = (k4^{2} + k^{2})/4
```

with both quadratic coefficients `1/4`. Reconstruct the displayed,
unadopted lopsided cut

```text
Q_lopsided = (4 k4^{2} + k^{2})/4
```

with temporal coefficient `1` and spatial coefficient `1/4`. If the
Euclidean form is written `(c_t^{2} k4^{2} + c_s^{2} k^{2})/4`, the
lopsided display is the speed ratio `c_t=2 c_s`. Neither Euclidean
polynomial names the linear Wick parameter `a`.

Linear Wick is the substitution `k4 = i a ω` with `a ∈ Q\{0}`. The
identity gates are

```text
omega_coeff_E(a) = −a^{2}/4
omega_coeff_lop(a) = −a^{2}
```

Speed-preservation (declared extra matching, not an axiom) equates the
absolute temporal coefficient to the spatial coefficient. For `Q_E`
that is `a^{2}=1`. For `Q_lopsided` the spatial coefficient is still
`1/4` while `|omega_coeff_lop|=a^{2}`, so `a^{2}=1/4` and `a=±1/2`.
Different Euclidean cuts select different Wick `|a|`.

Current Lattice names `Z^3`, nearest-neighbor adjacency, and proper
cubic rotations. It does not name a Euclidean tick or `c_t`. The
kinetic-isotropy primitive supplies `c_t=c_s` rather than deriving it.
The clock wall therefore lives in the *primitive cut*, not in Lattice.
`Q_lopsided` is displayed; it is not adopted. OS0 is not dropped.
`a=1` is not installed.

Candidate C5 does not dissolve formation occupancy `o`, Newton pairing
`B`, or a color algebra `M_3`. It says only that the clock extra is
attached to OS0, not to the four axioms.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Q_E and Q_lopsided are reconstructed as a-free Euclidean quadratics; speed-preservation selects a^{2}=1 on Q_E and a^{2}=1/4 on Q_lopsided; Lattice is quoted as not naming a Euclidean tick or c_t; OS0 remains the primitive cut and is not moved into Lattice or dropped."
trace_class: axiom_challenge_counterfactual
target_claim_id: os0_euclidean_isotropy_is_lattice_content
target_blocker_text: "does current Lattice already contain OS0 Euclidean isotropy c_t=c_s, so that the clock extra is not a primitive cut?"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact for the displayed Q_E/Q_lopsided algebra and the quoted Lattice versus kinetic-isotropy location; a=1 is not installed and Q_lopsided is not adopted"
hypothetical_axiom_status: "C5: OS0 Euclidean isotropy is a primitive cut; not moved into Lattice; not dropped"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Let `k4` be the Euclidean temporal momentum and `k` a spatial momentum
magnitude. Work throughout with exact `Fraction` coefficients.

The **OS0 Euclidean quadratic** is

```text
Q_E(k4, k) = (k4^{2} + k^{2})/4.
```

Both quadratic coefficients equal `1/4`. This is the kinetic-form
statement `c_t=c_s`. The monomials are `k4^{2}` and `k^{2}` only. There
is no symbol `a` in `Q_E`.

The **displayed lopsided Euclidean quadratic** (not adopted) is

```text
Q_lopsided(k4, k) = (4 k4^{2} + k^{2})/4.
```

The temporal coefficient is `1` and the spatial coefficient is `1/4`.
Equivalently, if `Q=(c_t^{2} k4^{2} + c_s^{2} k^{2})/4` with `c_s=1`,
this is `c_t=2 c_s`. There is no symbol `a` in `Q_lopsided`.

**Linear Wick** is the substitution `k4 = i a ω` with `a ∈ Q\{0}`. Then
`k4^{2} = −a^{2} ω^{2}`, so

```text
Q_E  ↦  (−a^{2} ω^{2} + k^{2})/4
Q_lopsided  ↦  −a^{2} ω^{2} + k^{2}/4.
```

The identity gates of the runner are the ω² coefficients

```text
omega_coeff_E(a) = −a^{2}/4
omega_coeff_lop(a) = −a^{2}.
```

**Speed-preservation** is the extra matching `|omega_coeff| =` spatial
coefficient. It is not an axiom sentence and is not installed here.

## Theorem 1 — Euclidean forms do not name `a`

`Q_E` is independent of `a`. Reconstructing the Euclidean polynomial
uses only `k4` and `k`. There is no `a` in `Q_E`.

`Q_lopsided` is also independent of `a`. Reconstructing that displayed
polynomial likewise uses only `k4` and `k`.

The predicate “`Q_E` names `a`” therefore fails.

The Wick parameter appears only after the linear substitution
`k4 = i a ω`. That substitution is not part of the Euclidean cut.

## Theorem 2 — Different Euclidean cuts select different Wick `|a|`

Speed-preservation for `Q_E` is `|omega_coeff_E(a)| = 1/4`, hence
`a^{2}/4 = 1/4`, hence `a^{2}=1`.

Speed-preservation for `Q_lopsided` is not the same condition. The
spatial coefficient remains `1/4` while `|omega_coeff_lop(a)|=a^{2}`,
so `a^{2}=1/4` and `a=±1/2`.

Explicit gates:

```text
omega_coeff_E(1)     = −1/4
omega_coeff_E(1/2)   = −1/16
omega_coeff_lop(1)   = −1
omega_coeff_lop(1/2) = −1/4
```

Thus `|omega_coeff_E(1)|` matches the OS0 spatial coefficient, while
`|omega_coeff_lop(1/2)|` matches the lopsided spatial coefficient and
`|omega_coeff_lop(1)|` does not.

The predicate “speed-preservation selects the same `a` for `Q_E` and
`Q_lopsided`” therefore fails (`1` versus `1/2`).

Different Euclidean cuts select different Wick `|a|`. Installing
`a=1` would silently assume the OS0 cut. That install is not made.

## Theorem 3 — The clock wall is the primitive cut, not Lattice

Quote Lattice. The current axiom memo states:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

That sentence names `Z^3`, nearest-neighbor adjacency, and proper cubic
rotations. It does not name a Euclidean tick, a temporal momentum `k4`,
or a kinetic-form ratio `c_t`. Equal spatial spacings are not a
Euclidean clock.

Quote the kinetic-isotropy primitive. That source states that the
framework takes one structural graining fact, the matter kinetic
normalization `c_t = c_s`, equivalently the Osterwalder-Schrader OS0
kinetic normalization, and that within this declaration `c_t = c_s` is
supplied rather than derived. The four-axiom baseline is not used there
as a derivation of that equality.

The clock wall therefore lives in the *primitive cut*, not in Lattice.
Display `Q_lopsided`; do not adopt it. Do not drop OS0. Do not install
`a=1`.

## Theorem 4 — C5 does not dissolve the other extras

Candidate C5 does not dissolve formation occupancy `o`, Newton pairing
`B`, or a color algebra `M_3`. Those remain separate extras. C5 says
only that the clock extra is attached to OS0, not to the four axioms.

This note does not force `r=1/2`. It does not adopt `L_phys`. It does
not adopt `Q_lopsided`. It does not drop OS0. It does not install
`a=1`. It does not claim Lorentz closure.

## Mutation Predicates

The following predicates are required to fail, and the identity gates
must call `omega_coeff_E(a)` and `omega_coeff_lop(a)`:

1. “`Q_E` names `a`” fails, because the Euclidean monomials are `k4^{2}`
   and `k^{2}` only.
2. “Speed-preservation selects the same `a` for `Q_E` and
   `Q_lopsided`” fails, because the selected values are `a^{2}=1` versus
   `a^{2}=1/4`.

## What This Note Does Not Do

- It does not move OS0 Euclidean isotropy into Lattice.
- It does not drop OS0 or the kinetic-isotropy primitive.
- It does not install `a=1` or any other Wick parameter.
- It does not adopt `Q_lopsided`.
- It does not adopt `L_phys`.
- It does not force `r=1/2`.
- It does not dissolve formation `o`, Newton `B`, or color `M_3`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not list an `a`-family as a new primitive.

## Quoted Current Wording

From `docs/MINIMAL_AXIOMS_2026-06-29.md`, Lattice:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

From `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`:

> Within this declaration, `c_t = c_s` is supplied rather than derived.

and

> It does not add or amend an axiom. The minimal framework baseline is the four
> named axioms in `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit,
> Admissibility, and Record.
