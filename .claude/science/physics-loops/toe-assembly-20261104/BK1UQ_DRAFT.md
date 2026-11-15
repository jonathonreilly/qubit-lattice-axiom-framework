lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# BK1-UQ: the strict-path charge-capacity obstruction, pass 1

Written 2026-11-09 by a Claude Opus 5.5 headless lane on the Mac mini, as a pass-1 lane of the TOE assembly (part BK1, wall W4, leaf UQ of `BK1_TREE.md`, rank 1). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. Every result below is proved by finite algebra (spectral blocks, CAR words, representation theory of `U(5)`), in a form a Lean formalization can follow. One "[check]" (after Lemma 5.4) is a tiny scratch computation, `check_bk1uq.py` in `/tmp/toe-BK1UQ/scripts/` (sparse matrices on the 1024-dimensional Fock space of one link's ten rishon modes, about 2 s, peak memory about 36 MB, started at 53 percent free memory). A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (working tree, HEAD) | `b5bf445d7` |
| `origin/docs/consolidate-gauge-matter-registers` (PR #10126; `git fetch -q origin <branch>`, then `git show <commit>:<path>`) | `7086189d10` |
| `origin/main` (same method) | `43a1fcc374` |

Files read, by line, at those commits (`T/` is this folder; last-change commit in brackets). `T/prior/BK1UQ.md` lines 1-65, all [`b5bf445d7`]. `T/BK1_TREE.md` lines 1-708, all [`a6291aad1`]; node UQ is lines 232-306, Lane 1 is lines 681-691. `T/EW1.md` [`12fb546f8`]: lines 1-60 (status, §2.1-2.4), 60-135 (Definition 2.5, §3, Theorem 4.1), 236-345 (§§5-6, including Lemmas 6.1-6.4, Theorem 6.3′, Proposition 6.5), 345-399 (§6.6, §7, §8). `T/LW1_5.md` [`4d1379fd8`]: lines 1-12 (status), 80-146 (§2 laws, §3, §4 Q, G, R, U), 228-262 (§6: (6.1), Σ-U, Z-U, H-U, the exterior-power embedding). `T/TOE_ASSEMBLY.md` [`15d00adcf`]: lines 169-190 (§3.2, the four tests), 201-270 (§§3.4-3.11), 743-759 (§11). `T/GA1_5.md` lines 1-8 [`913ef70a5`], `T/VC1_5.md` lines 1-8 [`727ad9884`], `T/VC1_5U_ODD.md` lines 1-8 [`c4e7cfa88`] (status blocks; no result of these three is used below). `T/CH1_5UQ.md` lines 3-6 and 116-126 [`1be8b7478`]. `T/GA2_Y2.md` lines 36-48 and 80-92 [`2ca9262f0`]. `T/Y2W_DRAFT.md` lines 1-40 (head format only). PR #10126 branch: `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 9-12 and 255-280. Main: `docs/RECORDS_REGISTER_COLOUR_ONLY_THROUGH_TRIALITY_AND_SINGLETS_THE_SU3_CASE_BOUNDED_THEOREM_NOTE_2026-09-04.md` lines 12-16 and 48-58.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U[m]`, EW1's definitions and BK1's root statement are read plainly. Two candidate transporter classes, C-SPLIT and (for `m ∈ {1, 9}` only) C-SPLIT-M, are stated in §8 for the owner, four-tested in §9, and not adopted.

**Working set used, by name.** PS-5 (five modes per site) and PS-6r (finite link registers), only through the law `L5-U[m]` of frozen `LW1_5.md` §2 (line 96). Frozen definitions used unchanged: EW1 Definitions 2.2 (bosonic composite), 2.3 (path transporter), 2.4 (the standard `H`) and 2.5 (R-FMS). BK1's root statement and node UQ are read from `BK1_TREE.md`, an unchecked sketch; each statement of it used below is checked first (§3.5). No other working-set entry is used. No energy reading, no tick, no stationarity and no vacuum property is used: every result below holds for every state of the quasi-local algebra.

**Inputs from outside the working set.** Standard finite-dimensional linear algebra, rebuilt where used: diagonal operators and their matrix entries, the canonical anticommutation relations (CAR) on finitely many modes, Schur's lemma for a central element acting on an irreducible representation, and orthogonality of eigenspaces of a unitary matrix for distinct eigenvalues. Literature (§2) is context and credit only; no proof step depends on it.

---

## 0. The question, quoted

`BK1_TREE.md` lines 683-689, Lane 1: "Fix EW1's transporter definition without alteration. Prove that every nonzero bosonic \(H\)-fixed charged component has charge in \(10\mathbb Z\). Prove that its single-link representation matrix vanishes on every \(L5\)-U\([m]\). Derive the two transport-defect floors." Then: "Use central characters and spectral blocks first. Use weights and CAR normal ordering second." Stopping rule: "a complete proof; an explicit admissible counterexample; or one unresolved lemma that fails all three attacks: **reducible-carrier decomposition**, **reverse and repeated-path ordering**, and **representation-projection multiplicities**." Last: "Then state the smallest network extension that removes the proved hypothesis. Do not claim that extension satisfies FMS."

`BK1_TREE.md` lines 234-248, node UQ: "Fix \(L5\)-U\([m]\), \(1\le m\le9\). Use exactly EW1 Definitions 2.2–2.5. Suppose \(H\subseteq\operatorname{Stab}(v)\), \(U(1)_{\rm centre}\not\subseteq\operatorname{Stab}(v)\). Then every strict transporter has a vanishing charged summand. Consequently, \(\omega(\|T^\dagger T-I_W\|_{\mathrm{HS}}^2)\ge1\), \(\omega(\|TT^\dagger-I_W\|_{\mathrm{HS}}^2)\ge1\). This would obstruct strict R-FMS BK1 on every live U-law register. This is a new candidate lemma. It is not a frozen negative." (Displays flattened to one line here.)

The root it serves, `BK1_TREE.md` lines 15-56 (`H` at line 17, `K_G` at line 36, the stabilizer clause at line 47): \(H=S(U(3)\times U(2))\); on the U branch \(Z_F=\{\pm I_5\}\) and \(K_G=HZ_F\); the proposed theorem asks for \(\operatorname{Stab}_G(v)=K_G\) and, for every \(\delta>0\), FMS data at tolerance \(\delta\) with the law, register, vacuum, representation and orbit point fixed before \(\delta\). Its clause (T) reads \(\omega(\|T_{XY}^\dagger T_{XY}-I\|_{\mathrm{HS}}^2)\le\delta\) and \(\omega(\|T_{XY}T_{XY}^\dagger-I\|_{\mathrm{HS}}^2)\le\delta\), with \(T_{YX}=T_{XY}^\dagger\). These are EW1's clauses (`EW1.md` line 66 onward, Definition 2.5).

"Strict" means EW1 Definition 2.3 (`EW1.md` line 50): "`𝒯_π := σ(𝐔_{ℓ_1}^{(ε_1)}/c) ⋯ σ(𝐔_{ℓ_N}^{(ε_N)}/c)` … For traversal in the reverse direction use its matrix adjoint, with the operator products reversed … A *transporter* from `z` to `z′` is a convex combination `T = Σ_{π∈Π} c_π𝒯_π` over a fixed finite set `Π` of paths from `z` to `z′`."

## 0.1 Outcome in one paragraph

**Proved, for every `m ∈ {1, …, 9}`, every state, every block size, every finite path set and every normalization `c > 0`.** No admissible counterexample exists, and no residual lemma is left for UQ. (i) **Charge (Theorem A).** Every summand of a bosonic composite on `L5-U` has even central charge (a port of frozen EW1 Theorem 4.1(1), rebuilt). If `H ⊆ Stab(v)` and `v_r ≠ 0`, then `5 | q_r`, because `e^{2πi/5}1_5 ∈ H`. So every nonzero `H`-fixed charged component has `q_r ∈ 10Z ∖ {0}`. A second proof uses weights: `H`-fixed vectors have only weights `(n, …, n)`. (ii) **Vanishing (Theorem B).** On one link of `L5-U[m]`, every operator matrix that is covariant at one end with central charge `q`, `|q| > d_m := min(m, 10 − m)`, is zero. Since `d_m ≤ 5 < 10`, the single-link representation matrix `σ_r(𝐔_ℓ/c)` and its adjoint vanish for every such summand, every link, every `m`, every realization `σ_r ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` (any copy, any `(p, p′)`, any factor order). A second proof counts CAR letters. (iii) **Floors (Theorem C).** Every strict transporter between distinct sites is zero on the subspace `W_cap` of all summands with `|q_r| > d_m`. Hence `‖T^†T − 1‖²_HS ≥ dim W_cap ≥ 1` and `‖TT^† − 1‖²_HS ≥ dim W_cap ≥ 1` as operator inequalities, so in every state. For `W = det^{±2}` both floors equal 1 and are attained. Corollary C.2 adds an alignment floor from (O), (C) and (A). Corollary C.3: strict R-FMS BK1 fails on every `L5-U[m]` at every tolerance `δ < 1`. **Attacks (§7).** The three named attacks fail to break the proof; so do two further variants (summand mixing, projection after the path product). **Network extension (§8).** The proved hypothesis is "one strand per summand: each link factor carries the full summand". The smallest change that removes it is candidate **C-SPLIT**: `k` strands joined only at the two endpoint sites by one fixed equivariant isometry `J`. Theorem D proves a converse count: a nonzero link-only charged block needs at least `⌈|q|/d_m⌉` links at each endpoint, and at `m ∈ {1, 9}` no link-only operator carries `|q| > 6` at a site. Proposition E: C-SPLIT has a nonzero charge-ten block for every `2 ≤ m ≤ 8`, with `⌈10/d_m⌉` strands. For `m ∈ {1, 9}` matter at both endpoints is necessary (Theorem D(ii)); candidate **C-SPLIT-M** adds it, and Proposition G gives a nonzero block. **Nonvanishing is not near-unitarity (Theorem F).** For any transporter class, `D_+ + D_− ≥ dim W_r` whenever `2|q_r|` exceeds the spectral diameter of the centre's action at the endpoint (`6d_m` for link-only entries, `5 + 6d_m` in general). So for charge-ten data carried at block sites, (T) fails below `½` for every charge-diagonal transporter on `m ∈ {1, 2, 8, 9}` and for every link-only transporter on `m ∈ {3, 7}` (Corollary F.1); and at `m = 5` the minimal two-strand transporter on one path pair still has `max(D_+, D_−) ≥ ½` (Proposition F′). No FMS property of either candidate is claimed. **Open by name, outside UQ:** T1-SPLIT (§8.7), two-sided transport of `det^{±2}` on `L5-U[4]`-`L5-U[6]` (link-only) or `L5-U[3]`-`L5-U[7]` (with endpoint matter).

## 1. Prior work used

Paths are relative to this folder unless a branch is named. Each item says what is ported, what is extended, and where it enters.

1. **Even central charge of bosonic composites.** Frozen `EW1.md` Theorem 4.1(1) on `L5-U` (lines 118-127): "Split `Φ^i = Σ_qΦ^i_q` into `Q_x`-charge components … So `Φ^i_q` has parity `(−1)^q`. `Φ^i` is even, so only even `q` occur". It rests on frozen `LW1_5.md` Z-U (line 242): "A local operator with definite \(Q_x\) charges has total charge equal to its matter-number change, and its matter parity is \((-1)^{\sum q_x}\)." Ported and rebuilt as Lemmas 4.1-4.2.
2. **The fifth root of unity lies in `H`.** Frozen `EW1.md` Proposition 6.5(1), proof (line 338): "`e^{2πi/5}1_5 = (e^{2πi/5}1_3) ⊕ (e^{2πi/5}1_2)` has determinant `e^{6πi/5}·e^{4πi/5} = 1`. For the standard ratio `π(H) = S(U(3) × U(2))`, so this element lies in `H`." Ported as Lemma 4.3, extended by the converse (the centre meets `H` exactly in the fifth roots).
3. **End-number interval.** Frozen `EW1.md` line 274: "each end number `N^x_ℓ := p_{ℓ,x}` takes the `K_m` consecutive values `max(0, m−5), …, min(5, m)`", citing frozen `GA2_Y2.md` Theorem 3.2 (line 85), "For L5-U let \(K_m=\min(m,10-m)+1\)". Rebuilt as Lemma 3.1, with `d_m = K_m − 1`.
4. **Letter count of a projected link product.** Frozen `EW1.md` §2.3 (line 44): "the centre `e^{iθ}1_5` acts on an irreducible `σ_r ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` by `e^{iq_rθ}` with central charge `q_r = p′ − p`." Frozen `EW1.md` Theorem 6.3′, lower bound (line 319): "An entry of `σ(𝐔)` with `σ ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` has `p` factors `U` and `p′` factors `U^†`, and `p − p′ = −q` in the creator convention." EW1 uses this for a floor. The vanishing conclusion drawn from it here (Theorem B, second proof) is new in the material searched.
5. **Graded floor.** Frozen `EW1.md` Lemma 6.3a (line 300) and `GA2_Y2.md` Theorem 3.2. For one link and `|q| ≥ K_m` the floor reads `2|z|^2`, which is the value of the left side at `Y = 0`. Theorem B says that this is not a coincidence: `Y` itself is zero there. Not used as a proof step.
6. **Block-diagonal transport and the cross-term argument.** Frozen `EW1.md` Lemma 6.4(3), proof (line 330): "`σ(𝐔)` is block diagonal over the fixed summands (§2.3), so `T_{XY} = ⊕_rT_r`", followed by the (O)-(C) estimate of the charged norms. Corollary C.2 reuses that estimate verbatim in structure; the step that kills the cross term changes from "sharp block matter" to "`T_r = 0`".
7. **Adjoint reversal.** Frozen `EW1.md` Definition 2.3 (line 50) and §8 item 1, the reverse-order counterexample ("In the `m=1` sector with `(N_x,N_y)=(1,0)` these are `1` and `0`"). Used unchanged in Theorem C and in Attack 2.
8. **Capacity method for a charge-three hop.** Frozen `CH1_5UQ.md` Theorem 5.1 (lines 120-122): the triple hop "is nonzero exactly when `3≤m≤7`", because "otherwise the operator, which raises `p_{ℓ,x}` by three, vanishes". Theorem B is the same mechanism for every single-link covariant matrix. Proposition E's nonvanishing proof (one surviving term between occupation basis vectors) follows the same pattern as its "no cancellation occurs".
9. **No invertible covariant link.** Frozen `GA2_Y2.md` Corollary 2.2 (line 43): "no invertible covariant link". Context: Theorem B is the stronger statement "zero" in the range `|q| > d_m`.
10. **Singlet criterion and the explicit exterior-power embedding.** Frozen `LW1_5.md` line 240 ("products \(\bigotimes_i\Lambda^{a_i}\mathbb C^5\) have an \(SU(5)\) singlet iff \(\sum_i a_i\equiv0\pmod5\)") and line 250 (the explicit maps). Rebuilt in Lemma 8.3 and used for the splitting isometry `J`.
11. **Repository rungs, author statements.** PR #10126 branch, `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` line 263, item 1: "U is nilpotent (U^2 = 0), not unitary"; item 5: "The det term, a colour-singlet rishon triple crossing the link, is SU(3)-invariant but changes the x-cluster's end number by 3". Main, `docs/RECORDS_REGISTER_COLOUR_ONLY_THROUGH_TRIALITY_AND_SINGLETS_THE_SU3_CASE_BOUNDED_THEOREM_NOTE_2026-09-04.md` line 53: "products U U = 0 on the one-rishon factor" (status line 14: "conditional supplied-model mathematics"). These are the smallest cases of Theorem B. Not used as proof steps.
12. **The tree's sketch.** `BK1_TREE.md` lines 250-306 (node UQ, both routes and the escape). Each statement is checked in §3.5 before use. The sketch is correct as far as it goes; its named first hard step ("certify the charge identity for every allowed projected representation, including multiplicities and ordering", line 288) is discharged by the covariance form of Theorem B, which does not depend on how the matrix was built.

**Prior work the digest missed.** (a) The word-count line of `EW1.md` Theorem 6.3′ (line 319, item 4 above): it already contains `[E_S, 𝒯_π] = −q𝒯_π`, which for `S` one link and `|q| ≥ K_m` gives vanishing. The digest cites Theorem 6.3′ only for its floor. (b) `EW1.md` line 105, R-FMS test 4: "without this restriction (A) is empty, since for a composite built from link operators only, `T := Φ_XΦ_Y^†/|v|^2` is a covariant link-only operator". This bounds every network extension: the transporter class must be fixed independently of `Φ` (used in §9). (c) `LW1_5.md` lines 240 and 250 (item 10). (d) `EW1.md` Lemma 7.2 (tracial state), a state-specific vanishing of cross terms; not used.

**Failed attempts on file, and why none is repeated.** The digest lists five. None is a step of the proofs below. Same-order reverse evaluation is not used (Definition 2.3's adjoints are). The omitted-(C) gap does not arise: Theorem C needs no (O), (C) or (A), and Corollary C.2 carries (C) explicitly. One-link quality, cut floors, collective states and the blanket triple exclusion concern other questions; Theorem B uses the exact charge `|q| ≥ 10 > 5 ≥ d_m` and so does not meet CH1-5U-q's refutation, which concerns charge 3.

## 2. Literature

Searched before building (2026-11-08): the rishon representation of `U(N)` quantum links and its determinant term; quantum link models; FMS; Fradkin–Shenker and Osterwalder–Seiler complementarity; Elitzur; Maas and collaborators on gauge-invariant spectra; charge-two Higgs fields on truncated or quantum links; rishon tensor networks. Each work below was fetched; the line says what was read. Where text could not be fetched the entry says **NOT VERIFIED**. No result below is a proof step. Every result used is proved natively in §§3-8.

- **L1. Brower, Chandrasekharan, Wiese, "QCD as a Quantum Link Model"**, arXiv:hep-th/9704106v1 (submitted 14 Apr 1997), Phys. Rev. D 60, 094502 (1999). Read: abstract page and the arXiv PDF text, §4, eqs. (4.1)-(4.7), printed pp. 14-15. Eq. (4.3): "\((U_{x,\mu})_{ij}=c^i_{x,+\mu}c^{j\dagger}_{x+\hat\mu,-\mu}\)". After (4.3): "all operators introduced so far (including the Hamiltonian) commute with the rishon number operator" (4.4) "on each individual link. Hence, we can limit ourselves to superselection sectors of fixed rishon number for each link." After (4.6), for \(\det U_{x,\mu}=N!\,c^1_{x,+\mu}c^{1\dagger}_{x+\hat\mu,-\mu}\cdots\): "Only when this operator acts on a state with exactly \(\mathcal N=N\) rishons (all of a different color), it can give a non-zero contribution. In all other cases the determinant vanishes." **Bearing.** This is the published special case "charge `N` on one link of `2N` rishon modes" of Theorem B below: with `N = 5`, `d_m ≥ 5` holds exactly at `m = 5`. L5-U's `U^{jk} = r^y_jr^{x†}_k` is BCW's (4.3) with the two ends relabelled. BCW use the determinant as a term of the Hamiltonian; it reduces `U(N)` to `SU(N)`. Here it appears only as a transport factor; the law is unchanged.
- **L2. Chandrasekharan, Wiese, "Quantum Link Models: A Discrete Approach to Gauge Theories"**, arXiv:hep-lat/9609042v2 (v1 26 Sep 1996, v2 31 Dec 1996), Nucl. Phys. B492 (1997) 455. Read: abstract page and the PDF text, §3, eqs. (3.14)-(3.16), printed p. 9. Eq. (3.16): "\(U_{x,\mu}=C_{x,\mu}+iS_{x,\mu}=S^1_{x,\mu}+iS^2_{x,\mu}=S^+_{x,\mu}\)", "i.e. a link variable is represented by a raising operator \(S^+_{x,\mu}\), and its inverse by the lowering operator \(S^-_{x,\mu}\)", and "the above commutation relations can be realized with any representation of SU(2)." **Bearing.** On a spin-`S` link, `(S^+)^k = 0` for `k > 2S`. This is the Abelian rung of Theorem B (Corollary 5.3).
- **L3. Banerjee, Bögli, Dalmonte, Rico, Stebler, Wiese, Zoller, "Atomic Quantum Simulation of U(N) and SU(N) Non-Abelian Lattice Gauge Theories"**, arXiv:1211.2242v2 (v1 9 Nov 2012), Phys. Rev. Lett. 110, 125303 (2013). Read: abstract page only. It concerns `U(N)` and `SU(N)` quantum link models with fermionic matter. Its rishon content: **NOT VERIFIED** (the abstract does not mention rishons, and the text was not read). Context only.
- **L4. Fröhlich, Morchio, Strocchi, "Higgs phenomenon without symmetry breaking order parameter"**, Nucl. Phys. B190 [FS3] (1981) 553; preprint IHES/P/81/12; no arXiv version. Read: the IHES scan's text layer, abstract (printed p. 1) and §5.1 (printed pp. 23-29). Abstract: "A complete set of gauge-invariant, observable composite fields for such theories, local ones and ones localized near strings (paths) is constructed." §5.1, printed p. 29: "let Ψ(φ) and Ψ'(φ) be two covariant fields transforming under the same representation Rψ of G. Then we form the field" [the displayed formula did not survive text extraction] "which is localized on the path ("string") connecting two points x and y." **Bearing.** EW1's strict path transporter is the quantum-link operator form of the representation matrix that FMS place on the path. On group-valued links that matrix is unitary. Theorem B shows that on `L5-U` it is zero for every bosonic `H`-fixed charged representation. So FMS's string construction does not port to `L5-U` strictly.
- **L5. Fradkin, Shenker, "Phase diagrams of lattice gauge theories with Higgs fields"**, SLAC-PUB-2238 (November 1978), "Submitted to Physical Review D"; no arXiv version. The journal reference Phys. Rev. D 19, 3682 (1979) is taken from `BK1_TREE.md` and was **NOT VERIFIED** here. Read: the preprint text (inspirehep file named in `BK1_TREE.md`), §1, printed pp. 8-9: "if the gauge group G has a non-trivial center C (like ZN for SU(N)) it is possible to introduce Higgs fields that transform trivially under the center of G (e.g., in the adjoint representation). If we introduce enough Higgs fields so that the gauge invariance G/C is completely broken in the unitary gauge (φ = constant vector), a leftover local C-invariance will still survive even at β = ∞." **Bearing.** The determinant-square carrier is blind to the tenth roots of unity in the centre of `U(5)`; with `H` this is the group `K_G = H{±1_5}` of the root theorem (Lemma 4.3(b)). The fully screened, complete-breaking hypothesis of the complementarity results does not hold for this carrier. Context only.
- **L6. Osterwalder, Seiler, "Gauge field theories on a lattice"**, Ann. Phys. 110 (1978) 440. Full text **NOT VERIFIED** (not found online). Its complementarity statement is recorded through **Seiler, "On the Higgs-Confinement Complementarity"**, arXiv:1506.00862v1 (2 Jun 2015), abstract read: in Higgs models with complete symmetry breaking "one can move from the confinement to the Higgs regime without crossing a phase boundary". Context only.
- **L7. Elitzur, "Impossibility of spontaneously breaking local symmetries"**, Phys. Rev. D 12, 3978 (1975). **NOT VERIFIED**: the APS page returned HTTP 403; only a search-engine record was seen. EW1 cites it as "Elitzur's point" when it rejects R-VEV (`EW1.md` §3). Not used.
- **L8. Maas, "Brout-Englert-Higgs physics: From foundations to phenomenology"**, arXiv:1712.04721v4 (v1 13 Dec 2017, v4 11 Feb 2019), Prog. Part. Nucl. Phys. 106 (2019) 132. Read: abstract page. A review of gauge-invariant (FMS) treatments of Higgs physics. Context only.
- **L9. Maas, Sondenheimer, Törek, "On the observable spectrum of theories with a Brout-Englert-Higgs effect"**, arXiv:1709.07477v3 (v1 21 Sep 2017), Ann. Phys. 402 (2019) 18. Read: abstract page. It says that the FMS link between elementary and gauge-invariant states "does not necessarily hold" beyond the Standard Model and studies GUT-like cases. Context for BK1's later channels (F1, M1); not used here.

**What the search did not find.** No published statement of the general lemma "on a fixed-number `U(N)` rishon link, every operator covariant at one end with central charge exceeding `min(m, 2N − m)` vanishes" was found. L1 and L2 are its closest published cases. Searches on charge-two Higgs fields on quantum links and on rishon tensor networks returned only lattice gauge-Higgs studies and a bibliographic record (Silvi, Rico, Calarco, Montangero, "Lattice gauge tensor networks", New J. Phys. 16 (2014) 103015; its arXiv number was not confirmed, **NOT VERIFIED**); none bears on the proofs.

## 3. Definitions, rebuilt

### 3.1 The link register and its end numbers

Frozen `LW1_5.md` line 96: "Each link carries \(\Lambda^m\mathbb C^{10}\), \(1\le m\le9\), with five rishon modes at each end. Put \(U_\ell^{jk}=r^{y}_jr^{x\dagger}_k\)". Line 102: "\(p_{\ell,x}=r_{\ell,x}^\dagger r_{\ell,x}\)". For an oriented link `ℓ` write `x` for its source and `y` for its target, so `U^{jk}` annihilates a rishon at the `y`-end and creates one at the `x`-end. The ten modes `r^x_1, …, r^x_5, r^y_1, …, r^y_5` obey the CAR among themselves. The link algebra `𝔅_ℓ = End(Λ^m C^{10})` is an ordinary tensor factor; it commutes with matter and with every other link.

**Lemma 3.1 (end numbers).** Fix `ℓ` and `m`. For `S` a set of `m` of the ten modes, the vectors `e_S := r^†_S|0⟩` (creators in a fixed order) form an orthonormal basis of `Λ^m C^{10}`. Each `e_S` is an eigenvector of `p_{ℓ,x}` with eigenvalue `|S ∩ X|` and of `p_{ℓ,y}` with eigenvalue `|S ∩ Y|`, where `X`, `Y` are the five `x`-end and `y`-end modes. The set of eigenvalues of `p_{ℓ,x}` is
\[
I_m=\{a\in\mathbb Z:\max(0,m-5)\le a\le\min(5,m)\},\qquad
d_m:=\max I_m-\min I_m=\min(m,10-m)\le5 .
\]
`p_{ℓ,y} = m − p_{ℓ,x}` on the register, and its eigenvalues form the same interval `I_m`.

*Proof.* The CAR give `r^{x†}_kr^x_k e_S = [k ∈ S]e_S` for each `x`-end mode `k`, so `p_{ℓ,x}e_S = |S ∩ X|e_S`; likewise at `y`. `|S ∩ X| + |S ∩ Y| = m`. The value `a` occurs iff some `S` has `|S ∩ X| = a` and `|S ∩ Y| = m − a`, that is, iff `0 ≤ a ≤ 5` and `0 ≤ m − a ≤ 5`. This is `I_m`. If `m ≤ 5`, `I_m = {0, …, m}` and `d_m = m`. If `m ≥ 5`, `I_m = {m − 5, …, 5}` and `d_m = 10 − m`. The map `a ↦ m − a` sends `I_m` onto itself. □

This matches frozen `EW1.md` line 274 ("the `K_m` consecutive values `max(0, m−5), …, min(5, m)`"); `d_m = K_m − 1`.

### 3.2 Central gauge actions

Frozen `EW1.md` line 125: "The central element `e^{iθ}1_5` of `U(5)_x` acts by `Ad e^{iθQ_x}`, with `Q_x = N_x + Σ_{ℓ∋x}p_{ℓ,x}`". This is `LW1_5.md`'s Gauss generator \(\mathcal G_x^T=c_x^\dagger Tc_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger Tr_{\ell,x}\) (line 96) at `T = 1`, and `LW1_5.md` line 228. Here `p_{ℓ,z}` is the number at the `z`-end of `ℓ`, whether `z` is the source or the target. So on `𝔅_ℓ`, the centre at the source acts by `Ad e^{iθp_{ℓ,x}}` and the centre at the target by `Ad e^{iθp_{ℓ,y}}`; on the matter at `z` it acts by `Ad e^{iθN_z}`; it acts trivially on every other factor.

**Lemma 3.2 (letter charges).** On `𝔅_ℓ`: `[p_{ℓ,x}, U^{jk}] = U^{jk}`, `[p_{ℓ,x}, (U^{jk})^†] = −(U^{jk})^†`, `[p_{ℓ,y}, U^{jk}] = −U^{jk}`, `[p_{ℓ,y}, (U^{jk})^†] = (U^{jk})^†`. Hence for a word `B` with `p` letters from `{U^{jk}}` and `p′` letters from `{(U^{jk})^†}`, in any order, `[p_{ℓ,x}, B] = (p − p′)B` and `[p_{ℓ,y}, B] = −(p − p′)B`.

*Proof.* From the CAR, `[r^†_kr_k, r^†_k] = r^†_k` and `[r^†_kr_k, r_k] = −r_k`, and an even bilinear in one mode commutes with every mode operator of another mode. So `[p_{ℓ,x}, r^{x†}_k] = r^{x†}_k` and `[p_{ℓ,x}, r^y_j] = 0`, which gives the first identity; the others are the same computation. A commutator with a fixed operator is a derivation, so the charges of letters add along a word. □

Changing the sign convention of the gauge action (`Ad e^{−iθQ_z}`) replaces every central charge `q` by `−q`. Every statement below depends on `|q|` only.

### 3.3 Representations and transporters

Frozen `EW1.md` line 44: `V` is "the dual of the creator representation `C^5` for `U(5)`", the centre acts on `V` by `e^{−iθ}`, and an irreducible `σ_r ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` has central charge `q_r = p′ − p`: `σ_r(e^{iθ}1_5) = e^{iq_rθ}1`. Every irreducible unitary representation of `U(5)` occurs in some `V^{⊗p} ⊗ V̄^{⊗p′}` (standard; cited, not rebuilt, and used in no proof below). EW1's Definition 2.3 presupposes such a realization for each summand, so no classification of characters is needed.

Definitions used unchanged: EW1 Definition 2.2 (bosonic composite carried at `x` in `σ`: local, fermion-even, linearly independent `Φ^i` with `a_{x,g}(Φ^i) = Σ_jσ(g)_{ji}Φ^j` and `a_{y,g}(Φ^i) = Φ^i` for `y ≠ x`); Definition 2.3 (strict path transporter; reverse factors are adjoints; a transporter is a convex combination over a finite path set from `z` to `z′`); Definition 2.5 (R-FMS: blocks `X = Ln + {0, …, L−1}^3`, block sites `x_X = Ln`, composites carried at `x_X`, transporters from `x_X` to `x_Y` with `T_{YX} = T_{XY}^†`, clauses (O), (C), (A), (T)). We read EW1's "fixed decomposition into irreducibles" as an orthogonal decomposition `W = ⊕_rW_r` with an adapted orthonormal basis, as its block notation `σ(𝐔) := ⊕_rσ_r(𝐔)` does. For `End(W)`-valued `M`, `‖M‖^2_HS := Σ_{ij}M_{ij}^†M_{ij}` (`EW1.md` line 54).

**Lemma 3.3 (basis independence).** For a scalar unitary `u` on `W`, `‖uMu^†‖^2_HS = ‖M‖^2_HS`.

*Proof.* `(uMu^†)_{ij} = Σ_{kl}u_{ik}M_{kl}\bar u_{jl}`. Expanding `Σ_{ij}(uMu^†)_{ij}^†(uMu^†)_{ij}` and using `Σ_i\bar u_{ik′}u_{ik} = δ_{kk′}` and `Σ_ju_{jl′}\bar u_{jl} = δ_{ll′}` gives `Σ_{kl}M_{kl}^†M_{kl}`. The scalars commute with the operator entries. □

**Lemma 3.4 (charge eigenspaces).** For `q ∈ Z` let `W^{(q)} := {w : σ(e^{iθ}1_5)w = e^{iqθ}w for all θ}`. These spaces are mutually orthogonal and `W = ⊕_qW^{(q)}`; each `W_r` lies in `W^{(q_r)}`.

*Proof.* Each `W_r` lies in `W^{(q_r)}` by §3.3, so the `W^{(q)}` span `W`. If `w ∈ W^{(q)}`, `w′ ∈ W^{(q′)}` and `q ≠ q′`, unitarity gives `⟨w, w′⟩ = ⟨σ(e^{iθ})w, σ(e^{iθ})w′⟩ = e^{i(q′−q)θ}⟨w, w′⟩` for all `θ`; take `θ = π/(q′ − q)`. □

### 3.4 The quantity `W_cap`

For `L5-U[m]` and a representation `(W, σ)` put
\[
W_{\rm cap}:=\bigoplus_{|q|>d_m}W^{(q)} ,
\]
the span of all summands whose central charge exceeds the single-link capacity `d_m`.

### 3.5 Check of the tree's statements before use

Each line of `BK1_TREE.md` node UQ used below was checked against the frozen sources and the proofs of §§4-8.

| Tree statement (line) | Verdict |
|---|---|
| "Some \(v_r\ne0\) has \(q_r\ne0\). Otherwise the central \(U(1)\) fixes \(v\)." (261) | Correct (Theorem A, step 1). |
| "Since \(e^{2\pi i/5}I_5\in H\), one has \(5\mid q_r\)." (263) | Correct for every `r` with `v_r ≠ 0` (Lemma 4.3, Theorem A). It needs `v_r ≠ 0`. |
| "Bosonic parity gives \(2\mid q_r\)." (263) | Correct for every summand (Lemma 4.2). It needs nonzero composite entries in `W_r`, which Definition 2.2's linear independence supplies. |
| "\(d_m=\min(m,10-m)\le5\)", source `EW1.md:274` (268-272) | Correct (Lemma 3.1); the cited line says this. |
| "\([p_{\ell,x},B]=\pm q_rB\)", source "`q_r = p′ − p`" at `EW1.md:44` (274-278) | Correct (Lemma 3.2, Theorem B). The cited line says this. |
| "every block vanishes. Thus \(B=0\)." (284) | Correct (Lemma 5.1). |
| "Every nonempty strict path vanishes on \(W_r\) … The identity in condition T then contributes \(\dim W_r\ge1\)." (286-290) | Correct; it needs block diagonality (`EW1.md` line 330) and distinct block sites. Sharpened in Theorem C to `dim W_cap`. |
| "An \(H\)-fixed weight has the form \((n,n,n,n,n)\)." (294) | Correct for the weights of the nonzero weight components of an `H`-fixed vector (Lemma 4.4). |
| "no monomial on one native link can move its endpoint number that far" (294) | Correct (Lemma 5.2). |
| "\(\operatorname{diam}(\sum_{\ell\ni x}p_{\ell,x})=6d_m\). For \(m=1,9\), this is smaller than ten." (304-306) | Correct (Lemma 8.1, Theorem D(ii)). |
| C1: "\(B_xD_{xy}B_y\) … has charge ten at \(x\)" at \(m=5\) (439-446) | Correct, and `m = 5` is forced: for `m ≠ 5`, `D_{xy} = 0` by Theorem B with `|q| = 5 > d_m` (Remark 5.5). |

## 4. The charge theorem: H-fixed bosonic components have charge in 10Z

**Lemma 4.1 (total central charge is matter-number change).** Let `B` be a local element of the quasi-local algebra of `L5-U[m]`: it lies in the algebra of a finite set `F` of matter sites and a finite set `Λ` of links. Suppose `a_{z,e^{iθ}1_5}(B) = e^{iq_zθ}B` for every site `z` and every `θ`. Let `S` be a finite set of sites containing `F` and both ends of every link of `Λ`. Then `q_z = 0` for `z ∉ S`, and
\[
e^{i\theta N_S}\,B\,e^{-i\theta N_S}=e^{i\theta\sum_{z\in S}q_z}\,B\qquad(\theta\in\mathbb R),\qquad N_S:=\sum_{z\in S}N_z .
\]

*Proof.* For `z ∉ S`, `Q_z` involves only matter at `z` and link ends at `z`, and no link with an end at `z` lies in `Λ`; so `Ad e^{iθQ_z}` fixes `B`, and `q_z = 0` (take `θ` with `e^{iq_zθ} ≠ 1` if `q_z ≠ 0`). The `Q_z` are sums of commuting number operators, so `∏_{z∈S}Ad e^{iθQ_z} = Ad e^{iθΣ_{z∈S}Q_z}`, and the left side maps `B` to `e^{iθΣ_{z∈S}q_z}B`. Now `Σ_{z∈S}Q_z = N_S + Σ_ℓ c_ℓ`, where a link with both ends in `S` contributes `c_ℓ = p_{ℓ,x} + p_{ℓ,y} = m`, a scalar, and a link with one end `z` in `S` contributes `c_ℓ = p_{ℓ,z}`, which acts on a link outside `Λ` and commutes with `B`. Scalars drop out of `Ad`. □

This is frozen `LW1_5.md` Z-U, "total charge equal to its matter-number change" (line 242), with its proof (line 244: "Every supported link contributes its fixed total \(m\), and other link terms commute with the operator"), rebuilt in the form used below.

**Lemma 4.2 (even central charge; port of `EW1.md` Theorem 4.1(1)).** Let `Φ` be a bosonic composite carried at `x` in `σ = ⊕_rσ_r`. Then every `q_r` is even.

*Proof.* Fix `r` and a basis index `i` of `W_r`. Linear independence gives `Φ^i ≠ 0`. In the adapted basis `σ(e^{iθ}1_5)` is the scalar `e^{iq_rθ}` on `W_r`, so `a_{x,e^{iθ}1_5}(Φ^i) = e^{iq_rθ}Φ^i`. For `z ≠ x`, `a_{z,g}(Φ^i) = Φ^i`. Lemma 4.1 with `θ = π` gives `(−1)^{N_S}Φ^i(−1)^{N_S} = (−1)^{q_r}Φ^i`. The fermion-parity automorphism acts on the matter modes of `S` by `Ad (−1)^{N_S}` and trivially on link factors, and `Φ^i` is even. So `Φ^i = (−1)^{q_r}Φ^i`, and `Φ^i ≠ 0` forces `q_r` even. □

**Lemma 4.3 (the centre meets H).** Let `H = S(U(3) × U(2)) = {A ⊕ B : det A · det B = 1}` and `λ ∈ U(1)`.
(a) `λ1_5 ∈ H` if and only if `λ^5 = 1`. In particular `e^{2πi/5}1_5 ∈ H`.
(b) `λ1_5 ∈ K_G = H{±1_5}` if and only if `λ^{10} = 1`.

*Proof.* (a) `λ1_5 = λ1_3 ⊕ λ1_2` and `det(λ1_3)det(λ1_2) = λ^5`. (b) `λ1_5 ∈ H{±1_5}` iff `λ1_5` or `−λ1_5` lies in `H`, iff `λ^5 = 1` or `(−λ)^5 = 1`, iff `λ^{10} = 1`. □

For the standard ratio, EW1's `H` (Definition 2.4) has image `π(H) = S(U(3) × U(2))` (`EW1.md` line 338), so this is the `H` of BK1's root.

**Lemma 4.4 (weights of H-fixed vectors).** Let `σ_r ⊆ V^{⊗p} ⊗ V̄^{⊗p′}` and let `w ∈ W_r` be fixed by `H`. Expand `w` in the tensor basis `e_{i_1} ⊗ ⋯ ⊗ e_{i_p} ⊗ ē_{j_1} ⊗ ⋯ ⊗ ē_{j_{p′}}`, and group the terms by weight `μ ∈ Z^5`, where `μ_k := #{s : j_s = k} − #{s : i_s = k}`; so `w = Σ_μw_μ` with `σ(diag(t))w_μ = t^μw_μ := (∏_kt_k^{μ_k})w_μ`. Then every `μ` with `w_μ ≠ 0` equals `(n, n, n, n, n)` for one integer `n`, and `q_r = 5n`.

*Proof.* `V` is dual to the creator representation, so `diag(t)` acts on `e_k` by `\bar t_k` and on `ē_k` by `t_k`; each basis tensor is a weight vector with the stated `μ`. For `k ≠ k′` and `s ∈ U(1)`, the diagonal `t` with `t_k = s`, `t_{k′} = s^{−1}` and other entries 1 lies in `H`. So `Σ_μs^{μ_k−μ_{k′}}w_μ = Σ_μw_μ`. Distinct weights give linearly independent groups of basis tensors, so `s^{μ_k−μ_{k′}}w_μ = w_μ` for each `μ`. If `w_μ ≠ 0` and `μ_k ≠ μ_{k′}`, the choice `s = e^{iπ/(μ_k−μ_{k′})}` gives a contradiction. Hence `μ = (n, …, n)`. Every basis tensor has `Σ_kμ_k = p′ − p = q_r`, so `q_r = 5n`. □

**Theorem A (charge in 10Z).** On `L5-U[m]`, let `Φ` be a bosonic composite carried at `x` in `σ = ⊕_rσ_r`, and `v ∈ W`.
(a) Every `q_r` is even.
(b) If `H ⊆ Stab(v)`, then `q_r ∈ 10Z` for every `r` with `v_r ≠ 0`.
(c) If `H ⊆ Stab(v)` and `U(1)_centre ⊄ Stab(v)`, then some `r` has `v_r ≠ 0` and `q_r ∈ 10Z ∖ {0}`. Hence `|q_r| ≥ 10 > 5 ≥ d_m` for every `m`, and `0 ≠ v_r ∈ W_cap`.
(d) If `Stab(v) = K_G`, the hypotheses of (c) hold.

*Proof (central characters).* (a) is Lemma 4.2. (b) Each `σ(h)` preserves each `W_r`, so `σ(h)v = v` gives `σ_r(h)v_r = v_r`. Take `h = ζ1_5`, `ζ = e^{2πi/5}`, which lies in `H` by Lemma 4.3(a). Then `ζ^{q_r}v_r = v_r`, and `v_r ≠ 0` forces `ζ^{q_r} = 1`, that is `5 | q_r`. With (a), `10 | q_r`. (c) If every `r` with `q_r ≠ 0` had `v_r = 0`, then `σ(e^{iθ}1_5)v = Σ_re^{iq_rθ}v_r = v` for all `θ`, and the central `U(1)` would fix `v`. So some `v_r ≠ 0` has `q_r ≠ 0`, and (b) gives `|q_r| ≥ 10`. Lemma 3.1 gives `d_m ≤ 5`. (d) `K_G ⊇ H`, and by Lemma 4.3(b) `K_G` meets the central `U(1)` only in the tenth roots of unity. □

*Second proof of (b) (weights).* Let `v_r ≠ 0`. It is `H`-fixed, so by Lemma 4.4 `q_r = 5n`. By (a), `5n` is even, so `n` is even and `q_r ∈ 10Z`. □

**Remarks.** (1) Step (b) uses only `μ_5 ⊆ Stab(v)`; step (a) uses only evenness. (2) The value 10 is attained: `det^{±2}` is one-dimensional, `H`-fixed, of central charge `±10`, and at `m = 5` the tree's composite `B_xD_{xy}B_y` (`BK1_TREE.md` lines 439-446) is a nonzero bosonic carrier of it (Remark 5.5). (3) Theorem A is a statement about representations and composites. It uses no state, no tick and no transporter.

## 5. The vanishing theorem on every L5-U[m]

**Lemma 5.1 (spectral blocks).** Let `E` act on a finite-dimensional space with an orthonormal basis `(f_u)` of eigenvectors, `Ef_u = e_uf_u`, all `e_u` in an integer interval of diameter `d`. Let `q ∈ Z` with `|q| > d`, and let `B` satisfy `e^{iθE}Be^{−iθE} = e^{iqθ}B` for all `θ`, or `[E, B] = qB`. Then `B = 0`.

*Proof.* Put `B_{uv} := ⟨f_u, Bf_v⟩`. The first hypothesis gives `e^{iθ(e_u−e_v)}B_{uv} = e^{iqθ}B_{uv}` for all `θ`; the second gives `(e_u − e_v)B_{uv} = qB_{uv}`. Since `|e_u − e_v| ≤ d < |q|`, the integer `e_u − e_v − q` is nonzero; take `θ = π/(e_u − e_v − q)` in the first case. Either way `B_{uv} = 0` for all `u, v`. □

**Theorem B (single-link capacity).** Fix `L5-U[m]`, a link `ℓ` with source `x` and target `y`, and `q ∈ Z` with `|q| > d_m = min(m, 10 − m)`.
(a) If `B ∈ 𝔅_ℓ` satisfies `a_{x,e^{iθ}1_5}(B) = e^{iqθ}B` for all `θ`, or `a_{y,e^{iθ}1_5}(B) = e^{iqθ}B` for all `θ`, then `B = 0`.
(b) Let `σ_r` be irreducible with `|q_r| > d_m`, realized in `V^{⊗p} ⊗ V̄^{⊗p′}` by any isometric copy, with any `(p, p′)` such that `p′ − p = q_r`, any fixed factor order, and any `c > 0`. Then `σ_r(𝐔_ℓ/c) = 0` and `σ_r(𝐔_ℓ/c)^† = 0`.
(c) In particular, for every bosonic composite and every `v` as in Theorem A(c), the single-link representation matrix of each summand with `v_r ≠ 0` and `q_r ≠ 0` vanishes on every link of every `L5-U[m]`, `1 ≤ m ≤ 9`, in both directions.

*Proof (central characters and spectral blocks).* (a) On `𝔅_ℓ` the centre at `x` acts by `Ad e^{iθp_{ℓ,x}}` and at `y` by `Ad e^{iθp_{ℓ,y}}` (§3.2). Both are diagonal in the occupation basis with eigenvalues in `I_m`, of diameter `d_m` (Lemma 3.1). Lemma 5.1 gives `B = 0`. (b) Each entry of `𝐔^{⊗p} ⊗ 𝐔̄^{⊗p′}` is, in the fixed order, a word with `p` letters `U^{jk}` and `p′` letters `(U^{jk})^†`. By Lemma 3.2 the centre at `x` multiplies such a word by `e^{i(p−p′)θ} = e^{−iq_rθ}`, so by (a) with `q = −q_r` every word is zero. Each entry of `σ_r(𝐔_ℓ/c)` is `c^{−(p+p′)}` times a linear combination of these words, whatever the projection, the copy or the identification of its range with `W_r`. So `σ_r(𝐔_ℓ/c) = 0`, and its matrix adjoint is zero. (c) Theorem A(c) gives `|q_r| ≥ 10 > 5 ≥ d_m`. □

The covariance form (a) does not use how the matrix was built. Every entry of a covariant single-link factor carries the central character of its summand at each end of the link, and that alone forces zero. This discharges the tree's named first hard step, "certify the charge identity for every allowed projected representation, including multiplicities and ordering" (`BK1_TREE.md` line 288).

**Lemma 5.2 (CAR normal ordering).** Let `ρ_1, …, ρ_5` be five modes obeying the CAR. Every word `w` in the letters `ρ_k, ρ_k^†` is a linear combination of normal-ordered monomials `ρ^†_{a_1}⋯ρ^†_{a_s}ρ_{b_1}⋯ρ_{b_t}` with `s − t` equal to the net creation number `n(w)` (creators minus annihilators in `w`). If `|n(w)| > 5` then `w = 0`.

*Proof.* Induct on the pair (length, number of annihilator-before-creator inversions), ordered lexicographically. If `w` has an inversion, some adjacent pair is `ρ_bρ_a^†`. Replace it by `δ_{ab} − ρ_a^†ρ_b`. The second term has the same length and one inversion fewer; the first, if present, is shorter by two and has the same net creation number. Both have the same `n`. So `w` is a combination of normal-ordered monomials with `s − t = n(w)`. If `n(w) > 5` then `s > 5`, so two creators carry the same mode; anticommuting them next to each other changes only a sign, and `(ρ_a^†)^2 = 0`. The case `n(w) < −5` is the same with annihilators. □

*Second proof of Theorem B(b) (weights of letters, CAR normal ordering).* In a word of `𝐔^{⊗p} ⊗ 𝐔̄^{⊗p′}`, write each `U^{jk} = r^y_jr^{x†}_k` and `(U^{jk})^† = r^x_kr^{y†}_j`. Letters at different ends anticommute, so the word equals `±(y-end subword)(x-end subword)`. The `x`-end subword has net creation number `p − p′ = −q_r`, and `|q_r| ≥ 10 > 5`. Lemma 5.2 makes it zero. □ This second proof is purely algebraic and holds on the whole rishon Fock space, for every `m`. It gives the capacity 5; the sharp capacity `d_m` needs the fixed-number register (Lemma 3.1), which the first proof uses.

**Corollary 5.3 (the Abelian rung).** On a spin-`S` `U(1)` quantum link with `U = S^+` (L2, eq. (3.16)), every operator `B` with `[S^3, B] = qB` and `|q| > 2S` is zero. In particular `(S^+)^2 = 0` for `S = 1/2`: charge-two transport on a spin-½ link vanishes, the tree's smallest rung (`BK1_TREE.md` line 290).

*Proof.* `S^3` has eigenvalues `−S, …, S`, of diameter `2S`. Apply Lemma 5.1. □

**Lemma 5.4 (product form of exterior-power link matrices).** For `1 ≤ a ≤ 5` realize `Λ^aV ⊂ V^{⊗a}` with orthonormal basis `e_I := (a!)^{−1/2}Σ_{π∈S_a}sgn(π)e_{i_{π(1)}} ⊗ ⋯ ⊗ e_{i_{π(a)}}`, `I = {i_1 < ⋯ < i_a}`. Then
\[
\sigma_{\Lambda^a}(\mathbf U_\ell)_{IJ}=a!\,s_a\,r^y_I\,r^{x\dagger}_J,\qquad
r^y_I:=r^y_{i_1}\cdots r^y_{i_a},\quad r^{x\dagger}_J:=r^{x\dagger}_{j_1}\cdots r^{x\dagger}_{j_a},\quad s_a:=(-1)^{a(a-1)/2}.
\]
Moreover `σ_{Λ^a}(𝐔_ℓ) ≠ 0` if and only if `a ≤ d_m`.

*Proof.* `σ_{Λ^a}(𝐔)_{IJ} = (a!)^{−1}Σ_{π,τ}sgn(π)sgn(τ)∏_{n=1}^aU^{i_{π(n)}j_{τ(n)}}`. In each product move every `r^y` to the left; the `n`-th annihilator passes `n − 1` creators, giving the sign `s_a`. Then reorder the `y`-annihilators to increasing order (sign `sgn π`) and the `x`-creators (sign `sgn τ`). Each of the `(a!)^2` terms equals `s_ar^y_Ir^{x†}_J`. If `a > d_m`, Theorem B gives zero. If `a ≤ d_m`, choose occupied sets `Y_0` at the `y`-end and `X_0` at the `x`-end with `I ∩ Y_0 = ∅`, `J ∩ X_0 = ∅`, `|Y_0| + |X_0| = m − a`, `|Y_0|, |X_0| ≤ 5 − a`; this is possible because `0 ≤ m − a ≤ 10 − 2a` is `a ≤ min(m, 10 − m)`. On the basis vector with `y`-end set `I ∪ Y_0` and `x`-end set `X_0`, `r^y_Ir^{x†}_J` gives `±` the basis vector with `y`-end set `Y_0` and `x`-end set `X_0 ∪ J`. □

[check] (`check_bk1uq.py`): with Jordan–Wigner rishon operators, the double-sum definition of `σ_{Λ^a}(𝐔)_{IJ}` equals `a!s_ar^y_Ir^{x†}_J` exactly (difference `0.0`) on sampled entries for `a = 1, …, 5`; restricted to each sector `m = 1, …, 9`, those entries are nonzero exactly when `a ≤ d_m`; and a ten-letter word in the `U^{jk}` is the zero matrix.

So an exterior-power link moves exactly when `a ≤ d_m`. At `a = 3` this is frozen `CH1_5UQ.md` Theorem 5.1's window `3 ≤ m ≤ 7`; at `a = N = 5` it is L1's (4.6): nonzero exactly at `m = 5`.

**Remark 5.5 (the tree's determinant carriers need m = 5).** `D_ℓ := σ_{Λ^5}(𝐔_ℓ) = 5!·r^y_{12345}r^{x†}_{12345}` (`s_5 = 1`). By Lemma 5.4 it is nonzero only at `m = 5`, where it is `5!` times a rank-one partial isometry from the unique vector with `p_{ℓ,x} = 0` to the unique vector with `p_{ℓ,x} = 5`, up to sign. So the C1 carrier `B_xD_{xy}B_y` and the T1 transporter `D_{π_1}D_{π_2}` of `BK1_TREE.md` (lines 439-446, 318-322) are nonzero only on `L5-U[5]`. At `m = 5`, `B_xD_{xy}B_y ≠ 0`: the matter factors and the link factor act on different tensor factors, and each is nonzero.

## 6. The two transport-defect floors

**Theorem C (strict transport floors).** Fix `L5-U[m]`, `1 ≤ m ≤ 9`, a representation `(W, σ)` with its fixed orthogonal decomposition, and a strict transporter `T` (EW1 Definition 2.3) from `z` to `z′ ≠ z`, with any finite path set, any convex weights and any `c > 0`.
(a) `T` vanishes on `W_cap` and maps `W_cap^⊥` into itself; so does its matrix adjoint `T^†`. In an orthonormal basis adapted to `W = W_cap ⊕ W_cap^⊥`, `T = 0 ⊕ T′`.
(b) As operator inequalities in the local algebra,
\[
\|T^\dagger T-1_W\|^2_{\mathrm{HS}}\ \ge\ (\dim W_{\rm cap})\,1,\qquad
\|TT^\dagger-1_W\|^2_{\mathrm{HS}}\ \ge\ (\dim W_{\rm cap})\,1 .
\]
(c) Hence for every state `ω`: `ω(‖T^†T − 1‖^2_HS) ≥ dim W_cap` and `ω(‖TT^† − 1‖^2_HS) ≥ dim W_cap`. Under the hypotheses of Theorem A(c), `dim W_cap ≥ 1`, which gives the two floors of node UQ.
(d) If `W = det^{±2}` (dimension one, central charge `±10`), then `T = 0` and both defects equal `1` in every state; the floor 1 is attained.

*Proof.* (a) Each path from `z` to `z′ ≠ z` has at least one link. Each factor `σ(𝐔_{ℓ_n}/c)` is block diagonal over the fixed summands (`EW1.md` line 44, and line 330: "`σ(𝐔)` is block diagonal over the fixed summands"). A reverse factor is the matrix adjoint of a forward factor, so it is block diagonal with the adjoint blocks. For every summand `W_r ⊆ W_cap`, both the forward block and its adjoint are zero by Theorem B(b), since `|q_r| > d_m`. The block of a product of block-diagonal matrices is the product of the blocks, so every path transport has zero block on every `W_r ⊆ W_cap`; so does every convex combination. The other blocks map each `W_r ⊆ W_cap^⊥` into itself (Lemma 3.4 places each summand in one charge eigenspace). The matrix adjoint has the adjoint blocks.
(b) By Lemma 3.3 we may compute in an adapted orthonormal basis. Let `i, j` index basis vectors of `W_cap`. Column `j` of `T` is zero, so `(T^†T)_{ij} = Σ_k(T_{ki})^†T_{kj} = 0`, and `(T^†T − 1)_{ij} = −δ_{ij}1`. Row `i` of `T` is zero, so `(TT^†)_{ij} = Σ_kT_{ik}(T_{jk})^† = 0` as well. With `M = T^†T − 1` or `M = TT^† − 1`,
\[
\|M\|^2_{\mathrm{HS}}=\sum_{\text{all }i,j}M_{ij}^\dagger M_{ij}\ \ge\ \sum_{i,j\in W_{\rm cap}}M_{ij}^\dagger M_{ij}=(\dim W_{\rm cap})\,1 ,
\]
because each omitted term `M_{ij}^†M_{ij}` is positive.
(c) States are positive and normalized. Theorem A(c) supplies `0 ≠ v_r ∈ W_cap`.
(d) Here `W = W_cap` is one-dimensional, so `T = 0` and `‖0 − 1‖^2_HS = 1`. □

The floors hold for every state of the quasi-local algebra, symmetric or not, stationary or not, at every block size, and for both orientations, since `T_{YX} = T_{XY}^†` exchanges the two inequalities.

**Corollary C.1 (strict R-FMS on L5-U).** Let `D` be R-FMS data on `L5-U[m]` whose representation has `W_cap ≠ 0`. Then no state satisfies clause (T) for any neighbouring pair with `δ < dim W_cap`. In particular this holds whenever `H ⊆ Stab(v)` and the central `U(1)` is not in `Stab(v)`, and so whenever `Stab(v) = K_G`, with `δ < 1`.

*Proof.* Theorem C(c) applies to `T_{XY}`, which joins the distinct block sites `x_X = Ln` and `x_Y = Ln′`. Theorem A(c)-(d) gives `W_cap ≠ 0`. □

**Corollary C.2 (alignment floor, without (T)).** In the setting of Corollary C.1 let `R_cap` be the set of summands in `W_cap`, `s := |R_cap|`, and `V_cap := Σ_{r∈R_cap}|v_r|^2`. If a state satisfies (O), (C) and (A) for one ordered pair `(X, Y)` with tolerance `δ`, then
\[
V_{\rm cap}\ \le\ \delta|v|^2+\Big(s+\tfrac12\sqrt{\dim W}\Big)\sqrt\delta ,
\qquad\text{hence}\qquad
\delta\ \ge\ \min\Big\{1,\ \Big(\frac{V_{\rm cap}}{|v|^2+s+\frac12\sqrt{\dim W}}\Big)^2\Big\}\ \text{ if } V_{\rm cap}>0 .
\]

*Proof.* Row `i ∈ W_cap` of `T_{XY}` is zero (Theorem C(a)), so `(T_{XY}Φ_Y)^i = 0` there. In an adapted basis, `|Φ_X − T_{XY}Φ_Y|^2 ≥ Σ_{i∈W_cap}Φ_X^{i†}Φ_X^i = Σ_{r∈R_cap}|Φ_{X,r}|^2`, the omitted terms being positive. So (A) gives `Σ_{r∈R_cap}ω(|Φ_{X,r}|^2) ≤ δ|v|^2`. For each `r`, `|w_r|^2` is in the generating set of Definition 2.5, and its symmetrized evaluation is `|Φ_{X,r}|^2 + ½Σ_{i∈r}[Φ^i_X, Φ^{i†}_X]`. By (O) and Cauchy–Schwarz (`ω(A)^2 ≤ ω(A^2)` for self-adjoint `A`), `ω(p_{r,sym}(Φ_X)) ≥ |v_r|^2 − √δ`. By (C) and Cauchy–Schwarz twice, `Σ_i|ω([Φ^i_X, Φ^{i†}_X])| ≤ √(dim W)·√δ`. Summing over `r ∈ R_cap` gives the first inequality. If `δ ≤ 1` then `δ ≤ √δ`, so `V_cap ≤ (|v|^2 + s + ½√dim W)√δ`, which is the second. □

This is the estimate of frozen `EW1.md` Lemma 6.4(3), with its sharp-matter step replaced by `T_r = 0`. Unlike Theorem 6.3′, the floor depends on no operator norm `c_Φ`, no cut and no state class.

**Corollary C.3 (the strict U branch of BK1).** BK1's root with H-FMS read as EW1's strict class (`BK1_TREE.md` line 65: "The initial branch uses EW1’s strict path definition") has no instance on any `L5-U[m]`, `1 ≤ m ≤ 9`: for the fixed triple with `Stab(v) = K_G`, clause (T) fails for every `δ < 1` in every state, at every block size and for every path family. The same triple also meets the alignment floor of Corollary C.2.

*Proof.* Corollary C.1 with Theorem A(d); Corollary C.2 with `V_cap ≥ |v_r|^2 > 0` for the summand of Theorem A(c). □

This is a proved negative for one branch. It says nothing about `L5-O`, about the network branch C-NET, or about other readings of "broken".

**Remark 6.1 (other charged data).** Theorem C needs only `W_cap ≠ 0`, not `H`. For example EW1's charge-four datum `Λ^4C^5` (`EW1.md` line 321, "`q = 4`") has `W_cap = W` on `L5-U[m]` for `m ∈ {1, 2, 3, 7, 8, 9}`, where `d_m ≤ 3`. There every strict transporter of that datum is zero and both defects are at least `dim Λ^4C^5 = 5`.

## 7. Attacks on the hypothesis, and counterexample search

UQ is proved, so the three named attacks are run against the proof. Each attack names a step it would need, and each such step is false.

### 7.1 Attack 1: reducible-carrier decomposition

*The step it needs:* "some charged summand that carries part of `v` escapes the zero block, because the carrier is reducible, its decomposition is not unique, or a transporter mixes summands."

**Lemma 7.1 (no mixing on one link).** Let `B ∈ 𝔅_ℓ` satisfy `Ad e^{iθp_{ℓ,y}}(B) = e^{iq_rθ}B` and `Ad e^{iθp_{ℓ,x}}(B) = e^{−iq_sθ}B` for all `θ` (rows transforming in `σ_r` at the target, columns in `σ_s` at the source). If `q_r ≠ q_s`, or if `q_r = q_s` and `|q_r| > d_m`, then `B = 0`.

*Proof.* `p_{ℓ,x} + p_{ℓ,y} = m` on the register, so `Ad e^{iθ(p_{ℓ,x}+p_{ℓ,y})}` is the identity, and the two hypotheses give `e^{i(q_r−q_s)θ}B = B` for all `θ`. If `q_r ≠ q_s`, take `θ = π/(q_r − q_s)`. If `q_r = q_s` and `|q_r| > d_m`, Theorem B(a) applies. □

*Where the attack fails.* (i) The proof of Theorem C uses only the canonical charge decomposition `W = ⊕_qW^{(q)}` (Lemma 3.4). Every fixed decomposition into irreducibles refines it, so non-uniqueness inside an isotypic component changes nothing. (ii) EW1's transporters are block diagonal; and even a class that allowed off-diagonal single-link blocks would have zero blocks into, out of and inside `W_cap`, by Lemma 7.1. (iii) If `v` has charged components in several summands, all of them lie in `W_cap` (Theorem A(b)-(c)), all are killed, and their dimensions add in the floor. The needed step is false.

### 7.2 Attack 2: reverse and repeated-path ordering

*The step it needs:* "a reversed factor, a repeated link or a back-and-forth path produces a nonzero product on `W_cap`, as happens for expectations of repeated-link products" (frozen `CH1_5UQ.md` line 116: "A path that repeats a link gives expectations of products in that one register, not products of one-link expectations").

*Where the attack fails.* (i) Under Definition 2.3 a reverse factor is `σ_r(𝐔/c)^† = 0^† = 0`. The convention that EW1 rejected (§8 item 1, line 392), same-order evaluation `σ_r(𝐔^†/c)`, is also zero: its words have net charge `q_r` at the source end (Lemma 3.2), and Theorem B(a) applies. (ii) Each factor is the zero matrix of operators, not an operator with zero expectation. A product with a zero factor is zero, whatever the order, repetition or state. (iii) Inside one factor, the order of letters changes no letter count, and Theorem B(a) uses only the central character.

A nearer variant projects after multiplying along the path. It is not EW1's definition; we test it because it is the natural way a repeated path could pool charge.

**Lemma 7.2 (net traversal).** For a path `z_0, ℓ_1, …, ℓ_N, z_N` in `Z^3`, let `n_ℓ` be the number of traversals of `ℓ` from `src(ℓ)` to `tgt(ℓ)` minus the number from `tgt(ℓ)` to `src(ℓ)`. Then `z_N − z_0 = Σ_ℓn_ℓ(tgt(ℓ) − src(ℓ))`. If `z_N ≠ z_0`, some `n_ℓ ≠ 0`.

*Proof.* Telescoping: `z_N − z_0 = Σ_n(z_n − z_{n−1})`, and each step contributes `±(tgt(ℓ_n) − src(ℓ_n))`. □

**Proposition 7.3 (projection after the path product vanishes).** Put `𝐔_π := 𝐔^{(ε_1)}_{ℓ_1}⋯𝐔^{(ε_N)}_{ℓ_N}` with `𝐔^{(−)} := 𝐔^†` (matrix adjoint), and `T^{hol}_π := P_σ(𝐔_π^{⊗p} ⊗ \bar{𝐔}_π^{⊗p′})P_σ` for `σ_r ⊆ V^{⊗p} ⊗ V̄^{⊗p′}`, in any fixed order of multiplication. If `z_N ≠ z_0` and `|q_r| > d_m`, then `T^{hol}_π = 0`.

*Proof.* Every entry is a combination of words in the letters `U^{jk}_ℓ`, `(U^{jk}_ℓ)^†` over the links of `π`. In each word the letters on `ℓ` raise `p_{ℓ,x}` by `ε_0(p − p′)n_ℓ = −ε_0q_rn_ℓ`, where the fixed sign `ε_0 = ±1` records which direction of traversal uses `𝐔_ℓ` rather than `𝐔_ℓ^†`: each copy of `𝐔_π` contributes `ε_0n_ℓ` and each copy of `\bar{𝐔}_π` contributes `−ε_0n_ℓ`. Letters on different links commute (different tensor factors), so the word equals the product over links of its subwords on each link, each in its original order. By Lemma 7.2 some `n_ℓ ≠ 0`; for it `|q_rn_ℓ| ≥ |q_r| > d_m`, and Theorem B(a) with Lemma 3.2 makes that subword zero. □

So the needed step is false for EW1's definition and for this variant.

### 7.3 Attack 3: representation-projection multiplicities

*The step it needs:* "if `σ_r` occurs in `V^{⊗p} ⊗ V̄^{⊗p′}` several times, or for several pairs `(p, p′)`, some copy, some cross-copy block `ι_1^†(𝐔^{⊗p} ⊗ 𝐔̄^{⊗p′})ι_2`, or some sum of copies is nonzero."

*Where the attack fails.* The proof of Theorem B(b) shows that every entry of the unprojected tensor `𝐔^{⊗p} ⊗ 𝐔̄^{⊗p′}` is zero once `|p − p′| > d_m`. Every copy, cross-copy block and sum is a linear combination of these entries. All pairs `(p, p′)` realizing `σ_r` have `p − p′ = −q_r`. There is nothing for a projection to select. The needed step is false.

### 7.4 Counterexample search

An admissible counterexample would be: some `m ∈ {1, …, 9}`, EW1 data on `L5-U[m]` with `H ⊆ Stab(v)` and the central `U(1)` not in `Stab(v)`, a strict transporter between distinct block sites, and a state with `ω(‖T^†T − 1‖^2_HS) < 1` or `ω(‖TT^† − 1‖^2_HS) < 1`. Theorem C excludes every such datum. The following examples each break exactly one hypothesis. They show which hypothesis each step uses; none is admissible.

| Example | Hypothesis broken | What happens |
|---|---|---|
| E1. `σ = Λ^5V = det^{−1}` (`q = −5`), `H`-fixed, carried by five matter annihilators at `x` | bosonic (the carrier is odd) | at `m = 5`, `σ(𝐔_ℓ) = 5!·r^y_{12345}r^{x†}_{12345} ≠ 0` (Lemma 5.4); evenness is what lifts `5` to `10` |
| E2. `σ = Λ^2V` (`q = −2`), `v = e_{45}` | `H ⊆ Stab(v)` (`ζ1_5` acts by `ζ^{−2} ≠ 1`) | for `2 ≤ m ≤ 8`, `σ(𝐔_ℓ) ≠ 0` (Lemma 5.4); the factor 5 is what pushes `|q|` past every `d_m` |
| E3. split transporters (§8) | strictness (one strand per summand) | the charge-ten block is nonzero for `2 ≤ m ≤ 8` (Proposition E) |
| E4. a link register with more than five rishon modes per end | the law `L5-U[m]` (PS-6r register fixed by LW1-5) | the capacity grows; this is a law change, not an instance |

No admissible counterexample exists. Each named attack fails at its named step, so there is no residual lemma for UQ.

## 8. The smallest network extension that removes the hypothesis

### 8.1 The hypothesis the proof uses

The proof of Theorem C uses one feature of Definition 2.3, called **H-strict** here: *for each summand `σ_r`, every link factor of a path transport is the full representation matrix `σ_r(𝐔_ℓ^{(ε)}/c)`*. So the whole central charge `q_r` of the summand passes through one link at a time, and Theorem B makes each factor zero. Any extension with nonzero charged blocks must spread `q_r` over several links in parallel. Theorem D says how many.

### 8.2 Endpoint capacity

**Lemma 8.1 (sum of end numbers).** Let `Λ_z` be a set of `k` links with an end at the site `z`, and `E_z := Σ_{ℓ∈Λ_z}p_{ℓ,z}`. In the product occupation basis of their registers, `E_z` is diagonal with eigenvalues exactly the integers of `[k·min I_m, k·max I_m]`, an interval of diameter `k·d_m`. For the six links at `z` this is `6d_m`.

*Proof.* Each `p_{ℓ,z}` takes every value of `I_m` (Lemma 3.1; at a target end use `m − I_m = I_m`). A sum of `k` independent integers, each ranging over an integer interval, ranges over the integer interval of the summed endpoints. □

**Theorem D (endpoint capacity of link-only operators).** Let `B` lie in the algebra of the registers of a finite set `Λ` of links, with no matter factor, and suppose `a_{z,e^{iθ}1_5}(B) = e^{iqθ}B` for all `θ` at a site `z`. Let `Λ_z ⊆ Λ` be the links of `Λ` with an end at `z`.
(i) If `B ≠ 0` then `|q| ≤ |Λ_z|·d_m`. So a nonzero link-only operator of central charge `q` at `z` acts on at least `⌈|q|/d_m⌉` links at `z`.
(ii) If `|q| > 6d_m`, then `B = 0`. On `L5-U[1]` and `L5-U[9]` (`d_m = 1`) every link-only operator of central charge `|q| ≥ 7` at a site is zero, whatever its shape: strict paths, networks, vertex tensors, any number of strands.

*Proof.* (i) On the algebra of `Λ` the centre at `z` acts by `Ad e^{iθE_z}`, with `E_z` built from `Λ_z` (links of `Λ` without an end at `z` are untouched). By Lemma 8.1 its eigenvalues lie in an interval of diameter `|Λ_z|d_m`; Lemma 5.1 gives `B = 0` when `|q|` exceeds it. (ii) `|Λ_z| ≤ 6`. □

For the charged `H`-fixed summand (`|q| ≥ 10`), Theorem D gives the minimum number of links at each endpoint: `2` at `m = 5`; `3` at `m = 4, 6`; `4` at `m = 3, 7`; `5` at `m = 2, 8`; and no link-only operator at all at `m = 1, 9`. This proves the tree's endpoint remark (`BK1_TREE.md` lines 304-306).

### 8.3 Candidate C-SPLIT

**Candidate C-SPLIT (proposed for the owner; not adopted).** Keep EW1 Definitions 2.2, 2.3 and 2.5 and add one kind of transporter. For each summand `σ_r` of the fixed decomposition, fix in advance a finite palette of splitting data `(σ_{s_1}, …, σ_{s_k}; J)`: irreducible `σ_{s_t}`, each realized as in Definition 2.3, and an isometric intertwiner `J : W_r → W_{s_1} ⊗ ⋯ ⊗ W_{s_k}`, `Jσ_r(g) = (σ_{s_1}(g) ⊗ ⋯ ⊗ σ_{s_k}(g))J`. For paths `π_1, …, π_k` from `z` to `z′` from a fixed finite, translation-covariant list, the **split transport** is
\[
\mathcal T^{J}_{\pi_1\ldots\pi_k}:=J^{T}\big(\mathcal T^{s_1}_{\pi_1}\otimes\cdots\otimes\mathcal T^{s_k}_{\pi_k}\big)\bar J ,
\]
where `𝒯^{s_t}_{π_t}` is the strict transport of `σ_{s_t}` along `π_t`, and tensor products of operator matrices multiply entries in a fixed left-to-right order. A C-SPLIT transporter is block diagonal over the summands; its block for `σ_r` is a convex combination of strict transports and split transports from the palette. Its reverse is the matrix adjoint, as in Definition 2.3. Nothing else changes: no interior vertex, no matter factor, no new constant beyond the pinned palette, and the choice is made independently of the composites `Φ`.

**Lemma 8.2 (covariance and normalization).** (a) `a_{z,g}(𝒯^J) = σ_r(g)^T𝒯^J`, `a_{z′,g}(𝒯^J) = 𝒯^J(σ_r(g)^T)^{−1}`, and `𝒯^J` is invariant at every other site. (b) If every strand transport were an identity matrix, `𝒯^J` would be `1_{W_r}`.

*Proof.* (a) Each `a_{u,g}` is an automorphism acting entrywise, so it acts on `⊗_t𝒯^{s_t}` at `z` by left multiplication with `⊗_tσ_{s_t}(g)^T` (EW1's covariance of each strand; scalars move out of products). Transposing the intertwining relation gives `σ_r(g)^TJ^T = J^T(⊗_tσ_{s_t}(g)^T)`, which gives the first identity. At `z′` each strand gives right multiplication by `(σ_{s_t}(g)^T)^{−1} = \bar σ_{s_t}(g)` (unitarity), and the conjugated relation `\bar J\bar σ_r(g) = (⊗_t\bar σ_{s_t}(g))\bar J` gives the second. At interior sites each strand is invariant. (b) `J^T\bar J = \overline{J^*J} = 1`. □

**Lemma 8.3 (splitting isometries exist; port of `LW1_5.md` lines 240 and 250).** Let `1 ≤ a_1, …, a_k ≤ 5` with `Σ_ta_t = 10`. Then `⊗_tΛ^{a_t}V` contains a copy of `det_V^2 := (Λ^5V)^{⊗2}`, so an isometric intertwiner `J : det_V^2 → ⊗_tΛ^{a_t}V` exists. The same holds with `V̄` and `det^2`.

*Proof.* Frozen `LW1_5.md` line 250 gives two equivariant maps, each nonzero: for `a + b ≤ 5`, the `(a, b)` part of the exterior coproduct `Λ^{a+b}V → Λ^aV ⊗ Λ^bV`, which sends `e_S` to `Σ_{A⊂S,|A|=a}±e_A ⊗ e_{S∖A}`; for `a + b ≥ 5`, with `c = a + b − 5`, the map `Λ^cV ⊗ Λ^5V → Λ^aV ⊗ Λ^bV`, `w ⊗ vol ↦ (id ⊗ ∧)(Δ_{a,5−a}(vol) ⊗ w)`, which is nonzero on `e_T` by choosing `A ⊃ T` ("distinct `A`'s give distinct basis tensors"). Both sources are irreducible, so both maps are injective. Write `b_t := (a_1 + ⋯ + a_t) mod 5` and `c_t := ⌊(a_1 + ⋯ + a_t)/5⌋`. By induction on `t` there is an injective equivariant map `φ_t : Λ^{b_t}V ⊗ (Λ^5V)^{⊗c_t} → Λ^{a_1}V ⊗ ⋯ ⊗ Λ^{a_t}V`. For `t = 1` it is the identity of `Λ^{a_1}V` (read `Λ^0V ⊗ Λ^5V = Λ^5V` if `a_1 = 5`). For the step, if `b_{t−1} + a_t < 5` the first map sends `Λ^{b_t}V` into `Λ^{b_{t−1}}V ⊗ Λ^{a_t}V`; if `b_{t−1} + a_t ≥ 5` the second map sends `Λ^{b_t}V ⊗ Λ^5V` into it, using up one factor `Λ^5V`. Tensor with the identity on the remaining factors `(Λ^5V)^{⊗c_{t−1}}`, reorder tensor factors, and compose with `φ_{t−1} ⊗ id`; a composite of injective maps is injective. At `t = k`, `b_k = 0` and `c_k = 2`. An injective equivariant map `φ` from an irreducible representation has `φ^*φ` equal to a positive scalar (Schur), so `J := φ/‖φ‖` is an isometric intertwiner. □

### 8.4 C-SPLIT removes the vanishing for 2 ≤ m ≤ 8

**Proposition E (nonzero charge-ten split transport).** Let `2 ≤ m ≤ 8`, `k := ⌈10/d_m⌉`, and `a_1, …, a_k ≤ d_m` with `Σ_ta_t = 10`; for example `(5,5)` at `m = 5`, `(4,3,3)` at `m = 4, 6`, `(3,3,2,2)` at `m = 3, 7`, `(2,2,2,2,2)` at `m = 2, 8`. Let `J` be as in Lemma 8.3, and let `π_1, …, π_k` be pairwise link-disjoint paths from `z` to `z′ ≠ z`, none repeating a link. Then `𝒯^J_{π_1…π_k} ≠ 0`. Between block sites `x_X` and `x_Y = x_X + Le_i` such paths exist for `k ≤ 5`: the straight path, and for each `j ≠ i` and sign `±` the path `x_X → x_X ± e_j → (straight) → x_Y ± e_j → x_Y`.

*Proof.* The summand is one-dimensional, so `𝒯^J = Σ_{α,β}J_α\bar J_β∏_t(𝒯^{a_t}_{π_t})_{α_tβ_t}`, where `J = Σ_αJ_αe_{α_1} ⊗ ⋯ ⊗ e_{α_k}` and each `α_t` is an `a_t`-subset of `{1, …, 5}`. Write `π_t = (u_0 = z, ℓ_1, u_1, …, ℓ_N, u_N = z′)`. By Lemma 5.4 and adjoint reversal, the `(I, K)` entry of the `n`-th factor of strand `t` is a nonzero constant times "annihilate the set `I` at the `u_{n−1}`-end of `ℓ_n`, then create the set `K` at the `u_n`-end": for a forward factor the rows sit at the target, and for a reverse factor the adjoint sends `r^y_Kr^{x†}_I` to `± r^x_Ir^{y†}_K`. Fix an index `A = (A_1, …, A_k)` with `J_A ≠ 0`. Choose an occupation basis vector `ψ_in` of the registers of all strand links: on each link `ℓ_n` of strand `t`, the `u_{n−1}`-end holds `A_t ∪ Y_0` and the `u_n`-end holds `X_0`, with `A_t ∩ Y_0 = ∅`, `A_t ∩ X_0 = ∅`, `|Y_0| + |X_0| = m − a_t` and `|Y_0|, |X_0| ≤ 5 − a_t` (possible since `a_t ≤ d_m`, as in Lemma 5.4). Let `ψ_out` hold `Y_0` and `X_0 ∪ A_t` instead. Each factor acts on its own link, and the links are distinct, so every term of `𝒯^J` acts on `ψ_in` as a tensor product of one-link operators. A term maps `ψ_in` to a multiple of `ψ_out` only if on every link the annihilated and created sets are `A_t`, which fixes all internal indices and `α = β = A`. So exactly one term contributes to `⟨ψ_out, 𝒯^Jψ_in⟩`, and that term is a nonzero constant times `|J_A|^2 ≠ 0`. The five listed paths are link-disjoint: the straight one stays on the line `x_X + Ze_i`, and the detour through `±e_j` uses the two links `(x_X, x_X ± e_j)`, `(x_Y ± e_j, x_Y)` and the line `x_X ± e_j + Ze_i`. □

So C-SPLIT removes H-strict's zero on `L5-U[m]` for every `2 ≤ m ≤ 8`, with the minimal number of strands that Theorem D(i) allows. Nonvanishing is all that is claimed.

### 8.5 What any transporter can do at one site: two-sided capacity

Nonvanishing is not near-unitarity. The same spectral-block argument bounds both defects together for every transporter class, strict or not, once the charge is large compared with the spectrum at one endpoint.

Call an `End(W)`-valued matrix `T` of local operators **covariant at `z`** if `a_{z,g}(T) = σ(g)^TT` for all `g`, and **charge-diagonal** if it maps each charge eigenspace `W^{(q)}` into itself. EW1's transporters and C-SPLIT transporters are block diagonal, hence charge-diagonal. A link-only `T` that is covariant at `z`, covariant with the inverse at `z′` and invariant elsewhere is charge-diagonal automatically: by Lemma 4.1 an entry from a column of charge `q_i` to a row of charge `q_k` has total charge `q_k − q_i` equal to its matter-number change, which is `0`.

**Theorem F (two-sided capacity at a site).** Let `T` be covariant at `z` and charge-diagonal. Let `Δ_z` be the diameter of the spectrum of the operator by which the centre at `z` acts on the entries of `T`: `Δ_z = 6d_m` if the entries are link-only, and `Δ_z = 5 + 6d_m` in general. Let `R_F` be the set of summands with `2|q_r| > Δ_z`. Then, as operator inequalities,
\[
\|T^\dagger T-1\|^2_{\mathrm{HS}}+\|TT^\dagger-1\|^2_{\mathrm{HS}}\ \ge\ \Big(\sum_{r\in R_F}\dim W_r\Big)\,1 ,
\]
so `ω(‖T^†T − 1‖^2_HS) + ω(‖TT^† − 1‖^2_HS) ≥ Σ_{r∈R_F}dim W_r` in every state.

*Proof.* On the entries of `T`, the centre at `z` acts by `Ad e^{iθQ_z}` with `Q_z = N_z + Σ_{ℓ∋z}p_{ℓ,z}`, or by `Ad e^{iθE_z}`, `E_z = Σ_{ℓ∋z}p_{ℓ,z}`, for link-only entries (§3.2). In the product occupation basis it is diagonal with integer eigenvalues in an interval `[e_−, e_+]` with `e_+ − e_− = Δ_z` (Lemma 8.1; `N_z ∈ {0, …, 5}`). Fix `r ∈ R_F` and let `q := q_r > 0`; the case `q < 0` is the same with the roles below exchanged. Every entry `T_{ki}` with `k` in the charge-`q` eigenspace satisfies `[Q_z, T_{ki}] = qT_{ki}` (Lemma 5.1's computation), so it maps the level `e` into the level `e + q`. Let `P_lo` project onto the levels `e ≤ e_+ − q` and `P_hi` onto the levels `e ≥ e_− + q`. Then `T_{ki} = P_hiT_{ki}P_lo`. Since `2q > Δ_z`, `e_+ − q < e_− + q`, so `P_loP_hi = 0` and `P_lo + P_hi ≤ 1`. For `i ∈ W_r`, charge-diagonality gives `(T^†T)_{ii} = Σ_kT_{ki}^†T_{ki} = P_lo(T^†T)_{ii}P_lo`; covariance at `z` alone gives `(TT^†)_{ii} = Σ_kT_{ik}T_{ik}^† = P_hi(TT^†)_{ii}P_hi`. If `X = P_lo X P_lo` is self-adjoint, then `(X − 1)^2 = (1 − P_lo) + P_lo(X − 1)^2P_lo ≥ 1 − P_lo`. Keeping only diagonal entries in `‖·‖^2_HS` (the other terms are positive),
\[
\|T^\dagger T-1\|^2_{\mathrm{HS}}+\|TT^\dagger-1\|^2_{\mathrm{HS}}\ \ge\ \sum_{r\in R_F}\dim W_r\,\big(2-P^{(r)}_{lo}-P^{(r)}_{hi}\big)\ \ge\ \sum_{r\in R_F}\dim W_r\cdot 1 .\qquad\square
\]

**Corollary F.1 (where charge-ten transport can be two-sided).** Take a summand with `|q_r| ≥ 10`, as Theorem A(c) supplies, and R-FMS clause (T) at tolerance `δ`, which needs both defects at most `δ`.
- On `L5-U[1]`, `L5-U[2]`, `L5-U[8]`, `L5-U[9]` (`5 + 6d_m ≤ 17 < 20`): every charge-diagonal transporter covariant at the block site, of any class, has `D_+ + D_− ≥ 1`; so (T) fails for every `δ < 1/2`.
- On `L5-U[3]` and `L5-U[7]` (`6d_m = 18 < 20 ≤ 5 + 6d_m`): every link-only transporter (strict, C-SPLIT, the tree's C-NET, or any convex combination) has `D_+ + D_− ≥ 1`; so (T) fails for every `δ < 1/2`. Transporters with matter at the endpoint are not bounded by this count.
- On `L5-U[4]`, `L5-U[5]`, `L5-U[6]` (`6d_m ≥ 24`): Theorem F gives no floor.

*Proof.* Theorem F with `Δ_z ∈ {5 + 6d_m, 6d_m}` and `2|q_r| ≥ 20`; `d_m = 1, 2, 3` for `m ∈ {1, 9}, {2, 8}, {3, 7}`. If `D_± ≤ δ` then `1 ≤ D_+ + D_− ≤ 2δ`. □

**Proposition F′ (a saturated first link).** Let `T` be a block-diagonal transporter whose entries in the block of one summand `σ_r` all change `p_{ℓ,z}` by the same amount, `+d_m` for all or `−d_m` for all, for one link `ℓ` at `z`. Then `‖T^†T − 1‖^2_HS + ‖TT^† − 1‖^2_HS ≥ dim W_r·1` on that summand, and `max(D_+, D_−) ≥ ½dim W_r` in every state. This holds for every single split transport `𝒯^J_{π_1…π_k}` on pairwise link-disjoint paths, none repeating a link, with the minimal strand number `k = ⌈10/d_m⌉`, and for convex combinations of such transports whose saturated strands all start with the same link `ℓ`.

*Proof.* `p_{ℓ,z}` has eigenvalues in `I_m`, of diameter `d_m`. An entry that changes it by exactly `−d_m` maps the level `max I_m` to the level `min I_m` and kills every other level, and the same holds with the roles exchanged for `+d_m`. So the proof of Theorem F applies with `P_lo, P_hi` the projections onto the two extreme levels, which are orthogonal because `d_m ≥ 1`. For the second sentence: if no strand had `a_t = d_m`, then `10 = Σ_ta_t ≤ k(d_m − 1)`, but `k(d_m − 1) = 8, 9, 8, 5` for `d_m = 5, 4, 3, 2`. A strand with `a_t = d_m` annihilates or creates `d_m` rishons at the `z`-end of its first link `ℓ`, and no other factor of the term touches `ℓ`. □

At `m = 5`, Proposition F′ covers the tree's T1 candidate `T_{det²} = D_{π_1}D_{π_2}` (`BK1_TREE.md` lines 318-322) on one pair of paths: there `D_+ + D_− ≥ 1`. Equality holds at the normalization `(5!/c^5)^{2N} = 1` (`N` links per path) for any state with weight `½` on each of the two configuration vectors of the path links, "all rishons at the `z`-side ends" and "all at the `z′`-side ends": then `T^†T` and `TT^†` are the projections onto these two vectors, and `D_+ = D_− = ½`. So the minimal extension removes the zero but not the two-sided floor. Convex combinations whose saturated strands start on different links at `z`, and splits with every `a_t < d_m` (possible at `m ∈ {3, …, 7}`), are not bounded here.

### 8.6 The registers m = 1 and m = 9: endpoint matter is necessary

**Proposition G.** Let `m ∈ {1, 9}` and let `T` be a transporter covariant at `z` whose block for a summand with `|q_r| ≥ 10` is nonzero.
(i) Every nonzero entry of that block has a nonzero component that changes the matter number `N_z` by some `n` with `|q_r − n| ≤ 6`, so `|n| ≥ 4`, in the direction of `q_r`. The same holds at `z′`. So the block needs matter operators at both endpoints.
(ii) Such blocks exist. Put `ψ_u := c_{u,5}c_{u,4}c_{u,3}c_{u,2}c_{u,1}`, which is carried at `u` in `Λ^5V = det_V` (`V` is the annihilator representation), and let `𝒟 := J_0^T(𝒯^V_{π_1} ⊗ ⋯ ⊗ 𝒯^V_{π_5})\bar J_0`, with `J_0` the unit vector spanning `Λ^5V ⊂ V^{⊗5}` and `π_1, …, π_5` the link-disjoint paths of Proposition E from `z` to `z′`. Then `T_M := ψ_zψ_{z′}^†𝒟` is even, covariant at `z` in `det_V^2`, covariant with the inverse at `z′`, invariant elsewhere, and nonzero.

*Proof.* (i) On an entry `B`, the centre at `z` acts by `Ad e^{iθ(N_z+E_z)}` with `[N_z, E_z] = 0`. Split `B = Σ_nB_n`, `B_n := Σ_{a−b=n}P^N_aBP^N_b` with `P^N_a` the spectral projections of `N_z`. Each `B_n` is again covariant with charge `q_r`, and `Ad e^{iθE_z}(B_n) = e^{i(q_r−n)θ}B_n`. `E_z` has eigenvalues in an interval of diameter `6d_m = 6` (Lemma 8.1), so Lemma 5.1 gives `B_n = 0` unless `|q_r − n| ≤ 6`. (ii) `ψ_z` has charge `−5` at `z`; `𝒟` is a C-SPLIT transport with `a_t = 1 ≤ d_m`, of charge `−5` at `z` and `+5` at `z′`; `ψ_{z′}^†` has charge `+5` at `z′`. The product has ten fermion factors, so it is even. Covariance follows as in Lemma 8.2, with the matter factor contributing `det_V` at each end. `ψ_zψ_{z′}^† ≠ 0`: it maps the Fock vector with `z` full and `z′` empty to `±` the vector with `z` empty and `z′` full. `𝒟 ≠ 0` by the single-surviving-term argument of Proposition E with `a_t = 1`. Matter and links are different tensor factors, so `T_M = ±(ψ_zψ_{z′}^†) ⊗ 𝒟 ≠ 0`. □

**Candidate C-SPLIT-M (proposed for the owner; not adopted).** For `m ∈ {1, 9}` only: C-SPLIT, plus in the palette one fixed matter multiplet `ψ` carried at a site, built from that site's five modes, inserted at the two endpoints as the matrix `(ψ_zψ_{z′}^†)_{ab} := ψ^a_z(ψ^b_{z′})^†`, with `J : W_r → M ⊗ W_{s_1} ⊗ ⋯ ⊗ W_{s_k}`. Proposition G(i) shows that endpoint matter is necessary there, and G(ii) shows that this candidate has nonzero charged blocks.

Corollary F.1 still applies: on `L5-U[1]` and `L5-U[9]` every transporter, dressed or not, has `D_+ + D_− ≥ 1` for the charge-ten summand. C-SPLIT-M removes the zero and nothing more.

### 8.7 Summary by register, and the open statement it leaves

For a summand of charge `|q| = 10` (for example `det^{±2}`), with block sites as endpoints:

| `m` | `d_m` | strict (EW1) | link-only, C-SPLIT or C-NET | any charge-diagonal transporter |
|---|---|---|---|---|
| 1, 9 | 1 | zero; each defect `≥ 1` (Thm C) | zero (Thm D(ii)) | needs endpoint matter (Prop G); `D_+ + D_− ≥ 1` (Cor F.1) |
| 2, 8 | 2 | zero; each defect `≥ 1` | nonzero with 5 strands (Prop E); `D_+ + D_− ≥ 1` | `D_+ + D_− ≥ 1` (Cor F.1) |
| 3, 7 | 3 | zero; each defect `≥ 1` | nonzero with 4 strands; `D_+ + D_− ≥ 1` (Cor F.1) | no floor proved with endpoint matter |
| 4, 6 | 4 | zero; each defect `≥ 1` | nonzero with 3 strands; one minimal tuple: `D_+ + D_− ≥ 1` (Prop F′) | no floor proved |
| 5 | 5 | zero; each defect `≥ 1` | nonzero with 2 strands; one minimal tuple: `D_+ + D_− ≥ 1` (Prop F′) | no floor proved |

**T1-SPLIT (open; outside UQ, inside BK1 node T1).** On `L5-U[m]` with `m ∈ {4, 5, 6}` for link-only transporters, or `m ∈ {3, …, 7}` with endpoint matter, for the summand `det^{±2}`: do a fixed palette of transporters and, for every `δ > 0`, a state exist with both transport defects at most `δ`? This file proves no bound there beyond Proposition F′, which covers single minimal tuples and combinations sharing a saturated first link. It is node T1's question, narrowed by Corollary F.1. It is recorded, not worked.

## 9. Smuggle checks

The four tests are those of `TOE_ASSEMBLY.md` §3.2 (lines 173-176): a specification fails if it "states or fixes something that a part lists as its target", is "open-ended, so a part can add to it to get a result", "settles a downstream physics question by premise", or "adds a structure or a constant that its own reasons do not need". Verdicts are this pass's assessments for the owner. Nothing is adopted.

**C-SPLIT (§8.3).**
1. *Target.* Passes. It defines a transporter class. It asserts none of (O), (C), (A), (T), no orbit and no `3 + 2` channel.
2. *Open-ended.* Passes once pinned: the palette of splitting data `(σ_{s_t}; J)` is a finite list fixed with the triple `(W, σ, v)`; the path list for each block size is finite and translation covariant, as H-QUANTIFIERS already allows (`BK1_TREE.md` line 67: "The composites and finite transporter networks may change with the block size"); `c` and the factor order are fixed; the choice is independent of `Φ`. Fails if the palette may be chosen after the state or the composites: `EW1.md` line 105 shows that an unrestricted class makes (A) empty ("`T := Φ_XΦ_Y^†/|v|^2` is a covariant link-only operator").
3. *Downstream premise.* Passes. Every FMS clause stays a conclusion. Corollary F.1 and Proposition F′ show that (T) is not automatic in this class.
4. *Unneeded structure.* Passes for `2 ≤ m ≤ 8`: one strand per summand gives zero (Theorem C), a nonzero link-only block needs at least `⌈|q|/d_m⌉` links at each endpoint (Theorem D(i)), and covariance forces the join at each endpoint to be an intertwiner (Lemma 8.2). C-SPLIT adds exactly that join, with no interior vertex, no matter and no constant beyond the palette. Conditional at `m ∈ {1, 9}`, where its charged blocks are zero (Theorem D(ii)) and the added structure does nothing.

C-SPLIT is the sub-case of the tree's C-NET (`BK1_TREE.md` line 630) whose vertices sit only at the two endpoints. Its test-4 reason answers part of C-NET's open condition there, "justify it as coarse transport of composite charges".

**C-SPLIT-M (§8.6), for `m ∈ {1, 9}` only.**
1. Passes, as for C-SPLIT. 2. Passes once the matter multiplet is pinned in the palette. 3. Passes; Corollary F.1 shows that (T) still fails below `½`. 4. Conditional: endpoint matter is necessary for a nonzero charged block (Proposition G(i)), but it does not make (T) reachable on these registers. Its only reason is nonvanishing.

**Reading used: EW1's "fixed decomposition into irreducibles" is orthogonal (§3.3).** 1. Passes. 2. Passes; it is closed. 3. Passes: Theorem C uses only `W_cap`, which is canonical and orthogonal to its complement by Lemma 3.4, so the floors are the same for a non-orthogonal decomposition. 4. Passes; it adds nothing the proofs need.

**H-strict (§8.1)** is a description of EW1 Definition 2.3, not a new specification.

## FINISH

**Proved (author-side, pass 1; not yet distilled or refereed).**
- Setting: Lemma 3.1 (end numbers, `d_m = min(m, 10 − m)`), Lemma 3.2 (letter charges), Lemma 3.3 (HS basis independence), Lemma 3.4 (charge eigenspaces).
- **Theorem A** (with Lemmas 4.1-4.4): every summand of a bosonic composite on `L5-U` has even central charge; an `H`-fixed nonzero component has `5 | q_r`; so every nonzero bosonic `H`-fixed charged component has `q_r ∈ 10Z ∖ {0}`. Two proofs: central characters, and weights `(n, …, n)`.
- **Theorem B** (with Lemmas 5.1-5.2): on one link of `L5-U[m]`, every operator covariant at one end with central charge `|q| > d_m` is zero; so the single-link representation matrix of every such summand, and its adjoint, vanish on every link of every `L5-U[m]`, for every realization, copy, factor order and normalization. Two proofs: spectral blocks, and CAR normal ordering. Corollary 5.3 (the spin-`S` Abelian rung), Lemma 5.4 (exterior-power links move exactly when `a ≤ d_m`), Remark 5.5 (the tree's determinant carriers need `m = 5`).
- **Theorem C**: every strict transporter between distinct sites is zero on `W_cap`, and `‖T^†T − 1‖^2_HS ≥ dim W_cap`, `‖TT^† − 1‖^2_HS ≥ dim W_cap` as operator inequalities, hence in every state; both floors equal 1 and are attained for `det^{±2}`. Corollary C.1 (no state meets (T) below `dim W_cap`), Corollary C.2 (alignment floor from (O), (C), (A), free of operator norms), Corollary C.3 (the strict U branch of BK1 has no instance on any `L5-U[m]`), Remark 6.1.
- Attacks: Lemma 7.1 (no mixing on one link), Lemma 7.2, Proposition 7.3 (projection after the path product also vanishes).
- Extension: Lemma 8.1, **Theorem D** (a nonzero link-only charged block needs `⌈|q|/d_m⌉` links at each endpoint; none exists at `m ∈ {1, 9}` for `|q| ≥ 7`), Lemmas 8.2-8.3, **Proposition E** (C-SPLIT has nonzero charge-ten blocks for `2 ≤ m ≤ 8`), **Theorem F** (two-sided capacity: `D_+ + D_− ≥ Σ dim W_r` whenever `2|q_r|` exceeds the spectral diameter at the endpoint), Corollary F.1, Proposition F′, **Proposition G** (at `m ∈ {1, 9}` a nonzero charge-ten block needs matter at both endpoints, and an explicit dressed block is nonzero).

**Counterexamples.** None to UQ: §7.4 shows that no admissible datum escapes Theorem C. Proved negatives for neighbouring statements: (1) the strict U branch of BK1's root fails on every `L5-U[m]`, `1 ≤ m ≤ 9`, at every tolerance below 1 (Corollary C.3); (2) on `L5-U[1]`, `L5-U[2]`, `L5-U[8]`, `L5-U[9]` no charge-diagonal transporter of any class reaches (T) below `½` for charge-ten data carried at block sites, and on `L5-U[3]`, `L5-U[7]` no link-only transporter does (Corollary F.1).

**Open by name.** For UQ: none; each named attack fails at its named step (§7). Downstream, outside UQ: **T1-SPLIT** (§8.7), two-sided transport of `det^{±2}` on `L5-U[4]`, `L5-U[5]`, `L5-U[6]` (link-only) or `L5-U[3]`-`L5-U[7]` (with endpoint matter), recorded and not worked.

**What changes downstream.**
- BK1 node UQ: proved here at pass 1, with the sharper floor `dim W_cap` and an added alignment floor. The strict U branch of BK1's root is refuted on every live U register. Nothing is said about `L5-O`.
- BK1 node T1 and the C-NET branch: the smallest change that removes the zero is C-SPLIT (endpoint joins of several strands), and it does so exactly for `2 ≤ m ≤ 8`. By Corollary F.1, two-sided transport of charge-ten data carried at block sites is excluded for every class of charge-diagonal transporters on `m ∈ {1, 2, 8, 9}`, and for link-only classes on `m ∈ {3, 7}`. The U-law network branch with single-site endpoints therefore lives only on `L5-U[4]`-`L5-U[6]` (link-only) or `L5-U[3]`-`L5-U[7]` (dressed endpoints). Elsewhere a change beyond the transporter would be needed, such as composites carried on several sites, which the tree calls "Distributed endpoints" (`BK1_TREE.md` line 306); no such change is proposed here. The tree's T1 candidate `D_{π_1}D_{π_2}` on one path pair has `max(D_+, D_−) ≥ ½` (Proposition F′).
- BK1 node C1: the determinant carrier `B_xD_{xy}B_y` is nonzero only on `L5-U[5]` (Remark 5.5).
- BK1 node A1: step 1 of its capacity ladder is Corollary 5.3. The lemma its step 3 asks for (`BK1_TREE.md` lines 362-369, "This bound itself needs a written lemma") follows from the proof of Theorem F applied to one spin-`S` link with `E = S^3` in place of `Q_z`: the spectral diameter is `2S = 2` and `2|q| = 4 > 2`, so `D_+ + D_− ≥ 1` and `max(D_+, D_−) ≥ ½` for every charge-two operator on one spin-1 link, in every state. At `S = 2`, `2|q| = 4` does not exceed `2S = 4`, and the argument gives no floor, as the tree's step 4 expects.
- EW1-U: strict transport of the charge-four datum `Λ^4C^5` is identically zero on `L5-U[m]` for `m ∈ {1, 2, 3, 7, 8, 9}` (Remark 6.1).
- FMS's path-localized fields (L4) do not port strictly to `L5-U` for bosonic `H`-fixed charged representations.
- No law, axiom, reading or working-set entry changes. C-SPLIT and C-SPLIT-M are candidates for the owner with their four-test verdicts (§9); neither is adopted, and no FMS property of either is claimed.
