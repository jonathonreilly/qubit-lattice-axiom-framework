**Proof tree, sketched (owner 2026-11-08: "do more physics on astra max for sketching the proof trees").** Written by Codex gpt-6-astra at max effort, read-only, on the laptop; finished 2026-11-08T20:08:51Z. Template `~/toe-lap/tmpl/treeSMG1.txt`. A sketch: no node below is proved by this file, and nobody has checked it. Statuses quote the frozen parts.

# W2 — Chirality and the 16 by symmetric mass generation

> [TOE_ASSEMBLY.md:261](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:261): “Tick stationarity remains a separate requirement.”

> [TOE_ASSEMBLY.md:262](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:262): “The existence of the light 16 remains to be proved.”

> [TOE_ASSEMBLY.md:263](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:263): “Require a fully stated replacement before claiming exclusion of every additional light sector.”

**Root status: OPEN.**

The root is a theorem schema until W2-LIGHT receives a closed definition. Its missing predicate cannot be supplied by assuming the desired spectrum.

Solid edges below denote proof dependencies. Dotted edges denote proposed intermediate models. Success in an intermediate model requires a transfer theorem.

```text
W2  One protected Weyl 16, with symmetric removal of every partner
│
├── C   Native carrier and symmetry-preserving interaction
│   ├── P8  Native U(5) operator family
│   └── P9  Finite-register witnesses and exact NN compilation
│
├── A   Actual symmetry group, anomaly class, and anomaly matching
│   └── P8  Perturbative anomaly arithmetic
│
├── M   Three-dimensional selective SMG and Weyl scaling
│   ├·· H   Isolated mirror chain: periodic and infinite-volume stability
│   │   ├── P1  Principal generators
│   │   ├── P2  Eight-Majorana atom
│   │   ├── P3  Zero-hop product ground state
│   │   └── P4  Conditional open-chain stability
│   │
│   ├·· S   S-GAP with nonzero light hopping
│   │   ├── P5  Exact configuration-conserving comparison
│   │   ├── P6  Exact second-order mixing identity
│   │   └── P7  S-GAP⁰
│   │
│   ├·· D   Controlled interacting light theory beside the mirror gap
│   │   ├── P5
│   │   └── P6
│   │
│   ├·· R2  A genuinely chiral 1+1-dimensional rung
│   └·· R3  A selective 2+1-dimensional rung
│
├── V   One pure state for the certified generator and the tick
│   ├── P1
│   └── P3
│
├── Q   Charged-sector realization and transverse transport
│   └── P10  Exact longitudinal string motion
│
└── L   W2-LIGHT: a closed criterion and a complete light-sector census

Frozen branch barriers:
N1  Old W2.4 quantifiers
N2  Vacuum-complement Floquet gap
N3  Bilinear Spin(10) carrier and conserved centre patterns
N4  Odd local gauge invariants and finite localized charges
N5  Empty-state finite-depth one-particle walks
N6  Gatewise nonlinear frames
N7  Particular disjoint block encodings
N8  Rigid rays and specified finite-range backgrounds
N9  A unique whole-system gap at half filling
N10 Circuit-dressed Hamiltonian identified with R-GEN
N11 Unrestricted window and per-parity-sector gap comparisons
```

## W2 — Root theorem

> [SMG1.md:21](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:21): “A site has `F_x = Λ C⁵`.”

> [SMG1.md:24](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:24): “pure, tick-stationary, `G`- and cell-invariant, and a ground state in R-GEN.”

> [SMG1.md:27](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:27): “the rescaled two-point function `Z δ_AB S_c`, `Z,c>0`.”

**Statement.** Fix the following hypotheses and definitions.

- **H5 — Native registers.** Sites are \(x\in\mathbb Z^3\). Each site has \(F_x=\Lambda\mathbb C^5\). Each nearest-neighbour link has a fixed finite-dimensional register. Register dimensions do not depend on volume.
- **HCAR — Local algebra.** Matter factors form the graded CAR algebra. Link factors are ordinary tensor factors. Their completion is the quasi-local algebra \(\mathfrak A\).
- **HCOV — Cell symmetry.** The specified lifts of
  \[
  \Gamma=2\mathbb Z^3\rtimes O_{c_0}
  \]
  act transitively on sites.
- **HNN — NN-a.** The tick \(\alpha\) has a fixed finite number of layers. Every factor acts on one edge triple. Every factor commutes with the parity of its two matter sites. Edge triples within a layer are disjoint. The complete tick commutes with the cell lifts and fixes every supplied local gauge generator.
- **HGEN — Certified bounded generator.** The decomposition is fixed before evaluating its gap:
  \[
  g=e^{-iX_g},\qquad X_g=X_g^*,\qquad \|X_g\|<\pi,
  \]
  \[
  H_U=\sum_gX_g,\qquad
  \delta(A)=i\sum_g[X_g,A].
  \]
- **HG — Exact symmetry.** A compact group \(G\) acts on site registers by even unitaries. Its specified action commutes with \(\alpha\). There is an injection
  \[
  G_{\rm SM}=\frac{SU(3)\times SU(2)\times U(1)}{\mathbb Z_6}\hookrightarrow G.
  \]
- **HQ — Charged fields.** The field algebra, charged-sector prescription, and correlation functional are fixed explicitly. For an ungauged model, these may be the ordinary field algebra and its state. A locally gauged model must supply the bridge in Q.
- **HL — Light-sector criterion.** A closed predicate \(\mathcal C_{\rm light}\) is fixed before testing the construction. Its admissible scaling families, carrier channels, and completeness requirement must be explicit. The owner has not selected this predicate.
- **HAS0 — One construction.** Every conclusion concerns the same registers, tick, certified decomposition, state, and charged prescription.

Construct such data together with a pure state \(\omega\), odd fields \(\psi_{A,s}\), and constants \(Z,c>0\), satisfying:

\[
\omega\circ\alpha=\omega,\qquad
\omega\circ\tau_\beta=\omega,\qquad
\omega\circ\gamma_g=\omega,
\]

\[
\omega(A^*[H_U,A])\geq0
\quad\text{for every local }A
\]
on the explicitly declared ground-state algebra.

The algebra on which purity is proved must also be declared.

The internal index is \(A=1,\ldots,16\). The Weyl-spinor index is \(s=1,2\). The fields transform in a unitary representation \(D\) satisfying

\[
\begin{aligned}
D|_{G_{\rm SM}}
={}&(\mathbf3,\mathbf2)_{1/6}
\oplus(\overline{\mathbf3},\mathbf1)_{-2/3}
\oplus(\overline{\mathbf3},\mathbf1)_{1/3}\\
&\oplus(\mathbf1,\mathbf2)_{-1/2}
\oplus(\mathbf1,\mathbf1)_1
\oplus(\mathbf1,\mathbf1)_0,
\end{aligned}
\]

\[
\operatorname{Sym}^2(D)^G=0.
\]

With the stated nearest-cell rule,

\[
\psi^\lambda_{A,s}(x,t)
=
\lambda^{3/2}\alpha^{\lfloor\lambda t\rfloor}
\bigl(\tau_{[\lambda x]}\psi_{A,s}\bigr),
\]

require the smeared distributional limit

\[
\lim_{\lambda\to\infty}
\left\langle
\psi^\lambda_{A,s}(x,t)
\bigl(\psi^\lambda_{B,r}(0,0)\bigr)^*
\right\rangle_{\omega,HQ}
=
Z\delta_{AB}[S_c(x,t)]_{sr},
\]

\[
S_c(x,t)=
\int_{\mathbb R^3}\frac{d^3p}{(2\pi)^3}
\frac{1-\widehat p\cdot\sigma}{2}
e^{\,i(p\cdot x-c|p|t)}.
\]

Prove uniform massive-sector estimates sufficient to remove the mirror degrees of freedom. Prove \(\mathcal C_{\rm light}\) for the resulting theory. Preserve \(G\) throughout the construction.

A gap for the entire GNS Hamiltonian is not the final target. The retained Weyl sector is gapless. A mirror tensor factor must be derived if the proof uses one.

> [TOE_ASSEMBLY.md:262](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:262): “It forces \(G\supsetneq G_{\rm SM}\), not \(G=\operatorname{Spin}(10)\).”

The **exact Spin(10) branch** additionally requires \(D=S^+\) under an exact Spin(10) action. The **U(5) branch** requires an explicit restriction or pullback of \(S^+\). A U(5) construction must not be reported as establishing exact Spin(10) symmetry.

**Status:** OPEN.

**Children:** C, A, M, V, Q, L.

**Imported hypotheses:** H5, HCAR, HCOV, HNN, HGEN, HG, HQ, HL, HAS0.

**Preferred route.** Build a native symmetry-preserving interaction. Prove selective massive elimination. Apply constructive infrared analysis to the retained fields. Prove the tick and census bridges separately. This ports the FK, Wang–Wen, and constructive fermion programmes listed below.

**First hard step.** Obtain a uniform mirror estimate in a model whose light degrees of freedom already move.

**Smallest rung.** S with \(t\epsilon\neq0\), followed by D in its controlled parameter wedge.

**Second route.** Start with an explicit chiral measure or boundary regulator. Prove its locality. Transfer it to a fixed finite-register NN-a law with its actual certified generator.

**First hard step.** Preserve the chiral pole and mirror estimate during that transfer.

**Smallest rung.** A finite-width R2 boundary problem with every interface and momentum channel included.

**Literature:** LFK, LWW, LKIK, LRG1, LRG3.

## Accepted proved inputs

These nodes are inputs with their stated hypotheses. Their frozen proofs are not reopened.

### P1 — Principal generators

> [SMG1.md:29](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:29): “It is then unique.”

**Statement.**
\[
g=e^{-iX},\quad X=X^*,\quad\|X\|<\pi
\]
has a solution exactly when \(-1\notin\operatorname{spec}(g)\). The solution is unique.

**Status:** PROVED — SMG1, Lemma G0.

**Children:** \(\varnothing\).

**Imports:** Finite-dimensional spectral theory; HGEN.

### P2 — The eight-Majorana atom

> [SMG1.md:53](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:53): “No nonzero quadratic in `c₁,…,c₈` is `S`-invariant.”

**Statement.** The specified \(S\cong(\mathbb Z_2)^4\) action on \(\Lambda\mathbb C^4\) has one copy of each character. Its quartic \(W\) has spectrum

\[
-14\quad(1),\qquad 0\quad(8),\qquad 2\quad(7).
\]

Its unique ground vector is even and \(S\)-fixed.

**Status:** PROVED — SMG1, Lemma 2.1 and Theorem 2.2.

**Children:** \(\varnothing\).

**Imports:** The four specified Clifford generators; exact CAR identities; the self-dual binary code.

This is an \(S\)-symmetric atom. Its symmetry has not thereby become U(5) or Spin(10).

### P3 — The zero-hop product model

> [SMG1.md:77](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:77): “It is stationary under the tick.”

**Statement.** Under the supplied positive parameters and principal-log bounds, the zero-hop model has a unique product ground state. Its gap is at least

\[
\Delta_0=\min(14\tau,\tau_5,\tau_E).
\]

The infinite-chain state is pure. Its GNS generator has a simple zero and the same gap bound. The state is tick-stationary.

**Status:** PROVED — SMG1, Theorem 4.1.

**Children:** P1, P2.

**Imports:** The specified fifth-mode penalty; positive electric term; commuting product Hamiltonian.

The fifth mode is empty in this input. This input supplies no light bath.

### P4 — Conditional open-chain stability

> [SMG1.md:118](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:118): “Conditional on that cited theorem.”

**Statement.** Assuming Fröhlich–Pizzo Theorem 3.5, the supplied open chain has a unique ground state and gap at least \(\Delta_0/2\) when

\[
|\theta|<t_0\Delta_0/4.
\]

The estimate is uniform in chain length.

**Status:** PROVED — SMG1, Lemma 5.1 and Theorem 5.2, as a conditional implication.

**Children:** P3.

**Imports:** LFP; local dimension \(64\); a unique on-site kernel; bounded nearest-neighbour perturbations.

> [SMG1.md:122](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:122): “No stationarity for `U` at nonzero `θ` follows.”

Periodic boundaries, the native infinite-chain proof, and tick stationarity remain separate.

### P5 — An exact gap beside a vector-like bath

> [SMG15.md:66](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:66): “the entire spectrum strictly below” the threshold “is exactly the free half-filled light spectrum.”

**Statement.** For the configuration-conserving family, \(L\in4\mathbb N\), \(L\geq8\), \(t_0\neq0\), and \(\delta<7\tau\), every nontrivial mirror configuration costs at least

\[
m(14\tau-2\delta).
\]

The finite half-filled ground state is unique. The spectrum below the charged threshold is exactly the stated free light spectrum, including both holonomies.

**Status:** PROVED — SMG15, Theorems 2 and 3.

**Children:** P2.

**Imports:** Exact Gauss reduction; fixed half filling; \(\tau_E=0\); conservation of every mirror configuration.

> [SMG15.md:74](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:74): “a vector-like light pair.”

This input retains opposite Fermi points. It does not supply chirality.

> [SMG15.md:217](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:217): “exactly when `μ(1,1)=0`.”

For this family, the canonical ground-state construction satisfies the unrestricted local R-GEN ground-state condition precisely under that additional condition. The GNS spectral extension still needs its core argument.

### P6 — The exact leading mixing calculation

> [SMG15.md:138](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:138): “`PH_4P=0`.”

**Statement.** With the stated mirror projection and atomic Hamiltonian,

\[
PH_4Q(QH_MQ)^{-1}QH_4P
=
\frac{2}{7\tau}\sum_x\Lambda_x^2P.
\]

For the hopping coupling, the formal second-order light correction is

\[
-\frac{4\epsilon^2}{7\tau}N
+
\frac{4\epsilon^2}{7\tau}\sum_xn_xn_{x+1}.
\]

**Status:** PROVED — SMG15, Theorem 7.

**Children:** P2.

**Imports:** The specified quartic coupling; atomic resolvent; exact CAR identities.

> [SMG15.md:144](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:144): “It does not yield volume-uniform decoupling.”

The displayed coefficient is not a bound on the omitted terms.

### P7 — S-GAP⁰

> [SGAP0.md:150](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP0.md:150): “Theorem 9 (Corollary C; S-GAP⁰).”

> [SGAP0.md:152](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP0.md:152): “`E_σ≥E_0+7τ`.”

**Statement.** For the supplied model,

\[
t=\tau_E=0,\qquad L\in4\mathbb N,\quad L\geq8,\quad N=L/2,
\]

\[
\tau>0,\qquad |\epsilon|\leq2\cdot10^{-10}\tau,
\]

every nontrivial allowed \(S\)-character satisfies

\[
E_\sigma\geq E_0+7\tau,\qquad E_0=E_1=e_{p_{\rm alt}}.
\]

**Status:** PROVED — SGAP0, Theorem 9.

**Children:** P2.

**Imports:** The supplied Gauss reduction; SGAP0 Theorems 2–8; the rebuilt polymer estimate; the parity-pattern comparison.

The load-bearing comparison is local in the differences between patterns:

> [SGAP0.md:124](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP0.md:124):
> “`e_p−e_{p_alt}≥|NW(p)| ε²/(6τ)`.”

**Imported subresult:** SGAP0, Theorem 8.

> [SGAP0.md:164](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP0.md:164): “Infinite-volume, GNS and tick statements are not established.”

No such extension is included in P7.

### P8 — The native U(5) operator family

> [CH1.md:220](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:220): “`(−3, 9, −15) = −3·(1, −3, 5)`.”

**Statement.** For \(2\leq m\leq8\), the live U(5) carrier contains an odd, sixteen-dimensional operator space carried at one site, with content

\[
10_{-3}\oplus\overline5_{9}\oplus1_{-15}.
\]

Its restriction is a full Standard Model family. Its perturbative U(5) anomalies vanish.

**Status:** PROVED — CH1, Corollary U-T″; Proposition AN supplies the associated anomaly-line arithmetic.

**Children:** \(\varnothing\).

**Imports:** The specified rishon registers; CH1’s native composite operators; the standard subgroup embedding.

> [CH1.md:224](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:224): “This is operator content only.”

A nonzero operator space supplies neither particle poles nor canonical sixteen-mode CAR.

### P9 — Finite-register witnesses and exact compilation

> [CG16B.md:74](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16B.md:74): “both witnesses meet NN-a read with their own registers.”

**Statement.** The specified nonlinear and rishon witnesses admit exact finite NN-a decompositions. Their registers and actions are those of the witnesses.

**Status:** PROVED — CG16B, Theorem 3.1 and Lemma NN-W.

**Children:** \(\varnothing\).

**Imports:** The witness representations; their cell lifts; finite-dimensional Lie-group generation.

> [CG16B.md:47](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16B.md:47): “these 16-component operator families are not CAR modes.”

Exact compilation does not establish a fermion spectrum. It also does not identify the sum of compiled principal generators with the original block Hamiltonian.

### P10 — Longitudinal charged motion

> [RCSP16.md:80](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCSP16.md:80): “defines a band `V(K)=e^{iK₁}`.”

**Statement.** The specified straight-string representation has an exact moving band with

\[
V(K)=e^{iK_1},\qquad N=(-1,0,0).
\]

**Status:** PROVED — RCSP16, Theorem 7.

**Children:** \(\varnothing\).

**Imports:** The specified string limits, covariant implementers, and charged-sector reading.

> [RCSP16.md:86](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCSP16.md:86): “No one-dimensional band has a three-dimensional Clifford cone.”

Theorem 8 prevents promoting this band to the required Weyl cone.

## Frozen negative branches and surviving variants

Every node below has **children \(\varnothing\)**. The escape named in a node removes a stated hypothesis. It does not prove the surviving construction.

### N1 — The old W2.4 quantifiers

> [SMG1.md:33](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:33): “The universal reading is inconsistent with W2.3.”

**Status:** REFUTED — SMG1, GAP W2.4.

**Blocked statement.** Every power normalization has the required finite limit.

**Load-bearing hypothesis.** Universal quantification over scaling powers.

Increasing both powers multiplies the nonzero W2.3 limit by \(\lambda^2\).

**Other failed variant.** Existential normalization permits every bounded operator to scale to zero. Undemodulated sampling can also erase a \(\pi\)-channel signal.

**Weakest surviving change.** Fix admissible scaling families and channel coverage before testing them. Prove that unwanted sectors cannot evade the admissibility definition. Node L carries this obligation.

**Imports:** W2.3; bounded local correlations; the stated scaling prescription.

### N2 — A vacuum-complement Floquet gap

> [SMG1.md:96](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:96): “`1 ∈ spec(U|H₁)`.”

**Status:** REFUTED — SMG1, Lemma F and Corollary F1.

**Blocked statement.** The tick spectrum avoids a neighbourhood of \(1\) on the vacuum complement.

**Load-bearing hypotheses.** Finite propagation. Infinite translation covariance. A stationary translation-invariant clustering state. A nonzero invariant-even vacuum complement.

**Weakest surviving change.** Use the owner-selected bounded R-GEN gap. Retain tick stationarity as a separate proof.

The lemma does not address finite rings. It does not exclude a gap after removing the entire fixed-vector space.

**Imports:** Lemma F hypotheses H1–H3; its specified GNS sector.

### N3 — A local spinor from the bilinear Spin(10) action

> [CG16B.md:39](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16B.md:39): “the bilinear action has `u(−1)=−1` and fails (F).”

**Status:** REFUTED — CG16B, Theorem 2.2; LW1_5, Theorem SC.

**Blocked statement.** The standard five-mode bilinear action supplies odd local spinor-class matter fields.

**Load-bearing hypothesis.** The internal central element \(-1\) acts as a scalar on the site Hilbert space. Its adjoint action therefore fixes every matter operator.

**Weakest surviving changes.**

- Retain U(5) and use the explicit composite family P8.
- Use a charged-sector construction outside the finite local centre-pattern reading.
- Change the site action to a nonlinear representation. This changes the candidate law and needs its own four-test assessment.

> [CG16B.md:110](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16B.md:110): “remains on `T` at every tick.”

Finite centre-defect patterns remain pinned when the complete tick preserves the local gauge generators.

**Imports:** The bilinear site representation; exact local gauge covariance; the finite-pattern charge reading.

### N4 — Odd local gauge invariants and finite localized charges

> [RCS1.md:70](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCS1.md:70): “Every `A∈𝔄^G` is matter-even.”

**Status:** REFUTED — RCS1, Theorem 4.

**Blocked statement.** A local invariant odd composite supplies the charged fermion.

**Weakest surviving change.** Construct a charged field extension or a superselection-sector prescription.

> [RCS1.md:64](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCS1.md:64): “no such translation is implemented in `π`.”

**Additional blocked variant.** A factor sector with finite odd relative centre support moves by ordinary translations.

**Load-bearing hypotheses.** Finite localization. Factor representations. A cell-periodic sharp background. Odd relative parity.

**Surviving variant.** Non-finitely-localized charged sectors remain available for construction.

> [CG16D.md:41](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16D.md:41): “For any `Spin(20)` register” the endpoint product is \(1\).

Changing the Spin(20) irrep alone does not remove that link-purity identity.

> [CG16D.md:45](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16D.md:45): “every `Φ_Λ=1`.”

On the stated \(S_+\) register, the specified negative-flux spinor sector is absent. A different charged identification remains a separate target.

**Imports:** RCS1’s centre identity; CG16D’s commuting endpoint actions and link-purity hypotheses.

### N5 — An empty-state finite-depth one-particle route

> [CG16S.md:114](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16S.md:114): “their net chirality is zero.”

**Status:** REFUTED — CG16S, Theorems 8–9 and Lemma RC-W.

**Blocked statement.** The specified empty-state one-particle walk has a net chiral Weyl spectrum.

**Load-bearing hypotheses.** Every gate preserves the empty vector and the one-site excitation subspace. The induced walk is a finite product of bounded local blocks. The node set consists of finitely many Weyl points.

**Weakest surviving change.** Use an interacting or filled background for which condition E fails. Prove its many-body infrared limit.

Adding more finite-depth layers does not remove RC-W. Intermediate translation covariance was not required.

> [CH1.md:84](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:84): “only at a quasi-free endpoint.”

CH1’s endpoint obstruction must retain that qualification.

**Imports:** Condition E; finite-component Bloch representation; the stated node regularity.

### N6 — Gatewise nonlinear frames

> [CG16B.md:43](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16B.md:43): “The whole-tick question is LW1-5-T.”

**Status:** REFUTED — CG16B, Corollary 2.3, for its gatewise compatibility target.

**Load-bearing hypotheses.** The named cube generator, or a cube gate outside the stated exceptional set, must preserve the frame gate by gate.

**Weakest surviving change.** Require compatibility of the complete tick. NN-a already permits gauge-variant intermediate factors. The actual complete-tick compatibility theorem remains open.

**Imports:** Faithful one-mode inflow; LW1_5’s frame theorem; the specified exceptional-angle qualifications.

### N7 — Particular disjoint block encodings

> [CG16K.md:39](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16K.md:39): “an equal-size partition into 5, 7 or 16 sites per coarse site is impossible.”

**Status:** REFUTED — CG16K, Theorems 2.1 and 2.3.

**Load-bearing hypotheses.** Disjoint finite blocks. The specified equivariance between two cubic structures. The required full stabilizer action. Equal block size for the stated exclusions.

**Weakest surviving change.** Change the geometric encoding hypothesis that creates the orbit or density obstruction. An overlapping or nonfactorizing encoding needs a new algebraic construction. A permitted larger block still needs a carrier theorem.

> [CG16K.md:142](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CG16K.md:142): “selection is supplied.”

The K27 comparison does not derive its selected dials.

**Imports:** CG16K Definitions 1–2 and 7; cubic equivariance; finite disjoint supports.

### N8 — Rigid rays and the specified finite-range backgrounds

> [RCSPC.md:67](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCSPC.md:67): “Then no band has a Clifford node.”

**Status:** REFUTED — RCSPC, Theorem 1, for its rigid-label cone target.

**Load-bearing hypotheses.** Orthogonal labels. The specified finite orbit structure. Translation stabilizers of rank at most two. Tick permutation of those labels.

The tick may move labels. That allowance does not remove the obstruction.

> [RCSPO.md:87](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/RCSPO.md:87): “If the positive-weight condition holds” in every transverse residue class, “no” such representation has a Clifford node.

**Additional blocked variant.** The stated factor ray sectors over \(SRE_{k,D}\) backgrounds.

**Exact additional hypothesis.** The relevant local projection has positive weight on an axial parity in every transverse residue class. This hypothesis must not be dropped.

**Weakest surviving change.** Construct transverse intertwiners in a background outside the proved disjointness setting. Node Q must establish those intertwiners. A superposition of unchanged orthogonal ray labels is insufficient.

**Imports:** RCSPC’s label structure; RCSPO Theorem 4.1 and Corollary 4.2; the stated ray limits.

### N9 — A unique whole-system gap at half filling

> [SMG15.md:104](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:104): “uniform gap.”

**Status:** REFUTED — SMG15, Theorem 5, for a unique uniformly gapped whole chain under its hypotheses.

**Load-bearing hypotheses.** Fixed-range local Hamiltonian. One-site translation. Number conservation. The specified \(S\) and Gauss symmetries. Half filling.

**Weakest surviving change.** Seek a gap in the charged mirror sector while retaining neutral low-energy states. This changes the desired conclusion. It needs no change to the rung’s law.

**Imports:** Theorem 5’s twist construction and filling assumptions.

### N10 — A dressed Hamiltonian declared to be R-GEN

> [SMG15.md:122](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:122): “not the R-GEN generator of any certified NN-a decomposition.”

**Status:** REFUTED — SMG15, Theorem 6 and its generator-scope amendment, for the stated dressed Hamiltonian.

**Load-bearing hypothesis.** Every certified \(X_g\) belongs to one edge-triple algebra. The dressed Hamiltonian develops support outside a sum of those algebras.

**Weakest surviving change.** Evaluate the actual certified sum. Prove its state and gap properties. Exact conjugation of another Hamiltonian does not supply those properties.

Changing the permitted generator support would require a new reading.

**Imports:** HGEN; the specified dressing; the nonzero-hopping support calculation.

### N11 — Unrestricted window and fixed-parity comparisons

> [SGAP.md:147](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP.md:147): “`λ_min(K+B)=λ_min(K)` exactly.”

**Status:** REFUTED — SGAP, A5 counterexample.

**Blocked statement.** The unrestricted local window gains a strictly positive energy under the charge-changing conjugation.

**Load-bearing hypothesis.** The window space is preserved by that conjugation.

**Weakest surviving change.** Retain the global sector constraint in the comparison.

> [SGAP.md:149](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP.md:149): “A per-sector half-filled charged-versus-neutral gap is false.”

**Additional blocked variant:** SGAP, Proposition 4.1.

**Weakest surviving change.** Compare with the true global neutral minimum. P7 does this at \(t=0\).

> [SGAP.md:141](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP.md:141): “This does not disprove that bound.”

The extensive odd-weight result does not itself refute \(W_{\rm odd}\leq Kw\). The missing localization estimate remains a possible route.

**Imports:** The exact charge-changing unitary; the supplied parity decomposition; unrestricted-window unitary equivalence.

## Literature programmes

“Corpus checked” below concerns the cited source record and locator. It does not mean that an external theorem has been independently rebuilt.

**FROM MEMORY** marks every programme whose cited locator was not checked in the supplied corpus. Where stated, its primary locator was checked online.

| ID | Programme and exact anchor | Scope used here |
|---|---|---|
| **LFK** | Fidkowski–Kitaev, 2009/2010, [arXiv:0904.2197v3](https://arxiv.org/abs/0904.2197v3), Eqs. (8), (11), §II.A. | Exact atomic interaction and interacting-chain programme. Corpus anchor: [SMG1.md:59](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:59), “term by term”. |
| **LFP** | Fröhlich–Pizzo, 2018/2020, [arXiv:1812.02457v2](https://arxiv.org/abs/1812.02457v2), Theorem 3.5; hypotheses (1.4), (1.6), (1.7). | Stability about a unique product ground state. Corpus anchor: [SMG1.md:122](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:122), “The theorem is cited, not rebuilt”. |
| **LY** | Yarotsky, 2004, [arXiv:math-ph/0411042](https://arxiv.org/abs/math-ph/0411042), Theorems 1–3, Eqs. (3)–(6). | Product-state stability and thermodynamic ground-state construction. Corpus anchor: [the gap note:36](/Users/jonreilly/toe-lap/ref/main/docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:36), “Theorems 2–3 supply the thermodynamic ground-state limit”. |
| **LPOL** | Fernández–Procacci, 2006/2007, [arXiv:math-ph/0605041v2](https://arxiv.org/abs/math-ph/0605041v2), Eq. (2.13). | Polymer convergence programme. For this tree, the accepted estimate is SGAP0’s native rebuild: [SGAP0.md:78](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP0.md:78), “The proof above is the input”. |
| **LSW** | Bravyi–DiVincenzo–Loss, 2011, [arXiv:1105.0675](https://arxiv.org/abs/1105.0675), Theorems 2–3; Eqs. (4.29)–(4.33). **FROM MEMORY; primary locator checked online.** | Local Schrieffer–Wolff expansions and linked clusters. A defect-relative bound beside a gapless bath is a new obligation. |
| **LRG1** | Benfatto–Mastropietro, 2009/2010, [arXiv:0907.2837](https://arxiv.org/abs/0907.2837), Theorem 1.1; Eqs. (14)–(18). **FROM MEMORY for these locators; primary checked online.** | Constructive one-dimensional infrared analysis. Its transfer is explicitly pending: [SMG15.md:144](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:144), “full hypotheses and transfer … are not checked here”. |
| **LNULL** | Wang–Wen, first posted 2013, published 2023, [arXiv:1307.7480v6](https://arxiv.org/abs/1307.7480v6), Eqs. (6), (7); Appendices C–D. **FROM MEMORY for these locators; primary checked online.** | Primitive null-lattice boundary gapping. Microscopic realization and the native gap estimate remain separate. |
| **LSTRIP** | Zeng–Zhu–Wang–You, 2022, [arXiv:2202.12355v2](https://arxiv.org/abs/2202.12355v2), Eqs. (1)–(3). | A mirror-boundary design. Corpus anchor: [LIT_SMG.md:168](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:168), “Finite-size data … do not prove a thermodynamic gap”. |
| **LRG2** | Giuliani–Mastropietro, 2008/2009, [arXiv:0811.1881v2](https://arxiv.org/html/0811.1881v2), Theorem 1; Eqs. (2.10)–(2.11). **FROM MEMORY; primary locator checked online.** | Stability of weakly interacting two-dimensional Dirac correlations. This does not remove mirrors. |
| **LRG3** | Mastropietro, 2013, [arXiv:1310.5638](https://arxiv.org/abs/1310.5638), unnumbered theorem in §II; Eqs. (16)–(18). **FROM MEMORY; primary locator checked online.** | Controlled Weyl singularities with weak interactions. The supplied model has paired Weyl nodes. |
| **LWW** | Wang–Wen, 2018/2020, [arXiv:1809.11171v3](https://arxiv.org/abs/1809.11171v3), Propositions 1–2; Eqs. (9), (13)–(16). | Anomaly and gapped-boundary programme. Corpus anchor: [LIT_SMG.md:34](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:34), “Proposition 2, explicitly introduced as an assumption”. |
| **LKIK** | Kikukawa, 2017/2019, [arXiv:1710.11618v5](https://arxiv.org/abs/1710.11618v5), Eqs. (3.2)–(3.7), (3.25), (3.68), (7.1). | Invariant mirror vertices and a chiral-measure construction. Corpus anchor: [LIT_SMG.md:134](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:134), “There remains the issue of smoothness/locality”. |
| **LAN** | García-Etxebarria–Montero, 2018/2019, [arXiv:1808.00009v3](https://arxiv.org/abs/1808.00009v3), Eqs. (3.19), (3.24), (3.25), (3.70), (4.14)–(4.16). | Dai–Freed anomalies and bordism calculations. Corpus locator: [LIT_SMG.md:7](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:7), “Exact anchors”. |
| **LGS** | Golterman–Shamir, 2025/2026, [arXiv:2505.20436v3](https://arxiv.org/abs/2505.20436v3), §III unnumbered theorem; Eqs. (1.1), (3.1)–(3.7). | A conditional interacting doubling test. Corpus anchor: [LIT_SMG.md:144](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:144), “a complete set of interpolating fields … has no zeros”. |
| **LALG** | Buchholz–Verch, 1995, [arXiv:hep-th/9501063](https://arxiv.org/abs/hep-th/9501063), Lemma 3.1; Eqs. (3.7)–(3.10), (3.17), (3.19). **FROM MEMORY; primary locators checked online.** | Scaling algebras. A lattice infrared version with charged sectors is new work. |
| **LINT** | Vanicat–Zadnik–Prosen, 2017/2018, [arXiv:1712.00431v2](https://arxiv.org/abs/1712.00431v2), Eqs. (3), (4), (7), (8). **FROM MEMORY; primary locators checked online.** | Integrable brickwork dynamics and transfer matrices. Its conserved charge need not equal the certified R-GEN sum. |
| **LSECT** | Naaijkens, 2010/2011, [arXiv:1012.3857](https://arxiv.org/abs/1012.3857), Proposition 3.4, Eq. (3.1); Theorem 3.7, Eq. (3.2). **FROM MEMORY for these locators; primary checked online.** | Cone-localized sectors in a two-dimensional model. Three-dimensional fermionic multiplets require a new construction. |

## Open frontier

### C — A native spectral carrier and interaction

> [CH1.md:244](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:244): “No proof binds the required composites into a chiral spectrum or gaps their mirrors.”

**Statement.** Construct a native carrier whose odd \(D\)-operators have nonzero spectral weight. Construct symmetry-preserving interactions on that carrier. Relate those interactions to actual edge-triple generators.

The first finite target is a full-rank Gram matrix for the proposed charged operators in a specified symmetric state. The next target is a nonzero transport matrix element. Neither target asserts chirality.

**Status:** OPEN.

**Children:** P8, P9.

**Imports:** H5, HCAR, HG, HNN, HCOV; N3–N7; LKIK, LSW.

**Preferred route — Native U(5) composites.** Use P8. Pull back the spinor invariant tensors to

\[
R_u=10_u\oplus\overline5_{-3u}\oplus1_{5u},
\qquad u=-3.
\]

Construct the charge-balanced channels \(A^3B\) and \(AB^2C\) from the actual composite operators. Compute their invariant matrix elements exactly. Then construct an allowed local generator that induces the required interaction.

> [LIT_SMG.md:82](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:82): “A mass at fixed nonzero `Phi` does not prove a gap after its orientation fluctuates.”

**First hard step.** Obtain a nonzero native carrier and interaction without replacing its composite algebra by canonical sixteen-mode CAR.

**Smallest rung.** The finite star supporting P8’s singlet. Prove the charged Gram matrix and one adjacent-star transfer identity by representation theory and exact CAR algebra.

**Programme:** LKIK’s invariant vertices, followed by a new native realization.

**Second route — An encoded low-energy carrier.** Construct a finite-block low-energy subspace from the existing registers. Derive its representation and matrix elements. Use perturbative gadgets only with a uniform error bound.

**First hard step.** Prevent unwanted block states from carrying additional low-energy channels. Preserve the required geometric covariance.

**Smallest rung.** Two adjoining blocks with one shared link. Prove their low-energy operator algebra and one generator identity exactly.

**Programme:** LSW. P9 supplies a compilation comparison. N10 still requires checking the actual R-GEN sum.

The exact Spin(10) branch additionally needs a carrier outside N3’s local bilinear obstruction. Q is a possible source of such a carrier.

### A — The actual anomaly problem

> [CH1.md:226](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:226): “The interacting flux-flow and infrared bridges remain open.”

**Statement.** Identify the exact global symmetry and its fermion-parity relation. Identify the allowed background bundles. Prove the relevant anomaly statement for \(D\). Prove the microscopic-to-infrared matching theorem used in the construction.

Anomaly cancellation is a compatibility condition. It is not a mirror-gap theorem.

**Status:** OPEN.

**Children:** P8.

**Imports:** HG; the actual parity action; the declared background category; LAN, LWW, LKIK.

**Preferred route — Direct anomaly calculation.** Compute the local anomaly polynomial. Compute the remaining exponentiated eta invariant on the actual bordism group. Then establish matching through the massive elimination map.

**First hard step.** Determine which bundles and tangential structures the microscopic charged prescription realizes. Ordinary Spin backgrounds and a parity-identified quotient cannot be interchanged.

**Smallest rung.** \(R_{-3}\) on ordinary Spin four-manifolds with arbitrary U(5) bundles. Include bundles that do not split into an SU(5) bundle and a line bundle.

**Programme:** LAN.

**Second route — Pullback from Spin(10).** Construct the explicit lift \(f_u:U(5)\to\operatorname{Spin}(10)\). Use naturality of the anomaly. Rebuild the parity-quotient case separately.

> [LIT_SMG.md:62](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:62): “it is **not** an embedding of the exact gauge group.”

**First hard step.** Retain the kernel and all U(5) bundle sectors. Then connect the continuum calculation to the actual microscopic measure or response.

**Smallest rung.** For \(u=-3\), use \(W_u=E\otimes\det E\). Check the lift, its kernel, and the pulled-back spinor representation by exact weight calculations.

**Programme:** LWW and LAN. LKIK offers a possible measure-level matching route.

### H — Native periodic and infinite-chain stability

> [SMG1.md:122](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:122): “R1-H retains the native proof and ring and infinite-chain versions.”

**Statement.** Extend the isolated mirror-chain stability result to the stated periodic and infinite-volume settings. Prove the GNS gap with its domain and uniqueness claims.

This node retains the fifth-mode penalty. It is not a gapless-bath theorem.

**Status:** OPEN.

**Children:** P1–P4.

**Imports:** HGEN; the supplied isolated-chain interaction; LFP, LY.

**Preferred route — Local Lie–Schwinger construction.** Rebuild the convergent local block diagonalization with boundary-independent estimates. Treat the periodic closing bond explicitly. Construct the infinite-volume ground state and generator.

**First hard step.** Control the periodic boundary and gauge sectors without turning a local estimate into a volume-dependent remainder.

**Smallest rung.** An even ring with one closing bond added to the open-chain construction. Keep the full parameter interval symbolic.

**Programme:** LFP, Theorem 3.5.

**Second route — Product-state stability.** Put the atomic Hamiltonian into the precise product-state stability hypotheses. Use bounded perturbation estimates. Derive the thermodynamic state and its GNS gap.

**First hard step.** Verify the physical gauge-sector and boundary hypotheses of the imported theorem.

**Smallest rung.** One atomic cell with its assigned link, followed by one interacting bond.

**Programme:** LY, Theorems 1–3.

### S — S-GAP at nonzero hopping

> [SGAP0.md:164](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SGAP0.md:164): “S-GAP at `t≠0`.”

**Statement.** For the specified gauged ring Hamiltonian

\[
H_\epsilon=
\tau\sum_x(W_x+14)
-t\sum_x\operatorname{hop}_x
+\epsilon\sum_{x,a}
i\gamma_{x,a}\gamma_{x+1,a}\operatorname{hop}^{0}_x,
\]

prove that there exist \(c_0,\Delta>0\), independent of \(L\), such that

\[
|t|,|\epsilon|\leq c_0\tau
\quad\Longrightarrow\quad
E_\chi(H_\epsilon)\geq E_0(H_\epsilon)+\Delta\tau
\]

for every allowed nontrivial \(S\)-character.

Retain \(L\in4\mathbb N\), \(L\geq8\), \(N=L/2\), and \(\tau_E=0\).

**Status:** OPEN.

**Children:** P5, P6, P7.

**Imports:** The SGAP model; global \(S\)-sectors; P7’s cancellation mechanism; LPOL, LSW.

**Preferred route — Cancel the neutral bath before estimating it.** Represent charged and neutral partition functions in a common expansion. Cancel histories that do not detect the charged insertion. Bound the remaining charged histories with fermionic determinants retained.

The desired estimate is a sector-energy comparison. A bound on each extensive vacuum energy separately is too weak.

**First hard step.** Prove a summable charged-history bound when the light propagator has algebraic tails. Absolute values taken before cancellation can destroy the estimate.

**Smallest rung.** One charged winding history with arbitrary free light propagation. Bound its normalized weight uniformly in ring length and inverse temperature. Then include two connected charged histories.

**Programme:** P7’s native polymer proof and LPOL, extended to a moving fermion bath.

**Second route — A defect-relative operator inequality.** Construct a local Schrieffer–Wolff expansion. Compare charged and neutral minima through a remainder controlled by the charged defect content.

**First hard step.** Obtain a defect-relative remainder. The usual extensive operator-norm remainder does not suffice. The gapless light spectrum also prevents assuming an isolated global low-energy block.

**Smallest rung.** A two-bond charged cluster coupled to an arbitrarily long free light chain. Prove the inequality before attempting all connected clusters.

**Programme:** LSW, Theorems 2–3.

**Boundary.** This node covers a small square in \((t,\epsilon)\). It does not assert a Luttinger liquid throughout that square.

### D — The light theory beside the gap

> [SMG15.md:144](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:144): “The ratio `ε²/(τ|t|)` is a useful proposed weak-interaction diagnostic.”

**Statement.** In an explicitly bounded wedge with \(t\neq0\), prove a controlled effective light action for the coupled model. Prove its infrared correlations. Retain a positive charged mirror gap in the same model.

A natural first domain is

\[
\frac{|t|}{\tau}\ll1,\qquad
\frac{|\epsilon|}{\tau}\ll1,\qquad
\frac{\epsilon^2}{\tau|t|}\ll1.
\]

The constants and inequalities must be supplied by the proof.

**Status:** OPEN.

**Children:** P5, P6.

**Imports:** The same coupled Hamiltonian; the chosen filling prescription; HGEN; LRG1, LSW.

**Preferred route — Massive integration followed by constructive RG.** Integrate mirror fluctuations with uniform connected-kernel bounds. Retain the induced density interaction from P6. Apply a constructive one-dimensional analysis to the resulting weak light interaction.

**First hard step.** Bound the induced retarded and higher-body kernels in the norms required by LRG1. The second-order coefficient alone does not establish those hypotheses.

**Smallest rung.** Prove the connected four-light-field kernel and its remainder bound. Check the chemical-potential and current Ward identities.

**Programme:** LRG1, Theorem 1.1.

**Second route — Local operator reduction.** Construct a quasi-local effective light Hamiltonian with a controlled local norm. Compare it with the exact configuration-conserving benchmark. Transfer its correlations through the dressing.

**First hard step.** Control the dressing of observables and the remainder uniformly in volume and infrared scale.

**Smallest rung.** A finite-support light observable through fourth order, with a bound on the uncomputed tail.

**Programme:** LSW followed by LRG1.

The wedge may exclude an ordered regime near \(t=0\). A charged gap can survive there without a gapless light bath.

### R2 — A chiral one-dimensional rung

> [CH1.md:116](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/CH1.md:116): “CH1C1.”

**Statement.** Construct an anomaly-free chiral \(1+1\)-dimensional theory on a native finite carrier. Gap its mirror sector by symmetry-preserving interactions. Prove the retained chiral correlations and the required census.

Use charges \(L=(1,7)\), \(R=(5,5)\) as a first candidate.

**Status:** OPEN.

**Children:** P2, P8 as separate algebraic comparisons.

**Imports:** HNN and HGEN in one dimension; an actual charged carrier; LNULL, LSTRIP, LRG1.

**Preferred route — Primitive null interactions.** Begin with

\[
K=\operatorname{diag}(1,1,-1,-1),\qquad
q=(1,7,5,5)^T,
\]

\[
B=
\begin{pmatrix}
1&2&2&1\\
2&-1&1&-2
\end{pmatrix}.
\]

The following hand identities give a concrete algebraic rung:

\[
BKB^T=0,\qquad BKq=0,\qquad q=3\ell_1-\ell_2.
\]

The maximal minors are

\[
(-5,-3,-4,4,-3,-5).
\]

Their gcd is \(1\). The null lattice is primitive.

With vertices \(e^{i\ell^T\phi}\), the free scaling dimensions are

\[
\Delta_{\ell_1}=\Delta_{\ell_2}
=\frac12(1+4+4+1)=5.
\]

Both vertices are irrelevant at the free point. Repeated fermions require point splitting. The microscopic interaction must reproduce that structure.

**First hard step.** Realize the charged fields and a positive forward-scattering metric that makes both null vertices relevant. Preserve locality and primitivity.

**Smallest rung.** The native operator realization of these two vertices. Then prove a mirror-sector gap in a controlled parameter domain.

**Programme:** LNULL, Eqs. (6)–(7). LRG1 supplies a subsequent infrared comparison programme.

**Second route — A finite-width boundary regulator.** Separate retained and mirror modes in a strip. Add explicit mirror interactions. Track the full boundary Green matrix during gapping.

**First hard step.** Prevent the mirror from reappearing at a displaced interface or at another quasienergy.

**Smallest rung.** One finite-width strip with every boundary included. Prove a uniform mirror estimate while a retained pole has nonzero residue.

**Programme:** LSTRIP’s design and LKIK’s projector construction.

> [prior/SMG15.md:49](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/prior/SMG15.md:49): “moves one layer in.”

That recorded failure supplies a specific interface test. It does not establish a general boundary obstruction.

### R3 — A two-dimensional selective rung

> [SMG1.md:136](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:136): “R3-H” and “R3-D.”

**Statement.** Construct a \(2+1\)-dimensional native model with a symmetric massive sector and a controlled gapless fermion sector. Prove selectivity and account for every low-energy channel.

**Status:** OPEN.

**Children:** P2; P6 as a coupling diagnostic.

**Imports:** A specified two-dimensional carrier; exact target symmetry; LRG2, LKIK, LWW.

**Preferred route — Massive atoms coupled to a Dirac bath.** Extend the charged-cluster estimate to two spatial dimensions. Integrate the massive sector. Use constructive Dirac RG for the retained fields.

**First hard step.** Preserve the mirror estimate under coupling to the bath. Prove that the induced interaction lies in the required weak-coupling class.

**Smallest rung.** One charged cluster in a free two-dimensional Dirac bath. Establish the connected-kernel bounds before proving the full lattice result.

**Programme:** LRG2, Theorem 1, combined with the native atomic and cluster constructions.

**Second route — An invariant vertex or boundary construction.** Build a two-dimensional interaction from the actual symmetry tensors. Prove its local spectrum and its selective extension across the lattice.

**First hard step.** Preserve the exact charge symmetry of the native carrier.

> [LIT_SMG.md:158](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:158): “The charge U(1) symmetry is explicitly broken.”

The SU(4) quartet comparison of You–He–Xu–Vishwanath, 2017/2018, [arXiv:1705.09313v2](https://arxiv.org/abs/1705.09313v2), Eqs. (1)–(3), therefore needs a new charge-preserving interaction before use in exact U(5).

**Smallest rung.** One finite cell with a charge-balanced quartic and an analytically computed spectrum.

**Programme:** That atomic construction, extended through LKIK’s invariant tensors. The extension remains a proposed proof route.

### M — Selective SMG in three spatial dimensions

> [SMG1.md:137](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:137): “W2.”

> [LIT_SMG.md:34](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_SMG.md:34): “no explicit, volume-uniform mirror-gap bound for these laws.”

**Statement.** For one constructed three-dimensional law, prove selective massive elimination. Prove the W2.3 Weyl distribution with positive residue. Prove the required mirror estimates uniformly in volume.

The interaction must preserve the actual \(G\). Its gap must concern the actual certified generator. Its light correlations must concern the actual tick and state.

**Status:** OPEN.

**Children:** C, A, V, L, and Q when locally gauged.

**Method children:** H, S, D, R2, R3. These are not automatic dimensional implications.

**Imports:** H5–HL; HAS0; LWW, LKIK, LRG3.

**Preferred route — Native mirror interaction plus controlled infrared analysis.** Use C to obtain exact invariant interactions. Establish massive connected-kernel bounds. Integrate the mirror sector. Prove a Weyl infrared limit for the retained fields.

**First hard step.** Prove selectivity in the actual three-dimensional carrier. A symmetric atomic gap can remove the desired field or expose a displaced partner.

**Smallest rung.** A finite transverse slab with one mirror interaction layer. Compute every interface channel analytically. Then seek a bound uniform in slab width and spatial volume.

**Programme:** LWW for anomaly compatibility; LKIK for invariant tensors; LRG3 for the final weak light-sector analysis.

LRG3 becomes relevant after selective elimination. Its paired-node model does not itself remove a partner.

A U(5) carrier has three inequivalent internal multiplets. One common limiting speed requires a proof. W2.1 by itself does not supply it.

**Second route — Local chiral measure followed by Hamiltonian transfer.** Prove uniform locality and smoothness of the mirror-saturated measure. Build a finite-register Hamiltonian and tick realization. Transfer the correlation and gap estimates.

**First hard step.** Establish the measure-locality estimate represented by LKIK Eq. (7.1).

**Smallest rung.** A fixed class of weak admissible gauge backgrounds with volume-uniform bounds on the mirror contribution.

**Programme:** LKIK.

The subsequent transfer must retain fixed register dimension and finite circuit depth. An auxiliary infinite-width or nonlocal projector limit cannot be left inside the final law.

### V — One state for the generator and the tick

> [SMG1_OWNER_CHECK.md:140](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_OWNER_CHECK.md:140): “Choosing R-GEN does not prove that its gap removes light tick correlations.”

**Statement.** For the selected certified law, construct one pure symmetric state satisfying both

\[
\omega\circ\alpha=\omega
\]

and

\[
\omega(A^*[H_U,A])\geq0
\]

on the declared algebra. Prove the required GNS sector estimates. Relate generator estimates to tick correlations.

**Status:** OPEN.

**Children:** P1, P3.

**Imports:** HGEN; the exact decomposition; the declared purity algebra; LINT, LFP, LY.

**Preferred route — Exact compatible dynamics.** Seek a brickwork construction with an explicit invariant state and exact conserved structure. Compute the principal generators of its actual factors. Check the ground-state inequality for their sum.

**First hard step.** Show that the relevant conserved Hamiltonian is the certified R-GEN Hamiltonian, or prove directly that the same state minimizes both.

**Smallest rung.** One two-site cell followed by the first overlapping bond. Then an infinite chain retaining one light Fermi pair.

**Programme:** LINT, Eqs. (3)–(8).

**Second route — Shared local ground constraints.** Construct local gates preserving a common state. Make their principal generators satisfy a compatible local ground inequality. Prove purity and the sector gap in infinite volume.

**First hard step.** Obtain a nontrivial gapless fermion state compatible with those constraints. Product-state compatibility alone supplies P3 again.

**Smallest rung.** The exact light-ring benchmark, with its generator ground state and tick sea treated as separate objects until equality is proved.

**Programme:** LY and LFP for the ground-state machinery, extended to the shared-state construction.

> [SMG15.md:195](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:195): “P3 (open).”

The half-parity implementability lemma is a concrete purity subproblem for that benchmark.

> [SMG1.md:110](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:110): “locally agrees with the generator ground state to `O(θ)`.”

That FLQ comparison is weaker than an exact common-state theorem. A fixed-step approximation also needs estimates uniform in the scaling time.

### Q — Charged sectors with transverse transport

> [TOE_ASSEMBLY.md:255](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:255): “Charged sectors … get no zoom from this map.”

**Statement.** Construct the charged-sector prescription needed by the locally gauged W2 instance. Prove fermion parity, the internal representation, translation covariance, and a three-dimensional propagating sector.

A field’s transformation law is insufficient. A longitudinal moving string is insufficient.

**Status:** OPEN.

**Children:** P10.

**Imports:** HQ; the actual gauge group and register algebra; N3, N4, N8; LSECT.

**Preferred route — Transportable cone-localized sectors.** Construct localized morphisms of the observable algebra. Prove equivalence under independent transverse translations. Build compatible translation and tick implementers.

**First hard step.** Produce a transverse intertwiner between the proposed sectors. Prove that it survives the infinite-volume limit.

**Smallest rung.** A finite-gauge deconfined-loop model with an exact charged-sector construction. Establish transport in two transverse directions before adding the continuous internal multiplet.

**Programme:** LSECT, Proposition 3.4 and Theorem 3.7.

**Second route — An entangled background with indistinguishable rays.** Construct a background outside N8’s finite-range factorization hypotheses. Prove that changing the string path gives equivalent charged sectors. Derive the resulting transport algebra.

**First hard step.** Establish path independence or controlled transverse equivalence. A declaration that the string is unobservable does not prove this.

**Smallest rung.** Two parallel rays separated by one cell. Construct their intertwiner and prove its norm and covariance identities.

**Programme:** LSECT’s transportability mechanism, ported to the native register model.

For L5-O, the construction must also identify the required internal class. RCSPO’s straight-string parity labels do not themselves supply a local spinor 16.

### L — W2-LIGHT and completeness

> [SMG1_OWNER_CHECK.md:126](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1_OWNER_CHECK.md:126): “It does not establish that every unwanted light sector has such a representative.”

**Statement.** Give a closed mathematical definition of the light-sector census. Prove that the chosen definition detects every additional light sector in the constructed model.

Specify:

- The observable and charged-field classes.
- The admissible normalization functions.
- Every momentum and quasienergy carrier.
- The treatment of composite fields.
- The treatment of static correlations.
- The meaning of completeness.

No equality with a desired infrared theory is assumed.

**Status:** OPEN.

**Children:** N1 as a constraint; P5 as a benchmark.

**Imports:** HL, HQ; the actual tick and state; LALG, LGS.

**Preferred route — A complete scaling algebra.** Define a lattice infrared scaling algebra before studying the candidate. Include demodulated carrier channels. Construct its scaling-limit representations. Prove that the intended Weyl fields generate the complete nontrivial limiting field content.

**First hard step.** Prove coverage. A chosen family of convergent power-normalized two-point functions may omit logarithmic normalizations, composites, or other carriers.

**Smallest rung.** Recover the complete free light theory of P5, including both Fermi points.

> [SMG15.md:174](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG15.md:174): “sampling only the same even sublattice can therefore miss that particular two-point signal.”

The first benchmark must detect that signal through a suitable cell field.

**Programme:** LALG. Its lattice infrared and charged extensions must be proved.

**Second route — A complete spectral-interpolator census.** Construct a complete family of elementary and composite interpolators. Control poles, zeros, spectral thresholds, and all carrier channels. Show that no extra scaling sector remains outside the family.

**First hard step.** Prove completeness independently of the selected \(16\times16\) propagator.

**Smallest rung.** Reconstruct P5’s entire strict-below-threshold spectrum across its symmetry and holonomy sectors.

**Programme:** LGS.

LGS also supplies a sharp compatibility test. Its vector-like conclusion requires its Hamiltonian, continuum, completeness, regularity, and no-zero hypotheses. A proposed chiral construction must establish which of those hypotheses does not apply. A zero in an elementary propagator is not itself a proof of successful mirror removal.

## Candidate specifications and the four tests

> [TOE_ASSEMBLY.md:173](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:173): “It states or fixes something that a part lists as its target.”

> [TOE_ASSEMBLY.md:174](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:174): “It is open-ended.”

> [TOE_ASSEMBLY.md:175](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:175): “It settles a downstream physics question by premise.”

> [TOE_ASSEMBLY.md:176](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:176): “its own reasons do not need.”

Here **P** means pass. **F** means fail. **U** means unresolved and unsuitable for adoption.

| Candidate | 1: target | 2: closed | 3: downstream | 4: necessary | Disposition |
|---|---:|---:|---:|---:|---|
| Name exact symmetry sectors in a fixed rung. Require their R-GEN gap as a theorem. | P | P | P | P | A bounded proof target. It does not identify every mirror. |
| Fix scaling families, channels, and completeness definitions before testing W2. | P | U | P | U | Node L must finish the definition. No replacement is adopted. |
| Assume that the limiting algebra is precisely a free Weyl algebra. | F | P | F | F | This supplies the desired content and stronger higher-correlation structure. |
| Insert sixteen independent local CAR modes with the desired representation. | F | P | F | F | This changes H5 and supplies the carrier target. |
| Use the nonlinear \(S'\) action as a new law premise. | F | P | F | U | It is a useful comparison model. Independent law reasons remain necessary. |
| Replace end-pure links by one explicitly specified end-mixed register. | P | P | P | U | It can remove a pinning hypothesis. Its independent justification remains open. |
| Treat the global-symmetry rung as already proving the locally gauged target. | F | P | F | F | Q and the gauge interfaces remain required. |
| Infer the R-GEN Hamiltonian from an exact circuit compilation. | P | P | F | F | Compute the actual principal-generator sum instead. |
| Identify all proposed string paths by definition. | F | P | F | U | Q must prove the required intertwiners. |

These are assessments of candidate readings. None is an adoption.

## Assembly edges and proof boundaries

> [TOE_ASSEMBLY.md:719](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:719): “All parts are proved for one law `L`.”

The final assembly cannot combine an S-gap on one model, a Weyl pole on another, and a stationary state on a third.

> [SMG1.md:27](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/SMG1.md:27): “separate interfaces.”

| Consumer | What a completed W2 supplies | Further obligation |
|---|---|---|
| **CH1** | A protected chiral fermion sector with selective mirror removal. | Local gauged measure, massless gauge sector, reflection positivity, and the charged correlation prescription. |
| **CG1** | One full family representation with \(\nu^c\), realized dynamically. | Its relation to the operational gauge group and the stated subgroup-selection questions. |
| **MT1** | A candidate odd Weyl sector. | The charged-sector spin and exchange identification in the same construction. |
| **FL1** | One multiplet as a unit for a family construction. | A law-derived family count. |

> [TOE_ASSEMBLY.md:519](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:519): “Three families are not derived.”

> [TOE_ASSEMBLY.md:637](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:637): “T0 is pure gauge.”

Neither family multiplication nor the chiral-matter extension of the pure-gauge theorem is included in W2.

All proposed proof routes use exact algebra, analytic estimates, representation theory, or operator-algebraic limits. Numerical spectra and finite-size fits are not proof inputs. The routes are formulated for eventual Lean formalization. No formalization is claimed.

## Ranking of the open leaves

This order weighs movement of the wall against proof plausibility. The assessments concern the stated nodes. A small successful rung does not inherit the full node’s conclusion.

| Rank | Leaf | Movement on success | Proof plausibility |
|---:|---|---|---|
| **1** | **S — Nonzero-hop S-GAP** | Establishes robust mirror charge protection beside moving light degrees of freedom. | Medium. P7 gives an exact cancellation mechanism. Moving-bath estimates are new. |
| **2** | **C — Native carrier and interaction** | Connects the exact target symmetry to the microscopic register algebra. | Medium for the finite carrier and vertex rung. Lower for a propagating spectral realization. |
| **3** | **V — Generator/tick compatibility** | Makes gap estimates relevant to the law’s actual state and dynamics. | Medium for decisive benchmark results. Low for a general exact construction. |
| **4** | **R2 — Chiral one-dimensional rung** | Establishes genuine selectivity with an anomaly-free chiral remainder. | Low to medium. The primitive null lattice is explicit. Its native strong-coupling realization is open. |
| **5** | **D — Controlled light theory** | Converts a mirror gap into a usable effective infrared theory. | Medium in a bounded weak-interaction wedge. |
| **6** | **A — Anomaly and matching** | Removes a precise symmetry obstruction and validates the chosen group. | Medium for continuum anomaly calculations. Lower for the microscopic matching bridge. |
| **7** | **H — Native isolated-chain stability** | Completes a clean analytic benchmark and GNS input. | Relatively high. Its direct movement toward selective chirality is limited. |
| **8** | **R3 — Two-dimensional selectivity** | Tests the mechanism beyond one dimension. | Low to medium once C and massive-kernel estimates exist. |
| **9** | **Q — Transverse charged sectors** | Removes a direct obstruction to using the locally gauged carriers. | Low for the target multiplet. A finite-gauge transport rung is more accessible. |
| **10** | **L — Complete light census** | Supplies the missing meaning and proof of “every mirror and doubler.” | Medium for a closed benchmark criterion. Low for general completeness. |

## Lane brief 1 — S

**Deliverable.** Prove the stated S-GAP inequality for a nonzero neighbourhood in \((t,\epsilon)\), uniformly in allowed ring length. Preserve the canonical sector and every allowed nontrivial character.

Start from P7’s cancellation of neutral histories. Normalize by the full moving-light partition function before taking absolute values. Seek an estimate tied to charged histories.

**Stopping rule.** Stop at a proof, an analytic counterexample, or one explicit residual lemma after these three attacks fail:

1. A charged polymer ratio with fermion determinants retained.
2. A defect-relative local Schrieffer–Wolff inequality.
3. A sector-aware localized charge-removal comparison.

Record the failed estimate and its parameter domain. Do not replace the full square by a weak-interaction wedge without naming the weaker theorem.

## Lane brief 2 — C

**Deliverable.** On the native \(2\leq m\leq8\) U(5) carrier, construct a symmetric finite-support state and the complete charged operator family. Prove a full-rank Gram matrix. Produce one nonzero transport matrix element and one charge-balanced interaction identity.

Keep the composite operator algebra explicit. Supply actual edge-triple generators before attaching an R-GEN claim.

**Stopping rule.** Stop at the stated carrier theorem, an exact representation or locality counterexample, or one residual lemma after these three attacks fail:

1. An invariant-projector construction on the native star.
2. A pulled-back Kikukawa vertex calculation.
3. A two-block effective encoding with a controlled local remainder.

A successful finite carrier is a new input to M. It does not establish a chiral pole.

## Lane brief 3 — V

**Deliverable.** Construct or rule out an exact common generator-ground and tick-stationary state for one explicit coupled rung. State the purity algebra. Prove the relevant GNS domain and sector estimate.

Fix the circuit decomposition first. Compute every principal generator. Compare the resulting state with the tick sea without assuming equality.

**Stopping rule.** Stop at a common-state theorem, an analytic counterexample for the candidate, or one residual compatibility lemma after these three attacks fail:

1. Shared local ground constraints.
2. An integrable brickwork transfer-matrix construction.
3. Exact circuit conjugation with complete principal-log accounting.

If exact compatibility fails, state the weaker comparison actually proved. A local \(O(\theta)\) comparison requires a further bound before use at scaling times.