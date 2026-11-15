**Proof tree, sketched (owner 2026-11-08: "do more physics on astra max for sketching the proof trees").** Written by Codex gpt-6-astra at max effort, read-only, on the laptop; finished 2026-11-08T20:39:22Z. Template `~/toe-lap/tmpl/treeZM1.txt`. A sketch: no node below is proved by this file, and nobody has checked it. Statuses quote the frozen parts.

# ZM1-I1[INV]: proof tree

## Z — The target theorem

> “Replace the full-algebra map by a unital injective *-homomorphism.”  
> [TOE_ASSEMBLY.md:252](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:252)

> “The other retained data stand: the VC1 fine vacuum, the admissible fine updates.”  
> [TOE_ASSEMBLY.md:253](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:253)

**Status: OPEN.**

**Children:** K-E or K-ODD, according to the fixed fine register; D for the same embedding. P-LOCK supplies a conditional shortcut. N-GAUSS through N-TOWER constrain possible constructions.

**Imported hypotheses:** H-LAW, H-CELL, H-TICK, H-VAC, R-form, ZM1-INV, ZM1-I1[a], PS-1c, PS-5, PS-6r, PS-7r.

The theorem is a proposition about fixed fine data. Choosing a convenient witness does not identify the VC1 vacuum.

> “The fine vacuum in the U statement is a VC1 vacuum; the O analogue is a separate proposed comparison.”  
> [ZM1_OBS.md:165](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1_OBS.md:165)

The root below is the U-law statement. K-O records the separate O analogue.

### Explicit hypotheses

**H-LAW.** Sites are \(x\in\mathbb Z^3\). Each site carries
\[
F_x=\Lambda\mathbb C^5,\qquad \operatorname{End}(F_x)\cong M_{32}(\mathbb C).
\]
Matter factors satisfy the CAR. Distinct link factors commute with matter and with each other.

Fix \(m\in\{1,\ldots,9\}\). Each nearest-neighbour link carries
\[
H_\ell=\Lambda^m(\mathbb C^5_x\oplus\mathbb C^5_y).
\]
The local gauge group is \(U(5)\). Its generators are
\[
\mathcal G_x(T)
=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x},
\qquad T=T^\dagger\in M_5(\mathbb C).
\]
Let \(\mathfrak A_m\) be the norm-completed quasi-local algebra. Define
\[
\mathfrak B_m=\mathfrak A_m^G
=\{A:\operatorname{Ad}(e^{i\theta\mathcal G_x(T)})(A)=A
\text{ for every }x,T,\theta\}.
\]
For a finite collection \(R\) of matter and link factors, put
\[
\mathfrak B_m(R)=\mathfrak A_m(R)\cap\mathfrak B_m.
\]
Gauge invariance is imposed at every endpoint touching \(R\), including exterior endpoints.

> “including outer link endpoints”  
> [ZM1INV.md:30](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:30)

**H-CELL.** The spatial group is
\[
\mathscr G=2\mathbb Z^3\rtimes O_{c_0},
\qquad c_0=(1/2,1/2,1/2),
\]
where \(O\) consists of determinant-one signed coordinate permutations.

Use the specified sign lifts. They carry link-end numbers to their geometric images. Arbitrary internal twists are excluded.

A coarse cell has eight sites. At scale \(L\), its fine block has \((2L)^3\) sites. Coarse translation by \(2b\) corresponds to fine translation by \(2Lb\).

> “an arbitrary internal automorphism is not included”  
> [KINV.md:18](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:18)

**H-TICK.** Fix the fine law before constructing the zoom. Its base update is
\[
U_0=W_EM_oM_e,
\]
where
\[
\begin{aligned}
H_C&=\frac1{\sqrt3}\sum_{\ell=(x,x+e_i)\subset C}\eta_i(x)h_\ell,\\
h_\ell&=\sum_{j,k}c^\dagger_{x+e_i,j}
r^{x+e_i}_j r^{x\dagger}_k c_{x,k}+\mathrm{h.c.},\\
M_e&=\prod_{C\in\mathcal T_e}e^{-i(\varepsilon-\mu/2)H_C},\\
M_o&=\prod_{C\in\mathcal T_o}e^{i(\varepsilon+\mu/2)H_C},\\
W_E&=\prod_\ell e^{-i\tau_E(p_{\ell,\mathrm{src}}-m/2)^2},
\end{aligned}
\]
with
\[
0\leq\mu<2\varepsilon<\pi,\qquad \tau_E\in\mathbb R,\qquad
\eta_i(x)=(-1)^{\sum_{j<i}x_j}.
\]
Here \(\mathcal T_e\) consists of cubes \(2u+\{0,1\}^3\). The odd tiling is its translate by \((1,1,1)\).

> “\(U_0=W_EM_oM_e\)”  
> [LW1_5.md:85](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LW1_5.md:85)

> “Put \(\eta_i(x)=(-1)^{\sum_{j<i}x_j}\)”  
> [LW1.md:59](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LW1.md:59)

A plaquette extension is allowed only when its finite gate formula and admissibility have been supplied separately. Its existence is not inferred from the desired comparison.

> “If supplied, its gate must be specified separately.”  
> [LW1_5.md:104](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LW1_5.md:104)

NN-a requires a fixed finite number of layers of even edge-triple unitaries. The complete update fixes the local gauge generators and commutes with the cell lifts.

> “Gauge invariance and cell covariance are required of the complete update only.”  
> [TOE_ASSEMBLY.md:235](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:235)

**H-VAC.** Fix the fine state \(\omega_0\) supplied by VC1. It is a normalized positive functional. It is stationary, locally gauge invariant, and invariant under the specified cell lifts. Any further selected VC1 reading remains attached to this datum.

No additional purity, gap, half-filling, or non-character hypothesis is inserted here.

> “Neither is adopted as an axiom or identified with F.”  
> [VC1_5.md:36](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/VC1_5.md:36)

### Conclusion to prove

There exist:

\[
L\in\mathbb N,\quad L\geq2,\qquad m_1\in\{1,\ldots,9\},
\]
a coarse law \(\alpha_1\) of the same five-mode U construction, a stationary coarse state \(\omega_1\), and
\[
\Phi:\mathfrak B_{m_1}\longrightarrow\mathfrak B_m
\]
such that the following hold.

1. **Algebra.** \(\Phi\) is a unital injective \(*\)-homomorphism.

2. **Covariance.** For each prescribed cell translation or rotation,
   \[
   \Phi\beta_g^{(1)}=\beta_{\widehat g_L}\Phi.
   \]

3. **Locality.** For every support radius \(R_0\), there are \(a_{R_0},\xi_{R_0}>0\) such that
   \[
   \operatorname{dist}\!\left(\Phi(A),\mathfrak A_m(N_R(B_L(\operatorname{supp}A)))\right)
   \leq a_{R_0}e^{-R/\xi_{R_0}}\|A\|.
   \]
   This holds uniformly over positions and invariant inputs of radius \(R_0\).

4. **Comparison.** Set
   \[
   \begin{aligned}
   F_0(A,B;\beta,t)
   &=\omega_0\!\left(\Phi(A)^*\alpha^{Lt}(\Phi(\tau_\beta B))\right)
     -\omega_0(\Phi(A)^*)\,\omega_0(\Phi(\tau_\beta B)),\\
   F_1(A,B;\beta,t)
   &=\omega_1\!\left(A^*\alpha_1^t(\tau_\beta B)\right)
     -\omega_1(A^*)\,\omega_1(\tau_\beta B),\\
   M_{A,B}(r,t)
   &=\sup_{|\beta'|_\infty\geq r}\max_{i=0,1}|F_i(A,B;\beta',t)|.
   \end{aligned}
   \]
   For every \(R_0\), every invariant \(A,B\) of norm at most one supported in its origin ball, every cell-group image of these data, every \(t\in\mathbb N_0\), and every \(r=|\beta|_\infty\geq1\),
   \[
   |F_0(A,B;\beta,t)-F_1(A,B;\beta,t)|
   \leq C_{R_0}(r^{-2}+tr^{-3})M_{A,B}(r,t).
   \]
   The constants are independent of \(A,B,\beta,t\). They may depend on the chosen laws, states, scale, and support radius.

> “A zero envelope gives zero values on both sides. No one-point matching is imposed.”  
> [ZM1INV.md:39](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:39)

The same \(\Phi\) must satisfy the algebraic and correlation obligations.

**Preferred proof route.** Construct invariant-algebra embeddings through finite commutants and compatible inclusions. Then construct the coarse state and update together with the comparison. This ports L-AF, L-GAUGE, and L-WAVELET. The first hard step is E1 across a cell boundary. The first rung is \(m=m_1=2\), \(L=2\), initially on a chain.

**Second proof route.** Construct an invariant image preserved exactly by \(\alpha^L\). Prove that its induced update has the prescribed coarse-law form. Pull back \(\omega_0\). This ports L-GAUGE and L-WAVELET. The first hard step is exact dynamical closure without a forbidden charge-equivariant extension. The first rung is one admissible invariant channel on two adjacent cells.

## Dependency tree

```text
Z  ZM1-I1[INV]                                                OPEN
│
├── K-E  Fine U[m], m even; coarse m₁ even                     OPEN
│   ├── E1  Embeddings across a cell boundary                 OPEN
│   ├── E2  Compatible extensions with exponential locality   OPEN
│   ├── P-AF  Finite invariant algebras and density            PROVED
│   ├── P-CHAR  Character constraints                         PROVED
│   └── P-SUPPORT  Orthogonal images must share support        PROVED
│
├── K-ODD  Alternative for a fixed odd fine register           OPEN
│   ├── E1 and E2, with odd-register multiplicities
│   └── P-ICE  Conditional state supply                       PROVED
│
├── D  Coarse law, stationary state, relative comparison      OPEN
│   ├── P-LOCK  Locked-state reduction                        PROVED
│   ├── D1  Minimal nonzero-tail rigidity rung                OPEN
│   ├── P-TAIL  Necessary tail matching                       PROVED
│   └── P-FREE  Free wave-packet comparison                   PROVED
│
├── Excluded construction branches
│   ├── N-GAUSS  Full-algebra singleton Gauss embedding       REFUTED
│   ├── N-ODD  Odd coarse m₁ over even-U or O fine law        REFUTED
│   ├── N-MATRIX  Neutral global matrix/Z₂ encoding           REFUTED
│   ├── N-J  Charge-equivariant representative decimation    REFUTED
│   ├── N-FILLER  One global character-filled complement      REFUTED
│   └── N-TOWER  Fixed-content exact quasi-free tower         REFUTED
│
└── Separate comparison branches
    ├── K-O  O-to-O invariant embedding                       OPEN
    ├── P-PATH  Good-sector path construction                 PROVED
    ├── P-REGROUP  Exact regrouping with growing content      PROVED
    └── P-GROUP  Finite-group chain refinement                PROVED
```

E1 and E2 describe sufficient construction programmes. Failure of a bounded rung need not refute K-E. D1 is a diagnostic child of D. It does not supply the full comparison.

## Literature imports

These are programme references. Their hypotheses must be rebuilt for the finite-register invariant nets.

**FROM MEMORY** marks every reference whose relevant theorem was not checked in the supplied corpus. Primary-source locators were checked online.

| ID | Programme and locator | What must be ported |
|---|---|---|
| **L-GAUGE** | Brothier–Stottmeister, 2019, [arXiv:1901.04940](https://arxiv.org/pdf/1901.04940), equation (2.1), Lemma 2.1 and equation (2.2). The finite-group chain calculation is checked in P-GROUP. | Refinement by multiplicative embeddings. Fixed quantum-link sectors and three-dimensional overlaps remain new obligations. |
| **L-AF** | **FROM MEMORY.** Amini–Elliott–Golestani, 2014/2015, [arXiv:1407.8413](https://arxiv.org/html/1407.8413), Theorem 2.1, Corollary 3.6, Theorem 4.1. | Multiplicity matrices and inductive-limit homomorphisms. Spatial locality and the prescribed cell action require additional proofs. |
| **L-PERT** | **FROM MEMORY.** Christensen–Sinclair–Smith–White–Winter, 2009/2012, [arXiv:0910.4953](https://arxiv.org/html/0910.4953), Lemmas 3.2 and 3.4, Theorem 4.3. | Correction of approximately multiplicative maps and nearby homomorphisms. Corrections must retain spatial support and symmetry. |
| **L-WAVELET** | **FROM MEMORY.** Morinelli–Morsella–Stottmeister–Tanimoto, 2020/2021, [arXiv:2010.11121](https://arxiv.org/html/2010.11121), equation (3.25), Theorem 4.11, equation (5.12). | Joint organization of local embeddings, states, and dynamics. Its free scalar results do not supply the present interacting comparison. |
| **L-FCS** | **FROM MEMORY.** Pérez-García–Verstraete–Wolf–Cirac, 2006/2007, [arXiv:quant-ph/0608197](https://arxiv.org/html/quant-ph/0608197), equations (3) and (6). | Exact transfer-operator formulas for correlations. The proposed port concerns uniform relative errors and observable cancellation. |

## K-E — The even-register embedding

> “These conditions do not establish existence or nonexistence.”  
> [KINV.md:99](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:99)

**Status: OPEN.**

**Statement.** For a fixed even fine \(m\in\{2,4,6,8\}\), construct some even \(m_1\in\{2,4,6,8\}\), some \(L\geq2\), and a map satisfying the algebra, covariance, and locality clauses of Z.

The existential family K-INV-E also permits the specified O fine algebra with a U coarse algebra. That mixed comparison must retain its separate type.

> “K-INV(O; m₁, L) asks for that map from a coarse L5-U[m₁] invariant algebra to the fine L5-O invariant algebra.”  
> [ZM1INV.md:32](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:32)

**Children:** E1, E2, P-AF, P-CHAR, P-SUPPORT.  
**Imports:** H-LAW, H-CELL, R-form, ZM1-INV. No state or update hypothesis.

**Preferred route — local AF refinement.**

Decompose finite invariant algebras into matrix summands. Construct unital embeddings that respect inclusion of regions. Retain every boundary representation. Impose the cell action on the multiplicity spaces. Pass to the norm limit through E2.

The first hard step is an embedding across a coarse-cell face. A copy inside one isolated fine block does not test the dilation constraint.

**Programme:** L-AF, with L-GAUGE as the geometric model.  
**Smallest rung:** five-mode U links with \(m=m_1=2\), \(L=2\), on a chain containing two adjacent cells.

**Second route — abstract embedding followed by localization.**

Construct a unital injective homomorphism through the ordered dimension-group or Bratteli data. Then replace it by a spatially controlled representative. Correct approximate covariance through local intertwiners.

The first hard step is localization. Abstract AF classification does not bound where matrix units land.

**Programme:** L-AF and L-PERT.  
**Smallest rung:** two neighboring finite interval algebras. Require a common correction that fixes their intersection.

## E1 — Embeddings across a cell boundary

> “It does not rule out K-INV or a direct-sum encoding.”  
> [ZM1INV.md:102](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:102)

**Status: OPEN.**

**Statement.** At \(m=m_1=2\) and \(L=2\), construct a finite invariant-algebra embedding on two adjacent coarse cells and their incident links. Require its restrictions to translated cell subalgebras to be related by the prescribed fine dilation. Require covariance under the stabilizer of the patch.

Write the finite commutants as
\[
\mathfrak B_1(R)=\bigoplus_\lambda M_{n_\lambda}(\mathbb C),
\qquad
\mathfrak B_0(S)=\bigoplus_\mu M_{d_\mu}(\mathbb C).
\]
The construction must supply multiplicities \(N_{\mu\lambda}\in\mathbb N_0\) satisfying
\[
\sum_\lambda N_{\mu\lambda}n_\lambda=d_\mu
\quad\text{for every }\mu,
\qquad
\forall\lambda\ \exists\mu:\ N_{\mu\lambda}>0.
\]
It must also supply the matrix units and symmetry intertwiners. The integer conditions alone are insufficient.

No target sector may be discarded. A coarse central projection need only commute with the image. It need not become central in the entire fine algebra.

**Children:** P-AF, P-CHAR, P-SUPPORT, P-PATH.  
**Imports:** H-LAW, H-CELL; L-AF as a programme.

**Preferred route — representation multiplicities.**

Decompose each boundary-charge representation by finite-dimensional \(U(5)\) representation theory. Retain its multiplicity algebra. Solve the unital representation problem in every fine summand. Impose the translated-cell restrictions before choosing matrix units.

The first hard step is simultaneous compatibility of the two endpoint regions with the stretched coarse edge.

**Programme:** L-AF, Theorem 2.1 and Corollary 3.6.  
**Smallest rung:** one edge crossing a coarse-cell boundary, with both endpoint matter factors and all gauge actions touching the patch.

**Second route — invariant recoupling.**

Begin with the path-sector construction P-PATH. Replace its single good sector by a decomposition containing every sector. Seek a refinement rule for invariant intertwiners. Require multiplication to survive recoupling.

The first hard step is a unit-preserving action on the defect sectors that agrees with the good-sector action on overlaps.

**Programme:** L-GAUGE, equations (2.1)–(2.2), ported to invariant commutants.  
**Smallest rung:** two fine links replacing one coarse link. Then add one adjacent coarse edge. A successful isolated path is insufficient.

## E2 — Compatible extensions with exponential locality

> “Compatibility across local supports and defect sectors remains to be constructed.”  
> [ZM1INV.md:126](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:126)

**Status: OPEN.**

**Statement.** Extend the E1 maps to an increasing family of finite-region embeddings. Arrange compatibility on every fixed local algebra. Preserve the prescribed cell action.

For each local \(A\), produce local approximants \(\phi_n(A)\) with
\[
\|\phi_{n+1}(A)-\phi_n(A)\|
\leq b_{R_0}e^{-cn}\|A\|,
\]
and support within distance \(O(n)\) of the corresponding fine block. The estimates must be uniform over translations. The limiting map must remain isometric on every local algebra.

These requirements yield a candidate
\[
\Phi(A)=\lim_{n\to\infty}\phi_n(A).
\]
The construction of the compatible family is the open assertion.

**Children:** E1, P-AF, P-SUPPORT, N-J, N-FILLER.  
**Imports:** H-CELL, ZM1-INV; L-AF and L-PERT as programmes.

**Preferred route — exact inclusion squares.**

Choose embeddings whose multiplicity diagrams commute. Correct the matrix-unit identifications by unitaries in appropriate relative commutants. Require each correction to preserve previously fixed faces.

The first hard step is simultaneous compatibility around a closed spatial cycle. Separate corrections on individual overlaps need not agree around that cycle.

**Programme:** L-AF, Corollary 3.6 and Theorem 4.1.  
**Smallest rung:** two adjacent plaquettes sharing an edge. The next rung is the six faces of one cube.

**Second route — controlled approximate intertwining.**

Construct approximately compatible local embeddings. Improve them through small local unitary corrections. Allocate a summable error budget. Prove exact multiplicativity, covariance, and injectivity in the limit.

The first hard step is obtaining corrections with controlled support. A small abstract unitary need not be local.

**Programme:** L-PERT, Lemmas 3.2 and 3.4.  
**Smallest rung:** two overlapping invariant algebras with an explicitly identified common subalgebra. Derive the correction estimate symbolically.

## K-ODD — A fixed odd fine register

> “Theorem 2 also supplies no odd-fine-m result.”  
> [KINV.md:49](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:49)

**Status: OPEN.**

**Statement.** For a fixed odd fine \(m\), construct a map satisfying Z’s three kinematic clauses for some allowed \(m_1\) and \(L\geq2\).

**Children:** the E1 and E2 constructions with odd-register multiplicities; P-PATH. P-ICE is a possible state supplier, not an embedding supplier.  
**Imports:** H-LAW, H-CELL, R-form, ZM1-INV.

**Preferred route — extend invariant path recoupling.**

Use \(m=m_1=1\). Track every path sector and every endpoint representation. Seek compatible invariant embeddings without assigning coarse end numbers to separated fine endpoints.

The first hard step is the extension from a good path sector to the full invariant algebra.

**Programme:** L-GAUGE.  
**Smallest rung:** two fine links and one coarse link, with both endpoint actions retained.

**Second route — character-equivariant AF construction.**

First construct a compatible action on the spaces of characters. Then lift the finite-region data to matrix summands. Test the fixed-point sets of the relevant rotation subgroups before attempting the lift.

The first hard step is matching the rotation action on characters. An oriented character cannot be treated as rotation invariant.

**Programme:** L-AF.  
**Smallest rung:** one plaquette and its end-exchanging rotations, followed by two translated plaquettes.

## K-O — The separate O-to-O analogue

> “K-INV-O is the analogous O-to-O question.”  
> [ZM1INV.md:32](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:32)

**Status: OPEN.**

**Statement.** With five matter modes per site, the \(512\)-dimensional even ten-rishon link sector \(S_+\), and local gauge group \(\operatorname{Spin}(10)\) at both scales, construct a cell-covariant, exponentially local, unital injective invariant-algebra homomorphism for some \(L\geq2\).

**Children:** E1 and E2 with the O representation data; P-AF and P-CHAR.  
**Imports:** PS-5, PS-6r, H-CELL, the specified O law. This is a separate comparison branch.

**Preferred route — spinor multiplicity algebras.**

Decompose finite \(\operatorname{Spin}(10)\) representations. Refine their multiplicity algebras. Retain both end-parity sectors. Impose the cubic stabilizer on the intertwiners.

The first hard step is a compatible unital decomposition across a stretched edge and its adjacent stars.

**Programme:** L-AF and L-GAUGE.  
**Smallest rung:** two \(S_+\) links with their common gauge vertex and endpoint matter.

**Second route — Clifford-based inclusion squares.**

Construct the local commutants directly from Clifford generators. Search for compatible inclusion squares before passing to representation labels.

The first hard step is preserving the global unit through every parity sector. A matrix corner does not suffice.

**Programme:** L-AF’s finite-dimensional inclusion method; L-PERT for controlled corrections.  
**Smallest rung:** one shared-vertex pair of link algebras, followed by a plaquette.

## D — The comparison in the specified fine vacuum

> “ZM1-I1[INV] in non-character vacua.”  
> [ZM1INV.md:17](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:17)

**Status: OPEN.**

**Statement.** For the fixed fine data and a kinematic embedding constructed above, produce an admissible coarse law and stationary coarse state satisfying Z’s relative bound.

A successful construction must permit revising the kinematic embedding. An arbitrary K-INV map need not support the required comparison.

**Children:** P-LOCK, D1, P-TAIL, P-FREE. The actual interacting comparison remains a terminal obligation after these tests.  
**Imports:** H-TICK, H-VAC, R-form, ZM1-I1[a], the same \(\Phi\) used in K-E or K-ODD.

**Preferred route — joint state and observable renormalization.**

Construct the coarse state and coarse couplings together. Use two-source functions
\[
Z_i(s,u;\beta,t)
=\omega_i\!\left(e^{sA_i^*}\alpha_i^{s_it}(e^{uB_{i,\beta}})\right),
\]
where \(s_0=L\), \(s_1=1\), \(A_0=\Phi(A)\), and \(A_1=A\). Their mixed logarithmic derivatives at the origin give the truncated correlations.

Prove the static error at relative order \(r^{-2}\). Prove the accumulated tick defect at relative order \(tr^{-3}\). Keep the same coarse couplings for every observable and support radius.

The first hard step is controlling cancellation uniformly over \(A,B\). Absolute decay estimates do not supply the pair-dependent denominator.

**Programme:** L-WAVELET for the joint algebra/state construction; L-FCS for the first analytic correlation tests.  
**Smallest rung:** D1. Then test one verified nonconstant invariant channel in an actual K-INV image.

**Second route — exact invariant dynamics.**

Prove
\[
\alpha^L\Phi=\Phi\alpha_1,
\qquad
\omega_1|_{\mathfrak B_{m_1}}=\omega_0\Phi.
\]
Gauge averaging extends the coarse state to the full algebra. These identities would give exact correlation equality.

The first hard step is proving that the induced observable dynamics extends to a coarse update of the prescribed five-mode form. Defining an arbitrary pullback automorphism does not establish that fact.

**Programme:** L-GAUGE and L-WAVELET, equation (5.12).  
**Smallest rung:** one invariant finite-dimensional channel with a specified admissible tick. Then include its neighboring channel.

## D1 — A minimal nonzero-tail rigidity theorem

**Status: OPEN.**

**Statement.** Let \(P,Q\) be strictly positive \(3\times3\) stochastic matrices. Assume both are reversible with respect to the same strictly positive probability vector \(\pi\). Assume their two nontrivial eigenvalues are distinct and lie in \((0,1)\).

Fix \(L\geq2\). For mean-zero functions \(f,g\), define
\[
F_0(n;f,g)=\langle f,P^{Ln}g\rangle_\pi,
\qquad
F_1(n;f,g)=\langle f,Q^ng\rangle_\pi,
\]
and
\[
M_{f,g}(n)=\sup_{k\geq n}\max_i|F_i(k;f,g)|.
\]

Prove
\[
\begin{split}
&\exists C<\infty\ \forall n\geq1\ \forall \|f\|_\infty,\|g\|_\infty\leq1:\\
&\qquad |F_0(n;f,g)-F_1(n;f,g)|
\leq Cn^{-2}M_{f,g}(n)
\end{split}
\quad\Longleftrightarrow\quad
Q=P^L.
\]

This is a proposed theorem. It is not an asserted new result.

**Children:** P-TAIL.  
**Imports:** finite-dimensional spectral theory, reversibility, the stated common stationary measure. The common measure is a rung hypothesis. It is not added to Z.

**Preferred route — isolate the two spectral channels.**

Use positive quadratic correlations \(f=g\). Recover the largest visible eigenvalue from the tail. Recover its eigenspace from the functions that annihilate that tail. Repeat on the orthogonal complement.

The first hard step is proving that the all-observable comparison aligns the spectral projections. Matching two decay rates alone is insufficient.

**Programme:** L-FCS, equations (3) and (6).  
**Smallest rung:** precisely the three-state model above. A two-state chain tests one decay mode but misses channel cancellation.

**Second route — rational generating functions.**

Express the correlations through resolvents on the mean-zero subspace. Recover the observable poles and residues from the relative tail condition.

The first hard step is justifying residue recovery from the pair-dependent envelope. Direct summation of a relative estimate needs care.

**Programme:** L-FCS’s transfer-matrix representation.  
**Smallest rung:** a two-dimensional mean-zero transfer space with two positive simple eigenvalues.

A proof would identify a rigidity mechanism in a bounded nonzero-correlation model. It would not establish that the interacting quantum vacuum has a finite transfer representation.

## Frozen input nodes

### P-AF — Finite commutants and density

> “The union of A^G(R) is norm dense in A^G.”  
> [GB1Z2L5.md:33](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:33)

**Status: PROVED — GB1Z2L5, Theorem 1; VC1_5, Theorem 2.1.**

Each finite invariant algebra is a finite-dimensional commutant. Gauge averaging preserves its support. The increasing finite-region system recovers the quasi-local invariant algebra.

> “with inverse φ↦φ∘E”  
> [VC1_5.md:48](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/VC1_5.md:48)

Invariant-algebra states therefore extend to gauge-invariant full-algebra states.

**Children:** none.  
**Imports:** H-LAW; compact local gauge groups. Compatibility with dynamics additionally uses H-TICK.

### P-CHAR — Character constraints

> “Each named-law invariant algebra has a character.”  
> [GB1Z2L5.md:37](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:37)

**Status: PROVED — GB1Z2L5, Theorem 2; KINV, Theorems 1, 3, and 4.**

Even-U locked characters and O locked characters are invariant under the specified cell lifts. Odd-U oriented characters are not end-reversal invariant.

For even coarse \(m_1\), every K-INV map obeys
\[
\chi_0\!\left(\Phi([p_{\ell,X}=m_1/2])\right)=1
\]
for every locked fine character \(\chi_0\).

> “For even m₁, a K-INV map and each locked fine character satisfy…”  
> [KINV.md:45](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:45)

The constant character map is covariant and local. It is not injective.

> “but not injective”  
> [KINV.md:53](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:53)

**Children:** P-AF.  
**Imports:** H-LAW, H-CELL; unitality for character pullback.

### P-SUPPORT — Shared support and central freezing

> “shared support for exponentially localized images”  
> [ZM1INV.md:136](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:136)

**Status: PROVED — ZM1INV, Theorem 3.6 and closure R6; KINV, Theorem 7.**

If \(P,P'\) are nonzero orthogonal coarse invariant projections and \(R_1,R_2\) are disjoint fine regions, then
\[
\operatorname{dist}(\Phi(P),\mathfrak A(R_1))
+\operatorname{dist}(\Phi(P'),\mathfrak A(R_2))
\geq\frac12.
\]

Also, with \(t=\min(5,m_1)\),
\[
\Pi_X=[Q_X=5+6t]
\]
is central in the coarse invariant algebra. Adjacent such projections are orthogonal.

> “For neighbouring sites X,Y, Π_XΠ_Y=0.”  
> [KINV.md:95](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:95)

**Children:** P-AF.  
**Imports:** H-LAW; injectivity and multiplicativity for the image bound.

**Blocked branch.** Assigning orthogonal coarse alternatives to independent fine factors fails.

**Weakest escape.** Allow their images to share a fine region. This changes the encoding ansatz. It changes no owner law.

### P-LOCK — Locked-state reduction

> “both truncated functions vanish for every input, separation and tick”  
> [ZM1INV.md:52](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:52)

**Status: PROVED — ZM1INV, Theorems 2.1–2.3 and closures R1–R2; KINV, Corollary 2.1.**

For stationary character states and gauge-preserving updates, every unital invariant homomorphism gives zero truncated correlations.

For a locked even-U fine witness and its base tick, Z is equivalent to the corresponding kinematic embedding with some even coarse register. The analogous typed reductions hold for the stated O comparisons.

> “equivalent to existence of the corresponding K-INV map for some even m₁”  
> [KINV.md:41](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:41)

**Children:** P-CHAR.  
**Imports:** the specified locked witnesses; base ticks; stationarity. A plaquette extension needs its own stationarity proof.

This proves a conditional benchmark. It does not select a physical vacuum.

> “These are supplied mathematical witnesses, not a selected VC1 vacuum.”  
> [KINV.md:20](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:20)

### P-TAIL — Necessary tail matching

> “the tail envelopes of the two sides agree to relative order r^{-p}”  
> [ZM1_OBS.md:292](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1_OBS.md:292)

**Status: PROVED — ZM1_OBS, Lemma ER.**

At fixed \(t\), let
\[
m_i(r)=\sup_{|\beta|_\infty\geq r}|F_i(A,B;\beta,t)|.
\]
Then class (a) implies
\[
|m_0(r)-m_1(r)|
\leq C_{R_0}(r^{-2}+tr^{-3})\max_i m_i(r).
\]
Positive exponential tails must have the same decay length and leading amplitude. Positive power-law tails must have the same exponent and leading amplitude.

**Children:** none.  
**Imports:** class (a), its pair-dependent envelope, and the stated asymptotic form when used.

This is necessary information. It is not a sufficient comparison theorem.

### P-FREE — The free wave-packet benchmark

> “massless free wave-packet estimates”  
> [ZM1.md:246](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:246)

**Status: PROVED — ZM1, Theorem Z2 and Corollary Z2.1.**

For the stated massless free walks, an exponentially local isometric embedding gives errors of order
\[
\kappa^2+t\kappa^3.
\]
The inputs are band-limited one-body vectors. The spatial interpretation has its stated time restriction.

> “physical separation r alone does not imply that support”  
> [ZM1.md:279](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:279)

This does not establish class (a) for arbitrary local invariant observables.

**Children:** none.  
**Imports:** the free c-number walk, \(\mu=0\), \(0<\varepsilon<\pi/2\), the stated momentum restrictions.

### P-PATH — A good-sector construction

> “On ran Pγ there is an equivariant unitary”  
> [ZM1INV.md:116](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:116)

**Status: PROVED — ZM1INV, Theorem 3.4.**

For \(m=m_1=1\), the aligned path sector carries a coarse link factor and interior representation factors. Its interior-gauge commutant contains the required coarse link action.

> “Extending this local good-sector action by zero is not unital.”  
> [ZM1INV.md:126](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:126)

**Children:** none.  
**Imports:** the specified finite path; its aligned-sector projection; the \(m=1\) representation.

The surviving extension problem includes every defect sector and every overlap.

### P-ICE — Conditional odd-register state supply

> “If ICE-T holds, every odd m…has two distinct P-witnesses.”  
> [VC1_5U_ODD.md:127](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/VC1_5U_ODD.md:127)

**Status: PROVED — VC1_5U_ODD, Theorems 4.2, 4.3, 5.1, and 5.3.**

A cell-invariant, quasi-invariant cubic-ice measure gives the stated stationary base-tick representation. Purity of its invariant-algebra state is equivalent to tail triviality.

> “is pure on A^gauge if and only if ν is tail-trivial”  
> [VC1_5U_ODD.md:115](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/VC1_5U_ODD.md:115)

**Children:** none within this wall.  
**Imports:** ICE-T when purity is required; the specified RK representation; the base tick.

ICE-T is an external unprovided hypothesis. This implication supplies neither K-INV nor the physical VC1 vacuum.

### P-REGROUP — Exact regrouping

> “Let Φ be the identity of A, regrouped, and α₁=α^L.”  
> [ZM1.md:97](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:97)

**Status: PROVED — ZM1, Theorem Z0.**

Exact regrouping gives a finite-range coarse update. Each coarse site retains the matter and assigned links of an entire fine block.

> “D grows like exp(c L³)”  
> [ZM1.md:102](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:102)

**Children:** none.  
**Imports:** the specified base tick and Z0’s separate block indexing.

Its growing content does not satisfy the fixed five-mode R-form target.

### P-GROUP — A finite-group chain refinement

> “unital, injective, of finite range and translation covariant”  
> [ZM1I1A.md:134](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:134)

**Status: PROVED — ZM1I1A, closure RC-6.**

For a finite group \(G\), the chain refinement
\[
R(b)=u(b\otimes1)u^*,
\qquad
(u\xi)(g,h)=\xi(gh,h)
\]
has the stated endpoint and midpoint gauge covariance.

**Children:** none.  
**Imports:** regular finite-group link registers; one spatial dimension; L-GAUGE’s refinement formula.

This is an established rung for the method. It is not a five-mode quantum-link embedding.

## Refuted construction branches

### N-GAUSS — Restore the old full-algebra map

> “there is no specified map for L≥2 under R-form”  
> [ZM1I1A.md:44](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:44)

**Status: REFUTED — ZM1I1A, Theorems 1–3 and 6; ZM1, Amendment 3.**

**Refuted statement.** A unital full-algebra block homomorphism satisfies the old locality and Gauss-identification conditions at \(L\geq2\).

**Exact blocking hypotheses:** full-algebra unitality; R-form; G1 on disjoint singleton representatives; Z-a; the stated assignment or Z-b.

Trace transfer preserves adjacency. Locality and density force \(L=1\).

**Surviving variant:** the owner’s invariant-only map. It imposes no Gauss-generator identification.

**Weakest escape:** remove the full-algebra Gauss-identification requirement. ZM1-INV already does this.

**Children:** none.  
**Imports:** the named finite-register laws and the old Definition-Z conditions. No vacuum or comparison hypothesis.

### N-ODD — Odd coarse \(m_1\) over even-U or O fine data

> “Injectivity and locality are not assumed.”  
> [KINV.md:37](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:37)

**Status: REFUTED — KINV, Theorem 2 and Corollary 2.1.**

**Refuted statement.** Such a unital homomorphism intertwines the specified end-exchanging rotation when \(m_1\) is odd.

**Exact blocking hypotheses:** a fine character fixed by that lift; unitality; rotation covariance; integer coarse end-number spectrum; and
\[
p_{\ell,X}+p_{\ell,Y}=m_1\,1.
\]
Character pullback gives
\[
\chi(p_{\ell,X})=\chi(p_{\ell,Y})=m_1/2,
\]
which contradicts the integer spectrum.

**Surviving variants:** even coarse \(m_1\); odd fine registers outside this theorem; changed rotation covariance.

**Weakest escape:** choose even \(m_1\), already permitted by R-form. No law change is needed.

A translation-only map requirement is a separate owner fork. Weakening locality or injectivity does not remove this obstruction.

**Children:** P-CHAR.  
**Imports:** H-LAW, H-CELL, unitality.

### N-MATRIX — Insert a neutral global matrix register

> “There is no unital *-homomorphism from any characterless unital C*-algebra.”  
> [GB1Z2L5.md:59](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:59)

**Status: REFUTED — GB1Z2L5, Theorems 3–6; ZM1INV, Theorem 3.2 and closure R5.**

**Refuted statement.** A global-unit \(M_D\), \(D\geq2\), or the standard characterless \(\mathbb Z_2\) invariant source embeds unitally into the full named-law invariant algebra.

**Exact blocking hypotheses:** a characterless source; a character on the target; unitality.

**Surviving variant:** a direct-sum coarse invariant algebra with characters. Non-unital finite corners also survive.

> “Thus it admits a non-unital embedding of M₂.”  
> [GB1Z2L5.md:89](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:89)

**Weakest escape:** retain the actual coarse invariant algebra. Do not replace it by a neutral matrix algebra.

Deleting the word “unital” alone is insufficient under the retained locality conditions.

> “is unital, even if unitality is not assumed”  
> [GB1Z2L5.md:75](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:75)

**Children:** P-CHAR.  
**Imports:** the full invariant target; uniform separating locality for the automatic-unit clause.

### N-J — Charge-equivariant representative decimation

> “no class J map exists for L≥2”  
> [KINV.md:83](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:83)

**Status: REFUTED — KINV, Theorem 6; ZM1INV, Theorems 3.3 and 3.5 for the stated path variants.**

**Exact blocking hypotheses:** a unital full-algebra extension \(\Psi\); injective site representatives with the dilated translation law; even finite-spectrum fine star operators; and
\[
\Psi\operatorname{Ad}(e^{i\theta Q_X})
=
\operatorname{Ad}(e^{i\theta Q^F_{x_X}})\Psi.
\]

The joint-spectrum argument forces neighboring representatives to remain fine neighbors.

The factorwise path variant also fails when the two coarse end actions are assigned to the first and last independent fine links.

**Surviving variant:** an invariant-only embedding without this full-algebra extension.

**Weakest escape:** remove the representative-star implementation requirement. The fine and coarse laws can retain their gauge symmetries.

> “It is not an already refereed result.”  
> [ZM1I1A_OWNER_CHECK.md:11](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A_OWNER_CHECK.md:11)

The earlier owner-check argument is not an additional proved input here. The frozen KINV theorem supplies this node.

**Children:** none.  
**Imports:** class J exactly as stated; H-LAW; dilated translations.

### N-FILLER — Complete one good sector by a character

> “No K-INV map has Φ(a)=ρ(a)+χ(a)(1−P_g).”  
> [KINV.md:75](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:75)

**Status: REFUTED — KINV, Theorem 5, closure R-NGF, and Corollary 5.1.**

**Exact blocking hypotheses:** injectivity; uniform locality over translated inputs; separating blocks; and a nonzero quasi-local projection \(E\) on which the entire coarse algebra acts through one character.

Unitality is unnecessary for this negative.

> “Theorem 5 holds without assuming that Φ is unital.”  
> [KINV.md:71](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:71)

**Surviving variant:** compatible local representations across all defect configurations. The complement need not carry one global character representation.

**Weakest escape:** abandon this global completion ansatz. No owner-law change is required.

Finite-patch character summands are not themselves forbidden. Their extension must satisfy the global locality theorem.

**Children:** P-PATH.  
**Imports:** uniform exponential locality, injectivity, quasi-locality of \(E\), and invariant evenness.

### N-TOWER — Fixed-content exact quasi-free iteration

> “a tower…needs (L₁…L_k)³ to divide d”  
> [ZM1.md:142](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1.md:142)

**Status: REFUTED — ZM1, Theorem Z1 and Corollary Z1.1.**

**Refuted statement.** Exact quasi-free refinements of the stated walk iterate indefinitely with fixed one-body content.

**Exact blocking hypotheses:** a one-body isometry; summable kernel; dilated translations; exact intertwining; fixed finite content.

**Surviving variants:** approximate comparison; nonlinear invariant maps; growing content.

**Weakest escape:** retain the approximate comparison already required by the owner. Exact quasi-free intertwining is an optional stronger ansatz.

**Children:** P-FREE, P-REGROUP.  
**Imports:** the specified free walk and one-body formulation.

This negative does not refute the one-step invariant theorem.

## Owner forks attached to the blocked branches

These are candidate changes of problem. None is adopted.

The tests are ordered as requested:

1. Does the text state or fix a part’s target?
2. Is it open-ended?
3. Does it settle downstream physics by premise?
4. Does it add structure its own reasons do not need?

**P** means pass. **F** means fail. **C** identifies an unresolved interpretation or cost.

| Candidate text | Tests 1–4 | Effect and limit |
|---|---|---|
| **Translation-only map covariance.** Require \(\Phi\tau_b=\tau_{Lb}\Phi\). Retain the existing cell symmetries of each law. | **P, P, C, P** | Removes the rotation premise of N-ODD. It supplies no rotational comparison for downstream consumers. |
| **Vacuum representation target.** Once \(\omega_0\) is fixed, replace the target by \(\pi_{\omega_0}(\mathfrak B_m)\). Use the induced local net, tick, and cell action. | **C, P, P, P** | Gives a closed sector-reading candidate. It changes global faithfulness. It asserts neither absence of characters nor existence of an embedding. |
| **Particle-hole-twisted coarse rotation at \(m_1=5\).** Compose the end-exchanging lift with that internal operation. | **P, P, C, F** | Changes N-ODD’s spectral symmetry premise. Its extra internal operation presently serves the obstruction escape rather than an independent law requirement. |
| **Exclude character vacua.** Require \(\omega_0|_{\mathfrak B_m}\) not to be a character. | **C, P, F, P** | Inserts a nonzero invariant excitation space by premise. It cannot be used to establish VC1’s excitation requirement. |

The translation-only assessment is recorded explicitly:

> “the draft's four tests are P P C P”  
> [KINV.md:109](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/KINV.md:109)

The sector construction has a precise GNS version:

> “J_S^GNS=ker π_S”  
> [GB1Z2L5.md:109](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:109)

A quotient need not remove the character obstruction:

> “the character factors through the quotient”  
> [GB1Z2L5.md:119](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:119)

For a locked character vacuum, its represented invariant algebra is \(\mathbb C\). That quotient cannot host the required faithful coarse algebra.

The non-character restriction carries the recorded failure:

> “Checks: C, P, F, P.”  
> [ZM1INV.md:184](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1INV.md:184)

The preferred E1–E2 programme needs none of these owner changes.

## Ranked open frontier

The ranking is a research-priority judgment. Likelihood concerns the stated deliverable. It does not estimate the probability of the TOE target.

| Rank | Open obligation | Wall movement on success | Proof likelihood |
|---:|---|---|---|
| **1** | **E1: boundary-crossing finite embedding** | Produces the first geometry-sensitive construction in the actual even-register algebra. Supplies concrete data for extension. | Moderate for the chain rung. Lower for the cubic patch. |
| **2** | **E2: compatible local extensions** | Establishes K-INV for the constructed register pair. Together with P-LOCK, establishes the locked-state instance of Z. | Low to moderate, conditional on E1. |
| **3** | **D1: two-channel relative-tail theorem** | Determines how much exact transfer data the relative criterion forces on the smallest nonzero-tail rung. | High for the stated reversible three-state case. |
| **4** | **D: actual interacting comparison** | Establishes Z for the specified fine vacuum when paired with the same kinematic embedding. | Low without a controlled joint state/update construction. |
| **5** | **K-O: O-to-O embedding** | Supplies the separate O kinematic branch and its locked-state reduction. | Low to moderate at finite patches. |
| **6** | **K-ODD: odd fine-register embedding** | Supplies a branch outside N-ODD’s hypotheses. | Low until its character action and defect-sector extension are understood. |

### Lane brief 1 — E1: cross one cell boundary

**Deliverable:** an explicit unital injective map for \(m=m_1=2\), \(L=2\), on two adjacent chain cells. Include every endpoint gauge action. Enforce the dilated translation relation between the cell restrictions. Give symbolic multiplicity decompositions and matrix units.

**Three attacks:** boundary representation decomposition; invariant path recoupling; enlargement by one specified collar.

**Stopping rule:** stop with a proof, a counterexample to the precisely bounded patch statement, or one named compatibility lemma left unproved after all three attacks fail. A failed collar does not refute unrestricted K-INV-E.

### Lane brief 2 — E2: make overlapping maps agree

**Deliverable:** extend an E1 construction across two overlapping plaquettes. Prove agreement on their intersection. Then formulate the cube consistency identity and a translation-uniform locality estimate.

**Three attacks:** exact commuting-square correction; equivariant correction inside the relative commutant; summable local approximate intertwining.

**Stopping rule:** stop with a compatible extension and estimate, an explicit obstruction for the supplied embeddings, or a named local-correction lemma left unproved after all three attacks fail. Keep failure of those embeddings separate from failure of every invariant embedding.

### Lane brief 3 — D1: test the relative criterion on two decay channels

**Deliverable:** prove or refute the displayed three-state theorem. Keep the observable quantifier uniform. Treat zero-tail pairs explicitly. Use exact spectral algebra.

**Three attacks:** eigenprojection isolation; positive quadratic-form tail limits; rational-resolvent pole and residue recovery.

**Stopping rule:** stop with a proof, an exact reversible counterexample, or a named observable-isolation lemma left unproved after all three attacks fail. A proof advances the diagnostic rung. It supplies no interacting quantum vacuum or coarse tick.

## Boundary of this tree

> “the sequence L_k approaches a fixed point or a controlled trajectory”  
> [TOE_ASSEMBLY.md:331](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:331)

Z is one step. A controlled trajectory and compatible image tower remain separate consumers.

> “Charged sectors…get no zoom from this map”  
> [TOE_ASSEMBLY.md:255](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:255)

No charged-sector bridge is included in Z.

> “Whether any map has such images is not shown.”  
> [ZM1I1A.md:126](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/ZM1I1A.md:126)

A fine propagating channel supplies a test only after its inclusion in the embedding image is proved.

> “Their link registers are finite quantum links…not group-valued Wilson links.”  
> [TOE_ASSEMBLY.md:631](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:631)

The Yang–Mills interface still requires its measure, domain, dictionary, and rate bridges.

> “none of it is load-bearing until re-proved on the framework”  
> [TOE_ASSEMBLY.md:745](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:745)

The proposed ports therefore remain proof obligations. Their intended arguments use finite representation theory, matrix units, exact spectral identities, and controlled norm limits. No computer-assisted step is assigned a proof role.