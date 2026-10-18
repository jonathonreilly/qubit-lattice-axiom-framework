# F6 route report: is the chirality wall misframed?

- **Agent:** route agent F6, Claude Opus 5.5. This is the same family as the supervisor, so it is not an independent referee.
- **Window:** 2026-10-14, 13:19–13:41Z.
- **Folder:** `routes/F6/` (the unusable PDG PDF download was deleted), holding `PREREG.md` (written before any run), `scripts/` and outputs, and this file.
- **Refresher read:**
  - `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full;
  - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, skimmed, along with the primitive list it generates;
  - `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`, skimmed;
  - the exercise SKILL steps 4 and 6, and `proof-search-governance.md`, both from origin/main;
  - the packet files `WALL.md`, `ASSUMPTIONS.md`, `APPROACH_REGISTRY.md` and `step0/PRIOR_ART.md`;
  - from HEAD: K2a, `TEST_LOG.md:58-96`, and `KILL_SHEET.md:75-83`;
  - `docs/repo/DEFERRED_DECISIONS.md:121-146`.
- **Labels:**
  - **proved:** a proof is given here;
  - **checked:** a runner in `scripts/`;
  - **suggested:** an argument that has not been checked;
  - **reading:** an interpretation;
  - **comparator:** an outside result used for comparison.
- **AX** = `docs/MINIMAL_AXIOMS_2026-06-29.md`.

## Verdict in plain words

The wall is **partly misframed**. Checked evidence supports four misframings. The core of the wall survives, but it is not specific to this framework.

**Misframed (checked):**
1. **"Handedness on the grid" names the wrong object.** One qubit per site already carries an exact handedness operator in continuous time. It is the shift along the body diagonal (checked: exact on L = 4, and proved for all even L). What the grid lacks is a *net* surplus of one hand. No larger site algebra and no parity or orientation choice changes that surplus: it is zero for 2 and for 4 states per site, with no symmetry imposed (proved by Stokes, illustrated on 40 random carriers).
   - So the parked M₄(ℂ) enlargement (#4) and the orientation bit (#2) are not prices for this wall.
   - #4's wake condition is *not* fired by this wall, contrary to `PRIOR_ART.md:230`.
2. **Every one-body or mass-term escape was guaranteed to fail.** A symmetric mass term can never change the net hand count. This is the index lemma (proved).
3. **One listed escape is ruled out by data.** "Break a symmetry so the mirrors get heavy" fails when the broken symmetry is the electroweak one, because mirror copies that get their mass that way are excluded (checked):
   - S is off by 6.5σ for three mirror families;
   - Δχ² ≥ 41 over all mass splittings;
   - the gg→h rate is ≥ 9.3 times the observed one.
4. **"The walker gives 8 species where 48 are needed" (T25) is a category error.** The single-handed three-corner triplet gives 3 per on-site multiplet. With the 16 carried on-site, that is exactly 3 × 16 = 48 (checked).

**Not misframed:** observation really does demand a light spectrum that is a complex representation of the exact gauge group, with no light mirrors, while every free lattice spectrum is a real one. This survives.

**What it is instead:**
- The framework's own mirror halves pass every anomaly gate I computed, once ν^c is included (checked). So nothing the framework itself fixes forbids gapping them symmetrically, as far as that gate reaches.
- What remains is the field-wide open question: does an anomaly-free mirror set gap symmetrically, leaving a truly chiral survivor? Golterman–Shamir now contest this with a generalized no-go (comparator). That no-go assumes a "fermions with a global symmetry first, gauge later" method which the axioms do not supply (reading).

## Dependency reduction: what the doubling no-gos assume, what the axioms supply, what observation demands

| Premise of the no-go family | Used by | Axioms supply? | Observation demands? |
|---|---|---|---|
| Translation invariance | NN; LATTICE_HANDEDNESS T1/T2; GS (A) | yes (AX:37-41, :57-58) | no; only emergent Poincaré invariance far below 1/a |
| Finite range / C¹ symbol | NN; LH T2 | the rule is nearest-neighbour (AX:57); the dynamics' range is **not supplied** (AX:116-123) | no; exponential locality at a = l_P is not observable |
| Free (bilinear) dynamics | NN; LH T1/T2; blocks 77/82/119/139 | **no** dynamics at all (AX:114-123) | no |
| Hermitian H / unitary tick | NN; LH | **no** (AX:116-123) | yes, for the infrared S-matrix |
| An exactly conserved **global, on-site** G acting on fermions before gauging | NN (every version); GS (B) | **no**: neither G nor fermions are supplied (AX:178 gate) | no. Observation demands exact *gauge* invariance of the infrared, not a global on-site G on ultraviolet fermions |
| No massless bosons in the ungauged infrared | GS (C) | n/a | **contradicted** by observation (photon, gluons); it holds only in the "global first, gauge later" method |
| Complete set of interpolating fields (no propagator zeros) | GS (D) | n/a | no direct demand |
| Parity / orientation | none of them | proper rotations only (AX:37-38) | weak parity violation (consistent) |
| Site-algebra size | none (NN holds for any N) | M₂(ℂ) (AX:47) | no |
| Light content is a complex rep of the exact infrared G, with mirrors invisible | the target | — | **yes**: Γ_Z, direct searches, S/T, Higgs rates (route F6-2) |

**Reading:** the bottom row is the only part of "chirality on the grid" that observation demands. Every other row is either supplied by method (free, Hermitian, on-site global G, the global-then-gauge order) or irrelevant (algebra size, parity). GS's conditions A–D are taken from a WebFetch summary of arXiv:2603.15985v1 §2–3.2. I did not read the full text.

## Routes

| Route | Family (object, mechanism, terminal obligation) | Premise it drops or changes | What you would have to believe | First artifact | Cost | What it would change if it worked |
|---|---|---|---|---|---|---|
| **F6-1 Wrong object** | object: the lattice chirality *operator* versus the *net* Weyl charge; mechanism: body-diagonal translation eigenvalue, and Stokes on T³; terminal: "no site algebra and no parity choice changes the net charge" | A2 (M₂(ℂ) as the binding constraint), the Clifford-parity reading, the orientation bit | nothing new; NN for N bands is standard | `scripts/tA_operator_vs_net.py` (**run, PASS**) | done (<1 s) | removes decisions #4 and #2 from the wall's price list; T2 becomes checked; stops M₄(ℂ) being woken by this wall |
| **F6-2 Observation's actual demand** | object: the light G-representation; mechanism: chiral-index invariance under G-invariant bilinears, plus non-decoupling S and gg→h; terminal: "a construction must contain one of five things: (i) a non-bilinear symmetric mirror gap, (ii) a non-on-site or emergent G, (iii) an extra coordinate, (iv) explicit tuned grid-scale gauge breaking, or (v) non-Hermitian or infinite-range dynamics" | the free/bilinear class as evidence; plain-version exit 1 (`WALL.md:18`) | the measured S/T and Higgs rates; G exact in the infrared | `scripts/tB_observation.py` (**run, PASS**) | done | replaces the 11-item "what currently fails" list (`WALL.md:48`) with one theorem; halts bilinear/covariant-term blocks; drops the "spontaneously heavy mirrors" exit |
| **F6-3 The cheaper question** | object: the framework's own mirror half (walker hw-split; KS/K2a T_d-split); mechanism: anomaly gate, then the GS-condition audit, then vacuum polarization; terminal: "a framework-fixed symmetry obstructs a symmetric mirror gap", or else "the wall is the field-wide SMG question" | the "construct the full SM chiral gauge theory" target as the framework's wall | SMG conjecture plus a way past GS A–D (most natural: C, through emergent gauge bosons) | `scripts/tC_anomaly_gate.py` (**run, PASS with ν^c**) and `scripts/tD_fmass.py` (**run, PASS**) | gate 1 done; GS audit ≈ 1 h desk work; vacuum polarization = K2b-scale | re-files the wall from "framework defect" to "shared open conjecture plus two framework prices (matter count; how gauge fields arise)" |

### F6-1 Wrong object: operator versus net chirality

**Lemma 1a (proved; checked on L = 4).** Take the walker H = Σ_a σ_a sin p_a on one qubit per site, on any even periodic L, with the body-diagonal shift T_d = T_xT_yT_z and the staggered sign ε = (−1)^{x+y+z}.
- **Claims:**
  1. [H, T_d] = 0;
  2. T_d ε T_d⁻¹ = −ε;
  3. on the node at corner k ∈ {0, π}³, T_d = e^{i(k_x+k_y+k_z)} = (−1)^{hw} = −(monopole charge).
- **Proof:**
  - claim 1 holds because H is translation-invariant;
  - claim 2 holds because a shift by (1,1,1) flips x + y + z mod 2;
  - for claim 3, the node chirality is sign Π cos k_a = (−1)^{hw}.
- **Consequence:** T_d commutes with the kinetic term and anticommutes with mε, the only mass that keeps the books (block 139). These are exactly the Hamiltonian-form properties of γ5.
- **Checked (`tA_output.txt`):** both commutators are 0.0 exactly. min|E(H + mε)| = m. The product T_d × monopole is −1 at all 8 corners, with monopoles computed independently by discrete Stokes.
- **Scope:** this is the walker analogue of K2a's KS result (`TEST_LOG.md:73`), now covering the walker and with an exact proof.

**Lemma 1b (proved: Stokes on T³; NN 1981; Haldane PRL 93, 206602).** Take any Hermitian N×N symbol H(k) on T³ that is C¹ (finite range suffices), for any N (M_N(ℂ) per site), with no parity, time-reversal or rotation symmetry. Then for every n, the charges of the Weyl nodes between bands n and n+1 sum to zero. With an exact on-site U(1), the same holds in each charge sector.
- **Proof:** let C_n(k_z) be the Chern number of P_{≤n} on the slice k_z = const. It jumps by the node charges as k_z crosses them, and C_n(0) = C_n(2π).
- **Open step (routine):** non-generic, non-isolated degeneracies are handled by a small perturbation that preserves the sum.
- **Checked illustration (`tA_output.txt`):** 20 random range-1 carriers with N = 2 and 20 with N = 4, no symmetry imposed. All have net 0; all 40 have nodes of both hands (N = 4: 10–24 per hand).

**Gap test.** L1 = 1a + 1b does not imply the target. It is weaker: it prunes routes rather than reaching for the target. It is not target-equivalent.

**Price:** none. It removes prices: #4 (M₄(ℂ)) and #2 (the orientation bit) do not bear on the doubling wall.

**Specific correction.** #4's premise is "chirality exists only for even Clifford dimension" (`DEFERRED_DECISIONS.md:122-125`). Its wake condition 1 fires only if "a live lane hits the M₂(ℂ) wall the proposal addresses" (:139-141).
- The wall this exercise faces is net chirality.
- M₄(ℂ) does not address net chirality (1b), and M₂(ℂ) already has the operator (1a).
- So this exercise does **not** fire #4 on chirality grounds. *(checked)*

**Law-achiral versus state-chiral (proved, one line).** Proper cubic rotations preserve hw and the monopole charge, and translations preserve k. So no axiom symmetry exchanges the walker's hands. A hand-selective law term is therefore already covariant, and neither a parity-symmetric law nor a spontaneous hand choice is needed. A2 shows that parity also does not protect against doubling.

### F6-2 What observation actually demands

**Lemma 2 (proved; index lemma).** Let V be the left-handed Weyl content, a finite-dimensional unitary representation of a compact G. Let M be any G-invariant symmetric mass form (Majorana or Dirac), and K = ker M the massless content. Then the class [V] − [V̄] equals [K] − [K̄] in the representation ring.
- **Proof:** the form is nondegenerate on V/K, so V/K ≅ (V/K)*, which is self-conjugate. Characters are additive.
- **Corollary:** vector-like V gives vector-like K.
- **Checked:** 200/200 random U(1) trials preserve the per-charge index n_q − n_{−q} (`tB_output.txt`).

Together with NN (free dynamics gives a vector-like infrared), this makes every route in the free/bilinear class fail by theorem. That includes:
- the Wilson-like and covariant site terms (blocks 77/82/119/139);
- mε;
- 3D mass walls;
- free ticks.

Their recorded failures (`WALL.md:48`; `PRIOR_ART.md:136-168`, items 1–5 and 8–9) carried no information beyond this lemma. *(reading, based on the proved lemma)*

**Observation check (checked, `tB_output.txt`).** Suppose the mirrors get their mass from SU(2)×U(1) breaking, by any Higgs sector. Their contribution to S is non-decoupling: N_c/(6π) per degenerate doublet (Peskin–Takeuchi, PRD 46, 381):

| Mirror content | S | Pull vs Gfitter 2013, U = 0 (S = 0.05 ± 0.09; arXiv:1306.0571) |
|---|---|---|
| One mirror family | 0.212 | 1.8σ |
| KS split, two families | 0.424 | 4.2σ |
| Walker split, three families | 0.637 | 6.5σ |

- **Splittings:** a scan over 0.4–5 TeV with the heavy-limit S and T and ρ_ST = 0.91 gives min Δχ² = 41.0. Splitting cannot rescue it.
- **gg→h:** with a mirror quark doublet that couples through the Standard Model Higgs, μ_ggF is 9.31–9.38 for one family and about 51 for three, at m_Q = 0.4–3 TeV. Measured μ_ggF is about 1.0 ± 0.1 (ATLAS and CMS, Nature 607 (2022) 52 and 60; approximate).
- **Comparator:** the sequential fourth generation is excluded at 5.3σ (Eberhardt et al., PRL 109, 241802; verified by search).
- **Pre-registered PASS met.**

**Reduction (proved from Lemma 2 plus NN; exhaustive by complement).** An observationally viable construction must contain at least one of:
- (i) a non-bilinear G-symmetric mirror gap (SMG);
- (ii) a G that is not on-site on the lattice fermions (Ginsparg–Wilson/Lüscher, or emergent G);
- (iii) mirrors placed elsewhere (an extra coordinate);
- (iv) explicit grid-scale G-breaking, restored by tuning. Its price is a tuned law, for example the vector-boson mass counterterm tuned to about (v/M_Pl)² ≈ 10⁻³⁴ (suggested estimate);
- (v) non-Hermitian or infinite-range dynamics.

This matches the wall's step-3 list (`ASSUMPTIONS.md:35-39`), with one change: "spontaneously heavy mirrors" is removed (checked). Plain-version exit 1 (`WALL.md:18`) survives only in reading (iv).

**Gap test.** This is a necessary-condition reduction, weaker than the target, and not target-equivalent.

**Price:** none at axiom level. The axioms supply no free carrier (AX:114-123), so dropping "free" costs nothing. Interactions are supplied dynamics and are counted under the contract (`WALL.md:43`).

### F6-3 The cheaper question that replaces the wall

**Q\* (precise).** Take the framework's own doubled content: the carrier fixes its mirror half, and the matter count fixes its multiplicity. Is that mirror half free of every anomaly of the symmetries the framework keeps exact? Those are translations, as corner Z₂ charges; proper rotations; fermion parity; and the supplied G_SM, with Spin-Z₄^X if kept.

Then, for any local symmetric interaction that gaps it, which of the Golterman–Shamir conditions A–D does it satisfy?
- **If an anomaly survives:** the exact price is breaking that symmetry, or adding content.
- **If none survives:** the chirality wall is not a framework wall. It is the shared SMG question, which the framework owes only through:
  - (a) a matter-count decision: 16 modes per site for KS, 32 for the walker, against one qubit per site (`PRIOR_ART.md:233`, open gate 8);
  - (b) whether gauge fields enter as links on a global G (the GS regime) or emerge together with the fermions.

**Why it is cheaper.** Gate 1 is finite arithmetic and gate 2 is a desk audit. The original target is the 40-year-open non-perturbative construction of the SM chiral gauge theory.

**Gap test.** Q\* passing is necessary, not sufficient (weaker). Gates 1–3 together would give W-a (fermion content), but not W-b (gauging). Strength vs target: unknown/comparable after gate 3, and weaker before it.

**First test, run: the anomaly gate (`tC_output.txt`, pre-registered T-C).** Fields carry left-handed-basis SM charges.

| Split | Light | Mirror |
|---|---|---|
| Walker | hw = 1 corners | hw = 0, 2, 3, i.e. 4×16̄ ⊕ 16 |
| KS/K2a | T_d-even, 2 × 16 | T_d-odd, 2 × 16̄ |

The coefficients checked were SU(3)³, Y³, Y-grav, SU(3)²Y, SU(2)²Y, Witten, Z₁₆ (X = 5(B−L) − 4Y), and Ibáñez–Ross mod-2 Z₂×G² for all 7 corner-translation Z₂s.
- **With ν^c:** every coefficient vanishes for both mirror halves. **PASS** (as expected).
- **Without ν^c:** Z₁₆ fails. The walker mirror gives 3 mod 16 and the KS mirror gives 2 mod 16, so if Z₄^X is kept exact, the price is ν^c (or a TQFT sector).
  - The script also flags Z₂-gravity mod 2 for the walker without ν^c.
  - For even N the Ibáñez–Ross gravitational condition is only mod N/2, which is vacuous for Z₂, and I take Ω₅^Spin(BZ₂) = 0 (Hsieh, arXiv:1808.02881; not re-derived). So I read that flag as not an anomaly.
- **Not computed:** global bordism classes of Spin × Z₂³ × G_SM beyond Z₁₆ and Witten. This is the named residual of gate 1.
- **Count (checked):** the walker split with 16 on-site fields gives 48 light Weyl fermions, all of one hand, which is exactly 3 × 16. So T25's "8 where 48 are needed" (`PRIOR_ART.md:126`) compares per-field nodes with total Weyl number. The deficit is a matter-count question, not a species one.

**Supporting construction (checked, `tD_output.txt`, pre-registered T-D).** Take the walker plus M_f = i ε F, where F has symbol f = s(s² − 1) and s = Σ cos k_a.
- **Properties:** range 3, invariant under cubic rotations, G-invariant, staggered like mε.
- **Exact checks:** M_f is Hermitian and {H, M_f} = 0, so the gap is |f|.
- **Zero modes:** exactly 12 at L = 4 and L = 8, sitting at hw = 1 (T_d = −1) and hw = 2 (T_d = +1).
- **Result:** one local bilinear reduces each field to 3 L + 3 R, graded by T_d on the nodes. The list a symmetric gap must remove is exactly 3 × 16̄, with no vector-like pair.
- **Caveat (reading):** M_f is T_d-odd and couples hw1 to hw2 at O(q²), a Wilson-like irrelevant light–mirror mixing. Any SMG candidate must survive it. Alternatively, keep hw0/hw3 and gap the whole hw0+2+3 half, which also passes gate 1.

**Generation side-findings (proved, one line each).**
- **Degeneracy.** If hw = 1 is the generations and translations are exact, a uniform (k = 0) Higgs gives Yukawas diagonal in the corner basis, because crystal momentum is conserved and corners are self-conjugate. Proper rotations, which permute the axes, then force the three generations to be degenerate. So mass splitting and CKM mixing need translation breaking at hw = 2 momenta e_i + e_j.
- **Mixing stays light.** Those momenta are T_d-even, since T_d(k+Q) = T_d(k)T_d(Q). Flavour mixing therefore does not by itself couple the T_d-selected light and mirror halves.

**Second test (named, not run; cheapest decisive next step).** Audit the two candidate interactions, the K2a Spin(10) quartic on P̄_Rψ and a walker T_d quartic, against GS conditions A–D (arXiv:2505.20436 v3; arXiv:2603.15985 §3.2).
- **Pre-registered reading:** if a candidate meets all of A–D, then per GS its survivor is vector-like and K2b *as posed* is blocked-equivalent. The route must then name which of B, C or D it gives up. If a candidate violates one, say which, and whether that violation is allowed by observation.
- **My expectation (suggested):** the K2a candidate meets A–D. The violation that is natural for this framework is C: gauge bosons that emerge with the fermions, since no G is supplied.
- **Who:** the F1 or F2 route agent, or the supervisor.

**Third test (decisive, expensive; already pre-registered as K2b/TW-3).** Use GS §4's proposed probe, the low-momentum current two-point function (vacuum polarization), in the smallest SMG cluster or slab.
- **Survivor chiral:** the coefficient counts the light set only.
- **GS correct:** composite partners restore the vector-like value.

## What not to do next (reading, based on the checks above)

- No more one-body or covariant-mass-term blocks aimed at net handedness (Lemma 2 plus NN).
- Do not wake #4 (M₄(ℂ)) or #2 (the orientation bit) on chirality grounds (F6-1).
- Do not plan "heavy mirrors from a second Higgs" (F6-2 check).
- Do not treat anomaly cancellation as sufficient for success. GS argue explicitly that it is not (comparator); gate 2 exists for this reason.

## Tests run (all pre-registered in `PREREG.md` before running; outputs beside the scripts)

| Test | Pre-registered PASS | Result |
|---|---|---|
| T-A1 operator on M₂(ℂ) | exact commutators; sign relation at 8 corners | **PASS**: 0.0, 0.0, min\|E\| = m, product −1 at all corners |
| T-A2 net = 0, N = 2 and 4, no symmetry | all nets 0; both hands in ≥ half of N = 4 | **PASS**: 40/40 net 0; both hands 20/20 for each N |
| T-B1 index lemma | 200/200 | **PASS** |
| T-B2 EW-mass mirrors | S(3 families) > 3σ and μ_ggF ≥ 5 | **PASS**: 6.5σ; Δχ² ≥ 41 over splittings; μ ≥ 9.31 |
| T-C anomaly gate | with ν^c all listed coefficients 0, both splits | **PASS**; without ν^c only Z₁₆ fails (as expected), plus the vacuous Z₂-grav flag |
| T-D f-mass construction | 12 zero modes at hw1/hw2 with T_d grading | **PASS** (L = 4, 8) |

**Resource use:** each script ran in under 3 s and under 0.1 GB (T-A peaked at 72 MB).

**Review:** no referee yet. These are all positive results, not failures read as no-gos. The two places a referee should look:
1. the Ibáñez–Ross mod-2 normalisation and the Z₂-gravity reading in T-C;
2. the heavy-limit S formula with splitting, and its hypercharge sign convention (both signs were scanned) in T-B2.

## Literature (cited for templates and comparators; none imported as proof)

- Nielsen–Ninomiya, Nucl. Phys. B185 (1981) 20 and PLB 105 (1981) 219.
- Haldane, PRL 93 (2004) 206602.
- Fukui–Hatsugai–Suzuki, JPSJ 74 (2005) 1674.
- Peskin–Takeuchi, PRD 46 (1992) 381.
- Gfitter, arXiv:1306.0571.
- Eberhardt et al., PRL 109 (2012) 241802 (arXiv:1209.1101).
- ATLAS and CMS, Nature 607 (2022) 52 and 60.
- Ibáñez–Ross, PLB 260 (1991) 291.
- Hsieh, arXiv:1808.02881.
- García-Etxebarria–Montero, JHEP 08 (2019) 003 (arXiv:1808.00009).
- Golterman–Shamir: arXiv:2311.12790 (zeros act as ghosts once gauged; unitarity lost), arXiv:2505.20436 v3 (generalized no-go, conditions), and arXiv:2603.15985 (SMG and NN; conditions A–D; "anomaly cancellation is no guarantee"). These were read through abstract and HTML summaries only.
- Zeng–Xu–Lu–You, arXiv:2405.05339 (treats zeros as physical).
