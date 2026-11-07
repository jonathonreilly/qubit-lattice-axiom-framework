# Check of library/walks-gw.md

- File checked: library/walks-gw.md (1069 lines; research text by Codex at a6e07cc0a8).
- Task: FINISH row 447. One line-by-line check.
- Date: 2026-11-07.
- Status: complete.

Sources read for this check: walks-gw.md in full (by ranges); print-inverse-r2.md §§3.1–3.4, 4.3 (Lemma 4.4), 5.1–5.3, 7.1;
gates/pi-r2-gate.md §8 (K10 detail); layer-pkg.md §§1.1–1.2, 2.1, 4.4; flat-port.md §§8.1–8.3, 11, 12;
a3-balaban.md §5; b98p5.md §1, §2.3 (11); b102.md H6 (630–720);
CA-I 13800–13850, 15260–15425, 166588–166601. No Balaban page image was needed: walks-gw.md makes no
direct load-bearing claim about a printed Balaban display; its Balaban content enters through PI.

## Verdict summary

| Section | Verdict | One line |
|---|---|---|
| Theorem statement (36–105) | ADVANCE | The claims match the proof; the word convention and its limits are stated. |
| 1. Strong source spaces | ADVANCE | The powers in (P1)–(P2) are scale-consistent and dual; the energy-dual remark is correct and not load-bearing. |
| 2. Flat mixed inverse | ADVANCE | Cell energy-dual bounds, (P3) decay, (P4)–(P5) summation and the Poisson upgrade (P6)–(P8) are correct. |
| 3. Strong coefficient comparison | ADVANCE | Every block of (P9) checks against PI Lemmas 4.4, 5.1, 5.2; only B and its first difference enter. |
| 4. Cutoff transitions | ADVANCE | (P11)–(P13), the transposes and the footprint containment are correct; the enlargement of PI's constants is legitimate. |
| 5. Endpoint majorants, spare exponentials | REVISE | (P14) and the Euler count are correct; the concatenated tree must also pass through the cubes met by insertion carriers, and the weighted majorants must be defined. Repair below. |
| 6. First-order branches | ADVANCE | The differentiated source pairs, the CA-I 13812–13848 formula and the j_* choices are correct. |
| 7. Averaging vertices, nonlinear source | REVISE | The averaging port and the scalar majorant are correct; the Wilson vertex bound is cited from a real-background calculation and needs one complex-background step. Repair below. |
| 8. Current-corrected source inverse | ADVANCE | (P18), the single tag per concatenation (CA-I 15266–15310) and the composite tags are correct. |
| Necessary test (4.11) | ADVANCE | (P19) follows from (T2) and the norm inequality. |
| Constant order | ADVANCE | Non-circular; see the table. |

## Theorem statement (lines 36–105) — ADVANCE

The three lines of (T2) are the three lines of GW in layer-pkg.md §4.4. The norms are those of
layer-pkg.md (1.1)–(1.2). The word convention at lines 27–34 matches CA-I 15283–15304: each primitive
operator of the list at CA-I 15281–15283 is expanded into its walks, the defining series of
\(G^J_\pi,\mathsf q_J,\tilde G^J\) into concatenated walks with side branches, and each walk term gets
one factor per cube met. The composites, \(H_0\) among them, are formed afterwards (CA-I 15304–15306).
So the two factors of \(H_0\) keep their own tags. This is correct.

The limits at lines 99–105 and 979–983 are correct and necessary. The identity convention
\(I=\sum_\tau h_\tau^2I\) for \(R=I-P\) is a choice. The account does not fix it. At \(s\equiv1\) it
gives the account's operator, since \(\sum h_\tau^2=1\) on every component (PI §5.2). This is
consistent with CA-I 15336 (iv).

## 1. Strong source spaces (lines 109–148) — ADVANCE

Check of (P1)–(P2). Take a cell of side \(s\sim m\). Each energy term of PI §3.2 is dimensionless
when \(A\sim m^{-1}\), \(h\sim m^{-2}\), \(\lambda\sim1\), \(\mu\sim m^{-4}\), \(\nu\sim1\). These are the
powers of (P1). The source weights of (P2) are the duals under the fine, top and counting pairings.
Row 1 of \(M_5\) pairs with \(A\) (weight \(m^3\) on \(f\)); row 2 pairs with \(h\) (\(m^2\) on \(g_1\));
row 3 pairs with \(\lambda\) (\(m^4\) on \(g_2\)); rows 4 and 5 pair with \(\mu,\nu\) (weight 1). I checked
this against the matrix in PI §3.1. It is correct.

The \(H^{-1}\) remark (lines 140–145) is correct: \(f=\eta^{-1}(-1)^{|k|}\) has bounded dual norm and
\(\Delta\Delta^{-1}f=f\) has size \(\eta^{-1}\). It bears no load.

## 2. The flat mixed inverse (lines 150–293) — ADVANCE

*Cell energy-dual bounds (158–172).* For a source on one cell: \(\|f\|_{E^*}\le s\|f\|_2\le s^3|f|\);
\(\|g_1\|_{L^2}\le s^2|g_1|\); \(\|g_2\|_{(H^2_m)^*}\le s^2\|g_2\|_2\le s^4|g_2|\); the top and counting
norms give \(|g_3|,|g_4|\) up to a bounded row count. These match (P2). Correct.

*Decay (P3).* flat-port.md §11 (lines 787–789) gives the absolute refinement: the sum of the norms of
all length-\(n\) words from a fixed patch is at most \(B_Lq^n\), with \(q<1/2\), in both directions. A
word joining cells at layer distance \(d\) has at least \(d/D-1\) transitions. So (P3) holds with
\(a=\log(1/q)/D\). Correct. No positivity of the mixed matrix is used.

*Summation (P4)–(P5).* These are a3-balaban.md (5.3)–(5.5), word for word. That proof needs the rate
before the gap (a3-balaban.md line 149). walks-gw.md uses the order rate, then gap. Correct.

*Upgrade (P6)–(P7).* I checked (P6) against \(M_5\) in PI §3.1. Row 3 gives
\(A_sh-Q'^T\mu=g_2\); row 2 gives \(-D^TA+h+A_s\lambda=g_1\); row 1 gives
\(B_vA-Dh-K^T\nu=f\), with \(\Delta(1)+DD^T=\Delta_{\rm comp}\) on fine 1-forms. The local bounds
\(m^4|\mu|,|\nu|\le\|X\|_{X,\rm loc}\), \(|Q'^Tm^{-2}Q'h|\le Cm^{-4}\|h\|_{2,\rm loc}\),
\(|Q^TaQA|\le Cm^{-4}\|A\|_{2,\rm loc}\) and \(|K^T\nu|\le Cm^{-3}|\nu|\) follow from Jensen and the
flat column count. The order \(h\), then \(A\), then \(\lambda\) is consistent: the \(A\) equation needs
only \(\nabla h\), and the \(\lambda\) equation needs \(D^TA\) and \(h\). The powers from (P7) are the
powers of (P1). The kernel bound in (P7) is the one in flat-port.md 144–204. Correct.

*Boundaries (280–283).* In PI's models the outer boundary is \(\partial(\Omega_0\cap K_0)\). There the
model level is zero, since \(K_1\) lies \(\rho'_F\ell_0\) inside \(K_0\) and the tower gaps hold
(PI §5.2, "Models"). At \(m=\eta\) every entry of \(Z\) is bounded by the local \(L^2\) norm and finite
differences. Correct.

*(P8).* \(B_Z\) depends on the flat construction, the flat rate and the (P5) constant. It does not
depend on \(M_t\). Correct.

Note (no repair needed). The flat-model gap is PI's \(\rho_F\) (§3.3 item 1). It is a constant choice,
not a tower hypothesis. Lines 51 and 199 require it above the (P5) floor at a rate \(a'<a\). This is
legitimate: flat-port.md §8.2 (line 582) and §12 fix \(M\) first and the gap afterwards, and \(q,D\) do not
depend on the gap. See the constant table.

## 3. Strong comparison of the coefficients (lines 295–397) — ADVANCE

*Differences.* \((D_U-D_1)v=cv_{\rm shifted}\) with \(|c|\le Ce/m\), \(|\partial c|\le Ce/m^2\) is PI
Lemma 5.1 ("Differences"). The second-order error is \(Ce(m^{-1}|\partial v|+m^{-2}|v|)\). With the
weights: \(g_1\): \(m^2\cdot e(m^{-1}|\partial\lambda|+m^{-2}|\lambda|)\le Ce\|X\|_Z\); \(g_2\):
\(m^4\cdot e(m^{-1}|\partial h|+m^{-2}|h|)\le Ce\|X\|_Z\). The first-order blocks \(-D_U\), \(-D_U^T\)
give \(Cem^2|h|\) and \(Cem|A|\). Correct.

*Rows.* PI Lemma 4.4 (lines 577–580) gives row sum \(\le C_R\varepsilon\) and column sum
\(\le C_R\varepsilon(\eta/\ell_j)^4\) for \(Q_j(U)-Q_j(1)\), with \(\varepsilon=Le\) (Lemma 5.1, "Rows").
Then \(|(K(U)^T-K(1)^T)\nu|\le\eta^{-4}m\,C\varepsilon(\eta/\ell)^4|\nu|\le Cem^{-3}|\nu|\). The same
computation gives the \(Q'^T\mu\) block (\(m^4\cdot Ce|\mu|\)) and the rows \(KA\), \(Q'\lambda\). No
derivative of a density appears, because \(V\) carries no derivative. Correct.

*Vector Hessian.* PI Lemma 5.1 gives \(|X_v-X^1_v|\le C\eta em^{-1}|v|\) and
\(|P-1|\le C\eta^2e/m^2\). The decomposition \((d+L_B)^*(1+E)(d+L_B)\) plus the commutator term is
exact. The \(d^*Ed\) bound uses \(|E|\le C\eta^4e^2m^{-4}\) and one difference \(\le2/\eta\):
\(C\eta^3e^2m^{-4}|\partial v|\le Ce^2m^{-1}|\partial v|\), since \(\eta\le m\). The other terms check.
Only \(B,\partial B\) enter. Correct.

*Background and norm comparisons; (P10).* The comparison \(D_W=D_{U_r}+c\) is Lemma 5.1 (iii) in
covariant form. With \(B_ZC_Ze\le1/8\) the Neumann series gives \((8/7)B_Z\); the two norm comparisons
give at most \((9/8)^2(8/7)B_Z<3B_Z\), as in PI Lemma 5.3. Correct.

## 4. Cutoff transitions (lines 399–491) — ADVANCE

*(P11).* With \(|\partial h_\tau|\le C/(M_t\ell_\tau)\) and \(m\le L\ell_\tau\) (two-level property, PI
§5.2), each flat term gives at most \(CL/M_t\) or \(CL^2/M_t^2\). Example:
\(m^3|\partial h||\partial A|\le m^3(M_t\ell_\tau)^{-1}m^{-2}\le L/M_t\). A row commutator is its
kernel times a cutoff oscillation over a double block of side \(\le2L\ell_\tau\), hence \(\le CL/M_t\).
The curved part needs \(e\le c/(M_tC_Zc_Z)\), fixed after \(M_t\). \(C_{\rm com}\) does not depend on
\(M_t\). Correct.

*(P12)–(P13).* \(\|T_\tau\|_{V\to V}\le(C_{\rm com}/M_t)\cdot3B_Z\cdot c_Z\le\theta_Z\). The identity
\(M\sum S_\tau=I+\sum T_\tau\) uses Agreement (PI §5.2) and \(\sum h^2_\tau=1\). The bound
\(\|\sum T_\tau\|_{V\to V}\le D_*\theta_Z\) holds because \(V\) is a supremum norm and at most \(D_*\) boxes
meet at a point. Correct.

*Enlarging PI's constants (452–454).* Put \(B_F\ge B_Z\), \(c_h\ge c_Z\), \(C_{88}\ge C_{\rm com}\),
\(C_C\ge C_Z\) (and the norm-comparison constants). Each is used in PI only as an upper bound. Then PI's
\(\theta\ge\theta_Z\), so PI item 3 gives \(\theta_Z\le(4D_*)^{-4}\). PI item 7 then gives
\(B_ZC_Ze\le1/8\) and \(2c_ZC_Ze\le C_{88}/M_t\). Correct and non-circular.

*Transposes (468–482).* \(T_\tau^T=h_\tau M_\tau^{-1}(h_\tau M_\tau-M_\tau h_\tau)=L_\tau\). This uses
bilinear symmetry of \(M_\tau\), which I checked from the matrix in PI §3.1. \(\|L_\tau\|_{Z\to Z}\le\theta_Z\).
The pairing check \(m^4\cdot m^{-1}\cdot m^{-3}=1\) is correct for each pair. Correct.

*Footprints (484–491).* A bump read at a point of the enlarged support has centre within
\((1+L)M_t\ell_\tau+2\eta\); its tile reaches \((1+3L/2)M_t\ell_\tau+2\eta<(2L+2)M_t\ell_\tau=\widehat r\ell_\tau\).
Correct.

## 5. Endpoint majorants and spare exponentials (lines 493–601) — REVISE

*Cells and (P14).* \(k_\omega(y,z)\le\|W_\omega\|_{V\to Z}\), since restriction of a \(V\) source to one
cell has norm one. The geometry \(d\le D_X(n+1)\) is PI (c); cells add a fixed constant, absorbed in
\(C\). The bound \(t_\omega\le17D_X(n+1)\) is pi-r2-gate.md §8 (K10 detail). It needs footprints smaller
than the cube side; the floor \(4\widehat r+8L\) gives this. With
\(\mu=\log(1/\theta_Z)/(140D_X)\): \(\mu(d+2t_\omega)\le\tfrac14(n+1)\log(1/\theta_Z)\), so
\(\theta_Z^ne^{\mu(d+2t)}\le\theta_Z^{-1/4}\theta_Z^{n/2}\). This is (P14). Also
\(\mu=\delta_q(\theta_Z)/20\le\delta_q(\theta_Z)/17\), so the gate's rate restriction holds.
Summation: \(\sum_nD_*^{n+1}N_t\theta_Z^{n/2}\le C\), since \(D_*\theta_Z^{1/4}\le1/4\). Correct.

*\(BW_\Delta\) (540–558).* \([M_4^{-1}]_{AA}=G_0\) is PI Lemma 7.1 (ii). The \(AA\) block of
\(M_5^{-1}\) is \(G_0-G_0K^T(KG_0K^T)^{-1}KG_0=G_0-G_0Q^Tq_0QG_0\), with \(K=mQ\),
\(K^T=Q^Tm^{-3}\). Correct, and not used to change a switched value.

*Euler count (560–582).* A tree of layer length \(t\) has axial length \(\le\ell_kt\). Its doubled
traversal splits into at most \(1+4t/M_{\rm dec}\) arcs of length \(\le M_{\rm dec}\ell_k/2\). Each arc
meets at most \(2^4\) cubes. So the tree meets at most \(16+64t/M_{\rm dec}\) cubes. Correct. With
\(M_{\rm dec}\ge64\kappa_1/\mu\), \(e^{\kappa_1\#}\le e^{16\kappa_1}e^{\mu t}\). This reproduces CA-I
15392–15402 without the printed count. Correct.

*Defect.* (P15) needs a tree that passes through **every** cube that the tag counts (CA-I 15367).
CA-I 15302–15304 counts the cubes met by the localisation domains of the pieces and side branches.
walks-gw.md counts more: its footprints "include every branch and every local carrier" (lines 901–902).
Lines 574–576 supply the tree only for the complete footprints of PI words. The step
\(t_\varpi\le\sum t_\omega+c_\iota n_\iota\) (the second inequality of (P15)) is not proved: a joining
segment of length \(\le c_\iota\) need not meet every cube met by an insertion carrier. Also the
majorants \(b^*,b^*_\Delta,g^*,h^*,\theta^*\) and \(C_1,C_2,C_3\) must carry the weight that pays (P15);
the text implies this ("one spare exponential pays (P15)") but never defines them so. The gap is
repairable.

*Repair (replace lines 574–576 and add after (P15)).*

> For a primitive concatenation
> \(\varpi=(\omega_0;\iota_1,\omega_1;\dots;\iota_n,\omega_n)\), side branches included, build a tree
> \(T_\varpi\) as follows. For each piece \(\omega_i\) take the tree of pi-r2-gate.md §8: it passes through
> a representative of every decoupling cube met by the complete footprint of \(\omega_i\), and has layer
> length \(t_{\omega_i}\le17D_X(|\omega_i|+1)\). Each local insertion \(\iota_i\) has a complete carrier:
> the double blocks of its averaging rows, its plaquette reads, the reads of \(\mathfrak j_J,\mathfrak k_J\)
> and its endpoint stencils. This carrier has layer diameter at most a fixed \(c_\iota=c_\iota(N,L)\),
> hence axial diameter at most \(c_\iota\ell_k\). Enlarge the first cube floor to
> \(\max\{4\widehat r+8L,\ c_\iota,\ 64\kappa_1/\mu\}\). Then the carrier meets at most \(2^4\) cubes. Join
> the insertion point to the end anchor of \(\omega_{i-1}\), to the start anchor of \(\omega_i\), and to
> one representative in each cube met by the carrier. Since
> \(d(y'_{i-1},y_i)\le c_\iota\) (CA-I 15357), this adds at most \(17c_\iota\) of layer length. Attach each
> side branch at its insertion point in the same way. The result is a connected graph through every cube
> met by the term; prune it to a tree. So
> \[
>  t_\varpi\le\sum_i t_{\omega_i}+17c_\iota n_\iota ,
> \]
> and the Euler count applies to \(T_\varpi\). Hence (P15) holds with \(c_\iota\) replaced by
> \(17c_\iota\).
>
> Define every first-order and graph majorant of §§5–8 with each piece weighted by its spare factor:
> \(b^*:=\sup_y\sum_{\omega,z}k_\omega(y,z)e^{\mu t_\omega}e^{\delta_*d(y,z)}\), and the same for
> \(b^*_\Delta,g^*,g^*_\Delta,h^*,h^*_\Delta\); in \(\theta^*\) and in \(C_1,C_2,C_3\), weight each insertion
> by \(e^{17\mu c_\iota}\). By (P14), \(k_\omega e^{\mu t_\omega}\le C\theta_Z^{n/2}e^{-\mu d-\mu t_\omega}\),
> so these sums are finite for \(\delta_*\le\mu\). They depend on \(\mu\) but not on \(\kappa_1\). With these
> definitions, (P15) and the term-by-term product give \(|\sigma_\varpi|\prod k\le e^{16\kappa_1}\prod(\text{weighted }k)\),
> which is the form used in (P18) and layer-pkg.md (2.2).

If only the account's cubes are counted (pieces and side branches), the carrier star is not needed:
the union of the piece trees and the joining segments already passes through every counted cube, and
\(t_\varpi\le\sum t_{\omega_i}+c_\iota n_\iota\). The repair covers the stronger count that walks-gw.md uses.

With this repair §5 proves the first line of (T2)–(T3).

## 6. First-order branches for the current insertions (lines 603–738) — ADVANCE

*Vector differentiated source (618–643).* The energy step uses \(\|Dg\|_{E^*}\le C\|g\|_2\)
(flat-port.md §8.3, line 598), with \(g\) localized by smooth cutoffs. The upgrade uses the second line
of (P7) for \(A\). (P9) and (P11) read only \(X\) and \(\partial X\), so they map the enlarged output
(value, gradient, Hölder gradient) into ordinary \(V\). The ordinary \(V\to Z\) inverse also gives the
Hölder gradient by (P7). So the Neumann series and each transition stay in the enlarged pair. Correct.

*Scalar differentiated source (645–676).* \(A_s(U)-A_s(1)=D^T(c\,\cdot)+c^TD+c^Tc\) plus a row term.
Moving the difference off \(B_2Du\) gives \(D^*(B'u)+C'u\) with \(|B'|\le Ce/m\), \(|C'|\le Ce/m^2\).
Its source norm is \(\le Ce\,m^a|u|\). The cutoff commutator has the same form with \(C/M_t\). The
product rule \(hD^*g=D^*(g\,h_{\rm shift})+(\nabla h)g\) makes the source cutoff bounded. I checked
\(P=[M_3^{-1}]_{hh}\) against PI Lemma 7.1 (i). Correct.

*The current formula (685–697).* CA-I 13824–13834 gives exactly
\(\theta=\psi+D_U\varphi\), \(\psi=\mathfrak k_J(\Lambda A)\),
\(\varphi=RG'(\mathfrak j_J(A)+m_3)+RG'D_U^*m_4\), with \(m_3\) pointwise in \([D_U\Lambda A,J]\) and
\(m_4\) in \([\Lambda A,J]\) (CA-I 13811–13820). \(J\) is not differentiated. The weights match CA-I
13836–13838: \(\psi\) at \(-3\), \(\mathfrak j_J(A)+m_3\) at \(-4\), \(m_4\) at \(-3\); so \(\varphi\) is at
\(-2\), in the scalar pair with \(a=2\). The Hölder claim for \(\varphi\) follows from the scalar word
bounds just proved, not from the printed CMP 99b (3.42)–(3.49) that CA-I 13840–13846 cites. Correct.

*Choices of \(j_*\) (706–715).* Composition of normalized cell majorants is submultiplicative by the
triangle inequality for \(d\), with no rate loss. So \(C_1j_*\le1/4\) makes the \(G^J_\pi\) series converge
absolutely. The identity \(q_J=(I+q_0Q(G^J_\pi-G_0)Q^T)^{-1}q_0\) is exact at one. Correct. The
constants \(C_1,C_2\) must be the weighted ones of the §5 repair; they then depend on \(\mu\), not on
\(\kappa_1\).

*Identity piece and transposes (719–738).* Correct as stated.

## 7. Averaging vertices and the nonlinear source (lines 740–911) — REVISE

*Averaging (742–767).* A positive-height row has its double block in \(\Omega_{j-1}\), in heights
\(j-1,j\). It lies in the box \(N_\tau\) of a tile of one of these heights, since \(r_N=7M_t\ge28L\).
(The phrase "based at one of its interior endpoints" should read "the (S1-loc) box \(N_\tau\) of a tile
of height \(j-1\) or \(j\) whose cutoff support contains the row's base point"; (S1-loc) is given only at
the prescribed centres.) PI Lemma 5.2 gives \(\ell_j|B|\le Lm|B|\le LC_S(L^2a_0+a_1)\) there, with a
unitary gauge \(u\). Then \(a_*\le\rho/(16C_{N,L})\) gives \(s_c\|B\|_\infty\le\rho/8<\rho\), which is
b98p5.md (11) (line 254). b98p5.md lines 308 and 359 state that §§2.3–2.4 give (3)–(4) whenever (11)
holds at every row. The density \(C\ell_c^{1-4}\) is b98p5.md (3). Correct.

*Wilson vertex (769–787) — defect.* The cited calculation, b102.md H6 637–718, is written at a real
background. Its constants use "Real backgrounds have unitary transports, so these constants are
independent of the number of fine sites" (b102.md, H6). GW is needed at the complex background \(W\).
walks-gw.md does not supply this step. It is repairable.

*Repair (insert after line 784).*

> At the complex background, work in the local gauge of PI Lemma 5.2 on the box \(N_\tau\) that contains
> the plaquette. There \(W=e^{i\eta B}\) with \(m|B|+m^2|\partial B|\le e\le e_L\le1\), and \(u\) is unitary.
> Each transport is a product of at most four factors \(e^{\pm i\eta B_b}\). So it and its inverse have
> norm at most \(e^{4\eta|B|}\le e^4\), and each differs from the identity by at most \(C\eta e/m\). Hence the
> degree-\(n\) words of the plaquette expansion have total norm at most \((4e^4\eta|A|_{\partial p})^n/n!\),
> and the terms of degree at least four are bounded by \(C|A|^4_{\partial p}e^{4e^4\eta|A|_{\partial p}}\).
> The holonomy obeys \(|W_p-1|\le C\eta^2e/m^2\) (proof of PI Lemma 5.1); this replaces
> \(|U_p-1|\le\alpha\eta^2\ell^{-2}\) with \(\alpha=Ce\). The identities (H6.1) and (H6.2) are polynomial
> identities in the transported fields; they hold verbatim at complex transports in a common frame. The
> holomorphic trace term is \(\tfrac12\operatorname{tr}\{P(t)W_p+W_p^{-1}P(t)^{-1}\}\), as in H6. The Cauchy
> ball of radius proportional to \(r/\ell\) stays inside the exponential and logarithm domain for
> \(e\le1\) and \(r\) below a fixed constant. Conjugation by the unitary \(u\) returns the bounds to the
> original gauge and preserves the norms. Thus (H6.3), that is the order-two majorant for \(V_0'(A)\) and
> the order-one majorant for \(V_0''(A)u\) from \(E_p\) to \(F_p\), holds at \(W\) with constants depending
> only on \(N,L\).

*\(\Theta_J\) and the legs (789–822).* \(\langle A,\Theta_JA\rangle=2\langle C^{(2)}(\ell A),H^{J,T}J\rangle\)
and b98p5.md (4) with \(\alpha=-4\) give \(\Theta_J:E\to F\). I checked each leg of the table by duality
(fine pairing between \(E\) and \(F\), top pairing between \(B\) and block \(-4\)). Correct.

*Scalar majorant (824–870).* For \(0\le t\le8r\), \(0\le x\le8Ct^2\):
\(t+Hx\le t(1+64HCr)\le2t\le16r<s/2\), so \(a(t+Hx)\le4Ct^2/(1-16r/s)\le8Ct^2\), and the
\(x\)-derivative is \(\le Ha'(16r)\le1/4\). Monotone iteration from zero gives nonnegative coefficients,
determined degree by degree because \(a\) starts at degree two. Correct.

*(P16)–(P17).* I matched the seven terms of (P16) against layer-pkg.md (1.5) in order. Each majorant
is correct and starts at degree two. \(v'(t)\le Ct\) on \([0,2r_{\kappa_1}]\) gives (P17). The radius
depends on \(\kappa_1\) through \(H,C\); the current ceiling does not. Correct.

## 8. The current-corrected source inverse (lines 913–959) — ADVANCE

CA-I 15282–15290 lists \(\tilde G^J\) as a primitive whose defining series is expanded into concatenated
walks and not re-summed. So one tag per concatenation is the account's rule, and (P15) applies once to
each term of \(\sum_nB_0(\Theta_JB_0)^n\). With the weighted majorants of the §5 repair,
\(g^*_\Delta\le b^*_\Delta/(1-b^*\theta^*)\le\tfrac43b^*_\Delta\), and
\(G(\sigma):F_p\to E^\Delta_p\) has majorant \(e^{16\kappa_1}g^*_\Delta\). The second line of (T2) composes
the composite \(\Theta_J(\sigma)\), with a fixed number of primitive tags. The third composes (P17); \(G\)
does not depend on \(A\). Tails and holomorphy follow from absolute convergence. The zero-switch
separation is CA-I 15330–15331 (iii), proved as in PI (e). Correct.

## Necessary test (lines 961–977) — ADVANCE

\(V'(0)=DV'(0)=0\) since every term of (1.5) has degree at least two (checked in §7), and
\(C(0)=DC(0)=0\). Differentiating (S5) gives \(D_bA'=\Gamma H_0+H_0=TH_0\) as a composite, with no
switched inverse identity. With \(\|u\|_p\le\|u\|^\Delta_p\):
\(\|Tj\|^\Delta_p\le(1+\gamma_\Delta)\|j\|^\Delta_p\) and
\(\|TH_0b\|^\Delta_p\le(h_\Delta+\gamma_\Delta h_0)|b|_p\), with \(\gamma_\Delta=C_{\kappa_1}|J|_{-3}\) and
\(h_\Delta=C_{\kappa_1}\) from (T2). This passes layer-pkg.md (4.11) uniformly at switches.

The use table (994–1029) only states where the conditional supply **G** applies. It discharges no full
N[U]. I did not check it use by use; that is outside row 447.

## Constant order — ADVANCE (non-circular)

Each constant is fixed after everything it depends on. No row depends on a later row.

| Step | Constant | Depends on | Source |
|---|---|---|---|
| 0 | \(N,L,\beta_0\); \(\epsilon=(1-\beta_0)/2\); \(b_0=8\) | given | theorem, §6 |
| 1 | flat tile \(M_F\) with \(q<1/2\); \(D\), \(B_L\); flat rate \(a=\log(1/q)/D\), \(a'=a/2\) | 0 | flat-port §11; walks §2 |
| 2 | flat gap \(\rho_F\ge\max\{\)flat-port floors, \(2(8+b_0)\log L/a'\}\); flat torus room \(t_FM_F\) | 1 | flat-port §§8.2, 12; walks (P5), (T1) |
| 3 | \(B_Z\) (all finite source/output pairs of §§2, 6) | 1, 2 | walks (P8), §6 |
| 4 | \(C_Z\) (P9), norm-comparison constants, \(c_Z\), \(C_{\rm com}\) (P11); PI's \(r_1,e_R,C_R,e_C,C_C,C_S\) | 0 | PI §3.3 item 2; walks §§3–4 |
| 5 | enlarge \(B_F\ge B_Z\), \(c_h\ge c_Z\), \(C_{88}\ge C_{\rm com}\), \(C_C\ge C_Z\) | 3, 4 | walks line 452 |
| 6 | \(M_t\): power of \(L\), multiple of \(LM_F\), \(\ge\max\{2\rho'_F,4L\}\), PI \(\theta\le(4D_*)^{-4}\) (so \(\theta_Z\le(4D_*)^{-4}\)) | 2, 5 | PI item 3; walks (P12) |
| 7 | \(r_N,\widehat r,D_X\); \(\delta_q\); \(\mu=\log(1/\theta_Z)/(140D_X)\); \(N_t\) | 6 | PI items 4–5; walks (P14) |
| 8 | insertion range \(c_\iota\) and costs \(e^{17\mu c_\iota}\); weighted majorants \(b^*,b^*_\Delta,g^*,h^*\) | 6, 7 | §5 repair |
| 9 | radii \(a_0^*,a_1^*\le a_*\): PI item 7 with enlarged constants; \(e\le c/(M_tC_Zc_Z)\); \(B_ZC_Ze\le1/8\); \(a_*\le\rho/(16C_{N,L})\) (b98p5 (2), (11)); increment ball | 4–6 | PI items 7–8; walks §§3, 4, 7 |
| 10 | \(C_1,C_2,C_3\) (with the §5 weights); \(j_*\) with \(C_1j_*,C_2j_*\le1/4\), \(b^*\theta^*\le1/4\) | 3, 7–9 | walks §§6–7 |
| 11 | \(\delta_*\le\mu\) and below every composite rate used | 7, 8 | walks §8 |
| 12 | tower floors: \(M_b\), \(R_1M_b\ge\max\{\)PI item 6, \(2(8+b_0)\log L/\delta'\}\) at every rate \(\delta'\) used; torus side (T1) | 6, 7, 11 | PI item 6; walks (P5), (T1) |
| 13 | given \(\kappa_1\): \(M_{\rm dec}\ge\max\{4\widehat r+8L,\ c_\iota,\ 64\kappa_1/\mu\}\) with grid divisibility | 6–8 | walks P15; §5 repair |
| 14 | \(H,C,s\) of the scalar majorant (contain \(e^{16\kappa_1}\) tag factors); \(r_{\kappa_1}\); \(C_{\kappa_1}\) | 9–13 | walks §7 |

Checks of the order.

- \(B_Z\) (row 3) does not depend on \(M_t\) or on the tower gap. The (P5) constant is uniform above its floor.
- \(C_{\rm com}\) and \(c_Z\) (row 4) are valid under \(m\le L\ell_\tau\). That condition is imposed at row 12
  (PI floor \(R_1M_b\ge4L(\widehat r+L)+1\)). The constants' values do not depend on it, so this is not circular.
- \(\mu\) (row 7) precedes \(j_*\) (row 10) and \(\kappa_1\) (row 13). \(j_*\) does not depend on \(\kappa_1\),
  as CA-I 15408–15412 requires.
- Smallness in \(r\) (row 14) depends on \(\kappa_1\); smallness of the current does not. This matches the theorem.
- Optional simplification: since row 5 gives PI \(\theta\ge\theta_Z\), (P13) also holds with PI's \(\theta\).
  One may put \(\theta_Z:=\theta\); then \(\mu=\delta_q/20\) and line 592's "common smaller rate" is \(\mu\) itself.

First failing step: §5, lines 574–576 and the second inequality of (P15) (the concatenated tree does not yet pass through the cubes met by local insertion carriers, which walks-gw.md counts). Repairable; repair written above.

## Overall verdict

**REVISE.** No step is false. No BLOCK. With the two repairs below, the theorem holds as stated on the
common constant choice, and it passes the necessary test (4.11).

1. §5 (lines 574–598): build the concatenated tree through the cubes met by insertion carriers, giving
   \(t_\varpi\le\sum t_{\omega_i}+17c_\iota n_\iota\); add \(c_\iota\) to the cube floor; define the
   majorants with the spare weights \(e^{\mu t_\omega}\) and \(e^{17\mu c_\iota}\).
2. §7 (lines 769–787): supply the complex-background step for the Wilson vertex (transport norms
   \(\le e^4\), \(|W_p-1|\le C\eta^2e/m^2\), polynomial identities unchanged, unitary gauge return).

Small wording fix (no change of content): §7 line 743, "based at one of its interior endpoints" becomes
"the (S1-loc) box \(N_\tau\) of a tile of height \(j-1\) or \(j\) whose cutoff support contains the row's base point".

Checked line by line by Claude (Opus 5.5).
