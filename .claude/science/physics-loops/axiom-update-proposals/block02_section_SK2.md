# Block 02 — SK-2: P-ABJ route (c), the imbalanced/curved EVALUATION complex

**Date:** 2026-06-20
**Crack id:** SK-2
**Target:** Close P-ABJ route (c) WITHOUT a new axiom by showing the emergent
matter complex (where the ABJ anomaly is evaluated) is forced IMBALANCED/CURVED
(`χ != 0`) by A_min's own geometry — so the square-block no_go (which kills only
equal-sublattice EVEN tori) would not apply and the internal staggered index is
nonzero.
**Outcome:** **WALL STANDS — axiom/external premise needed.** No A_min-native
crack. The genuinely new path (the OPEN evaluation complex) was tried and is
decisively adjudicated: it is a *regulator* choice, not an A_min-forced feature.
**Runner:** `scripts/frontier_abj_pabj_evaluation_complex_imbalance_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_pabj_evaluation_complex_imbalance_2026_06_20.txt`
— `TOTAL: PASS=75 FAIL=0`.
**Status authority:** independent audit lane / owner is sole authority. This
section sets no audit verdict; `proposal_allowed = false`. READ-ONLY on
`docs/audit/data/`. No git ops.

---

## 1. What the no_go actually needs, and the exact door

`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30` proves the staggered
`ε`-index

```text
A_t[U] = Tr( ε exp(-t D[U]^† D[U]) ) = 0
```

for **every** U(1) background, on any finite **even periodic** `Z^4` torus with
**equal** `ε=+1` / `ε=-1` sublattices. The load-bearing hypothesis is precisely
`N_+ = N_-`: ε-parity ordering puts `D` in bipartite form
`[[0,B],[-B^†,0]]` with `B` **square**, so `BB^†` and `B^†B` share spectrum
including zero multiplicity ⇒ the signed heat trace cancels.

The no_go names its own escape (N1/N6/N7): *"an imbalanced or curved cell complex
with `χ != 0`"* (route (c) in the WALL_TO_GATE_MAP, fanout ~1105). So the only
combinatorial door to route (c) **without curvature** is a **sublattice
imbalance** `N_+ != N_-` making `B` rectangular. The runner's **Part A**
establishes the exact criterion:

> `N_+ = N_-` (square block, no_go applies) **iff at least one extent is EVEN**;
> **ALL-ODD** hypercubic extents give `|N_+ − N_-| = 1` exactly.

Confirmed across `3^4` (41/40), `3³×1` (14/13, single-clock `d_t=1`), `5×3³`,
`3³`, `5³`, etc. — all `|imbalance| = 1`. This is a chi-like cardinality imbalance
**with zero angular deficit / zero curvature**: it is the one curvature-free door.

## 2. Prior block, and the path it did NOT try

The prior block (block05 chi-native-curvature ray,
`frontier_abj_chi_native_curvature_routes_2026_06_20`, reconstructed from its
cached `.pyc`) probed **CLOSED** complexes and found:

- **Prong A** — the `Z_τ` time circle and any twisted (Klein/Möbius) gluing leave
  `χ = 0`: χ is a cell-count invariant; gluing changes orientability/homology,
  never χ. Enumerated flat-cubic tori (edge lengths 2..5): every one χ=0, every
  vertex link = 4 squares (zero deficit).
- **Prong B** — induced holonomy off the closed-shell sea gives a *state-dependent
  LOCAL* curvature `C` (0 on the sea, >0 off it) but **no monodromy `Q`**
  (winding 0) and **not law-invariant** ⇒ REGISTERED DATA (realized_state
  counterfactual clause), not a derivation, and never a global χ/`Q`.
- **Prong C** — a disclined square complex (cube surface, χ=+2) exists, **but a
  disclination is a vertex with `≠ 4` square links ⇒ it BREAKS the
  translation-invariant flat-cubic Lattice axiom** ⇒ ADMITTED curvature.

The prior block's net: every A_min-native **closed** complex is flat-cubic χ=0.
**It did not test the OPEN / boundaried / matter-occupied EVALUATION complex** —
exactly the PUSH-HARDER target here. The all-odd imbalance of Part A is invisible
to the prior block because a *closed* (periodic) all-odd torus is ill-defined for
this operator (Part B below), and the prior block only enumerated closed objects.

## 3. The new path: is the EVALUATION complex open and imbalanced? (Parts B, C)

**Part B — the periodic obstruction (decisive sub-result).** The only way an
imbalance could be *closed and translation-invariant* (and so survive as an
A_min-native object the way the prior block demanded) is an **all-odd PERIODIC
torus**. It does not exist as an `ε`-index surface: an odd extent makes that
direction an **odd cycle, which is not bipartite**, so the site-parity grading
`ε(x)=(-1)^{Σx_μ}` is not single-valued under the wrap and the staggered phases
`η_μ` are not periodic. The runner verifies, exactly:

- all-even periodic (`Z4^4`, `Z4×Z2³`): `{ε,D}=0` holds (`max = 0`);
- all-odd periodic (`3^4`, `3³`): `{ε,D}=0` **BREAKS** (`max|εDε+D| = 1.0`);
- one-odd-among-even periodic: **also breaks** — `{ε,D}=0` holds **iff ALL
  extents even**;
- `η_μ` wrap-flips **iff** the extent is odd.

So a curvature-free imbalance is **unreachable on any closed/periodic surface**.
The only remaining host is an **OPEN / boundaried** region.

**Part C — the OPEN evaluation complex is a live `χ != 0` surface.** Build the
massless staggered operator on an OPEN (Dirichlet/free-edge) all-odd box. With no
wraparound the grading is fine and the index is nonzero:

| open box | `N_+ : N_-` | `B` shape | `{ε,D}=0` | `A_t` | `= N_+−N_-`? | analytic index |
|---|---|---|---|---|---|---|
| `3^4` | 41:40 | (41,40) rect | `0` | `+1` (t-indep, spread 3e-15) | yes | +1 |
| `3³×1` (d_t=1) | 14:13 | (14,13) rect | `0` | `+1` | yes | +1 |
| `3³` | 14:13 | (14,13) rect | `0` | `+1` | yes | +1 |
| `5×3×3` | 23:22 | (23,22) rect | `0` | `+1` | yes | +1 |
| `3×3×1` | 5:4 | (5,4) rect | `0` | `+1` | yes | +1 |

The signed heat trace equals the open-box parity imbalance `N_+ − N_-` (the
boundary/open "χ"), is t-independent, equals the analytic graded zero-mode count,
and **survives an arbitrary random U(1) background** (gauge-robust). On this
surface the square-block proof genuinely fails (`B` is rectangular) and **P-ABJ
route (c) WOULD close**. This is the strongest form of the SK-2 hope, made
concrete — and it is exactly what forces the honesty gate below.

## 4. The decisive honesty gate: is the imbalance A_min-NATIVE? (Part D)

A crack requires `χ != 0` forced by **A_min-native** structure — not an admitted
geometry, not a realized-state choice. The open-box imbalance fails all three
nativity tests:

**D1 — the index FLIPS with the boundary condition (BC is not A_min-fixed).**
A_min's Lattice axiom is **infinite `Z^3` with NO boundary condition** (verbatim:
*"does not supply a … boundary condition … continuum or infrared limit"*). Both
PERIODIC and OPEN are A_min-admissible regulators. On the SAME even site set:
periodic → index 0, open → index 0 (even is balanced). The nonzero value appears
**only** for an OPEN all-odd box → `+1`. The index value is therefore *selected by
the regulator* (BC + extent parity), neither of which A_min supplies. A number
that flips `0 → ±1` across A_min-admissible regulators is **not A_min-forced**.

**D2 — even among OPEN boxes the imbalance is an extent-parity choice.** Open `4³`
(even) → 0; open `3³` (odd) → ±1; open `4×3×3` (mixed) → 0; open `5×3×3` (odd) →
±1. A_min supplies **no finite extent at all** (the lattice is infinite), so the
choice "all-odd finite box" is a region selection, not a forced feature.

**D3 — the realized-state occupied region's imbalance is REGISTERED DATA.** The
matter-side candidate ("the occupied region is intrinsically imbalanced") fails
the realized_state counterfactual clause. On a *balanced* A_min box (`4³`,
`N_+=N_-`, so nothing is forced), two law-admissible occupied regions of EQUAL
particle number (N=8) have DIFFERENT parity imbalance: a balanced 2×2×2 subcube
(imbalance 0) vs a `6-plus/2-minus` region (imbalance +4). A value that changes
under another law-admissible state is registered data, **not** derivation output
(`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11`, counterfactual clause) — exactly the
prior block's Prong-B finding, now made for the *cardinality/occupancy* channel
rather than the holonomy channel.

## 5. Primitive-disavowal check (registry rule 5 — no mis-citation)

- **Lattice axiom** grants `Z^3` adjacency but **disavows** any boundary condition
  and any finite extent. So *open-vs-periodic* and *extent-parity* — the only
  curvature-free imbalance levers — are **not A_min-granted**. Citing A_min for an
  open all-odd box would be mis-citation.
- **realized_state primitive** grants pointwise evaluation and **disavows** any
  value that would differ for another admissible state. The occupied-region
  imbalance (D3) is such a value ⇒ registered data, not a derivation. Citing it as
  a *forced* imbalance would be mis-citation.
- **scale_reference** (units-only) and **kinetic_isotropy** (OS0 form `c_t=c_s`)
  carry **no topological/cardinality content** and explicitly supply "no selector"
  / "no dimensionless content" ⇒ they cannot supply `χ != 0`.

No primitive is mis-cited; the attempt does not launder any disavowed content.

## 6. Verdict and consequence

**Cracked: NO. Wall stands; axiom/external premise needed.** Across every
A_min-native front the nonzero-index route is one of:
(i) an OPEN/boundaried region with all-odd extents — a **regulator** choice (BC +
extent parity), not A_min-forced (index flips `0 → ±1`, D1/D2);
(ii) curvature/disclination — already adjudicated **ADMITTED** by the prior block
(breaks the translation-invariant flat-cubic Lattice axiom);
(iii) a realized-state occupied region — whose imbalance is **REGISTERED DATA**
(D3). And the one closed/translation-invariant imbalance that could have been
A_min-native (all-odd periodic torus) **is not a valid `ε`-index surface at all**
(non-bipartite odd cycle, Part B).

Therefore `χ != 0` is **not forced by A_min-native structure**, and P-ABJ route
(c) does **not** crack without an external input. The honest residual is exactly:
*a boundary-condition / finite-region selection (which regulator the emergent
matter complex realizes), or the matter occupancy that fixes the evaluation
region* — content that lives in the **gauge-content / particle-content** family
(Cluster 3), or equivalently the P-ABJ premise (a)/(b) itself.

**Consequence for the proposal set:** SK-2 does **not** shrink Cluster 3. The
WALL_TO_GATE_MAP listed P-ABJ route (c) as a candidate no-new-axiom crack ("χ≠0 is
geometry"); this block demotes that flag — the geometry that yields χ≠0 is either
admitted curvature, a regulator boundary choice, or realized-state occupancy, none
of which A_min supplies. The P-ABJ wall therefore stands on all of routes (a)/(b)/
(c): the framework still needs **either** the standard ABJ-anomaly-to-inconsistency
premise (route a), **or** a framework-internal taste-singlet/Adams/overlap chiral
measure validated as a physical readout (route b), **or** an external boundary/
occupancy premise fixing the evaluation region (the sharpened route c). The full
ABJ fanout (~1105) remains attributed to **Cluster 3** (gauge-content/
particle-content), unchanged.

**What is genuinely new here (vs the prior block):** the prior block closed the
*closed*-complex case; this block (a) gives the exact balance criterion (all-odd ⇔
|imbalance|=1, the unique curvature-free door), (b) proves the *all-odd periodic*
host is non-bipartite and so disqualified for the `ε`-index, and (c) exhibits the
*open* evaluation complex as a live χ≠0 surface — then shows by a regulator-flip
(D1/D2) and a state-counterfactual (D3) that its imbalance is not A_min-native.
The wall is thus re-localized and **sharpened** onto the **boundary-condition /
finite-region / occupancy** selection — i.e. precisely the gauge-/particle-content
gate the minimal-axioms memo lists as open. Honest either way: the new path was
real, was pushed, and decisively does not deliver an axiom-free χ≠0.
