Provenance: Codex (gpt-6-astra), xhigh, FINISH row 379, checkout `242d44119c604042a21e4188bc1e176cd45073f7`. One line-by-line research check of the two Claude texts; not an audit, human review, or grant of scientific status.

# B98-I: iterate and level-zero cube check

**Result: Lemma I0 ADVANCE. Lemma I REVISE at the logarithm-chart and constant choices; its estimates ADVANCE with repair 1 below. Lemma C0 REVISE at the change of matrix norm; its conclusion ADVANCE with repair 2 below. No BLOCK.** The repairs preserve the stated consumers. They do not prove further Balaban imports.

Credit: Tadeusz Balaban supplies the averaging operations and cube-gauge statements. The outline and complete account are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Claude wrote `library/b98-iterate.md` and `gates/b98-gate.md`; the previously checked one-step inputs are Codex's `library/b98.md`, Lemmas 1–5. Those inputs are used, not checked again here.

`library/prior/b98i-gate.md` is absent. The registry assigns the underlying B98-SIGNED and B98-CUBE statements to `b98`; row 379 assigns this remaining check. No separate completed or competing check was found. The index marks CA-II `8.11:lem-signed-averaging` **cited**, not proved for the iterate. This check does not reopen the separate B98-P2, B98-P6 or B98-EXTRA rows.

## 1. Line-by-line decisions

Line numbers below refer to `library/b98-iterate.md` at the pinned checkout. C0 is its line 106 and finding 2, line 35, of `gates/b98-gate.md`.

| Step | Decision | Checked conclusion |
|---|---|---|
| L9, scope of the repair | ADVANCE | CA-I 858–860 defines composition. CA-II 123074 and 123215–123220 use that composition. One step of side \(L^k\) would not suffice. |
| L13–19, blocks and \(Q\) | ADVANCE | Balanced offsets partition the parent block. Both contour conventions give a direction-independent connector, with the stated length and translation properties. |
| L23–37, I0 and reversed bonds | ADVANCE | The negative-bond formula follows by reversing both endpoints and the straight path with the same offset. |
| L39–50, I0 induction | ADVANCE | Interior connectors cancel at each fixed offset. The two endpoint terms concatenate into paths from \(y\) to \(y+L^jo''\). The offset bijection, convex weights, and length bound are correct. |
| L31 and L52, I0.a | ADVANCE | The bound is \((d+1)L^m\|e\|_\infty\), not \((d+1)^mL^m\|e\|_\infty\). At exponent zero in Step 3 use \(Q^0=I\), which satisfies the looser bound with factor \(d+1\). |
| L32–35 and L52, I0.b | ADVANCE | The four endpoint connectors cancel. Interior fine edges then cancel with their signs. This is an additive matrix identity. |
| L56 and L67, domain of the iterate | ADVANCE | The four blocks form the stated rectangular set of sites. The recursive connectors stay in their parent blocks; straight segments stay in the corresponding double block. Every required fine bond and plaquette stays in \(\Delta(P)\). |
| L69, axial bound and covariance | REVISE | The bond bound, locality, gauge-invariance of \(\mathcal S_c\), and plaquette-norm equality hold. The inference from distance \(\le1/2\) to a **traceless** logarithm needs the group-chart condition from the cited lemma. Repair 1 supplies it. |
| L71, one-step remainder and branch | ADVANCE with repair 1 | The logarithm remainder is quadratic with a dimensional constant. CA-I 819 uses normalized Hilbert–Schmidt norm, which is indeed at most operator norm. The strict plaquette test selects branch (a) before using its formula. |
| L73–90, induction | ADVANCE | The exact linear expansion and geometric sum give \(K L^{2m}(\tau/n)^2\). The factor is \(L/(L-1)\le3/2\). The absorption \(K\tau\le1\) proves both bounds in \(H_m\), uniformly in \(k\). |
| L92, plaquette and fine-flux replacement | ADVANCE | The three errors are \(16(d+2)^2\tau^2\), \(4K\tau^2\), and \(80\tau^2\). The last uses total weight \(n^2\), not \(n^{d+2}\) after normalization. The displayed \(C_I\) is valid. |
| L94–98, clauses 3–4 | ADVANCE | The gauge-difference identity, path length \(\le2dn\), and adjoint estimate give \(32d^2\alpha^2\). No constancy of the change of gauge is assumed. |
| L65 and L100, constants and application | REVISE | Replace “largest” under a strict inequality by a positive choice with slack. Retain a common threshold with the unsigned estimate. Repair 1 gives the choices. |
| L106, level and collar hypotheses | ADVANCE | At \(k=0\), \(\eta=\xi_0=1\), \(\square_0=\square+r\). Reg\(_0\) on \(\square^a+4r\) supplies the **level-zero** plaquette bound. No \(\Omega_{-1}\) or level \(-1\) estimate is used. |
| L106, axial potential bound | REVISE | The displayed operator-norm estimate alone does not yield the following bound in Balaban's norm \(|\cdot|\). Carry the axial telescoping and logarithm estimate in that same norm; see repair 2. Retain the inherited group-chart ceiling in \(c_1\). |
| L106, direct differences and stencil fit | ADVANCE | On the written \(Q=\square+3r\), even the conservative reach \(2\le2r\) fits. The requested smaller \(\square+2r\) also works, by the explicit stencil check in repair 2. |
| L106, gauge composition and \(B_1\) | ADVANCE | \(u^{-1}=av^{-1}\) has the correct order. The already permitted choice \(B_1>C_*\) can include \(B_1>8d\); it gives strict (C5). The seed-cube consumer uses only the potential and first differences. |

## 2. Repair 1: charts and constants for Lemma I

The first unsupported inference is L69's claim that a small operator-norm distance alone makes the principal logarithm traceless. For example, in \(SU(16)\),
\[
 Z=e^{2\pi i/16}I,\qquad
 \|Z-I\|=2\sin(\pi/16)<\tfrac12,\qquad
 \operatorname{Tr}\log Z=2\pi i.
\]
This refutes that intermediate inference, **not** Lemma I under a suitably chosen smallness threshold. `b98.md` Lemma 3 explicitly requires the fixed group logarithm chart. CA-I 42743–42748 also distinguishes the matrix logarithm estimate from its group-chart condition.

Here is a concrete replacement for the constants paragraph. Retain the dimensional \(C_4,t_*,K,C_I\). Choose
\[
 c_I=\frac12\min\left\{
 \frac1{4(d-1)},\quad
 \frac{t_*}{4d(d+2)},\quad
 \frac{\omega_M(L)}{32d(d+2)},\quad
 \frac1{4dK},\quad
 \frac1{64d(d+2)},\quad
 \frac1{16d(d+2)N}
 \right\}.
\tag{R1}
\]
All of (S) and the two other printed smallness conditions hold, including the strict inequality. The fine axial links lie in the group chart. Indeed, for \(W\in SU(N)\) with \(\|W-I\|\le1/(4N)\), (2) gives \(\|\log W\|\le1/(2N)\). Its trace is in \(2\pi i\mathbb Z\) and has modulus at most \(1/2\), so it is zero. This verifies the needed chart directly.

Use the same check at each stage. The principal logarithm exists by Step 2's small matrix ball. The bounds proved in \(H_m\) give
\[
 \|a^{(m)}\|\le(d+2)\tau\le\frac1{8N},
\]
so its trace is zero. There is no circular assumption here: the norm estimate uses the matrix logarithm; tracelessness follows afterwards. In the one-step expansions, scale the already traceless input by \(t\in[0,1]\). The small-field test and the Taylor bounds hold along that path. Every small relative logarithm stays on its identity branch, so the matrix-series logarithm agrees with the intrinsic logarithm in Definition 1.5(a). The mean is the local branch specified there. Neither \(C_4\) nor \(C_I\) acquires an \(N\)- or depth-dependent factor.

For the application, denote the previously permissible unsigned constants by \(c_{2,u}\) and \(C_u\). Use
\[
 c_2=\min\{c_{2,u},c_I,[2(C_I+1)]^{-1}\},\qquad
 C_0''\ge\max\{C_u,C_I+32d^2\}.
\tag{R2}
\]
Choose dependent constants after these choices. This preserves CMP 98 Proposition 2 as quoted: its (52)–(54) concern the iterate, with local fine support in the four iterated blocks. Its unsigned conclusion is not itself a proof of signed (B3).

The same signed expansion also permits a shared unsigned error constant for the symmetric map. From (2), \(\|\Phi(p)\|\le f+f^2\), so
\[
 \|\mathsf A_P^{\rm loc}\|\le\alpha+\alpha^2/n^2,
 \qquad
 \|(M^kU)(\partial P)-I\|\le\alpha+(C_I+1)\alpha^2.
\]
Thus (R2) dominates both errors and gives the unsigned \(<2\alpha\) conclusion for \(\alpha>0\). At \(\alpha=0\) the coarse plaquette is the identity.

**Consumer check: ADVANCE with (R1)–(R2).** Set \(k=k_o\), \(n=L^{k_o}=\eta^{-1}\), and \(f=\varepsilon_a\eta^2\). Clause 4 covers the local axial gauge used at CA-II 123180–123190, whose links satisfy \(\|U_b^{\rm loc}-I\|\le2dnf\). It gives exactly the bound used at 123215–123220. The subsequent comparison with the complete axial gauge retains its \((1+\mathsf L\eta)\varepsilon_a^2\) error. No bound for a single averaged link in an arbitrary gauge is required. If depth zero is admitted, the separate \(M^0=I,n=1\) case follows directly from \(\|\log V\|\le\|V-I\|+\|V-I\|^2\).

## 3. Repair 2: C0 on the box enlarged by \(2r\)

The checked text uses \(\square+3r\), not \(\square+2r\). Its larger box is available from the consumer and is not a defect. The following replacement uses the smaller box requested here and makes the norm and stencil arguments explicit.

Put
\[
 Q_2=\square+2r,\qquad \square_0=\square+r,
 \qquad s=7dL^2M^*\alpha_0,\qquad r=R_1M_1\ge1.
\]
The side of \(Q_2\) is \(M^*+4r\le5M^*\). It contains \(\widetilde\square\), whether at depth zero the smallest grid cover is \(\square_0\) or the larger enclosing cube is retained. Reg\(_0[\square^a+4r;\alpha_0]\) supplies
\[
 |U_0(\partial p)-I|<\alpha_0\quad(p\subset Q_2).
\]
This is the actual level-zero hypothesis. It is stronger domain information than regularity only on the minimal enclosing cube, and it is supplied by the seed-cube consumer (CA-I 36382–36410). The current bound is not needed for this finite-mesh argument.

Use the axial gauge \(a\) of the already checked Lemma 3 on \(Q_2\), carrying its unitary telescoping in Balaban's norm \(|\cdot|\), throughout:
\[
 |U_0^a(b)-I|\le5(d-1)M^*\alpha_0\le s/9.
\tag{R3}
\]
CA-I 35057–35060 specifies a unitarily invariant norm dominating operator norm. Unitary telescoping works in this norm, and
\( |Z^m|\le\|Z\|_{\rm op}^{m-1}|Z| \)
gives the logarithm-series estimate in the same norm. Retain the fixed group-chart ceiling already required in `b98.md` Lemma 12; \(s\le1/6\) alone is not a substitute for it. Then
\[
 U_0^a=e^{iA_0},\qquad
 |A_0|\le\tfrac65|U_0^a-I|
 \le6(d-1)M^*\alpha_0<s
 \quad\text{on }Q_2.
\tag{R4}
\]
For explicit bookkeeping at fixed \(G=SU(N)\), one may decrease the inherited \(c_1\) to also satisfy \(c_1\le\min\{1/6,9/(4N)\}\). Equations (R3) and the trace argument in repair 1 then verify the chart. This is a fixed-group statement; it asserts no new uniformity as \(N\) varies.

**Stencil fit.** Write \(\partial_\nu^+A(x)=A(x+e_\nu)-A(x)\) and \(\partial_\nu^-A(x)=A(x)-A(x-e_\nu)\). For a tested bond \(b=(x,x+e_\mu)\subset\square_0\), the operators have the forms
\[
 (\Delta A)_\mu(x)=\sum_\nu\partial_\nu^-\partial_\nu^+A_\mu(x),
 \qquad
 (\partial^*\partial A)_\mu(x)
 =-\Delta A_\mu(x)+\sum_\nu\partial_\mu^+\partial_\nu^-A_\nu(x).
\tag{R5}
\]
The first expression reads the parallel bonds at \(x,x\pm e_\nu\). The second adds \(\nu\)-bonds based at
\(x,x-e_\nu,x+e_\mu,x+e_\mu-e_\nu\).
Every endpoint is within sup-distance one of an endpoint of \(b\). The first-gradient stencil has the same property. Thus all reads lie in
\[
 \square_0+1\subset\square+2r=Q_2,
\]
including \(r=1\). Two differences do not require two units of outward sup-distance here. Keep \(A_0\) on \(Q_2\) while evaluating these stencils. The direct bounds are precisely
\[
 |\nabla A_0|\le2s,\qquad |\Delta A_0|\le4ds,
 \qquad |\partial^*\partial A_0|\le8ds
 \quad\text{on }\square_0.
\]

Finally, on \(\widetilde\square\), write \(U_0'=U_0^v\) and set \(u^{-1}=av^{-1}\). Then
\[
 (U_0')^{u^{-1}}=U_0^a=e^{iA_0}.
\]
This is (C4), with \(\lambda=0\). At \(j=0\) all powers of \(\xi_0\) equal one. The potential bound and the three difference bounds are strictly below \(B_1s\) once \(B_1>8d\), as already permitted by \(B_1>C_*\). These give (C5). Restriction to the seed cube and its internal adjacent bond pairs gives exactly CA-I 35299–35312 and 36483–36504. No undefined \(\Omega_{-1}\) enters the proof.

## 4. Sources and limits of this check

The outline and CA-I were fetched once at `31a47c543775`; CA-II was fetched once at the same revision. The outline index README, the relevant chunk-07 rows and obligations, the CA-full rows, and the CA 4.12–4.19 index located the source passages. The decisive bounded reads were:

- Outline 7043–7074: prescribed mean, contours, and meaning of iteration.
- CA-I 788–860: Definition 1.5 and its norm; 35049–35083, 35201–35276, 35281–35312: cube conventions and target; 36261–36310, 36382–36504: level-zero regularity and consumer; 42724–42764, 43787–43865: logarithm-chart distinction and axial bond bound.
- CA-II 122046–122104, 122354–122370: gauge and units; 122938–123007: signed statement and its cited argument; 123070–123242: complete weighted-flux consumer.
- Local Balaban text: `cmp98.txt` 382–548, including journal p. 26, Proposition 2 and its local four-block support; `cmp109.txt` 190–206 and 248–280, the actual symmetric mean; `cmp99a.txt` 127–150 and 1276–1330, level bounds, admission of \(k=0\), and \(U_0'\) as a gauge transform. The quoted CMP 98 Proposition 2 was checked in this local text, not against a newly obtained PDF.

Source identities (SHA-256):

| Source | Hash |
|---|---|
| `library/b98-iterate.md` | `992fdfadf642bc6eea151ec5d2cac2e54cca28c3dce9d44e805889e684234f79` |
| `gates/b98-gate.md` | `3c9604491631fa4f63375cb98a70b782f2c494ce47f7ce9f0fad7b9e7ece16d0` |
| Outline | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| CA-I | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| CA-II | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |

All mathematical checks above are written arguments. Downloads, searches and hashes supplied source text and bookkeeping only. Only `gates/b98i-gate.md` was written. The other source files, registry and scientific status are unchanged. The result covers the iterated (B3) and the level-zero seed-cube use, with the written repairs; it does not assert the extra normalized gauge clauses or a full proof of the surrounding Yang–Mills chain.

Checked line by line by Codex (gpt-6-astra).
