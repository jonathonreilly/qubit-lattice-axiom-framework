lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T10:23Z

# Gate: the `a3-balaban.md` reads of P82° (queue row 101)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session; branch `claude/ym4d-hard-route` at `9aa9759b4`; Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (sha256 `d7f77d4d…4d6f`, the hash recorded in `library/p82-curved.md`). Gate by hand of a Codex text (`library/a3-balaban.md`, written by OpenAI Codex) as read by a Claude text (`library/p82-curved.md`), with the list of reads fixed by a Codex gate (`gates/p82-curved-gate.md`, "Exact reads"). Same provider as the consumer, different provider from the gated text. One read, not an audit; grants no status.

Credit. T. Bałaban for the averaging, straightening and background-propagator architecture these lemmas port (CMP 98, 99, 102). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's contour mean, block average, straightened rows, block factors, reduced datum, pillar mean, layer metric \(d_{\mathbf B}\) and its ball count (PX4)–(PX10). OpenAI Codex for `a3-balaban.md` and the P82 gate. Claude for `p82-curved.md`.

## Verdicts

Scope is exactly the gate's "Exact reads" table, including its (12.1) row, which the (7.19) proof uses. Each item was redone line by line; the checks are in the next section.

| Item | Read by P82 at | Verdict | First failing step |
|---|---|---|---|
| R1. §3 (3.1)–(3.2): \(R\) is the orthogonal projection onto \(\ker(Q_sS)=\Delta\ker Q_s\); Gram matrix positive | Section 3, Lemma 3.1, Theorem P(a) | ADVANCE | none |
| R2. §5 (5.1)–(5.5): collar crossings, scale comparison, ball count, weighted sum | Theorem P(b)–(d), at \(p=0\) | ADVANCE | none |
| R3. (7.19), value and gradient proof, with its inputs (12.1) and Lemma H | Lemma 6.1 steps (1)–(2) | ADVANCE | none |
| R4. §8.4: one-step map, holomorphy, cancellation at 1, (8.3) | Lemmas 3.2, 4.2 | ADVANCE | none |
| R5. §8.5: read width, exact composition, value recursion, (8.7), (8.9) | Locality, Lemmas 3.2, 4.2 | ADVANCE | none |
| R6. §8.6: outward reduced row (8.10) | Section 3 (which \(K\)), Lemma 4.2 | ADVANCE | none |
| R7. §8.7: (8.11)–(8.12), common-gauge comparison with the flat rows and pillar means | Lemma 4.2, hence 4.1, 5.1 | ADVANCE | none |

**First failing step: none.** No defect breaks a statement P82 reads. Four non-breaking remarks are in the last section but one.

## Checks

### R1. §3, (3.1)–(3.2) — ADVANCE

Hypotheses: \(A_s=\Delta+Q_s^*aQ_s>0\), \(Q_s\) onto, \(a>0\) diagonal on tops. Every adjoint is taken in the fixed fine and top pairings, so \(S=A_s^{-1}\) is self-adjoint. With \(T=Q_sS\), one has \(T^*=SQ_s^*\) and \(TT^*=Q_sS^2Q_s^*\), and \(\langle b,TT^*b\rangle=\|SQ_s^*b\|^2>0\) for \(b\ne0\), because \(Q_s^*\) is injective. So \(N\) exists. The operator \(SQ_s^*NQ_sS=T^*(TT^*)^{-1}T\) is symmetric and idempotent and fixes \(\operatorname{ran}T^*\), so it is the orthogonal projection onto \((\ker T)^\perp\), and \(R\) projects onto \(\ker T\).

(3.2), both inclusions:
- If \(Q_s\lambda=0\), then \(A_s\lambda=\Delta\lambda\), so \(Q_sS\Delta\lambda=Q_s\lambda=0\).
- If \(Q_sSf=0\), then \(\lambda:=Sf\) has \(Q_s\lambda=0\) and \(\Delta\lambda=A_s\lambda-Q_s^*aQ_s\lambda=f\).

P82 uses two consequences, and both are correct. First, \(\operatorname{ran}R=\Delta_U\ker Q'\), and \(\Delta_U\) is injective on \(\ker Q'\) because \(\ker\Delta_U\cap\ker Q'\subset\ker A_s=0\). Second, \(R\) is independent of the positive top weight: \(\Delta\ker Q'\) does not involve \(a\), and orthogonality is in the fine pairing, which \(a\) does not touch. The hypotheses at the curved \(U\) are supplied by P82 Lemma 3.1(i), not by §3. P82 consumes no bound on (3.3) and nothing from the complex paragraph.

### R2. §5, (5.1)–(5.5) — ADVANCE

**Metric.** Checked against SA 9602: \(d_{\mathbf B}\) is the infimum over curves on the torus of \(\sum_{j\ge1}\xi_j^{-1}\,\mathrm{length}(\Gamma\cap(\Omega_j\setminus\Omega_{j+1}))+\eta^{-1}\,\mathrm{length}(\Gamma\setminus\Omega_1)\). This is §5's metric, the outside of \(\Omega_0\) included at bare cost.

**(5.1).** Take a curve of cost \(\le r\) from \(y\) in layer \(i\) that reaches layer \(h>i\), and fix \(q\) with \(i<q<h\). Then \(y\notin\Omega_q\), and the curve enters \(\Omega_{q+1}\). Consider the arc from the last visit to \(\Omega_q^c\) before the first entrance into \(\Omega_{q+1}\) up to that entrance. It lies in layer \(q\), has Euclidean length at least \(\operatorname{dist}_\infty(\Omega_q^c,\Omega_{q+1})>\rho s_q\), and so has cost greater than \(\rho\). The arcs for different \(q\) lie in different layers, so they are disjoint. Hence \((h-i-1)\rho<r\).

The bound holds at every point of the curve, which gives maximum scale \(\le s_iL^{1+r/\rho}\) and Euclidean displacement \(\le r\,s_iL^{1+r/\rho}\). (5.2) follows by reversal, since the metric is symmetric. If \(d\le r\) is attained only as an infimum, apply this with \(r+\epsilon\) and let \(\epsilon\to0\); the level is an integer and the cube is closed.

**(5.3).** At level \(j\) the tops lie on a translate of the \(s_j\)-grid. A sup-norm ball of radius \(R=r\,s_iL^{1+r/\rho}\) contains at most \((1+2R/s_j)^4\le(1+2rL^{2+2r/\rho})^4\) of them, using \(i-j\le1+r/\rho\). Further, there are at most \(3+2r/\rho\) levels, and the scale ratio is at most \(L^{|p|(1+r/\rho)}\). The product of these three factors is (5.3); the constant 3 in place of 1 is a harmless overcount. On the torus, lift along the curve; counting lifted grid points overcounts distinct tops.

**(5.5).** In the shell \(n\le d<n+1\) every top is reached by a curve of cost \(<n+1\), so (5.3) at \(r=n+1\) applies. Under (5.4) its exponential is at most \(e^{\tau(n+1)/2}\), which leaves \(5(5/2)^4L^{8+p_0}e^{\tau/2}\sum_n(n+2)^5e^{-\tau n/2}\). Since \(\log t\le2\sqrt t\) for \(t\ge1\), one has \(5\log(n+2)\le\tau n/4\) once \(n\ge3200/\tau^2\). Beyond that the terms are at most \(e^{-\tau n/4}\), and the rest is a finite sum. The constant depends on \(L,p_0,\tau\) only.

**Use in P82.** P82 reads (5.5) at \(p=0\), \(\tau=\delta_w/2\), with \(\rho_0\ge32\log L/\delta_w\), and that threshold is exactly (5.4). The argument is the outline's own (PX4)–(PX10), SA 10626–10660, which is credited above. (5.6) is not read by P82; it was checked in passing and is correct.

### R3. (7.19), value and gradient proof, with (12.1) and Lemma H — ADVANCE

**Value.** Kato's inequality \(\Delta|u|\le|\Delta_Uu|\) was redone. At \(u(x)\ne0\), pair with \(u(x)/|u(x)|\) and use that \(\operatorname{Ad}U\) is orthogonal for real \(U\). At \(u(x)=0\) the left side is \(-\sum_z|u(z)|\le0\). This half uses no gauge hypothesis.

Comparison: the function \(|u|-(\text{Poisson extension of }|u|\text{ from }\partial Q_\rho)-G_{Q_\rho}|g|\) is subharmonic and vanishes on \(\partial Q_\rho\), so it is \(\le0\). Its two pieces are bounded as follows.
- **Poisson coefficients.** \(P(x,b)=G_{Q_\rho}(x,x_b')\), where \(x_b'\) is the unique interior neighbour of \(b\). By domain monotonicity, \(P(x,b)\le G_H(x,x_b')=G(x-x_b')-G(x-\sigma x_b')\), where \(H\) is the half-space of the face of \(b\) and \(\sigma\) its reflection, with \(|x_b'-\sigma x_b'|=2\). By (12.1) with \(n=1\) this is \(\le Cr^{-3}\) at distance \(\ge r/2\).
- **Green mass.** \(\sum_{x'}G_{Q_\rho}(x,x')\le(R^2-|x-c|^2)/8\), because \(\Delta|x|^2=-8\) for the positive Laplacian.

Shell choice: \(\sum_{\rho=r}^{2r}\|u\|^2_{\partial Q_\rho}\le\|u\|^2_{Q_{2r}}\). With \(\#\partial Q_\rho\le Cr^3\), Cauchy–Schwarz gives \(Cr^{-3}r^{3/2}(r^{-1}\|u\|_2^2)^{1/2}=Cr^{-2}\|u\|_2\).

The statement leaves the ratio of the inner to the larger cube unspecified. The proof works for any fixed ratio, by choosing the shell between the two radii. That covers P82's use with \(Q'/2\subset Q'\), side \(r'\ge16\eta\): there are \(r'/8\eta\ge2\) shells, at distance \(\ge r'/8\).

**Gradient.**
- **Expansion.** The paired-shift expansion \(\Delta_U=\Delta+B\cdot\nabla+C''\) holds with \(|B|\le C|A|\) and \(|C''|\le C(|\nabla A|+|A|^2)\). This was redone: \(A(x,-e)=-A(x-e,e)\) pairs the two shifts, and the exponential remainder is \(O(|A|^2)\).
- **Poisson gradient bound.** The harmonic part is bounded by \(Cd^{-1}\sup|h|\), using Lemma H on differences together with Caccioppoli. For the Green part, (12.1) gives \(\sum_{|z|\le d}(1+|z|)^{-3}\le Cd\) for its gradient and \(\sum_{|z|\le2d}(1+|z|)^{-2}\le Cd^2\) for the boundary values of its harmonic correction.
- **Absorption.** Let \(x_0\) maximise \(d(x)|\nabla u(x)|\), with maximum \(M\), and suppose \(d_0=d(x_0)\ge K\). On the cube of radius \(d_0/4\) one has \(d\ge3d_0/4\). So the drift contributes at most \(C(\delta/r)d_0\cdot(4M/3d_0)\cdot d_0\le C\delta M\), and the zeroth-order term at most \(C\delta(d_0/r)^2\sup|u|\). Absorb these for \(C\delta\le1/2\). If \(d_0<K\), then \(M\le2K\sup|u|\).
- **Covariant gradient.** Finally \(\nabla_U-\nabla=O(|A|)\).

**(12.1).** Redone in two ranges of frequency.
- **Low frequencies** \(|p|\le2/R\): these give \(CR^{-n-2}\).
- **High frequencies:** integrate by parts \(n+3\) times in a coordinate with \(|x_\nu|=R\), using \(|\partial^\beta\sigma_n|\le C|p|^{n-2-|\beta|}\). The boundary terms cancel by periodicity, and the cutoff derivatives scale the same way.

**Lemma H** and its Caccioppoli step are written out in `library/a3-response.md` and were kept ADVANCE by `gates/a3-gate-b2c312b2e.md`. So every input of the (7.19) proof is now gated library text.

Status: in progress (R4–R7 next).
