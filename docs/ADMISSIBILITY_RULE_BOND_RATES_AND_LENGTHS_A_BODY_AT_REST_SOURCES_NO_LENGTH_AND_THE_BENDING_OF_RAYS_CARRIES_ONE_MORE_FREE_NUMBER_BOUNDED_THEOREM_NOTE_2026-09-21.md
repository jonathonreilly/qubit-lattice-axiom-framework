---
claim_id: admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For a supplied linear generator with independent positive site and bond rates: logarithmic derivatives at fixed amplitude give its on-site and hop energy contributions. A real envelope with constant spinor has zero instantaneous hop energy, not a proven stationary body. The specified linear nearest-bond law has three coefficients and zero-wave-vector spectrum 0,-12*beta,-12*beta; for beta nonzero its normalized acoustic stiffness is (alpha+2*beta+2*delta)/3. Long-distance slaving requires additional stability and nondegeneracy assumptions. In a separately supplied ray dispersion, massive zero-momentum acceleration and massless axial transverse acceleration compare local logarithmic rate gradients. A separate positive scalar quadratic weak-field energy ties log length to log rate through a free signed stiffness ratio. No universal packet-force or empirical deflection result follows."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_2026_09_21.py
---

# Independent bond rates: energy derivatives, a normalized acoustic branch, and conditional ray acceleration

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within the supplied clauses of blocks 53 to 57 widened by a rate for every bond; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates and for amplitudes timed by them, widened by a rate for every bond; it reports what such rates and the lengths they define can and cannot do; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Independent bond rates are an additional mathematical model. Its generator depends only on bond rates when the on-site term is zero. This is a statement about that generator, not every possible measurement or interaction. Fixed-state energy derivatives identify variational source terms if the field equations are supplied; conservation alone does not uniquely require them.

A real envelope with a constant spinor has zero instantaneous hop expectation on every bond, without establishing a stationary bound body. The nearest-bond symbol has a twofold nonzero gap at zero momentum when beta is nonzero; its normalized scalar stiffness is `(alpha+2 beta+2 delta)/3`, correcting the original missing division by three. A nonzero gap alone does not guarantee stable invertibility or a universal far field.

The ray comparison applies at the same location and local bond speed: a massive particle at zero momentum versus the transverse acceleration of a massless axial ray. It is not an integrated bending or general wave-packet force theorem. A scalar weak-field cross-energy can tie log length to log rate with a free signed coefficient; it does not derive a nonlinear completion or an empirical normalization.

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

The bounded content is the explicit finite-rate energy decomposition, nearest-bond symbol and stated conditional models. Historical physical comparisons are not used as evidence for these conclusions.

## Theorem T1 — what one walker sees

*Statement.* If `m_x = 0` for all `x`, `H = Σ_b c_b h_b`: the site rates do not appear. Block 54's clause is the restriction of the `3N` bond rates to the product form `c_b = √(w_x w_y)` of `N` site rates.

*Proof.* By inspection. ∎

For this generator with no on-site term, rescaling all lengths by s at fixed site rates rescales all hop coefficients by 1/s. Additional observables or couplings could distinguish the fields; no universal observability claim is made.

## Theorem T2 — fixed-state logarithmic energy derivatives

*Statement.* `∂⟨H⟩/∂log c_b = t_b`, `∂⟨H⟩/∂log w_x = r_x`, and `Σ_b t_b + Σ_x r_x = ⟨H⟩`. For an instantaneous real envelope with constant spinor `(1, 1)` `t_b = 0` on every bond. For a plane wave of the walk along an axis, with its content along that axis, `t_b` vanishes on the bonds of the other two axes. In the product form, `e_x = r_x + ½ Σ_{b ∋ x} t_b`.

*Proof.* `⟨H⟩` is linear in each rate. For the rest content, `(1,1)σ_2(1,1)ᵀ = (1,1)σ_3(1,1)ᵀ = 0` and `(1,1)σ_1(1,1)ᵀ` is real, so `Re[(i/2)·real]= 0` on every bond. For the content `(1, 0)`, `⟨σ_1⟩ = ⟨σ_2⟩ = 0`. In the product form `∂/∂u_x` acts on the six bonds at `x` with the factor one half each. ∎

Under the separately supplied variational field equations, block 55's energy-density source is what this becomes when every bond's energy is made to slow the clocks at both its ends, in all directions alike. With rates of their own, the bonds a walker crosses are the ones it loads.

## Theorem T3 — a law for bond rates: three numbers, one scalar

*Statement.* The 8 rotations that keep a bond sort the 14 bonds within one site of its midpoint into three classes: 8 perpendicular and touching (squared distance ½), 2 collinear and 4 parallel (squared distance 1). A linear covariant law with the shift symmetry is `c_0 u_b + α Σ_coll u + β Σ_perp u + δ Σ_par u = s_b`, `c_0 = −2α − 8β − 4δ`. On the three fields `u_j(k)` (bonds along `j`, taken at their midpoints) its matrix is `M_jj = c_0 + 2α cos k_j + 2δ Σ_{l≠j} cos k_l`, `M_jl = 4β cos(k_j/2) cos(k_l/2)`. At `k = 0` its eigenvalues are `0` on `(1,1,1)` and `−12β` twice. For `β != 0`, projection onto the normalized uniform vector gives the isolated branch eigenvalue `−(α + 2β + 2δ)|k|²/3 + O(k⁴)`. The unnormalized sum of all rows has a coefficient three times larger; `(1,1,1)` is not an exact eigenvector at general nonzero k. And `(M(1,1,1))_j = −(δ + β/2)|k|² − (α − δ + β/2) k_j² + O(k⁴)`, so at long wavelength `u_j − ū = ((α − δ + β/2)/(12β)) (∂_j² − ∇²/3) ū`.

*Proof.* Count the orbits; expand the cosines. The anisotropic components are driven at order `k²` by the direction-dependent part of `M(1,1,1)` and restored at order one by `−12β`. ∎

The coefficient family has three parameters. For beta nonzero, the displayed anisotropic slaving relation is a small-k expansion away from direct anisotropic sources. Interpreting it as two extra powers of decay requires a stable elliptic scalar branch with nonzero stiffness, no other relevant symbol zeros and suitable localized sources and infinite-volume limits. Beta nonzero alone supplies none of these global conditions. With beta zero, the three directional fields decouple in this chosen symbol.

## Theorem T4 — bending against falling

*Statement.* For rays of `E² = a² m² + c² Σ_j sin² k_j`: for positive m at `k = 0`, `dv/dt = −c² ∇log a`; for `m = 0` and a wave vector along an axis across the gradient, the transverse acceleration is `−c² ∇log c`, exactly on the lattice. For parallel gradients, nonzero denominator, and the same local c, the ratio of the stated transverse components is `d log c/d log a`. No arbitrary direction, extended packet, or integrated scattering angle is covered.

*Proof.* `v_j = ∂E/∂k_j`, `dk/dt = −∇E`. At `k = 0`, `∂v_j/∂k_l = δ_jl c²/(am)` and `dk_l/dt = −m ∂_l a`. For the ray, `∂v_z/∂k_z = c²/E` at `k_z = 0` and `dk_z/dt = −(c ∂_z c) sin² k_x/E`. ∎

## Theorem T5 — what could tie lengths to rates

*Statement.* (a) Let `ℓ_b = G(w_x, w_y)` with `G` unchanged by a change of the unit of rate. Then `G` depends on `w_x/w_y` only, and `ℓ = G(1)` wherever the rate is uniform, however deep. `ℓ = w̄/√(w_x w_y)` is unchanged, and uses the ambient rate. (b) With the field energy `(S_u/2) uᵀΛu + (S/2) λᵀΛλ + κ λᵀΛu`, `S_u > 0`, `S > 0`, `|κ| < sqrt(S_u S)`, held walls, and a source for `u` only, the static solution has `λ = −(κ/S)(u − ū)`: `ℓ = (w̄/w)^β`, `β = κ/S`. (c) For the instantaneous zero-hop state and the chosen variational sources, this scalar ansatz has a source for u only. It is a separate one-length-field model, not an identification of all three bond fields of T3. In the smooth scalar identification c=a/ell, T4 gives the stated local transverse ratio `1 + β`. The signed coefficient obeys `|β| < sqrt(S_u/S)`. Exponentiating the linear log-field solution defines a length for this ansatz, not an exact nonlinear field theory.

*Proof.* (a) Weight zero. (b) Stationarity in `λ` is `Λ(Sλ + κu) = 0` inside with `Sλ + κu = κū` on the walls; the only such field is the constant. (c) `c = √(w_x w_y)/ℓ`, so `d log c = (1 + β) d log a`. ∎

The reference to the ambient rate comes in through the walls, not through the law — the same walls block 56 held to fix the unit of rate and block 57 used in its separate reference-clock wave model. `β` is the ratio of two stiffnesses of the field's energy. Nothing in blocks 53 to 57 fixes it; their clauses are the case `β = 0`.

## Historical experiments — deferred

Original packet simulations and comparator ratios are preserved on the original branch. They are not fresh canonical evidence and do not establish a universal force law or empirical bending normalization. The fresh runner checks finite exact energy identities, the local symbol, specified ray states and a scalar segment model.

## No-Go Discipline Gate

The note's negative sentences: the specified instantaneous zero-hop state gives no direct bond source under the variational model; an algebraic local clause cannot make a length follow the depth of a rate; the specified local rest-versus-transverse-ray comparison gives a ratio of one when c is proportional to a; the bond-rate law is not unique.

### N1 — Routes by which the sentences could fail
1. *Rest energy that is internal hop energy.* Such composite states require a separate effective-dispersion and source analysis. Dependence on bond rates alone does not prove a universal acceleration ratio; no exclusion of that route is claimed here.
2. *A cross term in the field's energy.* Found, and stated as T5(b): it ties lengths to rates with a free exponent.
3. *A source for lengths other than the ledger's.* Possible with other variational models; energy conservation alone does not uniquely fix a source.
4. *Bond rates that are not isotropic at long range.* The conditional small-wave-vector relation of T3 does not exclude additional zeros, instability or anisotropic sources.
5. *A different notion of a bond's neighbours.* A longer reach adds numbers; symmetry preserves the uniform zero mode, but coefficients can cancel the anisotropic gap despite directional couplings.

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
| "each rate sourced by the energy it times; a supplied real-envelope constant-spinor state has zero instantaneous hop energy; conditional three-number scalar mode; local transverse acceleration ratio = `d log c/d log a`; no algebraic local tie; a cross term gives `1 + β`" | executed: hop energies on 108 bonds and on-site energies on 36 sites of a `3×3×4` torus; a body at rest; a walker along one axis | executed: block 55's energy density against half the hop energies at each site | executed: the classes of bonds near a bond; the law's matrix at zero wave vector, its isotropic mode and its row sums at a rational wave vector | executed: exact rays for three relations between bond and site rates; three clauses for a length under a change of unit; the cross-term law on a segment | T1, T2 all amplitudes and rates; T3 the stated reach; T4 the specified local massive-rest and massless-axial ray comparison; T5(a) algebraic clauses, T5(b) linear static laws with held walls; bond rates themselves, their law's numbers, `β`, a rest energy not derived |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository; whether it bears on a relation between site rates and bond rates is not decided here and it is not used. `scale_reference_primitive` converts units; `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Strongest objections
The original scalar stiffness missed a factor of three by summing unnormalized components. The correction is explicit and executable. Zero instantaneous hop expectation is insufficient to establish a stationary body. Neither the conditional ray calculation nor generator parameter counting establishes a composite-body universality theorem.

### N8 — Cross-cycle echo
Block 51 found the record layer's wind direction-dependent at every distance; block 54 found the walk's fall direction-dependent only at second order in the wave vector; here the bond rates' direction dependence is slaved to second derivatives of a scalar. Block 53 had one law and one number; block 55 fixed the second order; block 56 found the strong field a matter of choice unless a principle is added; here the law of bond rates has three numbers and the bending one more. The reference to the ambient rate, through held walls, is the same object in blocks 56, 57 and here.

## Falsifiers

- An amplitude and rates with `Σ t_b + Σ r_x ≠ ⟨H⟩`; a real-envelope constant-spinor state with a non-zero hop energy on some bond.
- A linear covariant shift-symmetric law of the stated reach outside the three-number family; one with `β ≠ 0` whose zero-wave-vector anisotropic modes have no restoring term.
- The specified massive zero-momentum and massless axial ray states, at the same local c with parallel gradients and nonzero denominator, violating the stated transverse acceleration ratio.
- An algebraic local clause for a length, unchanged by a change of the unit of rate, that differs between two uniform rate fields of different depth.

## Boundaries and non-claims

That bonds have rates of their own is supplied. Their law has three free numbers and the tie of lengths to rates one more; none is derived. A slow body needs an on-site rest energy, which one walker does not have; the composite internal-hop case remains open. T3 and T5(b) are linear, weak-field statements with held walls. A law of motion for lengths is not given. The comparator's value is quoted as a comparator: no gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's silence on a time metric, amplitude dynamics and a conserved energy. Blocks 53 to 57 and the decision record (PRs #8568, #8570, #8571, #8573, #8578, #8572, open): restated or placed.
- Named standard imports at definition level: linearity of an expectation in a parameter; orbits of a finite group; symbols of lattice operators; rays of an energy function; minimization of a quadratic form.
- Reference only: Einstein (1911, 1915); Eddington; Brans and Dicke; Regge.

## Dependencies

The linked source notes are used only with the corrected conditional scopes stated here. Historical campaign decisions and deferred experiments are not premise authority.

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Companion source PR #8568](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8570](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8571](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8573](ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Companion source PR #8578](ADMISSIBILITY_RULE_A_DELAY_FOR_THE_RATE_FIELD_NEIGHBOUR_REFERRED_MOTION_DOES_NOT_PROPAGATE_A_REFERENCE_TO_DISTANT_CLOCKS_DOES_AT_A_SPEED_SET_BY_THE_LOCAL_RATE_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

Original author experiments and review history remain recoverable at PR #8581 head `7ff9b1540a3f53ff0072f6102d01968c127d151d` on `physics-loop/admissibility-induced-law-block59-bond-rates-and-lengths-a-body-at-rest-stretches-no-lengths-20260921`. Landing review corrects the normalized acoustic coefficient and narrows zero-hop, far-field and ray quantifiers. Auxiliary simulations are deferred. No independent audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_bond_rates_and_lengths_a_body_at_rest_sources_no_length_and_the_bending_of_rays_carries_one_more_free_number_2026_09_21.py
```

The fresh cache reports the executed checks.
