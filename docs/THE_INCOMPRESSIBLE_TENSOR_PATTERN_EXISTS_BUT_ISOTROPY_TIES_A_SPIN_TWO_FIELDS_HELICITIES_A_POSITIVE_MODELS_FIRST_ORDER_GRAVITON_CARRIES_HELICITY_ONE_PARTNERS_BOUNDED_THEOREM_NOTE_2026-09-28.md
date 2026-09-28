---
claim_id: the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "(T1, refutation) An incompressible momentum-rule tensor with a light-cone channel exists in a local model. For a supplied photon triplet (three U(1) fields; A~ are their electric, canonical-momentum variables, each with its own Gauss law; Maxwell Hamiltonian), E = curl_1(A~ - I tr A~/2) is symmetric and obeys the landed tensor stencil exactly on the landed slot placement. In the Gaussian triplet, E's helicity-2 channel has omega = sqrt(UK)|K|, chi ~ q^2, S ~ q^3 and m1 ~ q^4. Three of the six photon modes (helicity 1 and 0) are invisible to E. (T2, textbook representation theory applied to sum rules) Take a spin-j >= 2 multiplet of operators with O_(-q) = O_q^dag, D(0) = 0 (the uniform component commutes with H), an analytic symmetrised f-sum D(eps,q) = <[O_q^dag,[H,O_q]]> and a ground state. Positivity removes odd orders. The q^2 coefficient, if rotation-covariant, is v_m = A + B(m^2 - j(j+1)/3) in the helicity basis, so 4 v_(+-1) = v_(+-2) + 3 v_0 and v_(+-1) >= v_(+-2)/4. This is the compressible route: a first-order helicity-2 sum rule carries a helicity-1 one. (T3) Linearised Einstein-Hilbert gives (1/2, 0, -1/6) k^2 (and the landed lattice symbol the same ratios), meeting the identity only through a negative helicity-0 compression of its indefinite scalar (transverse-trace) sector. Pretko's scalar-charge form and the photon triplet give (1, 1/2, 1/3) k^2. (T4) Under the momentum rule the helicity-1 operators vanish, so with a ground state v2 = v0 = 0 at order q^2. This holds with cubic symmetry alone: the cubic-invariant forms that annihilate helicity 1 in every direction are the Einstein-Hilbert form only, which is indefinite. (T5) With a helicity-1 susceptibility bounded below, the compressible route has gapless helicity-1 spectral weight. (T6) A cubic positive form can evade T2 along an axis only with a direction-dependent helicity-2 f-sum; its wave speeds are not analysed. Not shown: any native qubit model; whether a non-composite incompressible graviton (probe 10's open route) needs partners; any bridge from records to a time constraint."
upstream_dependencies:
  - minimal_axioms
runner: scripts/isotropy_ties_spin_two_helicity_sum_rules_and_incompressible_tensor_patterns_2026_09_28.py
---

# The incompressible tensor pattern exists, but isotropy ties a spin-2 field's helicities: a positive model's first-order graviton carries helicity-1 partners

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** a standard representation-theory identity applied to spectral sum
rules, with exact checks and a supplied lattice construction; unaudited.
Independent checks are recorded below.

## In one paragraph

The previous probe found that a light-cone graviton, made from qubit records
obeying the tensor momentum rule, needs an "incompressible" electric
pattern. The owner asked me to prove that impossible or refute it.

- **Refuted as an impossibility.** Build the momentum-rule tensor as the
  curl of three ordinary photon fields. It obeys the rule exactly on the
  lattice, it is incompressible, and its helicity-2 waves travel on the
  light cone. Three of the six photon waves are invisible to the tensor but
  still exist.
- **The compressible route is closed, with partners.** Rotation symmetry
  ties together the long-wavelength sum rules of any spin-2 field:
  - 4 × (helicity-1 push) = (helicity-2 push) + 3 × (helicity-0 push);
  - with an ordinary ground state no push is negative;
  - so a graviton channel with a first-order (compressible) sum rule always
    comes with a helicity-1 channel carrying at least a quarter of it.
  The same identity recovers the previous probe's q^4 law, and it holds with
  cubic symmetry alone.
- **Einstein's gravity** meets the identity only through a negative
  helicity-0 part. That comes from its indefinite scalar sector (the
  transverse trace), which has no ground state and which its constraints
  remove.
- **Still open:** the incompressible route itself when the graviton is not a
  composite. The one incompressible example here is a composite, and its
  partners sit in its constituents.

## Prior art

On main, a search of docs, meta notes, block memories and the probes branch
found no statement of T1–T6. External and textbook sources, re-proved here
and not premises:
- **T2's representation step is textbook.** It is Wigner–Eckart for a rank-2
  tensor on spin j, the Stevens operator-equivalent D[J_z^2 − J(J+1)/3]. It
  has long been used for rotationally invariant correlation functions (e.g.
  Hubbard, Phys. Rev. 180, 319 (1969)).
- **The spin-projector decomposition of linearised gravity** (Barnes–Rivers
  1965; van Nieuwenhuizen 1973) gives E-H = P^2 − (1/2) P^0_s, with a
  negative scalar sector. The ADM/Fierz–Pauli constraint reduction is
  standard.
- **Cubic acoustic anisotropy** is standard Christoffel/elasticity theory
  (Every, PRL 42, 1065 (1979)).
- **Pretko's vector-charge theory**, whose Gauss law ∂_i E_ij = ρ_j is the
  momentum rule, has a two-derivative field strength and ω ∝ k^2. That is
  prior art for T4's conclusion. Pretko's scalar-charge theory is the form
  used in T3.
- **Weinberg (1964–65)**: massless helicity-h local covariant fields carry h
  derivatives.
- **Linearised teleparallel gravity** (translation gauge fields), for the
  triplet idea.
- **Maldacena (1998)**, as a non-local emergence of a graviton.

What is used here, and not found in these sources or on main (a repo-only
search cannot establish external novelty):
- the application to ground-state f-sum positivity and graviton partners;
- the cubic-only version of T4;
- the lattice-exact composite construction.

Landed context: the tensor notes of 2026-09-14 and 2026-09-24 (the E-H
lattice symbol is used in check B), the ring-model moment chain of
2026-09-25, and probe 10 of this PR.

## Premises

- **(P1)** A Hamiltonian H and an eigenstate |0>. For the inequalities, |0>
  is a ground state, so every m_1 >= 0.
- **(P2)** Operators O_q(eps) form a spin-j >= 2 multiplet at long
  wavelength, with O_(-q) = O_q^dag for Hermitian densities. Copies and
  mixing with other spins are allowed; the statements concern the
  compression to the spin-j copies.
  - This gives reciprocity, D(eps,−q) = D(eps*,q), not evenness.
- **(P3)** The symmetrised f-sum
  `D(eps,q) = <0|[O_q^dag,[H,O_q]]|0> = m1(O_q) + m1(O_q^dag)` is analytic
  in q, and D(0) = 0 because [H, O_0] = 0.
  - With P1, positivity then removes the odd orders. A first-order term, or
    a third-order term once the second-order one vanishes, would change sign
    between q and −q; for example (J.q) ⊗ C is covariant and Hermitian but
    is killed by positivity.
  - So D = q^2 V(qhat) + O(q^4) with V Hermitian. T2 assumes V is
    rotation-covariant: leading-order isotropy.
- **(P4, T5 only)** The helicity-1 static susceptibility chi_(+-1)(q) is
  bounded below at small q.

## T1 — an incompressible momentum-rule tensor with a light-cone channel (check D)

**Construction.**
- Three photon fields, l = x, y, z. A~_(l j) is photon l's electric
  (canonical-momentum) variable and a_(l j) its vector potential.
- The Maxwell Hamiltonian is `H = sum_l [ (U/2)|A~_l|^2 + (K/2)|curl a_l|^2 ]`.
- Each photon has its own Gauss law, `sum_j D_j A~_(l j) = 0`.
- Photon l's component j sits at s − e_l/2 + e_j/2, with s = (1/2,1/2,1/2):
  diagonal components at cube centres, the others on links.
- Define `E_ij = sum_(k,l) eps_(ikl) D_k A_(l j)`, with
  `A = A~ − (1/2) I tr A~` and the midpoint difference D_k.
- E_ii then sits at vertices and E_ij (i ≠ j) at faces: the landed slot
  placement. Every stencil term lands on a photon slot, and 2E has integer
  coefficients.

**Exact identities.**
- The first-index divergence vanishes by antisymmetry.
- The antisymmetric part equals the photon Gauss laws, and so vanishes.
- Hence E is symmetric and G E = 0 identically. The residual is 8e-16 over
  30 zone momenta; the Fable check found it exactly 0 in integer real space.

**Gaussian spectra** (U = K = 1).
- The six transverse photon modes have omega = sqrt(UK)|K|.
- E's helicity-2 channel has chi ~ q^2, S ~ q^3 and m1 ~ q^4 (exponents
  1.999, 2.999 and 3.998). That is a light-cone lowest mode meeting probe
  10's necessary conditions.
- Rank counting leaves 3 photon modes, of helicities ±1 and 0, invisible to
  E.
- The triplet's own spin-2 multiplet has chi·U = (1, 1/2, 1/3) and
  m1/|K|^2 = (1/2, 1/4, 1/6). That obeys T2, and its helicity-1 channel is
  compressible and gapless.

**For qubits.** Compressible photons with one qubit per link are not
established on main (the landed pure-ring model is quadratic at L ≤ 12).
T1 is a harmonic-regime construction, conditional for qubits.

## T2 — isotropy ties the helicities (check A)

**Statement.** Under P1–P3 with rotation-covariant V, in the helicity basis
about qhat:

`v_m = A + B (m^2 − j(j+1)/3)`,

with A and B copy-space matrices. Hence

`4 v_(+-1) = v_(+-2) + 3 v_0`,

and for a ground state `v_(+-1) ⪰ v_(+-2)/4`.

**Proof.**
1. V(qhat) = sum_ab qhat_a qhat_b V_ab is an equivariant linear map from
   Sym^2(R^3) = (spin 0) ⊕ (spin 2) into End(spin j ⊗ C^d).
2. Spins 0 and 2 each occur once in End(spin j) when j ≥ 1, with
   operator equivalents 1 and (J.qhat)^2 − j(j+1)/3.
3. J.qhat = m in the helicity basis. ∎

Cross-spin blocks are not constrained; the statement is about the spin-j
compression.

**Checks.**
- Exact invariant projection (check A): spin 2 with one and two copies and
  spin 3, to 5e-15. Twenty positive Haar-averaged families give smallest
  v1/v2 = 0.567.
- The Fable check reproduced the closed form for j = 2, 3, 4. It also
  showed that a non-analytic term |q|^2 (J.qhat)^4 breaks the identity, so
  analyticity (P3) is load-bearing.

## T3 — worked forms (check B)

The values are for unit-Frobenius spin-2 tensors, at three directions.

| Form | (v2, v1, v0)/k^2 | 4v1 = v2 + 3v0 |
|---|---|---|
| linearised Einstein–Hilbert | (1/2, 0, −1/6) | holds; v0 < 0 |
| landed lattice E-H symbol | v1 = 0, v0/v2 = −1/3 | holds; v0 < 0 |
| Pretko scalar charge (\|curl A\|^2) | (1, 1/2, 1/3) | holds |
| photon triplet (sum of \|k × a_m\|^2) | (1, 1/2, 1/3) | holds |

What E-H's negative value is:
- v0 = −1/6 is the spin-2 compression of E-H's helicity-0 block. On
  (spin-2 m = 0, trace) that block is `k^2 [[−1/6, √2/6], [√2/6, −1/3]]`,
  with eigenvalue 0 on the gauge direction qhat qhat and −1/2 k^2 on the
  transverse trace (δ − qhat qhat)/√2.
- That transverse-trace (Newtonian/conformal) direction is the indefinite
  scalar sector: the unconstrained E-H Hamiltonian has no ground state
  there.
- Physical linearised GR fixes that mode with the Hamiltonian constraint
  and gauges its conjugate with the lapse. Its positive TT spectrum appears
  only after all four constraints are imposed and the gauge is reduced.
- A model with a ground state (P1) cannot have v0 < 0.

## T4 — the momentum rule removes helicity 1 (checks C, C2)

- ker G(k) of the landed stencil has zero overlap (9e-16) with the spin-2
  helicity-1 tensors about the lattice momentum.
- So v_(+-1) = 0. T2 then gives v2 = −3 v0, and a ground state forces
  v2 = v0 = 0. By P3's parity argument D = O(q^4): probe 10's law.

**Isotropy is not needed.** Check C2 takes the real symmetric forms
invariant under the 24 proper cubic rotations. There are 6 of them (irrep
count 2A1 + 2E + 2T2; the isotropic ones are 2). Among these, the forms that
annihilate the helicity-1 tensors about 40 random directions make up one
dimension, the E-H spin-2 form (v0/v2 = −1/3), which is indefinite. So under
cubic symmetry, the momentum rule plus a ground state force v2 = 0 at order
q^2.

This agrees with Pretko's vector-charge theory (ω ∝ k^2).

## T5 — the compressible route has gapless helicity-1 weight

- A compressible light-cone graviton channel needs a first-order sum rule.
  The moment chain gives ω_min ≤ sqrt(2 m1/chi), so ω_min ≥ c|q| with
  chi ≥ chi_0 forces m1 ≥ chi_0 c^2 q^2/2.
- T2 then gives v_(+-1) ⪰ v_(+-2)/4 ≻ 0.
- With P4, `omega_min(+-1) <= sqrt(2 m1(+-1)/chi_(+-1)) = O(q)`. There is
  gapless helicity-1 spectral weight; this does not say whether it is a
  sharp quasiparticle.
- **P4 can fail.** chi_(+-1) → 0 while m1(+-1) ≍ q^2 can arise from either
  of these:
  - derivative or selection-rule structure: the helicity-1 operators couple
    to the low-energy states only through derivatives of other local
    operators (as in T1, where E is a derivative of the triplet);
  - a long-range (1/q^2) energy on the helicity-1 components. In Gaussian,
    constant-overlap models this is the only mechanism.

  An exact rule on the multiplet's own slots fixes which operators exist,
  not their susceptibility.

## T6 — a cubic form can evade T2, only with a direction-dependent f-sum (check E)

- A cubic-invariant positive form escapes along an axis: along z it gives
  (v2, v1, v0) = (0.8, 0, 0.6) k^2, and it is positive by construction
  (termwise).
- Its helicity-2 f-sum depends on direction: body diagonal / axis = 0.528.
- An f-sum does not by itself fix wave speeds. Whether a compensating
  anisotropy in the susceptibility could still give isotropic speeds is not
  analysed.
- The Fable check found by SDP that a positive cubic form with v1 = 0 on the
  axes and a direction-independent helicity-2 f-sum is infeasible.
- By T4, exact-rule fields cannot use this escape at all.

## What this means

**For the owner's question.**
- The incompressible pattern is possible. It is not an impossibility.
- The compressible route to a light-cone graviton is closed with partners,
  in any model with an ordinary ground state and isotropic (or, for T4,
  cubic) leading order: a first-order helicity-2 sum rule carries a
  helicity-1 one. These partners have gapless spectral weight unless P4
  fails.
- The incompressible route (probe 10) stays open. T1 is one composite
  instance, whose partners sit in the constituent photons. Whether a
  non-composite incompressible graviton needs partners is not decided here.

**Open routes to a pure-helicity-2 light-cone graviton made of records:**
1. **An incompressible graviton that is not a composite.** Probe 10's route;
   open. In the continuum it is known only through non-local emergence such
   as holography (reference only).
2. **A constraint removing an indefinite scalar sector,** as GR's
   Hamiltonian constraint does. There, local time is generated by the
   system and is not an external parameter.
   - Speculation: the owner's reading "time is the shifting or creation of
     records" is a candidate. There is no bridge. The Record axiom supplies
     neither time dynamics nor refoliation symmetry.
   - On the lattice this route meets the landed compact bound, k^3 in the
     regular class.
3. **Failure of P4** for the helicity-1 channel: derivative structure or a
   long-range energy (T5).

**Observations** (reference only). Gravitational-wave polarisation tests so
far agree with pure tensor modes. Whether helicity-1 partners would also
produce static long-range forces depends on their coupling. Derivative or
selection rules could suppress it.

## No-Go Discipline Gate

The bounded negative claim: under P1–P3, the compression of a spin-j ≥ 2
multiplet with v_(+-2) ≻ 0 has v_(+-1) ⪰ v_(+-2)/4. Under the momentum rule
(cubic symmetry suffices), v_(+-2) = 0 at order q^2.

- **N1 — attack routes.**
  1. *Anisotropic leading order.* ATTEMPTED (checks E, C2). For free fields
     it escapes T2 only with a direction-dependent helicity-2 f-sum. For
     exact-rule fields it gives nothing, since C2 leaves only the indefinite
     E-H form.
  2. *A negative sector.* ATTEMPTED (check B). E-H has v0 < 0; outside P1.
  3. *Removing helicity 1 with an exact rule.* ATTEMPTED (checks C, C2).
     Then v2 = 0 at first order.
  4. *A first-derivative composite.* ATTEMPTED (check D). The composite's
     own first-order sum rule vanishes, so T2 is vacuous for it. The
     constituent photons carry v1 = v2/2.
  5. *Copies, or mixing with other spins.* ATTEMPTED (check A). The identity
     holds on the spin-j compression.
  6. *Higher spin* (j = 3, and j = 4 in the Fable check). ATTEMPTED; the
     same identity holds.
  7. *Parity-odd, linear-in-q terms.* RULED OUT by P1 positivity with
     D(0) = 0 (P3); P2 alone does not exclude them.

  **Open routes left** (not attacks on the claim): a non-composite
  incompressible graviton; a constraint removing an indefinite sector;
  failure of P4.
- **N2 — conditions.**
  - W_iso (P3's covariance) and W_pos (P1) are independent. Positive
    anisotropic forms exist (check E), and so do isotropic indefinite ones
    (check B).
  - For T4, W_iso can be weakened to cubic symmetry (C2).
  - W_chi (P4): whether it follows from P1–P3 is unresolved. The Maxwell
    triplet satisfies all four. A derivative-structure example (sol) shows
    that chi_1 → 0 is possible in general, but was not built inside the
    graviton setting.
- **N3 — hidden conditions.**
  - Analyticity is load-bearing: a non-analytic term breaks the identity
    (Fable).
  - D(0) = 0 needs [H, O_0] = 0.
  - Order q^2 only: at q^4 there are three invariants and no identity.
  - The Gaussian spectra are illustrations.
- **N4 — residual matching.**

  | Cited source | What it supplies | Match |
  | --- | --- | --- |
  | landed E-H lattice symbol | the E-H ratios | yes |
  | ring-note chain | "m1 ≥ chi c^2 q^2/2" and the T5 bound | yes |
  | landed U(1) lane | compressible qubit photons | not established there, so T1 is conditional for qubits |
  | textbook Wigner–Eckart | the representation step | yes, cited |

- **N5 — rhetoric audit.**
  - The identity: per mode and per copy block, proved.
  - Per block: j = 2 (one and two copies) and j = 3 checked; j = 4 in the
    Fable check.
  - Lattice-wide: any state meeting P1–P3; no phase computed.
  - "Partners" means helicity-1 f-sum weight. "Gapless" carries P4.
  - "Light-cone graviton" is narrowed to "first-order (compressible)
    helicity-2 sum rule".
- **N6 — partial closure.** No convention supplies P4 or removes a helicity
  sector. GR's escape is a physical constraint.
- **N7 — steelman.** A non-composite incompressible graviton, or a failure
  of P4, might give a partner-free light-cone mode. Both are unclosed, and
  the claim is scoped to the compressible route.
- **N8 — cross-cycle echo.**
  - Probe 10: its law is recovered as T4, now under cubic symmetry.
  - The landed compact bound and the oscillator note: not retired.
  - The U(1) lane's photon wall: not retired; T1 depends on it for qubits.
- **Outcome:** PASS as scoped: a bounded theorem on the compressible route,
  with the routes above left open.

## What this does not show

It does not show any of these:
- a native qubit model, or its susceptibilities or phase;
- that compressible qubit photons exist on Z^3;
- whether a non-composite incompressible graviton, or a record-based time
  constraint, exists;
- any statement at order q^4;
- anything about matter coupling or universality.

## Independent checks

- **Fable check** (Claude Fable 5.1): "CONFIRMED WITH CORRECTIONS".
  - It independently reproduced:
    - T2 for j = 2, 3 and 4 and two copies, and that a non-analytic term
      breaks it;
    - T3's values;
    - T1 in integer real space (residual exactly 0; exponents 1.998, 2.997
      and 3.996 at U ≠ K; invisible helicities ±1 and 0);
    - T4.
  - Its corrections, all applied:
    - The framing: T2 closes the compressible route only; the
      incompressible route stays open, with T1 a composite instance.
    - The strengthening: T4 needs only cubic symmetry, now check C2, and
      exact-rule fields cannot use T6's escape. Its SDP shows that a
      direction-independent helicity-2 f-sum with v1 = 0 on the axes is
      infeasible.
    - Evenness comes from P1, not P2.
    - "Transverse-trace (Newtonian/conformal) mode" replaces "the conformal
      mode".
    - Textbook citations added.
    - The owner's time reading is "a candidate".
- **Codex `gpt-5.6-sol`, first round: "STANDS WITH CORRECTIONS".**
  - It independently confirmed:
    - the T2 representation step (integer spin compression);
    - T3's values;
    - T1's positions, identities, exponents and rank;
    - T4.
  - Its corrections, all applied:
    - Evenness is derived from positivity and D(0) = 0 via [H, O_0] = 0.
    - The E-H scalar block and the physical-GR statement are made precise.
    - A~ is the photons' canonical momentum, with the Hamiltonian explicit.
    - T5 speaks of "gapless spectral weight", and its P4 failure modes now
      include derivative and selection-rule structure.
    - T6's speed conclusion is withdrawn; the f-sum is not a wave speed.
      Every (1979) is cited.
    - N2's P4 relation is marked unresolved.
    - "Light-cone graviton" is narrowed to "a first-order helicity-2 sum
      rule".
    - The record/lapse link is marked speculation.
    - The matter-force remark is softened.
    - Textbook novelty is cited (Wigner–Eckart/Stevens; Hubbard 1969).

## Reproduction

`python3 scripts/isotropy_ties_spin_two_helicity_sum_rules_and_incompressible_tensor_patterns_2026_09_28.py`
prints 6 checks (A, B, C, C2, D, E), the N5 lines and TOTAL, in about 1 s.
The canonical cache is at
logs/runner-cache/isotropy_ties_spin_two_helicity_sum_rules_and_incompressible_tensor_patterns_2026_09_28.txt.
