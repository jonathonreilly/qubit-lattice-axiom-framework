# LW1 referee report (pass 3)

**Referee.** Claude Opus 5.5 subagent (model id `claude-opus-5-5`), pass 3, max effort, 2026-11-04. This session wrote neither pass 1 (`LW1_DRAFT.md`) nor pass 2 (`LW1.md`). This is one check: one whole-part, line-by-line read. No review of this review was commissioned.

**Text read.** `LW1.md` as of commit `74098489da` (the last commit that touches it; unchanged at branch head `58d5c77701` when read). SHA-256 of the file read: `663702e2ef5d033d046c6debaa6b53f4a7d05940a54bb68565c7540ecf3b10e6`. Line numbers below refer to that file.

**References consulted.** `LW1_DRAFT.md` (SHA-256 `f35997...cf22a9`, the hash LW1 records); `TOE_ASSEMBLY.md` lines 71-227 (section 3 premises and the LW1 target; the hash of lines 167-227 equals the one LW1 records); `origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md`. The audit ledger was not read. `LW1U_DRAFT.md` was not read.

**Method.** Every proof was re-derived by hand. A `[check]` is a small scratch computation outside the repo (script in the session scratchpad, under a minute, a few MB). It guides only and proves nothing. Verdicts: CORRECT; ERROR (a false line, quoted, with a fix or counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step.

**Counts.** 92 items: 85 CORRECT, 3 ERROR, 4 INCOMPLETE. The 28 distiller definitions count as 28 items; the six premise quotations count as one. No ERROR or INCOMPLETE item changes the content of a theorem.

---

## 1. Verdict table

| # | Item (LW1 line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 "Proved here" and "Open by name" lists (7, 9) | CORRECT | Each listed result is proved below; each open item appears in §4. |
| 2 | §0 premise line (11) | ERROR | Cites `TOE_ASSEMBLY.md` "lines 167–206"; section 3.2 is lines 167-185. |
| 3 | §1 Sites and symmetry (21-26) | CORRECT | |
| 4 | §1 Matter and links (28-40) | CORRECT | |
| 5 | §1 Free tick (42-48) | CORRECT | |
| 6 | §1 Dressed tick (50-55) | CORRECT | |
| 7 | §1 Time and states (57) | CORRECT | `ω_{2n}=ω_0∘α^n` checked. |
| 8 | §1 Occupations, odds and records (59-69) | ERROR | Typo `(1−n_x)^{1−χ_x}`; must be `1−σ_x`. |
| 9 | §1 Transport, finite (71-80) | CORRECT | |
| 10 | §1 Cell-invariant optimiser set `𝒪_h` (82-88) | CORRECT | Limit defining `s` is proved in E6 (forward pointer given). |
| 11 | §1 Sea and momentum (90-92) | CORRECT | |
| 12 | §1 Events (94) | CORRECT | |
| 13-40 | Distiller definitions 1-28 (100-127) | CORRECT (28) | 25 and 26 are readings or premises outside the working-set text; list them at freeze. |
| 41 | §2 six premise quotations (133-149) | CORRECT | Exact match with `TOE_ASSEMBLY.md` 178-183 `[check: string comparison]`. |
| 42 | §2 law specification (151-159) | INCOMPLETE | The finite-region `Act` clause does not define one configuration on `Z^3`; non-invariant infinite case not referenced. |
| 43 | §2 free vacuum and LW1 target paragraphs (161-163) | CORRECT | |
| 44 | Lemma A1 (169) | CORRECT | |
| 45 | Lemma A1a (173) | CORRECT | Layers are not rotation-covariant one by one; see note. |
| 46 | Dressed factorization, closed by the distiller (179-188) | CORRECT | |
| 47 | GAP UALL (190) | CORRECT | Counterexample valid; referee closure for the trace step. |
| 48 | Theorem A2 (192-200) | CORRECT | |
| 49 | Theorem A3 (202-212) | CORRECT | |
| 50 | Theorem B2 (216-218) | CORRECT | |
| 51 | Lemma B3 (220-222) | CORRECT | |
| 52 | Theorem B4 (224-226) | CORRECT | |
| 53 | Gauged covariance and B1/B1q (228-230) | CORRECT | |
| 54 | Theorem B5(a) (232-234) | CORRECT | |
| 55 | B5(b) and GAP B5(b) (236-238) | CORRECT | Counterexample `U(1)^8` per cell valid. |
| 56 | Lemma B6 (242-253) | CORRECT | |
| 57 | Theorem B7 (255-257) | CORRECT | |
| 58 | Support factorization (259-263) | CORRECT | |
| 59 | Theorem B8 (265-276) | CORRECT | |
| 60 | Corollary B8a (278-280) | CORRECT | |
| 61 | Theorem B8b (282-291) | INCOMPLETE | Value-law clause of (ii) uses Born one-time marginals of the history measure without stating or citing them. |
| 62 | Theorem B9, established clauses (293-299) | INCOMPLETE | Same missing hypothesis; undefined symbol `ℙ`. |
| 63 | GAP LW1-i/B9 (301) | CORRECT | Counterexample valid. |
| 64 | Theorem B10 (305-341) | CORRECT | `[check]` agrees. |
| 65 | Theorem B11 (343-352) | CORRECT | |
| 66 | Theorem C1 (354-372) | CORRECT | `[check]` agrees. |
| 67 | Theorem B12 (374-376) | CORRECT | |
| 68 | GAP B12(ii-iii) (378) | CORRECT | Gap real. |
| 69 | Law-choice paragraph (380) | CORRECT | No mathematical claim. |
| 70 | Theorem E1 (384-392) | CORRECT | Statement should say each plaquette sublayer has commuting gates. |
| 71 | Theorem E2a (394) | CORRECT | |
| 72 | GAP E2a-0, closed by the distiller (396-402) | CORRECT | Closure complete. |
| 73 | Theorem E2b (404-419) | CORRECT | |
| 74 | Theorem E3 (421-423) | CORRECT | |
| 75 | Theorem E4 (425-431) | CORRECT | |
| 76 | Theorem E5 (433-439) | CORRECT | Not circular with B9. |
| 77 | Theorem E6 (441-455) | CORRECT | |
| 78 | Lemma LW1-U, OPEN (459-461) | CORRECT (open) | Scope remark: non-ergodic states; reconcile with branch commit `58d5c77701`. |
| 79 | LW1-U Attack 1 (463) | CORRECT | |
| 80 | LW1-U Attack 2 (464) | ERROR | "no recovery sequence matches ..." asserts an unproved nonexistence. |
| 81 | LW1-U Attack 3 (465) | CORRECT | |
| 82 | LW1-edge, CLOSED (467) | CORRECT | |
| 83 | GA1-P, OPEN, with the commutator (469-475) | CORRECT | `[check]` agrees. |
| 84 | GAP LW1-i/B9, OPEN (477) | CORRECT | |
| 85 | GAP LW1-ii/F, OPEN (479-483) | CORRECT | Gap real; referee closure (negative): the closed-box reading is false. |
| 86 | GAP B5(b), OPEN (485) | CORRECT | |
| 87 | GAP B12(ii), OPEN (487) | CORRECT | |
| 88 | GAP B12(iii), OPEN (489) | CORRECT | |
| 89 | GAP LW1-N, OPEN (491) | CORRECT | |
| 90 | GAP LW1-R, OPEN (493) | CORRECT | Counterexample (tracial state) valid. |
| 91 | VC1, OPEN (495) | CORRECT | |
| 92 | Premise naming per result (whole text) | INCOMPLETE | Several results carry no "under PS-x" tag; refined entries, PS-2 and `realized_state_primitive` need stating. |

---

## 2. Details of the non-CORRECT items

### 2.1 ERRORS

**Item 2 (line 11, citation).** LW1: "Under the FINAL PS-1c, PS-3h, PS-3c, PS-6r, PS-7r and PS-11c in `TOE_ASSEMBLY.md`, lines 167–206". Section 3.2 of `TOE_ASSEMBLY.md` is lines 167-185; lines 186-206 are section 4 and the head of section 5. (The excerpt hash LW1 records equals the hash of the current lines 167-227, so the line numbers have not moved.) Fix: "lines 167–185".

**Item 8 (line 61, typo; one symbol with two meanings).** LW1: "P_{F,σ}=∏_{x∈F} n_x^{σ_x}(1−n_x)^{1−χ_x}". The symbol `χ_x` is undefined; with it the operator is not the occupation-pattern projector. The letter `χ` is defined on line 90 as `χ(K)=(1/3)Σ_i cos K_i`. Fix: `(1−n_x)^{1−σ_x}`. Every later use (B6, B8, B11, E4) reads `P_{F,σ}` as the pattern projector, so no proof is affected.

**Item 80 (line 464, LW1-U Attack 2, wording).** LW1: "torus limits fail to establish selection: no recovery sequence matches the exact torus Born marginals while preserving the allowed cube supports and approaching both variational optima". This asserts that no such sequence exists. Nothing proves that. The draft (line 532) says only: "No estimate of a 'support-respecting distance' between the torus laws and `mu_h` is available. Without it, (a) is not shown". Fix: "no recovery sequence has been constructed that matches ...".

### 2.2 INCOMPLETE

**Item 42 (lines 158-159, law specification of `Act`).** LW1: "On each finite active region, Act uses B7's least-change, greatest-entropy coupling. On the infinite cell-invariant domain it uses an element of 𝒪_h." Two steps are missing.
- (a) Section 1 defines the finite transport from "its reduced density matrix", that is, for a region of a larger system. For one infinite system, the B7 couplings of two nested regions are not shown to be restrictions of one another, so the clause does not define one actual configuration on `Z^3`, which PS-3 requires. Fix: restrict the clause to closed finite systems (an even torus, or a closed box with a stated boundary prescription), and say that the infinite-volume configuration comes from `𝒪_h` only.
- (b) For non-invariant infinite states (for example the B8b witnesses) the section gives no rule. §4 names this as LW1-N; §2 should point to it.

**Item 61 (Theorem B8b(ii), line 291).** LW1: "The copy test then forms a record at x and its locked value has the stated Born distribution." Formation is law-level and holds as stated. The value law needs one more step: the law of `r_x=ξ_2(x)` under the history measure is the time-2 Born marginal. This holds for any history measure whose one-time marginals are the `ν_h`. Referee closure: on closed finite systems this is B7 (the kernel carries `p` to `p'`, so by induction `ξ_h∼ν_h`); at infinite volume it is the first paragraph of the proof of E5, which does not use B8b or B9. With it, `ℚ(ξ_2(x)=1)=ν_2(ξ_x=1)=ω_ψ(n_x)=1/2`.

**Item 62 (Theorem B9, established clauses, lines 293-299).** LW1: "ℙ(r_x=v)=ϱ_n(n_y^v(1−n_y)^{1−v})" and, in the proof, "Its zero expectation gives ξ_{2n}(x)=ξ_{2n}(y) almost surely." The symbol `ℙ` is not defined (section 1 names the history measure `ℚ`). The step from `ϱ_n(D_xy)=0` to almost-sure equality needs `ξ_{2n}∼ν_{2n}` under `ℚ`, which is not stated. Referee closure: state B9 "for any history measure `ℚ` whose one-time marginals are the `ν_h`" (B7 on closed finite systems; E5 at infinite volume). Then `ℚ(ξ_{2n}(x)≠ξ_{2n}(y))=ν_{2n}(ξ_x≠ξ_y)=ϱ_n(D_xy)=0`, and the rest of the proof goes through. Since E5 builds `ℚ` and its marginals before it cites B9, the citation is not circular.

**Item 92 (premise naming per result).** `TOE_ASSEMBLY.md` section 3 says: "Every part that uses one names it, for example 'under PS-1'", and section 3.2 says: "Parts cite these as 'under PS-1c' and so on." LW1 names its premises once in section 0, and per result in: gauged covariance ("Under PS-1c"), B7 ("PS-3"), support factorization ("PS-3h"), B8a ("PS-3c"), B11 ("FINAL PS-11c"), B12 ("PS-1"), E5 ("PS-4"), E6 ("PS-3"). Missing:
- B8b: PS-3c (formation) and PS-4 ("Initialize no records"); B9: PS-3c; E3: PS-3c; E4: PS-3h (the cube supports). B8b, B9 and E4-E6 also use the joint Born identification (distiller definition 26).
- Section 0 lists the refinements but not the entries they refine. Each refinement "fixes the reading of the entry it names", so the list should read: PS-1 under PS-1c, PS-3 under PS-3h and PS-3c, PS-6 under PS-6r, PS-7 under PS-7r, PS-11 under PS-11c.
- PS-2 is listed (line 11) but no proof uses it: the joint Born rule is supplied directly and already gives the one-site trace form. Drop PS-2 or show where it enters.
- The LW1 target lists `realized_state_primitive` among LW1's premises (`TOE_ASSEMBLY.md` line 215). LW1 never names it. LW1 should say whether its "A realized history is supplied subject to PS-11c" (line 11) uses it.
- Two items are premises or readings outside the working-set text and should be listed as such: the joint Born identification (definition 26) and the record-memory reading of "locks" (definition 25).

### 2.3 Notes on CORRECT items that bear on the freeze

- **LW1-U scope (item 78).** The hypothesis admits every `2Z^3`-invariant state, including non-ergodic ones. For those, an invariant coupling can distribute mass among the ergodic components of the two marginals. Since `d̄` and `s` are affine, none of the three attacks addresses whether this freedom gives several optimisers. A branch commit made after `LW1.md`, `58d5c77701`, is titled "docs(toe): LW1-U pass 1, a counterexample for non-factor states". This session did not read it (outside its brief) and does not rely on it. If it stands, LW1-U needs a factor or ergodic hypothesis, or a restriction to the state sequences the law reaches.
- **LW1-ii/F (item 85), referee closure (negative).** In the closed-box reading the displayed identity is false; see section 3.G. So item 3 of the target needs an owner reading, not a proof: in the marginal reading (restrictions of one infinite history) it holds by E5; in the closed-box reading it fails.
- **LW1-R (item 90).** The tracial state is in the law's domain (even, gauge-invariant, no records) and forms no records ever. So "Records form." holds only on a restricted domain or under an existential reading. That is an owner decision.
- **Lemma A1a and the dressed factorization (items 45-46).** The nearest-neighbour layers they produce are `2Z^3`-covariant but not rotation-covariant one by one (the Givens order and the chosen word break the cube rotations). Only the product, the cube layer, is covariant. This meets PS-1 as PS-1c reads it ("the update is covariant"). It does not meet a reading in which each nearest-neighbour layer must be covariant. The freeze should record this reading.
- **Theorem E1 (item 70).** The statement "A supplied finite-depth layer of finite-support gauge-invariant plaquette gates has the same properties" is covered only when each sublayer consists of pairwise commuting gates (the proof's hypothesis). GA1-P shows that quantum-link plaquette terms on a shared link do not commute. The proof's last sentence says "layer by layer"; the statement should say so too.
- **Notation.** `𝖧` means both the entropy `𝖧_Λ` (line 78) and the subgroup of finite words (line 181). `s` means both the specific entropy (line 85) and `s_ε=sin ε` (line 90). `w` is both the signed quasi-energy (line 90) and the band function `w(K)≥0` (line 308). `ℚ` (history measure), `Q∈O` (rotation) and `Q_m` (box) share a letter; so do `𝒢` (group), `𝒢_x` (Gauss generator) and `G` (covariance), and `K` (momentum), `𝒦` (conjugation), `𝖪` (kernel). Fonts separate most of these; the `𝖧` and `s` clashes are in the same font. "Active cube" is used on line 71 before line 94 defines events; its meaning (the cubes of the half-tick's tiling) is clear from `W_h`. A frozen text should rename the subgroup and the specific entropy.

---

## 3. Checks behind the verdicts, section by section

### 3.A Section 0, section 1, section 2

**Premise quotations.** The six quoted refinements (PS-1c, PS-3h, PS-3c, PS-6r, PS-7r, PS-11c) were compared character by character with `TOE_ASSEMBLY.md` lines 178-183 `[check: exact string comparison]`. All six match exactly.

**Section 1, checked and correct:**
- Tilings, the action of `O` about `c_0`, and preservation of both tilings (`Q1−1∈2Z^3`).
- `[E_ℓ,J_ℓ]=J_ℓ`; `H_C` is even and Hermitian; each hop term `c_y^†J_ℓc_x` commutes with `𝒢_x` and `𝒢_y` (at `x` the change `−1` in `n_x` cancels `+1` in `E_ℓ`; at `y`, `+1` cancels `−1`).
- Cubes of one tiling are disjoint in sites and in internal links, so the factors of `M_e` (and of `M_o`) commute.
- Time convention: `β_0∘β_1(A)=(W_1W_0)^*A(W_1W_0)=α(A)` with `W_1W_0=W_EM_oM_e=U_0`, so `ω_{2n}=ω_0∘α^n`; and `ω_{h+1}(A)=tr(W_hρW_h^*A)`.
- `ν_ω` is well defined (with `σ` in the exponent): commuting projectors summing to `1`, consistent marginals, Kolmogorov extension on the compact product `{0,1}^{Z^3}`.
- `ν(ξ_x≠ξ_y)=ω(D_xy)`, since `(n_x−n_y)^2=n_x(1−n_y)+n_y(1−n_x)`. So `F_n` is PS-3c's criterion read on the law of the time-`2n` configuration (given Born one-time marginals; see item 62).
- `ω_G(c_y^†c_x)=G_xy` gives `G=P` for the state filling the range of `P`.
- Events: even cubes at even `h` give `X∈2Z^3`; odd cubes at odd `h` give `X∈1+2Z^3`.

**Distiller definitions 1-28.** Each was checked against the draft passage it cites.
- 1 (implementer normalisation). The draft (A1(5)) says "`Gamma(W)` is the unique number-conserving even unitary with `Gamma(W) c^dag(f) Gamma(W)^* = c^dag(W f)`". That relation fixes `Γ(W)` only up to a scalar phase. Fixing the empty vector removes it and gives `Γ(W_1W_2)=Γ(W_1)Γ(W_2)`.
- 2 (Heisenberg direction). Draft E1 defines `beta(a) = (prod g_j) a (prod ...)^*`, the Schrödinger direction, while draft E4 reads the evolved Born law as that of `U rho U^*`. They do not match; LW1's `A↦U^*AU` does.
- 4 (electric placement). `W_E` acts on links only and commutes with every `n_x`.
- 5 (spin range). A spin-`S` representation needs `2S∈N`.
- 6 (link reversal). `e^{iπS^x}` sends `S^z↦−S^z`, `S^+↦S^-`; a hop term on a reversed link maps to the `J^†` term of `H_C`; `𝒢_x` keeps its form; `W_E` is even in `E`.
- 7 (covariance lifts). A sign lift `D_dP_Q` is unique up to a global sign (a `±1` diagonal commuting with a connected nearest-neighbour hop is constant), so lifts compose up to a sign.
- 3, 8-17, 20, 22, 24, 27, 28: conventions that match their use in the cited proofs. (13: the history law does not depend on a kernel's values on a null set of inputs.)
- 18: correct given B10's band formula. 19: correct (B8b). 21: `e_4∉ℰ`, `2e_4∈ℰ`. 23: the gap is real (B9).
- 25 (record memory): a stated reading. It decides the meaning of "locks" in the Record axiom ("a record locks exactly one admissible local possibility") and in PS-3c ("it locks the site's actual value"). The stronger reading (later actual values at a recorded site stay equal to the record) is not refuted; it would constrain the transport.
- 26 (joint Born identification): a stated premise, not working-set text; PS-2's quotation is one-site.

**Section 2.** The law specification agrees with PS-6r ("Which gauge-invariant gates the update contains is part of the law choice in LW1, and each gate class carries its own named free constant"): the dressed gates are required, `W_E` carries `τ_E`, and the plaquette class is open by name. Section 2 calls `ω_P` the vacuum of the free tick only, in line with PS-7r ("For the gauged law, the vacuum is the state VC1 builds from this sea").

### 3.B Section 3.1 (geometry and finite gates)

- **Lemma A1.** Offset `o` holds both ends of `(x,x+e_i)` iff `x_i≡o_i (mod 2)`; exactly one offset fits, and the cube is unique. Face sign: for `i<j`, `η_i(x)η_j(x+e_i)η_i(x+e_j)η_j(x)=−1`. In one cube `A_i^2=I` and `A_iA_j=−A_jA_i` (the two paths round a face differ by the face sign), so `(A_1+A_2+A_3)^2=3I` and `R_C^2=I`.
- **Lemma A1a.** The Gray-code order is a Hamiltonian path on cube edges. Adjacent-row Givens elimination is standard QR; an upper-triangular unitary is diagonal. `Γ` is a homomorphism under the empty-vector normalisation; the lift of a two-mode Givens factor is an even edge gate; disjoint even gates commute.
- **Dressed factorization.** This is the standard proof that the group generated by the one-parameter groups `exp(tX_j)` is the analytic subgroup `𝖫` of the generated Lie algebra `𝔤`. `𝔳=span{Ad_hX_j}` is `ad_{X_j}`-invariant (differentiate inside a closed subspace), so it contains all iterated brackets; and `𝔤` is `Ad_h`-invariant, so `𝔳=𝔤`. The map `t↦∏_k exp(t_kY_k)` is smooth into `𝖫` (each factor is a one-parameter subgroup of `𝖫`) with invertible differential at `0`, so `𝖧` contains a neighbourhood of the identity, is open, hence closed, hence all of connected `𝖫`. `−iθH_C=θΣX_j∈𝔤`. Each letter is even, sits on one edge triple, and commutes with every `𝒢_x`. Cubes of one tiling carry translated words on disjoint supports.
- **GAP UALL.** The draft says (line 258) "The even operators supported on one edge triple ... generate as a Lie algebra all even operators of the cube system." `φ(X)=tr(𝒫_CX)` vanishes on even edge-triple operators and on brackets of even operators (`tr(𝒫_CYX)=tr(X𝒫_CY)=tr(𝒫_CXY)` for even `X`), but `φ(i𝒫_C)=i dim ℋ_C≠0`, and `i𝒫_C` is even. Referee closure for "at least one unused matter mode contributes `tr((−1)^n)=0`" (a Jordan-Wigner string can carry `(−1)^{n_z}` factors, so the factorised trace needs a word): take an unused mode `z` and the self-adjoint unitary `u=c_z+c_z^†`. It commutes with every even operator not involving `z` and anticommutes with `𝒫_C`, so `tr(𝒫_CX)=tr(u𝒫_CXu)=−tr(𝒫_CX)=0`.
- **Theorem A2.** Even translations fix both tilings and every `η_i`. For `Q∈O`, `x↦Qx+c_0−Qc_0` fixes each tiling; the pulled-back signs have face products `−1`, so their ratio to `η` is a flat `Z_2` edge function, equal to `d(x)d(y)` because every closed edge path in `Z^3` is a sum of face boundaries. Exclusion: with `R^2=I`, `V=(cos a_o+i sin a_oR_o)(cos a_e−i sin a_eR_e)`; `|⟨2e_i|V|0⟩|=sin a_e sin a_o/3>0` (one path, even edge then odd edge); from `t` with `t_i` odd the needed order is absent, so the entry is `0`; diagonal gauges keep moduli. Every orientation-preserving isometry is a `c_0`-rotation followed by an integer translation. Stabiliser: the identity and the two body-diagonal turns (a symmetry fixing `x` fixes `x`'s unique even cube). Window: `0≤μ<2ε<π` gives `0<a_e≤a_o<π`. Glide: `S=D_sD_dT_{(1,1,1)}` gives `SV_eS^{-1}=e^{ia_eR_o}` and `SV_oS^{-1}=e^{−ia_oR_e}`; these equal `V_o,V_e` iff `a_e=a_o`, that is `μ=0`, and then `SVS^{-1}=V_eV_o`.
- **Theorem A3.** `ℰ` is the set of integer 4-vectors whose coordinates share one parity, which is `2D_4^*`. Shortest vectors: the sixteen `(±1)^4` and the eight `±2e_j`, squared length 4. `Φ` halves squared lengths and maps `ℰ` onto `D_4` (integer coordinates with sum `v_1+v_3`, even); the stated inverse maps `D_4` into `ℰ`. The correction to the draft (draft A3: "the time direction `e_4` is a shortest vector") is right. Uses `kinetic_isotropy_primitive` for `cΔ=a`, as section 0 states.

### 3.C Section 3.2 (local frames and Gauss laws)

- **Theorem B2.** `W_{yx}=w_{y−x}`; `|w|=1` on the torus and uniqueness of Fourier coefficients give `ww^*=1` in `C[z^{±1}]`. Lexicographic order on `Z^d` is a total order compatible with addition, so the top exponent of a product is the sum of the top exponents. Hence `max supp w=min supp w` and `W=e^{iφ}T_a`; a site rotation conjugates `T_a` to `T_{Qa}`, a diagonal gauge keeps the displacement, so `a=0`.
- **Lemma B3.** `{d,c_y}=2(aI+bn_x)c_y`, so `(aI+bn_x)c_y=(aI+bn_x)c_y^†=0`; right-multiplying by `c_y^†`, `c_y` and adding gives `aI+bn_x=0`. Then `d^2=uvI=0` and `dd^†+d^†d=(|u|^2+|v|^2)I=I`. The map `c_x↦vc_x^†` satisfies the CAR, so it is an automorphism; conjugating `c_x↦uc_x` by it gives `c_x↦\bar u c_x`.
- **Theorem B4.** `[n_x,c_x]=−c_x` and `[E_ℓ,J_ℓ]=J_ℓ` give `[𝒢_x,A_ℓ]=0`; `[n_y,c_y^†]=c_y^†` and `−[E_ℓ,J_ℓ]` give `[𝒢_y,A_ℓ]=0`. In a plaquette monomial, at each corner the outgoing traversal has weight `+1` and the incoming one `−1`, for either link orientation.
- **Gauged covariance.** A hop term on a reversed link maps to the `J^†` term of the image link. A2's sign function `d` depends only on the geometric map and corrects the signs, because the dressed hop is symmetric under (reversal, `J↔J^†`) as the free hop is under reversal. Each tiling is preserved, so each cube Hamiltonian maps to the image cube's with the same angle; `E^2` is reversal-invariant. This proves `𝒢⊆Sym(U_0)`, which is what PS-1c asks. (A2's exactness is for the free `V`; exactness for `U_0` is neither claimed nor needed.)
- **Theorem B5(a).** A one-body unitary on a one-dimensional space is a phase.
- **B5(b) and GAP B5(b).** The draft's proof (line 264) says "The dressed gate of `C` is `Gamma(u_C)` times link factors", which is false for the dressed gate, and "with frames per cell, has no link registers inside `A`", while `L_cube` has twelve internal links per cube. Counterexample check: for `g=diag(e^{iθ_x})_{x∈A}`, combine with `e^{i(θ_{\rm source}−θ_{\rm target})E_ℓ}` on each link of the gate's own cube; a term `c_y^†J_ℓc_x` picks up `e^{iθ_y}e^{i(θ_x−θ_y)}e^{−iθ_x}=1`. This works for the even gate of `A` and for each odd gate (one corner of `A`, compensated on its three links in the odd cube).

### 3.D Section 3.3 (transport and records)

- **Lemma B6.** `P_AW=P_AWP_N`, so `p'(A)=tr((P_AW)X(P_AW)^*)≤p(N^t(A))`; with `A` the complement of `N(B)`, this gives Hall's condition `p(B)≤p'(N(B))`. Every cut not crossing a middle edge has capacity `1−p(B)+p'(D)≥1`, so a unit flow exists and saturates all source and sink edges.
- **Theorem B7.** A nonempty polytope; a nonempty compact convex face of cost minimisers; joint entropy is continuous and strictly concave, so the maximiser on the face exists and is unique.
- **Support factorization.** With a Jordan-Wigner order listing modes cube by cube, an even cube operator is a tensor factor, and `P_ζW_ΛP_ξ=⊗_CP_{ζ_C}W_CP_{ξ_C}` is nonzero iff every factor is. External even gates cancel from region expectations. `W_L` commutes with matter projectors and is invertible.
- **Theorem B8.** For `x≠y`, `ω_G(n_xn_y)=ω_G(c_x^†c_y^†c_yc_x)=G_xxG_yy−|G_xy|^2`, giving the displayed sum of three nonnegative terms. (For `0≤G≤I`, `G_xx∈{0,1}` already forces `G_xy=0`.)
- **Corollary B8a.** Correct given B10. Its scope is the free tick, as stated.
- **Theorem B8b.** (i) Each cube layer enlarges an occupation observable's support by at most one per coordinate, so the seven outputs depend only on even cubes within sup-distance 3 of `x`, all inside the empty cube. A state with `ω(N_C)=0` is supported on `ker N_C` (Cauchy-Schwarz), and `H_C` annihilates that subspace for any link state. The product hypothesis is not needed. (ii) `|ψ⟩` is a parity eigenvector, so `ω_ψ` is even; `ω_0=ω_ψ∘α^{-1}` is a state because `α` is an automorphism (E1); `ρ_1=ω_ψ` has both copies. See item 61 for the value law.
- **Theorem B9.** `t_x` is a deterministic function of the state sequence, so conditioning on formation adds no constraint on `ξ`. The all-empty and all-occupied matter states keep their occupation laws under `U_0` (`H_C` annihilates both, for any link state; `W_E` acts on links only), pass the copy test, and give different laws: the "varies with" clause. The support statement is a countable intersection of probability-one cylinder events, so under PS-11c(1) it holds in the realized history. See item 62.
- **GAP LW1-i/B9.** Both extensions are diagonal, hence even; their shell marginals agree; their copy pairs differ (`y_1,y_2` versus `y_3,y_4`); centre laws are `1/3` and `2/3`; both are reachable at tick one. The same pair also refutes the reading "conditions = the realized shell configuration": given the shell configuration `(b,b,1−b,1−b,0,0)` the locked value is `b` in one case and `1−b` in the other. What is proved is that the locked-value law is a function of the joint centre-and-shell reduced state (it is the centre's Born marginal). Whether Admissibility's "nearest-neighbor conditions" may include the centre is the owner-level reading LW1-i.

### 3.E Section 3.4 (the free sea, probability-one statements, dispersion)

- **Theorem B10.**
  - `{R_e,R_o}=(1/3)Σ_i(T_{2e_i}+T_{−2e_i})`: return paths would reuse one edge in both tilings; for `±e_i±e_j` the two paths use the tiling pairs `(p(x_i),p(x_j))` and `(p(x_j),p(x_i))`, so either neither contributes or both do with opposite signs; for `±2e_i` the one path has opposite ownership and sign product `1`.
  - `V+V^*=2cos a_e cos a_o+sin a_e sin a_o{R_e,R_o}`, so each fibre eigenvalue has real part `a_bandχ−b_band` (`sin a_e sin a_o=(cos μ−cos 2ε)/2`, `cos a_e cos a_o=(cos μ+cos 2ε)/2`), ranging over `[cos 2ε,cos μ]`.
  - Multiplicities: fibre hops change the residue, so `tr R_T(K)=0` and `det V(K)=1`; where `w/π` is irrational, `e^{iw(m_+−m_−)}=1` forces `m_+=m_−=4`; Riesz projections are continuous where the eigenvalues differ; `T^3` and `T^3∖{0}` are connected.
  - `ΘVΘ^{-1}=V`; an antiunitary commuting with `V` exchanges the `e^{∓iw}` eigenspaces; the cuts carry no spectral projection; so `ΘPΘ^{-1}=I−P` and `P_xx=1/2`.
  - Item 3 uses the standard quasi-free existence and purity results (Powers-Størmer, Araki); the evolved covariance is `VPV^*=P`.
  - Item 4: the Combes-Thomas argument is complete (`|e^{t(f_N(x)−f_N(z))}−1|≤e^{tr}−1` on the range, Schur test, Neumann series, `f_N(y)=0`, `N→∞` at fixed `x`); the Riesz projection of a normal operator is its spectral projection.
  - `[check: 200 random fibres at (ε,μ)=(0.7,0.3): real parts match a_bandχ−b_band to 2e-15, eight eigenvalues split 4+4; on an L=8 torus, max|P_xx−1/2|=3e-14.]`
- **Theorem B11.** Singletons are measurable, so for an atomless law the singleton complements are probability-one events with empty intersection. `ω_P(∏_Fn_x)=det P_F≤∏P_xx=2^{−|F|}` (Hadamard), and `det(I−P)_F` for holes. The tracial state is stationary because each local Heisenberg image is a unitary conjugation. Each frequency is a finite average of cylinder indicators, so the convergence events are Borel; countable subadditivity gives probability one. Consistency only is claimed.
- **Theorem C1.** At `μ=0`, `1−cos w=s_ε^2(1−χ)`. With `u=w^2=Ak^2+Bk^4+O(k^6)`: `A=s_ε^2/3`, `B=A^2/12−s_ε^2T_4/36`; then `w=√A k(1+(B/2A)k^2+O(k^4))`, `B/2A=s_ε^2/72−T_4/24`; `k=2|q|` gives `−T_4|q|^2/6`. `[check: at k=0.05 along three directions the remainder is O(k^4) relative.]`
- **Theorem B12.** The slice-preserving property is the theorem's hypothesis. The linear part must preserve `e_4^⊥`, hence the line of `e_4`. Swapping coordinates 1 and 4 preserves `ℰ` and moves `2e_4` to `2e_1`. The stabiliser of `e_4` permutes `{±2e_i}`, so it is the 48 signed spatial permutations, all of which preserve `ℰ`; with time reversal, 96.
- **GAP B12(ii-iii).** The draft's scalar step (line 375: "exponentially local", which is not "finitely many layers of nearest-neighbour gates") is a non sequitur, since a finite-depth circuit is exponentially local. The fermion step rests on quotations only.

### 3.F Section 3.5 (infinite volume)

- **Theorem E1.** A gate `g_k` disjoint from `F` commutes with `A` and with the listed gates `G`, so `(Gg_k)^*A(Gg_k)=G^*AG`. The inverse uses `g_j^*`. The map is isometric on the local algebra and extends. Gauge exponentials are fixed by B4.
- **GAP E2a-0 (closed by the distiller).** At `μ=0`, `K≠0`, `(V−V^*)/(2i)` is `±sin w` on the two eigenspaces, and `√(1−g^2)=sin w>0` since `0<w≤2ε<π`, so the formula is the negative-quasi-energy projection. `1−g^2≍|K|^2` with derivative `O(|K|)`, so `‖∂_jP‖≤C/|K|`, integrable in three dimensions; the excised-ball boundary term is `O(r^2)`; one integration by parts gives `|P_xy|≤(2π)^{-3}‖∂_jP‖_{L^1}/|d_j|`.
- **Theorem E2b.** The telescoping bound gives stationarity. Spatial and gauge actions commute with `α`. Every 2x2x2 cube holds one site of each residue class, so in a cell-invariant state every cube has expected number `8ρ`; each half-layer conserves `N_C` on its cubes and keeps cell invariance, so `ρ` is preserved. The tracial state is a witness.
- **Theorem E3.** If `ω_0∘γ=ω_0` and `γα=αγ`, then `ρ_n∘γ=ρ_n` and `γ(D_xy)=D_{g(x)g(y)}`.
- **Theorem E4.** B6 on exhausting unions; Prokhorov on a compact metrizable space; clopen cylinders carry marginals and support zero-sets to the limit; Følner averaging gives invariance.
- **Theorem E5.** Disintegration and Ionescu-Tulcea give the Markov measure; induction gives Born marginals; pair marginals are the `γ_h`. B9 is cited only after the marginals are established.
- **Theorem E6.** `𝒞_h` is nonempty, compact and convex; `d̄` is continuous and affine; dyadic subadditivity makes `H_{Q_m}/|Q_m|` decreasing, so `s` is an infimum of continuous functions (upper semicontinuous); the mixture bound gives affinity; superlevel sets of an upper semicontinuous function are closed.

### 3.G Section 4 (open statements)

- **LW1-U and its attacks.** See items 78-81 and section 2.3.
- **GA1-P commutator.** With `B_p=JA+J^†A^†`, `B_q=JB+J^†B^†` and `A,B` commuting with each other and with `J`: `[JA,JB]=J^2[A,B]=0`, `[JA,J^†B^†]=[J,J^†]AB^†`, `[J^†A^†,JB]=−[J,J^†]A^†B`, and `[J,J^†]=2E`. Nonvanishing: put each link of `A` at the extremal weight that `A^†` annihilates and `A` does not, choose the `q`-links so `B^†` acts nontrivially, and put `ℓ` at `m=S≠0`. `[check: identity holds to 1e-15 for S=1/2 and S=1, commutator nonzero.]`
- **GAP LW1-ii/F, referee closure (negative).** Let `Λ` be a finite union of even cubes and `Λ'⊇Λ` a larger one, chosen so that the odd cubes crossing the boundary of `Λ'` do not meet `Λ`. Evolve each as a closed system whose box dynamics conserves the box's particle number (gates that cross the box boundary omitted, or replaced by number-conserving gates inside the box). Take `S=1/2`. Pick `x∈Λ` whose odd cube `C` lies in `Λ'` but not in `Λ`, and a neighbour `y∈C∖Λ`. Choose the half-tick-1 state as a product over odd cubes (and even links):
  - In `C`: `x` occupied, `y` empty, every other site occupied. The link `ℓ` between `x` and `y` is at the weight that allows the hop `x→y`. The two other links of `C` at `y` are at the weights that block hops into `y`, and the two other links of `C` at `x` at the weights that block hops into `x`. (For `S=1/2` each hop direction on a link is open at exactly one weight. The four links are distinct, since adjacent `x,y` have no common neighbour in the cube.)
  - Every other odd cube in `Λ'` is completely full or completely empty, so its gate acts trivially.

  Pull this state back through the even layer, which is internal to both boxes, so both boxes start from restrictions of one state. In `C`, the only open move is `x→y`, and after it the only open move is `y→x`. So `H_C` preserves the two-dimensional span of these two configurations and acts there as `1/√3` times a phase-twisted Pauli flip. In `Λ'` the particle leaves `Λ` with probability `sin^2(a_o/√3)>0` for every `0<a_o<π`; in the closed box `Λ`, `N_Λ` is conserved. So the laws of `N_Λ` at half-tick 2 differ, and `(res_{Λ'→Λ})_*ℚ_{Λ'}≠ℚ_Λ`. (For the free tick the same holds with one particle, since the hop amplitude is `i sin a_o η/√3≠0`.) One-time Born marginals do not depend on the transport, so no choice of `Act` can repair this.
- **GAP LW1-N.** The per-site cost and the specific entropy need invariance. The B8b witnesses are not invariant, so `Act` is undefined for them at infinite volume. Their record-value laws are one-time Born marginals, so B8b and B9 do not depend on `Act`.
- **GAP LW1-R.** The tracial state is stationary for `U_0`, has independent fair bits, so `ρ_n(D_xy)=1/2` and `F_n=∅` for every `n`.
- **GAP B5(b), GAP B12(ii), GAP B12(iii), VC1, LW1-edge.** As in 3.B, 3.C and 3.E.

**Lean-formalizability.** Every argument has finitely many steps and uses named standard results: the analytic subgroup and inverse function theorems, Givens QR, max-flow min-cut, Kolmogorov extension, Wick's rule, Hadamard's inequality, the Powers-Størmer and Araki results on quasi-free states, the spectral theorem and Riesz projections, Banach-Alaoglu, Prokhorov, disintegration, Ionescu-Tulcea, Følner averaging, and Shannon entropy subadditivity. The Combes-Thomas bound and the scalar-walk theorem are proved in the text. No numerical check is used as a proof; LW1 says so (line 15) and none was found.

---

## 4. Freeze recommendation

LW1 can be frozen with its open statements named, after a short list of edits. Every result that LW1 marks as proved was re-derived and holds, including the three steps the distiller closed (the dressed factorization, the event-lattice similarity, and the massless decay bound). The three ERRORs are a typo (line 61), a line citation (line 11) and one overstated sentence (line 464). The four INCOMPLETE items are a missing hypothesis in B8b and B9, an ambiguous `Act` clause in section 2, and per-result premise tags. These must change first:
1. Line 61: replace `χ_x` by `σ_x`.
2. Line 11: cite lines 167-185.
3. Line 464: "no recovery sequence has been constructed that matches ...".
4. B8b and B9: state "for any history measure `ℚ` whose one-time marginals are the `ν_h`" (B7, E5), and replace `ℙ` by `ℚ` in B9.
5. Section 2: restrict the B7 `Act` clause to closed finite systems, and point to LW1-N for non-invariant infinite states.
6. Premise tags: add PS-3c to B8b, B9 and E3, PS-4 to B8b, and PS-3h to E4; write the refined entries as "PS-1 under PS-1c" and so on; drop PS-2 or show its use; say whether `realized_state_primitive` is used; list the joint Born identification and the record-memory reading as premises or readings outside the working-set text.
7. Reconcile the text of LW1-U with the branch work in `58d5c77701` (non-factor states) before its statement is frozen.
8. Add to LW1-ii/F that the closed-box reading is false (section 3.G), so target item 3 needs an owner reading rather than a proof.

The open statements to carry, by name: LW1-U; LW1-i/B9 (owner reading of "conditions"; the shell-only reading is false); LW1-ii/F (owner reading of item 3); LW1-N; LW1-R (owner decision on the domain, or the reading of "Records form."); B5(b); B12(ii); B12(iii); GA1-P; VC1. Optional before freeze: rename the subgroup `𝖧` and the specific entropy `s`, and add "each sublayer of commuting gates" to the statement of E1. With these changes the frozen LW1 does not establish the assembly target; it records what is proved toward it and names the open items exactly.
