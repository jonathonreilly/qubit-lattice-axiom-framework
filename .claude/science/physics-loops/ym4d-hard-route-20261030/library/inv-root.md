# The UM inverse root and its carriers
Provenance: Codex (GPT-6; exact runtime model ID unavailable), max queue assignment; checkout `e38557a33547d2a14b5460e6bf16d83a57f139b9`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; grants no status.

## 1. Check of um-envelope, Sections 4–5

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the UM construction. `SA` denotes their pinned `YM4_sketch_500.tex`. Credit Tadeusz Balaban for the covariance and walk constructions discussed below. Local paths are relative to this research folder.

This addresses FINISH row 165 and its consumers in rows 117, 160 and 163. The check below is by Codex, the same provider as `um-envelope.md`. It is not an other-model check.

**Checked line by line by Codex; first failing step none in the conditional claims.** The retained A2 and walk premises remain premises.

- **Section 4, (4): correct.** SA 14164–14170 defines two separately decoupled series. It does not identify their functional calculi.
- **Section 4, (5): correct conditionally.** Use the repaired count, full field hull and all parameter cubes from `h-walk-gate.md:150–188` and `h-walk-fix-gate.md:143`. The collar loss is `R_h=C_L M_1`. With `w>=c_w M>=2R_h`, the exponent is at most `16 kappa-bar-delta c_w M/8`.
- **Section 4, inverse comparison: correct.** Compression preserves the real gap. Errors `a/2` and `a/4` give inverse bounds `2/a` and `4/a`. Multiplying these bounds in the resolvent identity gives `8e/a^2`. The upper bound uses the repaired `a2-full-gate.md:72–76` inputs.
- **Section 4, (6)–(7): correct as an implication.** Add and subtract `X_s r_0`. This gives `BR`, `TE` and the stated `K_0`. It does not prove (6).
- **Section 5, rate window: correct.** Its lower slope is less than `1/(4C_h^WF)`. Its upper slope is `1/(2C_h^WF)`. A sufficiently large `kappa` leaves a strict interval. Since `Theta>0`, `kappa-bar>=Theta+1` implies `exp(kappa-bar)-1>=exp(Theta)`.
- **Section 5, budgets: correct conditionally.** The bound `M^4 exp(-dM)<=5!/(d^5 M)` proves (9). Its two half-budgets sum to the required `epsilon_G`. Each term of (1) is then at most `1/3`. Reducing the later radii preserves their window: with `alpha_1=t`, `alpha_0=t/(2D_r)`, every squared-radius condition holds for small `t`. The final logarithmic thresholds follow from the displayed exponential-series estimate. These steps use the prior constant table; they prove no new analytic input.

Thus the conditional order survives this check. The inverse-root estimate remains the exact next obligation.

## 2. Inputs and the series to construct

Balaban, CMP **99** (1985), 389–434, pp. 408–410, (3.87)–(3.94), constructs local approximations and expands their defects. Pages 431–432, (3.174)–(3.187), construct the unit-lattice covariance. CMP **109** (1987), pp. 267–270, identifies the pivot covariance and introduces the independent-current extension. I read these excerpts in `cmp99b.txt` and `cmp109.txt` in the supplied paper folder. They do not supply the shifted, independently decoupled root estimate below. CMP **116**, QED3 and YM3 were absent from the allowed source inventory. No unread square-root theorem is used.

Use the actual precision

\[
 A=C_V^{\mathsf T}\{\mathrm{GF}^{(2)}_V+(QG_1Q^{\mathsf T})^{-1}-\mathsf a
                  -E^{(2)}[H_1^{\mathsf T}J]\}C_V.                 \tag{10}
\]

Retain the repaired A2 bounds `Re A>=a I`, `||A||<=b` on a fixed complex regular-pair neighbourhood. Here `a,b>0` are fixed before `M,kappa-bar`. Retain h-walk's inverse and absolute second-jet premises, including their cut-down uniformity. Use only its repaired fixed-region norm, count and full field-hull conclusions. `pw-bridge.md:314–321` lists the same premises. Its Section 7.2 also requires composition before assigning a new operator's tags.

All coordinates below are free level-`k` coordinates, in counting measure. Use physical distance in these unit-lattice coordinates. The depth-`k` metric dominates this distance. The full read hull of a precision term lies within `R_h` of a tree through its endpoints. Let `l_omega(x,y)` be the infimum of these tree lengths. Infima can be approached from above in every estimate.

Fix `M_1` above the repaired summation floor. The h-walk bound and count give, for some `eta>0`,

\[
 \max\left\{\sup_x\sum_{y,\omega},\sup_y\sum_{x,\omega}\right\}
 e^{\eta l_\omega(x,y)}|A_\omega(x,y)|\le W.                 \tag{11}
\]

Indeed, take `eta<=delta_h/2`. At each left endpoint there are boundedly many roots. The remaining sum is bounded by
`C sum_m(C M_1^(-1/3))^m sum_z exp(-delta_h |z|/2)`.
The first sum is geometric. The second is bounded by a product of four geometric sums, times the fixed bond/color multiplicity. Summing first over the left endpoint gives the column bound too. This proves (11), without using cancellation. Constants may depend on the already fixed `L,M_1`; they do not depend on depth, volume or `M`.

For a labelled family, write `|O|_theta` for the maximum in (11), with its assigned lengths. Keep intermediate coordinates as labels in a product. Assign the sum of factor lengths to that label. Direct summation gives

\[
 |UV|_\theta\le |U|_\theta|V|_\theta.                         \tag{12}
\]

Joined trees are connected. If every factor hull lies within `R_*` of its tree, the product hull does too. Its diameter satisfies `D<=length+2R_*`. Compression preserves (11) and the spectral bounds on the retained coordinate space. The construction below therefore also applies to every `A_J=chi_J A chi_J` acting on that space.

## 3. A shifted resolvent expansion with an integrable majorant

This rebuilds the defect-expansion argument. It uses finite local polynomials in place of assumed local shifted inverses.

Keep the precision entries with `l_omega(x,y)<=r`, and call their sum `A_<`. Put `E=A-A_<`. For `theta<=eta/2`,

\[
 |E|_\theta\le W e^{-\eta r/2}.                              \tag{13}
\]

Each entry of `A_<` has range at most `r` and reads fields within `r+R_h` of its endpoints. Choose `r>=1` large enough that `||E||<=a/2`. Then `Re A_<>=a_s I`, `||A_<||<=b_s`, where `a_s=a/2`, `b_s=b+a/2`. Schur's inequality justifies the operator bound from (13).

Set

\[
 \lambda=2b_s^2/a_s,\qquad
 \rho=\sqrt{1-3a_s^2/(4b_s^2)}<1,\qquad
 N_t={\lambda I-A_<\over\lambda+t}.
\]

Expanding the squared Hilbert norm gives
`||I-A_</lambda||^2<=1-2a_s/lambda+b_s^2/lambda^2=rho^2`.
Thus `||N_t^j||<=rho^j(lambda/(lambda+t))^j`. Its entries vanish beyond distance `jr`. A row or column has at most `c(1+jr)^4` entries. Cauchy–Schwarz bounds its absolute sum by
`sqrt(c)(1+jr)^2 rho^j(lambda/(lambda+t))^j`.

Choose `0<theta<=min(eta/2,-log(rho)/(2r))`. Define

\[
 P_t={1\over\lambda+t}\sum_{j=0}^{n-1}N_t^j,\qquad Q_t=N_t^n.
\]

Group each matrix entry of these finite polynomials into one coefficient. Assign it the union of the two endpoint balls of radius `R_*=nr+R_h`. This contains every field read. Assign length `|x-y|` to this coefficient. The preceding bound gives

\[
 |P_t|_\theta\le {p_r\over\lambda+t},\quad
 p_r=\sqrt c\,r^2\sum_{j\ge0}(j+1)^2\rho^{j/2},\qquad
 |Q_t|_\theta\le\sqrt c(1+nr)^2\rho^{n/2}.                  \tag{14}
\]

The series defining `p_r/r^2` converges: its ratio tends to `sqrt(rho)<1`. First increase `r` until `W exp(-eta r/2)p_r/lambda<=1/4`. This is possible since `p_r` is a fixed constant times `r^2`. The inequality `exp(eta r/2)>=(eta r/2)^3/3!` suffices. Then fix `theta` as above. Choose `n` so the last bound in (14) is at most `1/4`. Exponential decay beats its quadratic factor by the same argument. All choices precede `M,kappa-bar`.

Since `(A_<+t)P_t=I-Q_t`,

\[
 (A+t)P_t=I-K_t,\qquad K_t=Q_t-EP_t,\qquad |K_t|_\theta\le\tfrac12.
\]

Expand each `K_t` factor into these two labelled alternatives. Formula (12) proves absolute convergence and the exact identity

\[
 (A+t)^{-1}=P_t\sum_{m\ge0}K_t^m,\qquad
 \left|\{P_tK_t^m\}_{m\ge0}\right|_\theta
       \le {2p_r\over\lambda+t}\quad(t\ge0).                \tag{15}
\]

Multiplication by `A+t` proves the identity; finite-dimensional accretivity gives uniqueness of its inverse. Each coefficient reads only its stated hull. A chain's tree has the sum of its factor lengths. Its full hull lies within the single fixed radius `R_*` of that tree. Hence (15) also gives the absolute carrier moment

\[
 \max\left\{\sup_x\sum_{y,\alpha},\sup_y\sum_{x,\alpha}\right\}
 e^{\theta D(\alpha)}|R_\alpha(t;x,y)|
 \le {2p_r e^{2\theta R_*}\over\lambda+t}.                  \tag{16}
\]

This construction groups coefficients **before** inserting parameters. Expanding those grouped polynomials again after tagging would define a different series.

## 4. Integrate first, then decouple

For real `z>0`, substitution `t=z u^2` gives

\[
 {1\over\pi}\int_0^\infty {t^{-1/2}\over t+z}\,dt=z^{-1/2}.
\]

Both sides are holomorphic on `Re z>0`; dominated differentiation and the identity theorem extend the identity there. Every eigenvalue of `A` has positive real part. On a Jordan block `zI+N`, its resolvent is the finite sum
`sum_j (-N)^j/(t+z)^(j+1)`. Differentiating the scalar identity integrates each term. The result is the principal inverse root: the identity `z(z^(-1/2))^2=1`, differentiated through that same finite sum, proves its square is the inverse block. This proves the matrix integral formula without assuming diagonalizability.

For the labels of (15), define

\[
 r_\alpha={1\over\pi}\int_0^\infty t^{-1/2}R_\alpha(t)\,dt.
\]

The nonnegative majorant in (15) permits interchange of every absolute sum and this integral. Since the scalar integral at `z=lambda` equals `pi/sqrt(lambda)`,

\[
 A^{-1/2}=\sum_\alpha r_\alpha,\qquad
 |\{r_\alpha\}|_\theta\le U:={2p_r\over\sqrt\lambda},\qquad
 \max\left\{\sup_x\sum_{y,\alpha},\sup_y\sum_{x,\alpha}\right\}
 e^{\theta D(\alpha)}|r_\alpha(x,y)|\le e^{2\theta R_*}U.       \tag{17}
\]

The coefficients are holomorphic in the regular pair. Uniform majorants on its neighbourhood justify their integrals and sums. When a transpose-closed family is needed, replace each final coefficient by two labelled terms `R_alpha/2` and `R_alpha^T/2`, with the same hull. Their total is unchanged because the full resolvent is symmetric. The two-sided bound is unchanged.

Define `r(s)=sum_alpha s^{P(alpha)} r_alpha`, tagging each parameter cube meeting the full hull once. This specifies the missing inverse-root series for (10). It is not a functional calculus of `A(s)`. It need not equal a differently assigned series at `s!=1`.

## 5. The collared product

Assume the stated UM geometry: parameter cubes have side `M`; their distance from `Z_0` is at least `w=c_w M`. Choose `M>=8R_*` with room for the fixed coordinate conversion. A tree of length `l` has a traversal of length `2l`. Divide it into pieces of length at most `M/4`. Each piece, thickened by `R_*`, has coordinate diameter less than `M`, so it meets at most sixteen grid cubes. Consequently

\[
 \#P(\alpha)\le16+C_g l/M.                                  \tag{18}
\]

This proof includes zero-length terms and all corner cubes. It is the length-versus-parameter argument attributed by SA 10558 to Balaban, rebuilt here. A carrier from a row of `Z_0` that meets a parameter cube has `l>=w-R_*`.

If `C_g kappa-bar/M<=theta/2`, (17)–(18) also give the tagged carrier moment
`sup_x sum_(y,alpha) exp(theta D(alpha)/2)|s^alpha r_alpha(x,y)|<=exp(16 kappa-bar+theta R_*)U`, and its column version. Thus the tagged series converges normally on the declared discs. The requested moment may use `kappa=theta/2>0`; it is not an assertion for every positive exponent.

Products in the **given** `Gamma=-chi A(s)(1-chi)r(s)` have two separately assigned tags. Keep both. Their total exponent is at most `32+C_g(l_1+l_2)/M`. This differs from tagging a new composed operator once, as in `pw-bridge.md:427–445`.

Take `C_g kappa-bar/M<=theta/2` and `w>=2R_*`. Equations (11), (12) and (17) bound a tagged product containing a varied parameter by

\[
 WU\exp(32\bar\kappa)\exp[-\theta(w-R_*)/2]
 \le WU\exp(32\bar\kappa-dM),\qquad d=\theta c_w/4.          \tag{19}
\]

This is a row and column sum bound, hence an operator bound. No new endpoint sum is omitted: it is already in (12). The same argument for one precision factor uses `16` in place of `32`.

Here is the field comparison used with it. Fix a real reference `(U,0)`. In its regular-pair chart write
`P_z=(exp(i z eta_k A')U,zJ)`. There is a fixed radius `h>0` for the natural field/current norm. If `epsilon=a_1+j_0<=h/2`, this path remains in the input neighbourhood for `|z|<=h/epsilon`. For each coefficient `f`, Cauchy's formula gives

\[
 f(1)-f(0)={1\over2\pi i}\int_{|z|=h/\epsilon}
                    {f(z)\over z(z-1)}\,dz.
\]

Sum absolute coefficients under this integral. Bounds (11) and (17) give field differences at most `2W epsilon/h` and `2U epsilon/h` in their length norms. At `epsilon=0` they vanish. Deleting terms at `s=0` only improves these bounds. The real core's `LM a_0` is needed for its admitted reference class; adding it to the error only weakens the estimate.

Use subscripts `0` exactly as in um-envelope (6). Deletion at the real reference gives `||r_0||<=U`, `||X_0||<=W`. Split

\[
\begin{split}
 (X_s-X_0)r_0
 &=\{X_s(P)-X_0(P)+X_0(P)-X_0(U,0)\}r_0,\\
 X_s(r_s-r_0)
 &=X_s(P)\{r_s(P)-r_0(P)\}
   +X_s(P)\{r_0(P)-r_0(U,0)\}.
\end{split}
\]

The first and third differences have a varied tag and obey (19). The other two obey the Cauchy bounds. Increase the later `M` floor so `exp(32 kappa-bar-dM)<=1`; then `||X_s(P)||<=2W`, and `Gamma` is bounded. Thus

\[
 \|(X_s-X_0)r_0\|+\|X_s(r_s-r_0)\|
 \le T\{e^{32\bar\kappa-dM}+LM a_0+a_1+j_0+|\tau-1|\}.       \tag{20}
\]

One may take `R=U`, `B=W` and `T=2WU+6WU/h`, enlarged by a fixed factor for the coefficient ratio. On `|tau-1|<=1/2`, use `sqrt(tau)-1=(tau-1)/(sqrt(tau)+1)`. The principal root has positive real part, so the denominator has modulus at least one. Multiplying the bounded `Gamma` gives the extra term. All these constants precede `M,kappa-bar`. Equations (17)–(20) prove um-envelope (6), from the named inputs, for this specified series.

The small perturbation estimate concerns collared products. The reference `r_0` is a deleted series. No inverse or square root of the mutilated form away from the collar was used. This respects SA 14202–14205.

## 6. What this gives the stored carrier series

Applying (15) at `t=0` to each compression constructs a carrier expansion of `C_J=(A_J)^(-1)`. With the full hulls specified above, (11) and (16) give exactly the two moments in sa-2.13-2 (4.1), with

\[
 W_A=e^{2\theta R_h}W,\qquad
 W_C={2p_r e^{2\theta R_*}\over\lambda},\qquad \kappa=\theta/2.
                                                               \tag{21}
\]

The larger exponent `theta` is available too. All constants are uniform in the conditioning set, depth, volume and `M`. Use the uncut connected hulls, including the endpoints, when applying the cut rule. Restriction of field reads to `Omega_0` need not remain connected; SA 10558 makes this distinction explicit.

**This proves (4.1) for the expansion constructed here. It does not identify it with a previously assigned covariance expansion.** Finite polynomial grouping and the endpoint-ball hulls are part of this construction. They cannot be changed after taking a stored cut. To apply sa-2.13-2 Lemma 4.1 literally, its covariance must use (15), and its precision must use the full repaired hulls in (11). Transpose pairing can be imposed before either cut. Intersecting connected carriers have union diameter at most the sum of their diameters. The summation in (12) therefore gives `W_A+W_A^2 W_C` for the Schur chains, as that lemma requires.

The remaining transfer to any different, already fixed carrier series stops at this identification. Equality of the summed covariance is insufficient. No claim about that different stored matrix follows from (21). No other part of row 117 is proved here.

## Result

**Proved by hand, conditional on the named A2 and repaired h-walk inputs:** the actual undecoupled UM precision has the explicitly constructed inverse-root expansion (17). Its absolute carrier moments are uniform in depth, volume and `M`. Its separately decoupled series satisfies um-envelope (6), with `R,B,T` fixed before `M,kappa-bar`. This supplies that note's conditional constant order for this series.

The same construction proves sa-2.13-2 (4.1) for every compressed covariance, with (21). Transfer to a different preassigned carrier cut remains unproved; Section 6 is the stopping point. These are research implications, not unconditional Yang–Mills results. The new proof has not been checked by the other model.

Recovery: preserve the grouping in (14), the full hulls and the two tags in `Gamma`. The source checkout is the provenance pin. The fetched outline's SHA-256 is `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. Only this note was written in the repository. No scientific computation, audit, subagent, commit, push, PR or post was used. No status is granted.
