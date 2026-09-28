---
claim_id: the_incompressible_tensor_pattern_exists_but_isotropy_ties_a_spin_two_fields_helicities_a_positive_models_first_order_graviton_carries_helicity_one_partners_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "(T1, refutation) An incompressible momentum-rule tensor with a light-cone channel exists in a local model. For a supplied photon triplet A~ (three U(1) fields, each with its own Gauss law), E = curl_1(A~ - I tr A~/2) is symmetric and obeys the landed tensor stencil exactly on the landed slot placement. In the Gaussian (Maxwell) triplet its helicity-2 channel has omega = sqrt(UK)|K|, chi ~ q^2, S ~ q^3 and m1 ~ q^4. Three of the six photon modes, helicity 1 and 0, are invisible to E. (T2, theorem) Take any spin-j >= 2 multiplet of operators whose symmetrised f-sum D(eps,q) = <[O_q(eps)^dag,[H,O_q(eps)]]> is q^2 times a rotation-covariant form plus o(q^2). In the helicity basis about q, that form is v_m = alpha + beta m^2 (as copy-space matrices), so 4 v_(+-1) = v_(+-2) + 3 v_0. In a ground state every v_m >= 0, hence v_(+-1) >= v_(+-2)/4. (T3) Einstein-Hilbert's linearised form gives (v2, v1, v0) = (1/2, 0, -1/6) k^2, and the landed lattice symbol the same ratios: it meets the identity only with a negative helicity-0 value. Pretko's scalar-charge theory and the photon triplet give (1, 1/2, 1/3) k^2. (T4) Under the momentum rule the helicity-1 operators vanish, so positivity and the identity force v2 = v0 = 0 at order q^2. (T5) If, in addition, the helicity-1 susceptibility is bounded below, the lowest helicity-1 excitation carrying weight has omega = O(q): a gapless partner. (T6) A cubic-only positive form can evade the identity along an axis, but only with a direction-dependent helicity-2 stiffness. Premises: a ground state (for the inequalities), leading-order isotropy, and analytic f-sums. Not shown: any native qubit model, its susceptibilities or phase, or whether a collective (non-composite) incompressible graviton exists."
upstream_dependencies:
  - minimal_axioms
runner: scripts/isotropy_ties_spin_two_helicity_sum_rules_and_incompressible_tensor_patterns_2026_09_28.py
---

# The incompressible tensor pattern exists, but isotropy ties a spin-2 field's helicities: a positive model's first-order graviton carries helicity-1 partners

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** representation-theoretic theorem with exact checks, and a supplied
lattice construction; unaudited. Independent checks are recorded below.

## In one paragraph

The previous probe found that a light-cone graviton, made from qubit records
obeying the tensor momentum rule, needs an "incompressible" electric pattern:
one whose energy grows as the pattern gets smoother. The owner asked me to
prove that impossible or refute it.

- **Refuted as an obstacle in itself.** Such a pattern exists. Build the
  momentum-rule tensor as the curl of three ordinary photon fields. It then
  obeys the rule exactly on the lattice, it is incompressible, and its
  helicity-2 waves travel on the light cone.
- **Replaced by a sharper obstacle.** Rotation symmetry ties together the
  sum rules of any spin-2 field at long wavelengths:
  - 4 × (helicity-1 push) = (helicity-2 push) + 3 × (helicity-0 push);
  - in a system with an ordinary ground state no push is negative;
  - so a graviton with first-order dynamics always has helicity-1 partners
    carrying at least a quarter of its push. The construction above has
    them: three of its six photon modes are invisible to the tensor but
    still there.
- **How Einstein's gravity gets out.** It satisfies the identity with a
  *negative* helicity-0 push. That is the conformal mode, which has no ground
  state and is removed by GR's energy (time) constraint.
- **What a records-based graviton therefore needs, in isotropic models with
  a ground state.** One of these:
  - helicity-1 partners;
  - a constraint of GR's kind, i.e. local time that is not an external
    parameter;
  - a long-range force that makes the partners' channel incompressible;
  - or a collective mechanism not yet identified.

## Prior art on main

A search of main (docs, meta notes, block memories and the probes branch)
for helicity identities, partner theorems, "incompressible", teleparallel,
tetrad and Weinberg-type statements found none of T1–T6. Context used:
- the landed tensor notes: the 2026-09-14 constraint complex and compact
  bound; the 2026-09-24 oscillator note's exact lattice E-H symbol, used in
  check B; the 2026-09-24 freeze/moves notes;
- the landed ring-model note (2026-09-25), for the spectral-moment chain in
  T5;
- probe 10 (this PR), for the q^4 sum rule and the incompressibility
  condition;
- the landed U(1)/Maxwell lane, for the photon fields;
- reference only:
  - Weinberg (1964–65): local covariant fields for massless helicity h carry
    h derivatives;
  - Pretko (arXiv:1604.05329): the scalar-charge theory;
  - linearised teleparallel gravity (translation gauge fields), for the
    triplet idea;
  - Maldacena (1998, AdS/CFT), as a known non-local emergence of a graviton.
  None is a premise.

## Premises

- **(P1)** A Hamiltonian H and an eigenstate |0>. For the inequalities, |0>
  is a ground state, so every m_1 >= 0.
- **(P2)** Operators O_q(eps) = sum_m eps_m O_q^(m) form a spin-j >= 2
  multiplet under rotations at long wavelength, with O_(-q) = O_q^dag for
  Hermitian densities. Several copies, or mixing with other spins, are
  allowed; the statement is about the compression to the spin-j copies.
- **(P3)** The symmetrised f-sum
  `D(eps,q) = <0|[O_q^dag,[H,O_q]]|0> = m1(O_q) + m1(O_q^dag)` is analytic
  and even in q (the evenness follows from P2). At small q it equals
  q^2 eps^dag V(qhat) eps + o(q^2), and V is rotation-covariant: leading-order
  isotropy. Local finite-range models give analytic D. D(0) = 0 whenever the
  uniform component is conserved, as it is for exact-rule fields.
- **(P4, for T5 only)** The helicity-1 static susceptibility chi_(+-1)(q) is
  bounded below at small q.

## T1 — an incompressible momentum-rule tensor with a light-cone channel (check D)

**Construction.**
- Three photon fields A~_(l j), l = x, y, z, each obey their own Gauss law
  `sum_j D_j A~_(l j) = 0`. The positions: photon l's component j sits at
  s − e_l/2 + e_j/2, with s = (1/2, 1/2, 1/2). So the diagonal components are
  at cube centres and the others on links.
- Define `E_ij = sum_(k,l) eps_(ikl) D_k A_(l j)` with
  `A = A~ − (1/2) I tr A~` and the midpoint difference D_k.
- Then E_ii sits at vertices and E_ij (i ≠ j) at faces: exactly the landed
  slot placement. Every stencil term lands on an actual photon slot (check D).
- 2E has integer coefficients.

**Exact identities.**
- The divergence on the first index vanishes by antisymmetry.
- The antisymmetric part of E equals
  `sum_j D_j A~_(n j) − (1/2) D_n tr A~ + (1/2) D_n tr A~ = 0` by the photon
  Gauss laws.
- So E is symmetric and obeys the landed stencil G E = 0 identically. The
  residual is 8e-16 over 30 random zone momenta.
- The momentum rule holds as an identity of the composite. It is not a
  separate constraint.

**Gaussian spectra** (Maxwell triplet, U = K = 1).
- All six photon modes have omega = sqrt(UK)|K|, where K = 2 sin(k/2).
- E's helicity-2 channel has chi ~ q^2, S ~ q^3 and m1 ~ q^4 (exponents
  1.999, 2.999 and 3.998). This meets exactly the necessary conditions of
  probe 10, with a light-cone lowest mode.
- Three photon modes (helicity 1 and 0) are invisible to E.
- The triplet's own spin-2 multiplet has chi·U = (1, 1/2, 1/3) and
  m1/|K|^2 = (1/2, 1/4, 1/6) for helicities (2, 1, 0). That satisfies
  T2's identity, and the helicity-1 channel is compressible and gapless.

**Qubits.** The construction needs compressible photons. With one qubit per
link that is not established on main: the landed pure-ring link model is
quadratic at L <= 12. So T1 is a harmonic-regime construction (large-spin or
clock links), conditional for qubits.

## T2 — isotropy ties the helicities (check A)

**Statement.** Under P2 and P3, in the helicity basis about qhat, V(qhat) is
block-diagonal:

`v_m = A + B (m^2 − j(j+1)/3)`,

where A and B are copy-space matrices independent of m and qhat. Hence

`4 v_(+-1) = v_(+-2) + 3 v_0`,

and, for a ground state (every v_m ⪰ 0), `v_(+-1) ⪰ v_(+-2)/4`.

**Proof.**
1. V(qhat) = sum_ab qhat_a qhat_b V_ab is a rotation-equivariant linear map
   from Sym^2(R^3) = (spin 0) ⊕ (spin 2) into End(spin j ⊗ C^d).
2. End(spin j) = ⊕_(L=0..2j) (spin L), each once. So by Schur and
   Wigner–Eckart, the spin-0 part maps to 1 ⊗ A and the spin-2 part to
   Q ⊗ B.
3. Here Q(qhat) = (J.qhat)^2 − j(j+1)/3 is the unique spin-2 operator on
   spin j.
4. In the helicity basis about qhat, J.qhat = m. ∎

**Checks.** Check A projects random Hermitian forms onto the rotation
invariants exactly (the kernel of the Casimir). It covers spin 2, spin 2
with two copies, and spin 3; the identity holds to 5e-15 about random
directions. Twenty positive (Haar-averaged) first-moment families all have
every v_m >= 0, with smallest v1/v2 = 0.567.

## T3 — worked forms, and Einstein's escape (check B)

These are unit-Frobenius spin-2 tensors, evaluated at three directions.

| Form | (v2, v1, v0)/k^2 | Identity 4v1 = v2 + 3v0 |
|---|---|---|
| linearised Einstein–Hilbert | (1/2, 0, −1/6) | holds, with v0 < 0 |
| landed lattice E-H symbol (2026-09-24) | v1 = 0, v0/v2 = −1/3 | holds, with v0 < 0 |
| Pretko scalar charge (\|curl A\|^2) | (1, 1/2, 1/3) | holds; v1 = v2/2 |
| photon triplet (sum of \|k × a_m\|^2) | (1, 1/2, 1/3) | holds; v1 = v2/2 |

Einstein's graviton has a first-order helicity-2 sum rule and no helicity-1
partner. That is possible only because its helicity-0 value is negative. The
unconstrained linearised E-H Hamiltonian has no ground state in that sector:
the conformal mode, and the landed note's "indefinite scalar block".
- GR removes the sector with the Hamiltonian (energy) constraint, generated
  by the lapse, i.e. by time reparametrisation.
- Its physical graviton momentum is then the transverse-traceless
  projection, which is non-local.
- A model with a ground state (P1) cannot have a negative v0.

## T4 — the momentum rule removes helicity 1 (check C)

- ker G(k) of the landed stencil has zero overlap (9e-16) with the spin-2
  helicity-1 tensors about the lattice momentum.
- So for momentum-rule fields v_(+-1) = 0, and T2 gives v2 = −3 v0. With a
  ground state, v2 = v0 = 0 at order q^2.
- This recovers probe 10's q^4 law from isotropy and positivity alone,
  without the moment lemma.
- Einstein's escape is again the negative v0.

## T5 — the partners are gapless unless their channel is incompressible

- Suppose a spin-2 multiplet carries a first-order helicity-2 sum rule,
  v_(+-2) ≻ 0. Any compressible light-cone graviton channel must: the moment
  chain gives omega_min <= sqrt(2 m1/chi), so omega_min >= c|q| with
  chi >= chi_0 forces m1 >= chi_0 c^2 q^2 / 2.
- Then T2 gives v_(+-1) ⪰ v_(+-2)/4 ≻ 0. So the helicity-1 operators carry
  spectral weight, with m1 ≍ q^2.
- With P4, the landed moment chain gives
  `omega_min(+-1) <= sqrt(2 m1(+-1)/chi_(+-1)) = O(q)`. That is a gapless
  helicity-1 excitation.
- The only way to gap the partners here is chi_(+-1)(q) -> 0 while their sum
  rule stays ≍ q^2. That is an incompressible helicity-1 channel.
  - An exact rule cannot do it without also removing the operators; then T4
    applies.
  - In a Gaussian model it needs a non-local (1/q^2) electric energy in the
    helicity-1 components. A local model could get that only collectively,
    for example if those components sourced a further long-range field. This
    is a reading, not constructed.

## T6 — isotropy is load-bearing (check E)

A cubic-invariant positive first-order form can escape along an axis. Along
z it gives (v2, v1, v0) = (0.8, 0, 0.6) k^2, which violates the identity, and
it is positive in 200 random directions. But its helicity-2 stiffness then
depends on direction: body diagonal / axis = 0.53. A single light cone for
the graviton rules out that escape unless it is tuned.

## What this means

**For the owner's question.** The incompressible pattern is possible, so it
is not the obstacle. The obstacle is T2: in an isotropic model with an
ordinary ground state, a graviton with first-order (light-cone-capable)
dynamics comes with helicity-1 partners in its sum rule. They are gapless
unless their channel is made incompressible.

**The routes that remain for a pure-helicity-2 light-cone graviton made of
records:**
1. **A constraint that removes a wrong-sign helicity-0 sector**, as
   Einstein's energy constraint does.
   - Physically, local time is not an external clock; it is generated by the
     system.
   - The owner's reading "time is the shifting or creation of records" is
     the natural candidate. That is untested.
   - On the lattice, this route meets the landed compact bound: the energy
     rule forces k^3 in the regular compact class. It would need non-compact
     collective variables.
2. **A long-range force on the helicity-1 components** (T5), making their
   channel incompressible.
3. **A collective, non-composite incompressible graviton.** Open. Known in
   the continuum only through non-local emergence such as holography
   (reference only).
4. **Anisotropy** (T6). Excluded by one light cone unless tuned.

**Observationally** (reference only), gravitational-wave polarisation tests
so far agree with pure tensor modes. Helicity-1 partners that couple to
matter would also carry extra long-range forces.

## No-Go Discipline Gate

The bounded negative claim: under P1–P3, a spin-j >= 2 multiplet with a
first-order helicity-2 sum rule has a helicity-1 sum rule at least a quarter
as large. With P4 as well, that partner is gapless.

- **N1 — attack routes.**
  1. *Anisotropic leading order.* ATTEMPTED (check E). It escapes the
     identity but makes the stiffness direction-dependent. Outside P3.
  2. *A negative sector (no ground state).* ATTEMPTED (check B, E-H). It
     meets the identity with v0 < 0. Outside P1.
  3. *Removing helicity 1 by an exact rule.* ATTEMPTED (check C). Then
     v2 = 0 at first order: no first-order graviton.
  4. *A first-derivative composite* (T1's construction). ATTEMPTED (check
     D). The partners sit in the underlying field (3 invisible modes; its
     v1 = v2/2).
  5. *Several copies, or mixing with other spins.* ATTEMPTED (check A, two
     copies). The identity holds as a matrix identity on the spin-j
     compression.
  6. *Carrying the graviton in a higher-spin field* (j = 3). ATTEMPTED
     (check A). The same identity holds.
  7. *Parity-odd, linear-in-q terms.* RULED OUT by the proof: D is even in q
     (P3).

  **Open routes left** (consistent with the claim, not attacks on it):
  - a GR-type constraint on a wrong-sign sector (route 1 above);
  - a long-range force making chi_(+-1) -> 0 (route 2);
  - collective incompressibility (route 3).
- **N2 — conditions.**
  - W_iso: isotropy (P3). W_pos: a ground state (P1). W_chi: P4, used only
    in T5.
  - W_iso and W_pos are independent. Anisotropic positive forms exist
    (check E), and isotropic non-positive ones exist (E-H, check B).
  - W_chi does not follow from W_iso and W_pos. Both hold in the Maxwell
    triplet, where chi_(+-1) = 1/(2U) > 0. Whether they can hold with
    chi_(+-1) -> 0 is unresolved.
- **N3 — hidden conditions.**
  - Analyticity and evenness of D are stated in P3.
  - "Leading order O(q^2)" is part of the claim's domain. At order q^4 there
    is no identity (three free invariants), consistent with T4.
  - The Gaussian spectra of T1 and T5 are harmonic-regime illustrations.
- **N4 — residual matching.**

  | Cited parent | What it supplies | Match |
  | --- | --- | --- |
  | landed E-H lattice symbol | the E-H ratios | yes (check B) |
  | landed ring-note chain | the T5 bound | yes: a general spectral inequality |
  | landed ring-note chain | "a compressible light-cone graviton needs m1 >= chi c^2 q^2/2" | yes |
  | landed U(1) lane | compressible qubit photons | NOT established there; T1 is conditional for qubits |

- **N5 — rhetoric audit.**
  - The identity is proved per mode (each helicity) and per element (each
    copy block).
  - It is checked per block: spin-2 with one and two copies, and spin 3.
  - Lattice-wide it is a statement about any state satisfying P1–P3; no
    phase is computed.
  - "Partners are gapless" carries P4 explicitly.
- **N6 — partial closure.** Isotropy and the ground state are premises. No
  convention or reframing supplies P4 or removes a helicity sector. GR's
  escape is physical (a constraint), not a relabelling.
- **N7 — steelman.** The graviton might not be carried by any local spin-2
  multiplet with a first-order sum rule: a collective or non-local
  emergence, route 3. Or a long-range field might make the partners
  incompressible, route 2. Both are unclosed, and the claim is scoped to
  multiplets satisfying P1–P3.
- **N8 — cross-cycle echo.**
  - The landed compact bound (2026-09-14) and the oscillator note: not
    retired.
  - Probe 10: its q^4 law is recovered here as T4.
  - The U(1) lane's photon wall: not retired. T1 needs its compressible
    photons.
  - No retirement mechanism applies to T2, which is a theorem of
    representation theory.
- **Outcome:** PASS as scoped.

## What this does not show

It does not show any of these:
- a native qubit model, or its susceptibilities or phase;
- that compressible qubit photons exist on Z^3;
- whether a collective incompressible graviton, or a record-based time
  constraint, exists;
- any statement at order q^4;
- anything about matter coupling or universality.

## Independent checks

Pending.

## Reproduction

`python3 scripts/isotropy_ties_spin_two_helicity_sum_rules_and_incompressible_tensor_patterns_2026_09_28.py`
prints 5 checks, A–E, the N5 lines and TOTAL, in about 1 s. The canonical
cache is at
logs/runner-cache/isotropy_ties_spin_two_helicity_sum_rules_and_incompressible_tensor_patterns_2026_09_28.txt.
