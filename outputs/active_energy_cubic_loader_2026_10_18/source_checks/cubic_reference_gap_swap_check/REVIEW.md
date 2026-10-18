# Distinct check: cubic ferromagnetic reference and operation costs

**Disposition: SUPPORT for the full many-body grid-gap inequality and its standalone local-reference SWAP corollary.** The ordered-path congestion, endpoint-transposition factors, symmetric-sector projection, incident loads, geometry, counts and sufficient \(\epsilon^{-7/3}\) runtime order are correct under the supplied premises. No required correction was found.

**The delayed-suffix full-loader corollary remains conditional on its separate distinct check.** I read that candidate completely and verified that the grid substitution preserves its stated reference, commutation, norm, parameter and geometry hypotheses. I did not duplicate or certify its new suffix/gauge/binomial-integral proof. Acceptance of the standalone corollary does not grant acceptance of that separate composition.

This is a positive finite-graph comparison theorem and a selective mathematical check. It establishes no optimal gap, optimal runtime, novelty, native Hamiltonian, preparation, reusable reference or permanent halt.

## 1. Exact sources and exposure

All paths below are relative to
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

| Source | Bytes | SHA256 | Actual coverage |
|---|---:|---|---|
| `cubic_reference_gap_swap/PROPOSAL.md` | 9999 | `72aa48a5423fb82fabeb5d1247a613376331b94610a2b673031e142b612c26ee` | Complete 98-line new argument read; new proof and both substitution interfaces reconstructed below. |
| `active_energy_loader_interface/PROPOSAL.md` | 21721 | `4adb0b1e3b7954ef0894cc68b73b2c3f37c645cb089f9d4b63d81769e9eaf570` | Complete 224 lines read; only preservation of its stated hypotheses and inventory is checked here. Its separate proof check was pending when assigned. |
| `local_reference_static_swap/PROPOSAL.md` | 16601 | `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70` | Complete text read in my immediately preceding task; unchanged bytes reverified here. Its checked abstract elimination/gate interfaces are reused. |
| `local_reference_static_swap_check/REVIEW.md` | 13502 | `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b` | Complete text read in that preceding task; unchanged bytes reverified here. This is inherited review evidence, not another new check of that proof. |

ROOT supplied the proposed grid theorem, intended exponent and proof route before this review. I share campaign ancestry, previously checked the product-reference rotation and have authorship exposure to separate exact-loader constructions. This is a same-model, source-exposed distinct reconstruction of the new grid argument, not blind replication or a claim of independent scientific lineage. The elementary gap proof below does not assume the desired runtime or a one-particle spectral-gap theorem.

## 2. Endpoint transposition: word, orientation and factors

For an arbitrary vector \(\psi\), put
\[
 E_{uv}=\langle\psi,(I-S_{uv})\psi\rangle,\qquad
 E_e=\langle\psi,(I-S_e)\psi\rangle.
\]
All swaps are Hermitian unitaries on the *entire* \(N\)-qubit space, so
\[
 \|(S_e-I)\psi\|^2=2E_e.
\tag{1}
\]
Normalization is unnecessary; every inequality is homogeneous.

For a simple path \(v_0=u,v_1,\ldots,v_d=v\), let \(s_j=S_{v_{j-1},v_j}\). The palindrome
\[
 s_1s_2\cdots s_d\,s_{d-1}\cdots s_1
\tag{2}
\]
is the endpoint transposition \(S_{uv}\). The first \(d-1\) edges occur twice and the last once. This holds for either direction of the path and uses no commuting-edge assumption.

For a word \(U_1\cdots U_l\), the exact prefix telescoping identity is
\[
 (U_1\cdots U_l-I)\psi
 =\sum_{r=1}^l U_1\cdots U_{r-1}(U_r-I)\psi.
\tag{3}
\]
Each prefix is unitary. Consequently Cauchy–Schwarz bounds its squared norm by \(l\sum_r\|(U_r-I)\psi\|^2\). Combining (1)–(3) with \(l=2d-1\) gives
\[
 2E_{uv}\leq (2d-1)\,2\sum_rE_{e(r)}
 \leq4(2d-1)\sum_{e\in{\rm path}}E_e,
\]
and therefore
\[
 E_{uv}\leq(4d-2)\sum_{e\in{\rm path}}E_e.
\tag{4}
\]
The source's factors are correct: division by two from the left displacement norm leaves \(2(2d-1)\), not \(4(2d-1)\). The energies on the right are evaluated on the original \(\psi\); no unproved control of energies on transported states is hidden in the telescoping argument.

For the axis-ordered shortest grid path, \(d\leq3(n-1)\). For distinct endpoints this yields \(4d-2\leq12n-14<12n\). The convenient \(12n\) ceiling is conservative. Equal endpoints contribute zero and need no length-zero version of (2).

## 3. Exact ordered-path congestion and the many-body gap

Use the fixed path order x, then y, then z for every *ordered* endpoint pair. Consider an edge between coordinate values \(k\) and \(k+1\), where \(0\leq k\leq n-2\). The pair of endpoints along that axis can straddle the cut in either direction in exactly
\[
 2(k+1)(n-k-1)
\tag{5}
\]
ways.

For an x-edge at fixed y,z, the source y,z coordinates must equal those of the edge; the target y,z coordinates are free. For a y-edge, target x and source z are fixed; source x and target z are free. For a z-edge, target x,y are fixed; source x,y are free. In every case the two remaining free coordinates supply \(n^2\) choices. Thus the exact ordered-path usage of that edge is
\[
 C_e=2n^2(k+1)(n-k-1)\leq n^4/2.
\tag{6}
\]
The path is simple, so it uses that edge at most once. Reverse endpoint order generally produces a different axis-ordered path; the count correctly includes both, without pretending the reversed path is the same canonical path.

As boundary checks, for \(n=2\) each edge has eight ordered usages, exactly \(n^4/2\). For odd \(n\), the actual maximum is \(2n^2\lfloor n^2/4\rfloor<n^4/2\). These checks agree with (6); no hidden orientation factor remains.

Since \(E_{uv}=E_{vu}\), summing (4) with the \(12n\) ceiling over ordered pairs gives
\[
 \begin{aligned}
 \sum_{u<v}E_{uv}
 &=\frac12\sum_{u\ne v}E_{uv}\\
 &\leq\frac12(12n)\sum_eC_eE_e\\
 &\leq3n^5\sum_eE_e.
 \end{aligned}
\tag{7}
\]
The factor \(1/2\) converts the *endpoint-energy sum*, even though the chosen reverse paths need not agree. This is the correct comparison with the unordered complete-graph Hamiltonian.

For spin \(1/2\), \(S_{uv}=2\mathbf s_u\cdot\mathbf s_v+I/2\) and \(\sum_u\mathbf s_u^2=3NI/4\). Expansion of \(\mathbf S_{\rm total}^2\) gives on the entire tensor-product space
\[
 H_{\rm complete}=\sum_{u<v}(I-S_{uv})
 =\frac{N(N+2)}4I-\mathbf S_{\rm total}^2.
\tag{8}
\]
The maximal-spin \(N/2\) multiplet is the completely symmetric subspace \(\Pi\). The next allowed spin is \(N/2-1\), whose \(S(S+1)\) value is lower by exactly \(N\); smaller spins have a larger difference. Thus
\[
 H_{\rm complete}\geq N(I-\Pi).
\tag{9}
\]
This standard finite-spin algebra is the unchanged checked premise from the line proof, and the coefficient has been reconstructed directly above. It includes all excitation sectors and multiplicities, rather than inferring a many-body statement from one magnon.

Equation (7) holds for every \(\psi\), hence is a quadratic-form operator inequality. With \(N=n^3\), (7)–(9) prove
\[
 \boxed{\ H_F=\kappa\sum_e(I-S_e)
 \geq\frac{\kappa}{3n^2}(I-\Pi).\ }
\tag{10}
\]
All these operators are finite-dimensional; no domain extension is needed. Tensoring arbitrary data and passive-reference spaces preserves the inequality.

The zero-space assertion is also exact. Each \(I-S_e\) is positive; zero expectation for their sum forces each term to annihilate the vector. Edge transpositions of any connected graph generate every permutation, so their common fixed space is precisely \(\Pi\). Conversely every symmetric vector is fixed by every edge swap. In particular \(H_F\Pi=\Pi H_F=0\), even though the grid Hamiltonian is not invariant under every permutation.

## 4. Projection and standalone comparison hypotheses

For any reference permutation \(T\), \(T\Pi=\Pi T=\Pi\). Conjugating the corner raising/lowering operators to those of any other site and compressing by \(\Pi\) therefore gives
\[
 \Pi\,{\rm exchange}_{P,B_{\rm corner}}\,\Pi
 =\frac1N\Pi\sum_v{\rm exchange}_{P,B_v}\Pi.
\tag{11}
\]
The star sum preserves \(\Pi\), and the data operator \(H_S\) acts trivially on the reference. This reasoning needs the symmetry of the projector, not a permutation-invariant \(H_F\) outside its kernel.

For the unchanged \(W=H_S+g\,{\rm exchange}_{P,B_{\rm corner}}\), its full norm remains
\[
 \|W\|\leq a+2b+c+g<4\lambda,\qquad
 \|(I-\Pi)W\Pi\|\leq g=\sqrt2\,\lambda.
\tag{12}
\]
Only the corner exchange contributes to the second bound. The product \(\beta=|+\rangle^{\otimes N}\) lies in \(\Pi\). Each grid swap conserves the equal-gap reference occupation, and the corner exchange conserves \(n_P+n_{B_{\rm corner}}\); all other P terms are diagonal and Q is freely degenerate. Hence the complete installed Hamiltonian still commutes with \(H_E\).

Equations (10)–(12) are exactly the changed hypotheses required by the checked local-source elimination lemma. That lemma allows arbitrary degeneracy in \(\Pi\) and uses no upper bound on \(\|H_F\|\). The growing number of grid bonds therefore introduces no uncharged volume term in that lemma. Its bound \(512\lambda/\Delta\) on \(0\leq t\leq2\pi/\lambda\), the projected-star residual \(g/(2\sqrt N)\), the effective SWAP and its scalar phase remain legitimate inherited interfaces after putting \(\Delta=\kappa/(3n^2)\).

The ferromagnetic identities remain part of \(H_F\), whose symmetric energy is zero. Adding a separate phase \(\kappa|E|t\) to the inherited comparator would be wrong; the source does not do so.

For the standalone prescription, \(n=\lceil(512\pi^2/\epsilon^2)^{1/3}\rceil\) gives \(N\geq512\pi^2/\epsilon^2\). Its minimum and revival rounding ensure
\[
 \lambda\leq\lambda_{\max}\leq\epsilon\Delta/16384
 \leq\Delta/8,\qquad 512\lambda/\Delta\leq\epsilon/32.
\]
Also \(w<\tau\), so the entire window has \(0<t<2\pi/\lambda\). There the inherited star error is strictly below \(\sqrt2\pi/\sqrt N\leq\epsilon/16\), and the inherited timing contribution is at most \(\epsilon/32\). Together with the elimination allowance, the total is strictly below \(\epsilon/8\). The normalized target is exactly
\[
 e^{-i(st+\pi/4)}\operatorname{SWAP}_{QP}\psi\otimes
 e^{-it\omega\sum_vn_{B_v}}\beta.
\tag{13}
\]
All reference, Q/P and passive-reference outputs are retained. The unhalved stabilized complete-output channel upper bound \(<\epsilon/4\) follows from this uniform isometry/vector upper bound, as in the parent proof. No record or conditioned-output claim is added.

## 5. Full-support loads, placement and inventory

The grid has \(3n^2(n-1)\) bonds, each of full norm \(2\kappa\). Its degree is at most six, and its attached corner has three grid neighbors plus P. With \(M=\Lambda-\omega>0\) and \(\kappa=M/32\), an unattached site's load is bounded by
\[
 \omega+12\kappa=\omega+3M/8<\Lambda.
\]
For the standalone policy \(C_P\lambda\leq M/2\),
\[
 \begin{aligned}
 {\rm load}(P)&\leq\omega+M/2,\\
 {\rm load}(Q)&\leq M/2,\\
 {\rm load}(B_{\rm corner})
 &\leq\omega+6\kappa+2g\\
 &<\omega+3M/16+M/2
 =\omega+11M/16<\Lambda.
 \end{aligned}
\tag{14}
\]
Here \(2g\leq\sqrt2 M/C_P<M/2\) follows from \(C_P>2\sqrt2\). Even the conservative six-neighbor charge \(12\kappa\), plus this exchange bound, stays below the cap. These sums use complete-support block norms, including physical identity shifts.

The placement \(B_{i,j,k}=(-1-i,-j,-k)\), \(P=(0,0,0)\), \(Q=(0,0,-1)\) is injective. Reference bonds, the corner-P exchange and QP interaction each have Manhattan length one. Q has x-coordinate zero and negative z, while every reference has negative x, so there is no collision. The installed standalone graph has degree at most six. Uninstalled geometric adjacency is not an extra interaction; the selective coupling premise remains explicit.

The inventory is \(N+2\) qubits and
\[
 (N+1)\ {\rm occupations}
 +5\ {\rm data/exchange\ blocks}
 +3n^2(n-1)\ {\rm reference\ blocks}
 =N+6+3n^2(n-1)
\tag{15}
\]
positive blocks. Substituting the line edge count \(N-1\) recovers the old \(2N+5\), a consistency check on the changed count.

## 6. Conditional preservation of the delayed-suffix interface

The pending source `4adb0b1e…` uses \(H_F\) only through its symmetric kernel/gap, the projected star and local norms, and its commutation with each suffix prefix. Each prefix acts on head rails/P/R and as identity on the reference, so it commutes with the cubic \(H_F\) just as with the line. Its P actions are diagonal, preserving commutation with the unchanged \(H_E\). The physical arm rotation acts only on heads and also commutes with \(H_F\). Thus replacing the reference graph introduces no new term into that candidate's transformed defect. Its bound by \(8\lambda\), its support in the late suffix and the factorized comparison's local-state norm do not acquire an \(n\)-dependent term from this substitution.

This checks applicability, not the new proof of the late-suffix identity or its binomial integral. Conditional on that proof, the grid prescription preserves every numerical hypothesis:
\[
 \begin{gathered}
 N=n^3\geq8192\pi^2/\epsilon^2,\qquad
 \lambda\leq\epsilon\Delta/65536,\qquad
 J_c=\lambda(L+1)/4\leq J_{\rm budget},\\
 512\lambda/\Delta\leq\epsilon/128,\qquad
 gt/(2\sqrt N)<\epsilon/64\quad(t<2\tau).
 \end{gathered}
\tag{16}
\]
The unchanged three-entry minimum for \(w\) supplies the local timing, defect-after-revival and head-target allowances. The unchanged \(L\) supplies the stated tail-integral allowance. Thus the candidate's claimed complete vector ceiling \(7\epsilon/128\) and channel ceiling \(7\epsilon/64\) retain exactly their original conditional budgets, rather than being inferred from the standalone theorem.

The target phase remains \(e^{-i(C_{\rm head}+s)t}i^Le^{-i\pi/4}\), with its full \(U_f\), external head embedding and the actual \(N\)-qubit \(\beta(t)\). The grid does not create a new scalar phase or repair the nonzero suffix gauge defect. In particular it supplies no exact all-time record factorization and does not transfer a uniform-output-ray dwell theorem.

The new grid lies at x at most \(-1\), outside the suffix cube and its upward rays. Q remains outside the cube at \((0,0,-1)\); P is shared at the specified corner, not duplicated. All grid bonds are nearest-neighbor. Existing suffix bonds retain range at most nine. The degree ceiling remains eight at R; P has four head contacts, Q and the reference corner, while grid sites have degree at most six and the attached corner degree four.

For this policy \(C_P\lambda\leq M/4\), \(J_c\leq M/64\). The P/Q/R/head load ceilings are unchanged; in particular P is at most \(\omega+M/4+M/8\). The attached reference corner has
\[
 \omega+6\kappa+2g
 <\omega+3M/16+M/4
 =\omega+7M/16<\Lambda,
\]
and other reference sites remain at most \(\omega+3M/8\). The total inventory becomes
\[
 \begin{aligned}
 {\rm qubits}&=4(L+1)+3+N=4L+N+7,\\
 {\rm blocks}&=(8L+34)+(N+6+3n^2(n-1))\\
 &=8L+N+40+3n^2(n-1).
 \end{aligned}
\tag{17}
\]
No mathematical spins from the scalar clock representation are added to this physical count.

## 7. Asymptotic order and what it does not imply

At fixed \(\omega>0\) and fixed \(M>0\), either prescription has
\[
 n=\Theta(\epsilon^{-2/3}),\quad
 N=\Theta(\epsilon^{-2}),\quad
 \Delta=\Theta(M\epsilon^{4/3}).
\tag{18}
\]
The cube rounding only changes constants: the unrounded \(n\) is already greater than one, so its ceiling lies between it and twice it. Consequently the accuracy entry in \(\lambda_{\max}\) is \(\Theta(M\epsilon^{7/3})\). In the standalone minimum it eventually beats the fixed \(\omega/2\) and \(M/(2C_P)\) entries. In the conditional full-loader minimum the extra clock entry is
\[
 4J_{\rm budget}/(L+1)=\Theta(M\epsilon^2),
\]
which is asymptotically *larger* than the accuracy entry, because \(\epsilon^{7/3}/\epsilon^2=\epsilon^{1/3}\to0\). Thus the accuracy entry eventually controls both prescriptions. The very large fixed constant in \(L\) can postpone that regime; the exact minimum, not the exponent alone, governs a finite parameter choice.

Finally \(\lambda_{\max}\leq\omega/2\) implies \(x=\omega/(2\lambda_{\max})\geq1\). Since \(x\leq\lceil x\rceil<2x\), the actual revival choice obeys
\[
 \lambda_{\max}/2<\lambda\leq\lambda_{\max}.
\]
It follows that
\[
 \boxed{\tau=\Theta(M^{-1}\epsilon^{-7/3}),\qquad
 {\rm qubits,\ blocks}=\Theta(\epsilon^{-2}).}
\tag{19}
\]
For the full-loader branch (19) remains conditional on the separate interface theorem; its substitution arithmetic itself is valid. The graph improvement changes the sufficient gap-limited time from the line prescription's \(\epsilon^{-5}\). It does not prove a lower bound on time, a practical crossover, a favorable window fraction or a new precision/preparation mechanism.

## 8. Work record and limits

The new proof was reconstructed analytically, including the ordered-axis edge counts, all factors in the graph comparison and the many-body spin coefficient. Tools read complete source text and verified bytes/hashes; no scientific executable, enumeration, spectral simulation, numerical fit, external literature search or new delegation was used. The small-\(n\) checks in section 3 are exact consequences of the displayed count, not numerical evidence substituted for proof.

Applicable instructions and the reviewer workflow were reused at the unchanged source revision already read in the preceding task. Only this REVIEW.md was written. No candidate source, W/canonical file, Git state, checkpoint, axiom, editable prompt, model/effort or publication/audit status was changed. Native product coherence, exact equal gaps and coefficients, selective positive interactions, isolation, reference preparation/reuse, arbitrary active P/environment dynamics and capture remain external supplies or open questions as stated by the sources.
