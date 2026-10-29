Reviewer model: claude-opus-5-5

# BFT4B55 — BFT-4 (b): locally gauge-invariant polymers on 𝒞_glob (Opus 5.5 worker)

UTC start: 2026-10-29T03:47:16Z
Brief: scratchpad/queue/bft4b.md; shared rules: scratchpad/REVIEW_BRIEF_55.md (worker; rules apply).
Writes: this file and `checks/b4b55_*` only. No git.

## 0. PRE-STATED (written before any derivation)

**Targets, in order.**

T0 (consumption). Decide whether BFT-4 (b) — locally gauge-invariant polymer pieces, as opposed
to BFT-4 (a)'s pieces that are invariant under constant gauges only — is consumed anywhere on the
live route. Trace at least: SMALLNESS_DAG edge 216 → eps_N5_unif; the RG induction's
effective-action form; CE-exp^k's (L-loc)_k; BFT34_55 §3.2 Finding F5. Outcome A: (a) suffices on
every consumer — then prove that, consumer by consumer, and stop. Outcome B: name at least one
consumer that needs local gauge invariance and say exactly which property it uses.

T1 (only under Outcome B). Construct (CovLift) on 𝒞_glob (a local, covariant-with-cocycle,
translation-commuting, frame-small, holomorphic map V ↦ Z^sm(V) from level-k fields to chains) and
prove its clauses (i)-(v) with k-, T-uniform constants; for each obvious candidate (covariant
multiscale interpolation of the level-k field; the composite critical point in a covariant gauge)
say whether it has the cocycle property and locality, and why.

T2 (only under Outcome B). Prove (Mult-Y), (Pair-loc), (I-id)_Z in the forms Theorem BB-gi_k
consumes, on the P_cc / Π_E family used by BFT4W55, and check the transfer from lane B's family.

T3 (only under Outcome B). Assemble BFT-4 (b) on 𝒞_glob as an implication with every input named
and its status.

**What would count as a refutation (of a claim I am testing or of my own target).**
- T0/Outcome A is refuted by one live consumer whose proof uses invariance under a NON-constant
  gauge transformation of the pieces (e.g. a step that gauge-fixes block by block, a step that
  compares a piece at two gauge-equivalent but not constant-gauge-equivalent fields, or a
  localization/extraction step that needs the piece to depend on gauge-invariant data only).
- T0/Outcome B is refuted by showing every such use can be routed through constant-gauge
  invariance plus a property (a) already delivers.
- A (CovLift) candidate is refuted by an explicit violation of the cocycle identity, of locality
  (dependence outside the stated neighbourhood), of translation commutation, of holomorphy on the
  stated domain, or of a k-/T-uniform bound (a constant that grows with k or with the torus size T).
- (Mult-Y)/(Pair-loc)/(I-id)_Z are refuted by an explicit field configuration in 𝒞_glob where the
  stated form fails, or by a mismatch between the form proved and the form BB-gi_k consumes.
- Any of my own conclusions is void if it rests on a statement that the Codex review of BFT4W55
  (CODEX_REVIEW_BFT4W.md, not on disk at start) refutes once it lands.

**Verdict vocabulary**: CONFIRMED / NOT-VERIFIED / REFUTED per REVIEW_BRIEF_55; PROVEN-HERE only
for steps I derive in this file.

---

## 1. Read record, Codex input, symbols pinned (appended after `date -u` printed 2026-10-29T04:11:27Z)

**Read (bounded ranges, located by string; no whole read of a large file).** REVIEW_BRIEF_55.md (all); queue/bft4b.md (all);
BFT4W55.md (all 878 lines, incl. §7 "Theorem BFT4a-glob", §5.2 "Proposition RWE" (Π_E inside every piece), §4.2 "Proposition
CORNER", §8 "What is not closed"); **CODEX_REVIEW_BFT4W.md (all 247 lines; complete — it ends with "Exactly what may be banked"
items 1-5 and the "Single most dangerous unverified input" paragraph; mtime 00:10 local = 04:10Z, read at ≈04:12Z, before any
derivation below)**; OFFGLOB55.md (all; only its PRE-STATED block exists; not used, not duplicated); PROOF.md l.1-40
("[S26-BANKED]" block), "L4. Small-field effective actions" (L4a-form, L4a-Π), "Lemma GT-lat (lattice Taylor lemma)",
"[R20-fix 12] (BG-unif), precise statement", "Proposition N5-sf_i (levels i ≥ 1)" ((NA-H_loc)_i), "Theorem NAH1 ((NA-H_loc) at
level 1"; SMALLNESS_DAG.md nodes BFT4, BFT012, eps_N5_unif, CEexp, eps1, eps_loc and every edge with BFT4 as head or tail
(edges 204-208, 216; 304-306); REVIEW_S22.md Part 5 ("Statement (BFT)", "Who needs which part"); BFT34_55.md §2.1-§2.7, §3.1-
§3.2 (Finding F5), §4; BFT_B.md "Corollary BB-4c (Cauchy consequences of BFT-4)" (i)-(v), "Failure mode B4-F1", "Session 2 does
not use BB-4-ind", §12.2 ((BB-gi)_k, (CovLift) (i)-(v), Lemma GI-frame, Lemma GI-pert, Construction BB-bond_k^cov, Theorem
GI-cov, Theorem BB-gi_k, Proposition GI-off, Corollary BFT4-poly^gi_k), §13.7-§13.10 status rows, l.2000-2010 ("REVIEW_S22
Part 5 / BFT-4", "SF.md (L-loc)_k"); BFT_A.md §1.1-§1.2 ("(C-glob) global small gauge class") and l.350-360 ("strict
subclass"); SF.md "Corollary CE-exp^k" with "[RSF2-fix CEk-1 + CEk-2" ((L-loc)_k); HIST.md §14.0-§14.3 ((I_k^E), (c1)-(c5)),
§20.3 (C) ((I_k^E)′, (b′) facts (1)-(4)), §25.6-§25.7 ((I_k^E)″); RLARGE.md "Thresholds [v3-T" ("N5 compatibility"), §7
(GT-lat′ use, "Each r_Y is gauge-invariant (CL (e))"); PLD.md "(SF-irr)_{k+1} (HYPOTHESIS"; HANDOFF.md (all); SESSION25_RESULTS
l.1781-1791; CODEX_REVIEW_BFT34.md (grep: R10, N7, "Exactly what may be banked"). Corpus (data only, cited by id + section,
nothing copied): Dimock 1502.02946 §5 "Polymer functions", Lemmas 15-16 (gauge invariance of E(X) used to move to a local gauge
on an enlarged cube, then a linear (complex) gauge removing the constant mode, to get the scaling improvement of small
polymers); 1512.04373 §4 "Polymers" (gauge invariance of the polymer norm used to reduce a sup over a gauge-saturated field
class to the potential-small class).

**Codex verdicts that bound what I may build on (CODEX_REVIEW_BFT4W, as on disk).** W9: Theorem BFT4a-glob is bankable only
as a **corrected conditional theorem** with (R)/F^σ and the zero-weight linear, projection, Ward and local analytic estimates
as named premises. W8: the all-torus prefactor 2e^{m_0}C_R is **REFUTED** for the small-torus fallback; the repaired k-, T-
uniform constant is C_all := max{2e^{m_0}C_R, e^{16m_0}C_{E2}(4R+14)⁴(C_0+1)C_0ε²} (+ C_∅). Item 5: "Do not bank … local gauge
invariance of the pieces, or extension off the global potential-small domain." **Everything below that uses BFT4a-glob uses it
in this corrected conditional form**, with polymer constant C_pol := C_all + C_∅ (k-, T-uniform). Nothing below uses W2's
refuted multilinear Lemma-LD sentence or W6's refuted coarse-site diameter formula.

**Symbols pinned (systemic defect 1).**
- **ε_gl** := BFT4a-glob's polydisc radius ε = ε_cc(s̄): a bound on the **potentials** B_c in one global gauge. 𝒫_ε := {B ∈
  (su(N)⊗ℂ)^{links} : max_c|B_c| ≤ ε} (BFT34_55 "(PD-glob)"). **ε_0** := BFT's **curvature** threshold (REVIEW_S22 "max_P|log
  V^r_{k,P}| ≤ ε ≤ ε_0"). **ε_1** := RLARGE's plaquette cut (SMALLNESS_DAG node eps1: "χ_Q := Π_{p⊂int Q}1{||1 - U(p)||_op <
  ε_1}") — also a curvature quantity. These three are different objects and are never compared below without units.
- **α_bg** := the background size in (NA-H_loc)_i (a potential bound in some gauge), not a Hölder exponent.
- **m** := the decay rate of N5's N_m norm; **m_0** := the polymer rate of BFT-4. **M_c** := cube side.
- **R(X)** := a polymer activity; **R_k** := E_k^br − S_W; **R̄(X)** := the gauge average defined in §3. (BFT4W55's box side R
  appears only through C_all.)
- **𝒢** := SU(N)^{sites} (real level-k gauge group) acting by (V^g)_b := g_x V_b g_y^{-1}, b = (x, y).
- **(a), (b), (c)** := BFT34_55 §2.6 / §4's split of BFT-4: (a) bounded constant-gauge-invariant polymers on 𝒞_glob; (b) the
  same with locally gauge-invariant pieces, i.e. lane B's (BB-gi)_k ("every polymer R(X) … is a locally gauge-invariant
  function of V: R(X)(V^h) = R(X)(V) for every level-k gauge h (on the class where the construction is defined)"); (c) BFT's
  class off 𝒞_glob. **(c₀)** := (c) **without** any invariance clause: a representation E_k^br = S_W + c + Σ_X R(X) on BFT's
  class 𝒦_BFT (below), with R(X) holomorphic and bounded on 𝒦_BFT restricted to its support, local, *-connected, with a k-, T-
  uniform polymer norm.
- **𝒞_glob** (BFT_A "(C-glob) global small gauge class 𝒞_glob(ε): real V_k = e^{B_k} with ||B_k||_D … ≤ ε in one global
  gauge"): as a set of gauge classes this is the gauge saturation Sat(𝒫_ε) := {(e^B)^h : B ∈ 𝒫_ε, h ∈ 𝒢}; every construction on
  file (BFT4a-glob included) works in the fixed chart B ∈ 𝒫_ε. **𝒦_BFT** := BFT's data class {e^zV^r : V^r real, max_P|log V^r_P|
  ≤ ε_0, |z|_∞ ≤ r_ℂε_0} (REVIEW_S22 "Statement (BFT)"; = BFT34_55's (PD-curv) globally). BFT_A l.355: "𝒞_glob(ε) is a **strict
  subclass** of BFT's data class".

---

## 2. T0 — is BFT-4 (b) consumed? The trace (appended after `date -u` printed 2026-10-29T04:12:58Z)

### 2.1 How the inventory was built
Every consumer of BFT-4 I could find by: (i) SMALLNESS_DAG — all edges with BFT4 as tail or head (only **216. BFT4 →
eps_N5_unif [req]** leaves BFT4; 204-208 enter it); (ii) REVIEW_S22 Part 5 "Who needs which part"; (iii) the re-pointings in
PROOF ("[R22-fix S22-9: re-pointed … (iv) ⇐ BFT-4 (by Cauchy)") and RLARGE ("(iv) ⇐ BFT-4 (PROOF l.6631)"); (iv) BFT34_55 §3.2
Finding F5; (v) grep of SF, HIST, RLARGE, PLD, HW, FLOW, SQ and EXISTENCE for "BFT-4", "BFT4", "gauge invariant", "gauge-
invariant", "locally gauge", "(L-loc)", "(I_k^E)", "(SF-irr)", "effective action". The inventory is complete **relative to these
searches**; a consumer stated without any of these strings would be missed (named as a limit in §9).

### 2.2 The consumers, the class each quantifies over, and what each uses

| # | Consumer (locating string) | Class of backgrounds it quantifies over | BFT-4 property it uses | Invariance of a **piece** under a non-constant gauge used? |
|---|---|---|---|---|
| K1 | **eps_N5_unif** (DAG node "level-uniform N5 background threshold"; edge 216; BFT34_55 F5: "The BFT-4 content it uses is (i) + (v)") — via BFT_B Corollary BB-4c (i) (C_♭^{(i)} level-uniform) and (v) ((NA-H_loc)_i, N5-sf_i's constants) | the ε_1-small (curvature) domain: RLARGE "N5 compatibility … ε_1, ε_loc, ε^J_loc ≤ the N5 background threshold (matching units)", ε_1 a plaquette cut; (NA-H_loc)_i's 𝔑_i(α) / Theorem NAH1's "curvature class 𝔅_1(ε)" — **gauge invariant**, strictly larger than 𝒞_glob | (i): Cauchy bounds on third derivatives; (v): "for every □ … there is a level-1 gauge g_□ … with N_m(\|(R_{g_□}Õ_1R_{g_□}^{-1} − Õ_1(1,1))_{Ω_□}\|) ≤ δ_H" — Hessian closeness after **some** box gauge | **No** (§4.4, §5.2): (v) evaluates the representation at the transformed field g_□U; it needs the identity there, not invariance of a piece |
| K2 | **(BG-unif) (iv)** (PROOF "[R20-fix 12] (BG-unif), precise statement": "(iv) the N_0-Lipschitz constants of Hess E_j^br in the chart at the lift are ≤ C_BG"; "(iv) ⇐ BFT-4 (by Cauchy)") | "every level-k field V_k … whose own-units plaquette logs and level-(k+1) soft fluctuations are ≤ ε" — curvature, **gauge invariant** | Cauchy (third derivatives) in a chart | **No** |
| K3 | **CE-exp^k's (L-loc)_k**, classical part (SF "[RSF2-fix CEk-1 + CEk-2": "𝓔_{k,x} = Σ_{R∋x}𝓔_{x,R}, with 𝓔_{x,R} depending on A on R only, holomorphic and ≤ S_ke^{-κ_Ld(R)} on the UNIFORM polydisc max_{b∈R}\|A_b\| < ρ_k"; BFT34_55 F5 "Live consumer 2") | the stage-k backgrounds: the ε_1 small-field region (curvature cut) — **gauge invariant** | strictly local holomorphic pieces, bounded on a uniform polydisc in the fluctuation A | **No** — the statement has **no** invariance clause |
| K4 | **The RG induction's effective-action form**: HIST "(I_k^E)″ (restated hypothesis)": main term u_k𝓔^{an}_k (the whole classical branch action); polymers "(b″) … holomorphic on 𝔇_{2ε_1,α_E}(X)"; HIST (c3): "the β = 0 tree part must stay in the main term, not in a per-cube-bounded polymer"; (c4): the coupling-shift polymer δβ(Σs − 𝓔_k) | 𝔇_{2ε_1,α_E}(X): HIST §20.3 (b′) fact (2) "gauge covariant" — **gauge invariant** | BFT-4 enters only through the main term's localisation ((a″) = K3; (a3-q)'s per-cube bound C_𝓔) and (c4)'s per-cube bound; (I_k^E)(b) lists "gauge invariant" for the polymers of the class | Only through (b″)'s "gauge invariant", **on a gauge-invariant domain** — supplied by Lemma AVG (§3) |
| K5 (not live) | BB-4c (iii) ((H-G) level-uniform) and (ii)'s flat-point clause ("On contractible X a flat field is gauge-trivial on X, so the same argument applies at every flat point") | BFT-2 polydisc in curvature form | ∇R(X) = 0 at flat points | **Yes** — but (iii) is off the live route: REVIEW_S22 "NAH-unif′, HG-ind's uniform form and (H-K) all become unnecessary"; F5 "Not consumed on the live route … the uniform form of (H-G)" |
| K6 (not live) | a per-level induction for R_k: BB-4-ind, the optional strengthening ‖R_{k+1} − R_k‖_𝒜 ≤ C_0λ^k, a Loc-extraction of R_k (BFT_B "Failure mode B4-F1 … the per-level induction must run in a stronger norm with a Loc-extraction") | per-level polydiscs | Dimock-type contraction of small polymers, which uses gauge invariance of E(X) to pass to a local gauge and then a linear gauge removing the constant mode (1502.02946 §5, Lemmas 15-16) | **Yes** — but off the live route: BFT_B "**Session 2 does not use BB-4-ind**"; REVIEW_S22 "Anti-circularity … one contraction for 𝔉_k"; BFT4W55 §8 item 7 "not addressed"; the composite route recomputes E_k^br at every k (HIST (c5″) "(c5) holds with critical values") |
| — | Not BFT-4 consumers (checked, excluded): RLARGE §7's GT-lat′ ("Each r_Y is gauge-invariant (CL (e))" — returned large-field clusters); PLD "(SF-irr)_{k+1}" (activities "bounded by K elsewhere in the cut-good domain" — returned/fluctuation activities, on a gauge-invariant domain); PROOF L4a-Π (transversality from gauge invariance of the **total** quadratic form, "(G) holds when Π is the Hessian at 0 of a gauge-invariant functional"); BB-4c (iv) (BFT-3's E-part at all orders — no live consumer beyond BFT-3 at n ≤ 4, F5; and it is a pure Cauchy consequence) | | | |

### 2.3 The result, stated (proofs: §3-§5)

> **Theorem T0 (BFT-4 (b) on 𝒞_glob has no consumer on the live route).**
> **(1) On 𝒞_glob.** For each live consumer K1-K4, its statement restricted to backgrounds in 𝒞_glob, read in the global chart
> B ∈ 𝒫_{ε_gl}, follows from the conclusions of Theorem BFT4a-glob (corrected conditional form, constant C_pol) by Cauchy
> estimates on 𝒫_{ε_gl}, locality, and constant-gauge invariance; **no step applies a non-constant gauge transformation to a
> piece** (Proposition GLOB, §4).
> **(2) Off 𝒞_glob.** Each live consumer quantifies over a **gauge-invariant** class strictly containing 𝒞_glob, and what it
> needs there is (c₀). By **Lemma AVG** (§3), (c₀) implies (c₀) with **locally gauge-invariant** pieces and the **same**
> constants; restricted to 𝒫_{ε′} ⊂ 𝒦_BFT this is (b) on 𝒞_glob (Proposition CURV, §5).
> **(3)** (b) on 𝒞_glob does **not** imply (c₀) (§5.3).
> **(4) Hence** wherever (a) does not suffice, the missing input is (c₀); (c₀) supplies (b), and (b) does not supply (c₀). BFT-4
> (b) on 𝒞_glob — and with it (CovLift), (Mult-Y), (Pair-loc), (I-id)_Z **as inputs on 𝒞_glob** — has no consumer. The only steps
> in the inventory that use invariance of a piece under a non-constant gauge are the two non-live ones, K5 and K6.
> **Status: PROVEN-HERE** — (1) as an implication of BFT4a-glob's conclusions; (2) unconditionally as a lemma about polymer
> representations (with hypothesis (H-inv), §3); the consumer list is complete relative to §2.1's searches.

This is the brief's stop condition in substance ("If (a) suffices everywhere on the live route, prove that and stop there"), with
one sharpening the brief did not anticipate: (a) does **not** suffice off 𝒞_glob, but what is missing there is (c₀), which makes
(b) automatic. So no (CovLift) construction is attempted in this file (brief step 1 is not reached).

---

## 3. Lemma AVG — on a gauge-invariant domain, local gauge invariance of the pieces is free (appended after `date -u` printed 2026-10-29T04:16:45Z)

**Setting.** A finite level-k lattice (torus or box) with oriented links b = (x, y); complexified link variables V_b ∈ SL(N, ℂ);
the real gauge group 𝒢 := SU(N)^{sites} acting by (V^g)_b := g_xV_bg_y^{-1} (complex-linear in each V_b). For a finite set of
links Ω, S(Ω) := the set of endpoints of its links, and SU(N)^{S(Ω)} acts on SL(N, ℂ)^Ω by the same formula.

> **Lemma AVG.** Let 𝒦 ⊂ SL(N, ℂ)^{links} be **open and 𝒢-invariant** (V ∈ 𝒦, g ∈ 𝒢 ⇒ V^g ∈ 𝒦). Let 𝔛 be a finite index set of
> polymers, Ω(X) a finite set of links (the support of X), 𝒦(X) := {V|_{Ω(X)} : V ∈ 𝒦}. Assume
> - **(H-inv)** E, S : 𝒦 → ℂ satisfy E(V^g) = E(V), S(V^g) = S(V) for all V ∈ 𝒦, g ∈ 𝒢;
> - R(X) : 𝒦(X) → ℂ is holomorphic with ‖R(X)‖ := sup_{𝒦(X)}|R(X)| < ∞, for every X ∈ 𝔛;
> - **E(V) = S(V) + c + Σ_{X∈𝔛} R(X)(V|_{Ω(X)})** for every V ∈ 𝒦 (c a constant).
>
> Put **R̄(X)(W) := ∫_{SU(N)^{S(Ω(X))}} R(X)(W^h) dh** (normalised Haar measure), W ∈ 𝒦(X). Then:
> - **(a)** R̄(X) is well defined, holomorphic on 𝒦(X), depends on V only through V|_{Ω(X)}, ‖R̄(X)‖ ≤ ‖R(X)‖, and R̄(X) is real
>   at real points where R(X) is;
> - **(b)** R̄(X)(V^g|_{Ω(X)}) = R̄(X)(V|_{Ω(X)}) for **every** g ∈ 𝒢 — every piece is locally gauge invariant in the sense of
>   lane B's (BB-gi)_k;
> - **(c)** E(V) = S(V) + c + Σ_X R̄(X)(V|_{Ω(X)}) for every V ∈ 𝒦 — the same identity, with the same constant;
> - **(d)** R̄(X) ≡ 0 whenever R(X) ≡ 0 (so "zero unless X is *-connected" survives), and every polymer norm of the form
>   sup_{Q_0}Σ_{X∋Q_0}‖R(X)‖w(X) (w ≥ 0) is not increased: **all constants, hence k- and T-uniformity, transfer unchanged**;
> - **(e)** if a lattice symmetry τ (translation, partition-preserving translation, hypercubic element) maps polymers to polymers
>   with Ω(τX) = τΩ(X) and R(τX)(τW) = R(X)(W), then R̄(τX)(τW) = R̄(X)(W);
> - **(f)** (complex gauges) if λ : S(Ω(X)) → su(N), W ∈ 𝒦(X), and W^{exp(ζλ)} ∈ 𝒦(X) for all ζ in a connected open D ⊂ ℂ with
>   D ∩ ℝ ⊃ an interval containing 0, then R̄(X)(W^{exp(ζλ)}) = R̄(X)(W) for all ζ ∈ D.

*Proof.* **(a)** Let W = V|_{Ω(X)}, V ∈ 𝒦, and h ∈ SU(N)^{S(Ω(X))}; extend h to g ∈ 𝒢 by g := 1 off S(Ω(X)). Then V^g ∈ 𝒦 and
(V^g)|_{Ω(X)} = W^h, because both endpoints of each link of Ω(X) lie in S(Ω(X)); so W^h ∈ 𝒦(X) and the integrand is defined.
𝒦(X) is open (the image of the open 𝒦 under a coordinate projection). The map (W, h) ↦ R(X)(W^h) is jointly continuous and
holomorphic in W for fixed h (W ↦ W^h is complex-linear in each link), and bounded by ‖R(X)‖. In local holomorphic coordinates
about any W_0 ∈ 𝒦(X) (e.g. W = W_0e^w, w ∈ sl(N, ℂ)^{Ω(X)} small), the integral is continuous (dominated convergence) and
holomorphic in each coordinate separately (Fubini + Morera: ∮∫ = ∫∮ = 0), hence holomorphic (Osgood). |R̄(X)(W)| ≤ ∫|R(X)(W^h)|dh
≤ ‖R(X)‖ since every W^h ∈ 𝒦(X). For real W, every W^h is real, so R̄(X)(W) is real when R(X) is real on real points.
**(b)** For h′ ∈ SU(N)^{S(Ω(X))}: ((W^{h′})^h)_b = h_xh′_xW_bh′^{-1}_yh^{-1}_y = (W^{hh′})_b, so R̄(X)(W^{h′}) = ∫R(X)(W^{hh′})dh =
∫R(X)(W^{h″})dh″ = R̄(X)(W) by right invariance of Haar measure on the compact group SU(N)^{S(Ω(X))}. For g ∈ 𝒢,
(V^g)|_{Ω(X)} = (V|_{Ω(X)})^{g|S(Ω(X))}.
**(c)** Let μ be the normalised Haar measure on 𝒢. For V ∈ 𝒦 and each X, g ↦ R(X)((V^g)|_{Ω(X)}) depends on g only through
g|_{S(Ω(X))}, and the push-forward of μ under g ↦ g|_{S(Ω(X))} is the normalised Haar measure of SU(N)^{S(Ω(X))} (a marginal of
a product of Haar measures). So ∫_𝒢 R(X)((V^g)|_{Ω(X)})dμ(g) = R̄(X)(V|_{Ω(X)}). Integrate the identity at V^g ∈ 𝒦 over g
(a finite sum of bounded continuous functions): Σ_X R̄(X)(V|_{Ω(X)}) = ∫[E(V^g) − S(V^g) − c]dμ(g) = E(V) − S(V) − c by (H-inv).
**(d)** Immediate from the definition and (a).
**(e)** τ acts on configurations by (τV)_{τb} = V_b (with V_b ↦ V_b^{-1} on links whose orientation τ reverses) and on gauges by
(τg)_{τx} = g_x; then (τW)^{τh} = τ(W^h) (for a reversed link (g_xV_bg_y^{-1})^{-1} = g_yV_b^{-1}g_x^{-1}, consistent). The
substitution h = τh′ is a Haar-preserving bijection SU(N)^{S(Ω(X))} → SU(N)^{S(Ω(τX))}, so R̄(τX)(τW) = ∫R(τX)(τ(W^{h′}))dh′ =
∫R(X)(W^{h′})dh′ = R̄(X)(W).
**(f)** ζ ↦ R̄(X)(W^{exp(ζλ)}) is holomorphic on D (composition of holomorphic maps) and, by (b), equals R̄(X)(W) on the real
interval in D ∩ ℝ (real ζ gives a real gauge); by the identity theorem it is constant on the connected D. ∎

**Remarks.**
1. *What AVG needs and what it does not.* It needs the pieces to be **defined and bounded on the whole gauge orbit** of every
   configuration they are evaluated at — i.e. on a gauge-invariant domain. It does **not** need any covariance of the
   construction that produced them (no cocycle, no covariant background, no frame transplant). It does not change E, S or c.
2. *Why it does not apply to Theorem BFT4a-glob's representation.* That representation lives on the chart 𝒫_{ε_gl}, which is
   **not** 𝒢-invariant: a gauge h with large variation takes e^B out of 𝒫_{ε_gl}, where R(X) is undefined. Constant gauges do
   preserve 𝒫_{ε_gl} (B ↦ Ad_gB), and averaging over them changes nothing (the pieces are already constant-gauge invariant). The
   pieces' smallness is a chart artefact: at the flat configuration of CODEX_REVIEW_BFT4W W8 (B_c = t·diag(i, −i) on
   direction-1 links) E_k^br = 0 while E_∅ ≥ κ_−T⁴ε²/6, so the non-invariant single-link part of (a)'s representation is
   compensated by the other pieces, not small at that flat point.
3. *The gauge saturation of 𝒞_glob.* Sat_ℂ(𝒫_ε) := {(e^B)^g : B ∈ int 𝒫_ε, g ∈ 𝒢} is open and 𝒢-invariant, so AVG applies on it:
   **(b) on 𝒞_glob is equivalent to "bounded local holomorphic pieces on Sat_ℂ(𝒫_ε)"** (⇐ by AVG; ⇒ because locally invariant
   chart pieces extend to Sat_ℂ(𝒫_ε) by R(X)(V) := R(X)(B) for any chart point B gauge-equivalent to V on S(Ω(X))). What (a)
   lacks for this is **locality on the saturation**: transporting a chart piece to (e^B)^g requires undoing g, and a choice of g
   as a function of V is a global gauge fixing, non-local in V. That locality — not invariance as such — is the content of (b).
4. *(H-inv) for E_k^br.* On 𝒦_BFT it is part of what BFT-0 off 𝒞_glob must deliver (a critical value of the gauge-invariant
   𝔉_k, unique modulo composite gauges in a covariantly defined ball); OFFGLOB55's scope. On the chart 𝒫_{ε_gl} the path form
   is Lemma ENV (§6).

---

## 4. Proposition GLOB — on 𝒞_glob, (a) serves every live consumer (appended after `date -u` printed 2026-10-29T04:17:32Z)

**Input (the corrected conditional form of Theorem BFT4a-glob; CODEX_REVIEW_BFT4W W8-W9).** At every level j ≥ 1 (j plays BFT4W55's
k), every coarse torus side T ≥ 3, every complex B ∈ 𝒫 := 𝒫_{ε_gl} in the global chart:
E_j^br(B) = S_W(e^B) + Σ_X R(X)(B), where the one-cube polymers also carry the single-plaquette and single-link terms of
E_∅ − S_W; each R(X) is holomorphic on int 𝒫, depends on B only through Ω(X) := the level-j links of X^{(5)} ⊂ X^+ (M_c ≥ 5),
vanishes unless X is *-connected, is invariant under constant gauges B ↦ Ad_gB; and
**sup_{Q_0}Σ_{X∋Q_0}sup_𝒫|R(X)|e^{m_0|X|} ≤ C_pol** (C_pol := C_all + C_∅ of Codex W8; k-, T-uniform). Coordinates:
B_b = Σ_a w_{b,a}T_a with (T_a) an HS-orthonormal basis of su(N), n_c := N² − 1, so |B_b| = (Σ_a|w_{b,a}|²)^{1/2}; n_Q := 4M_c⁴
(links per cube); ν(X) := n_c·#Ω(X) ≤ 81n_cn_Q|X| (|X^+| ≤ 3⁴|X|). Distances are level-j coarse ℓ^∞ distances; for b, b′ ∈ Ω(X),
d(b, b′) ≤ M_c(|X| + 2) (a *-connected set of |X| cubes has ℓ^∞ extent ≤ M_c|X|; X^+ adds 2M_c).

**(G0) Cauchy on the chart.** If B_0 ∈ 𝒫 is real with ‖B_0‖_D ≤ (1 − θ)ε_gl (0 < θ ≤ 1) and r_θ := θε_gl/√n_c, the coordinate
polydisc {|w_{b,a} − w_{0,b,a}| < r_θ ∀(b, a)} lies in int 𝒫 (|B_b| < (1 − θ)ε_gl + √n_c·r_θ = ε_gl). Hence for every multi-index
α, |∂^αR(X)(B_0)| ≤ α!·r_θ^{−|α|}·sup_𝒫|R(X)|. ∎

**(G1) BB-4c (i) on 𝒞_glob (consumer K1; and K2's Lipschitz constant).** For real B_0, ‖B_0‖_D ≤ ε_gl/2, every (b, a):
  Σ_{(b′,a′),(b″,a″)}|∂_{b,a}∂_{b′,a′}∂_{b″,a″}(E_j^br − S_W)(B_0)| ≤ Σ_{X:b∈Ω(X)}ν(X)²·3!·r_{1/2}^{−3}sup_𝒫|R(X)|
    ≤ **6·81³(n_cn_Q)²(2/(em_0))²(2√n_c/ε_gl)³·C_pol =: C_♭^{gl}**,
using: only X with b ∈ Ω(X) contribute; such X contain a cube of the 81-cube neighbourhood of b's cube; ν(X)² ≤ (81n_cn_Q)²|X|² and
|X|²e^{−m_0|X|} ≤ (2/(em_0))². C_♭^{gl} is k-, T-uniform. This is BB-4c (i) with ρ_c → ε_gl/2 in the global chart. The second-
and first-order sums are bounded the same way (factors 2!·r^{−2}·ν(X), r^{−1}), so third derivatives in the left-trivialised
chart (combinations of chart derivatives of orders 1-3 with the bounded dexp coefficients for |B_b| ≤ ε_gl ≤ 1) obey a k-, T-
uniform bound as well. **No gauge transformation is used.**

**(G2) BB-4c (ii) at the trivial field.** ∂_B R(X)(0) = 0 for every X (including the E_∅ − S_W singletons), hence
∇_B(E_j^br − S_W)(0) = 0. *Proof.* Constant g acts linearly, e^{Ad_gB} = ge^Bg^{-1}, and R(X)(Ad_gB) = R(X)(B). Differentiating at
B = 0, the complex-linear functional ℓ_b := ∂_{B_b}R(X)(0) on su(N)⊗ℂ satisfies ℓ_b∘Ad_g = ℓ_b. Its real and imaginary parts
restricted to su(N) are Ad-invariant real functionals, i.e. ⟨w, ·⟩_HS with Ad_gw = w for all g; w is central, and su(N) has
trivial centre (N ≥ 2); so ℓ_b = 0 on su(N), hence on su(N)⊗ℂ. (The singletons κφ̂_c(e^{B_c}; 1) and the plaquette terms are
Ad-invariant functions of their links.) ∎ **Only constant gauges are used.** (BB-4c (ii)'s *flat-point* clause — the one that
needs non-constant gauges — feeds only (iii), which is not on the live route: K5.)

**(G3) BB-4c (iv) (E-part of BFT-3, every order).** Cauchy in distinct variables on the polydisc of (G0), exactly as BB-4c (iv)
in Codex BFT34 R10's repaired form (attachment −3n/2, prefactor 81e^{3m_0n/4}, rate m_0/(8M_c)), with ρ_c → ε_gl/2. Not a gauge
question; constants not re-derived here (BFT4W55 §7 states the same use).

**(G4) BB-4c (v) / (NA-H_loc)_j's BFT-4 part on 𝒞_glob (consumer K1).** For real B_0 with ‖B_0‖_D ≤ α_bg ≤ ε_gl/4, and
0 ≤ m ≤ m_0/(2M_c):
  **N_m(|Hess_B(E_j^br − S_W)(B_0) − Hess_B(E_j^br − S_W)(0)|) ≤ C_H·α_bg,
  C_H := 6·81³(n_cn_Q)²(4/(em_0))²e^{m_0}(4√n_c/(3ε_gl))³·C_pol** (k-, T-uniform),
with N_m(K) := sup_xΣ_yK(x, y)e^{md(x,y)} (PROOF "N_m(K) := sup_xΣ_yK(x, y)e^{md(x,y)}"), applied to the entrywise modulus.
*Proof.* Hess R(X)(B_0) − Hess R(X)(0) = ∫_0^1 D³R(X)(tB_0)[B_0, ·, ·]dt. For |tB_0| ≤ ε_gl/4 use (G0) with θ = 3/4:
|∂³R(X)(tB_0)| ≤ 6r_{3/4}^{−3}sup|R(X)|, and |w_{0,b″,a″}| ≤ |B_{0,b″}| ≤ α_bg, so each entry indexed by (b, a), (b′, a′) ∈ Ω(X) is
≤ ν(X)α_bg·6r_{3/4}^{−3}sup|R(X)|. The weighted row sum at (b, a) is ≤ Σ_{X:b∈Ω(X)}ν(X)²α_bg·6r_{3/4}^{−3}sup|R(X)|e^{mM_c(|X|+2)};
with mM_c ≤ m_0/2, e^{mM_c(|X|+2)} ≤ e^{m_0}e^{(m_0/2)|X|}, and |X|²e^{−(m_0/2)|X|} ≤ (4/(em_0))²; sum over the 81 neighbouring
anchors. ∎ **Relation to (NA-H_loc).** Membership in 𝔑(α) is "for every □ … **there is** a real gauge g_□ on Ω^+_□ with
|log(g_□U)_e| … ≤ α" (PROOF "*Background classes.* 𝔑(α)"), and Theorem NAH1 (b) proves "for every … box □ **there is** a level-1
gauge g_□ … with N_m(…) ≤ δ_H^{(1)}". For a background in 𝒫_{α_bg} in the global chart, **g_□ := 1** witnesses membership on
every box, and (G4) is the BFT-4 contribution to δ_H with that witness: δ_H^{BFT-4} ≤ C_Hα_bg → 0 as α_bg → 0, k-uniformly. The
other parts of Õ_j (soft term, slice, residual — Setting N5-bg) are not BFT-4 content. **No gauge transformation is applied.**
At level j < k of a level-k problem on 𝒞_glob, the tower component U_j = e^{x_j(B)} lies in level-j's chart with own-unit size
≤ L^{−(k−j)}C_0ε (BFT_A "U_j is in 𝒞_glob(ε_j) with ε_j = |x_j|_∞ own ≤ L^{-(k-j)}C_0ε (same gauge)"), so (G4) applies with
α_bg = L^{−(k−j)}C_0ε_gl. (Which per-level object N5 needs at level j — E_j^br of the composite level-j problem vs the per-level
tower — is the (NSL) identification, NOT-VERIFIED, and is independent of gauge invariance of pieces.)

**(G5) (BG-unif) (iv) on 𝒞_glob (consumer K2).** For real B_1, B_2 ∈ 𝒫_{ε_gl/4}: N_0(|Hess(E_j^br − S_W)(B_1) − Hess(E_j^br −
S_W)(B_2)|) ≤ C_H‖B_1 − B_2‖_D (the proof of (G4) along the segment from B_2 to B_1, which stays in 𝒫_{ε_gl/4}). The chart is the
global B-chart (BFT_A: the lift chart of COMP "fails in every norm BFT allows"; BFT re-pointed (BG-unif) to its own chart).
**No gauge transformation is used.**

**(G6) (L-loc)_k classical part on 𝒞_glob (consumer K3; = BFT34_55 §3.1 last bullet, BFT_B Corollary BB-Lloc_k).** Fix a real
background B_0 with ‖B_0‖_D ≤ ε_gl/2 and let the stage-k fluctuation A act by e^{A_b}e^{B_{0,b}} = e^{β(A_b,B_{0,b})} (β = BCH,
link by link). For |A_b| < ρ := ε_gl/4 and ε_gl ≤ 2/C_BCH (C_BCH: |β(X, Y) − X − Y| ≤ C_BCH|X||Y| for |X|, |Y| ≤ 1),
|β| < ε_gl/4 + ε_gl/2 + C_BCHε_gl²/8 ≤ ε_gl, so β(A, B_0) ∈ int 𝒫. Put 𝓔_{x,X}(A) := R(X)(β(A, B_0))/|X| for every cube x ∈ X
(plus the strictly local Wilson densities). Each 𝓔_{x,X} depends on A only on Ω(X), is holomorphic on the **uniform** polydisc
max_b|A_b| < ρ, and Σ_{X∋x}sup|𝓔_{x,X}|e^{m_0|X|} ≤ C_pol, with e^{−m_0|X|} ≤ e^{−(m_0/M_c)(diam_∞X − 2M_c)}: (L-loc)_k's form with
κ_L ≍ m_0/M_c (in the cube-unit reading of SF's d(R); the rate remark of BFT_B [RBB3-fix] stands). (L-loc)_k has **no** gauge-
invariance clause, and **no gauge transformation is used**.

**(G7) The induction's per-cube uses on 𝒞_glob (consumer K4, restricted to the chart).** (a3-q)'s per-cube bound on the main-term
density and (c4)'s coupling-shift polymer δβ(Σs − 𝓔_k) need sup_xΣ_{X∋x}sup|R(X)|/|X| ≤ C_pol, i.e. per-cube boundedness of the
localised R_j: given by the input. **No gauge transformation is used.**

> **Proposition GLOB.** (G1)-(G7) hold, for every level j ≥ 1 and every T ≥ 3, with k-, T-uniform constants, as implications of
> the corrected conditional Theorem BFT4a-glob; their proofs use holomorphy and sup bounds on the chart 𝒫_{ε_gl}, locality
> (Ω(X) ⊂ X^+) and, in (G2) only, invariance under **constant** gauges. **Status: PROVEN-HERE as an implication** (inherits
> BFT4a-glob's premises: (R)/F^σ and the zero-weight linear, projection, Ward and local analytic estimates, Codex BFT4W W9).
> Consequently, on 𝒞_glob, every live consumer K1-K4 is served by (a); the invariance clause of (b) is used by none of them.

*Scope caveat (stated so that it cannot be over-read).* GLOB serves the consumers **at 𝒞_glob backgrounds read in the global
chart**. It says nothing about backgrounds outside 𝒞_glob (§5), and it does not cover a hypothetical re-scoping of the
induction's polymer class (b″) from its gauge-covariant domain 𝔇 to the chart 𝒫_{ε_gl}: a piecewise per-level contraction on a
potential chart would use invariance of pieces in Dimock's way (K6's mechanism; 1502.02946 §5 Lemmas 15-16). The live
(I_k^E)″ is not of that form (HIST §25.6 "(b″) Polymers E_k(X; ·) holomorphic on 𝔇_{2ε_1,α_E}(X)").

---

## 5. Proposition CURV — off 𝒞_glob the consumers need (c₀), and (c₀) supplies (b) (appended after `date -u` printed 2026-10-29T04:18:42Z)

### 5.1 Every live consumer's class is gauge invariant (and strictly larger than 𝒞_glob)
- **𝒦_BFT** = {e^zV^r : V^r real, max_P|log V^r_P| ≤ ε_0, |z|_∞ ≤ r_ℂε_0} (also BB-4c's "BFT-2's polydisc: every e^zV^r with V^r real
  of curvature ≤ ε_0 and |z_c| ≤ ρ_c", and (BG-unif)'s class): (e^{z_b}V^r_b)^g = g_xe^{z_b}V^r_bg_y^{-1} = e^{Ad_{g_x}z_b}·(V^r)^g_b,
  |Ad_{g_x}z_b|_HS = |z_b|_HS, and the plaquettes of (V^r)^g are conjugates of those of V^r. Its interior (strict inequalities) is
  open in SL(N, ℂ)^{links} (image of an open set under the submersion (V^r, z) ↦ e^zV^r near z = 0) and 𝒢-invariant.
- **𝔇_{2ε_1,α_E}(X)** of (I_k^E)″: (V_be^{H_b})^g = (V^g)_be^{Ad_{g_y}H_b} — HIST §20.3 (b′) fact (2) "(2) gauge covariant".
- **𝔑_i(α)** of (NA-H_loc)_i: if g_□ witnesses (U, V) on □, then g_□h^{-1} witnesses (U, V)^h.
- **The ε_1 cut** χ_Q (plaquette condition) and the cut-good domain of (SF-irr): conditions on plaquettes, invariant.
All strictly contain 𝒞_glob and even Sat(𝒞_glob): BFT_A "𝒞_glob(ε) is a **strict subclass** of BFT's data class … flux sectors
(εT² ≳ 2π) admit no small global gauge"; and on single polymers HIST "[GAP S2-2] a single-gauge polydisc on X does NOT contain
the ε_1-domain when X contains an m × m square with m > 4α_E/ε_1 (Stokes …)".

### 5.2 What each consumer needs there: (c₀), not (b)
- **K1 (N5).** (v)'s proof evaluates the representation at the box-gauged field g_□U (near polymers by Cauchy at a point within
  α_bg of the identity, far polymers by sup bounds and the e^{−m_0|X|} tails): this needs E_j^br = S_W + c + ΣR(X) **at g_□U** and
  sup bounds of the pieces on the class — (c₀). It never compares R(X)(U) with R(X)(g_□U). (i) is Cauchy at a point of the class
  in left-trivialised coordinates (HIST (b′) fact (4): the polydisc {(U_be^{w_bY_b}) : |w_b| ≤ r} lies in the domain) — (c₀).
- **K2 ((BG-unif) (iv)).** Cauchy at points of the class — (c₀).
- **K3 ((L-loc)_k).** Pieces evaluated at e^AU, U anywhere in the ε_1 small-field region — (c₀); no invariance clause.
- **K4 ((I_k^E)″).** Polymers holomorphic and bounded on 𝔇 — (c₀)-type data; the clause "gauge invariant" of (I_k^E)(b) is then
  supplied by Lemma AVG (𝔇 is 𝒢-invariant), with the same bounds; Dimock-type uses of invariance under real and complex gauges
  (1502.02946 §5 Lemmas 15-16; 1512.04373 §4) are covered by AVG (b), (f).
So off 𝒞_glob each consumer needs (c₀) (with (H-inv) for E_j^br, i.e. BFT-0 off 𝒞_glob), and by Lemma AVG its pieces may be taken
locally gauge invariant **at no cost in any constant**.

### 5.3 (c₀) ⇒ (b) on 𝒞_glob; (b) on 𝒞_glob ⇏ (c₀)
**(⇒).** *Chart containment.* For complex B with |B_b| ≤ ε′: e^{B_b} = e^{z_b}V^r_b with V^r_b := e^{Re B_b} ∈ SU(N) (Re w.r.t.
su(N)⊗ℂ = su(N) ⊕ i·su(N)) and z_b := log(e^{B_b}e^{−Re B_b}) = i·Im B_b + O(|B_b|²), so |z_b| ≤ ε′(1 + C_BCHε′); the plaquettes of
V^r have |log| ≤ 4ε′(1 + C′ε′). Hence **int 𝒫_{ε′} ⊂ int 𝒦_BFT whenever 4ε′(1 + C′ε′) < ε_0 and ε′(1 + C_BCHε′) < r_ℂε_0** (this is
BFT34_55 §2.1's "(PD-glob) ⊂ (PD-curv) after the B4N-1 adjustment", re-derived). Apply Lemma AVG on int 𝒦_BFT (open, 𝒢-
invariant) to a (c₀) representation and restrict the averaged pieces to int 𝒫_{ε′}: E_j^br = S_W + c + ΣR̄(X) there, with R̄(X)
holomorphic, local (Ω(X)), *-connected, bounded by the same polymer norm, and **R̄(X)(V^h) = R̄(X)(V) for every real level-j gauge
h** — (b) on 𝒞_glob(ε′), provided the two definitions of E_j^br (chart and class) agree on 𝒞_glob, which any (c₀) extending BFT
on 𝒞_glob must ensure. ∎
**(⇏).** (i) (b) is a statement on the chart (or its gauge saturation, Remark 3 of §3); it assigns no value to E_j^br at
configurations outside Sat(𝒞_glob) — those values are BFT-0-off-𝒞_glob content (OFFGLOB55). (ii) Even granting E_j^br there, a
chart piece R(X) has a value at V ∈ 𝒦_BFT only if V|_{Ω(X)} is gauge-equivalent on S(Ω(X)) to a point of 𝒫_{ε_gl}|_{Ω(X)}. By the
Stokes bound (HIST GAP S2-2: flux ≈ m²ε ≤ 4m·max|B|), a configuration of 𝒦_BFT with plaquette logs ≍ ε_0 on an m × m square of
X^+ needs max|B| ≳ mε_0/4 in **every** gauge on X^+, so for m > 4ε_gl/ε_0 no local gauge brings it into the chart. Since
*-connected polymers of every size occur, (b) on 𝒞_glob(ε_gl) reaches 𝒦_BFT only on polymers of ℓ^∞ extent ≲ ε_gl/ε_0 (via
local axial gauges, Lemma AX's 3·diam·ε bound) and leaves the representation undefined beyond. So (b) does not give (c₀). ∎

> **Proposition CURV.** (1) Every live consumer K1-K4 quantifies over a 𝒢-invariant class strictly containing Sat(𝒞_glob), on
> which it needs (c₀) and never invariance of a piece beyond what Lemma AVG supplies. (2) (c₀) + (H-inv) ⇒ (c₀) with locally
> gauge-invariant pieces and identical constants ⇒ (b) on 𝒞_glob(ε′). (3) (b) on 𝒞_glob ⇏ (c₀). **Status: PROVEN-HERE**
> ((1) relative to §2.1's inventory; (2)-(3) unconditional given (H-inv) and the chart containment above).

### 5.4 Consequence for (CovLift), (Mult-Y), (Pair-loc), (I-id)_Z
These are the inputs of lane B's Theorem BB-gi_k (BFT_B "Relative to Theorem BB-mix_k's hypothesis set, the new inputs are
(CovLift) (structural, OPEN) and (Mult-Y)"; + (Pair-loc), (I-id)_Z per [RBB4-fix RS4-7]). Their only output is (b). **On 𝒞_glob
they therefore have no consumer.** Their possible role is inside a **construction of (c₀)**: lane B's Proposition GI-off runs the
covariant construction BB-bond_k^cov off 𝒞_glob with per-box frames, and (CovLift)'s cocycle makes the frame choices cancel. By
Lemma AVG, invariance of the final pieces does **not** require that cocycle — any construction producing bounded holomorphic
local pieces on 𝒦_BFT, e.g. with frames chosen as holomorphic functions of V (axial-tree holonomies), can be averaged afterwards.
Whether a (c₀) construction needs covariance **for its estimates** (compatibility of local inverses across boxes, transition
functions) is a question about that construction — OFFGLOB55's scope (smooth lift, local gauges off 𝒞_glob), not decided here.
The [S26-BANKED] sentence "the full nonlinear (CovLift) bound is NOT-VERIFIED" is unchanged; what changes is that no item on
𝒞_glob waits on it.

---

## 6. Lemma ENV — the total E_j^br is locally gauge invariant on the chart, in path form (appended after `date -u` printed 2026-10-29T04:20:03Z)

Not needed for Theorem T0; recorded because it settles that (b) is not obstructed by the **total**, and because it is the path
form of Lemma AVG's hypothesis (H-inv) on the chart.

> **Lemma ENV.** Let F(x; B) := 𝔉_j(e^x; e^B) (TOWER-VAR, composite coordinates about the trivial chain) and let x(B) be the
> unique **full** critical point of F(·; B) in the slice ball, holomorphic in B ∈ int 𝒫 (banked BFT-E: PROOF [S26-BANKED] "GV55 +
> CODEX_REVIEW_GV"; BFT4W55 Lemma UQ "x(B) (BFT-E) is the unique critical point of F in 𝔅_u"). Put E(B) := F(x(B); B). Then for
> every λ : level-j sites → su(N) and B ∈ int 𝒫, with e^{B_t} := (e^B)^{exp(tλ)}: **dE(B_t)/dt|_{t=0} = 0.** Consequently
> E(B_1) = E(B_0) whenever e^{B_t} = (e^{B_0})^{h_t} along a C¹ path of real gauges h_t (h_0 = 1) with B_t ∈ int 𝒫 for all t.

*Proof.* Extend λ to a composite generator λ̂ = (λ_0, …, λ_{j−1}, λ_j := λ) compatible at roots, λ_i(c_X) = λ_{i+1}(X) (e.g.
λ_i := λ_{i+1}(X) on every level-i site of the block of X). By Lemma N5-cov (PROOF "Lemma N5-cov (gauge covariance": "M̄_c(g·U) =
g(c_X)M̄_c(U)g(c_Y)^{-1} …, W_0 is covariant …, and φ(gV; g·M) = φ(V; M)"; Wilson terms are class functions of plaquettes),
𝔉_j(Z^Ĝ; V^{g_j}) = 𝔉_j(Z; V) for every composite gauge Ĝ with root compatibility and arbitrary top component g_j; for complex
data and real Ĝ by analytic continuation (N5-cov: "For complex backgrounds and real g the same holds"). With Ĝ_t := exp(tλ̂) and
e^{x_t} := (e^x)^{Ĝ_t} (defined for small t), F(x_t; B_t) = F(x; B). Differentiate at t = 0, x = x(B): ∂_xF(x(B); B)[ẋ] +
∂_BF(x(B); B)[Ḃ] = 0, and ∂_xF(x(B); B) = 0 on **all** directions (full critical point), so ∂_BF(x(B); B)[Ḃ] = 0. By the chain
rule dE(B_t)/dt|_0 = ∂_xF(x(B); B)[Dx(B)Ḃ] + ∂_BF(x(B); B)[Ḃ] = 0. Along a path, apply this at each B_t with generator
ḣ_th_t^{-1}. ∎
*Scope.* ENV gives (H-inv) on each path component of {h : (e^{B_0})^h ∈ int 𝒫}; invariance between components (e.g. gauges
winding around a long torus cycle) is not claimed. It uses only full criticality — no orbit-coverage statement (Codex BFT4W W5:
"No nonlinear orbit-coverage claim is required" for the identification; the same holds here).

---

## 7. What changes in the ledger (appended after `date -u` printed 2026-10-29T04:20:03Z)

1. **Critical path (HANDOFF row "BFT-4").** Replace "reduced to local ARGUED items + (CovLift)" by: *BFT-4 (a) on 𝒞_glob:
   conditional implication (BFT4W55 + CODEX_REVIEW_BFT4W W9; premise (R)/F^σ; all-torus constant C_all per W8). BFT-4 (b) on
   𝒞_glob: **no consumer** (BFT4B55 Theorem T0, pending Codex) — off the critical path. BFT-4 off 𝒞_glob = (c₀): bounded local
   holomorphic pieces on BFT's gauge-invariant class; local invariance then free (Lemma AVG). (CovLift), (Mult-Y), (Pair-loc),
   (I-id)_Z are candidate ingredients of a (c₀) construction only (OFFGLOB55 scope).*
2. **PROOF.md's 105-item tally** does not move (lane-level result).
3. **SMALLNESS_DAG.** No edge changes for (b) (it has no node). BFT34_55 F5's proposed edge "BFT4 → CEexp (classical part)" is
   supported by (G6) + K3 (on 𝒞_glob from (a); off 𝒞_glob from (c₀)).
4. **The BFT-4 statement itself (REVIEW_S22 Part 5).** Its words "a sum of gauge-invariant local polymers" are redundant on its
   own polydisc (BFT-2's, curvature form, 𝒢-invariant): by Lemma AVG any bounded local holomorphic representation there can be
   replaced by a locally gauge-invariant one with the same constants. The clause can be kept as harmless; it is not a separate
   obligation.
5. **Not changed:** the status of (b) itself (NOT-VERIFIED / OPEN as a statement — nothing here constructs it), the
   [S26-BANKED] (CovLift) sentence, lane B's implications BB-gi_k / GI-cov (not re-derived; not needed), and the open status of
   BFT-0..4 off 𝒞_glob.

---

## 8. Check b4b55_1 — exact finite-group test of Lemma AVG's algebra (appended after `date -u` printed 2026-10-29T04:22:06Z)

**Criteria** `checks/b4b55_1_criteria.md` written 04:22:06Z (before any b4b55 script). Model, gates P0-P6, controls K1-K4 and
what the check cannot decide are stated there.

**Hand derivation of the predicted averages (written before the script; P4 tests it).** S_3 with M(q)[r][c] = [q(c) = r].
- *Single entry.* For a link value U and endpoint gauges a, b: M(aUb^{-1})[r][c] = [a(U(b^{-1}(c))) = r]. For each of the 6 values
  of b, exactly 2 of the 6 elements a map the point U(b^{-1}(c)) to r. Average = 12/36 = **1/3**. So avg h = (1 + 2 + 3)/3 = 2 and
  avg h2 = 2/3.
- *Open path.* P_p ↦ g(s)P_pg(s+e1)^{-1} and C_p = U(s,1)^{-1} ↦ g(s+e1)C_pg(s)^{-1} (the interior sites of P_p cancel). With
  a := g(s), b := g(s+e1), i := a^{-1}(0), j := b^{-1}(1): [aP_pb^{-1}(1) = 0] = [P_p(j) = i] and [bC_pa^{-1}(0) = 1] = [C_p(i) = j].
  Both hold iff j = C_p(i) and i is a fixed point of P_p∘C_p = U_p. For each such i there are 2 choices of a (a^{-1}(0) = i) and 2
  of b (b^{-1}(1) = j). Average = 4·fix(U_p)/36 = **χ(U_p)/9**.
- *Hence* R̄({p}) = χ(U_p) + 2χ(U_p²) + (2 + 2 − 2 − 2) + [p ∈ Tset]χ(U_p)/9 − [p − e0 ∈ Tset]·2/3 and R̄(D_q) = −χ(U_q)/9 + 2/3;
  the totals agree: the χ/9 terms and the 2/3 terms cancel between {p} and D_q, as Lemma AVG (c) requires.

**Run record (appended after `date -u` printed 2026-10-29T04:26:55Z).** Script `checks/b4b55_1_avg.py` written 04:23:55Z (after the
criteria, 04:22:06Z). **One run**, 04:24:10-04:24:20Z, `nice -n 10 /usr/bin/time -l python3 -I -B`, output `checks/b4b55_1.out`,
stderr `checks/b4b55_1_err.txt` (timing only: 10.3 s, 17 MB peak). No edit of criteria or script after the run; no earlier run.
**OVERALL: PASS.** P0 and P1: Σ_XR(X) = Σ_XR̄(X) = E exactly for all five configurations (E = 81, 77, 55, 51, 28 for A, C, R1, R2,
R3). P2: every R̄(X) invariant under both non-constant random gauges, every configuration. P3: every R̄(X) unchanged by a change
outside its support (the gauge acted on **all** links incident to the averaging set and every polymer was evaluated on the full
configuration). P4: every R̄(X) equals the hand formula (χ(U_p)/9 and 2/3 terms) exactly. P5: (a) some input piece is not
invariant; (b) R̄({(0,0)}) − χ(U_p) − 2χ(U_p²) = 1/3 at A and 1/9 at C (non-constant, = χ(U_p)/9). P6: over all 1296 local
configurations, max|R̄| = 28/3 ≤ max|R| = 19. Controls: **K1, K2, K3, K4 all fired.**
*What it decides:* the averaging set of Lemma AVG (all endpoints of the support links), the exact identity, invariance under
non-constant gauges, locality, and the hand computation of two non-trivial averages, in a non-abelian instance whose input pieces
are genuinely non-invariant. *What it cannot decide (as pre-registered):* holomorphy, complex domains, SU(N), sup bounds on
non-compact complex domains, any property of BFT-4's actual pieces, k-/T-uniformity, and Theorem T0's consumer trace (a reading of
the ledger, not a computation). *Could it have failed?* Yes: each control made its gate fail, and P4 compares against an
independently derived formula (K4 shows a 1/8-for-1/9 slip is caught). A scratch symbolic restatement of the elementary identity
d/ds[2 − 2cos(t + s)]|_{s=0} = 2 sin t (used in finding V6 below; a hand computation) was run outside the repository; it is not a gate.

---

## 9. Errata and precisions to §1-§8 (appended after a full re-read; nothing above is edited)
- **E1 (§3 Remark 3, the "⇒" direction).** Read (b) in its local form — R(X)(W^h) = R(X)(W) whenever W and W^h are both points of
  𝒫_ε|_{Ω(X)} — and add the hypothesis (H-inv) for E_j^br on Sat_ℂ(𝒫_ε) (Lemma ENV supplies it only on path components). With
  these, the extension R(X)(V) := R(X)(B) is well defined and the identity holds on the saturation. The "⇐" direction (AVG) is
  as written.
- **E2 (§4 (G4), distance convention).** If N5's d in N_m is the ℓ¹ distance rather than ℓ^∞, replace m ≤ m_0/(2M_c) by
  m ≤ m_0/(8M_c) (d_1 ≤ 4d_∞ in d = 4); C_H is unchanged. No conclusion changes.
- **E3 (§4 (G6), the BCH constant).** C_BCH is used only for |X|, |Y| ≤ ε_gl/2 ≤ 1/8, inside the absolute-convergence region of
  the BCH series (‖X‖ + ‖Y‖ < log 2 in operator norm, which the HS bound implies); read "for |X|, |Y| ≤ 1/8" for "≤ 1". And read
  "diam_∞Ω(X)" for "diam_∞X" in the decay factor: diam_∞Ω(X) ≤ M_c(|X| + 2) gives e^{−m_0|X|} ≤ e^{2m_0}e^{−(m_0/M_c)diam_∞Ω(X)}.
- **E4 (§2.2, K1's quoted text).** The quoted "for every □ … there is a level-1 gauge g_□ … ≤ δ_H" is Theorem NAH1 (b), i.e. what
  (NA-H_loc) asks; BB-4c (v) is the BFT-4 route to it ("In a local AX gauge, Hess E_i^br(U) − Hess E_i^br(1) is bounded in N_m").
- **E5 (§5.3 (⇏) (ii), making the Stokes step rigorous).** Take an abelian configuration: all links of X^+ in one maximal torus,
  V^r_P = exp(fH) on the plaquettes of one plane of an m × m square (|fH| ≤ ε_0), trivial elsewhere, m²|fH| < π. The boundary
  holonomy of the square is conjugate to exp(m²fH) in every gauge (its conjugacy class is gauge invariant), and for the bi-
  invariant distance on SU(N), d(1, Πu_i) ≤ Σd(1, u_i); so in every gauge on X^+ some boundary link has |log U_b| ≥ m|fH|/4. For
  4ε_gl/ε_0 < m < (π/ε_0)^{1/2} (non-empty for ε_gl < (πε_0)^{1/2}/4) no gauge brings V|_{X^+} into 𝒫_{ε_gl}; since X^+ has side
  ≥ 3M_c, such squares fit in X^+ of a single cube when 4ε_gl/ε_0 < 3M_c. So (b) on 𝒞_glob(ε_gl) leaves pieces undefined at
  configurations of 𝒦_BFT already on one-cube polymers.

---

## 10. Findings, claim by claim (verdict; file + locating string; reason)

**Claims of others that this work rests on or settles.**
- **V1 — BFT34_55 §3.2 "FINDING F5" ("Live consumer 1: eps_N5_unif … The BFT-4 content it uses is (i) + (v)"; "Live consumer 2:
  CEexp … For the classical (branch-action) part this is REFUTED: BFT-4 as stated implies it"; "Not consumed on the live route: …
  the uniform form of (H-G)"). CONFIRMED.** Re-traced: SMALLNESS_DAG's only out-edge of BFT4 is 216 → eps_N5_unif; REVIEW_S22
  "PROOF/N5: BFT-0, 1 (θ_w = 0 suffices), 2 and 4"; PROOF "(iv) ⇐ BFT-4 (by Cauchy)"; SF's (L-loc)_k statement; REVIEW_S22 "NAH-
  unif′, HG-ind's uniform form and (H-K) all become unnecessary". Addition (Theorem T0): neither live consumer uses invariance of
  a piece under a non-constant gauge.
- **V2 — BFT34_55 §2.1 "sup_{𝒟(X)}|R(X)| is meaningful only for a gauge-invariant R(X) that extends holomorphically to
  curvature-small (not potential-small) data on X^+". REFUTED in its "only for a gauge-invariant R(X)".** Counterexample: the
  singleton κφ̂_c(V_c; 1) (holomorphic form κ(N − ½(tr V_c + tr V_c^{-1}))) is holomorphic and bounded on 𝒟(X) and not invariant
  under gauges at the endpoints of c. *Correct statement:* the sup is meaningful for any R(X) holomorphic and bounded on 𝒟(X); by
  Lemma AVG such a family can be replaced by a locally gauge-invariant one with the same bounds. The section's conclusion "BFT-4
  as stated is (PD-curv)" is unaffected (CONFIRMED).
- **V3 — BFT34_55 §2.6 (b) / §4 "(b) locally gauge-invariant pieces ⇐ (a) + (CovLift) … + (Mult-Y) + (Pair-loc) + (I-id)_Z".
  NOT-VERIFIED** (lane B's implication, not re-derived; not needed: (b) has no consumer, Theorem T0).
- **V4 — BFT_B "SF.md (L-loc)_k. With Theorem BB-gi_k the classical pieces of (L-loc)_k can be taken locally gauge invariant
  (given (CovLift), (Mult-Y))". NOT-VERIFIED as a sufficiency claim** (not re-derived). Superseded: (L-loc)_k has no invariance
  clause, and on the gauge-invariant class the invariance is free (Lemma AVG) without (CovLift) or (Mult-Y).
- **V5 — BFT4W55 §7 "The pieces are **not** locally gauge invariant (E_∅ is a sum of single-link terms …)". CONFIRMED** (e.g. at
  B = 0 a gauge with h_x ≠ h_y changes κφ̂_c(·; 1) from 0 to κφ̂(h_xh_y^{-1}; 1) ≠ 0), and sharpened by V6.
- **V6 — BFT_B Corollary BB-4c (ii) "On contractible X a flat field is gauge-trivial on X, so the same argument applies at every
  flat point", applied to Theorem BFT4a-glob's representation. REFUTED for that representation** (BB-4c itself assumes
  gauge-invariant pieces and is unaffected). Counterexample, in 𝒞_glob: Codex BFT4W W8's flat field B_c = t·diag(i, −i) on
  direction-1 top links (|B_c| = √2|t| ≤ ε_gl for |t| ≤ ε_gl/√2; every plaquette product = I). The singleton
  κφ̂_c(e^{B_c}; 1) = κ(2 − 2cos t) (SU(2)) has derivative κ·d/ds[2 − 2cos(t + s)]|_{s=0} = 2κ sin t ≠ 0 in the direction a at that
  flat point, on a one-cube (contractible) polymer. Consequence: none on the live route — the flat-point clause feeds only BB-4c
  (iii), which is not consumed (K5) — but it shows K5's use genuinely needs invariant pieces.
- **V7 — HANDOFF row "BFT-4 | … reduced to local ARGUED items + (CovLift) | BFT4W55 (running)". REFUTED as worded (superseded).**
  Correct: (a) on 𝒞_glob is a conditional implication (BFT4W55 + Codex BFT4W W9); (CovLift) is not on any 𝒞_glob critical path
  (Theorem T0); what BFT-4 on BFT's class needs is (c₀) plus BFT-0 off 𝒞_glob (§7 item 1 gives the replacement text).
- **V8 — REVIEW_S22 Part 5 "BFT-4 (branch-action class). E_k^br = S_W + R_k with R_k = Σ_X R_k(X) a sum of gauge-invariant local
  polymers … The polydisc is the BFT-2 one in curvature-adapted coordinates". CONFIRMED as a correct target**; its invariance
  clause is redundant given the rest on that 𝒢-invariant polydisc (Lemma AVG) — a simplification, not a refutation.

**New results of this file (status, not verdicts).** N1 **Theorem T0** (BFT-4 (b) on 𝒞_glob has no consumer on the live route) —
PROVEN-HERE, relative to §2.1's inventory. N2 **Lemma AVG** — PROVEN-HERE (b4b55_1 PASS checks its algebra). N3 **Proposition
GLOB** — PROVEN-HERE as an implication of the corrected conditional Theorem BFT4a-glob. N4 **Proposition CURV** — PROVEN-HERE
((1) relative to the inventory; (2)-(3) given (H-inv)), with E5. N5 **Lemma ENV** — PROVEN-HERE as an implication of banked BFT-E
and Lemma N5-cov (whose covariance identities I re-derived: contour averages between roots, the unique maximiser W_0, and
φ(gV; g·M) = φ(V; M) from φ = N^{-1}[Re tr(W_0^{-1}M) − Re tr(V^{-1}M)]).

## 11. Summary table

| # | Claim (file, locating string) | Verdict / status | Where |
|---|---|---|---|
| V1 | BFT34_55 §3.2 "FINDING F5" (consumers of BFT-4) | CONFIRMED (+ no live consumer uses piece invariance) | §2, §4 |
| V2 | BFT34_55 §2.1 "meaningful only for a gauge-invariant R(X)" | **REFUTED** in letter (singleton κφ̂_c counterexample); conclusion (PD-curv) stands | §10 |
| V3 | BFT34_55 §2.6 (b) / §4 reduction of (b) to (CovLift) + (Mult-Y) + (Pair-loc) + (I-id)_Z | NOT-VERIFIED (not needed) | §5.4 |
| V4 | BFT_B "(L-loc)_k … can be taken locally gauge invariant (given (CovLift), (Mult-Y))" | NOT-VERIFIED (superseded by AVG) | §5.2 |
| V5 | BFT4W55 §7 "The pieces are not locally gauge invariant" | CONFIRMED | §10 |
| V6 | BFT_B BB-4c (ii) flat-point clause, for BFT4a-glob's pieces | **REFUTED** for those pieces (2κ sin t ≠ 0); no live consequence | §10 |
| V7 | HANDOFF "BFT-4 … reduced to local ARGUED items + (CovLift)" | **REFUTED** as worded (superseded) | §7 |
| V8 | REVIEW_S22 BFT-4 "gauge-invariant local polymers" on the BFT-2 polydisc | CONFIRMED as target; invariance clause redundant | §7 |
| N1 | **Theorem T0** — (b) on 𝒞_glob has no consumer; wherever (a) fails the missing input is (c₀), which implies (b) | PROVEN-HERE (relative to the §2.1 inventory) | §2-§5 |
| N2 | **Lemma AVG** — Haar averaging on a gauge-invariant domain | PROVEN-HERE; b4b55_1 PASS | §3, §8 |
| N3 | **Proposition GLOB** — (G0)-(G7), every consumer's 𝒞_glob form from (a) | PROVEN-HERE as implication (BFT4a-glob conditional, C_pol) | §4 |
| N4 | **Proposition CURV** — consumers' classes 𝒢-invariant; (c₀) ⇒ (b); (b) ⇏ (c₀) | PROVEN-HERE (with E5) | §5 |
| N5 | **Lemma ENV** — E_j^br path-invariant under local gauges on the chart | PROVEN-HERE as implication of BFT-E + N5-cov | §6 |
| — | b4b55_1 | PASS (7 gates; 4 controls fired) | §8 |

**Counts (claims of others): CONFIRMED 3 (V1, V5, V8), NOT-VERIFIED 2 (V3, V4), REFUTED 3 (V2, V6, V7).**

## 12. Codex verdicts used — agree or disagree, explicitly
- **CODEX_REVIEW_BFT4W (complete on disk, 247 lines).** W8 (small-torus prefactor REFUTED; repair C_all): **AGREE** — I re-did
  the exponent count (C_E ∝ ε²(q⁶ + q³) with q = s̄ ∝ e^{m_0}, so 2e^{m_0}C_R grows like e^{7m_0}, against the fallback's e^{16m_0}
  weight) and used C_all throughout. W9 (BFT4a-glob bankable only as a conditional theorem with (R)/F^σ named): **AGREE** — GLOB
  is stated as an implication of that conditional form. W5 (identification needs no orbit coverage): **AGREE**; Lemma ENV likewise
  uses only full criticality. Item 5 ("Do not bank … local gauge invariance of the pieces, or extension off the global potential-
  small domain"): **AGREE**, and Theorem T0 adds that the first is not needed on 𝒞_glob and is free off it once the second (c₀)
  holds. W1, W2, W6, W7, W10: not used (no disagreement noted).
- **CODEX_REVIEW_BFT34.** R10 (repaired Cauchy consequences: attachment −3n/2, 81e^{3m_0n/4}, rate m_0/(8M_c)): **AGREE** as
  banked; used only by reference in (G3), constants not re-derived. N7 ("full BFT-4 remains OPEN. The local gauge-invariant
  polymers, curvature-small domain, decoupling-family construction and branch identification have not been proved here"):
  **AGREE**; Theorem T0 refines it — the "local gauge-invariant polymers" item is subsumed by the "curvature-small domain" item.

## 13. For the lead (short)
1. **BFT-4 (b) on 𝒞_glob has no consumer on the live route (Theorem T0).** On 𝒞_glob every live consumer — eps_N5_unif (via BB-4c
   (i) and (v)/(NA-H_loc)), (BG-unif) (iv), CE-exp^k's (L-loc)_k, the induction's (I_k^E)″ per-cube uses — is served by (a) in the
   global chart (Proposition GLOB: Cauchy, locality, constant gauges only). Off 𝒞_glob every consumer lives on a gauge-INVARIANT
   class and needs (c₀) = bounded local holomorphic pieces there; **by Lemma AVG (Haar averaging) local gauge invariance then comes
   free with identical constants**, and (c₀) implies (b), while (b) does not imply (c₀). So (b) is dominated; no (CovLift)
   construction was attempted (brief step 1 not reached, by design of the brief).
2. **Critical-path change (HANDOFF row BFT-4):** drop (b) and, on 𝒞_glob, (CovLift)/(Mult-Y)/(Pair-loc)/(I-id)_Z; the open BFT-4
   item is (c₀) off 𝒞_glob (with BFT-0 there), OFFGLOB55's territory. Whether a (c₀) construction needs covariance for its
   *estimates* is that construction's question; invariance of the final pieces does not need it. Replacement text: §7 item 1.
3. **PROOF.md's 105-item tally does not move.** BFT-4's statement (REVIEW_S22) may keep "gauge-invariant" — it is redundant on its
   own (𝒢-invariant) polydisc.
4. **Two precise refutations, no live consequence:** BFT34_55 §2.1's "meaningful only for gauge-invariant R(X)" (V2), and BB-4c
   (ii)'s flat-point clause for BFT4a-glob's pieces (V6: gradient 2κ sin t ≠ 0 at Codex W8's flat field).
5. **Scope caveat:** T0 is relative to the consumers as written (inventory §2.1). If the induction's polymer class (b″) were ever
   moved from its gauge-covariant domain 𝔇 onto a potential chart, a Dimock-type piecewise contraction (1502.02946 §5) would
   consume piece invariance on the chart; the live (I_k^E)″ is not of that form.
6. **Suggested Codex check, in this order:** the consumer inventory (§2.2: is there a consumer of BFT-4 that quantifies over 𝒞_glob
   only, or that uses invariance of a piece under a non-constant gauge on the live route?); Lemma AVG (c) and the 𝒢-invariance
   of each consumer domain (§5.1); (G4) against N5-sf_i's existence quantifier for g_□; V6's counterexample.

*File ends here (appended 2026-10-29 after `date -u` printed 04:26:55Z).*

---

## 14. Addendum — files that changed during this run (appended after `date -u` printed 2026-10-29T04:29:31Z)

A final listing showed files modified after my criteria (04:22Z) by other sessions: CODEX_REVIEW_BFT4W.md (247 → 249 lines),
HANDOFF.md, OFFGLOB55.md, ASSEMBLY55.md, SESSION25_RESULTS.md, others. Read now, as on disk:

- **CODEX_REVIEW_BFT4W.md.** Every "**Verdict:**" line (W1-W10) and the "Exactly what may be banked" list (items 1-5) are as I
  used them in §1/§12; the two added lines change no verdict I rely on. §12 stands.
- **OFFGLOB55.md (now 800 lines).** It states Theorem OFF (BFT-0/1/2 off 𝒞_glob as an implication; "pending Codex") and leaves
  BFT-3/4 open (HANDOFF: "identification clause, BFT-3/4, boxes open"). Read only for overlap: it does not construct polymer
  pieces, so there is no duplication; its Proposition C4 ("𝒞*_glob is a strict subclass") agrees with §5.1. If Theorem OFF
  survives Codex, it is the natural source of Lemma AVG's (H-inv) off 𝒞_glob (its §6.6 "Proposition UQ (uniqueness modulo
  gauge)"); I did not verify it.
- **HANDOFF.md — the BFT-4 row was rewritten after I read it.** It now reads "(a) on 𝒞_glob banked conditionally on the local
  reading (R); (b) gauge-invariant pieces open | RLOC55 on (R); BFT4B55 on (b)". So **V7's target text is gone from disk**: V7
  stays REFUTED for the superseded wording only (other files may still quote it). **V7′ (current row): CONFIRMED as a status**
  ((b) is indeed not constructed), with one annotation to add: *"(b): no consumer on the live route (BFT4B55 Theorem T0) — off the
  critical path; the open BFT-4 item is (c₀) off 𝒞_glob."*
- **A seventh consumer, not in §2.2: SRC's decay node.** HANDOFF row "SRC": "(B) real conditional decay = a decaying polymer
  representation (same object as BFT-4)"; SRCCD55 §3.2: "the mechanism **SRC-poly** (conditional multiscale polymer
  representation, analytic in a complex e-source on a fixed polydisc)", norm "(N4) Mechanism: a BFT-4-type polymer norm",
  quantified "for every U_K ∈ 𝒮_K", with "𝒮_K is the set of U_K with max_P|log U_{K,P}|_op ≤ ε_0 (BFT's ε_0 at level K)".
  **K7 analysis.** (i) Its class 𝒮_K is a curvature condition — 𝒢-invariant and strictly larger than 𝒞_glob (§5.1). (ii) Its
  polydisc is in the **source** η, not in the gauge field, and its statement has no gauge-invariance clause for pieces. (iii)
  It is a representation of a different functional (the conditional source-inserted generating function, with fluctuations),
  not of E_k^br; ASSEMBLY55 F24 records "decay = BFT-4's decoupling family" as identifying "a classical family with the quantum
  (D1)" (not checked by me). Hence, whether or not SRC-poly is built from BFT-4-type data, what it could consume is BFT-4 data
  **on 𝒮_K**, i.e. (c₀); and if SRC-poly's pieces are ever required to be gauge invariant in U_K, Lemma AVG supplies it on the
  𝒢-invariant 𝒮_K. **K7 does not consume (b) on 𝒞_glob.** Theorem T0 extends to K1-K7 unchanged.
- **ASSEMBLY55.md** (C1, C2) independently records, for (BG-unif) and (N5-unif): "Also a CLASS mismatch remains: (BG-unif) is
  for curvature-small V, BFT-E for 𝒞_glob (OPEN, OFFGLOB55)" — the same class observation as Proposition CURV (1). Its
  convention point (E^br vs E^cb, i.e. (NSL)) is independent of gauge invariance of pieces (noted in (G4)).

**Counts, final (claims of others): CONFIRMED 4 (V1, V5, V7′, V8), NOT-VERIFIED 2 (V3, V4), REFUTED 3 (V2, V6, V7 —
the last for wording already superseded on disk).**
