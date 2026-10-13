# C5 R19-28 report: set B with (Σ) — do set B's refereed walls survive, and what is set B's bill?

**Author and provenance.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 07:03Z to about 07:25Z. I edited no repository file and downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `S/` = `.../scratchpad/C5/R19-28/` (this folder).
- `vX` = the referee record of item X (in `TESTS`, or `P/agents/C5_X_referee*.md`). `rX` = `P/agents/C5_X_report.md`.

**Labels.** proved (a complete argument under stated hypotheses; mine, unrefereed) / checked (numerics run here) / suggested (argued, not proved) / reading (interpretation) / comparator (outside reference; RECALLED = from memory). Sources are marked **[ref]** (referee record) or **[worker]** (unrefereed).

**Inputs read in full or at the cited lines.** AX (all 233 lines); the C5 method (`TESTS:2302-2320`); the set-B records T1 (`TESTS:17-85`), T2 (`TESTS:87-141`), O1 (`TESTS:2376-2381`), O2 (`TESTS:2383-2394`), RK2 (`TESTS:1480-1510,1663-1675`), R2-1/R2-4/R2-5 pre-registrations and verdicts (`TESTS:2442-2611,2728-2756`), R10-2 (`TESTS:3971-3980,4280-4285`), the R19-28 item (`TESTS:8504-8531`); SUMMARY §§17, 21-26; `rR19-20` + `vR19-20`; `rR19-24` and its referee (recorded at `TESTS:8560-8571` during this run); PRICE_NOTE (v5 + v6 delta); the referee files for K1, K2, F2, R2-1, R2-4, R2-5, R10-2; the O5 synthesis's set-B table (`P/agents/C5_O5_synthesis.md:348-376`, same family, unrefereed).

---

## 0. Against the FIXED readings (`TESTS:8527-8530`)

**Reading: B-STILL-WALLED, on the literal registered setting.** Same-family worker reading; a referee is recommended because it is a wall-type reading.

- **The wall (cite): R10-2, the reflection-positivity (RP) clause** [ref] (`TESTS:4280-4285`; `P/agents/C5_R10-2_referee_verdict.md:20-23`).
  - Proper smooth-box Gaussian covariances fail both site RP and link RP. So do small correlator-continuous perturbations of them.
  - No smooth periodic two-point function is exactly O(4) on an open box.
- **(Σ) does not touch it.** (Σ) changes what gravitates. It does not change any matter or graviton two-point function: by Lemma E it is a graviton kinetic counterterm and nothing else [ref, `TESTS:8567-8568`].
- **No stated price passes it.**
  - The single exception, the whole-zone scalar SLAC, is link-RP, but its transfer spectrum runs continuously down to −1, which gives time-alternating energies down to zero [ref, verdict:12,23].
  - Arbitrary interacting bare box symbols lie outside the class. No construction is on record, and none is priced.
- **The registered setting contradicts itself inside R10-2's class (reading).** It asks for "a transfer matrix, records via RP, and box symbols per R10-2" (`TESTS:8517`). In that class, box symbols remove RP, so the OS transfer matrix and "records via RP" are lost.
  - (Σ) loses its domain as well. "The lowest state" needs a Hamiltonian (`rR19-20:112`; `vR19-20:74`, "a specified source/Hamiltonian identification"). On Euclidean Z⁴ that Hamiltonian is the OS transfer matrix (reading).

**The scope: what the wall depends on, stated so the reading is not overread.**
- **The wall rests entirely on the box-symbol component.**
  - The box symbols' registered purpose was to lower set B's 11 graviton tunings (`TESTS:3971-3974`). (Σ) now does that job by stipulation (§3).
  - On Z⁴ the matter cone needs no box: W(B4) already zeroes every dimension-4 speed row [ref T1, F2, O1].
  - So under (Σ) the box symbols are dispensable (reading).
- **Without them (O5's original set B, `TESTS:2426,2444`), R10-2 does not apply, and the reading would be OPEN, not B-PACKAGE:**
  - **R2-5 (records):** the registered realization, records in the OS-reconstructed theory, lies outside R2-5's theorem, and no construction meets that item's conditions (i)–(iii) [ref, `TESTS:2739`; `C5_R2-5_referee.md:75`]. So it is open, neither priced nor walled.
  - **RK2 K2:** coupled RP is unproved, and the O(κ²) Killing closure fails for the displayed realizations [ref, `C4_K2_referee.md:13-17`]. This is neither removed by (Σ) nor priced.
  - **R2-4:** it binds, and (Σ) makes it bind (§3.3). It is priced by its own named price.

**Against the expectation (`TESTS:8531`).**
- **Borne out:**
  - the surviving wall is an RP wall that (Σ) cannot touch;
  - the walls (Σ) does address are exactly the source-side ones: K1's 11, T2's stiffness floor, and O5's B5/B6.
- **Not borne out for the record wall.** R2-5 does not qualify as "a wall no price passes" for the registered "records via RP" realization, because OS-reconstructed records are explicitly outside its theorem.
- **Not anticipated:**
  - **(Σ) on Z⁴ needs no Lorentz condition** (checked, §3.1). The graviton cone is fixed by W(B4) plus the Ward identity alone.
  - **The C-box enthalpy hazard is absent on Z⁴ by symmetry** (proved, §3.2).
  - **Set B's bill is lower than C-box's under both bookkeeping conventions** (§4). The reading is decided by the walls, not by the bill.

---

## 1. In plain words

- **Gravity side.** With (Σ), set B's big gravity cost, K1's 11 hand-set graviton numbers, becomes the same kind of stipulation C-box makes: "the vacuum gravitates as a relativistic vacuum with zero Λ".
  - On the 4D grid that stipulation is smaller than on C-box's 3D grid. It fixes 12 conditions instead of 33, because the 4D grid's symmetry already ties the graviton's speed to light's.
  - A pleasant surprise: on the 4D grid the vacuum's pressure is automatically minus its energy density. So the huge "vacuum enthalpy" mismatch that threatens C-box across the electroweak crossover cannot arise for vacua.
- **Charge side.** The particle light cones need nothing: the 4D grid's 90° time–space turn protects them at every order.
- **What (Σ) cannot fix.**
  - **The "box" version of set B** (relativistic-exact symbols on a 4D box) breaks reflection positivity (refereed). Without reflection positivity there is no Hamiltonian, no real-time quantum theory, and nothing for "records via RP" or for (Σ)'s "lowest state" to refer to. As registered, set B is still walled.
  - **Dropping the box** removes that wall; (Σ) has made the box unnecessary. Three items then stay open or priced, none of them a gravity-source issue:
    - whether records can form inside the reconstructed real-time theory (R2-5, open);
    - whether matter plus graviton is jointly reflection-positive (K2, open);
    - Euclidean gravity's wrong-sign conformal mode (R2-4). (Σ) makes this one bind, because it stipulates exactly GR's form, and it costs a non-positive gravity weight or a non-real/non-local gravity bridge.

---

## 2. Setting, hypotheses, removed hypothesis, prior art

**Hypotheses (stated before titles).**
- **Set B** (`TESTS:2426,2444`; O5 B1–B6, `C5_O5_synthesis.md:352-359` [worker]):
  - Euclidean Z⁴ with a_t = a_s (ξ = 1);
  - the whole law covariant under Z⁴ translations and B4⁺ (W(B4) where reflections are also kept);
  - Admissibility read as the conditional of a reflection-positive Gibbs specification, with physical probabilities only after OS reconstruction;
  - the arrow of time in the state.
- **Registered additions** (`TESTS:8517-8518`): a transfer matrix, records via RP, box symbols per R10-2, plus (Σ), W1-weight (+N) and a carrier (R19-20).
- **(Σ) on Z⁴.** This is R19-20's rule (`rR19-20:101-107`) with O_h × T replaced by W(B4) and (ω, q) replaced by the Euclidean 4-momentum p. The lowest state is the vacuum of the OS-reconstructed transfer matrix. Analyticity of the vacuum response through O(p²) is assumed, as in `vR19-20:37`.
- **The graviton** is supplied (P-N1), as in every set.

**Removed hypothesis:** set B judged without (Σ).

**Excluded alternatives:**
- set B′ / LRL (the R3–R5 rounds), which is not Z⁴;
- RF3 (foliated gravity on Z⁴ matter), which is not set B because set B has no foliation;
- sets A and C.

R5-x are LRL items. They apply only through R5-3 (⟨Λ⟩ OPEN in every set, `TESTS:2985`), which (S) ⊂ (Σ) handles by stipulation.

**Prior art, each counted once:**
- T0, T1, T2;
- C4 F2, K1, K2, RF3;
- K7a (via `PRICE_NOTE:23`);
- O1, O2;
- R2-1, R2-4, R2-5;
- R10-2;
- R19-12, R19-15, R19-19 [worker], R19-20, R19-21, R19-23, R19-24 (all with verdicts, recorded at `TESTS:8099-8571`);
- `B_referee.md:23`, cited by `PRICE_NOTE:117`, for the W(B4) mass count of 3;
- the O5 set-B table [worker].

---

## 3. (a)+(b) The set-B walls, classified, and what (Σ) does to each

| # | Wall (verdict) | Citation | Side | Does (Σ) remove it? | Status in set B + (Σ) |
|---|---|---|---|---|---|
| 1 | **RK2 K1:** N_tune(Z⁴) = 11 = 3 mass + 8 kinetic, after a separate CC tadpole (CWC) | `TESTS:1663-1667`; `C4_K1_referee.md:3,15` | **source** (the lowest state's linear graviton response) | **Yes**, in the law-functional bookkeeping: (Σ) on Z⁴ imposes exactly these 11 Ward conditions plus Λ = 0 (checked, §3.1). In codimension bookkeeping it re-books them; vR19-24: Σ "imposes, not predicts" (`TESTS:8569-8570`) | removed by stipulation |
| 2 | **T2:** RP hypercubic kernels keep a power-law TT stiffness floor (bounded FAIL, CWC) | `TESTS:128-141` | **source** (lowest-state uniform-strain Hessian; vR19-15 Lemma H, `TESTS:8128`) | **Yes**, as for #1: the degree-0 part of (Σ) | removed by stipulation |
| 3 | **O5 B5/B6:** an exact identity or 11 tunings; Λ + E_g + mass forms | `C5_O5_synthesis.md:358-359` [worker] | **source** | **Yes** (#1–#2); Λ via (S) ⊂ (Σ) | removed by stipulation |
| 4 | **R10-2:** box symbols fail site and link RP (bounded FAIL, CWC). Without RP, the count is 5 + Λ | `TESTS:4280-4285`; verdict `:20-23` | **matter/graviton kinetic symbol and unitarity (RP)** | **No.** (Σ) supersedes the box's *graviton* purpose (11 → 5+Λ). It cannot restore RP for box symbols | **WALL for the registered setting**; inapplicable if the box symbols are dropped |
| 5 | **R2-4:** a positive local Gibbs realization cannot give GR: a ≤ 1/3, so γ ≤ 1/2 (DERIVED through gravity, CWC). The price is named | `TESTS:2728-2733`; `C5_R2-4_referee.md:34,77,80` | **gravity-sector weight (Admissibility positivity)**, not the vacuum source | **No. (Σ) makes it bind** (§3.3) | **priced:** "positivity of the sourced Euclidean weight must be abandoned; alternatively the bridge/constraint sector must become non-real or nonlocal" (`C5_R2-4_referee.md:77`) |
| 6 | **R2-5:** strict permanence plus bulk formation is impossible for classical non-negative NN RP slice laws; only boundary formation survives (SUGGESTED, CWC) | `TESTS:2737-2739`; `C5_R2-5_referee.md:72-75` | **record** | **No** | **OPEN for the registered realization:** OS-reconstructed real-time records are outside the theorem; no construction meets (i)–(iii). In the classical-slice reading, the outside-theorem escapes are probabilistic permanence (a Record price; P3's RP soft labels need near-degeneracy and an ru bound, "not only a one-parameter tuning", `C5_R2-5_referee.md:41`) or a non-RP tagged law (P2, which loses RP) |
| 7 | **R2-1:** an exact additive charge on a finite fibre is impossible, so it COLLAPSES-TO-A (bounded, one-particle/spectral). Its perfect-action covariance also fails OS RP | `TESTS:2748-2756`; `C5_R2-1_referee_verdict.md:9,11` | **matter** (the matter charge algebra) | **No.** But its motivating premise, that an exact identity is needed to avoid K1's 11, is superseded by (Σ) for the vacuum rows (reading) | **bypassed, with a residue:** in-band translation and boost defects at O((pa)²), i.e. dimension 6. Tree-level size about 2e-41 at nucleon momenta [ref O2, `TESTS:2390`]; dimension-6 LV margin 7.76 decades [worker, `C5_O5_synthesis.md:362`] |
| 8 | **RK2 K2:** O(κ) is exact; O(κ²) Killing closure fails for the scalar and the naive/staggered fermion (bounded); coupled RP unproved (INCONCLUSIVE, CWC) | `TESTS:1669-1675`; `C4_K2_referee.md:9,13,15,17` | **matter–graviton coupling beyond linear order; RP** | **No.** (Σ) is linear-order and lowest-state only (`rR19-20:216-219`, L1–L3) | **OPEN.** The closure factor is cos k_ρ (scalar) or cos 2k_ρ (fermion) (`C4_K2_report.md:126,130`), so in-band it is O((ka)²) (suggested). C-box's nonlinear Bianchi completion is equally unestablished (`TESTS:8132`) |
| 9 | **K7a/F2 matter content:** 4D staggered has 4 tastes; the leapfrog is unstable at the hypercubic tick | `PRICE_NOTE:23`; `C4_F2_referee.md:28`; `C4_K2_referee.md:13` | **matter** | **No** | **not a wall in the Euclidean form:** "9.899 is only a leapfrog instability", the Euclidean transfer is positive [ref]. Tastes and chirality: no class-wide no-go [ref R2-4, `C5_R2-4_referee.md:61-63,75`]. Doublers are shared with C-box, where they appear as charged-doubler relics (`rR19-20:234`) |
| — | **Positives, not walls:** T1, F2, O1 (dimension-4 speeds zero by W(B4)) | `TESTS:60,82,85`; `C4_F2_referee.md:33`; `TESTS:2379` | matter | — | charge block = 0 at every order; two-loop toy control zero [ref, `TESTS:8566`] |

### 3.1 What (Σ) imposes on Z⁴ (checked; `S/scripts/r1928_count_z4.py` → `.out`, 10 s)

I wrote this from scratch and imported nothing from R19-20. Setup:
- Kernels Π^{mnrs}(p) = C + D·pp with the symmetries (mn), (rs), (mn)↔(rs) and (ab).
- The Euclidean Ward identity p_mΠ^{mnrs}(p) ≡ 0.

| Group | one-point | deg-0 | deg-2 | total | Ward-exact (deg-0, deg-2) | Ward conditions |
|---|---|---|---|---|---|---|
| **W(B4)** (and B4⁺, identical) | 1 | 3 | 9 | **13** | (0, 1) | **11** |
| O(4) | 1 | 2 | 4 | 7 | (0, 1) | 5 |
| O_h × T (control) | 2 | 6 | 26 | 34 | (0, 2) | 30 |

- **The control reproduces R19-20's 34 and 30** (`vR19-20:22-35`). **W(B4) reproduces K1's** 3 masses, 9 kinetic forms and unique gauge-invariant combination (`C4_K1_referee.md:3`). **O(4) reproduces R10-2's 5 + Λ** (`verdict:15`). (checked)
- **So (Σ) on Z⁴ fixes 13 local numbers:**
  - 11 by the Ward identity (= K1's 3 + 8);
  - 0 by Lorentz conditions;
  - 1 by Λ = 0;
  - 1 by the Z convention.

  Compare Z³ × ℝ: 30 Ward + **2 Lorentz** + Λ + Z (`vR19-20:32-35`). (checked count; the split is proved from it.)
- **Why there are no Lorentz conditions** (proved, given the counts).
  - The W(B4) Ward-exact space is one-dimensional and contains the O(4) Einstein–Hilbert kernel. So it *is* linearized EH: under the Ward identity alone, the Z⁴ graviton cone equals the matter cone.
  - The one-point space is only δ_μν, which Wick-rotates to η_μν. So no separate W₀ exists.
  - This is the Z⁴ counterpart of R19-19's Lemma G. On Z³ that lemma leaves one isotropic speed row (`TESTS:8135` [worker]; `vR19-20:33`).
- **Of the 11 Ward conditions:**
  - 6 are hypercubic anisotropies (13 − 7);
  - 5 are O(4)-invariant Ward violations, namely 2 masses and 3 non-EH kinetic forms (checked by difference).

### 3.2 The lowest-state enthalpy vanishes on Z⁴ (proved)

**Hypotheses.**
- The lattice stress transforms as a rank-2 W(B4) tensor.
- The state is W(B4)-invariant, i.e. any vacuum of a W(B4)-covariant law.

**Claim.** ⟨T_μν⟩ = e·δ_μν (the only invariant, checked count 1). After OS rotation this is −e·η_μν, so ρ + p ≡ 0.

**Consequences.**
- W₀ ≡ 0 for every set-B vacuum, whatever the masses.
- The vacuum-to-vacuum enthalpy mismatch has no set-B counterpart. That mismatch is R19-20's item 3 and R19-21's 2.68e106 ρ_Λ on the D1 root, the latter confirmed [ref] (`TESTS:8553`). Its V1 version is the gap R19-27 [worker] addresses.
- On Z³ × ℝ the same object has two invariants (e₀, W₀), checked in the control row.
- Thermal states break W(B4) and carry the physical sT, plus lattice corrections (suggested: O((Ta)²) relative).

### 3.3 (Σ) makes R2-4 bind (reading, from two refereed facts)

1. **(Σ) is the graviton kinetic counterterm.** It sets the dressed quadratic action to (1/16πG + Z)E_EH [ref Lemma E, `TESTS:8568`].
2. **E_EH has a negative eigenvalue in Euclidean signature.** On the gauge quotient, the five traceless directions have +½p², and the normalized trace has −p² [ref, `C5_R2-4_referee.md:34`].

**So:**
- (Σ) is a real, local source bridge that reproduces linear GR, which is exactly R2-4's premise. R10-2's referee confirms R2-4 "binds unchanged" under "real summable source-bridge" premises (`verdict:18`).
- Set B + (Σ) must therefore pay R2-4's named price.
- **The payment consistent with K2 (suggested):**
  - keep only the TT polarizations in the transfer matrix, which is positive [ref, `C4_K2_referee.md:13`];
  - carry the Newtonian/conformal part as a non-local constraint bridge.

  That is R2-4's "nonlocal bridge/constraint" escape. Coupled RP of this arrangement is not computed.

### 3.4 Non-lowest-state hazards carried over from C-box (suggested)

- **The shear mismatch survives on Z⁴.** W(B4) allows 3 mass forms (checked count; `B_referee.md:23` via `PRICE_NOTE:117`), including 2 in TT. A lowest-state-tied (Σ) therefore leaves a pre-crossover shear mismatch, as on Z³. Its size is not computed.
- R19-21 is NOT CONFIRMED → OPEN on C-box [ref, `TESTS:8548-8557`]. The same openness applies here.

---

## 4. (c) The total bill: set B + (Σ) against C-box + (Σ)

Count once with vR19-12, vR19-20 and vR19-24. "Bill" means numbers and clauses on one law, as in `rR19-20:280-284` and `rR19-24:324-327`. Axiom prices are in §5.

| Block | C-box + (Σ) | Set B + (Σ) (box-free) | Source |
|---|---|---|---|
| Gravity, law-functional bookkeeping | 0 numbers; (Σ), W1-weight (+N), carrier: "a proposed three-component package" | 0 numbers; the same three. The carrier is still needed if the arena grows (ė₀ in a growing lattice, cf. `TESTS:7806-7807`), though no longer for W₀ (§3.2) | [ref] `vR19-20:64`; §3.2 proved |
| Gravity, codimension bookkeeping | **33** imposed conditions (30 Ward + 2 Lorentz + Λ) + Z | **12** (11 Ward + Λ) + Z | [ref] `vR19-20:37`; **checked** §3.1 |
| Charge block | 4 per class / 10 per species, re-set at every order. Under the law-functional precedent: 0 numbers + 1 clause (D1∞) | **0, by W(B4), at all orders, no clause** | [ref] `TESTS:8102,8569`; [ref] T1/F2/O1; [ref] two-loop toy control `TESTS:8566` |
| CC | 0 numbers via (S) ⊂ (Σ) (1 imposed condition) | same | `rR19-20:283` |
| **Total, law-functional** | **0 numbers, 4 clauses** (3 + D1∞) | **0 numbers, 3 clauses** | reading on refereed parts |
| **Total, codimension** | **33 + 4/class (10/species) at every loop order** | **12** | checked + [ref] |

**Bill comparison (checked against the verdicts).** Set B + (Σ) is lower than C-box's under both conventions.
- The saving is the charge block, by symmetry.
- On top of that, (Σ) itself is smaller on Z⁴: 21 fewer imposed conditions, including both Lorentz conditions.

This meets B-PACKAGE's bill clause. B-PACKAGE fails only on its wall clause.

---

## 5. (d) Prices (named, none adopted; counted once)

- **B1 / P12 (Lattice).** Z³ → Z⁴ with a_t = a_s (`AX:37`; `PRICE_NOTE:366`).
- **B2 (Admissibility, covariance).** Whole-law B4⁺ covariance: regulator, counterterms, records (`AX:57-58`).
- **B3 (Admissibility, probability).**
  - The site distribution is the conditional of a reflection-positive (RP) Euclidean Gibbs weight. Physical probabilities exist only after OS reconstruction (`AX:60-61,63-73`).
  - **Plus R2-4's price, now forced by (Σ):** the gravity sector's Euclidean weight is non-positive, or the bridge is non-real or non-local (`C5_R2-4_referee.md:77`).
  - **Chiral matter (suggested):** Ginsparg–Wilson/overlap couplings (quasi-local), or 4D tastes/doublers (2⁴ − 1 corners), or Wilson-type additive mass tunings (comparator, RECALLED). No class-wide no-go [ref].
- **B4 (Record).**
  - The arrow sits in the state (Lemma E [ref]).
  - "Records via RP" means records formed in the OS-reconstructed real-time theory. Record's sites are then the reconstructed slice sites, not Z⁴ events (reading; `AX:77-83`).
  - This realization is OPEN (R2-5).
- **(Σ), W1-weight (+N), carrier.** Unchanged in kind from R19-20 (P-R19-19a, P145 + P-r193a, P70/P52 or P-r1917c).
  - On Z⁴ (Σ) = 11 Ward + Λ (checked).
  - **W1-weight on Z⁴ (suggested):** it must name the Ward-renormalized lattice stress. On a hypercubic lattice the traceless stress splits into 3 + 6 irreps with separate finite renormalizations, fixed by translation Ward identities (comparator, RECALLED: Caracciolo–Curci–Menotti–Pelissetto 1990; Giusti–Pepe).
- **Box symbols.**
  - **If kept:** R10-2's RP failure, which no price passes. **The wall.**
  - **If dropped:** the dimension-6 in-band residue O((pa)²), from rows 7–8.
- **Growth arena (suggested; unexamined for Z⁴).**
  - Site creation (forced at 3H for fixed proper density [ref R12-2, `TESTS:4511`]) breaks the regular Z⁴.
  - A comoving conformal Z⁴ keeps a_t = a_s but gives a V1-type growing physical spacing.
  - No set-B item has tested either.
- **P-N1.** The graviton is supplied. This is shared with every set.

**Axiom lines touched:** `AX:37` (Lattice); `AX:57-61` and the reading notes `:63-73` (Admissibility); `AX:77-83` (Record); `AX:94` ("a law privileges no states", through "the lowest state"); `AX:116-123` (no Hamiltonian or transfer operator supplied); `AX:185-187` (arrow, source/action).

---

## 6. Strong-word check

- **"Proved":**
  - §3.1's split, given the counts;
  - §3.2, which is one line of representation theory;
  - the "no Lorentz condition" statement (the Ward-exact space is 1-dimensional and contains EH).

  All are unrefereed.
- **"Checked":** the four kernel counts, with the control reproducing R19-20's 34/30 and the W(B4) row reproducing K1.
- **"Wall":** used only for R10-2, which is a refereed bounded FAIL in its stated class (proper smooth-box Gaussian covariances and small correlator-continuous perturbations).
- **"The setting contradicts itself":** holds only inside R10-2's class (reading).
- **"(Σ) removes":** in the campaign's law-functional sense only. Under codimension counting it re-books the same 11 + Λ conditions [ref vR19-24].
- **"All orders"** for the charge block: a symmetry statement for dimension-4 speeds, given a W(B4)-covariant whole law including the regulator [ref, `C4_F2_referee.md:33`].
- **Not claimed:**
  - coupled RP for set B + (Σ);
  - any record construction;
  - the size of the non-lowest-state shear mismatch on Z⁴;
  - growth on Z⁴;
  - chiral SM content on Z⁴.

## 7. For the referee

1. **Literal reading.** Is B-STILL-WALLED via R10-2 correct, given that the registered setting includes "box symbols per R10-2" (`TESTS:8517`)? Or should the box component be read as optional, given that (Σ) supersedes its purpose? In that case my box-free reading is OPEN.
2. **The count.** Check §3.1's counts and the "no Lorentz condition on Z⁴" statement (`S/scripts/r1928_count_z4.out`).
3. **§3.2.** Is W₀ ≡ 0 for every W(B4)-invariant vacuum (hence no vacuum enthalpy mismatch) sound, given OS reconstruction?
4. **§3.3.** Does (Σ), via Lemma E, necessarily trigger R2-4's price? Is the reduced-TT plus non-local-constraint payment admissible under R2-4's "nonlocal bridge/constraint" escape?
5. **R2-5.** Is it right to treat it as OPEN, not a wall, for "records via RP" read as OS-reconstructed records?

## 8. Files (`S/`)

- `scripts/r1928_count_z4.py` / `.out`: invariant vacuum-response kernels and Ward-exact spaces for W(B4), B4⁺, O(4) and O_h × T (control). 10 s, `OMP_NUM_THREADS=2`.
- `R19-28_report.md`: this report.
