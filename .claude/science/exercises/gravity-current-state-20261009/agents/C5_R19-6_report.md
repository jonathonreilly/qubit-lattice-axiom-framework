# C5 R19-6 report: one weight-1 source clause for both arenas?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. **Unrefereed.** Run 2026-10-13, 04:19Z to 04:43Z. No repository file was edited. Nothing was downloaded.

**Scratch folder.** `S/` = `.../scratchpad/C5/R19-6/`. Every script ran in under 130 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r196_lib.py`: shared second-order machinery, written from scratch (it imports no earlier C5 runner). It covers the plane-wave phase average, G_μν to O(h²) with the exact second-order inverse, and the contravariant weight-w density (−g)^{w/2}G^{μν}.
- `S/scripts/r196_lemmaL.py` / `.out` [a3174365…]: [L1]–[L3], Lemma L and its two instances (exact rationals, off-shell, random draws).
  - `r196_lemmaL_v0_floatbug.out` is superseded. The first run computed (w/2) with Python int/int, which gave floats and produced false "nonzero" counts at w = 1 and 2. The lib now uses `sp.sympify(w)/2`. It is kept only as a record.
- `S/scripts/r196_setA.py` / `.out` [ff35e887…]: [A0]–[A4]. Set A's mean noise source written in weight-1 form, for all six channel variables, in the Poisson and harmonic gauges, with symbolic a; I₀ at the complete split.
- `S/scripts/r196_vacuum.py` / `.out` [5197c63a…]: [V]. The same functional applied to the on-shell graviton vacuum (TT and Feynman–de Donder), for weights w = 0, 1, 2 and for the lower-index G_μν.
- `S/scripts/r196_kernel.py` / `.out` [3f7d0801…]: [K]. Checks the relative channel normalization behind I₀ (the exchange kernel).
- `S/recheck/`: copies of the archived R18-11, R19-2, R19-3, R18-6 and R18-7 runners, rerun (`S/recheck/run_all.log`, `S/recheck/rerun_summary.txt`). Results are in §9.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `rX` = `P/agents/C5_X_report.md` and `vX` = `P/agents/C5_X_referee_verdict.md`.
- `vR19-3` = `P/agents/C5_R19-3_referee.md` and `vR19-2` = `P/agents/C5_R19-2_referee.md`, the long-form verdicts. I first read them in `scratchpad/C5/ref_R19-{3,2}/`, where they appeared during this run; the archived files have the same line structure. Both are now recorded at `TESTS:7527-7545`: R19-2 NOT CONFIRMED on w → −1, reading OPEN, I₀ confirmed off cone (`TESTS:7527-7534`); R19-3 CONFIRMED WITH CORRECTIONS, J2-GAUGE-BRIDGE (`TESTS:7535-7545`). The short forms are `P/agents/C5_R19-{2,3}_referee_verdict.md`.
- `L:n`, `A:n`, `V:n`, `K:n` = line n of my `.out` files.

**Read.**
- In full: `AX`. The C5 method (`TESTS:2302-2320`). The Round 19 head (`TESTS:7114-7136`) and items R19-2, R19-3 and R19-6 (`TESTS:7186-7253, 7395-7423`). The entries and verdicts for R16-14 (`TESTS:5630-5653, 5998-6006`), R17-11 (`TESTS:6230-6250, 6590-6600`), R18-6 (`TESTS:6684-6711, 6826-6843, 6969`), R18-7 (`TESTS:6713-6736, 6898-6916, 7020-7027`), R18-11 (`TESTS:6918-6942, 7028-7044, 7298-7305`), and R19-2/R19-3 as workers (`TESTS:7350-7381`).
- Also in full: rR18-11, vR18-11 and its long form; rR19-2, rR19-3 and both new verdicts; rR18-6, vR18-6 and its long form; rR18-7, vR18-7 and its long form; S26 §4 (`P/agents/C5_S26_synthesis.md:442-588`).
- Not read: R15-2 in full. Its least-decoherence split enters only through R19-2's powers, whose normalization I recheck in [K].

**Labels.** proved (derived here under stated hypotheses) / checked (an exact result in a `.out` of this run) / suggested (argued, not proved) / reading (interpretation) / comparator (literature RECALLED, or via an earlier referee).

**Order and subtraction.** O(G·noise²) for set A's mean source; one loop for the graviton vacuum; O(G²) static for β. Nothing is subtracted except what a named clause subtracts.

---

## 0. Reading against the FIXED readings (`TESTS:7419-7422`)

**Worker reading: UNIFIED, checked, within the scope stated below.** SPLIT is not met: I found no demonstration, and no candidate, that the two arenas need different weights.

**The clause (W1).** *"The gravitating one-point source is the weight-1 contravariant density 𝔗^{μν} = √−g T^{μν}. Records of stress record 𝔗, and a mean or quantum expectation of the source is taken of 𝔗 itself. Gravity's own stress enters as −[√−g G^{μν}]^{(≥2)}/8πG."* One sentence, no number.

| Job (`TESTS:7404-7407`) | What W1 gives | Label |
|---|---|---|
| Set A's insertion | The record is √−g T^{μν}, i.e. a = 2 (= R18-11's Theorem G selection, `vR18-11:3`) | proved (definition) + checked: the mean is readout-gauge independent iff a = 2 (`A:31-38`) |
| Quantum graviton vacuum source (A′) | The one-point source is −⟨[√−g G^{μν}]^{(2)}⟩/8πG = (A′), with c = 1 per mode in TT and in Feynman–de Donder (`V:2-9`; `vR19-3:7-23`) | proved (definition) + checked |
| N_red's readout | N_red becomes √−g G^{μν} = 8πG[𝔗_m^{μν} − √−g(V − e₀)g^{μν}]. Classically this is identical to N_red. At the quantum and noisy-record level it fixes the object that is averaged, and it replaces N_red's "equivalently, LL form" (`rR18-6:72`), whose quantum vacuum value is (2 + ξ)e_g (`vR19-3:33-39`) | proved (equivalence of the classical equations); the quantum part rests on vR19-3 |

**Why it is one clause and not three (proved, checked).**
- Theorem G (records) and Lemma D (field) are one identity, **Lemma L**, applied to the two conserved objects that enter a one-point source (§3.1; `L:1-26`).
- At a = 2 set A's whole mean noise source *is* the functional A′ evaluated on the record-noise metric (**Proposition U**, `A:9-21`). So both arenas gravitate through the same functional, applied to two different two-point functions: classical record noise, and the quantum vacuum.
- Theorem I₀ is A′[h_n] = 0 on every spacelike off-cone mode at the complete split, in both gauges (`A:40-44`).

**Fork check (Exhaustive forks rule, `TESTS:7123`).**
- UNIFIED: yes (worker, checked).
- SPLIT: no. Every refereed result listed in the item is consistent with W1 (§4.6). In C-box-E, W1 is *admissible* rather than *forced* wherever the readout gauge is fixed by the lattice frame (§4.6, reading). That is not a demonstration that a different weight is needed.
- OPEN would apply if a referee rejects Proposition U or Lemma L, or reads "consistent with R18-7's harmonic construction" as requiring R18-7's stipulated a = 4 (§4.6(c)).

**Scope of UNIFIED.**
- Means only: the coarse-grained O(G·noise²) mean, and one-loop one-point functions. Fluctuations are not covered.
- Weight uniqueness only within the contravariant power-density families (`vR18-11:3`; `vR19-3:9-23`).
- Linear covariant gauges plus TT and Coulomb for the graviton (`vR19-3:9-23`).
- A′ is the Einstein–Hilbert part. The full gauge-fixed effective-action source equals it only after the gauge-fixing and ghost stresses cancel, which is checked at β = ½, ξ = 1 only (`vR19-3:25-31`).
- The noise's *size* is not fixed by W1. It still needs P-r192a/b/c and P146 (§4.3).

---

## 1. In plain words

- **The question.** Three separate calculations each found that gravity behaves well only if its source is written with one extra factor of the volume element √−g (a "weight-1 density"):
  - the record noise of set A (R18-11);
  - the graviton's own zero-point jitter on the grid (R19-3);
  - the cancellation of the record noise for slowly varying modes (R19-2).

  Are these one rule or three?
- **One rule.** A mean is an integral over spacetime. Such an integral gives the same answer in every coordinate system only if the thing integrated carries its own volume factor, i.e. is a weight-1 density. The gravitating mean source is exactly such an average. So it must be built from weight-1 densities, and that single fact does all three jobs.
- **What it fixes.**
  - Set A's record is read as √−g T.
  - The graviton jitter's weight is counted once in every gauge tested, and the two existing rules (S) and (d-i) then remove it with no number.
  - The metric readout N_red keeps its classical content exactly. Only its quantum and noisy versions change.
- **What it does not fix.** How large set A's record noise is, and its sign. That depends on how the records are split between channels and on how the bookkeeping term behaves in an expanding universe. Those remain separate choices.
- **Cost.** One sentence, no numbers. It merges two earlier prices into one, and in set A it removes the free number a.

---

## 2. Prior art (each counted once)

1. **R18-11 and vR18-11.** Theorem G: within C_w, readout-gauge independence of the coarse-grained mean selects w = 1 (a = 2) (`vR18-11:3`; `rR18-11:134-148`). Lemma P: zero-start homogeneous energy is pinned; homogeneous pressure is a completion datum (`vR18-11:5`).
2. **R19-3 and vR19-3** (CONFIRMED WITH CORRECTIONS, J2-GAUGE-BRIDGE).
   - Lemma D holds within the contravariant Einstein-density family (`vR19-3:9-23`).
   - c = (B 4, A 2, A′ 1) in harmonic gauge (`vR19-3:7`).
   - A′ is the Einstein–Hilbert part; the full source is EH + gauge fixing + ghosts = 1 + 4 − 4 (`vR19-3:25-31`).
   - Literal N's vacuum is (2 + ξ)e_g (`vR19-3:33-39`).
   - With P-r193a, H-V3, P136(ii) and (d-i), there is no number (`vR19-3:43`).
3. **R19-2 and vR19-2** (NOT CONFIRMED overall; reading OPEN).
   - Theorem I₀ is confirmed **only off cone, under the newly priced complete split P-r192b** (`vR19-2:5`).
   - Under the registered comoving stationarity, FRW lift A gives dust, not Λ (`vR19-2:12-16`).
4. **R18-6 and vR18-6.** The modified net-source bridge (S) + (d-i) + N_red: three clauses, zero numbers, exact classical GR in class 𝒟 (`vR18-6:3,13`). Literal N with W ≠ 0 is JOINT-CONFLICT (`vR18-6:5`). J2 is open (`vR18-6:7`). In set A, the matter vacuum has W = 0 and (d-i) has no receiver (`vR18-6:9`).
5. **R18-7 and vR18-7.** E1 + N_c with Π is CONSTRUCTED in weak-field harmonic static/quasi-static scope (`vR18-7:26`). Π is causal, conserving and nonlocal (`vR18-7:3`); CP holds by the Kraus form U_rA_r (`vR18-7:11`); β = γ = 1 after mass renormalization (`vR18-7:18`). The static zero at the *stipulated* a = 4 is scoped to the homogeneous scalar channel (`vR18-7:20`).
6. **R17-11 and vR17-11.** (d-i) as Q_ν = ∇^μ(W h_μν) in class 𝒟 (`TESTS:6590-6600`).
7. **R16-14 and vR16-14.** Linear completions are excluded by Mercury; N is the uncompleted nonlinear bridge (`TESTS:6000-6006`).
8. **R15-2.** The channel set and the least-decoherence trade-off, used only through R19-2's powers (`S/recheck/R19-2/r192_split.py:5-9`).
9. **Comparators (RECALLED).** Lie derivatives of tensor densities. The covariant divergence ∇_μT^{μν} = (−g)^{−1/2}∂_μ(√−g T^{μν}) + Γ^ν_{μλ}T^{μλ}. The Hilbert stress 2δS/δg_μν, which is a weight-1 density. On-shell gauge independence of the one-loop effective action (DeWitt; Kallosh–Tarasov–Tyutin).
10. **Repository grep.** I grepped `P/agents/` for "weight-1", "Lie-derivative", "same clause" and "density weight". The only hits are the suggestion at `rR19-3:269` ("P-r193a and P-r1811a are the same clause", suggested, not checked) and S26's ledger rows P145/P-r193a. There is no prior derivation that the two mechanisms are one identity. `docs/` was not grepped.

## 3. Hypotheses and the clause (probe (a))

**Hypotheses (stated before titles).**
- H1. Set A is as in R18-11/R19-2: E1 + N_c, R15-2's six channel variables, flat-conserved record J, Π, P76 and P88. The insertion family is C_w, with a = 4 − 2w.
- H2. C-box-E is as in R18-6: class 𝒟, H-imp, sites on normals, and (S), (d-i) and N_red as written at `rR18-6:68-73`. The graviton is R9-9's box graviton with H-V3, as in R19-3.
- H3. Gaussian noise or quasi-free vacua; means are phase or ensemble averages.
- Excluded: E2 (that is R19-8), strong field, interactions beyond one loop, non-Gaussian meters, and fluctuation-level statements.

**The clause as an equation in each arena (proved: each is an exact rewriting, or a definition).**
- **C-box-E (classical + quantum):**
  - 𝔊^{μν}[g] := √−g G^{μν} = κ[𝔗_m^{μν} − √−g(V − e₀)g^{μν}], with λ = −κe₀[H] (S) and Q_ν = ∇^μ(W h_μν) (d-i).
  - For a quantum metric sector, the one-point source of the long-wave metric is −⟨𝔊^{(2)}⟩/κ = A′ (the weight-1 object of R19-3).
- **Set A:** √−g G^{μν}[g] = κ(J^{μν} + K^{μν}), with J the record (now read as 𝔗) and K Π's completion. For a general insertion a this reads √−g G = κ[(−g)^{(a−2)/4}J + K]. W1 sets the exponent to zero.

### 3.1 Lemma L: Theorem G and Lemma D are one identity (proved; checked)

- **Statement.** Let 𝔜^{μν} be a symmetric contravariant density of weight w that is flat-conserved at linear order (∂_μ𝔜^{μν} = 0). Let ξ be a vector field linear in the same fluctuation. Then the zero-momentum (averaged) part of the Lie derivative is

  ⟨(L_ξ𝔜)^{μν}⟩ = (w − 1)⟨(∂·ξ)𝔜^{μν}⟩.

- **Proof.** Write L_ξ𝔜 = ξ·∂𝔜 − 𝔜^{λν}∂_λξ^μ − 𝔜^{μλ}∂_λξ^ν + w(∂·ξ)𝔜.
  - The first term averages to −⟨(∂·ξ)𝔜⟩ by parts.
  - The second and third average to ⟨ξ^μ∂_λ𝔜^{λν}⟩ + ⟨ξ^ν∂_λ𝔜^{μλ}⟩ = 0 by conservation. ∎
- **Plain form.** At zero momentum the spacetime integral of a conserved weight-1 tensor density is coordinate-invariant to first order; for any other weight it is not.
- **Checked.** For a generic conserved mode (the record mode with all six channel variables), the identity holds in 16/16 components, and ⟨(∂·ξ)𝔜⟩ ≠ 0 in 16/16, over 4 off-shell draws with symbolic w (`L:1-7`).
- **Instance (i), records: Theorem G.** 𝔜 = the record J (flat-conserved by R15-2's construction). The two readout gauges' laws differ by L_ξJ (`rR18-11:137`), whose mean vanishes iff w = 1.
- **Instance (ii), field: Lemma D.** 𝔜 = G^{(1)μν}[X] for arbitrary X, which is conserved identically by linearized Bianchi.
  - Checked: the forward cross term 2Y_w^{(2)}(L_ξη, X) equals ⟨L_ξ G^{(1)}[X]⟩ and equals (w − 1)⟨(∂·ξ)G^{(1)}[X]⟩ for w = 0, 1, 2 in 2 off-shell draws. It is nonzero in 16/16 components for w = 0, 2 and for the lower-index G_μν, and in 0/16 for w = 1 (`L:9-23`).
  - This independently reproduces `rR19-3:220-229` and `vR19-3:9-23`.
- **Scope.** Contravariant power-density families. One Fourier pair (zero total momentum after averaging). Linear order in ξ.

### 3.2 Proposition U: at a = 2 set A gravitates through A′ (proved; checked)

- **Statement.** Write the set-A law in weight-1 form, √−g G^{μν} = κ[(−g)^{(a−2)/4}J + K]. Its O(G·noise²) mean source per frame mode is

  τ_a = ((a − 2)/4)⟨tr(ηh)J⟩ + A′[h_n],   A′[h] := −⟨[√−g G^{μν}]^{(2)}[h,h]⟩/8πG,

  plus Π's homogeneous mode (Lemma P/F0). At a = 2 the record term vanishes identically.
- **Proof.** Expand both sides to second order. The first-order equation G^{(1)}[h_n] = κJ holds pointwise, so no other cross terms survive.
- **Checked.**
  - Poisson and harmonic solutions both satisfy G^{(1)} = 8πJ (`A:2-4`).
  - The weight-1 form reproduces R19-2's lower-index table in 14/14 entries, so the source does not depend on how the field equation is written (`A:10`).
  - A′[h_n] is identical in Poisson and harmonic gauge for every monomial (`A:31-37`): that is Lemma D on the classical noise metric.
  - Every gauge difference sits in the record term and carries the factor (a − 2) (`A:32-36`). For example, ρ² gives 2x²(a − 2) and 2x⁴(a − 2), which is R18-11's Δ (`P/agents/C5_R18-11_referee.md:32-35`).
- **Consequence.**
  - At a = 2 set A's readout-gauge independence *is* Lemma D. Off a = 2, the gauge dependence *is* Lemma L instance (i).
  - The record noise of set A and the graviton vacuum of C-box-E gravitate through the **same functional A′**. Only the two-point function differs: classical record noise versus the quantum vacuum.
- **Channel table at a = 2** (A′ per monomial, units π/k², `A:14-21`):

  | monomial | τ₀₀ | τ_kk |
  |---|---|---|
  | ρ² | x² − 3 | −(1 + x²) |
  | ρT_⊥ | −2 | 2 |
  | T_⊥² | 0 | 0 |
  | j² (each) | 4 | −4 |
  | t² (each) | 4(1 + x²)/(1 − x²)² | 4(3 − x²)/(1 − x²)² |

  The ρ² row matches `vR18-11:7-10`; the TT row matches `vR19-2:5`.

---

## 4. Probe (b): consistency checks in each arena

### 4.1 Gauge independence
- **Set A.** At a = 2 the mean is independent of the readout gauge, for all six channel variables, Poisson versus harmonic (checked, `A:31-38`). In the C_w family this holds only at a = 2 (Theorem G, refereed).
- **Graviton vacuum.** On shell, per mode, the contravariant family gives c = w in Feynman–de Donder (w = 0 → 0, 1 → 1, 2 → 2) and c = 1 in TT for every weight. The lower-index G_μν gives 4 (checked, `V:2-9`).
  - This matches vR19-3's (B) = 4 and (A) = 2, the latter because ⟨(−g)t_LL⟩ = −⟨[(−g)G]^{(2)}⟩/8πG up to an averaged total derivative (`rR19-3:171-174`).
  - New datum: the weight-0 contravariant form undercounts, with c = 0. Weight 1 is the only member of the family that gives the TT value in both vacua.
  - The β-gauge scan is vR19-3's (`vR19-3:23`). It was not redone here.

### 4.2 Bianchi consistency (proved)
- **The identity.** For any weight: ∂_μ[(−g)^{w/2}T^{μν}] = (−g)^{w/2}[∇_μT^{μν} − Γ^ν_{μλ}T^{μλ} + (w − 1)∂_μ ln√−g T^{μν}] (textbook; comparator).
  - At w = 1, covariant conservation is ∂_μ𝔗^{μν} = −Γ^ν_{μλ}𝔗^{μλ}: the pure gravitational force, with no volume-change term. The (w − 1) factor is Lemma L's.
  - So the defect that Π must complete for a flat-conserved record is −Γ^ν_{μλ}[h]J^{μλ}.
- **Its mean.** For a stationary mode in either gauge, h_n ∝ J ∝ cos θ, so ⟨Γ[h_n]J_n⟩ ∝ ⟨sin θ cos θ⟩ = 0 (proved, one line). Π's mean is then only the homogeneous switch-on part (Lemma P, refereed), at any w.
  - So Bianchi consistency holds at every weight for the mean. What selects w = 1 is gauge blindness, not Bianchi.
- **C-box-E.** The classical equations are unchanged, so Bianchi is exact as in `vR18-6:3`.
  - The quantum one-loop A′ vacuum stress is forward-conserved per mode (k̃^μt_μν = 0, `rR19-3:181-182`).
  - After cubic-invariant summation it is ρnn + ph, whose enthalpy (d-i) receives (`vR19-3:43`).

### 4.3 Predictions
- **Matter (β, γ).**
  - *C-box-E:* β = γ = 1. W1 does not alter the classical equations (proved), so `vR18-6:13` stands.
  - *Set A at a = 2:* γ = 1 at O(G), independent of a (`TESTS:6000-6006`). β = 1 (proved, structure):
    - Relative to R18-7's a = 4 source, a = 2 changes the O(G²) source by −½tr(ηh₁)J = −2Uρ_F (static, harmonic, (−g) = 1 + 4U, `vR18-7:20`).
    - That change is supported on the filtered body, so its exterior effect is an O(G²)/r monopole (mass renormalization) plus Gaussian tails.
    - Π's response to a compact static defect changes only the O(G²)/r mass term, not the M²/r² coefficient (`vR18-7:18`).
    - Not checked numerically.
- **Noise (R19-2).**
  - W1 fixes a = 2, so the gravitating mean is A′[h_n] (Proposition U).
  - At the complete split P-r192b, A′[h_n] = (0, 0) on every spacelike off-cone mode and (4, −4)u₀ on timelike modes, in **both** gauges (checked, `A:40-44`). So (U) gives ρ_act = 0 off cone. The x = 1 band is not covered (`vR19-2:5`).
  - Normalization check: the zero depends on the relative channel normalization of R19-2's powers. Their exchange kernel is reproduced from my own Poisson solution in one convention (checked, `K:1-9`).
  - What W1 does **not** predict: the size and sign of the near-cone and timelike remainder (P-r192c), the FRW fate (P-r192a; under comoving stationarity it is dust-like, `vR19-2:12-16`), and the energy history (P146).
- **Graviton vacuum (R19-3).**
  - c = 1 per mode in TT, Coulomb and the registered linear covariant gauges (`vR19-3:7-23`; my FdD check, `V:5`).
  - Then e_g = 2.447/a⁴ is removed by (S) and W_g = 4e_g/3 by (d-i), with no number. This is conditional on P136(ii) and H-V3 (`vR19-3:43`).

### 4.4 The quantum readout of N_red (proved on refereed inputs)
- N_red as written (`rR18-6:70-73`) adds "equivalently, in Landau–Lifshitz form, τ = (−g)(T^eff + t_LL) + t_H". At the quantum one-point level that form gives (2 + ξ)e_g (`vR19-3:33-39`). After (S), it leaves (1 + ξ)e_g.
- W1 replaces it by the weight-1 readout. So W1 is not redundant with N_red: classically it is inert, and at the quantum level it is necessary within the registered gauge class.

### 4.5 Set A, P88 and P139
- **P88 (zero TT free data).** Untouched. W1 is a statement about sources, not free data.
- **P139 (readout gauge).**
  - Immaterial for the *mean* at a = 2 (checked, `A:31-38`, consistent with `rR18-11:233`).
  - Not shown immaterial for fluctuations. The two gauges' laws differ by the source κL_ξJ, which has zero mean but nonzero variance. So P139 remains law data at the fluctuation level (suggested).

### 4.6 Conflict check against the refereed results named in the item (`TESTS:7408`)
(a) **(d-i)** (`vR17-11`; `vR18-6:3`).
- No conflict (proved). W1 does not touch W, Q or the receiver.
- Its quantum use requires the graviton's A′ vacuum to be of the absorbable form ρnn + ph. It is, by cubic invariance and the null per-mode tensors (`vR19-3:43`).

(b) **P88.** No conflict (§4.5).
- *Reading:* for a quantum graviton in C-box-E, P88's "h_TT = 0" can only mean "the TT sector starts in its ground state". That is a P88/J2 interpretation point which W1 does not create.

(c) **R18-7's harmonic construction** (`vR18-7:26`). Literal-first statement: R18-7 stipulated a = 4 (P140). W1 replaces that stipulated value with a = 2. So the literal R18-7 *law* and W1 are alternatives for P140, not a conflict of results. Every refereed *property* of the construction survives at a = 2:
- Π is causal and conserving for any source S (`vR18-7:3`).
- h₁ is E1, since a enters only at O(G²).
- CP (proved, structural): at a = 2 the measured operator is √−g[h_past]T, a record-controlled instrument. Its Kraus operators U_rA_r(r_<) stay CP for any classical record dependence. This extends `vR18-7:11`; R18-11 cites the same argument (`rR18-11:221`).
- β = γ = 1 (§4.3).
- What does not survive is the static ρ-channel zero, which vR18-7 scopes to the stipulated a = 4 (`vR18-7:20`). At a = 2 that channel alone gives −4u₁ under (U) (`vR18-11:7-10`). But all four channels at P-r192b give 0 off cone (`vR19-2:5`; `A:41`).
- If a referee reads "consistent with R18-7's harmonic construction" as "consistent with a = 4", then UNIFIED fails on that letter, and the reading would be OPEN rather than SPLIT, since nothing forces a = 4. Theorem G already shows that a = 4 depends on the gauge (`vR18-11:3`).

(d) **R18-6 bridge** (`vR18-6:13`). No conflict (proved). The classical equations are identical in weight-1 form. W1 supplies the J2 step that vR18-6 left open (`vR18-6:7`), via `vR19-3:41-47`. Literal N stays excluded (W18), now for two reasons: the classical Q = 0 conflict (`vR18-6:5`) and the quantum overcount (`vR19-3:33-39`).

(e) **Also checked: R18-11** (`vR18-11:3,5`). W1 *is* Theorem G's selection, and Lemma P is untouched. **R16-14** (`TESTS:6000-6006`): γ, α₁ and α₂ at O(G) are a-independent.

(f) **C-box-E, readout gauge (reading).** In C-box-E the lattice frame (sites on normals, H-imp) may fix the readout coordinates. If so, the record weight is not *forced* there by gauge independence; W1 is admissible and fixes it. With TT/Coulomb quantization in the lattice frame, every weight gives c = 1 (`V:2-8`), so there W1 is again admissible rather than forced. This is not a SPLIT: no result requires a different weight in either arena.

---

## 5. Probe (c): sentence count

| Arena | Bridge sentences | Numbers | Carried sector stipulations (not bridge sentences) |
|---|---|---|---|
| **C-box-E, classical + quantum** | **4:** (S) [P92], (d-i) [P70(d-i)/P-vac′], N_red [P135], W1 [P145 ≡ P-r193a] | **0** | P136(i) on P-N1 (GR's self-coupled graviton; W7 degree 3); P136(ii) (gravity inside H, which R18-6 writes into (S)'s definition of H, `rR18-6:68`); P-r193b/H-V3 (lattice forward vertex); arena P52/P53, P128, P93 |
| C-box-E, classical only | 3 ((S), (d-i), N_red). W1 is inert classically (proved) | 0 | as R18-6 |
| **Set A** | (S), N_c [P107 + P138 Π], W1. **W1 replaces P140, which was one number, and makes P139 immaterial for the mean** | **0** | P76, P88 (free data); the noise budget: P146, P-r192a, P-r192b, P-r192c; P-r15c if used |

- **Independence (reading on refereed inputs).**
  - Dropping W1 brings back the gauge-dependent graviton remainder (c − 1)e_g, of order 1e123 ρ_Λ (`vR19-3:41`), and the free, gauge-dependent a in set A (`vR18-11:3`).
  - Dropping (S), (d-i) or N_red reproduces `rR18-6:164-167`.
- **Merging.** W1 cannot be absorbed into N_red as a rewording. Classically N_red does not imply W1, and W1 alone says nothing about what gravitates (vacuum subtraction, gravity's own stress).
- **Result.** Four clauses, zero numbers, as expected. The P136(ii) scope clause and H-V3 are counted separately as sector stipulations.

## 6. Probe (d): prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r196a = W1** | "The gravitating one-point source is the weight-1 density √−g T^{μν}; records record it; means are taken of it." It **merges P145 (P-r1811a) and P-r193a into one price**, counted once. In set A it replaces P140 (a number) and makes P139 immaterial for the mean. | `AX:187` (source/action, physical-observable identification); `AX:82-83` (readout by record content: √−g[h] is a functional of records) | proved consistent in the stated scope; checked; unforced by the axiom texts |
| Not fixed by W1 | P146 (energy history); P-r192a (FRW lift); P-r192b (complete split); P-r192c (near-cone split); P88; P76; P136(ii); P-r193b (H-V3); P139 at fluctuation level | as recorded | carried |

- No new price.
- Net effect on the ledger: two rows (P145, P-r193a) become one, and P140 leaves the set-A bill.
- **Forced versus number-free.** W1 is number-free and *selected* by gauge blindness inside the stated families. It is not derived from the four axiom texts (`AX:85-90, 187`).

## 7. Corrections and refinements to earlier records (worker)

- **rR19-3:269 ("possibly the same clause", suggested).** Now proved and checked: P-r193a and P-r1811a are the same identity (Lemma L), and at a = 2 set A's source is the same functional A′ (Proposition U).
- **R19-2's Theorem I₀ "structural reason not identified" (`rR19-2:198`).** Partly identified. I₀ is A′[h_n] = 0, so the zero lives entirely in the field functional, the record term being absent at a = 2. Why A′ vanishes on spacelike modes at the complete split is still not explained beyond the channel sum (suggested: the floor makes the metric-noise covariance ∝ |G|).
- **N_red's "equivalently, LL form" (`rR18-6:72`).** Holds classically only. At the quantum one-point level it must be read through W1 (`vR19-3:33-39`).
- **New datum.** In Feynman–de Donder, the contravariant weight-0 form gives c = 0 (`V:3`), so c = w across the contravariant family. Undercounting (w = 0) and overcounting (w = 2, LL) bracket the weight-1 value.

## 8. Strong words checked

- **"One clause."** One sentence covering three uses. Its content is the same identity, Lemma L, proved and checked. It is not one equation in the sense of a single derivation from the axioms.
- **"Same functional."** A′ evaluated on two different two-point functions (`A:14-21`; `V:5`). Checked per mode, at one loop and at O(G·noise²).
- **"Gauge independent."**
  - Set A: the mean only, Poisson versus harmonic (checked), and every readout pair for the C_w family (Theorem G).
  - Graviton: the registered linear gauges only (vR19-3), plus my FdD and TT check.
- **"Consistent with every refereed result."** The results named at `TESTS:7408`, plus R18-11 and R16-14. For R18-7 this is property-wise, at the replaced value a = 2 (§4.6(c)). vR19-2 and vR19-3 are now recorded (`TESTS:7527-7545`). From vR19-2 I use only item 1 (I₀, off cone, under P-r192b) and its comoving-stationarity correction. From vR19-3 I use items 1–6 with their scope corrections.
- **"Zero numbers."** No fitted or tuned constant enters W1. Uniqueness of w = 1 is inside the stated families only.
- **"Checked."** Exact rational and symbolic identities in my `.out` files. β at a = 2 is proved by structure, not checked numerically.

## 9. Recheck of archived runners (`S/recheck/rerun_summary.txt`)

- R18-11 (4), R19-2 (4), R19-3 (8), R18-6 (2) and R18-7 (3) were copied and rerun.
  - Byte-identical: r1811_budget, r1811_pin, r192_budget, r192_frw, r192_split, r193_C_zeropoint, r193_LLcheck, r193_lattice, r186_cbox_bridge, r187_checks, r187_lapse.
  - Differing in timing lines only: r1811_insertions, r1811_modes, r192_modes, r193_beta_family, r193_gauge_family (both confirmed by a timing-stripped diff), r193_lemmaD, r193_onepoint, r193_relaxed, r187_ll.
- **r186_vacuum_parts, line 12.** Stored `[[T00,…],[0,−T00,…]]`, rerun `[[−T33,…],[0,T33,…]]`. This is the same invariant family T^{μν} = cη^{μν}: a sympy free-variable choice. Benign.
- **Archive defect.** `scripts/C5/R19-3/r193_lattice.py:14` imports `../recheck/R9-9`, which is not archived (also noted at `vR19-3:43`). The rerun used a copy of `scripts/C5/R9-9` at that relative path and is IDENTICAL. Suggested fix: point it at `../R9-9`.

## 10. Against the expectation (`TESTS:7423`)

- **"UNIFIED. All three are the same statement: Lie-derivative covariance of the one-point source."** Confirmed. The statement is Lemma L. Two refinements:
  - Theorem I₀ is not itself a gauge statement. It is A′ evaluated at a specific split (P-r192b). W1 is necessary for it (the zero is at a = 2 only, `A:41-44`) but not sufficient.
  - In C-box-E, W1 is admissible rather than forced wherever the lattice fixes the frame.
- **"Four clauses and zero numbers."** Confirmed, with P136(ii) and H-V3 carried as sector stipulations (§5).

## 11. Notes for a referee

1. Lemma L's proof (§3.1) and `L:1-23`. Is "flat-conserved at linear order, one Fourier pair" the right hypothesis for both instances?
2. Proposition U: the pointwise first-order equation is what makes the source independent of how the field equation is written (`A:10`). The gauge-independence split is at `A:31-38`.
3. §4.6(c): whether replacing R18-7's stipulated a = 4 counts as "consistent with R18-7's harmonic construction".
4. The CP extension to a record-controlled measured operator (§4.6(c)).
5. β at a = 2 is argued by structure plus `vR18-7:18`, not computed.
