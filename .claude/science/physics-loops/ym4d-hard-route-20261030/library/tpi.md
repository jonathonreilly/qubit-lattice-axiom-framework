# TPI: the retained free background

Codex, 2026-11-08; checkout `43942f5fe45479712937aef15adb4697f772b83f`.
Research text. Not an audit. This note grants no status.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their source text. Credit Tadeusz Balaban for the free-field method.
All arguments below are written mathematics. No numerical test discharges a step.

## 1. Sources and exact target

`SA` denotes `YM4_sketch_500.tex`, supplied at `31a47c543775`.
`CA-I` and `CA-II` denote `theorem_0_complete_account_raw_I.tex`
and `theorem_0_complete_account_raw_II.tex` at that revision.
`N` denotes `YM4_1400.tex`, supplied at `2bc0658f9`.
The older files are in `/Users/jonreilly/ym4d-lead/sa/`.
The new outline is [YM4_1400.tex](</private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/sa1400/YM4_1400.tex>).
References below are source line numbers.

The prior digest was read first and in full. Its completed algebra is reused.
The source index was consulted before the old outline and account excerpts.
`open-registry.md:501` assigns this join to TP1-FREE, owner TP1.
FINISH row 479 assigns this note its proof lane.
The workflow file named by the repository entry point is absent here.

Fix TP1's odd integer L and compatible torus of physical side
ell = 2 L^m, with m >= m_0. Let a = L^(-K) and a_j = L^j a.
Use one real colour, unit coupling, and one orientation per coordinate plane.
Raw cochains have the counting inner product. Write E = ran d_1.
Let P be the orthogonal projection onto E.

Use the actual plaquette average A_j of SA:7634-7641 and N:4329-4332.
It comes from the centered straight bond average. The plain derivative
has the same induced map on curvature.
Set

\[
 W_j=E\ominus(E\cap\ker A_j),\qquad
 R_j=P_{W_j},\qquad G_j=R_{j-1}-R_j.
\]

The task is the all-level estimate

\[
 R_j(p,p)\le C L^{-4j},\qquad 0\le j\le K.                 \tag{1}
\]

P3:464-470 then gives the required bound on every entry.
The constant must be independent of K, j, torus volume and p.
The terminal R_K remains in the exact decomposition.
The slice estimates and the full-P continuum comparison are prior work.

## 2. Source trace: what is already supplied

SA:7641-7649 and N:4332-4340 give the nested projections and independent
slices. SA:26028-26036 and N:100448-100456 identify
R_j = C^bg_(K,K-j). P3 supplies the finite Gaussian algebra.
That algebra will not be reproved here.

N:101043-101077 supplies the flat comparison of the two quadratic laws.
Its proof removes the constant part of a coarse closed form by a fine
constant. It removes the exact part by a fine gradient. The plain map
uses prescribed center values; the straight map uses prescribed block means.
Normalized integration of the soft contour weight gives a constant on
each curvature fibre. The sharp tree gauge chooses one lift per fibre.
The constant Jacobians cancel. Thus both laws give the same bare slice.
This strengthens the conditional identification in SA:26143-26148.

N:102258-102291 keeps the covariance subtraction at the zero terminal
field. Its G_j is this note's R_j. At N:102280-102281 it invokes
"the coarse covariance bound" for |R_(k_1)| <= C L^(-4 k_1).
No theorem number accompanies that phrase. The supplier trace continues below.

N:100989-101032 proves the curvature lift estimate from its joint strong
inverse, Proposition `prop:hb-joint-strong-inverse`, N:41990-42038.
The setting N:41668-41706 has h = L^(-j), coarse spacing one,
integer torus side at least two, and physical fine pairing h^4 sum.
At zero fine force its solution is

\[
 H_h=K_0^{-1}Q^\sharp(QK_0^{-1}Q^\sharp)^{-1}.
\]

The weighted strong bound controls d_h H_h pointwise.
The source restores raw curvature by multiplying by h^2.
Thus it obtains |Hcal_j(p,b)| <= C h^2 exp(-delta dist(p,b))
in coarse units. Scaling alone is not its argument.

### 2.1. The coarse covariance reference

The exact matching statement in the account is
`8.1:eq-kernel-bounds-a`, CA-II:69958-69965:

\[
 |C^{\rm bg}_{K,s}(p,q)|
 \le C_u\eta^4(1+|x_p-x_q|)^{-4}.                         \tag{2}
\]

Here eta = L^(-(K-s)); positions are in cells of level K-s.
CA-II:70002-70016 assigns (2) to hypothesis (h1), stated at
69927-69929. That hypothesis cites Balaban's minimizer estimates and
the operator theorem at free current. It is an input, as P3 records.
CA-II:69600-69659 also retains the potential and block-law identification.
CA-II:69849-69912 proves the finite tower, conditional on its identification.

The premise trace for this account route is as follows.

| Premise of (2) | Source status | What the account route still requires |
|---|---|---|
| Specified massless potential, block map, and minimizer law | Cited in CA-II:69605-69612 to Balaban CMP 95 (1.3), (1.5), (1.18), (1.19). | H-BG in P3. |
| Identification of the orthogonal tower with the flat RG steps | Finite algebra proved at CA-II:69874-69902; identification invoked as an implication at 69903-69912. | H-TOWER in P3; the newer flat-law proof is ported above. |
| Minimizer kernel bounds | Cited at CA-II:69927-69929,70011-70016 to Balaban CMP 102b, Theorem 1, (9)-(10). | H1-MIN in P3, including its claimed consequence for these kernels. |
| Operator theorem at free current | Theorem stated at CA-I:46035-46156; its proof is assigned to the rest of that section at 46170-46171. | Prepared-nest (A1), (A2), block-size floors and ceilings are explicit premises at 46044-46051. Their admission is not proved by the covariance lemma. |

The last theorem is cited here only to identify the account's premise.
Its full proof and nonlinear admission are not imported into this lane.
The flux and continuum hypotheses (h2)-(h3) serve the later lower bounds;
the displayed proof of (2) assigns its upper bounds to (h1).

N:102280 has no numbered reference identifying an antecedent for its phrase.
The "coarse covariance" formula at N:6223-6230 is the auxiliary potential
covariance FX7. That is a different kernel.
Thus (2) is the precise account statement matching the claimed estimate;
the new sentence alone is not a proof of its application to every j.
The join below proves the weaker bound needed here from N's written
strong-inverse proof. It does not assume (2).

### 2.2. Premises of the strong inverse

The following statuses concern the supplied source text, not an audit.
Only the trivial flat reference and homogeneous periodic geometry are used.

| Premise | Source and status | Scope used here |
|---|---|---|
| Centered rows, physical adjoints, and QD = d_c q | N:41668-41706; definitions and telescoping identity. SA:7634-7641 supplies the corresponding raw curvature identity. | h = L^(-j); coarse side an integer >= 2; fine pairing h^4 sum. |
| Scalar block gap and positive site Gram matrix | Proved in SA:766-844; N:123124-123204. FP1 Lemma 2 gives the same proof. | Unit physical blocks; arbitrary fine subdivision and periodic volume. |
| Scalar exponential cell bounds | Proved in SA:950-1074; N:123310-123433. | Relative form conjugation, with periodic distance. |
| Differentiated heat bounds | Proved in SA:12438-12530; N:24496-24593. N:25131-25169 supplies the pointwise version. | Uniform mesh bounds for time at most one; periodization handles volume. |
| Homogeneous projected Landau gap | Proved in N:25793-26025, especially 25865-26019. The old SA:26141 only sketches this input. | All depths and Bloch phases; no layered or nonlinear admission premise. |
| Exact smooth right inverses of q and Q | Proved in N:41708-41779. | Signed two-moment field seeds; a separate finite-mesh construction includes h = 1. |
| Strong scalar regularization and site-projector smoothing | Proved in N:41781-41941 from the preceding scalar results. | Bounded scalar forcing gives a bounded first derivative. No endpoint Riesz estimate is assumed. |
| Full vector inverse, Schur inverse, and multiplier | Proved in N:41943-42038 from the preceding gap and seeds. | The strong constant is independent of mesh and volume. |
| Removal of the flat gauge penalty and curvature minimization | Proved in N:101007-101019, using N:42043-42061. SA:26133-26148 sketches the earlier route. | Closed coarse forms split into gradients and constants on the trivial torus. |

The gap proof uses compactness on one fixed Bloch cell.
Its uniform first-derivative bound controls the squared L2 Fourier tail by C/T^2
above frequency T. Finite Fourier truncations are compact. This is the
compactness step in N:25938-25983; it requires no numerical spectral test.
The zero-kernel argument at N:25991-26019 covers both fixed meshes
and the continuum limit. Hence the resulting positive gap is uniform.

For the scalar package, the Gram lower bound comes from a smooth mean-one
lift with bounded Laplacian. Conjugating the scalar resolvent also controls
its first derivative in energy norm. Applying the Gram lower bound after
small exponential conjugation gives the inverse Gram's coarse cell decay.
These are the site/Gram bounds used at N:41895-41924.
There is no extra unproved site inverse in this homogeneous specialization.

Balaban's method is cited at SA:26141 and N:100997.
The old centered-block bootstrap at SA:26141 is a sketch.
N replaces it by the written scalar-equation argument above.
The account's stronger input (2) remains cited there.
Neither that input nor the interacting operator theorem is used below.
No Balaban paper was accessed. `lit-balaban.md` is a search record,
not a verification of those papers.

## 3. Port of the curvature lift, with its normalization

Fix a level j. Put n = L^j, h = n^(-1), and rescale a_j to one.
The coarse torus side is

\[
 N_j=\ell/a_j=2L^{m+K-j}\ge2.                              \tag{3}
\]

This is an admitted torus for the source strong inverse, including j = K.
Its parameter called M is this N_j, not TP1's localization size M.
Fix the source Hölder exponent at 1/2 throughout.

Write D_h for the physical fine gradient, d_h for the physical fine curl,
and d_c for raw coarse curl. The coarse spacing is one.
Write R_g for the source's site gauge projection, to distinguish it from R_j.
For a physical fine potential v and raw fine potential w = h v,

\[
 Q_hv=S_nw,\qquad dw=h^2d_hv,\qquad
 \sum_p|(dw)(p)|^2=h^4\sum_p|(d_hv)(p)|^2.                \tag{4}
\]

The first identity follows directly from the h^5 straight-row formula.
The last equality uses dimension four. Both energies therefore have the
unit-coupling normalization used by the standard Gaussian on E.

Here is the portion of N's strong-inverse proof that the port consumes.
Let \(L_h=D_h^\sharp D_h\), \(G_s=(L_h+q^\sharp q)^{-1}\),
and \(F_s=G_sq^\sharp\). Put

\[
 P_s=F_s(F_s^\sharp F_s)^{-1}F_s^\sharp,\quad R_g=I-P_s,
 \quad K_0=d_h^\sharp d_h+D_hR_gD_h^\sharp+Q_h^\sharp Q_h.
\]

The homogeneous gap gives a uniform inverse in energy norm.
Its small exponential conjugations give cell bounds for K_0^(-1).
For u = K_0^(-1)f these yield
\(\|u\|_{2,\mathrm{cell},\infty}\le C\|f\|_\infty\).
The site factorization

\[
 D_hP_sD_h^\sharp
 =(D_hF_s)(F_s^\sharp F_s)^{-1}(D_hF_s)^\sharp
\]

maps this cell norm to the supremum norm, by N:41908-41930.
The rows Q_h and their physical transposes have bounded norms between
the cell norm and the relevant supremum norms.
The flat Hodge identity now gives the scalar equation

\[
 L_hu=f+D_hP_sD_h^\sharp u-Q_h^\sharp Q_hu.
\]

Its right side is bounded by \(C\|f\|_\infty\).
The heat identity \(u=e^{-L_h}u+\int_0^1e^{-tL_h}L_hu\,dt\)
and the integrable first-derivative bound C(t+h^2)^(-1/2) give
\(\|u\|_\infty+\|D_hu\|_\infty\le C\|f\|_\infty\).
This is N:41960-41987, using N:41781-41884.

Set \(S=Q_hK_0^{-1}Q_h^\sharp\). The source's exact right inverse E_Q
has bounded K_0 energy. Therefore

\[
 \|b\|_2^2
 =\langle K_0^{-1}Q_h^\sharp b,K_0E_Qb\rangle
 \le C\langle b,Sb\rangle^{1/2}\|b\|_2.
\]

This gives S >= cI. The weighted inverse gives exponential decay of S;
small conjugation and the lower bound give it also for S^(-1).
Summing coarse cells makes S^(-1) bounded on the supremum norm.
N:42009-42038 thus gives, with zero fine force,

\[
 H_hB=K_0^{-1}Q_h^\sharp S^{-1}B,\qquad
 \|d_hH_hB\|_\infty\le C_H\|B\|_\infty.                \tag{5}
\]

C_H is independent of h and N_j. The curl costs at most two first
derivative terms in the source norm. This fixes C_H once and for all.

For completeness, the curvature identification follows the source exactly.
The saddle equation is

\[
 (d_h^\sharp d_h+D_hR_gD_h^\sharp)H_hB-Q_h^\sharp\omega=0,
 \qquad Q_hH_hB=B.
\]

Test it against D_h lambda with q lambda = 0.
The curl and multiplier terms vanish. The identity
ran R_g = L_h(ker q) makes the remaining tests fill ran R_g.
Thus \(R_gD_h^\sharp H_hB=0\). The field minimizes curl energy on
\(Q_hv=B\). This uses the source's proved site range identity.

If an exact raw curvature f satisfies A_j f = d_c B, write f = dw.
Then S_n w - B is a closed coarse one-form.
A coarse closed form is a gradient plus a constant: the nonzero Fourier
modes are gradients, and the zero modes are constants.
A fine constant removes the latter, since S_n sends a fine constant c
to n c. A fine gradient removes the former, since S_n d = d_c q
and q is onto. Both corrections preserve f.
Consequently the affine potential fibre and the prescribed-curvature
fibre have the same curvature image.

The least-norm curvature in that image is unique. Equations (4)-(5) give

\[
 \mathcal H_j B=h^2d_hH_hB.                               \tag{6}
\]

This is the minimizer in SA:7649,26133 and N:4340,100989-101029.
In particular it depends on B only through d_c B.
No representative of a closed fine one-form remains in (6).

Write T_h = d_h H_h in ordinary coarse coordinate values.
Because the matrices are real, apply (5) to the signs of any one row.
The resulting coarse datum has supremum norm at most one. Hence

\[
 \sup_p\sum_b|T_h(p,b)|\le C_H.                           \tag{7}
\]

This consequence of the strong bound is enough for the diagonal estimate.
It avoids needing an additional spatial estimate for the coarse covariance.

## 4. The actual blocked law has bounded coarse potential variance

Let F be the standard Gaussian on E. On the coarse torus put

\[
 E_c=\operatorname{ran}d_c,\quad P_c=P_{E_c},\quad
 C_j=A_jF,\quad V_j=\operatorname{Cov}(C_j)=A_jPA_j^*.
\]

C_j is the actual blocked curvature. Its law need not be a fresh Maxwell law.

The contraction \(\|A_j\|_{2\to2}\le1\) is already proved by
Sussman and Alpoge: SA:8521-8554; N:5568-5605; FP1:157-159.
Its nonnegative row weights sum to n^2. Its column weights sum to n^(-2).
Weighted Cauchy-Schwarz gives their product, one, in dimension four.
The proof counts periodic multiplicities and therefore applies to (3).
Since A_j maps exact curvature to exact curvature, this gives

\[
 0\preceq V_j\preceq P_c.                                \tag{8}
\]

Indeed V_j has range in E_c. On that space its quadratic form is at
most \(\|A_j^*u\|^2\le\|u\|^2\); it vanishes on the orthogonal complement.

Use the canonical coarse potential space
\(X_c=(\ker d_c)^\perp=\operatorname{ran}d_c^*\).
The restriction \(d_c:X_c\to E_c\) is a bijection. Denote its inverse by T_c.
Define

\[
 B_j=T_c C_j.                                             \tag{9}
\]

This chooses the coexact representative of the actual blocked curvature.
It removes gradients and constant one-forms only from that representative.
It does not remove any component of C_j or of the retained fine background.
The possibly degenerate Gaussian law in (9) is defined without a density
or a potential gauge integral.

Taking covariance in (9) and using (8) gives

\[
 S_j:=\operatorname{Cov}(B_j)
 \preceq T_cP_cT_c^*
 =\iota_X(d_c^*d_c|_{X_c})^{-1}\iota_X^*.                 \tag{10}
\]

Here iota_X includes X_c into the coarse one-forms.
The equality is the inverse identity for the bijection \(d_c|_{X_c}\).
It follows either by multiplying both sides by d_c and d_c^*,
or by writing the inverse in orthonormal bases of X_c and E_c.

The coarse Hodge identity is

\[
 d_c^*d_c+d_{0,c}d_{0,c}^*=\Delta_c I.
\]

CA-II:69541-69565 proves this identity in counting coordinates;
N:41960-41972 uses its physical version.
It holds at coarse spacing one by relabeling the same torus calculation.
On X_c the second term vanishes. Also X_c is orthogonal to constant
one-forms and is invariant under Delta_c. Thus the right side of (10)
is \(\Delta_c^+\Pi_{X_c}\preceq\Delta_c^+ I\).
The characters \(N^{-2}e^{2\pi i k\cdot x/N}\) form an orthonormal basis.
Applying the coarse Laplacian gives eigenvalue
\(4\sum_\mu\sin^2(\pi k_\mu/N)\). Each character has squared modulus N^(-4).
In particular, for every coarse bond b,

\[
 S_j(b,b)\le g_{N_j}(0),\qquad
 g_N(0)=N^{-4}\sum_{k\ne0}
    \frac1{4\sum_{\mu=1}^4\sin^2(\pi k_\mu/N)}.          \tag{11}
\]

Use one set of integer frequency representatives with |k_mu| <= N/2.
The zero frequency is omitted. This is the inverse of the raw coarse
scalar Laplacian on mean-zero functions, not an infrared mass assumption.

Here is a uniform hand bound for (11). For 0 <= t <= pi/2,
concavity of sine gives sin t >= 2t/pi. Hence the denominator in (11)
is at least \(16|k|^2/N^2\).
The shell |k|_infinity = r has at most

\[
 (2r+1)^4-(2r-1)^4=64r^3+16r\le80r^3
\]

integer points. Restricting to the frequency representatives only lowers
this count. Put q = floor(N/2). Then, for every integer N >= 2,

\[
 g_N(0)\le\frac5{N^2}\sum_{r=1}^q r
 =\frac{5q(q+1)}{2N^2}
 \le\frac58+\frac5{4N}\le\frac54.                        \tag{12}
\]

Covariance Cauchy-Schwarz, already proved at P3:464-470, now gives

\[
 |S_j(b,c)|\le5/4                                        \tag{13}
\]

for every pair of coarse bonds. This estimate is for the induced law (9).
The comparison in (10) establishes it without replacing that law.

## 5. The diagonal bound and the terminal level

By the finite conditioning result already ported in P3,
\(Y_j=\mathbb E[F\mid A_jF]=P_{W_j}F\).
It is the least-norm exact fine curvature with datum C_j.
Equation (6), applied to (9), has precisely that datum. Consequently

\[
 Y_j=\mathcal H_jB_j=h^2T_hB_j,\qquad
 R_j=h^4T_hS_jT_h^*.                                     \tag{14}
\]

This identifies both the random field and its covariance. It does not
infer a covariance identity merely from an equality of minimum values.
All matrices in (14) act on ordinary coordinate values.
The physical adjoint was used only in constructing H_h; (4) fixes its
conversion to the raw field in (14).

Combining (7), (13), and (14) proves

\[
 0\le R_j(p,p)
 \le\frac54 h^4\left(\sum_b|T_h(p,b)|\right)^2
 \le\frac54 C_H^2 L^{-4j}.                              \tag{15}
\]

This is a bound at every fine plaquette. It is not a rank average.
Apply P3's covariance inequality once more:

\[
 |R_j(p,q)|\le\sqrt{R_j(p,p)R_j(q,q)}
 \le C_R L^{-4j}=C_R(a/a_j)^4,
 \qquad C_R=\max\{1,5C_H^2/4\}.                          \tag{16}
\]

No parameter chosen in this proof depends on K, j, m, p, or q.
The same C_H applies by (3) at every level.
For j = 0, A_0 is the identity on E, so R_0 = P; also P <= I.
For j = K, h = L^(-K) = a, and (16) reads |R_K(p,q)| <= C_R a^4.
Equation (14) still contains the terminal coarse Gaussian B_K.
Neither B_K nor R_K has been set to zero.

## 6. Joining TP1's free tower

Port the nested projections of SA:7641-7649,26028-26036 and
N:4332-4340,100448-100456. They give

\[
 R_0=P,\qquad G_i=R_{i-1}-R_i\succeq0,\qquad R_j\succeq0,
 \qquad P=\sum_{i=1}^jG_i+R_j\quad(0\le j\le K).          \tag{17}
\]

Positivity here means positive semidefinite. Covariance entries can have
either sign. The independent pieces are the source's orthogonal pieces.
The source's flat-law comparison in §2 identifies these same pieces
with the plain/soft-contour and straight/tree quadratic steps.
It includes closed forms, harmonic constants and normalized gauge integration.
It concerns full free quadratic laws; no cutoff-window statement is imported.

The spacing dictionary is

\[
 a_{K-j}^{\rm SA}=a_j^{\rm TP1},\qquad
 \eta_j^{\rm SA}=a/a_j=L^{-j}.
\]

SA:32521-32524 states these source conventions. The source slice bound
in SA:7646,26138 and N:4337,100994 is at a_(j-1) in TP1 units.
TP1:77 allows this fixed shift. Explicitly,
\((a/a_{j-1})^4=L^4(a/a_j)^4\) and a_(j-1) = a_j/L.
Thus fixed changes of C and delta put the supplied slice estimate
in TP1's convention. This proof did not need that estimate for (16).

The attachment point and barycentre of a bare plaquette are separated
by a/sqrt(2). Changing both endpoints changes their periodic distance
by at most sqrt(2) a. The slice exponential therefore changes by a fixed
factor at every j >= 1. The residual bound has no distance factor.
Use periodic distance for a global torus kernel and the corresponding
short lifted distances on TP1's test patch.

Running factors x_i^(-1) never enter (14)-(17). These are unit-coupling
covariances. The density convention is a^(-4)R_j; (16) equivalently bounds
its entries by C_R a_j^(-4). This is a change of units after the proof.

## Result

**Proof.** The requested FREE join is established, with the slice estimate
supplied by the task. Equations (16)-(17) hold on every compatible torus,
at every level, with the terminal R_K retained.

The new argument is the join (8)-(16). It combines Sussman and Alpoge's
actual curvature contraction and strong minimizer with a coarse variance
comparison. Their projection algebra, flat-law comparison, heat estimates,
gap and strong inverse are ported work, not new claims of this note.
The stronger spatial background bound (2) was not needed.

This is a complete written proof of tasks 13.1-13.2 using those ported
results and the stipulated slice estimate. No new supplier lemma remains.
The note has not been checked by another model. It grants no retained status.
It does not address REG, AMP, the interacting source law, or T0.

**Recovery checkpoint.** The checkout revision is fixed in the header.
The source revisions and the exact invoked ranges are recorded above.
Only this file was written. No numerical proof, audit, registry change,
commit, push, or external post was performed.
There is no failed proof route or unresolved supplier in the residual join.
The next review should check (8)-(16) and the source-domain match (3)-(6).

| Claim | Status | Source or limit |
|---|---|---|
| Actual centered curvature map and its contraction | Ported from SA:7634-7641,8521-8554; N:4324-4332,5568-5605 | Counting norms and periodic multiplicities. |
| Nested projections, independent slices, retained terminal background | Ported from SA:7641-7649,26028-26036; N:4332-4340,100448-100456 | Finite algebra already checked in P3. |
| Plain/soft-contour and straight/tree curvature laws agree | Ported from N:101043-101077; earlier conditional account at SA:26143-26148 | Full flat quadratic laws only. |
| Uniform strong inverse and curvature lift | Ported from N:41659-42061,100989-101029 | Premise-by-premise trace in §2.2; SA:26141 was a sketch. |
| Row sum (7) | Proved here from the ported strong bound | Valid for all coarse bond data. |
| Actual blocked covariance domination (8)-(11) | Proved here using the ported contraction and CA-II:69541-69565 | No replacement of the blocked law. |
| Uniform coarse variance (12)-(13) | Proved here | Finite Fourier formula and displayed shell inequality. |
| Field identity (14), diagonal and residual bounds (15)-(16) | Proved here using the ported minimizer identification | All j, including 0 and K; all compatible volumes and positions. |
| Slice kernel estimate | Input supplied by the task: SA:7646,26138; N:4337,100994 | Not reproved; not used to prove the residual bound. |
| TP1 units, level shift, positions and terminal admission | Proved here in (3)-(4) and §6 | Construction parameters fixed before K and volume. |
| First unresolved supplier for tasks 13.1-13.2 | None | The stipulated slice estimate remains an input. Stronger spatial bounds and interacting claims are outside this proof. |
