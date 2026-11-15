---
statement: LW1-text
commit: 70ef4aaf655005045d240bb86d54cf47aaa5f28c
content: d911cfea0e4c17ed13b1de2a8e858417b0042b28d68762f2d66526d76dad2575
text:
  - ead33ee916faeae0038cd4a67492b30b7db98a44e402a9de1c22282b76bc3d9c .claude/science/physics-loops/toe-assembly-20261104/LW1.md#1. Definitions
  - 2485dc1f464b4652855270785014e0d340f8f28e9aa90a1a2d607a4082bc2816 .claude/science/physics-loops/toe-assembly-20261104/LW1.md#2. Statement of \(L_{\rm cube}\)
  - 26d0e19dba6d7f246c0b8e1f605276153c3127f842c5733f7098b3652bbd4ce6 .claude/science/physics-loops/toe-assembly-20261104/LW1.md#3. Theorems and proofs
reads:
  - 65bec1c250e422913cb86dac6c5f3ea6daca0b9a0db11f733f7d39d2cf089956 - .claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md#3. Proposed axiom update (working set)
verdict: right
failure: none
path: Each result re-derived by hand along a different argument where one exists; the finite ones tested on the checker's own exact or floating-point instances with controls that fail, written from the statements and not from the proofs (eight scripts, see the dispatch note).
checker: anthropic/claude-fable-5-2/medium 57845b86-f838-4517-b116-4f9736df6046/check-LW1
author: anthropic/claude-opus-5-5/unreported 5a2a0affe1
answers: none
steer: none
---
## Finding

**Dispatch note, written by the session that dispatched the check, not by the checker.**

- Statement: every result that `LW1.md` section 3 states as proved follows, as written, from its hypotheses, the definitions of sections 1 and 2, and the working premises of `TOE_ASSEMBLY.md` section 3. The premises were taken as given. Items that section 3 itself marks open or unproved are excluded and listed below.
- Independence, stated plainly. The text of sections 1 to 3 was distilled by Codex (`gpt-6-astra`, high) and last edited by a Claude Opus 5.5 lead session (commit `5a2a0affe1`). The checker is a fresh Claude Fable 5.2 session at medium effort: a different model from both, in a separate context, with three files only (`LW1.md`, the section 3 premises, the axioms memo). It is from the same provider as the last editor, because no third provider is available. It read the authors' status section and section 4 only after its table was written.
- What it read as the axioms. The memo from `origin/main` at `7fc6b1a3e6` (lines 1 to 80), which says "neighborhood" where this branch's copy still says "nearest-neighbor" (the wording changed on `main` on 2026-11-08). The checker reports that no proof in section 3 quotes the axioms, so the memo is not in `reads`.
- Its computations. Eight scripts with their outputs are in `check-evidence/LW1-text-70ef4aaf6550/`. The dispatching session reran all eight on 2026-11-13; each output was identical to the checker's. They are the checker's scratch evidence. They are not repository runners, and the "Verification owed" list below says which results still need one, or a Lean certificate.
- This is one check of one text. It is not an audit. It says nothing about whether the working premises are true, and the LW1 target itself stays open (`parts/LW1.md`).

### Claim list

All are formal implications from the section-1 definitions and the working premises. None asserts a physical identification beyond the definitions (the joint Born identification and the record-memory reading are taken as definitions 26 and 25).

1. **Lemma A1** (l.186). Every positive edge lies in exactly one cube of exactly one tiling; every unit face has sign product -1; R_e^2 = R_o^2 = I. Hyp: definitions of eta_i, tilings.
2. **Lemma A1a** (l.190). Each free half-tick is an exact finite product of nearest-neighbour (edge) gate layers, the same in every cube. Hyp: none beyond definitions.
3. **Dressed factorization** (l.196). Each dressed cube gate exp(-i theta H_C) is an exact finite word in even, gauge-invariant single-edge-triple gates exp(t X_j); so U_0 has finite depth. Hyp: finite S, any angle.
4. **UALL remark** (l.207, labelled GAP against the draft, but stated with a proof). Even edge-triple operators do not generate all even cube operators as a Lie algebra (trace-with-parity obstruction).
5. **Theorem A2** (l.209). Among orientation-preserving lattice isometries, those preserving V up to site phases are exactly G = 2Z^3 x| O_{c0}; even translations exact; cube-centred rotations fix each half-tick up to one common sign gauge; transitive on sites, site stabilizer of order 3; at mu = 0 the shift by (1,1,1) with D_s and a sign gauge exchanges the half-steps. Hyp: 0 <= mu < 2 eps < pi.
6. **Theorem A3** (l.219). Event set = equal-parity vectors of Z^4 = 2 D4^*, similar to D4; 16 + 8 shortest vectors; time axis parallel to 2e_4. Hyp: c Delta = a, two-sided h.
7. **Theorem B2** (l.233). Finite-range translation-commuting unitary on l^2(Z^d) is phase times translation; with rotation covariance up to diagonal conjugation (no common fixed vector) it is a scalar.
8. **Lemma B3** (l.237). One-site CAR automorphisms fixing all other modes: c_x -> u c_x or v c_x^dagger, |.|=1; group U(1) x| Z_2; number-preserving part U(1). Hyp: at least one other mode exists (true on Z^3).
9. **Theorem B4** (l.241). Dressed edge terms, cube gates, electric gates and oriented plaquette monomials commute with every G_x; U_0 fixes every local gauge transformation.
10. **Gauged covariance / B1, B1q** (l.245). U_0 is cell covariant (with link reversal by exp(-i pi S^x) and A2's sign gauge), transitive on sites, locally unitary, finite nearest-neighbour depth, one-site algebra M_2(C); same for W_B if that layer is cell covariant.
11. **Theorem B5(a)** (l.249). Site-local number-preserving one-body frames on one-mode sites have abelian image in a product of U(1)'s.
12. **Lemma B6** (l.259). For finite-dimensional unitary W, any orthogonal resolution of identity, any density matrix: a coupling of p, p' supported on nonzero blocks exists.
13. **Theorem B7** (l.272). On a finite union of active cubes / an even torus the least-cost then greatest-entropy coupling exists and is unique; its kernel carries p to p' on allowed blocks.
14. **Support factorization** (l.276). Half-layer support is the product of cube supports; a region's output Born marginal depends only on its reduced state and internal gates; a later link-only unitary changes neither support nor matter marginal.
15. **Theorem B8** (l.282). In a number-invariant quasi-free state, omega(D_xy)=0 iff G_xy=0 and (G_xx,G_yy) in {(0,0),(1,1)}.
16. **Corollary B8a** (l.295). Free tick from the free sea: every F_n is empty. Hyp: free tick, PS-3c, B10.
17. **Theorem B8b** (l.299). (i) empty matter on the side-7 cube about x at tick 0 gives probability-one empty occupations at x and its six neighbours at tick 1; (ii) some supplied initial state gives a tick-one record at x with value odds 1/2. Hyp: base law U_0, PS-3c, PS-4, one-time marginals nu_h.
18. **Theorem B9, established clauses** (l.310). Locked value law equals the copy neighbour's one-site Born law at the formation tick; same for all copy neighbours; differs between all-empty and all-full states; copy test equivariant; records single, permanent, of positive Born weight a.s. Hyp: PS-3c, definition 25, marginals nu_h.
19. **Theorem B10** (l.322). (1) fibre eigenvalues exp(+-i w), cos w = a chi - b, mu <= w <= 2 eps, multiplicity 4+4; (2) Theta P Theta^-1 = I - P, P_xx = 1/2; (3) omega_P pure, stationary, G-invariant, half filled; (4) exponential decay of P_xy for mu > 0.
20. **Theorem B11** (l.360). No atomless history law has a history meeting all probability-one statements; free-sea and tracial Born measures are atomless; the PS-11c list is countable and consistent with any history law.
21. **Theorem C1** (l.371). mu = 0 small-k expansion of w with coefficient s^2/72 - T4/24; site-momentum form -T4 |q|^2/6.
22. **Theorem B12, proved part** (l.391). A slice-preserving orthogonal symmetry keeps the time line; oriented stabilizer in the event lattice has 48 elements (line stabilizer 96); W(F4) is not a symmetry of the ordered data.
23. **Theorem E1** (l.401). Base layers and the tick are automorphisms of the quasi-local algebra fixing every exp(it G_x); same for a finite-depth gauge-invariant plaquette layer with commuting sublayers.
24. **Theorem E2a** (l.411). mu > 0: free sea pure, stationary, cell symmetric, half filled, exponential decay. mu = 0: same state properties and |P_xy| <= C/(1+|x-y|).
25. **Theorem E2b** (l.421). Cesaro limit points of a cell-invariant, gauge-invariant, half-filled (cell average) state are stationary with the same properties; such states exist (tracial state); for U_0, and for link-only cell-covariant gauge-invariant finite-circuit W_B.
26. **Theorem E3** (l.438). F_n, R_n, t_x well defined for every initial state, deterministic in the state sequence, increasing, covariant.
27. **Theorem E4** (l.442). Every state and half-step admit a coupling of input/output Born measures obeying all cube supports a.s.; cell-invariant if the state is.
28. **Theorem E5** (l.450). A Markov history measure with marginals nu_h and supported steps exists for every omega_0; records single, permanent, admissible a.s., none at tick zero; steps may be taken in O_h for cell-invariant sequences.
29. **Theorem E6** (l.458). For a cell-invariant input state O_h is nonempty, compact, convex.

### Per-result table

label | verdict | failing step or counterexample | my different path | not checked
---|---|---|---|---
A1 | right | none | brute enumeration on the L=6 torus of ownership, all face products, R^2 (`check_A1_A2_B10_C1.py`); hand recomputation of eta shifts | L odd tori (not in domain)
A1a | right | none | hand: the listed corner order is a Hamiltonian path of the cube (checked each step), adjacent-row Givens QR is standard; Gamma multiplicative | no numerical factorization run
Dressed factorization | right | none | hand re-derivation (group generated by one-parameter subgroups is the analytic subgroup of the generated Lie algebra; checked the Ad-invariant span step and the submersion step); instance test by a different implementation: direct least-squares for a fixed alternating word on a 3-site, 2-link chain, S=1/2 and S=1, exact to 1e-15 at length 6 while Trotter of equal length is off by 1e-2..1e-1 (`check_dressed_factorization.py`) | full cube (12 edges, 2^8 (2S+1)^12 dims) not computed; word length for the cube not bounded
UALL remark | right | none | 3-mode instance: Lie closure of all even pair generators has real dimension 31 of 32 and misses iP; tr(PX)=0 on the closure (`check_B4_gauge_UALL.py`) | only the fermion-pair instance (no link factor)
A2 | right | none | L=6 torus: all 24 rotations about c0 fix BOTH R_e and R_o with one BFS sign gauge; all 168 classes with an odd translation fail the modulus test |V| (necessary condition); stabilizer 3, orbit 8; mu=0 exchange verified exactly and fails at mu=0.3 (control) | only one (eps,mu) for the exclusion; exclusion proof by hand uses sin a_e sin a_o > 0 on the whole window
A3 | right | none | enumeration in a box: events from the cube-centre definition = equal-parity vectors = 2 D4^*; 24 shortest vectors (16+8); Phi and its inverse exact with `fractions` (`check_A3_B12.py`) | none
B2 | right | none | different derivation: in one variable a Laurent polynomial unimodular on the circle is z^m times a polynomial that is a pole-free finite Blaschke product, hence a monomial; induct on variables with the others fixed on the torus; rotation step by support displacement | no script
B3 | right | none | linear-algebra kernel of the anticommutation constraint on span{I,n,c,c^dag} has dimension 2; CAR tested on instances (`check_B4_gauge_UALL.py`) | statement needs a second mode to exist; true on Z^3 (remark, not a defect)
B4 | right | none | dense matrices on a face (4 sites, 4 links), S=1/2 and 1: [G_v, edge terms], [G_v, exp(-iaH)], [G_v, W_E], [G_v, J_p] all zero; controls with wrong orientation are nonzero; [E,J]=J for S up to 5/2 | full cube; S >= 3/2 on the face (algebra is S-independent)
Gauged covariance | right | none | exp(-i pi S^x) sends E to -E and J to J^dag for S=1/2..5/2; reversed-link hop term identity checked; sign gauge from A2 check; hand check of image-cube Hamiltonian | no full gauged cube rotation computed
B5(a) | right | none | immediate: U(1) is the unitary group of a one-dimensional space | none
B6 | right | none | LP feasibility (HiGHS) on 300 random block-sparse unitaries with rank>1 projectors and low-rank states: 300/300 feasible, 207 with forbidden blocks; control with a non-Born output marginal infeasible 100/100 (`check_B6_B7_B8_B11.py`) | none
B7 | right | none | hand: strict concavity of entropy on a compact convex face; instance: entropy maximiser on the min-cost face identical from 4 starts (`check_B7_unique.py`) | first SLSQP attempt in `check_B6_B7_B8_B11.out` did not converge (my optimiser, spread 8e-3); superseded by `check_B7_unique.py`
Support factorization | right | none | 4-mode instance with two disjoint gates, one with zero blocks: support of product equals product of supports; hand check of the Jordan-Wigner tensor form for even block operators | link-only layer step by hand only
B8 | right | none | explicit Fock-space quasi-free density matrices on 4 modes (200 random G incl. projections and decoupled cases): formula and iff both hold | none
B8a | right | none | P_xx = 1/2 computed three ways (torus spectral projector, Bloch integral for mu=0 and mu>0, Theta symmetry) then B8 | relies on B10(3) stationarity at full ticks
B8b | right | none | (i) different argument: each layer conserves the cube number N_C, so ancestors within sup-distance 3 stay empty; one-body cone check for all 8 residues of x: zero amplitude from distance >= 4, nonzero from distance 3 (`check_B8b_cone.py`); empty-matter subspace fixed by dressed gate on a face. (ii) by hand: state is even, alpha^-1 exists by E1, x in F_1 | (ii) not computed
B9 clauses | right | none | by hand from definitions of F_n, t_x, r_x; read with n = t_x (the tick at which the record forms) | reading where "a formation time" means a later n with x in F_n again: then the display need not hold; PS-3c lets a record form only once, so I take n = t_x
B10 | right | none | torus L=6 spectrum against the formula to 1e-15 for four (eps,mu) incl. window ends; 2000 random fibres; anticommutator identity exact; Theta V Theta^-1 = V exact; P_xx = 1/2; decay table for mu=0.6 (`check_A1_A2_B10_C1.py`, `check_E2a_decay.py`); hand check of a_band, b_band by product-to-sum | (4) only observed numerically plus the standard Combes-Thomas argument re-read; purity criterion taken from the cited theorem
B11 | right | none | det G_F and Hadamard bound verified on Fock space instances; countability and measurability by hand | none
C1 | right | none | sympy series of arccos(1 - s^2(1-chi)) equals the stated polynomial; numerical fibre eigenvalues: relative error scales as k^4 (ratio 16.0) for 12 (eps, direction) pairs; control T4/23 gives ratio 4 | none
B12 proved part | right | none | enumerated all 1152 orthogonal automorphisms of the event lattice: oriented stabilizer 48, line stabilizer 96, exactly the 96 line-keeping ones preserve slices (`check_A3_B12.py`) | "symmetry of an ordered PS-1 update" is read as an orthogonal map of the event lattice
E1 | right | none | by hand: well-definedness, inverse and gauge-fixing re-derived; commuting-gate hypothesis is in the statement | none computed
E2a | right | none | closed formula for P(K) equals spectral projector (1e-15); |K| * ||dP|| -> 0.5 near zero; Bloch-integral table: |P_xy|(1+r) bounded and decreasing at mu=0 | constant C not computed; grid N=40 only
E2b | right | none | by hand: Cesaro bound, commutation of symmetries with alpha, N_C conservation ([N,H]=0 on the face instance), residue counting for translated cubes, tracial witness | no numerical instance
E3 | right | none | by hand from definitions | none computed
E4 | right | none | by hand: local marginal identity, compactness, cylinder events, Folner averaging; B6 instance tests cover the finite step, also for non-even and low-rank states | no infinite-volume instance (not computable)
E5 | right | none | by hand: disintegration, Ionescu-Tulcea, induction on marginals | none computed
E6 | right | none | by hand: closedness of constraints, subadditivity along dyadic boxes, affinity via mixture label, usc + compactness | none computed

### Excluded

- **B5(b)** (l.253): stated as "retained as an unproved draft statement"; GAP B5(b) (l.255) says it is false under its hypotheses. Excluded as unproved. Remark: the GAP's counterexample (eight site phases compensated on incident links) does satisfy the hypothesis, by B4.
- **GAP LW1-i/B9** (l.318): shell-only Admissibility, marked GAP/open. Excluded. Remark: the two extensions given do have equal shell marginals, both pass the two-copy test, and give centre odds 1/3 and 2/3.
- **GAP B12(ii-iii)** (l.395): transfer-kernel and fermion positivity assertions, marked GAP. Excluded.
- **Plaquette class / W_B**: unspecified law data. Statements about W_B appear only as conditional clauses inside the gauged-covariance paragraph, E1 and E2b; those implications are checked with their hypotheses, the existence of an admissible W_B is not claimed and is excluded.
- **Law-choice paragraph** (l.397): a selection, not a theorem; it says it asserts no classification. Excluded.
- The label "GAP: UALL" (l.207) is a negative result with a proof; I checked it as a result (row "UALL remark") instead of excluding it.

### Against sections 0 and 4

Read only after the table above was written. No verdict was changed.

- Section 0 "Proved here" lists A2, A3, B2, B3, B5(a), B4, the gate factorization, B6-B7, B8 and witnesses, record permanence, B10, B11, C1, E1-E6. **Agree**, item by item: each is `right` in my table. Section 0 does not name A1, A1a, the support factorization, B8a or the proved part of B12 in that list; I checked them and found them right as well.
- Section 0 says claims about an unspecified plaquette update are conditional. **Agree**; I checked them only as implications.
- Section 0 "Open by name" and section 4 mark B5(b), LW1-i/B9, B12(ii-iii), LW1-U, LW1-N, LW1-ii/F, LW1-R, GA1-P, VC1 as open. **Agree** that section 3 proves none of these; none is in my included list. LW1-U, LW1-N, LW1-ii/F, LW1-R, VC1 are stated only in sections 2 and 4, not as section-3 results.
- Section 0 reports a referee count ("92 items, 85 correct, 3 errors and 4 incomplete ... edits applied"). Not evidence; I did not see the referee file. I found no remaining error in section 3.
- Section 4 "LW1-edge (CLOSED)": **agree** (row "Dressed factorization"). Section 4 on UALL: **agree** (row "UALL remark").
- Section 4, E6 "Attack 1" (specific entropy is affine, so strict concavity is lost at infinite volume): **agree**, this is E6's own affinity step.
- Section 4, GA1-P commutator [B_p,B_q] = 2 E_l (A B^dag - A^dag B): recomputed by hand from [J,J^dag] = 2E; **agree**. Outside the statement under check.
- Section 4, LW1-R: tracial state gives rho_n(D_xy) = 1/2 and no record; free sea forms none by B8a. **Agree** (fair independent bits; B8a row).
- Section 4, LW1-ii/F: the closed-box identity is said to fail with leaving probability "sin^2(a_o/sqrt3) > 0". The qualitative claim (a particle can leave Lambda in the larger box, so the identity fails) I **agree** with. The printed value I do **not** confirm: for the free cube gate, R_C^2 = I gives exp(i a_o R_C) = cos a_o + i sin a_o R_C, so one particle leaves its site with probability sin^2 a_o, one third to each cube neighbour; the dressed value also depends on the link state. This is in an item section 4 marks GAP, outside the statement under check, and positivity is all that the argument uses. Recorded as a remark only.
- Section 0 amendments 1-3 (Admissibility under PS-Ar, B5B.md, LW1U_SEA.md) cite files outside this folder. Not checked. They say no proved result of section 3 changes; consistent with what I found.
- One reading note that sections 0 and 4 do not raise: B9's display is right when n is the tick at which the record at x forms (n = t_x). The statement's words "a formation time" do not bind n explicitly. Under PS-3c a record forms once, so I read n = t_x. A consumer should cite it that way.
- B3 needs at least one other mode (on a single isolated mode the automorphism group of M_2(C) is larger). On Z^3 this always holds. Not a defect of the statement as posed on the lattice.

### Verification owed

- A1, A2 (inclusion, exclusion by moduli, stabilizer, mu=0 exchange), B10(1)-(2), the anticommutator identity: repository compute check on an even torus with a control (odd translation; mu > 0 for the exchange). A Lean certificate is feasible for A1 (finite parity facts) and I would choose Lean for A1, compute for A2 and B10(1)-(2).
- A1a: Lean (Givens QR along a Hamiltonian path) or a compute check that factors a random 8x8 unitary; choose compute.
- Dressed factorization: Lean in principle (Lie theory: subgroup generated by one-parameter subgroups); a compute check can only test instances (as in `check_dressed_factorization.py`, control: Trotter word). Choose Lean for the general statement; compute for instances.
- UALL remark: compute check (Lie-closure dimension, control: add iP) or Lean (trace functional argument); choose Lean, it is three lines.
- A3, B12 proved part: compute check by enumeration (control: an automorphism moving e_4); Lean also feasible; choose compute.
- B2, B3, B5(a): Lean. B2 is a clean Laurent-polynomial statement; B3 is finite algebra.
- B4, gauged covariance, support factorization: compute check on face/edge instances for several S with orientation controls; choose compute. Lean feasible for B4 (commutator algebra).
- B6: Lean (max-flow/Hall) or compute by LP with a non-Born control; choose compute. B7: Lean (strict concavity on a compact convex set); compute only tests instances.
- B8, B11 determinant bound: compute check on Fock instances (control: G with G_xy != 0); Lean feasible for B8 given Wick.
- B8a: follows from B8 and B10; compute check of P_xx.
- B8b(i): compute check of the cone (control: distance 3); B8b(ii), B9, E3: neither (definition chasing); Lean possible but low value.
- B10(3): neither for purity (cited theorem); B10(4), E2a: neither as proofs; a compute check can display decay but cannot certify a constant.
- B11 (atomless/countable consistency): Lean.
- C1: compute check (series by computer algebra, control with a perturbed coefficient) ; choose compute.
- E1, E2b, E4, E5, E6: neither for a compute check (infinite volume); Lean is the only certificate kind and is a large job (quasi-local algebra, Prokhorov, Ionescu-Tulcea).

## Not run

- Did not read any file outside this folder; did not use git or the network. `LW1_DRAFT.md`, `LW1_REFEREE.md`, `TOE_ASSEMBLY.md`, `B5B.md`, `LW1U_*.md`, GA1-P files: not available, not read.
- `MINIMAL_AXIOMS_2026-06-29.md`: read lines 1-80 (the four axioms); the remaining lines not read. No section-3 proof quotes them.
- No computation on a full dressed cube (8 sites, 12 links); gauge and number checks were on a face and on a 3-site chain, S = 1/2 and 1 (link algebra alone up to S = 5/2).
- Dressed factorization: no word computed for the cube; no bound on word length.
- B10(4) and E2a: no certified constants; decay shown on an N=40 midpoint Bloch grid only.
- B10(3) purity criterion (Powers-Stormer/Araki) and the analytic subgroup theorem, Prokhorov, disintegration, Ionescu-Tulcea, Kolmogorov: used as standard theorems, not re-proved.
- E1-E6: hand re-derivation only.
- B9 under the alternative reading (n a later tick with x in F_n): no counterexample constructed, no proof either.
- Section 4's closed-box leaving probability: not computed for the dressed gate.
- The first B7 instance in `check_B6_B7_B8_B11.out` shows a non-converged optimiser of mine; `check_B7_unique.out` is the valid run.
- Files written: `check_A1_A2_B10_C1.py`, `check_A3_B12.py`, `check_B4_gauge_UALL.py`, `check_dressed_factorization.py`, `check_B6_B7_B8_B11.py`, `check_B7_unique.py`, `check_E2a_decay.py`, `check_B8b_cone.py`, each with its `.out`.
