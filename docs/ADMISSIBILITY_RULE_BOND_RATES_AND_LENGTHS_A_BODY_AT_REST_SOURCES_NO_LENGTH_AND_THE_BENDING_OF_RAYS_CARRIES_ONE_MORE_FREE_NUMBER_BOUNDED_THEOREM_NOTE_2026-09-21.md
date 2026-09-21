---
claim_id: admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN the supplied clauses of blocks 53 to 57 (open PRs #8568, #8570, #8571, #8573, #8578; not adopted), WIDENED by one supplied clause: every bond b has its own crossing rate c_b > 0 and every site its rate w_x > 0, H = sum_b c_b h_b + sum_x w_x m_x, h_b the rate-independent hop on b and m_x a rate-independent on-site term (a rest energy, if there is one). Block 54 is the product form c_b = sqrt(w_x w_y). The LENGTH of a bond is l_b = sqrt(w_x w_y)/c_b, a pure number, unchanged by a change of the time parameter. (T1) With no on-site term H contains the bond rates only: one walker with no rest energy cannot tell site rates from lengths; it sees the rate at which each bond is crossed. (T2) By the ledger each rate is sourced by the energy it times: d<H>/dlog c_b = t_b, the hop energy on b; d<H>/dlog w_x = r_x, the on-site energy; sum_b t_b + sum_x r_x = <H>. A body at rest (real envelope, rest content) has t_b = 0 on every bond: it sources site rates and no bond rate or length. A walker with no rest energy moving along an axis has all of its energy on that axis's bonds. In the product form e_x = r_x + (1/2) sum of t_b over the bonds at x (block 55). (T3) Linear, covariant, shift-symmetric laws for log c_b that reach the bonds within one site of a bond's midpoint form a THREE-parameter family (8 perpendicular touching bonds beta, 2 collinear alpha, 4 parallel delta) where block 53's law for site rates had no free number; at zero wave vector the isotropic mode is annihilated and the two anisotropic modes have the restoring term -12 beta, so they carry no long-range field of their own: at distance u_j - mean = ((alpha - delta + beta/2)/(12 beta)) (d_j^2 - Lap/3) u, two powers of the distance below the one scalar that survives, whose stiffness is alpha + 2 beta + 2 delta. (T4) For rays of E^2 = a^2 m^2 + c^2 sum sin^2 k_j a slow body falls at -c^2 grad log a and a ray crossing the gradient bends at -c^2 grad log c, exactly: the ratio of bending to fall is dlog c/dlog a: 1 for locked lengths, 2 for l = abar/a, 0 for bond rates that ignore the site rates. (T5) What could tie lengths to rates: (a) an algebraic local clause l_b = G(w_x, w_y) cannot depend on the depth of the rate, only on w_x/w_y, because a length is a pure number and a rate is not; (b) a local LAW can: a cross term kappa sum sqrt(w_x w_y)(dlog l)(du) in the field's quadratic energy gives, for a body at rest and held walls, log l = -(kappa/S)(u - ubar), that is l = (wbar/w)^beta with beta = kappa/S a free number below sqrt(S_u/S); (c) by T2 a body at rest sources no length directly. The ratio of bending to fall is then 1 + beta: 1 for the clauses of blocks 53 to 57, 2 for beta = 1. EXECUTED, NOT CLAIMED: in a 64^3 box a packet of the walk crossing a uniform gradient bends by -1.6164 with locked lengths and -3.1783 with l = wbar/w (ratio 1.966; clouds of rays -1.6110, -3.1680); on a line a slow body with an on-site rest energy falls by -9.88 and -10.08 under the two clauses (ratio 1.02). NOT claimed: that bonds have rates of their own; the law they obey or its numbers; the number beta; any reference to the ambient rate; a rest energy; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_2026_09_21.py
---

# Bond rates and lengths: a body at rest sources no length, and the bending of rays carries one more free number

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 57 widened by a rate for every bond; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates and for amplitudes timed by them, widened by a rate for every bond; it reports what such rates and the lengths they define can and cannot do; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 57 (open PR #8578) ended: with no master clock and nearest-neighbour laws the rate field carries no delay; a delay needs a reference to distant clocks *or a field that is not a rate* — a field of lengths, say. The decision record (PR #8572) has lengths as the owner's sixth fork, with one blunt fact attached: a field of clock rates alone bends a ray past a body by *half* of what the comparator theory gives. This note asks what lengths can be in the framework's vocabulary and whether they supply the other half.

**The widening (supplied).** Block 54 timed every hop by the clocks at the bond's two ends, `√(w_x w_y)`. Let every bond have a crossing rate `c_b` of its own. The *length* of a bond is then the pure number `ℓ_b = √(w_x w_y)/c_b`: site ticks per crossing. Block 54 is `ℓ = 1`.

1. **What one walker sees.** A walker with no rest energy — and block 54's walker has none — never meets a site rate. Its generator contains the bond rates only. For it, "clock rate" and "length" are not two things (T1).
2. **Each rate is sourced by the energy it times.** By the ledger of block 55, a bond rate is sourced by the hop energy on that bond and a site rate by the on-site energy; together they make up the whole. A body at rest has *exactly zero* hop energy on every bond: it slows site clocks and sources no bond rate and no length. A walker with no rest energy moving along an axis loads that axis's bonds and no others (T2).
3. **A law for bond rates.** Block 53's argument, run for bonds, no longer gives one law: covariant nearest laws for `log c_b` have three free numbers. But the directions lock: at long range only the mode with all three directions equal survives as a field; the differences between directions are driven by the second derivatives of that scalar and fall off two powers of the distance faster (T3).
4. **Bending against falling.** For rays, a slow body falls by the gradient of the log *site* rate and a ray crossing the gradient bends by the gradient of the log *bond* rate. Their ratio is `d log c/d log a`: 1 if lengths are locked, 2 if `ℓ = w̄/w`, 0 if bond rates ignore site rates (T4).
5. **What could make it 2.** Not a local formula for the length: a length is a pure number and a rate is not, so a formula `ℓ = G(w_x, w_y)` can only see the ratio `w_x/w_y` — the gradient of the rate, never its depth. A local *law* can: a cross term in the field's energy between the differences of `log ℓ` and of `u` gives `ℓ = (w̄/w)^β` around a body at rest, with `β` a free number; the ambient rate enters through the walls, as it did for block 57's front. And the ledger gives a body at rest no direct source for lengths. So the ratio is `1 + β`: **one more free number. The clauses of blocks 53 to 57 give 1; the comparator's value is 2** (T5).
6. **Executed.** A packet of the walk crossing a uniform gradient in a `64³` box: bending `−1.616` with locked lengths, `−3.178` with `ℓ = w̄/w` (ratio 1.97, clouds of rays to 0.3 per cent). A slow body on a line falls alike under both (ratio 1.02).

In plain terms: what blocks 53 to 56 built is a theory of clock rates. It makes slow bodies fall correctly by construction, and it bends rays by half the comparator's amount. Lengths that stretch where clocks slow would supply the other half, and the framework's vocabulary has room for them — but nothing found so far forces them to stretch by the right amount, or at all.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 57 (PR #8578), next_trace_action: 'a field that is not a rate as the carrier of the delay: a field of lengths on the bonds ... and whether it also supplies the second half of the comparator's bending of light'; decision record (PR #8572), fork 6: 'a field of clock rates gives the fall of slow bodies in full and half of the comparator's bending of light. A clause for lengths is not proposed.'"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "whether anything in the framework fixes beta (the comparator's 1 would need the cross stiffness to equal the lengths' own); a law of motion for lengths and the front it carries (block 57 T5); bodies whose rest energy is internal hop energy, for which site rates never appear; the owner's decision whether bonds have rates of their own"
conditional_surface_status: "T1, T2 exact for every amplitude and all positive rates; T3 exact for linear covariant shift-symmetric laws reaching the bonds within one site of a bond's midpoint; T4 exact for rays of the stated energy function; T5(a) exact for algebraic local clauses, T5(b) exact for the linear static laws with a cross term and held walls"
hypothetical_axiom_status: "blocks 53 to 57's clauses; a crossing rate for every bond; an on-site rest energy where T4 and T5 compare a slow body with a ray; for T5(b) a cross term in the field's energy; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, the covariance sentence of Admissibility, and its silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 57 (open PRs) supply the rates, the clocked amplitudes, the ledger, and the change of parameter under which a rate has weight one and a pure number weight zero.

- **Rates.** Site rates `w_x > 0`, bond rates `c_b > 0`, both of weight one. **Length** `ℓ_b = √(w_x w_y)/c_b`, weight zero.
- **Generator.** `H = Σ_b c_b h_b + Σ_x w_x m_x`; for the walk `h_b = (i/2)σ_j(|y⟩⟨x| − |x⟩⟨y|)` on the bond from `x` to `y = x + e_j`; `m_x` an on-site hermitian matrix (zero for block 54's walker; `mσ_1` on block 54's reduced walk).
- **Energies.** `t_b = c_b · 2Re χ_y† (i/2)σ_j χ_x`, the hop energy on `b`; `r_x = w_x χ_x† m_x χ_x`, the on-site energy.
- **Neighbours of a bond** (T3): the bonds whose midpoints lie within one site of its midpoint.
- **Rays** of `E² = a(x)² m² + c(x)² Σ_j sin² k_j`: `a` the site rate, `c` the (isotropic) bond rate, `m` a rest energy.
- **Field energy with a cross term** (T5b): at weak field `(S_u/2) uᵀΛu + (S/2) λᵀΛλ + κ λᵀΛu`, `λ = log ℓ`, `Λ` the lattice operator of `Σ_bonds (v_x − v_y)²`, walls held at `u = ū`, `λ = 0`.

That a theory in which only the rate of clocks varies bends light by half of the full amount is the history of Einstein's calculation of 1911 against that of 1915, and the measurement is Eddington's; that the difference is the stretching of lengths is Einstein's line element with its spatial part. A scalar and a second field tied by one free number is the form of the theory of Brans and Dicke. Lengths carried by the bonds of a lattice are the calculus of Regge. None is used as authority, and the comparator's value is quoted as a comparator.

## Prior art and what is new

Every piece is classical. What is new is the statement inside the framework's vocabulary: that block 54's walker, having no rest energy, cannot tell a clock rate from a length, so that the natural widening of block 54 is a rate for every bond; that the ledger of block 55 then says exactly what sources which rate, and that a body at rest sources no length; that block 53's uniqueness argument, run for bonds, leaves three numbers but one long-range scalar; that the ratio of a ray's bending to a slow body's fall is `d log c/d log a`; that no local formula can make a length follow the depth of a rate, while a cross term in the field's energy can, with a free exponent; and hence that the direction's clauses as they stand give half of the comparator's bending, with the other half a free number. No gravitational claim is made.

## Exact target and obligation graph

Target: what bond rates and lengths can and cannot do within the clauses. Obligations: (O1) what the walker sees; (O2) what sources what; (O3) the law of bond rates; (O4) bending against falling; (O5) what could tie lengths to rates. T1–T5 discharge them.

## Theorem T1 — what one walker sees

*Statement.* If `m_x = 0` for all `x`, `H = Σ_b c_b h_b`: the site rates do not appear. Block 54's clause is the restriction of the `3N` bond rates to the product form `c_b = √(w_x w_y)` of `N` site rates.

*Proof.* By inspection. ∎

For a walker with no rest energy, scaling all lengths by `s` is the same as scaling all rates by `1/s`. Site rates acquire a meaning of their own only through something that sits still: an on-site energy.

## Theorem T2 — each rate is sourced by the energy it times

*Statement.* `∂⟨H⟩/∂log c_b = t_b`, `∂⟨H⟩/∂log w_x = r_x`, and `Σ_b t_b + Σ_x r_x = ⟨H⟩`. For a body at rest on block 54's reduced walk (real envelope, rest content `(1, 1)`) `t_b = 0` on every bond. For a plane wave of the walk along an axis, with its content along that axis, `t_b` vanishes on the bonds of the other two axes. In the product form, `e_x = r_x + ½ Σ_{b ∋ x} t_b`.

*Proof.* `⟨H⟩` is linear in each rate. For the rest content, `(1,1)σ_2(1,1)ᵀ = (1,1)σ_3(1,1)ᵀ = 0` and `(1,1)σ_1(1,1)ᵀ` is real, so `Re[(i/2)·real]= 0` on every bond. For the content `(1, 0)`, `⟨σ_1⟩ = ⟨σ_2⟩ = 0`. In the product form `∂/∂u_x` acts on the six bonds at `x` with the factor one half each. ∎

Block 55's single source, the energy density, is what this becomes when every bond's energy is made to slow the clocks at both its ends, in all directions alike. With rates of their own, the bonds a walker crosses are the ones it loads.

## Theorem T3 — a law for bond rates: three numbers, one scalar

*Statement.* The 8 rotations that keep a bond sort the 14 bonds within one site of its midpoint into three classes: 8 perpendicular and touching (squared distance ½), 2 collinear and 4 parallel (squared distance 1). A linear covariant law with the shift symmetry is `c_0 u_b + α Σ_coll u + β Σ_perp u + δ Σ_par u = s_b`, `c_0 = −2α − 8β − 4δ`. On the three fields `u_j(k)` (bonds along `j`, taken at their midpoints) its matrix is `M_jj = c_0 + 2α cos k_j + 2δ Σ_{l≠j} cos k_l`, `M_jl = 4β cos(k_j/2) cos(k_l/2)`. At `k = 0` its eigenvalues are `0` on `(1,1,1)` and `−12β` twice. On `(1,1,1)`, `M = −(α + 2β + 2δ)|k|² + O(k⁴)`. And `(M(1,1,1))_j = −(δ + β/2)|k|² − (α − δ + β/2) k_j² + O(k⁴)`, so at long wavelength `u_j − ū = ((α − δ + β/2)/(12β)) (∂_j² − ∇²/3) ū`.

*Proof.* Count the orbits; expand the cosines. The anisotropic components are driven at order `k²` by the direction-dependent part of `M(1,1,1)` and restored at order one by `−12β`. ∎

Block 53's uniqueness is lost: three numbers, where site rates had none. But for `β ≠ 0` the three directions are not three long-range fields. One scalar is left, with block 53's operator and the stiffness `α + 2β + 2δ`; the differences between directions are of the size of its second derivatives, a tide. With `β = 0` the three directions would not talk to each other at all.

## Theorem T4 — bending against falling

*Statement.* For rays of `E² = a² m² + c² Σ_j sin² k_j`: at `k = 0`, `dv/dt = −c² ∇log a`; for `m = 0` and a wave vector along an axis across the gradient, the transverse acceleration is `−c² ∇log c`, exactly on the lattice. The ratio of the two is `d log c/d log a`.

*Proof.* `v_j = ∂E/∂k_j`, `dk/dt = −∇E`. At `k = 0`, `∂v_j/∂k_l = δ_jl c²/(am)` and `dk_l/dt = −m ∂_l a`. For the ray, `∂v_z/∂k_z = c²/E` at `k_z = 0` and `dk_z/dt = −(c ∂_z c) sin² k_x/E`. ∎

## Theorem T5 — what could tie lengths to rates

*Statement.* (a) Let `ℓ_b = G(w_x, w_y)` with `G` unchanged by a change of the unit of rate. Then `G` depends on `w_x/w_y` only, and `ℓ = G(1)` wherever the rate is uniform, however deep. `ℓ = w̄/√(w_x w_y)` is unchanged, and uses the ambient rate. (b) With the field energy `(S_u/2) uᵀΛu + (S/2) λᵀΛλ + κ λᵀΛu`, `S_u S > κ²`, held walls, and a source for `u` only, the static solution has `λ = −(κ/S)(u − ū)`: `ℓ = (w̄/w)^β`, `β = κ/S`. (c) By T2 a body at rest is a source for `u` only. Then by T4 the ratio of a ray's bending to a slow body's fall is `1 + β`.

*Proof.* (a) Weight zero. (b) Stationarity in `λ` is `Λ(Sλ + κu) = 0` inside with `Sλ + κu = κū` on the walls; the only such field is the constant. (c) `c = √(w_x w_y)/ℓ`, so `d log c = (1 + β) d log a`. ∎

The reference to the ambient rate comes in through the walls, not through the law — the same walls block 56 held to fix the unit of rate and block 57 used as the reference clock of its front. `β` is the ratio of two stiffnesses of the field's energy. Nothing in blocks 53 to 57 fixes it; their clauses are the case `β = 0`.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block59_bending.py`. (a) A positive-energy packet of the walk (no rest energy), wave vector 0.5 along `x`, in a `64³` box with `u = gz`, `g = 0.004`, `T = 30`, bond amplitudes `(φ_x φ_y)^{1+β}`: the part of its `z`-displacement odd in `g` is `−1.6164` for `β = 0` (cloud of rays with `E = cε`: `−1.6110`) and `−3.1783` for `β = 1` (cloud `−3.1680`): ratio `1.966`, against 2 at first order in `g`. (b) A slow body on a line, rest energy 0.4 timed by the site rate and hops timed by `c = w^{1+β}`, `g = 0.002`, `T = 100`: falls `−9.8815` and `−10.0838` (ratio `1.02`; `−gT²/2 = −10`).

## No-Go Discipline Gate

The note's negative sentences: a body at rest sources no bond rate and no length; an algebraic local clause cannot make a length follow the depth of a rate; the clauses of blocks 53 to 57 give a ratio of bending to fall of one; the bond-rate law is not unique.

### N1 — Routes by which the sentences could fail
1. *Rest energy that is internal hop energy.* If every rest energy is the hop energy of something moving inside the body (block 54's reduced walk is an instance), site rates never appear, everything is bond rates, and a ray and a slow body see the same field: the ratio is one again. Not a way to two.
2. *A cross term in the field's energy.* Found, and stated as T5(b): it ties lengths to rates with a free exponent.
3. *A source for lengths other than the ledger's.* Possible only by leaving block 55's premise.
4. *Bond rates that are not isotropic at long range.* T3: the anisotropic parts are slaved to the scalar's second derivatives; a body's far field is isotropic.
5. *A different notion of a bond's neighbours.* A longer reach adds numbers; the zero mode and the restoring term for the anisotropic modes stay as long as directions are coupled.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
That bonds have rates of their own is a supplied widening of block 54's clause, which by itself forces the product form. The comparison of a ray with a slow body needs an on-site rest energy, which block 54's walker does not have. T3 and T5(b) are weak-field, linear statements. T5(b)'s walls are held.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its rotations; the covariance sentence; the absences that motivate the clauses | yes (premise) |
| block 54 (open PR #8570) | the walk, its hop, the product form, the ray law, the reduced walk | yes (restated) |
| block 55 (open PR #8571) | the ledger; a source is the derivative of the clocked energy | yes (restated) |
| block 53 (open PR #8568) | the uniqueness argument that T3 re-runs | restated |
| blocks 56, 57 (open PRs #8573, #8578) | held walls; weight zero and the front a non-rate field can carry | placement |
| decision record (open PR #8572) | fork 6 | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "each rate sourced by the energy it times; a body at rest has no hop energy; three-number law with one scalar; bending over fall = `d log c/d log a`; no algebraic local tie; a cross term gives `1 + β`" | executed: hop energies on 108 bonds and on-site energies on 36 sites of a `3×3×4` torus; a body at rest; a walker along one axis | executed: block 55's energy density against half the hop energies at each site | executed: the classes of bonds near a bond; the law's matrix at zero wave vector, its isotropic mode and its row sums at a rational wave vector | executed: exact rays for three relations between bond and site rates; three clauses for a length under a change of unit; the cross-term law on a segment | T1, T2 all amplitudes and rates; T3 the stated reach; T4 rays; T5(a) algebraic clauses, T5(b) linear static laws with held walls; bond rates themselves, their law's numbers, `β`, a rest energy not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; whether it bears on a relation between site rates and bond rates is not decided here and it is not used. `scale_reference_primitive` converts units; `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "Half the bending is a known failure of scalar theories; why re-derive it?" Reply: because the owner's direction is, so far, such a theory, reached from three clauses, and the decision record should carry the fact with its exact form in the framework's terms: the ratio is `d log c/d log a`, the clauses give 1, and the missing half is one free stiffness ratio, not a contradiction. Second objection: "Bond rates are an invention." Reply: they are a widening of block 54's clause, supplied and named as such; T1 is the reason to look at them — the walker block 54 actually has cannot tell a rate from a length. Third objection: "T5(a) is trivial." Reply: yes; it is there because the obvious way to get the second half — write `ℓ = 1/w` — is not available without a reference, and the note's first draft claimed more than that (see the Review record).

### N8 — Cross-cycle echo
Block 51 found the record layer's wind direction-dependent at every distance; block 54 found the walk's fall direction-dependent only at second order in the wave vector; here the bond rates' direction dependence is slaved to second derivatives of a scalar. Block 53 had one law and one number; block 55 fixed the second order; block 56 found the strong field a matter of choice unless a principle is added; here the law of bond rates has three numbers and the bending one more. The reference to the ambient rate, through held walls, is the same object in blocks 56, 57 and here.

## Falsifiers

- An amplitude and rates with `Σ t_b + Σ r_x ≠ ⟨H⟩`; a body at rest with a non-zero hop energy on some bond.
- A linear covariant shift-symmetric law of the stated reach outside the three-number family; one with `β ≠ 0` whose anisotropic modes have no restoring term.
- Rays of the stated energy function whose ratio of bending to fall is not `d log c/d log a`.
- An algebraic local clause for a length, unchanged by a change of the unit of rate, that differs between two uniform rate fields of different depth.

## Boundaries and non-claims

That bonds have rates of their own is supplied. Their law has three free numbers and the tie of lengths to rates one more; none is derived. A slow body needs an on-site rest energy, which one walker does not have; if rest energy is internal hop energy the ratio is one. T3 and T5(b) are linear, weak-field statements with held walls. A law of motion for lengths is not given. The comparator's value is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 57 and the decision record (PRs #8568, #8570, #8571, #8573, #8578, #8572, open): restated or placed.
- Named standard imports at definition level: linearity of an expectation in a parameter; orbits of a finite group; symbols of lattice operators; rays of an energy function; minimization of a quadratic form.
- Reference only: Einstein (1911, 1915); Eddington; Brans and Dicke; Regge.

## Review record
Supervisor-run block, the seventh of the source-link direction and the third of the owner's 12-hour campaign. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: block 54's clause forces the product form, so bond rates are a widening and must be named as one; the walker has no rest energy, so the comparison of a ray with a slow body is conditional on an on-site energy. A rigour lens: two statements of the first draft were too strong and were broken by the supervisor before the gates. First, "the anisotropic bond-rate modes are short-ranged": the refuting pass's transform solve showed a power law, not an exponential — the modes have a restoring term but are driven by the scalar's second derivatives, and the note now gives the slaving coefficient, checked at three off-axis points to a few per cent. Second, "no local law ties a length to the depth of a rate" (it stood in the file name): true for an algebraic clause, false for a field equation — a cross term in the field's energy does it, the ambient rate entering through the walls; the claim, the file names and T5 were rewritten, and the headline became "one more free number". A comparator lens: half the bending is the known mark of a theory of clock rates alone; named under the Premises and Prior art; several phrases the repository forbids are avoided. A strategy lens: the owner should have the fact in one sentence, with the size of what is missing. Refuting pass (`specs/supervisor_control_block59_refuter.py`, machinery disjoint from the runner's): W1 symbolic rays; W2 the law's matrix with symbolic numbers (eigenvalues, the scalar's stiffness, the drive of the anisotropic modes); W3 an isotropic source on a `48³` torus by transform: anisotropic parts against the slaved form at three points; W4 a random complex amplitude on a `4³` torus: the parts add to the whole (`4×10⁻¹⁵`), finite-difference derivatives against `t_b` (`2×10⁻⁹`), a body at rest (`2×10⁻¹⁶`); W5 three clauses for a length under a change of unit, symbolically; W6 the cross-term law on a `7³` box (`5×10⁻¹⁷`). All pass. Mutation census: 10 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_2026_09_21.py
```

Expected: `TOTAL: PASS=15 FAIL=0`.
