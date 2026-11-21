# T0 joins J1 and J6

Provenance: Research text at repository commit 7365c83681b8d5222f9f90b2df54dcc49531f991. Assembly of frozen local T0 parts with text by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, pinned at 31a47c543775. No audit or scientific status is granted.

Author: OpenAI Codex. Hand arguments only; not independently checked. This note changes no frozen input.

## Scope and source convention

The obligations are J1 and J6 of `t0-tree.md`, §5.4. J2 is recorded separately below. A proof of a join is an implication from its named suppliers. It does not prove their interacting estimates. In particular, neither a component witness nor NT2 follows from assembly.

SA denotes the outline `/tmp/sa_ym4.tex`; CA-I denotes `/tmp/sa_ca_I.tex`. Both were fetched once from the revision above. Source line numbers refer to those files. Library line numbers refer to this checkout. The index README, relevant chunk rows and their neighbours, and relevant entries of `obligations.md` precede the raw-source readings. The CA 4.12–4.19 index locates the first-passage application. No numerical or computer-assisted proof is used.

## J1. Dictionary and actual-construction interface

### 1. Exact finite dictionary

Use the CA convention throughout the finite integral. The entries below follow from P1 §§1–2, CA-I 403–525 and 606–686, and the definitions in SR1, CL1 and RO1.

| Object | CA convention | Frozen T0 convention and identification |
|---|---|---|
| Group and trace | \(N=2\), \(\operatorname{tr}1=1\) | \(\operatorname{tr}=\operatorname{Tr}/2\); thus \(a_p=1-\operatorname{Re}\operatorname{tr}U_p=1-\tfrac12\operatorname{Re}\operatorname{Tr}U_p\). |
| Measure | Product normalized Haar on one orientation of each bond; inverse on the reversed bond | Exactly the same measure after relabeling bonds. Count each unoriented plaquette once, six plane types per site. |
| Bare coefficient | \(x_0=g_0^{-2}\) | \(\beta=x_0\). The CA symbol \(\beta_j\) for an increment is not this bare \(\beta\). |
| Lattice | \(a(\mathbb Z+\tfrac12)^4\), \(a=L^{-K}\), side \(\ell=2L^m\) | Translate coordinates by \(-\delta_a\), \(\delta_a=(a/2,a/2,a/2,a/2)\), to obtain \(a\mathbb Z^4\). |
| Test | \(f^{\rm CA}(x)=f(x-\delta_a)\) | The plaquette bijection gives \(\mathcal O^{\rm CA}(f^{\rm CA})=\mathcal O_a(f)\) exactly. Supremum and Lipschitz norms are unchanged. |
| Observable | \(A(f,U)=\sum_p f(x(p))a_p\) | \(\mathcal O_a(f)\) has no factor \(a^4\), \(g_0^{-2}\), or an extra orientation factor. |
| Source | \(\rho_0^W=e^{-A(\beta-W,U)-E}\) | \(Z(W)/Z(0)=\langle e^{\mathcal O_a(W)}\rangle\). The source shifts \(\beta\) to \(\beta-W\). |
| Scale | RG step \(k\) has physical spacing \(L^{k-K}\) | SR1's scale \(s=K-k\) has \(a_s=L^{-s}\). Thus \(0\le k\le K\) is exactly \(0\le s\le K\). |
| Centering | A single bare Wilson law and its DLR states | \(Z_j(f)=\mathcal O_{a_j}(f)-\nu_j\mathcal O_{a_j}(f)\), with \(\rho_j,\nu_j\in\mathcal G_{a_j,\beta_j}\). Keep the same \(\nu_j\) in every component. |

**Proof of the finite identifications.** Translation is a bijection of sites, bonds and plaquettes on each torus. Relabeling the product Haar variables preserves the measure and preserves each holonomy product. The equality of traces proves the action equality term by term. The test pullback then proves the observable equality term by term. Linearity of the finite sum gives
\[
 -\beta A(U)+\mathcal O_a(W)=-A(\beta-W,U).          \tag{J1.1}
\]
The constant \(e^{-E}\) cancels in the ratio. The DLR specifications are carried by the same bijection, including all plaquettes meeting the integrated bonds. Hence the dictionary also identifies the classes of states used by the consumers. The physical spacing identity proves the reversed scale index. This is an exact finite-cutoff identification, not an appeal to a smooth classical expansion.

For \(SU(2)\), the CA one-loop coefficient is
\[
 c_0^{\rm CA}=\frac{11N^2}{12\pi^2}\log L
             =\frac{11}{3\pi^2}\log L=c_0^{\rm IN}.
                                                               \tag{J1.2}
\]
This checks the numerical convention; it does not identify the two extracted increments. IN1's coefficient is its R16 readout in the declared response chart (`in1.md:42–57,110–127`). P7 extracts the CA polarization coefficient with its own domain, background map and localized members (CA-I 58990–59047). Agreement of the bare observable does not identify these intermediate objects.

**Vacuum normalization.** Let \(Z_b\) use \(E=0\), and let \(Z_v=e^{-E_{\rm vac}}Z_b\) use P10's fixed unsourced normalization. If a raw-source upper bound and floor hold for \(Z_v\) with common exponent \(V_v\), then they hold for \(Z_b\) with
\(V_b=V_v+E_{\rm vac}\). Their ratio, point terms and domain terms are unchanged. This follows by multiplying both inequalities by the positive number \(e^{E_{\rm vac}}\). P10 §§5.2–5.3 explicitly retains this convention. A20 preserves the sourced mass only on its admitted source induction (P10 §6.1; CA-I 157263–157283). It does not allow a new source-dependent normalization. In particular, it neither supplies an unsourced floor by itself nor identifies the RG fields with bare observable pushforwards.

### 2. Remaining actual-data premises, stated before using them

The following register is the precise scope of the conditional J1 construction. The premises are about the actual Wilson construction, uniformly over the finite prefixes and tori stated below.

**J1-CA.** Supply CA clause (0) on that construction. Concretely retain CA-I 56419–56441: (H1)–(H6); the one-step theorem; widened small-cube condition and its preservation; the finite one-loop and unmarked-increment estimates; the large-field increment bound; localized independence; free-current operator bounds; large-field representation and bounds; the one-power hereditary class; torus independence; and the effective-density representation at already reached levels. P1 proves the arithmetic implication, not these inputs. P7 supplies torus independence conditionally on its full input register (`p7-torus.md:257–300`). P10 §3 retains H-TORUS, H-FLOW, H-CELL and H-AUX. P10 §§4–6 retains its representation, stability and sourced-induction hypotheses. All remain attached whenever their respective conclusions are used. In particular, CA-I 56361–56378 explicitly retains incomplete one-loop and unmarked proofs.

**J1-IN.** Supply the hypotheses of frozen IN1 Theorem 12 for an actual construction: H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O and H-SUM, with the exact domains, coefficient readout, companion uniformity and ten-row order, including Amendment 1. This is the theorem's antecedent, not its conclusion. P10's exactness alone does not supply it. The consumer chain still imports it literally at SR1's order paragraph, CL1 I1, PH1's order paragraph, RO1's order paragraph and WR1's order paragraph.

**J1-ID (the cross-construction premise).** For every bare \(\beta\) in the eventual half-line and every common admitted prefix, the two constructions in J1-CA and J1-IN have the same real extracted increment:
\[
 b_{k+1}^{\rm IN}(\beta)=\beta_{k+1}^{\rm CA}(\beta),           \tag{J1.3}
\]
after the finite dictionary above, with the same \(L\) and bare coefficient. This must hold before choosing the next frame entry, uniformly over unused finer cutoffs and common nonwrapping torus lifts. It is enough to prove equality of these readouts; equality of every presentation is not demanded. A proposed proof through charts must identify their actual backgrounds, independent currents, relative gauges, normalized quadratic extraction and own-counterterm subtraction. Those are IN1's stated inputs, not arbitrary Hessians. If these have different admitted domains, prove the equality on the common domain actually used, and prove its admission. P7's site independence is an equality within the CA construction. It does not assert (J1.3) between CA and the outline-based IN1 construction.

**J1-ORDER (the common parameter premise).** Supply one admissible assignment for J1-CA, J1-IN and the source package, with common \(L\) and the source geometry used by SR1. It must preserve both source and IN dependencies. Distinct auxiliary constants may remain distinct; equal printed letters do not identify them. In particular:

1. Every floor imposed on \(L\) reads only pre-\(L\) data; include odd \(L\ge27\), CA's \(L_0(2)\), IN1's geometric floors and Amendment 1.
2. The actual localization cubes, their collars, the rooted entropy and source decay must be identified with the geometry in SR1 (5)–(6). IN1's entropy floors, including \(\kappa/4>\kappa_D\), precede its final smallness choice. Enlarging a torus later cannot fix a failed decay window.
3. Retain IN1 rows 3–8 with all their internal order: early matrix and Gaussian constants before decay windows; localization sizes before post-size charts; amplitudes/radii before list and volume costs; all source, flow-error and tube constants before \(X_0^{\rm IN}\). The returned constants must have the declared earlier-parameter uniformity.
4. Retain CA (H3)'s order, including the pre-\(L\) cube-size exponents, its weak triple before \(\gamma^{\rm CA}\), then \(\gamma_H^{\rm CA}\); retain (H7)'s source radius \(\varrho\) after \(\gamma_H^{\rm CA}\) and its returned \(\gamma_J^{\rm CA}\). These are CA-I 1126–1182. The source constants requested before IN's \(X_0\) must actually be available then. A proof must give this order embedding; taking minima of two unexplained ceilings does not prove it.

This last condition is a finite parameter-identification obligation, not an extra estimate claimed here. For example, CA's pre-\(L\) power convention and IN's post-decay localization choice cannot be equated by a shared letter \(M\). One must verify the required uniformity or keep two auxiliary sizes and prove the source-domain translation. The present ports do not state this cross-construction identification.

**Source and witness premises.** The full ordinary rooted source estimates are exactly J2 below; they remain a separate leaf. RO1's state-uniform TU10 and its fixed shape class are J3. The coupling ceilings returned by those packages are retained. J1 chooses a datum inside the ceilings; it does not prove J2 or J3.

### 3. An explicit common trajectory, conditional on that register

Use superscripts \(I,C\) to distinguish IN and CA constants. They are not interchangeable:
\[
 \lambda_I=c_0-\varsigma_I,\quad B_I=c_0+2c_2^I+\varsigma_I,
 \qquad
 \lambda_C=c_0/2-\bar\varsigma_C,\quad B_C=C_\beta^C+\bar\varsigma_C.
                                                               \tag{J1.4}
\]
These are IN1 (25) and P1 §2.1. Each \(B\) is positive and each \(\lambda\) is positive on its own hypotheses. Neither equality of the returned slopes nor equality of the finite one-loop error constants is needed.

Complete J1-ORDER, performing the norm-radius conversion of §5 in its designated source row. Fix the source radius and RO1 shape \(\vartheta_*=1/12000\) before requesting their final ceilings. Let \(\epsilon_I,\epsilon_C>0\) be the minimum of the finitely many applicable reference-coupling ceilings in the respective conventions. Include \(\gamma_I\) on the IN side and \(\gamma_J^{\rm CA}\le\gamma_H^{\rm CA}\) on the CA side, and the witness ceiling on whichever side supplies it. These minima are positive because the supplied ceilings are positive. No upstream constant is then changed.

Choose a real \(h_I\) so large that
\[
 h_I>\max\{1,\epsilon_I^{-2},\epsilon_C^{-2}+B_C-B_I\}.
\]
Define
\[
 h_C=h_I+B_I-B_C,\quad g_I=h_I^{-1/2},\quad g_C=h_C^{-1/2},
 \quad T=h_I+B_I=h_C+B_C.                              \tag{J1.5}
\]
Then \(h_C>0\), \(g_I<\epsilon_I\), \(g_C<\epsilon_C\). Thus both references are admitted. This is a scalar match of stopping thresholds, not a reference-change theorem for RG constructions. J1-ID supplies the actual common run: its zeroth entries equal \(\beta\), and (J1.3) plus subtraction proves equality of every subsequent entry by induction. Consequently the two first-passage indices at these references are exactly the same minimum of \(\{k:x_k\le T\}\).

For each integer \(j\ge1\), set
\[
 \beta^{(j)}=T+j,\quad g_0^{(j)}=(T+j)^{-1/2},\quad
 K_j=\min\{k:x_k(\beta^{(j)})\le T\},\quad a_j=L^{-K_j}.
                                                               \tag{J1.6}
\]
IN1 Theorem 12 and CA clause (0) apply to this same pair. For either \(A=I,C\), their bounds give
\[
 h_A<x_{K_j}\le T,\qquad
 \frac{j}{B_A}\le K_j\le1+\frac{j+c_5^A}{\lambda_A}.       \tag{J1.7}
\]
Thus every \(K_j\) is finite and \(K_j\to\infty\); hence \(a_j\to0\). If strictly decreasing spacing is desired, successively choose a later index with larger \(K_j\), which exists by divergence. No assertion that every integer depth is realized is used. Also \(\beta^{(j)}\ge T\) is exactly both bare-coupling conditions. The reference windows and the physical cutoff are now fixed consistently. The stronger IN leading-log conclusion is used only on J1-IN, not inferred from CA's weaker drift bound.

### 4. Cofinal tori and boards

In the CA convention, \(g_-^C(g_C)=T^{-1/2}\), so the volume floor is the single fixed integer
\[
 m_C=11+m'_C+\log_LR_C(T^{-1/2}).                       \tag{J1.8}
\]
It does not grow with \(j\). P10's H-CELL gives
\(\check R_i\le L^{K-i}\check R_K\le L^{K-i}R_C(T^{-1/2})\).
For \(m\ge m_C\), multiply this inequality by \(L^{11}M_C\); it gives
\(L^{m+K-i}\ge L^{11}M_C\check R_i\) at every \(i\le K\). These are the site-admission inequalities in P10 §3. P7, with its hypotheses, identifies the resulting increments on all these sites.

The IN floor can also be chosen independently of \(K\). Put
\[
 A=T,\quad B=B_I,\quad r=r_I,\qquad
 S=\sup_{n\ge0}L^{-n}[\log(A+Bn)]^r.
\]
Here \(A>1\), \(B>0\). A hand bound proves \(S<\infty\). Since
\(A+Bn\le(A+B)(n+1)\) and \(\log(n+1)\le n\), one has
\(\log(A+Bn)\le C(n+1)\) for \(C=\max\{1,\log(A+B)\}\).
For \(n+1\ge2r\), the binomial expansion yields
\[
 \left(1+\frac1{n+1}\right)^r
 \le\sum_{k=0}^r\left(\frac r{n+1}\right)^k\le2.
\]
Therefore the ratio of successive terms of \(L^{-n}(n+1)^r\) is at most \(2/L<1\) beyond that finite index. Its supremum is bounded by the maximum of a finite initial segment and its first tail term. This proves finiteness without enumerating that segment.

Choose \(m_I\) with \(2L^{m_I}\ge2L^{12}M_I S\). At level \(i\), write \(n=K-i\). IN's upper drift gives \(x_i\le T+B_In\). Its running-minimum radius obeys
\(R_i\le L[\log x_i]^r\), since rounding to the next power of \(L\) costs at most \(L\). Hence, for \(\ell\ge2L^{m_I}\),
\[
 \ell L^{K-i}\ge2L^{12}M_I[\log(T+B_In)]^r
                 \ge2L^{11}M_I R_i.
\]
This verifies IN1's displayed torus-size requirement. Additional fixed grid floors remain those of its supplied geometry. Take \(m_*\) above \(m_C,m_I\), the localization exponents and those fixed floors. Then \(\ell=2L^m\), \(m\ge m_*\), is a common cofinal family at every datum (J1.6).

For a fixed board side \(l=L^b\ge a_j\), \(b\in\mathbb Z\), choose the board origin so its planes cut lattice links. There are \(l/a_j=L^{b+K_j}\) mesh intervals per cell. For every \(m\ge\max\{m_*,b\}\),
\[
 \ell/l=2L^{m-b}
\]
is an even integer. Thus every fixed board in SR1 or RO1 tiles all sufficiently large tori in this family. Any finite set of boards and compact supports is accommodated by increasing \(m\). This choice is after the constants and does not alter them. No uniform upper bound on board size or volume is imposed.

At each fixed \((a_j,\beta^{(j)})\), CL1 Lemma 1 supplies a torus-limit Wilson DLR state on a subsequence of this family. Choose one as \(\nu_j\); the self-centered limit uses \(\rho_j=\nu_j\). Its compactness argument uses the fixed-cutoff probability measure and continuous DLR kernels, not a continuum estimate. With J2 and LG1 supplied, CL1 then extracts a cutoff subsequence of the centered moments. PH1's later realizing states remain in \(\mathcal G_{a_j,\beta^{(j)}}\) on their respective subsequences. This is volume first, cutoff second. It does not assert that every periodic state is a torus limit.

### 5. Source radius and consumer coverage

Let the CA norm have coefficient \(c_C>0\) and the consumer norm have coefficient \(c_I>0\). Set \(D=\max\{1,c_C/c_I\}\). Directly from their definitions,
\[
 \max(\|f\|_\infty,c_C\operatorname{Lip}f)
 \le D\max(\|f\|_\infty,c_I\operatorname{Lip}f).
\]
If the CA source radius is \(\varrho\), choose \(r_{\rm src}>0\) with \(2Dr_{\rm src}<\varrho\), also inside every other supplied ordinary-source radius. Then \(\sum_i|z_i|\|f_i\|_\sharp<2r_{\rm src}\) implies CA source admission by this norm inequality. Spatial relabeling preserves both norms. Mirror copying a profile supported away from the cell faces preserves its supremum and Lipschitz bounds: on each cell reflection is an isometry; across faces join the segment pieces, using the common zero boundary values. Arbitrary lists and independent even/odd holomorphy still require J2; radius arithmetic alone does not prove them.

| Consumer hypothesis | Supplier or exact remaining premise |
|---|---|
| SR1/B03 bare law, observable, all scales | §1 proves the identification, with \(s=K-k\). |
| SR1/B03 common cofinal tori and even boards | §4 proves these, retaining the admitted geometry of J1-CA/J1-IN. |
| SR1/B03 full raw bound, floor, locality, rooted counting and source order | J2 supplies the estimates; J1-ORDER supplies their position in the common order; §5 supplies the norm-radius conversion. |
| CL1/B06 I1, unbounded depths and terminal window | J1-IN plus §§3–4; actual applicability and the CA match retain J1-CA/J1-ID/J1-ORDER. |
| CL1 I2/I3 | LG1 and SR1 on these same finite laws; their respective premises remain attached. |
| RO1/B19 realization and H-U | CL1/PH1 realizations above and J2; no torus-only substitution for all-state transfer. |
| RO1 H-T, shape and coupling ceiling | J3 in the exact shape class of RO1 (D.4); §3 places the reference inside its supplied ceiling. |
| PH1 and WR1 inherited IN order | J1-ORDER and IN1's full table, including Amendment 1. The later spectral, approximation and test parameters never feed back. |
| Stability/exact sourced integral used by J2 | P10 A19/A20 on their own hypotheses and the common normalization of §1; the full J2 source bound remains separate. |

This proves every dictionary, stopping, volume and radius inference conditional on the register. It does **not** prove J1-ID or J1-ORDER, nor instantiate the actual-construction antecedents J1-CA/J1-IN. Merely asserting both source theorems does not fill these links. In particular, same bare integrals constrain normalized observables but do not specify a localized coefficient extraction. No equality of an outline independent-current construction with a CA datum is used without J1-ID. The exact residual of J1 is recorded in the Result.

## J6. Full positive-time qualitative clustering

### Statement

Fix one PH1 component \(\sigma=\sigma_\xi\), with the common centering of PH1. Use its unique diagonal-flat moment extensions \(G_n\), including \(G_0=1\). Assume exactly PH1 Theorem 1(3)–(4), CL1 Lemmas 5–6, and the component completion supplied by PH1 Lemma 10 and its change-log item 2. Then, for every \(m,n\ge0\),
\[
 G_{m+n}(\Theta\overline\varphi\otimes\tau_{(v,0)}\psi)
 \longrightarrow \overline{G_m(\varphi)}G_n(\psi),
 \qquad |v|\longrightarrow\infty,                       \tag{J6.1}
\]
for \(\varphi\in\mathcal S_{+,m}\), \(\psi\in\mathcal S_{+,n}\). These are Schwartz tests flat on internal coincidence diagonals and outside strictly positive time. This is the literal spatial cluster statement at SA 118–129. There is no asserted inverse-square rate on this full domain.

### Proof

Let \(\mathcal D\) be the classes of finite sums of compact smooth separated positive-time tensors, including the empty tensor. CL1 and PH1 supply a Hilbert space \(\mathcal H_\xi\), a unit vector \(\Omega=[1]\), and spatial unitaries
\[
 U(v)[F]=[\tau_{(v,0)}F],\qquad U(v)\Omega=\Omega,
 \quad \langle[F],[G]\rangle=\sigma(\theta\overline F\cdot G).
                                                               \tag{J6.2}
\]
The inner product is antilinear in its first argument. PH1 applies CL1 to the component's realizing pair of lattice states; these are not merely the operators of the averaged hierarchy.

For \(a=[F],b=[G]\in\mathcal D\), apply compact clustering to \(\theta\overline F\) and \(G\). Reflection preserves internal separation. Their opposite strict time supports keep every cross pair separated under every spatial translation. PH1's reflection invariance and reality give
\[
 \sigma(\theta\overline F)=\overline{\sigma(F)},\qquad
 \langle\Omega,[F]\rangle=\sigma(F).
\]
Finite sums are allowed by addition. Thus
\[
 \langle a,U(v)b\rangle\longrightarrow
 \langle a,\Omega\rangle\langle\Omega,b\rangle
                                                               \tag{J6.3}
\]
with PH1's inverse-square rate for these fixed representatives.

Write \(P b=\Omega\langle\Omega,b\rangle\) and \(Q=I-P\). These are orthogonal projections because \(\|\Omega\|=1\). Since \(U(v)\Omega=\Omega\), both \(U(v)\) and its inverse preserve \(\Omega^\perp\); hence they commute with \(P,Q\). Therefore
\[
 D_v(a,b):=\langle a,U(v)b\rangle
       -\langle a,\Omega\rangle\langle\Omega,b\rangle
       =\langle Qa,U(v)Qb\rangle.
\]
For any approximants \(a',b'\), Cauchy–Schwarz gives the bound
\[
 |D_v(a,b)-D_v(a',b')|
 \le \|a-a'\|\,\|b\|+\|a'\|\,\|b-b'\|.             \tag{J6.4}
\]
Its right side is independent of \(v\). Indeed, subtract the two bilinear expressions, use \(\|Q\|\le1\), and use \(\|U(v)c\|=\|c\|\). No Schwartz seminorm of a translated test occurs.

Choose \(a_r,b_r\in\mathcal D\) converging in norm to arbitrary \(a,b\in\mathcal H_\xi\). The norms \(\|a_r\|\) are bounded. For fixed \(r\), (J6.3) makes \(D_v(a_r,b_r)\to0\). Taking \(\limsup_{|v|\to\infty}\) in (J6.4), then \(r\to\infty\), proves (J6.3) on the full Hilbert space. This order of limits needs no uniform rate for the approximants.

It remains to identify the full tests in (J6.1) with those vectors. For a finite positive-time sequence \(\Phi\), CL1 Lemma 6 defines
\[
 q(\Phi,\Psi)=\sum_{p,q}G_{p+q}
             (\Theta\overline{\Phi_p}\otimes\Psi_q).
                                                               \tag{J6.5}
\]
Each mixed tensor is diagonal-flat. Internal coincidences are killed by the corresponding factor. At a cross coincidence with positive time, the reflected factor vanishes with every derivative. At negative time, the positive-time factor does so. At time zero, both are flat. The same argument works after a spatial translation. Products of Schwartz functions in disjoint variable groups are Schwartz, so all evaluations are defined.

Constrained tensor density and continuity of \(G_{p+q}\) make the class map \(j\Phi\) well defined in the isometrically identified completion. Explicitly, approximate each of the finitely many \(\Phi_p\) by compact smooth separated tensors in Schwartz topology. Tensor multiplication is continuous, as follows from Leibniz's rule and
\(1+|x|^2+|y|^2\le(1+|x|^2)(1+|y|^2)\).
Applying the extension bound to the squared difference in (J6.5) makes its norm tend to zero. This proves the required Hilbert approximation, not only convergence of scalar evaluations.

For each fixed \(v\), translation is continuous on Schwartz space and preserves positive time and internal flatness. Apply the preceding approximation before and after this fixed translation. Equality (J6.2) on the common compact domain and the isometry of \(U(v)\) give
\[
 j(\tau_{(v,0)}\Psi)=U(v)j\Psi,
 \quad G_{m+n}(\Theta\overline\varphi\otimes\tau_{(v,0)}\psi)
       =\langle j\varphi,U(v)j\psi\rangle,
 \quad G_m(\varphi)=\langle\Omega,j\varphi\rangle.       \tag{J6.6}
\]
Only this identification uses continuity for fixed \(v\). The subsequent infinite-translation limit uses (J6.4), which is uniform. Apply the full-Hilbert-space version of (J6.3) to \(j\varphi,j\psi\). This proves (J6.1). When either degree is zero, the identities follow directly from the invariant vacuum and scalar linearity. The same proof covers arbitrary finite sequences. \(\square\)

### Same hierarchy and reconstruction

Take one sequence of first-passage pairs and one centering state \(\nu_j\) at each pair. PH1 realizes every selected component by integrating states \(\rho_j^\xi\) with this same centering, after its permitted subsequences. Its mean can be nonzero: \(G_{\xi,1}(f)=c_\xi\int f\). The factors in (J6.1) are these actual means; they are not set to zero.

On this component, SR1 supplies growth and density; CL1 supplies positivity, translations and the cube cone; PH1 supplies compact clustering and the unique vacuum. RO1 must be applied to this component with H-U and H-T uniform over its realizing states. Invariance of the mixture does not replace that hypothesis. Under these imports, WR1 Theorem 11 uses this very reflection Hilbert space and reconstructs this very hierarchy. Its continuation agrees on compact separated tensors and hence, by continuity and constrained density, on all diagonal-flat tests. Thus no second scalar theory is introduced when extending clustering or invoking reconstruction.

Nontriviality remains separate. To claim NT1 for a selected component, the positive reflected connected two-point witness of J4 must belong to that component. Its vacuum-subtracted vector is then nonzero and orthogonal to \(\Omega\). Since PH1 gives \(\ker H=\mathbb C\Omega\), the restriction of \(H\) to \(\Omega^\perp\) cannot be zero. A positive mixture covariance alone does not give this component witness. NT2 still requires J5's common blocked-state and scale identification with the selected scalar hierarchy. These are existing J4/J5 premises, not consequences of J6. WR1's claimed conclusion is a unique vacuum, not a Wightman cluster theorem (`wr1.md:403–446`).

## J2. Exact rooted ordinary-source contract and supplier map

This section records the additional leaf; it does not claim its proof. The contract is SR1 (4)–(6), including its preceding quantifiers, and RO1 H-U (`sr1.md:38–67`; `ro1.md:54–62`). It is about **every** ordinary finite real Lipschitz torus list, with repetitions and overlaps allowed. Neither separated-list estimates nor holomorphy only after a conjugate substitution suffice.

For every admitted first-passage pair, every sufficiently large compatible torus, and every such list, put
\[
 W=\sum_i z_i f_i,\quad
 \sum_i|z_i|t_{f_i}<2r_{\rm src},\quad
 t_f=\max\{\|f\|_\infty,c_M\operatorname{Lip}f\}.
\]
There must be fixed positive \(r_{\rm src},A_{\rm src},C_+,C_-\) and real \(V_{K,\ell}\) such that
\[
 \begin{split}
 |Z_{K,\ell}(W)|&\le
 \exp\{V_{K,\ell}+\operatorname{Re}[U_{K,\ell}(W)
             +\sum_{s=0}^K\sum_Xe_{K,\ell,s,X}(W)]+C_+\ell^4\},\\
 Z_{K,\ell}(0)&\ge\exp\{V_{K,\ell}-C_-\ell^4\},\qquad
 Z(W)/Z(0)=\langle e^{\mathcal O_K(W)}\rangle.             \tag{J2.1}
 \end{split}
\]
The constants are independent of cutoff, torus and list, at the fixed reference data. There is no global nonvanishing assertion for \(Z(W)\).

The point term has the exact form \(U(W)=\sum_pu_p(W(x(p)))\). Each \(u_p\) is holomorphic, zero at zero, and bounded on smaller discs uniformly in \(p,\ell\) at fixed \(K\); these bounds may grow with \(K\). Each domain term is holomorphic, zero at zero, and depends only on \(W|_{X^+}\), independently of its list representation. It vanishes if that restriction is zero. Require
\[
 |e_{s,X}(W)|\le A_{\rm src}e^{-\kappa m(X)},\qquad
 \operatorname{diam}X^+\le C_{\rm dep}a_s(m(X)+1),\quad a_s=L^{-s}.
                                                               \tag{J2.2}
\]
The sums converge normally on smaller source balls. The actual domains are indexed by nonempty finite unions of cubes of side \(Ma_s\). The integer \(m(X)\) is the least number of edges of a connected cubical edge tree meeting every cube of \(X\). The enlargement \(X^+\) lies in a fixed number of neighbouring layers. The decay rate satisfies \(\kappa>\kappa_D\), where \(\kappa_D\) is a valid rooted entropy rate including **all** domain-type multiplicities. Also require the stated ST6 bound
\[
 \sum_{X:X^+\cap B(R)\ne\varnothing,\ m(X)\ge t}
      e^{-\kappa m(X)}
 \le C(R+1)^4a_s^{-4}e^{-ct}.                            \tag{J2.3}
\]
Here the constants are position-uniform. The source class includes global mirror-periodized Lipschitz profiles. For RO1 it includes independent even and odd coefficient lists on their joint complex ball, before evaluating the odd coefficients as conjugates. Taking \(C_{\rm st}=C_++C_-\) and dividing (J2.1) by its floor gives precisely RO1 (H.U).

| Candidate statement already ported | Portion it supplies, at its own hypotheses | Match still required for J2 |
|---|---|---|
| P6 B3, `5.1:thm-correlation-theorem`; its input register at `p6-correlation.md:2645–2671` | Conditional sourced RG format, local energies, source shifts and torus-bound machinery. | Its admitted, preparatory, polydisc, frozen-disc and last-lattice inputs remain. Identify one common ordinary-source domain and the actual produced terms, including all repeated lists. |
| P8 H-LOC, `p8-positivity.md:152–166` | Local dependence on plaquette values in \(X^+\), holomorphy, zero-source subtraction, list independence and decay \(C_e e^{-(1-\delta)\kappa d_j(X)}\). | Convert its actual tree metric and enlarged support to (J2.2), with rate losses and every multiplicity accounted for. Identify any point term separately; an arbitrary nonlocal divergent term cannot be put into \(U\). H-LOC is an input to P8, not a consequence of reflection positivity. |
| P8 H-DOM, `p8-positivity.md:200–208`, and §3.5 | Explicit weight-class or every-finite-list reading, with ordinary transported lists and the factor-two mirror-list radius. | Use the full reading, not only its separated tests with \(n\ge2\). Admit the independent even/odd list before conjugation. This distinction matters for the one-point state comparison and all-order insertion estimates. |
| P8 H-TREE, `p8-positivity.md:191–198` | The cited anchored sum at rate \((1-\delta)\kappa-c_\kappa\), with a positive margin \(c_\kappa\). | This is retained there as a Balaban input. Identify the rooted edge-tree indexing and type multiplicity of SR1; convergence of a sum in a different metric is not this identification. |
| Frozen LSC (5a)–(5b), §1(b), Result and final freeze record | Common vacuum-normalized sourced upper bound and unsourced floor, with bounded last-scale constants and a bounded change-of-units offset. | Apply the same zero-source energy identification and its eight sourced upper hypotheses. Transport the inequalities and local terms to the original physical torus and all required scales. Include the small-cutoff cases; the displayed LSC §1(b) branch assumes \(K_J\ge m_J\). |
| P10 A19 and A20, §§5–6 | Stability and equality of masses in a single convention; exact sourced mass on the actual admitted induction. | Retain positivity/representation and complex-move hypotheses. Neither equality of masses nor a source-free bound yields (J2.1) on arbitrary complex lists. |
| LG1 plus SR1 Lemmas 2–6, once (J2.1)–(J2.3) hold | The all-periodic-state transfer, a common holomorphic cell normalizer, one-point comparison and graded moments. | Apply to the same \((a,\beta)\), cofinal boards and centering states. No separate per-state normalizer or new state-wise source estimate is permitted. |

For clarity, LSC's volume rescaling is harmless for constants once its full hypotheses apply. Its original physical side is \(\ell=2L^{m_1}\) and its auxiliary side is \(N=2L^{m_1+b}\), with \(b\) in a fixed finite set. Hence \(N^4=L^{4b}\ell^4\). Multiplying its upper and lower constants by the finite maximum of \(L^{4b}\) gives physical-volume constants. Set \(V=E_{\rm vac}\) when returning to the bare integral. This proves that normalization/volume conversion; it does not identify the local-energy sum with the all-scale rooted package. In particular, an omitted-step estimate cannot silently supply every term at \(0\le s\le K\).

The outstanding J2 match is therefore the aggregate ordinary raw-source representation (J2.1), with its actual localized terms (J2.2), domain admission and rooted geometry (J2.3), at these common data. The supplier map separates existing conditional ingredients from that assertion. No CA-II raw passage was fetched or quoted in this lane; the statements here refer to the explicitly read local ports, preserving their input registers.

## Source checks and recovery checkpoint

Repository sources are pinned at `7365c83681b8d5222f9f90b2df54dcc49531f991`. The missing-on-disk workflow was read through `git show HEAD:docs/ai_methodology/SCIENCE_WORKFLOW.md`; the checkout is sparse. The task's explicit research-text scope governs this file. No planning branch, audit, status file, prompt file or frozen theorem was edited.

| Directly read original source | What this note uses |
|---|---|
| SA 66–130 | Full positive-time diagonal-flat cluster target; a theorem statement with a sketch, not this completion proof. |
| SA 22304–22339 | Prescribed order and separate scope of later comparison interfaces; no identification of different constructions follows from it. |
| SA 25905–25960 | Conditional isometric identification of the enlarged positive-time quotient from growth and constrained density. The completed-space argument above adds the explicit uniform-in-translation estimate. |
| CA-I 403–525, 606–686 | Wilson action, normalized trace, shifted lattice, source sign, physical units, running-coupling and first-passage definitions. |
| CA-I 1126–1210 | Exact (H1)–(H7) and order declarations, including the source radius after \(\gamma_H\); these do not establish a common order with IN1. |
| CA-I 3636–3721, 56342–56412, 56419–56525 | First-passage and flow arithmetic, and the actual-construction antecedents of clause (0). Their conditional use is retained. |
| CA-I 58990–59047 | CA site-free coefficient statement and the beginning of its proof; only the statement is used, via P7's checked port. This excerpt is not a new full check of that proof. |
| CA-I 157263–157283 | Sourced exactness on admitted correlation induction. The full local port P10 remains its supplier. |

Navigation used SA chunks 01, 20, 23–24 and the corresponding obligation rows, plus CA 4.12–4.19 chunk 11 and neighbouring full-index entries for P7/P10. Quoted formulas and source claims above were compared with these excerpts or the named local-port passages. No claim rests on a truncated display or on an index status alone. The frozen local results were used within their stated hypotheses, not re-audited.

Current checkpoint: the finite dictionary, threshold matching and cofinal-board deductions are written in J1 §§1,3–5. J1-ID and J1-ORDER remain unproved; J1-CA/J1-IN retain their upstream actual inputs. J6's full test-domain implication is proved by (J6.4)–(J6.6). J2 is an exact contract and supplier map. A next J1 lane must identify the actual coefficient readouts and give the common order, or explicitly replace the frozen consumers' IN1 import with a checked CA interface. It must not infer that replacement from a similar scalar stopping formula.

## Result

**J1 — remaining premise.** For one common ordered Wilson construction, instantiate **J1-CA** and **J1-IN**, prove the cross-construction increment identity **J1-ID (J1.3)** on every used prefix, and supply **J1-ORDER** with the admitted source geometry. These are precise retained premises, not supplied by P1 arithmetic, P7's internal site independence, or P10 mass exactness. Conditional on them, §§1–5 give an explicit common trajectory, exact observable/source normalization, compatible stopping windows, positive coupling/source ceilings, and cofinal even-cell boards/tori for B03/B06/B19 and the inherited IN-order passages. J2 and J3 remain their separate estimate inputs.

**J6 — Proof.** PH1 compact clustering, component spatial unitaries and the isometric constrained completion imply the full positive-time diagonal-flat qualitative cluster statement (J6.1). Bound (J6.4) is uniform in spatial translation. Reconstruction uses the same hierarchy under WR1's stated componentwise inputs; selected nontriviality witnesses still require J4/J5 on that hierarchy. No full-domain inverse-square rate, Wightman cluster theorem, unconditional T0 claim, or status is asserted.

This is a written assembly proof and an explicit remaining interface premise. It is not an audit, and it has not been independently checked.
