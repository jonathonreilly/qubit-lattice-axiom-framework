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

### R4. §8.4, one-step map, holomorphy, cancellation, (8.3) — ADVANCE

**Definitions,** checked against SA 7065–7096:
- the contour family \(\mathcal G(y,x)\): at most \(4!\) coordinate-ordered shortest paths, inside \(B(y)\) for centred blocks;
- the Federbush mean;
- the block average \(\mathcal M(U)(c)=\exp(L^{-4}\sum_x\log W_x)U[c]\), with \(W_x=U(c_-,x)U([x,x'])U(x',c_+)U[c]^{-1}\);
- the block factor \(\mathsf u(y)=\exp(L^{-4}\sum_x\log[\mathbf W(y,x)W_0(y,x)^{-1}])\), with \(e^{i\mathcal Q^1}\mathcal M(W_0)=\mathsf u(c_-)^{-1}\mathcal M(\mathbf W)\mathsf u(c_+)\).

§8.4's gauge \(g(x)=W_0(y,x)^{-1}v_y^{-1}W(y,x)\) gives \(W^g(y,x)=W_0(y,x)\) and \(\mathcal M(W^g)(c)=v_{c_-}^{-1}\mathcal M(W)(c)v_{c_+}\). This is the outline's straightening, with \(v=\mathsf u\).

**Tree gauge.** Each non-tree link is a product of at most \(C_L\) conjugated plaquettes, and \(\|\prod g_k-1\|\le\sum\|g_k-1\|\) for unitaries.

**Mean.** Write the defining equation as \(v=f(v,z)\) with \(\partial_vf(0,0)=0\). On a fixed ball, \(\|\partial_vf\|\le\frac12\) and smallness of \(f(0,z)\) give a unique fixed point, holomorphic as a uniform limit. Cauchy's formula on a smaller ball bounds the derivatives of order \(\le3\). Uniqueness near a family that is not near 1 follows from the right-invariance of \(\sum\log(V_\gamma V^{-1})=0\). This is the "uniqueness of each finite step" that P82 Lemma 3.2 uses.

**Cancellation at 1.** \(d\mathcal M=\mathsf Q^{\rm pl}=\sigma(c_-)+\mathsf Q^{\rm s}-\sigma(c_+)\) (SA 7086) and \(d\log v_y=\sigma(y)\), so the straightened derivative is \(\mathsf Q^{\rm s}\), the straight-segment average.

**Row and column sums.** Row: \(L^{-4}\cdot L^4\cdot L=L\). Column: a fine bond \((w,w+e)\) lies on exactly the \(L\) segments with \(x=w-te\), \(t<L\). These lie in at most two blocks, with weight \(L\cdot L^{-4}=L^{-3}\). Bonds in other directions are not read.

**(8.3).** Apply the mean value theorem to the finite-dimensional holomorphic Jacobian. The entries move by at most \(C_L(q+u)\), and each row and each column has at most \(C_L\) entries. The factors \(L\) and \(L^{-3}\) are absorbed into \(C_L\). P82 uses only the case of reference \(e^{ib}\) with \(a=0\), in the given gauge and without a tree gauge.

### R5. §8.5, read width, exact composition, value recursion, (8.7), (8.9) — ADVANCE

**Read width.** Step \(m\) adds at most \(c_Ls_m\), and \(\sum_{m<j}s_m\le s_j/(L-1)\). With \(\rho>4(a_L+2)L\) and \(\operatorname{dist}(\Omega_j,\Omega_{j-1}^c)>\rho s_{j-1}=\rho s_j/L\), every read set lies in \(\Omega_{j-1}\subset\Omega_0\), so the local scale there is at least \(s_{j-1}\). The un-enlarged functional reads only the final double block, because level-\((m+1)\) blocks are unions of level-\(m\) blocks.

**Composition.** Suppose \(\mathcal M^m(e^{i\eta A}U_0)=v_me^{ia_m}W_mv_m^{-1}\). Covariance of \(\mathcal M\) at block centres and the one-step identity \(\mathcal M(e^{ia}W)=\mathsf v\,e^{iS_W(a)}\mathcal M(W)\,\mathsf v^{-1}\) give the identity at level \(m+1\), with \(v_{m+1}=v_m|_{\rm new}\mathsf v_m\). This is the outline's SA 9632–9634, so \(a_j=\mathcal Q^{\rm st}_j(A)\) by definition.

**Value recursion.** \(a_{m+1}=\int_0^1S'_{W_m}(ta_m)a_m\,dt\), bounded by the row norm in (8.3). Assume the bootstrap \(u_m\le2LrL^{m-j}\). The product of the correction factors is then \(<\frac32\), which improves the bootstrap to \(\frac32LrL^{m-j}\).

**(8.7).** By the chain rule, \(D_{a_0}a_j\) is a product of block-sparse matrices on the union of the read sets. Row and column norms are submultiplicative. Column sums run over all rows of one height, and deleting rows only lowers them.

**(8.9).** \(\|\mathsf v_m-1\|\le C_Lu_m\), then product telescoping. Units: \(\eta L^j=s_j\) and \(\eta L^{-3j}=\eta^4s_j^{-3}\), which matches P82 (4.1).

**Reading by heights.** A fine bond in layer \(l\) is read only by rows of height \(l\) and by outward rows of height \(l+1\). For a top \(y\) of layer \(j\), \(B^j(y)\) lies in layer \(j\), and an outward row's outer block \(B^j(z)\) lies in layer \(j-1\). This is the bounded number of heights in P82 Lemma 4.1(ii).

**What P82 uses.** P82 uses only the identity-reference case: \(q_m=0\), \(W_m=1\), \(a_0=\eta A_0\) with \(\sup m|A_0|\le\delta\). There the curvature recurrence (8.5)–(8.6) is not needed.

### R6. §8.6, (8.10) — ADVANCE

With \(u(c_-)v_j(c_-)=1\), \(u(z)v_{j-1}(z)=1\) and \(v_j(z)=v_{j-1}(z)\mathsf v_z\),
\[
\mathcal M^j((e^{i\eta A}U_0)^u)(c)=e^{i\mathcal Q^{\rm st}_j(A)(c)}\mathbf V_0(c)\,v_j(z)^{-1}v_{j-1}(z)=e^{i\mathcal Q^{\rm st}_j(A)(c)}\mathbf V_0(c)\,\mathsf v_z^{-1}.
\]
This equals \(e^{iB(c)}\mathbf V_0(c)\) exactly when (8.10) holds.

**Why \(\mathsf v_z\) is a function of \(B\) alone.** \(\mathsf v_z\) reads the level-\((j-1)\) data in \(B(z)\). The block \(B(z)\) lies in layer \(j-1\), because \(\Omega_j\) is a union of level-\(j\) blocks and \(\rho s_{j-1}>2s_j\). Those bonds are interior rows, where \(\mathsf b=B\).

The inverse is triangular, the map is locally holomorphic, and \(\sup|\mathsf b(B)|\le C_L\sup|B|\). The formula is verbatim the outline's reduced datum, SA 9644. The linearised outward constraint is \(K\) with data \(D\mathsf b\cdot\delta B\): it has the same kernel, and the change of data is triangular and invertible. This is how P82 takes \(K\) at outward rows.

### R7. §8.7, (8.11)–(8.12) — ADVANCE

**Setup.** Redone at the identity reference in one fixed real gauge: \(\mathcal M^mU_0=t_me^{ib_m}t_m^{-1}\), with \(|b_m|,|z_m-1|\le C_L\delta L^{m-j}\) and \(|t_m-1|\le C_L\delta\).

**Covariance.** \(S'_m=\operatorname{Ad}(t_m)|_{m+1}(Q_0+E_m)\operatorname{Ad}(t_m)^{-1}|_m\), where \(\|E_m\|_{\rm row}/L\) and \(\|E_m\|_{\rm col}/L^{-3}\) are at most \(C_L\delta L^{m-j}\), by (8.3) at reference \(e^{ib_m}\). At level-\((m+1)\) sites \(\operatorname{Ad}(t_{m+1})^{-1}\operatorname{Ad}(t_m)=\operatorname{Ad}(z_m^{-1})\), because \(t_{m+1}=t_mz_m\) there.

**(8.11).** Replace one factor at a time. The \(m\)-th term has row norm at most \(L^{j-m-1}e^{C}\cdot LC_L\delta L^{m-j}\cdot L^m\), and these sum to \(C_L\delta L^j/(L-1)\). Columns are the same with \(L^{-3}\). The output factor \(\operatorname{Ad}(t_{j-1})\) at \(c_-\) is within \(C_L\delta\) of 1.

**(8.12).** \(Q'_j\) is built from \(\mathsf T_j(y,x)\), the product of the level-wise mean transports (SA 10670, (PX31)).
- With the same \(t_m\), the intermediate factors are \(z_m^{\pm1}\), so \(|\mathsf T-1|\le C_L\delta\).
- Pillars of one height are disjoint, and each has \(L^{4j}\) sites of weight \(L^{-4j}\).
- Hence the row norm is at most \(C_L\delta\) and the column norm at most \(C_L\delta L^{-4j}\).

**Flat comparator.** \(K_1=\eta Q_0^j\) is the length-\(L^j\) straight-segment average over the pillar, because \(t'L+t\) runs once through \(0,\dots,L^2-1\); checked.

**Outward rows.** At outward rows, and at rows near the outer edge of layer \(j\), the read set reaches layer \(j-1\), where the gauge bound is \(L\delta/s_j\). That is a factor \(L\), absorbed.

## Remarks that break nothing

1. **Output factor in P82 Lemma 4.2.** P82 writes it as \(\operatorname{Ad}(t_j)\). In the product it is \(\operatorname{Ad}(t_{j-1})\) at \(c_-\), that is \(\operatorname{Ad}(t_j)\operatorname{Ad}(z_{j-1}^{-1})\). Both are within \(C_L\delta\) of 1, so nothing changes.
2. **Statement of (7.19).** It does not fix the ratio of the inner cube to the larger one; any fixed ratio works with the same proof, which covers P82's ratio 2 (R3). Its value half holds at every real \(U\), with no gauge hypothesis.
3. **Which mean in §8.4.** §8.4 says "block mean" without saying which. The outline's block factor is the exponential of the mean logarithm (SA 7092). Both choices are finite analytic, with the arithmetic mean as derivative at 1, so the cancellation and (8.3) are unchanged.
4. **Outside this gate.** The following are not read by P82 and are not gated here; this gate asserts nothing about them:
   - (3.3) and the complex paragraph of §3;
   - (5.6), which was checked in passing and is correct;
   - the curvature recurrence (8.4)–(8.6) and the Cauchy bounds (8.8);
   - the complex-reference, regular-pair and Ward-identity paragraphs of §§8.4 and 8.7;
   - (7.20)–(7.21), §12 beyond (12.1), and §§9–14.

## What this moves, and what stays open

**Moves.** Row 101 is closed: every `a3-balaban.md` statement listed under "Exact reads" in `gates/p82-curved-gate.md` passes one cross-provider read, with first failing step none and no repair needed. Together with rows 99 and 100, P82° Theorem P(a)–(f) at real references of the class (Reg\(_\alpha\)) is an implication each of whose inputs has had one read by another provider. The lead can drop row 101 from the open list of the real-critical A3 obligation; `p82-curved.md` and its gate stand as written.

**Stays open on that obligation** (unchanged by this gate):
- membership of the critical reference \(U_0\) in (Reg\(_\alpha\)): this is row 81's premise \(U_0\in\mathcal U_k\), CMP 99a (1.7)–(1.9), whose (1.9) goes beyond plaquettes;
- A1's pointed-core admission (10.2);
- 2.8's joined-family identification (G1);
- M1 weight matching and the consumer identification kept by `gates/a3-derivative-gate.md`;
- complex references, the independent current (M2) and the periodisation clause.

## Method

- **Checks.** Every check above was done by hand. No numeric or symbolic computation was needed, so the numeric lock was not taken and `memory_pressure` was not consulted.
- **Sources.** The outline was fetched once by URL into a private scratch folder and read as data with `sed` and `grep`. Bałaban's papers were not opened: the reads' proofs are self-contained, and their Bałaban citations are credit, not proof steps.
- **Housekeeping.** No subagent was used. Only this gate file was written. No commit, push, PR or post.
