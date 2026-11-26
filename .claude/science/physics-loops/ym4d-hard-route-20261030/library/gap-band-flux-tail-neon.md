# Lower-Tail Seam-Bias Ambiguity Lemma in 4D $\mathrm{SU}(2)$ Wilson Lattice Gauge Theory

**Author:** Gemini 4 Neon (research text only, unchecked; grants no scientific or audit status).
**Target:** The lower-tail lemma named in check 1585 (`library/gap-band-direction5-check-astra62.md`, section (v), "First lemma for the next band proof row"), in the fixed band $\beta \in [2, 3]$ and, separately, along the calibrated release trajectory $\beta_K$.
**Method:** Purely by hand. No Monte Carlo, no floating-point proof steps, no Lean computation.
**Labels:** Every claim is marked **PROVED** (proved here by hand, unchecked), **PROVED GIVEN [X]** (proved here conditional on a named theorem or checked lane input), **ON FILE** (cited from a checked lane file), **ARGUED** (heuristic or belief-grade physical argument), **GUIDE** (numerical or literature value, never a proof step), or **OPEN**.

---

## 1. Exact Setup, Consumer Chain to (N-flux), Non-Equivalence, and What Remains for $\Pi$

### 1.1 Setting and Statement of the Lower-Tail Lemma

Fix spacetime dimension $D = 4$ (and general $D \ge 3$ for comparison models). Fix the spatial torus $\Lambda = (\mathbb{Z}/n\mathbb{Z})^{D-1}$ with $n \in 1024\mathbb{N}$ (specifically $n = \ell b^K$ with release odd block factor $b$, calibration level $g_0$, and fixed $\ell \in 1024\mathbb{N}$, as in check 1453 and `library/gap-k2-tool-design-fable.md` §3.1). Set $u = n/512$ and consider the two temporal periods
$$
d = 2v \in \{u, 2u\} = \{n/512,\, n/256\}.
$$
(For $n \ge 5 \cdot 1024 = 5120$ we have $d \ge u \ge 10 > 9$; below, $d \ge 9$ ensures $m = \lfloor\sqrt{d}\rfloor \ge 3$ and $2 l_j < d$.)

Let $G = \mathrm{SU}(2)$ (identified with unit quaternions $S^3 \subset \mathbb{H}$, $\operatorname{Re} q = \frac{1}{2}\operatorname{tr} q$), $\mathcal{E}$ the positively oriented spatial links of $\Lambda$, and $T = P e^{-V/2} C_{\mathcal{E}} e^{-V/2} P$ the gauge-projected Wilson transfer operator at coupling $\beta > 0$, with strictly positive real-analytic symmetric kernel $K_1(x, y)$ and $l$-step kernel $K_l(x, y)$ of $T^l$ (`library/gap-transfer.md`, Statement 1; `library/gap-band-cut-covariance-neon.md` §1.1, checked in row 1572). Write $C_z$ ($z \in \mathbb{Z}_2^{D-1}$) for the spatial centre translations ($C_z$ multiplies by $-1$ all spatial $i$-links with $z_i = 1$ and $x_i = 0$), $Z^z(t) = \operatorname{Tr}(C_z T^t)$ for the 't Hooft twisted partition functions, $P_0 = 2^{-(D-1)} \sum_z C_z$ for the centre-neutral projection, $Z_+(t) = \operatorname{Tr}(P_0 T^t)$, $P_K = Z_+(2u)/Z_+(u)^2$, and $\Pi = P_{\rm full} = Z^0(2u)/Z^0(u)^2$.

Fix the single-axis centre flip $C := C_{e_1}$ along direction $1$, with orthogonal sector projections $P_{\rm ev} = \frac{1}{2}(I + C)$ and $P_{\rm od} = \frac{1}{2}(I - C)$ commuting with $T$. Put
$$
K_l^{\rm ev}(x, y) := \frac{K_l(x, y) + K_l(Cx, y)}{2} > 0, \qquad K_l^{\rm od}(x, y) := \frac{K_l(x, y) - K_l(Cx, y)}{2},
$$
and $Z_{\rm ev}(d) := \operatorname{Tr}(P_{\rm ev} T^d) = \frac{1}{2}(Z^0(d) + Z^{e_1}(d))$, $Z_{\rm od}(d) := \operatorname{Tr}(P_{\rm od} T^d) = \frac{1}{2}(Z^0(d) - Z^{e_1}(d))$.

Split the time circle $\mathbb{Z}/d\mathbb{Z}$ into $m = \lfloor \sqrt{d} \rfloor$ contiguous arcs of lengths $l_0, \dots, l_{m-1} \in \{\lfloor d/m \rfloor, \lceil d/m \rceil\}$ summing to $d$. Define the **one-axis even pin probability law** $\Pr_{\rm ev}$ on $(x_0, \dots, x_{m-1}) \in (G^{\mathcal{E}})^m$ (with $x_m := x_0$) by
$$
d\Pr_{\rm ev}(x_0, \dots, x_{m-1}) := \frac{1}{Z_{\rm ev}(d)} \prod_{j=0}^{m-1} K_{l_j}^{\rm ev}(x_j, x_{j+1})\, dx_0 \cdots dx_{m-1}, \tag{1.1}
$$
and define on each arc $j \in \{0, \dots, m-1\}$ the conditional seam-label bias
$$
b_j := b_j(x_j, x_{j+1}) := \frac{K_{l_j}(x_j, x_{j+1}) - K_{l_j}(Cx_j, x_{j+1})}{K_{l_j}(x_j, x_{j+1}) + K_{l_j}(Cx_j, x_{j+1})} = \frac{K_{l_j}^{\rm od}(x_j, x_{j+1})}{K_{l_j}^{\rm ev}(x_j, x_{j+1})} \in (-1, 1). \tag{1.2}
$$
Note that $|b_j| \le \frac{1}{2}$ if and only if $\frac{1}{3} \le \frac{K_{l_j}(x_j, x_{j+1})}{K_{l_j}(Cx_j, x_{j+1})} \le 3$, i.e. $|\log(K_{l_j}(x_j, x_{j+1})/K_{l_j}(Cx_j, x_{j+1}))| \le \log 3$. Put $G_j := \mathbf{1}_{\{|b_j| \le 1/2\}}$ and $N_{\rm amb} := \sum_{j=0}^{m-1} G_j = \#\{j : |b_j| \le \frac{1}{2}\}$.

**Target Lemma (L-tail) (check 1585 §(v), lines 119–128).** There exist constants $c, \epsilon, C_0 > 0$ such that at both periods $d \in \{u, 2u\}$,
$$
\Pr_{\rm ev}\!\left\{\#\{j : |b_j| \le \tfrac{1}{2}\} < c \log n\right\} \le C_0 n^{-\epsilon}. \tag{L-tail}
$$
We investigate `(L-tail)` in two separate coupling quantifiers:
1. **Fixed order-one band:** uniformly for $\beta \in [2, 3]$ as $n \to \infty$ ($n \in 1024\mathbb{N}$);
2. **Calibrated release trajectory:** along $\beta = \beta_K$ at fixed release witnesses $(b, g_0)$ and fixed $\ell \in 1024\mathbb{N}$ as $K \to \infty$, where $n = \ell b^K$ and $\beta_K / \log(b^K) \to \frac{11}{3\pi^2}$ (rows 1451, 1453, `BND-2`).

---

### 1.2 Exact Consumer Chain to (N-flux) and Reduction of (PUR-io) to $\Pi$ (PROVED)

Credit: G. 't Hooft (1978, 1979) for centre twists and electric-flux sectors; check 1585 §(v) (gpt-6.2-astra) for the arc-product bound (1.3); row 1566 (Claude Fable) and check 1570 (gpt-6.2-astra) for `(N-flux)` and the two-period purity sandwich with its positivity repair.

**Proposition 1.1 (Exact consequences of `(L-tail)` toward `(N-flux)` and $\Pi$; PROVED).**
Suppose `(L-tail)` holds at a coupling $\beta > 0$ and side $n \in 1024\mathbb{N}$ at both periods $d \in \{u, 2u\}$, with constants $c, \epsilon, C_0 > 0$. Put
$$
\rho_d := C_0 n^{-\epsilon} + n^{-c \log 2}, \qquad r_1(d) := \frac{Z_{\rm od}(d)}{Z_{\rm ev}(d)}, \qquad f(d) := 1 - \frac{Z_+(d)}{Z^0(d)}.
$$
Then:
1. **(One-axis flux bound, check 1585 §(v)).**
   $$
   r_1(d) = \frac{\operatorname{Tr}(P_{\rm od} T^d)}{\operatorname{Tr}(P_{\rm ev} T^d)} = \mathbb{E}_{\rm ev}\!\left[\prod_{j=0}^{m-1} b_j\right] \le \mathbb{E}_{\rm ev}\!\left[\prod_{j=0}^{m-1} |b_j|\right] \le \rho_d. \tag{1.3}
   $$
2. **(Full three-axis electric-flux bound `(N-flux)`).** Write $W_e(d) = \operatorname{Tr}(P_e T^d) \ge 0$ for the eight electric-flux sectors $e \in \mathbb{Z}_2^3$ ($P_e = \frac{1}{8}\sum_z (-1)^{e \cdot z} C_z$, $W_0 = Z_+$, $\sum_e W_e = Z^0$). By cubic permutation symmetry on $(\mathbb{Z}/n)^3$, the single-axis odd fraction $p_{e_i}(d) := \sum_{e: e_i = 1} W_e(d)/Z^0(d)$ is independent of $i \in \{1, 2, 3\}$ and equals $\frac{r_1(d)}{1 + r_1(d)} \le \rho_d$. Hence
   $$
   p_{e_1}(d) \;\le\; f(d) = \sum_{e \ne 0} \frac{W_e(d)}{Z^0(d)} \;\le\; \sum_{i=1}^3 p_{e_i}(d) = \frac{3 r_1(d)}{1 + r_1(d)} \;\le\; 3 \rho_d. \tag{1.4}
   $$
   With $\epsilon' := \min(\epsilon, c \log 2)$ and $C' := 3(C_0 + 1) \cdot 512^{-\epsilon'}$, this gives `(N-flux, \epsilon')` of row 1566: $f(2v) \le C' v^{-\epsilon'}$ for $2v \in \{u, 2u\}$. Furthermore, every twist ratio $z \in \mathbb{Z}_2^3$ obeys
   $$
   1 - 6 \rho_d \;\le\; 1 - 2 f(d) \;\le\; \frac{Z^z(d)}{Z^0(d)} \;\le\; 1. \tag{1.5}
   $$
3. **(Two-period purity sandwich comparing $P_K$ and $\Pi = P_{\rm full}$).** Set $a_t := Z_+(t)/Z^0(t) = 1 - f(t)$ and $\alpha_t := \max\!\big(\frac{1}{8},\, 1 - 3 \rho_t\big) > 0$. Since $Z_+(t) = \frac{1}{8}\sum_z Z^z(t) \ge \frac{1}{8} Z^0(t)$ (each $Z^z(t) > 0$), we have $\alpha_t \le a_t \le 1$, and therefore
   $$
   \alpha_{2u}\, \Pi \;\le\; P_K = \frac{a_{2u}}{a_u^2}\, \Pi \;\le\; \alpha_u^{-2}\, \Pi. \tag{1.6}
   $$
   In particular, whenever $3 \rho_u < 1$ (valid for all sufficiently large $n$),
   $$
   (1 - 3\rho_{2u})\, \Pi \;\le\; P_K \;\le\; \frac{\Pi}{(1 - 3\rho_u)^2}, \tag{1.7}
   $$
   matching row 1566's sandwich $(1 - \frac{21}{8}\delta_u) P_{\rm full} \le P_K \le P_{\rm full}/(1 - \frac{21}{8}\delta_{u/2})^2$ (with $3\rho_{2u}, 3\rho_u$ in place of $\frac{21}{8}\delta_u, \frac{21}{8}\delta_{u/2}$ and incorporating check 1570's positivity floor $\alpha_u \ge 1/8$).

*Proof.* (1) Since $P_{\rm od}^m = P_{\rm od}$ and $P_{\rm od}$ commutes with $T$, $\operatorname{Tr}(P_{\rm od} T^d) = \operatorname{Tr}(\prod_{j=0}^{m-1} P_{\rm od} T^{l_j}) = \int \prod_{j=0}^{m-1} K_{l_j}^{\rm od}(x_j, x_{j+1})\, dx$. Dividing and multiplying by $\prod_j K_{l_j}^{\rm ev}(x_j, x_{j+1}) > 0$ gives $r_1(d) = \mathbb{E}_{\rm ev}[\prod_j b_j] \le \mathbb{E}_{\rm ev}[\prod_j |b_j|]$. Splitting on $\{N_{\rm amb} < c\log n\}$ (where $\prod |b_j| \le 1$) and its complement (where $\prod |b_j| \le 2^{-c\log n} = n^{-c\log 2}$) gives (1.3).
(2) By character orthogonality, $\operatorname{Tr}(P_{\rm od} T^d) = \sum_{e: e_1 = 1} W_e(d)$ and $\operatorname{Tr}(P_{\rm ev} T^d) = \sum_{e: e_1 = 0} W_e(d)$, so $p_{e_1}(d) = \frac{r_1(d)}{1 + r_1(d)}$. Cubic axis permutations preserve Haar measure and the isotropic Wilson action, so $p_{e_1} = p_{e_2} = p_{e_3}$. Every $e \ne 0$ has $e_i = 1$ for at least one $i \in \{1, 2, 3\}$, giving (1.4). Since $n = 512 u \ge 512 v$, $n^{-\epsilon'} \le 512^{-\epsilon'} v^{-\epsilon'}$. For (1.5), $Z^z(d)/Z^0(d) = 1 - 2\sum_{e: e\cdot z = 1} W_e(d)/Z^0(d) \ge 1 - 2 f(d) \ge 1 - 6\rho_d$ and $Z^z(d) \le Z^0(d)$ because $T^d \ge 0$.
(3) Immediate from $P_K = Z_+(2u)/Z_+(u)^2 = (a_{2u}/a_u^2)\Pi$ and $\alpha_t \le a_t \le 1$. $\square$

---

### 1.3 What `(L-tail)` Leaves Open for $\Pi$ and `(PUR-io)`, and Strict Non-Equivalence (PROVED)

Even a complete proof of `(L-tail)` uniformly on $\beta \in [2, 3]$ leaves **two independent major gaps** before `(PUR-io)`:
1. **Untwisted full purity $\Pi = Z^0(2u)/Z^0(u)^2$ at $\beta \in [2, 3]$:** By (1.7), `(L-tail)` collapses the sixteen twisted masses to the two untwisted masses $Z^0(u), Z^0(2u)$ up to $1 + O(n^{-\epsilon'})$ factors, reducing $P_K \ge 457/625$ at the tested coupling to $\Pi \ge (457/625)/(1 - 3\rho_{2u})$. It provides **zero** information about $\Pi$ or the neutral excited thermal sum $S_+(u) = Z_+(u)/\lambda_0^u - 1$, because neutral excitations cancel identically in $b_j$.
2. **The carry from $\beta \in [2, 3]$ to the calibrated release trajectory $\beta_K$:** `(PUR-io)` requires $P_K \ge 457/625$ at infinitely many calibrated roots $\beta_K \sim \frac{11}{3\pi^2}\log n$ (at fixed $(\ell, g_0)$), not on $\beta \in [2, 3]$. Moreover, Theorem 4 below proves that `(L-tail)` **cannot** simply be carried verbatim to $\beta_K$: on $\beta_K$ at fixed $\ell$, `(L-tail)` is incompatible with any finite-energy continuum electric-flux sector on $\mathbb{T}_\ell^3 \times S_D^1$.

We record the exact logical separations on strictly positive, positive-definite reflection-positive transfer data (enforcing the rule *Equivalent is not progress*):

**Proposition 1.2 (Strict non-equivalences on positive transfer data; PROVED).**
1. **(`(L-tail)` $\not\Rightarrow$ `(PUR-io)` — Neutral spectator blindness).** Let $T^{\rm tot} = T \otimes T_{\rm spec}$ with $C^{\rm tot} = C \otimes I$, where $T_{\rm spec}$ has strictly positive symmetric kernel $K_1^{\rm spec}(a, b) > 0$. Then $K_l^{\rm tot}((x, a), (y, b)) = K_l(x, y) K_l^{\rm spec}(a, b)$ and $K_l^{\rm tot, ev}((x, a), (y, b)) = K_l^{\rm ev}(x, y) K_l^{\rm spec}(a, b)$. Hence $K_l^{\rm spec}$ cancels identically in $b_j^{\rm tot}((x_j, a_j), (x_{j+1}, a_{j+1})) = b_j(x_j, x_{j+1})$, and $\Pr_{\rm ev}^{\rm tot} = \Pr_{\rm ev} \otimes \Pr_{\rm spec}$. The entire joint distribution of $(b_0, \dots, b_{m-1})$ is **unchanged**, while $\Pi^{\rm tot} = \Pi \cdot P_{\rm spec}$ and $P_K^{\rm tot} = P_K \cdot P_{\rm spec}$ can be made arbitrarily close to $0$ (e.g. via copies of the neutral circle heat kernel of row 1565 / check 1570).
2. **(`(PUR-io)` $\not\Rightarrow$ `(N-flux)` and `(N-flux)` $\not\Rightarrow$ `(L-tail)` — ON FILE / check 1585).** On the regular representation of $\mathbb{Z}_2^3$, $T_n = e^{-1/n^2} I + (1 - e^{-1/n^2}) P_{\rm const}$ gives $P_K = 1$ with charged fraction $f(d) \to 7/8$ (check 1550 / check 1570). On two points exchanged by $C$, $T_n$ with even eigenvalue $1$ and odd eigenvalue $r_n = \exp[-(\log n)^2 / n]$ gives $r_1(d) = r_n^d = o(n^{-M})$ for every $M > 0$, while $|b_j| = r_n^{l_j} \to 1$ deterministically on every arc, violating `(L-tail)` with probability $1$ (check 1585 line 142).
3. **(Check 1585's conditional route is strictly stronger than `(L-tail)` — NEW explicit 4-state witness).** Check 1585 line 140 proposed the sufficient route $\mathbb{P}_{\rm ev}(G_j = 1 \mid G_0, \dots, G_{j-1}) \ge \eta \log n / m$ a.s. Consider a $4$-state space $\{A_+, A_-, B_+, B_-\}$ with $C(A_\pm) = A_\mp$, $C(B_\pm) = B_\mp$, orthonormal even basis $e_A = \frac{1}{\sqrt{2}}(\delta_{A_+} + \delta_{A_-})$, $e_B = \frac{1}{\sqrt{2}}(\delta_{B_+} + \delta_{B_-})$, and odd basis $o_A, o_B$. Put $\alpha_n := n^{-2/d} \in (0, 1)$, $r_n := e^{-1/n^2}$, and define the symmetric operator $T_n = P_{\rm ev} T_{{\rm ev}, n} + P_{\rm od} T_{{\rm od}, n}$ by
   $$
   T_{{\rm ev}, n} = \begin{pmatrix} 1 & 0 \\ 0 & \alpha_n \end{pmatrix} + \delta_n \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \quad \text{in } (e_A, e_B), \qquad
   T_{{\rm od}, n} = \begin{pmatrix} 1/4 & 0 \\ 0 & \alpha_n r_n \end{pmatrix} \quad \text{in } (o_A, o_B),
   $$
   with $\delta_n > 0$ sufficiently small for each $n$. Then $T_n$ is **strictly positive definite** ($T_{{\rm ev}, n} > 0$, $T_{{\rm od}, n} > 0$) and has **strictly positive kernel entries**: on $A \times A$ entries are $\frac{1}{2}(1 + \delta_n \pm \frac{1}{4}) > 0$; on $B \times B$ entries are $\frac{1}{2}(\alpha_n + \delta_n \pm \alpha_n r_n) > 0$; on $A \times B$ and $B \times A$ entries are $\frac{1}{2}\delta_n > 0$. At $\delta_n = 0$, $Z_{\rm ev}(d) = 1 + n^{-2}$; with probability $\frac{1}{1 + n^{-2}}$ all pins lie in $A$ with $|b_j| = 4^{-l_j} < \frac{1}{2}$ ($N_{\rm amb} = m$), while with probability $\frac{n^{-2}}{1 + n^{-2}}$ all pins lie in $B$ with $|b_j| = r_n^{l_j} \to 1 > \frac{1}{2}$ ($N_{\rm amb} = 0$), and $\mathbb{P}_{\rm ev}(G_1 = 1 \mid G_0 = 0) = 0$. By continuity of finite matrix powers $T_n^l$ as $\delta_n \downarrow 0$, choosing $\delta_n > 0$ tiny enough at each $n$ preserves $\Pr_{\rm ev}(N_{\rm amb} < m) \le n^{-2}$ (so `(L-tail)` **HOLDS** with $\epsilon = 2$ and arbitrary $c > 0$) while forcing $\mathbb{P}_{\rm ev}(G_1 = 1 \mid G_0 = 0) \le e^{-n} \ll \eta \log n / m$ for every $\eta > 0$. $\square$

---

## 2. Exact Probabilistic Structure, Spectral Bridge, and Exact Hölder Flux Lower Bound

We now derive the exact information-theoretic and spectral identities governing the arc biases $b_j$. These identities hold for every reflection-positive transfer operator $T > 0$ commuting with an involution $C$, and in particular for $D$-dimensional $\mathrm{SU}(2)$ and $\mathrm{U}(1)$ Wilson and Villain lattice gauge theories at every coupling $\beta > 0$.

### 2.1 Joint Seam-Label Representation and Exact Denominator-Cancellation Identities (PROVED)

**Theorem 1 (Exact TV, Hellinger, and Markov-Bridge Identities for $b_j$; PROVED).**
For each arc $j \in \{0, \dots, m-1\}$ of length $l = l_j$, define the two probability densities on $G^{\mathcal{E}} \times G^{\mathcal{E}}$:
$$
p_+^{(j)}(x, y) := \frac{K_l(x, y)\, K_{d - l}^{\rm ev}(y, x)}{Z_{\rm ev}(d)}, \qquad
p_-^{(j)}(x, y) := p_+^{(j)}(Cx, y) = \frac{K_l(Cx, y)\, K_{d - l}^{\rm ev}(y, x)}{Z_{\rm ev}(d)}. \tag{2.1}
$$
Then:
1. **(Joint $(x, \sigma)$ representation).** Define the probability law $\mathbb{P}_{\rm joint}$ on $(x, \sigma) \in (G^{\mathcal{E}})^m \times \{\pm 1\}^m$ by
   $$
   d\mathbb{P}_{\rm joint}(x, \sigma) := \frac{1}{2^m Z_{\rm ev}(d)} \prod_{k=0}^{m-1} K_{l_k}\!\big(C^{(1-\sigma_k)/2} x_k,\, x_{k+1}\big)\, dx. \tag{2.2}
   $$
   Its $x$-marginal is $\Pr_{\rm ev}$. Conditional on $x$, the seam labels $\sigma_0, \dots, \sigma_{m-1}$ are mutually independent with $\mathbb{E}_{\rm joint}[\sigma_k \mid x] = b_k(x_k, x_{k+1})$. The global parity $\Pi(\sigma) := \prod_{k=0}^{m-1} \sigma_k$ obeys $\mathbb{P}_{\rm joint}(\Pi(\sigma) = +1) = \frac{Z^0(d)}{2 Z_{\rm ev}(d)}$ and $\mathbb{P}_{\rm joint}(\Pi(\sigma) = -1) = \frac{Z^{e_1}(d)}{2 Z_{\rm ev}(d)}$. Under $\mathbb{P}_{\rm joint}$, the pair $\big(C^{(1-\sigma_j)/2} x_j,\, x_{j+1}\big)$ has exact density $p_+^{(j)}$ — namely the two-slice marginal $(U(0), U(l_j))$ of the one-axis thermal mixture $\mathbb{P}_{\rm mix}^{(d)} := \frac{Z^0(d)}{2 Z_{\rm ev}(d)} \mathbb{P}_0^{(d)} + \frac{Z^{e_1}(d)}{2 Z_{\rm ev}(d)} \mathbb{P}_{e_1}^{(d)}$ with the twist of $\mathbb{P}_{e_1}^{(d)}$ placed in the complementary arc $[l_j, d]$.
2. **(Exact marginal denominator cancellation).** The marginal density of $(x_j, x_{j+1})$ under $\Pr_{\rm ev}$ is $p_{\rm ev}^{(j)} = \frac{1}{2}(p_+^{(j)} + p_-^{(j)}) = \frac{K_l^{\rm ev}(x, y) K_{d-l}^{\rm ev}(y, x)}{Z_{\rm ev}(d)}$, and $b_j = \frac{p_+^{(j)} - p_-^{(j)}}{p_+^{(j)} + p_-^{(j)}}$. Consequently $K_l^{\rm ev}(x, y)$ cancels identically in the following three exact expectations:
   $$
   \mathbb{E}_{\rm ev}\big[|b_j|\big] = d_{\rm TV}\!\big(p_+^{(j)},\, p_-^{(j)}\big) = \frac{1}{Z_{\rm ev}(d)} \iint \big|K_l^{\rm od}(x, y)\big|\, K_{d-l}^{\rm ev}(y, x)\, dx\, dy, \tag{2.3}
   $$
   $$
   \mathbb{E}_{\rm ev}\big[1 - |b_j|\big] = 1 - d_{\rm TV}\!\big(p_+^{(j)},\, p_-^{(j)}\big) = \iint \min\!\big(p_+^{(j)}(x, y),\, p_-^{(j)}(x, y)\big)\, dx\, dy, \tag{2.4}
   $$
   $$
   \mathbb{E}_{\rm ev}\!\big[\sqrt{1 - b_j^2}\big] = H_{\rm aff}\!\big(p_+^{(j)},\, p_-^{(j)}\big) := \iint \sqrt{p_+^{(j)}(x, y)\, p_-^{(j)}(x, y)}\, dx\, dy. \tag{2.5}
   $$
3. **(Exact Markov-bridge conditional expectation).** For every $0 \le j \le m - 2$, setting $L_{\rm rem}(j) := \sum_{k=j+1}^{m-1} l_k$,
   $$
   \mathbb{E}_{\rm ev}\!\big[|b_j| \mid x_0, \dots, x_j\big] = \frac{\int |K_{l_j}^{\rm od}(x_j, y)|\, K_{L_{\rm rem}(j)}^{\rm ev}(y, x_0)\, dy}{K_{l_j + L_{\rm rem}(j)}^{\rm ev}(x_j, x_0)}. \tag{2.6}
   $$
4. **(Two-sided ambiguity bounds and predictor / variational tests).** For every $j$,
   $$
   \Pr_{\rm ev}\!\big(|b_j| > \tfrac{1}{2}\big) \le 2\, d_{\rm TV}\!\big(p_+^{(j)},\, p_-^{(j)}\big), \tag{2.7}
   $$
   $$
   \Pr_{\rm ev}\!\big(|b_j| \le \tfrac{1}{2}\big) \le \min\!\left\{2\Big(1 - d_{\rm TV}\!\big(p_+^{(j)},\, p_-^{(j)}\big)\Big),\;\; \frac{2}{\sqrt{3}}\, H_{\rm aff}\!\big(p_+^{(j)},\, p_-^{(j)}\big)\right\}. \tag{2.8}
   $$
   For every measurable $C$-odd function $f(x, y)$ ($f(Cx, y) = -f(x, y)$ a.e.) with $\|f\|_\infty \le 1$, and every measurable $C$-odd sign predictor $\hat\sigma(x, y) \in \{-1, +1\}$ ($\hat\sigma(Cx, y) = -\hat\sigma(x, y)$ a.e.),
   $$
   \mathbb{E}_{\rm ev}\big[|b_j|\big] = d_{\rm TV}\!\big(p_+^{(j)},\, p_-^{(j)}\big) \ge \mathbb{E}_{p_+^{(j)}}[f(x, y)], \qquad
   \Pr_{\rm ev}\!\big(|b_j| \le \tfrac{1}{2}\big) \le 4\, \mathbb{P}_{p_+^{(j)}}\!\big(\hat\sigma(x, y) = -1\big). \tag{2.9}
   $$

*Proof.* First verify normalization of $p_+^{(j)}$: $\iint K_l(x, y) K_{d-l}^{\rm ev}(y, x)\, dx\, dy = \operatorname{Tr}(T^l P_{\rm ev} T^{d-l}) = \operatorname{Tr}(P_{\rm ev} T^d) = Z_{\rm ev}(d)$. Since $K_{d-l}^{\rm ev}(y, Cx) = K_{d-l}^{\rm ev}(y, x)$ and $C$ preserves Haar measure, $p_-^{(j)} = (C \times I)_* p_+^{(j)}$ is also normalized.
(1) Summing (2.2) over $\sigma \in \{\pm 1\}^m$ factors across arcs into $\prod_k K_{l_k}^{\rm ev}(x_k, x_{k+1}) / Z_{\rm ev}(d) = d\Pr_{\rm ev}$, and the ratio of $\sigma_k = +1$ to $\sigma_k = -1$ weights given $x$ is $K_{l_k}(x_k, x_{k+1})/K_{l_k}(Cx_k, x_{k+1})$, giving $\mathbb{E}[\sigma_k \mid x] = b_k$. For any fixed $\sigma$, defining $\tilde x_k := C^{s_k} x_k$ with $s_j = (1-\sigma_j)/2$ and $s_{k+1} \equiv s_k + (1-\sigma_k)/2 \pmod 2$ for $k = j+1, \dots, j-1$ absorbs every flip except the total parity $\Pi(\sigma)$ placed on arc $j-1$ (in the complementary arc $[l_j, d]$). Each of the $2^{m-1}$ strings with $\Pi(\sigma) = +1$ (resp. $-1$) thus has total weight $2^{-m} Z^0(d)/Z_{\rm ev}(d)$ (resp. $2^{-m} Z^{e_1}(d)/Z_{\rm ev}(d)$) and marginal $(U(0), U(l_j))$ of $\mathbb{P}_0^{(d)}$ (resp. $\mathbb{P}_{e_1}^{(d)}$ with the twist in $[l_j, d]$). Summing over $\sigma$ yields density $p_+^{(j)}$ for $(C^{(1-\sigma_j)/2} x_j, x_{j+1})$.
(2) Integrating out all $x_k$ ($k \notin \{j, j+1\}$) in (1.1) using $(P_{\rm ev} T^a)(P_{\rm ev} T^b) = P_{\rm ev} T^{a+b}$ gives $p_{\rm ev}^{(j)} = \frac{1}{2}(p_+^{(j)} + p_-^{(j)})$. Direct substitution of $b_j = (p_+^{(j)} - p_-^{(j)})/(p_+^{(j)} + p_-^{(j)})$ gives $p_{\rm ev}^{(j)} |b_j| = \frac{1}{2}|p_+^{(j)} - p_-^{(j)}|$, $p_{\rm ev}^{(j)}(1 - |b_j|) = \min(p_+^{(j)}, p_-^{(j)})$, and $p_{\rm ev}^{(j)}\sqrt{1 - b_j^2} = \sqrt{p_+^{(j)} p_-^{(j)}}$; integrating yields (2.3)–(2.5).
(3) By the Markov property of (1.1) along the circle, the conditional density of $x_{j+1} = y$ given $(x_0, \dots, x_j)$ is $K_{l_j}^{\rm ev}(x_j, y) K_{L_{\rm rem}(j)}^{\rm ev}(y, x_0) / K_{l_j + L_{\rm rem}(j)}^{\rm ev}(x_j, x_0)$; multiplying by $|b_j| = |K_{l_j}^{\rm od}|/K_{l_j}^{\rm ev}$ cancels $K_{l_j}^{\rm ev}$ and gives (2.6).
(4) Equation (2.7) is Markov's inequality applied to (2.3). Equation (2.8) uses $\mathbf{1}_{\{|b_j| \le 1/2\}} \le 2(1 - |b_j|)$ and $\mathbf{1}_{\{|b_j| \le 1/2\}} \le \frac{2}{\sqrt{3}}\sqrt{1 - b_j^2}$ with (2.4)–(2.5). For (2.9), $C$-oddness gives $\mathbb{E}_{p_-^{(j)}}[f] = -\mathbb{E}_{p_+^{(j)}}[f]$, so $\mathbb{E}_{p_+^{(j)}}[f] = \frac{1}{2}\iint f (p_+^{(j)} - p_-^{(j)}) \le \frac{1}{2}\iint |p_+^{(j)} - p_-^{(j)}| = d_{\rm TV}(p_+^{(j)}, p_-^{(j)})$. Specializing to $f = \hat\sigma$ gives $1 - d_{\rm TV}(p_+^{(j)}, p_-^{(j)}) \le 1 - \mathbb{E}_{p_+^{(j)}}[\hat\sigma] = 2 \mathbb{P}_{p_+^{(j)}}(\hat\sigma = -1)$, and substituting into (2.8) yields the second bound in (2.9). $\square$

---

### 2.2 Exact Spectral Cauchy–Schwarz Bridge (PROVED)

Let $\lambda_0 := \|P_{\rm ev} T\|_{\rm op} > 0$ be the unique Perron–Frobenius vacuum eigenvalue of $T$, and define the normalized even and odd thermal sums
$$
S_{\rm ev}(t) := \frac{Z_{\rm ev}(t)}{\lambda_0^t} - 1 = \sum_{i \ge 1,\, {\rm ev}} \left(\frac{\lambda_i^{\rm ev}}{\lambda_0}\right)^t \ge 0, \qquad
S_{\rm od}(t) := \frac{Z_{\rm od}(t)}{\lambda_0^t} = \sum_{\alpha \in {\rm od}} \left(\frac{\lambda_\alpha^{\rm od}}{\lambda_0}\right)^t > 0.
$$

**Theorem 2 (Exact Spectral Cauchy–Schwarz Bridge — No Rough-Cut Wall; PROVED).**
For every $d \ge 9$ (so $m = \lfloor\sqrt{d}\rfloor \ge 3$ and $2 l_j < d$ for every $j = 0, \dots, m-1$):
1. For every arc $j \in \{0, \dots, m-1\}$,
   $$
   \mathbb{E}_{\rm ev}\big[|b_j|\big] = d_{\rm TV}\!\big(p_+^{(j)},\, p_-^{(j)}\big)
   \le \frac{\sqrt{Z_{\rm od}(2 l_j)\, Z_{\rm ev}(2d - 2 l_j)}}{Z_{\rm ev}(d)}
   \le \sqrt{\frac{S_{\rm od}(2 l_j)}{1 + S_{\rm ev}(d)}}
   \le \sqrt{S_{\rm od}(2 l_j)}. \tag{2.10}
   $$
2. For every $c > 0$ with $m > c \log n$,
   $$
   \Pr_{\rm ev}\!\left\{\#\{j : |b_j| \le \tfrac{1}{2}\} < c \log n\right\}
   \le \frac{2 m}{m - c \log n} \max_{0 \le j < m} \frac{\sqrt{Z_{\rm od}(2 l_j)\, Z_{\rm ev}(2d - 2 l_j)}}{Z_{\rm ev}(d)}
   \le \frac{2 m}{m - c \log n} \max_{0 \le j < m} \sqrt{\frac{S_{\rm od}(2 l_j)}{1 + S_{\rm ev}(d)}}. \tag{2.11}
   $$

*Proof.* First check $2 l_j < d$ for all $d \ge 9$: for $d \in \{9, \dots, 15\}$, $m = 3$ and direct inspection gives $2\lceil d/3\rceil \in \{6, 8, 8, 8, 10, 10, 10\} < d$; for $d \ge 16$, $m \ge 4$ and $2 l_j \le 2\lceil d/m \rceil < 2(d/4 + 1) = d/2 + 2 < d$.
(1) Applying Cauchy–Schwarz in $L^2(dx\, dy)$ to (2.3) gives
$$
\mathbb{E}_{\rm ev}\big[|b_j|\big] \le \frac{1}{Z_{\rm ev}(d)} \left(\iint K_{l_j}^{\rm od}(x, y)^2\, dx\, dy\right)^{1/2} \left(\iint K_{d-l_j}^{\rm ev}(y, x)^2\, dx\, dy\right)^{1/2} = \frac{\sqrt{Z_{\rm od}(2 l_j)\, Z_{\rm ev}(2d - 2 l_j)}}{Z_{\rm ev}(d)},
$$
since $\|P_{\rm od} T^{l_j}\|_{\rm HS}^2 = \operatorname{Tr}(P_{\rm od} T^{2 l_j}) = Z_{\rm od}(2 l_j)$ and $\|P_{\rm ev} T^{d-l_j}\|_{\rm HS}^2 = Z_{\rm ev}(2d - 2 l_j)$. Because $2d - 2 l_j > d$ and every even eigenvalue satisfies $0 \le \lambda_i^{\rm ev} \le \lambda_0$, we have $Z_{\rm ev}(2d - 2 l_j) = \sum_{i \in {\rm ev}} (\lambda_i^{\rm ev})^{2d - 2 l_j} \le \lambda_0^{d - 2 l_j} Z_{\rm ev}(d)$. Substituting this gives
$$
\frac{\sqrt{Z_{\rm od}(2 l_j)\, Z_{\rm ev}(2d - 2 l_j)}}{Z_{\rm ev}(d)} \le \sqrt{\frac{Z_{\rm od}(2 l_j)}{\lambda_0^{2 l_j}} \cdot \frac{\lambda_0^d}{Z_{\rm ev}(d)}} = \sqrt{\frac{S_{\rm od}(2 l_j)}{1 + S_{\rm ev}(d)}} \le \sqrt{S_{\rm od}(2 l_j)}.
$$
(2) Write $m - N_{\rm amb} = \sum_{j=0}^{m-1} \mathbf{1}_{\{|b_j| > 1/2\}}$. By Markov's inequality, (2.7), and (2.10),
$$
\Pr_{\rm ev}(N_{\rm amb} < c \log n) = \Pr_{\rm ev}(m - N_{\rm amb} > m - c \log n) \le \frac{\sum_{j=0}^{m-1} \Pr_{\rm ev}(|b_j| > 1/2)}{m - c\log n} \le \frac{2 m}{m - c\log n} \max_j \mathbb{E}_{\rm ev}[|b_j|],
$$
which gives (2.11). $\square$

*Structural contrast with `BC(eps)` of check 1556 / rows 1565–1568:* For `BC(eps)`, even assuming a volume-uniform mass gap and full thermal-sum control at $\beta \in [2, 3]$ failed to yield the bound because of the `sup_{s, t}` rough-cut wall of $2n^2$ excited boundary plaquettes (row 1566 A2; row 1568 Theorem 2 Failure 1b). Theorem 2 shows that `(L-tail)` has **no rough-cut wall**: any spectral bound $S_{\rm od}(2 l_j)/(1 + S_{\rm ev}(d)) \le C n^{-2\epsilon}$ at the shorter time $2 l_j \approx 2\sqrt{d}$ immediately implies `(L-tail)` (in fact with $N_{\rm amb} \ge m/2$ rather than $c\log n$).

---

### 2.3 Exact Untwisted Hölder Flux Lower Bound (PROVED)

We next prove the exact dual (converse-side) spectral bound relating $r_1(d) = Z_{\rm od}(d)/Z_{\rm ev}(d)$ and $\mathbb{E}_{\rm ev}[|b_j|]$ to ordinary untwisted periodic two-point functions of any bounded $C$-odd spatial-slice observable $W$.

**Theorem 3 (Exact Untwisted Hölder Flux Bound and Arc-Bias Lower Bound; PROVED).**
Let $W \in L^\infty(G^{\mathcal{E}})$ be any real-valued gauge-invariant observable satisfying $W(Cx) = -W(x)$ a.e. and $\|W\|_\infty > 0$. Write $\mathbb{E}_0[\cdot]$ for expectation in the ordinary untwisted periodic Wilson torus $\mathbb{P}_0^{(d)}$ of period $d$, and for $t \in \{1, \dots, d-1\}$ put
$$
G_W(t) := \frac{\operatorname{Tr}\!\big(P_{\rm ev} W T^t W T^{d-t}\big)}{Z_{\rm ev}(d)} = \mathbb{E}_{p_+^{(t)}}\!\big[W(x) W(y)\big] \ge 0,
$$
where $p_+^{(t)}(x, y) = K_t(x, y) K_{d-t}^{\rm ev}(y, x)/Z_{\rm ev}(d)$. Then:
1. **(Exact untwisted-to-even decomposition).** For every $t \in \{1, \dots, d-1\}$,
   $$
   \mathbb{E}_0\big[W(U(0))\, W(U(t))\big] = \frac{G_W(t) + G_W(d - t)}{1 + r_1(d)}. \tag{2.12}
   $$
2. **(Exact Hölder bound on $G_W(t)$ and $\mathbb{E}_0[W(U(0)) W(U(t))]$).** For every $t \in \{1, \dots, d-1\}$,
   $$
   0 \le G_W(t) \le \big(\mathbb{E}_{\rm ev}[W^2]\big)^{1 - t/d} \big(\|W\|_\infty^2\, r_1(d)\big)^{t/d} \le \|W\|_\infty^2\, r_1(d)^{t/d}, \tag{2.13}
   $$
   and hence on the ordinary untwisted periodic torus $\mathbb{P}_0^{(d)}$:
   $$
   0 \le \mathbb{E}_0\big[W(U(0))\, W(U(t))\big] \le \|W\|_\infty^2\, \frac{r_1(d)^{t/d} + r_1(d)^{1 - t/d}}{1 + r_1(d)} \le 2 \|W\|_\infty^2\, r_1(d)^{\min(t, d-t)/d}. \tag{2.14}
   $$
   In particular, at half-period $t = d/2$ ($d$ even),
   $$
   r_1(d) = \frac{Z_{\rm od}(d)}{Z_{\rm ev}(d)} \ge \left(\frac{\mathbb{E}_0[W(U(0))\, W(U(d/2))]}{2 \|W\|_\infty^2}\right)^2. \tag{2.15}
   $$
3. **(Arc-bias lower bound from untwisted two-point correlation).** For every arc $j$ of length $l_j$,
   $$
   \mathbb{E}_{\rm ev}\big[|b_j|\big] \ge \frac{G_W(l_j)}{\|W\|_\infty^2} \ge \frac{\mathbb{E}_0[W(U(0))\, W(U(l_j))]}{\|W\|_\infty^2} - r_1(d)^{1 - l_j/d}. \tag{2.16}
   $$

*Proof.* (1) Since $W$ is $C$-odd, $W P_{\rm ev} = P_{\rm od} W$ and $W P_{\rm od} = P_{\rm ev} W$, while $T$ commutes with $P_{\rm ev}, P_{\rm od}$. Thus $W T^t W P_{\rm ev} = P_{\rm ev} W T^t W$, which verifies $\mathbb{E}_{p_+^{(t)}}[W(x) W(y)] = Z_{\rm ev}(d)^{-1} \operatorname{Tr}(W T^t W P_{\rm ev} T^{d-t}) = G_W(t)$. On the untwisted torus, splitting $I = P_{\rm ev} + P_{\rm od}$ and using cyclicity of trace gives
$$
\operatorname{Tr}(P_{\rm od} W T^t W T^{d-t}) = \operatorname{Tr}(W P_{\rm ev} T^t W P_{\rm od} T^{d-t}) = \operatorname{Tr}(P_{\rm ev} W T^{d-t} W T^t) = Z_{\rm ev}(d)\, G_W(d - t).
$$
Summing with $\operatorname{Tr}(P_{\rm ev} W T^t W T^{d-t}) = Z_{\rm ev}(d)\, G_W(t)$ and dividing by $Z^0(d) = Z_{\rm ev}(d)(1 + r_1(d))$ yields (2.12).
(2) Expand $G_W(t)$ in orthonormal eigenbases $\{|i\rangle\}$ of $P_{\rm ev} T$ (eigenvalues $\lambda_i^{\rm ev} \ge 0$) and $\{|\alpha\rangle\}$ of $P_{\rm od} T$ (eigenvalues $\lambda_\alpha^{\rm od} \ge 0$), putting $w_{i\alpha} := |\langle i | W | \alpha \rangle|^2 \ge 0$:
$$
Z_{\rm ev}(d)\, G_W(t) = \sum_{i \in {\rm ev}} \sum_{\alpha \in {\rm od}} (\lambda_i^{\rm ev})^{d-t} (\lambda_\alpha^{\rm od})^t\, w_{i\alpha} \ge 0.
$$
Applying Hölder's inequality with conjugate exponents $p = \frac{d}{d-t}$ and $q = \frac{d}{t}$ gives
$$
Z_{\rm ev}(d)\, G_W(t) \le \left(\sum_{i, \alpha} (\lambda_i^{\rm ev})^d w_{i\alpha}\right)^{1 - t/d} \left(\sum_{i, \alpha} (\lambda_\alpha^{\rm od})^d w_{i\alpha}\right)^{t/d}.
$$
Since $W |i\rangle \in \operatorname{ran} P_{\rm od}$ and $W |\alpha\rangle \in \operatorname{ran} P_{\rm ev}$, Parseval gives $\sum_\alpha w_{i\alpha} = \langle i | W^2 | i \rangle$ and $\sum_i w_{i\alpha} = \langle \alpha | W^2 | \alpha \rangle \le \|W\|_\infty^2$. Thus the first sum is $\operatorname{Tr}(P_{\rm ev} T^d W^2) = Z_{\rm ev}(d)\, \mathbb{E}_{\rm ev}[W^2]$ and the second is at most $\|W\|_\infty^2 Z_{\rm od}(d)$. Dividing by $Z_{\rm ev}(d)$ gives (2.13). Substituting (2.13) at $t$ and $d - t$ into (2.12) gives (2.14) (using $r_1(d) \le 1$, so $r_1(d)^{t/d} + r_1(d)^{1-t/d} \le 2 r_1(d)^{\min(t, d-t)/d}$). Setting $t = d/2$ in (2.14) and dropping $1 + r_1(d) \ge 1$ yields (2.15).
(3) Taking $f(x, y) := W(x) W(y) / \|W\|_\infty^2$ (which is $C$-odd in $x$ with $\|f\|_\infty \le 1$) in (2.9) yields $\mathbb{E}_{\rm ev}[|b_j|] \ge G_W(l_j)/\|W\|_\infty^2$. From (2.12) and (2.13) at $d - l_j$, $G_W(l_j) = (1 + r_1(d)) \mathbb{E}_0[W(U(0)) W(U(l_j))] - G_W(d - l_j) \ge \mathbb{E}_0[W(U(0)) W(U(l_j))] - \|W\|_\infty^2 r_1(d)^{1 - l_j/d}$, proving (2.16). $\square$

---

## 3. Separate Verdict on the Calibrated Trajectory $\beta_K$ and All Selectivity / Control Tests

### 3.1 Separate Analysis Along the Calibrated Trajectory $\beta_K$ (and Weak-Coupling Scaling)

Along the calibrated release trajectory $\beta_K$ (credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text; rows 1451, 1453, 1461, 1465), the physical torus side $\ell \in 1024\mathbb{N}$, block factor $b$, and calibration level $g_0$ are **fixed**, while the cutoff $K \to \infty$, $n = \ell b^K \to \infty$, lattice spacing $a_K = b^{-K} \to 0$, and $\beta_K / \log(b^K) \to \frac{11}{3\pi^2}$. Crucially:
- The **physical** 4-torus $\mathbb{T}_\ell^3 \times S_D^1$ ($D = d a_K \in \{\ell/512, \ell/256\}$) is **FIXED** independent of $K$.
- The **physical** duration of each of the $m = \lfloor \sqrt{d} \rfloor$ arcs is $\Delta\tau_j = l_j a_K \asymp \sqrt{\ell}\, b^{-K/2} \to 0$.

**Theorem 4 (Obstruction to `(L-tail)` along the calibrated trajectory $\beta_K$, and unconditional weak-coupling refutation; PROVED / PROVED GIVEN).**
1. **(Continuum incompatibility along $\beta_K$ — PROVED conditional implication).** Fix $(\ell, g_0)$. If `(L-tail)` holds along a subsequence of calibrated cutoffs $(n_K, \beta_K)$ with $n_K = \ell b^K \to \infty$, then:
   - By (1.3), $r_1(d_K) = Z_{\rm od}(d_K)/Z_{\rm ev}(d_K) \le \rho_{d_K} \to 0$ (equivalently $Z^{e_1}(d_K)/Z^0(d_K) \to 1$ on the fixed physical 4-torus $\mathbb{T}_\ell^3 \times S_D^1$).
   - By Theorem 3 (2.14), for **every** sequence of uniformly bounded gauge-invariant $C_1$-odd spatial-slice observables $W_K$ ($\|W_K\|_\infty \le 1$) and **every** fixed physical time fraction $\alpha \in (0, 1)$ (taking $t_K = \lfloor \alpha d_K \rfloor$),
     $$
     \lim_{K \to \infty} \mathbb{E}_0^{(d_K, \beta_K)}\!\big[W_K(U(0))\, W_K(U(t_K))\big] = 0. \tag{3.1}
     $$
   Thus `(L-tail)` along $\beta_K$ is **mathematically incompatible** with any continuum limit on $\mathbb{T}_\ell^3 \times S_D^1$ possessing a nontrivial finite-energy electric-flux sector (i.e. any fixed-physical-scale bounded $C_1$-odd observable, such as a smeared or blocked spatial Polyakov loop on $\mathbb{T}_\ell^3$, whose two-point function stays strictly positive at separation $\tau = \alpha D > 0$, or equivalently finite continuum electric-flux energy $E_{\rm flux}^{\rm phys}(\ell) < \infty$).
   - **Equivalently via exact coarse blocking (Lemma TW of row 1468 §3.2):** Under any centre-equivariant probability block map sending $(n_K^3 \times d_K)$ to the fixed finite coarse lattice $(\ell^3 \times D)$ ($D \in \{\ell/512, \ell/256\}$), $Z^{e_1}(d_K)/Z^0(d_K) = Z_{\rm eff, K}^{e_1}(D; \ell)/Z_{\rm eff, K}^0(D; \ell)$ is preserved identically; thus `(L-tail)` along $\beta_K$ is incompatible with any coarse effective limit satisfying $\limsup_K Z_{\rm eff, K}^{e_1}(D; \ell)/Z_{\rm eff, K}^0(D; \ell) < 1$ on the fixed finite torus $\ell^3 \times D$.
2. **(Short-arc physical-duration obstruction along $\beta_K$ — PROVED conditional implication).** Even if the consumer right-hand side of `(L-tail)` were relaxed from $C_0 n^{-\epsilon}$ to a fixed small constant $\delta(\ell) > 0$, if there exists a sequence of $\pm 1$-valued $C_1$-odd spatial observables $W_K$ (e.g. signs of fixed-physical-scale smeared spatial Polyakov loops) that are mean-square continuous at vanishing physical time separation $\Delta\tau_K = l_j b^{-K} \to 0$ (meaning $\mathbb{E}_{p_+^{(j)}}[W_K(x) W_K(y)] \to 1$ as $K \to \infty$), then by (2.8)–(2.9),
   $$
   \mathbb{E}_{\rm ev}\big[|b_j|\big] \ge \mathbb{E}_{p_+^{(j)}}\!\big[W_K(x) W_K(y)\big] \longrightarrow 1, \qquad
   \Pr_{\rm ev}\!\big(|b_j| \le \tfrac{1}{2}\big) \le 2\Big(1 - \mathbb{E}_{p_+^{(j)}}\!\big[W_K(x) W_K(y)\big]\Big) \longrightarrow 0
   $$
   on every arc $j$. (In fact, for a vector $\mathbf{W}_K \in \mathbb{R}^N$ of $N \ge 3$ fixed-physical-scale smeared winding loops with $\hat\sigma(x, y) = \operatorname{sgn}(\mathbf{W}_K(x) \cdot \mathbf{W}_K(y))$, heuristic diffusive scaling gives $\Pr_{p_+}(\hat\sigma = -1) \lesssim (\Delta\tau_K)^{N/2} = o(1/m)$, driving $\mathbb{E}_{\rm ev}[N_{\rm amb}] \to 0$, **ARGUED**.)
3. **(Unconditional refutation of `(L-tail)` at weak-coupling scaling $\beta(n) \gg n^2 / \log n$ and at fixed $(n, d), \beta \to \infty$ — PROVED GIVEN checked row 1143/1144).** Let $K > 0$ be the absolute constant of row 1143 (7) (`library/gap-solve-astra62.md`, lines 112–140, checked in row 1144). For every 4D $\mathrm{SU}(2)$ Wilson torus $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/d)$ with $n \ge 3$, $d \in \{u, 2u\}$ even, and every $\beta \ge \max(4, 2K)$,
   $$
   r_1(d) = \frac{Z_{\rm od}(d)}{Z_{\rm ev}(d)} \ge \frac{1}{64} \left(1 - \frac{K}{\beta}\right)^{n d} \ge \frac{1}{64} \exp\!\left(-\frac{K n^2}{128 \beta}\right). \tag{3.2}
   $$
   In particular, `(L-tail)` (and `(N-flux)`) **FAILS UNCONDITIONALLY** along any bare sequence $\beta(n) \ge \max(4, 2K)$ satisfying $\frac{n^2}{\beta(n) \log n} \to 0$ (e.g. $\beta(n) = n^2$), and no constants $(c, \epsilon, C_0)$ uniform in $\beta \in [2, \infty)$ can exist (Remark STAB / test (g5); at fixed $(n, d)$ and $\beta \to \infty$, row 1143 (6) also gives $r_1(d) \to 1$).

*Proof.* Parts (1) and (2) follow immediately from Proposition 1.1(1), Theorem 1 (2.8)–(2.9), and Theorem 3 (2.14). For Part (3), let $W = P_1 = \frac{1}{2}\operatorname{tr} H_1$ be the straight spatial winding loop in direction $1$, which is gauge-invariant, $C_1$-odd, and satisfies $\|P_1\|_\infty = 1$. By row 1143 line 139 (checked in row 1144), for every even $d > t \ge 1$ and $\beta \ge \max(4, 2K)$, $4 \mathbb{E}_0[P_1(0) P_1(t)] \ge (1 - K/\beta)^{n t}$. Setting $t = d/2$ and substituting into Theorem 3 (2.15) gives
$$
r_1(d) \ge \left(\frac{\mathbb{E}_0[P_1(0) P_1(d/2)]}{2}\right)^2 \ge \frac{1}{64} \left(1 - \frac{K}{\beta}\right)^{n d}.
$$
Since $x = K/\beta \in (0, 1/2]$ and $1 - x \ge e^{-2x}$ on $[0, 1/2]$ (as $x \mapsto 1 - x - e^{-2x}$ is concave and nonnegative at $0$ and $1/2$), and $d \le 2u = n/256$ so $2 n d \le n^2 / 128$, we obtain (3.2). If $\frac{n^2}{\beta(n)\log n} \to 0$, then $r_1(d) = n^{-o(1)}$, contradicting $r_1(d) \le C_0 n^{-\epsilon} + n^{-c\log 2}$ for every $c, \epsilon, C_0 > 0$. $\square$

*Honest scope on $\beta_K$:* Because the calibrated trajectory has $\beta_K \sim \frac{11}{3\pi^2}\log n \ll n^2/\log n$, Part (3)'s bare-loop bound (3.2) does not by itself reach $\beta_K$ (bare winding loops suffer UV perimeter self-energy $e^{-c n/\beta_K}$). Refuting `(L-tail)` unconditionally on $\beta_K$ requires controlling fixed-physical-scale smeared/blocked winding observables across $K$ RG steps (or extending the release's coarse-torus control to rectangular and twisted tori, noted absent in row 1457). Part (1) nonetheless proves rigorously that `(L-tail)` on $\beta_K$ is the **wrong mathematical statement** for the continuum limit: `(PUR-io)` asks for a fixed constant margin $457/625$ on the fixed physical torus $\mathbb{T}_\ell^3 \times S_D^1$, whereas `(L-tail)` demands $n^{-\epsilon} \to 0$ decay with the UV cutoff $n = \ell b^K$ and splits time into $m = \lfloor\sqrt{d}\rfloor$ arcs of vanishing physical duration. Thus `(L-tail)` is strictly an **IR volume-scaling lemma at fixed bare coupling $\beta \in [2, 3]$**.

---

### 3.2 Exact $D$-Dimensional Free Maxwell + Compact Rotor Analysis (PROVED unconditionally)

We next test `(L-tail)` directly on the $D$-dimensional free Maxwell + compact harmonic rotor model ($D \ge 3$; row 929, check 1570).

**Theorem 5 (Exact Single-Arc Hellinger Bound in $D$-Dimensional Free Maxwell + Compact Rotor; PROVED unconditionally).**
Consider $D$-dimensional free compact-rotor Maxwell theory ($D \ge 3$) on $(\mathbb{Z}/n)^{D-1} \times (\mathbb{Z}/d)$ at fixed $\beta > 0$, $d \in \{n/512, n/256\}$ ($d \ge 9$), with compact $1$-direction harmonic mode $\Phi_1(t) \in \mathbb{R}/(2\pi\mathbb{Z})$ shifted by $\pi$ under $C_1$, and $p \ne 0$ transverse Gaussian modes. Set $\gamma_l := \frac{\beta n^{D-3}}{l}$.
1. **(Exact spectator factorization of $p \ne 0$ modes).** Modulo a well-defined $\mathrm{U}(1)$ spatial vertex gauge transformation $g(x) = \exp(i\pi\lambda(x))$ ($\lambda(x) = 1 - x_1/n$ for $1 \le x_1 \le n-1$, $\lambda(0, x_\perp) = 0$; row 1566 Lemma Z), $C_1$ acts solely by $\Phi_1 \mapsto \Phi_1 + \pi$ and fixes every $p \ne 0$ transverse mode identically. Hence $b_j$ depends solely on $(\Phi_1(x_j), \Phi_1(x_{j+1}))$, governed by the compact rotor kernel
   $$
   K_l^{\rm rot}(\phi, \psi) = \sum_{q \in \mathbb{Z}} e^{-\frac{q^2}{2\gamma_l}} e^{i q (\psi - \phi)} = \sqrt{2\pi\gamma_l} \sum_{k \in \mathbb{Z}} e^{-\frac{\gamma_l}{2}(\psi - \phi + 2\pi k)^2}. \tag{3.3}
   $$
2. **(Exact Hellinger upper bound for $\gamma_l \ge 1$).** Whenever $\gamma_{l_j} \ge 1$,
   $$
   H_{\rm aff}\!\big(p_+^{(j)},\, p_-^{(j)}\big) \le \sqrt{12\pi \gamma_{l_j}}\, e^{-\frac{\pi^2}{8}\gamma_{l_j}}, \qquad
   \Pr_{\rm ev}\!\big(|b_j| \le \tfrac{1}{2}\big) \le 4\sqrt{\pi \gamma_{l_j}}\, e^{-\frac{\pi^2}{8}\gamma_{l_j}}. \tag{3.4}
   $$
3. **(Dimensional verdicts for `(L-tail)` at fixed $\beta > 0$):**
   - **$D = 4$ (FAILS exponentially on every arc):** $\gamma_{l_j} = \frac{\beta n}{l_j} \ge c_4 \beta \sqrt{n}$, so by a union bound over all $m = \lfloor\sqrt{d}\rfloor$ arcs,
     $$
     \Pr_{\rm ev}\!\big(N_{\rm amb} \ge 1\big) \le 4 m \sqrt{\pi \gamma_{\max}}\, e^{-\frac{\pi^2}{8}\gamma_{\min}} = O\!\big(\beta^{1/2} n^{3/4} e^{-c' \beta \sqrt{n}}\big) \longrightarrow 0.
     $$
     Not even a single arc is ambiguous with probability tending to $1$.
   - **$D = 5$ (FAILS exponentially in $n^{3/2}$):** $\gamma_{l_j} = \frac{\beta n^2}{l_j} \ge c_5 \beta n^{3/2}$, so $\Pr_{\rm ev}(N_{\rm amb} \ge 1) \le O(\beta^{1/2} n^{5/4} e^{-c''\beta n^{3/2}}) \to 0$.
   - **$D = 3$ (HOLDS deterministically on every arc):** $\gamma_{l_j} = \frac{\beta}{l_j} \asymp \frac{\beta}{\sqrt{n}} \to 0$. Since $K_l^{\rm rot, od}(\Delta) = 2\sum_{q \ge 1\, {\rm odd}} e^{-q^2/(2\gamma_l)} \cos(q\Delta)$ and $K_l^{\rm rot, ev}(\Delta) = 1 + 2\sum_{q \ge 2\, {\rm even}} e^{-q^2/(2\gamma_l)} \cos(q\Delta)$, once $e^{-1/(2\gamma_l)} \le \frac{1}{8}$ (i.e. $l_j \ge 2\beta \log 8$) we have $|K_l^{\rm rot, od}| \le \frac{2 e^{-1/(2\gamma_l)}}{1 - e^{-4/\gamma_l}} \le \frac{1}{3}$ and $K_l^{\rm rot, ev} \ge 1 - \frac{2 e^{-2/\gamma_l}}{1 - e^{-6/\gamma_l}} \ge \frac{5}{6}$, giving $|b_j| \le \frac{2}{5} < \frac{1}{2}$ **uniformly on every arc** ($\Pr_{\rm ev}(N_{\rm amb} = m) = 1$ eventually). Thus in $D = 3$, `(L-tail)` is passed already by the massless free photon with zero confinement input.

*Proof.* (1) Verify the gauge map: for $g(x) = e^{i\pi\lambda(x)}$, $g(x) g(x+\hat 1)^{-1}$ equals $e^{-i\pi(1-1/n)} = -e^{i\pi/n}$ at $x_1 = 0$ and $e^{i\pi/n}$ for $1 \le x_1 \le n-1$, while $g(x) g(x+\hat j)^{-1} = 1$ for $j \ne 1$. Thus $g \cdot C_1$ multiplies every $1$-link uniformly by $e^{i\pi/n}$, shifting $\Phi_1 \mapsto \Phi_1 + \pi$ and leaving all $p \ne 0$ modes invariant. Because the free action splits additively between $\Phi_1$ and the $p \ne 0$ modes, the $p \ne 0$ modes cancel identically in $b_j$ (as in Proposition 1.2(1)). Equation (3.3) is Poisson summation with the row 929 / Theorem B harmonic variance $\gamma_l = \beta n^{D-3}/l$.
(2) Let $\Delta = (\psi - \phi) \bmod 2\pi \in [-\pi, \pi]$, put $u = \min(|\Delta|, \pi - |\Delta|) \in [0, \pi/2]$ and $v = \pi - u \in [\pi/2, \pi]$, so $\{K_l^{\rm rot}(\Delta), K_l^{\rm rot}(\Delta - \pi)\} = \{K_l^{\rm rot}(u), K_l^{\rm rot}(v)\}$. For $\gamma = \gamma_l \ge 1$:
- At $u \in [0, \pi/2]$: for $k \ne 0$, $(u + 2\pi k)^2 - u^2 \ge 2\pi^2 k^2$, so $\sum_{k \in \mathbb{Z}} e^{-\frac{\gamma}{2}(u + 2\pi k)^2} \le e^{-\frac{\gamma}{2}u^2}(1 + 2\sum_{k \ge 1} e^{-\pi^2 k^2}) \le 2 e^{-\frac{\gamma}{2}u^2}$.
- At $v \in [\pi/2, \pi]$: $2\pi - v \ge v$, and for $k \ge 1$ or $k \le -2$ the excess over $v^2$ is at least $6\pi^2 m^2$ ($m \ge 1$), so $\sum_{k \in \mathbb{Z}} e^{-\frac{\gamma}{2}(v + 2\pi k)^2} \le e^{-\frac{\gamma}{2}v^2}(2 + 2\sum_{m \ge 1} e^{-3\pi^2 m^2}) \le 3 e^{-\frac{\gamma}{2}v^2}$.
Since $u^2 + v^2 = u^2 + (\pi - u)^2 = \frac{\pi^2}{2} + 2(u - \frac{\pi}{2})^2 \ge \frac{\pi^2}{2}$, we obtain pointwise for all $(\phi, \psi) \in (S^1)^2$:
$$
\sqrt{K_l^{\rm rot}(\phi, \psi)\, K_l^{\rm rot}(C\phi, \psi)} \le \sqrt{2\pi \gamma}\, \sqrt{6}\, e^{-\frac{\gamma}{4}(u^2 + v^2)} \le \sqrt{12\pi \gamma}\, e^{-\frac{\pi^2}{8}\gamma}.
$$
Integrating against $K_{d-l}^{\rm rot, ev}(\psi, \phi) \frac{d\phi d\psi}{(2\pi)^2} / Z_{\rm ev}(d)$ in (2.5), using $\iint K_{d-l}^{\rm rot, ev}(\psi - \phi) \frac{d\phi d\psi}{(2\pi)^2} = 1$ (its $q = 0$ mode) and $Z_{\rm ev}(d) = \sum_{q\, {\rm even}} e^{-q^2/(2\gamma_d)} \ge 1$, proves the first inequality in (3.4). Multiplying by $\frac{2}{\sqrt{3}}$ in (2.8) gives the second (as $\frac{2}{\sqrt{3}}\sqrt{12\pi} = 4\sqrt{\pi}$).
(3) Immediate from (3.4) for $D = 4, 5$, and from the displayed $q$-sum bounds for $D = 3$ (noting $e^{-2/\gamma} \le (1/8)^4 = 2^{-12}$ when $e^{-1/(2\gamma)} \le 1/8$). $\square$

---

### 3.3 Remaining Control Models and Selectivity Summary Table

We collect all control verdicts for `(L-tail)`:
- **Weak 4D compact $\mathrm{U}(1)$ (Villain $\beta \ge 2000$ and Wilson $\beta_W \ge \beta_*$, existential) — FAILS (PROVED GIVEN checked rows 1565/1571):** Rows 1565/1571 prove $\Pr(Q \text{ odd}) \ge \eta > 0$ uniformly in $n, d$, hence $r_1(d) \ge \frac{\eta}{1 - \eta} > 0$, refuting (1.3) and therefore `(L-tail)` (as already noted in check 1585 §(v)).
- **Strong-coupling gapped twins — HOLDS with probability $1$ eventually (PROVED GIVEN checked row 1568 Theorem E / check 1572):** For $q = \frac{6(D-1)}{m_G}\beta < 1$ (4D $\mathrm{SU}(2)$ $\beta < 2/9$; 5D $\mathrm{SU}(2)$ $\beta < 1/6$; 4D $\mathrm{U}(1)$ $\beta < 1/9$; 3D $\mathrm{U}(1)$ $\beta < 1/6$), Theorem E of row 1568 integrated across the four corners of Theorem A gives, outside the Haar-null central-plaquette locus,
  $$
  \left|\log \frac{K_{l_j}(x_j, x_{j+1})}{K_{l_j}(Cx_j, x_{j+1})}\right| \le \frac{\pi^2}{2} n^{D-2} \cdot \frac{3\beta^2}{(1-q)^2}\, l_j\, q^{l_j - 2}.
  $$
  Since $l_j \ge \sqrt{n/512} - 1$ and $q < 1$, the right-hand side tends to $0$ exponentially in $\sqrt{n}$; once it is $\le \log 3$, every arc satisfies $|b_j| \le 1/2$ almost surely ($\Pr_{\rm ev}(N_{\rm amb} = m) = 1$).
- **Anisotropic 4D $\mathrm{SU}(2)$ with temporal coupling $b_t \in [2, 3]$ and spatial coupling $0 \le \kappa \le \kappa_*$ — HOLDS with probability $1$ eventually (PROVED GIVEN checked row 1565 §2 / check 1571):** Row 1565 §2 bounds the pinned mixed-derivative row sum uniformly in $(x, y)$ by $4 b_t^2 L n^2 e^{-a(l_j - 2)}$ ($a > 0$). Four-corner integration yields $|\log(K_{l_j}/K_{l_j, C})| \le 2\pi^2 b_t^2 L n^4 e^{-a(l_j - 2)} \to 0$, so again $|b_j| \le 1/2$ a.s. on every arc eventually. (As row 1565 notes, this anisotropic result also holds for abelian $\mathrm{U}(1)$ and in 5D, so it supplies no isotropic 4D selectivity.)
- **Weak 5D $\mathrm{SU}(2)$ ($\beta \in [2, 3]$, above the numerical transition $\beta_c^{\rm 5D} \approx 1.64$, GUIDE) — FAILS (ARGUED):** Under the belief-grade IR-free massless gluon phase of 5D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$ (row 1531), the twist cost scales as $\log(Z^0(d)/Z^{e_1}(d)) \asymp \beta_{\rm eff} n^2/d \asymp \beta_{\rm eff} n \to \infty$, driving $r_1(d) \to 1$ and refuting `(L-tail)`.

| Model / Regime | Verdict for `(L-tail)` | Key estimate / reason | Standing |
|---|---|---|---|
| 4D free Maxwell + compact rotor ($\beta > 0$) | **FAILS** | $\Pr_{\rm ev}(N_{\rm amb} \ge 1) \le C \beta^{1/2} n^{3/4} e^{-c\beta\sqrt{n}} \to 0$ | **PROVED** (Thm 5) |
| 5D free Maxwell + compact rotor ($\beta > 0$) | **FAILS** | $\Pr_{\rm ev}(N_{\rm amb} \ge 1) \le C \beta^{1/2} n^{5/4} e^{-c\beta n^{3/2}} \to 0$ | **PROVED** (Thm 5) |
| 3D free Maxwell + compact rotor ($\beta > 0$) | **HOLDS** | $|b_j| \le 2/5$ deterministically for $l_j \ge 2\beta\log 8$ | **PROVED** (Thm 5) |
| 4D compact $\mathrm{U}(1)$ Villain ($\beta \ge 2000$) & Wilson ($\beta_W \ge \beta_*$) | **FAILS** | $r_1(d) \ge \eta/(1-\eta) > 0$ | **PROVED GIVEN** 1565/1571 |
| 4D/5D $\mathrm{SU}(2)$ ($\beta < 2/9, 1/6$) & 4D/3D $\mathrm{U}(1)$ ($\beta < 1/9, 1/6$) | **HOLDS** | $|b_j| \le C n^{D-3/2} q^{\sqrt{n/512}} \to 0$ a.s. | **PROVED GIVEN** 1568/1572 |
| Anisotropic 4D $\mathrm{SU}(2)$ ($b_t \in [2,3]$, $0 \le \kappa \le \kappa_*$) | **HOLDS** | $|b_j| \le C n^4 e^{-a\sqrt{n/512}} \to 0$ a.s. | **PROVED GIVEN** 1565/1571 |
| 4D $\mathrm{SU}(2)$, $\beta(n) \gg n^2/\log n$ (and fixed $(n,d), \beta \to \infty$) | **FAILS** | $r_1(d) \ge \frac{1}{64} e^{-K n^2/(128\beta)}$ | **PROVED GIVEN** 1143/1144 (Thm 4(3)) |
| 4D $\mathrm{SU}(2)$ along calibrated trajectory $\beta_K$ (fixed $\ell, g_0$) | **INCOMPATIBLE WITH CONTINUUM ELECTRIC FLUX** | Kills every bounded $C_1$-odd two-point function at fixed physical $\tau \in (0, D)$; $\Delta\tau_j \to 0$ drives $|b_j| \to 1$ | **PROVED** conditional (Thm 4(1)–(2)) |
| 5D $\mathrm{SU}(2)$ weak coupling ($\beta \in [2, 3]$) | **FAILS** | Believed massless gluon phase, $r_1(d) \to 1$ | **ARGUED** (belief-grade) |
| 4D $\mathrm{SU}(2) \times$ neutral spectator | **BLIND** | Joint law of $(b_0, \dots, b_{m-1})$ identically unchanged | **PROVED** (Prop 1.2(1)) |
| **4D $\mathrm{SU}(2)$ isotropic, fixed $\beta \in [2, 3]$** | **OPEN** (expected **HOLDS**) | Requires 4D-selective order-one electric-flux confinement | **OPEN** (§4) |

---

## 4. Three Distinct Attacks on `(L-tail)` for 4D $\mathrm{SU}(2)$ Wilson at $\beta \in [2, 3]$

At fixed $\beta \in [2, 3]$, 4D $\mathrm{SU}(2)$ Wilson theory is believed to lie in a massive confining phase with correlation length $\xi(\beta) \in [1, 30]$ and string tension $\sigma(\beta) > 0$ (GUIDE), where $l_j \asymp \sqrt{n} \gg \xi(\beta) \log n$ and Theorem 2 predicts $\mathbb{E}_{\rm ev}[|b_j|] \le \sqrt{S_{\rm od}(2l_j)} \sim n e^{-\sigma(\beta) n \sqrt{d}} \to 0$. Hence `(L-tail)` is expected to **HOLD** (with all $m$ arcs ambiguous with overwhelming probability), and no refutation at $\beta \in [2, 3]$ is expected. Conversely, by Proposition 1.1, proving `(L-tail)` at $\beta = 3$ would prove rigorous electric-flux confinement $\lim_{n \to \infty} Z^{e_1}(n/512; n^3, \beta = 3)/Z^0(n/512; n^3, \beta = 3) = 1$, a major open non-perturbative problem.

We attack `(L-tail)` at $\beta \in [2, 3]$ by **three genuinely distinct methods**, proving exact structural identities and sharp barriers in each.

---

### 4.1 Attack 1: Spectral Cauchy–Schwarz Bridge and Exposed-Indicator Conditioning

Attack 1 uses the transfer-operator structure directly via Theorems 1 and 2, testing both the global spectral bridge (2.11) and check 1585's sequential conditional route $\mathbb{P}_{\rm ev}(G_j = 1 \mid G_0, \dots, G_{j-1}) \ge \eta \log n / m$.

**What succeeds (PROVED):** Unlike `BC(eps)` of check 1556, Theorem 2 completely removes the rough-cut wall: (2.11) proves that `(L-tail)` follows directly from the single spectral inequality $S_{\rm od}(2 l_j)/(1 + S_{\rm ev}(d)) \le C n^{-2\epsilon}$ on the physical thermal torus, with no boundary perturbations. Moreover, Theorem 1 (2.6) gives the exact Markov-bridge conditional bias $\mathbb{E}_{\rm ev}[|b_j| \mid x_0, \dots, x_j]$ with exact denominator cancellation.

**Exact failure points at $\beta \in [2, 3]$:**
1. *(Failure 1a — stronger-than-consumer premise in Theorem 2):* Since every odd eigenvalue obeys $\lambda_\alpha^{\rm od} < \lambda_0$ and $2 l_j < d$, $S_{\rm od}(2 l_j)$ is strictly decreasing in time, so
   $$
   S_{\rm od}(2 l_j) > S_{\rm od}(d) = \frac{Z_{\rm od}(d)}{\lambda_0^d} \ge \frac{Z_{\rm od}(d)}{Z_{\rm ev}(d)} = r_1(d).
   $$
   Thus controlling the numerator $S_{\rm od}(2 l_j)$ of Theorem 2 requires electric-flux decay already at the **shorter** period $2 l_j \approx 2\sqrt{d} \ll d$ — strictly stronger than `(N-flux)` at period $d$. (Retaining the denominator $1 + S_{\rm ev}(d)$ gives $\frac{S_{\rm od}(2l_j)}{1 + S_{\rm ev}(d)} = \frac{Z_{\rm od}(2l_j)}{Z_{\rm ev}(2l_j)} \cdot \frac{1 + S_{\rm ev}(2l_j)}{1 + S_{\rm ev}(d)}$, which still demands both shorter-period odd suppression and control of the neutral excitation ratio $(1 + S_{\rm ev}(2 l_j))/(1 + S_{\rm ev}(d))$.) Applying Cauchy–Schwarz to a product of $k$ arcs $\mathbb{E}_{\rm ev}[\prod_{r=1}^k |b_{j_r}|]$ likewise splits into products of $\|P_{\rm od} T^{l_{j_r}}\|_{\rm HS}$ and $\|P_{\rm ev} T^{g_r}\|_{\rm HS}$, hitting the same shorter-period wall.
2. *(Failure 1b — rare-tail conditioning barrier in check 1585's exposed-indicator route):* To prove $\mathbb{P}_{\rm ev}(G_j = 1 \mid G_0, \dots, G_{j-1}) \ge \frac{\eta \log n}{m}$ a.s., one must in particular lower-bound $\mathbb{P}_{\rm ev}(G_j = 1 \mid G_0 = \cdots = G_{j-1} = 0)$. Under the expected truth of `(L-tail)`, the conditioning event $\{G_0 = \cdots = G_{j-1} = 0\}$ is an **extreme rare-tail event** (for $j \asymp m$) that tilts $(x_0, x_j)$ toward atypical pin configurations maximizing $|b_0|, \dots, |b_{j-1}|$. Without a boundary-uniform lower bound on $\inf_{x_0, x_j} \mathbb{P}_{\rm ev}(|b_j| \le 1/2 \mid x_0, x_j)$ (blocked at $\beta \in [2, 3]$ by **Proposition CA-FAIL**, $\beta > 2 W_3 \approx 1.0109$, row 1072 / checks 1074–1075, and global Doeblin giving only $e^{-O(\beta n^3)}$), one has no control over the measure tilted by $\prod_{i < j} \mathbf{1}_{\{|b_i| > 1/2\}}$. Furthermore, Proposition 1.2(3) proves that this conditional route is strictly stronger than `(L-tail)` even on 4-state strictly positive transfer data.

---

### 4.2 Attack 2: Direct Haar-Preserving Seam-Spreading Maps and Jensen's Inequality Inside One Arc

Because $|b_j(x, y)| \le \frac{1}{2} \iff \frac{1}{3} \le \frac{K_l(Cx, y)}{K_l(x, y)} \le 3$, a second distinct attack seeks to lower-bound the single-arc partition-function ratio $\frac{K_l(Cx, y)}{K_l(x, y)}$ (for typical $(x, y) \sim p_+^{(j)}$) directly by a Haar-preserving change of variables $\Psi$ on the interior links $\Phi_{\rm int}$ of the slab $[0, l] \times (\mathbb{Z}/n)^3$ and Jensen's inequality, following the Mack–Petkova / Tomboulis / row-1171 paradigm.

We prove an exact KL/Jensen identity and an explicit **extensive barrier** showing that naive cut-flipping and smooth abelian/axis-field seam-spreading maps fail by powers of $n$ — **even in the strong-coupling Dobrushin regime**!

**Proposition 4.1 (Exact KL/Jensen Barrier and Extensive Cost of Single-Arc Seam Maps; PROVED).**
Fix an arc of length $l = l_j \ge 3$ and any Haar-preserving bijection $\Psi$ on the slab interior $\Phi_{\rm int}$ with action difference $\Delta S_\Psi(x, y; \Phi_{\rm int}) := S_{\rm int}(Cx, y; \Psi(\Phi_{\rm int})) - S_{\rm int}(x, y; \Phi_{\rm int})$ (where $S_{\rm int} = -\beta \sum_{p \in \mathcal{P}_{\rm slab}} \operatorname{Re} U_p$).
1. **(Exact KL defect of Jensen's inequality).** For every $(x, y)$,
   $$
   \log \frac{K_l(Cx, y)}{K_l(x, y)} = -\mathbb{E}_{\nu_{x, y}}\!\big[\Delta S_\Psi\big] + D_{\rm KL}\!\big(\Psi_* \nu_{x, y} \,\big\|\, \nu_{Cx, y}\big), \tag{4.1}
   $$
   where $\nu_{x, y}$ is the pinned-slab interior Gibbs law of $K_l(x, y)$. Thus Jensen's lower bound $\frac{K_l(Cx, y)}{K_l(x, y)} \ge e^{-\mathbb{E}_{\nu_{x, y}}[\Delta S_\Psi]}$ can reach the ambiguity threshold $\frac{1}{3}$ (i.e. $\mathbb{E}_{\nu_{x, y}}[\Delta S_\Psi] \le \log 3$) **only if** $D_{\rm KL}(\Psi_* \nu_{x, y} \| \nu_{Cx, y}) \le \log 3 + \log(K_l(Cx, y)/K_l(x, y)) = O(1)$ across all $n^2$ transverse columns (average KL mismatch $O(n^{-2})$ per column).
2. **(Exact one-plaquette positivity bound on $\mathbb{P}_{\rm ev}$).** For every $\beta > 0$, $n \ge 3$, $d \ge 2$, and every temporal $(0, 1)$-plaquette $p$ inside the untwisted arc $[0, l]$ of $p_+^{(j)}$,
   $$
   \mathbb{E}_{p_+^{(j)}}\!\big[\operatorname{Re} U_p\big] = \mathbb{E}_{\rm ev}\!\big[\operatorname{Re} U_{01}(0, x_\perp, t_*)\big] \ge \alpha(\beta) := \min\!\left(\frac{I_2(\beta)}{I_1(\beta)},\, \frac{1}{\beta}\right) > 0. \tag{4.2}
   $$
   For every $\beta \in [2, 3]$, $\alpha(\beta) \ge \frac{1}{3}$ and $\beta \alpha(\beta) \ge \frac{31}{36}$.
3. **(Exact area barrier for the interior cut-flip map at EVERY $\beta > 0$).** Let $\Psi_{\rm cut}$ flip the sign of all spatial $1$-links at $x_1 = 0$ on interior slices $t = 1, \dots, t_* := \lfloor l/2 \rfloor$ (leaving all other interior links fixed). Then $\Delta S_{\Psi_{\rm cut}} = 2\beta \sum_{x_\perp \in (\mathbb{Z}/n)^2} \operatorname{Re} P_{01}(0, x_\perp, t_*)$, and averaged over $(x, y) \sim p_+^{(j)}$:
   $$
   \mathbb{E}_{p_+^{(j)}}\!\big[\mathbb{E}_{\nu_{x, y}}[\Delta S_{\Psi_{\rm cut}}]\big] \ge 2\beta \alpha(\beta)\, n^2 \qquad (\forall \beta > 0), \tag{4.3}
   $$
   which is at least $\frac{31}{18} n^2$ uniformly on $\beta \in [2, 3]$ (and $\Theta(\beta^2 n^2) \to \infty$ even at $\beta = 0.01$ inside the strong-coupling Dobrushin regime!).
4. **(Smooth-spreading cost across the $(0, 1)$-plane).** Spreading the $\pi$-angle linearly in time across $l$ steps on $x_1 = 0$ about a covariant axis field $v$ (averaging $\pm\epsilon$ as in row 1171 eq. (10)) incurs quadratic temporal cost $\gtrsim \beta \frac{n^2}{l} \asymp \beta n^{3/2}$ even with zero axis error ($d_p = 0$). Spreading uniformly across all $n l$ plaquettes of each $(0, 1)$-plane (a $\pi/(n l)$ angle per plaquette) still incurs quadratic cost $\gtrsim \beta (l n^3) (\frac{\pi}{n l})^2 = \pi^2 \beta \frac{n}{l} \asymp \beta \sqrt{n} \to \infty$ (the exact abelian Coulomb barrier of Theorem 5), plus non-abelian covariant axis-gradient cost $\beta \sum_p d_p^2 a_p^2$. Localized vortex profiles of radius $R \sim \sqrt{\beta}$ (row 1171 eq. (9)–(10)) cost $O(n^2 \log^5(2+\beta))$.

*Proof.* (1) By Haar invariance of $\Psi$, $d(\Psi_* \nu_{x, y}) / d\nu_{Cx, y} = \frac{K_l(Cx, y)}{K_l(x, y)} e^{\Delta S_\Psi \circ \Psi^{-1}}$. Taking $\mathbb{E}_{\Psi_* \nu_{x, y}}[\log(\cdot)]$ gives $D_{\rm KL}(\Psi_* \nu_{x, y} \| \nu_{Cx, y}) = \log\frac{K_l(Cx, y)}{K_l(x, y)} + \mathbb{E}_{\nu_{x, y}}[\Delta S_\Psi]$, which is (4.1).
(2) On $\mathrm{SU}(2)$, the one-link convolution operator $C_e$ with kernel $e^{\beta \operatorname{Re}(u w^{-1})}$ is diagonal in the Peter–Weyl basis with eigenvalues $c_j(\beta) = \frac{1}{2j+1}\int_{\mathrm{SU}(2)} e^{\beta\operatorname{Re} g}\chi_j(g)\, dg = \frac{1}{2j+1}(I_{2j}(\beta) - I_{2j+2}(\beta)) = \frac{2}{\beta} I_{2j+1}(\beta) > 0$ ($j \in \frac{1}{2}\mathbb{Z}_{\ge 0}$). Differentiating $e^{\beta \operatorname{Re}(u w^{-1})}$ in $\beta$ shows that the operator $\widetilde{C}_e$ with kernel $\operatorname{Re}(u w^{-1}) e^{\beta \operatorname{Re}(u w^{-1})}$ is diagonal in the same Peter–Weyl basis with eigenvalues $c_j'(\beta)$. Using $I_\nu'(\beta) = \frac{\nu}{\beta} I_\nu(\beta) + I_{\nu+1}(\beta)$ at $\nu = 2j + 1$,
$$
\frac{c_j'(\beta)}{c_j(\beta)} = \frac{2j}{\beta} + \frac{I_{2j+2}(\beta)}{I_{2j+1}(\beta)} \ge \min\!\left(\frac{I_2(\beta)}{I_1(\beta)},\, \frac{1}{\beta}\right) = \alpha(\beta) > 0 \qquad \forall j \in \tfrac{1}{2}\mathbb{Z}_{\ge 0}.
$$
Hence $\widetilde{C}_e \succeq \alpha(\beta) C_e$ in Loewner operator order on $L^2(G_e)$, and tensoring with the positive operator $C_{\mathcal{E}\setminus\{e\}} \succeq 0$ gives $\widetilde{C}_e \otimes C_{\mathcal{E}\setminus\{e\}} \succeq \alpha(\beta) C_{\mathcal{E}}$. Under $p_+^{(j)}$ (whose interior arc $[0, l]$ carries no twist seam), inserting $\operatorname{Re} U_{01}(0, x_\perp, t_*)$ replaces $C_e$ by $\widetilde{C}_e$ in one time step of $T$:
$$
Z_{\rm ev}(d)\, \mathbb{E}_{p_+^{(j)}}\!\big[\operatorname{Re} U_{01}(0, x_\perp, t_*)\big]
= \operatorname{Tr}\!\Big(P e^{-V/2} P_{\rm ev} T^{d-1} e^{-V/2} P \cdot \big(\widetilde{C}_e \otimes C_{\mathcal{E}\setminus\{e\}}\big)\Big)
\ge \alpha(\beta)\, \operatorname{Tr}(P_{\rm ev} T^d) = \alpha(\beta)\, Z_{\rm ev}(d),
$$
since $P e^{-V/2} P_{\rm ev} T^{d-1} e^{-V/2} P \succeq 0$. This proves (4.2). For $\beta \in [2, 3]$, $\frac{I_2(\beta)}{I_1(\beta)} = \frac{c_0'(\beta)}{c_0(\beta)} = \mathbb{E}_{\text{1-link},\beta}[\operatorname{Re} g]$ has derivative $\operatorname{Var}_{\text{1-link},\beta}(\operatorname{Re} g) > 0$, so it is strictly increasing in $\beta$. At $\beta = 2$, exact series bounds give
$$
I_2(2) = \sum_{k=0}^\infty \frac{1}{k!(k+2)!} > \frac{1}{2} + \frac{1}{6} + \frac{1}{48} + \frac{1}{720} = \frac{31}{45},
$$
and (bounding the $k \ge 4$ tail geometrically by $\frac{1}{2880} \sum_{r \ge 0} 30^{-r} = \frac{1}{2784} < \frac{1}{1440}$)
$$
I_1(2) = \sum_{k=0}^\infty \frac{1}{k!(k+1)!} < 1 + \frac{1}{2} + \frac{1}{12} + \frac{1}{144} + \frac{1}{1440} = \frac{2291}{1440} < \frac{8}{5}.
$$
Hence $I_2(\beta)/I_1(\beta) \ge I_2(2)/I_1(2) > \frac{31/45}{8/5} = \frac{31}{72} > \frac{1}{3}$ for all $\beta \in [2, 3]$, giving $\alpha(\beta) \ge \frac{1}{3}$ and $\beta \alpha(\beta) = \min(\beta I_2(\beta)/I_1(\beta), 1) \ge \min(2 \cdot \frac{31}{72}, 1) = \frac{31}{36}$.
(3) Applying $\Psi_{\rm cut}$ changes only the $n^2$ temporal $(0, 1)$-plaquettes at $x_1 = 0, t = t_*$, flipping their sign from $+\beta \operatorname{Re} P_{01}$ to $-\beta \operatorname{Re} P_{01}$. Taking expectation under $p_+^{(j)}$ and applying (4.2) gives (4.3), which is at least $2 \cdot \frac{31}{36} n^2 = \frac{31}{18} n^2$ uniformly on $\beta \in [2, 3]$.
(4) Direct quadratic counting of $(1 - \cos\theta) \ge 2\theta^2/\pi^2$ for the stated profiles (with row 1171 eq. (10) for the localized vortex profile). $\square$

**Exact failure point of Attack 2:** Any single-map Jensen lower bound throws away the KL/cumulant fluctuations in (4.1) that cancel the extensive action shift $\mathbb{E}[\Delta S] = \Omega(n^2)$ (or $\Omega(\beta\sqrt{n})$) down to $O(1)$. Because this failure occurs even at $\beta = 0.01$ inside the Dobrushin regime, proving $|b_j| \le 1/2$ requires capturing interior measure cancellation / mixing rather than a single action-comparison bijection.

---

### 4.3 Attack 3: $\mathbb{Z}_2 \times \mathrm{SO}(3)$ Centre-Coset Disintegration, Explicit 4D $\mathbb{Z}_2$ Peierls Locking Theorem, and Slab Coupling

A third genuinely distinct attack exploits the fact that $C_1$ is a pure $\mathbb{Z}_2$ centre transformation leaving every $\mathrm{SO}(3)$ adjoint link invariant, following Mack–Petkova (1979) and Tomboulis (1981).

Choose a measurable section $V: \mathrm{SO}(3) \to \mathrm{SU}(2)$ and factor every link as $U_e = z_e V_e$ ($z_e \in \{\pm 1\}$). Because $V(C_1 x) = V(x)$ identically, $C_1 x$ and $x$ differ **only** in their boundary $\mathbb{Z}_2$ sign cochain on $\mathcal{C}_1$. Conditional on the interior adjoint field $V_{\rm int}$ on the slab $X = [0, l] \times (\mathbb{Z}/n)^3$, define the induced couplings $J_p(V) := \beta |\operatorname{Re} V_p| \ge 0$ and signs $\eta_p(V) := \operatorname{sgn}(\operatorname{Re} V_p) \in \{\pm 1\}$, the two $\mathbb{Z}_2$ gauge partition functions
$$
Z_{\mathbb{Z}_2}^+(x, y; V_{\rm int}) := \sum_{z \in \{\pm 1\}^{\mathcal{I}}} \exp\!\left(\sum_{p \in \mathcal{P}_{\rm slab}} J_p(V) \eta_p(V) (dz)_p\right) \quad \text{(boundary } (z(x), z(y))\text{)},
$$
and $Z_{\mathbb{Z}_2}^-(x, y; V_{\rm int})$ (same sum with boundary $(C_1 z(x), z(y))$), and the conditional $\mathbb{Z}_2$ bias
$$
b_j^{\mathbb{Z}_2}(x, y; V_{\rm int}) := \frac{Z_{\mathbb{Z}_2}^+(x, y; V_{\rm int}) - Z_{\mathbb{Z}_2}^-(x, y; V_{\rm int})}{Z_{\mathbb{Z}_2}^+(x, y; V_{\rm int}) + Z_{\mathbb{Z}_2}^-(x, y; V_{\rm int})} \in (-1, 1). \tag{4.4}
$$

**Proposition 4.2 (Exact Centre-Coset Bias Formula; PROVED).**
For every $\beta > 0$, every $l = l_j \ge 2$, and every pin pair $(x, y)$,
$$
b_j(x, y) = \mathbb{E}_{\nu_{x, y}^{\rm ev}}\!\Big[b_j^{\mathbb{Z}_2}(x, y;\, V_{\rm int})\Big], \tag{4.5}
$$
where $\nu_{x, y}^{\rm ev}$ is the interior Gibbs law of the even pinned slab $K_l^{\rm ev}(x, y) = \frac{1}{2}(K_l(x, y) + K_l(Cx, y))$.

*Proof.* Disintegrating Haar measure on interior links into $dV_{\rm int}$ times uniform measure on $z \in \{\pm 1\}^{\mathcal{I}}$, we have $K_l(x, y) \pm K_l(Cx, y) = 2^{-|\mathcal{I}|} e^{-\frac{1}{2}V(x) - \frac{1}{2}V(y)} \int (Z_{\mathbb{Z}_2}^+ \pm Z_{\mathbb{Z}_2}^-)\, dV_{\rm int}$. Under $\nu_{x, y}^{\rm ev}$, the marginal density of $V_{\rm int}$ is proportional to $Z_{\mathbb{Z}_2}^+(x, y; V_{\rm int}) + Z_{\mathbb{Z}_2}^-(x, y; V_{\rm int})$. Multiplying by $b_j^{\mathbb{Z}_2} = (Z_{\mathbb{Z}_2}^+ - Z_{\mathbb{Z}_2}^-)/(Z_{\mathbb{Z}_2}^+ + Z_{\mathbb{Z}_2}^-)$ cancels the denominator and yields $(K_l - K_{l, C})/(K_l + K_{l, C}) = b_j(x, y)$. $\square$

We now prove that at the upper end of the band $\beta \in [2, 3]$, conditional thin-$\mathbb{Z}_2$ fluctuations are **ordered (locked)** on unfrustrated backgrounds $V_{\rm int}$, establishing a sharp quantitative barrier against any triangle-inequality / thin-vortex bound $|b_j| \le \mathbb{E}[|b_j^{\mathbb{Z}_2}|]$.

**Theorem 6 (Explicit 4D $\mathbb{Z}_2$ Slab Peierls Locking Theorem; PROVED unconditionally).**
Let $X = [0, l] \times (\mathbb{Z}/n)^3$ ($n \ge 3$, $l \ge 2$). Suppose $V_{\rm int}$ and boundary pins $(x, y)$ are unfrustrated ($\eta_p(V) = +1$ for all $p \in \mathcal{P}_{\rm slab}$ and $z(x) = z(y) \equiv +1$, or any boundary gauge-equivalent to it) and satisfy $J_p(V) \ge J_0$ for all $p \in \mathcal{P}_{\rm slab}$. Whenever $80 e^{-2 J_0} < 1$ (i.e. $J_0 > \frac{1}{2}\log 80 \approx 2.192$),
$$
\frac{Z_{\mathbb{Z}_2}^-(x, y; V_{\rm int})}{Z_{\mathbb{Z}_2}^+(x, y; V_{\rm int})} \le \frac{l n\, (80 e^{-2 J_0})^{n^2}}{1 - 80 e^{-2 J_0}}, \qquad
b_j^{\mathbb{Z}_2}(x, y; V_{\rm int}) \ge 1 - \frac{2 l n\, (80 e^{-2 J_0})^{n^2}}{1 - 80 e^{-2 J_0}}. \tag{4.6}
$$
In particular, inside the band at $\beta = 3$, whenever $|\operatorname{Re} V_p| \ge \frac{5}{6}$ ($J_0 = \frac{5}{2}$), exact rational arithmetic gives $e^5 > (27/10)^5 = 143.48907 > 140$, so $80 e^{-5} < \frac{4}{7}$ and
$$
b_j^{\mathbb{Z}_2}(x, y; V_{\rm int}) \ge 1 - \frac{14}{3}\, l n\, \left(\frac{4}{7}\right)^{n^2} \longrightarrow 1. \tag{4.7}
$$

*Proof.* Write $\mathcal{P}_{{\rm seam}, i} := \{p_{0i}(x, 0) : x_i = 0\}$ ($i = 1, 2, 3$) for the three $(0, i)$-twist seams at $t = 0$, and for $w = (w_1, w_2, w_3) \in \mathbb{Z}_2^3$ let $Z_{\mathbb{Z}_2}^w$ be the partition function with sign $-1$ inserted on $\mathcal{P}_{\rm seam}^w := \triangle_{i: w_i = 1} \mathcal{P}_{{\rm seam}, i}$ (so $Z_{\mathbb{Z}_2}^{(0,0,0)} = Z_{\mathbb{Z}_2}^+$ and $Z_{\mathbb{Z}_2}^{(1,0,0)} = Z_{\mathbb{Z}_2}^-$).

*Step 1 (Character-expansion domination $Z_{\mathbb{Z}_2}^w \le Z_{\mathbb{Z}_2}^+$).* Expanding $e^{\pm J_p (dz)_p} = \cosh(J_p)(1 \pm \tanh(J_p) (dz)_p)$ and summing over $z \in \{\pm 1\}^{\mathcal{I}}$ gives
$$
Z_{\mathbb{Z}_2}^w = 2^{|\mathcal{I}|} \left(\prod_p \cosh J_p\right) \sum_{\substack{S \subset \mathcal{P}_{\rm slab} \\ \partial S \subset \mathcal{E}_0 \cup \mathcal{E}_l}} (-1)^{|S \cap \mathcal{P}_{\rm seam}^w|} \prod_{p \in S} \tanh J_p.
$$
Since $J_p \ge 0$, every product $\prod_{p \in S} \tanh J_p \ge 0$, so the triangle inequality yields $Z_{\mathbb{Z}_2}^w \le Z_{\mathbb{Z}_2}^+$ for every $w \in \mathbb{Z}_2^3$.

*Step 2 (Closed dual $2$-cycles and odd connected component).* For any $z \in \{\pm 1\}^{\mathcal{I}}$ contributing to $Z_{\mathbb{Z}_2}^-$, let $B(z) := \mathcal{P}_{{\rm seam}, 1} \triangle \{p \in \mathcal{P}_{\rm slab} : (dz)_p = -1\}$ be its set of unsatisfied plaquettes (contributing $-J_p$ instead of $+J_p$). Notice that every elementary $3$-cube $c$ of $X$ (either a temporal $3$-cube $[t, t+1] \times p_{ij}(x)$ for $0 \le t \le l-1$, or an interior spatial $3$-cube $\{t\} \times c_3$ for $1 \le t \le l-1$) has $\prod_{p \in \partial c} (dz)_p = +1$ (with boundary spatial plaquettes at $t = 0, l$ identically satisfied and hence excluded from $B(z)$) and meets $\mathcal{P}_{{\rm seam}, 1}$ in an even number ($0$ or $2$) of faces. Hence $B(z)$ meets every $3$-cube in an even number of faces, so its dual $B^*(z)$ is a closed dual $2$-cycle ($\partial^* B^*(z) = 0$) in the dual complex of $X$.

Decompose $B^*(z)$ into its dual-edge-connected components $\Gamma_1^*, \dots, \Gamma_r^*$; each $\Gamma_a^*$ is itself closed ($\partial^* \Gamma_a^* = 0$). For each $i \in \{1, 2, 3\}$ and each transverse coordinate $x_\perp^{(i)} \in (\mathbb{Z}/n)^2$, let $R^{(0, i)}(x_\perp^{(i)}) = \{p_{0i}(x, t) : x_i \in \mathbb{Z}/n,\, 0 \le t < l\}$ be the corresponding $n \times l$ ribbon. Between two adjacent parallel ribbons $R^{(0, i)}(x_\perp^{(i)})$ and $R^{(0, i)}(x_\perp^{(i)} + \hat j)$ ($j \ne i$), summing the even-incidence condition $\partial^* \Gamma_a^* = 0$ mod $2$ over the $n l$ intervening temporal $(0, i, j)$ $3$-cubes (whose boundary spatial plaquettes at $t = 0, l$ do not meet $\Gamma_a^*$) shows that $|\Gamma_a^* \cap R^{(0, i)}(x_\perp^{(i)})| \pmod 2$ is **independent of $x_\perp^{(i)}$**. Because $|B(z) \cap R^{(0, 1)}(0, 0)| \equiv |\mathcal{P}_{{\rm seam}, 1} \cap R^{(0, 1)}(0, 0)| = 1 \pmod 2$, at least one connected component $\Gamma^*$ of $B^*(z)$ satisfies $|\Gamma^* \cap R^{(0, 1)}(x_\perp)| \equiv 1 \pmod 2$ for every $x_\perp \in (\mathbb{Z}/n)^2$. In particular, since the $n^2$ ribbons $R^{(0, 1)}(x_\perp)$ are pairwise disjoint, $|\Gamma^*| \ge n^2$, and $\Gamma^*$ meets $R^{(0, 1)}(0, 0)$ (which contains $l n$ plaquettes).

*Step 3 (Explicit $\mathbb{Z}_2$ coboundary construction and Peierls injection).* Fix such a connected closed dual $2$-cycle $\Gamma^*$ and put $w_i := |\Gamma^* \cap R^{(0, i)}(0, 0)| \pmod 2$ ($i = 2, 3$), $w := (0, w_2, w_3) \in \mathbb{Z}_2^3$. Set $\Delta := \Gamma^* \triangle \mathcal{P}_{{\rm seam}, 1} \triangle \mathcal{P}_{\rm seam}^w \subset \mathcal{P}_{\rm slab}$ (viewed as an additive $\mathbb{Z}_2$ $2$-cochain with $\Delta_{ij}(x, 0) = \Delta_{ij}(x, l) = 0$). Then $d\Delta = 0$ on every $3$-cube of $X$ and $\sum_{x_i, t} \Delta_{0i} = 0$ (mod $2$) on every $(0, i)$-ribbon ($i = 1, 2, 3$). We explicitly construct $\tau \in \mathbb{Z}_2^{\mathcal{I}}$ (extended by $0$ on $t = 0, l$) with $d\tau = \Delta$:
- For $1 \le t \le l-1$ and $i \in \{1, 2, 3\}$, put $\tau_i(x, t) := \sum_{s=0}^{t-1} \Delta_{0i}(x, s) \pmod 2$.
- Put $A_i(x) := \sum_{s=0}^{l-1} \Delta_{0i}(x, s) \pmod 2$. Summing $(d\Delta)_{0ij}(x, s) = 0$ over $s = 0, \dots, l-1$ gives $(d_{\rm space} A)_{ij}(x) = \Delta_{ij}(x, l) - \Delta_{ij}(x, 0) = 0$. Since $A$ is closed on $(\mathbb{Z}/n)^3$ and all three coordinate periods $\sum_{x_i} A_i = |\Delta \cap R^{(0, i)}| = 0$ vanish mod $2$, integrating $A$ along coordinate paths from the origin defines $\phi : (\mathbb{Z}/n)^3 \to \mathbb{Z}_2$ with $d_{\rm space}\phi = A$.
- Set $\tau_0(x, t) := 0$ for $0 \le t \le l-2$ and $\tau_0(x, l-1) := \phi(x)$.
Direct evaluation confirms $(d\tau)_{0i}(x, t) = \Delta_{0i}(x, t)$ for $0 \le t \le l-2$, $(d\tau)_{0i}(x, l-1) = -\tau_i(x, l-1) - A_i(x) = \Delta_{0i}(x, l-1)$ in $\mathbb{Z}_2$, and $(d\tau)_{ij}(x, t) = \sum_{s=0}^{t-1} (d_{\rm space}\Delta_0)_{ij}(x, s) = \Delta_{ij}(x, t) - \Delta_{ij}(x, 0) = \Delta_{ij}(x, t)$ for $1 \le t \le l-1$.

Now map $z \mapsto \tilde z$ by multiplying each interior link $z_e$ by $(-1)^{\tau_e}$. This bijection transforms the unsatisfied-plaquette set $B(z)$ in $Z_{\mathbb{Z}_2}^-$ to $B(z) \triangle \Gamma^* = B(z) \setminus \Gamma^*$ in $Z_{\mathbb{Z}_2}^w$, switching every plaquette $p \in \Gamma^*$ from $-J_p$ to $+J_p$ and multiplying the Boltzmann weight by $\prod_{p \in \Gamma^*} e^{2 J_p} \ge e^{2 J_0 |\Gamma^*|}$. Summing over $z$ with $\Gamma^* \subset B^*(z)$ and applying Step 1 gives
$$
Z_{\mathbb{Z}_2}^-\big(\Gamma^* \subset B^*(z)\big) \le e^{-2 J_0 |\Gamma^*|} Z_{\mathbb{Z}_2}^w \le e^{-2 J_0 |\Gamma^*|} Z_{\mathbb{Z}_2}^+.
$$

*Step 4 (Connected dual-face count).* Each dual $2$-face in $\mathbb{Z}^4$ has $4$ boundary dual edges, and each dual edge meets $5$ other dual $2$-faces, so the dual-face adjacency graph has maximum degree $\Delta \le 20$. By encoding a rooted spanning tree of a connected $k$-element subset $\Gamma^*$ via a depth-first traversal of length $2(k-1)$ (at most $\binom{2k-2}{k-1} \le 4^{k-1}$ up/down patterns and at most $\Delta^{k-1}$ neighbor choices on downward steps), the number of connected sets $\Gamma^*$ of size $k$ containing a fixed root face in $R^{(0, 1)}(0, 0)$ is at most $(4\Delta)^{k-1} \le 80^k$. Summing over the $l n$ possible roots in $R^{(0, 1)}(0, 0)$ and all $k \ge n^2$ gives (4.6). Finally, $e > \sum_{j=0}^5 \frac{1}{j!} = \frac{163}{60} > \frac{27}{10}$ gives $e^5 > (27/10)^5 = 143.48907 > 140$, yielding (4.7). $\square$

**Exact failure points of Attack 3 at $\beta \in [2, 3]$:**
1. *(Failure 3a — thin-$\mathbb{Z}_2$ locking and required thick-vortex sign cancellation):* Theorem 6 proves that at $\beta = 3$, thin $\mathbb{Z}_2$ fluctuations conditional on $V_{\rm int}$ are deep in the ordered (deconfined $\mathbb{Z}_2$) phase on cold/unfrustrated backgrounds ($J_0 = 2.5$ gives $b_j^{\mathbb{Z}_2} \ge 1 - \frac{14}{3} l n (4/7)^{n^2}$, and the Peierls threshold $\frac{1}{2}\log 80 \approx 2.192$ sits inside $\beta \in [2, 3]$, far above the exact 4D $\mathbb{Z}_2$ critical point $\beta_c^{\mathbb{Z}_2} = \frac{1}{2}\log(1+\sqrt{2}) \approx 0.4407$). Meanwhile, check 1556 §(vi) proves that frustrated $\mathbb{Z}_2$-monopole cubes occur at positive density $c(\beta) > 0$, making the conditional $\mathbb{Z}_2$ law on typical $V_{\rm int}$ a frustrated 4D $\mathbb{Z}_2$ gauge spin glass with no FKG/Griffiths positivity. Physically (ARGUED), at $\beta = 3$ the dilute monopole cubes do not disorder the $\mathbb{Z}_2$ spin glass: instead $|b_j^{\mathbb{Z}_2}(x, y; V_{\rm int})| \approx 1$ locks to the parity of thick $\mathrm{SO}(3)$ centre vortices in $V_{\rm int}$, and $|b_j| = |\mathbb{E}[b_j^{\mathbb{Z}_2}]| \ll 1$ arises ONLY from **sign cancellation** between even- and odd-vortex $\mathrm{SO}(3)$ sectors. Thus any triangle-inequality bound $|b_j| \le \mathbb{E}[|b_j^{\mathbb{Z}_2}|]$ fails at $\beta = 3$, and capturing the sign cancellation requires non-perturbative control of thick $\mathrm{SO}(3)$ vortices — which distinguish 4D $\mathrm{SU}(2)$ from 5D $\mathrm{SU}(2)$ at the same $\beta = 3$.
2. *(Failure 3b — direct full-$\mathrm{SU}(2)$ slab disagreement/replica coupling):* Coupling two replicas of the full $\mathrm{SU}(2)$ slab $[0, l_j]$ to lower-bound $1 - d_{\rm TV}(p_+^{(j)}, p_-^{(j)})$ succeeds in the strong-coupling Dobrushin regime ($\beta < 2/9$, Theorem E) and the anisotropic regime ($b_t \in [2, 3], \kappa \le \kappa_*$, row 1565 §2), but fails at isotropic $\beta \in [2, 3]$: single-link replica marking violates $J p_s L < 1$ (row 1565 §2), single-link Dobrushin has $q = \frac{9}{2}\beta \in [9, 13.5]$ (and exact worst-case row sum $> 18/10$ at $\beta = 2$, row 1565 §1), single-slab Durhuus–Fröhlich mixing fails by **CA-FAIL** ($\beta > 1.0109$), and worst-boundary block Hamming contraction fails up to block side $10$ at $\beta \ge 2.3$ (rows 1511/1514). Because $x$ and $Cx$ are locally gauge-equivalent on every contractible patch, any typical-field slab coupling across $l_j \asymp \sqrt{n}$ must nucleate a percolating $2$-dimensional thick centre-vortex sheet spanning the $n^2$ transverse plane — an open 4D-selective order-one mixing theorem (which fails in 5D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$).

---

## 5. Stopping Point, Credits, and Claim-by-Claim Audit

### 5.1 Stopping Point (Rule: Equivalent Is Not Progress)

- **At fixed $\beta \in [2, 3]$:** `(L-tail)` of check 1585 §(v) is **neither proved nor refuted** for 4D $\mathrm{SU}(2)$ Wilson theory. In compliance with the rule *Equivalent is not progress*, we propose no equivalent rewrite of `(L-tail)`, `(N-flux)`, or `(PUR-io)` as progress; we stop cleanly at **`(L-tail)`** itself after three distinct attacks (spectral Cauchy–Schwarz bridge / exposed-indicator conditioning; direct Haar-preserving seam-spreading + Jensen; and $\mathbb{Z}_2 \times \mathrm{SO}(3)$ centre-coset Peierls locking + slab coupling).
- **Along the calibrated release trajectory $\beta_K$:** Theorem 4 proves that `(L-tail)` is **mathematically incompatible** with any nontrivial continuum electric-flux two-point function at fixed physical separation on $\mathbb{T}_\ell^3 \times S_D^1$ (and its $\sqrt{d}$-arc splitting drives physical arc duration to $0$), so `(L-tail)` is strictly an IR fixed-coupling statement and cannot be carried verbatim to $\beta_K$.
- **Relation to `(N-flux)` and $\Pi$:** `(L-tail)` at fixed $\beta \in [2, 3]$ implies `(N-flux)` with $f(d) \le 3(C_0 n^{-\epsilon} + n^{-c\log 2})$ and sandwiches $P_K$ against $\Pi = P_{\rm full}$ via $(1 - 3\rho_{2u})\Pi \le P_K \le \Pi/(1 - 3\rho_u)^2$ (once $3\rho_u < 1$), while leaving completely open both the untwisted two-period purity $\Pi$ at $\beta \in [2, 3]$ and the carry from $\beta \in [2, 3]$ to the calibrated release trajectory $\beta_K$.

### 5.2 Credits

- **G. 't Hooft (1978, 1979):** Centre twists, twisted partition functions, and electric/magnetic flux sectors on periodic tori.
- **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text:** The YM4 release, calibrated trajectory $\beta_K$, soft block map (`kernelImage`), and continuum-limit / transfer-operator framework cited via rows 1451–1468 and `library/gap-k2-tool-design-fable.md` (with **T. Balaban** for the underlying ultraviolet renormalization-group method).
- **A. Guth (1980); J. Fröhlich and T. Spencer (1982); G. Mack and V. B. Petkova (1979); E. T. Tomboulis (1981); J. Fröhlich, B. Simon, and T. Spencer (1976); K. Osterwalder and E. Seiler (1978); M. Lüscher (1977); R. L. Dobrushin (1970); M. Creutz (1979):** Statistical-mechanics and lattice gauge theory results cited in context.
- **Lane rows credited:** Check 1585 (gpt-6.2-astra: statement of `(L-tail)`, arc-product consumer bound, exposed-indicator sufficient route, 2-state separation); row 1566 / check 1570 (Claude Fable / gpt-6.2-astra: `(N-flux)`, two-period purity sandwich and positivity floor, Lemma Z); row 1565 / check 1571 (gpt-6.2-astra / Claude Opus: interacting 4D compact $\mathrm{U}(1)$ Villain/Wilson flux refutation, anisotropic replica-exchange bound, single-link TV obstruction); row 1568 / check 1572 (Gemini 4 Neon / Claude Opus: Theorem E strong-coupling thresholds, Theorem A four-corner identity); row 1143 / check 1144 (gpt-6.2-astra / Claude Opus: weak-coupling bare winding-loop bound (7) and twist asymptotics (6)); row 1171 / check 1172 (gpt-6.2-astra / Claude Opus: conditional seam affinity and vortex profile); rows 929, 1072/1074–1075 (CA-FAIL), 1451/1453, 1457, 1468, 1511/1514, 1556.

### 5.3 Claim-by-Claim Audit

| Claim | Standing |
|---|---|
| Proposition 1.1: consumer chain from `(L-tail)` to $r_1(d) \le \rho_d$, `(N-flux)` ($f(d) \le 3\rho_d$), twist ratios $1 - 6\rho_d \le Z^z/Z^0 \le 1$, and positivity-safe purity sandwich $\max(\frac{1}{8}, 1-3\rho_{2u})\Pi \le P_K \le \Pi/\max(\frac{1}{8}, 1-3\rho_u)^2$ | **PROVED** |
| Proposition 1.2: spectator blindness of `(L-tail)`; non-equivalence with `(PUR-io)` and `(N-flux)`; explicit 4-state strictly positive, strictly positive-definite transfer counterexample separating `(L-tail)` from check 1585's conditional route | **PROVED** |
| Theorem 1: joint $(x, \sigma)$ representation, exact marginal TV / Hellinger / Markov-bridge denominator-cancellation identities (2.3)–(2.6), and predictor/variational bounds (2.7)–(2.9) | **PROVED** |
| Theorem 2: exact spectral Cauchy–Schwarz bridge $\mathbb{E}_{\rm ev}[|b_j|] \le \sqrt{Z_{\rm od}(2l_j) Z_{\rm ev}(2d-2l_j)}/Z_{\rm ev}(d) \le \sqrt{S_{\rm od}(2l_j)/(1+S_{\rm ev}(d))}$ and lower-tail bound (2.11) for all $d \ge 9$ (no rough-cut wall) | **PROVED** |
| Theorem 3: exact untwisted-to-even decomposition (2.12), untwisted Hölder flux lower bound (2.14)–(2.15), and single-arc bias lower bound (2.16) | **PROVED** |
| Theorem 4(1)–(2): incompatibility of `(L-tail)` along calibrated $\beta_K$ with any nontrivial continuum $C_1$-odd two-point limit on $\mathbb{T}_\ell^3 \times S_D^1$ (and short-arc $\Delta\tau_j \to 0$ limit $|b_j| \to 1$) | **PROVED** (conditional on stated continuum/coarse properties) |
| Theorem 4(3): unconditional refutation $r_1(d) \ge \frac{1}{64} e^{-K n^2/(128\beta)}$ for 4D $\mathrm{SU}(2)$ Wilson whenever $\beta(n) \gg n^2/\log n$ (and fixed $(n, d), \beta \to \infty$) | **PROVED GIVEN** checked row 1143/1144 |
| Theorem 5: exact $p \ne 0$ spectator factorization and Hellinger bound $\Pr_{\rm ev}(|b_j| \le 1/2) \le 4\sqrt{\pi\gamma_l} e^{-\frac{\pi^2}{8}\gamma_l}$ in $D$-dimensional free Maxwell + compact rotor (FAILS exponentially in $D = 4, 5$; HOLDS deterministically in $D = 3$) | **PROVED** |
| Weak 4D compact $\mathrm{U}(1)$ (Villain $\beta \ge 2000$, Wilson $\beta_W \ge \beta_*$) FAILS; strong-coupling twins and anisotropic 4D $\mathrm{SU}(2)$ ($b_t \in [2,3], \kappa \le \kappa_*$) HOLD a.s. | **PROVED GIVEN** checked rows 1565/1571, 1568/1572 |
| Proposition 4.1: exact KL/Jensen identity (4.1), exact Peter–Weyl Loewner plaquette lower bound $\mathbb{E}_{p_+^{(j)}}[\operatorname{Re} U_{01}] \ge \alpha(\beta) = \min(I_2(\beta)/I_1(\beta), 1/\beta)$ (4.2), and extensive cut-flip barrier $\ge 2\beta\alpha(\beta) n^2$ ($\ge \frac{31}{18} n^2$ on $[2, 3]$) at every $\beta > 0$ | **PROVED** |
| Proposition 4.2 & Theorem 6: exact centre-coset formula $b_j = \mathbb{E}[b_j^{\mathbb{Z}_2}]$ and explicit 4D $\mathbb{Z}_2$ slab Peierls locking bound $b_j^{\mathbb{Z}_2} \ge 1 - \frac{2ln(80 e^{-2 J_0})^{n^2}}{1 - 80 e^{-2 J_0}}$ for unfrustrated $J_p \ge J_0 > \frac{1}{2}\log 80$ (with rational $J_0 = 5/2$ bound $\ge 1 - \frac{14}{3} l n (4/7)^{n^2}$ at $\beta = 3$) | **PROVED** |
| Failure of `(L-tail)` in 5D weak $\mathrm{SU}(2)$ ($\beta \in [2, 3]$); sign-cancellation picture of thick $\mathrm{SO}(3)$ vortices at $\beta = 3$ | **ARGUED** |
| `(L-tail)` for isotropic 4D $\mathrm{SU}(2)$ Wilson at fixed $\beta \in [2, 3]$, `(N-flux)` on $[2, 3]$, $\Pi$, release carry, `(PUR-io)`, and the mass gap | **OPEN** |

RESULT: OPEN at fixed beta in [2, 3] (and PROVED incompatible with any nontrivial continuum electric-flux sector along the calibrated trajectory beta_K) — We stop at the lower-tail lemma (L-tail) of check 1585 section (v) after three distinct attacks (spectral Cauchy-Schwarz bridge / exposed-indicator conditioning; direct Haar-preserving seam-spreading + Jensen; and Z_2 x SO(3) centre-coset Peierls locking + slab coupling). PROVED unconditionally: exact consumer chain from (L-tail) to (N-flux) with f(d) <= 3 rho_d (rho_d = C_0 n^(-eps) + n^(-c log 2)) and positivity-safe purity sandwich max(1/8, 1 - 3 rho_(2u)) Pi <= P_K <= Pi / max(1/8, 1 - 3 rho_u)^2 (Proposition 1.1); neutral spectator blindness and a 4-state strictly positive, strictly positive-definite transfer counterexample proving check 1585's conditional route is strictly stronger than (L-tail) (Proposition 1.2); exact joint (x, sigma) law and denominator-cancelling TV/Hellinger/Markov-bridge identities E_ev|b_j| = d_TV(p_+, p_-), E_ev sqrt(1 - b_j^2) = H_aff(p_+, p_-) (Theorem 1); exact spectral Cauchy-Schwarz bridge E_ev|b_j| <= sqrt(S_od(2 l_j)/(1 + S_ev(d))) for d >= 9 eliminating the rough-cut wall of check 1556's BC(eps) (Theorem 2); exact untwisted Holder flux bound E_0[W(0)W(t)] <= 2 ||W||_inf^2 r_1(d)^(min(t, d-t)/d) and arc-bias lower bound (Theorem 3); exact single-arc Hellinger bound in D-dimensional free Maxwell + compact rotor proving (L-tail) FAILS exponentially on every arc in D = 4, 5 and HOLDS deterministically in D = 3 (Theorem 5); exact KL/Jensen identity, Peter-Weyl Loewner plaquette bound E[Re U_01] >= min(I_2(beta)/I_1(beta), 1/beta) > 0, and extensive cut-flip barrier >= 2 beta alpha(beta) n^2 (>= (31/18) n^2 on [2, 3]) failing even at beta = 0.01 (Proposition 4.1); exact centre-coset identity b_j = E[b_j^(Z_2)] and explicit 4D Z_2 slab Peierls locking theorem b_j^(Z_2) >= 1 - 2 l n (80 e^(-2 J_0))^(n^2)/(1 - 80 e^(-2 J_0)) for unfrustrated J_p >= J_0 > (1/2) log 80 (with exact rational bound >= 1 - (14/3) l n (4/7)^(n^2) at J_0 = 5/2 inside beta = 3), proving thin-Z_2 locking and the necessity of thick-SO(3)-vortex sign cancellation (Proposition 4.2, Theorem 6). PROVED conditional / GIVEN checked inputs: along the calibrated trajectory beta_K at fixed (l, g_0), (L-tail) kills every uniformly bounded C_1-odd two-point function at every fixed physical separation tau in (0, D) and drives physical arc length to zero (Theorem 4(1)-(2)); given checked row 1143/1144, r_1(d) >= (1/64) exp(-K n^2/(128 beta)), refuting (L-tail) unconditionally for 4D SU(2) Wilson whenever beta(n) >> n^2/log n (Theorem 4(3)); weak 4D compact U(1) FAILS (1565/1571) while strong-coupling twins (1568/1572) and anisotropic 4D SU(2) (1565/1571) HOLD a.s. What (L-tail) leaves open: (L-tail) and (N-flux) at isotropic beta in [2, 3], the untwisted two-period purity Pi = Z^0(2u)/Z^0(u)^2 (to which (L-tail) is completely blind), the release carry from [2, 3] to beta_K, (PUR-io), and the mass gap.
