---
claim_id: admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_at_a_speed_set_by_the_local_rate_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 56 (open PRs #8568, #8570, #8571, #8573; not adopted): rates w_x = exp(u_x) on Z^3, amplitudes timed by them, a kept ledger whose terms have weight one. PREMISE OF THIS NOTE (the reading of 'no master clock' for motion): the parameter t along which motion is written is a label; under t -> f(t), f' > 0, the rates go to w/f', so u -> u - log f' and du/dt -> (du/dt - f''/f')/f'. Block 54's law i dchi/dt = H_w chi and every ledger term of weight one are unchanged by this (L dt is invariant): the premise costs nothing so far. (T1) A Lagrangian that depends on the first time derivatives of the rates is unchanged for every f iff it depends on them only through differences between sites and has weight one; for a quadratic form (1/2) v^T M v, v = du/dt, iff M 1 = 0. The on-site term sum_x (du_x/dt)^2 / w_x is unchanged only for f'' = 0: it needs a parameter that is more than a label. (T2) Nearest-neighbour, covariant quadratic forms with M 1 = 0 are the multiples of the lattice operator Lam of sum over bonds (v_x - v_y)^2, the same operator as the weak-field bond energy. With such a kinetic term the weak-field law is Lam[(kappa/wbar) d^2u/dt^2 + (wbar/gamma) u] = -P_0 s: every mode swings at the one frequency wbar/sqrt(gamma kappa), and u(t) = -(gamma/wbar) Lam^+ P_0 applied to a time-filtered source: the static profile at every instant, everywhere at once; nothing travels. For a kinetic form of any longer finite range the symbol is an even trigonometric polynomial vanishing at k = 0, so omega^2 = V/M has no branch through zero: no waves at long wavelength. Beyond weak field the accelerations follow from the inverse of a weighted lattice operator, which couples every site to every other at the same instant. (T3) Referring every rate to ONE clock of the system (the clocks at held walls, or the lattice mean) gives forms with M 1 = 0 that are not of finite range; the simplest, (1/(2 gamma c^2)) sum (d(u_x - u_ref)/dt)^2 / w_x, gives at weak field d^2u/dt^2 = c^2 wbar^2 Lap u - gamma c^2 wbar (e - mean): a front that moves c sites per local tick, c a second pure number; the uniform mode carries no momentum; the static law of blocks 55 and 56 is its limit for slow sources. (T4) The on-site term in a master parameter, (1/(2 gamma c^2)) sum (du/dt)^2/w = (2/(gamma c^2)) sum (dpsi/dt)^2 with psi = w^(-1/2), gives the same waves, and on a closed lattice a uniform mode that moves: psi_0^2 = psi_0(0)^2 + a t^2 from rest, a = gamma c^2 (static part of the ledger)/(2 N): every clock slows together against the parameter, which only a master parameter could notice. (T5) A field q that is NOT a rate (unchanged by a change of parameter) may carry the on-site term sum (dq_x/dt)^2 / w_x with nearest-neighbour bond energy sum sqrt(w_x w_y)(q_x - q_y)^2: L dt is invariant and the field has a front at a speed set by the local rate, with nearest-neighbour terms only; block 54's amplitude is such a field. EXECUTED, NOT CLAIMED: two walkers 300 sites apart on a line with walls, the full non-linear law referred to the wall clocks, the field switched on from the ambient rate: B's wave vector stays below 3e-4 of its later values until t = 250 and then grows, the front expected at 300; at c = 2 and at four times the ambient rate the same happens at 150 and 75; the ledger with its kinetic part moves by 1e-7; from the static field the motion follows the static law to 0.7 and 1.2 per cent at 0.03 of the limiting speed and to 2 and 4 per cent at 0.1. In a 61^3 box the half-rise times at r = 8 to 24 are r/(c wbar) + 0.25 to 0.5; under the neighbours-only law the ratio u/u_static is the same number at distances 1, 6 and 21 at every time. NOT claimed: which reference, if any, the framework would state (a reference to distant clocks is not a nearest-neighbour law); the number c; the premise itself; any field of lengths; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_2026_09_21.py
---

# A delay for the rate field: referred to its neighbours its motion does not propagate; referred to the distant clocks it does, at a speed set by the local rate

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 56 and one premise — that the parameter of motion is a label; the non-linear coupled motion is executed, not proved; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger; it reports which motions of the rate field survive an arbitrary change of the time parameter and whether they carry a delay; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The clock law of blocks 53, 55 and 56 is static: move a body and the rates everywhere change at the same instant. The decision record (PR #8572) lists this as the owner's seventh fork. This note asks what motion of its own the rate field can have when there is no master clock.

**The premise.** If no clock is the master, the parameter `t` in the equations is only a label: replacing `t` by `f(t)` and every rate `w` by `w/f'` changes nothing anyone could observe. Block 54's law for the amplitude and every ledger term of weight one are already unchanged by this; that is what weight one *means*. So the premise has cost nothing so far. It bites only now.

1. **What a kinetic term may see.** Under a change of parameter every `du_x/dt` is shifted by the same amount. A kinetic term survives iff it sees only *differences* of `du/dt` between sites. The obvious term, `Σ (du_x/dt)²/w_x`, does not survive: it needs a `t` that is more than a label (T1).
2. **Referred to neighbours: nothing travels.** A nearest-neighbour covariant kinetic form that sees only differences is a multiple of the lattice operator of `Σ_bonds (v_x − v_y)²` — *the same operator as the field's weak-field energy*. Kinetic and potential terms then have the same shape, every mode swings at the one frequency `w̄/√(γκ)`, and the field of a source is its static profile at every instant, everywhere at once. Longer finite range does not help: there is still no branch through zero frequency (T2).
3. **Referred to the distant clocks: a front.** If every rate is referred to one clock of the system — the clocks at the walls, held at the ambient rate — the term `Σ (d(u_x − u_ref)/dt)²/w_x` survives, and the weak-field law is a wave equation: a front that moves `c` sites *per local tick*. `c` is a second pure number. This is not a nearest-neighbour law: every site refers to the same far clocks (T3).
4. **A master parameter.** Keeping the obvious on-site term means keeping a master parameter. It gives the same waves, and one thing more: on a closed lattice all clocks slow together, `ψ_0² = ψ_0(0)² + a t²` with `ψ = w^{−1/2}` — a motion only a master parameter could notice (T4).
5. **What can carry a delay with nearest-neighbour terms only:** a field that is not a rate. Its on-site kinetic term, timed by the local clock, survives any change of parameter, and it has a front at a speed set by the local rate. Block 54's amplitude is such a field; a field of lengths would be another (T5).
6. **Executed.** Two walkers 300 sites apart, the full non-linear law referred to the wall clocks, the field switched on from the ambient rate: `A`'s pull reaches `B` at `t ≈ 300`; at `c = 2`, at 150; at four times the ambient rate, at 75. The ledger, kinetic part included, holds to `10⁻⁷`. Started from the static field, slow motion follows the static law of block 56 to about one per cent at 0.03 of the limiting speed.

So the owner's seventh fork (delay) and sixth (lengths) are tied: **with no master clock and nearest-neighbour laws, the rate field cannot carry a delay; a delay needs a reference to distant clocks, or a field that is not a rate.**

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "blocks 53 and 55 (PRs #8568, #8571): 'The law is static: nothing is said about how the field follows a change of its sources'; decision record (PR #8572), fork 7: 'Delay. The law of A and C is static: it acts at a distance. A field with its own motion is not worked.'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a field that is not a rate as the carrier of the delay: a field of lengths on the bonds with a nearest-neighbour law timed by the local clock, and whether it also supplies the second half of the comparator's bending of light; or the owner's decision that rates may be referred to the distant clocks; the number c"
conditional_surface_status: "T1 exact for every first-order Lagrangian of the rates; T2 exact at weak field for nearest-neighbour covariant quadratic forms, and as 'no branch through zero' for every finite range; T3, T4 exact at weak field, T4's uniform mode exact; T5 exact; the non-linear coupled motion is executed only"
hypothetical_axiom_status: "blocks 53 to 56's clauses; the parameter of motion as a label; for T3 a reference to the wall clocks or the lattice mean; for T4 a master parameter; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the covariance sentence of Admissibility and its statement that Admissibility does not "define a time metric". Blocks 53 to 56 (open PRs) supply the rates, the clocked amplitudes and the ledger.

- **Rates.** `w_x = φ_x² = exp(u_x)`; `ψ_x = w_x^{−1/2}`. **Weight one:** a ledger term `T` with `T[tw] = tT[w]`.
- **Change of parameter.** `t' = f(t)`, `f' > 0`; elapsed ticks `w_x dt` are unchanged, so `w' = w/f'`, `u' = u − log f'`, `du'/dt' = (du/dt − f''/f')/f'`. An amplitude `χ` and any field `q` that is not a rate are unchanged: `dq/dt' = (dq/dt)/f'`.
- **Kinetic terms.** On-site: `Σ_x (du_x/dt)²/w_x`. Neighbour-referred: `Σ_bonds (du_x/dt − du_y/dt)²/√(w_x w_y)`. Wall-referred: `Σ_x (d(u_x − u_ref)/dt)²/w_x`, `u_ref` the log-rate of the held walls; mean-referred: `min_b Σ_x (du_x/dt − b)²/w_x`.
- **Weak field.** `w = w̄ e^{u}` with small `u`; `Λ` the matrix of `Σ_bonds (v_x − v_y)²`; `E(k) = Σ_j (2 − 2cos k_j)` its symbol; bond energy `(w̄/2γ) uᵀΛu` (blocks 53, 55); `P_0` removes the mean.
- **Fronts** are read on the lattice as exact zeros of a leapfrog recursion beyond a distance that grows by one site per step, and in the controls as half-rise times.

That a kinetic energy should see only differences, because the absolute is unobservable, is the programme of Mach as carried out by Barbour and Bertotti, and an action unchanged by a change of parameter goes back to Jacobi. In Einstein's theory, as Arnowitt, Deser and Misner set it out, the rate of clocks has no kinetic term of its own: it is fixed at each instant by a constraint, as the potential of Coulomb is in Maxwell's theory in the gauge named after him, and what travels is carried by the measures of length. The leapfrog recursion and its stability limit are Courant's. None is used as authority.

## Prior art and what is new

That a field fixed by a constraint acts at once, and that a theory of clock rates alone has nothing of its own to make waves with, is known from the comparator theory. What is new is the statement and proof inside the framework's vocabulary: that blocks 53 to 55's premise, read for motion, is invariance under a change of the parameter, which those blocks already have; that it restricts a kinetic term of the rates to differences; that with the Admissibility axiom's form — nearest-neighbour, covariant — the kinetic operator *is* the potential operator, so nothing propagates, exactly; that the two ways out are a reference to a clock of the system, which is not nearest-neighbour and brings a second number, and a field that is not a rate; and an executed non-linear run of the first. It ties the decision record's forks on delay and on lengths together. No gravitational claim is made.

## Exact target and obligation graph

Target: what motion of its own the rate field can have with no master clock, and whether it carries a delay. Obligations: (O1) which kinetic terms are allowed; (O2) the nearest-neighbour case; (O3) what gives a front, and at what speed; (O4) what a master parameter would add; (O5) what else could carry a delay. T1–T5 discharge them; the non-linear coupled motion is executed and not claimed.

## Theorem T1 — what a kinetic term may see

*Statement.* Let `L` depend on the rates and on their first derivatives `v_x = du_x/dt`. `L dt` is unchanged by every change of parameter iff (i) `L` depends on `v` only through the differences `v_x − v_y`, and (ii) `L[tw, v/…]` has weight one in the sense that `L dt` is unchanged by `f' = ` const. For `L = ½ vᵀM(w)v − F`: iff `M(w)1 = 0` and `M` has weight minus one. The on-site form `M = diag(1/w_x)` has `M1 ≠ 0`: `L dt` changes by a multiple of `f''`.

*Proof.* At an instant `f'` and `f''` may be chosen independently. `f'' ≠ 0` with `f' = 1` shifts every `v_x` by the same `−f''` and changes nothing else, so invariance requires `L` to be unchanged by a common shift of the `v_x`: a function of differences. `f'' = 0` is a change of unit and gives (ii). For a quadratic form the common shift `ε` adds `−ε 1ᵀMv + ½ε²1ᵀM1`, which vanishes for every `v` iff `M1 = 0`. ∎

Blocks 54 and 55 pass the test without change: `i dχ/dt' = (1/f') H_w χ = H_{w'}χ` because `H_w` is linear in the rates, and a ledger term of weight one gives `T[w'] dt' = T[w] dt`.

## Theorem T2 — referred to neighbours, nothing travels

*Statement.* (a) The nearest-neighbour symmetric forms `M` that are covariant under translations and the 24 rotations and have `M1 = 0` are the multiples of `Λ`. (b) With `K = (κ/2w̄) vᵀΛv` and the weak-field bond energy `(w̄/2γ) uᵀΛu`, the law is `Λ[(κ/w̄) d²u/dt² + (w̄/γ) u] = −P_0 s`. Every zero-sum mode has the frequency `ω_0 = w̄/√(γκ)`. For any source, `u(t) = −(γ/w̄) Λ⁺P_0 ∫ ω_0 sin(ω_0(t − t')) s(t') dt'`: the static kernel applied to a time-filtered source. A source of fixed shape switched on at `t = 0` gives `u(x, t) = (1 − cos ω_0 t) u_static(x)`. (c) For a covariant form of any finite range with `M1 = 0`, the symbol `M(k)` is an even trigonometric polynomial with `M(0) = 0`, so `M(k) = O(k²)` and `ω²(k) = V(k)/M(k)` does not tend to zero with `k`: there is no branch of waves through zero frequency. (d) Beyond weak field `M(w)` is the matrix of `Σ_bonds (v_x − v_y)²/√(w_x w_y)`; the accelerations are `M(w)⁻¹` applied to local terms, and the inverse of such a matrix (with held walls) has no vanishing entry.

*Proof.* (a) Covariance makes the six neighbour coefficients equal (the rotations are transitive on the directions) and `M1 = 0` fixes the site coefficient: one parameter; `Λ` is in the family. (b) `Λ` multiplies both terms; on zero-sum fields it is invertible, which gives one oscillator equation for every mode, solved by the stated kernel. (c) Finite range makes `M(k)` a trigonometric polynomial; a real symmetric form has a real, even symbol; `M1 = 0` is `M(0) = 0`. `V(k) = (w̄/γ)E(k)(1 + …)` vanishes to second order exactly. (d) The matrix has non-positive off-diagonal entries and is irreducible, so its inverse is entrywise positive. ∎

This is the case the Admissibility axiom's own form points to — one covariant rule, nearest neighbours — and in it the rate field has no waves of its own. It is not that they are slow or damped: the kinetic and the potential operator are the same operator, so there is nothing for a disturbance to travel *in*. What the kinetic term adds is a swing in time of the whole static profile.

## Theorem T3 — referred to the distant clocks, a front

*Statement.* `K_ref = (1/(2γc²)) Σ_x (d(u_x − u_ref)/dt)²/w_x` satisfies T1's condition; its matrix couples every site to the reference and is not of finite range. With walls held at the ambient rate and `t` the walls' time, `K_ref = (1/(2γc²)) Σ_x (du_x/dt)²/w_x = (2/(γc²)) Σ_x (dψ_x/dt)²`, the law is `d²ψ_x/dt² = (γc²/(2ψ_x)) (∂F/∂u_x + e_x)`, the ledger `⟨H_w⟩ + F + K_ref` is kept, and at weak field `d²u/dt² = c² w̄² Δ_lat u − γ c² w̄ (e − mean)`: `ω² = c² w̄² E(k)`, a front at `c w̄` sites per unit of the walls' time, that is `c` sites per local tick. On the lattice the leapfrog recursion of this law, with the step fixed in local ticks, does not contain `w̄`, and its field is exactly zero beyond a distance that grows by one site per step. With the mean as reference the uniform mode carries no momentum. For sources slow against `c w̄` the law reduces to the static law of blocks 55 and 56.

*Proof.* `u_x − u_ref` is a difference, so T1 applies. In the walls' time `du_ref/dt = 0`. `u = −2 log ψ` gives `(du/dt)²/w = 4(dψ/dt)²` and `d²u/dt² − ½(du/dt)² = −2(d²ψ/dt²)/ψ`; the equation of motion follows from `d/dt(∂K/∂v_x) − ∂K/∂u_x + ∂F/∂u_x + e_x = 0` with `∂K/∂u_x = −½(du_x/dt)²/(γc²w_x)`. The ledger's rate is `Σ_x (du_x/dt)[…] = 0` by block 55 T1. Linearizing `∂F/∂u_x = −(w̄/γ)Δ_lat u` gives the wave equation. ∎

The price is twofold. The law is no longer nearest-neighbour: each site's motion is reckoned against the same far clocks — the clocks that block 56 already held at the walls to fix the unit of rate. And a second pure number appears: `c`, the ratio of the field's speed to the limiting speed of block 54's walk. Nothing here fixes it; `c = 1` would be the statement that there is one limiting speed.

## Theorem T4 — what a master parameter would add

*Statement.* With the on-site term in a parameter that is more than a label, the waves are those of T3, and on a closed lattice the uniform mode moves: for uniform rates `ψ_0(t)² = ψ_0(0)² + a t²` from rest, `a = γc² S/(2N)`, `S` the static part of the ledger at unit rate and `N` the number of sites: `w_0(t) = w_0(0)/(1 + a t²/ψ_0(0)²)`.

*Proof.* Summing the equation of motion over sites and using weight one, `Σ_x (∂F/∂u_x + e_x) = F + ⟨H_w⟩ = S w_0`, gives `d²ψ_0/dt² = a/ψ_0³`, solved by the stated form. ∎

Every clock slows together, faster the more energy the lattice holds — and no comparison of clocks could show it. That is what it means for the on-site term to need a master parameter. With a form that satisfies T1 the uniform mode has no momentum and no such motion exists.

## Theorem T5 — a field that is not a rate can carry a delay with nearest-neighbour terms

*Statement.* Let `q` be unchanged by a change of parameter. `L_q = ½ Σ_x (dq_x/dt)²/w_x − (c_q²/2) Σ_bonds √(w_x w_y)(q_x − q_y)²` gives an invariant `L_q dt`, with nearest-neighbour terms only, and at uniform rate the law `d²q/dt² = c_q² w̄² Δ_lat q`: a front at `c_q` sites per local tick.

*Proof.* `dq/dt' = (dq/dt)/f'`, `1/w' = f'/w`, `dt' = f' dt`: the kinetic term is unchanged with no differences needed, because `q` has no shift; the bond term has weight one. ∎

Block 54's amplitude is of this kind (first order in time), and it is already the carrier of every delay in blocks 54 to 56: the rates at a distance change at once, but only because energy arrives, and energy moves no faster than the local limit. What is still instantaneous is the response of far rates to a *rearrangement* of energy that is already there. A field of lengths on the bonds would be another field of this kind; it is not treated here.

## Executed (supervisor controls; floating point; evidence, not proof)

`specs/supervisor_control_block57_retarded_pull.py` — a line of 1500 sites with held walls; block 54's reduced walk for two walkers (rest energies 0.3 and 0.6, 300 sites apart, widths 30); block 56's simplest bond energy; the wall-referred kinetic term; the full non-linear law in `ψ`; `G = 0.002`.

Switch-on from the ambient rate (each walker's own field builds up symmetrically and pulls it nowhere; the other's arrives as a front). `B`'s wave vector:

| | front expected at | `k_B` at 1/3, 2/3, 5/6 of that time | at 1, 1.17, 1.33, 1.5 times it | ledger moved |
|---|---|---|---|---|
| `c = 1`, ambient rate 1 | 300 | `−1.9×10⁻⁹`, `−1.6×10⁻⁵`, `−2.5×10⁻⁴` | `−0.0018, −0.0064, −0.0132, −0.0201` | `−8×10⁻⁸` |
| `c = 2`, ambient rate 1 | 150 | `−1.9×10⁻⁹`, `−2.0×10⁻⁵`, `−3.0×10⁻⁴` | `−0.0017, −0.0047, −0.0085, −0.0122` (at 160, 186, 213, 239) | `−8×10⁻⁸` |
| `c = 1`, ambient rate 4 | 75 | `−4.0×10⁻⁹`, `−3.4×10⁻⁵`, `−5.1×10⁻⁴` | `−0.0032, −0.0093, −0.0168, −0.0239` (at 80, 93, 106, 120) | `−3×10⁻⁷` |

The front is smeared over about 60 sites by the widths of source and receiver. From the static field, `T = 300`, the dynamic law against the static law of block 56: at `G = 0.0004` (speeds up to 0.03 and 0.02 of the limit) `k_A = 0.008735` against `0.008792` and `k_B = −0.011572` against `−0.011710`; at `G = 0.002` (speeds 0.10 and 0.065) `0.030086` against `0.030701` and `−0.038966` against `−0.040447`; ledger moved by `5×10⁻¹²` and `1×10⁻¹⁰`.

`specs/supervisor_control_block57_fronts.py` — weak field. Wall-referred law, `61³` box, point source switched on, `c = 1`: half-rise times along an axis at `r = 8, 16, 24`: `8.25, 16.50, 24.50` at ambient rate 1 and `4.12, 8.25, 12.25` at ambient rate 2; along a body diagonal at `r = 8.66, 15.59, 24.25`: `9.00, 16.00, 24.75` and `4.50, 8.00, 12.38`. Neighbours-only law, `24³` torus: `u/u_static` at distances 1, 6 and 20.8 is `0.459785, 0.459785, 0.459785` at `t = 1` and `1.990037` (three times) at `t = 3`, against `1 − cos ω_0 t = 0.459698, 1.989992`.

## No-Go Discipline Gate

The note's negative sentences: the on-site kinetic term does not survive a change of parameter; a nearest-neighbour (or any finite-range) kinetic term that survives gives no waves at long wavelength, and at nearest-neighbour range the field of a source appears everywhere at once.

### N1 — Routes by which the sentences could fail
1. *A reference to a clock of the system.* Found, and stated as T3: it is not of finite range, and it is the owner's to decide whether the framework would state it.
2. *A master parameter.* T4: possible, with a uniform motion no comparison of clocks can show.
3. *A field that is not a rate.* T5: carries a delay with nearest-neighbour terms; it does not make the rate field itself propagate.
4. *Laws of first order in time* (a relaxation). The same shift applies to `du/dt`, so such a law may involve only differences; referred to neighbours it requires the same lattice inverse and acts at once; referred to a reference it spreads without a front. Not worked further.
5. *Higher time derivatives, or Lagrangians that are not functions of `u` and `du/dt` alone.* Not treated.
6. *Rates that are functions of other fields* (for instance of lengths). Then the rate is not an independent field and T5 is the relevant statement.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The premise — the parameter is a label — is this note's reading of "only ratios of rates mean anything" for motion; block 53 stated the weaker form (a constant change of unit). T2(b) and T3's wave equation are weak-field statements; T2(d) and the executed runs are the non-linear evidence. On a closed lattice, if the unit of rate were also varied, invariance under a change of parameter would make the whole ledger vanish, kinetic part included; as in block 55 T4(b) it is not varied. Held walls are the reference clock of T3 and of block 56.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its rotations; the covariance sentence; the absence of a time metric | yes (premise; the absence motivates the reading and does not prove it) |
| blocks 53, 55 (open PRs #8568, #8571) | the weak-field operator; weight one; the ledger identity | yes (restated) |
| block 54 (open PR #8570) | the clocked amplitude's invariance; the limiting speed | yes (restated) |
| block 56 (open PR #8573) | the simplest bond energy; held walls; the static law the dynamic one reduces to | restated / executed comparison |
| decision record (open PR #8572) | forks 6 and 7 | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "kinetic terms may see only differences; nearest-neighbour ones are multiples of `Λ` and nothing travels; a reference gives a front at `c` sites per local tick; the on-site term moves the uniform mode" | executed: the change of parameter on six rational rates and velocities, four kinetic terms and the bond energy, with and without `f''` | executed: a source switched on: the opposite site of a ring after one step and proportionality to the static profile for six steps; exact zeros beyond the front on a segment for eight steps | executed: squared frequencies at the four rational symbols of a ring of 12 for three kinds of kinetic form | executed: the one-parameter family of nearest-neighbour covariant forms with `M1 = 0`; the uniform mode's equation | T1 for every first-order Lagrangian of the rates; T2 at weak field and, as "no branch through zero", for every finite range; T3, T4 at weak field; T5 exact; non-linear coupled motion executed only |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants the equality `c_t = c_s` of a kinetic form of the repository; whether it bears on the number `c` of T3 is not decided here and it is not used. `scale_reference_primitive` converts units; `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Block 53's premise was a constant change of unit; you have strengthened it to get a no-go." Reply: the note says so. But the strengthening is not a new demand on blocks 54 and 55 — their laws already have the stronger invariance, because weight one is exactly that — and "only ratios of rates mean anything" at every instant *is* the stronger statement. If the weaker reading is kept, T4 applies and shows its cost. Second objection: "A reference to the walls is a master clock by another name." Reply: it is a clock of the system, the one block 56 already used to fix the unit of rate, and every statement is about ratios to it; but it is not a nearest-neighbour law, and the note says that this is the price. Third objection: "Instant action is not a defect if nothing can use it." Reply: agreed that the note does not show a usable signal: the total energy cannot be changed from inside, so the leading far field cannot; what changes at once is the response to a rearrangement. The note claims only what the equations do.

### N8 — Cross-cycle echo
Block 43 found that record-layer fields arrive by diffusion and that a long-range carrier needs a speed; block 53 removed the mass term with the freedom of the unit of rate; block 55 found that the same freedom forbids varying the unit of rate. Here it is the same freedom, at every instant, that removes the rate field's own waves. Block 56 held the walls at the ambient rate to keep the static law linear; the same held walls are the reference clock that gives a front.

## Falsifiers

- A kinetic term of the rates, not a function of differences, whose `L dt` is unchanged by every change of parameter.
- A nearest-neighbour covariant quadratic form with `M1 = 0` that is not a multiple of `Λ`; a finite-range one whose frequencies tend to zero with the wave vector.
- Under the neighbours-only law, a source switched on whose field is not the static profile times one function of time.
- Under the wall-referred law, a non-zero field beyond the front of the leapfrog recursion; a front speed that is not `c` sites per local tick at two ambient rates.
- A closed lattice with the on-site term whose uniform mode does not follow `ψ_0² = ψ_0(0)² + at²`.

## Boundaries and non-claims

The premise is a reading, supplied. Which reference, if any, the framework would state is the owner's decision; a reference to distant clocks is not a nearest-neighbour law. `c` is not derived. T2(b), T3 and T4's waves are weak-field statements; the non-linear coupled motion is executed on a line. The note does not show that the instant response of the static law can carry a usable signal, nor that it cannot. A field of lengths is named as a possible carrier and is not treated. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's statement that no time metric is defined. Blocks 53 to 56 and the decision record (PRs #8568, #8570, #8571, #8573, #8572, open): restated or placed.
- Named standard imports at definition level: invariance of `L dt` under a change of parameter; the equations of motion of a Lagrangian; symbols of finite-range lattice operators; the entrywise positive inverse of an irreducible matrix with non-positive off-diagonal entries; the leapfrog recursion.
- Reference only: Mach; Barbour and Bertotti; Jacobi; Einstein; Arnowitt, Deser and Misner; Coulomb and Maxwell; Courant.

## Review record
Supervisor-run block, the fifth of the source-link direction and the first of the owner's 12-hour campaign of 2026-09-21 ("ok do the delay block next … personally managed and executed"). Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: the faithful reading of "no master clock" for motion is that the parameter is a label; blocks 54 and 55 already have that invariance, so the premise is not an added demand on them — but it is stronger than block 53's sentence, and the note says so and gives the weaker reading its own theorem (T4). A rigour lens: the first form of the no-go ("the rate field cannot have waves") was too strong — the supervisor found the way round it while trying to break it: a kinetic term referred to the lattice mean or to held walls has `M1 = 0` and gives ordinary waves; the no-go is for finite range, and the note is now a trichotomy. A square-root action does not evade T1, because the shift of `du/dt` is inhomogeneous. On a closed lattice varying the unit of rate would make the ledger vanish (recorded under N3). A comparator lens: a rate fixed at each instant by a constraint, with the travelling carried by lengths, is the structure of the comparator theory; named under the Premises and Prior art; three phrases the repository forbids are avoided. A strategy lens: the block ties the owner's forks on delay and on lengths together and names the next block. Refuting pass (`specs/supervisor_control_block57_refuter.py`, machinery disjoint from the runner's): W1 generic `f(t)` symbolically (the on-site term changes by a multiple of `f''`); W2 generalized eigenproblems on a `6³` torus (215 equal frequencies to `3×10⁻¹⁴`; `c²w̄²E(k)` to `10⁻¹³`); W3 the non-linear neighbours-only law on a line with walls: the acceleration forty sites from a source switched on changes at once, by 0.18 of its change at the source, and by exactly zero under the wall-referred law; W4 half-rise times at two ambient rates; W5 the uniform mode on a ring. All pass. Findings folded: W5's first prediction used a constant acceleration and missed by 15 per cent; the uniform mode has the closed form `ψ_0² = 1 + at²`, now in T4 (agreement `0.341064` against `0.341641`). The first run of the control at four times the ambient rate blew up: the step was outside the lattice stability limit `c w̄ dt < 1`; the step is now set in local ticks. The fronts control's first step used `h²a` where a start from rest needs `h²a/2`. Mutation census: 9 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_2026_09_21.py
```

Expected: `TOTAL: PASS=14 FAIL=0`.
