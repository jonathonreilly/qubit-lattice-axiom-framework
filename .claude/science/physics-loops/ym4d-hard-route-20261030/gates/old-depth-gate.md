lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T20:31Z

# Gate: `library/old-depth.md` (row 141)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), max effort, Mac mini worker, 2026-11-03; statement pinned at commit 6b7b42737 of `claude/ym4d-hard-route`. A Claude gate of a Codex text, done by hand; not an audit; it grants no status. No numerics were run.

Read for this gate: `library/old-depth.md` (all); `wf-room-2.md` §6 (Current-I); `o1-decoupled.md` §2 (Definition D) and `gates/o1-decoupled-gate.md` §2.1; `h-walk.md` §§4, 6 (Theorem W); `removed-fix.md` (5.3). Also the Sussman–Alpoge outline at `31a47c543775` (`YM4_sketch_500.tex`, fetched by URL into a scratch folder, not committed): (R8)-(R11) at SA 5747-5822; tower and core definitions with Theorems 5-6 at SA 9605-9790; constant order, room clause, R9 and mechanisms (i)-(j) at SA 10244, 10355-10404, 10552-10584; WF1-WF13 at SA 15719-16220. Balaban CMP 109 (3.37)-(3.38), p. 278 (`~/ym4d-papers/cmp109.txt`).

Credit: the construction under test is Codex's. The window, the box maps, R9 and WF1-WF13 are Ethan Sussman and Levent Alpoge's outline, with Claude and Codex as authors of their text. Restriction at a background's own averages is Balaban's (CMP 109 (3.38)). Current-I and Definition D are Claude's local specifications, with their Codex gates.

## Verdicts

**First failing step: none.** By hand, every computation of the counterexample checks out, and Lemma CR and (7.1)-(7.13) hold as the implications they are stated to be. There are two scope defects, and neither is a wrong step:

- **D1:** the one-cube partition lies outside the outline's own room clause. It is repaired here by **Proposition V**, which carries the counterexample to the outline's grid partitions.
- **D2:** what is refuted is the direct WF4 replacement (row 137's identity), not WF7 as the outline words it.

| Statement | Verdict |
|---|---|
| §1, (1.1)-(1.6): one-cube readout \(z^2f\) against actual current \(zf\) | ADVANCE (implication from Flat lift, D, R9, Current-I) |
| §4, Cartan family (4.1)-(4.9) | ADVANCE |
| §5, window (5.1)-(5.10) | ADVANCE: admissible under the first rule, Current-I, and D with its one-cube option |
| §5.3, room | ADVANCE (radii depending on \(k\), which is all the argument uses) |
| §6.1-6.3, coefficient \(\ge\sigma_1^3/8\) | ADVANCE at \(z=1/2\). It does not hold on the whole disc (it vanishes to leading order at \(z=0,1\)), and the argument does not need that |
| §6.4, §8, Result: scope statements | CORRECT; see D2 |
| Lemma CR, (2.1)-(2.3) | ADVANCE |
| (7.1), (7.2) | ADVANCE (an identity, and its value in the example) |
| (7.3)-(7.6) | ADVANCE as implications |
| Collar response lemma (7.7)-(7.9) | ADVANCE after a wording repair (W1) |
| (7.10)-(7.12) | ADVANCE as implications |
| (7.13) | ADVANCE as an implication from RF-CD (its Claude gate, row 136, is pending) |
| (7.14)-(7.15) | CORRECT-NO-ADVANCE: well-posed on admitted charts, and the endpoint identity holds. Its use as the window extension is open |

## 1. Counterexample first: the window, clause by clause

### 1.1 The readout algebra (§1), against the sources

- **R9** (SA 10360-10366): \(X=\mathcal C(A_\bullet-H(s)X)\), \(A_\bullet=H_1(s)B'+\mathbf A\), \(\mathbf A+\mathfrak G(s)\mathsf W_s(A_\bullet)=0\), \(\mathbf H=A_\bullet-H(s)X\).
  - \(\mathcal C\) vanishes to second order.
  - So does \(\mathsf W_s\): it is Lipschitz with constant \(C\widehat b^2r\) on balls of radius \(r\) (SA 10385-10388; mechanism (j), SA 10562), and the response vanishes at \(B'=0\) (SA 5765).
  - So at \((\mathbf 1,0)\), \(\mathbf H(\epsilon)=\epsilon H_1(s)b+O(\epsilon^2)\), and (1.3) holds.
- **D** (`o1-decoupled.md` (2.1)): \(s^\omega\) is the product over every cube meeting the enlarged hull, the walk's own cube included.
  - This is the outline's own convention: "on the cubes around a row where \(s\) vanishes, every term is absent, so that \(Q\mathsf H(s)\) equals \(0\) there" (SA 10562). The \(e^{2^4\bar\kappa}\) left over in mechanism (i) is consistent with it.
  - One cube therefore gives \(H(z)=zH\) and \(H_1(z)=zH_1\). At \(\mathbf J=0\) the \(G_1\) tree vertices vanish, so \(H_1=H\) (`h-walk.md` §7). So (1.2) holds.
- **Current-I** (`wf-room-2.md` (6.1), the same as `removed-fix.md` (5.3)):
  - At \((\mathbf 1,0)\): \(F'_{\mathbf 1}(0)=J(\mathbf 1)=0\), so \(\lambda^{\rm I}_0=0\). Also \(T=O(\epsilon)\) and \(R_{\mathbf H}=1+O(\epsilon)\).
  - Hence \(\dot{\mathsf j}=K^{\mathsf T}H(z)^{\mathsf T}\mathscr L(zh)=z^2K^{\mathsf T}(KH)^{\mathsf T}\lambda=z^2f\), by \(K_0H(1)=1\) ((I-a)).
  - The actual current has derivative \(\mathscr L(zh)=zf\), so (1.4)-(1.6) hold.
  - The gate's \(\mathbf J\)-dependence repair of (6.1) is inactive at \(\mathbf J=0\).

### 1.2 The Cartan family (§4), recomputed

- **Parity.**
  - Block 0 has \(p=\epsilon(v+1)/N^3\), and block 2 has its negative.
  - Block 1 has \(\epsilon(1-(v+1)/N)/N^2\), and block 3 has its negative.
  - Every other block is zero: \(q_{m+1}=q_m\) for \(4\le m\le L-1\), with \(q_L=q_0\).
  - Arcsine is odd, so \(\sum\vartheta=0\) over a period, and \(a\) is periodic.
- **(4.7)** also holds across a block boundary: the first value of block \(m+1\) minus the last value of block \(m\) is \(\epsilon(q_{m+2}-q_{m+1})/N^3\).
- **(4.5)-(4.6).**
  - For commuting links, the mean is the exponential of the mean angle.
  - A contour's direction-2 angle is odd in \(x_2-y_2\) at fixed \(x_1\). So the site factors are \(1\), the end contours of a straight segment cancel, and the level-1 angle is \(\sum_{x_1\in\text{block}}a_{x_1}\).
  - Iterating gives (4.5), and the period sum gives (4.6).
- **(4.8).** \(\partial_{a_i}\sum(1-\cos\vartheta)=\sin\vartheta_{i-1}-\sin\vartheta_i=-\epsilon(q_{m+1}-q_m)/N^3\). The factor \(\eta\) from potential to angle and the pairing factor \(\eta^{-4}\) then give \(J_2=-\epsilon(q_{m+1}-q_m)T\) in level-\(k\) units.
- **Criticality.**
  - Linearized, \((KA)(c)=\eta^4\sum_{b\in{\rm carrier}(c)}A(b)\), so \(K^{\mathsf T}\mu\) takes the value \(\mu(c)\) on the carrier of \(c\). Hence \(J=K^{\mathsf T}\mu\) with \(\mu_2(m)=-\epsilon(q_{m+1}-q_m)T\).
  - \(\mu_2\) does not depend on \(y_2\), so it annihilates the coarse-gradient (site-factor) part of \(D\mathcal M^k\).
  - Perpendicular colour directions vanish by \(e^{itT}\)-invariance.
  - \(U(\epsilon)\) is regular (plaquette angles \(\le2|\epsilon|\eta^2\)), so BG's uniqueness identifies it with the critical orbit.
- **Size of \(f_k\).** \(|f_k(b_*)|=1\) in a block with \(q_{m+1}-q_m=1\), at every mesh.

### 1.3 The window (§5) against the outline's clauses

- **First rule** (SA 9646): cubes of side \(\mathfrak M\) in their own unit, with a gap \(>\rho\) in the outer member's unit. (5.3) is this rule cut at depth \(j=1\), which is what SA 9769 prescribes for the box tower of the inner substitution.
- **Inner substitution** (SA 9759-9766, WF3-WF4).
  - The data are \(U_+=\mathbf 1\), \(\mathbf H_{k+1}=0\), \(\mathbf A=\nu\zeta A_z\), \(B'=0\), \(\varsigma=1\), and a box of \(O(1)\) current cubes.
  - The age is \(k-1\to\infty\), so the global half-datum-ball condition (SA 15827) holds.
- **(5.6).** \(\partial_\epsilon V|_{\nu=0}=0\) and \(\partial_\nu V|_{\epsilon=0}=0\), so the second derivative of the box map does not enter.
- **(5.7)** is Lemma CR (Section 3) differentiated along the Cartan family.
- **(5.8)-(5.9)** are crude: a fixed power of \(\sigma^{-1}\) against \(e^{-\theta dM/\sigma}\). That is enough.
- **The norm in WF7.** WF7's norm is the member's local pair norm in level-\(j\) units (SA 15857-15861). In it the current carries the factor \(L^{-3(k-j)}=\sigma^3\) (SA 9757), and the norm bounds the current at \(b_*\). So the derivative extraction (6.3) is legitimate.
  - Suppose WF7 is read for the construction's fixed amplitude \(\delta_k\) rather than for \(\delta_k=C_b|\epsilon|\). The removed field vanishes at \(B'=0\), so Schwarz's lemma in \(B'\) gives the same derivative bound, and §6.2 stands either way.
- **The coefficient at \(z=1/2\).** \(|(z^2-z)\sigma^3f_k(b_*)|=\sigma^3/4\) and \(\mathcal E_k=o(\sigma^3)\), so the coefficient is \(\ge\sigma^3/8\) for large \(k\).
  - It is not \(\ge\sigma^3/8\) on the whole disc: it vanishes to leading order at \(z=0\) and \(z=1\).
  - One point of the disc suffices against a bound claimed on all of it.

So the window meets every clause the queue names: the first rule, Current-I, and D with its one-cube option. The only scope question is D1.

## 2. D1: the one-cube partition and the outline's room clause; Proposition V

The outline says: "Statements 7, 8 need room for three cubes of side \(\ell_{\mathsf P}\)" (SA 10244). The decoupling partition is "the partition of side \(\ell_{\mathsf P}\) in statement 7" (SA 10552), with \(\ell_{\mathsf P}\) chosen after \(L,M_1,R_1,\bar\kappa\) (SA 10582). A one-cube partition has no such room. `gates/o1-decoupled-gate.md` §2.1 admits the one-cube option for Definition D ("small tori"), so the note is right for D as gated. The outline, however, asserts statements 7-8, and with them the decoupled discs of WF5-WF7, only for grids with room. As written, the counterexample reaches the outline only through that local option. The following removes the dependence.

**Proposition V (grid version).**

*Inputs.* Those of `old-depth.md` §3, together with `h-walk.md` Theorem W(a)-(b) at the flat pair (gated in `gates/h-walk-gate.md`).

*Setting.*
- Let \(\mathcal P\) be a grid of cubes of side \(\ell_{\mathsf P}\) on a torus with room for three cubes per direction. The torus side is a common multiple of \(L\) and \(\ell_{\mathsf P}\).
- Fix \(\Delta_*\in\mathcal P\), and put \(s_{\Delta_*}=z\) and \(s_\Delta=1\) for every other cube.
- Translate the profile (4.1) so that a block with \(q_{m+1}-q_m=1\) contains the centre of \(\Delta_*\), and take \(b_*\) there.
- Build the window of §5 around \(b_*\), with \(M\) and \(R\) as there. \(R\) may meet many cubes of \(\mathcal P\).

*Claim.* There is \(\ell_*=\ell_*(L,M_1)\) such that, for \(\ell_{\mathsf P}\ge\ell_*\), the direct replacement of §6.1 satisfies
\[
 \partial_\epsilon\partial_\nu[\mathcal R_{1,k}]_J(b_*)\big|_{0,0}
 =\sigma^3(z^2-z)\,(f_k+r_k)(b_*)+o(\sigma^3),
 \qquad |r_k(b_*)|\le\tfrac12\ \text{ for every }k .
\]
At \(z=1/2\) its norm is \(\ge\sigma^3/16\) for all large \(k\), and the contradiction of §6.2 with WF7 follows word for word.

*Proof.*

(a) **Exact factor on \(\Delta_*\).**
- By Theorem W(b), the output of \(T_\omega\) lies in \(\operatorname{supp}\tilde h_{\kappa_0}\) and its input in \(\operatorname{supp}\theta_{\kappa_n}\), both inside \([\![\omega]\!]\subset[\![\omega]\!]^+\).
- So a kernel entry \(T_\omega(x,c)\ne0\) with \(x\) or \(c\) in \(\Delta_*\) has \(\Delta_*\in\mathsf P(\omega)\), and then \(s^\omega=z\).
- Let \(H_\Delta\) be the part of the sum (2.1) of `o1-decoupled.md` over walks with \(\Delta_*\in\mathsf P(\omega)\). It is absolutely convergent by Theorem W(a).
- Then \(H(s)=H+(z-1)H_\Delta\), and the same holds for \(H_1=H\) at \(\mathbf J=0\).
- Moreover \(H_\Delta(x,\cdot)=H(x,\cdot)\) for bonds \(x\) in \(\Delta_*\), and \(H_\Delta(\cdot,c)=H(\cdot,c)\) for rows \(c\) in \(\Delta_*\).

(b) **Field.** By R9, \(\dot{\mathbf H}=H_1(s)b=zh+(z-1)w\) with \(w:=H_\Delta b-h\). By (a), \(w=0\) on the bonds of \(\Delta_*\).

(c) **Assigned current.**
- By (6.1) at \((\mathbf 1,0)\), \(\dot{\mathsf j}=K^{\mathsf T}H(s)^{\mathsf T}\mathscr L\dot{\mathbf H}\).
- The rows \(c\) with \(K(c,b_*)\ne0\) lie in \(\Delta_*\), so on them \(H(s)^{\mathsf T}\) acts as \(zH^{\mathsf T}\).
- With \(\mathscr L\dot{\mathbf H}=f+(z-1)(f+\mathscr Lw)\) and \(K^{\mathsf T}H^{\mathsf T}f=f\), this gives
  \[
   \dot{\mathsf j}(b_*)=z^2f(b_*)+(z^2-z)\,r(b_*),\qquad r:=K^{\mathsf T}H^{\mathsf T}\mathscr Lw .
  \]

(d) **Actual inner current.** WF4 does not involve \(s\). Its mixed derivative at \(b_*\) is
\[
 z\mathcal J_RDM_{T(R)}(\mathbf 1)[\zeta h](b_*)+(z-1)\mathcal J_RDM_{T(R)}(\mathbf 1)[\zeta w](b_*).
\]
- The first term is \(zf_k(b_*)+O(C_M\sigma^{-3}e^{-\theta dM/\sigma})\), by (5.7)-(5.9).
- In the second term, the datum vanishes on every row whose carrier lies in \(\Delta_*\): \(w=0\) there, and the average is local (SA 7127). So the datum sits at Euclidean distance \(\ge\ell_{\mathsf P}/2-C_L\sigma\) from \(b_*\), that is, at \(d_T\ge\ell_{\mathsf P}/(2\sigma)-C_L\).
- T4, together with a finite-lattice comparison of norms that costs a fixed power of \(\sigma^{-1}\), bounds the second term by \(C\sigma^{-p}e^{-\theta\ell_{\mathsf P}/(2\sigma)}=o(\sigma^3)\).

(e) **Subtract and change units.** Subtract (d) from (c) and multiply by \(\sigma^3\). This gives the display.

(f) **Bound on \(r\).**
- \(r(b_*)=\sum_cK^{\mathsf T}(b_*,c)\langle DHe_c,Dw\rangle\), summed over the boundedly many rows \(c\) near \(b_*\).
- \(Dw\) lives within one bare step of the complement of \(\Delta_*\), so at \(d_{\mathbf B}\ge\ell_{\mathsf P}/2-C\) from each such \(c\).
- Summing (6.2) over walks gives \(\|He_c\|_{\mathcal X,y}\le C_1e^{-(\tau_L/2)d_{\mathbf B}(y,c)}\). For the sub-sum, \(\|w\|_{\mathcal X,y}\le C_2\sup|b|\le8C_2\), uniformly in \(k\).
- The \(E\)-part of the \(\mathcal X\)-norm controls the \(L^2\) norm of the gradient on each pillar (`h-walk.md` §4).
- Cauchy–Schwarz pillar by pillar then gives \(|r(b_*)|\le C_3(L,M_1)\,e^{-\tau_L\ell_{\mathsf P}/8}\). This is \(\le1/2\) once \(\ell_{\mathsf P}\ge\ell_*\).

(g) **Room.** At \(|z|\le1\) we have \(|s^\omega|\le1\), so every decoupled sum is dominated by its absolute sum at \(s=1\). The finite-lattice existence argument of §5.3 therefore applies unchanged. \(\square\)

*What this uses, and what it gives.* Proposition V needs neither Lemma P nor Theorem B: only the walk bounds at \(s=1\) enter. Under the outline's own partition rule and order of constants, the direct replacement violates WF7 for every \(\ell_{\mathsf P}\ge\ell_*\). In the one-cube case \(r\equiv0\), because every walk meets the single cube; this recovers §1.

## 3. Lemma CR and Section 7

**Lemma CR, (2.1): ADVANCE.**
- The proof rests on one dichotomy: a level-\(q\) average with no endpoint in \(\Omega'_{q+1}\) is either a prescribed row, or its double block misses \(\Omega'_q\). This is exactly the outline's convention (SA 9607): \(\Gamma_q\) consists of the level-\(q\) bonds of \(\Omega_0\) with an endpoint in \(\Omega_q\) and none in \(\Omega_{q+1}\), so outward bonds are rows and inward bonds are not.
- With alignment by whole blocks, a level-\(q\) bond with no endpoint in \(\Omega'_q\) has both of its blocks outside \(\Omega'_q\). Locality (SA 7127: \(\mathcal M^q(W)(c)\) depends on \(W\) only in \(B^q(c_-)\cup B^q(c_+)\)) closes the induction.
- Every original row has no endpoint in \(\Omega_{q+1}\supset\Omega'_{q+1}\), so it is preserved. The stencil argument and BG's uniqueness then give (2.1).
- This re-proves the outline's Theorem 6(b) (SA 9776-9786), and adds a correct identity-theorem continuation in the critical datum only.
- The citation is right: Balaban CMP 109 (3.37)-(3.38), p. 278, restricts a generated box background to a smaller determining problem at its own averages, with a gauge constant on blocks.
- (2.2)-(2.3) are the chain rule and the derivative of \(g_-Ug_+^{-1}\). Checked.

**(7.1)** is an identity in one fixed chart; its use is to isolate \(E_j\). **(7.2):** the global depth-one projection of the constant torus sequence has no collar, so its coefficient is \(z\sigma^3f_k\) up to the \(\zeta\)-tail. ADVANCE.

**(7.3)-(7.4):** ADVANCE as an implication.
- \(W\) has \(V\)'s averages on every row of \(S^{\le j}\), so \(\beta\) is carried by the meet's new collar rows.
- \(F_R\) is one map, by Lemma CR applied to \(W\) and the meet.
- Identifying the meet with WF4's determining problem is correctly left as a separate premise.

**(7.6):** \(\sum_{q<j}(\rho\xi_q+\mathfrak M\xi_{q+1})/\xi_j=\rho\sum_{m=1}^{j}L^{-m}+\mathfrak M\sum_{m=0}^{j-1}L^{-m}\le(\rho+L\mathfrak M)/(L-1)\). ADVANCE. (7.5) carries RF-G's hypotheses, as stated.

**Collar response lemma (7.7)-(7.9):** ADVANCE.
- The integral formula is right, and so is \((v+t\beta)'=(1-t)v'+tw'\).
- The Cauchy step costs \(K/r\) per unit direction, and the weighted variant is right.
- **W1 (wording).** The Cauchy step evaluates \(DF_R\) at \(u+\zeta u_0\) with \(|\zeta|<r\). So (7.7) must hold on the \(r\)-neighbourhood, in the normalized supremum norm, of every point of the segments, not only "on the common datum neighbourhood". The hypothesis should say so.

**(7.10)-(7.12):** implications, ADVANCE.
- (7.10)'s \(B\le Cr\) for an unweighted collar sum is a strong premise. The note says plainly that it is not proved.
- (7.12) is the triangle inequality.

**(7.13):** RF (7.5) plus the change of units (potential \(\sigma_j\), current \(\sigma_j^3\le\sigma_j\)). It is an implication from RF-CD, whose Claude gate (row 136) is pending.

## 4. Is (7.14) well-posed?

Yes, as a map. Verdict: CORRECT-NO-ADVANCE, since it is a change of specification and not yet a closure.

- **The map.** \(V\mapsto\Phi_{S^{\le j}}(M_{S^{\le j}}V)\), in Theorem 3's Landau representative and with the actual current of its image, is a composite of two maps. The first is the holomorphic extension of the nonlinear averages (SA 1b.2). The second is BG's complex datum chart (A1, rows 79, 81). The composite is defined wherever \(M_{S^{\le j}}V\) lies in that chart.
- **Its datum.** It has the supremum-norm size of the inner datum, so (WF5)-(WF6) give the inclusion at old ages. At the finitely many young ages where the global half-datum-ball condition fails (SA 15827-15831), chart membership is an extra premise. (7.15) states it as an assumption.
- **Endpoints.** At complete physical endpoints, \(V(0)=U_+\) and \(V(1)=e^{i\eta\mathbf H}U_+\) are depth-\(k\) critical, and \(S^{\le j}\subset S\) memberwise. So Lemma CR gives \(\Phi(MV(i))=V(i)\) up to the residual gauge. \(G_j\) is gauge invariant, so (7.15) follows by the fundamental theorem of calculus.
- **Its window decomposition.** The decomposition of (7.15) is WF3 exactly, with the global old map in place of the original pair. Its inner term is WF13a unchanged. Its near-window removed term is the collar comparison (7.3)-(7.9) and nothing else.
- **At Proposition V's window.** The removed current of (7.14) at \(b_*\) is the difference of two old-critical projections of one datum. That is an old-rate collar term, for every \(z\): neither the readout factor of §1 nor the face term \(r_k\) enters.
- **Open, as the note says.** The filing (local members, read sets, fine brackets, declared domains), the (7.10) bounds, and how the next step uses independent currents, since (7.14) reads \(\mathbf J\) only through \(\mathbf H(s;P,B')\).

## 5. D2, and whether the composition route survives

**What is refuted.** The note's \(\mathcal R_{j,k}\) (§6.1) compares the assigned step pair (R8/R10, current from Current-I) with WF4's pair, whose current is the box background's actual current. The outline words its removed fields differently: "The inner pair in (WF4) carries the actual current of its generated box background, also for complex data on its analytic domain. Outer and removed substitutions use their prescribed reduced-current assignments away from the critical physical locus. At physical parameters these assignments agree with the currents of the corresponding critical configurations" (SA 15954-15959). It also asserts the window identity only at complete physical pairs (SA 15840-15846). In the outline's reading, then, the box side of a removed field carries its own prescribed reduced current, and off the physical locus the inner, outer and removed terms need not add up.

The counterexample therefore refutes two things:

1. Row 137's target: the identity "assigned step pair = WF4 old pair up to \(e^{-cM/\sigma_j}\)" on the full discs, for Current-I and D. By Proposition V this holds on the outline's grid partitions too.
2. Every proof of WF7 that puts WF4's actual pair on the box side of the removed field. That is the only mechanism on file for the factor \(e^{-cM/\sigma_j}\) (`removed-fix.md` §7, row 137).

It does not refute WF7 as the outline words it. The note says so itself (§6.4, §8, Result). The row 137 summary in FINISH, "against WF7's age-uniform \(C\sigma e^{-cM/\sigma}\)", needs that qualifier.

**The outline's reading at Proposition V's window (a risk, not decided).**
- The outline never specifies the old-depth box-side reduced current (C3 of `wf-room-2.md`). (S6) there uses a box system at the step's own depth, whose comparison gives only \(e^{-cM}\), as in (7.13).
- The natural old-depth choice is the note's §6.4 example: the old box lift \(H_R\), decoupled by the same \(s\) under Definition D, read on WF4's field.
- WF4's field tangent \(u\) is exactly box-critical: \(\mathscr L_Ru=K_R^{\mathsf T}\mu\) in the Landau representative. The support property of the box walk expansion gives \(H_R(s)^{\mathsf T}=zH_R^{\mathsf T}\) at rows in \(\Delta_*\).
- So the box readout at \(b_*\) is \(zK_R^{\mathsf T}\mu(b_*)\), which is \(z\) times the actual box current, \(=z^2f_k(b_*)+o(1)\) by Proposition V (d).
- Subtracting this from (c), the removed current at \(b_*\) is \(\sigma^3(z^2-z)r_k(b_*)+o(\sigma^3)\). WF7 for this specification therefore holds at this window only if \(r_k(b_*)\) tends to zero like \(\sigma^{-p}e^{-c/\sigma}\).
- \(r_k\) is a quantity at \(s=1\): the part of the physical multiplier response at \(b_*\) carried by walks whose hull avoids \(\Delta_*\). Nothing visible makes it vanish, and its size, of order \(e^{-\tau_L\ell_{\mathsf P}/8}\), does not shrink as \(\sigma\to0\). Whether \(r_k(b_*)\ne0\) is not decided here.
- This is a face effect: near parameter faces the decoupled response is not old-critical, while the box side is. In the one-cube case \(r\equiv0\), which is why the note's §6.4 cancellation holds there.

**Carrying the defect does not work.** (7.11) keeps \(E_j\).
- Per old base point, \(E_j\) is of order \(|\nu|\delta_k\sigma_j^3\) in level-\(j\) units (its current component), against WF7's \(\sigma_je^{-cM/\sigma_j}\).
- WF11 multiplies by the \(C_M\sigma_j^{-4}\) base points of a window. That leaves \(s_kg_j\rho_j\sigma_j^{-1}\) in place of \(s_kg_j\rho_j\sigma_j^{-3}e^{-cM/\sigma_j}\).
- WF12 can absorb only the latter. So WF11-WF12 cannot be obtained with the defect carried, and a change of specification is forced, as the note concludes.

**Does the route survive?**
- Not in its direct form (removed field = assigned pair minus WF4 pair), for Current-I and D, on the outline's own partitions.
- The outline's literal reading survives this example only through an unspecified old-depth box readout, and the natural choice leaves a face term not shown to vanish.
- (7.14) is the one construction on file that this window does not break. On this evidence, rank 4's next lane should adopt (7.14) as the specification and prove its filing and the (7.10) bounds.

**Remark at \(s=1\) (not proved).**
- Both direct readings compare WF4's field with the unprojected interpolation \(\varphi_t=e^{i\eta t\mathbf H}U_+\).
- Along a critical family \(U(\epsilon)=e^{i\eta(\epsilon h+\epsilon^2h_2+\dots)}\), Lemma CR gives \(D\Pi[h]=h\) and \(D\Pi[h_2]=h_2-\tfrac12D^2\Pi[h,h]\) for the box projection \(\Pi\). Hence, on the plateau and modulo gauge,
  \[
   \Pi(\varphi_t)-\varphi_t=\tfrac12(t^2-t)\,\epsilon^2D^2\Pi[h,h]+O(\epsilon^3).
  \]
- So the removed field at \(s=1\), taken pointwise in \(t\), carries \(\tfrac12(2t-1)\epsilon^2D^2\Pi[h,h]\).
- Its \(t\)-integral vanishes: at \(s=1\) the integrated difference telescopes to critical endpoints. SA 16100-16104, however, applies WF7 before the \(t\)-integration.
- For the Cartan family \(D^2\Pi[h,h]=0\), because the family is odd in \(\epsilon\). Whether it is nonzero for an admissible nonabelian family is not decided here. (7.14) is not affected.

## Defects that break something

1. **D1 (scope).** As written, the counterexample uses a one-cube partition, which SA 10244's room clause excludes. What it breaks: the reach of the counterexample to the outline as worded. Repaired here, with proof, by Proposition V.
2. **D2 (scope of the claim).** The counterexample refutes row 137's identity and every proof of WF7 through WF4's actual pair, not WF7 as worded. What it breaks: any reading of row 137 as "WF7 is false".
3. **W1 (wording).** Hypothesis (7.7) must hold on the \(r\)-neighbourhood of the segments. It breaks nothing once stated.

## Result

First failing step: none. The window of §§4-6 is admissible under the first rule, Current-I and D (one-cube option). Its mixed current coefficient is \(\ge\sigma_1^3/8\) at \(z=1/2\). Lemma CR and (7.1)-(7.13) pass as implications, and (7.14) is well-posed.

Added here: Proposition V. It moves the counterexample onto the outline's grid partitions for \(\ell_{\mathsf P}\ge\ell_*(L,M_1)\). It is new same-model (Claude) text and needs a Codex gate before it counts. The hardest steps are (a), the support property read from Theorem W(b), and (f), the bound on \(r\).

Still open:
- WF7 as worded: its old-depth box readout is unspecified, and the natural choice leaves \(\sigma^3(z^2-z)r_k(b_*)\).
- (7.14)'s filing and its (7.10) bounds.
