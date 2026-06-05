# Q1 keystone (angle B) — the holomorphic (det_C, r=1/2) reading does NOT overreach and is NOT cleanly sector-dependent via Dirac/Majorana, chirality, or color: it names two points on a continuous per-sector modulus, and only charged leptons sit on the holomorphic one

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** a clarification of the *structure* of the Q1 keystone (does the holomorphic reading overreach? is it sector-dependent via a clean discriminator?). It does **not** derive `r=1/2` for any sector, does not derive the per-sector readout, and does not consume PDG values as load-bearing inputs. Two prior framings are corrected; one positive sharpening is added.
**Runner:** [`scripts/q1_holomorphy_sector_dependence_2026_06_04.py`](../scripts/q1_holomorphy_sector_dependence_2026_06_04.py) (SCORECARD 23/23 PASS).
**Status authority:** independent audit lane only. This note does not set, predict, or propose an audit/effective-status outcome, and adds no axiom, import, or new theory language.

## The tension this resolves

A sister angle (angle A) tests whether the division-algebra structure **forces** the generation Yukawa to be read holomorphically (det_C → `r=1/2` → `Q=2/3`). Angle B is the consistency check: **if** the holomorphic reading were forced by structure shared across sectors, it would force `r=1/2` for *every* sector whose generation algebra is the real group algebra `ℝ[Z₃] = ℝ ⊕ ℂ`. But the observed Koide ratios are sector-specific and do **not** all sit at `r=1/2` (charged leptons ≈ `1/2`; up/down quarks ≈ `0.6–0.77`; neutrinos `< 1/2`). So either the forcing is wrong (overreach) or the holomorphic-vs-real reading is **sector-dependent** via some clean discriminator. This note determines which.

## The algebraic spine (signed readout)

On the `C₃`-character split of a positive 3-vector `v` (the retained Koide-cone variables `a₀, z`), with `r := |z|²/a₀²`, the **signed-eigenvalue** (Hermitian / det_R / Brannen-class) Koide ratio is the exact identity

```text
Q(r) = (1 + 2r)/3 ,     so     Q = 2/3 ⇔ r = 1/2 (det_C point),   Q = 1 ⇔ r = 1 (det_R default).
```

(This restates the retained cone-note `P1`; verified symbolically + numerically, runner block A. The singular-value/Yukawa readout breaks the clean identity off the sign-homogeneous window — runner A5 — consistent with the signed-vs-singular lever.) The point: on the signed readout, **what sets `Q` is the single continuous modulus `r`**, and `det_C`/`det_R` are just two distinguished values of it.

## Verdict: NOT-CLEANLY-SECTOR-DEPENDENT and NOT-OVERREACHING

### No overreach — the forcing premise is false (J_cs exists everywhere but is measure-neutral)

For **every** `ℝ[Z₃]` sector, Schur forces a complex structure `J_cs = (C−C²)/√3` on the doublet (eigenvalues `{+i,−i,0}`: a genuine complex structure `J²=−P_doublet` on the 2-d doublet — the "one complex mode" object — and `0` on the singlet axis; unique up to sign; `[J_cs,C]=0`). Its **existence is sector-independent** (runner O1). But `exp(θJ_cs)=SO(2)` preserves **both** the real volume measure (`det = 1`) **and** the holomorphic measure (`[U,J_cs]=0`, i.e. `ℂ`-linear) — it is **measure-neutral** (runner O2). So the *existence* of `J_cs` does **not** pick out `det_C`. Hence "holomorphic forced by the shared division-algebra structure" is **false**, and the overreach it would imply (`r=1/2` everywhere) does not occur. (This is the round-1 / round-4 J-hunt result, restated as the no-overreach guarantee.)

### Not cleanly sector-dependent — none of the three candidate discriminators sets the *generation* readout

The three proposed clean discriminators all act **off** the generation index, so they cannot set `r` per sector:

| candidate | where it lives | effect on generation `r` | verdict |
|---|---|---|---|
| **Dirac / Majorana** | spin / Nambu factor | factorizes as `(·) ⊗ I_gen`; charge conjugation = identity on `(e,μ,τ)`; the Dirac "`i`" restricts to the central scalar `i·I₃`, which **commutes** with every `C₃`-circulant `H` and **cancels in `r`** | **generation-blind** (runner DM1–DM4) |
| **chirality** | a grading `Γ_χ=(2/3)J−I` | the det_C/`U(1)_b` generator `G_U1=(C−C²)/√3` **commutes** with `Γ_χ` and with `C` (on-block); the chiral orbit-splitting grading is off-block. The two bits are **independent** | **orthogonal binary** (runner χ1–χ4) |
| **color / weak isospin** | color / isospin index | `U_c ⊗ I_gen` commutes with the generation operator and cancels in `r` | **generation-blind** (runner color1–color2) |

So **no** clean Dirac/Majorana, chirality, or color discriminator gives "charged leptons holomorphic (`r=1/2`), quarks real-ish, neutrinos degenerate" at the level that sets the generation-doublet modulus. The win the prompt hoped for — a clean per-sector mechanism — is **not** available through these three.

### The positive sharpening — det_C/det_R is a two-point question on a continuous dial

The decisive quantitative point (runner N4): `det_C` is the **single** value `r=1/2` and `det_R` the **single** value `r=1`. The observed quark moduli sit **strictly between** them (`r_up ≈ 0.77`, `r_down ≈ 0.60`), and the neutrino modulus **below** `r=1/2`. So quarks are **not** "det_R (`r=1`)" — they are **intermediate moduli**, and neutrinos are at neither special point. The holomorphic-vs-real binary therefore **does not classify all sectors**; it names two distinguished values of a continuous per-sector modulus `r`, and **only charged leptons happen to land exactly on the holomorphic point `r=1/2`** (and only as matched to data — not derived). The correct sector variable is the continuous modulus `r`, not a holomorphic/real label.

## Two prior framings corrected

1. **The coverage-audit "Q1 holomorphy = chirality, same binary" claim is refuted.** `G_U1` commutes with `Γ_χ`; the two bits are independent (runner χ; matches Correction #1 of `FLAVOR_DETR_DEFAULT_FULL_EXERCISE`). Flipping `det_R↔det_C` is **not** the same as flipping chirality.
2. **The "quarks read det_R" framing is imprecise.** Quarks sit at intermediate `r`, not at the `det_R` point `r=1` (runner N4). The det_C/det_R dichotomy is a two-point sampling of a continuum, not a per-sector classification.

## What this means for Q1

The Q1 keystone is **not** "holomorphic vs real, decided once per sector by a clean discriminator." It is the **per-sector value of the continuous Fourier modulus `r = |z|²/a²`** on the (largely-native, signed/Hermitian) readout. `det_C`/`det_R` are the two reference points `r=1/2` and `r=1`; charged leptons sit on the former, the other sectors elsewhere. So Q1 does **not** close the lane assignment by itself — it names a binary that turns out to be two points on the real dial that actually carries the per-sector information. This is consistent with (not weaker than) the standing charged-lepton result: the *structure* (3 chiral generations, the exact `Q=1/3+(2/3)r`, the `C₃` channels and carrier, the forced `J_cs`) is derived; the per-sector *value* `r` is the open modulus — matching the literature, where Koide & Nishiura (arXiv:1301.4143) leave the per-sector ratio a free fit for every sector.

## The next paths this opens (not a closing statement)

- The per-sector modulus `r` is one continuous number per sector. The natural live thread is a **finite-β KMS / modular-equilibrium** condition on the doublet operator block that could pin `|b|=a/√2` for the charged-lepton reference state (a non-tracial weight carries a nontrivial modular automorphism) — and, separately, whatever fixes the *different* quark/neutrino moduli. A per-sector modular/equilibrium reference state is the structure that would carry sector-dependence the three kinematic discriminators do not.
- Whether a lifted `M₂(ℂ) ⊗ (Z₂)³` substrate-parent couples the (independent) holomorphy and chirality bits is the open unification frontier flagged by `FLAVOR_DETR_DEFAULT_FULL_EXERCISE`; this note shows they are independent on `ℝ³`, so any coupling must come from the parent, not the generation algebra.

## No-Go Discipline Gate

- **N1 alternative routes:** four discriminator routes attacked (J_cs existence, Dirac/Majorana, chirality, color) plus the algebraic-spine + continuum-sampling argument; all are reported as negative-for-clean-sector-dependence + no-overreach, none as a positive derivation of `r`.
- **N2 wall independence:** the per-sector modulus `r`, the readout class (signed vs singular), and the absolute scale are separate residuals; this note touches only whether holomorphy is forced/sector-dependent.
- **N3 hidden-wall scan:** PDG masses appear **only** in sidecar block S2 (illustrative, explicitly non-load-bearing), matching the repo pattern of citing Koide phenomenology as a sidecar. No fitted selector or unit convention is load-bearing.
- **N4 residual matching:** the cited retained no-go/bounded rows match the residual they bound (measure-neutrality of `J_cs`, the `C³=I` rephasing obstruction, the off-block chirality gate), and are not cited as positive derivations.
- **N5 rhetoric audit:** "not cleanly sector-dependent / not overreaching" is a structural finding about the *form* of Q1, not a claim that `r=1/2` is derived or forbidden.
- **N6 partial-closure scan:** the structure (channels, carrier, `Q=1/3+(2/3)r`, forced `J_cs`) remains derived; the per-sector `r` remains open for all sectors.
- **N7 steelman:** a reviewer could note that a *different* sector property (a modular/equilibrium reference state) might still carry sector-dependence; this note explicitly flags that as the open path and does not foreclose it.
- **N8 cross-cycle echo:** this consolidates the J-hunt rounds (esp. round 3, Dirac-generation-blind) and the det_R-default exercises into the explicit overreach/sector-dependence check; it is not treated as an audit verdict.

## What this does NOT claim

- Does **not** derive `r=1/2`, `Q=2/3`, or any per-sector modulus.
- Does **not** derive the signed/Hermitian readout class (taken as the comparator-compatible class per the signed-vs-singular lever; that selection is a separate residual).
- Does **not** consume PDG values as load-bearing; the S2 sidecar is illustrative only.
- Does **not** add an axiom, an import, or new theory language; it relabels existing retained structure.
- Does **not** modify or promote any registry/Tier-A entry, and does not set an audit outcome.
- Does **not** load-bear on `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route`.

## Provenance (verified 2026-06-04)

- `Q(r)=(1+2r)/3` and `det_C`(r=1/2)/`det_R`(r=1); singular-value readout breaks the identity off the sign-homogeneous window; `J_cs` complex-structure-on-doublet + measure-neutrality of `exp(θJ_cs)`; Dirac scalar `i·I₃` and the continuous centralizer commute with `H` and cancel in `r`; `[G_U1,Γ_χ]=0`, `[G_U1,C]=0`; color factor `U_c⊗I_gen` leaves `r` fixed; `Q(r)` strict monotonicity; quark moduli strictly between `r=1/2` and `r=1`: verified directly (runner 23/23).
- Anchors (status verified vs `origin/main` ledger): `koide_c3_generator_rephasing_obstruction` (retained), `koide_z3_equivariant_anticommuting_no_go` (retained_bounded), `koide_anticommuting_operator_derivation_theorem` (retained), `koide_q23_block_weight_frontier` (retained_bounded), `koide_emergent_time_eta_conjugation_parity` (retained_bounded), `koide_frobenius_isotype_split_uniqueness` (retained_no_go).
- Consolidates: `FLAVOR_FIND_J_ROUND3_DIRAC_GENERATION_BLIND_2026-06-02`, `FLAVOR_FIND_J_CONSOLIDATION_KAPPA_IS_THE_INPUT_2026-06-02`, `FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30` (Correction #1), `FLAVOR_DOUBLET_ROTATION_EXHAUSTIVE_NOTE_2026-05-30` (Schur-forced `J_cs`), `CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10` (the `P1` spine).
- Stale-citation flag: `koide_signed_eigenvalue_vs_singular_value_readout` is `unaudited` on the ledger; used here only for the qualitative signed-vs-singular distinction, not cited as retained.
- Attribution: Koide & Nishiura `Z₃` parametrization (arXiv:1301.4143) leaves the per-sector ratio a free fit for every sector — this note's sidecar S2 is consistent with that and adds no derivation of any sector's value.

## Validation

```bash
python3 scripts/q1_holomorphy_sector_dependence_2026_06_04.py
```

Checks: the signed-readout `Q(r)` identity and its `det_C`/`det_R` points (block A); `J_cs` existence/uniqueness/measure-neutrality and the falsified overreach premise (block O); generation-blindness of Dirac/Majorana (block D/M), orthogonality of chirality (block χ), generation-blindness of color (block color); strict monotonicity of `Q(r)`, three distinct dial points, and the two-point-on-a-continuum sharpening (block N); the non-load-bearing empirical sidecar (block S2).
