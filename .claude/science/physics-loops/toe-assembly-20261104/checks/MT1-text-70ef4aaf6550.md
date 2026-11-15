---
statement: MT1-text
commit: 70ef4aaf655005045d240bb86d54cf47aaa5f28c
content: 0e4ec889bde2b95e3282aeeb7be449f8a0ecc4156f29a1525aa6b948b031f5bf
text:
  - 5a651ded39423c3d1597c619e28da4128bc5dd5f7b246010a19f91a5b8bdb4eb .claude/science/physics-loops/toe-assembly-20261104/MT1.md#1. Definitions inferred by the distiller
  - 086ef59b7d39fed520273a1a1096a2f01c23d544a7a9ce7c4ae4bef9d3c8a4ce .claude/science/physics-loops/toe-assembly-20261104/MT1.md#2. Lifts and exchange algebra
  - 3da2d7abf566ab3bca3a0bfd3acd47581f594175695cea0faa0beece618ce5df .claude/science/physics-loops/toe-assembly-20261104/MT1.md#3. Clifford cell and lattice rotations
  - bab350e26ccdbe3f6839d2f6ac71ec2549a15206b55c37f2f328d86aa0add1bc .claude/science/physics-loops/toe-assembly-20261104/MT1.md#4. Free node and emergent spin
  - 11ecdf368a0c3202fba23341012de0895d46af57bfdbf0ed715f34e8cb1a873f .claude/science/physics-loops/toe-assembly-20261104/MT1.md#5. A symmetry-allowed cone splitting
  - 35d4b64599ab5fab5877bb4e6d38748a96b5842d9e15dcaaf1f6c041ea62ce16 .claude/science/physics-loops/toe-assembly-20261104/MT1.md#7. Referee closures
reads:
  - 65bec1c250e422913cb86dac6c5f3ea6daca0b9a0db11f733f7d39d2cf089956 - .claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md#3. Proposed axiom update (working set)
  - ead33ee916faeae0038cd4a67492b30b7db98a44e402a9de1c22282b76bc3d9c LW1-text .claude/science/physics-loops/toe-assembly-20261104/LW1.md#1. Definitions
  - 2485dc1f464b4652855270785014e0d340f8f28e9aa90a1a2d607a4082bc2816 LW1-text .claude/science/physics-loops/toe-assembly-20261104/LW1.md#2. Statement of \(L_{\rm cube}\)
  - 26d0e19dba6d7f246c0b8e1f605276153c3127f842c5733f7098b3652bbd4ce6 LW1-text .claude/science/physics-loops/toe-assembly-20261104/LW1.md#3. Theorems and proofs
  - 25943a6b383b6a20e40c47a3b539ab4f79b51d8ef2a5050fdf9c9ebd62a2de10 VC1_5-text .claude/science/physics-loops/toe-assembly-20261104/VC1_5.md#1. Definitions inferred by the distiller
  - da135973997aba6730bf72a5208c8e0c1967117dce71273a70f8e14d554596da VC1_5-text .claude/science/physics-loops/toe-assembly-20261104/VC1_5.md#2. Laws, averaging and symmetry
  - bb7fd75578c8d54449c4bd4b4280ad1fa9d31a6b5e75e6b290b3572d4b91ed10 LW1_5-text .claude/science/physics-loops/toe-assembly-20261104/LW1_5.md
verdict: right
failure: none
path: Operators were rebuilt from LW1's lattice definitions on tori and Fock spaces and each identity, commutant dimension and solution space was computed directly with failing controls, instead of following the text's Clifford-algebra derivations.
checker: anthropic/claude-fable-5-2/medium 57845b86-f838-4517-b116-4f9736df6046/check-MT1
author: anthropic/claude-opus-5-5/unreported 9daf652347
answers: none
steer: none
---
## Finding

**Dispatch note, written by the session that dispatched the check, not by the checker.**

- Statement: every result that `MT1.md` sections 2 to 5 and the referee closures C1 to C8 of section 7 state as proved follows, as written, from its hypotheses, the definitions of section 1, the working premises of `TOE_ASSEMBLY.md` section 3, and the imported results it cites, taken as given. Items the text marks open, GAP or a reading that is not adopted are excluded and listed below. Every verdict is for a formal implication; words such as "spin", "taste" and "exchange" are not judged as physical identifications.
- What it does not cover. The text quotes `LW1_5.md`, which the checker was not given. It closed the five-mode clauses from the restatements in `VC1_5.md` (section 1 item 1, section 2, Theorem 2.2) and did not verify the `LW1_5.md` quotations. Both files are in `reads`, so this record stands only given `VC1_5-text` and `LW1_5-text`. If `LW1_5.md` defines the link operators, the centre or the dressed lifts differently from those restatements, Theorems 3, 5 (dressed clause), 6 (O clause) and C1, C2, C5, C7(a), C8 need a recheck. No result of `ZM1.md` is used.
- Two things the checker found that are not failures. One sentence in the proof of C8 ("two share at most one link") is false on the smallest torus; the conclusion still holds by the reason the checker gives. Two sentences in the unchecked status and open sections disagree with each other about an antiunitary symmetry of the dressed L5-O tick (section 0 Amendment 1 against section 6.2 A1).
- Independence, stated plainly. The text was distilled by Codex (`gpt-6.1-terra`, high) and last edited by a Claude Opus 5.5 lead session (commit `9daf652347`); the closures C1 to C8 come from a Claude Opus 5.5 referee. The checker is a fresh Claude Fable 5.2 session at medium effort: a different model from all of them, in a separate context, with six files only. It is from the same provider as the last editor, because no third provider is available. It read the authors' status section and section 6 only after its table was written.
- Its computations. Six scripts with their outputs are in `check-evidence/MT1-text-70ef4aaf6550/`. The dispatching session reran the five that produce output on 2026-11-13; each computed output was identical to the checker's (the saved files carry one extra shell timing line). They are scratch evidence, not repository runners; "Verification owed" below says which results still need one, or a Lean certificate.
- This is one check of one text. It is not an audit. The MT1 target itself stays open (`parts/MT1.md`).

Checker's tally: 23 right, 0 wrong, 0 undecided, 11 excluded.

### Claim list

All results are formal implications about the stated operators. None of the included results asserts a physical identification; where the text uses the words "spin", "taste", "exchange" it marks the physical reading as proposed or open (lines 43, 45, 47, 60, 99, 111, 115), and my verdicts do not cover those readings.

- **Theorem 1 (lifts)**, line 58. Each proper cubic rotation Q about c_0 has a site-permuting sign lift commuting with R_e and R_o; it is cell-periodic; any lift with site phases equals it up to one constant phase; a five-flavour lift is rho(Q) (x) w; fibre matrix is K-independent and rho-hat R_T(K) rho-hat* = R_T(QK); all of it on every even torus. Uses LW1 A1 (face flux -1), LW1 A2 (existence of the sign gauge).
- **Theorem 2 (resolved hopping identity)**, line 62. For distinct neighbours j,k,l of i, link operators commuting with each other and with matter, same central mode: t_il t_ki t_ij = - t_ij t_ki t_il, for the U (complex) and O (Majorana) forms. Uses only CAR.
- **Theorem 3 (finite cluster presentation)**, line 72. On an even torus, with 35 modes per site cluster, the law's Hilbert space is the constrained subspace of the tensor product of cluster Fock spaces; hops are sums of products of two endpoint-cluster operators; the centre at a site is cluster parity up to a scalar; centre-even local law operators are cluster-local (via C2). Uses the five-mode law structure (VC1_5 section 2), link/matter commutation (VC1_5 section 1 item 1).
- **Negative statement inside the GAP at line 76**: no encoding represents single odd matter operators on disjoint tensor factors. Proof given in the line.
- **Theorem 4 (cell algebra)**, line 80. A_j, Gamma_j are six anticommuting Hermitian involutions; 64 monomials are an orthogonal basis of M_8; fibre formulas for R_e(K), R_o(K); rho-hat A_j rho-hat* = A_pi(j), rho-hat Gamma_j rho-hat* = s_j Gamma_pi(j). Uses LW1 definitions of R_T, eta; Theorem 1.
- **Theorem 5 (half-turns and parity)**, line 89. Lifts of perpendicular face half-turns anticommute (one-body, every even torus); same with five flavours for a projective action with scalar squares; Fock lifts commute up to (-1)^N; dressed lifts' automorphisms obey alpha_1 alpha_2 = theta alpha_2 alpha_1. Uses Theorems 1, 4; LW1 gauged covariance (line 247); VC1_5 Theorem 2.2.
- **Remarks after Theorem 5**, line 93. Perpendicular edge half-turn lifts anticommute; a sign-lift face quarter-turn has fourth power -1; a constant phase changes the fourth power but not the half-turn commutator.
- **Theorem 6 (centre and matter parity)**, line 95. For an operator supported in Lambda (links with both endpoints in Lambda), theta is conjugation by the product of centres over Lambda, on L_cube, U, O[S_+]; gauge-invariant local operators are theta-even; on every even torus the product of all centres is (-1)^N. Uses LW1 Gauss generator; VC1_5 section 2 (Q_x, S_+).
- **Theorem 7 (free node)**, line 103. At mu=0, V(K)=exp(-ih), h = v sum K_j G_j + O(K^2), v = sin(eps)/sqrt3, G_j = U Gamma_j U*, U = exp(i eps R_e/2); eigenvalues +-v|K| fourfold; V=I only at K=0; at mu>0, V(0)=exp(i mu R_e) and {R_e, Gamma_j}=0. Uses Theorem 4, LW1 B10 item 1.
- **Correction**, line 113. chi = -i Gamma_1 Gamma_2 Gamma_3 anticommutes with R_e; U chi U* differs from chi in the window; chi_G = U chi U*; chi eigenspaces are rotation-invariant.
- **Theorem 8 (spin times taste)**, line 115. S, S^A commuting spin-1/2 triples; S commutes with R_e; rho-hat(Q)=S(Q~)T(Q) with T commuting with Gamma and permuting A; face half-turns have scalar T; three-cycles and transpositions have the stated taste rotations; taste and the 4-dimensional projective cell representation are irreducible on each chirality. Remark at line 119: character moduli 4,1,0,0,0.
- **Theorem 9 (ER boost algebra)**, line 121. Under the ER definition with Clifford N_j: [K_i,K_j] = -i v^2 eps_ijk (L_k+S^N_k), J = L+S^N, [J,h_1]=0, internal summands spin 1/2; the free massless node satisfies the ER hypothesis with internal generator S (D S D* for L5-O by the convention of line 37); at mu>0 the R_e eigenspaces carry spin 1/2 with multiplicity two. Uses Theorem 7.
- **Corollary 9.1**, line 129. Spin factors of cell rotations lie in the ER SU(2); T(Q)=U T(Q) U* commutes with G_j; rho-hat(Q) is a phase times a pure spin rotation exactly for the identity and the three face half-turns; no homomorphism SU(2)->U(2) restricts (up to phases) to the taste action on the lifts of O.
- **Theorem 10 (cone splitting)**, line 137. h_u = v sum K_j (G_j + u Z^G_j) is covariant under the 24 rotations and inversion and obeys the antiunitary condition; for small nonzero u it is not one isotropic Clifford cone; the added term is the leading term of a finite-range cell-periodic operator.
- **Paragraph after Theorem 10**, line 141. At mu=0, sigma = V_e^{-1} tau commutes with V; same for M_e^{-1} tau on the dressed base tick at tau_E=0. Uses LW1 A2 last paragraph.
- **C1**, line 167. With the laws' own link components, both sides of Theorem 2 are nonzero.
- **C2**, line 180. Centre-even finitely supported law operators map to finite sums of products of operators on the cluster factors of their sites and link endpoints.
- **C3**, line 192. Fibre of sigma at K=0 is c chi_G; node forms of the four symmetries on the linear term.
- **C4 (Proposition C)**, line 202. Hermitian 8x8 triples with (R),(I),(Theta),(sigma) are a G_j, a real; each of (I),(Theta),(sigma) is needed, with three witnesses. Remark at line 223 (unconditional parts).
- **C5**, line 225. Inversion x -> 1-x lifts to a symmetry of the dressed base tick on all three laws for all eps, mu, tau_E.
- **C6**, line 236. On a finite even torus Theta_d = D_s K fixes U_0 at tau_E=0 (L5-U, L_cube) and inverts W_E otherwise.
- **C7 (a)-(d)**, line 242. Dressed L5-O lift acts on matter by rho(Q); rho(Q) is a lift of W V W* exactly for the three rotations with all s_j=+1; V-frame fibre of the dressed lift is a phase times rho-hat(Q) prod_{s_j=-1} Z_j with the stated action; W rho(Q) W* = c-bar rho(Q) D_Q.
- **C8**, line 260. Product of all centres on an even torus is (-1)^N exactly.

### Per-result table

| label | verdict | failing step or counterexample | different path taken | not checked |
|---|---|---|---|---|
| Theorem 1 | right | none | `check_lattice.py`: built R_e, R_o from LW1 section 1 on tori L=2,4,6; solved for the sign gauge of all 24 rotations by graph search; tested cell-periodicity, commutation, fibre covariance at every torus momentum, and that the diagonal commutant of {R_e,R_o} is 1-dimensional. Flavour form by hand: a site-matrix ratio w_x obeys w_y = w_x on each edge. | infinite lattice only through LW1 A2 (given); tori L>6 |
| Theorem 2 | right | none | `check_T2_C1.py`: explicit Jordan-Wigner Fock space, 4 sites, random complex link matrices on separate tensor factors, both U and Majorana forms. Controls: different central mode, and hard-core bosons (sign +) are rejected. Hand derivation with c c^dag = 1-n agrees. | nothing |
| Theorem 3 | right | none | Hand check of each clause (parity of each hop factor per species, centre = cluster parity, restriction to the constraint). The O centre clause checked without the LW1_5 identities: any Spin(10) centre generator is a product of ten-Majorana volume elements, each a scalar times a parity (`check_T2_C1.py`: product of ten end Majoranas = i(-1)^p). Mechanism run on a reduced analog (3-site ring, 9 modes) in `check_T3_C2_analog.py` with controls (single odd operators are not local). | no instance of the full statement was computed (smallest has 280 modes); extension to L_cube at S=1/2 (line 76) rests on WORKING_SET 3.5 and was not separately computed; "plaquette operators are covered if they preserve the constraints" is conditional |
| Negative statement, line 76 | right | none | Hand: operators on disjoint tensor factors commute; c_x c_y = -c_y c_x and c_x c_y is nonzero, so both cannot hold. Control in `check_T3_C2_analog.py`. | nothing |
| Theorem 4 | right | none | `check_lattice.py`: Bloch-projected torus operators compared with the displayed fibres at all momenta of L=2,4,6 (control: wrong sign of the sin term rejected); Gram matrix of the 64 monomials = 8*identity; rotation rules tested on torus-derived fibre lifts for all 24 Q (the text differentiates the covariance instead). | nothing |
| Theorem 5 | right | none | `check_lattice.py`: anticommutation of the full torus lifts (not only fibres) at L=2,4,6. Flavour clause by hand: commutator scalar lambda, a^2 b = lambda^2 b a^2 gives lambda^2=1, and det over C^5 gives (-lambda)^5=1, so lambda=-1. Dressed clause: matter part is the sign lift (LW1 line 247; VC1_5 Theorem 2.2), link parts are permutations with an involutive flip, which commute. | the dressed O lift is taken as VC1_5 Theorem 2.2 describes it (sign on matter, swap of ends) |
| Remarks after Theorem 5 | right | none | `check_lattice.py`: edge half-turns about (1,1,0) and (1,-1,0) anticommute; quarter-turn sign lift to the fourth power = -1, at L=2,4,6. | the other two perpendicular edge pairs (they follow by the three-cycle) |
| Theorem 6 | right | none | Hand: L_cube e^{i pi E} e^{-i pi E}=1; U (-1)^{p_x+p_y}=(-1)^m; O end factors are (+-i)(-1)^{p} each and their product is a scalar on S_+ under either sign convention (`check_T2_C1.py`). Torus product: scalars (+-i)^V, (-1)^{3V}, (-1)^{3Vm} are 1 because 8 divides V. | exact form of omega_x in LW1_5 (my path does not need it) |
| Theorem 7 | right | none | Hand via the closed form e^{i eps (R+d)} = cos(eps r) + i sin(eps r)(R+d)/r for anticommuting R, d (not Duhamel). `check_lattice.py`: i log V(K) against v sum K_j G_j at |K|=1e-3,1e-4 for four eps; control with Gamma_j in place of G_j rejected; grid scan for V=I. | "only node" rests on LW1 B10 item 1 (given); the grid is a sanity test, not a proof |
| Correction, line 113 | right | none | Hand: A_j passes three Gammas. `check_lattice.py`: sigma-hat(0) is proportional to chi_G and not to chi. | nothing |
| Theorem 8 and line 119 | right | none | `check_lattice.py`: T := S(Q~)^{-1} rho-hat(Q) computed from torus lifts for all 24 Q; commutation with Gamma, permutation of A, the explicit taste rotations, scalar T exactly for 4 elements; irreducibility by commutant dimension (1 for the 4-dim representation, 4 for the taste operators) on both chiralities; character moduli by class. | nothing |
| Theorem 9 | right | none | `check_T9.py`: exact sympy computation on vector-valued functions for three Clifford triples (Pauli, a reducible 4-dim one, the opposite chirality). Controls: L - S^N and a non-Clifford triple are rejected. Node clause: N_j = v G_j from Theorem 7 and U S U* = S (`check_lattice.py`). | the claim is formal; that J generates the physical rotation group is marked open by the text (line 47) |
| Corollary 9.1 | right | none | `check_lattice.py` for clauses 2 and 3. Clause 4 by hand: a homomorphism sending one trace-zero element to a scalar sends all of them to that scalar, and SU(2) is generated by products of two of them. | read "extending" with respect to the given embedding of O in SO(3); under that reading the proof closes |
| Theorem 10 | right | none | `check_T10_C4.py`: inversion lift found on the torus (fibre +-A1A2A3); covariance residuals for 24 rotations, inversion, and the antiunitary condition at 1e-15; axial squared speed exactly 1+u^2; diagonal squared velocity 1+(2u/3)Y+u^2(sum Z)^2/3 with Y of eigenvalues +-3.46, 0; anticommutator test of isotropy fails for u = 1e-3, 1e-2, 0.1, -0.05; fibre of the finite-range operator at 27 momenta. | "all sufficiently small u" is by the first-order argument; sampled u only numerically |
| Paragraph after Theorem 10 (sigma) | right | none | `check_lattice.py`: constructed tau on tori L=2,4,6 and verified sigma V sigma^{-1} = V for three eps. Dressed clause by hand: tau maps H_C to -H_{C+1}, so M_e and M_o are exchanged when a_e=a_o. | dressed clause not computed |
| C1 | right | none | `check_T2_C1.py`: r^y_j r^x_k^dag nonzero on Lambda^m C^10 for every 1<=m<=9 and every (j,k); control m=0,10 gives zero; (i eta_a eta_{10+b})^2=1 for all a,b. | that these are the laws' own link components is taken from the statement and VC1_5 section 2 |
| C2 | right | none | Hand, with the species order (matter first) made explicit: link-even factors carry no Klein string, so the extension uses only modes of clusters in T. Step 1 matrix units in `check_T2_C1.py`; mechanism on the reduced analog. | no full instance |
| C3 and node forms | right | none | `check_lattice.py`: tau built from its defining relations on tori; fibre at K=0 proportional to chi; sigma-hat(0) proportional to chi_G for three eps (control: not proportional to chi). | nothing |
| C4 | right | none | `check_T10_C4.py`: solved the real-linear system on Hermitian triples directly (192 unknowns): dimensions 8, 4, 3, 1, 2, 2 for (R), (R,I), (R,I,Theta), all four, (R,I,sigma), (R,Theta,sigma), at two eps. Witnesses: each Hermitian, satisfies its three conditions at 1e-15, violates the fourth, fails the isotropy test for four values of u; squared-speed spreads 0.0566 and 0.0283 at u=0.01. Controls: unconjugated Gamma_j rejected. | Remark at line 223: only the unconditional sentences; its hypothesis is excluded |
| C5 | right | none | `check_T10_C4.py`: the inversion sign gauge exists on the L=4 torus and commutes with R_e, R_o. Hand: tilings preserved; reversed-link maps for the three laws (L_cube from LW1 line 247; U and O from VC1_5 Theorem 2.2 and the swap in C7(a)); electric layers even under reversal. | dressed gates not computed |
| C6 | right | none | Hand: reality of c, rishons, J, E in the stated basis; antiunitary conjugation of e^{-iaH}. Free analog D_s conj(V) D_s = V computed in `check_T10_C4.py`. | dressed torus instance not computed |
| C7 (a)-(d) and consequence | right | none | (a) by hand from the end swap. (b),(c),(d) in `check_lattice.py` on L=4: exactly 3 of 24 lifts commute with W R_T W*; both conjugates are phases times rho D_Q; fibre action Gamma_k -> Gamma_pi(k), A_k -> s_k A_pi(k). | L not divisible by 4 (W is not periodic there) |
| C8 | right | none | Same hand computation as Theorem 6. The sentence "two share at most one link" (line 264) is false on the L=2 torus, where neighbours share two links; commutation still holds because each centre acts on each link through its own end factor, so the conclusion stands. | nothing |

### Excluded

- Line 43, reading R-X (exchange statistic): proposed, not adopted.
- Line 45, spinor-class label; line 47, ER as the physical rotation group; line 49, family readings M1-M3: proposed or unadopted readings.
- Line 68, GAP (draft 2.1): that every excitation moved by the laws has a physical exchange statistic. Marked GAP. The draft's U example is "a reported numerical check, not reproduced".
- Line 76, GAP (draft Corollary 2.3): MT1-i remains open; the BKSF-and-role-pattern input is not proved. Marked open. (The one proved negative sentence in that paragraph is included above.)
- Line 99: "a physical charged state and its boundary dressing still need specification". Open.
- Line 119: identification of the physical continuum spin. Not claimed.
- Line 135: physical uniqueness of the ER choice. Open.
- Line 141, last sentence: the draft's numerical dimensions, sample speeds and sigma = -chi identification are "reported checks, not independently verified results". (I recomputed the dimensions and spreads; they agree.)
- Line 223, C4 Remark: the hypothesis that the leading generator of light fermion-odd excitations is such a triple. "The hypothesis is not proved."
- Line 240, last sentence: non-applicability of the C6 argument to L5-O. A statement about an argument, not a result; gamma_{2j} = -i(c - c^dag) is indeed not real.
- Line 165: the closures "have not been independently refereed" is a status note, not a result.

### Imported results used

- `LW1.md` section 1 definitions (eta_i, R_T, V_e, V_o, V, tori, Theta, D_s): Theorems 1, 4, 7, 10, C3, C6.
- `LW1.md` Lemma A1 (face sign product -1, involutions): Theorems 1, 4; C5.
- `LW1.md` Theorem A2 and its proof (sign gauge; last paragraph on the diagonal translation): Theorem 1, paragraph after Theorem 10, C3, C5.
- `LW1.md` gauged covariance proof, line 247 (reversed link): Theorem 5 (dressed clause), C5.
- `LW1.md` Theorem B10 item 1 and the line "Each R_T is real and satisfies D_s R_T D_s = -R_T": Theorem 7 (only node), Theorem 10 (antiunitary condition), C6.
- `VC1_5.md` section 1 item 1 (links commute with matter and with one another): Theorems 2, 3, C1, C2.
- `VC1_5.md` section 2 (law description: rishons, Q_x, S_+, electric factors) and Theorem 2.2 (dressed U and O lifts): Theorems 3, 5, 6, C1, C5, C7(a), C8.
- `WORKING_SET.md` PS-5 (five modes), PS-6r (finite links), 3.5 (both five-mode laws live; one-mode U is L_cube at S=1/2): setting of Theorems 3, 6.
- `ZM1.md`: no result of it is used by the checked sections. `MINIMAL_AXIOMS_2026-06-29.md`: not used directly by any proof step in the checked sections.
- `LW1_5.md` (not in the folder): quoted at lines 171, 231-232, 250, 256, 264. Not verifiable here; my paths avoid needing the quotations except as the definition of the end swap, which VC1_5 Theorem 2.2 also states.

### Against sections 0 and 6

Read after the table above was written. No verdict was changed.

- Section 0, "Proved in the stated algebraic setting" (line 26). Item by item: sign lift unique up to phase (Theorem 1): agrees. Matter parity implemented locally by the centre (Theorem 6): agrees. Hopping identity sign -1: agrees. Local cluster presentation for the centre-even algebra: agrees, with my remark that no full instance was computed. Six-generator Clifford algebra: agrees. Half-turn lifts anticommute: agrees. One isotropic Clifford cone at the massless free node: agrees (Theorem 7). Spin 1/2 under ER: agrees as a formal statement. Spin-taste factorization and irreducibility per chirality: agrees. Corollary 9.1: agrees under the reading of "extending" stated in my table. Cone splitting allowed by rotations, inversion and the antiunitary symmetry, forbidden by sigma at mu=0: agrees (my solution-space dimensions 3 and 1).
- Section 0, same paragraph, last sentence, and section 6 Theorem 11 (20 Weyl fields, representations). Outside the statement under check (section 6). Not checked. No verdict.
- Section 0, GAP (line 28). It says the closures C1-C8 are unrefereed and that the interacting use of the free symmetry action remains open. My check covers C1-C8 as formal statements and finds them right; it does not touch the interacting use, which I list as excluded (C4 Remark hypothesis). Agrees.
- Section 0, GAP: "MT1-S alone gives spin 1/2 under ER, but does not identify ER with the physical long-distance rotation group." Agrees with my scope: Theorem 9 is checked as a formal implication only.
- Section 0, Amendments 1 to 3 (lines 7-22). They concern `LZ1.md`, `RCS1.md` and a prior-work digest, none of which is in the folder. Each says "No proved result of this file changes". I found no included result that depends on them. Not checked.
- Section 0, Amendment 1, third bullet says `LZ1.md` Theorem 5.2 gives an antiunitary symmetry of the dressed L5-O[S_+] tick for all constants. Section 6.2 A1 (line 157) says "no antiunitary symmetry of the dressed tick is known" on L5-O. These two sentences of the unchecked sections disagree with each other. Neither is in the statement under check. C6's last sentence (line 240) only says the C6 argument does not apply to L5-O, which is consistent with both.
- Section 0, Provenance (line 31). The draft's checks in `/tmp/toe-mt1/check/` were unavailable to the authors' session. I did not use them; all computations here are my own.
- Section 6.2, A1 (line 157): "On L5-U at mu=0=tau_E, rotations, inversion, Theta and sigma are symmetries of the dressed tick, and their free node forms allow only the free direction (C4-C6)". Agrees with C4, C5, C6 and line 141 as I checked them. "Where sigma is absent (tau_E != 0), the route fails at Theorem 10": consistent with the dimension 3 I found for (R, I, Theta).
- Section 6.2, A2 (line 158): "Even an arbitrarily small perturbation need not preserve the Clifford condition, by Theorem 10". Agrees with Theorem 10 as checked. The C7 statement about L5-O agrees with C7(d).
- Section 6.1 and the rest of 6.2: readings and open statements. Not checked.

### Verification owed

- Theorem 1: repository compute check (tori L=2,4,6, all 24 rotations; control: a gauge with one flipped site sign fails commutation). A Lean certificate is possible for the finite L=2 cell but the compute check is the better fit.
- Theorem 2: Lean certificate (pure CAR algebra identity); a compute check on a 4-site Fock space with the boson control is the cheaper alternative. I would choose Lean.
- Theorem 3 and C2: neither in full. The statement is structural (Klein and Jordan-Wigner). A compute check exists only on a reduced analog (as in `check_T3_C2_analog.py`); a Lean proof of the general graded-tensor statement would be the real test.
- Negative statement at line 76: Lean (two lines).
- Theorem 4: compute check (exact integer or Gaussian-integer arithmetic on 8x8 matrices plus Bloch projection on a torus; control: sign of the sin term).
- Theorem 5 and remarks: compute check on tori for the one-body clauses (control: parallel half-turns commute); the flavour clause is a short Lean lemma (scalar commutator, determinant on C^5).
- Theorem 6 and C8: Lean or hand for L_cube and U (parity bookkeeping); compute check for the Majorana products on one link (1024 dimensions; control: the odd sector S_- gives +1).
- Theorem 7 and the Correction: compute check (series of i log V at small K with the G_j versus Gamma_j control); the algebraic identity {R, Gamma_j}=0 could be a Lean lemma.
- Theorem 8: compute check (finite group, 8x8 matrices, commutant dimensions; control: drop one generator and the commutant grows).
- Theorem 9: Lean certificate for the commutator identity in the Weyl algebra tensor a Clifford algebra; the sympy check with the non-Clifford control is the compute alternative. I would choose the compute check first.
- Corollary 9.1: compute check for clauses 2 and 3; clause 4 is a short group-theory proof, Lean possible.
- Theorem 10 and C4: compute check (rank of the real-linear system; witnesses; control: unconjugated Gamma_j). Exact rational arithmetic is possible after conjugating by U*, since the conditions then have Gaussian-integer coefficients.
- Paragraph after Theorem 10, C3: compute check on tori (control: sigma-hat(0) not proportional to chi).
- C1: compute check (as run; control m=0,10).
- C5, C6: compute check of the free analogs on a torus; the dressed statements would need a small dressed instance (one cube with links) which I did not build. Neither Lean nor compute is cheap for the full dressed statement.
- C7: compute check on the L=4 torus for (b)-(d) (control: count of commuting lifts is 3, not 24); (a) is a hand sign computation, Lean possible.

## Not run

- `LW1_5.md` is not in the folder. I did not read it and could not confirm the quotations at MT1 lines 171, 231-232, 250, 256 and 264, or the definitions that section 1 says to take from it. Results that touch five-mode content were closed from VC1_5 section 1 item 1, VC1_5 section 2 and Theorem 2.2, and the definitions given inside the results themselves. If `LW1_5.md` defines the link operators, the centre omega_x or the dressed lifts differently from those restatements, Theorems 3, 5 (dressed clause), 6 (O clause) and C1, C2, C5, C7(a), C8 would need to be rechecked against it.
- `MT1_REFEREE.md`, `check_witness.py`, the draft and its `/tmp/toe-mt1/check/` scripts: not in the folder, not read.
- Not read: `LW1.md` section 0, section 3.2 beyond line 247, sections 3.3, 3.5 and 4; `ZM1.md` beyond its headings and citation lines; `VC1_5.md` section 0 and sections 3 to 9; most of `WORKING_SET.md` (read: the table rows for PS-5 and PS-6r, sections 3.4 and 3.5); `MINIMAL_AXIOMS_2026-06-29.md` beyond its first 2 KB. No checked proof step cites the unread parts.
- Section 6 of MT1 (Theorem 11, readings M1-M3, attacks A1-A3): outside the statement; read only for the comparison above.
- No full instance of Theorem 3 or C2 (280 modes at L=2). No dressed-gate instance for Theorem 5 (dressed clause), the dressed sigma of line 141, C5 or C6; these were closed by hand.
- Infinite-lattice statements were tested on tori L=2,4,6 only and otherwise rest on LW1 A2 and B10 as given. C7 was computed at L=4 only.
- Theorem 7's "only node" claim: closed from LW1 B10 item 1; my 13^3 grid scan is a sanity test.
- Theorem 10 "all sufficiently small nonzero u": closed by the first-order term; computed at four values of u.
- The first run of `check_T2_C1.py` used dense matrices, exceeded the time budget and was stopped; the saved script is the sparse rewrite, which runs in about one second.
- No network, no git, no file outside the folder.
