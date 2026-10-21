# Complete exercise argument with controlling corrections

Original source: `.claude/science/exercises/hierarchy-scale-ladder-20261018/H2/REPORT.md`; exact SHA-256 `6e048a2dfb7edd7b036d2404f69f4b8bbde796a6eb9c5dca224006a5958411a8`.

**Controlling scope:** Period-two Bloch corrections differ from dilute or longer-period breaking. Singular values are not generally gaps. The original representation is a comparator, not the full actual projective action. Degree-seven ranks and coefficient spans are not all-order mass classifications. Shared coefficients, labels and degeneracy hypotheses are required for proportional-sector mixing conclusions.

**Source-use boundary:** The complete argument below is preserved for inspection, including its original qualifications and counterexamples. Its old verdict labels, claims of completed reviews, operational history and numerical outputs are historical provenance only. Terminal physical exclusions and claims stronger than the controlling scope are deferred, not active conclusions. The canonical conditional exercise note and its correction register control. This attachment is not a separately promoted scientific claim and is not a fresh replay of its exploratory computations.

---

**Provenance:** the worker's final message, saved verbatim by the supervisor.

## HIER-2 report: fermion mass hierarchy on the scale ladder

**Reading: MASS-NO**, for a stated class: one lattice breaking whose form is fixed by symmetry. **OPEN** outside that class.

### In plain words

Following PR #9702 item 4, I took masses to be zero while the lattice symmetry holds and proportional to the breaking strength ε once it is broken. The idea under test was that the three generations feel the same breaking at different orders, ε, ε², ε³…, so their masses form a ladder.

Three things block it.

1. **The ladder cannot supply ε.** A suppression such as (a/w)^p, with a the lattice spacing and w the packet width, multiplies the momentum and vanishes at zero momentum, where a mass is defined. So ε has to be the strength of a breaking term. PR #9702 says such couplings are carried up the ladder but never fixed by it.
2. **The ladder cannot tell the up, down and lepton sectors apart.** Its symmetries act only on lattice labels. With shared coefficients, the top, bottom and tau get the same prediction. Their observed spread is 74 to 98, against at most 9 allowed by the factor-3 tolerance. The quark mixing matrix also comes out as the identity.
3. **Symmetry allows only two orders.** I checked every one-term breaking with a symmetry-fixed form at the eight cube-point nodes, in eight versions of how the symmetries act on the node states. Every mass appears at order ε or ε³, or stays exactly zero; no breaking produces three distinct orders. Even sector by sector, two levels can't fit the data: the best fit is off by a factor of 4.1 for leptons, 4.4 for down quarks and 12–18 for up quarks.

I also checked how much a successful fit would mean. If the integer exponents are fitted freely, every one of 400 random fake spectra fits within a factor of 3. So such a fit is evidence only if symmetry fixes the exponents, and here it doesn't.

### Results

**R1, proved: ε cannot be a ladder ratio.** A mass is the gap of the Bloch Hamiltonian H(k) at the node. Rung corrections (a/w)^p come from terms of order |q|^p in H(k*+q), which vanish at q = 0. Corollary: a localized breaking shifts a packet's energy by about (a/L)³ and gives no gap in infinite volume. So ε is a breaking amplitude, which the ladder transports but does not fix (PR #9702 note:367).

**R2, proved, arithmetic checked: sector blindness.**
- If the ladder acts trivially on internal labels and couples identically to all sectors, then M_u ∝ M_d ∝ M_e. That gives identical mass ratios across sectors and V_CKM = 1; a random check gives off-diagonal |V| of 2e-16.
- With unit coefficients, a fit within ×3 needs each generation's spread across sectors to be at most 9. Observed t : b : τ spreads are 98.3 (M_Z), 74.0 (2e16 GeV) and 97.2 (MIX set) (`fit_control.out`).
- The best sector-blind fit is ×9.9 at ε = 0.2165 with n = (7, 4, 1) — inside ×10, but only if those integers were fixed by symmetry. R5 shows they are not.
- Prior art says the same: `YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md:399` (×33 on m_b) and `YT_GENERATION_HIERARCHY_PRIMITIVE_ANALYSIS_NOTE_2026-04-18.md:513` (the sector columns are not proportional).

**R3, proved and checked: placing generations as an internal label (X2′) fixes nothing.**
- Proved: the ladder's symmetries act trivially on that label, so no exponent is fixed. Any integers would be supplied charges, i.e. an import.
- Checked: free-integer fits reach ×3 with a largest exponent of only 3 (ε ≈ 0.026). Every ε ≥ 1/9 fits automatically. 400 of 400 random log-uniform spectra fit (`fit_control.out`).
- This agrees with the prior FN results: `PRIMITIVE_P_HEAVYQ_..._pPheavyq.md:409` (WEAK) and `HIERARCHY_VALUE_FRONTIER_PROBE_2026-06-05.md:139-157` (loose).
- It also matches GEN1 (`campaign/GEN1/REPORT.md:17`, "the 3 is put in by hand") on branch `claude/chirality-grid-exercise-20261014`.

**R4, proved: structure lemmas for the eight nodes.** The node and chirality structure is that of PR #9702 note:89-96: chirality (−1)^hw, little groups O and D4.
- (a) A mass term pairs a left node s with a right node s′ and carries translation charge s+s′, which is always odd. For each odd charge c the allowed pairs form one permutation pattern P_c, and the four patterns tile the left–right grid like a Klein-group Latin square.
- (b) Node momentum differences lie in πZ³, so mass charges live in Z2³ whatever the spurion's period.
- (c) A spurion with a single harmonic Q reaches only one odd charge. Every mass then comes from one pattern, starting at a common order j0.
- (d) A single amplitude whose direction is fixed by symmetry must lie in one irreducible representation. In a sum of representations, the fixed spaces add.
- (e) One-dimensional representations give orders {1, ∞} only, because φⁿ transforms like φ for odd n.

Together these define class L1: one period-2 spurion in one irreducible representation, with a symmetry-fixed direction.

**R5, checked numerically (not a proof for higher-dimensional representations): L1 gives orders {1, 3} only.**
- Method (`scripts/orders_group.py`): Γ = Z2³ ⋊ O_h acting on 16 node states (eight nodes × spin ½); 40 irreducible spurion representations; 111 symmetry-fixed directions, taken from 2,644 subgroups. For each direction I built a generic equivariant effective Hamiltonian Σ εⁿ f_n(φ), n ≤ 7, and read the Dirac masses as singular values of its chirality-odd block.
- I ran 8 node-representation twist variants (a character of O on the k* orbit times a character of D4 on the six doublers), with 2 random seeds each, and no seed disagreements.
- In every variant every finite order is 1 or 3, with at most 2 distinct orders per spurion.
- Patterns in units of Dirac fermions (all four massless, all four at ε, and so on): (∞⁴) ×55, (1⁴) ×28, (1², ∞²) ×16, (1³, 3) ×10, (1², 3²) ×2 (`parse_variants.out`).
- Span check: the order-n terms fill nested spaces V1 ⊆ V3 ⊆ V5 inside the space of mass terms the stabiliser allows.
  - All 32 single-charge directions fill that space by order 3.
  - Of the 26 multi-charge directions, 22 fill it by order 3; the other 4 do so by order 5, but all their masses are nonzero by order 3, so order 5 cannot add a new mass.
- Independent check: `scripts/check_saturation.py` shares no code and solves the equivariance constraints directly. It matches all 6 compared charge-111 directions (E_g, T1_g, T2_g).

**R6, checked: two levels cannot fit** (`fit_twolevel.out`, unit coefficients, Λ and ε fitted).
- One sector: leptons ×4.1, down ×4.4, up ×11.7–17.8.
- All nine, with any assignment of {1, 3}: ×14–18. Sector-blind: ×22–43.
- These fail both MASS-PARTIAL clauses as I read them: one sector within ×3, or all nine within ×10.
- If the clause is read as "one sector within ×10", leptons and down quarks would pass. They do so only by putting two generations at the same order, which is not the ε^{n_i} ladder the item asks about.

**R7, checked: PR #9702 item 4's own mass gives no hierarchy.** I take its staggered term to be the charge-111 one-dimensional spurion; the mapping between my labels and the PR's PSG labels is assumed, not derived. That spurion gives all four Dirac fermions a mass at order ε, split 1 + 3 (multiplicities [2, 6]). The three doublers stay degenerate, as in main's S3 result (`YT_GENERATION_..._2026-04-18.md`, Outcome D).

### Supplied inputs

- **Masses** (recalled, not fetched): Xing–Zhang–Zhou SM running masses at M_Z and at 2e16 GeV, plus main's mixed set (`YT_GENERATION_...:482-490`). CKM magnitudes recalled.
- **Node model:** a naive-type node representation, which is a comparator and not the corner model itself, covered by 8 twist variants. All eight nodes are assumed at E = 0 in the symmetric theory.
- **Coefficients:** generic O(1) coefficients at each order, normalized to unit norm, and unit coefficients in the fits.
- **Parameters:** two continuous parameters, the overall scale Λ and ε. Tolerances ×3 and ×10.

### Prior art reused (cited, not re-derived)

- The GST rank-1 see-saw (`GST_TEXTURE_..._2026-06-08.md:30-31`) is the unprotected two-level version of the same result.
- The circulant correction (`YT_GENERATION_...:45-70`).
- FN with ε = 1/3 gives |V_us| = |V_cb| (`CKM_FROM_MASS_HIERARCHY_NOTE.md:271`).
- The historic EWSB cascade (`historic_intake/HISTORIC_EWSB_GENERATION_CASCADE_..._2026-08-05.md:46`).
- GEN-2: full O_h symmetry gives Y = a·1 + b·J, which has a degenerate pair (`sf_referees/GEN1_GEN2_LOCK1.md:77`).
- Axioms: `MINIMAL_AXIOMS_2026-06-29.md:37-41`.

The novelty claims rest on a `git grep` of main docs only. The structure lemmas (R4) and the L1 orders result (R5) were not found on main.

### Open, and limits of scope

- **Two amplitudes.** If the framework fixed the overall scale, a second breaking amplitude would fit the budget. Two-spurion classes are untested.
- **Patterns outside L1.** Multi-harmonic or longer-period textures need supplied pattern choices. With a single harmonic all masses share an offset; how the point group raises orders for longer periods is not computed.
- **Internal flavour symmetries** amount to supplying FN charges, an import.
- **Interaction-driven masses** (B7, PR note:47) fall outside the "mass proportional to breaking" class.
- Time reversal was not imposed. It can only remove terms, so the 26 cases that fill the allowed space by order 3 still hold.
- The corner model's actual node representation was not extracted.
- This is same-family work and unrefereed.
- The prediction I wrote before the runs (MASS-NO for L1 plus sector blindness) held.
- I did not read `SUPERVISOR_PREDICTION.md`.
- Nothing is left running.

### Files

All are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hier/H2/`:
- `PREREG.md` (11:40Z, before any run) and `PREREG_FOLLOWUP_2026-10-18.md` (12:16Z and 13:02Z: the lattice illustration replaced by the generic node-space computation, the variants added, and the superseded outputs listed).
- `scripts/fit_control.py` and `.out`, `scripts/orders_group.py`, `scripts/orders_A?-??.out` (the eight variants), `scripts/run_variants.sh`, `scripts/parse_variants.py` and `.out`, `scripts/check_saturation.py` and `.out`, `scripts/fit_twolevel.py` and `.out`.

Every run used `capped.sh`, one at a time; peak memory was 322 MB.