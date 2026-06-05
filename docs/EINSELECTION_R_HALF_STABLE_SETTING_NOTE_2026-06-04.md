# Flavor — einselection / predictability sieve: r=1/2 (the C₃-CHARGE pointer basis, Q=2/3) is ONE of a DISCRETE set of STABLE einselection pointer-basis settings {r=0, 1/2, 1} on the Koide dial — STABLE, ROBUST, but NOT forced and NOT exclusive. Charged leptons sit at r=1/2 because their irreversible record monitors a C₃-respecting (K-real) interaction.

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** an interpretive reframe in einselection / predictability-sieve language (a verified pointer-basis-stability computation on the C₃ generation factor) + an explicit NO-OVERREACH verdict. This note does **not** force r=1/2, does not claim it is unique, and does not change any axiom; it characterizes the *stable-set structure* of the readout-basis dial. The lane assignment (which monitoring class a sector realizes) remains the standing physical input.
**Runner:** `scripts/einselection_r_half_stable_setting_2026_06_04.py` (SCORECARD 32/32).
**Cache:** `logs/runner-cache/einselection_r_half_stable_setting_2026_06_04.txt`.

## The frame (NOT "force r=1/2")
The charged-lepton Brannen modulus is `r = |b|²/a²` with `Q = 1/3 + (2/3)r`. The reading of the
generation Yukawa depends on the **basis the irreversible record monitors** — exactly the det_C-vs-det_R
choice, which a prior Q1 attack established is a *basis choice*, not forced. This note tests whether
**r=1/2 is a STABLE einselection pointer-basis setting** — one of a *discrete* set of stable settings on
the dial — using the **predictability sieve** (Zurek einselection): pointer states are the states that
survive monitoring (generate the least entropy under the decoherence channel); the stable pointer bases
are the fixed points of einselection.

The win sought (and obtained) is: **"r=1/2 is a stable, robust, non-exclusive pointer-basis setting"** —
NOT "r=1/2 is forced/unique."

## Set-up (generation factor C³ = regular rep of Z₃ = ℝ[Z₃] = ℝ⊕ℂ)
- `C` = cyclic shift (Z₃ generator), `C³=I`; `eig(C)={1,ω,ω²}` — the 3 **C₃-charge / Fourier modes**.
- `S = C+C² = J−I` — the **C₃-invariant, K-EVEN** (time-reversal-real) Hermitian sector observable,
  `eig(S)={+2,−1,−1}` → singlet (rank 1) + doublet (rank 2) = the **2 isotype sectors**.
- `A = i(C−C²)` — the **K-ODD** partner (`conj A = −A`, T-violating), `eig{0,±√3}`, resolves the doublet.

**Predictability sieve:** a monitoring interaction `H_int` decoheres the system; the pointer basis is the
one whose states generate the least entropy under the monitoring channel `N[ρ]=Σ P_k ρ P_k` (fixed points
generate exactly 0). Equivalent **Zurek commutant criterion**: pointer observable `O` is einselected by
`H_int` iff `[O,H_int]=0`.

## Verdict
### r=1/2 (C₃-charge eigenbasis) = **STABLE-SETTING**
For a **C₃-respecting, K-real** monitored interaction (couples to `span_ℝ{I,S}`), the **C₃-charge (Fourier)
eigenbasis is the einselected pointer basis**:
- the C₃-charge eigenstates are **exact `S`-eigenstates** (residual ~10⁻¹⁵) → they generate **ZERO entropy**
  under K-real C₃-respecting monitoring (they survive); position states generate +0.64 (they decohere);
- the C₃-charge observable `C` **commutes** with the monitor `S` (`[C,S]=0`) — Zurek pointer; position `X`
  does not;
- **ROBUST**: the C₃-charge basis stays the pointer (worst-case entropy gen ~2×10⁻¹⁵) over **2000 random**
  C₃-respecting couplings `H_int=g₀I+g₁S` — not fine-tuned;
- the C₃-charge pointer **setting is r=1/2**: the 2-isotype-sector entropy `S₂(r)` has a **concave interior
  max** at r=1/2 (`S₂''(1/2)=−1<0`, `S₂(1/2)=log2`) — a robust, **non-marginal** pointer setting.

This is a genuine STABLE-SETTING, not ONLY-MARGINALLY-STABLE: it is the entropy-min pointer basis, the
commutant of the whole C₃-respecting class, and a concave (not flat/inflection) extremum.

### {r=0, 1/2, 1} = a DISCRETE set of STABLE settings (multi-stable, NO overreach)
| setting | monitoring class (respecting `H_int`) | pointer basis | Q |
|--------|----------------------------------------|---------------|---|
| **r=0** | scalar / trivial (resolve `I`) | degenerate / democratic | 1/3 |
| **r=1/2** | **C₃-respecting, K-real** (resolve `S`) | **C₃-charge (Fourier / isotype-sector)** | **2/3** ← charged leptons |
| **r=1** | position (resolve site `X`, breaks C₃) | real position basis | 1 |

Each setting is the einselection **fixed point of its OWN respecting monitoring** (0 entropy gen) **and
decoheres under the others'** (position states gain +0.64 under `S`; C₃-charge states gain +1.10 under `X`).
So **r=1/2 is stable BUT NOT EXCLUSIVE**: no sector is *forced* onto r=1/2; different sectors einselect
different stable bases. This is the correct structure — the win, with no overreach.

### Coincidence with the records-flow dial fixed points — YES
The records-flow `r→2r²` (`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX`) has distinguished settings
r=0 (stable fixed point), r=1/2 (separatrix fixed point), and r=1 (doublet-collapse runaway endpoint).
The **three einselection-stable pointer-basis settings {0, 1/2, 1} are exactly these three**. The
pointer-basis settings ARE the dial's distinguished settings.

**Two notions of "stable", orthogonal and consistent.** The predictability-sieve stability here (robust
pointer basis = slow-decohering / commuting / entropy-min) is a *different axis* from the records-FLOW
dynamical stability of the separatrix note (where r=1/2 is the unstable saddle of `r→2r²`). Both are true:
a pointer **setting** can be einselection-robust (a concave `S₂` max, 0 entropy gen) while the **flow
between settings** repels from it. So this note does **not** contradict the separatrix note — it adds the
einselection reading and shows r=1/2 is a robust *occupancy* even though the inter-setting flow is repelling
(which is exactly why occupying it is a *lane assignment*, not a dynamical attraction).

## Honest residual (no overreach)
r=1/2 is stable **only under a C₃-respecting, K-real** interaction; under position monitoring the position
basis is the stable one and r=1/2 is not. **Which monitoring class a sector's record realizes is the
standing physical input** — the same det_C/det_R / K-reality / block-counting input mapped into every prior
framing (measure, state, partition, dynamics; now einselection). Specifically: K-reality is what kills the
3-mode (r=0-type full-charge) partition — resolving ω from ω² needs the **K-odd** `A` (T-violating). This
note supplies the *stable-set structure*; it does not supply the lane assignment.

## Net standing of the charged-lepton value (einselection frame)
- **Structure** — derived: 3 chiral generations, `Q=1/3+(2/3)r`, the C₃ channels, the carrier.
- **r=1/2** — **one of three stable einselection pointer-basis settings** (the C₃-charge eigenbasis under
  K-real C₃-respecting monitoring); robust, concave-max, commutant-characterized; NOT forced, NOT exclusive.
- **Open (natural form)** — the **lane assignment**: charged leptons sit at r=1/2 because their record
  monitors a C₃-respecting (K-real) interaction; *why that monitoring class* is the standing input, and the
  next path is whether the emergent generation coupling is C₃-respecting + K-real (the T-odd / chirality
  ingredient that would pin δ=0 is the candidate, per the 2-sector-modulo-K-reality note).

## The next paths this opens (not closing)
- Derive the C₃-respecting + K-reality of the actual emergent generation-monitoring coupling from
  framework baseline + emergent spacetime (would convert the r=1/2 *occupancy* into a derivation).
- Map the lane assignment across sectors: does the quark / neutrino record monitor a position-type
  (→r=1) or different interaction? The discrete stable-set predicts each sector occupies a distinguished
  setting; testing this against CKM/PMNS readouts is a concrete next object.

## Provenance (verified 2026-06-04)
- C³=I; eig(C)={1,ω,ω²}; eig(S)={+2,−1,−1}, S K-even; A=i(C−C²) K-odd, eig{0,±√3}; predictability sieve
  (C₃-charge 0 entropy gen / position +0.64 under K-real S-monitoring); [C,S]=0 vs [X,S]≠0; robustness over
  2000 random C₃-respecting H_int (worst ~2e-15); S₂ concave max at r=1/2 (S₂''=−1); position→r=1 (S₃ peak
  at 1); degenerate→r=0; the three settings ↔ the records-flow fixed points: verified directly (runner 32/32).
- Anchors (status checked on origin/main): `koide_emergent_time_eta_conjugation_parity` (retained_bounded),
  `koide_frobenius_isotype_split_uniqueness` (retained_no_go), `koide_c3_generator_rephasing_obstruction`
  (retained). The records-flow `r→2r²` map rests on `luders_rule_from_composition_consistency` which is
  **unaudited** on origin/main — flagged, and the coincidence claim (5b) uses only the elementary fixed-point
  arithmetic of `r→2r²`, not the audit status of the Lüders derivation. Matches Koide arXiv:1301.4143 (the
  per-sector ratio is a free fit).
- Sibling reframes this extends (consistently): `FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02`
  (r=1/2 = distinguished stationary point, the three lanes are distinguished points), `FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02`
  (records-FLOW fixed points; r=1/2 the saddle of the flow — orthogonal stability axis), `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`
  (einselection→2-sector partition modulo K-reality; the partition half). This note adds the *pointer-basis
  stability* statement and the *discrete stable-set / no-overreach* structure.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`. Does not
  change any axiom. claim_type=meta (interpretive reframe + verified pointer-basis-stability computation).
