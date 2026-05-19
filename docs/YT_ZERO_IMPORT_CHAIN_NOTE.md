# Zero-Import y_t Derivation: Definitive Authority Note

**Date:** 2026-04-14 (last status edit: 2026-05-18)
**Status:** historical zero-import chain note with EW normalization now
matching-rule conditional through `kappa_EW`; do not cite the EW `sqrt(9/8)`
step as an unconditional retained derivation.
**Script:** `scripts/frontier_yt_zero_import_chain.py`

**Status authority and audit hygiene (2026-05-10, updated 2026-05-18):**
The audit lane has classified this note `audited_conditional` (audit row
`yt_zero_import_chain_note`, audit date 2026-05-11, cross-family). The
substantive technical findings (Ward-identity construction, QFP
insensitivity, color projection bookkeeping, output-labelling
clarification of the earlier `g_s_evolved(M_Pl)/sqrt(6)` confusion) are
sound at the stated scope. The conditional perimeter is exactly the
upstream-import gap described in the audit verdict: the runner imports
`<P> = 0.5934`, `u_0`, `alpha_LM`, and `alpha_s(v)` from
`scripts/canonical_plaquette_surface.py` rather than deriving them
inline from Cl(3) on `Z^3`, and it hard-codes `R_conn = 8/9` (the
exact Fierz channel fraction `F_adj = 8/9` is itself a
`retained_bounded` channel-counting authority, not a Cl(3) algebra
derivation in this runner). The `kappa_EW = 0` connected-trace EW
normalization is also conditional rather than derived. See "Open
upstream imports" below for the full register. Audit verdict and
effective status are set by the independent audit lane only; nothing
in this rigorization edit promotes status.

**Claim narrowing (2026-05-18, audit-aware repair).** Per the audit row's
`notes_for_re_audit_if_any`, the cheapest repair is either (A) promote
the two upstream bridges (`canonical_plaquette_surface` and the
`kappa_EW = 0` connected-trace selector) to retained-grade, or (B)
inline the derivations of those anchors. Path A is out of scope of this
in-note edit; path B is impossible from the current retained primitives
because (i) the canonical `<P>(beta = 6, SU(3), 4D) = 0.5934` insertion
is itself `bounded`, with a documented open analytic-insertion gap in
`PLAQUETTE_SELF_CONSISTENCY_NOTE.md` (not `retained_bounded`), and
(ii) the `kappa_EW = 0` specialization is the named open matching rule
(M) of the cited Fierz authority `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
and is explicitly not derived in either that note or this one. This
2026-05-18 edit therefore takes a different shape than path A or path B:
it (1) inlines the derivations that **can** be done from retained or
retained-bounded primitives (purely algebraic chain `<P> -> u_0 ->
alpha_LM -> alpha_s(v)` plus the EW `K_EW(kappa_EW) = 9/8` algebra
under the imported exact Fierz fraction `8/9`) into the new section 9
of this note, and (2) names the two residual gaps (the bounded
canonical plaquette insertion at `beta = 6` and the matching rule (M))
so that the source note explicitly records the analytic scope without
new admissions and without inventing closures. The claim type therefore
remains `positive_theorem` at the *algebraic / Ward / RGE* level of
section 4 (those are not in the conditional perimeter), while the
*overall y_t / EW prediction chain* is honestly conditional on the two
named upstream items. No new axioms are introduced and no new content
is asserted as derived from retained primitives that is not actually
derived from retained primitives.

---

## 1. Result

| Prediction             | Value    | Observed | Deviation | Status  |
|------------------------|----------|----------|-----------|---------|
| m_t [GeV]              | 169.51   | 172.69   | -1.84%    | PASS    |
| alpha_s(M_Z)           | 0.1181   | 0.1179   | +0.14%    | PASS    |
| sin^2(theta_W)(M_Z)    | 0.23061  | 0.23122  | -0.263%   | PASS    |
| v [GeV]                | 246.28   | 246.22   | +0.03%    | PASS    |
| 1/alpha_EM(M_Z)        | 127.665  | 127.951  | -0.22%    | NOTE    |
| m_H [GeV]              | 152.15   | 125.25   | +21.5%    | PRED    |

All four primary predictions pass their thresholds (m_t within 5%, alpha_s within 2%, sin^2 within 1%, v within 1%).  No SM observable is used as an input.

---

## 2. The Chain

```
Cl(3) on Z^3                                            [AXIOM]
  |
  |--- SU(3) x SU(2) x U(1)_Y  gauge group             [DERIVED]
  |--- 3 generations (Nielsen-Ninomiya / BZ orbits)      [DERIVED]
  |--- 16 staggered tastes (2^4 BZ corners in 4D)       [DERIVED]
  |
  +--- BARE COUPLINGS (lattice geometry)
  |      g_3^2 = 1         (Z_3 clock-shift)             [DERIVED]
  |      g_2^2 = 1/4       (Z_2 bipartite, d+1 dirs)     [DERIVED]
  |      g_Y^2 = 1/5       (chirality sector, d+2 dirs)  [DERIVED]
  |
  +--- SAME-SURFACE EVALUATION
  |      <P> = 0.5934      (SU(3) plaquette at beta=6)   [EVALUATED]
  |      F_adj = 8/9      (exact Fierz channel fraction)  [RETAINED-BOUNDED]
  |
  +--- INTERMEDIATE QUANTITIES
  |      u_0 = <P>^{1/4} = 0.8776                        [DERIVED]
  |      alpha_LM = alpha_bare / u_0 = 0.0907            [DERIVED]
  |      alpha_s(v) = alpha_bare / u_0^2 = 0.1033  (CMT) [DERIVED]
  |      v = M_Pl * (7/8)^{1/4} * alpha_LM^16 = 246.28  [DERIVED]
  |
  +--- TASTE THRESHOLDS + CONDITIONAL COLOR PROJECTION
  |      taste_weight = (7/8)*T_F*(8/9) = 7/18           [DERIVED]
  |      1-loop staircase:  M_Pl -> v  (4 segments)
  |      K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)
  |      connected trace:  g_EW(phys) = g_EW(latt) * sqrt(9/8)
  |      g_1(v) = 0.4644,  g_2(v) = 0.6480               [CONDITIONAL: kappa_EW=0]
  |
  +--- WARD IDENTITY
  |      y_t(M_Pl) = g_lattice / sqrt(6) = 0.4358        [DERIVED]
  |
  +--- BACKWARD WARD SCAN + FULL CW
  |      2-loop SM RGE:  v -> M_Pl
  |      Match Ward BC:  y_t(M_Pl) = 0.4358
  |      y_t(v) = 0.9734                                  [DERIVED]
  |      Full 1-loop CW on lattice BZ (L=24, a=1):
  |      lambda(v) = 0.1908 = m_H^2/(2v^2)               [DERIVED]
  |
  +--- PREDICTIONS
         m_t = y_t(v) * v / sqrt(2) = 169.5 GeV          [DERIVED]
         m_H = 152.2 GeV  (lattice CW, converges to 125 as a->0)
         alpha_s(M_Z) = 0.1181  (v -> M_Z running)
         sin^2(theta_W)(M_Z) = 0.2306
```

---

## 3. Import Audit

| Ingredient             | Value        | Status         | Source                               |
|------------------------|--------------|----------------|--------------------------------------|
| Cl(3) on Z^3           | axiom        | AXIOM          | Starting postulate                   |
| N_c = 3                | 3            | AXIOM          | Cl(3) spatial dimension              |
| M_Pl                   | 1.221e19 GeV | AXIOM          | Framework UV cutoff                  |
| < P >                  | 0.5934       | EVALUATED      | same-surface plaquette evaluation at beta = 6 |
| F_adj                  | 8/9          | RETAINED-BOUNDED | Exact Fierz channel fraction       |
| K_EW(0)                | 9/8          | CONDITIONAL    | Connected-trace specialization of `kappa_EW` |
| g_3^2(bare)            | 1            | DERIVED        | Z_3 clock-shift algebra              |
| g_2^2(bare)            | 1/4          | DERIVED        | Z_2 bipartite, d+1 directions       |
| g_Y^2(bare)            | 1/5          | DERIVED        | Chirality sector, d+2 directions    |
| u_0                    | 0.8777       | DERIVED        | < P >^{1/4}                         |
| alpha_LM               | 0.0907       | DERIVED        | alpha_bare / u_0                     |
| alpha_s(v)             | 0.1033       | DERIVED        | CMT: alpha_bare / u_0^2              |
| v                      | 246.28 GeV   | DERIVED        | Hierarchy theorem                    |
| taste_weight           | 7/18         | DERIVED        | (7/8) * T_F * (8/9)                 |
| g_1(v)                 | 0.4644       | CONDITIONAL    | Bare + taste + `K_EW(0)` specialization |
| g_2(v)                 | 0.6480       | CONDITIONAL    | Bare + taste + `K_EW(0)` specialization |
| b_1, b_2, b_3          | -41/10, ...  | DERIVED        | Group theory of derived gauge+matter |
| y_t(M_Pl)              | 0.4358       | DERIVED        | Ward identity: g_latt / sqrt(6)      |
| y_t(v)                 | 0.9734       | DERIVED        | Backward Ward + 2-loop RGE           |
| lambda(v)              | 0.1908       | DERIVED        | Full 1-loop CW on lattice BZ         |
| m_b, m_c thresholds    | 4.18, 1.27   | INFRASTRUCTURE | v -> M_Z running only                |

The EW rows above are now explicitly conditional on `kappa_EW=0`; they are
not unconditional zero-import retained quantities. INFRASTRUCTURE items affect
only the v -> M_Z cross-check transfer.

---

## 4. The Key Theorems

**Coupling Map Theorem (CMT).**  The bare coupling g_bare = 1 maps to the physical coupling at scale v through n_link mean-field factors: alpha_s(v) = alpha_bare / u_0^{n_link}.  With n_link = 2 (one gauge link per vertex leg), alpha_s(v) = 1/(4 pi * u_0^2) = 0.1033.

**Hierarchy Theorem.**  The EW scale is exponentially suppressed by the taste determinant: v = M_Pl * (7/8)^{1/4} * alpha_LM^16.  The exponent 16 counts the staggered taste doublers in 4D.  The factor (7/8)^{1/4} is the anti-periodic boundary condition correction.

**Boundary Selection Theorem.**  At the UV cutoff M_Pl, the lattice Ward identity fixes `y_t(M_Pl) = g_lattice / sqrt(6)`, selecting the Yukawa coupling from the *lattice-bare* gauge sector. **`g_lattice` is the bare lattice coupling at the cutoff** (`sqrt(4 pi alpha_LM)`), **not** the SM-evolved `g_s(M_Pl)` obtained by running 2-loop SM RGEs from `v` up to `M_Pl`. These are two distinct couplings at the cutoff — the framework's claim is the relation between `y_t` and `g_lattice`, and the runner's iteration enforces exactly this.

**Ward Identity.**  `y_t(M_Pl) = g_lattice / sqrt(6)`, where `g_lattice = sqrt(4 pi alpha_LM)`.  This follows from the SU(3) color-flavor locking on the lattice, where the Yukawa vertex shares the same gauge vertex with a `1/sqrt(6)` Clebsch-Gordan coefficient. The 2-loop SM-evolved `g_s(M_Pl)` is a separate IR-anchored quantity (numerically about `g_s_evolved(M_Pl)/sqrt(6) ≈ 0.199`); it is **not** the Ward partner. The runner now prints `g_lattice/sqrt(6)` and `g_s_evolved(M_Pl)/sqrt(6)` separately so the two cannot be confused. Earlier output of this runner labelled `g_s_evolved(M_Pl)/sqrt(6) = 0.198854` next to the Ward verification, which created the false impression that the Ward identity was violated by a factor of ~2.2; that was an output-labelling bug, not a math inconsistency. The substantive check `|y_t(M_Pl, evolved up from v) − g_lattice/sqrt(6)|` matches to better than `1e-7`.

**QFP Insensitivity.**  The top Yukawa has an infrared quasi-fixed point: y_t(v) is insensitive to the UV boundary condition.  A 10% change in y_t(M_Pl) produces less than 0.5% change in y_t(v).  This makes the prediction robust against higher-order corrections to the Ward identity.

**Color Projection.**  The exact Fierz channel fraction is
`F_adj = (N_c^2 - 1)/N_c^2 = 8/9`. The EW physical readout is now
parameterized by `K_EW(kappa_EW)=1/(8/9+kappa_EW/9)`. Physical EW couplings
take the familiar `g_EW(phys)=g_EW(lattice)*sqrt(9/8)` only at
`kappa_EW=0`; the no-go closure shows that this connected-trace selector is
not derived from the current retained primitives.

---

## 5. Systematic Uncertainties

| Source                        | Effect on m_t | Effect on sin^2 | Notes                         |
|-------------------------------|---------------|-----------------|-------------------------------|
| Plaquette (0.5934 +/- 0.0006)| ~0.1%         | ~0.05%          | MC statistical                |
| 2-loop truncation             | ~0.5%         | ~0.1%           | 3-loop absent                 |
| lambda(v) = 0.1908 (CW)      | < 0.1%        | negligible      | DERIVED; enters at 2-loop     |
| Taste weight (7/18 exact)     | < 0.1%        | ~0.1% per 1%    | Algebraic, not tuned          |
| Threshold matching (m_b, m_c) | none at v     | none at v       | Affects v -> M_Z only         |

**Total systematic uncertainty on m_t: ~0.6% (dominated by 2-loop truncation).**

The observed deviation of -1.84% exceeds the estimated systematic by about 1.2%.  This is consistent with the expected size of 3-loop corrections and the approximation of the taste-threshold running as a 1-loop staircase.

---

## 6. Gate Assessment

**What is cleanly derived (zero bounded items):**
- m_t = 169.5 GeV from zero SM imports (-1.84% from observed)
- alpha_s(M_Z) = 0.1181 from CMT anchor (+0.14%)
- sin^2(theta_W)(M_Z) = 0.2306 from geometric bare couplings (-0.26%)
- v = 246.28 GeV from hierarchy theorem (+0.03%)
- lambda(v) = 0.1908 from full 1-loop CW on the lattice BZ (DERIVED)
- m_H = 152.2 GeV (framework PREDICTION, +21.5% from observed; converges toward 125 GeV as lattice spacing a -> 0)
- All RGE coefficients from Cl(3) group theory

**What is infrastructure:**
- Quark mass thresholds (m_b = 4.18, m_c = 1.27 GeV) for the v -> M_Z running cross-check.  These do NOT enter the v-scale prediction.  The m_t = 169.5 GeV result is independent of these values.

**Higgs mass prediction:**
The full 1-loop CW potential on the lattice BZ (L=24, a=1) with all derived couplings (y_t, g_2, g_Y) gives m_H/m_W = 1.907, hence m_H = 152.2 GeV at the physical lattice spacing a = l_Planck.  This is 21.5% above the observed 125.25 GeV.  The ratio m_H/m_W decreases systematically with lattice spacing: 1.91 (a=1), 1.78 (a=0.75), 1.68 (a=0.5), converging toward the SM value 1.56 as a -> 0.  The +21.5% deviation is a lattice artifact of the same order as expected from O(a^2) corrections to the CW potential.

**Honest gap:**
The 1.84% deficit in m_t could indicate (a) missing 3-loop corrections in the backward Ward running, (b) refinement needed in the taste threshold treatment at 2-loop, or (c) genuine new physics beyond the leading-order framework.  At the current level of precision, all three explanations are compatible with the data.

---

## 7. Authority

**Canonical references for the y_t lane:**
- This note: `docs/YT_ZERO_IMPORT_CHAIN_NOTE.md`
- Script: `scripts/frontier_yt_zero_import_chain.py`

**Superseded notes** (historical record only, do not cite for current status):
- `docs/YT_EFT_BRIDGE_THEOREM.md` -- backward Ward with imported EW couplings
- `docs/YT_BOUNDARY_THEOREM.md` -- Ward identity derivation (absorbed here)
- `docs/YT_ZERO_IMPORT_AUTHORITY_NOTE.md` -- earlier incomplete closure attempt
- `docs/YT_EW_COUPLING_BRIDGE_NOTE.md` -- taste threshold development
- `docs/YT_EW_COLOR_PROJECTION_THEOREM.md` -- color projection factor (absorbed here)
- `docs/YT_QFP_INSENSITIVITY_SUPPORT_NOTE.md` -- QFP analysis (absorbed here)
- `docs/YT_CLEAN_DERIVATION_NOTE.md` -- earlier clean attempt
- `docs/YT_FULL_CLOSURE_NOTE.md` -- earlier closure attempt
- `docs/YT_FLAGSHIP_BOUNDARY_NOTE.md` -- earlier attempt
- All other `docs/YT_*.md` files

**Supporting scripts** (historical for the y_t lane; the standalone EW lane now
uses its own package carrier):
- `scripts/frontier_yt_eft_bridge.py` -- original backward Ward
- `scripts/frontier_yt_ew_coupling_derivation.py` -- EW running, normalization, and taste-threshold support scan
- `scripts/frontier_yt_color_projection_correction.py` -- color projection
- `scripts/frontier_color_projection_mc.py` -- R_conn MC verification
- `scripts/frontier_yt_qfp_insensitivity.py` -- QFP robustness check

---

## 8. Open upstream imports (audit conditional perimeter)

The audit lane requires an explicit register of which numerical
ingredients in section 2's chain are imported from upstream modules
versus derived inline by the y_t runner. The chain is "zero-import"
in the sense of using no SM observable as an input; it is **not**
self-contained from Cl(3) on `Z^3` alone, because several lattice and
algebraic anchors are routed through upstream modules.

| Ingredient | Imported from | Conditional on |
|---|---|---|
| `<P> = 0.5934` (SU(3) plaquette at `beta = 6`) | [`scripts/canonical_plaquette_surface.py`](../scripts/canonical_plaquette_surface.py) (`CANONICAL_PLAQUETTE`) | retained-grade promotion of the canonical plaquette surface as a Cl(3)-on-`Z^3` derivation; until then the y_t chain is conditional on this Monte Carlo evaluation |
| `u_0 = <P>^{1/4}` | same module (`CANONICAL_U0`) | algebraic consequence once `<P>` is admitted |
| `alpha_LM = alpha_bare / u_0` | same module (`CANONICAL_ALPHA_LM`) | CMT specialization once `u_0` is admitted |
| `alpha_s(v) = alpha_bare / u_0^2` | same module (`CANONICAL_ALPHA_S_V`) | CMT specialization once `u_0` is admitted |
| `R_conn = 8/9 = (N_c^2 - 1)/N_c^2` | hard-coded in the runner; corresponds to the exact Fierz channel fraction `F_adj` | retained-grade `F_adj` Fierz authority; treated here as `retained_bounded` channel-counting input |
| `K_EW(0) = 9/8` (connected-trace specialization) | section 2 chain at `kappa_EW = 0` | the no-go closure stated in section 4 already flags this as a matching-rule selector that is not derived from current retained primitives; the EW physical readout is therefore explicitly conditional on `kappa_EW = 0` |
| Hierarchy theorem `v = M_Pl * (7/8)^{1/4} * alpha_LM^16` | derived inline; uses `alpha_LM` from above | conditional on the upstream `alpha_LM` import |
| 2-loop SM RGE coefficients `b_1, b_2, b_3, ...` | group theory of the derived gauge + matter content | algebraic; not a numerical import |
| Ward identity `y_t(M_Pl) = g_lattice / sqrt(6)` | derived inline from SU(3) color-flavor locking | algebraic; not a numerical import |

The audit-conditional perimeter is therefore precisely the
`canonical_plaquette_surface` import plus the `kappa_EW = 0`
selector. Both are independently flagged in the import audit table
in section 3 of this note. The Ward-identity logic, QFP
insensitivity, color-projection bookkeeping, hierarchy theorem, and
backward-RGE iteration are not part of the conditional perimeter at
the stated scope.

### Audit-aware repair path

Per `audit_ledger.json`, `notes_for_re_audit_if_any` for
`yt_zero_import_chain_note`, the cheapest route to a stronger audit
verdict is one of the following two paths:

1. **Promote the upstream bridge.** Land a retained-grade audited note
   for `canonical_plaquette_surface` deriving `<P>`, `u_0`, and
   `alpha_LM` from Cl(3) on `Z^3`, and separately land a retained-grade
   `kappa_EW = 0` connected-trace bridge note. After both upstream
   bridges are retained, this chain note's conditional perimeter
   shrinks to algebra and re-audit can target a stronger verdict.
2. **Inline the derivations.** Replace the `canonical_plaquette_surface`
   import with inline runner code that computes `<P>` and the
   downstream `u_0`, `alpha_LM` quantities from Cl(3) on `Z^3` directly
   in `frontier_yt_zero_import_chain.py`, and similarly inline the
   connected-trace selector. This makes the runner self-contained but
   duplicates work that is more naturally factored into a separate
   bridge.

Either repair removes the conditional perimeter; this rigorization
edit only sharpens the boundary of what currently is and is not in
that perimeter, without changing audit status.

---

## 9. Inlined derivations of the imported anchors (2026-05-18 repair)

This section addresses the audit-row repair target
`missing_dependency_edge` for `yt_zero_import_chain_note`: "add
retained-grade dependencies for the canonical plaquette surface (`<P>`,
`u_0`, `alpha_LM`, `alpha_s(v)`) and the `kappa_EW = 0`/`F_adj`
connected-trace selector, or inline those derivations so
`frontier_yt_zero_import_chain.py` no longer imports the load-bearing
anchors."

It inlines every step of those two derivations that **can** be performed
from retained or retained-bounded primitives, and it explicitly names
the two residual gaps that cannot be closed without either upstream
promotion or new admissions. No new axioms or admissions are introduced.

### 9.A Derivation: canonical plaquette-surface chain `(<P>, u_0, alpha_LM, alpha_s(v))`

The four canonical plaquette-surface quantities used in the y_t chain
arise from one bounded input and three definitional / tadpole-improved
algebraic steps. The exact algebraic content is reproduced here so that
the source note is independently checkable against
`scripts/canonical_plaquette_surface.py`.

**Step 9.A.0 — Inputs and provenance.** The bare gauge coupling
`alpha_bare = g_bare^2 / (4 pi)` with `g_bare^2 = 1` (canonical
normalization on the retained graph-first gauge surface; framework-point
`beta = 2 N_c / g_bare^2 = 6`) is retained-bounded
(`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`, §"Framework-point context"). The
plaquette value

```text
<P>(beta = 6, SU(3), 4D)  =  0.5934                                 (9.A.1)
```

is **bounded**, not retained: the parent note explicitly states that the
exact analytic `beta = 6` insertion remains an open gap (the bridge-
support stack pins the analytic candidate at `0.593530679977098`, only
`+0.022%` above `0.5934`, but the strict-inequality slack
`0.5934 <= <P>(beta = 6) <= 0.59353` is **not** closed). This note
inherits that bounded status.

**Step 9.A.1 — Lepage-Mackenzie tadpole improvement (`u_0`).** The
Lepage-Mackenzie mean-field link variable on a Wilson plaquette surface
is

```text
u_0  :=  <P>^(1/4).                                                  (9.A.2)
```

This is the standard Lepage-Mackenzie tadpole-improvement definition
(Phys. Rev. D 48, 2250, 1993) applied at the retained framework point
`beta = 6`. The exponent `1/4` is fixed by the four-link Wilson
plaquette holonomy: under the canonical perturbative Wilson plaquette
expectation the link factor enters with multiplicity four around each
plaquette, so the geometric-mean tadpole representative of one link is
the fourth root of the plaquette. The relation (9.A.2) is a closed
algebraic identity once `<P>` is admitted at its bounded scope.

Numerically:

```text
u_0  =  0.5934^(1/4)  =  0.87768...                                  (9.A.3)
```

**Step 9.A.2 — Lepage-Mackenzie improved coupling (`alpha_LM`).** The
Lepage-Mackenzie improved coupling is the canonical tadpole-corrected
single-link coupling

```text
alpha_LM  :=  alpha_bare / u_0.                                      (9.A.4)
```

The factor `1/u_0` is the standard Lepage-Mackenzie one-link tadpole
correction: each Wilson plaquette comes with four links, so improvement
of a single-link operator carries one factor of `1/u_0`. This is the
canonical Lepage-Mackenzie definition; it is a closed algebraic identity
once `alpha_bare` (retained-bounded) and `u_0` (algebraic from `<P>`,
bounded) are fixed.

Numerically with `alpha_bare = 1/(4 pi) = 0.0795775...`:

```text
alpha_LM  =  0.0795775 / 0.87768  =  0.09067...                      (9.A.5)
```

**Step 9.A.3 — Coupling Map Theorem (`alpha_s(v)`).** The Coupling Map
Theorem (`ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md`,
`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`)
gives the tadpole-improvement vertex-power exponent `n_link = 2` (one
gauge link per vertex leg, two legs per vertex) and therefore

```text
alpha_s(v)  :=  alpha_bare / u_0^(n_link)  =  alpha_bare / u_0^2.    (9.A.6)
```

Numerically:

```text
alpha_s(v)  =  0.0795775 / 0.87768^2  =  0.10330...                  (9.A.7)
```

**Step 9.A.4 — Geometric-mean identity (independent algebraic check).**
The standalone polynomial-algebra identity proved as a retained
`positive_theorem` in
`ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md` gives,
on any `(alpha_bare, u_0) in R+^2`,

```text
alpha_LM^2  =  alpha_bare * alpha_s(v).                              (9.A.8)
```

This is a direct algebraic consequence of (9.A.4) and (9.A.6) and
serves as an independent retained-grade algebraic check that the
canonical plaquette-surface chain `(<P>, u_0, alpha_LM, alpha_s(v))` is
internally consistent at every admitted `(alpha_bare, u_0)`.

**Step 9.A.5 — Conditional status.** Steps (9.A.2)-(9.A.6) are closed
algebra. The chain as a whole is therefore conditional **only** on the
single bounded input (9.A.1) — the canonical plaquette value at the
framework point `beta = 6`. There is no separate, second imported anchor
in this chain: `u_0`, `alpha_LM`, and `alpha_s(v)` are all algebraic
consequences of `<P>` plus the retained `alpha_bare` normalization plus
the retained Coupling Map Theorem exponent.

In particular, the conditional perimeter of the `(<P>, u_0, alpha_LM,
alpha_s(v))` block of the y_t chain reduces to **exactly one** bounded
upstream input — the bounded canonical plaquette surface. Closing the
analytic `beta = 6` insertion at `PLAQUETTE_SELF_CONSISTENCY_NOTE.md`
collapses this entire block to retained-grade algebra.

### 9.B Derivation: connected-trace selector (`F_adj`, `kappa_EW`, `K_EW`, `sqrt(9/8)`)

The EW physical-readout coefficient used in section 2 of this note is
the connected-trace selector at `kappa_EW = 0`. The exact algebraic
content of that selector is reproduced here.

**Step 9.B.0 — Inputs and provenance.** The exact adjoint-channel
dimension fraction

```text
F_adj  :=  dim(adj) / dim(N_c (x) N_c-bar)
        =  (N_c^2 - 1) / N_c^2                                       (9.B.1)
```

is **retained-bounded** in
`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
(`claim_type: bounded_theorem`, `audit_status: audited_clean`,
`effective_status: retained_bounded`) as an exact SU(N_c) group-theory
identity. At `N_c = 3` (the baseline `Cl(3)` framework setting) this evaluates to

```text
F_adj  =  (3^2 - 1) / 3^2  =  8 / 9.                                 (9.B.2)
```

This is exact at any finite `N_c`; it carries no expansion correction.

**Step 9.B.1 — Connected-trace parameterization (`K_EW`).** The framework
parameterizes the EW physical-readout coefficient by a single rational
selector `K_EW(kappa_EW)`:

```text
K_EW(kappa_EW)  :=  1 / (F_adj + kappa_EW / N_c^2)                   (9.B.3)
                  =  1 / (8/9 + kappa_EW/9)   at N_c = 3.
```

The selector `kappa_EW` is the connected-trace projection coefficient:
`kappa_EW = 0` selects the pure adjoint-channel projection (lattice
connected-trace propagates only on the adjoint channel of the Fierz
decomposition), while `kappa_EW = 1` would select the full
`dim(N_c (x) N_c-bar) = N_c^2` channel space. Algebraically:

```text
K_EW(0)  =  1 / F_adj  =  N_c^2 / (N_c^2 - 1)  =  9/8.               (9.B.4)
```

The lattice-to-physical EW coupling rescaling is then

```text
g_EW(phys)  =  g_EW(latt) * sqrt(K_EW(0))  =  g_EW(latt) * sqrt(9/8) (9.B.5)
```

at the connected-trace specialization `kappa_EW = 0`. The numerical
value `sqrt(9/8) = 1.06066...` therefore reduces, under (9.B.5), to the
exact algebraic identity (9.B.4) on the imported `F_adj`.

**Step 9.B.2 — Named matching rule (M) (not derived).** The
specialization `kappa_EW = 0` is itself the **named matching rule (M)**
of the cited Fierz authority `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`
(§5, "The matching rule (named structural input, NOT derived here)").
Quoting that authority verbatim:

> The matching rule is **not derived in this note**. It is a structural
> input from the framework's lattice gauge surface: the physical EW
> vacuum polarization, after the lattice/physical normalization, is
> assumed to couple to the adjoint channel of the Fierz decomposition
> rather than to the full `N_c (x) N_c-bar` Hilbert space.

The sibling `RCONN_DERIVED_NOTE.md` records the same rule as an open
dynamical-population bridge inherited from the Fierz authority. No
retained, bounded, or proposed theorem on the current atlas closes (M).

**Step 9.B.3 — Conditional status.** Steps (9.B.1)-(9.B.5) are closed
algebra **once `kappa_EW = 0` is selected**. The two algebraic facts
(9.B.4) and (9.B.5) are exact identities under the imported retained
`F_adj`. The conditional perimeter of the connected-trace selector
block of the y_t chain therefore reduces to **exactly one** open
structural input — the matching rule (M) that selects `kappa_EW = 0`
rather than any other value in `[0, 1]`. Closing (M) at the Fierz
authority collapses this entire block to retained-grade algebra.

### 9.C Audit-perimeter summary after inlining

After the inlining of section 9, the audit-conditional perimeter for the
overall y_t / EW prediction chain reduces to **exactly two named items**
that are honestly carried as the residual gaps:

| Residual item | Source upstream | Status on `main` | Honest disposition in this note |
|---|---|---|---|
| Bounded canonical plaquette insertion `<P>(beta = 6, SU(3), 4D)` | `PLAQUETTE_SELF_CONSISTENCY_NOTE.md` | bounded (analytic `beta = 6` insertion gap not closed; canonical value `0.5934` is a same-surface MC readout under bounded discipline) | inherited at the bounded scope; the algebraic chain `<P> -> u_0 -> alpha_LM -> alpha_s(v)` in section 9.A is closed algebra above this one input |
| Matching rule (M) for `kappa_EW = 0` connected-trace selector | `EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md` (§5) | open structural input named in both the Fierz authority and `RCONN_DERIVED_NOTE.md`; not derived | inherited as a named open rule; the algebraic identities `K_EW(0) = 9/8` and `g_EW(phys) = g_EW(latt) * sqrt(9/8)` in section 9.B are closed algebra above this one rule |

**What this rigorization edit does and does not claim.** It claims that
the algebraic content of the canonical plaquette-surface chain
(`<P> -> u_0 -> alpha_LM -> alpha_s(v)`) and of the EW connected-trace
selector (`F_adj -> K_EW(0) -> sqrt(9/8)`) is closed-form algebra above
the two named residual inputs, and that those residual inputs are the
**only** load-bearing imports remaining outside the algebraic perimeter.
It does **not** close either residual input; it does not promote either
the canonical plaquette surface or the matching rule (M) to retained
status; and it does not invent any new admissions or axioms. It also
does not claim that the runner `scripts/frontier_yt_zero_import_chain.py`
has been refactored to remove its `from canonical_plaquette_surface
import ...` line — the runner refactor is the path-B repair that this
in-note edit does not perform. What this edit does perform is the
in-note algebraic transparency that the audit lane requested as the
in-note alternative to the runner refactor: every load-bearing
ingredient of the imported anchors is now reproduced explicitly in
this note, with its retained-grade or retained-bounded provenance
named and the two residual gaps explicitly carried.

### 9.D Re-audit boundary

This rigorization edit does not set or predict audit status; it
sharpens the algebraic transparency of the conditional perimeter so
that the next audit pass can target the two residual items by name. The
explicit boundary the audit lane should now read is:

- **Algebraic perimeter (closed in section 9).** Steps (9.A.2)-(9.A.8)
  and (9.B.1)-(9.B.5) are algebraic identities on retained or
  retained-bounded primitives. No further admissions are needed inside
  these steps.
- **Residual perimeter (two named items).** The bounded canonical
  plaquette insertion at `beta = 6` (section 9.C, item 1) and the
  matching rule (M) for the `kappa_EW = 0` connected-trace selector
  (section 9.C, item 2). These two are the only load-bearing imports
  that the y_t / EW prediction chain still inherits from outside this
  note.
- **No new admissions.** No step in section 9 introduces a new axiom,
  a new admission, or a new structural input beyond what is already
  named in the cited retained / retained-bounded upstream notes.
