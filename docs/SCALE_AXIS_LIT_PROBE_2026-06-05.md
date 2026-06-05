---
claim_id: scale_axis_lit_probe_2026_06_05
claim_type: meta
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Scale-Axis Literature Probe + Wrong-Escape-via-Citation Check (2026-06-05)

**Claim type:** meta (literature provenance audit; no new science, no axiom, no import).
**Role:** classifies the three scale-axis "derived" claims as
GENUINE-FRAMEWORK-DERIVATION vs GAUGE-CONTENT-GENERIC vs IMPORTED-GUT-RESULT,
and runs the wrong-escape check (does citing a standard SM/GUT result under a
framework label relabel textbook physics as a framework win?).
**Method:** read the framework's own scale-axis notes on `origin/main`; cross-check
against the historical literature via web search.
**Optional runner:** none (provenance audit; all evidence is documentary).

This note does not modify any retained surface, any publication table, or the
status of any of the notes it audits.

---

## Notes audited (all present on `origin/main`)

| Note | ledger `effective_status` (2026-06-05) |
|---|---|
| `YT_WARD_IDENTITY_DERIVATION_THEOREM.md` (the `1/√6` core) | `audited_conditional` |
| `YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md` (√6 democratic route) | `retained_bounded` (audited_clean) |
| `YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md` (b-Yukawa / "unification") | `unaudited` |
| `YT_QFP_INSENSITIVITY_SUPPORT_NOTE.md` (Pendleton-Ross focusing) | `unaudited` |
| `QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10.md` (QFP attractor) | `unaudited` |
| `YT_BOUNDARY_THEOREM.md` (Ward BC transfer endpoint) | `unaudited` |
| `CHARGED_LEPTON_Y_TAU_WARD_COMBINED_NO_GO_NOTE_2026-05-10.md` (the tau side) | (no_go) |

Key context: only the **√6 democratic component-amplitude lemma** is
`retained_bounded`. Everything else on the scale axis is `unaudited` or
explicitly a no-go. The "scale-axis derivations" are therefore **already
self-labelled by the framework as bounded / candidate / surrogate**, not as
promoted closures. The probe's job is to confirm that the literature provenance
matches that honesty.

---

## Claim 1 — b-tau Yukawa unification

**Literature.** b-tau (and down-type/charged-lepton) Yukawa unification at
M_GUT is the canonical SU(5)/SO(10) result: Chanowitz-Ellis-Gaillard, Nucl.
Phys. B128 (1977) 506; Buras-Ellis-Gaillard-Nanopoulos, Nucl. Phys. B135
(1978) 66. The mechanism is representation-theoretic: in SU(5), `d^c` and the
lepton doublet `L` both sit in the **same** `5-bar`, forcing `Y_d = Y_e^T` at
M_GUT. The low-energy `m_b/m_τ ≈ 3` then arises because below M_GUT the
down-quark Yukawa runs with the QCD term (`-8g_3²` sits in `β_{y_b}`) while the
tau Yukawa, being colorless, does not — pure SM RGE running of two couplings
with different gauge charges.

**What the framework actually does.** It does NOT reproduce the SU(5)
mechanism, and it does NOT claim b-tau unification as a win. Two findings:

1. The framework has **no `y_τ(M_Pl)` Ward identity at all.**
   `CHARGED_LEPTON_Y_TAU_WARD_COMBINED_NO_GO_NOTE_2026-05-10` proves a no-go:
   the `1/√6` Ward construction is intrinsically a **color (SU(3) Fierz)**
   object (`y_bare = g/√(2N_c)`, `N_c=3`); the lepton doublet `L_L=(2,1)` is a
   **color singlet**, so there is no color sector to Fierz-contract and the
   entire single-cycle `y_τ` Ward surface is closed. The framework puts the
   bottom and the tau on **opposite** footings (bottom gets the √6 Ward; tau
   gets nothing) — the exact inverse of the SU(5) story, where down and lepton
   unify *because* they share the `5-bar`.

2. Where the framework does extend the Ward identity to a **second quark**
   (`y_b(M_Pl)=g_s/√6`, by the same Block-6 species-uniform Clebsch-Gordan as
   the top), it produces a top-bottom unified BC `y_t(M_Pl)=y_b(M_Pl)`, runs it
   forward through standard 2-loop SM RGE, and finds it is **FALSIFIED** —
   `m_b ≈ 140 GeV` (33× too big) and `m_t` collapses to ≈99 GeV (coupled QFP).
   `YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS` §0 is explicit that this kills the
   *species-uniform interpretation*, and the framework's retained `m_t` chain
   uses a *species-privileged* BC that does not unify b with t.

**Verdict: NOT A FRAMEWORK CLAIM (and where attempted, FALSIFIED).** There is
no live "b-tau unification" win to relabel. The SU(5) sharing mechanism is
absent (the tau has no Ward partner), and the one unification the framework can
write down (top-bottom, not b-tau) is internally falsified. The standard
down-vs-lepton RGE color-asymmetry (`-8g_3²` in `β_{y_b}` only) is **textbook SM
running that follows from gauge charges**; the framework neither adds to it nor
needs it, because its tau Yukawa is not Ward-derived. **Wrong-escape check:
PASS — the framework does not cite b-tau unification as a win.** (Note 1.6 of
the bottom-Yukawa note *names* "Chanowitz-Ellis-Gaillard 1977 structure" only
to identify the BC it is about to falsify, not to claim it.)

## Claim 2 — top quasi-fixed point (Pendleton-Ross / Hill)

**Literature.** The IR quasi-fixed point of `y_t` is Pendleton-Ross, Phys.
Lett. B98 (1981) 291 (fixed line) and Hill, Phys. Rev. D24 (1981) 691
(quasi-FP). It is a property of the SM (and MSSM) `β_{y_t} ∝ y_t(9/2 y_t² -
8g_3² - ...)`: large UV `y_t` focuses to an IR band (≈220 GeV in the original
SM estimate). It is "independent of the precise UV symmetry conditions."

**What the framework does.** `YT_QFP_INSENSITIVITY_SUPPORT_NOTE` cites
Pendleton-Ross (1981) by name and labels the focusing "**STRUCTURAL
(topological, not model-dependent)**" in its own import table. The framework
**adds exactly one thing**: a UV boundary condition `y_t(M_Pl)=g_lattice/√6`
(Claim 3), used as the IR-anchored value to *select a trajectory*. The QFP is
explicitly used as a **robustness argument** (any smooth flow obeying the same
BC + gauge anchor lands within ~3%), not as a top-mass predictor. The
framework's own `QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO` then proves the QFP
*attractor* does **not** close `m_t` to target (generic UV focuses to ≈218 GeV,
not 173), and the 2026-05-10 correction stanza in the insensitivity note demotes
even the `m_t=169.4 GeV` Ward-BC result to a **"trajectory-truncation artifact,"
not a QFP attractor closure**.

**Verdict: IMPORTED-SM-RESULT, correctly labelled.** The QFP physics is 100%
standard SM RGE, self-labelled "STRUCTURAL / not model-dependent." The only
framework-native ingredient bolted onto it is the UV BC of Claim 3. The
framework does NOT claim the QFP as its own derivation, and its own no-go
forecloses the naive "QFP predicts m_t" reading. **Wrong-escape check: PASS** —
the QFP is cited as imported structure, not relabelled as a framework win.

## Claim 3 — the Ward boundary `y_t(M_Pl) = g_lattice/√6`

**The `√6` factor.** From `YT_WARD_IDENTITY_DERIVATION_THEOREM`:
`y_t_bare = g_bare/√(2 N_c) = g_bare/√6`, where `2N_c = N_c·N_iso = 3·2 = 6` is
the dimension of the `Q_L=(2,3)` color-isospin carrier (equivalently the
unit-norm normalization `Z² = N_c·N_iso` of the composite scalar singlet). The
same `√6 = √(2N_c)` is the **canonical Yukawa-from-bilinear normalization
factor** for a quark bilinear in the fundamental of SU(3) × a doublet of SU(2):
it is a Fierz/Clebsch-Gordan constant, not a novel object. The
`YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE` note reaches the identical
`1/√6` from the S_6-democratic unit vector on the 6-dim carrier — same `6 =
2·3`, same gauge content, different dressing.

**Literature analog for `y_t = g`-type UV boundary.** Yukawa-gauge boundary
relations at a high scale are a standard genre: partial GUT relations,
Pendleton-Ross's own `y_t/g` *fixed line*, and trans-Planckian asymptotic safety
(Eichhorn-Held, arXiv:1707.01107, predicting `m_t ≈ 171 GeV` from a UV relation
fixing `y_t` in terms of the gauge sector). The framework's own
`YT_FIERZ_PROJECTION_DEFENSE` note carries Eichhorn-Held as an external
comparator. So "fix `y_t` to a gauge coupling at a UV scale, run down" is a
recognised mechanism class; the framework's instance is one member of it.

**Is `√6` framework-specific?** No — it is `√(2N_c)`, a group-theory factor that
appears in **any** model normalizing a fundamental-color quark Yukawa from a
bilinear/composite operator. It is "derived" only in the modest sense that the
gauge content (`N_c=3`, weak doublet) is separately derived; the factor itself
is gauge-content-generic.

**Verdict on Claim 3: MIXED — GAUGE-CONTENT-GENERIC factor + framework-specific
*normalization choice*.**
- The `√6 = √(2N_c)` factor: **GAUGE-CONTENT-GENERIC.**
- The *boundary equality* `y_t(M_Pl) = g_lattice/√6` (locking the Yukawa to the
  *non-perturbative lattice* coupling `g_lattice = √(4π α_LM) = 1.067` at M_Pl,
  rather than to the SM-EFT `g_3(M_Pl)=0.487`): **framework-specific** — it
  follows from the lattice Ward identity + the lattice-vs-EFT domain separation
  (`YT_BOUNDARY_THEOREM`), which is genuinely framework-native machinery. But
  the framework itself flags the bridge from the `H_unit` matrix element to the
  *physical* top Yukawa as an **admitted, not-derived input**
  (`YT_QUBIT_DEMOCRATIC` audit split: load-bearing core = the finite-dim `1/√6`;
  non-load-bearing/admitted = "this amplitude is the physical top response
  coefficient"), and `YT_WARD_IDENTITY_DERIVATION` is `audited_conditional`, not
  retained. So even the framework-specific part is **bounded, not closed**.

**Wrong-escape check: PASS.** The framework does not present `√6` as a novel
discovery; it derives it from `√(2N_c)` and labels the physical-Yukawa bridge as
open. The `y_t=g`-at-a-scale idea is acknowledged via the Eichhorn-Held
comparator.

---

## Overall verdict (how much is framework-native?)

| Piece | Classification | Framework adds |
|---|---|---|
| b-tau unification | **NOT a framework claim** (no `y_τ` Ward; tau is a color singlet). The one unification it can write (top-bottom) is internally **falsified**. | nothing — opposite footing to SU(5) |
| down-vs-lepton RGE color asymmetry (`-8g_3²` in `β_{y_b}`) | **IMPORTED / textbook SM** (true for any model with these charges) | nothing |
| top quasi-fixed point | **IMPORTED SM-RGE** (self-labelled "STRUCTURAL"), Pendleton-Ross/Hill 1981 | only the UV BC of Claim 3; own no-go forecloses naive "QFP→m_t" |
| `√6 = √(2N_c)` factor | **GAUGE-CONTENT-GENERIC** | derived only because `N_c=3`, doublet are derived |
| BC `y_t(M_Pl)=g_lattice/√6` (lock to lattice coupling) | **framework-specific but BOUNDED** (lattice Ward + domain separation; physical-Yukawa bridge = admitted) | the lattice-vs-EFT endpoint machinery |

**Bottom line.** The scale-axis "derived" content is **almost entirely standard
SM/GUT physics that follows from the separately-derived gauge content**, plus
**one** framework-specific, still-bounded ingredient: the choice to anchor the
top Yukawa to the *non-perturbative lattice* coupling at M_Pl (`y_t(M_Pl) =
g_lattice/√6`) under a lattice-vs-EFT domain separation. The `√6` is `√(2N_c)`
(gauge-content-generic); the QFP is Pendleton-Ross/Hill (imported, self-labelled
structural); b-tau unification is not a framework claim at all (the tau has no
Ward partner) and is falsified where attempted.

The fair, modest reading — **"these relations hold because the gauge content is
derived and standard SM/GUT relations then follow"** — is supported. The strong
reading — **"novel framework derivation of b-tau unification / the top
quasi-FP / the √6 boundary"** — is **NOT** supported. Crucially, the framework's
own notes already make exactly this modest claim: the QFP is tagged "STRUCTURAL,"
the SM RGE is tagged "STANDARD infrastructure," the `1/√6` is split from its
admitted physical bridge, and the species-uniform (b-tau-style) reading is
self-falsified. **The wrong-escape-via-citation check returns PASS on all three
claims:** no standard SM/GUT result is relabelled as a framework win. The only
correction this probe registers is one of *emphasis* in any synthesis prose that
might present "b-tau unification" or "the quasi-fixed point" as scale-axis
*wins* — they are, respectively, a falsified non-claim and an explicitly imported
structure; the single genuinely framework-native, load-bearing scale-axis input
is the bounded lattice-coupling Ward boundary `y_t(M_Pl) = g_lattice/√6`.

---

## References (literature)

- M.S. Chanowitz, J. Ellis, M.K. Gaillard, *Nucl. Phys.* **B128** (1977) 506 — down/charged-lepton Yukawa unification in SU(5).
- A. Buras, J. Ellis, M.K. Gaillard, D.V. Nanopoulos, *Nucl. Phys.* **B135** (1978) 66 — GUT mass relations / b-tau.
- B. Pendleton, G.G. Ross, *Phys. Lett.* **B98** (1981) 291 — Yukawa-gauge fixed line.
- C.T. Hill, *Phys. Rev.* **D24** (1981) 691 — top-Yukawa infrared quasi-fixed point.
- A. Eichhorn, A. Held, *Phys. Lett.* **B777** (2018) 217 (arXiv:1707.01107) — top mass from trans-Planckian asymptotic safety (UV `y_t`-gauge relation), used as the framework's own external comparator.
