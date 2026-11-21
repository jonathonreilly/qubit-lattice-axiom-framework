# STAGE: rebuilding the quoted stage theorem

Provenance: Codex, 2026-11-05, checkout `3c3984cf29705bbb02167f552c1a28a837a670a0`; research text, not an audit; grants no status. Hand arguments only. This is not yet checked by another model.

Source credit: Tadeusz Balaban for the stage theorem in CMP 122a, (1.60)–(1.70). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the quotation, definitions and organization in their complete account, commit `31a47c543775`. CMP 122a is unavailable locally; this note rebuilds only what their account specifies.

## Scope and source trail

The target is H-STAGE in `port/p10-stability.md`, as assumed at CA-I 54989–54998. The comparison uses frozen `st1-r4.md`, `dom.md`, `geoh.md`, and `pda.md`. The account's drop-out application condition is separate (CA-I 49495–49546).

CA-I and SA denote the two files at upstream commit `31a47c543775`:
[complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex)
and [outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
Each was fetched once to the requested `/tmp` path. Line references below are to those files, not rendered pages.

The outline index README, neighbouring chunk-05 rows for R19–R25,
chunk-13 rows for UM1–UM6, and the corresponding obligations were read first.
The CA 4.12–4.19 index, especially chunks 06 and 10, located the stage import
and its uses. The literature record reused is `lit-balaban.md`, §3's
R-operation row. No independent copy of CMP 122a is used.
The pinned repository workflow was read through `git show`, since `docs/`
is absent from this sparse working tree. Only this research file is edited.

## 1. The exact import, and what its quotation does not specify

Here is the mathematical content of CA-I 54989–54998, retaining its two
separate hypotheses. This is a restatement, not a new theorem.

**H-STAGE.** Fix step \(k\). Balaban's inductive theorem for one stage of
the preparatory integrations, CMP 122a (1.60)–(1.70), is valid for the
profiles in those displays, under that theorem's standing hypotheses.
This imported theorem supplies

\[
 \|\cdot\|,\quad\text{the analyticity spaces},\quad
 c_G,K_L,\mathfrak s,\mathfrak p_j,\mathfrak l_j,q,C_2,
 \kappa_1,\vartheta,K'_S,\quad (a_m)_m,
 \quad (K),(Q^+),\ \gamma\le\gamma_0.                 \tag{S1}
\]

**H-PROFILE-CLASS**, CA-I 54996–54998, is a second hypothesis:
the cited statements and H-STAGE remain valid for every system whose
profiles are admissible at every stage. It is not part of the first bullet.
P10 §2.1 preserves this distinction. The prepared family can fail the
admissible-profile test; its companion satisfies it (CA-I 53925–53955).

**Source limitation.** These ten lines import a theorem by reference;
they do not reproduce (1.60)–(1.70) as a self-contained quantified theorem.
In particular, CA-I 54358–54362 assigns several symbols back to that same
theorem. Its later proof invokes the Gaussian normalization lemma, cluster
proposition and cumulation lemma as parts of the import (55080–55086,
55167–55183). Those are not proofs supplied by ST1.

The table defines every item of (S1) to the extent specified by this
account. An imported predicate remains an imported predicate. Giving it
a convenient new definition would change H-STAGE.

| Item | Definition or precise supplied role in CA-I |
|---|---|
| \(k,n,j,h,N,N_0,k_0\) | \(k\) is the RG step; \(N=k-h\) is the number of preparatory integrations; \(0\le n<N\), \(j=h+n\). \(N_0\) is the least positive integer with \(L^{N_0-1}=R_{k-N_0+1}\), and \(k_0=k-N_0\). The operation requires \(N_0<N\le R_k\) (53755–53773). |
| Geometry | Fine mesh \(\eta=L^{-k}\), level mesh \(u_i=L^{i-k}\); \(\pi_i=\mathcal Q_{Mu_i}\); cells have side \(MR_i u_i\) (53633–53674). \(Z\) is an eligible component; \(Z_i=\Lambda_i^c\). Prepared \(Z''_i\) replace levels in order. The collar is \(R_n=Z_{j+1}\setminus Z''_{j+1}\) inside \(Z\) (53737–53815). This \(R_n\) is a region, distinct from the cell parameter \(R_i\). |
| Profiles | For a member \(A\) made of \(b\)-cubes, \(\mathcal P(A)\) consists of smooth \(0\le\varphi\le1\), zero near \(A\), and one outside \(A\) and its touching \(b\)-cubes. The companion smooths the actual \(b\)-cubes; the prepared profile smooths the containing cells (53894–53955). |
| Pair and current | \(\mathbb U=e^{i\eta A'}U\), \(U\in SU(2)\), with independent complex current \(\mathbb J\). Auxiliary \(U_{p,X}\) is the critical branch for the prescribed averaged data and determining set; \(J_{p,X}\) is its derived current. Neither replaces the independent current. See 9830–9879 and 49593–49618. |
| Analyticity spaces | \(\widetilde U_k^{(n)c}(X;\widetilde\alpha_0,\widetilde\alpha_1)\) are the descending stage spaces of CMP 122a (1.64)–(1.69), with the hereditary reading denoted \(\Sigma\). They impose simple, auxiliary-background, current, potential, derivative and real gauge clauses, with the specified stage territories, weights and radii. The seven entries and weight placement are transcribed at 49593–49642; the unmodified layered clauses are explicit at 9830–9919. These references do not justify replacing the space by ST1's roster. |
| Filing and norm | \(m(X)\) is the least \(m\ge j+1\) with \(X\subset\Omega_{m+1}^c\). \(X\in\mathbb D_m\) is a face-connected union of \(\pi_m\)-cubes, meeting both \(\Omega_m\) and \(R_n\). The norm is (S4) below (54341–54357). The later explicit definition is \(d_m(X)=\tau(X)/(Mu_m)\), where \(\tau(X)\) is the length of a shortest tree contained in \(X\) meeting every closed cube of \(X\) (103055–103077). Its single-cube value is zero (55107–55112). It is not defined as the number of cubes minus one. |
| \(c_G,C_0\) | \(c_G=c_G(d,L,M)\) bounds the Gaussian family; the boundary bound is \(C_0=c_G+1\) (55019–55044). This \(C_0\) is not the coefficient of the running radius also called \(C_0\). |
| \(K_L,\mathfrak s,\mathfrak p_j,\mathfrak l_j,q,C_2\) | Imported parameters of the cluster bound (S6); CA-I 54358–54362 and 55147–55154 give their role, not a self-contained defining formula for this stage package. Later reuse of a symbol, for example \(\mathfrak l_j\) for a window tile count, is not an identification with this slot. In particular the exponent \(q\) in \(M^q\) is not identified here with ST1's running-radius exponent. |
| \(\kappa,\kappa_1,\beta\) | \(\kappa\) is the decay parameter; \(\kappa_1\) the enlarged decoupling parameter, chosen after it (1468–1498). \(\beta\) is the layered schedule fraction (9924–9952); the earlier layered convention sets \(\beta=1/4\) at 9882–9888. Different later schedule conventions are not silently substituted. |
| \(\vartheta,K'_S\) | \(\vartheta\) is the small stage-bound parameter, proportional to \((\log g_k^{-2})^{p_1-q_*}\), not the glossary's separation-window parameter (54908). A later normalization convention specifies \(\vartheta=K_\vartheta(A_1/C_*)(\tfrac12\log g_k^{-2})^{p_1-q_*}\), with positive fixed \(K_\vartheta,C_*\), and \(q_*\ge p_1+1\) (104019–104026, 104100). CA-I 70627–70637 defines \(q_*\) as the earlier lower bound on the radius exponent \(q\). The block-weight convention at 70401–70413 instead uses \(A_0\) and \(p_1-q\); these conventions are not silently equated. \(K'_S\) is the imported interaction constant in (S7) (55039–55044). |
| \(a_m,(F_m)\) | \(a_k=(1+3\beta)\kappa\); for \(j+1\le m<k\), \(a_m=(1+3\beta)\kappa\) if the imported predicate \((F_m)\) holds, and \(a_m=(1-\beta)\kappa\) otherwise (55020–55024, 55194–55204). The passage does not define \((F_m)\). |
| \((K),(Q^+),\gamma_0\) | The imported stage-theorem restrictions. Under them the last inequality of (S6) and the bound in (S7) hold. \(0<\gamma\le\gamma_0\) is a last coupling ceiling. No explicit predicate \((K)\) or \((Q^+)\), or formula for this \(\gamma_0\), is supplied at their occurrences in this stage argument. They remain **U-K**, **U-Q** and **U-ceiling**, rather than predicates invented here. |

Thus the requested fully expanded statement cannot be recovered from this
quotation alone. Its *used conclusions* can be stated exactly. That is the
contract compared below. This source limitation is not the reason for
stopping the proof attempt: §§4–6 attack its mathematical admission content.

For clarity about units, the explicit ordinary layered definition at
CA-I 9830–9879 can be written as follows. Put \(\lambda_m=L^m\xi\), where
\(\xi\) is the fine spacing in that definition, and normalize the seven
entries in their quoted order by
\[
\begin{split}
 Q_1&=\lambda_m^2\xi^{-2}|\partial\mathbb U-I|,&
 Q_2&=L^{2p}(L^{m-p})^2|\partial U_{p,X}-I|,\\
 Q_3&=\lambda_m^3|\mathbb J|,&
 Q_4&=L^{\min(p,m)-m}(L^{m-p})^3|J_{p,X}|,\\
 Q_5&=\lambda_m^2\xi^{-2}|\partial U-I|,&
 Q_6&=\lambda_m|A'|,\quad Q_7=\lambda_m^2|\nabla_U^\xi A'|.
\end{split}                                                        \tag{S0}
\]
At a step of depth \(b\), entries 1–5 are less than
\([1-\beta(1-2^{-(b-m)})]\alpha_{0,m}\); entries 6–7 use
\(\alpha_{1,m}\). The territory is \(X\cap(\Omega_m\setminus\Omega_{m+1})\)
for \(m<b\), and \(X\cap\Omega_b\) at the top. Here
\(U_{p,X}=U(\mathbf B_p(X)\cup\{\Gamma_i\}_{i<p},M^\cdot(\mathbb U))\)
and \(J_{p,X}\) is its prescribed background current. These determining
sets, averaging maps and branches are the account's actual ones; an
alternative erosion rule is not their definition.

The real gauge condition is separate. On each prescribed cube of side
\(CM\lambda_m\), respectively \(CM\) at the top, a real gauge on its
intersection with \(X\) gives
\(\lambda_m|A|,\lambda_m^2|\nabla^\xi A|<BCM\alpha_{0,m}\); there is
no schedule factor. The intermediate cubes lie in
\(\Omega_m\setminus\Omega_{m+2}\) and meet \(\Omega_{m+1}^c\).
The source admits \(C=1\) as well as \(C=2\), and does not restrict this
condition to partition-aligned cubes (9907–9919).

For the preparatory spaces the account specifies the following changes
at 49593–49637. The first row's numerical coefficient is (S12) below;
the second is described there as the analogous coefficient.

| CMP 122a clause | Territory | Radius index | Factor on **all seven** entries |
|---|---|---|---|
| (1.64) | \((\Omega''_m\setminus\Omega''_{m+1})\cap X\), \(1\le m<j\); at \(m=j\), \((\Omega''_j\setminus\Omega_{k_0+1})\cap X\) | \(m\) | \(\mathsf L_0^{2\max(0,m-k_0)}\) |
| (1.66) | \((\Omega_m\setminus\Omega_{m+1})\cap X\), \(k_0+1\le m\le j\) | \(j\) | \(\mathsf L_0^{2(j-m)}\) |
| (1.68) | \((\Omega_m\setminus\Omega_{m+1})\cap X\), \(j<m<k\); top \(\Omega_k\cap X\) | \(m\) | (1) |

The paired real gauge clauses are (1.65), (1.67), (1.69); CA-I
49495–49547 explains their application-side supply. This transcription
does not fill in an omitted CMP 122a clause or silently impose the
different ST1 full-core roster. The source's explicit reference back
to Balaban, including the undefined predicates in (S1), remains part
of the specification boundary.

## 2. The stage contract actually consumed by A10

Use \(A(w,\mathbb U)=\sum_p w(x_-(p))\mathcal A_p(\mathbb U)\), with
Balaban's Wilson plaquette function. Set

\[
 A^{(n)}=-A(x^{(n)},\cdot)+\mathfrak E^{(n)},\qquad
 W^{(n)}=A(x^{(n)}-g_j^{-2},\cdot),\qquad
 \mathcal R^{(n)}=A^{(n)}+g_j^{-2}A.
\]

The prescribed response reconstructs the old background from the new
background and collar variables \(A_j,B_j\). Denote it by \(\mathbb U^{\rm sh}\).
The interaction is
\(\mathfrak K^{(n)}=\mathcal R^{(n)}(\mathbb U^{\rm sh})-
\mathcal R^{(n)}(U_k^{(n+1)},A_j=0)\).
The fluctuation integral is exactly

\[
 I_{n+1}=\int dA_j\,\chi^{(j)}e^{-\langle A_j,C^*\Delta^{(j)}_{\Lambda_{j+1}}CA_j\rangle/2}
 z^{(j)}\int dB_j\,\chi'^{(j)}
 e^{-\langle B_j,C^*\Delta^{(j)}CB_j\rangle/2+
 \mathbb P^{(j)}+\mathfrak K^{(n)}}.                    \tag{S2}
\]

The outer factor \(\chi_k^{(n+1)}\) and \(E_0^{(j)}\) in CA-I
54290–54300 are outside this integral. Here \(C\) is the prescribed
constraint-coordinate map, \(\Delta^{(j)}\) the stage quadratic form,
\(\mathbb P^{(j)}\) its higher Wilson remainder, and \(z^{(j)}\) its
normalization. These are the actual operators, cutoffs and factors of that
display, not any Gaussian having the same covariance at zero.
The account cites their construction to CMP 122a at 54241–54257.

With the branch of the logarithm supplied by the expansion,

\[
 C_{n+1}:=\mathbb C_k^{(n+1)}=\log I_{n+1}+\Delta W_{n+1},\quad
 \Delta W_{n+1}=A(x^{(n+1)}-x^{(n)},U_k^{(n+1)}),\quad
 \mathbb B_k^{(n)}=\sum_{i=1}^n C_i.                  \tag{S3}
\]

CA-I 54314–54339 defines this recursion. It does not by itself prove
that \(I_{n+1}\) has a single-valued holomorphic logarithm.
For the filing described in §1,

\[
 \|C\|=\sup_m\sup_{\square\in\pi_m}
 \sum_{X\ni\square,\ m(X)=m}\|C(X)\|_\infty e^{a_m d_m(X)}.       \tag{S4}
\]

The supremum inside each summand is over the whole prescribed local
complex space \(\widetilde U_k^{(n+1)c,\Sigma}(X)\), with its allowed
exterior fields. The imported stage theorem gives local holomorphic
families \(C_G,C_L\) for \(\log I_{n+1}\); adding the filed cube terms
of \(\Delta W_{n+1}\) gives \(C_{n+1}\). A10 consumes all of:

\[
 \begin{gathered}
 C_{n+1}=\sum_X C_{n+1}(X),\qquad \|C_{n+1}\|\le C_0,\qquad
 |C_{n+1}(X;P)|\le C_0e^{-a_{m(X)}d_{m(X)}(X)},\
 \sup_x\sum_{i\le n+1}\sum_{X\ni x}\|C_i(X)\|_\infty
       \le3(N_0+3)C_0.                                  \tag{S5}
 \end{gathered}
\]

Each term reads the pair and exterior fields only in its indicated domain.
Its explicit norm calculation is

\[
 \|C_{n+1}\|\le c_G+
 K_L(\mathfrak s+\mathfrak p_j+\mathfrak l_j)M^q
 e^{C_2\kappa_1+4\sqrt d(2+4\beta)\kappa}+\vartheta
 \le c_G+1.                                             \tag{S6}
\]

The more precise split \(C_{n+1}=C_G+C_I\) satisfies

\[
 \|C_G\|\le c_G,\quad
 \|C_G-C_G|_{(1,0)}\|\le\vartheta,\quad
 \|C_I\|\le K'_S(N_0+8)C_0\vartheta\le1.                \tag{S7}
\]

Here ((1,0)) is the trivial field and zero independent current, with
the other parameters retained as prescribed. Sources for (S5)–(S7):
55013–55044, 55140–55183. Profile transfer of these conclusions is the
proved implication in P10; it is not a proof of their companion-system input.

## 3. Line-by-line comparison with the frozen package

“Weaker” below refers to the relevant conclusion, with all its premises.
No row asserts a logical independence theorem for the actual Yang–Mills construction.

| CA-I line / required content | Frozen result and exact difference |
|---|---|
| 54989–54991: one inductive integration stage, for the printed profiles | **Different formulation.** ST1 Theorem 14 is hereditary substitution of an already bounded activity and a finite Boolean re-expansion. It does not construct (S2)'s logarithm or reproduce an integration-stage class. |
| 54991: standing hypotheses | **Conditional in both.** ST1 explicitly retains GEO, background/response theorems, independent-current bounds, CH, actual membership, CI and stage matching. Naming them is not verification of Balaban's standing hypotheses. |
| 54992: weighted norm | **Weaker.** ST1 (77) bounds one excess by \(2b_f\rho_X^{-1}(e^{\bar\kappa}-1)^{-\lvert Y\setminus X^\uparrow\rvert}\). It contains the supplied amplitude \(b_f\). It proves neither (S4)'s bound on the integrated logarithm nor its stage sum (S5). |
| 54992–54993: analytic spaces | **Different, no proved inclusion.** ST1 uses chart-free intrinsic towers, R1 cores, unit analytic lifts and permanently frozen records. CA uses stage weights \(\mathsf L_0^{2e}\), its own auxiliary determining systems and gauge cubes. DOM Theorem 8 still assumes its input is in the proposed roster. |
| 54993–54994: Gaussian, interaction and other constants | **Not supplied.** ST1's radius coefficients and response constants are not the constants of (S6)–(S7). CI assumes old activity bounds; it is not the missing Gaussian/cluster theorem. |
| 54994: decay rates \(a_m\) | **Different.** Switch decay in an added-cell count is not yet the filed tree norm. ST1 gives no \((F_m)\) decision or the two quoted rates. |
| 54994–54995: \((K),(Q^+),\gamma\le\gamma_0\) | **Different restrictions.** ST1's final coupling ceilings prove T1–T3 and source budgets. They cannot stand in for the unstated imported predicates or establish (S6) by renaming constants. |
| 54996–54998: all admissible profiles | **Not supplied.** Neither ST1 nor the geometric files prove this profile-class extension. The profile-transfer identity is available conditionally in P10. |
| 55080–55086: Gaussian normalization and cluster representation | **Not supplied.** ST1's finite identity is before integration. Theorem FM concerns a specified real Haar/delta integrand; the actual CA density still needs FM-match and SLOT-CA. |
| 55167–55183: stage cumulation and split | **Not supplied.** Single-activity substitution gives no cumulative supremum or Gaussian oscillation bound. |

The relevant positive contributions are precise:

* **ST1** Lemmas 5, 8, 9′ and 11 give intrinsic continuation and stable
  substitution on admitted domains. Theorem 14, hypotheses 2 and 4
  (`st1-r4.md:1542,1544`), retains complex input membership and CI.
  A real-background formation proof does not eliminate either premise.
* **DOM** Theorems 3, 7 and 8 prove conditional operator-domain and
  substitution inclusions. Its lines 221–224 explicitly retain the map
  \(P_+(\mathcal E)\subset\mathcal D^\flat_{a|+}\). Its proposed roster
  requires all full carriers and every consumer core level (lines 25–35).
* **PDA** proves the actual prepared geometric (A1) condition and stopped
  prefixes. Its §5 expressly excludes gauge, current and analytic membership.
  (A2) remains separate. This supplies geometry, not field admission.
* **GEOH** supplies the stated history geometry under its explicit class
  conventions. Lemmas 9–10 identify intrinsic removed/free rows. Amendment
  GS replaces GEO-slot by SLOT-ST and, for CA, SLOT-CA. Under the incident
  convention the literal collar identification fails at the outer interface
  (`geoh.md`, (11)); a rim reassignment must carry its original integrand.
* **Amendment CV** controls the mean-contour representative. It changes the
  passing-test design; it does not identify the old and new passing branches
  (`st1-r4.md:41`, 1129–1191). FC-mean-match, FC-test and the FC2 analytic
  majorant remain additional hypotheses for the actual complex contour.

The drop-out extension is separate from H-STAGE throughout. CA-I
49495–49547 requires a supplied real gauge family and later drop-out spaces
outside the operator theorem's implication. Neither (S5) nor the frozen
geometric prefix result fills this analytic application condition.

## 4. What the radius estimates actually close

### 4.1 The order of choice is part of the problem

Use the account's order (CA-I 1468–1649): structural exponents and \(L\);
\(\kappa\); then \(\kappa_1\); then \(M_1\), its enlargements and the
background/kernel constants; then the fixed kernel rates and widths;
then \(M\); then test amplitudes and running-radius coefficients;
finally \(\gamma\), and subsequently the further coupling choices.
In particular the global kernel rate used to choose a width cannot be
replaced afterwards by an \(M\)-dependent rate. The radius coefficient
called \(C_0\) below is not the boundary norm \(C_0=c_G+1\).

ST1 fixes its intrinsic/background constants and \(M_1\) before its consumer
\(\kappa\), at lines 158–171. This is not literally the account's order.
One may reuse an estimate independent of these choices, but may not
claim a common choice exists by juxtaposing the two tables. Call the
still-needed dependency check **ORDER-match**. In particular, a bound
proved only after the account's \(M_1\) may depend on its previously chosen
\(\kappa_1\); that dependence must be exposed in a later coupling ceiling,
not hidden inside an asserted \(\kappa\)-independent ST1 constant.
The hand estimates in this section put all their smallness requirements
at the last \(\gamma\) choice and do not move an earlier constant.

### 4.2 A useful consequence of the weaker tower estimate

**Lemma 1 (quadratic error on running radii).** Let
\[
 r_i(t)=C_i g_t\ell_t^q,\qquad
 \ell_t=\log g_t^{-2},\qquad
 1\le w_t\le D\ell_t^r,
\]
with fixed positive \(C_i,D\), fixed finite \(q,r\), and
\(g_t^{-2}\ge\gamma^{-2}\). For any fixed \(K>0\) and \(\epsilon>0\), a last
ceiling on \(\gamma\) gives, uniformly in \(t\) and the allowed weights,
\[
 K(w_t r_1(t))^2\le\epsilon w_t r_0(t).                 \tag{S8}
\]
The same holds with both radii multiplied by any \(0<\mu\le1\).

*Proof.* Division by the positive right-hand radius gives
\[
 K\frac{(w_t r_1)^2}{w_t r_0}
 =K w_t\frac{C_1^2}{C_0}g_t\ell_t^q
 \le KD\frac{C_1^2}{C_0}e^{-\ell_t/2}\ell_t^{q+r}.
\]
For an integer \(a>q+r\), the exponential series implies
\(e^{\ell/4}\ge(\ell/4)^a/a!\). Consequently the last expression tends
to zero uniformly for \(\ell\ge\log\gamma^{-2}\to\infty\).
Replacing \(w_t r_i\) by \(\mu w_t r_i\) multiplies the ratio by \(\mu\).
This proves both assertions without a numerical estimate. ∎

The account's stage factors satisfy \(w_t=\mathsf L_0^{2e}\le\mathsf c_1R_t\)
at CA-I 49626–49661. Its logarithmic cell-size bound supplies the required
\(D\ell_t^r\) envelope; the row's *radius index*, including \(t=j\) in
(1.66), is the one to use. Thus the \(\epsilon_1^2\) term of B109 P20,
equation (110), is absorbable on these running slices. Specifically its
bound
\[
 K(\epsilon_0+\epsilon_1^2),\qquad
 (\epsilon_0,\epsilon_1)=(\mu w_t r_0,\mu w_t r_1),
\]
is at most \((K+\epsilon)\mu w_t r_0\). The two curvature/current mesh
factors in B109 (110) remain unchanged. P20 is used with its real-orbit,
averaging and analytic-ball premises, not as an unconditional supplier.
Its proof and its limitation are at `b109.md:3340–3462`.

This is **not L17**. L17 asks for the particular earlier constant \(2B_3\)
on the whole independent-radius small-pair domain, with no quadratic
budget (`b109.md:3186–3248`). Neither \(K\le2B_3\) nor an admissible
enlargement of that already chosen \(B_3\) follows from P20. More relevant
to STAGE, (S8) removes a nonlinear error; it does not turn a bound with
leading coefficient \(K\) into a prescribed stage inequality with coefficient
less than one. At an R1 core it must also fit the factor \(L^{-(i-p)}\)
and the actual element radius. Those comparisons are not in (S8).

### 4.3 Cauchy smallness is available after admission

For an admitted ST1 input and its full source carriers, its (71) gives
\[
 \rho_X=(2a_X)^{-1},\qquad
 a_X\le C_{\rm st}E_{\bar\kappa}\frac{A_1}{C_0}
       \ell_j^{p_1+r-q}
       +C_DE_{\bar\kappa}C_AA_1g_j\ell_j^{p_1}
          K_{\rm pin}/\epsilon_{\rm lev}.               \tag{S9}
\]
All constants on the right have already been fixed. Since
\(q>p_0+2r_R\) and \(p_0-p_1>r\), the first power is negative, and the
second term tends to zero. Hence \(a_X<1/4\) and \(\rho_X>2\) follow
uniformly by the final ceiling, **on the hypotheses of that estimate**.
This is a hand consequence of `st1-r4.md:1455–1507`, not a proof of
complex input membership, DR, or a change of the actual source map.

For such an admitted composition \(\Phi\), put \(G=\Phi-f_0\). It vanishes
at \(z=0\) and is bounded by \(2b_f\). On \(|z|<\rho_X\), Schwarz's inequality
gives \(|G(s,1)|\le2b_f/\rho_X\). Cauchy in each distinct switch variable
then gives (77). Multiplying \(f\) by any scalar multiplies this estimate
by the same scalar. Thus substitution preserves a supplied activity
bound and makes its *increment* small; it cannot manufacture (S6)'s
normalization or the bound on the Gaussian family.

This also locates the order-of-limits issue: finite Boolean inversion
requires no infinite-series theorem. Passing from those finitely many
identities to the logarithm of (S2), uniformly over growing regions,
requires separate local Gaussian and cluster majorants.

## 5. One admission lemma, and three attacks

The following is the next target of the **ST1 reconstruction route**.
It is a preliminary response lemma, not a renamed conjunction of all
parts of H-STAGE. It does not assert that all the later integration
estimates follow from it.

**AD-ST(2), the unswitched stage response disc.** Fix an eligible ordinary
preparatory stage, its actual determining sets, boundary data and collar,
and a carried local term with read region \(X\). Let
\[
 \mathcal A_+(\widehat X)=\widetilde U_k^{(n+1)c,\Sigma}(\widehat X),
 \qquad \mathcal A_-(X)=\widetilde U_k^{(n)c,\Sigma}(X),               \tag{S10}
\]
with exactly the prescribed radii, stage factors, auxiliary configurations
and gauge clauses. Here \(\widehat X\) denotes the union of the **actual
complete input carriers** read by the stage reconstruction on \(X\),
including its determining rows, outward endpoints and boundary data.
It is not an arbitrarily chosen larger domain to which the field may
be extended. Exterior data allowed by the local-space definition are
retained and quantified over. All assertions below are required
hereditarily on the admissible subregions, with their own determining
systems.

For \(P=(U,A',\mathbb J)\) presenting a point of \(\mathcal A_+(\widehat X)\),
keep the real factor \(U\) and all Borel variables fixed. Let \(\phi=(A_j,B_j)\)
range over the actual real passing support of \(\chi^{(j)}\chi'^{(j)}\)
in (S2), on the real integration stratum associated to those fixed data.
That stratum is held fixed when the analytic variables vary; no indicator
is evaluated on a complex argument. Fix its prescribed coordinate/datum
map; do not replace it by ST1's redesigned passing test. Write
\((H(P;\phi),K(P;\phi))\) for the
response germ at real admitted data of CA-I 54247–54248, so that
\[
 \mathcal E_z(P;\phi)=
  \bigl(e^{iz\eta H(P;\phi)}\mathbb U,
                 \mathbb J+zK(P;\phi)\bigr).                       \tag{S11}
\]
The germ is normalized by the real critical branch and the prescribed
stored transports. The variable \(z\) scales the **response field**;
\(\mathcal E_z\) need not equal the physical solution for datum \(z\phi\).
At \(z=1\) it must be the actual shifted pair in (S2).

Prove that this germ has a single-valued, restriction-compatible
holomorphic continuation in the declared complex pair variables to the
whole \(\mathcal A_+(\widehat X)\), and that
\[
       \mathcal E_z(P;\phi)|_X\in\mathcal A_-(X)
                   \qquad (|z|<2).                               \tag{AD-ST(2)}
\]
Membership includes existence of every required auxiliary branch,
the bounds on all seven entries, and the full real gauge clauses in the
fixed real-factor Cauchy presentation. The independent current remains
\(\mathbb J+zK\), not the physical current of the first component.
Constants must be chosen in §4.1's order with one positive final coupling
ceiling independent of stage, history, mesh, volume and \(X\).

Retain the background/response theorems only **on their admitted inputs**,
and the finite real coordinate identities on their stated supports.
Do not assume the complex conclusion of (AD-ST(2)), ST1 hypothesis 2,
a common-chart path to every input, or H-STAGE. The named matching and
admission inputs discussed below remain open, rather than being folded
into the word “actual.” The radius two is a deliberately modest first
target: it is less than the disc furnished by (S9) on already admitted
ST1 inputs. The full switch polydisc and the quantitative radius needed
for (S6) are later requirements.

### Attack 1: use ST1 directly, with its radius table

The proposed argument is to read the seven CA entries as ST1 records,
apply the coefficient-gap lemma, then Lemmas 11 and 13 and Theorem 14.
The last three implications are available. The first identification is
not.

The discrepancy is already visible before taking a derivative. On a
prepared layer, the CA bound has the form
\[
 c^{\rm CA}_{n,m}\mathsf L_0^{2e}r_i(t),\qquad
 c^{\rm CA}_{n,m}=1-\beta\sum_{v=h+1}^{j}2^{-|m-v|}
                    -\beta\sum_{v=m+1}^{k}2^{-(v-m)},              \tag{S12}
\]
with the radius index and exponent specified at 49626–49637. Every one
of the seven entries has this lift. ST1's analytic record instead has
unit lift, its own \(c^*\), its birth radius and its permanently frozen
function. It is therefore invalid to infer
\[
 |Q|<c^{\rm CA}_{n,m}\mathsf L_0^{2e}r_i(t)
       \quad\Longrightarrow\quad |Q|<c^*r_i(t)                    \tag{S13}
\]
without the scalar inequality between those two coefficients. Where
the coefficient on the left is larger, a scalar strictly between them
refutes this *inference of inequalities*. This is not an assertion that
an actual pair satisfying every other CA condition realizes that scalar.
Reducing \(\gamma\) does not change the ratio of these two bounds.

Enlarging ST1's \(C_i\) or choosing a larger logarithmic exponent can
cover some of the input inequalities, but then its CI premise requires
old activities to be bounded on the resulting larger **whole** domain.
Their bounds on the account's smaller domain do not imply that premise.
Choosing a smaller ST1 domain has the reverse problem: it does not cover
the supremum in (S4). Neither operation is a proof by restriction.

Moreover, R1 reads both erosion rules on every consumer subdomain,
including the towers of the real factor \(U\), and retains their open
continuation domains. CA-I 9902–9906 expressly distinguishes the layered
complex-tower bounds from bounds on those real-factor towers; 9988–10016
defines the latter as an additional condition in the post-step setting.
Equality of the words “tower” or “hereditary” identifies neither the
determining systems nor these extra clauses.

**Failure 1.** The actual source space and the frozen record domain have
not been identified, even at zero response. The proposed application
uses ST1 Theorem 14 hypothesis 2 as its own proof. DOM's enlarged roster
does not repair this: it is proposed and its input membership is retained.
This attack neither proves nor refutes (AD-ST(2)).

### Attack 2: form the missing towers from simple small-pair bounds

Try to avoid the domain identification by rebuilding all needed towers
from their curvature, potential and gauge inputs. The two-rule P20
estimate is the strongest available bound used in this attempt.
Lemma 1 proves that its quadratic term is harmless on a fixed running
slice. The remaining comparison is quantitative, not asymptotic:
if the target permits \(b_0^{\rm target}\) and P20 gives
\((K+\epsilon)b_0^{\rm source}\), admission still needs
\[
 (K+\epsilon)b_0^{\rm source}<b_0^{\rm target}.                      \tag{S14}
\]
No such reserve is provided by identifying two almost equal stage
radii. A last coupling ceiling can make \(\epsilon\) small but cannot
make \(K\) smaller. The exact \(2B_3\) alternative is L17, still open,
and would itself need the appropriate \(2B_3\)-sized reserve and a match
to these determining systems. We have not proved those comparisons.

There is a second uniformity issue if one tries to charge an absolute
formation error to a schedule gap instead of using a localized response.
For example the account's main-step coefficient reserve is
\((1-\theta_S)\beta2^{-a}r_0(t)\), with age \(a=k+1-t\)
(CA-I 9928–9950). A crude error \(K r_1(t)^2\) would require
\[
 \frac{K r_1(t)^2}{(1-\theta_S)\beta2^{-a}r_0(t)}
       =\frac K{(1-\theta_S)\beta}\frac{C_1^2}{C_0}
                    2^a g_t\ell_t^q<1.                            \tag{S15}
\]
Lemma 1 gives no estimate uniform in an independent unbounded \(a\).
Equation (S15) diagnoses this *proposed charging argument*; it does
not assume that age and coupling can actually be varied independently
in an admitted history. A history comparison that offsets \(2^a\), or
the spatial screening used by ST1's (74), would have to be proved and
applied. It cannot be replaced by the pointwise limit in (S8).

Finally, P20's existence statement is for its two prescribed maximal
towers on their separated determining sets. It does not supply the
whole roster's current stencils, boundary cubes and continuation paths
on every localized stage carrier. PDA's erosion calculation supplies
its (A1) geometry, not these analytic assertions; real cube gauges on
\(Q\cap X\) do not automatically furnish one gauge on an enlarged
consumer cube outside \(X\).

**Failure 2.** The running-radius calculation closes only the quadratic
error. The fixed leading coefficient, the relative reserve and the
actual full-carrier match needed in (S14) remain unproved. L17 has not
been discharged or silently weakened to P20.

### Attack 3: identify the real branch, then continue without exiting

This attacks the branch issue directly. There is a useful exact
finite-dimensional observation. Suppose two constraint maps for the
**same** action and boundary problem satisfy \(Q_+=\pi\circ Q_-\).
At a regular point,
\[
 \ker DQ_-\subset\ker DQ_+.
\]
Consequently a critical point under \(Q_+=q_+\) is also critical under
\(Q_-=Q_-(U_+)\): its action derivative vanishes on the smaller tangent
space. If it is in the earlier problem's uniqueness neighbourhood,
it is that earlier critical representative, up to the declared gauge.
This proves the real zero-fluctuation identity on a matched admitted
system. It does not give that uniqueness neighbourhood, identify two
different boundary problems, or continue the representative to an
arbitrary complex pair.

The natural next step is a first-exit argument. For each target record
\(r\), write its defining analytic read as \(F_r\), its threshold as
\(B_r\), and suppose the zero-response point has a known reserve
\[
 |F_r(P)|\le B_r-\Delta_r,\qquad \Delta_r>0.
\]
If a common chart exists along the response path and its derivative
estimate gives
\[
 \left|\frac{d}{dz}F_r(\mathcal E_z(P;\phi))\right|
                 \le\Delta_r/4,                                  \tag{S16}
\]
then integration along \(tz\), \(0\le t\le1\), proves, for \(|z|<2\),
\[
 |F_r(\mathcal E_z(P;\phi))|
     < B_r-\Delta_r/2.                                             \tag{S17}
\]
The derivative here is taken only in a genuinely holomorphic chart.
If those charts also have a uniform continuation margin, (S17) excludes
a first exit through any defining bound. The open continuation-domain
boundary must be excluded too; bounds on a list of output coordinates
alone do not exclude it.

ST1 proves just this mechanism on its admitted input, with its persistent
records, source decay and chart margins. In this application the missing
facts are the common chart and reserves for the *actual CA* auxiliary
functions throughout the full complex source space. Knowing the real
branch and an identity on real data does not supply a holomorphic
domain on which to apply the identity theorem. A merely holomorphic
localization rule does not give a bounded chart either: for real \(x\),
\(|\epsilon\sin(Nx)|\le\epsilon\), whereas at \(x=iy\) its modulus is
\(\epsilon\sinh(N|y|)\). There is no bound on any fixed complex strip
uniform in \(N\). This elementary example concerns the invalid
real-to-complex inference, not the actual Yang–Mills map.

The geometry does not supply the missing chart. Cutting a determining
system down to its read region can destroy the two-rule separation;
extending by a flat exterior changes its boundary data; a local gauge
witness is not a coherent extension on all overlaps. These are the
same precise issues retained by DOM Lemmas 12 and 14. SA 12294–12384
(BGR32–33), located through neighbouring chunk-11 index rows, likewise
uses a completely admitted reference and uniform inverse along the
comparison. It does not remove those premises by a first-exit slogan.

**Failure 3.** The zero-fluctuation identity is conditional on matching
and real admission. Continuation then needs the actual common-chart
reserve and uniform inverse before (S16) can be used. Assuming them on
every reached complex datum assumes the missing admission. No first-exit
proof or counterexample to (AD-ST(2)) has resulted.

## 6. Remaining inputs, without merging distinct problems

The comparison has at least three separate analytic steps: admission
of the actual response; identification and analytic control of the exact
integrand; construction and bounds of its local logarithm. The frozen
geometric results assist the first two but are not analytic estimates.
The following register says exactly what was, and was not, used here.

| Input | Role and standing in this attempt |
|---|---|
| ST1's background imports | A1/F0/REG, the matched P82 derivative/current theorem, PROF/RCG4, OPS/SLICE/UNQ, AV/CURV and CH are retained on their stated admitted classes. Real formation also retains RUN, actual tests, complete carriers and initial/unfinished comparisons. We have not rebuilt these suppliers by citing ST1. |
| DR and actual source/branch matching | ST1's full complex-switch response and its fixed source budget are hypotheses. The physical CA datum and real branch still require ST-test/LOC and the stated matching; a response theorem on an already admitted pair is not admission of every CA pair. AD-ST(2) isolates an unswitched part of this gap. |
| CI; NL1/LF1 formation | Whole-domain old-activity bounds and locally uniform integral/series majorants are still required. A bound after substitution is not formation on that domain. Their amplitudes cannot select the earlier radii or precision constants. |
| SLOT-CA, FM-match, FC-mean-match, FC-test and FC2 | These match the original slot set, transports, Haar/delta density, Gaussian/linear terms and every moved-variable factor. The real FM identity and CV/GS do not remove them. The analytic majorant for the outer rim integration is separate. |
| L17 in `b109.md` | Open curvature-controlled complex-tower bound with constant \(2B_3\), on the actual two-rule systems and the independent-radius domain. Attack 2 uses its proved weaker P20 substitute on running slices only; neither L17 nor the exact domain comparison follows. |
| \(C_M\) in `open-core.md:49–67` | If the Gaussian part is rebuilt through the prescribed local resolvent/root words, their full-domain continuation and summable spectral envelopes are needed. This is the precise fixed-word input, at its fixed early rate; a global inverse or a newly regrouped series does not supply it. It was not assumed to prove Lemma 1 or (S9). |
| \(C_R\),\(C_A\) in `open-core.md:69–136` | \(C_R\) supplies the two outside-consumer real minimizer estimates if that consumer is used. \(C_A\) supplies fixed-birth-date completion-collar membership in the arrest/drop-out extension. Neither has been proved here; neither is an automatic consequence of ordinary H-STAGE or PDA's geometry. They are not hypotheses secretly used for the ordinary-stage hand deductions. |
| \(C_H\),\(C_W\),\(C_O\),\(C_V\) in `open-core.md:138–238` | Respectively the three localized CMP 122b response links, correlation windows with screening, the actual near-flat precision words, and reality of the scalar sum at independent current. They remain open. None is asserted equivalent to AD-ST(2) or H-STAGE; none was needed for the elementary deductions in §4. If a later reconstruction uses those consumers, it must name the corresponding input. |

Even a proof of AD-ST(2) would not establish (S5)–(S7). The Gaussian
normalization has to be localized with its actual measure and form;
the non-Gaussian interactions must have a convergent connected expansion
with the quoted constants and filing. SA 14276–14414 (UM1–UM6) supplies
an explicit list of the regular-gas requirements: actual potential
bounds, actual cutoff/Mayer factors, local-functional derivative
majorants, enlarged switch discs, local matrix perturbation/dimension
control, and the Gaussian comparison and failed-test tail. Its parameter
choice at 14774–14816 does not prove those requirements for an unmatched
stage integrand. Those passages were located through chunk-13 and its
neighbouring rows before reading. The elementary connected-gas argument
already rebuilt in B109 P8 is a conditional consumer of an activity
majorant, not a supplier of one for (S2).

There is a simple hand check against another shortcut. For the
probability measure giving mass \(1/2\) to each point of \(\{-1,1\}\),
and any positive integer \(V\),
\[
 Z_V(z)=\int e^{Vz\sigma}\,d\nu(\sigma)=\cosh(Vz)
\]
is entire and positive for real \(z\), but
\(Z_V(i\pi/(2V))=0\). Thus finite integration, real positivity and
holomorphy alone do not provide a volume-independent nonvanishing
neighbourhood or a holomorphic logarithm. This is a counterexample to
that general inference, **not** to H-STAGE. The actual local cluster
estimates are the ingredient meant to avoid this problem.

The later account also explicitly leaves a per-rate-to-stage-norm
conversion outstanding at CA-I 106533–106587, in the survivors'
normalization argument. Its stage norm sums over filing levels, unlike
the supremum over filing levels explicitly defined in (S4). It is not
legitimate to identify those norms or claim that closing that later
lemma proves the original H-STAGE. We did not substitute that later
problem for the present response-domain target.

Only this checkout file has been created or changed. Source retrieval, searching and textual
checks supply navigation, not mathematical discharge. The original hand
deductions are Lemma 1, the conditional radius consequence (S9), and
the finite constraint/first-exit calculations in Attack 3. They retain
their stated premises and have not received an independent check.

## 7. Continuation round: the actual clause reserve

Provenance: Codex, continuation on 2026-11-05 at the same pinned checkout;
the preceding round was read in full before this continuation. This is
research, not an audit or an independent check of the preceding round.

This round keeps the CA domains. The target remains AD-ST(2), with
the distinction from H-STAGE made in §5. It tests three approaches:
the literal stage reserve,
the free-current contraction chart, and the later inherited-domain proof.

The source trail for this round is CA-I 49593–49637, 12935–12977,
14376–14645, 124189–124310, 125926–126055 and 128962–129080;
SA 12294–12384; ST1 Lemmas 7, 8, 11, 13 and Theorem 14; DOM's
actual-input paragraph and Lemmas 12–14. The CA full index located the
chart and the three inclusion results; their neighbouring rows were
also checked.

Two promising-looking later results do not yet supply this admission.
CA-I 125926–126055 bounds weighted radii by a density-indexed maximum.
It does not compare the functions read by two different determining
systems. CA-I 128962–129080 explicitly assumes its one-step tube
inclusion in (III), and its composite-entry increment bounds in (IV).
The source-image proof at 124189–124324 independently invokes increment
bounds and the arrest theorem. Importing it would retain those inputs.

### 7.1 Attack 4: spend the literal CA stage gap

First keep the same read, carrier, radius index and weight on both sides.
For example, take a common interior portion of a (1.64) layer with
\(m<j\). This excludes newly exposed territories and changes of clause
type. Write \(c_{j,m}\) for (S12) and
\(w_m=\mathsf L_0^{2\max(0,m-k_0)}\). Direct subtraction gives
\[
 c_{j,m}-c_{j+1,m}=\beta2^{-|m-(j+1)|},\qquad
 \Delta_{i,m}=\beta2^{-|m-(j+1)|}w_mr_i(m).             \tag{S18}
\]
This is the account's gap, not ST1's different permanent-record gap.
There is no factor \(1/N\) in (S18). Its derivation uses only the
coefficient printed at CA-I 49606–49617, at consecutive stages.

**Lemma 2 (persistent simple clauses).** On such complete common reads,
assume the source satisfies the new-stage inequalities, including the
full-stencil absolute ceilings used in ST1 Lemma 7. Suppose its
actual response is defined and holomorphic and satisfies
\[
 \max\{\lambda_m|H|,\lambda_m^2|\nabla_UH|,
                         \lambda_m^3|K|\}
 \le D\epsilon_j e^{-\mu d},\qquad
 \epsilon_j=A_{\rm src}g_j\ell_j^{p_{\rm src}},\quad p_{\rm src}<q,
                                                               \tag{S19}
\]
on every full stencil used below. Here \(\lambda_m=L^m\eta\).
Suppose the distance of that stencil from the full source carrier obeys
\[
 d\ge\rho(|m-j|-c)_+-b,\qquad \mu\rho\ge\log4,                    \tag{S20}
\]
where \(b\ge0\) and the integer \(c\ge0\) are fixed. Retain the
adjacent-radius comparison \(r_i(m+1)/r_i(m)\in[1/2,2]\), and
\(C_1\ge C_0\). All constants and the exponent in (S19) are fixed
before the last coupling ceiling. Then that ceiling makes the shifted
pair satisfy entries 1, 3, 5, 6 and 7 of the old clause for every
\(|z|<2\). At least half of each gap (S18) remains. Any identical
real gauge clause on the same carrier remains true.

The actual completed datum must supply (S19); a passing indicator alone
is not that assertion. In particular this lemma does not assume that
both variables \((A_j,B_j)\) in (S2) have ST1's \(\delta'_j\) bound.
ST1's own reconstructed stage has \(p_{\rm src}=p_1\). A different
stage datum must supply its own \(A_{\rm src},p_{\rm src},D\).

*Proof.* The stage weights have the polylogarithmic envelope in §4.2.
Thus a last ceiling makes all normalized source twists, their gradients
and complex plaquette defects smaller than any fixed positive constant.
The same ceiling makes the response small on \(|z|<2\). No lower
bound on \(c_{j,m}\), uniform in the stage depth, is needed here.

For completeness, apply ST1 Lemma 7's local product estimates (45)
at scale \(\lambda=\lambda_m\). Set
\[
 s=\max\{\lambda|zH|,\lambda^2|\nabla_U(zH)|,
                                      \lambda^3|zK|\},
 \quad
 v=\max\{\lambda|A'|,\lambda^2|\nabla_UA'|,
                    \lambda^2\eta^{-2}|\partial\mathbb U-I|\}.
\]
Take maxima over the complete stencil. We can require \(s,v\le1\)
and the smaller fixed logarithm ceilings of that lemma. For
\(D_A=A''-A'\), its first two bounds imply
\[
 \lambda|D_A|\le5s,\qquad
 \lambda^2|\nabla_UD_A|\le13s+96(\eta/\lambda)sv\le109s.
\]
Its plaquette bound gives
\[
 \lambda^2\eta^{-2}
 |\partial(e^{iz\eta H}\mathbb U)-\partial\mathbb U|
 \le2^{12}\{s+s^2+sv+(\eta/\lambda)sv\}\le2^{14}s.
                                                               \tag{S21}
\]
Here \(\eta/\lambda\le1\). These inequalities also construct the
small logarithm for \(A''\); no auxiliary tower was used. The
independent-current increment is at most \(s\), and the real
curvature is unchanged. We may use \(K_{\rm pt}=2^{15}\) for all
five entries. Consequently their changes are bounded by
\(2K_{\rm pt}D\epsilon_j e^{-\mu d}\).

Put \(a=|m-j|\). For either radius, the adjacent comparison and
\(C_i\ge C_0\) give
\[
 {\epsilon_j\over r_i(m)}
 \le {A_{\rm src}\over C_0}\ell_j^{p_{\rm src}-q}2^a.
\]
Since \(|m-j-1|\le a+1\), \(w_m\ge1\), and
\(4^a e^{-\mu\rho(a-c)_+}\le4^c\), we obtain
\[
 {2K_{\rm pt}D\epsilon_j e^{-\mu d}\over\Delta_{i,m}}
 \le {4K_{\rm pt}D A_{\rm src}\over\beta C_0}
       e^{\mu b}4^c\ell_j^{p_{\rm src}-q}.                         \tag{S22}
\]
The right side is at most \(1/2\) uniformly after a last ceiling,
because \(p_{\rm src}<q\) and \(\ell_j\ge\log\gamma^{-2}\).
The source bound plus this increment is less than the old bound
minus half its gap. The real factor stays fixed, so any identical
gauge witness stays valid. This proves the lemma. ∎

The order in this conditional estimate is the account's order.
Use an earlier fixed rate \(\mu\) and a permitted later separation
floor for (S20); then fix the response amplitude and running radii;
finally choose \(\gamma\). If that earlier rate and the actual
separation are not available, (S20) remains a premise. This argument
does not lower a rate after a width has read it. It imports the
adjacent comparison, rather than inferring a CA trajectory from ST1.

**Failure 4.** This removes a possible age loss for the five simple
entries on persistent reads. It supplies neither entry 2 nor entry 4:
those are nonlinear functions of an auxiliary critical background.
ST1 Lemma 8 would give the needed relative, exponentially localized
increment on a matched ambient/subordinate system. Its proof reads
settlement, a raw-datum ball, a regular real centre, and complete
carriers. It cannot be applied merely because both sides name a tower.
The CA input does not even impose the corresponding real-factor tower
bounds (CA-I 9902–9906). A reconstruction of those real towers and
the domain match would be additional work.

Newly exposed clauses, the (1.66) radius-index changes and new gauge
cubes are also outside Lemma 2. Neither (S18) nor PDA supplies them.
L17 remains a possible absolute formation input, not this relative
increment theorem. Its \(2B_3\) bound would still have to fit the
actual clause and its reserve. Thus the scalar gap is not the terminal
obstacle in this attack; the actual auxiliary chart and carrier are.

### 7.2 Attack 5: construct the response on one absolute operator class

The free-current chart offers a way to avoid a path between arbitrary
source points. CA-I 12935–12977 defines its class \(\mathfrak S\):
\(\mathbb U=e^{i\eta\mathfrak a}U_r\), with real \(U_r\) in small
cube gauges, \(N_{U_r}(\mathfrak a)<a_1\), and
\(|\mathbb J|_{(-3)}<a_\gamma\). Each required gauge is on a whole
cube of the prescribed class, including the stated enlarged cubes.
The current is independent. For a datum \(|B|<c_9\), the chart's
unknown solves
\[
 A_0=\widetilde{\mathfrak G}_0
       [\Theta_J(A_0+H_0B)-\mathbb V'^{J}(A_0+H_0B)].              \tag{S23}
\]
Here \(\widetilde{\mathfrak G}_0=P_0G_0\) is the constrained Green
operator, \(H_0B\) is the linear lift, \(\Theta_J\) is the linear
correction at free current, and \(\mathbb V'^J\) is the gradient of
the higher-order action. The iteration norm is
\(N(A)=\max\{\sup_m\lambda_m|A|,\sup_m\lambda_m^2|\nabla_UA|\}\)
(CA-I 12738–12753).
This is CA-I 14376–14430's equation, not a substituted physical-current
equation. Its contraction proof, 14540–14645, uses the free-current
operators and nonlinear-correction lemmas. The useful contraction
condition is
\[
 B'_0[C_\Theta a_\gamma+8C_4^J\bar\varepsilon_4]\le\tfrac12,
 \qquad B_0c_9\le\bar\varepsilon_4\le a_3/4.                      \tag{S24}
\]
The account proves the conditional analytic fixed point; we reuse that
proof with credit, rather than present a new proof of it.

There is a real partial simplification. If every source read lies in
this very class, the uniform fixed-point iteration defines the response
on each fixed-real-factor slice. Uniqueness identifies overlapping
charts wherever their equations, coordinates and small balls agree.
One does not need a path connecting all real source backgrounds.
The weighted running radii make the absolute twist/current ceilings
small after \(\gamma\). For a supplied whole-cube witness the same
is true of \(BCM w_m r_0(m)\). This follows from §4.2's exponential
versus power estimate, with \(M\) already fixed.

But a bound on the iteration variable in (S23) is not an invariant-domain
bound for every composed auxiliary function. The equations control
\(A_0\) and the derived response. They do not assert
\[
 \|F_r(\mathcal E_z(P;\phi))-F_r(P)\|
                   \le\tfrac12\Delta_r                          \tag{S25}
\]
for the actual old tower read \(F_r\), uniformly over its full source
space and all its hereditary determining systems.

**Failure 5.** Applying this construction to AD-ST(2) still requires:
the actual complete source reads in \(\mathfrak S\); the actual
completed datum within \(|B|<c_9\) on the complex source; identification
of (S23)'s branch and coordinates with (S2); and (S25) on each auxiliary
carrier. Real passing tests prove none of their complex counterparts
by themselves. The cube-supply issue is exactly the kind distinguished
at CA-I 49495–49525; local gauges on intersections are not extensions
to missing parts of a carrier. On already matched complete reads the
contraction is usable. Assuming those matches for every original read
would supply the missing admission, rather than derive it.

If localization is implemented with the prescribed resolvent words,
the whole-domain word bounds of \(C_M\) remain open. An unswitched
global contraction does not prove \(C_M\). Conversely, this argument
does not assert that \(C_M\) is necessary for every possible proof of
AD-ST(2). L17 is likewise not discharged by the absolute contraction.

### 7.3 Attack 6: port the account's later source-image inclusion

This attack asks whether the later theorem already supplies the missing
implication in its own spaces. The source-image proposition at CA-I
124189 uses \(\mathfrak S_{\rm src}\), the arrested source with all its
\((\Sigma^*)\)-triples, and concludes membership in the inherited
domain \(\mathfrak D_n^\flat(X)\). Its proof separates retained
components, old pieces and half-margin clauses.

For unchanged entries the proof compares thresholds. For changed
entries it charges the increment to a quarter of the inherited room.
On excluded components it invokes the arrest theorem. These steps
work under their stated inputs; no new derivation of that implication
is needed here. Their application to (S10) would require an actual
identification of the source, target and tube, together with those
inputs.

The precise unresolved use is visible in CA-I 128999–129016.
Hypothesis (III) already requires that the one-step tube send
\(\mathfrak L_{l+1}\) into \(\mathfrak L_l\) on
\(Z^{\mathrm{on}}\). Hypothesis (IV) supplies the composite-entry
move in every frame and every \((\Sigma^*)\)-triple, including the
derived-entry bound. These are later-space counterparts of the
estimates sought in Attack 4; their domains have not been identified.
The maximum defining \(\gamma_0^{(k)}\) at 125932–125937 merely
dominates the existing weighted radii. Taking a maximum cannot create
an auxiliary branch or prove its displacement estimate.

**Failure 6.** The attempted port leaves tube inclusion as an explicit
hypothesis of the later theorem, along with composite increment
assumptions on every retained triple. It is not a proof of them.
Furthermore,
\(\mathfrak N^{(n)}\), its dated weights and arrested source have
not been identified with the ordinary spaces (S10). Even their printed
schedule bounds differ: 125938–125939 uses \(1+2\beta\le1.4\),
whereas the earlier layered convention sets \(\beta=1/4\).
This is a required convention match, not a counterexample to either
conditional theorem. The later arrest/completion route would retain
\(C_A\); it cannot be used to assert that ordinary H-STAGE proves
that separate core obligation.

### 7.4 Checkpoint after the three further attacks

Lemma 2 is a conditional hand deduction for the literal CA schedule.
It advances the comparison beyond §5's unmatched ST1 coefficients:
on persistent simple clauses, the correct gap can absorb the localized
response without a depth-dependent loss. It does not supply the actual
response estimate, auxiliary continuation, or changed-clause admission.
The later contraction and inheritance results were used only with
their explicit premises. No integration-stage norm clause was closed.

The exact-string source occurrences of \((K)\), \((Q^+)\) and
\((F_m)\) were also inspected. They refer back to the imported stage
theorem at 54358–54362, 54487–54491 and 55194–55224; they do not
expand those predicates there. Thus §1 deliberately retains the
unexpanded imported slots. A fully self-contained statement with those
predicates defined has not been recovered from the permitted quotation.
This is a limitation on the requested transcription, not a mathematical
counterexample or a substitute for the six attempted arguments.

## Result

**Open lemma**

**AD-ST(2): actual preparatory response admission.** In the ordinary
CA preparatory stage, with the exact spaces, carriers, real integration
stratum and response germ specified in (S10)–(S11), prove a single-valued
hereditary holomorphic continuation on the whole new complex domain
such that
\[
 \left(e^{iz\eta H(P;\phi)}\mathbb U,
                  \mathbb J+zK(P;\phi)\right)\big|_X
       \in\widetilde U_k^{(n)c,\Sigma}(X)
       \quad\text{for every }|z|<2,
\]
uniformly over the permitted stages and inputs, with constants in the
account's order. All seven field bounds, auxiliary continuation domains
and prescribed real gauge clauses are required; the current remains
independent. Do not assume complex input admission or the conclusion
as a premise of a derivative theorem.

The earlier three attacks in §5 failed at the domain/radius identification,
the fixed tower coefficient and full-carrier reserve, and common-chart
continuation. The continuation's three attacks in §7 failed at the actual
auxiliary-function and carrier match, the admission and invariant-domain
inputs of the free-current contraction, and the explicit tube-inclusion
premise of the later inherited-domain proof. Lemma 2 does pay the literal
stage gap for the five persistent simple entries under its response and
geometry hypotheses. It does not pay for missing auxiliary branches.
No counterexample to this lemma or to H-STAGE was established.

The quotation of H-STAGE and its separate profile-class assumption have
been recovered with their source-defined content and explicit imported
slots. Frozen ST1 is a different conditional substitution theorem;
DOM, GEOH and PDA do not make it the quoted integration-stage theorem.
The running-radius quadratic error is controlled by Lemma 1, and Lemma 2
controls the specified persistent simple clauses conditionally. Nevertheless,
H-STAGE, its exact Gaussian/cluster bounds, the additional drop-out
application conditions and the top-to-bottom T0 proof remain open.
