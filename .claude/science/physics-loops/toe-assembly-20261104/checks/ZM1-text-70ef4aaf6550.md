---
statement: ZM1-text
commit: 70ef4aaf655005045d240bb86d54cf47aaa5f28c
content: bb3c9c473fa6728602b432f3bc76db56137710bf67e2c4cd4631b881c0b20dc9
text:
  - 5db0050c47bedfa2804b4ef26a22c73def7649643e404655bfff1ee1842273d9 .claude/science/physics-loops/toe-assembly-20261104/ZM1.md#1. Definitions inferred by the distiller
  - de96ea1bd998e57fe141d17097a4f957217e12cc5b945fe611c0c9efe5e74170 .claude/science/physics-loops/toe-assembly-20261104/ZM1.md#3. Exact block maps (question Q-E)
  - 40bde2ea2b3e7bc0d3aaccae8f7bd53d89e98a0cf78461f0039384bb7b42155e .claude/science/physics-loops/toe-assembly-20261104/ZM1.md#4. The free tick with error control (question Q-F)
  - a5810e979ba4e2b6f017cbb0da9aa05a203311e24e6cd0b0440f8969b27c494e .claude/science/physics-loops/toe-assembly-20261104/ZM1.md#5. The first interacting step (question Q-I)
reads:
  - 65bec1c250e422913cb86dac6c5f3ea6daca0b9a0db11f733f7d39d2cf089956 - .claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md#3. Proposed axiom update (working set)
  - ead33ee916faeae0038cd4a67492b30b7db98a44e402a9de1c22282b76bc3d9c LW1-text .claude/science/physics-loops/toe-assembly-20261104/LW1.md#1. Definitions
  - 2485dc1f464b4652855270785014e0d340f8f28e9aa90a1a2d607a4082bc2816 LW1-text .claude/science/physics-loops/toe-assembly-20261104/LW1.md#2. Statement of \(L_{\rm cube}\)
  - 26d0e19dba6d7f246c0b8e1f605276153c3127f842c5733f7098b3652bbd4ce6 LW1-text .claude/science/physics-loops/toe-assembly-20261104/LW1.md#3. Theorems and proofs
  - bb7fd75578c8d54449c4bd4b4280ad1fa9d31a6b5e75e6b290b3572d4b91ed10 LW1_5-text .claude/science/physics-loops/toe-assembly-20261104/LW1_5.md
verdict: right
failure: none
path: I rebuilt the fibres, kernel and block walk from the real-space LW1 definitions and tested every exact identity and bound by my own code with failing controls, redid each constant and bridge by hand, and solved the Z3 constraints numerically on a small instance; clauses about L5-U/L5-O rest on quoted LW1_5/MT1 lines that are not in the folder.
checker: anthropic/claude-fable-5-2/medium 57845b86-f838-4517-b116-4f9736df6046/check-ZM1
author: anthropic/claude-opus-5-5/unreported 73a4991666
answers: none
steer: none
---
## Finding

**Dispatch note, written by the session that dispatched the check, not by the checker.**

- Statement: every result that `ZM1.md` sections 3 to 5 state as proved follows, as written, from its hypotheses, the definitions of section 1, the working premises of `TOE_ASSEMBLY.md` section 3, and the results of `LW1.md` section 3 taken as given. Items those sections mark open, GAP or a failed attack are excluded and listed below.
- What it does not cover. Several clauses about the five-mode laws rest on lines quoted from `LW1_5.md`, which the checker was not given. It treated each quoted line as a hypothesis and did not verify the quotation, so `LW1_5.md` is in `reads` under the name `LW1_5-text`, and this record stands only given that text. The checker rebuilt the one input cited from `MT1.md` (the cell-periodic sign lift) by its own computation.
- Independence, stated plainly. The text was distilled by Codex (`gpt-6.1-terra`, high) and last edited by a Claude Opus 5.5 lead session (commit `73a4991666`). The checker is a fresh Claude Fable 5.2 session at medium effort: a different model from both, in a separate context, with four files only. It is from the same provider as the last editor, because no third provider is available. It read the authors' status section and section 6 only after its table was written.
- A caution the checker raises for consumers: a later amendment in the file's status section says the open statement ZM1-I1 "as stated has no instance". If so, some results here hold vacuously for the five-mode laws. They stay right as implications; a consumer must not read them as describing a block map that exists.
- Its computations. Six scripts with their outputs are in `check-evidence/ZM1-text-70ef4aaf6550/`. The dispatching session reran the five that produce output on 2026-11-13; each output was identical to the checker's. They are scratch evidence, not repository runners; "Verification owed" below says which results still need one, or a Lean certificate.
- This is one check of one text. It is not an audit. The ZM1 target itself stays open (`parts/ZM1.md`).

Checker's tally: 21 right, 0 wrong, 0 undecided, 8 excluded.

### Claim list

- **Theorem Z0** (line 97, indexing line 95). For `L_cube`, `L5-U`, `L5-O` with base tick `U_0` and any `L>=1`: identity regrouping into blocks of side `2L` with `alpha_1=alpha^L` is (1) exact, (2) of range one block (27 coarse sites) and a finite product of layers of commuting gauge-invariant gates on at most two face-adjacent blocks, (3) covariant under coarse cell translations (`4Lb`) and proper rotations about coarse cell centres, transitive on coarse sites, (4) commutes with every fine gauge transformation, (5) `D = 2^{2 n_s 8L^3} d_l^{48L^3}`. Also the remark (line 106) on a plaquette layer of `l_P` sublayers. Uses LW1: E1 (local automorphisms), dressed factorization, A2, B4, gauged covariance; LW1_5 quotes for the five-mode laws.
- **Lemma Z1a** (line 114). For `0<=mu<2eps<pi`, `delta` not in `2 pi Z^3`: `w`, `w(K)-w(K+delta)`, `w(K)+w(K+delta)` are not constant on any open set, except `w(K)+w(K+Pi)=pi` when `2eps+mu=pi`. Uses LW1 B10(1).
- **Theorem Z1** (line 121). `L>=2`, `n,d>=1`, `J` an isometry commuting with coarse translations with summable kernel, `V^n J = J V_1` with `V_1` bounded: then `d = L^3(d_+ + d_-)`, `0<=d_+-<=4F`, or `d=L^3 d'`, `d'<=8F` in the exceptional case (`2eps+mu=pi`, `L`,`n` even); `1<=d/L^3<=8F`. Uses B10(1), Lemma Z1a.
- **Theorem Z1 for real Majorana maps** (line 135). Same for the real `L5-O` walk: `d=L^3 r_M`, `1<=r_M<=80`; PS-5 content (80 Majorana modes per coarse cell) forces `L=2`, `r_M=10`; no two-step exact tower. Uses Theorem Z1 and the quoted LW1_5 lines 255, 257.
- **Corollary Z1.1** (line 139) and the sentence at line 148. (1) an exact quasi-free zoom keeps at least `L^3` modes per coarse cell; (2) 40 modes per coarse cell forces `L=2`, `r=5`; (3) exact zooms compose, a `k`-step tower needs `(L_1...L_k)^3 | d`, none with two steps at PS-5 content; every quasi-free zoom with fewer than `L^3` modes per coarse cell has nonzero error. Uses Theorem Z1, PS-5.
- **Lemma Z2.0** (line 158). Clifford relations of `A_j, Gamma_j`; fibres `R_e(K)`, `R_o(K)`; `V(K)=1+i s D(K) e^{-i eps R}`, `||D(K)||=(2/sqrt3)(sum sin^2(K_j/2))^{1/2}`. `mu=0`, `0<eps<pi/2`. Uses LW1 A1 and the definitions of `R_T`.
- **Lemma Z2.1** (line 171). `G_j`, `C_j` properties; `h=h_1+h_2+r_3`, `||r_3||<=|K|^3/2` for `|K|<=1`; `{G_j,C_k}=0`. Uses Z2.0, B10 proof.
- **Lemma Z2.2** (line 190). `Y`, `Y^tr` Hermitian; `i[Y,h_1]=h_2`; trig form; `||Y^tr||<=(1/4)sum|sin theta_j|<=(sqrt3/4)|theta|`; rotation covariance. Uses Z2.1 and the cell-periodic sign lift (MT1 Theorem 1, quoted; rebuilt).
- **Lemma Z2.3** (line 201) with its 3D statement (line 208) and covariance Claim (line 221). Orthonormal symmetric kernel `psi`; `g>=0.078L^3`; leakage `<=1.75 theta^4`; exponential decay; `J_L` isometry with fibre `sum_m alpha_m iota_m`, `l(theta)<=1.33|theta|^2`; `J_L rho_c(Q)=F_Q J_L`, `J~_L rho_c(Q)=F_Q J~_L`, `F_Q` the lift of the rotation about the block centre, unique up to phase. Uses A2.
- **Lemma Z2.4** (line 234). Spectral projection perturbation bound `2 delta/(2g-delta)`.
- **Theorem Z2** (line 246). `mu=0`, `0<eps<pi/2`, `L>=2`, `F=1` or `5`: (1) `J~_L` is an isometry, exponentially local, covariant, `Phi_L` is a block map of Definition Z; (2) the coarse law is the fine free walk; (3) `||V^{Lt}J~f-J~V^t f||<=(2.66 kappa^2+1.5 t kappa^3)||f||` for support `|theta|<=kappa<=1`; (4) sea two-point bound with `3.5/v` for `kappa<=sqrt(v)/2`, also with `1-P`. Uses Z2.0-Z2.4, B10, PS-7r, A1a, A2.
- **Higher correlations** (line 283). `|F-F_c|<=n^{(n+2)/2} beta` for normally ordered `2n`-point functions; remark that `p=2` holds for every fixed number of band-limited fields. Uses Z2(3),(4), LW1 definition of quasi-free states.
- **Corollary Z2.1** (line 289). At `L=2^k`, `kappa=2^k a/r<=sqrt(v)/2`, `t<=r/(2^k a)`: two-point error `(3.5/v+2.66+1.5) kappa^2`; zoomed generator `h_1+h_2/L+O(|theta|^3/L^2)`; spectral correction from C1. Uses Z2, C1.
- **Corollary Z2.2** (line 297). `L5-O`: `J~^O=W_f J~_L W_c^*` carries the O walk to the coarse O walk with the same bounds; real kernel, commutes with `SO(10)`; coarse translations intertwined up to parity for even `L`. Uses Z2 and LW1_5 A2-5 (quoted; walk part rebuilt).
- **Remark, massive free tick** (line 301). `V(0)=e^{i mu R}`; exponential decay of equal-time block two-point functions from B10(4).
- **Theorem Z4** (line 315). (G1) implies `D_u>=n_0|S_u|+1`; block-constant embedding gives `40L^3+1` or `8L^3+1`.
- **Theorem Z3** (line 323). (G1),(G2), `Phi(psi)` finite and linear in fine matter with link-algebra coefficients: coefficients vanish at every site outside `S_u`.
- **Theorem Z3'** (line 351) with the Coefficients paragraph (line 349). Same for the norm-closed class.
- **Consequence for Attack 1** (line 359; restated line 386). A norm-convergent grouping of the minimally coupled series of `J~_L` is not `Phi` of a coarse fermion; `J~_L e_u` is not supported on one site.
- **Corollary Z3.1** (line 361). Bounded content `D` and (G1),(G2): linear coarse fermion fields have coefficients on at most `(D-1)/n_0` sites; full-weight transported block averages fail once `8L^3>(D-1)/n_0`.
- **Lemma R-GI** (line 374) and its **Consequence** (line 378). Off-site two-point functions vanish in gauge-invariant states; the ZM1-I1 bound can hold (under the added invariance hypotheses) only if all same-site two-point functions agree exactly for every `t`.

### Per-result table

| label | verdict | failing step / counterexample | the different path I took | what I did not check |
|---|---|---|---|---|
| Theorem Z0 | right | none | Hand rederivation of the support rule (a cube gate that shares a site or a link with `X` contains a point of `X`; electric gates do not enlarge), block geometry and count; `check_Z0_Z1.py`: one free tick moves sup-distance exactly 2 on an `8^3` torus (control: not `<=1`); coarse-cell centre is an odd cube centre, rotation about it = `c_0`-rotation + even translation, blocks permuted, 8 blocks one orbit, for `L=1..5` (control: site-centred rotation fails). | For `L5-U`, `L5-O`: tick structure, covariance (B1-5, B1-U), the values `d_l=C(10,m)`, 512 are from `LW1_5.md`, not here. The dressed (non-free) support rule was derived by hand only, not computed. The plaquette remark (line 106) is conditional on an unspecified layer; derived by hand only. |
| Lemma Z1a | right | none | Redone by hand: used the separation of variables of `chi` for (ii) and, for (iii), `x^2=y^2` with `x-y` strictly monotone in `cos K_i`. `check_Z0_Z1.py`: `w(K)+w(K+Pi)-pi=0` at `2eps+mu=pi` (controls: spread 0.13 and 0.34 at other parameters; the six other half-period shifts vary). | Nothing. |
| Theorem Z1 | right | none | Redone line by line. Independent instance: block fibre built from the hopping rule with twisted block boundary conditions (no use of `iota_m`); spectrum equals `{+-w(xi_m)}` each x4 (error 4e-15); eigenvalue multiplicities of `V_block^n` are 4 with `2L^3` distinct values generically and 8 with `L^3` values exactly in the exceptional case (controls: `n` odd, `L` odd, `2eps+mu != pi` give 4). | No finite computation can test the no-go itself; the continuity/connectedness count (Step 5) is checked by reading only. |
| Theorem Z1, Majorana | right | none | Hand: complexified fibre is `V'(K) x 1_5 (+) conj(V'(-K)) x 1_5`, eigenvalues `e^{+-iw'(K)}` each x40 since `w'` is even; arithmetic `L^3 | 80` in `check_Z0_Z1.out`. Realness of the O-frame walk rebuilt from LW1 (`check_Z2_extras.py`, residual 0). | That the `L5-O` Majorana walk is `O = (V' x 1_5)` in real form (LW1_5 lines 255, 257; quoted, file absent). |
| Corollary Z1.1 (+ line 148) | right | none | Supplied the bridge the text leaves implicit: exactness gives `alpha^L(c(Jf)) in Phi(A_1)`, an element `c(g)` lies in CAR(ran J) only if `g in ran J`, so `ran J` is `V^{-L}`-invariant, hence (fibrewise unitary, finite dimension) `V^L J = J V_1`; this holds for any automorphism `alpha_1`, quasi-free or not. Arithmetic by script. | (2) reads "zoom" as `L>=2`; at `L=1` the identity has `r=40`. PS-5 read as 5 complex modes per site. |
| Lemma Z2.0 | right | none | `check_Z2_cell.py`: fibres built from the real-space definition of `R_T`, compared with the formulas at 200 random `(K, eps)`; residuals <=1e-15 (controls: no `eta` signs, wrong sign of `sin K_j`). | Nothing. |
| Lemma Z2.1 | right | none | Hand recomputation of all constants (0.0992, 0.448, 0.152, total 0.476). Script: `h=i logm V` directly; `max ||h-h_1-h_2||/|K|^3 = 0.065` over `|K|<=1`, six `eps` including 1.5607; algebra residuals 1e-15 (control: wrong `C_j` gives 3.15 at `|K|=0.027`). | Sampling is not a proof of the bound; the bound is by the hand derivation. |
| Lemma Z2.2 | right | none | Script: commutator identities to 5e-15; norm bound never exceeded; brute-force search finds exactly one cell-periodic sign lift (with `s(000)=+1`) for each of the 24 rotations, and `rho Y^tr(theta) rho^* = Y^tr(Q theta)`, `rho V(K) rho^* = V(QK)` to 7e-16 (control without `Q`: 1.02). This rebuilds the MT1 Theorem 1 input. | Nothing. |
| Lemma Z2.3 + Claim | right | none | Hand recomputation of constants (0.2866, 0.0784, 2.165, 27.7/16=1.73). `check_Z2_kernel_thm.py`: `psi` tabulated in real space by FFT for `L=2,3,4,5,8`; Gram residual <=4e-16, symmetry <=1e-16, `min g/L^3 >= 0.25`, `max leak/theta^4 = 0.0054` (control: box kernel 625-820); Claim (5) tested on site coefficients for 8 rotations, `L=2,3`, residual <=3e-17 (control: shifted centre 0.31, 0.22). | Decay rate (4) only observed (`eta=0.5` fits), proved by the contour argument I read. Claim (4) uniqueness read only. |
| Lemma Z2.4 | right | none | Hand: the integral representation and `F-E=FE'-F'E`. Script: 4000 random cases, max ratio 0.361 (control bound `delta/(4g)` is violated, 1.57). | Nothing. |
| Theorem Z2 | right | none | Hand recomputation of every constant (0.516, 0.298, 0.125, 0.049; 1.4175, 3.340, 0.146). Script, different implementation: `J~(theta)` from real-space `psi` and the block fibre from the hopping rule, `L=2,3`, `eps in {0.1,0.8,1.4}`, `t in {1,2,5,1/|theta|}`: `max lhs/bound = 0.029` for (3), `0.0012` for (4); isometry residual 2.5e-15; `m=0` step `0.020 <= 1.5` (control: without the twist the ratio grows like `1/|theta|`: 0.26, 1.05, 4.21). | (1): super-exponential decay of `cal W` read only. `F=5`: the statement that the `L5-U` free walk is `V x 1_5` (LW1_5 section 2) taken as the definition. `1-P` case by algebra only. |
| Higher correlations | right | none | Hand: determinant formula with the LW1 convention `omega(c_y^dag c_x)=P_xy` gives the stated `M_ik`; telescoping + Hadamard. Script: 20000 random pairs, max ratio 1.000 (attained at `n=1`); control without the `n` factor 38. | The closing sentence "p = 2 for every fixed number of band-limited fields" needs, for general orderings, the c-number anticommutators, which Z2(3) bounds; it carries no constant and I checked it by that argument only. |
| Corollary Z2.1 | right | none | Arithmetic: `t kappa<=1` in Z2(4); `L w(theta/L)` from C1 with `k=|theta|/L`. | The Weyl-field counts are quoted from MT1 Theorems 7, 11 (file absent); they are descriptive and not used. |
| Corollary Z2.2 | right | none | Hand: translation phases `(-1)^{(L+1) sum u}`; `check_Z2_extras.py`: O-frame walk and O-frame twist satisfy the position-space reality condition exactly (control: twist without the gauge 0.12); residue phases cancel. | The `SO(10)` clause needs the form of the `SO(10)` action on Majorana flavours (LW1_5, absent). |
| Remark, massive tick | right | none | Script: `V(0)=e^{i mu R}` to 4e-16. Decay statement follows from B10(4) and the exponential kernels by a convolution bound (hand). | Nothing. |
| Theorem Z4 | right | none | Hand; instance count in `check_Z3_Z4.py` (4,5,6,7 distinct values for `|S|=1..4`). | Gauss generator forms for `L5-U`, `L5-O` are as stated at line 307 (LW1_5 absent). |
| Theorem Z3 | right | none | Different path: on the smallest `L_cube` instance (two sites, one link, `S=1/2` and `S=1`) solved CAR + `[G_y,Psi]=0` numerically from 30 random starts each; all 60 exact solutions have `||T_y||,||T'_y|| <= 3e-8` (solver tolerance; the constraint is quadratic there). Controls: CAR without the gauge condition gives `T_y` of norm 1.6-2.0; the gauge condition without CAR admits `J^dag c_y`, which fails `{Psi,Psi^*}=1` by 2.0 and 3.5. Also read line by line. | `L5-U`, `L5-O`: that link operators commute with matter and the choices `T=E_jj`, `M^{2j-1,2j}` have matter part `n_{x,j}` (LW1_5 absent). |
| Theorem Z3' | right | none | Read line by line and rederived (c): `E_0(Psi_k^2)=1` and the `c^dag(1-n)c` trick; (d) with spectral projections. | Same LW1_5 items as Z3. No computation (infinite-dimensional statement). |
| Consequence for Attack 1 | right | none | Hand: `|fine Bloch transform of J~_L e_u| = |psi^(3)^(K)|`, zero at `K=2 pi m/L`, `m != 0`, nonzero at 0; a one-site vector has constant modulus. | Linear independence of `r^y_j r^{x dag}_k` (LW1_5 line 117) and `ZM1_REFEREE.md` section 3.8, both absent; for `L_cube` the transport `prod J_l` along distinct links is nonzero by LW1 section 1. |
| Corollary Z3.1 | right | none | Z3 + Z4 combined by hand. | As Z3, Z4. |
| Lemma R-GI + Consequence | right | none | Hand: charge counting under `e^{i theta G^1_x}`; for the Consequence, the same-site reduction, translation invariance, a unit profile with support in `|theta|<=kappa`, then `kappa -> 0` at fixed `t`. | "LW1_5 line 136, U" taken as quoted. The Consequence also uses (Z-b) and coarse-translation covariance of `alpha_1`, which the precise statement of ZM1-I1 supplies. |

### Excluded

- **GAP Z2-spatial** (line 279): the text itself says the bound does not cover spatially separated observables, times beyond `1/kappa`, a tower, or ZM1(a)1-3. Marked GAP.
- **ZM1-I1** (line 367): marked open; only Lemma R-GI and its Consequence about it are checked.
- **Attack 1** as an attack (line 386): a failed attack; its proved failing step is the "Consequence for Attack 1" above, which is included.
- **Attack 2** (line 388): a failed attack; the text says the error bounds "have not been transferred" and that the cited coherence bound (GA2_Y2 Theorem 3.4, absent) does not rule out other approximations. Nothing is claimed proved.
- **GAP Attack 3 / Attack 3** (lines 390-392): marked GAP, "not a proof"; the rank bound is stated as conditional on an unproved restriction.
- **Scope paragraphs** (lines 146, 363) and the nonlinear example `W c W^*`: statements of what is not decided; the example is asserted without proof as an illustration and "extending it ... is a separate obligation". Not counted.
- **"Four Weyl fields per cell / twenty"** and "Clifford cone of MT1 Theorem 7" (line 293): quotations of MT1, descriptive.
- **[check] lines** (165, 186, 230, 277): reports of the authors' scripts `check_h2.py`, `check_z2.py`, `check_static.py`, which are not in this folder. Not evidence here; my scripts gave compatible numbers (0.065, 0.0054) by independent code.

### Against sections 0 and 6

Read after the table above was written. No verdict was changed.

- Section 0 "Proved within the stated scopes" lists Z0, Z1, Z2.0-Z2.4, Z2, Z4, Z3. **Agree** on each. It calls Z2 "conditional on the source formulas"; I rebuilt those formulas (`R_e(K)`, `R_o(K)`, `V+V^*` scalar, the cell-periodic sign lifts) from the `LW1.md` definitions by computation, so for `L_cube` that condition is discharged here.
- Section 0 does not list among the proved results: Theorem Z1 for Majorana maps, the covariance Claim of Lemma Z2.3, the `1-P` case of Z2(4), Higher correlations, Theorem Z3' (it is named under GAP as "also holds"), the Consequence for Attack 1, Lemma R-GI and its Consequence. It says "Referee closures imported below are unrefereed". I checked each of these and found them right. **No disagreement**, but their status in section 0 is weaker than what I found.
- Section 0 GAP list (Z2-spatial, Attack 3, Attack 2 not exhaustive, massive decay not an empty limit): **agree**; these are the items I excluded.
- Section 0 Amendment 3 says that ZM1-I1 "as stated has no instance": a unital Definition-Z block map with (G1) on disjoint singleton sets and (Z-a) forces `L=1` on `L5-U[m]` and `L5-O[S_+]` (`ZM1I1A.md`, not in this folder; **not verified**). Two remarks. (a) It is consistent with, and stronger than, the Consequence of Lemma R-GI that I checked. (b) If it holds, then for the five-mode laws the hypothesis "Phi satisfies (G1)-(G2) with singleton `S_u`, `L>=2`" is empty, so Theorem Z3, Z3', Corollary Z3.1 and Lemma R-GI are true there vacuously in that case. They stay right as implications; a consumer must not read them as describing an existing block map. Also lines 392-394 of section 5 ("two failed attacks on file", "not a proof that ZM1-I1 is false. No counterexample is known") are older than Amendment 3 and are superseded by it; they are not proved results, so no verdict is affected.
- Section 0 Amendments 1, 2, 4: about prior work, an owner decision and a later item. Nothing to compare; none changes a proved result, as section 0 itself says.
- Section 0: "Draft numerical checks are reports, not independently rerun." **Agree**; I did not have those scripts. My own scripts reproduce the two reported maxima (0.065 for `r_3`, 0.0054 for the leakage) with independent code; the reported `0.039` for the `m=0` step is over a different sample from mine (`0.020`), both far below 1.5.
- Section 6: Z1 excludes exact quasi-free towers only; Z2 is a band-limited comparison; Z3/Z3' exclude linear fields only; Definitions Z and G are proposed readings. **Agree**; my verdicts cover exactly those scopes.

### Verification owed

- Z0: repository compute check possible for the free instance (support growth, block permutation; done here) and, on a small torus with spin-1/2 links, for the dressed support rule (not done; needs a 2-cube system, feasible). Counting (5) and the geometry of (3) suit a Lean certificate. I would choose the compute check.
- Lemma Z1a: Lean-formalizable (trigonometric identities plus the identity theorem); compute check only for the exceptional identity. Choose Lean if a certificate is wanted; otherwise the instance check here.
- Theorem Z1, Majorana form, Corollary Z1.1: no-go statements over all isometries; no finite compute check tests them. Step 1 and Step 3 have finite instances (done here). A Lean certificate is the only real test; it is a sizeable formalization (continuity of fibre projections, connectedness). The divisibility arithmetic is trivially Lean.
- Lemma Z2.0: exact finite matrix identities; compute check (done) or Lean (`8x8` matrices over `Q(i, sqrt3)`); choose the compute check with exact arithmetic.
- Lemma Z2.1, Z2.2: (1),(3) are exact matrix identities (compute or Lean); the `|K|^3/2` bound is an inequality over a ball, compute gives sampling only; Lean possible with interval bounds. Choose compute for the identities, Lean only if the constant matters downstream.
- Lemma Z2.3 and Claim: orthonormality, symmetry and Claim (5) are exact and suit a compute check (done for `L<=8`); the bounds for all `L` are inequalities, Lean-formalizable. Choose compute.
- Lemma Z2.4: standard; Lean-formalizable; compute check by random instances (done). Choose compute.
- Theorem Z2, Corollary Z2.1, Higher correlations: inequalities with explicit constants; compute check with the block fibre built from the hopping rule plus the no-twist control (done for `L=2,3`). Choose compute.
- Corollary Z2.2: exact reality identity; compute check (done for the walk and the twist). The `SO(10)` clause: neither, until `LW1_5.md` is at hand.
- Remark (massive): compute check (done) for `V(0)`; decay statement neither.
- Theorem Z4: counting; Lean, or a small exact compute check. Choose compute.
- Theorem Z3: small exact instances by computer algebra (solve CAR + Gauss commutation over a spin-1/2 link exactly, e.g. a Groebner or linear-then-normal argument) with the two controls used here; or Lean (the proof is short and finite-dimensional). I would choose Lean for Z3, since the numerical solve reaches only solver tolerance.
- Theorem Z3', Consequence for Attack 1, Corollary Z3.1, Lemma R-GI and Consequence: C*-algebraic statements; compute: neither; Lean possible but heavy. Neither is my choice short of a formalization project.

## Not run

- Did not read `LW1.md` section 0 or section 4 (as instructed), nor its section 3 beyond the cited results (A1, A1a, dressed factorization, UALL gap note, A2, A3, B2-B5 as they appeared in the range read, B10, C1). E1 was used only as cited (local automorphisms; gates away from the support cancel) and its text was not read.
- Did not read `WORKING_SET.md` or the axioms file in full; only the PS-1c, PS-5, PS-6r, PS-7r rows found by search.
- `LW1_5.md`, `MT1.md`, `GA2_Y2.md`, `ZM1_REFEREE.md`, `ZM1I1A.md`, `check_h2.py`, `check_z2.py`, `check_static.py`, arXiv:2511.23398: not in the folder, not read. Every clause that depends on them is listed in the table.
- No computation of the dressed (interacting) tick. No instance of Z3 beyond two sites and one link; none for `L5-U` or `L5-O`.
- Z2(3),(4) computed only for `L=2,3` (block dimension 64, 216), three `eps`, 18 momenta per `L`; kernel properties for `L<=8`. The bounds for general `L` rest on the hand derivation.
- No check of whether Definitions Z and G are the right readings, nor of any four-test assessment; those are premises here.
- Scripts and outputs: `check_common.py` (shared definitions), `check_Z0_Z1.py/.out`, `check_Z2_cell.py/.out`, `check_Z2_kernel_thm.py/.out`, `check_Z2_extras.py/.out`, `check_Z3_Z4.py/.out`.
