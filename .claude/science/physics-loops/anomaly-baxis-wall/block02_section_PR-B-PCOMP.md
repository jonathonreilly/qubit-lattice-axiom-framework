# Block02 Section — ROUTE PR-B (P-COMP, Hamming-ODD complementary sector + S4)

**Campaign:** anomaly_forces_time ABJ premise-bridge wall consolidation (block02)
**Keystone:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (ledger=unaudited; fanout 1105)
**Edge:** P-COMP = EXISTENCE/minimality of the opposite-chirality SU(2)-singlet RH completion template `{u_R, d_R, e_R, n_R}` (incl. neutral `n_R`) consumed by keystone step **(B3)**, `(y_1,y_2,y_3,y_4)=(4/3,-2/3,-2,0)` at `a=1/3`.
**Branch:** `physics-loop/anomaly-abj-bridge-block02-20260620`
**Runner:** `scripts/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.py` → `logs/runner-cache/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.txt` — **TOTAL: PASS=31 FAIL=0**
**Date:** 2026-06-20
**Outcome:** `wall_stands` (decisive finite KILL of the candidate crack). cracked = **no**.

---

## 0. The route and the gap it targeted

Block01's P-COMP runner (`frontier_abj_pcomp_block01_template_existence_2026_06_20.py`, PASS=49) inspected **only the Hamming-EVEN L-sector** of `Λ(C³)=(C²)^⊗3` (dim 8):

> even-parity L-sector (hw ∈ {0,2}) = `{|000>,|011>,|101>,|110>}`

and concluded "the carrier supplies ONLY the LH 6+2 surface; the RH completion must be adjoined" — but it never computed the gauge quantum numbers on the **complementary Hamming-ODD sector** `{|001>,|010>,|100>,|111>}`. PR-B's hypothesis (the "likely crack"): that odd sector is the **4_-** block of the `8 = 4_+ ⊕ 4_-` chirality split, and its quantum numbers might **match** the RH template `{u_R,d_R,e_R,n_R}` — making P-COMP existence **native** (deps-all-retained bankable) and breaking the circularity-on-parent.

**DECISIVE-FAILURE test run BEFORE any crack claim** (per posture): if the odd-sector color rep is the same `3` as the even sector (not `3̄`), or the odd sector is an SU(2)-doublet (not singlet), or the J/CPT image is vectorlike, the route is **killed**. All three failure conditions fired. The route is dead; P-COMP existence stays walled → register-as-premise.

---

## 1. Source discipline — recomputed in-tree (no blind keystone cite)

The carrier `Γ₁=σ₁⊗I⊗I, Γ₂=σ₃⊗σ₁⊗I, Γ₃=σ₃⊗σ₃⊗σ₁` (`{Γᵢ,Γⱼ}=2δᵢⱼI₈`), the lifted retained `Y=(1/3)P_sym − P_anti`, the fiber SU(2)_weak `Jf_i=I₄⊗σᵢ/2`, and the SU(3) color generators on the base-symmetric subspace were **all rebuilt numerically** (checks 0.1, A0–A2, B0, C0–C1). They reproduce the retained-grade surface: full `Y` spectrum `{+1/3 ×6, −1 ×2}` (A1), `[SU(3),Y]=[SU(3),SU(2)_weak]=0` (C1), fundamental anomaly index `A(3)=+1` (C3). Retained authorities used (recomputed, not cited blind): `cl3_color_automorphism_theorem` (retained_bounded, chain_closes=True), `cl3_complexification_split_narrow_theorem_note_2026-05-10` (retained, chain_closes=True).

---

## 2. DECISIVE-FAILURE #0 — the route's structural premise is FALSE (checks 0.5–0.7)

The route assumed "Hamming-odd = the 4_- chirality block." **It is not.** The Cl(3) pseudoscalar `ω=Γ₁Γ₂Γ₃` (the chirality element, `ω²=−I₈`, central — check 0.2) is the **anti-diagonal bit-complement**: `ω|b₁b₂b₃> ∝ |~b₁~b₂~b₃>`, which sends `hw → 3−hw` and therefore **flips Hamming parity**. So:

- `ω` is **zero within** each Hamming-parity block and maps even↔odd (0.5) — the Hamming-parity split is **not** the chirality split.
- The genuine `ω`-chirality (±i) eigenspaces are **50/50 even/odd mixtures** (0.6, `max|w_even−w_odd|=2.2e-16`); neither chirality eigenspace is a Hamming sector.

This is the complexification-split content (`e_±=(1∓iω)/2`, `ω→±i`) seen explicitly: the `4_+⊕4_-` split lives in the complexified algebra and cuts ACROSS Hamming parity. The Hamming-odd sector is a legitimate **subspace** to read gauge quantum numbers on (0.7) but is **not** an opposite-chirality block — already fatal to "native RH."

---

## 3. The explicit quantum-number table (the deliverable, either way)

| object | RH template (keystone B3) | Hamming-ODD sector `{|001>,|010>,|100>,|111>}` |
|---|---|---|
| chirality (ω ±i block?) | OPPOSITE (RH) | **NOT a chirality block** (ω flips parity; §2) |
| SU(2)_weak rep | **singlet** (T(F)=0) | **fiber DOUBLET-half** (T₃=±1/2, Casimir=3/4) |
| color rep | **3̄** (A=−1) | carrier color = **3** (A=+1); odd sector not an SU(3) subrep |
| Y spectrum (a=1/3) | `{4/3, −2/3, −2, 0}` | `{+1/3, +1/3, +1/3, −1}` (same as even LH) |
| relation to even sector | independent, adjoined | **SU(2)_weak fiber-flip image** (vectorlike) |
| neutral n=0 ray | present (`n_R`) | **absent** (`Y` has no 0 eigenvalue) |

Every row is a mismatch. The three load-bearing decisive failures:

- **#1 color (C2–C5):** SU(3) acts on the base-symmetric 3D subspace and does **not** preserve Hamming parity (C2, parity-block-diagonal=False), so "the odd sector's color rep" is not even a well-defined SU(3) subrep. The well-defined carrier color content is the **fundamental 3** (`A=+1`, C4), giving net carrier `SU(3)³ = +2` (C5). The RH completion the keystone consumes needs **3̄** (`A=−1`, per `RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL` — note: that note is `unaudited`, but the conclusion does not depend on it: the carrier provably supplies `3`, not `3̄`, computed from the retained color carrier). No native `3̄`.
- **#2 hypercharge (A3–A5, D1):** `Y` is built from the base SWAP and is fiber-trivial, hence **parity-blind** (`[Y,P_parity]=0`, A2). The odd sector carries the **same** `{+1/3 ×3, −1}` spectrum as the even LH sector (A4, D1), **not** `{4/3,−2/3,−2,0}` (A5).
- **#3 SU(2) (B1–B2, D2):** the fiber flip `σ₁` on `b₃` (an SU(2)_weak group element, a **symmetry** not a chirality flip) permutes even↔odd (B1, D2). So the odd sector is the SU(2)_weak partner-half of the LH content: a **doublet-half** (Casimir=3/4, T₃=±1/2, B2), not an SU(2)-singlet.

**Even-sector saturation ⇒ vectorlike-exclusion (D4):** the even sector already realizes the full `{+1/3 ×6, −1 ×2}` LH surface; the odd sector is merely its SU(2)_weak image. The 8-dim carrier is **one LH SU(2)-doublet generation that is SU(2)-vectorlike across the parity split**, NOT `LH ⊕ opposite-chirality-RH`. It supplies **no** independent opposite-chirality SU(2)-singlet 3̄ RH block. The block01 conclusion ("RH completion must be adjoined") **stands, now proven by direct computation of the complementary block** rather than asserted from inspecting only the even sector.

---

## 4. Route S4 — Record K/CPT conjugation J on the LH 6+2 surface (checks E-S4)

S4 asked whether the antilinear Record/CPT conjugation `J=K` on the LH surface yields the chiral RH SU(2)-singlet completion with `n=0` fixed. All three legs **fail**:

- **(i)** `J=CPT` of an LH SU(2) **doublet** is a doublet (SU(2) is pseudoreal, `2̄≅2`; conj-doublet Casimir = 3/4, E-S4(i)) — **not** an SU(2)-singlet.
- **(ii)** `J=CPT` sends `Y → −Y`, giving `{−1/3 ×6, +1 ×2}` — the CPT **mirror** of the LH set, **not** the RH template `{4/3,−2/3,−2,0}` (E-S4(ii)).
- **(iii)** the neutral `n=0` ray **does not exist** in the carrier: `Y` has spectrum `{+1/3,−1}` with **no** zero eigenvalue (E-S4(iii)). The neutral singlet `n_R` is an adjoined template slot, not a carrier J-fixed ray.

S4 produces a **vectorlike CPT-mirror** (doublet, `Y→−Y`, no `n=0`), consistent with §3, not a chiral RH completion. No crack from the Record/CPT route either. This is exactly the `CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05` content made quantitative: Record/CPT is a consumer of chirality (it conjugates an existing doublet), not a source of the opposite-chirality singlet sector.

---

## 5. Verdict

**P-COMP existence stays WALLED — `register-as-premise`. cracked = no.** The candidate crack (Hamming-odd = native RH template) is **decisively killed** by a finite in-tree computation: the odd sector is (a) not an ω-chirality block, (b) an SU(2)_weak doublet-half not a singlet, (c) color **3** not **3̄**, with (d) the same parity-blind `{+1/3,−1}` hypercharge as the even LH sector — it is the SU(2)_weak fiber image of the LH content (vectorlike), and S4's J/CPT route gives only the CPT mirror with no native `n=0`. The carrier is one LH generation; the opposite-chirality SU(2)-singlet 3̄ RH completion (incl. neutral `n_R`) must still be **adjoined**, and A_min (Lattice+Quantum+Record) + the four approved primitives withhold that second-chirality matter sector. No new axiom/primitive available to supply it.

**What it unlocks on the 1105 cone:** nothing new is unlocked for movement; the decisive-FAILURE outcome instead **sharpens** the P-COMP wall from block01's "asserted via axiom-withholding / steelman-defeat" to a **computed no-go on the complementary chirality block**: the only candidate native supplier (the unused half of the carrier) is provably the vectorlike SU(2) partner of the LH content, not the chiral RH template. P-COMP existence remains non-bankable (existence-side suppliers `rh_completion_color_anti_fundamental` and `su3_anomaly_forced_3bar` are `unaudited`; `su3_dabc_symmetric` is `audited_failed`); only the block01 **arithmetic core** (given template+n=0 ⇒ `{4a,−2a,−6a,0}`, re-derived here in F1) remains bankable deps-all-retained, and **circular-on-parent persists**. The keystone P-COMP edge stays a named admitted premise.

---

## 6. Firewall / forbidden-surface attestation

New artifacts only: this section, `scripts/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.py`, and its cache `logs/runner-cache/frontier_abj_pcomp_hamming_odd_sector_2026_06_20.txt`. **No file under `docs/audit/`, `docs/publication/`, AUDIT_LEDGER/QUEUE, or MISSING_DERIVATION_PROMPTS was edited.** `docs/audit/data/audit_ledger.json` was parsed READ-ONLY (python) to confirm effective_status/chain_closes of the cited authorities. No row/effective status set; no audit verdict asserted. Independent audit lane is the sole authority before any effective-retained movement.
