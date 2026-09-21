---
claim_id: admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 55 (open PRs #8568, #8570, #8571; not adopted) AND A CHOICE those clauses leave open: the simplest bond energy of weight one, F = (2/gamma) sum over bonds (phi_x - phi_y)^2, phi = sqrt(w). Bodies at rest are supplied point bodies with bare rest energies m_x and energy density e_x = m_x w_x (block 55); one walker of block 54 has no rest energy. The box's walls are held at the ambient rate phi = 1 (the unit of rate); the rates inside are free. (T1) The static law (12/gamma) phi_x (phi_x - average of phi over the six neighbours) = -m_x phi_x^2 is, for positive rates, the LINEAR problem ((1 - A) + (gamma/12) M) phi = 0 inside with phi = 1 on the walls: it has exactly one solution, 0 < phi <= 1, and raising any bare energy lowers phi at every site. Linearity does not need rest: for ANY fixed amplitude e_x = phi_x (K phi)_x with K_xy = Re chi_x^dagger H_xy chi_y independent of the rates, so the law is ((12/gamma)(1 - A) + K) phi = 0; rest gives K = diag(m) >= 0 and with it uniqueness, the bounds and monotonicity (for an amplitude with negative energy density phi exceeds 1 in places). (T2) (a) For EVERY bond energy of weight one, at a static solution the ledger equals the sum over wall sites of dF/du_x: it is a surface term. (b) For the simplest one the ledger is sum_i m_i phi_i exactly — not the sum of the bare energies and not the sum of the energies m_i phi_i^2 the bodies have in the field — and the flux sum over wall bonds of (1 - phi) is gamma/2 times it. (T3) One body: phi_0 = 1/(1 + x), x = (gamma/12) g_0 m, g_0 the potential of 1 - A at the body; its ledger m/(1 + x) rises with m and stays below 12/(gamma g_0); the energy it has in the field, m/(1 + x)^2, is largest at x = 1, where it is 3/(gamma g_0); its clock runs at 1/(1 + x)^2 of the ambient rate and stops only in the limit. Any arrangement on a set B: the ledger (12/gamma) 1^T (D^-1 + G_B)^-1 1, D = (gamma/12) M, rises with every bare energy and stays below (12/gamma) Cap(B), Cap(B) = 1^T G_B^-1 1 the capacity of B for 1 - A, reached as the bare energies grow without limit and the clocks on B stop. (T4) Two bodies: phi from the 2x2 problem (1 + G D) phi = 1 in closed form; the pair's ledger is below the sum of its members' ledgers alone by (gamma/12) c (m_1 phi_1^alone m_2 phi_2 + m_2 phi_2^alone m_1 phi_1), c their mutual potential, with leading term (gamma/6) m_1 m_2 c; and d(ledger)/dc = -(24/gamma) d_1 d_2 (1 + d_1 (a - c))(1 + d_2 (b - c))/det^2 < 0: the ledger falls as the bodies approach, at any field strength. (T5; a SUPPLIED PRINCIPLE that makes the choice) Block 54's clause makes the amplitudes' energy bilinear in the root rates with rate-independent coefficients, <H_w> = sum phi_x phi_y h_xy. If the field's own energy is timed the same way, F = sum phi_x J_xy phi_y with J independent of the rates, then nearest-neighbour range, covariance and the requirement that uniform rates solve the empty-space law leave exactly one family, c sum over bonds (phi_x - phi_y)^2 (alpha = -3 beta): the simplest bond energy, of weight one automatically; the whole ledger is then one quadratic form in phi. The second bond energy of the refuting pass is not of this form. EXECUTED, NOT CLAIMED: in boxes of side 41 to 81, stopped balls of radius 2, 4, 6 have ledgers 0.85, 0.90, 0.93 of 8 pi R/gamma after extrapolation in the box size (proportional to the radius: 1.30, 0.35, 0.15 per site against 7.9 for one site alone); outside a stopped ball 1 - phi = a/r - b with a within 1 per cent of gamma x ledger/(8 pi); for a pair with x = 2.5 each the defect is 0.08 of its weak-field value and within 10 to 1 per cent of (gamma/6)(m phi)^2 g at separations 2 to 12. BOUNDARY FOUND IN THE REFUTING PASS: for another bond energy of weight one with the same second order, (1/gamma) sum (w_x - w_y)^2/(w_x + w_y), the static law is not linear, the surface term holds, phi_0 agrees at weak field and differs at strong field, and the clock at a body stops at the FINITE bare energy 18/gamma, beyond which no static solution has a positive rate there: whether and where clocks stop is a property of the bond energy, which blocks 53 to 55 fix only through second order. NOT claimed: the principle of T5 or any other choice of bond energy; bodies with a rest energy; any motion, delay or formation of records; the number gamma; lengths; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_2026_09_21.py
---

# The strong field, exactly: bodies at rest make the clock law linear in the root of the rate; the ledger is a surface term, bounded by a capacity

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 55 and one further choice they leave open — the simplest bond energy; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger, with the simplest bond energy of weight one; it reports the exact static law for bodies at rest; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 53 (open PR #8568) found that at weak field the sources of the rate field add exactly. Block 55 (open PR #8571) then fixed the second order of the clock law — through second order it is the averaging law for `φ = √w` — and left one function beyond that. This note takes the simplest member, for which the field's own energy is `(2/γ) Σ_bonds (φ_x − φ_y)²`, and asks what happens when the field is not weak.

1. **The law is linear.** For bodies at rest, `e_x = m_x w_x`, the law `(12/γ) φ_x (φ_x − avg φ) = −m_x φ_x²` can be divided by `φ_x`: what is left is a *linear* problem for `φ`, `((1 − A) + (γ/12)M) φ = 0`, with `φ = 1` on the walls. Any number of bodies, any strengths: one linear solve. The solution is unique, lies between 0 and 1, and more energy anywhere slows every clock (T1).
2. **The ledger is a surface term, and it is `Σ m φ`.** For every bond energy of weight one the ledger of a static arrangement equals a sum over the wall sites: what the outside responds to is the ledger. For the simplest one it is exactly `Σ_i m_i φ_i` — less than the bare energies `Σ m_i`, more than the energies `Σ m_i φ_i²` the bodies have in the field (T2).
3. **Saturation.** One body: `φ_0 = 1/(1 + x)`, `x = (γ/12) g_0 m`. However much bare energy is put at a site, its ledger `m/(1 + x)` stays below `12/(γ g_0)` — on `Z³`, `7.9/γ`. Its clock runs at `1/(1 + x)²` of the ambient rate and stops only in the limit. For any region the ledger is bounded by `(12/γ)` times the region's *capacity*, which grows with its radius, not its volume (T3).
4. **Pairs.** The ledger of two bodies is less than the sum of their ledgers alone, by an amount bilinear in the "charges" `m φ`; it falls as they approach, at any field strength (T4).
5. **A boundary, found by the refuting pass.** Nothing in item 3 is forced by blocks 53 to 55. Another admissible bond energy, with the same second order, stops the clock at a body at the *finite* bare energy `18/γ`, and has no static solution beyond. What is general is the surface term of item 2 and everything at weak field. Whether and where clocks stop is a property of the bond energy, which the clauses leave open beyond second order.
6. **What would make the choice.** Block 54's clause makes an amplitude's energy *bilinear in the root rates*: every term is `φ_x φ_y` times something that does not depend on the rates. If the local clock times the field's own energy in the same way, the bond energy is not a choice: nearest-neighbour range, covariance and "uniform rates solve the empty-space law" leave `c Σ_bonds (φ_x − φ_y)²` and nothing else, and the whole ledger is one quadratic form in `φ` (T5). That is a supplied principle, stated as one; the second member of item 5 does not satisfy it. It also explains item 1: the law is linear in `φ` for *any* fixed amplitude, moving or not; what rest adds is the bounds.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 55 (PR #8571): 'the function f beyond second order' is not derived and 'T3 is a statement about point bodies in weak fields'; block 53 (PR #8568): 'the non-linear completion is not fixed'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "whether the principle of T5 (the local clock times the field's own energy as it times an amplitude) is one the owner would state; the coupled motion at strong field, where the law is linear in phi at each instant but K is not positive; a delay of the field; sources under the record reading; the number gamma"
conditional_surface_status: "T1, T2(b), T3, T4 exact for any finite set of bodies at rest in any box with walls at the ambient rate, for the simplest bond energy; T2(a) exact for every bond energy of weight one; T5 exact given its principle; the large-box figures are executed only"
hypothetical_axiom_status: "blocks 53 to 55's clauses; the simplest bond energy, or the principle of T5 that yields it; point bodies at rest with a bare rest energy; walls at the ambient rate; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom and through its silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 55 (open PRs #8568, #8570, #8571) supply the rates, the clocked amplitudes and the ledger.

- **Rates.** `w_x = φ_x² > 0`. **Box.** A finite box; its wall sites are held at the ambient rate, `φ = 1` there, which fixes the unit of rate; the rates at interior sites are free. With the walls held, stationarity of the ledger holds for every interior `u_x` separately and no multiplier appears (block 55 T4 treats the closed lattice, where the unit of rate is excluded from the variation by a constraint).
- **Bond energy.** `F = (2/γ) Σ_bonds (φ_x − φ_y)²`, over all bonds of the box: block 55's simplest member, for which the empty-space law is `φ_x =` average of `φ` exactly.
- **Bodies.** Finitely many interior sites `x_i` with bare rest energies `m_i > 0`; the energy a body has in the field is `m_i w_{x_i}` (block 55 T2c: a body at rest has `e = m w |χ|²`). `M` is the diagonal matrix of the `m_x`, `D = (γ/12) M`.
- **`A`** is the average over the six neighbours; `G` is the inverse of `1 − A` on the interior with zero walls; `G_B` its restriction to a set `B`; `g_0 = G(x, x)`; `Cap(B) = 1ᵀ G_B⁻¹ 1`.
- **Ledger.** `Σ_i m_i φ_i² + F`.

That the square root of the local rate obeys a linear equation is the form of Einstein's second static theory of 1912. Matrices with non-positive off-diagonal entries and a non-negative inverse are those of Stieltjes; that the inverse is monotone decreasing on positive matrices is Löwner's; the capacity of a set for a potential is classical (Kelvin, Gauss); the value `1.51639` of the potential of `1 − A` at the origin of `Z³` is three times Watson's integral. None is used as authority.

## Prior art and what is new

In the continuum the linear equation for the root of the local rate is Einstein's of 1912, and a bound on how much energy a region of a given size can show to the outside is familiar from the comparator theory, where it has a different constant and a different origin. What is new is the exact lattice statement inside the framework's vocabulary: that block 55's simplest clock law, which looks non-linear, is a linear problem for any number of bodies at rest; that its ledger is `Σ m φ` and, for every weight-one bond energy, a surface term; the exact saturation and capacity bound; the exact pair ledger with the sign of its slope at any field strength; and — from the refuting pass — that these strong-field statements are properties of the bond energy and not of blocks 53 to 55's clauses, with a second admissible member whose clocks stop at a finite energy. No gravitational claim is made.

## Exact target and obligation graph

Target: the static rate field of bodies at rest beyond weak field. Obligations: (O1) the law and its solutions; (O2) the ledger, and what the outside sees; (O3) what happens as bare energies grow; (O4) pairs; (O5) which statements depend on the choice of bond energy. T1–T4 discharge O1–O4 for the simplest bond energy; O5 is answered by T2(a), by the refuting pass's second member, and by T5, which names a principle under which the bond energy is not a choice.

## Theorem T1 — the law is linear

*Statement.* A positive rate field is a static solution iff `φ` solves `((1 − A) + D) φ = 0` at every interior site with `φ = 1` on the walls. This problem has exactly one solution; it satisfies `0 < φ_x ≤ 1`, with `φ_x < 1` at every interior site once some `m_i > 0`; and `∂φ_x/∂m_i < 0` for every interior `x` and every body `i`.

*Proof.* Stationarity of the ledger in `u_x` at an interior site is `∂F/∂u_x + m_x φ_x² = 0` (block 55 T1–T2), and `∂F/∂u_x = (φ_x/2) ∂F/∂φ_x = (2/γ) φ_x Σ_y (φ_x − φ_y) = (12/γ) φ_x (φ_x − (Aφ)_x)`. Dividing by `φ_x > 0` gives the linear problem; conversely a positive solution of the linear problem satisfies the law. `L = (1 − A) + D` has non-positive off-diagonal entries, is irreducibly diagonally dominant on the connected interior with strict dominance next to the walls, so it is non-singular with an entrywise positive inverse. The right-hand side from the walls is non-negative and not zero, so `φ = L⁻¹ b > 0`. `ψ = 1 − φ` solves `Lψ = D1 ≥ 0`, so `ψ ≥ 0`, strictly once some `m_i > 0`. `∂φ/∂m_i = −(γ/12) φ_i L⁻¹ e_i < 0`. ∎

*Remark (linearity does not need rest).* For any amplitude, `e_x = Re χ_x†(H_wχ)_x = φ_x Σ_y φ_y Re(χ_x†H_{xy}χ_y) = φ_x (Kφ)_x`, with `K_{xy} = Re χ_x†H_{xy}χ_y` independent of the rates. So at a fixed amplitude the law is `((12/γ)(1 − A) + K) φ = 0`, linear in `φ`. For a body at rest `K` is the diagonal matrix of the `m_x`; for a moving or spread amplitude it has entries on the bonds, of either sign, and the inverse-positive argument is not available: uniqueness, `φ ≤ 1` and monotonicity are statements about bodies at rest (in the refuting pass a random amplitude, with energy density of both signs, has `φ` between `0.87` and `1.18`).

## Theorem T2 — the ledger is a surface term, and it is `Σ m φ`

*Statement.* (a) Let `F` be any bond energy of weight one, and let no body sit on the walls. At a static solution `Σ_i m_i w_i + F = Σ_{x ∈ walls} ∂F/∂u_x`. (b) For the simplest bond energy the ledger is `Σ_i m_i φ_i`, and `Σ_{wall bonds} (1 − φ) = (γ/2) Σ_i m_i φ_i`.

*Proof.* (a) Both terms have weight one, so the sum over *all* sites of `∂/∂u_x` of the ledger is the ledger (block 55 T4b). Stationarity makes every interior term vanish, and the bodies' energy does not depend on the walls' rates. (b) `(1 − A)φ = −q` with `q_i = (γ/12) m_i φ_i`. Writing each squared difference as `φ_x(φ_x − φ_y) + φ_y(φ_y − φ_x)`, `Σ_bonds (φ_x − φ_y)² = Σ_x φ_x Σ_y (φ_x − φ_y)` over all sites. The interior sites give `6 Σ_x φ_x ((1 − A)φ)_x = −6 Σ_i q_i φ_i`. The wall sites give `Σ_{wall bonds} (1 − φ)`, which equals `6 Σ_i q_i` because the interior bonds cancel in `Σ_{x interior} Σ_y (φ_x − φ_y) = −6 Σ_i q_i`. So `F = (12/γ) Σ_i q_i (1 − φ_i) = Σ_i m_i φ_i (1 − φ_i)`, and adding `Σ_i m_i φ_i²` gives `Σ_i m_i φ_i`. ∎

Three energies are in play. The bare energies `m_i` are what is put in. The energies in the field, `m_i φ_i²`, are what block 54's pull acts on. The ledger `Σ m_i φ_i` lies between them; it is what is kept, and by (a) it is what the walls, and anything outside them, respond to.

## Theorem T3 — saturation and the capacity bound

*Statement.* (a) One body: `φ_0 = 1/(1 + x)`, `x = (γ/12) g_0 m`. Its ledger `m/(1 + x)` is increasing in `m` and less than `12/(γ g_0)`. Its energy in the field `m/(1 + x)²` is largest at `x = 1`, with the value `3/(γ g_0)`. Its rate is `1/(1 + x)²` of the ambient rate: positive for every `m`, tending to zero. (b) Bodies on a set `B`: `φ_B = (1 + G_B D)⁻¹ 1` and the ledger is `(12/γ) 1ᵀ (D⁻¹ + G_B)⁻¹ 1`. It increases with every `m_i` and is less than `(12/γ) Cap(B)`; as all `m_i → ∞` it tends to that value and `φ → 0` on `B`.

*Proof.* `φ = 1 − G q` on the interior, with `q` supported on `B`; on `B`, `φ_B = 1 − G_B D φ_B`. (a) is the case of one site. (b) `q = Dφ_B = D(1 + G_B D)⁻¹ 1 = (D⁻¹ + G_B)⁻¹ 1`. `G_B` is positive definite. If `D` increases, `D⁻¹ + G_B` decreases in the order of positive matrices and its inverse increases, so `1ᵀ(D⁻¹ + G_B)⁻¹1` increases, and it is bounded by its limit `1ᵀG_B⁻¹1`. ∎

A site's energy seen from outside is bounded however much is put there, and beyond `x = 1` adding bare energy *lowers* the energy the body has in the field. For a region the bound is its capacity. The capacity of a ball grows with its radius: a large region cannot show more than an amount proportional to its size, and per site far less than a single site alone can show.

## Theorem T4 — pairs

*Statement.* For two bodies with `a = G(x_1, x_1)`, `b = G(x_2, x_2)`, `c = G(x_1, x_2)`, `d_i = (γ/12) m_i`, `det = (1 + a d_1)(1 + b d_2) − d_1 d_2 c²`: `φ_1 = (1 + d_2 (b − c))/det`, `φ_2 = (1 + d_1 (a − c))/det`. The pair's ledger is below the sum of the members' ledgers alone by `(γ/12) c (m_1 φ_1^{alone} m_2 φ_2 + m_2 φ_2^{alone} m_1 φ_1)`, whose leading term is `(γ/6) m_1 m_2 c`. And `∂(ledger)/∂c = −(24/γ) d_1 d_2 (1 + d_1 (a − c))(1 + d_2 (b − c))/det² < 0`.

*Proof.* Invert the `2×2` matrix `1 + G_B D`. `c < a, b` because the potential of `1 − A` is largest at its source. The rest is algebra (checked symbolically in the refuting pass). ∎

The ledger of a pair is one function of the bodies' places, and its slope pulls each towards the other whether the field is weak or not. The "charges" that enter are `m φ`, not `m`: a body whose clock is slowed by its own field or by its partner's pulls and is pulled less.

## Theorem T5 — what would make the choice (a supplied principle)

*Principle (supplied).* Block 54's clause gives `⟨H_w⟩ = Σ_{x,y} φ_x φ_y h_{xy}`, `h_{xy} = χ_x†H_{xy}χ_y` independent of the rates: the amplitudes' energy is bilinear in the root rates. Suppose the local clock times the field's own energy in the same way: `F = Σ_{x,y} φ_x J_{xy} φ_y`, `J` real, symmetric and independent of the rates.

*Statement.* If `J` reaches nearest neighbours only and is covariant under translations and the 24 rotations, and if uniform rates solve the empty-space law, then `F = c Σ_bonds (φ_x − φ_y)²` for one real `c`; `F ≥ 0` requires `c > 0`, and `c = 2/γ` is block 55's simplest member. Weight one holds automatically. The ledger is then the single quadratic form `φᵀ(K[χ] + c Λ)φ`, `Λ` the matrix of `Σ_bonds (φ_x − φ_y)²`, and at a fixed amplitude its stationarity in the interior rates is linear in `φ` (the Remark to T1). A bond energy that is not a quadratic form in `φ`, such as the second member of the refuting pass, violates the principle.

*Proof.* Translation invariance and the range give `J_{xx} = α` and one number `β_e` for the bonds in each direction; the rotations are transitive on the directions, so `β_e = β` and `F = α Σ_x φ_x² + β Σ_bonds φ_x φ_y`. At uniform rates `∂F/∂u_x = (φ̄²/2)(2α + 6β)`, which vanishes iff `α = −3β`. Every site lies on six bonds, so `Σ_x φ_x² = (1/6) Σ_bonds (φ_x² + φ_y²)` and `F = −(β/2) Σ_bonds (φ_x − φ_y)²`. A quadratic form satisfies `Q(a + b) + Q(a − b) = 2Q(a) + 2Q(b)`; `Σ_bonds (w_x − w_y)²/(w_x + w_y)` does not (runner E2). ∎

In words: if keeping local time means the same thing for the field's energy as for an amplitude's — a product of the root rates at the two ends of each term, times something the rates do not enter — then there is no function left to choose, only the number `γ`. The note does not claim the principle; it records that the choice on which T1 to T4 rest is equivalent to it within nearest-neighbour covariant energies.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block56_saturation.py`, `γ = 1`.

One body at the centre of a `41³` box (`g_0 = 1.49551`; on `Z³`, `1.51639`): for `m = 0.1, 1, 8, 30, 10³, 10⁶`, `φ_0 = 0.98769, 0.88918, 0.50075, 0.21102, 0.00796, 0.00001`, equal to `1/(1 + x)` to the digits shown; ledgers `0.0988, 0.889, 4.006, 6.331, 7.960, 8.0239` below the bound `8.0240`; energies in the field `0.098, 0.791, 2.006, 1.336, 0.063, 0.00006`, the largest at `x = 1`. The ledger read from the wall flux agrees in every case.

Stopped balls (`φ = 0` on every site within `R` of the centre, the limit of T3b), ledger in boxes of side 41, 61, 81 and extrapolated linearly in the inverse side:

| `R` | 41 | 61 | 81 | extrapolated | of `8πR/γ` | per site of the ball |
|---|---|---|---|---|---|---|
| 2 | 46.50 | 45.28 | 44.69 | 42.90 | 0.854 | 1.300 |
| 4 | 108.72 | 102.27 | 99.32 | 90.34 | 0.899 | 0.352 |
| 6 | 192.32 | 173.02 | 164.76 | 139.56 | 0.925 | 0.151 |

One site alone can show `7.91`. Outside the stopped ball of radius 6 (side 81) `1 − φ = a/r − b` fitted at `r = 8, 24` gives `a = 6.51`, against `γ ×` ledger`/(8π) = 6.56`, and reproduces `r = 12, 18` to 1 per cent.

A pair with bare energy 20 each (`x = 2.5` alone), separations 2, 4, 8, 12: defects `1.162, 0.527, 0.213, 0.110`, against weak-field values `15.77, 6.73, 2.65, 1.35` and against `(γ/6)(mφ_1)(mφ_2) g = 1.293, 0.552, 0.217, 0.111`.

## No-Go Discipline Gate

The note's negative sentences: a site cannot show more than `12/(γ g_0)` to the outside; a region cannot show more than `(12/γ)` times its capacity; a clock at a body does not stop at any finite bare energy; none of these three is forced by blocks 53 to 55.

### N1 — Routes by which the sentences could fail
1. *Another bond energy.* Established, not hypothetical: for `(1/γ) Σ (w_x − w_y)²/(w_x + w_y)` — weight one, even, the same second order — the law at a body reads `(1/γ) Σ_y (w_0 − w_y)(w_0 + 3w_y)/(w_0 + w_y)² = −m`, whose left side tends to `−18/γ` as `w_0 → 0`: no static solution with a positive rate at the body exists for `m > 18/γ` (refuting pass W5: `φ_0 = 0.067` at `m = 29.5`, none at `31`, `γ = 0.6`). The third sentence above is a property of the simplest bond energy.
2. *Bodies that are not at rest.* The law stays linear in `φ` at a fixed amplitude (Remark to T1), but `K` then has bond entries of either sign, so uniqueness, the bounds and monotonicity are not established; and the amplitude moves, so a static solution is a snapshot. The coupled motion at strong field is not worked.
3. *A closed lattice.* With no walls the unit of rate is fixed by a constraint and a multiplier appears (block 55 T4b); the law is then `((1 − A) + D)φ = (γ/12) μ/φ`, not linear. Walls at the ambient rate are the setting here.
4. *Bodies with no rest energy.* One walker of block 54 has none; the bodies here are supplied.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The choice of bond energy is the main hidden wall and is declared in the title line, the scope and item 5 of the Result. The walls' rates are held. Bodies are points, at rest, with a rest energy. The law is static. The large-box figures are executed, with an extrapolation in the box size.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the absences that motivate the clauses | yes (premise) |
| block 55 (open PR #8571) | the ledger, the energy density of a body at rest, the weight-one class and its simplest member, the degree-one identity | yes (restated) |
| blocks 53, 54 (open PRs #8568, #8570) | the rate field; the pull on an energy in the field | restated / placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "linear law, one solution in (0, 1], monotone; ledger `Σ m φ`, a surface term; saturation and capacity bound; pair closed form and defect" | executed: the law at each of 125 interior sites for three bodies; the sign of the change of `φ` at each site | executed: one body for three bare energies against `1/(1 + x)`; the energy in the field at `x = 1/2, 1, 2` | executed: the capacity of the seven-site cross from its exact potential matrix; seven bodies for three bare energies | executed: the ledger identity and the surface term for three bodies; the pair at separations 4, 2, 1; the clock law for an amplitude spread over six sites; the one-dimensional family of bilinear energies and the parallelogram identity on the `3×3×3` torus | T1–T4 for any finite set of bodies at rest in any box with walls at the ambient rate, simplest bond energy; T2(a) for every weight-one bond energy; other bond energies' strong fields not established beyond the refuting pass's example |

### N6 — Partial-closure paths and primitive scan
The registered primitives do not choose a bond energy or supply a rest energy: `scale_reference_primitive` converts units; `kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form; `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You picked the one bond energy that linearizes and then reported its special properties." Reply: yes, and the note says so in its first paragraph, in the scope and in the Result; the refuting pass was pointed at exactly this and produced the second member whose clock stops at a finite energy, which is reported as a boundary with its exact threshold. What survives the choice is stated separately (the surface term; everything through second order), and T5 names the principle the choice amounts to, as a supplied principle. Second objection: "Bodies at rest do not exist for one walker." Reply: agreed (block 54); the bodies are supplied, and composite bodies are queued. Third objection: "Walls at a held rate are a master clock." Reply: they fix the unit of rate, which is all a held value can do when only ratios mean anything; every statement is about ratios to the walls' rate.

### N8 — Cross-cycle echo
Block 42 found records entering a record-layer field as boundary values, so that a body's strength was a capacity and not a count; block 53's supervisor withdrew a capacity argument for clocks because a pinned absolute rate needs a master clock. Here a capacity appears without any pin: a clock slowed by the energy at its own site approaches zero *relative to the ambient rate*, a ratio, and the bound is the limit of that. Block 41's additive count of sources survives at weak field only.

## Falsifiers

- A positive static solution of the simplest law that does not solve the linear problem, or two distinct solutions, or a `φ` outside `(0, 1]`.
- An arrangement whose ledger differs from `Σ m φ`, or from the sum over wall sites of `∂F/∂u_x`.
- A body whose ledger exceeds `12/(γ g_0)`, or an arrangement on `B` whose ledger exceeds `(12/γ) Cap(B)`, or a ledger that falls when a bare energy is raised.
- A pair whose ledger rises as its mutual potential grows.

## Boundaries and non-claims

The bond energy is a choice blocks 53 to 55 leave open beyond second order; T1, T2(b), T3 and T4 are properties of the simplest member, and another admissible member stops a clock at the finite bare energy `18/γ`. T5's principle would make the choice; it is supplied, not derived. Linearity in `φ` holds for any fixed amplitude, but the bounds of T1 and everything in T3 and T4 are for bodies at rest. Bodies at rest with a rest energy are supplied. Nothing moves in this note: no delay, no approach to the static field, no formation of records. The walls are held at the ambient rate. `γ` is not derived. Lengths are not addressed. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 55 (PRs #8568, #8570, #8571, open): restated.
- Named standard imports at definition level: matrices with non-positive off-diagonal entries and a positive inverse; the order of positive matrices under inversion; the capacity of a finite set for a potential; the degree-one identity.
- Reference only: Einstein (1912); Stieltjes; Löwner; Kelvin and Gauss; Watson.

## Review record
Supervisor-run block, the fourth of the source-link direction. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: block 55 fixes the bond energy only through second order, so every strong-field statement must carry the choice of bond energy in its first line, and what survives the choice must be separated out — this produced T2(a) and pointed the refuting pass at a second member; bodies at rest are supplied. A rigour lens: positivity before dividing by `φ`; the inverse-positive matrix for uniqueness, bounds and monotonicity; the order of positive matrices for the capacity bound; walls at a held rate in place of the closed lattice's multiplier, which would break linearity. A comparator lens: the continuum form and the existence of a size bound are known; named under the Premises and Prior art; two words the repository forbids are avoided. A strategy lens: the block closes the question block 53 opened (do sources add?) — exactly at weak field, through a linear problem for `√w` beyond it — and hands the owner a new fork: what chooses the bond energy. Refuting pass (`specs/supervisor_control_block56_refuter.py`, machinery disjoint from the runner's): W1 the law solved as a non-linear system in `u`, with no division by `φ` (`10⁻¹⁵` from the linear solve); W2 stationarity of the ledger under every interior variation by finite differences, and the sum of its derivatives over the 218 wall sites against the ledger (`6.791327` both); W3 the pair symbolically (leading defect, the exact bilinear form, the sign of the slope); W4 forty random arrangements (bounds, monotonicity, capacity; largest ratio `0.9934`); W5 the second bond energy; W6 the bilinear family symbolically and the clock law for a random complex amplitude. All pass. Findings folded: W5's first normalization of the second bond energy was off by a factor of two (its weak field then disagreed by 3 per cent, which is how it was caught); with the right normalization it agrees at weak field to `10⁻⁵`, and **its clock stops at the finite bare energy `18/γ`** — a boundary the note now states in its scope and Result; the control's first comparison of stopped balls used an ad hoc wall correction and was replaced by an extrapolation in the box size; its first profile comparison ignored the walls. Two things were added after the first gates had been started (they were stopped, not completed): the supervisor noticed that the amplitudes' energy is bilinear in the root rates and that asking the same of the field's energy leaves the simplest bond energy and nothing else (T5; runner E2; refuting pass W6a), and, in checking it, that the note's first statement about moving bodies was wrong — the law is linear in `φ` for any fixed amplitude, and what rest supplies is the positivity of `K` (Remark to T1; runner B3 with a spread amplitude; W6b with a random complex amplitude under the walk, `φ` between `0.87` and `1.18`). Mutation census: 12 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_2026_09_21.py
```

Expected: `TOTAL: PASS=17 FAIL=0`.
