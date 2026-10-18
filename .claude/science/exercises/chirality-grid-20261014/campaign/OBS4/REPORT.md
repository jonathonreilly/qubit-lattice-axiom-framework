# OBS-4 report: tree-level FCNC from the corner carriers in X2's texture escape

> **Referee (codex gpt-5.6-sol, 14:33Z): CONFIRMED WITH CORRECTIONS. FCNC-PRICE is correct.**
> - **Confirmed:** S1; the mass-basis couplings; M* (7.7e3 / 3.8e3 TeV); class S losing X2-L2.
> - **Not established:**
>   - the 1.1 TeV ceiling as a general bound (single-source estimate; heuristic search; 8π point unbounded below);
>   - D6 coverage;
>   - a universal KILL for X2 as written: shown only for the tested D3 spectra.
>
> See `REFEREE_VERDICT.md` and `referee/REFEREE.md`.

**Reading: FCNC-PRICE.**

**For X2 as written, the outcome is at KILL level.** The electroweak-doublet carriers are forced light. They fail ΔF = 2 by at least ×180 at every carrier mass the potential allows.

**Why PRICE and not KILL.** One passing realisation exists once a named structure is added: an electroweak-neutral condensate at the hw2 momenta that breaks unit translations spontaneously above the electroweak scale (the singlet-flavon route, class S). That structure contradicts the exact-translation premise of X2-L1/L2.

**Provenance.**
- **Worker:** Claude Opus 5.5 at xhigh. Same family as the supervisor, X2 and OBS-1–3, so not independent. Unrefereed.
- **Window and resources:** 13:27–14:15Z on 2026-10-15. Peak memory 83 MB, one process at a time.
- **PREREG timing:** written before any run (file time 13:45:26Z; first output 13:48:36Z). Its header says 13:46Z, typed about one minute ahead of the clock; this is recorded in the follow-up file.
- **Independence:** SUPERVISOR_OWN_THREAD.md was read only after all results were in.
- **This file:** the harness blocks subagents from writing REPORT.md, so the supervisor saved this from the worker's final message, lightly condensed. Every number and file reference is the worker's.

## Plain words

1. **Off-diagonal masses need extra Higgs doublets.** With exact grid translations, mixing two generations (corners) needs a Higgs-like field that carries the difference momentum, an hw2 momentum such as (π,π,0). So OBS-3's escape needs three extra Higgs doublets besides the ordinary one, each carrying one pair of off-diagonal entries.
2. **These doublets change quark flavour at tree level.** Rotated to quark mass eigenstates, they have large flavour-changing couplings: up to about 0.66 for u–c and about 0.015 for s–d. Even the ordinary momentum-0 Higgs part is flavour-changing, because B-gen's near-democratic textures leave the light up and charm directions badly misaligned between left and right.
3. **How heavy they would have to be.** Without tuning, passing K and D mixing needs these scalars above about 1,300–8,000 TeV, depending on the realisation, the coupling scale and the carrier class. D mixing and ε_K bind.
4. **How heavy the construction can make them.** Exact translations forbid the term that would let a heavy doublet pick up a small vev from the ordinary Higgs. So the usual "heavy second doublet" decoupling limit does not exist here, and the carriers come out at about 1 TeV or less (checked numerically).
   - That is a shortfall of about 10⁶ in amplitude.
   - Even tuning the vev ratios for cancellation, the best found still needs 15 TeV: a shortfall of ×180.
5. **The way out costs the light-generation protection.**
   - Make the momentum-carrying field an electroweak singlet that condenses near the lattice scale. Then only one Higgs doublet exists at low energy, and tree-level FCNC vanishes.
   - The cost is spontaneous breaking of unit translations at the lattice scale. That removes the exact-translation premise on which X2's light–mirror protection rests (X2-L1, X2-L2).
   - It also allows O(1/a) light–mirror (hw1–hw3) hopping, whose effect is not computed.

## Reading (FIXED, TESTS.md:441-453; PREREG rule 10)

- **Not FCNC-SAFE.** Inside X2 as written, no realisation passes at the masses the construction supplies. Class S passes, but only with structure X2 as written does not supply. PREREG rule 10, written before any run, counts that as named structure.
- **Not FCNC-KILL.** Class S, built with the same exact B-gen matrices, passes every ΔF = 2 row.
- **FCNC-PRICE.** Any one of three forms:
  - **(P1) Structure.** An electroweak-neutral condensate at the three hw2 momenta, with f ≳ 0.03/a (the up-sector entry needs g·f·a ≈ 0.33 with g ≤ 4π).
    - Below f, the surviving translations form a BCC lattice, and hw1 and hw3 share a label.
    - Cost: new per-site scalar content, and loss of X2-L1/L2's exact-translation premise.
  - **(P2) Tuning.** Use the same condensate only as a tadpole source, with the doublet carriers at M ≥ M* far below 1/a. That needs a hierarchy tuning of about (M*·a)² per carrier mass: about 1e-25 for 1/a = M_Pl, and 1e-20 for 1/a = 2e16 GeV.
  - **(P3) Cancellation (existence not shown).** Keep the carriers at 1 TeV or below. Then the non-degenerate heavy spectrum must be tuned so that the K and D amplitudes cancel to about 1e-6 of their natural size, and the 125 GeV h must be aligned to |sin ε| ≲ 5e-5.
- **Alignment is not available** (proved, §1).

## 1. The carrier sector

**S1 (proved): the selection rule.**
- Under a unit translation, a fermion at corner c picks up a phase e^{iQ_c·a}, and a scalar mode at momentum K picks up e^{iK·a}.
- So a Yukawa entry (c, c′) is allowed only with K = Q_c + Q_c′ (mod 2π).
  - Diagonal entries need K = 0, i.e. the ordinary Higgs H₀.
  - The entry pair {(y,z), (z,y)} needs K_x = (0,π,π), and similarly for K_y and K_z.
- The carriers therefore have disjoint supports in the corner basis. This agrees with X2-L3 (COMBO_REPORT:103): the same carrier also couples hw1 to the hw3 mirror.

**Field content.**
- **Carriers:** SU(2) doublets with Y = 1/2, singlets of colour and Spin(10). Their spin structure is τ_xσ_c, a Lorentz scalar at leading order (OBS-2's side finding).
- **D3 (primary, type III):** one doublet per K, coupling to both the up and the down pairs. That is four doublets, giving 13 physical scalars: h, plus three each of H⁰, A⁰ and H±.
- **D6:** separate up and down carriers. That is seven doublets: h, plus six each of H⁰, A⁰ and H±.
- **OBS-3's mechanism 2** (a Higgs degenerate at the corner-difference momenta) is D3.
  - It arises naturally from a scalar that hops only along body diagonals, with ε(q) = 1 − cos q_x cos q_y cos q_z.
  - This ε vanishes exactly at {0} ∪ hw2 and is isotropic, about q²/2, near each of these points (proved, one line).
  - The result is four light doublets for one mass tuning, at range √3.
- **The off-diagonal condensate is spontaneous.** A vev at K ≠ 0 breaks unit translations. The law is translation-covariant (AX:57), so OBS-1's frozen (π,π,0) mass term must be read as the vev of a K-carrying field.

**Couplings in the mass basis.** Ŷ^K = W†·P_K(M)·X / v_K. B-gen is rebuilt exactly from p, with the quark fields rephased to the PDG CKM convention (residual 1.5e-13).
- **Check:** the light direction Σ_K v_K Ŷ^K / v equals M/v and is exactly diagonal: off-diagonal ≤ 3e-16 (`table.out`).
- Each carrier separately, for B-gen (conjugated), with v_K = v/2 (`table.out:3-7`):

| Carrier | Aligned u, c, t | \|uc\|, \|cu\| | \|sd\|, \|ds\| | \|bd\|, \|db\| | \|bs\|, \|sb\| |
|---|---|---|---|---|---|
| H₀ (k = 0) | 0.067, 0.067, 0.660 | 0.657, 0.657 | 1.5e-2, 1.5e-2 | 1.9e-4, 1.4e-4 | 1.2e-4, 1.8e-4 |
| K_x | 0.448, 0.421, 0.441 | 0.158, 0.287 | 5.1e-3, 7.1e-3 | 5.9e-3, 5.4e-3 | 4.7e-3, 5.3e-3 |
| K_y | 0.148, 0.175, 0.441 | 0.629, 0.192 | 4.1e-3, 1.4e-2 | 7.0e-3, 2.5e-3 | 2.8e-3, 7.2e-3 |
| K_z | 0.261, 0.288, 0.441 | 0.128, 0.564 | 1.5e-2, 5.0e-3 | 1.9e-3, 7.3e-3 | 7.3e-3, 2.1e-3 |

B-gen120 is similar (`table.out:9-13`).

**No-alignment lemma (proved).**
- **Pich–Tuzón alignment** (Y^K ∝ M for every K) is impossible: the supports are disjoint, and M has full support.
- **Weaker alignment** (every heavy combination diagonal in the mass basis) would require all Y^K to be bi-diagonalised by the same (W, X).
  - With an invertible diagonal part D, the matrices A_K = O_K·D⁻¹ would have to be normal and commute.
  - But (A_x A_y)₁₀ = a₁₂b₂₀ ≠ 0, while (A_y A_x)₁₀ = 0.
  - So at most one off-diagonal carrier per sector is possible. That gives a CKM matrix with an exact zero, which is excluded since |V_ub| ≠ 0.
- **Natural flavour conservation** (one doublet per charge sector) gives monomial supports, so |V_CKM| would be a permutation matrix (proved). This is the Z₂³ analogue of main's `NEUTRINO_DIRAC_Z3_SUPPORT_TRICHOTOMY_NOTE.md` and `LEPTON_SINGLE_HIGGS_PMNS_TRIVIALITY_NOTE.md`.

## 2. ΔF = 2 at tree level

**The effective Hamiltonian (S2, proved).**
- Decoupling form, with H and A degenerate at M. The aligned light direction drops out by unitarity of the Higgs-basis rotation, leaving C4^{ij} = −Σ_K Ŷ^K_ij Ŷ^{K*}_ji / M², for the operator Q4 = (q̄_R^i q_L^j)(q̄_L^i q_R^j).
- If H and A are split, C2-type operators also appear.

**Primary bounds.** Isidori–Nir–Perez, arXiv:1002.0900, Table 1, LR rows (fetched). Λ in TeV:

| Row | Re | Im |
|---|---|---|
| K | 1.8e4 | 3.2e5 |
| D | 6.2e3 | 1.5e4 |
| B_d | 1.9e3 | 3.6e3 |
| B_s (modulus) | 3.7e2 | — |

These rest on UTfit, arXiv:0707.0636 (fetched): NLO RI-MOM running from Λ, with that paper's Table 2 bag parameters.

**M\* in TeV** (D3 model, INP rows; `r1.out`, `refit.out`):

| Realisation | Equal vevs, couplings ×1 | Equal vevs, ×0.5 | Vev-tuned minimum, ×1 / ×0.5 |
|---|---|---|---|
| B-gen (conjugated) | 7.7e3 | 3.8e3 | 29.7 / 14.8 |
| B-gen120 | 3.8e3 | 1.9e3 | 43 / 21.5 |
| 11 further exact B-gen/B-gen120 refits | 3.8e3–7.9e3 | — | — |
| 35 FCNC-seeking exact refits | lowest 2.55e3 | lowest 1.27e3 | — |
| A-M1 #0, #1, #2 | 3.2e3, 6.2e3, 2.6e3 | 1.6e3, 3.1e3, 1.3e3 | — |

- **D6** at equal vevs comes out 1.3× higher, because more doublets dilute the vevs.
- **Binding rows:** D_Im, D_Re and K_Im.
- **The ×0.5 column** uses a recalled estimate of the Yukawa running to 10³–10⁴ TeV.

**The vev-tuned minimum is itself fine-tuned** (`r2.out:22-27`).
- At the optimum, the D amplitude cancels to 4e-5 of Σ|terms|.
- A 1% random jitter of the vevs restores M* to about 900 TeV (median).
- A joint search over the exact family plus the vevs did not go below 50 TeV at ×1 (`tuned.out`).

**Own cross-check** (`r2.out:17,20`).
- Inputs: FLAG 2024 B4^K = 0.903 (MS-bar, 3 GeV, Nf = 2+1); B4 = 1.0 for B and D (recalled); LO running with γ₄₄ = −16, which reproduces UTfit's a₄ = −1.143.
- Result for B-gen: M*_direct = 1.9e4 TeV from the D CP phase and 2.2e3 TeV from ε_K, against M*_INP = 7.7e3 TeV. The same order.

**H/A split, with A decoupled** (UTfit C2 and C4 rows). Again the same order: D needs about 1.2–1.7e3 TeV and ε_K about 0.4–2e3 TeV (`r2.out:18,35`).

## 3. Can the construction supply M*?

**S4 (proved, tree level): there is no decoupling limit.**
- Exact translations act on (H₀, Φ_x, Φ_y, Φ_z) as Z₂×Z₂. Every mixed bilinear Φ_a†Φ_b is odd, so there is no tadpole μ²H₀†Φ_K and no m₁₂².
- This is therefore not a 2HDM decoupling limit.
- The only odd sources are quartic terms such as λ′v₀v_yv_z. These give a seesaw, M_x² ≈ λ′v₀v_yv_z/v_x, for at most one carrier.
- Requiring all three carriers to be heavy gives (M_xM_yM_z)² ≤ λ′³·max(v₀³v_xv_yv_z).

**The numbers.**
- **Analytic:** 0.88 TeV for the seesaw carrier with λ ≤ 4π (1.25 TeV with 8π), using v_x ≥ 16.2 GeV, which follows from Yukawa ≤ √(4π) (`r2.out:50-53`).
- **Checked:** differential evolution over the general Z₂×Z₂-symmetric four-doublet potential (28 quartics; local minimum required; boundedness from below not imposed). The maximum, over couplings and vevs, of the lightest non-h state is 0.77 TeV at 4π and 1.09 TeV at 8π (`potential.out:3,6`). This is a global search, not a proof.

**The shortfall at M = 1.09 TeV.**

| Case | Shortfall in amplitude |
|---|---|
| Untuned | ≥ 1.4e6 |
| Vev-tuned optimum | ≥ 180 |
| Generous 10 TeV cap, untuned | ≥ 1.6e4 |
| Generous 10 TeV cap, vev-tuned | 2.2 |

**The task's decoupling question.** Suppose a tadpole existed. Then v_K = μ²v₀/M², and off-diagonal entries of y/3 with perturbative couplings would need μ²/M² ≥ 0.093 (up sector). That is possible with couplings below √(4π), but only given a K-carrying source, and X2 as written has none.

**Alternatives.**
- **Mechanism 1, a single light Higgs through a lattice-scale operator (proved).**
  - A k = 0 vev cannot change the corner. So an operator ψψH₀S_K with a K-carrying neutral condensate is needed, and that is class S.
  - With one electroweak doublet, h's dimension-4 couplings are exactly M/v, so there is no tree-level FCNC (proved).
  - Flavon exchange is about (m_off/f)²/f², below 1e-50 of the bound (suggested).
  - Whether OBS-3's one-loop Lorentz-violation zero survives in class S: suggested yes (OBS-3's on-site kernel identity plus Lemma S), not recomputed.
- **Pich–Tuzón alignment:** impossible (proved, §1).
- **Flavour symmetries.** Natural flavour conservation is impossible (proved). Any other symmetry only selects realisations within the exact family. The FCNC-seeking search over that family found an untuned M* of at least 1.3e3 TeV (checked; a local search, not a lower bound).

## Side findings

- **B-gen's J has the wrong sign as saved by OBS-3** (checked): J = −3.1157e-5, the CP conjugate of the observed value, because OBS-3 fitted |J|. Its complex conjugate has identical moduli and the same escape, so OBS-3's conclusions are unchanged.
- **The ordinary Higgs part is itself flavour-changing** (checked). |Ŷ⁰_uc| ≈ 0.66 at v₀ = v/2, because the light 2×2 block of W_u†X_u is an O(1) rotation.
- **h alignment** (checked arithmetic, HKZ rows). Within X2 as written, h must be aligned to |sin ε| ≲ 4e-5 to 2e-4 (`r2.out:28-30, 45-47`).
- **Class S hazard** (allowed, proved; effect not computed). The lattice-scale condensate leaves BCC translations, under which hw1 and hw3 share a label. So ψ†_{hw1}σψ_{hw3}S_K is allowed by every symmetry, which voids X2-L2's exact corner decoupling.
- **Domain walls** (suggested). Electroweak-scale spontaneous breaking of the discrete translations by doublet carriers implies domain walls.

## Controls

- **B-gen reproduced:** masses to 1e-11, |V| to 1.3e-14, |J| exact (`r1.out:2-6`).
- **Alignment control:** with every carrier proportional to M, the flavour-changing entries are 3.2e-16. The single-doublet control gives 1.5e-16 (`r1.out:11-12`).
- **Published comparisons.**
  - UTfit's C4 rows reproduce Harnik–Kopp–Zupan (arXiv:1209.1397) Table 2 to 1% (`r2.out:2-6`).
  - Crivellin–Kokulu–Greub's 2HDM-III (arXiv:1303.5877, eq. 39) uses the same C4 = −εε*/m_H² form. Their bound |ε^u₁₂ε^u*₂₁| < 2e-8 at 500 GeV is ×3 looser than the INP row's 6.5e-9 (different data and new-physics allowance).

## Deviations (`PREREG_FOLLOWUP_2026-10-15.md`)

- **C3 partly missed.** My direct K-Re row is ×2.8 looser than HKZ, while the registered threshold was ×2. The cause is the 100% Δm_K allowance. The reading uses the INP rows.
- **Added after the PREREG:** the cancellation and vev-jitter test, the FCNC-seeking and joint-tuned refits, the potential search, and the CKG comparison.
- **PREREG header time:** about one minute ahead of the clock.
- **Recalled, not fetched:** the B and D bag parameters, the quark masses at hadronic scales, and the Yukawa ×0.5 factor.

## Prior art

- A grep of main finds no FCNC analysis.
- Main's Z₃ support-trichotomy and single-Higgs-triviality notes are the generation-charge analogue of S1 and of the NFC result. They are cited, not reused.
- Within this packet the sources are X2-L3, OBS-3 §4 and OBS-3's referee §5.2.

## Comparison with the supervisor's own thread (read after the results)

- **Agreed:** PRICE; the translation-breaking condensate; mechanism 1 failing through the corner label.
- **Different:** the up sector (D mixing, |Ŷ_uc| up to 0.66) and ε_K bind, not the down sector. M* is about 10³–10⁴ TeV, not 10²–10³.
- **The supervisor's (v/M*)² tuning** assumes a tadpole, which X2 as written lacks. So the carriers are forced light, which is the supervisor's own KILL branch. PRICE survives only through the named structure.

## Scope

- Tree level only: no H± boxes, loops, electroweak precision tests or direct searches.
- Carrier models D3 and D6 (doublets) and S (singlets).
- Primary spectrum: degenerate H and A (decoupling form); the H-only split was checked.
- Matrix elements and running: INP/UTfit 2007 (NLO, RI-MOM, their bag parameters), with an own LO cross-check (FLAG 2024 B4^K; B4 = 1 for B and D).
- Couplings at the low scale and ×0.5.
- Realisations: B-gen, B-gen120, 46 further exact refits, and A-M1 #0–2.
- The scalar-potential ceiling is tree-level and perturbative (λ ≤ 4π or 8π), found by global search.

**Not shown:**
- that no non-degenerate fine-tuned cancellation exists at 1.1 TeV or below;
- that class S keeps OBS-3's Lorentz-violation zero;
- that class S is consistent with X2-L2.

## Files (`campaign/OBS4/`)

- `PREREG.md`, `PREREG_FOLLOWUP_2026-10-15.md`.
- In `scripts/`:
  - `obs4_core.py`, plus `obs4_{r1, r2, table, refit, tuned, potential, archive}.py` with their outputs;
  - `refit_solutions.npz`, `tuned_solutions.npz`;
  - `obs4_archive.npz` (574 arrays);
  - copied inputs `univ_B_gen.npz`, `univ_B_gen120.npz`, `univ_A_M1.npz`, `obs3_univ_copy.py`;
  - `capped.sh`.
