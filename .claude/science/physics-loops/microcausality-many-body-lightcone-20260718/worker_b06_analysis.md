# Directional tilt data for the bond-adjacency walk on \(\mathbb Z^3\)

All load-bearing arithmetic below is exact; every decimal is labeled advisory-only.

## Local neighbor enumeration

For a bond with positive-coordinate representation \(b=(x,i)=\{x,x+e_i\}\),
\[
\phi(b)=2x_1+\mathbf 1_{i=1}.
\]

### 1. Parallel start

By translation, take \(b=\{0,e_1\}\), so \(\phi(b)=1\). At the endpoint \(0\), excluding \(b\), the incident bonds are

- \(\{-e_1,0\}\), with height \(-1\) and \(\Delta=-2\);
- \(\{0,\pm e_2\}\) and \(\{0,\pm e_3\}\), each with height \(0\) and \(\Delta=-1\).

At the endpoint \(e_1\), excluding \(b\), they are

- \(\{e_1,2e_1\}\), with height \(3\) and \(\Delta=2\);
- the four transverse bonds from \(e_1\), each with height \(2\) and \(\Delta=1\).

Thus the exact multiset is
\[
\{-2,\underbrace{-1,-1,-1,-1}_{4},
  \underbrace{1,1,1,1}_{4},2\},
\]
or, as counts,

| \(\Delta\) | \(-2\) | \(-1\) | \(0\) | \(1\) | \(2\) |
|---:|---:|---:|---:|---:|---:|
| parallel count | 1 | 4 | 0 | 4 | 1 |

### 2. Transverse start

Take \(b=\{0,e_2\}\), so \(\phi(b)=0\). At each of its two endpoints there is one incident parallel bond going in the negative \(e_1\) direction, with height \(-1\), and one going in the positive \(e_1\) direction, with height \(1\). The other three allowed bonds at each endpoint are transverse and have height \(0\). Therefore
\[
\#\{\Delta=-1\}=2,\qquad
\#\{\Delta=0\}=6,\qquad
\#\{\Delta=1\}=2.
\]

| \(\Delta\) | \(-2\) | \(-1\) | \(0\) | \(1\) | \(2\) |
|---:|---:|---:|---:|---:|---:|
| transverse count | 0 | 2 | 6 | 2 | 0 |

Both rows sum to the degree \(10\).

### 3. Independent finite-box check

The script constructs every positive-axis nearest-neighbor bond with endpoints in \([-L,L]^3\), builds adjacency from endpoint incidence, and tests both central starts. It also tests every bond having both endpoints in the one-layer-interior box \([-L+1,L-1]^3\), so every one of its ten neighbors is present. The results are stable:

| \(L\) | total box bonds | safe parallel tested | safe transverse tested | result |
|---:|---:|---:|---:|:---|
| 2 | 300 | 18 | 36 | all exact signatures agree |
| 4 | 1944 | 294 | 588 | all exact signatures agree |

## 4. Tilt polynomials and the honest uniform bound

The two exact weighted row sums are
\[
\begin{aligned}
S_{\parallel}(y)&=y^{-2}+4y^{-1}+4y+y^2,\\
S_{\perp}(y)&=2y^{-1}+6+2y.
\end{aligned}
\]

If “coefficient-wise maximum” is taken literally across the two orientation rows, the resulting simultaneous envelope (the coefficient-wise \(S(y)\)) is
\[
S_{\mathrm{cw}}(y)=y^{-2}+4y^{-1}+6+4y+y^2.
\]
It is honest but unnecessarily loose because its coefficients combine entries that never occur in one row; in particular \(S_{\mathrm{cw}}(1)=16\).

The sharp pointwise row maximum requested for the walk bound is instead
\[
S_{\max}(y)=\max\{S_{\parallel}(y),S_{\perp}(y)\}.
\]
Exactly,
\[
\begin{aligned}
S_{\parallel}(y)-S_{\perp}(y)
&=y^2+2y-6+2y^{-1}+y^{-2}\\
&=\frac{(y-1)^2(y^2+4y+1)}{y^2}\ge 0
\qquad (y\ge1).
\end{aligned}
\]
Hence
\[
\boxed{S_*(y)=S_{\max}(y)=S_{\parallel}(y)quad\text{for }y\ge1.}
\]
At \(y=1\), both actual row sums, and therefore \(S_*\), equal \(10\), as required.

## 5. Walk-tilt inequality

Let \(\mathcal B_0\) be a finite set of allowed start bonds, let \(N_{\rm start}=|\mathcal B_0|\), and let
\[
w=(b_1,\ldots,b_k),\qquad b_1\in\mathcal B_0,
\qquad b_{j+1}\sim b_j\quad(1\le j<k).
\]
Here \(k\ge1\), \(m\in\mathbb Z\), and \(y\ge1\). Put
\[
\Delta_j=\phi(b_{j+1})-\phi(b_j),
\qquad
G(w)=\sum_{j=1}^{k-1}\Delta_j
=\phi(b_k)-\phi(b_1).
\]

First prove the stepwise partition-sum bound. For a fixed bond \(b\), define
\[
F_0(b)=1,
\]
and, for \(n\ge0\),
\[
F_{n+1}(b)
=\sum_{b'\sim b}y^{\phi(b')-\phi(b)}F_n(b').
\]
This recursion is exactly the sum of \(y^{\text{total gain}}\) over all \(n+1\) step continuations from \(b\). If \(F_n(b')\le S_*(y)^n\) for every \(b'\), then
\[
\begin{aligned}
F_{n+1}(b)
&=\sum_{b'\sim b}y^{\phi(b')-\phi(b)}F_n(b')\\
&\le S_*(y)^n
  \sum_{b'\sim b}y^{\phi(b')-\phi(b)}\\
&\le S_*(y)^n S_*(y)
=S_*(y)^{n+1}.
\end{aligned}
\]
The first inequality uses positivity of every weight and the induction hypothesis; the second uses the uniform pointwise row-sum bound. Since \(F_0=1\), induction gives
\[
F_n(b)\le S_*(y)^n
\quad\text{for every bond }b.
\]
Consequently,
\[
\sum_{\substack{w=(b_1,\ldots,b_k)\\b_1\in\mathcal B_0}}y^{G(w)}
=\sum_{b_1\in\mathcal B_0}F_{k-1}(b_1)
\le N_{\rm start}S_*(y)^{k-1}.
\]

For each walk, monotonicity of \(g\mapsto y^g\) at \(y\ge1\) gives the pointwise indicator inequality
\[
\mathbf 1_{\{G(w)\ge m\}}
\le y^{G(w)-m}.
\]
Indeed, if \(G(w)\ge m\), the right side is at least one; otherwise the left side is zero and the right side remains positive. Summing it over all walks gives every step explicitly:
\[
\begin{aligned}
\#\{w:G(w)\ge m\}
&=\sum_w\mathbf 1_{\{G(w)\ge m\}}\\
&\le\sum_w y^{G(w)-m}\\
&=y^{-m}\sum_w y^{G(w)}\\
&\le
N_{\rm start}S_*(y)^{k-1}y^{-m}.
\end{aligned}
\]
Thus
\[
\boxed{\#\{w:G(w)\ge m\}
\le N_{\rm start}S_*(y)^{k-1}y^{-m}.}
\]
For one fixed initial bond, \(N_{\rm start}=1\), which is exactly the no-prefactor form stated in the task. For a finite start set, the \(N_{\rm start}\) factor is necessary and is retained below.

## 6. Exact height offset and velocity bookkeeping

Let \(H_r=\{x\in\mathbb Z^3:x_1=r\}\), take integer \(d\ge1\), and suppose the start bond touches \(H_0\) while the end bond touches \(H_d\). A bond touching \(H_r\) has one of the following heights:

- a parallel bond from level \(r-1\) to \(r\): \(2r-1\);
- a transverse bond within level \(r\): \(2r\);
- a parallel bond from level \(r\) to \(r+1\): \(2r+1\).

Therefore
\[
\phi(b_1)\le1,
\qquad
\phi(b_k)\ge2d-1,
\]
and every such crossing walk obeys
\[
G(w)=\phi(b_k)-\phi(b_1)
\ge(2d-1)-1=2d-2.
\]
The uniform offset is thus exactly
\[
\boxed{m=2d-2,\qquad c_0=2.}
\]
It is sharp for this definition of “touch”: a start bond from level \(0\) to \(1\) has height \(1\), and an end bond from level \(d-1\) to \(d\) has height \(2d-1\).

Assume the parent expansion assigns a length-\(k\) bond walk the nonnegative magnitude factor \((2J)^k t^k/k!\), with \(J,t\ge0\). Applying the preceding count to the subset whose end touches \(H_d\) yields
\[
\begin{aligned}
\mathcal B(d,t)
&\le\sum_{k\ge1}
 \frac{(2J)^k t^k}{k!}
 N_{\rm start}S_*(y)^{k-1}y^{-(2d-2)}\\
&=\frac{N_{\rm start}}{S_*(y)}y^{-(2d-2)}
  \sum_{k\ge1}\frac{(2J S_*(y)t)^k}{k!}\\
&=\boxed{\frac{N_{\rm start}}{S_*(y)}y^{-(2d-2)}
  \left(e^{2J S_*(y)t}-1\right)}.
\end{aligned}
\]
The equality on the second line only factors out \(S_*^{-1}\); the last uses
\(\sum_{k\ge1}z^k/k!=e^z-1\).

For \(y>1\), use \(e^a-1\le e^a\) for \(a\ge0\):
\[
\begin{aligned}
\mathcal B(d,t)
&\le \frac{N_{\rm start}}{S_*(y)}
   \exp\!\left(-(2d-2)\ln y+2J S_*(y)t\right)\\
&=\frac{N_{\rm start}y^2}{S_*(y)}
   \exp\!\left(-2d\ln y+2J S_*(y)t\right)\\
&=\frac{N_{\rm start}y^2}{S_*(y)}
   \exp\!\left[-2\ln y\left(d-
      \frac{J S_*(y)}{\ln y}t\right)\right].
\end{aligned}
\]
Thus the site-distance velocity delivered by this bound is
\[
\boxed{v(y)=\frac{J S_*(y)}{\ln y},\qquad y>1.}
\]
There is no additional factor \(1/2\): the height penalty contributes \(-2d\ln y\), while the parent series contributes \(+2J S_*t\), so the factors of two cancel. More explicitly, to make the last envelope at most a target \(\varepsilon>0\), it is sufficient that
\[
2d\ln y\ge 2J S_*(y)t
+\ln\!\left(\frac{N_{\rm start}y^2}{S_*(y)\varepsilon}\right).
\]
This is the requested condition \(2d\ln y>2J S_*t+O(1)\), with the isolated walk-sum prefactor displayed exactly.

## 7. Exact rational tilt scan

Since \(S_*=S_{\parallel}\) on the entire scan, the exact data are:

| \(y\) | \(S_{\parallel}(y)=S_*(y)\) | \(S_{\perp}(y)\) | exact \(v(y)/J\) | advisory-only decimal \(v(y)/J\) |
|---:|---:|---:|---:|---:|
| \(5/4\) | \(4161/400\) | \(101/10\) | \(4161/(400\ln(5/4))\) | 46.6179727746 |
| \(3/2\) | \(409/36\) | \(31/3\) | \(409/(36\ln(3/2))\) | 28.0199476698 |
| \(2\) | \(57/4\) | \(11\) | \(57/(4\ln 2)\) | 20.5584043327 |
| \(5/2\) | \(1801/100\) | \(59/5\) | \(1801/(100\ln(5/2))\) | 19.6553335896 |
| \(3\) | \(202/9\) | \(38/3\) | \(202/(9\ln 3)\) | 20.4298137532 |
| \(4\) | \(529/16\) | \(29/2\) | \(529/(16\ln 4)\) | 23.8495523947 |

The identification of the best scanned point does not rely on the decimal column. For positive \(a,b,S_a,S_b\),
\[
\frac{S_a}{\ln a}<\frac{S_b}{\ln b}
\iff S_a\ln b<S_b\ln a
\iff b^{S_a}<a^{S_b}.
\]
Clearing only the rational denominators of the two \(S\) values turns the last comparison into an exact rational-number comparison. For \(a=5/2\), the script verifies the following five exact inequalities:
\[
\begin{array}{rcl}
(5/4)^{7204}&<&(5/2)^{4161},\\
(3/2)^{16209}&<&(5/2)^{10225},\\
2^{1801}&<&(5/2)^{1425},\\
3^{16209}&<&(5/2)^{20200},\\
4^{7204}&<&(5/2)^{13225}.
\end{array}
\]
Each is equivalent to saying that the \(5/2\) velocity is smaller than the corresponding other scanned velocity. Hence the best certified value **within the requested finite scan** is
\[
\boxed{y=\frac52,\qquad
v_{\rm scan}=\frac{1801}{100\ln(5/2)}J.}
\]
Its advisory-only value is \(19.6553335896J\). The parent readout is exactly \(20eJ\), advisory-only \(54.3656365692J\) (about \(54.37J\)). Their exact ratio is
\[
\frac{20eJ}{v_{\rm scan}}
=\frac{2000e\ln(5/2)}{1801},
\]
with advisory-only value \(2.76594830210\).

## 8. Sanity and large-reach behavior

At \(y=1\),
\[
S_*(1)=1+4+4+1=10,
\]
so the tilted count reduces to the ordinary degree bound
\(N_{\rm start}10^{k-1}\).

Every single step has \(\Delta\le2\). Therefore a \(k\)-bond walk has
\[
G(w)\le2(k-1).
\]
If \(m>2(k-1)\), the reach event is empty. This also follows qualitatively from the tilt inequality: as \(y\to\infty\),
\[
S_*(y)=y^2\left(1+4y^{-1}+4y^{-3}+y^{-4}\right),
\]
so
\[
S_*(y)^{k-1}y^{-m}
\sim y^{2(k-1)-m}\longrightarrow0
\quad\text{when }m>2(k-1).
\]
Because the walk count is a nonnegative integer bounded by this expression for every \(y\), it must then be zero. With \(m=2d-2\), a crossing requires
\[
2(k-1)\ge2d-2,
\qquad\text{hence}\qquad k\ge d,
\]
which is the expected qualitative reach lemma in site units.

## Script output (verbatim)

```text
EXACT LOCAL SIGNATURES
parallel:   {-2: 1, -1: 4, 1: 4, 2: 1}
transverse: {-1: 2, 0: 6, 1: 2}

FINITE-BOX STABILITY CHECKS
radius=2: total_bonds=300, safe_parallel_checked=18, safe_transverse_checked=36
  central parallel   {-2: 1, -1: 4, 1: 4, 2: 1}
  central transverse {-1: 2, 0: 6, 1: 2}
radius=4: total_bonds=1944, safe_parallel_checked=294, safe_transverse_checked=588
  central parallel   {-2: 1, -1: 4, 1: 4, 2: 1}
  central transverse {-1: 2, 0: 6, 1: 2}

SYMBOLIC TILT DATA
S_par(y)  = y**2 + 4*y + 4/y + y**(-2)
S_perp(y) = 2*y + 6 + 2/y
S_coefficientwise(y) = y**2 + 4*y + 6 + 4/y + y**(-2)
S_par(y) - S_perp(y) = (y - 1)**2*(y**2 + 4*y + 1)/y**2
S_max(y) = S_par(y) for y >= 1
S_par(1) = 10, S_perp(1) = 10

RATIONAL TILT SCAN
velocity convention: v(y)/J = S_max(y)/ln(y)
y=5/4: S_par=4161/400, S_perp=101/10, v/J=(4161/400)/ln(5/4), advisory_float=46.6179727746
y=3/2: S_par=409/36, S_perp=31/3, v/J=(409/36)/ln(3/2), advisory_float=28.0199476698
y=2: S_par=57/4, S_perp=11, v/J=(57/4)/ln(2), advisory_float=20.5584043327
y=5/2: S_par=1801/100, S_perp=59/5, v/J=(1801/100)/ln(5/2), advisory_float=19.6553335896
y=3: S_par=202/9, S_perp=38/3, v/J=(202/9)/ln(3), advisory_float=20.4298137532
y=4: S_par=529/16, S_perp=29/2, v/J=(529/16)/ln(4), advisory_float=23.8495523947

SCAN SUMMARY
best scanned y=5/2: v=(1801/100)*J/ln(5/2)
exact best-point certificates (each is equivalent to v_best < v_other):
  (5/4)^7204 < (5/2)^4161: True
  (3/2)^16209 < (5/2)^10225: True
  (2)^1801 < (5/2)^1425: True
  (3)^16209 < (5/2)^20200: True
  (4)^7204 < (5/2)^13225: True
best advisory v/J=19.6553335896
parent 20*e advisory=54.3656365692
parent/best exact ratio=2000*E*log(5/2)/1801
parent/best advisory ratio=2.76594830210
```

## LIMITS

- The point \(y=5/2\) is proved best only among the six requested rational tilts. No claim is made that it minimizes \(J S_*(y)/\ln y\) over all real \(y>1\).
- The uniform maximum-row-sum method is valid but is not proved optimal among all multi-step, orientation-sensitive transfer-matrix bounds.
- The exact offset \(c_0=2\) applies to integer coordinate planes and the stated convention that both boundary-straddling and transverse bonds “touch” a plane. Other support geometries require recomputing the endpoint height extrema.
- The displayed exponential sum assumes the parent coefficient \((2J)^k t^k/k!\) and no additional \(d\)- or \(t\)-dependent factors. Any omitted parent prefactor would modify the additive \(O(1)\) threshold term, though not the derived slope \(v(y)\).
- Advisory decimals are for readability only and carry no proof burden.
