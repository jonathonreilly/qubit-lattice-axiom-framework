# NL1 input (L): product-box holomorphy and the CI reduction

Provenance: Codex, 2026-11-04, pass 2 of Claude's `nl1-L-draft.md`, at repository commit `2afa141308f85e0fb262acd684c25a49e354feb6`. Research text; not an audit; grants no status; not yet refereed. Source material is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, at `31a47c543775`.

Theorem 4 proves the main-step input (L), conditionally, with radius
\(R=(\log\theta_{i-1})^q\). Theorem 7 gives a corrected CI reduction.
Neither theorem supplies the actual activity construction. All arguments below
are written proofs. No run discharges a mathematical step.
The substitution design comes from Claude's draft and the ST1 notes;
the underlying block integration is Bałaban's, as attributed in CA-II.

## 1. Definitions

**D1 — finite geometry and variables.** Fix a finite history, a main step
\((i-1,\mathrm{out})\to(i,\mathrm{in})\), and its other real data \(\mathscr R\).
Let \(I\) be its integrated free bonds. Use the Pauli basis \(T_1,T_2,T_3\),
orthonormal for \(\frac12\operatorname{Tr}(AB)\), and
\[
 E_{\mathbb C}=(\mathbb C^3)^I,\quad
 |\zeta|_\infty=\max_{b,a}|\zeta_{b,a}|,\quad
 \mathbb D_t=\{\zeta:|\zeta|_\infty<t\},\quad
 u(\zeta)(b)=g\sum_a\zeta_{b,a}T_a,\qquad c_T=3.
 \tag{1}
\]
Thus \(\|u(\zeta)\|_\infty\le c_Tg|\zeta|_\infty\) in matrix norm.
An empty \(I\) gives a constant function; omit constant terms from subsequent
minima over read sets. The norm of the empty vector is zero.
The physical window \(\mathcal W\) contains zero and satisfies
\(|y|_\infty\le C_{\rm win}A_1\ell^{p_0}\), where
\(\ell=\log\theta_{i-1}\), \(g=\theta_{i-1}^{-1/2}\).

Let \(\mathcal C\) be the level-\((i-1)\) cubes of side \(M\). Fix boundary
tie rules. Assign a free bond to its midpoint cube \(\Delta_b\), and a source
row to its initial-site cube. Connected means connected by faces, edges or
corners, unless explicitly called face-connected. For nonempty connected \(X\), set
\[
 \mathbb S_X=\{s\in\mathbb C^{\mathcal C}:|s_\Delta|<e^{\bar\kappa},\ s|_X=1\},
 \quad K_X(s)=\text{the component of }\operatorname{supp}s\text{ containing }X,
 \quad(s\odot\zeta)_{b,a}=s_{\Delta_b}\zeta_{b,a}.
 \tag{2}
\]
Holomorphy on \(\mathbb S_X\) means holomorphy in its unfixed coordinates.
All carriers include the stencils, endpoint pillars and pinning reads they use.

**D2 — frames and chain domains.** Use the frame of frozen [IN1](in1.md),
(1)–(2): for \(m\le n\),
\[
 \theta_j\ge\gamma^{-2},\qquad
 \underline\lambda(n-m)-c_5\le\theta_m-\theta_n\le\bar B(n-m).
\]
Here \(0<\underline\lambda\le\bar B\), \(c_5\ge0\),
\(g_m=\theta_m^{-1/2}\) and \(\ell_m=\log\theta_m\).
Put \(\epsilon_m=A_0\theta_m^{-1/2}(\log\theta_m)^{p_0}\) and adopt
\[
 r_\iota(m)=C_\iota\theta_m^{-1/2}(\log\theta_m)^q,
 \qquad C_1\ge C_0>0.                                      \tag{Tq}
\]
In every simple, tower, core and witness radius of [ST1 round 2](st1-r2.md),
(14), (18) and §1, replace \(\alpha_\iota\epsilon_m\) by \(r_\iota(m)\).
Use the permanent coefficient \(c^*\) of [ST1](st1-r3.md) (the ledger; Definition M1 of the round-3 draft),
with \(c_{\min}\le c^*\le1+\beta_s\). Keep each record's function, units,
formation frame and lift frozen. Either use round-3 per-element cores R1,
or the scalar-infimum cores after Lemma 1's formation comparison.
Write \(\lambda_\tau^{\rm test}\) for ST1 (56)'s smoothed domination of
the raw tests, and \(\Lambda_Q^{\rm test}=\sup_{Q^+}\lambda_\tau^{\rm test}\).
The **domain multipliers** are these quantities for Tq. The optional **Tq0**
design sets the domain multipliers to one; it leaves the raw test exponents
and \(\lambda_\tau^{\rm test},\Lambda_Q^{\rm test}\) unchanged.
Initial and unfinished entries must satisfy the same comparisons explicitly.

Write \(\mathcal D_{\rm in},\mathcal D_{\rm tar}\) for the resulting chain
domains of this transition. On their fixed-real-factor fibres use
\[
 P=(U,A',\mathbf J),\quad \mathbf U=e^{i\eta A'}U,\qquad
 P\dotplus(H,K)=
 \bigl(U,(i\eta)^{-1}\Log(e^{i\eta H}e^{i\eta A'}),\mathbf J+K\bigr).
 \tag{3}
\]
The real \(U\) stays fixed. The current remains independent at complex points.
Use ST1's input layer metric \(d_+\), layer \(m_+\), scale \(l_+\), and
\[
 n_b(h)=\max\{l_+|H|,l_+^2|\nabla^UH|,l_+^3|K|\},\quad
 \beta_*=(1-\theta_s)\beta_s,\quad
 w(m)=\tfrac12\beta_*2^{m-i}r_0(m),\quad
 \|h\|_w=\max_{b\in\mathcal R_f}n_b(h)/w(m_+(b)).             \tag{4}
\]
Here \(\mathcal R_f\) is the complete read set of an activity. The value
\(w(i)\) is a comparison weight; it does not assert a new top-level gap.
Actual target-record gaps are required separately below.
All margins are positive, with \(0<\theta_s<1\), \(\beta_s>0\),
\(c_{\min}>0\) and \(C_{\rm car}\ge0\).

**D3 — the centred substitution.** Let \(v_0\) be the unscaled stored free
datum, fixed by \(\mathscr R\); let \(S\) be its completed-source map and
\(h(s;P,S)\) the regional response. Define
\[
 \begin{split}
 v(s,\zeta)&=v_0\oplus u(s\odot\zeta),\\
 h_0(P)&=h(\mathbf1;P,S(v_0)),\\
 H_f(P;s,\zeta)&=h_0(P)+h(s;P,S(v(s,\zeta)))-h(s;P,S(v_0)),\\
 \Pi_f(P;s,\zeta)&=\rho_f^{\rm res}
       \bigl(P\dotplus\mathcal P_P(H_f(P;s,\zeta))\bigr).
 \end{split}                                                    \tag{5}
\]
\(\mathcal P_P(h)=h^\delta\) is ST1's pin applied to the *total* shift;
\(\rho_f^{\rm res}\) restricts and changes units as in ST1 (9).
Stored slots \(\mathfrak q_f\) are separate fixed arguments.

## 2. Exact hypotheses and order of choice

The following are imports, with their scope part of the hypothesis.

**H-ST (domain calculus).** Import ST1 Theorem 14's geometry, averaging,
background, derivative, profile, gauge, inverse and uniqueness hypotheses:
GEO, AV/CURV, A1/F0/REG, P82°–M1, PROF/RCG4 and OPS/SLICE/UNQ.
Require their uniform estimates on the absolute envelope containing the Tq
domains. Require actual compatible gaps ST1 (13), the input point in
\(\mathcal D_{\rm in}\), all working cores, real turning gauges, branch and
witness ceilings, and all read-carrier embeddings. In particular:

- ST1 Lemma 4 supplies a local, real pin, holomorphic where every relevant
  endpoint top is forced levelled. If
  \(n_b(h)\le A e^{-\mu d_+(b,\mathcal S_{\rm src})}\), then
  \(n_b(\mathcal P_P h)\le C_{\rm lev}A e^{-\mu d_+(b,\mathcal S_{\rm src})/2}\) and
  \(\widehat\epsilon_y(h)\le K_{\rm pin}A e^{-\mu d_+(y,\mathcal S_{\rm src})/2}\).
  The levelling threshold is \(\epsilon_{\rm lev}\).
- ST1 ([st1-r3.md](st1-r3.md)) Lemmas 5, 8 and 11 in the lift-free branch Tq0 (round-3 draft Lemma 11′ for lifted cores is not used; see the scope note),
  admit a pinned shift of norm at most \(r_*\) into \(\mathcal D_{\rm tar}\),
  leaving half every gap and continuation-tube room \(\delta_B/8\).
- The full source carrier \(\mathcal S_{\rm src}\) satisfies, with \(j=i-1\),
  \(d_+(b,\mathcal S_{\rm src})\ge\rho_0(j-m_+(b)-3)_+-C_{\rm car}\).
  Input layers satisfy \(m_+(b)\le i\).

These are conditional domain estimates. Frozen [P82](p82.md), Theorem P82,
concerns a real critical reference; it does not supply the whole complex
response package below. Round 3's all-transition admission additionally reads
GEO-mark, GEO-box, RUN-low, BOX-bg/id/resp, ST-test and LOC-form or LOC-decay.
Their validity for the actual history is not inferred here from a radius change.

**H-FL (completed source and physical identity).** On \(\|v\|_\infty<a_{\rm ch}\),
\(S(v)=b_V(a_V(v))\), with \(V=M_-(U)\), is holomorphic, real at real data,
zero at zero, and \(\|S(v)\|_{\rm src}\le C_A\|v\|_\infty\).
Each source row reads only free rows within distance \(R_\sigma\).
For a fixed \(C_{\rm st}\), require
\[
 \|v_0\|_\infty\le\delta_0:=C_{\rm st}A_1g\ell^{p_0}.          \tag{6}
\]
All completed sources in (5) are supported in \(\mathcal S_{\rm src}\), including the
stored source. An empty \(\mathcal S_{\rm src}\) gives a constant carried term and is
omitted from the distance minima below. At \(s=\mathbf1,y\in\mathcal W\), ST1 Lemma 12 identifies
\(\Pi_f\) with the actual old pair and its stored transports. Its regularity,
boundary, retained-row and current identities are required.
ST1's chart construction F1–F5 ([st1-r3.md](st1-r3.md)) and the finite analytic reduced map motivate this package.
**Outstanding:** F8 leaves the stored-threshold comparison explicit; a small
completed source alone is not the raw-datum bound (6). CA-II's displayed
change of variables does not establish this package on its own. H-ST's
layer separation is required for the full source, including its stored part.

**H-DR (complex response and exact component reads).** For every admitted
input pair, \(|s_\Delta|<e^{\bar\kappa}\) and
\(\|S\|_{\rm src}<s_D:=\epsilon_De^{-c_D\bar\kappa}\), the response is jointly
holomorphic in the complex pair, source and switches, real at real arguments,
zero at zero source, and satisfies
\[
 n_b(h(s;P,S))\le C_DE_{\bar\kappa}\|S\|_{\rm src}
          e^{-\mu d_+(b,\operatorname{supp}S)},\qquad E_{\bar\kappa}\ge1.
 \tag{7}
\]
For each face-component \(K'\) of \(\operatorname{supp}s\), the response on the bonds and stencils of \(K'\) depends
only on \(s|_{K'}\) and the source rows assigned to \(K'\), at fixed \(P\) (as SA 5797–5801 splits it).
Require restriction consistency and the ST1 covariance conventions.
**Outstanding:** this uniform complex-source estimate, including its current,
and this precise row-locality clause strengthen the printed ST1 (16).
Multiplying one already formed response by a scalar does not prove (7).

**H-ACT (activities and exact term decomposition).** On the restricted target
domain each carried activity has ST1 §1's holomorphic, Borel, stored-slot,
real-tie and real-gauge interface, and is real on real triples. Assume the
actual non-Gaussian exponent, modulo its value at zero, is the sum of the
following evaluations. All required domain inclusions are part of this import.

| Kind | Required function and bound on the whole declared complex domain |
|---|---|
| S: strip; Z: carried elimination logarithms | Holomorphic pair functions with \(|f|\le b_f\); the branch of each \(\log z\) is supplied. |
| E, R: regular and remainder terms, including healed terms | The actual carried functions with \(|f|\le b_f\), including their creation-domain and radius-ratio conventions. |
| B: boundary terms, including drop-outs | \(|f|\le\mathsf B e^{-\kappa d^\natural(\mathcal S;X)}=:b_f\); a connected carrier containing every read is supplied. |
| K: kept forms | At fixed stored field, \(\sup_{P,Q}|f(P)-f(Q)|\le O_f\) on the target domain. Use the relative-form carriage and native-action hypotheses of [kept-cov-check](../gates/kept-cov-check.md), Defects 1–2. |
| I: standing islands | \(\Psi=\Phi-\Phi^\circ\) is holomorphic and \(\operatorname{Re}\Psi\le B_f:=C_\Psi V^\circ\); the restricted chain domain lies in its full fixed creation domain. |
| W: local remainders | The functions \(\phi_f\) and maps \(w_f\) specified in Lemma 3. |

The step's own elimination factors, independent of the integrated fluctuation,
are constant terms. For each other carried term choose a nonempty connected
\(X_f\) containing every read and pin carrier. Bounds on the sums of these
carriers are additional PAN inputs, not a consequence of their existence.
**Outstanding:** H-ACT on the changed domains is CI plus the actual term
identifications. It is not supplied by the bounds on SA's differently defined
domains. In particular the strip identification, W decomposition, logarithm
branches, kept-form oscillation, and island-domain inclusion remain explicit.

**Order.** Retain frozen IN1's order, including its independent early precision
and actual-matrix requirements. No early constant may read a later amplitude.

| Choice | Dependence and conditions |
|---|---|
| Before \(\kappa\) | Fix margins and power-count bounds, including the lift exponent budget \(r_R\); choose the exponents with \(q>p_0+2r_R\) and IN1's other inequalities. Then choose odd \(L\) under frozen IN1's row-2 floors (which imply \(L\ge27\); the local need here is only \(L\ge13\)), \(2\le L_\flat<L/2\), weak frame constants and the imported analytic packages in IN1 rows 2–4. Fix \(C_A,C_{\rm st},C_{\rm win},C_D,\mu,C_{\rm lev},K_{\rm pin},\epsilon_{\rm lev},\epsilon_D,c_D,a_{\rm ch},R_\sigma,R_W,C_{\rm car}\) on the fixed absolute envelope. Choose \(\rho_0\) with \(\mu\rho_0/2\ge\log16\); then fix the remaining ST1 domain constants, including \(r_*\). Put \(C_Q^{\rm L}=256e^{\mu C_{\rm car}/2}\). All are independent of \(M,\bar\kappa\). Set \(c_R=1\). |
| Then \(\kappa,\bar\kappa\) | Take \(\bar\kappa\ge1\) and fix \(E_{\bar\kappa},s_D\). They never enter an early precision or tower constant. |
| Then \(M\) | Impose ST1's lower bounds and \(M>R_\sigma+2\). For Lemma 3 also impose \(M>2R_W+2\). Choose post-\(M\) box constants afterwards. |
| Then amplitudes and radii | Choose \(A_1,A_0\), then \(C_0\) satisfying (8), then \(C_1\ge K_{\rm rad}MC_0\), where \(K_{\rm rad}\) is the lower-ratio constant of the imported radius window. Choose that absolute window, \(c_W\), and all activity amplitudes in IN1's order, before \(\gamma\). |
| Last \(\gamma\) | Impose (9), Lemma 1's formation and absolute ceilings, and all remaining imported ceilings. Choose actual run data only afterwards. |

The lift bound in Lemma 1 must hold with this *already chosen* exponent
budget. Newly set ST1 exponents permit \(r_R=r\): if
\(\mathcal E\le N_t^0-1\) and
\(L^{N_t^0-1}=\check R\le L(\log\theta)^r\), then
\(L_\flat^{\mathcal E}\le L(\log\theta)^r\).
Inherited exponents and comparison with the layer's frame remain part of
ST1's global bound (56)–(57); a later returned exponent cannot select \(q\).

Set \(B_L=C_{\rm lev}C_DE_{\bar\kappa}C_AC_Q^{\rm L}\), a *late* constant. Require
\[
 C_0\ge\frac{8c_Te^{\bar\kappa}B_L}{\beta_*r_*}.             \tag{8}
\]
For every \(\theta\ge\gamma^{-2}\), with \(g=\theta^{-1/2}\),
\(\ell=\log\theta\), \(R=\ell^q\), impose
\[
 \begin{gathered}
 \frac{3B_LC_{\rm st}A_1\ell^{p_0-q}}{\beta_*C_0}\le r_*/8,
 \qquad 2K_{\rm pin}C_DE_{\bar\kappa}C_A
       (3\delta_0+c_Tge^{\bar\kappa}R)<\epsilon_{\rm lev},\\
 C_A(\delta_0+c_Tge^{\bar\kappa}R)<s_D,\qquad
 \delta_0+c_Tge^{\bar\kappa}R<a_{\rm ch},\qquad
 C_{\rm win}A_1\ell^{p_0}<R.                                  \tag{9}
 \end{gathered}
\]
These are uniform coupling ceilings. Their left sides tending to zero, where
appropriate after division by \(R\), will be proved in Lemma 1.

## 3. Radius and substitution estimates

**Lemma 1 (the radius change and formation).** Suppose ST1's raw test,
profile, restriction and cube-gauge inputs hold, including the global bound
\(1\le\lambda_\tau^{\rm test}(x)\le C_\lambda(\log\theta_{m(x)})^{2r_R}\).
Then Tq permits ST1's formation comparisons, including scalar-infimum cores,
and Tq0 permits the same comparisons without domain lifts. The replacements
in the substitution estimates preserve their early constants. All additional
conditions are floors on late radius coefficients or ceilings on \(\gamma\).
This asserts a change of the conditional domain calculus, not an extension
of activities to the new domains.

*Proof.* For \(r(\theta)=C\theta^{-1/2}(\log\theta)^q\),
\(|(\log r)'|\le(1/2+q)/\theta\) when \(\theta\ge e\).
Bounded adjacent frame increments therefore give
\(1/2\le r_\iota(m+1)/r_\iota(m)\le2\) after one uniform floor on
\(\gamma^{-2}\). Consequently
\(w(m')\le4^{|m'-m|}w(m)\) and
\(L^{-p\nu}w(m+\nu)\le w(m)\) for \(p\ge1,\nu\ge0,L>4\).
These are the radius comparisons in ST1 Lemmas 1, 11 and 13.

ST1 (59) bounds the normalized real curvature and current by
\(C_{\rm RA}\lambda^{\rm test}\epsilon_m\). With Tq's matching domain
multiplier, its pointwise formation comparison becomes
\[
 C_{\rm RA}A_0(\log\theta)^{p_0-q}
       \le c_{\min}^2C_0/16.                                  \tag{10}
\]
For Tq0 use the stronger comparison with
\(C_{\rm RA}C_\lambda A_0(\log\theta)^{p_0+2r_R-q}\).
Both tend to zero. Real potential components vanish at a plain triple.
Tower formation uses restriction to the real background, not a new estimate
of a complex field. The adjacent-radius comparison pays the factors
\(L^{-2(m-i)}\) and \(L^{-3(m-i)}\) in ST1 (14).

For completeness, a scalar core at level \(i\) has its address in
\(\Omega_i\), with layers \(m\ge i\), and needs a uniform comparison
over that address. Put \(\nu=m-i\ge0\). For
\(\gamma^{-2}\ge\max(\bar B,c_5,e)\), the frame gives
\(\theta_i/\theta_m\le1+\nu\) and
\(\log\theta_m\le2\log\theta_i\). Thus, for \(a=2,3\),
\[
 \lambda^{\rm test}(x)\epsilon_m L^{-a\nu}
 \le C_\lambda A_0 2^{p_0+2r_R}
       g_i(\log\theta_i)^{p_0+2r_R},                         \tag{11}
\]
since \((1+\nu)^{1/2}L^{-2\nu}\le1\). The scalar target radius is at least
\(c_{\min}C_0g_i(\log\theta_i)^q\), even after removing the lift.
Equation (11), with the formation fraction included, fits that radius by a
coupling ceiling. For an enlarged witness cube in layers \(\ge i-1\),
\(\Lambda_Q^{\rm test}\le C(\log\theta_i)^{2r_R}\). ST1 (60) gives a gauge bound
\(C(s+2)\Lambda_Q^{\rm test}\epsilon_i\), and \(s+2\le C'LM\).
Dividing by the required witness factor, proportional to \(M r_0(i)\),
again gives a constant times \((\log\theta_i)^{p_0+2r_R-q}\).
The existing carrier and RCG4 smallness hypotheses are still necessary.
For per-element cores this argument applies on each read stencil.

At an output, BOX-bg supplies its separate \(C(M)\epsilon_t\) contribution.
The profile estimate and (11) bound formation by a fixed multiple of
\([C(M)+C_\lambda(\log\theta)^{2r_R}]\epsilon\). This too fits Tq0
after \(M\) is fixed. No claim that the raw tests have lost their lifts is used.

All remaining absolute conditions have the form
\(C(M)g(\log\theta)^{q+2r_R}\ll1\), or a smaller quantity.
They ensure chart, real-gauge, pin and continuation ceilings.
The proofs of ST1 Lemmas 7–9 and round-3 Lemma 9′ use those absolute ceilings;
their increment bounds are linear in the permitted shift and in the available
radius gaps. In Lemma 11, simple and tower gaps and \(w\) all acquire the same
\(r_0\); the core comparison uses \(b_0^{\rm mid}\ge c_{\min}r_0(i)\).
Witness drift is compared to \(g_Q\Lambda_Qr_0(i)\). Hence its constants
\(K_{\rm pt},K_{\rm tw},K_{\rm core},r_*\) do not acquire \(C_0,C_1\).
The mark ledger, pin formulas and physical fibre identities contain no radius
table. The output budget uses \(C(M)E_{\bar\kappa}\delta'_t/r_0(t)\to0\).
The real-stage budget uses
\(E_{\bar\kappa}N(\theta_j)\delta'_j/r_0(j)
 \le C E_{\bar\kappa}(\log\theta_j)^{p_1+r-q}\to0\),
under IN1's exponent inequalities. This does not give a stage box of radius
\((\log\theta_j)^q\) in a free fluctuation.

Finally, every logarithmic negative power tends to zero. For any fixed
\(d\ge0\), choose an integer \(n>d\); the exponential series gives
\(e^{-x/2}x^d\le2^n n!x^{d-n}\to0\).
This proves all asserted smallness limits, including (9). The supremum over
\(\theta\ge\gamma^{-2}\) is small once that endpoint is large. ∎

**Lemma 2 (main-step read budget).** Under H-ST and the adjacent-radius
comparison, set
\(D_f=\min_{b\in\mathcal R_f}d_+(b,\mathcal S_{\rm src})\). Then
\[
 Q_f:=\max_{b\in\mathcal R_f}
       \frac{e^{-\mu d_+(b,\mathcal S_{\rm src})/2}}{w(m_+(b))}
 \le \frac{C_Q^{\rm L}}{\beta_*r_0(i-1)},\qquad
 Q_f\le\frac{C_Q^{\rm L}e^{-\mu D_f/4}}{\beta_*r_0(i-1)}.            \tag{12}
\]

*Proof.* Put \(\nu=i-1-m_+(b)\ge-1\). Equation (4) and adjacent ratios give
\(w(m_+(b))^{-1}\le4\,4^{\nu_+}/(\beta_*r_0(i-1))\).
The separation hypothesis and \(\mu\rho_0/2\ge\log16\) bound the remaining
factor by \(e^{\mu C_{\rm car}/2}16^{-(\nu-3)_+}\).
The product \(4^{\nu_+}16^{-(\nu-3)_+}\) is at most \(64\): for
\(\nu\le3\) this is immediate; for \(\nu\ge4\) it is \(4^{6-\nu}\).
For the second inequality reserve \(e^{-\mu D_f/4}\), and use
\(\mu\rho_0/4\ge\log4\). Now
\(4^{\nu_+}4^{-(\nu-3)_+}\le64\). Multiplication proves (12). ∎

**Lemma 3 (local remainder presentation).** Assume for each W term an
affine map \(w_f(\zeta)\), supported in a nonwrapping neighbourhood of radius
\(R_W\), with
\(\|w_f(\zeta)\|_\infty\le\delta_0+c_Tg|\zeta|_\infty\).
Suppose \(\phi_f\) is holomorphic on \(\|w\|_\infty<c_W\), real on real
points, bounded by \(B_f\), with all derivatives of order below
\(k_f\ge1\) zero at zero. If \(\delta_0+c_TgR<c_W/2\), then
\(F_f(s,\zeta)=\phi_f(w_f(\zeta))\) has a connected carrier of at most
\(16\) cubes and
\[
 |F_f(s,\zeta)-F_f(s,0)|
 \le 2B_f\left(\frac{\delta_0+c_TgR}{c_W}\right)^{k_f}
 =:\omega_f.                                                \tag{13}
\]

*Proof.* A neighbourhood of diameter \(2R_W+2<M\) meets at most two cubes
per coordinate. Take all those cubes as \(X_f\); they form a connected set.
For \(w\ne0\), put \(e=w/\|w\|_\infty\). The holomorphic function
\(t\mapsto\phi_f(te)\) has a zero of order at least \(k_f\).
On \(|t|=c'<c_W\), its quotient by \(t^{k_f}\) is bounded by
\(B_f/(c')^{k_f}\). The maximum principle, followed by \(c'\uparrow c_W\),
gives \(|\phi_f(w)|\le B_f(\|w\|_\infty/c_W)^{k_f}\).
Apply this at \(w_f(\zeta)\) and \(w_f(0)\). Their difference gives (13).
Holomorphy, reality and locality follow from the stated affine reads;
there is no switch dependence. ∎

If NL1 supplies respectively
\((B_f,k_f)=(O(\theta),3),(O(1),1),(O(1+\check R_i),1),
(O(\theta\epsilon_{i-1}),2)\), the corresponding bounds are
\(O(g\ell^{3q}),O(g\ell^q),O((1+\check R_i)g\ell^q),
O(A_0g\ell^{p_0+2q})\), after \(\delta_0\le c_TgR\).
Here \(\check R_i\le L\ell^r\). These are \(O(g\ell^{3q+r})\) with
the *supplied* amplitudes retained. **Outstanding:** CA-II 79920–80013 does
not supply this local decomposition, these zero orders, or early uniform
constants. The coupling-profile term there reads a background map; the
finite range of the pivot correction alone does not make it a local function
of the free field. Lemma 3 is conditional on precisely that extra data.

**Theorem 4 (main statement: input L).** Assume H-ST, H-FL, H-DR and H-ACT,
the Tq or Tq0 design of Lemma 1, (8)–(9), and Lemma 3's hypotheses for W.
For every admitted finite history, main step and real data \(\mathscr R\),
each exponent term has a nonempty connected \(X_f\) and a holomorphic
\(F_f:\mathbb S_{X_f}\times\mathbb D_R\to\mathbb C\), with
\(R=c_R\ell^q,\ c_R=1\), such that:

1. At \(s=\mathbf1\), \(F_f(\mathbf1,y)\) is the specified term for every
   \(y\in\mathcal W\), with the same additive constant convention.
2. If \(K_{X_f}(s)=K_{X_f}(s')=K\), \(s|_K=s'|_K\), and
   \(\zeta|_{I\cap K}=\zeta'|_{I\cap K}\), then
   \(F_f(s,\zeta)=F_f(s',\zeta')\).
3. \(F_f\) is real at real arguments and
   \(F_f(s,0)=f_0:=F_f(\mathbf1,0)\) for every \(s\).
4. For S, Z, E, R and B,
   \(|F_f-f_0|\le\omega_f:=2b_f\). For K, use \(\omega_f=O_f\).
   For I, \(\operatorname{Re}F_f\le f_0+\omega_f\), with
   \(\omega_f=B_f-f_0\ge0\). For W use (13); for constant factors use zero.

The radius coefficient is fixed before \(\kappa\), independently of
\(M,\bar\kappa\). Bounds on \(\omega_f\) may contain later class amplitudes.
For carried terms take \(F_f=f(\Pi_f;\mathfrak q_f)\), using (5).

*Proof.* For \(|\zeta|_\infty<R\), masking gives
\(\|v(s,\zeta)\|\le\delta_0+c_Tge^{\bar\kappa}R\).
Equations (9), H-FL and H-DR therefore define all three responses in (5).
Their triangle bound is
\[
 n_b(H_f)\le A_V e^{-\mu d_+(b,\mathcal S_{\rm src})},\qquad
 A_V=C_DE_{\bar\kappa}C_A(3\delta_0+c_Tge^{\bar\kappa}R).    \tag{14}
\]
The levelling inequality in (9) forces every required top to be levelled on
the whole product domain. H-ST makes the pin jointly holomorphic there.
By Lemma 2,
\[
 \|\mathcal P_PH_f\|_w
 \le\frac{B_L(3\delta_0+c_Tge^{\bar\kappa}R)}
            {\beta_*C_0g\ell^q}
 \le r_*/8+r_*/8<r_*/2.                                   \tag{15}
\]
Half-gap admission and the continuation tubes follow from H-ST.
Composition with the activity proves holomorphy and its stated bound.
Neither the real factor nor a stored slot changes.

At \(s=\mathbf1\), (5) reduces to the response to the full actual source;
H-FL gives physical identification. At \(\zeta=0\), its last two terms
cancel, so the centre is independent of switches. Real inputs give real
sources, responses, pins and activities. These facts also give
\(f_0\in\mathbb R\) and \(B_f-f_0\ge0\) for I.

For locality, no cube outside \(K\) and adjacent to \(K\) has a nonzero
switch. Hence the masked free fields agree both on \(K\) and on its first
neighbouring layer, where they vanish. Since \(M>R_\sigma+2\), every source
row assigned to \(K\) reads only that layer and \(K\). Its completed values
therefore agree. Each face-component meeting \(X_f\) is contained in \(K\)
and is the same for the two switch choices. H-DR gives identical responses
on the reads in \(X_f\), including for the subtracted stored source.
The added \(h_0\) is common. All pinning reads lie in \(X_f\), so the pins,
restricted pairs and activity values agree. Lemma 3 proves the W assertions.
This establishes all six clauses of L with the oscillation form of L6. ∎

The same proof is uniform on any open fixed-\(U\) fibre
\(\mathcal O\subset\mathcal D_{\rm in}\) on which **all** hypotheses hold
uniformly: \(F_f(P;s,\zeta)\) is jointly holomorphic in
\((A',\mathbf J,s,\zeta)\). The centre may be complex there, so the island
bound is stated as \(\operatorname{Re}F_f\le B_f\), without a real-centre
claim. This proves analyticity of the displayed family. Its identification
with an actual formation integrand at every complex external pair remains
part of Theorem 7's formation hypothesis. Agreement on real critical pairs
alone does not identify a function of an independent complex current.

**Corollary 4.1 (the oscillation version of PAN L6).** For the two-sided
cases of Theorem 4, on any supplied radius \(R_f\),
\(\sup_{\mathbb D_r}|F_f-f_0|\le\omega_f r/R_f\) for \(r<R_f\), uniformly
in the switches. Thus PAN Lemma 5.3(a) can use \(|F_f-f_0|\le\omega_f\)
as its hypothesis.

*Proof.* For \(|e|_\infty=1\), the function
\(t\mapsto(F_f(s,te)-f_0)/t\) has a removable singularity at zero.
The maximum principle on circles of radius \(t'<R_f\) bounds it by
\(\omega_f/t'\). Let \(t'\uparrow R_f\), then take the supremum over
directions. The proof requires a change to PAN's stated hypothesis;
it does not assert its original absolute bound for kept forms. ∎

**Lemma 5 (a guaranteed screened radius).** Use Theorem 4's hypotheses for
a carried term. With \(D_f\) measuring distance to the **full** source
carrier of (14), put
\[
 \begin{split}
 c_{\rm cap}&=\min\{s_D/4,\ C_Aa_{\rm ch}/4,
               \epsilon_{\rm lev}/(8K_{\rm pin}C_DE_{\bar\kappa})\},\\
 R_{\rm cap}&=c_{\rm cap}/(c_TC_Ae^{\bar\kappa}g),\qquad
 R_f^{\rm scr}=\min\{R e^{\mu D_f/4},R_{\rm cap}\}.
 \end{split}                                                    \tag{16}
\]
Further decrease \(\gamma\) so that \(R_{\rm cap}\ge R\) and
\(3C_A\delta_0<c_{\rm cap}\). Then Theorem 4 holds on
\(\mathbb D_{R_f^{\rm scr}}\), with the same bounds, and
\[
 \frac{R}{R_f^{\rm scr}}
 =\max\{e^{-\mu D_f/4},R/R_{\rm cap}\}
 \le e^{-\mu D_f/4}+R/R_{\rm cap}.                           \tag{17}
\]

*Proof.* For this radius, \(C_Ac_Tge^{\bar\kappa}R_f^{\rm scr}\le c_{\rm cap}\).
The source, raw chart and global levelling budgets follow directly from
the three entries of (16) and \(3C_A\delta_0<c_{\rm cap}\).
Use the second inequality of (12) in (15). The stored part costs at most
\(r_*/8\); the fluctuation part costs at most \(r_*/8\), because
\(R_f^{\rm scr}e^{-\mu D_f/4}\le R\). The remainder of Theorem 4's proof
is unchanged. The new ceilings follow from \(g\ell^q\to0\).
The equality in (17) is the reciprocal of a minimum. ∎

**Outstanding — the proposed PAN consequence.** Lemma 5 does not prove the
draft's replacement of PAN Lemmas 7.4–7.6. First, \(\mathcal S_{\rm src}\) contains
\(\operatorname{supp}S(v_0)\), which can meet the stored region near the
activity. PAN's G-gap separates that activity from the *integrated* source;
it does not show \(D_f\ge10LM\check R_i-C\) for this full source.
The subtraction in (5) cancels at zero, but the triangle bound (14) does not
localize an increment to the support of the source difference.
One needs a spatial difference-response estimate about the nonzero stored
source, with compatible pinning, or another argument.

Second, even with a free-source distance supplied, dropping PAN's age factor
does not preserve its sums as written. A kept/island amplitude may contain
\(\ell_m^\tau\) at its creation level. The cap term gives
\(C g\ell^q\ell_m^\tau\), not \(C g\ell^{q+\tau}\).
At fixed current \(\theta_{i-1}\), frames allow
\(\theta_m=\theta_{i-1}+b(i-1-m)\),
\(\underline\lambda\le b\le\bar B\), with arbitrarily large age.
Thus \(\ell_m\) is unbounded. The proposed upper bound does not control
those amplitudes uniformly. A retained age gain is required.
Finally, \(R_{\rm cap}\) caps this *guarantee from the imported domains*;
it is not an upper bound on the maximal analytic continuation of \(F_f\).
No singularity at that cap has been proved.

**Lemma 6 (the draft's radius obstruction fails its interface).** The activity
in draft Proposition C does not satisfy ST1's real-tie condition.

*Proof.* Its formula uses
\[
 B(P)=i^{-1}\Log\bigl(\mathcal M(\mathbf U)(c_0)
                             \mathcal M(U)(c_0)^{-1}\bigr),\quad
 f(P)=b_f\frac{\operatorname{Tr}(B(P)^2)/(8\rho_D^2)}
                   {1-\operatorname{Tr}(B(P)^2)/(8\rho_D^2)}.
\]
Take a sufficiently small flat commuting configuration \(W\), with a
nonidentity averaged bond at \(c_0\), and independent current zero.
For example constant links \(e^{itT_3}\) in one direction have average
\(e^{iLtT_3}\) in that direction. The pair \((W,0)\) has real splittings
\((U,A')=(W,0)\) and \((I,(i\eta)^{-1}\Log W)\).
Both are admitted for sufficiently small nonzero \(t\) in the finite chart.
The first gives \(B=0\), hence \(f=0\); the second gives \(B\ne0\) and
\(\operatorname{Tr}B^2>0\), hence \(f\ne0\). ST1 §1 requires equality.
Simultaneous gauge invariance does not repair this dependence on the splitting. ∎

**Outstanding:** the claimed full-interface counterexample under
\(r_\iota=\alpha_\iota\epsilon_m\) must be replaced. Its one-variable pole
argument is correct for its test function, but the test function is inadmissible.
Tq is a sufficient design here; its necessity for actual NL1 activities is
not proved. A bound on a smaller domain alone supplies no extension theorem.

## 4. CI reduction

**D4 — CI and formation.** CI at a structure \(\sigma\) means that every
activity formed there is defined on the full specified chain domain
\(\mathcal D_{a|\sigma}\), with its bound and the complete H-ACT interface.
The domain includes continuation, gauge witnesses and stored-slot clauses.
Activity amplitudes may be chosen after \(M,\bar\kappa\); they cannot feed
any constant that was required earlier. This is the dependency rule used here.

For a formation formula, **local normal domination** means the following.
On each fixed-real-factor fibre, also including the declared holomorphic
stored variables, it has a representation
\[
 f(P)=\sum_\nu\int G_\nu(P,\xi)\,d\mu_\nu(\xi),\qquad
 \sum_\nu\int\sup_{P\in K}|G_\nu(P,\xi)|\,d\mu_\nu(\xi)<\infty
 \tag{18}
\]
for every compact polydisc \(K\) in that fibre. Use fixed positive
\(\sigma\)-finite measures, placing all external-parameter dependence in
\(G_\nu\); the displayed supremum has a Borel
integrable majorant. Integrands are holomorphic in those parameters and
jointly Borel in the remaining variables. Contour and normalization identities
must first justify such a representation when the original Gaussian varies.

**Theorem 7 (conditional CI induction).** Order the structures of a finite
history. Assume:

1. **CI-base:** all initial activities satisfy CI, on their specified initial
   domains. Bare Wilson plaquette functions satisfy their holomorphic clause;
   other initial factors and bounds are included in this assumption.
2. **CI-maps:** at each main step, Theorem 4's hypotheses other than the old
   activity bounds hold uniformly on every fibre of the entire new chain
   domain. The substitution maps take values in earlier activities' domains.
   At stages and outputs supply the corresponding admissible, holomorphic,
   local maps on their own required fluctuation domains.
3. **CI-Gauss:** on these full complex domains the actual precision/comparison
   package holds. This includes the actual matrices, normalization, heredity,
   wall factorization and early uniform envelope of frozen IN1 **H-M**;
   a real-background inverse alone is insufficient.
4. **CI-form:** NL1/LF1's actual formation formulas on the *whole new domain*
   are built from these maps and earlier activities. Given their bounds and
   CI-Gauss, the formulas have (18) and return the required \(b_f\), or the
   stated oscillation/one-sided bound. They preserve realness, real ties,
   gauge covariance, restriction consistency, and the near/far stored-slot
   rules. Branches and formulas agree on overlaps of fibre charts.

Then CI holds at every structure. For main steps, Theorem 4 supplies the
fluctuation holomorphy and old-factor bounds used in CI-form.

*Proof.* Induct over the finite ordered history. At a main step, CI for old
activities supplies the bound and interface for the carried factors; the term identifications in H-ACT come from CI-maps. CI-maps and Theorem 4
give their jointly holomorphic admitted compositions. At a stage or output,
use the separately supplied maps. CI-Gauss and CI-form then give (18) and
the new activity bounds at every point of the entire new domain.

To prove holomorphy, fix a compact polydisc. Its majorants permit integration
of Cauchy's formula for each integrand; the resulting integrals are
holomorphic on the interior. Equation (18) gives locally uniform absolute
convergence of their series, so Cauchy's formula also passes to the sum.
The same majorants give continuity. Thus the sum is jointly holomorphic.
Reality and the required identities pass through the integrals and sums by
CI-form; Borel dependence follows from joint measurability and limits.
Overlap agreement defines the activity on the full domain. This proves the
inductive step and, with CI-base, the theorem. ∎

**Outstanding — what this reduction does not supply.** The draft's CI-form
states a pointwise output bound and then infers (18). That inference is
invalid: cancellation in a bounded sum does not bound the sum of absolute
integrands. For example, the constant holomorphic terms
\((-1)^{n+1}/n\) have a bounded convergent sum: pair them to obtain
\(1/[2n(2n-1)]\le1/[n(n+1)]\). Their absolute series diverges, since
each dyadic block of the harmonic series has sum at least \(1/2\).
The actual locally normal
Mayer estimate, and LF1's external-parameter-independent Borel domination,
must be supplied. Frozen IN1 H-SF/H-E expressly retain these obligations.

The main-step theorem cannot be applied at every structure. At a stage of
level \(j\), ST1 (18) gives
\(w(j)=\beta_sr_0(j)/(16N(\theta_j))\). Applying the same norm budget to
a free box of radius \((\log\theta_j)^q\) costs
\(C E_{\bar\kappa}N(\theta_j)/C_0\), which is unbounded as the coupling
decreases. The existing real-stage estimate instead uses the smaller
amplitude \(\delta'_j\), as Lemma 1 explains. CI-maps therefore needs a
stage-specific box or a stronger response/margin result. Outputs have their
separate BOX maps and budgets.

Nor does a bound on \(f\circ\Pi\) establish CI without a covering argument.
For example \(f(z_1,z_2)=(2-z_2)^{-1}\) is bounded on the image
\(\Pi(t)=(t,0)\), but cannot extend to a domain containing \(z_2=2\).
This illustrates the missing inference, not a dimension count for the actual
ST1 map. Theorem 4 already *uses* the appropriate activity-domain inclusion.

Thus CI remains outstanding through CI-maps, CI-Gauss and CI-form, including
their full-domain identifications. Complex layered precision (the draft's
PR-lay) is one input, not the only identified obstruction. The fixed-real
source family (5) must also be identified with the actual formation rule at
complex external pairs; holomorphy alone cannot supply that identity.

## 5. Source checks and supplied definitions

All upstream locators below refer to `31a47c543775` in
[Sussman–Alpoge's repository](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/31a47c543775).
SA is `YM4_sketch_500.tex`; CA-I/II/III are
`theorem_0_complete_account_raw_I.tex`, `_II.tex`, `_III.tex`; YM3 is
`YM3/YM3_I.tex`. Each was fetched once. The outline index's neighbouring
rows and obligations, and the CA-I 4.12–4.19 index, were consulted before
bounded source reads. The table checks the draft's source quotations and
the passages used here; it does not import entire chapters as proofs.

| Source lines checked | What they support, and their limit here |
|---|---|
| SA 4006–4012 | B4's product box varies sources and couplings. It is not the free-fluctuation polydisc (1). |
| SA 4863–4885; 5999–6048 | The norms use specified pair domains; the running analytic radius at 6033 is Tq. The running minimum and the independent current are retained. These formulas do not identify ST1's domains with SA's. |
| SA 5762–5825; 10354–10410 | R9 specifies joint source/switch holomorphy, response bounds and component splitting; the later contraction discussion relies on its operator estimates. H-DR names the precise source ball, current bound and row reads needed here. |
| SA 6143–6158; 6180–6214 | The raw lift, boundary origins and hull convention, class bounds and reality are present. Domain inclusions are expressly analytic hypotheses at 6155–6158. Removing a lift does not prove those inclusions. |
| SA 14276–14412; 14518–14560; 14640–14657; 14730–14811 | UM assumes the actual potentials' holomorphy and actual Gaussian/structural package. It derives positive activity/logarithm majorants conditionally, and uses them for normal convergence at 14763–14766. This supports the strengthened CI-form, not a deduction from an isolated pointwise output bound. |
| SA 15150–15174; 15721–15745; 15784–15820 | The response/window radius is scalar amplification of size \(\alpha/\delta\). The response-bracket coefficient may lose \(e^{-C\bar\kappa}\). Membership is an input, not proved by the ensuing Cauchy estimate. Equation (8) compensates such a late loss without changing \(c_R\). |
| SA 17518–17542; 17550–17564; 17648–17654 | The strip, its Jacobian, carried elimination factors, kept forms and drop-out allocation have the stated roles. The kept-form oscillation is stated at 17564. These passages do not supply all H-ACT bounds, branches or domains. |
| SA 17270–17278; 17797–17831 | Island bounds use a fixed creation domain and a supremum inside the stored-variable integral. The real/oscillatory splitting is described. The required later ST1-domain inclusion is not a consequence of having the same radius table. |
| SA 17882–17936; 17982–17997 | The shell weight difference is \(O(k-j)\) at 17888. This is not the draft's claimed uniform \(C_x(1+\check R_i)\) local decomposition. The walk argument, the stage factor \(N_k\), and healed/boundary filing are present; their domain hypotheses remain necessary. |
| SA 19466–19493 | Radius coefficients and class amplitudes follow \(M,\bar\kappa\); uniform coupling ceilings are legitimate in that order. The draft's \(q-p_0>Cr\) locator is **19490**, not 19491. Frozen IN1 supplies the more explicit early-package order used here. |
| CA-I 48527–48578; 49495–49546 | The four witness families have their specified, differing exponents. Inclusion of the actual backgrounds and later drop-out domains is explicitly outside the operator theorem's implication. Tq0 removes a multiplier comparison, not these obligations. |
| CA-I 54280–54296; 54985–55005 | The shifted background is prescribed in the stage recursion. The preparatory boundary theorem assumes the stage theorem and its profile-class extension; it is not a proof of the new complex stage maps. |
| CA-II 79910–79965; 79979–80013 | The displayed exponent has the carried-background and coupling-profile brace. The stored/free split is at **79996–79997**, not 80003–80006; \(z^{(k)}\) precedes the integral at **79985**, not 79990. The derivation is attributed to Bałaban and expressly not reproduced at 80010–80011. No W-in locality/zero-order theorem follows just from this display. |
| YM3 39230–39246; 39296–39309; 52573–52588; 53550–53565 | The field domain has matrix radius \(C_{\mathcal A}\mathfrak b\), the interpolated potentials are holomorphic there, the conditional Gaussian uses the hull product of masked switches, and the actual field fits a half-box under its stated constant inequality. This is a three-dimensional analogue, not a four-dimensional radius proof. |
| CA-III 111381–111402 | Its own inventory marks the stage/domain/continuation items listed there as having incomplete proofs. No discharge of H-ST or CI is inferred from that inventory. |

Definitions supplied or made explicit in this distillation are:

1. The coordinate polydisc and matrix comparison (1); cube/row ownership,
   the two adjacency conventions, the mask and complete read carriers (2).
2. The Tq/Tq0 replacement on frozen records, its early lift-exponent budget,
   and the distinction between the comparison weight \(w(i)\) and an actual gap.
3. The unscaled stored datum \(v_0\), its separate bound \(\delta_0\), the
   full source carrier, and the centred response followed by one total pin (5).
4. The exact source-ball and row-locality interface; the W affine reads,
   vanishing orders and carrier range; and the oscillation/one-sided versions
   of the activity bound. These definitions carry the stated extra hypotheses.
5. The budget constants \(C_Q^{\rm L},B_L,A_V,Q_f\), the guaranteed screened radius
   and its source/chart/levelling cap (16). No maximal continuation radius
   is defined by that cap.
6. Full-domain CI, the distinction between main/stage/output maps, and local
   normal domination with fixed measures, Borel majorants and chart agreement
   in D4 and Theorem 7.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/nl1-L-gate.md` (Claude fresh session, first failing step none):
1. ST1 is cited as the distilled [st1-r3.md](st1-r3.md). **Scope note:** Theorem 4 is stated for the lift-free branch Tq0, which st1-r3 supplies in full (st1-r3: lambda = 1 under SA's table). The Tq-with-lifts branch rested on the round-3 draft's Lemma 11', which st1-r3 does not use, and is withdrawn. Displays numbered (56), (59), (60) in the text refer to the round-2 numbering; read them as the corresponding st1-r3 displays.
2. The full source carrier is renamed S_src; SA's label in d-natural(S; X) is unchanged.
3. The new budget constant is renamed C_Q^L, distinct from ST1's AV/CURV constant and PAN's C_Q(M).
4. The local floor L >= 13 is subordinate to frozen IN1's row-2 floors.
5. H-DR row locality now says the response on a face-component's bonds and stencils depends only on its switches and source rows (SA 5797-5801).
6. Theorem 7's proof wording: CI gives the bound and interface; CI-maps gives the term identifications.

**Status: frozen (Tq0 branch).** Reopens only on a `wrong` signal or when an import it reads changes.

## Result

Theorem 4 proves **conditional main-step input (L), with oscillation L6 and
\(c_R=1\)**. Lemma 1 supplies the Tq formation comparisons, including the
conditional scalar-core and lift-free alternatives. Lemma 5 supplies a
capped *sufficient* screened radius. Theorem 7 proves CI by finite induction
under its strengthened formation hypotheses.

The imports are H-ST's named geometric, background, inverse, derivative,
profile, gauge and domain packages; H-FL's actual completed-source map and
stored bound; H-DR's complex source/current estimate and row locality;
H-ACT's exact term presentations, bounds, branches and domains; and the
global lift/test and W hypotheses of Lemmas 1 and 3. CI additionally imports
CI-base, the full-domain main/stage/output maps, frozen IN1 H-M for the actual
Gaussian family, and CI-form's normal domination and identities. Frozen IN1
H-SF/H-E remain formation/envelope obligations. Frozen P82 does not establish
the complex package, and this text does not establish PAN, AG or the
(CL)(P) input retained in frozen [TP1](tp1.md)'s hypothesis AG.

Every substantive correction or proposed correction in the draft has the
following disposition; none changes another library file.

| Draft claim or proposed correction | Disposition in this text |
|---|---|
| ST1 needs Tq; Proposition C proves necessity | Tq gives the stated sufficient budgets. Necessity is withdrawn: Proposition C violates the real tie (Lemma 6). Fixed prefactors and the raw lift alone do not improve the available logarithmic estimate, but that is not a nonextension theorem. |
| Every ST1/round-3 theorem survives verbatim | The homogeneous substitution estimates and formation comparisons survive **conditionally** (Lemma 1). Actual-history inputs, absolute envelopes and changed activity domains are retained. The early exponent budget is fixed before choosing \(q\), not returned later. |
| Outstanding R and the lift can be removed under Tq | The scalar-infimum and Tq0 formation comparisons are correct under the global raw-lift/profile/gauge hypotheses. Round-3 R0 uses Tε and does not refute them. Raw tests still carry their lifts; intrinsic/R5, witness, gauge and continuation comparisons are not proved. |
| Scalar ST1 holomorphy supplies the free complex source | Correctly rejected by the draft. H-DR is the stronger necessary import for this proof. H-FL's stored raw bound and physical map identification are also explicit; round-3 F8 does not silently discharge them. |
| Masking and centring give L3 and L5; \(c_R=1\) is early | Correct under the exact row locality and full read-carrier hypotheses. Equations (8)–(15) retain every parameter loss in late \(C_0\) or coupling ceilings. |
| Oscillation L6 suffices for PAN | Correct at the Schwarz/recentring step (Corollary 4.1). PAN Lemma 5.3(a)'s hypothesis must be amended. The real-centre island formula is not used at complex external pairs. |
| PAN's screened radius needs a cap, but its theorem survives without the age factor | The cap and decay-rate losses yield Lemma 5's guarantee. A maximal-radius upper bound and the PAN closure are withdrawn: full-source distance is not free-source distance, and old logarithmic amplitudes still need age control. |
| PAN §4.1 asks no more than the usual field box | The draft's correction is right. B4 is a source box; YM3's field radius is proportional to the window; scalar response amplification is a separate input. |
| W follows locally from the cited Bałaban display | Retained as an extra presentation hypothesis. Corrected the stored scaling to \(\delta_0+c_TgR\) and imposed the separate diameter floor \(M>2R_W+2\). Its amplitudes remain supplied constants: in particular [c4-order](c4-order.md), row 20, does not place \(C_x\) before \(M\). |
| CI follows from pointwise CI-form and PR-lay is its first sole obstruction | Replaced by Theorem 7: normal domination, actual complex Gaussian/structural data, the entire target domain, chart agreement and separate stage/output maps are necessary. A pullback bound is not a full-domain bound; a dimension-count assertion about the actual map is not needed. |
| CI's amplitude order is literally false for SA's class | The useful clarification is that early constants must not read late amplitudes. The asserted contradiction is withdrawn: round-3 CI already permits declared later amplitude factors, and a later choice of a bound alone does not prove that an earlier bound is impossible. |
| Source locators and claimed discharge of the seven kinds | Corrected the SA/CA-II locators listed above; separated their displayed formulas from the extra strip, logarithm, kept-form, island and W hypotheses. The frozen imports replace the draft's older IN1 shorthand. |

This is a research manuscript, **not yet refereed**. It grants no scientific
or audit status and does not claim unconditional input (L), CI or four-dimensional
Yang–Mills construction.


*Referee status (lead, 2026-11-05): refereed line by line by a fresh Claude session; see the change log above and `gates/nl1-L-gate.md` (st1-r4: `gates/st1-r4-gate.md`). The "not yet refereed" sentence in the Result above predates that check.*
