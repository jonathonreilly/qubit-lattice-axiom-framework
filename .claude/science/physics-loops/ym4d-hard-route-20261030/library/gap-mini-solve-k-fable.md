lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T13:41Z

# gap-mini-solve-k-fable: attack on the four-dimensional SU(2) mass gap

Queue row 1201. Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit 20239923e.
This is research-stage working state. It grants no status and is not a public claim.

Labels used below: PROVED (every step written here or in a cited checked note), ARGUED (argument given, a step is not written out or not checked), GUIDE (numerics or heuristics, never a proof step), OPEN.

## 0. Plan (written first, before any reading of earlier attempts)

1. Repo search: read the RESULT lines of the earlier `gap-*` rows in FINISH.md, `parts/gap.md`, `library/open-core.md`, and the earlier `gap-mini-solve-*` notes, so that this run does not repeat an attack.
2. Choose one route that the earlier runs did not take, or the first unproved step of the best earlier route.
3. Attack it, one step per response, and append each step here.

## 1. Repo search (done 2026-11-20T02:10Z)

Read in full: `FINISH.md` L1-84 and L299-356 (rules), row 1201 (this item), rows 1188-1211 (the plain-brief rows a-f, their checks, the gpt-6.2-astra chain rows 1192, 1204, the two Argon rows and checks); `GOAL.md`; `parts/gap.md` L1-322 (state of attack, obligations, route registry, test table, price); `library/gap-crux-restate.md` Sections 1, 2 and 3.4 (DEF, candidates C1-C5, Theorem S). `library/open-core.md` holds the existence chain only; it has no entry for the gap lane (headings read, grep for N-phys empty).

Where the lane stands, in my words (GUIDE, a reading; every item is cited to its row in `parts/gap.md`):

- Engine (Theorem S, row 697, checked rows 698-699): on periodic tori, one inequality S(n; (2n)^3) < 1/5041 at one size gives a uniform gap on all larger cubes. It holds for every group. The whole open content is the seed at a physical size, uniformly in the cutoff: (W), equivalently (PHYS-SEED); in the later split, (N-phys) (centre-neutral excited trace at most 1/2 at aspect K = 512) plus the branch selection (BS), plus the continuum datum of the T0 chain.
- Every route on file ends at one order-one inequality in the band beta 2.3-2.6 that must be selective: false for compact U(1), for a product with a massless factor, for frozen Z_2 (periodic form), for a peaked weight w_p at its transition.
- Routes on file with their first failing step: contraction of the Casimir energy (RA), sign in beta (RB), one-scale number (RC), sector engines (RE), functional inequalities and log-Sobolev (RF, LC), hierarchical comparison (RG), the anisotropic bridge BR-2 with (SING), the pinned short step (T-pin), the Dobrushin-Shlosman hypothesis (DS-W), the slab extraction (A), ports of the posted 2D O(N) proofs (rows 1007-1050, 1188, 1193), aligned and Coulomb frames (route (ii)), vortex containers and Tomboulis-Kanazawa decimation, Lee-Yang and zero transport (Route Z), surface expansions with signs (method 35), swap criteria in law (method 34), the weak-coupling end and the electric strip (rows 1143-1175).
- The six plain-brief Fable rows a-f screened 12 + 17 + 10 + 7 + 5 candidate routes and found each on the map.

Consequence for this run: a seventh screening has no value. This run picks one mechanism and works on it.

## 2. Choice of attack (written 2026-11-20T02:20Z)

### 2.1 What a proof must contain (reading of the record; ARGUED there, cited)

1. The Jaffe-Witten gap clause reads one lattice premise, the neutral one-cube bound (N-phys), plus the continuum datum (row 1179 Theorem BP; row 1161; check 1183). The flux half (BS) is on the path of (W) only.
2. In pure gauge theory every stiffness, twist or frame mechanism on file acts on the flux half: the bracket of the posted 2D O(4) proof gives the charged half, and the neutral half there comes from association (row 1193, citing rows 1009, 1076-1086). The gauge port of association failed three ways (row 1084); the eight plaquette monomials have a sign pattern that no phase shift removes (row 1190 2.1).
3. So the missing object is a mechanism for neutral mixing at order-one coupling that reads the group. The record names it (SING) in two dimensions and (N-phys) in four.

### 2.2 Candidates generated in this run, each grepped before any work (rule 0a)

| # | Candidate | On file as | Verdict |
|---|---|---|---|
| 1 | Port of the 2D stiffness iteration with a colour frame | rows 1007-1050, 1188, 1193 (Propositions B, B', Theorem BH, Lemma PC, route (ii)) | found again |
| 2 | The time-independent gauge group as rigid group in temporal gauge | row 1016 QL1, HAM1; row 1190 item 2 | found again: its response is the static-charge (Polyakov) family, blind |
| 3 | Durhuus-Frohlich layers with the posted O(4) theorem | rows 712, 819, 825; method 36 (two-sided backgrounds order the layer at large b) | found again |
| 4 | Small-volume (toron) gap carried by a monotone step-scaling function | row 859 items 8, 36; rows 1143, 1008; route RA | found again: no step that excludes a zero of the step-scaling function |
| 5 | Hellmann-Feynman in beta with a bound on the action excess of the lightest state | row 859 item 46 and G8, (NOCRIT-HF); route RB | found again |
| 6 | Trace anomaly: scale derivative of D equals the finite-size plaquette shift | (MONO-Delta), `gap-phys-seed.md` L351; Proposition VIR; route RB | found again |
| 7 | Bakry-Emery on the orbit space (Singer's curvature) | method 31; rows 957, 968; Proposition G1 of row 1128 | found again |
| 8 | Three-dimensional compact U(1) (Gopfert and Mack) as a template or test | row 859 item 34; exercise 2 I20, (m2) | found again |
| 9 | Griffiths-type positivity for products of characters | (EP) false, Theorem EP-NO of row 754; method 35 | found again |
| 10 | A neutral soft mode needs a first-order-like structure; the Wilson axis is near a first-order end point | Proposition V, K7, (NO-1ST) of row 1109 | found again |
| 11 | The spacetime symmetry group of the box as the rigid non-abelian group: every glueball state except a scalar at rest is charged under it | sheared tori and Lemma SHIFT (row 962 A4, 7.4); rotated tori (row 963); "shape twists" in row 1190 item 3 (one line, "found again") | in part: the identities are on file; the question "does the bracket of this group give a gain" is not answered on file |

Candidate 11 is the only one with an unanswered question. Section 3 answers it.

A failed step of my own, kept as a negative result (ARGUED): I tried to get (MONO-Delta) for compact U(1) from Ginibre's inequality by "identifying periodic images". This is wrong. Identifying the sites of the kn-torus modulo n gives the n-torus at coupling k^4 beta, not at beta. So Ginibre compares different couplings and gives no sign for the finite-size plaquette shift. The record already holds that (MONO-Delta) fails for the ordered Ising model, which has Griffiths' inequalities (`gap-phys-seed.md` L367-373).

## 3. Candidate 11: the symmetry group of the box as the rigid group (written 2026-11-20T02:35Z)

**The idea.** In the 2D O(4) proof a rigid non-abelian group acts on the spins, the stiffness is a second-order twist response of the form "direct cost minus current covariance", and the bracket of the group lowers the stiffness at every scale (OpenAI (3.4)-(3.8), (3.50)-(3.54), as read in `library/prior/gap-o4-pinned-cell-read-opus.md`). Pure gauge theory has no rigid colour group on gauge-invariant data (Lemma CEN+ of row 1016). It does have one rigid non-abelian group that moves gauge-invariant data: the symmetry group of the lattice. Every glueball state except a scalar at rest is charged under it. Question: does a stiffness with a bracket gain exist for this group?

**Answer: no. First failing step: the direct term.** Details in 3.1-3.4.

### 3.1 Lemma G1 (sector identity; PROVED, elementary)

Setting: the periodic box B = Z_n^3, T its transfer operator on the gauge-invariant space H ((TM), `gap-crux-restate.md` Section 1). Let GG be the finite group generated by the translations of B and the 48 signed permutations of the axes. For g in GG let U_g act on functions of the spatial links by relabelling the links, with the link variable inverted where g reverses the direction of a link.

Statement. (a) U_g is unitary and commutes with T. (b) Z(g; t) := Tr(T^t U_g) is the Wilson partition function on the flat lattice obtained from Z x B by the identification (x_0 + t, x) ~ (x_0, g x). (c) With H = sum over irreducible rho of H_rho tensor V_rho and T = sum of T_rho tensor 1: Z(g; t) = sum over rho of chi_rho(g) Tr(T_rho^t), and Tr(T_rho^t) = |GG|^(-1) sum over g of conj(chi_rho(g)) Z(g; t). (d) |Z(g; t)| <= Z(1; t). (e) The GG-invariant excited sum is S_0(t) := Tr(T_triv^t)/lambda_0^t - 1 = |GG|^(-1) sum over g of Z(g; t)/lambda_0^t - 1, and the charged sum is S_ch(t) := S(t) - S_0(t) = |GG|^(-1) sum over g of (Z(1; t) - Z(g; t))/lambda_0^t.

Proof. (a) The map of link configurations is a bijection that preserves the product Haar measure (inversion preserves Haar measure) and the gauge group, and it maps plaquettes to plaquettes with the trace preserved (tr U^(-1) = tr U in SU(2)). T is built from the plaquette weights of one time step, so it commutes with U_g. (b) Insert U_g into the trace as a change of the identification of the last time slice with the first. (c) Schur orthogonality for the finite group GG. (d) T^t is positive and U_g is unitary and commutes with it, so |Tr(T^t U_g)| <= Tr(T^t). (e) is (c) for the trivial representation; the vacuum is GG-invariant because it is simple and positive (TM). QED

For translations alone this is the sheared-torus family of row 962 (Lemma SHIFT, 7.4). The signed permutations add the mapping tori of the cubic rotations. Nothing here reads the group SU(2).

### 3.2 What GG sees and what it does not (ARGUED)

- A state at rest with spin, and every state with momentum, is GG-charged. So S_ch(t) small at one physical size would bound all of these.
- The GG-invariant excited states are the zero-momentum scalars. In a small periodic box these are exactly the dangerous ones: the lowest excitations of SU(2) on a small torus are zero-momentum states of the constant modes, with size-times-gap of order g(L)^(2/3) (Luscher's small-volume result, recalled; the record's first-passage data, rows 1143, 1008). They have no momentum partners below 2 pi/L. So a bound on S_ch does not bound S_0. A vacuum degeneracy gives the same picture (the record's critical elements "log m", Proposition CONST of row 1028).
- In a large box a light scalar has light partners at momentum 2 pi/L by Lorentz covariance of the continuum datum. This is not a lattice theorem, and it needs the O(4) clause of T0, which is open.

### 3.3 The stiffness for GG: the first failing step (ARGUED; one exact remark)

1. Exact remark: GG is finite, so on the lattice there is no one-parameter twist and no second-order response. A twist by g costs F(g; t) := -log(Z(g; t)/Z(1; t)) >= 0, and by Lemma G1 (e) the mean of 1 - e^(-F) over GG is S_ch(t)/(1 + S(t)). So "small twist cost for all g" is the statement "small thermal weight of charged states". It is torus data of the kind Theorem S reads, not a new handle.
2. In the continuum, on a torus, the connected symmetry group is the group of translations. It is abelian. Rotations do not preserve the torus. So there is no bracket.
3. For a pinned cell, a displacement xi of the boundary data can be extended inside and removed by pulling back the field. The action then changes only through the metric, and a pure displacement gives a flat metric. So the free energy of a cell with displaced pins equals the free energy of the displaced cell with the old pins. The bulk response to a displacement vanishes identically. In the words of the 2D proof: the direct quadratic cost and the current covariance cancel in the bulk, because the current is the conserved stress tensor. What is left is a boundary quantity (the dependence on the shape, a Casimir term). For an internal group the direct cost is the bulk gradient energy b |grad u|^2 and it stays; that is the term the bracket then lowers.
4. So the only stiffness this group has is the shape dependence of the torus free energy, which is the record's D and route RA, or the scale derivative, which is the trace anomaly and route RB.

### 3.4 The comparison case (PROVED GIVEN the free-photon facts on file)

The free Maxwell field on the same tori has every identity of 3.1 and, in the continuum, every Ward identity of the Euclidean group and of the conformal group. Its torus data are scale invariant with S of order one at every size (test table of `parts/gap.md`, row "Free photon through the rate"; rows 975, 988). So no inequality of the form "D or S_ch contracts under doubling" can follow from the group structure of spacetime alone. A selective step would have to read the breaking of scale invariance, that is the sign and size of the finite-size plaquette shift. That is (MONO-Delta) and route RB.

**Verdict on candidate 11 (ARGUED).** Found again, with the reason now written: it is route RA in its identities and route RB in its only selective input. It gives no mechanism for the neutral half. Lemma G1 has no consumer.

Status of this file: step 4 in progress.
