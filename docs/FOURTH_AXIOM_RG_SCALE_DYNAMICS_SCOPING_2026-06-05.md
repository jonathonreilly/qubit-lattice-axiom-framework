# Fourth-Axiom Scoping — RG / Scale Dynamics for the Generation Yukawa Moduli

**Date:** 2026-06-05
**Type:** meta
**Claim type:** meta (historical fourth-axiom RG/scale-dynamics scoping note; non-claim source)
**Scope boundary:** Historical/provenance banking only. This note records an owner-authorized exploration of a candidate fourth axiom and its runner-backed scoping verdict; it does not add, approve, or revise any framework axiom, primitive, theorem, dependency edge, or publication surface.
**Audit boundary:** Independent audit lane only. This source note does
not set, predict, or ratify an audit outcome and sets no `effective_status`.
**Owner authorization:** owner-authorized EXPLORATION (scoping) of a
candidate fourth axiom — **NOT** adoption. No new axiom, import, or
boundary condition is added to the retained surface by this note.
**Primary runner:** [`scripts/cl3_fourth_axiom_rg_scale_dynamics_scoping_2026_06_05.py`](../scripts/cl3_fourth_axiom_rg_scale_dynamics_scoping_2026_06_05.py)
**Cache:** [`logs/runner-cache/cl3_fourth_axiom_rg_scale_dynamics_scoping_2026_06_05.txt`](../logs/runner-cache/cl3_fourth_axiom_rg_scale_dynamics_scoping_2026_06_05.txt)

---

## 0. Scope and question

A1/A2/A3 carry no dynamics. The per-sector generation Yukawa modulus

```text
r_sector = |b|^2 / a^2 ,        Koide  Q_sector = 1/3 + (2/3) r_sector
```

(for the `C_3`-circulant Yukawa `Y = a I + b U + b̄ U^{-1}` on the
`hw = 1 ≅ C^3` generation factor) is a **free input** per sector. This
note scopes a candidate **FOURTH AXIOM** supplying a
renormalization-group / scale (dimensional-transmutation) dynamics on the
qubit-lattice degrees of freedom, with the moduli emerging as **outputs**
— a UV fixed point, or a UV boundary condition running to the EW scale.

It is a **scoping** note: it states the candidate, builds a computable
toy RG flow, and enforces two honesty bars. It does **not** adopt the
axiom.

This **generalizes** the existing context note
`KOIDE_A1_PROBE_RG_FIXED_POINT_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_probe5.md`
(which closed the single-sector `r_lep = 1/2` fixed-point hypothesis as a
bounded obstruction) to the **four-sector** generic-values question, and
formalizes the **input-count** (relocation) bar, mirroring the
boundary-condition contamination already recorded for the Higgs
`λ(M_Pl) = 0` run in
`KOIDE_Z_S4B_RGE_IMPORT_TIER_REVIEW_NOTE_2026-05-08_probeZ_S4b_audit.md`
and
`KOIDE_Y_S4B_RGE_TIER_DOWNGRADE_CORRECTION_NOTE_2026-05-10.md`.

## 1. The two honesty bars

- **BAR 1 — Generic values.** Does the flow reproduce the OBSERVED moduli
  of all four sectors, or only special / fixed-point values? The four
  observed moduli (anchor only; PDG masses):

  | sector | observed `r` |
  |--------|-------------:|
  | lepton | `0.500` |
  | down   | `0.597` |
  | up     | `0.774` |
  | nu     | `< 0.5` (hierarchical normal ordering; band only) |

  These are **four distinct numbers** spanning `0.274` (over lep/down/up).
  A single scale-invariant fixed point is **one number**.

- **BAR 2 — Relocation / input count.** What does the flow take as INPUT
  (gauge couplings, a UV boundary condition, a scale reference, anomalous
  dimensions)? Do those inputs re-encode the moduli? Count inputs vs
  outputs. RG flows famously need a UV boundary condition; is the modulus
  derived, or is the boundary condition relabeled?

## 2. Computable findings (runner, 15/15 EXACT PASS)

### 2.1 BAR 1 — a fixed point is the wrong category for four distinct moduli

The four observed `r` are genuinely distinct (spread `0.274`). The best
single universal value (mid-range `r* = 0.637`) still misses a sector by
`0.137`. A **single scale-invariant fixed point gives one number and is
falsified by the quark sectors** — and, equivalently, an IR-attractive
fixed point **funnels generic UV data onto one value** (runner §2: seven
UV seeds `0.05 … 1.2` all land on the single attractor to `< 1e-2`). A
universal fixed point therefore reproduces at most one sector. This is the
WRONG-VALUES corner.

### 2.2 Toy `β(r)` and its fixed points (sympy)

For the most generic low-order one-coupling flow a 4th axiom could induce,

```text
dr/dt = β(r) = c1 · r · (r − r*) ,    fixed points  r = 0, r = r* ,
β'(0) = −c1 r* ,   β'(r*) = c1 r* .
```

With the IR convention `t → −∞` and `c1 > 0`, `0 < r* < 1`: `r = 0` is
IR-repulsive and `r = r*` is the **unique IR attractor** — and `r*` is an
**input of `β`** (a coefficient one writes down), not an output.

### 2.3 BAR 2 — running from a UV boundary condition is a relabel

A generic non-fixed-point flow over a finite window (e.g.
`dr/dt = −k r`, `k = 0.03`, 17 decades) gives the closed form
`r_IR = e^{−k·t_window} · r_UV = 0.309 · r_UV`, a **strictly monotone,
invertible** map. To land on each observed sector value one solves for its
**own UV boundary condition** (`r_lep` needs `r_UV = 1.618`, `r_down` needs
`1.932`, `r_up` needs `2.503`). The IR modulus is `r_UV` pushed through an
invertible map: **supplying `r_IR` is supplying `r_UV`.** The modulus is
**relocated to the boundary condition**, not produced.

Input/output ledger (running option, per sector): **3 inputs**
(UV boundary condition `r_UV` = the modulus relabeled; scale reference /
window; anomalous-dimension coefficient `k`) → **1 output** (`r_IR`).
Outputs never exceed inputs.

### 2.4 The third option (IR-attractive funnel) does not beat relocation

The honest escape — an IR-attractive structure funnelling generic UV data
to the observed IR values **without itself being the input** — is tested
in four forms (runner §4):

- **(a) one universal attractor** → one value (BAR 1 fail);
- **(b) per-sector attractor** `dr/dt = c(r − r*_s)` → lands each sector on
  its observed value **only because `r*_s` was set equal to it**: the
  attractor location **is** the modulus (one input per sector, BAR 2 fail);
- **(c) sector-independent `β`, four UV seeds** → needs no in-window
  attractor, hence `r_IR = Φ(r_UV)` invertibly: four observed values need
  four UV boundary conditions (four inputs, same count as the free moduli);
- **(d) STEELMAN — one universal `β` + one shared UV BC driven by an
  EXISTING sector charge `q_s`** (the only configuration that could give
  four outputs from fewer inputs). Tested with the two most natural
  charges. It **fails on the observed numbers**: fixing the single rate by
  the lepton, hypercharge-like `Y^2` mispredicts down/up by `0.33`, and
  color/triality mispredicts by `0.65`. Decisively, **down and up carry the
  same color charge**, so a color-driven universal law forces
  `r_down = r_up`, contradicting `0.597 ≠ 0.774`. No existing single sector
  charge plus a universal scale law reproduces the four moduli; any fit
  re-tunes per sector.

**Toy structure theorem.** Producing `N` distinct sector moduli via scale
dynamics costs `N` inputs (`N` attractor sites OR `N` UV boundary
conditions). No configuration yields outputs `>` inputs for the modulus.

### 2.5 Standard-RG input ledger and the gauge-cancellation fact

A real RG flow that could move `r` needs: a UV boundary condition
(**is** the modulus at the cutoff), a scale reference (a **new
dimensionful primitive** A1/A2/A3 do not contain), gauge/Yukawa couplings
in `β_r`, and anomalous-dimension coefficients (matter-sector circulant
`β` is **not** retained content — an import). Crucially, the
**gauge-coupling channel cannot supply `r`**: a uniform dressing
`Y → f(μ) Y` leaves `|b|^2/a^2` invariant (runner §5: base `r = 0.360`,
dressed `r = 0.360` for `f ∈ {0.3, 1, 2.7, 11}`). So the only channels
that move the ratio are the UV boundary condition (which **is** the
modulus) and the matter-sector `β` coefficients (an unretained import) —
exactly the boundary-condition contamination already recorded for the
Higgs `λ(M_Pl) = 0` run.

## 3. Verdict

**RELOCATES** (to a UV boundary condition / the matter-sector `β`
coefficients), with a **WRONG-VALUES** corner for the single-fixed-point
sub-option (a fixed point gives one number; falsified by the distinct
quark sectors).

- **Input count:** `≥ N` (one per sector — UV boundary condition or
  attractor location) `+ 1` scale-reference primitive; the scale dynamics
  never uses fewer inputs than the `N` moduli it would explain.
- **Behavior:** a fixed point / IR attractor funnels generic UV data onto
  **one** value (cannot make four distinct moduli); a generic UV → IR run
  is an invertible map whose IR value is the boundary condition relabeled;
  the steelman universal-charge law is empirically closed by `r_down ≠
  r_up` at equal color.
- **No third-option escape** survives: the funnel does not beat
  relocation.

The candidate fourth axiom (RG / scale dynamics) does **not** derive the
generation moduli. It **relocates** the per-sector modulus to a UV
boundary condition (or to unretained matter-sector `β` coefficients) and
additionally requires a new dimensionful scale-reference primitive. The
single-fixed-point reading is independently falsified by the quark
sectors.

## 4. Not claimed

- No fourth axiom is adopted; no new axiom, import, literature comparator,
  boundary condition, or framing primitive is added to the retained
  surface.
- No closure of the modulus gap (`r = 1/2` chirality / readout gates) is
  proposed or implied. The status quo (per-sector `r` free) is unchanged.
- PDG masses appear only as the falsifiability comparator (the four
  observed `r`), never as a derivation input.
- This note sets no audit status; the independent audit lane owns all
  verdicts.

## 5. What this opens

The negative is sharp and points forward. Scale dynamics fails because the
modulus is a **dimensionless ratio invariant under the gauge channel** and
a fixed point is **one number** for **four** sectors. Two directions this
scopes for next attacks:

- A mechanism that fixes `r` must act on the **circulant amplitude ratio
  directly** (not via a dimensionful scale or a multiplicative gauge
  dressing, both of which are inert on the ratio) — consistent with the
  existing focus on the `r = 1/2` eigenvector-balance / chirality / readout
  gates rather than on dynamics.
- The four distinct sector values, with `r_down ≠ r_up` at equal color,
  argue that whatever selects `r` is **sector-structured by a non-color
  label** (the steelman ruled out color/hypercharge universal laws) — a
  constraint on any future selection principle, scale-based or otherwise.
