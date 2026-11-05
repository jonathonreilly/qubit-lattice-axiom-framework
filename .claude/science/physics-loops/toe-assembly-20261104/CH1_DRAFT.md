# CH1, pass 1 (long draft): chirality, a gauged chiral light sector

Written 2026-11-04 by a Claude Opus 5.5 subagent, as pass 1 of part CH1 of the TOE assembly (method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (scripts outside the repo, under 100 MB, under a minute); a check guides and never proves. Nothing here is a verdict.

**Source revisions read** (through `git show` and `gh`, after `git fetch -q origin` on 2026-11-04):

| Ref | Commit |
|---|---|
| `origin/main` | `f5af11cd01` |
| `origin/claude/toe-assembly` (skeleton, LW1 draft, section 3.2) | `f3f61bed43` |
| `origin/docs/consolidate-chirality-doublers` (#10131 synthesis) | `a1bced899b` |

The closed source PRs #9863, #9911, #9992, #10004, #10030, #10049, #10073 and #10085 were read in the verbatim copies of their note text and `claim_scope` that the #10131 synthesis carries (file `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` at `a1bced899b`; each copy names its source branch and head). #9927 and #9939 were read in the synthesis's "logged" table (scope text only). Literature: arXiv abstracts fetched on 2026-11-04 for Thorngren-Preskill-Fidkowski (arXiv:2601.04304), Golterman-Shamir (arXiv:2505.20436), Sun-Xiao-Bzdusek-Zhang-Fan (arXiv:1806.09296) and Higashikawa-Nakagawa-Ueda (arXiv:1806.06868); other references are from memory and are labelled so. Citations are never load-bearing: every lemma a proof uses is rebuilt here, or the step is marked "credited".

**Owner guidance applied.** "our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms are read plainly.

**Working set used, by name.** PS-1 (the finite-depth clause, Theorem F1), PS-1c (the covariance group and transitivity, Lemmas S1 and C3), PS-6 with PS-6r (the gauge group and finite link registers, Lemma S1, Lemma C2), PS-7 with PS-7r (the sea and its gap at `pi`, Corollary F2a, Theorem F3). PS-8 is a law to test (section 5), never a premise. PS-2, PS-3, PS-3h, PS-3c, PS-4, PS-11 and PS-11c are not used: chirality is a property of the update and the vacuum, and no step below reads records or actual configurations. (The records route to chirality is closed on file: #9895 "every history chosen by records, conditional odds, c-number link feedback or an adversary has flow index 0".)

---

**Lead note, 2026-11-04 (after LW1 pass 2).** Theorem S3 (i) and owner decision D1 cite LW1 Theorem B5 for frames on cells. The LW1 distillation (`LW1.md`, GAP B5(b)) found the draft's cell form false as stated: independent site phases, compensated on the cell's internal links, satisfy its hypotheses and are not scalar. It also found that the exclusion of non-abelian cell-mixing frames still needs a proof. What stands is B5(a), site-local frames. So S3 holds under PS-6 read per site, which is PS-6's own wording ("The internal frame of each site's possibilities is local"). For cell frames it waits on B5(b). D1 is not put to the owner until B5(b) is settled. Lemma S1 and Theorem S2 do not use B5(b).

## 0. The target, quoted

From the skeleton (`TOE_ASSEMBLY.md`, CH1 (a)):

> "Within `L` there is a local lattice theory, invariant under `G`, whose light spectrum at scales `>> a` is exactly the chiral content of CG1 (one Weyl 16, or the Standard Model multiplet, per family), with every doubler and every mirror gapped at scale `~ 1/a` [**open input CH1-i**: symmetric mass generation for the mirrors without releasing light partners], no extra light charged state, gauge anomalies cancelling, the gauge field kept massless [**open input CH1-ii**: a local gauged measure], and the measure reflection positive."

Premises listed there: "PS-1, PS-5, PS-6, PS-8. Imports: MT1, GA1, ZM1". Order of attack (skeleton section 7.3, item 2): "Ladder: 1+1D rotors (#9927, #9939) -> 2+1D -> the 3+1D wall with PS-8. Kill first: test whether PS-8's mirror term releases light partners on the chosen carrier (it does in #9911, #9992)."

`L` is the law chosen in LW1: `L_cube`, the cube tick with one fermion mode per site, flux `pi` on every unit face, two Margolus tilings, gauged by `U(1)` link registers (`LW1_DRAFT.md` section 4). LW1's Theorem B5: "one mode per site gives no non-abelian frame group for the tick".

## 0.1 Summary of the outcome

**Outcome in one line.** On the chosen law, the kill test is negative for PS-8: no free update has a chiral light sector at any locality (proved), PS-8 acting on the elementary content must release light partners (proved at every quasi-free endpoint; forced by anomaly matching in general), and the exact gauge `U(1)` of `L_cube` cannot be hypercharge (proved). What is left of CH1 on `L_cube` is a chiral sector of odd-charge bound states; its 1+1D form is the first open statement, Lemma CH1-C1.

**Proved here (pass 1, not refereed):**

1. **Theorem F1.** Every finite-depth circuit of number-conserving quasi-free gates, covariant under a finite-index sublattice of `Z^d`, has a Bloch unitary that is homotopic to the identity. So `W3 = 0` and every `W1 = 0`. This proves lead 1 in full for PS-1's clause "built from finitely many layers of nearest-neighbour gates", by an elementary argument; #9863 had it for "products of coins and coin-conditioned shifts" and cited the vanishing of `SK1` of the Laurent ring for the finite-range case.
2. **Theorem F2.** If one quasi-energy is in a gap at every momentum, the Bloch unitary is homotopic to the identity, at any locality. The PS-7r sea needs a gap at `pi`. So **every free update that has a PS-7r sea has `W3 = 0`**, whatever its range (Corollary F2a).
3. **Theorem F3 (a Floquet Nielsen-Ninomiya theorem, any locality).** For any Bloch unitary that is `C^1` in momentum and any sea that fills the arc between the cuts `0` and `pi`, the Berry monopole charges of all light pockets (at both cuts) sum to zero, in each charge sector. Near a Weyl node at `pi` the filling is inverted, so the cut-`pi` pockets enter with the opposite sign. The light content of every free sea is therefore vector-like, charge by charge. Locality plays no role.
4. **Theorem F4.** With linear Weyl nodes, the net chirality at the cut `0` equals the net chirality at `pi` (each read with its own lower band), and both equal `sigma W3`, with one universal sign `sigma`. So `W3` only decides how the light Weyl content splits between the two cuts. This answers lead 2: a quasi-local walk or a QCA with `W3 != 0` (#9863's walk) has no gap at any quasi-energy, so it has no PS-7r sea, and by F3 its light content is still vector-like.
5. **Lemma S1 (charge parity).** On one-mode sites under PS-6 and PS-1c, every fermionic excitation has an odd gauge charge (in units of the elementary charge) and every bosonic one an even charge.
6. **Theorem S2.** If the exact `U(1)` of `L_cube` acts on one Standard Model family (with `nu^c`) as `X = aY + b(B-L)`, then `(a, b) = q(2 alpha, beta)` with `alpha` even, `beta` odd and `alpha + beta = 0 mod 3`. **Hypercharge alone and electric charge are excluded.** `B-L` and the `SO(10)` charge `5(B-L) - 4Y` are allowed. On `L_cube` every neutral excitation is a boson.
7. **Lemma C3.** Under PS-1c's covariance group, a partition of `Z^3` into clusters of one odd size that the law fixes (a partition invariant under the group) has cluster size 1. The 1D analogue holds too. So odd composite charges cannot be built into the law as a fixed layout. They must arise as bound states.
8. **Theorem K1 (the kill test at its endpoints).** For any cell-local choice of "mirror" modes and any endpoint at which the light modes move under a quasi-free, covariant dynamics, the light sector is vector-like in each charge sector (from F3). On `L_cube` all charges are equal, so a light Weyl node kept at `K = 0` forces released partners of the opposite chirality. This extends #9911's endpoint result for one supplied `H'` to every cell-local mirror and to Floquet updates.
9. **Lemma C2 (cluster modes).** On a set of `s` sites with `s` odd, the product of the `s` mode operators is an exact fermion mode of charge `s` on the subspace where the set is empty or full. Gauge-covariant cluster hops keep that subspace exactly.

**Found here (conflicts with the target as worded):**

- CH1 (a) asks for "the chiral content of CG1" invariant under `G`. On `L_cube`, `G` is `U(1)` (LW1 B5). By Theorem S2 that `U(1)` cannot be hypercharge. So CH1 (a) cannot hold on `L_cube` with `G` the exact gauge group. It needs PS-5's fallback or a non-abelian structure that emerges at long distance. For PS-5 this is a named failing step of the cell route ("used only if the cell route fails at a named step"). The owner decides.
- PS-8 as worded ("the unique singlet interaction of the block's mirror modes") is aimed at keeping one chirality of the elementary charge-1 content. On `L_cube` that content is anomalous for the gauge `U(1)` (Theorem K2), so the aim is excluded at every quasi-free endpoint (K1), and by anomaly matching in general (Lemma AM, a standard principle, not proved here for interacting Floquet updates).

**No proposed specification.** No widening of PS-1 is proposed. The free obstruction (F3) holds at every locality, so widening PS-1 to quasi-local or QCA updates would add structure that its own reasons do not need (smuggle test 4). Section 10 gives the reasons, and lists two owner decisions that the results raise.

**First open statement: Lemma CH1-C1** (section 7). In 1+1D, on one-mode sites with `U(1)` quantum links, there is a gauge-covariant finite-depth update and an invariant stationary state whose light excitations are the anomaly-free chiral set L: `(1, 7)`, R: `(5, 5)`. Three distinct attacks are written out, with the exact reason each fails: free (Theorem F3 forbids it), a cluster layout fixed by the law (Lemma C3 forbids it, and once covariance is relaxed it reduces to an unproved strong-coupling flow), and symmetry disentanglers (they need infinite-dimensional rotors, which the Qubit axiom and PS-6r do not allow).

---
## 1. Sources and what each one states

Each line quotes the text before saying what it shows.

### 1.1 Axioms and working set

- Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." "No site is privileged."
- Qubit: "The full one-site possibility domain has algebraic presentation `M_2(C)`."
- Admissibility: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." And: "Admissibility is not a dynamics axiom."
- PS-1: "There is one fixed update. It acts on the joint possibilities of all sites as a unitary map built from finitely many layers of nearest-neighbour gates, covariant under lattice translations and proper cubic rotations."
- PS-1c: "the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre, and its symmetry group acts transitively on sites."
- PS-6: "The internal frame of each site's possibilities is local. Each nearest-neighbour link carries a register that transports frames between its two sites. The update is unchanged when the frame at one site and the registers on its links are changed together."
- PS-6r: "Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs."
- PS-7r: "the half-filled sea of a tick is the quasi-free state that fills every one-body mode with quasi-energy in `(-pi, 0)`, quasi-energy read in `(-pi, pi]`. It is defined when `pi` lies in a gap."
- PS-8 (law to test): "The update includes, on each matter block, the unique singlet interaction of the block's mirror modes, at a coupling large against the hop." The skeleton's reason: "#9992 (chirality theme): the block-local quartic gaps the Dirac mirror symmetrically ... but "releases the light partners"."

### 1.2 LW1 results used (`LW1_DRAFT.md`, pass 1)

- Definition A1 and Theorem B10: the one-body tick `V = V_o V_e`, `V_e = exp(-i(eps - mu/2) R_e)`, `V_o = exp(+i(eps + mu/2) R_o)`, with bands `cos w = A S(K) - B` and "each value with multiplicity 4 for each sign of `w`"; "`|w|` lies in `[mu, 2 eps]`"; for `mu = 0` "the band touches `w = 0` only at `K = 0`".
- Theorem A2: the exact covariance group is "`G_U = 2Z^3 ⋊ O_{c_0}` (translations of the cell lattice, rotations about cell centres)"; Corollary A2a: it acts transitively on sites, and "The stabiliser of a site in `G_U` is `C_3`".
- Lemma B3: the frame group of one fermion-mode site is `O(2)`, "The subgroup that commutes with the number operator `sum n` is `U(1)`."
- Theorem B4: exact `U(1)` Gauss laws `G_x = n_x + sum_{out} E_l - sum_{in} E_l`.
- Theorem B5: for one-body frame actions, "the image of `G` in the transformations of the modes is abelian". Its scope: "It covers one-body (mode-linear) frame actions."
- Section 7.2: "Without the copy mass the light content at `K = 0` is two degenerate Dirac copies (#10016: "the four tastes are E + E")."

### 1.3 The chirality theme (#10131 synthesis at `a1bced899b`)

- Synthesis answer: "**Answer: not obtained.** No kept result constructs a consistently gauged chiral light sector in 3+1D with its mirror and doublers removed. What remains is supplied-model, finite, 1+1D or Euclidean-only."
- #9863, claim scope: "For supplied two-component SU(2) walks on Z^3, the net chirality of the Weyl cones at quasi-energy 0 equals that at quasi-energy pi and equals minus the 3D winding W3; products of coins and coin-conditioned shifts have W3 = 0, and a supplied quasi-local walk with W3 = -1 has a single cone at quasi-energy 0 and an exponential tail". Its text: "That every finite-range walk has W3 = 0 follows from the vanishing of SK1 of the Laurent ring C[Z^3]; this input is cited, not rederived." And: "At m = -2 it has exactly one cone at quasi-energy 0, at k = 0 with chirality +1, and all seven doublers at pi (four of +, three of -)." What it shows: the degree theorem for two bands; the finite-range case rests on a cited K-theory input. Theorems F1-F4 below rebuild the circuit case, extend to `n` bands, and add the light-content statement.
- #9911, claim scope: "with the mirror gapped the light copy has 8 Weyl nodes per sublattice (4 left, 4 right), a vector-like spectrum; a 1+1D chain shows the same release". Its derivation: "Any endpoint that freezes local light combinations leaves a finite-range free Hamiltonian, whose nodes have net chirality zero per sector by Nielsen-Ninomiya". What it shows: the endpoint argument for one supplied `H'`. Theorem K1 is that argument for every cell-local mirror and for Floquet updates.
- #9992, claim scope: "the Dirac mirror is massless for g/t <= 2, crosses over near g/t ~ 4, and is symmetric and gapped for g/t >= 8 ... the symmetric mirror gap releases every light mode the mirror was pairing (exact at the Dirac point once the mirror propagator has a zero). The toy is not Spin(10), the band is not the CL-1 cube tick". What it shows: the release in a finite sign-free toy, not on `L_cube`.
- #10004, claim scope: "Survival of the K gap as L -> infinity is not established: inconclusive." And: "an exhaustive search of the band commutant finds every Z4-type symmetry of H_int at Z16 index 0 mod 16".
- #10030, claim scope: "with a Weyl at K = 0 at quasienergy 0, the light-labelled sector is gapless at or around every X and M -- a node at quasienergy 0 or pi, a crossing surface, or a zero of the light block. No light-light partner mass exists."
- #10049, claim scope: "for any g5-hermitian kernel, V = g5 sign(g5 X) is unitary and D = 1 + V obeys the Ginsparg-Wilson relation ... The 3+1 tick unitary U(K) itself is not such a V". "Not covered: a chiral walk (tick) realisation, reflection positivity of the chiral theory, non-abelian chiral existence (open in the literature)".
- #10073, claim scope: "(A1) In each turn sector the net eigenphase flow through every quasi-energy equals the det winding W_a, so W_a != 0 puts a BULK Bloch eigenstate at every quasi-energy (pi included) on the axis loop ... (A2) Every interval filling has flow W at both cuts; intersection lemma: a band filling with no occupied-empty touching on the axis forces W = 0." What it shows: the one-loop (1D) form of Theorems F2 and F3, on the turn axis.
- #10085, claim scope: "NOT met: the headline (c4 vanishing like p^2 with T-agreement)". The corrections section: "#10085 does not show that the one-family four-field coefficient is non-local".
- #9927 (logged), scope: "on chains of one-mode fermion sites with the staggered hop, the vector charge and the Kitaev-pairing axial charge are exact, but the chiral 3450 combination has non-integer one-body and many-body spectra, so no circuit, free or interacting, on-site or not, makes it an exact U(1) (spectral obstruction). With non-slipping rotor matter (an angle per site and a winding integer per link), the rederived Thorngren-Preskill-Fidkowski disentangler ... maps the 3450 symmetry exactly onto an on-site ancilla symmetry ... With Z_5 clocks only Z_5 is exact." And: "no derivation of rotor matter from the axioms".
- #9939 (logged), scope: "A construction on fermion modes plus two supplied SU(2)-singlet compact rotors ... leaves exactly free Weyl modes ... Supplied model, finite diagnostic: rotor matter, charges, locking couplings and forward scattering supplied; the flow to the locked phase is cited, not computed; 1+1D only."

### 1.4 Literature (credited; never load-bearing)

- Thorngren, Preskill, Fidkowski, "Chiral Lattice Gauge Theories from Symmetry Disentanglers", arXiv:2601.04304 (abstract fetched): symmetry disentanglers are "constant-depth circuits of local unitaries" that make not-on-site symmetries on-site; built "using lattice rotor models" for `U(1)` symmetries with cancelling mixed anomalies in 1+1D and 3+1D; "an exactly solvable lattice Hamiltonian for the (1+1)-dimensional "3450" chiral gauge theory". From a fetch of the HTML text (quotes as returned by the fetch tool): the result has "a tensor-product Hilbert space, albeit with infinite-dimensional rotor degrees of freedom"; the hypercharge step rests on a "plausible but unproven conjecture"; the gauged model's low-energy spectrum is not computed in the part read.
- Golterman, Shamir, "Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories", arXiv:2505.20436 (abstract fetched): using "a one-particle lattice Hamiltonian, the authors derive conditions under which the Nielsen-Ninomiya theorem applies. When those conditions hold, the massless fermion spectrum must be vector-like, regardless of interaction strength"; they conjecture that SMG interactions produce bound states of opposite chirality.
- Sun, Xiao, Bzdusek, Zhang, Fan, "Three-dimensional Chiral Lattice Fermion in Floquet Systems", PRL 121, 196401 (2018), arXiv:1806.09296 (abstract fetched): "the Nielsen-Ninomiya no-go theorem still holds on Floquet lattice"; a low-energy sub-block can carry one handedness in the adiabatic limit.
- Higashikawa, Nakagawa, Ueda, "Floquet chiral magnetic effect", PRL 123, 066403 (2019), arXiv:1806.06868 (abstract fetched): a single Weyl fermion "can arise in a periodically driven three-dimensional lattice", requiring a Floquet unitary "with nontrivial topology".
- From memory, not re-fetched: Nielsen and Ninomiya (1981); 't Hooft (1980, anomaly matching); Eichten and Preskill (1986, mirror gapping); Luscher, "Abelian chiral gauge theories on the lattice with exact gauge invariance", Nucl. Phys. B549 (1999) 295; Hernandez, Jansen and Luscher (locality of the overlap for admissible fields); Fidkowski and Kitaev (2010, `Z -> Z8` for interacting Majorana chains); Wang and Wen (the 3-4-5-0 model, PRD 99, 111501 (2019)); Zeng, Zhu, Wang and You (DMRG evidence for symmetric mass generation in 3-4-5-0, 2022); Tong, "Comments on symmetric mass generation in 2d and 4d" (2021); Razamat and Tong, "Gapped chiral fermions" (PRX 2021); Golterman and Shamir on propagator zeros (2023-2024); Haldane (2004) and Son and Yamamoto (2012) on Fermi-surface Berry monopoles and the chiral anomaly; Rudner, Lindner, Berg and Levin (2013, anomalous Floquet); Gross, Nesme, Vogts and Werner (2012, GNVW index); Freedman and Hastings (QCA classification); Fidkowski, Po, Potter and Vishwanath (fermionic QCA index).

---

## 2. Conventions

**C1. Carrier.** As in LW1 C1: one fermion mode `c_x` per site of `Z^d` (`d = 3`, or `d = 1` for the 1+1D rung), the CAR algebra, even local operators (LW1 C2). In section 3 the number of modes per site, `r`, is arbitrary, so the free theorems cover every carrier.

**C2. Free updates and Bloch unitaries.** A *free update* is the Fock lift `Gamma(V)` of a one-body unitary `V` on `l^2(Z^d) ⊗ C^r`. It is *covariant under* a sublattice `Lambda` of finite index if `V` commutes with the translations of `Lambda`. Fix a fundamental domain `D` of `Lambda` (`|D| r = n`). The Bloch transform makes `V` a multiplication operator by a matrix function `U : T^d -> U(n)`, `T^d` the dual torus of `Lambda`. A change of fundamental domain `x -> x + lambda(x)` (`lambda(x)` in `Lambda`) conjugates `U(k)` by the diagonal unitary `Delta(k) = diag(e^{i k.lambda(x)})`. Finite range gives `U` with Laurent-polynomial entries; exponential decay gives `U` real-analytic. Below `U` is `C^1` at least, and `C^3` in Theorem F4.

**C3. Quasi-energy and cuts.** The quasi-energies of `U(k)` are the `w` with eigenvalue `e^{-iw}` (as in LW1 B10). For a cut `a` in `R/2piZ`, `N_a = {k : e^{-ia} in spec U(k)}`. The cut `a` is *in a gap* if `N_a` is empty.

**C4. The sea.** The *sea* is the gauge-invariant quasi-free state whose one-body projection is `P(k)`, the spectral projection of `U(k)` onto quasi-energies in `(-pi, 0)`, i.e. onto eigenvalues in the open upper half of the unit circle. Where `1` and `-1` are not eigenvalues, `P(k)` is the Riesz projection `(1/2 pi i) oint_Gamma (z - U(k))^{-1} dz` along a contour `Gamma` that crosses the unit circle only at `+1` and `-1`; so `P` is `C^1` (as smooth as `U`) on `T^d \ (N_0 ∪ N_pi)`. Under PS-7r the sea "is defined when `pi` lies in a gap"; Theorem F3 also treats seas without that gap.

**C5. Light pockets and their charges.** *Light* means low quasi-energy excitations of the sea, read modulo `2 pi`. They sit near `N_0` and near `N_pi`. (Near `N_pi`, moving a particle from just above `-pi` (filled) to just below `pi` (empty) changes the quasi-energy by `2pi - delta`, i.e. by `-delta` modulo `2 pi`. So cut-`pi` excitations are light in a Floquet law. #10072 treats them so: "its free pi copy is excluded by estimates with supplied numbers".) A *pocket decomposition* is a finite family of disjoint closed balls `B_j` in `T^3` with `N_0 ∪ N_pi` inside their union and none of `N_0 ∪ N_pi` on their boundaries. The *pocket charge* is
`c_j = (i / 2 pi) ∫_{∂B_j} tr(P dP ∧ dP)`,
with `∂B_j` oriented as the boundary of `B_j`. It is the Berry monopole charge of the filled states around the pocket (the first Chern number of the bundle `ran P` over the sphere). For a Fermi pocket it is the anomaly coefficient of the pocket (Haldane; Son and Yamamoto; credited, used only to name the quantity).

**C6. Weyl nodes and chirality.** A point `k_0` of `N_a` is a *linear Weyl node* if `e^{-ia}` is a double eigenvalue of `U(k_0)` and, on that two-dimensional eigenspace, `e^{ia} U(k_0 + q) = 1 - i (M q).sigma - i t(q) + O(q^2)` with `det M != 0` and `t` a scalar linear form. Its *local Hamiltonian* is `h(q) = (Mq).sigma + t(q)`. Its *chirality* `chi` is the Chern number of the lower band of `h` on a small sphere around `q = 0`, with the normalisation of C5. (It is `+-sign det M`, with one fixed sign convention.)

**C7. Vector-like.** Suppose `V` commutes with a site-local, `Lambda`-invariant charge operator with integer eigenvalues. Then `U(k)` is block diagonal by charge, and each block has its own pockets. The free light content is *vector-like* if, for each charge value, the pocket charges of that block sum to zero. For Weyl nodes this says that the net chirality of the light content of each charge is zero (with the sign of C5, which counts a cut-`pi` node with the opposite sign; Lemma F3a). Vector-like content has no gauge anomaly. The converse fails: an anomaly-free set such as L: `(1,7)`, R: `(5,5)` is not vector-like.

**C8. Windings.** `omega = (1/24 pi^2) tr((g^{-1} dg)^3)` on `U(n)`. `W3(U) = ∫_{T^3} U^* omega` (the orientation of `T^3` comes from the coordinates `k_1, k_2, k_3`). `W1` along a loop is the winding number of `det U`. Three facts are used, each with a one-line proof. (i) `omega` is closed: `d(g^{-1}dg) = -(g^{-1}dg)^2`, so `d tr(A^3) = -tr(A^4)`, and `tr(A^4) = 0` for a matrix 1-form `A` (cyclicity of the trace moves one factor past three 1-forms with sign `(-1)^3`). (ii) For a scalar phase `e^{i theta}`, `omega(e^{i theta} g) = omega(g)`: `g^{-1}dg` gains `i dtheta 1`, and the cross terms contain `dtheta ∧ dtheta = 0` or `tr(A ∧ A) = 0`. (iii) `omega` is additive on block-diagonal maps, and vanishes on maps whose image lies in a one-parameter family of commuting matrices. Homotopy invariance of `W3` follows from (i) and Stokes's theorem on `T^3 x [0,1]`.

---
## 3. Rung F: free updates, any dimension, any locality

This rung answers leads 1 and 2. It is the hardest-first kill of the cheapest route: if a free update could carry a chiral light sector, CH1 would not need PS-8 at all.

### 3.1 Finite-depth circuits (lead 1)

**Theorem F1 (finite-depth quasi-free circuits are null-homotopic).** Let `V = V_L ... V_2 V_1` be a one-body unitary on `l^2(Z^d) ⊗ C^r`. Each *layer* `V_l` is a direct sum of unitaries `u_B` on `l^2(B) ⊗ C^r`, over a family `F_l` of pairwise disjoint finite blocks `B` that covers `Z^d` (blocks of one site carry on-site unitaries). Each layer is covariant under a sublattice `Lambda_l` of finite index: `F_l` is `Lambda_l`-invariant, and `u_{B + lambda}` is the translate of `u_B`. Let `Lambda = ∩_l Lambda_l`, which has finite index. Then the Bloch unitary `U : T^d -> U(n)` of `V` over `Lambda` is homotopic to the constant `1` through continuous maps `T^d -> U(n)`. Hence `det U(k)` is constant, every `W1` is zero, and for `d = 3`, `W3(U) = 0`.

*Proof.* Step 1 (one layer has a constant Bloch matrix in an adapted domain). `Lambda` acts on `F_l` without fixed points, because a nonzero translation fixes no finite set. Choose one block from each `Lambda`-orbit of blocks. Let `D_l` be the union of the chosen blocks. `D_l` is a fundamental domain of `Lambda`. Every site `x` lies in a unique block `B`, and `B = lambda + B'` for a unique chosen `B'` and a unique `lambda` (uniqueness of `lambda` because the action is free). So `x - lambda` is in `D_l`. If `x - lambda` and `x - lambda'` were both in `D_l`, then the blocks `lambda + B'` and `lambda' + B''` would both contain `x`, so they would be equal. Then `B'` and `B''` would be in one orbit, so `B' = B''` and `lambda = lambda'`. In the Bloch basis built on `D_l`, the layer maps the copy `lambda + D_l` to itself, with the same matrix `C_l = ⊕_{B'} u_{B'}` in every copy. So its Bloch matrix is the constant `C_l`.
Step 2 (common domain). Fix one fundamental domain `D`. By C2, in the `D` basis, `V_l(k) = Delta_l(k) C_l Delta_l(k)^{-1}`, with `Delta_l(k)` diagonal with entries `e^{i k.lambda_l(x)}`.
Step 3 (homotopy). `U(n)` is path-connected: write `C_l = W diag(e^{i theta_1}, ..., e^{i theta_n}) W^*` and set `C_l(t) = W diag(e^{i t theta_j}) W^*`. Then `U(k; t) = prod_l Delta_l(k) C_l(t) Delta_l(k)^{-1}` is continuous in `(k, t)`, unitary, and equals `1` at `t = 0` and `U(k)` at `t = 1`.
Step 4 (windings). `det U(k) = prod_l det C_l` does not depend on `k`, so every `W1` is zero. `W3` is a homotopy invariant (C8), and `W3(1) = 0`. ∎

*Remark (layers of overlapping commuting gates).* PS-1 speaks of "layers of nearest-neighbour gates". If a layer is given as a product of commuting gates whose supports overlap, it can be rewritten as finitely many layers of disjoint gates. Take a sublattice `Lambda' ⊂ Lambda` so sparse that two translates of one gate by distinct elements of `Lambda'` are disjoint. Then colour each gate by (its `Lambda`-orbit, its coset in `Lambda / Lambda'`). Each colour class is a `Lambda'`-covariant layer of disjoint gates. Since the gates commute, the order of the classes does not matter. So Theorem F1 covers every reading of PS-1's clause for quasi-free gates.

*Scope.* It covers the free cube tick of `L_cube`: each half-tick is a direct sum over the cubes of one tiling, covariant under `2Z^3` (LW1 Definition A1 (2) and (5)). It covers any number of modes per site, any gate range, any finite depth. It does not cover interacting gates, which have no Bloch unitary, or a gauged tick in a background that breaks `Lambda`.

*Relation to #9863.* #9863 states "products of coins and coin-conditioned shifts have W3 = 0" for two bands, and, for all finite-range walks, cites "the vanishing of SK1 of the Laurent ring C[Z^3]". Theorem F1 is the circuit case for any number of bands, proved without K-theory. The finite-range (QCA) case is discussed in 3.6.

### 3.2 A gap at one cut (any locality)

**Theorem F2.** Let `U : T^d -> U(n)` be continuous and let one cut `a` be in a gap. Then `U` is homotopic to `1`. In particular every `W1` is zero and, for `d = 3`, `W3(U) = 0`.

*Proof.* By compactness of `T^d` and continuity, the spectrum of `U(k)` stays at distance at least some `delta > 0` from `e^{-ia}`. Let `Log_a` be the branch of the logarithm on `C \ {t e^{-ia} : t >= 0}` with imaginary part in `(-a - 2pi, -a)`. Then `H(k) = i Log_a(U(k))` is defined by the holomorphic functional calculus on a contour that avoids the ray. It is continuous in `k`, Hermitian, and `U(k) = exp(-i H(k))`. `U_t(k) = exp(-i t H(k))`, `t` in `[0,1]`, is the homotopy. ∎

**Corollary F2a (the PS-7r sea forces `W3 = 0`).** If a free update has a PS-7r sea, then its Bloch unitary has `W3 = 0` and all `W1 = 0`, at any locality. *Proof.* PS-7r: the sea "is defined when `pi` lies in a gap". Apply Theorem F2 with `a = pi`. ∎

**Corollary F2b.** If `W3(U) != 0`, every quasi-energy is in the spectrum of some `U(k)`. This is the 3D form of #10073 (A1) ("W_a != 0 puts a BULK Bloch eigenstate at every quasi-energy").

### 3.3 The light content of every free sea (any locality)

**Theorem F3 (Floquet Nielsen-Ninomiya).** Let `U : T^3 -> U(n)` be `C^1`. Let `B_1, ..., B_m` be a pocket decomposition (C5) for the cuts `0` and `pi`. Then `sum_j c_j = 0`. If `V` commutes with a charge operator (C7), the same holds in each charge block. So the free light content is vector-like.

*Proof.* Let `M = T^3 \ ∪_j int B_j`, a compact 3-manifold whose boundary is the union of the spheres `∂B_j`. On `M` neither `1` nor `-1` is an eigenvalue, so `P` is `C^1` on a neighbourhood of `M` (C4). Let `Omega = tr(P dP ∧ dP)`.
(i) `dOmega = tr(dP ∧ dP ∧ dP)`. From `P^2 = P`: `P dP P = 0` and `(1 - P) dP (1 - P) = 0` (differentiate `P^2 = P` to get `dP = dP P + P dP`, then multiply on both sides by `P`, or by `1 - P`). So `dP` maps `ran P` into `ker P` and `ker P` into `ran P`. A product of three such maps again exchanges the two subspaces, so its diagonal blocks vanish and its trace is zero. Hence `dOmega = 0` on `M`.
(ii) Stokes's theorem on `M`: `0 = ∫_M dOmega = ∫_{∂M} Omega`. The boundary orientation of `M` on `∂B_j` is opposite to the boundary orientation of `B_j`. So `sum_j c_j = -(i/2pi) ∫_{∂M} Omega = 0`.
(iii) Charge blocks. Each block is a `C^1` map into a smaller unitary group, and its sea projection is the block of `P`. Apply (i)-(ii) to each block. ∎

Integrality of the `c_j` is not used in the proof. It is the standard integrality of first Chern numbers of projector families on the sphere (credited), and it is used only to read `c_j` as a count.

**Lemma F3a (how Weyl nodes enter).** Let `B_j` be a small ball around one linear Weyl node `k_0` of chirality `chi` at the cut `a` (C6). Take `B_j` so small that `B_j` meets no other point of `N_0 ∪ N_pi`, and the two eigenvalues near `e^{-ia}` stay separated from the rest of the spectrum on `B_j`. Then `c_j = chi` if `a = 0`, and `c_j = -chi` if `a = pi`.

*Proof.* On `B_j` let `Pi(k)` be the Riesz projection onto the two eigenvalues near `e^{-ia}`. It is `C^1` on all of `B_j`, so its Chern number on `∂B_j` is zero (Stokes on the ball, with (i) of the proof above). Let `Q(k)` be the projection onto the filled eigenvalues outside the pair. It is also `C^1` on the ball, so its Chern number is zero. On `∂B_j`, `P = Q + P_f`, where `P_f` is the filled part of the pair. Chern numbers add over orthogonal sums of projector families (standard; credited). Write the pair's quasi-energies as `w = a + e`, with `e` an eigenvalue of the local Hamiltonian `h` (C6). If `a = 0`, the filled member (quasi-energy in `(-pi, 0)`) is `e < 0`, the lower band of `h`, so `c_j = chi`. If `a = pi`, the filled member has `w` just above `pi`, i.e. just above `-pi` after reduction to `(-pi, pi]`, which is `e > 0`, the upper band of `h`. The two bands add up to `Pi`, whose Chern number is zero, so the upper band has Chern number `-chi`. ∎

**Corollary F3b.** If the cut-`0` and cut-`pi` points are all linear Weyl nodes, then
`chi_net(0) = chi_net(pi)`,
where each side is the sum of the chiralities of the nodes at that cut. If in addition `pi` is in a gap (PS-7r), then `chi_net(0) = 0`: Nielsen-Ninomiya for the PS-7r sea.

*Proof.* Theorem F3 and Lemma F3a: `chi_net(0) - chi_net(pi) = sum_j c_j = 0`. ∎

So a cut-`pi` node of the same chirality as a cut-`0` node is, for the sea, a light partner of the opposite sign: the filling near it is inverted. This is the precise form of the observation in #10070/#10072 that the `pi` sector is "a light charged inverted copy" (title of #10072).

### 3.4 The one-dimensional form

**Theorem F3' (1+1D).** Let `U : T^1 -> U(n)` be continuous. Suppose `N_0 ∪ N_pi` is a finite set `{k_1, ..., k_m}`. Let `c_j = rank P(k_j + 0) - rank P(k_j - 0)` (the jump of the number of filled bands as `k` crosses `k_j` upward). Then `sum_j c_j = 0`, in each charge block.

*Proof.* `rank P` is constant on each arc of `T^1 \ {k_j}` (a continuous family of projections has locally constant rank). Going once around the circle, the jumps add up to zero. ∎

*Reading.* At the cut `0`, a band whose quasi-energy increases with `k` through `0` leaves the filled arc, so `c = -1`. A band that decreases through `0` gives `c = +1`. At the cut `pi` the signs reverse. The one-band chiral shift `U(k) = e^{ik}` has `w = -k`. It crosses `0` downward (`c = +1`) and `pi` downward (`c = -1`), and the sum is `0`. The shift has a nonzero GNVW index, and its light content in the sea sense is still vector-like.

### 3.5 What `W3` measures

**Theorem F4 (`W3` counts the chirality at either cut).** Let `U : T^3 -> U(n)` be `C^3`. Let the cut `a` have finitely many points, all linear Weyl nodes, with chiralities `chi_1, ..., chi_m`. Then `W3(U) = sigma sum_j chi_j`, where `sigma` is `+1` or `-1`, depends only on the orientation conventions, and is the same for every `U` and every `a`.

*Proof.* Step 1 (cut out the nodes). Let `X_eps = T^3 \ ∪_j B_eps(k_j)`. On a neighbourhood of `X_eps`, `e^{-ia}` is not an eigenvalue, so `H(k) = i Log_a U(k)` is `C^3` there, with eigenvalues in `(a, a + 2pi)` (the branch of Theorem F2). Let `F(k, s) = exp(-i s H(k))` on `X_eps x [0,1]`. `F^* omega` is closed (C8 (i)). Stokes's theorem on `X_eps x [0,1]` gives
`∫_{X_eps} U^* omega - ∫_{X_eps} 1^* omega = ± sum_j ∫_{S_j x [0,1]} F^* omega`,
with `S_j = ∂B_eps(k_j)` and one sign fixed by orientations. The second term on the left is zero. As `eps -> 0`, the left side tends to `W3(U)`, because `U^* omega` is bounded and the removed balls have volume `O(eps^3)`. So `W3(U) = ± lim_{eps -> 0} sum_j nu_j(eps)`, with `nu_j(eps) = ∫_{S_j x [0,1]} F^* omega`.
Step 2 (the local limit). Fix `j` and write `k = k_j + eps n`, `n` in `S^2`. Let `Pi(k)` be the rank-two Riesz projection onto the eigenvalues near `e^{-ia}`, and `Pi^perp = 1 - Pi`; both are `C^3` on the ball. On the range of `Pi^perp`, `H` is `C^3` on the whole ball, so as a function of `(n, s)` it converges in `C^1` to the constant `H(k_j)` restricted there. On the range of `Pi`, `e^{ia} U = 1 - i eps ((Mn).sigma + t(n)) + O(eps^2)` in a `C^3` frame. Because `det M != 0`, `|Mn|` is bounded below on `S^2`. So the two eigenvalues are `a + eps(t(n) +- |Mn|) + O(eps^2)`, and their eigenprojections `P_+-(k_j + eps n)` converge in `C^1(S^2)` to the projections `P_+-(n)` of `(Mn).sigma`. With the branch of Step 1, the upper eigenvalue gives `H = a + O(eps)`, and the lower one gives `H = a + 2pi - O(eps)`. So `F(k_j + eps n, s)` converges in `C^1(S^2 x [0,1])` to
`F_0(n, s) = e^{-isa} [ (1 + (e^{-2 pi i s} - 1) P_-(n)) ⊕ e^{-is(H_perp - a)} ]`,
where `H_perp` is a constant matrix. Since the forms are continuous in the `C^1` topology of maps, `nu_j(eps) -> ∫ F_0^* omega`.
Step 3 (evaluate). By C8 (ii) the phase `e^{-isa}` drops out. By C8 (iii) the second block contributes nothing (it depends on `s` only, and its values commute), and `omega` adds over the blocks. On the first block, with `P_-(n) = (1 - m(n).sigma)/2` and `m(n) = Mn/|Mn|`,
`1 + (e^{-2 pi i s} - 1) P_- = e^{-i pi s} (cos(pi s) + i sin(pi s) m(n).sigma)`.
After the phase is dropped, the map `(n, s) -> cos(pi s) + i sin(pi s) m(n).sigma` sends `S^2 x {0}` to `1` and `S^2 x {1}` to `-1`. It is the suspension of `m : S^2 -> S^2`, a map from `S^3` to `SU(2) = S^3` of degree `+- deg(m)`. `deg(m) = sign det M`, the degree of a linear isomorphism normalised to the sphere. The normalised integral of `omega` over a map `S^3 -> SU(2)` is its degree, up to one convention sign. And `chi = +- sign det M` (C6), with one convention sign. So `lim nu_j = sigma' chi_j`, with `sigma'` built from these fixed conventions only.
Step 4. Summing over `j` gives `W3(U) = sigma sum_j chi_j` with a universal `sigma`. ∎

*The value of `sigma`.* Nothing below uses it. [check] For #9863's quasi-local walk `U = (n_0 - i n.sigma)/|(n_0, n)|` with `n_0 = m + sum_i cos k_i` and `n = sin k`: on a `32^3` grid, `W3 = -0.993` at `m = -2` and `m = 2`, and `1.978` at `m = 0.5`. At `m = -2` there is one node at the cut `0` (at `k = 0`) and seven at `pi`, as #9863 states. The chiralities read off from the linearisation match `chi_net(0) = chi_net(pi) = -W3` in #9863's convention ("chirality sign det M, where U(k0 + q) = s(1 - i sum M_ij q_j sigma_i + O(q^2))"), which agrees with Corollary F3b.

*Combining F3b and F4.* `chi_net(0) = chi_net(pi) = sigma W3`. A free update can have an unpaired Weyl node at the cut `0` only if `W3 != 0`. Then (F2b) no cut is in a gap, the node's partners sit at `pi` with the same chirality, and by Lemma F3a they enter the sea with the opposite sign. The light content is vector-like either way.

### 3.6 Answers to leads 1 and 2

**Lead 1, closed.** The lead asked for a proof that "every finite-depth circuit of nearest-neighbour one-body (number-conserving, quasi-free) gates on Z^3 has W3 = 0 for its Bloch unitary, hence zero net Weyl chirality". Theorem F1 proves `W3 = 0` for every such circuit, with any gate range and any number of modes per site. Corollary F3b gives zero net chirality at the cut `0` whenever `pi` is in a gap. But "hence" is not the right logic. Zero net chirality of the light content (Theorem F3) holds for every free update, with or without `W3 = 0`. What `W3 = 0` adds is that the cut-`0` content alone is balanced, without help from the cut `pi`.

**Lead 2, closed for free updates.**
- *QCAs that are not circuits.* The 1D chiral shift is a QCA with nonzero GNVW index (Gross, Nesme, Vogts and Werner; for fermions, Fidkowski, Po, Potter and Vishwanath) and `W1 = 1`. Theorem F3' shows that its light content is still vector-like in the sea sense (3.4).
- *Strictly finite-range QCAs in 3D.* A finite-range translation-covariant one-body unitary has Laurent-polynomial entries and a monomial determinant (LW1 Theorem B2's units lemma, applied to `det U`). By the vanishing of `SK1` of `C[Z^3]` (the K-theory of Laurent polynomial rings over a field: Bass-Heller-Swan and Suslin; credited, not rebuilt, and not used below), such a unitary is stably a product of elementary matrices and a monomial diagonal, hence has `W3 = 0`. This is #9863's cited input. Theorem F1 does not need it, because PS-1 asks for circuits.
- *Quasi-local (exponentially local) walks.* `W3 != 0` occurs: #9863's walk has "an exponential tail", and Higashikawa, Nakagawa and Ueda realise "a single Weyl fermion" with a Floquet unitary "with nontrivial topology". Owner memory allows "exponentially local rules". But Corollary F2b says such a walk has no gap at any quasi-energy, so it has no PS-7r sea (Corollary F2a). And for any sea filled between the cuts `0` and `pi`, Theorem F3 makes the light content vector-like. Sun, Xiao, Bzdusek, Zhang and Fan state the same conclusion for Floquet lattices: "the Nielsen-Ninomiya no-go theorem still holds on Floquet lattice". Their one-handed bands live in a low-energy sub-block in the adiabatic limit, and the partners sit in the other sub-block.
- *Gauging such a walk with an exact local Gauss law.* For c-number (rotor eigenvalue) link fields this is possible: if `N` is a finite-range covariant operator with `U = N (N^* N)^{-1/2}`, then `U[A] = N[A] (N[A]^* N[A])^{-1/2}` is unitary and gauge covariant wherever `N[A]^* N[A]` is invertible, and quasi-local under a gap bound (the Hernandez-Jansen-Luscher mechanism for the overlap; credited). This is not pursued: by Theorem F3 the free light content is vector-like before gauging, so gauging cannot make it chiral.
- *Consequence for PS-1.* Widening PS-1 from "finitely many layers of nearest-neighbour gates" to QCAs or quasi-local unitaries changes `W3` but not the light content of any free sea. So CH1 gives no reason to widen PS-1. A proposed widening would add structure that its own reasons do not need, which is smuggle test 4. None is proposed (section 10).

---
## 4. Rung S: the gauge charges the chosen carrier allows

Section 3 needs interactions for any chiral light sector. Before testing PS-8, this section fixes what the chosen carrier allows as light charges at all, whatever the dynamics.

### 4.1 Charge parity

**Lemma S1 (charge parity on one-mode sites).** Work in the fermion reading (C1), under PS-6 and PS-6r, with the gauge group `G = U(1)` acting on site `x` by `c_x -> e^{-i q_x theta} c_x` for integers `q_x` (LW1 Lemma B3: the number-conserving frame group of a one-mode site is `U(1)`, and its continuous homomorphisms to `U(1)` are `theta -> q theta`). Suppose the law, with its Gauss laws, is covariant under a group that acts transitively on sites (PS-1c). Then:
(i) `|q_x| = q` is the same for all sites;
(ii) every even or odd local operator of definite gauge charge `Q_O` (that is, `[sum_x q_x n_x, O] = Q_O O`) has `Q_O = q` times an integer of the same parity as the fermion parity of `O`.
So every fermionic excitation of any state has charge an odd multiple of `q`, and every bosonic excitation an even multiple.

*Proof.* (i) The Gauss operator at `x` is `G_x = q_x n_x + (div E)_x` (LW1 Theorem B4 with charge `q_x`). A symmetry `g` of the law maps the set of Gauss operators to itself (it maps gauge transformations to gauge transformations), and `n_{gx}` to `n_{gx}` or to `1 - n_{gx}` (the two automorphisms of LW1 Lemma B3 that act on the number operator). So `q_{gx} = +-q_x`. Transitivity gives (i). (ii) Write `O` as a finite sum of monomials in the `c_x` and `c_x^dag` (times link operators, which carry no fermion parity and do not change `sum q_x n_x`). A monomial with `f` mode factors changes `sum_x q_x n_x` by a sum of `f` terms, each `+q` or `-q`. That sum is `q` times an integer with the parity of `f`. If `O` has definite charge, every monomial in it has that charge. Fermion parity of the monomial is `(-1)^f`. ∎

*Normalise `q = 1`.* Then fermion parity equals `(-1)^(charge)` on every local excitation.

**Corollary S1a (3-4-5-0 is excluded).** The 1+1D 3-4-5-0 model (left-movers of charges 3 and 4, right-movers of charges 5 and 0) cannot be the light content of any update on one-mode sites under PS-6 and a site-transitive covariance group, either as elementary fields or as composites: it contains fermions of charges 4 and 0. This agrees with #9927's spectral obstruction ("One-mode free sites carry no exact 3450 charge"), which is a different statement (about the 3450 combination as a symmetry of a free chain). Lemma S1 is about the gauge charges of excitations, and it holds for every dynamics.

### 4.2 Which Standard Model charges the exact `U(1)` can carry

**Theorem S2.** On one family with `nu^c`, in left-handed Weyl fields `Q_L, u^c, d^c, L, e^c, nu^c`, let a `U(1)` act as `X = aY + b(B - L)`, with `Y` normalised so that `Y(Q_L) = 1/6`. Suppose `X` acts as the gauge `U(1)` of Lemma S1 with elementary charge `q`. Then every `X` charge is an odd multiple of `q`. This holds if and only if `a = 2 alpha q` and `b = beta q` with `alpha` an even integer, `beta` an odd integer and `alpha + beta = 0 (mod 3)`.

*Proof.* The charges are `X(Q_L) = q(alpha + beta)/3`, `X(u^c) = -q(4 alpha + beta)/3`, `X(d^c) = q(2 alpha - beta)/3`, `X(L) = -q(alpha + beta)`, `X(e^c) = q(2 alpha + beta)` and `X(nu^c) = q beta`, with `alpha = a/(2q)` and `beta = b/q`. Necessity: `nu^c` makes `beta` an odd integer. `e^c` makes `2 alpha + beta` an odd integer, so `2 alpha` is an even integer and `alpha` is an integer. `L` makes `alpha + beta` odd, so `alpha` is even. `Q_L` makes `(alpha + beta)/3` an integer, so `3` divides `alpha + beta`. Sufficiency: `alpha + beta` is odd and divisible by 3, so `(alpha + beta)/3` is odd. `2 alpha - beta = 3 alpha - (alpha + beta)` and `4 alpha + beta = 3 alpha + (alpha + beta)` are divisible by 3 and odd, so their thirds are odd. `alpha + beta`, `2 alpha + beta` and `beta` are odd. ∎

[check] The four cases below were evaluated numerically, with `sum X` and `sum X^3` over the family both zero.

**Consequences.**
- *Hypercharge is excluded.* `b = 0` means `beta = 0`, which is not odd. Directly: `Y(u^c)/Y(Q_L) = -4`, which is not a ratio of two odd integers. Without `nu^c`, the only anomaly-free combination in this span is `Y`, which is excluded the same way.
- *Electric charge is excluded.* `Q(u)/Q(d) = -2`. Also, the neutron and the neutrinos are neutral fermions, and Lemma S1 makes every neutral excitation a boson. **On `L_cube` every neutral excitation is a boson.**
- *Allowed:* `B - L` (`alpha = 0`, `beta = 3`; charges `(1, -1, -1, -3, 3, 3)` in units of `q`). It is vector-like as a `U(1)` by itself: the multiset of charges is symmetric under sign change. Also allowed: the `SO(10)` charge `X_10 = 5(B - L) - 4Y` (`alpha = -2`, `beta = 5`; charges `+1` on the 10, `-3` on the 5bar, `+5` on the singlet). It is chiral and anomaly-free (`sum X = 10 - 15 + 5 = 0`, `sum X^3 = 10 - 135 + 125 = 0`). Also allowed: `4Y + (B - L)` (`alpha = 2`, `beta = 1`; charges `(1, -3, 1, -3, 5, 1)`).

**What S2 does and does not say.** It says the exact gauge `U(1)` of `L_cube` (LW1 B4, B5) cannot itself be hypercharge or electric charge. It does not exclude a hypercharge that is a combination of that `U(1)` and a `U(1)` that emerges at long distance, and it says nothing about non-abelian factors. It bears on CG1-i (P-HY) and GA1-i: under `L_cube`, the exact `U(1)` can be at most of `B - L` or `X_10` type.

### 4.3 CH1 (a) on the chosen law

**Theorem S3 (what CH1 (a) needs on `L_cube`).** On `L_cube`, with `G` the exact gauge group:
(i) `G = U(1)` for one-body frame actions (LW1 Theorem B5);
(ii) the light content of CG1 ("one Weyl 16, or the Standard Model multiplet") cannot carry its non-abelian charges under `G` (by (i)), and cannot carry its hypercharges under `G` (Theorem S2);
(iii) hence CH1 (a), read with `G` the exact gauge group of `L_cube`, fails. It can hold only if `G` is enlarged (PS-5's fallback, or several modes per site in a form PS-6 accepts) or if the non-abelian factors and hypercharge emerge at long distance. Neither is supplied by `L_cube`.

*Proof.* (i) and (ii) are restatements. (iii) CH1 (a) asks for a theory "invariant under `G`, whose light spectrum ... is exactly the chiral content of CG1". With `G = U(1)`, the only exact quantum number besides the space-time labels is the `U(1)` charge, and (ii) excludes the Standard Model charge assignment for it. ∎

*For PS-5.* PS-5 reads: "Build site content on cells of qubits. The five-mode fallback is used only if the cell route fails at a named step." Theorem S3 names a step: LW1 B5 (abelian one-body frames on cells of one-mode sites) together with S2 (that abelian group cannot be hypercharge). B5's scope note keeps open "Many-body unitaries on a cell's Fock space can have non-abelian commutants", which #9882 says "are not minimal-coupling gauge groups". So whether the cell route has failed is an owner decision under PS-5; this draft does not make it.

### 4.4 The `U(1)` problem that remains on `L_cube`

What CH1 can still ask on `L_cube` is a chiral, anomaly-free light sector for the one gauge `U(1)`, with every fermion of odd charge (Lemma S1). Such sets exist.

- *1+1D.* Anomaly-free means `sum_L q^2 = sum_R q^2` and equal numbers of left- and right-movers. [check] Among sets with two movers on each side and `|q| <= 9`, the only odd-charge one that is not vector-like is L: `(1, 7)`, R: `(5, 5)` (`1 + 49 = 25 + 25`). For its mirror-doubled version (Dirac fields of charges 1, 7, 5, 5, mirror L: `(5,5)`, R: `(1,7)`), the null-vector condition of the symmetric-gapping criterion (Haldane; used by Wang and Wen for 3-4-5-0) has primitive mutually null charge-neutral solutions. [check] `l_1 = (0, 5, 3, 4)` and `l_2 = (1, -3, -1, -3)` in the basis `(1, 7 | 5, 5)` with `K = diag(1, 1, -1, -1)`: `l.K.l = 0` for both, `l_1.K.l_2 = 0`, both are charge neutral, and the `2 x 2` minors have gcd 1. These are guidance for a construction, not a gapping proof.
- *3+1D.* Anomaly-free means `sum q = sum q^3 = 0` over left-handed Weyl fields. [check] With odd charges and `|q| <= 9`, no non-vector-like set has 7 or fewer fields; with 8 fields there are two, `(-9, -3, -3, -3, -1, 5, 7, 7)` and its negative. The 16 with its `X_10` charges (`+1` ten times, `-3` five times, `+5` once) is a 16-field example.

On one-mode sites, charges other than `+-1` can only be bound states of several elementary fermions (Lemma S1 fixes `q = 1`). Section 6 asks whether the law can fix them by layout (Lemma C3: it cannot), and section 7 states the bound-state question.

---
## 5. The kill test: does PS-8 release light partners on the chosen carrier?

### 5.1 The elementary light content of `L_cube`

At `mu = 0` the one-body tick has `w = 0` only at `K = 0`, where all eight cell states are degenerate (LW1 B10 (i)-(ii): `cos w = A S(K) - B`, and at `K = 0` this is `A - B = cos mu = 1`). LW1 7.2, from #10016: "the four tastes are E + E of O (one E per chirality)". So the light content is two left-handed and two right-handed Weyl fields, all of gauge charge 1 (LW1 B4; Lemma S1), with net chirality 0, as Theorem F1 with Corollary F3b requires. At `mu > 0` there is no light content (`|w| >= mu`).

PS-8 asks to gap "the block's mirror modes" (one chirality, here the right-handed `E`) symmetrically and keep the other.

### 5.2 The endpoint theorem

**Theorem K1 (quasi-free endpoints release partners).** Let the cell dynamics have `n` one-body modes per cell, covariant under `Lambda`. Let `P_m(k)` be any `C^1` projector field on `T^3` (the *mirror*; for a block-local mirror, `P_m` is constant in the cell basis) and `P_l = 1 - P_m`. Suppose that at the endpoint the light modes move under a `C^1`, `Lambda`-covariant one-body generator on `ran P_l`: either (Hamiltonian reading) a Hermitian `H_l(k)` with `H_l = P_l H_l P_l`, or (Floquet reading) a unitary `U_l(k)` on `ran P_l` with `pi` in its gap. Then the light pockets at zero energy (or at the cut `0`) have pocket charges summing to zero in each charge sector. In particular, on `L_cube` (one charge sector), if the light sector keeps Weyl nodes of net chirality `chi != 0` at `K = 0`, it has further light nodes or pockets of total charge `-chi` elsewhere.

*Proof.* Hamiltonian reading: let `H~(k) = H_l(k) + c P_m(k)` with `c > 0` larger than `sup ||H_l||`. `H~` is `C^1` and Hermitian on `C^n`, its zero-energy set is that of `H_l` on `ran P_l`, and the mirror directions are at positive energy, so they are empty. The filled projection `1_{(-inf, 0)}(H~(k))` is `C^1` off the zero-energy set (Riesz projection on a contour crossing the real axis only at `0` and below `-c`). The proof of Theorem F3 with one cut gives `sum_j c_j = 0`. Floquet reading: let `U~ = U_l ⊕ e^{-i pi/2} P_m`. The mirror directions sit at quasi-energy `pi/2`, which is empty and away from both cuts. `pi` is in the gap of `U~`. Theorem F3 and Corollary F3b apply. On `L_cube` all modes have charge 1 (Lemma S1), so there is one sector. ∎

*Scope.* K1 covers every cell-local or `C^1` choice of mirror, and every endpoint at which the light sector is quasi-free. It does not depend on the form of the mirror interaction or on its symmetry group. This is #9911's endpoint argument ("Any endpoint that freezes local light combinations leaves a finite-range free Hamiltonian, whose nodes have net chirality zero per sector by Nielsen-Ninomiya") made general: any `C^1` light generator (so any locality), either reading. It also explains #9992's finding that "the symmetric mirror gap releases every light mode the mirror was pairing": the light copy's own band must be vector-like at the endpoint.

*On "a coupling large against the hop" in a Floquet law.* In a unitary circuit a coupling enters as an angle modulo `2pi`, so "large" has meaning only in the Hamiltonian reading: step angle `eps` small, interaction angle `g eps` with `g >> 1` and `g eps << pi`. Then the tick is close to `exp(-i eps (H_hop + g H_mirror))` and the Hamiltonian reading of K1 is the relevant one.

### 5.3 Away from the endpoints: the anomaly

**Lemma K2 (anomaly arithmetic on `L_cube`).** Every set of light Weyl fields drawn from the elementary content of 5.1 with net chirality `chi != 0` has `U(1)^3` coefficient `sum chi_i q_i^3 = chi` and mixed gravitational coefficient `sum chi_i q_i = chi`, both nonzero. *Proof.* All `q_i = 1`. ∎

So keeping the two left-handed fields light and gapping the two right-handed ones leaves an anomalous set (coefficients `2` and `2`). By 't Hooft anomaly matching, an exact on-site `U(1)` (here gauged, with exact Gauss laws, LW1 B4) cannot have that set as its whole light content.

**Lemma AM (anomaly matching for gauge-covariant updates; not proved here).** Let `U` satisfy PS-1, PS-1c, PS-6 and PS-6r on one-mode sites (`q = 1`). Let `omega` be a stationary state invariant under `G_U` and under gauge transformations. Suppose (hypothesis IR) there are quasi-local fermion-odd operators `psi_i` of charges `q_i` such that the correlations of `omega` at large separations agree with those of free Weyl fields of chiralities `chi_i`, and all other connected correlations decay exponentially. Then `sum chi_i q_i^3 = 0` and `sum chi_i q_i = 0` (in 1+1D, `sum chi_i q_i^2 = 0` and `sum chi_i = 0`).

*Status.* For quasi-free `U` and quasi-free `omega` it is Theorem F3 with Lemma F3a, at any locality. For interacting `U` it is the standard principle, and it is not proved here. The usual proof is flux insertion. Two of its three steps are exact on the lattice. (a) With background link phases twisted by `theta` around a torus cycle, `U[theta + 2pi] = W U[theta] W^*`, with `W` the large gauge transformation (LW1 B4's covariance, applied to c-number links). (b) The total charge is exactly conserved. (c) As `theta` goes from `0` to `2pi`, `omega` follows the flux, and the charge it gains equals the infrared spectral flow, `sum chi q^2` per unit of flux in 1+1D (the 3+1D case reduces to this in a background magnetic field). Step (c) fails as a lattice theorem. Many-body Floquet operators have no general adiabatic theorem: the quasi-energy spectrum of a large system is dense modulo `2pi`. And hypothesis IR speaks of correlations, not of spectral flow. Golterman and Shamir (arXiv:2505.20436) give conditions on "a one-particle lattice Hamiltonian" under which "the massless fermion spectrum must be vector-like, regardless of interaction strength". Their conditions are not checked here for `L_cube`.

Lemma AM is not CH1's first open statement. The kill test does not need it at the endpoints (K1), and every route in section 7 already has an anomaly-free target.

### 5.4 Verdict of the kill test

On the chosen carrier, PS-8 as worded aims at an anomalous light set (K2). At every quasi-free endpoint the aim fails, and partners of the opposite net chirality are released (K1, proved). In the interacting regime the aim is excluded by anomaly matching (Lemma AM, a standard principle not proved here). Golterman and Shamir's conjecture, "SMG interactions produce bound states of opposite chirality", is the interacting form of the same release. So the skeleton's kill test is answered: **PS-8, applied to the elementary content of `L_cube`, releases light partners.** On `L_cube` it cannot deliver CH1.

What would change this verdict, by name:
- light content that is anomaly-free by itself, with odd charges other than `+-1` (section 4.4). On one-mode sites these are bound states (sections 6 and 7);
- more modes per site with a non-abelian frame group (PS-5's fallback), on which a 16 of `Spin(10)` and its mirror are the classic SMG candidate. That is a different carrier, and #10027 records that "every parity-odd excitation is vector class, never the 16" for site-bilinear `Spin(10)` on five-mode sites.

---
## 6. Rung 1+1D: what holds, exactly

### 6.1 The carrier

The 1D analogue of `L_cube`: one fermion mode per site of `Z`. The even tiling is `{2j, 2j + 1}` and the odd tiling `{2j + 1, 2j + 2}`. One tick is `V = exp(+i beta R_o) exp(-i alpha R_e)`, with `R` the real hop inside each pair. There are `U(1)` quantum links on the edges (PS-6r) and exact Gauss laws as in LW1 B4. The covariance group is `G_1 = 2Z ⋊ Z_2`, where `Z_2` is the reflection `x -> 1 - x` about the centre of the cell `{0, 1}`. It maps each tiling to itself and fixes the real hops, and it acts transitively on sites with trivial site stabilisers (the 1D form of PS-1c).

### 6.2 What holds

1. *Free:* every free update has vector-like light content in the sea sense, at any locality (Theorem F3'). The chiral shift is no exception (3.4).
2. *Charges:* every fermionic excitation has odd charge (Lemma S1, with transitivity from `G_1`). 3-4-5-0 is excluded (Corollary S1a).
3. *Elementary content:* the light content of the free walk is one Dirac field of charge 1 (its two light branches have opposite `c`, Theorem F3'). Gapping one branch leaves `sum chi q^2 = +-1`, which is anomalous. So K1 and K2 apply verbatim: PS-8 on the elementary content releases the partner. The 1+1D chain of #9911 shows the same: "The p = pi doubler is released as a left-mover".
4. *Anomaly-free odd targets exist:* L: `(1, 7)`, R: `(5, 5)`, with gapping null vectors on file [check] (section 4.4).
5. *Rotor constructions are exact but leave the axioms' site content.* #9927: "With non-slipping rotor matter (an angle per site and a winding integer per link), the rederived Thorngren-Preskill-Fidkowski disentangler ... maps the 3450 symmetry exactly onto an on-site ancilla symmetry", and "With Z_5 clocks only Z_5 is exact". The source paper, as fetched, has "infinite-dimensional rotor degrees of freedom". The Qubit axiom gives each site `M_2(C)`, and PS-6r makes each link register "a finite-dimensional register". So rotor matter is outside the working set. Section 7 (Attack 3) makes this precise.

### 6.3 Cluster modes: odd charges inside an invariant subspace

**Lemma C2 (cluster modes).** Let `S = {x_1 < ... < x_s}` be a finite set of sites with `s` odd, and `C_S = c_{x_1} c_{x_2} ... c_{x_s}`. Then:
(i) `C_S^2 = 0`, `C_S^* C_S = prod_{x in S} n_x` (the set `S` is full) and `C_S C_S^* = prod_{x in S}(1 - n_x)` (the set `S` is empty). So `C_S C_S^* + C_S^* C_S = Pi_S`, the projection onto "`S` empty or full".
(ii) For disjoint odd sets `S, S'`: `C_S C_{S'} = -C_{S'} C_S` and `C_S C_{S'}^* = -C_{S'}^* C_S`.
(iii) `[sum_x n_x, C_S] = -s C_S`: `C_S` has charge `-s`.
(iv) Fix a family `𝒞` of disjoint odd sets (a *layout*) and let `H_𝒞` be the range of `prod_{S in 𝒞} Pi_S`. Each `C_S`, `S` in `𝒞`, maps `H_𝒞` into itself, and on `H_𝒞` the `C_S` satisfy the canonical anticommutation relations. So they are fermion modes of charges `s`.
(v) For `S, S'` in `𝒞` with `|S| = |S'| = s`, a bijection `b : S -> S'` and edge paths `gamma_x` from `x` to `b(x)`, let `O = C_{S'}^* Y C_S` with `Y = prod_{x in S} U(gamma_x)` (the ordered product of link raising operators along `gamma_x`, oriented from `x` to `b(x)`). Then `O` commutes with every Gauss operator. The gate `exp(-i tau (O + O^*))` maps `H_𝒞 ⊗ (links)` into itself.

*Proof.* (i) In `C_S C_S` each `c_x` occurs twice; moving the second copy next to the first gives a sign times `c_x^2 = 0`. For `C_S^* C_S = c_{x_s}^* ... c_{x_1}^* c_{x_1} ... c_{x_s}`, the middle pair is `n_{x_1}`, which is even and commutes with `c_{x_2}` and `c_{x_2}^*`, so the next pair gives `n_{x_1} n_{x_2}`, and so on. `C_S C_S^*` is the same computation with `c c^* = 1 - n`. (ii) Moving a product of `s` mode operators past a product of `s'` mode operators on disjoint sites gives the sign `(-1)^{s s'} = -1`. (iii) Each `c_x` lowers `sum n` by one. (iv) `C_S` commutes with `Pi_{S'}` for `S' != S`, because `Pi_{S'}` is a polynomial in the `n_y`, `y` in `S'`, which are even and act on other sites. On `ran Pi_S`, `C_S` maps "full" to "empty" and annihilates "empty", so it maps `ran Pi_S` into itself. Then (i) and (ii) restricted to `H_𝒞` are the CAR. (v) Under a gauge transformation, `C_S` gains `e^{-i sum_{x in S} theta_x}`, `C_{S'}^*` gains `e^{+i sum_{y in S'} theta_y}`, and `U(gamma_x)` gains `e^{i(theta_x - theta_{b(x)})}` (LW1 B4's computation, edge by edge). The product is invariant. `O` commutes with `Pi_{S''}` for `S''` other than `S, S'`. On `ran Pi_S Pi_{S'}` it maps (`S` full, `S'` empty) to (`S` empty, `S'` full) and annihilates the other three cases. So `O`, `O^*` and the gate keep `H_𝒞 ⊗ (links)`. ∎

*What C2 gives.* Every free walk of odd-charge modes on a layout embeds exactly in the update of one-mode sites, inside the invariant subspace `H_𝒞`, with exact Gauss laws. With PS-6r quantum links of spin `S_link`, a raising operator on a link at the top of its range gives zero. So gates that cross the same link several times need `S_link` large enough, or they are truncated (they remain gauge invariant). The cluster gates are local but act on `2s` sites. Their factorisation into nearest-neighbour gates uses the credited universality step of LW1 5.3.

### 6.4 The law cannot fix an odd layout

**Lemma C3 (no law-fixed odd clusters).** (3D) Let `G_U = 2Z^3 ⋊ O_{c_0}` be the covariance group of `L_cube` (LW1 A2). Let `𝒫` be a partition of `Z^3` into finite sets of one size `s` that `G_U` maps to itself. If `s` is odd, then `s = 1`. (1D) The same holds for `G_1 = 2Z ⋊ Z_2`.

*Proof.* (3D) `G_U` is transitive on sites (LW1 A2a). So it is transitive on `𝒫`: for `S, S'` in `𝒫`, pick `x` in `S`, `y` in `S'` and `g` with `g x = y`; then `gS` is the member of `𝒫` that contains `y`, which is `S'`. Let `H` be the setwise stabiliser of a member `S`. `H` meets `2Z^3` only in `0`, because a nonzero translation fixes no finite set. So the quotient map `G_U -> G_U / 2Z^3 = O` (order 24) is injective on `H`, and `|H|` divides 24. Next, `2Z^3` acts freely on `𝒫`. Each `2Z^3`-orbit of members covers a translation-invariant set of sites with `s` sites per cell of 8 sites, so there are `8/s` orbits. `O` acts transitively on these orbits. The stabiliser of the orbit of `S` is the image of `{g : gS = S + t, t in 2Z^3} = 2Z^3 H`, which is a copy of `H`. By orbit-stabiliser, `8/s = 24/|H|`, so `|H| = 3s`. Since `|H|` divides 24, `s` divides 8, and an odd `s` is 1. (1D) The same count with 2 sites per cell and `|G_1 / 2Z| = 2` gives `2/s = 2/|H|` with `|H|` dividing 2, so `s` is 1 or 2. ∎

*Reading.* Lemma C3 allows even cluster sizes (2, 4, 8), whose modes are bosons. A layout of odd clusters of size above 1 must break the covariance of PS-1c (as CL-1's "role layout ... departs from no site is privileged" did, per LW1 3.1), or must be carried by the state. The PS-7r sea is invariant under `G_U` (LW1 B10 (iv)), so it carries no layout either. Odd charges above 1 can therefore come only from bound states in an invariant vacuum. Section 7 states that question.

### 6.5 The 2+1D rung

The skeleton's ladder lists 2+1D between the 1+1D rotors and the 3+1D wall. In 2+1D there is no chiral gauge anomaly of the 3+1D kind. The 2+1D objects on file are slabs and domain walls that carry 1+1D chiral modes (#9971, #10056, #10064). Every theorem of sections 3-5 is already proved in 3+1D, and the open statement of section 7 is a 1+1D statement with a direct 3+1D lift. By the worth-doing test, a 2+1D pass would move no named item, so it is not done here. It stays the natural home of a domain-wall version of Attack 2.

---
## 7. The first open statement

**Lemma CH1-C1 (open).** There exist
(a) an update `U` on the 1D carrier of 6.1 (one fermion mode per site, PS-6r quantum links of some finite spin, `U` a finite product of layers of gauge-invariant local gates, covariant under `G_1`), and
(b) a state `omega`, stationary under `U` and invariant under `G_1` and under gauge transformations,
such that hypothesis IR of Lemma AM holds with light fields of charges L: `(1, 7)`, R: `(5, 5)` and no other light excitations.

*Why this one.* It is the 1+1D form of what is left of CH1 on `L_cube` (sections 4.4 and 5.4): an anomaly-free chiral light sector of the one gauge `U(1)`, with odd charges, built from charge-1 sites. Its 3+1D lift, **CH1-C3**, is the same statement on `L_cube` with an anomaly-free odd 3+1D set (for example the 16 with its `X_10` charges `(+1)^10 (-3)^5 (+5)^1`, or the 8-field set of 4.4). Every attack below lifts to it word for word, with Lemma C3 in its 3D form.

### Attack 1: a free construction

Take `U` quasi-free in the matter at zero gauge coupling and `omega` a quasi-free sea. *Exact reason it fails:* by Theorem F3' the light content is vector-like in each charge sector, at any locality. By Lemma S1 all elementary charges are 1, so a quasi-free sea has no light field of charge 5 or 7 at all. Both failures are theorems.

### Attack 2: an odd layout of clusters, then symmetric mirror gapping

The plan. (1) Use Lemma C2 with a layout of clusters of sizes `1, 7, 5, 5` repeated with period 18. Cluster walks then give Dirac fields of charges `1, 7, 5, 5`, which is vector-like content and allowed by Theorem F3'. (2) Gap the mirror half (L: `(5, 5)`, R: `(1, 7)`) with the charge-neutral multi-fermion gates of the null vectors `l_1 = (0, 5, 3, 4)` and `l_2 = (1, -3, -1, -3)` (section 4.4). Each gate is gauge invariant by the dressing of Lemma C2 (v). The plan is the Wang-Wen route for 3-4-5-0, moved to clusters.
*Exact reasons it fails.*
(i) Step (1) breaks the covariance clause. By Lemma C3 no `G_1`-invariant layout of odd clusters larger than one site exists, so `U` is not covariant under `G_1`, which (a) requires. Relaxing the clause for this purpose would add a premise in order to obtain a target, which is smuggle tests 2 and 4. It is not proposed.
(ii) Even with the layout granted, step (2) is a strong-coupling statement with no proof. At the free point, the vertex operator of a null vector `l` has scaling dimension `(1/2) sum_i l_i^2` (unit-radius chiral bosons, `K = diag(1, 1, -1, -1)`). That is 25 for `l_1` and 10 for `l_2` (the search did not minimise), far above 2, so both terms are irrelevant there. A gapped symmetric phase needs a flow, driven by marginal forward-scattering terms, to a point where they become relevant. For 3-4-5-0 the literature makes this point (Tong, 2021, from memory), and the evidence for gapping is numerical (Zeng, Zhu, Wang and You, 2022, DMRG, from memory). #10076 on file reports a 3450 far-wall gap that falls with size ("persistence is not established"). No theorem gives the flow.

### Attack 3: a symmetry disentangler

The plan. Thorngren, Preskill and Fidkowski make a not-on-site chiral `U(1)` on-site with a constant-depth circuit, then gauge it by standard methods. They realise this "using lattice rotor models" for anomaly-free `U(1)` sets, with an exactly solvable 3450 Hamiltonian. Here one would build compact bosons of charges `(1, 7 | 5, 5)` the same way.
*Exact reason it fails.* The disentangler acts on "infinite-dimensional rotor degrees of freedom", whose integer variables (the "winding integer per link" of #9927) are shifted by charges. A shift `n -> n + q` is a bijection of `Z`, and it is not a bijection of any finite range `{-N, ..., N}`. So no finite truncation keeps the identity. #9927 states the result of truncating: "With Z_5 clocks only Z_5 is exact." The Qubit axiom gives each site `M_2(C)` and PS-6r makes each link register "a finite-dimensional register", so the infinite-dimensional variables are not available. A cell of qubits cannot host them either: the charge spectrum on a finite-dimensional space is bounded, so it cannot carry an unbounded integer variable with an exact shift. (The paper also states that its hypercharge step rests on a "plausible but unproven conjecture"; that concerns 3+1D, not this lemma.)

### What would settle CH1-C1

- *True:* a bound-state mechanism in a `G_1`-invariant vacuum that produces light charge-7 and charge-5 fermions and gaps the mirror, with a proof of IR. This is the template for CH1-C3, and so for the `U(1)` part of CH1 on `L_cube`.
- *False:* a theorem that, on one-mode sites with `q = 1` and site-transitive covariance, every light fermion of a stationary invariant state has charge `+-1`. That would be a strengthening of Lemma S1 from parity to value. It would move CH1 off `L_cube` and onto PS-5's fallback.
- *The easier test to run next* (guidance only, no proof weight): exact diagonalisation of a `G_1`-invariant 1D chain with strong on-site-cell attraction (clusters forming dynamically), to see whether light odd-charge composites appear at all, before any chirality question.

---

## 8. The 3+1D wall: what is proved, what lifts

- Proved in 3+1D: Theorems F1-F4 (free, any locality), Lemma S1, Theorem S2, Theorem S3, Lemma C2 (in any dimension), Lemma C3 (3D), Theorem K1, Lemma K2.
- The kill test (skeleton 7.3): answered in section 5.4.
- What lifts from 1+1D: CH1-C1 lifts to CH1-C3. All three attacks fail for the same reasons, with Lemma C3 in 3D.
- With PS-5's fallback (five modes per site), the 3+1D question becomes symmetric mass generation for the mirror 16bar of a `Spin(10)` 16. On file: #10004, "Survival of the K gap as L -> infinity is not established: inconclusive", and #10027 (via the skeleton) "every parity-odd excitation is vector class, never the 16". In the literature (from memory): Razamat and Tong exhibit 4D chiral theories that flow to gapped phases; Wang and Wen propose the `Spin(10)` mirror gapping; Golterman and Shamir (arXiv:2505.20436) set conditions under which the spectrum stays vector-like and conjecture that SMG produces bound states of opposite chirality. Nothing here proves or refutes it. This is outside `L_cube`, and the owner decides under PS-5 whether to open it.

## 9. CH1-ii and reflection positivity

- *The gauged measure.* Luscher (1999, from memory) constructs abelian chiral lattice gauge theories with exact gauge invariance in the Euclidean setting, for anomaly-free `U(1)` multiplets, using the overlap (Ginsparg-Wilson) operator, which is exponentially local for admissible fields. On `L_cube` the exact group is `U(1)`, so Luscher's theorem is the relevant comparison object for CH1-ii. But its elementary fields carry the multiplet's charges, while `L_cube`'s elementary fields all carry charge 1 (Lemma S1). So it is a target for the long-distance theory of CH1-C3, not a law on `L_cube`. #10049 records that "The 3+1 tick unitary U(K) itself is not such a V". #10085 concerns the one-family Wilson-kernel overlap density and "does not show that the one-family four-field coefficient is non-local".
- *Reflection positivity.* No source read here establishes reflection positivity for the chiral overlap measure (#10049 lists it under "Not covered"). For a unitary tick, LW1 7.3 notes that "a unitary `T >= 0` is the identity", so positivity is a long-distance statement (ZM1), not a lattice identity.
- Both items stay open inputs of CH1 as the skeleton names them. This draft does not attack them, because on `L_cube` they come after CH1-C3.

---
## 10. Proposed specifications, collected

**None.** Each candidate was considered and rejected, with its reason.

1. *Widen PS-1 to QCAs or quasi-local unitaries* (lead 2). Rejected. Theorems F3 and F4 show that the widening changes `W3` but not the light content of any free sea. Corollary F2a shows that a free update with `W3 != 0` has no PS-7r sea. And no interacting route in section 7 needs it. The widening would add structure its own reasons do not need (smuggle test 4).
2. *Relax PS-1c's transitivity so that a law can fix an odd cluster layout* (Attack 2). Rejected. It would be added to reach a result (smuggle test 2), and it would add a role structure (test 4). Even with it, Attack 2 stops at an unproved strong-coupling flow.
3. *Admit rotor (infinite-dimensional) site or link content* (Attack 3). Not proposed. It conflicts with Qubit and PS-6r ("a finite-dimensional register"), and its reason would be one construction (test 4).
4. *A reading rule for "light" in a Floquet law* (C5). Not a specification. It is a definition of a word in CH1's own target, and under PS-7r the cut `pi` is gapped anyway.

**Owner decisions that the results raise** (decisions, not specifications):

- **D1 (PS-5).** Theorem S3 names a step at which the cell route fails for CH1 and CG1: abelian one-body frames (LW1 B5), and that group cannot be hypercharge (S2). Whether this triggers PS-5's five-mode fallback is the owner's call. The fallback has its own open step (#10027).
- **D2 (PS-8).** The kill test is negative on `L_cube` (5.4). PS-8 as worded should not stay the law to test for CH1 on `L_cube`. Its successor would be a statement about bound states (CH1-C1/C3), which is a target, not a law clause. So no replacement text is offered.

---

## 11. Status (FINISH-style, author-side)

**Part.** CH1, chirality: a gauged chiral light sector. Pass 1 long draft, Claude Opus 5.5 subagent, 2026-11-04. Not distilled, not refereed.

**Target as stated.** CH1 (a) of the skeleton, under `L = L_cube`.

**Outcome.**
- CH1 (a) as stated: **fails on `L_cube`** with `G` the exact gauge group (Theorem S3). It needs PS-5's fallback or non-abelian structure that emerges at long distance (owner decision D1).
- Kill test of PS-8 on the chosen carrier: **PS-8 releases light partners.** Proved at every quasi-free endpoint (K1). In the interacting regime it is forced by anomaly matching (K2 with Lemma AM, a standard principle not proved here).
- Free route: **closed at every locality** (F1-F4). Leads 1 and 2 are answered (3.6), and no widening of PS-1 is warranted.

**Proved here (in full, unrefereed).** Theorem F1, Theorem F2 with Corollaries F2a and F2b, Theorem F3 with Lemma F3a and Corollary F3b, Theorem F3', Theorem F4 (the value of `sigma` only by [check]), Lemma S1 with Corollary S1a, Theorem S2, Theorem S3, Lemma C2, Lemma C3, Theorem K1, Lemma K2.

**Credited, not rebuilt (none is load-bearing for a stated conclusion except as marked).**
- Integrality and additivity of first Chern numbers of projector families on `S^2`. F3's identity does not use them; Lemma F3a uses additivity.
- The degree of the suspension and the normalisation of `omega` as degree (F4, Step 3).
- Vanishing of `SK1(C[Z^3])` (3.6, not used).
- Universality of local gates for factorising the cluster gates (inherited from LW1 5.3).
- Literature in 1.4, for orientation only.

**[check] runs** (scratch, outside the repo, under 15 s each): `W3` and node chiralities of #9863's walk at `m = -2, 0.5, 2` (`32^3` grid); the odd anomaly-free charge sets in 1+1D and 3+1D; the null vectors for `(1, 7 | 5, 5)`; the four Standard Model `U(1)` assignments of S2. They guide only. Each statement they touch has its own proof, or is labelled as guidance.

**Open inputs, by name.**
1. **CH1-C1** (first open statement, section 7): a 1+1D chiral, anomaly-free, odd-charge light sector (L: `(1, 7)`, R: `(5, 5)`) from a `G_1`-covariant gauge-invariant circuit on one-mode sites, in an invariant stationary state. Three attacks are written out, each with its exact failure: F3' (free), Lemma C3 plus an unproved flow (cluster layout), finite dimension (disentangler).
2. **CH1-C3**: its 3+1D lift on `L_cube`.
3. **Lemma AM**: anomaly matching for interacting gauge-covariant updates. The free case is proved (F3); the interacting case fails at the adiabatic step (c) of 5.3.
4. **CH1-ii** and **reflection positivity**, as named in the skeleton (section 9).
5. Owner decisions **D1** (PS-5 fallback) and **D2** (PS-8 retired as the law to test on `L_cube`).

**Corrections to carry into other parts.**
- GA1-i and CG1-i: on `L_cube` the exact gauge `U(1)` cannot be hypercharge or electric charge. At most it is of `B - L` or `X_10` type (Theorem S2).
- MT1 and VC1: on `L_cube` every neutral excitation is a boson (Lemma S1).
- FL1-ii (shared with CH1-i): #10022's condition "If the mirror 16bars are gapped keeping Spin(10)" lives on five-mode sites. On `L_cube` there is no `Spin(10)` to keep (Theorem S3).

**Nothing here uses established physics to justify a step.** Established physics names the targets (the Standard Model charges in S2, the 3-4-5-0 and `(1, 7 | 5, 5)` sets) and the literature is credited for orientation.
