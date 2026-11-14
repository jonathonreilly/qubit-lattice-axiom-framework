**Proof tree, sketched (owner 2026-11-08: "do more physics on astra max for sketching the proof trees").** Written by Codex gpt-6-astra at max effort, read-only, on the laptop; finished 2026-11-08T21:39:07Z. Template `~/toe-lap/tmpl/treeGB1.txt`. A sketch: no node below is proved by this file, and nobody has checked it. Statuses quote the frozen parts.

# W1 — GB1: an exact gauge bridge with a conditional YM4D hand-off

> “equals a named lattice gauge theory” — [TOE_ASSEMBLY.md:466](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:466).

**Status: OPEN.**

The finite quantum-link version remains a target. The full regular-link version has a frozen obstruction.

## Root theorem sought

Let \(\mathscr L_{\mathrm{WS}}\) denote the following class of fully specified laws.

- Space is \(\mathbb Z^3\).
- Each site carries \(F_x=\Lambda\mathbb C^5\).
- Each link carries one fixed finite-dimensional register.
- The register and hopping operators come from an admitted five-mode construction.
- Every gate is even.
- The tick has a fixed finite NN-a decomposition.
- Its depth is independent of volume.
- The complete tick preserves the local gauge action.
- The complete tick commutes with \(\mathscr G=2\mathbb Z^3\rtimes O_{c_0}\).
- The law’s coefficients, gate ordering and representation are fixed.
- A zoom uses the owner’s R-form construction.
- A state \(\omega_0\) is supplied by VC1.
- Its membership in any proposed pure-gauge sector remains a proof obligation.

> “Gauge invariance and cell covariance are required of the complete update only.” — [TOE_ASSEMBLY.md:235](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:235).
>
> “Coarse sites carry the same five-mode construction” — [TOE_ASSEMBLY.md:252](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:252).
>
> “one law `L` … one zoom … one vacuum” — [TOE_ASSEMBLY.md:719](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:719).

Fix an independently defined target \(Q_G\) from this ladder.

| Rung | Named target | Link register | Electric operator |
|---|---|---|---|
| \(\mathbb Z_2\) | Hamiltonian \(\mathbb Z_2\) lattice gauge theory | \(\mathbb C^2\) | \(-X_\ell\) |
| \(U(1)\) | Spin-\(S\) quantum-link gauge theory | \(\mathbb C^{2S+1}\) | \((S_\ell^z)^2\) |
| \(SU(2)\) | Horn–Chandrasekharan–Wiese quantum-link theory | \(R_s=\bigoplus_{k=0}^{s}\mathcal H_k(S^3)\) | \(E_\ell^2|_{\mathcal H_k}=k(k+2)/4\) |

The magnetic operator is the sum of the named oriented plaquette operators. Its implementation as an admissible tick is node **C**. It must include interactions between the original disjoint cubes.

> “the exact regular \(\mathbb Z_2\) link” — [GB1.md:83](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:83).
>
> “the defined matter-coupled U(1) quantum-link model” — [GB1.md:107](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:107).
>
> “the \(SU(2)\) quantum link model of Chandrasekharan-Wiese” — [GB1QL.md:60](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md:60).

For \(G=SU(2)\), prove that there exist one \(\mathcal L\in\mathscr L_{\mathrm{WS}}\), one permitted zoom rung, one finite \(s\), and a map
\[
\Phi:\mathcal B_{Q_G}^{G}\longrightarrow\mathfrak A_{\mathcal L}^{K}
\]
with all the following properties.

1. \(\Phi\) is a unital injective \(*\)-homomorphism.
2. Its range is the independently specified framework link sector.
3. It intertwines the cell actions.
4. It has uniform exponential locality:
   \[
   \forall R_0\ \exists C_{R_0},\xi_{R_0}>0\
   \forall A\in\mathcal B_{Q_G}^{G}(B_{R_0})\
   \forall R\ge0:\quad
   \operatorname{dist}\!\left(\Phi(A),\mathfrak A_{\mathcal L}(B_R)\right)
   \le C_{R_0}e^{-R/\xi_{R_0}}\|A\|.
   \]
   The target neighbourhood is centred on the prescribed image block.
5. For the prescribed number \(b\) of fine ticks,
   \[
   \alpha_{\mathcal L}^{\,b}\circ\Phi=\Phi\circ\alpha_{Q_G}.
   \]
6. The register, Gauss action, electric operators and magnetic operators have an explicit dictionary.
7. The source state is \(\omega_Q=\omega_0\circ\Phi\).
8. A specified generator reading supplies Euclidean correlations of this same state.
9. Those correlations admit the complete YM4D input interface.
10. The observable dictionary identifies the required \(\operatorname{tr}F^2\) hierarchy.
11. The GA2 error estimates hold with the required uniformity.

These are conclusions to prove. They are not added hypotheses.

The exact identities in items 1, 3, 5 and 7 would give zero error in the corresponding invariant two-point comparison. An approximate replacement must instead prove the owner’s bound:
\[
|F_0^T-F_1^T|
\le C_{R_0}\bigl(r^{-2}+tr^{-3}\bigr)M(r,t).
\]

> “It is a success criterion, not a claim that the rate is achieved.” — [TOE_ASSEMBLY.md:244](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:244).

The final implication is conditional on the external T0 construction. It does not prove that construction.

> “T0 remains open.” — [t0-tree.md:8](/Users/jonreilly/toe-lap/ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library/t0-tree.md:8).
>
> “Half B is essential.” — [t0-tree.md:13](/Users/jonreilly/toe-lap/ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library/t0-tree.md:13).

**Children:** **G**, **Z**, **U**, **S**, **N**, **C**, **E**, **V**, **F**, **H**, **RATE**.  
**Alternative candidate branch:** **R**, using a specified growing-register family.  
**Imported hypotheses:** PS-1, PS-5, PS-6, PS-6r; NN-a; ZM1-INV; R-form; class (a), \(p=2\); AS0; VC1; the conditional T0 contract. R-GB1Φ is a candidate interpretation where an external LGT supplies the source algebra.

**Preferred route.** Identify a finite quantum-link sector. Supply a magnetic update that couples cubes. Prove its state enters a pinned RG class. Port the anisotropic constructive programme. The first hard step is **N**, followed by **C**. Start with the \(U(1)\) sector and two neighbouring plaquettes. Programmes: **L-QL**, **L-RISHON**, **L-RG** below.

**Second route.** Use a fully specified family of finite laws. Prove local state and correlator convergence to the regular-link Hamiltonian theory. Then prove heat-kernel admission into the YM4D programme. The first hard step is uniform state control in **R**. Start with one \(U(1)\) plaquette, then two coupled cubes. Programmes: **L-CUTOFF**, **L-QL**, **L-RG**. This route needs an owner-approved change of quantifiers before it establishes the root for one fixed law.

---

## Dependency tree

```text
W1  OPEN
├─ G   PROVED: exact gauge action and NN-a compilation inputs
├─ Z   PROVED: independent five-mode Z₂ benchmark
│  ├─ Z−  REFUTED: its unital readout into the live full invariant algebras
│  └─ ZQ  OPEN: a law-selected quotient or autonomous sector
├─ U   PROVED: finite U(1) quantum-link identities and bounded comparisons
├─ S   PROVED: the so(5) SU(2) test family and its bounded comparison
│  ├─ N−  REFUTED: the specified native growing-block attempts
│  └─ N   OPEN: a native autonomous pure-SU(2) sector
├─ REG− REFUTED: a uniformly local full regular-link readout
├─ CF−  REFUTED: a nontrivial isotropic limit of the scoped cube product
├─ FP   PROVED: full-plaquette counting on the regular-link target
│  └─ C   OPEN: an admissible finite-register cube-coupling update
├─ E    PROVED: the specified finite-box Euclidean lifts
│  ├─ E−   REFUTED: bounded-generator lifts of the specified kind
│  ├─ W−   REFUTED: exact heat-kernel/Wilson-weight identification
│  └─ K−   REFUTED: the specified finite-rank positive-kernel shortcut
├─ V    OPEN: the common state and generator interface
├─ F    OPEN: entry into a controlled window at fixed register
├─ R    OPEN: local state convergence for a growing-register candidate
├─ H    OPEN: anisotropic admission and the complete T0 hand-off
└─ RATE OPEN: GA2 rates and the relative-tail comparison
```

The \(\mathbb Z_2\) and \(U(1)\) rungs test mechanisms. They are not logical implications to the \(SU(2)\) rung.

## G — Gauge structure and compilation

> “Every closed subgroup … has the restricted Gauss law” — [LW1_5.md:149](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LW1_5.md:149).
>
> “every unitary \(G\) … is a finite product” — [GA1_5.md:236](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA1_5.md:236).

**Statement.** The live constructions possess the stated local gauge actions. Finite-support link unitaries admit NN-a compilation. The applicable periodic scheduling gives finite depth.

**Status: PROVED.** `LW1_5.md`, Proposition T and the gauge statements U/R; `GA1_5.md`, Lemma U and Proposition C.

**Children:** none.

**Imported hypotheses:** five-mode CAR algebra; finite link factors; connected compilation support; NN-a; the finite-orbit scheduling hypotheses.

Compilation does not establish covariance of a proposed complete magnetic word.

> “reduces … to gauge invariance and covariance of the full layer” — [GA1_5.md:272](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA1_5.md:272).

## Z — The independent \(\mathbb Z_2\) benchmark

> “The identity readout gives algebra-level equality” — [GB1.md:176](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:176).

**Statement.** The specified five-mode \(\mathbb Z_2\) test law equals the specified matter-coupled \(\mathbb Z_2\) lattice theory. Its pure-link evolution agrees on the empty-matter class.

**Status: PROVED.** `GB1.md`, Theorem 5M, using Theorems 3.2–3.3.

**Children:** **Z−**, **ZQ**.

**Imported hypotheses:** the test-law register \(\mathbb C^2\); its flavour-blind hop; all plaquettes; the specified angles; NN-a’s gate text. Pure evolution additionally imports empty matter.

The pure-sector statement is weaker than full-algebra intertwining.

> “The inclusion fails to intertwine” — [GB1.md:177](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:177).

### Z− — The full-invariant-algebra embedding

> “no unital \(*\)-homomorphism” — [GB1Z2L5.md:59](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:59).

**Statement refuted.**
\[
\exists\ \Phi:\mathcal B_{\mathbb Z_2}^{\mathbb Z_2}
\longrightarrow \mathfrak A_{\mathcal L}^{K}
\quad\text{unital and multiplicative}
\]
for \(\mathcal L=L5\text{-}U[m]\), \(1\le m\le9\), or \(L5\text{-}O[S_+]\), with the full local group \(K\).

**Status: REFUTED.** `GB1Z2L5.md`, Theorems 2–4.

**Children:** **ZQ**.

**Imported hypotheses:** full-group invariants; the stated registers; a global unit; the standard electric–magnetic \(\mathbb Z_2\) source.

The target has a character. The source has none. This obstruction uses neither the tick nor the state.

**Weakest escape from this argument.** Change the codomain to a justified sector quotient. Merely restricting comparison states leaves the algebra unchanged.

> “Restricting the class of states does not change the target algebra.” — [GB1Z2L5.md:63](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:63).

Dropping unitality does not suffice under the stated separating uniform-locality condition.

> “is unital, even if unitality is not assumed” — [GB1Z2L5.md:75](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:75).

### ZQ — A law-selected quotient or autonomous sector

> “GB1-Z2[L5,SEC] remains open” — [GB1Z2L5.md:121](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:121).

**Statement.** A state class selected independently of the desired embedding defines
\[
J_{\mathcal S}=\ker\!\left(\bigoplus_{\omega\in\mathcal S}\pi_\omega\right).
\]
The quotient supports compatible local \(\mathbb Z_2\) electric and plaquette operators. Their dynamics agrees with the specified \(\mathbb Z_2\) tick.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** candidate R-SEC; two-sided tick invariance of \(\mathcal S\); cell invariance of \(\mathcal S\); quotient-norm locality; the required state’s membership in \(\mathcal S\).

**Preferred route.** Start from the proved invariant multiplicity corner. Construct compatible matrix units on overlapping regions. Prove that their units agree in the law-selected quotient. The first hard step is global compatibility of the corner projections. Start with two adjacent plaquettes. Port **L-Z2** and the finite representation algebra of **L-RISHON**.

**Second route.** Construct an autonomous encoded sector directly. Identify its Pauli algebra and prove invariance under every complete tick. The first hard step is simultaneous invariance under matter and magnetic layers. Start with one plaquette and its incident matter factors. Port **L-Z2** and **L-QL**.

A character surviving in the quotient blocks either unital construction.

> “then \(\mathfrak A^G/J_{\mathcal S}\) has a character” — [GB1Z2L5.md:117](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:117).

## U — The \(U(1)\) rung

> “the \(U(1)\) rung at \(S=1/2\) inside the named law” — [GB1.md:184](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:184).
>
> “the error is \(O((\log S)^4/S^2)\)” — [GB1.md:117](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:117).

**Statement.** The specified odd-\(m\) frozen sector of \(L5\)-U gives the spin-\(\tfrac12\) \(U(1)\) quantum-link tick. The separate integer-\(S\) test family approximates the cube-face rotor tick at fixed box, time and flux.

**Status: PROVED.** `GB1.md`, Theorems 5U, 5.1 and 5.2.

**Children:** **REG−**, **F**, **R**.

**Imported hypotheses:** the named frozen spectators; the specified matter class; cube-face magnetism; the flux cutoff; the stated order of limits.

This does not provide an increasing register inside a fixed \(L5\)-U law.

> “does not fit inside one named law, because \(m\) is fixed” — [GB1.md:188](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:188).

## S — The finite \(SU(2)\) quantum-link family

> “For fixed \(\theta\), \(R\), \(n\) and \(M\)” — [GB1QL.md:245](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md:245).
>
> “Every gate … commutes with the \(SU(2)\) gauge action” — [GB1QL.md:299](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md:299).

**Statement.** The specified \(R_s\) test family has exact gauge covariance and an admissible cube-face tick. Matched bounded-flux local correlators converge to the regular-link cube-face theory at rate
\[
O\!\left(\frac{(\log s)^4}{s^2}\right).
\]
The stated local-energy comparison gives \(O(s^{-2/3})\).

**Status: PROVED.** `GB1QL.md`, Proposition 4.2, Theorem 4.8, Corollaries 4.9–4.10 and Proposition 4.11.

**Children:** **N−**, **N**, **R**.

**Imported hypotheses:** the explicit \(so(5)\) representation; matched states on the backward light cone; fixed support and time; bounded flux or the stated local-energy bound; empty matter for the five-mode realisation.

The comparison map is compression. It is not the root’s exact algebra readout. In general,
\[
D_s(AB)-D_s(A)D_s(B)
=\iota^*A(1-\iota\iota^*)B\iota.
\]

### N− — The specified native growing-block attempts

> “the block register then has dimension \(\binom4{m'}\le6\)” — [GB1QL.md:310](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md:310).
>
> “this is the specified Trotterized \(U(2)\) rishon quantum-link model” — [GB1.md:129](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:129).
>
> “the matter-empty frozen class is not invariant” — [GB1.md:163](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:163).

**Statements refuted.**

- The frozen \(L5\)-U block contains the required growing \(SU(2)\) register family.
- Its proved \(U(2)\) identity already identifies pure \(SU(2)\).
- The corresponding empty-matter frozen-spectator construction is invariant under the \(L5\)-O matter layer.

**Status: REFUTED.** `GB1QL.md`, §4.12, step U2 and Proposition 4.12; `GB1.md`, Theorem 6.1 and Lemma O2.

**Children:** **N**.

**Imported hypotheses:** fixed \(m\); R-form; the specified block and spectators; the existing electric term; the existing Majorana hop.

**Weakest escapes.**

- Register growth needs a specified new representation family.
- Removing the extra \(U(1)\) needs a separate mechanism.
- A nonconstant positive \(SU(2)\) electric energy needs a separate operator check.
- The O-law needs a different invariant class or a changed matter coupling.

The electric mismatch is concrete.

> “\(1-(4/3)E_{\ell,x}^2\)” — [GB1QL.md:316](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1QL.md:316).

## N — Native autonomous pure-\(SU(2)\) dynamics

**Statement.** An admitted five-mode law has a prespecified link sector whose register, Gauss action, electric term and complete dynamics identify a pure \(SU(2)\) quantum-link theory.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** **G**, **S**, the limits in **N−**, AS0, and any explicitly proposed representation or sector reading.

**Preferred route.** Use representation branching and invariant multiplicity spaces. Seek an intertwiner for every gate on one common sector. Match the electric operator separately. The first hard step is invariance under both hopping and plaquette dynamics. Start with the smallest two-link matter patch carrying an \(SU(2)\) doublet. Port **L-RISHON** and **L-QL**.

**Second route.** Use the O-law’s summed corner factorisation. Search for a correlated matter–link sector in the joint kernel of the unwanted exchanges. The first hard step is invariance of that kernel under every neighbouring plaquette. Start with one corner, then two faces sharing an edge. Port **L-MAJORANA**.

The second route must use cancellations or correlated states. Termwise annihilation of individual Majorana link entries cannot supply it.

> “a product of entries … has no nonzero kernel” — [GB1.md:149](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:149).

## REG− — The exact regular-link specialization

> “No injective readout … has the uniform exponential locality” — [GB1.md:99](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:99).

**Statement refuted.** A finite-register law admits the root’s uniformly local injective readout from the full regular \(U(1)\) or \(SU(2)\) invariant link algebra.

**Status: REFUTED.** `GB1.md`, Theorem 4.1 and Corollary 4.2.

**Children:** **F**, **R**.

**Imported hypotheses:** source local algebra containing \(B(L^2(G))\); infinitely many invariant Peter–Weyl projections; finite target regions; locality constants uniform over the unit ball at fixed source support.

**Weakest escapes from the stated argument.**

- Replace the exact regular-link source by a finite quantum-link source.
- Replace the exact readout by a quantified low-energy correlator comparison.
- Weaken the locality quantifier explicitly.

The last change removes this argument’s uniformity hypothesis. It does not construct an embedding.

> “an approximate low-flux dictionary, a finite truncation, a different source algebra” — [GB1.md:103](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:103).

## CF− — The original cube-product continuum branch

> “the reconstructed Hilbert space is \(\mathbb C\Omega\)” — [GB1ISO.md:148](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:148).

**Statement refuted.** The specified cube-face lifts yield a nontrivial isotropic scalar-curvature theory under all these hypotheses:

\[
\begin{aligned}
&\text{P1: volume-first states, or controlled torus approximants;}\\
&\text{P2: bounded invariant densities with }a_kr_k\to0;\\
&\text{all-order separated-test convergence;}\\
&\text{OS reconstruction;}\\
&\text{rotation invariance after one fixed }0<c<\infty\text{ time rescaling.}
\end{aligned}
\]

**Status: REFUTED.** `GB1ISO.md`, Theorem 5.2, Extension 1, Corollary R2′ and Proposition R1.

**Children:** **FP**, **C**.

**Imported hypotheses:** disjoint cube factorisation; P1; P2; the stated convergence and symmetry.

**Weakest useful law change.** Add a genuine gauge-invariant interaction between distinct cube factors. Full-plaquette coupling is a concrete candidate.

Changing parameters within the same cube product does not remove factorisation. Leaving P1 or P2 leaves this theorem’s scope. Such a change still needs a separate physical argument.

> “\(Z_k^n\delta^{(k)}\to0\) for every \(n\)” — [GB1ISO.md:143](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:143).
>
> “\(a_kr_k\to0\)” — [GB1ISO.md:144](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:144).

## FP — The regular-link full-plaquette identity

> “Every spatial plaquette occurs twice” — [GB1ISO.md:161](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:161).

**Statement.** For the four translated cube tilings,
\[
W_B^{FP}
=\prod_{v\in\{0,e_1,e_2,e_3\}}\prod_{C\in\mathcal C+v}
e^{-i(\theta/2)B_C}.
\]
On the regular-link target, the multiplication operators commute. Therefore
\[
W_B^{FP}=e^{-i\theta\sum_p B_p}.
\]

**Status: PROVED.** `GB1ISO.md`, Theorem 6.1.

**Children:** **C**, **W−**.

**Imported hypotheses:** the four specified tilings; regular group-valued multiplication operators; the stated plaquette orientation.

## C — Finite-register cube coupling with exact covariance

> “the ordered product’s covariance and exact full-sum form do not follow” — [GB1ISO.md:165](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:165).

**Statement.** Construct a finite-register magnetic update that couples the cube factors, obeys NN-a, and commutes exactly with every required cell symmetry. State its relation to the full quantum-link plaquette Hamiltonian exactly.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** **G**, **FP**, the fixed finite representation, NN-a and the unchanged cell group.

**Preferred route.** Analyse the four-tiling word in the finite quantum-link algebra. Compute its covariance defect symbolically:
\[
D_g(\theta)=\beta_g(W_B^{FP}(\theta))-W_B^{FP}(\theta).
\]
A nonzero Taylor coefficient gives an analytic counterexample to that word. If it fails, seek exact intertwiner relations that permit a different covariant finite word. The first hard step is covariance under a rotation exchanging shifted tilings. Start with spin-one \(U(1)\) links on overlapping plaquettes. Then use the five-state \(SU(2)\) link. Port **L-QL**.

A palindrome cancels some expansion terms. It does not establish exact covariance.

**Second route.** Propose a local Hamiltonian law with
\[
H=\tau_E\sum_\ell E_\ell^2+\theta\sum_p B_p.
\]
Prove gauge symmetry and spatial covariance directly. Use its quasi-local Hamiltonian dynamics. The first hard step is deciding whether the required tick can still have exact finite NN-a depth. Otherwise this is an explicit change of PS-1/NN-a. Start with two overlapping \(U(1)\) plaquettes. Port **L-QL** and **L-CUTOFF**.

The second route must not identify \(e^{-iH}\) with an existing ordered tick without proof.

## E — The Euclidean lift inputs

> “positive injective transfer” — [GB1E.md:60](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:60).
>
> “The exact lift exists” — [GB1E.md:76](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:76).
>
> “reflection positive for coordinate link reflections in all four directions” — [GB1E.md:131](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:131).

**Statement.** The specified regular-link cube-face model has the following finite-box lifts.

| Reading | Supplied object | Proved consequence |
|---|---|---|
| R-SUM | \(H=\tau_EA+\theta H_B\), with the written \(\tau_E>0\) | \(e^{-a_0H}\) has the specified positive-kernel lift. |
| R-IA | One fixed \(\lambda>0\), with \(T_\lambda=e^{-\lambda\theta H_B/2}e^{-\lambda\tau_EA}e^{-\lambda\theta H_B/2}\) | A positive local transfer with temporal heat weights. |

**Status: PROVED.** `GB1E.md`, Theorems 3.1–3.2 and 6.1.

**Children:** **E−**, **W−**, **K−**, **V**, **H**.

**Imported hypotheses:** even spatial side \(N\ge4\); even \(N_t\ge2\); normalized Haar measure; the regular \(SU(2)\) link; positive unwrapped electric coefficient; the specified kernel representation.

The readings remain distinct.

> “R-SUM generally does not satisfy \(e^{-iH}=U_{KS}\)” — [GB1_GEN_OWNER_CHECK.md:7](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1_GEN_OWNER_CHECK.md:7).
>
> “Keep it fixed across the register family.” — [GB1_GEN_OWNER_CHECK.md:38](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1_GEN_OWNER_CHECK.md:38).

### E− — Strict R-GEN and non-strict R3

> “any nonnegative kernel representation has infinite partition integral” — [GB1E.md:103](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:103).

**Statement refuted.** A bounded generator on the regular-link finite spatial box supplies the specified normalized Haar transfer-kernel lift.

**Status: REFUTED.** `GB1E.md`, Theorems 5.1–5.2 and closures R2–R3.

**Children:** none.

**Imported hypotheses:** bounded self-adjoint gauge-invariant generator; infinite-dimensional regular-link Hilbert space; infinite-rank Gauss projector; nonnegative kernel; finite partition integral.

The four readings remain separate branches.

| Reading | Exact issue |
|---|---|
| R-SUM | Requires supplied unwrapped coefficients. |
| R-IA | Requires one supplied positive step per law. |
| Strict R-GEN | Requires \(-1\notin\operatorname{spec}g\) for every gate. Where defined, its finite-box sum is bounded. |
| R3 | Requires uniqueness with \(\|X_g\|\le\pi\). This holds when \(-1\) is not an eigenvalue. Its sum remains bounded. |

> “every gate has \(-1\notin\operatorname{spec}g\)” — [GB1_GEN_OWNER_CHECK.md:50](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1_GEN_OWNER_CHECK.md:50).
>
> “exactly when no gate has eigenvalue \(-1\)” — [GB1_GEN_OWNER_CHECK.md:56](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1_GEN_OWNER_CHECK.md:56).

**Weakest escape.** Supply an unbounded electric-energy reading such as R-SUM, or change the specified representation of the Euclidean theory. A finite register also removes the infinite-rank trace argument. It does not thereby establish a positive group-variable kernel.

No reading is selected here.

> “no reading is adopted, and all four stay live” — [TOE_ASSEMBLY.md:269](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:269).

### W− — Heat weights are not Wilson weights

> “the local lift uses heat weights in time” — [GB1E.md:180](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:180).

**Statement refuted.** Parameter matching makes the temporal \(SU(2)\) heat kernel exactly a Wilson plaquette weight:
\[
k_t(g)=C e^{b\,\operatorname{Tr}g}.
\]

**Status: REFUTED.** `GB1E.md`, Theorem 7.1. The full-plaquette local lift’s exchange-symmetry consequence is `GB1ISO.md`, Theorem 6.1.

**Children:** **H**.

**Imported hypotheses:** \(t>0\); the stated heat kernel; exact equality of class functions; the local R-IA lift.

**Weakest escape.** Prove universality with controlled errors. Alternatively, change the temporal weight as an explicit law choice. Neither escape follows from matching the quadratic smooth-field coefficient.

### K− — The finite-rank kernel shortcut

> “negative on a nonempty open set” — [GB1E.md:186](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:186).

**Statement refuted.** The Peter–Weyl embedding of the finite-register transfer automatically gives a nonnegative group-variable kernel at arbitrarily small Euclidean step.

**Status: REFUTED.** `GB1E.md`, Theorem 8.1.

**Children:** **R**, **F**.

**Imported hypotheses:** the specified finite-rank embedding; its continuous kernel; the theorem’s small-step bound.

**Weakest escape.** Take the controlled register limit before demanding this kernel representation. Another possibility is a separately proved positive blocked kernel. The theorem does not exclude every representation or every step.

A positive-basis shortcut has a different obstruction.

> “a connected group … is trivial” — [GB1E.md:192](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:192).

Theorem 8.2 applies when the nontrivial finite-dimensional gauge representation itself must preserve an orthonormal basis’s nonnegative cone.

## V — One physical state for the tick and Euclidean theory

> “Tick stationarity remains a separate requirement.” — [TOE_ASSEMBLY.md:261](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:261).
>
> “Nor does Theorem 6.1 show that the VC1 vacuum belongs to \(\mathcal S_J\).” — [GB1.md:153](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:153).

**Statement.** The VC1 state belongs to the identified gauge sector. Its Euclidean correlations are those of the selected transfer or Hamiltonian reading. Its integer-tick stationarity is established independently.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** VC1; AS0; the sector from **N** or **ZQ**; one fully specified generator reading; its state-selection rule.

**Preferred route.** Seek an exact common invariant state. On finite regions, compare the tick with the ground-state projection of the supplied Hamiltonian or transfer. Then establish compatible infinite-volume states. The first hard step is
\[
U P_{\mathrm{ground}}U^*=P_{\mathrm{ground}}
\]
for the actual noncommuting layers. Start with a single \(U(1)\) plaquette. Port the Hamiltonian quantum-link programme **L-QL**.

A generic failure on that rung would refute the proposed common-state identification. It would not refute every vacuum prescription.

**Second route.** Use a specified small-step family. Prove local convergence of tick dynamics to Hamiltonian dynamics in a selected ground state. Track the state through the same limit. The first hard step is uniform control as volume grows. Start with two coupled \(U(1)\) plaquettes. Port **L-CUTOFF**.

This second route establishes a limiting statement. Exact stationarity at a fixed nonzero tick remains separate.

## F — A controlled window at fixed register

> “Coherence tending to one in a chosen product state is not a proof of a classical phase” — [GA2_Y2.md:107](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA2_Y2.md:107).

**Statement.** For one fixed admissible law and its selected state, a specified block procedure produces gauge-invariant correlators or integration variables in a pinned weak-coupling RG class. Its errors are controlled on a stated scale window.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** **N**, **C**, **V**; fixed finite register; R-form; a specified observable dictionary; the eventual class and norm from **H**.

**Preferred route.** Decompose block tensor products into gauge representations. Derive a concentration estimate for the selected state on useful representations and coherent configurations. Control the discarded weights. The first hard step is concentration in the actual state. Start with two coupled spin-\(\tfrac12\) \(U(1)\) cubes. Port **L-COHERENT**.

The representation decomposition is kinematics. Concentration is dynamics.

**Second route.** Construct an exact finite-register Euclidean functional. Integrate or block it before introducing group variables. Prove positivity and a controlled local action for those variables. The first hard step is a nonnegative blocked representation that survives the finite-rank obstruction **K−**. Start with one \(U(1)\) plaquette at finite Euclidean time. Port **L-COHERENT** and the transfer construction in **E**.

A strong-coupling result would validate the representation method. It would not yet supply the required weak-coupling window.

The usual dimensional-reduction argument does not supply a fourth Euclidean dimension here.

> “three spatial directions plus one time give three after reduction, not four” — [GB1.md:123](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:123).

## R — Local state convergence for a growing-register candidate

> “The limit is fixed-box, fixed \(a_0,N_t\), then \(s\to\infty\).” — [GB1E.md:206](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1E.md:206).

**Statement.** For a fully specified family with the repaired magnetic interaction, prove local convergence of selected states and Euclidean correlators as \(s\to\infty\). Control volume dependence. State every allowed interchange of limits.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** candidate family \(L[s]\); **C**; positive unwrapped \(\tau_E\); a fixed state prescription; **S**; the fixed-box semigroup theorem `GB1E.md`, Theorem 8.3.

**Preferred route: ground-state compactness.**

Use the zero-flux trial state and the representation-uniform plaquette norm. Seek a cell-orbit bound of the form
\[
\omega_s(E_\ell^2)\le C\frac{|\theta|}{\tau_E}.
\]
This should give local electric-tail tightness. Combine it with finite-flux operator convergence. Pass the ground-state inequality
\[
\omega_s\!\left(A^*[H_s,A]\right)\ge0
\]
to a limit on a local core. Then establish convergence of Euclidean insertions.

The first hard step is controlling the cutoff remainder in this inequality and in multi-time correlators. Start with one \(U(1)\) plaquette. Then treat two coupled cubes. Port **L-CUTOFF**.

The first result may identify subsequential ground states. It must not claim uniqueness or VC1 membership.

**Second route: local Gibbs comparison.**

Compare normalized local expectations through Duhamel expansions or a convergent character expansion. Cancel remote contributions before estimating errors. The first hard step is replacing a global trace-norm bound by a local bound independent of ambient volume. Start in a \(U(1)\) strong-coupling region. Then test the \(SU(2)\) five-state rung. Port **L-CUTOFF** and **L-QL**.

No uniform spectral gap is assumed merely to use an eigenstate-tail theorem.

## H — Anisotropic admission and the complete YM4D hand-off

> “not CA-I’s complete list” — [GB1.md:207](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:207).
>
> “the class and topology must be pinned” — [GA2_Y2.md:178](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA2_Y2.md:178).

**Statement.** The actual measure and observable dictionary satisfy a complete, pinned input theorem. That theorem either admits these starts into the Wilson construction or extends the constructive estimates to them. It supplies the required scalar-curvature theory after a finite positive time rescaling.

**Status: OPEN.**

**Children:** **RATE**.

**Imported hypotheses:** **C**, **E**, **V**; either **F** or the candidate-family result **R**; the complete CA-I `3.1:thm-main` interface; the T0 half-B interfaces; a precisely defined RG norm and trajectory.

The visible interface requires at least the following distinct checks.

| Obligation | Required proof |
|---|---|
| Measure | One normalized four-dimensional gauge-invariant measure. |
| Reference variables | The actual Haar-variable representation. |
| Reflections | The consumer’s complete reflection interface. |
| Action class | Membership in a pinned class and topology. |
| Trajectory | The same coupling and blocking trajectory used by the construction. |
| Observables | The normalized scalar-curvature source dictionary. |
| States | The same selected component through the limits. |
| Uniformity | CT1–CT4 with the required spacing, volume and start independence. |
| Reconstruction | The separate T0 symmetry, clustering and reconstruction inputs. |

This table is not claimed to enumerate the unavailable complete CA-I statement.

**Preferred route: anisotropic constructive RG.**

Start with full spatial plaquettes and temporal heat weights. Introduce separate positive quadratic coefficients \(Z_t,Z_s\). Keep their ratio in a fixed compact positive interval. Rebuild propagator, block, localization and large-field estimates uniformly in that interval. Prove convergence of the renormalized metric. Derive rotational restoration after rescaling.

The first hard step is one RG step with non-Abelian large-field control and source bounds. The smallest analytic rung is noncompact \(U(1)\), with gauge and zero modes removed. Its transverse covariance tests the anisotropic norm:
\[
\bigl(Z_t\widehat p_0^{\,2}+Z_s|\widehat{\mathbf p}|^2\bigr)^{-1}.
\]
Next use compact \(U(1)\). Then use \(SU(2)\). Port **L-RG**.

**Second route: comparison with a Wilson start.**

Match the relevant quadratic parameters. Express the remaining heat/Wilson difference as controlled local interactions. Prove that exact blocking carries this difference into the allowed irrelevant directions. The first hard step is a bound valid outside the small-field chart. A Taylor expansion near the identity is insufficient. Start with one compact \(U(1)\) block. Then prove the corresponding \(SU(2)\) character-tail estimate. Port **L-RG** and **L-CUTOFF**.

Coordinate reflection positivity cannot substitute for missing diagonal-mirror hypotheses.

> “its diagonal-mirror hypotheses are not supplied by axis reflection positivity” — [GB1ISO.md:167](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:167).

Nor may a finite anisotropy be declared harmless by premise.

> “control the anisotropy flow and justify any limiting speed” — [GB1ISO.md:174](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:174).

## RATE — Quantitative delivery to GA2

> “T0 as stated gives existence of a limit, not a rate.” — [TOE_ASSEMBLY.md:638](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/TOE_ASSEMBLY.md:638).

**Statement.** Establish the required scale-dependent correlator errors and running-coupling errors. For an approximate zoom bridge, establish class (a) with \(p=2\). Keep these as distinct estimates.

**Status: OPEN.**

**Children:** none.

**Imported hypotheses:** **H**; its exact observable normalization; its uniform CT bounds; the owner’s full class-(a) quantifiers; **V**.

**Preferred route.** Track irrelevant interactions and observable insertions through every RG step. Separate metric renormalization, field normalization and genuinely irrelevant errors. Prove that the remaining contribution has the required power. The first hard step is controlling marginal logarithms and leading tail data. Start with the free transverse \(U(1)\) theory under one exact block step. Port **L-RG**.

**Second route.** Decompose the error:
\[
\epsilon_{\mathrm{total}}
\le
\epsilon_{\mathrm{state}}
+\epsilon_{\mathrm{register}}
+\epsilon_{\mathrm{time}}
+\epsilon_{\mathrm{RG}}
+\epsilon_{\mathrm{observable}}.
\]
Choose a single permitted scaling of all parameters. Prove bounds uniform on the stated comparison domain. The first hard step is converting absolute cutoff errors into the relative tail estimate. Start with one nonzero correlation mode whose decay rate and amplitude are explicit. Port **L-CUTOFF** and **L-RG**.

A changing register can support a family estimate. It cannot silently become an all-distance estimate for one fixed register.

---

## Candidate readings and law changes

These are attached conditions on the open branches. None is adopted.

The tests are:

1. Does the specification state or fix a part’s target?
2. Is it open-ended?
3. Does it settle a downstream question by premise?
4. Does it add structure without an independent need?

**P** means the stated concern is absent. **F** means failure. **C** means an unresolved condition. A C is not permission to use the candidate.

| Candidate | Exact scope | Tests 1–4 | Condition before use |
|---|---|---|---|
| R-GB1Φ | Apply ZM1-INV’s map properties to the external named LGT source. Keep R-form for the actual zoom. | C P P P | Owner resolves the source-reading question. |
| Repaired R-SEC | Use the GNS quotient of a class fixed independently of the target embedding. | C C P P | Supply the class and its two-sided invariance. |
| Finite FP word | Supply the four translated cube layers with the stated order. | C P P P | Prove exact finite-register covariance and NN-a admissibility. |
| R-SUM | Supply written real coefficients, with positive unwrapped electric energy. | P P C P | Treat the energy reading as supplied physical data. |
| R-IA | Supply one fixed positive step per instantiated law. | P P C C | Give an independent reason for that step. |
| Strict R-GEN | Supply the fixed decomposition and strict principal branches. | P P C P | Check the spectral domain. Preserve **E−**. |
| R3 | Supply the non-strict bound and uniqueness requirement. | P P C P | Check the eigenvalue condition. Preserve **E−**. |
| R-ISO calibration | Choose the step to enforce tree-level isotropy. | F P F C | Fails the stated tests. |
| Local Hamiltonian revision | Replace exact finite-depth tick dynamics by a fully specified local Hamiltonian flow. | P P C P | Owner decides the changed causal/update requirement. |
| Unspecified “large register” | Leave the representation or limit unfixed. | C F P C | Fails until a complete family is supplied. |
| “Assume the start is in the successful RG class” | Use desired membership as law text. | F F F C | Fails. Membership must be proved. |

> “R-GB1Φ … C P P P” — [GB1.md:229](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1.md:229).
>
> “the freely chosen class can be tailored” — [GB1Z2L5.md:107](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5.md:107).
>
> “C P P P” — [GB1ISO.md:165](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:165).
>
> “C marks a supplied physical choice that must remain explicit.” — [GB1_GEN_OWNER_CHECK.md:73](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1_GEN_OWNER_CHECK.md:73).
>
> “2 fails for unspecified ‘large’” — [GA2_Y2.md:161](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GA2_Y2.md:161).

A specified \(L[s]\) family repairs the open-ended quantifier. It does not itself justify choosing that family as the physical law. It also does not supply AS0.

---

## Literature programmes imported by the open nodes

These are programme and locator checks. They are not new proofs of the cited results.

- **L-Z2.** Alexei Kitaev, 1997 preprint / 2003 publication. [arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021). Equations (1) and (4). Port the local star/plaquette algebra and compatible encoded operator construction. Do not import a three-dimensional dynamical gauge bridge from the two-dimensional toric-code example.

  > “section 1, Eq. (1)” — [GB1Z2L5_DRAFT.md:74](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1Z2L5_DRAFT.md:74).

  This locator is in an unfrozen bibliographic record. The primary paper was also inspected.

- **L-QL.** David Horn, 1981. *Finite Matrix Models with Continuous Local Gauge Invariance*. Equations (1)–(11), especially (10). [Primary paper](https://www.tau.ac.il/~horn/publications/horn1981.pdf). No arXiv identifier was located in the corpus record. Port the finite matrix representation and exact Gauss commutator.

  > “Eq. (10) is the vanishing plaquette/Gauss commutator” — [LIT_QLM.md:143](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:143).

  Shailesh Chandrasekharan and Uwe-Jens Wiese, 1996 / 1997. [arXiv:hep-lat/9609042v2](https://arxiv.org/abs/hep-lat/9609042v2). Equations (5.4)–(5.7) identify the dimensional-reduction programme. They do not prove the required four-dimensional convergence from the present three-dimensional quantum lattice.

  > “physics-level effective-action and universality argument” — [LIT_QLM.md:13](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:13).

- **L-RISHON.** Richard Brower, Shailesh Chandrasekharan and Uwe-Jens Wiese, 1997 / 1999. [arXiv:hep-th/9704106v1](https://arxiv.org/abs/hep-th/9704106v1). Equations (4.2)–(4.6). Port the fermionic rishon algebra and fixed-number representation constraints.

  > “exact finite-dimensional algebra for the rishons” — [LIT_QLM.md:21](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:21).

- **L-MAJORANA.** Richard Brower, Shailesh Chandrasekharan, Stefan Riederer and Uwe-Jens Wiese, 2003 / 2004. [arXiv:hep-lat/0309182v1](https://arxiv.org/abs/hep-lat/0309182v1). Equations (4.39)–(4.42), especially (4.41). Port the \(so(2N)\) Majorana construction.

  > “This algebraic construction is exact.” — [LIT_QLM.md:53](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:53).

- **L-COHERENT.** Björn Schlittgen and Uwe-Jens Wiese, 2000 / 2001. [arXiv:hep-lat/0012014v1](https://arxiv.org/abs/hep-lat/0012014v1). Equations (6.20)–(6.30). Port the coherent-state expansion, while proving the missing concentration and remainder estimates.

  > “does not provide uniform remainder bounds” — [LIT_QLM.md:33](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:33).

  Oliver Bär, Richard Brower, Björn Schlittgen and Uwe-Jens Wiese, 2001 / 2002. [arXiv:hep-lat/0110148v1](https://arxiv.org/abs/hep-lat/0110148v1). Equations (5)–(6) and (9)–(11). Port representation constraints and the coherent-state resolution.

  > “exact representation/coherent-state identities” — [LIT_QLM.md:43](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:43).

- **L-CUTOFF.** Yu Tong, Victor Albert, Jarrod McClean, John Preskill and Yuan Su, 2021 / 2022. [arXiv:2110.06942v2](https://arxiv.org/abs/2110.06942v2). Theorems 5–6, Equation (65), and the hypotheses in Equation (24). Theorem 12 has additional isolated-eigenvalue hypotheses. Port leakage and truncation estimates. Prove the quantum-link coefficient comparison separately.

  > “Its regulator is a projection … not the repo’s rishon or so(20) quantum link.” — [LIT_QLM.md:85](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/LIT_QLM.md:85).

- **L-RG.** Tadeusz Bałaban’s constructive lattice-gauge programme, as ported in the Ethan Sussman–Levent Alpoge complete account and the 2026 YM4D corpus. The named source is CA-I `3.1:thm-main`, at `31a47c543775`. The corpus supplies no arXiv identifier for this account. The symmetry port is RO1 Theorem 9, with H-U, H-L, H-C and H-T.

  > “credit for the underlying RG inputs belongs to Tadeusz Bałaban” — [t0-tree.md:24](/Users/jonreilly/toe-lap/ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library/t0-tree.md:24).
  >
  > “RO1 … Theorem 9 as conditional on H-U, H-L, H-C and H-T” — [GB1ISO.md:175](/Users/jonreilly/toe-lap/repo/.claude/science/physics-loops/toe-assembly-20261104/GB1ISO.md:175).

  Port the actual estimates and interfaces. The index is not a substitute for the complete theorem statement.

---

## Ranked open leaves

The likelihoods are judgments about the stated bounded deliverable. They are not probabilities of completing W1.

| Rank | Leaf | Wall movement on success | Proof outlook |
|---:|---|---|---|
| 1 | **C** | Removes the demonstrated cube-factorisation mechanism. Gives a usable magnetic law or a precise failed ansatz. | High for deciding a fixed finite word. Moderate-to-low for an exact admissible repair. |
| 2 | **R** | Connects finite registers to states of a regular-link theory. Strengthens the family route substantially. | Moderate for subsequential local ground-state convergence at fixed couplings. Lower for uniform quantitative Euclidean bounds. |
| 3 | **H** | Supplies the direct nontrivial YM4D admission step. | Low overall. The Gaussian anisotropic rung is much more accessible. |
| 4 | **V** | Establishes the common-state requirement needed by every physical hand-off. | High for a small-rung counterexample to a proposed identification. Low for a general positive theorem. |
| 5 | **N** | Converts a benchmark theorem into a theorem about a live law. | Low-to-moderate for a sharply specified sector. |
| 6 | **F** | Could establish the bridge without changing the fixed-register premise. | Low. The selected-state phase estimate is the main difficulty. |
| 7 | **RATE** | Delivers the quantitative GA2 claim. | Low before **H**. Exact Gaussian tests are accessible. |
| 8 | **ZQ** | Clarifies a valid encoded \(\mathbb Z_2\) rung and its readout meaning. | Moderate for a local sector lemma. Lower for a compatible infinite net. |

### Lane brief 1 — C: decide finite-register FP covariance

Fix the ordered four-tiling word. Use spin-one \(U(1)\) links first. Prove or refute covariance under generators of the cell group. Expand exact finite matrices symbolically. Identify the first potentially nonzero covariance coefficient. If the word fails, isolate the algebraic relation a repair would need. Keep NN-a compilation separate.

**Stopping rule:** a proof of exact covariance and compilation; an analytic counterexample to the fixed word; or one remaining lemma that fails three named attacks: **rotation–ordering**, **shared-link commutators**, and **NN-a scheduling**.

### Lane brief 2 — R: pass selected ground states through the register limit

Use a specified cube-coupling Hamiltonian with positive electric energy. Prove a local electric-energy bound independent of volume and register size. Derive tail tightness. Pass the local ground-state inequality to a regular-link limit. Then treat bounded Euclidean insertions. Start with one \(U(1)\) plaquette. Extend to coupled cubes before \(SU(2)\). Claim subsequential states unless uniqueness is proved.

**Stopping rule:** a local convergence theorem; a counterexample to the proposed uniform bound; or one remaining lemma that fails **energy-tail control**, **local commutator convergence**, and **normalized Euclidean insertion control**.

### Lane brief 3 — H: one anisotropic RG step

Pin one full-plaquette heat-kernel start and one RG norm. Prove the anisotropic Gaussian block estimate first. Keep \(Z_s/Z_t\) in a fixed compact positive interval. Then attempt the first non-Abelian step. Track sources and large fields. Do not infer continuum isotropy from quadratic matching.

**Stopping rule:** a uniform one-step theorem; a counterexample to stability of the pinned class; or one remaining lemma that fails **anisotropic propagator control**, **large-field suppression**, and **source/Ward remainder control**.