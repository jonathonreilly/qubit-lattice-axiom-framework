# Cut-Covariance Band Lemma Investigation

**Author:** Gemini 4 Neon (research note, unchecked; grants no scientific or audit status).
**Target:** The first band lemma proposed by check 1556 (`library/gap-mech-direction4-check-astra62.md`, section (v), lines 56–111), for four-dimensional $\mathrm{SU}(2)$ Wilson lattice gauge theory at $\beta \in [2, 3]$.
**Method:** Purely by hand. No Monte Carlo, no floating-point proof steps, no Lean computation.
**Labels:** Every claim is marked **PROVED** (proved here by hand, unchecked), **PROVED GIVEN [X]** (proved here conditional on a named theorem/premise), **ON FILE** (cited from a checked lane file), **ARGUED** (heuristic or belief-grade physical argument), **GUIDE** (numerical literature value, never a proof step), or **OPEN**.

---

## 1. Exact Setup, Cut-Covariance Identity, and Four-Corner Consequences

### 1.1 Setting and Target Lemma

Fix spacetime dimension $d = 4$ (and below, general $d \ge 3$ for comparisons). Let $\Lambda = (\mathbb{Z}/n\mathbb{Z})^{d-1}$ be the spatial torus of side $n \in 1024\mathbb{N}$, with $u = n/512$ and half-cylinder length $v \in \{u/2, u\}$, $v \ge 3$. For $G = \mathrm{SU}(2)$ identified with unit quaternions $S^3 \subset \mathbb{H}$ ($\operatorname{Re} q = \frac{1}{2}\operatorname{tr} q$, $\operatorname{Im} q \in \mathbb{R}^3 \cong \operatorname{Im}\mathbb{H}$), let $\mathcal{E}$ be the positively oriented spatial links of $\Lambda$, $X, Y \in G^{\mathcal{E}}$ two spatial slices, and $V(U) = \beta \sum_{p \subset \Lambda} (1 - \operatorname{Re} U_p)$ the spatial Wilson action.

Following `library/gap-transfer.md` (Statement 1), the gauge-projected transfer operator $T = \mathsf{T}_P = P e^{-V/2} C_{\mathcal{E}} e^{-V/2} P$ on $L^2(G^{\mathcal{E}})$ has positive real-analytic integral kernel $A_T(X, Y)$, and $T^v$ has integral kernel
$$
K_v(X, Y) = e^{-\frac{1}{2} V(X) - \frac{1}{2} V(Y)} \int \left(\prod_{t=1}^{v-1} e^{-V(U(t))}\, dU(t)\right) \left(\prod_{t=0}^{v-1} K_0\big(U(t),\, g_t \cdot U(t+1)\big)\, dg_t\right), \tag{1.1}
$$
with $U(0) = X$, $U(v) = Y$, $K_0(u, w) = \prod_{e \in \mathcal{E}} e^{-\beta(1 - \operatorname{Re}(u_e w_e^{-1}))}$, and $(g_t \cdot U(t+1))_{(x, i)} = g_t(x) U(t+1)_{(x, i)} g_t(x+\hat i)^{-1}$. Let $\Phi_{\rm int} = (U(1), \dots, U(v-1), g_0, \dots, g_{v-1})$ denote the interior variables and $\nu_{X, Y}$ the conditional Gibbs probability measure on $\Phi_{\rm int}$ defined by the integrand of (1.1) with pinned boundary slices $(X, Y)$. For each spatial centre twist $z \in \mathbb{Z}_2^{d-1}$ ($C_z$ flips all $i$-links with $z_i = 1$ and $x_i = 0$), put $Z^z(2v) = \operatorname{Tr}(C_z T^{2v}) = \int K_v(A, B) K_v(B, C_z A)\, dA\, dB$, and define the sewn-torus two-slice marginal
$$
d\mu_{z, 2v}(A, B) = \frac{K_v(A, B) K_v(B, C_z A)}{Z^z(2v)}\, dA\, dB. \tag{1.2}
$$

On a spatial slice $U$, let $\mathcal{C}_1 = \{x = (0, x_\perp) : x_\perp \in (\mathbb{Z}/n\mathbb{Z})^{d-2}\}$ index the positive $1$-links with tail at $x_1 = 0$ ($|\mathcal{C}_1| = n^{d-2}$; in $d=4$, $|\mathcal{C}_1| = n^2$). Following check 1556 §(v), for $d \ge 4$ let $Q_x(U) = U_{(x,2)} U_{(x+\hat 2, 3)} U_{(x+\hat 3, 2)}^{-1} U_{(x,3)}^{-1}$ be the untouched based $23$-plaquette at $x \in \mathcal{C}_1$, and set
$$
a_x(U) = \begin{cases} \operatorname{Im} Q_x(U) / |\operatorname{Im} Q_x(U)|, & Q_x(U) \ne \pm 1, \\ 0, & Q_x(U) = \pm 1, \end{cases}
\qquad (R_{\mathbf{s}} U)_{(x, 1)} = \exp(s_x a_x(U)) U_{(x, 1)} \quad (x \in \mathcal{C}_1), \tag{1.3}
$$
with $(R_{\mathbf{s}} U)_e = U_e$ on all other links, and $R_s := R_{(s, \dots, s)}$. As verified in check 1556 §(v), $a_x(U)$ is independent of all $1$-links, so $a_x(R_{\mathbf{s}} U) = a_x(U)$; $R_s$ preserves product Haar measure, commutes with spatial gauge transformations $\mathcal{G}$ and centre flips $C_z$, and satisfies $R_\pi = C_1$ on the full-measure set $\{Q_x \ne \pm 1\ \forall x \in \mathcal{C}_1\}$. Write $D_x = \left.\frac{\partial}{\partial s_x}\right|_{s_x=0}$ for the individual cut-link derivative, and $D_x^{(1)}, D_y^{(2)}$ for $D_x, D_y$ acting on the first and second slice arguments of $K_v(X, Y)$.

**Target Lemma (L) (check 1556 §(v), lines 104–108).** Fix $d = 4$. There exist constants $C < \infty$ and $\epsilon > 0$, independent of $\beta \in [2, 3]$, $n \in 1024\mathbb{N}$, $v \in \{u/2, u\}$ ($v \ge 3$), and $z \in \mathbb{Z}_2^3$, such that
$$
\mathcal{L}_z(n, v; \beta) := \sup_{s, t \in [0, \pi]} \sup_{x \in \mathcal{C}_1} \sum_{y \in \mathcal{C}_1} \mathbb{E}_{\mu_{z, 2v}}\big|(D_x^{(1)} D_y^{(2)} \log K_v)(R_s B, R_t C_z A)\big| \le C v^{-2-\epsilon}. \tag{L}
$$

We also record the strictly weaker **signed** variant:
$$
\mathcal{L}_z^{\rm signed}(n, v; \beta) := \sup_{s, t \in [0, \pi]} \left| \frac{1}{|\mathcal{C}_1|} \sum_{x \in \mathcal{C}_1} \sum_{y \in \mathcal{C}_1} \mathbb{E}_{\mu_{z, 2v}}\big[(D_x^{(1)} D_y^{(2)} \log K_v)(R_s B, R_t C_z A)\big] \right| \le C v^{-2-\epsilon}. \tag{L-signed}
$$
Clearly $\mathcal{L}_z^{\rm signed} \le \mathcal{L}_z$ by the triangle inequality and spatial translation invariance along $\mathcal{C}_1$.

### 1.2 Exact Connected-Covariance Formula (PROVED)

**Lemma 1.1 (PROVED).** For all $d \ge 3$ (using any bounded $1$-link-independent gauge-covariant axis $a_x$), all $n \ge 3$, $v \ge 2$, $\beta > 0$, and every $(X, Y) \in (G^{\mathcal{E}})^2$:
1. The mixed derivative is the exact connected covariance in the pinned cylinder $\nu_{X, Y}$:
   $$
   (D_x^{(1)} D_y^{(2)} \log K_v)(X, Y) = \operatorname{Cov}_{\nu_{X, Y}}\!\big(\mathcal{O}_x^{(1)},\, \mathcal{O}_y^{(2)}\big), \tag{1.4}
   $$
   where
   $$
   \begin{aligned}
   \mathcal{O}_x^{(1)} &:= \beta \, \operatorname{Im}\!\big(P_{01}(x, 0)\big) \cdot a_x(X), \qquad P_{01}(x, 0) = g_0(x) U(1)_{(x, 1)} g_0(x+\hat 1)^{-1} X_{(x, 1)}^{-1}, \\
   \mathcal{O}_y^{(2)} &:= -\beta \, \operatorname{Im}\!\big(W_y^{(v)}\big) \cdot a_y(Y), \qquad W_y^{(v)} = Y_{(y, 1)} g_{v-1}(y+\hat 1)^{-1} U(v-1)_{(y, 1)}^{-1} g_{v-1}(y).
   \end{aligned} \tag{1.5}
   $$
2. Pointwise on all configurations: $|\mathcal{O}_x^{(1)}| \le \beta$, $|\mathcal{O}_y^{(2)}| \le \beta$, and $|(D_x^{(1)} D_y^{(2)} \log K_v)(X, Y)| \le \beta^2$.
3. $(D_x^{(1)} D_y^{(2)} \log K_v)(h_0 \cdot X, h_v \cdot Y) = (D_x^{(1)} D_y^{(2)} \log K_v)(X, Y)$ for all independent $h_0, h_v \in \mathcal{G}$, and $(D_x^{(1)} D_y^{(2)} \log K_v)(C_w X, C_w Y) = (D_x^{(1)} D_y^{(2)} \log K_v)(X, Y)$ for all $w \in \mathbb{Z}_2^{d-1}$.
4. For $v \ge 3$, $\mathcal{O}_x^{(1)}$ (supported on $\{g_0(x), U(1)_{(x,1)}, g_0(x+\hat 1)\}$) and $\mathcal{O}_y^{(2)}$ (supported on $\{g_{v-1}(y), U(v-1)_{(y,1)}, g_{v-1}(y+\hat 1)\}$) have disjoint supports in $\Phi_{\rm int}$.

*Proof.* Write $\log K_v(X, Y) = -\frac{1}{2} V(X) - \frac{1}{2} V(Y) + \log \widetilde{K}_v(X, Y)$, where $\widetilde{K}_v(X, Y) = \int e^{-\widetilde{S}(X, Y; \Phi_{\rm int})}\, d\Phi_{\rm int}$. Because $V(X)$ depends only on $X$ and $V(Y)$ only on $Y$, $D_x^{(1)} D_y^{(2)} V(X) = D_x^{(1)} D_y^{(2)} V(Y) = 0$. Inside $\widetilde{S}$, the link $X_{(x,1)}$ occurs in exactly one plaquette, namely $P_{01}(x, 0)$ in slab $0 \to 1$, and $Y_{(y,1)}$ occurs in exactly one plaquette, namely $W_y^{(v)}$ (the cyclic equivalent of $P_{01}(y, v-1)$) in slab $v-1 \to v$. For $v \ge 2$ these slabs are distinct, so $D_x^{(1)} D_y^{(2)} \widetilde{S} = 0$. Replacing $X_{(x,1)} \mapsto e^{\theta a_x} X_{(x,1)}$ sends $P_{01}(x, 0) \mapsto P_{01}(x, 0) e^{-\theta a_x}$; using $\operatorname{Re}(q a) = -\operatorname{Im}(q) \cdot a$ for $a \in \operatorname{Im}\mathbb{H}$,
$$
\left.\frac{\partial}{\partial \theta}\right|_{\theta=0} \beta \operatorname{Re}\!\big(P_{01}(x, 0) e^{-\theta a_x}\big) = -\beta \operatorname{Re}\!\big(P_{01}(x, 0) a_x\big) = \beta \operatorname{Im}\!\big(P_{01}(x, 0)\big) \cdot a_x = \mathcal{O}_x^{(1)}.
$$
Similarly, replacing $Y_{(y,1)} \mapsto e^{\phi a_y} Y_{(y,1)}$ gives $\left.\frac{\partial}{\partial\phi}\right|_{\phi=0} \beta \operatorname{Re}(e^{\phi a_y} W_y^{(v)}) = -\beta \operatorname{Im}(W_y^{(v)}) \cdot a_y = \mathcal{O}_y^{(2)}$. Since $a_x(X), a_y(Y)$ are independent of the moved $1$-links and bounded by $1$, and $\widetilde{K}_v > 0$ on the compact integration domain, differentiating under the integral twice yields (1.4). Bounds (2) follow from $|\operatorname{Im} q| \le 1$ and $|a_x|, |a_y| \le 1$. Invariance (3) follows because $R_{\mathbf{s}}$ commutes with $\mathcal{G}$ and $C_w$, and $K_v(h_0 \cdot X, h_v \cdot Y) = K_v(X, Y)$ and $K_v(C_w X, C_w Y) = K_v(X, Y)$. Disjointness (4) is immediate because slice $1$ and slice $v-1$ are distinct for $v \ge 3$. $\square$

### 1.3 Four-Corner Identity, Universal Sandwich, and Exact Consequences (PROVED)

Credit: 't Hooft (1978, 1979) for centre twists; check 1556 §(v) (gpt-6.2-astra) for the cut rotation $R_s$ and four-corner identity.

**Theorem A (Four-Corner Sandwich and Exact Consequences of (L) / (L-signed); PROVED).** Let $d \ge 3$ and assume $R_s$ is a circle action on $\mathcal{C}_1$ with $R_\pi = C_1$ a.e. and $K_v(C_1 X, C_1 Y) = K_v(X, Y)$ (for $d \ge 4$ and $G = \mathrm{SU}(2)$ or $\mathrm{U}(1)$, the map (1.3); for $G = \mathrm{U}(1)$ in any $d \ge 3$, also the constant-axis map $a_x \equiv i$). Then:

1. **(Four-corner identity, check 1556 §(v)).** For $\mu_{z, 2v}$-a.e. $(A, B)$,
   $$
   \int_0^\pi\!\int_0^\pi \sum_{x \in \mathcal{C}_1} \sum_{y \in \mathcal{C}_1} (D_x^{(1)} D_y^{(2)} \log K_v)(R_s B, R_t C_z A)\, ds\, dt = 2 \log \frac{K_v(B, C_z A)}{K_v(B, C_1 C_z A)}. \tag{1.6}
   $$
2. **(Universal lower bound at $z = 0$).** For every $\beta > 0$, $n \ge 3$, $v \ge 2$,
   $$
   0 \le \log \frac{Z^0(2v)}{Z^{e_1}(2v)} \le \mathbb{E}_{\mu_{0, 2v}}\!\left[\log \frac{K_v(B, A)}{K_v(B, C_1 A)}\right] \le \frac{\pi^2}{2} n^{d-2} \mathcal{L}_0^{\rm signed}(n, v; \beta) \le \frac{\pi^2}{2} n^{d-2} \mathcal{L}_0(n, v; \beta). \tag{1.7}
   $$
3. **(Exact consequence of Lemma (L) — or even (L-signed) — in $d = 4$).** If $\mathcal{L}_z^{\rm signed}(n, v; \beta) \le C v^{-2-\epsilon}$ uniformly over $z \in \mathbb{Z}_2^3$, then for every $z \in \mathbb{Z}_2^3$ and every axis $j \in \{1, 2, 3\}$,
   $$
   \left|\log \frac{Z^{z + e_j}(2v)}{Z^z(2v)}\right| \le \frac{\pi^2}{2} C \left(\frac{n}{v}\right)^2 v^{-\epsilon}, \qquad 0 \le \log \frac{Z^0(2v)}{Z^z(2v)} \le |z| \frac{\pi^2}{2} C \left(\frac{n}{v}\right)^2 v^{-\epsilon}, \tag{1.8}
   $$
   where $|z| \le 3$ is the Hamming weight of $z$ and $(n/v)^2 \le 1024^2$. Consequently, writing $Z_+(2v) = \frac{1}{8}\sum_{z \in \mathbb{Z}_2^3} Z^z(2v) = \operatorname{Tr}(P_0 T^{2v})$ and $Z_e(2v) = \operatorname{Tr}(P_e T^{2v}) = \frac{1}{8}\sum_z (-1)^{e \cdot z} Z^z(2v)$ for the electric-flux sectors $e \in \mathbb{Z}_2^3$:
   $$
   1 - \frac{3\pi^2}{4} C \left(\frac{n}{v}\right)^2 v^{-\epsilon} \le \frac{Z_+(2v)}{Z^0(2v)} \le 1, \qquad \sum_{e \ne 0} \frac{Z_e(2v)}{Z^0(2v)} \le \frac{3\pi^2}{4} C \left(\frac{n}{v}\right)^2 v^{-\epsilon}. \tag{1.9}
   $$

*Proof.* (1) Put $F(s, t) = \log K_v(R_s B, R_t C_z A)$. By the fundamental theorem of calculus on $[0, \pi]^2$, $\iint \partial_s \partial_t F = F(\pi, \pi) - F(\pi, 0) - F(0, \pi) + F(0, 0)$. Since $R_\pi = C_1$ a.e. and $K_v(C_1 X, C_1 Y) = K_v(X, Y)$, $F(\pi, \pi) = F(0, 0)$ and $F(\pi, 0) = F(0, \pi) = \log K_v(B, C_1 C_z A)$, giving (1.6).
(2) Because $T^{2v} \ge 0$ and $C_1$ is a unitary involution commuting with $T$, $Z^0(2v) - Z^{e_1}(2v) = 2 \operatorname{Tr}(P_{C_1 = -1} T^{2v}) \ge 0$, so $\log(Z^0(2v)/Z^{e_1}(2v)) \ge 0$. Next, $Z^{e_1}(2v)/Z^0(2v) = \mathbb{E}_{\mu_{0, 2v}}[K_v(B, C_1 A)/K_v(B, A)]$. Applying Jensen's inequality $\log \mathbb{E}[e^W] \ge \mathbb{E}[W]$ to $W = \log(K_v(B, C_1 A)/K_v(B, A))$ and negating gives $\log(Z^0(2v)/Z^{e_1}(2v)) \le \mathbb{E}_{\mu_{0,2v}}[\log(K_v(B, A)/K_v(B, C_1 A))]$. Substituting (1.6) and exchanging expectation with the finite integral and sum (justified by Lemma 1.1(2)) yields (1.7).
(3) Applying the same Jensen step at arbitrary $z \in \mathbb{Z}_2^3$ gives $\log(Z^z(2v)/Z^{z+e_1}(2v)) \le \frac{\pi^2}{2} n^2 \mathcal{L}_z^{\rm signed}$. Swapping $z$ and $z + e_1$ yields the reverse inequality, hence the first bound in (1.8) for $j = 1$, and for $j = 2, 3$ by spatial permutation symmetry. Telescoping at most $|z|$ flips from $0$ to $z$ gives the second bound (with $Z^z(2v) \le Z^0(2v)$ from $T^{2v} \ge 0$). Averaging $e^{-x} \ge 1 - x$ over the $8$ twists $z \in \mathbb{Z}_2^3$ (average Hamming weight $3/2$) gives (1.9). $\square$

*Remark (strengthening of check 1556 §(v)).* Theorem A(3) shows that the absolute value inside $\mathcal{L}_z$ is **not** needed to bound the twist ratios $Z^z(2v)/Z^0(2v)$ via Jensen: the weaker signed bound (L-signed) already gives (1.8)–(1.9) with the same constant. (The absolute value inside (L) additionally bounds $\mathbb{E}_{\mu_{z,2v}}|\log(K_v(B, C_1 C_z A)/K_v(B, C_z A))|$, i.e. $L^1$ concentration of the log-ratio, not just its mean.)

### 1.4 Why Lemma (L) Is Not Equivalent to (PUR-io), and What Further Input Is Needed (PROVED)

Recall `(PUR-io)` (`library/gap-k2-tool-design-fable.md` §3.1, credit Sussman and Alpoge with Claude and Codex for the release calibration, rows 1461/1462/1465 and `lean/gapchain` for the seed-to-gap chain): at the calibrated release couplings $\beta_K \sim \text{const} \cdot \log n$, $P_K = Z_+(2u)/Z_+(u)^2 \ge 457/625$ at infinitely many $K$ for one $\ell \in 1024\mathbb{N}$ and one $g_0$.

**Proposition 1.2 (Logical incomparability with (PUR-io) on reflection-positive gauge transfer data; PROVED).**
1. **((L) $\not\Rightarrow$ (PUR-io): neutral spectator obstruction, check 1556 §(iii),(v)).** Adjoin any independent reflection-positive neutral spectator with transfer operator $T_{\rm spec}$ (positive kernel $K_v^{\rm spec}(a, b)$ on a state space $\mathcal{X}_{\rm spec}$, invariant under $C_z \otimes 1$ and $R_s \otimes 1$). Then $K_v^{\rm tot}((X, a), (Y, b)) = K_v(X, Y) K_v^{\rm spec}(a, b)$, so $\log K_v^{\rm tot}$ is additive, $D_x^{(1)} D_y^{(2)} \log K_v^{\rm tot} = D_x^{(1)} D_y^{(2)} \log K_v$ pointwise, and $\mu_{z, 2v}^{\rm tot} = \mu_{z, 2v} \otimes \mu_{2v}^{\rm spec}$. Hence $\mathcal{L}_z$ and $\mathcal{L}_z^{\rm signed}$ are **identically unchanged**, while $P^{\rm tot} = P \cdot P^{\rm spec}$ with $P^{\rm spec} = \operatorname{Tr}(T_{\rm spec}^{2u}) / (\operatorname{Tr} T_{\rm spec}^u)^2$. Choosing a two-state positive symmetric spectator kernel $\left(\begin{smallmatrix} 1 & a \\ a & 1 \end{smallmatrix}\right)$ with $a \downarrow 0$ (check 1527 §(vi)) or any seedless spectator (check 1556 §(iii)) drives $P^{\rm spec} \to 1/2 < 457/625$ (or to $0$), destroying purity without changing Lemma (L).
2. **((PUR-io) $\not\Rightarrow$ (L) on abstract transfer data).** In the transfer counterexample of check 1541 line 70 ($T_n = \operatorname{diag}(1, e^{-1/n^2}, e^{-\Delta})$ with centre signs $(+, -, +)$, $\Delta > 0$), neutral purity $P \to 1 \ge 457/625$, whereas $Z^{e_1}(2v)/Z^0(2v) = (1 - e^{-2v/n^2} + e^{-2v\Delta})/(1 + e^{-2v/n^2} + e^{-2v\Delta}) \sim v/n^2$, so $\log(Z^0/Z^{e_1}) \sim \log n$, and any gauge-theoretic realization would force $\mathcal{L}_0$ to violate any decaying bound of the form $o(n^{-2} \log n)$ by (1.7). Moreover, within pure $\mathrm{SU}(2)$ Wilson theory, Lemma (L) is stated on the fixed interval $\beta \in [2, 3]$, whereas (PUR-io) lives on the drifting calibrated trajectory $\beta_K \to \infty$.

**Exact further inputs required beyond Lemma (L) to reach (PUR-io).**
Even if Lemma (L) were proved in full for $\beta \in [2, 3]$:
1. **Common neutral normalization across the two periods $u$ and $2u$:** By (1.9), Lemma (L) implies only $Z_+(2v) / Z^0(2v) = 1 - O(v^{-\epsilon})$ for $2v \in \{u, 2u\}$, hence
   $$
   P(n, \beta) = \frac{Z_+(2u)}{Z_+(u)^2} = \big(1 + O(u^{-\epsilon})\big) \frac{Z^0(2u)}{Z^0(u)^2}.
   $$
   It gives **no** bound on the untwisted two-period ratio $Z^0(2u)/Z^0(u)^2 = (1 + S(2u; n^3)) / (1 + S(u; n^3))^2$ (equivalently, no bound on the neutral excited-state sum $s_+(u)$, which is invisible to centre twists and to neutral spectators).
2. **Carry to the calibrated release roots $\beta_K$:** Lemma (L) holds at fixed $\beta \in [2, 3]$, whereas (PUR-io) requires purity at $\beta_K \sim \frac{11}{3\pi^2}\log n \to \infty$. Passing from fixed $\beta \in [2, 3]$ to $\beta_K$ still requires an ultraviolet/infrared carry (such as Theorem T's (A1)–(A3) of rows 1332, 1391, check 1556 §(viii), or a (K-II) chain plus (BASE-K2) of row 1468).

---

## 2. Pre-Proof Selectivity and Control Tests (Row 1553 §1.5, Corrected by Check 1556)

Before attempting a proof at $\beta \in [2, 3]$, we test Lemma (L) and (L-signed) against all controls of row 1553 §1.5 (as corrected in check 1556 §§(iii)–(iv)).

### 2.1 Test (g1): 4D Gaussian Maxwell and 4D Compact $\mathrm{U}(1)$ at Weak Coupling

We first test the lead's rough count (GUESSED: "a Coulomb field-strength connected correlator summed over a cut of area $n^2$ at distance $v$ gives order $v^{-2}$, so $\epsilon > 0$ might fail exactly there"). We **confirm** the exact exponent $-2$ rigorously and uncover three structural refinements.

#### Theorem B (Exact $d$-dimensional Gaussian Maxwell scaling; PROVED unconditionally)

Consider non-compact Gaussian Maxwell theory on the cylinder $[0, v] \times (\mathbb{Z}/n\mathbb{Z})^{d-1}$ ($d \ge 3$, $n \ge v \ge 3$, $\beta > 0$) with action
$$
S_{\rm G}(A) = \frac{\beta}{2} \sum_{t=0}^{v-1} \sum_{x \in \Lambda} \sum_{i=1}^{d-1} \big(A_i(t+1, x) - A_i(t, x) - (\partial_i A_0)(t, x)\big)^2 + \sum_{t=0}^v w_t \frac{\beta}{2} \sum_{x \in \Lambda} \sum_{1 \le i < j \le d-1} \big(\partial_i A_j(t, x) - \partial_j A_i(t, x)\big)^2,
$$
where $w_0 = w_v = 1/2$, $w_t = 1$ ($1 \le t \le v-1$), $A_i(0, \cdot) = X_i$, $A_i(v, \cdot) = Y_i$, and $(A_i(t))_{1 \le t \le v-1}$, $(A_0(t))_{0 \le t \le v-1}$ (modulo spatial constants) are integrated over $\mathbb{R}$. Then:

1. **Exact kernel:** Independent of $(X, Y)$,
   $$
   M_v(x - y) := \frac{\partial^2 \log K_v(X, Y)}{\partial X_{(x,1)} \partial Y_{(y,1)}} = \frac{\beta}{n^{d-1}} \sum_{p \in \Lambda^*} e^{i p \cdot (x - y)} \widehat{M}_v(p), \qquad \Lambda^* = \frac{2\pi}{n}(\mathbb{Z}/n\mathbb{Z})^{d-1}, \tag{2.1}
   $$
   where $\hat p_j = e^{i p_j} - 1$, $|\hat p|^2 = \sum_{j=1}^{d-1} 4\sin^2(p_j/2)$, $\omega(p) = 2\operatorname{arsinh}(|\hat p|/2) > 0$ for $p \ne 0$, and
   $$
   \widehat{M}_v(p) = \begin{cases} \dfrac{1}{v}, & p = 0, \\[8pt] \left(1 - \dfrac{|\hat p_1|^2}{|\hat p|^2}\right) \dfrac{\sinh\omega(p)}{\sinh(\omega(p) v)}, & p \ne 0. \end{cases} \tag{2.2}
   $$
2. **Exact signed cut sum:** For every $x \in \mathcal{C}_1$,
   $$
   \sum_{y \in \mathcal{C}_1} M_v(x - y) = \frac{\beta}{n v}. \tag{2.3}
   $$
3. **Exact two-sided $\ell^1$ cut bound:** With $\alpha_d := \frac{2}{3\pi\sqrt{d(d-1)}}$ and $B_d := 2 + (\pi \alpha_d)^{-1}$, for all $d \ge 3$, $n \ge v \ge 3$, $\beta > 0$,
   $$
   \frac{\beta}{n v} \le \sum_{y \in \mathcal{C}_1} |M_v(x - y)| \le 4 B_d^{d/2} \left(\frac{n}{v}\right)^{\frac{d-2}{2}} \frac{\beta}{v^2}. \tag{2.4}
   $$
   In $d = 4$ with $n/v \in \{512, 1024\}$, $\frac{\beta}{1024 v^2} \le \sum_{y \in \mathcal{C}_1} |M_v(x - y)| \le 4(2+3\sqrt{3})^2 \cdot 1024 \cdot \frac{\beta}{v^2}$, so **Lemma (L) fails at the exact exponent $-2$** (no $\epsilon > 0$).

*Proof.* (1) Diagonalize in spatial Fourier modes $p \in \Lambda^*$. For $p \ne 0$, decompose $\tilde A(t, p)$ into its longitudinal part along $\hat p$ and $d - 2$ transverse polarizations $\hat p^\dagger \tilde A_\perp(t, p) = 0$. Integrating out $\tilde A_0(t, p)$ removes the longitudinal coupling completely (yielding a constant independent of $X, Y$). Each transverse mode is a 1D harmonic chain with mass-squared $|\hat p|^2 = 4\sinh^2(\omega/2) = 2(\cosh\omega - 1)$. Its Euler–Lagrange solution $\phi(t) = \frac{\sinh(\omega(v-t))}{\sinh(\omega v)} x + \frac{\sinh(\omega t)}{\sinh(\omega v)} y$ satisfies $\phi(t+1) - 2\phi(t) + \phi(t-1) = |\hat p|^2 \phi(t)$ for $1 \le t \le v-1$. Summing by parts, the interior sum vanishes and the boundary terms simplify via $\sinh(\omega(v-1)) = \sinh(\omega v)\cosh\omega - \cosh(\omega v)\sinh\omega$ and $1 - \cosh\omega + \frac{1}{2}|\hat p|^2 = 0$, giving
$$
S_{\rm 1D}(\phi) = \frac{\beta}{2} \frac{\sinh\omega}{\sinh(\omega v)}\Big(\cosh(\omega v)(|x|^2 + |y|^2) - 2\operatorname{Re}(\bar x y)\Big).
$$
At $p = 0$, $\tilde A_0(t, 0)$ drops out and $S_{p=0}(\phi) = \frac{\beta}{2v}\sum_i |\tilde Y_i(0) - \tilde X_i(0)|^2$. The $(1, 1)$ entry of the transverse projector $I - \frac{\hat p \hat p^\dagger}{|\hat p|^2}$ is $1 - \frac{|\hat p_1|^2}{|\hat p|^2}$, giving (2.1)–(2.2).

(2) On $\mathcal{C}_1$, $x - y = (0, x_\perp - y_\perp)$. Summing $e^{-i p_\perp \cdot y_\perp}$ over $y_\perp \in (\mathbb{Z}/n)^{d-2}$ gives $n^{d-2}\delta_{p_\perp, 0}$, leaving $\frac{\beta}{n}\sum_{p_1} \widehat{M}_v(p_1, 0)$. For $p_1 \ne 0$ and $p_\perp = 0$, $1 - |\hat p_1|^2/|\hat p|^2 = 0$, so only $p_1 = 0$ survives, giving $\frac{\beta}{n} \cdot \frac{1}{v} = \frac{\beta}{nv}$.

(3) The lower bound in (2.4) follows immediately from (2.3) by the triangle inequality. For the upper bound, write $q = e^{-\omega} \in (0, 1]$, so $\frac{\sinh\omega}{\sinh(\omega v)} = q^{v-1} / \sum_{j=0}^{v-1} q^{2j}$.
- If $q^{v-1} \ge 1/2$, then $\sum_{j=0}^{v-1} q^{2j} \ge v q^{2v-2} \ge v/4$, so the ratio is $\le \frac{4}{v} q^{v-1} \le \frac{4}{v} q^{(v-1)/2}$.
- If $q^{v-1} < 1/2$, then $\sum_{j=0}^{v-1} q^{2j} = (1 - e^{-2\omega v})/(1 - e^{-2\omega}) \ge \frac{3/4}{2\omega}$, so the ratio is $\le \frac{8}{3}\omega e^{-\omega(v-1)} \le \frac{16}{3e(v-1)} e^{-\frac{1}{2}\omega(v-1)} \le \frac{4}{v} e^{-\frac{1}{2}\omega(v-1)}$ (using $te^{-t/2} \le 2/e$ and $v - 1 \ge \frac{2}{3}v$ for $v \ge 3$).
Since $(v-1)/2 \ge v/3$ for $v \ge 3$, we have $\widehat{M}_v(p) \le \frac{4}{v} e^{-\frac{1}{3}\omega(p) v}$ for all $p \in \Lambda^*$. Next, representing $p_j \in (-\pi, \pi]$, $|\hat p| \ge \frac{2}{\pi}|p| \ge \frac{2}{\pi\sqrt{d-1}}\|p\|_1$ and $|\hat p|/2 \le \sqrt{d-1}$. Since $\operatorname{arsinh}(u) = \int_0^u (1+t^2)^{-1/2} dt \ge u / \sqrt{1+u^2}$, we get $\omega(p) \ge |\hat p|/\sqrt{d} \ge 3\alpha_d \|p\|_1$, hence $\widehat{M}_v(p) \le \frac{4}{v} e^{-\alpha_d v \|p\|_1}$.

For each $p_\perp \in \frac{2\pi}{n}(\mathbb{Z}/n)^{d-2}$, define $\widetilde{M}_v(p_\perp) = \frac{1}{n}\sum_{p_1} \widehat{M}_v(p_1, p_\perp)$. Using $1 - e^{-t} \ge t/(1+t)$ ($t > 0$) and $n \ge v$,
$$
\frac{1}{n}\sum_{p_1} e^{-\alpha_d v |p_1|} \le \frac{1}{n}\left(1 + 2\sum_{k=1}^\infty e^{-\frac{2\pi\alpha_d v}{n} k}\right) \le \frac{2}{n}\left(1 + \frac{n}{2\pi\alpha_d v}\right) \le \frac{B_d}{v}.
$$
Thus $0 \le \widetilde{M}_v(p_\perp) \le \frac{4 B_d}{v^2} e^{-\alpha_d v \|p_\perp\|_1}$ for all $p_\perp$ (including $p_\perp = 0$, where $\widetilde{M}_v(0) = \frac{1}{nv} \le \frac{4 B_d}{v^2}$). By Parseval on $(\mathbb{Z}/n)^{d-2}$ and $e^{-2\alpha_d v |p_j|} \le e^{-\alpha_d v |p_j|}$,
$$
\sum_{y_\perp} |M_v(0, y_\perp)|^2 = \frac{\beta^2}{n^{d-2}} \sum_{p_\perp} \widetilde{M}_v(p_\perp)^2 \le \frac{16 B_d^2 \beta^2}{v^4} \left(\frac{1}{n}\sum_{p_2} e^{-\alpha_d v |p_2|}\right)^{d-2} \le \frac{16 B_d^d \beta^2}{v^{d+2}}.
$$
Cauchy–Schwarz over the $n^{d-2}$ cut sites yields $\sum_{y_\perp} |M_v(0, y_\perp)| \le n^{(d-2)/2} \cdot 4 B_d^{d/2} \beta v^{-(d+2)/2}$, which is (2.4). $\square$

**Three structural refinements to the lead's rough count:**
1. **Gauss-law electrostatic tail and sign change (ARGUED from (2.1)–(2.2)):** In the scaling limit $n/v \gg 1$, $\widetilde{M}_v(q_\perp/v) \approx v^{-2} \Phi(q_\perp)$ with $\Phi(q_\perp) = \int_{\mathbb{R}} \frac{dq_1}{2\pi} \frac{|q_\perp|^2}{\sqrt{q_1^2 + |q_\perp|^2}\sinh(\sqrt{q_1^2+|q_\perp|^2})}$. As $q_\perp \to 0$, $\Phi(q_\perp) \sim \frac{1}{2}|q_\perp|$ (a non-smooth cusp from the Gauss-law projector $1 - |\hat p_1|^2/|\hat p|^2$), whose $(d-2)$-dimensional Fourier transform produces a **negative** electrostatic tail $M_v(0, y_\perp) \sim -c_d \beta / (v |y_\perp|^{d-1})$ for $v \ll |y_\perp| \ll n$ (in $d = 4$, $-\frac{\beta}{4\pi v |y_\perp|^3}$, rather than $(v^2 + |y_\perp|^2)^{-2}$). This tail is still integrable on $\mathbb{R}^{d-2}$ and gives the same $\Theta(\beta v^{-2})$ sum as the positive core $|y_\perp| \lesssim v$, while the signed sum cancels down to the $p = 0$ mode $\frac{\beta}{nv}$.
2. **Dimension-independence of the exponent $-2$ (PROVED in (2.4)):** Because the cut has dimension $d - 2$ and the core scales as $v^{-d}$ (and the tail as $v^{-1}|y_\perp|^{-(d-1)}$), the free-field $\ell^1$ cut sum is $\Theta_d(\beta v^{-2})$ in **every** dimension $d \ge 3$ ($d = 3, 4, 5, \dots$).
3. **Random-axis behaviour in $\mathrm{U}(1)$:** For check 1556's literal map (1.3) specialized to $\mathrm{U}(1)$ ($a_x(U) = i\operatorname{sign}(\sin \theta_{23}(x))$ for $\sin \theta_{23} \ne 0$, so $R_\pi = C_1$ a.e.), at $s = t = 0$ we have $|a_x(B)| = |a_y(A)| = 1$ a.e., so the random signs **vanish completely** inside the absolute value of Lemma (L). By contrast, in the *signed* sum at $s = t = 0$ alone, $\mathbb{E}[a_x(B) a_y(A)] = O(v^{-4})$ in 4D Gaussian Maxwell, giving $O(v^{-6})$ cancellation at $s = t = 0$; yet for compact $\mathrm{U}(1)$, the circle wrap-around $e^{\pm i\pi} = -1$ at $s = t = \pi$ forces the signed integral over $[0, \pi]^2$ back up to $\ge \frac{2}{\pi^2 n^2}\log(Z^0/Z^{e_1})$ by (1.7)!

#### Theorem C (Exact Interacting $\mathrm{U}(1)$ Lower Bound; PROVED unconditionally)

Consider $d$-dimensional compact $\mathrm{U}(1)$ lattice gauge theory ($d \ge 3$, either Wilson cosine weight $e^{\beta \cos \theta_p}$ or Villain weight $\phi_\beta(\theta_p) = \sum_{m \in \mathbb{Z}} e^{-\frac{\beta}{2}(\theta_p + 2\pi m)^2}$). Let $(R_\alpha^{\rm const} U)_{(x, 1)} = e^{i\alpha} U_{(x, 1)}$ ($x \in \mathcal{C}_1$) be the uniform cut shift, and define the continuously twisted partition function and periodic-torus dielectric stiffness:
$$
Z^0(\alpha; 2v) := \int K_v(A, B) K_v(B, R_\alpha^{\rm const} A)\, dA\, dB = \operatorname{Tr}\!\big(R_\alpha^{\rm const} T^{2v}\big), \qquad \beta_{\rm eff, d}(n, 2v; \beta) := \frac{2v}{n^{d-3}} \left(-\left.\frac{d^2}{d\alpha^2}\right|_{\alpha=0} \log Z^0(\alpha; 2v)\right). \tag{2.5}
$$
Put $g(\alpha) := \log K_v(B, R_\alpha^{\rm const} A)$ and $F(\alpha) := \log Z^0(\alpha; 2v)$. Then:
1. **(Exact variance-stiffness identity).**
   $$
   \sum_{x, y \in \mathcal{C}_1} \mathbb{E}_{\mu_{0, 2v}}\!\left[\frac{\partial^2 \log K_v}{\partial \theta_{(x,1)}^{(1)} \partial \theta_{(y,1)}^{(2)}}(B, A)\right] = \mathbb{E}_{\mu_{0, 2v}}[-g''(0)] = 2\operatorname{Var}_{\mu_{0, 2v}}(g'(0)) = 2\big(-F''(0)\big) \ge 0. \tag{2.6}
   $$
2. **(Universal lower bound for both $R_s$ and $R_s^{\rm const}$).** Using either check 1556's map $a_x = i\operatorname{sign}(\sin \theta_{23}(x))$ ($d \ge 4$) or the constant-axis map $a_x \equiv i$ ($d \ge 3$),
   $$
   \mathcal{L}_0^{\mathrm{U}(1), d}(n, v; \beta) \ge \frac{2\big(-F''(0)\big)}{n^{d-2}} = \frac{\beta_{\rm eff, d}(n, 2v; \beta)}{n v}, \tag{2.7}
   $$
   and in addition, for both $\mathcal{L}_0$ and $\mathcal{L}_0^{\rm signed}$,
   $$
   \mathcal{L}_0^{\mathrm{U}(1), d}(n, v; \beta) \ge \mathcal{L}_0^{\rm signed, \mathrm{U}(1), d}(n, v; \beta) \ge \frac{2}{\pi^2 n^{d-2}} \log \frac{Z^0(2v)}{Z^{e_1}(2v)}. \tag{2.8}
   $$

*Proof.* (1) Because $R_s^{\rm const}$ applied to every slice of the cylinder preserves every spatial and temporal plaquette, $K_v(R_s^{\rm const} X, R_s^{\rm const} Y) = K_v(X, Y)$ for all $s \in \mathbb{R}$. Hence $\log K_v(R_s^{\rm const} B, R_t^{\rm const} A) = g(t - s)$, so $\partial_s \partial_t|_{0,0} \log K_v = -g''(0)$ and $\partial_s|_0 \log K_v = -g'(0)$, $\partial_t|_0 \log K_v = +g'(0)$. Differentiating $F(\alpha) = \log \mathbb{E}_{\mu_{0,2v}}[e^{g(\alpha) - g(0)}]$ twice at $\alpha = 0$ gives
$$
F''(0) = \mathbb{E}_{\mu_{0,2v}}[g''(0)] + \operatorname{Var}_{\mu_{0,2v}}(g'(0)), \qquad \text{i.e., } \mathbb{E}_{\mu_{0,2v}}[-g''(0)] = -F''(0) + \operatorname{Var}_{\mu_{0,2v}}(g'(0)). \tag{2.9}
$$
On the other hand, applying the Two-Slice IBP Identity (Theorem 1 in §3.1 below, proved independently for any Haar-preserving vector field) to $D = \sum_{x \in \mathcal{C}_1} \partial/\partial\theta_{(x,1)}$ on $d\mu_{0,2v} = Z^0(2v)^{-1} K_v(B, A)^2 dA dB$ gives
$$
\mathbb{E}_{\mu_{0,2v}}[-g''(0)] = \mathbb{E}_{\mu_{0,2v}}[(D^{(1)} D^{(2)} \log K_v)(B, A)] = -2 \mathbb{E}_{\mu_{0,2v}}[(D^{(1)}\log K_v)(D^{(2)}\log K_v)] = +2 \mathbb{E}_{\mu_{0,2v}}[g'(0)^2] = 2\operatorname{Var}_{\mu_{0,2v}}(g'(0)), \tag{2.10}
$$
since $\mathbb{E}_{\mu_{0,2v}}[g'(0)] = \frac{1}{2}\mathbb{E}_{\mu_{0,2v}}[D^{(2)}\log \mu_{0,2v}] = 0$. Combining (2.9) and (2.10) proves $\operatorname{Var}_{\mu_{0,2v}}(g'(0)) = -F''(0)$ and $\mathbb{E}_{\mu_{0,2v}}[-g''(0)] = 2(-F''(0))$. Since $R_\alpha^{\rm const}$ is unitary and commutes with $T^{2v} \ge 0$, $Z^0(\alpha; 2v) = \sum_{q \in \mathbb{Z}} e^{iq\alpha}\operatorname{Tr}_q(T^{2v})$ with $\operatorname{Tr}_q(T^{2v}) = \operatorname{Tr}_{-q}(T^{2v}) \ge 0$, so $-F''(0) = \langle q^2 \rangle \ge 0$.

(2) Restricting $\sup_{s, t \in [0, \pi]}$ to $s = t = 0$, using $|a_x(B)| = |a_y(A)| = 1$ a.e. (for both $a_x = i\operatorname{sign}(\sin\theta_{23})$ and $a_x \equiv i$), translation invariance on $\mathcal{C}_1$, the triangle inequality, and (2.6):
$$
\mathcal{L}_0^{\mathrm{U}(1), d} \ge \frac{1}{n^{d-2}} \sum_{x, y \in \mathcal{C}_1} \mathbb{E}_{\mu_{0,2v}}\!\left|\frac{\partial^2 \log K_v}{\partial\theta_{(x,1)}^{(1)}\partial\theta_{(y,1)}^{(2)}}(B, A)\right| \ge \frac{1}{n^{d-2}} \mathbb{E}_{\mu_{0,2v}}[-g''(0)] = \frac{2(-F''(0))}{n^{d-2}} = \frac{\beta_{\rm eff, d}(n, 2v; \beta)}{n v}.
$$
Equation (2.8) is Theorem A(2). $\square$

#### Proposition D (Exact Villain Harmonic–Monopole Factorization; PROVED unconditionally)

For $d$-dimensional Villain $\mathrm{U}(1)$ on $\mathbb{T} = (\mathbb{Z}/n\mathbb{Z})^{d-1} \times (\mathbb{Z}/2v\mathbb{Z})$, write $\omega_{01} = \delta_{x_1, 0} dx_1 \wedge \delta_{t, 0} dt$, $\hat\omega_{01} = \frac{1}{2vn}\mathbf{1}_{\mathcal{P}_{01}}$ its harmonic projection, and $\Theta(\phi; \gamma) := \sum_{k \in \mathbb{Z}} \exp\!\big(-\frac{\gamma}{2}(\phi + 2\pi k)^2\big)$. Then, with $M_{01}(m) := \sum_{p \in \mathcal{P}_{01}} m_p$,
$$
Z_{\rm Vil}^0(\alpha; 2v) = \mathrm{const} \cdot \sum_{q \in d_2(\mathbb{Z}^{\mathcal{P}})} \widetilde{W}(q) \, \Theta\!\left(\alpha + \frac{2\pi M_{01}(m_0(q))}{n^{d-2}};\; \frac{\beta n^{d-3}}{2v}\right), \tag{2.11}
$$
where $m_0(q) \in \mathbb{Z}^{\mathcal{P}}$ is any fixed representative with $d_2 m_0(q) = q$ and $\widetilde{W}(q) > 0$ is independent of $\alpha$. Moreover, in the dual integer two-form law $\nu_{\beta, \mathbb{T}}(n) \propto e^{-\|n\|^2/(2\beta)} \mathbf{1}_{\{d_1^* n = 0\}}$, $-F''(0) = \langle Q_{01}(n)^2 \rangle_{\nu_{\beta, \mathbb{T}}}$ where $Q_{01}(n) = (\omega_{01}, n) = (\hat\omega_{01}, n) \in \mathbb{Z}$.

*Proof.* Since $d_2(\omega_{01} - \hat\omega_{01}) = 0$ and $\omega_{01} - \hat\omega_{01}$ has zero periods on all coordinate $2$-tori, $\omega_{01} - \hat\omega_{01} = d_1\lambda$ for a periodic $1$-form $\lambda$. Shifting $\theta \mapsto \theta - \alpha\lambda$ preserves circle Haar measure and replaces $\alpha\omega_{01}$ by $\alpha\hat\omega_{01}$. Unfolding $\theta \in [-\pi, \pi)^{\mathcal{E}}$ by summing over $d_1\mathbb{Z}^{\mathcal{E}}$ reduces $\mathbb{Z}^{\mathcal{P}} / d_1\mathbb{Z}^{\mathcal{E}}$ to $m_0(q) + \sum_{\mu<\nu} k_{\mu\nu} \omega_{\mu\nu}$ ($k_{\mu\nu} \in \mathbb{Z}$, $q \in d_2(\mathbb{Z}^{\mathcal{P}})$). Integrating out $d_1\phi \in P_e\mathbb{R}^{\mathcal{P}}$ projects $2\pi m + \alpha\hat\omega_{01}$ orthogonally onto $P_c \oplus P_h$. Since $d_2\omega_{\mu\nu} = 0$, $P_c(\omega_{\mu\nu}) = 0$, and the harmonic components along distinct coordinate planes are mutually orthogonal, with $\|\hat\omega_{01}\|^2 = \frac{2v n^{d-1}}{(2vn)^2} = \frac{n^{d-3}}{2v}$ and $(P_h(2\pi m_0(q)) + 2\pi k_{01}\hat\omega_{01} + \alpha\hat\omega_{01})_{01} = \frac{1}{2vn}(\frac{2\pi M_{01}(m_0(q))}{n^{d-2}} + 2\pi k_{01} + \alpha)$. Summing over $k_{01} \in \mathbb{Z}$ yields (2.11). Poisson summation on each plaquette gives the dual representation $\langle e^{i\alpha Q_{01}(n)}\rangle_{\nu_{\beta,\mathbb{T}}}$, whence $-F''(0) = \langle Q_{01}(n)^2\rangle$. $\square$

**Verdict on Test (g1) (4D compact $\mathrm{U}(1)$ at weak coupling):**
- **PROVED unconditionally:** For 4D Gaussian Maxwell, $\frac{\beta}{1024 v^2} \le \mathcal{L}_0 \le C \frac{\beta}{v^2}$ (Theorem B), refuting Lemma (L) right at the exponent $-2$.
- **PROVED GIVEN uniform positive periodic-torus dielectric stiffness $\beta_{\rm eff, 4}(n, 2v; \beta) \ge c_0 > 0$:** By Theorem C (2.7), $\mathcal{L}_0^{\mathrm{U}(1), 4}(n, v; \beta) \ge \frac{c_0}{1024 v^2}$, refuting Lemma (L) (and by (2.8), if $Z^{e_1}(2v)/Z^0(2v) \le 1 - \delta$, refuting (L-signed) as well!).
- **Standing of the periodic-torus input (honest scope, cf. rows 782, 784, 786 and check 1556 line 32):** Guth (1980) and Fröhlich–Spencer (1982, CMP 83) prove masslessness and positive dielectric stiffness for 4D Villain $\mathrm{U}(1)$ at sufficiently large $\beta$ on $\mathbb{Z}^4$ with fixed boundary conditions (and state extension to Wilson cosine without full published details). On periodic tori, row 786 (`library/gap-tu-retry.md` (9), checked row 794) proves $\beta(1 - \delta_*) P_c \preceq C_{\mathbb{T}} \preceq \beta(P_c + P_h)$ for $\beta \ge 2^{14}$ on $(\mathbb{Z}/M)^4$, dropping $P_h$ from the lower bound when conditioning on cosets of $d_2^*\mathbb{Z}^{C^3}$. Extending that lower bound to the harmonic projection $P_h$ on rectangular tori $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/2v)$ (equivalently controlling $\operatorname{Var}(\phi_q)$ in (2.11)) is standard in Fröhlich–Spencer's method (and cited in `gap-tu-retry.md` line 119 as joint harmonic averaging in PV) but is **not** re-proved from scratch here. Under that periodic-torus bridge, **Lemma (L) FAILS in 4D compact $\mathrm{U}(1)$ at weak coupling** right at the threshold exponent $-2$.

### 2.2 Test (g2): 5D $\mathrm{SU}(2)$ at Weak Coupling

In $d = 5$, $\Lambda = (\mathbb{Z}/n)^4$, the cut $\mathcal{C}_1$ has 3-dimensional area $n^3$, and check 1556's circle action (1.3) (still using $Q_x = U_{23}(x)$) is unchanged.

- **Universal lower bound (PROVED):** By Theorem A(2) with $d = 5$,
  $$
  \mathcal{L}_0^{\mathrm{SU}(2), 5}(n, v; \beta) \ge \mathcal{L}_0^{\rm signed, \mathrm{SU}(2), 5}(n, v; \beta) \ge \frac{2}{\pi^2 n^3} \log \frac{Z^0(2v)}{Z^{e_1}(2v)}. \tag{2.12}
  $$
- **Behaviour at weak coupling (ARGUED; 5D weak-coupling masslessness is belief-grade, row 1531):** In 5D $\mathrm{SU}(2)$ Wilson theory, numerical evidence places a first-order bulk transition at $\beta_c^{\rm 5D} \approx 1.64$ (Creutz 1979, GUIDE), so the tested band $\beta \in [2, 3]$ **already lies in the believed deconfined, IR-free massless gluon phase**! In this phase, the bare gauge coupling is irrelevant in the infrared ($g_{\rm eff}^2(L) \sim g_0^2 / L \to 0$) and long-distance physics is governed by $3$ free massless gluons with effective inverse coupling $\beta_{\rm eff} > 0$:
  1. Via (2.12): a $01$-twist of $\pi$ on the $n^4 \times 2v$ torus has classical/Coulomb free energy $\log(Z^0(2v)/Z^{e_1}(2v)) \asymp \frac{\pi^2 \beta_{\rm eff}}{4} \frac{n^2}{v} = \Theta(\beta_{\rm eff} v)$. Dividing by $n^3$ in (2.12) gives
     $$
     \mathcal{L}_0^{\mathrm{SU}(2), 5}(n, v; \beta) \ge c \frac{\beta_{\rm eff}}{n v} = \Theta(\beta_{\rm eff} v^{-2}).
     $$
  2. Directly at $s = t = 0$ in linearized perturbation theory around a flat background ($X = e^{g\xi}$, $Y = e^{g\eta}$, $g = \beta_{\rm eff}^{-1/2}$): temporal gauge writes $K_v(X, Y) = \int_{\mathcal{G}} dh\, K_v^{\rm temp}(X, h \cdot Y)$. Separating the constant relative global colour rotation $\Omega \in \mathrm{SU}(2)$ in $h(x) = \Omega e^{g\lambda(x)}$, for $X = I$ the symmetry $g_0(x) \mapsto \Omega g_0(x)$ forces $\operatorname{Cov}_{\nu_{I, Y}}(\mathcal{O}_x^{(1)}, \mathcal{O}_y^{(2)}) = 0$ identically (**PROVED**). However, for typical weak-coupling $(A, B) \sim \mu_{0, 2v}$, the modes $2\pi/n \le |p| \le 1/v$ contribute $\sum_{2\pi/n \le |p| \le 1/v} \frac{1}{|p|^2 v^2} \asymp (n/v)^{d-1} = 512^4$ to the $\Omega$-locking action $S_{\rm cross}(\Omega)$, locking $\Omega$ near $I$ with fluctuation variance $\operatorname{Var}(\theta_\Omega) = O((v/n)^4)$. Conditional on $\Omega \approx I$, the three free massless gluons give $\beta_{\rm eff} (a_x(B) \cdot \operatorname{Ad}(\Omega) a_y(A)) M_v^{(5D)}(0, x_\perp - y_\perp)$, whose $\ell^1$ sum over $y_\perp \in (\mathbb{Z}/n)^3$ is $\Theta(\beta_{\rm eff} v^{-2})$ by Theorem B (with the global $\Omega$-fluctuation adding an independent $O(\beta_{\rm eff} v^{-2})$ contribution suppressed by $512^{-4}$ at $x = y$).

Thus, in 5D $\mathrm{SU}(2)$ at weak coupling (including $\beta \in [2, 3]$ under the belief-grade phase picture), **even the literal 4D bound $C v^{-2-\epsilon}$ FAILS** (and the 5D cut-area bound $C v^{-3-\epsilon}$ needed to control $Z^{e_1}/Z^0$ fails by a full power of $v$).

### 2.3 Test (g3): Gapped Twins

#### Theorem E (Strong-Coupling Exponential Decay in 4D/5D $\mathrm{SU}(2)$ and 3D/4D $\mathrm{U}(1)$; PROVED unconditionally)

Let $G = \mathrm{SU}(2) \cong S^3 \subset \mathbb{R}^4$ ($m = 4$) or $G = \mathrm{U}(1) \cong S^1 \subset \mathbb{R}^2$ ($m = 2$), in any spacetime dimension $d \ge 3$, with Wilson action and any $1$-link-independent cut axes $|a_x| \le 1$. Put
$$
q := \frac{6(d - 1)}{m} \beta = \begin{cases} \frac{9}{2}\beta, & G = \mathrm{SU}(2),\, d = 4, \\ 6\beta, & G = \mathrm{SU}(2),\, d = 5, \\ 9\beta, & G = \mathrm{U}(1),\, d = 4, \\ 6\beta, & G = \mathrm{U}(1),\, d = 3. \end{cases}
$$
Whenever $q < 1$ (i.e., $\beta < 2/9$ for 4D $\mathrm{SU}(2)$; $\beta < 1/6$ for 5D $\mathrm{SU}(2)$; $\beta < 1/9$ for 4D $\mathrm{U}(1)$; $\beta < 1/6$ for 3D $\mathrm{U}(1)$), for all $n \ge 3$, all $v \ge 3$, and **every** pair of boundary slices $(X, Y) \in (G^{\mathcal{E}})^2$ (hence uniformly in $s, t \in [0, \pi]$ and $z \in \mathbb{Z}_2^{d-1}$):
$$
\sup_{X, Y} \sup_{x \in \mathcal{C}_1} \sum_{y \in \mathcal{C}_1} \big|(D_x^{(1)} D_y^{(2)} \log K_v)(X, Y)\big| \le \frac{3\beta^2}{(1 - q)^2} \, v \, q^{v-2}. \tag{2.13}
$$
In particular, Lemma (L) **HOLDS** with exponential decay in all four strong-coupling gapped twins.

*Proof (self-contained; Step 1 generalizes Theorem V of row 785, `library/gap-vmf-lip.md`, checked row 790, from $S^3$ to $S^{m-1}$, crediting gpt-6-astra).*

**Step 1 (Sharp chord-$W_1$ bound on $S^{m-1}$, $m \ge 2$).** Let $\sigma$ be normalized surface measure on $S^{m-1} = \partial B^m \subset \mathbb{R}^m$, $z(k) = \int_{S^{m-1}} e^{k h_1}\, d\sigma(h)$, and $d\mu_F(h) = z(|F|)^{-1} e^{F \cdot h}\, d\sigma(h)$ for $F \in \mathbb{R}^m$. Put $a_m(k) := z'(k)/(k z(k))$ ($a_m(0) = 1/m$). For $F = k u$ ($k > 0$, $|u| = 1$), put $S_k = \int_{\partial B^m} e^{F \cdot h} dS = |\partial B^m| z(k)$ and $V_k = \int_{B^m} e^{F \cdot x} dx = |\partial B^m| \int_0^1 r^{m-1} z(kr)\, dr$. The divergence theorem gives $\int_{\partial B^m} h e^{F \cdot h} dS = F V_k$, while rotational symmetry gives $S_k \frac{z'(k)}{z(k)} u$, hence $V_k/S_k = a_m(k)$ and
$$
a_m(k) = \frac{\int_0^1 r^{m-1} z(kr)\, dr}{z(k)} \le \int_0^1 r^{m-1}\, dr = \frac{1}{m},
$$
because $z(t) = \sum_{j \ge 0} c_j t^{2j}$ ($c_j > 0$) is increasing on $[0, \infty)$. On $B^m$, $b(x) := z(k|x|)/z(k)$ satisfies $\Delta b = k^2 b$ (averaging $\Delta_x e^{k x \cdot h} = k^2 e^{k x \cdot h}$ over $h \in S^{m-1}$), so $w(x) := (1 - b(x))/k^2$ solves $(-\Delta + k^2)w = 1$, $w|_{\partial B^m} = 0$, and $V(x) := -\nabla w(x) + F w(x)$ satisfies $\operatorname{div}(e^{F \cdot x} V) = e^{F \cdot x}$ with $V(h) \cdot h = a_m(k)$ on $\partial B^m$. For any unit vector $e \in \mathbb{R}^m$, $J_e(x) := e^{F \cdot x}(e - (F \cdot e)V(x)) =: e^{F \cdot x} M(x) e$ is divergence-free with $J_e(h) \cdot h = e^{F \cdot h}(h \cdot e - a_m(k) F \cdot e)$. For any smooth $1$-Lipschitz extension $\Phi$ to $B^m$ of a $1$-chord-Lipschitz function $\phi$ on $S^{m-1}$ (obtained by Kirszbraun extension and mollification), the divergence theorem gives $\operatorname{Cov}_{\mu_F}(\phi, h \cdot e) = a_m(k) \int_{B^m} \nabla\Phi(x) \cdot M(x) e\, d\nu_F(x)$ where $d\nu_F = V_k^{-1} e^{F \cdot x} dx$. Writing $e = e_\perp + c u$ and $x = r h$, $s = k r$, $m(s) = z'(s)/z(s)$, direct differentiation gives $M(rh)e = e_\perp + c b(r)(u - m(s)h)$. Conditional on $r$, $h \sim \mu_{su}$ has mean $m(s) u \perp e_\perp$, so $\mathbb{E}_{\nu_F}[|M(x) e|^2 \mid r] = |e_\perp|^2 + c^2 b(r)^2 (1 - m(s)^2) \le |e_\perp|^2 + c^2 = 1$ (since $0 \le b(r) \le 1$ and $|m(s)| \le 1$). Cauchy–Schwarz yields $|\operatorname{Cov}_{\mu_F}(\phi, h \cdot e)| \le a_m(k) \le 1/m$. Integrating along $F(t) = (1-t)F + tF'$ and taking $\sup_{\|\phi\|_{\rm Lip} \le 1}$ gives by Kantorovich–Rubinstein:
$$
W_1^{\rm chord}(\mu_F, \mu_{F'}) \le \frac{1}{m} |F - F'| \qquad \forall F, F' \in \mathbb{R}^m. \tag{2.14}
$$

**Step 2 (Dobrushin matrix on the pinned cylinder $\nu_{X, Y}$).** Let $\mathcal{I}$ be the set of interior links $\Phi_{\rm int}$ of the cylinder $[0, v] \times \Lambda$. Each $e \in \mathcal{I}$ lies in $2(d-1)$ plaquettes, hence shares a plaquette with at most $6(d-1)$ other links $e' \in \mathcal{I}$ (and any pair $(e, e')$ shares at most one plaquette since $n, v \ge 3$). The conditional law $\gamma_e(\cdot \mid U_{-e})$ of $U_e$ under $\nu_{X, Y}$ is $\mu_{F_e}$ with $F_e = \beta \sum_{p \ni e} \sigma_p \in \mathbb{R}^m$, where each staple $\sigma_p$ is a product of $3$ links in $G \subset \mathbb{R}^m$. Because group multiplication in $\mathrm{SU}(2) \subset \mathbb{H}$ or $\mathrm{U}(1) \subset \mathbb{C}$ is an Euclidean isometry of $\mathbb{R}^m$, changing a single neighbour $U_{e'} \to U_{e'}'$ shifts $F_e$ by at most $\beta |U_{e'} - U_{e'}'|$. By (2.14), the Dobrushin interdependence matrix $C_{e, e'} := \frac{\beta}{m} \mathbf{1}_{e \sim e'}$ ($e, e' \in \mathcal{I}$) is symmetric, satisfies $W_1^{\rm chord}(\gamma_e(\cdot \mid U), \gamma_e(\cdot \mid U')) \le \sum_{e' \in \mathcal{I}} C_{e, e'} |U_{e'} - U_{e'}'|$, and has row sums $\le \frac{6(d-1)}{m}\beta = q < 1$. Put $D := (I - C)^{-1} = \sum_{k=0}^\infty C^k$.

**Step 3 (Martingale Dobrushin covariance bound; credit Dobrushin, Föllmer 1982, Künsch 1982).** Order $\mathcal{I} = \{e_1, \dots, e_M\}$. For smooth $f, g$ on $(S^{m-1})^{\mathcal{I}}$, put $\delta_e(f) := \sup_{U = U' \text{ off } e} |f(U) - f(U')| / |U_e - U_e'|$ and form the Doob martingales $M_j = \mathbb{E}_{\nu_{X, Y}}[f \mid \mathcal{F}_j]$, $N_j = \mathbb{E}_{\nu_{X, Y}}[g \mid \mathcal{F}_j]$ ($\mathcal{F}_j = \sigma(U_{e_1}, \dots, U_{e_j})$). Fix $j$ and condition on $\mathcal{F}_{j-1}$, setting $h_j(u) := \mathbb{E}_{\nu_{X, Y}}[f \mid \mathcal{F}_{j-1}, U_{e_j} = u]$. Compare the conditional laws $\nu_u, \nu_{u'}$ on $\mathcal{I}_j = \{e_{j+1}, \dots, e_M\}$ at $U_{e_j} = u$ vs $u'$. Run a systematic-scan Gibbs sampler coupling $(W^{(t)}, \tilde W^{(t)})$ starting from $W^{(0)} = \tilde W^{(0)}$, updating each site $e \in \mathcal{I}_j$ sequentially by an optimal $W_1^{\rm chord}$-coupling of $\gamma_e(\cdot \mid W_{-e}, u)$ and $\gamma_e(\cdot \mid \tilde W_{-e}, u')$. Let $\bar d := (I - C_{\mathcal{I}_j})^{-1} C_{\mathcal{I}_j, e_j} |u - u'| \le (DC)_{\mathcal{I}_j, e_j} |u - u'| = D_{\mathcal{I}_j, e_j} |u - u'|$ (since $C \ge 0$ and $e \ne e_j$). If $\mathbb{E}[|W_e - \tilde W_e|] \le \bar d_e$ holds for all $e \in \mathcal{I}_j$, updating site $e$ yields $\mathbb{E}[|W_e^{\rm new} - \tilde W_e^{\rm new}|] \le C_{e, e_j}|u - u'| + \sum_{e' \in \mathcal{I}_j} C_{e, e'} \bar d_{e'} = \bar d_e$. By induction from $t = 0$, the bound holds at every step. By uniform Doeblin ergodicity of the finite-volume positive-density Gibbs sampler on compact $(S^{m-1})^{\mathcal{I}_j}$, a subsequential limit gives a coupling of $\nu_u$ and $\nu_{u'}$ with $\mathbb{E}[|W_e - \tilde W_e|] \le D_{e, e_j} |u - u'|$ for all $e \in \mathcal{I}_j$ (and trivially for $e = e_j$, as $D_{e_j, e_j} \ge 1$). Therefore $h_j$ is $L_j(f)$-chord-Lipschitz on $S^{m-1}$ with $L_j(f) \le \sum_{e \in \mathcal{I}} \delta_e(f) D_{e, e_j}$. Since $\operatorname{diam}(S^{m-1}) = 2$, $\operatorname{osc}(h_j) \le 2 L_j(f)$, so $\operatorname{Var}(h_j(U_{e_j}) \mid \mathcal{F}_{j-1}) \le L_j(f)^2$. By martingale orthogonality and Cauchy–Schwarz,
$$
\big|\operatorname{Cov}_{\nu_{X, Y}}(f, g)\big| = \left|\sum_{j=1}^M \mathbb{E}[\Delta_j M \, \Delta_j N]\right| \le \sum_{j=1}^M L_j(f) L_j(g) \le \sum_{e, e' \in \mathcal{I}} \delta_e(f)\, \delta_{e'}(g)\, (D D^T)_{e, e'}. \tag{2.15}
$$

**Step 4 (Application to $\mathcal{O}_x^{(1)}$ and $\mathcal{O}_y^{(2)}$).** By (1.5) and isometry of multiplication in $\mathbb{R}^m$, $\delta_e(\mathcal{O}_x^{(1)}) \le \beta$ for the $3$ links $e \in S_x := \{g_0(x), U(1)_{(x,1)}, g_0(x+\hat 1)\}$ and $0$ otherwise; similarly $\delta_{e'}(\mathcal{O}_y^{(2)}) \le \beta$ for $e' \in S'_y := \{g_{v-1}(y), U(v-1)_{(y,1)}, g_{v-1}(y+\hat 1)\}$ and $0$ otherwise. Because $n \ge 3$ and every $y \in \mathcal{C}_1$ has $y_1 = 0$, the sets $(S'_y)_{y \in \mathcal{C}_1}$ are pairwise disjoint! Assign each link its time coordinate $\tau(e) \in \{0, \frac{1}{2}, 1, \dots, v\}$ ($\tau = t$ for slice-$t$ spatial links, $t + \frac{1}{2}$ for slab-$t$ temporal links). Every edge $e \sim e'$ of $C$ changes $\tau$ by at most $1$. Since $\tau(e) \le 1$ on $S_x$ and $\tau(e') \ge v - 1$ on $S'_y$, every nonzero entry $(C^k (C^T)^\ell)_{e, e'} = (C^{k+\ell})_{e, e'}$ between $S_x$ and $\bigcup_y S'_y$ requires $k + \ell \ge v - 2$. Summing (2.15) over $y \in \mathcal{C}_1$ gives
$$
\sum_{y \in \mathcal{C}_1} \big|\operatorname{Cov}_{\nu_{X,Y}}(\mathcal{O}_x^{(1)}, \mathcal{O}_y^{(2)})\big| \le \beta^2 \sum_{e \in S_x} \sum_{k + \ell \ge v - 2} \sum_{e' \in \mathcal{I}} (C^{k+\ell})_{e, e'} \le 3\beta^2 \sum_{r = v - 2}^\infty (r + 1) q^r \le \frac{3\beta^2}{(1 - q)^2} \, v \, q^{v-2}. \quad \square
$$

**3D compact $\mathrm{U}(1)$ at weak coupling (Göpfert–Mack 1982 gapped twin):**
- *Geometric note:* In $d = 3$, the spatial slice $(\mathbb{Z}/n)^2$ has only two spatial directions, so no untouched $23$-plaquette $Q_x$ exists; the appropriate abelian cut map is $R_s^{\rm const}$ ($a_x \equiv i$), which preserves every spatial plaquette and satisfies $R_\pi^{\rm const} = C_1$ everywhere. On the cylinder $[0, v]$, shifting $Y$ by $R_{t-s}^{\rm const}$ is gauge-equivalent to adding a uniform $01$-background shift $\frac{t-s}{nv}$ on every $01$-plaquette with untouched boundaries $(B, C_z A)$.
- *Non-compact 3D Maxwell (massless):* **PROVED** to FAIL Lemma (L) by Theorem B (2.4) at $d = 3$ ($\frac{\beta}{nv} \le \sum_{y_2} |M_v(0, y_2)| \le C_3 \sqrt{n/v} \frac{\beta}{v^2}$).
- *Compact 3D Villain $\mathrm{U}(1)$ at large $\beta$ (gapped, Göpfert–Mack 1982):* **ARGUED** to HOLD at fixed $\beta$ for $v \gg m_{\rm GM}(\beta)^{-1}$ with exponential decay $O(e^{-m_{\rm GM}(\beta) v}) \ll C(\beta) v^{-2-\epsilon}$ (where $m_{\rm GM}(\beta) \sim c\beta^{1/2} e^{-c'\beta} > 0$ is the Debye screening mass of the 3D point-monopole plasma, and $C(\beta)$ grows exponentially with $\beta$; not proved here on the pinned cylinder for arbitrary $s, t$).

### 2.4 Remaining Tests ((g4), (g5), (t3), (t6), (g6)) and Summary Table

- **(g4) Gapless members with an $\mathrm{SU}(2)$ factor:**
  - *Product with a neutral massless spectator:* **PROVED** (Proposition 1.2(1)) that Lemma (L) **remains TRUE** (if true for pure $\mathrm{SU}(2)$) — Lemma (L) is completely blind to neutral spectators. This is not a flaw in Lemma (L) as a confinement/twist-weight lemma, and precisely explains why Lemma (L) does not imply (PUR-io).
  - *4D $\mathrm{SU}(2)$ + adjoint Higgs in the Coulomb phase (belief-grade):* **ARGUED** Lemma (L) **FAILS** ($\Theta(\beta_{\rm eff} v^{-2})$): at large Higgs coupling the massive $W^\pm$ bosons decouple, $a_x(U) \approx \pm \hat\Phi(x)$ aligns with the unbroken $\mathrm{U}(1)$ generator, and $\mathcal{O}_x^{(1)}$ couples directly to the massless photon $E_1^{\rm em}$.
  - *K7 fundamental-adjoint critical endpoint (belief-grade confining massless $0^{++}$ scalar):* **ARGUED** Lemma (L) **FAILS** ($\Theta(v^{-2})$), because on a pinned cylinder with generic fixed $(X, Y)$, boundary data break parity and allow $\mathcal{O}_x^{(1)}$ to couple to the massless scalar (Dirichlet BCs induce normal derivatives at $t = 0, v$, giving $\operatorname{Cov}_D \sim r^{-4}$ and cut sum $\sim v^{-2}$), whereas the **signed** variant (L-signed) can still hold at K7 since electric flux remains confined ($Z^{e_1}/Z^0 \to 1$).
- **(g5) Scale test / Remark STAB (PROVED GIVEN row 1143/1144):** Fix $(n, v)$ and let $\beta \to \infty$ in 4D $\mathrm{SU}(2)$. By row 1143 (6) (checked row 1144), the one-plane twist cost obeys $\log(Z^0(2v)/Z^{e_1}(2v)) = \frac{3}{2}\log\beta + \log\log\beta + O_{n, v}(1) \to +\infty$. Substituting into Theorem A(2) (1.7) proves unconditionally:
  $$
  \mathcal{L}_0^{\mathrm{SU}(2), 4}(n, v; \beta) \ge \mathcal{L}_0^{\rm signed, \mathrm{SU}(2), 4}(n, v; \beta) \ge \frac{3}{\pi^2 n^2} \log\beta + O_{n, v}(1) \longrightarrow +\infty \quad (\beta \to \infty). \tag{2.16}
  $$
  Thus no $\beta$-uniform constant $C$ can exist on a fixed lattice: Lemma (L) **PASSES (g5) / Remark STAB**. (In fact, at $s = t = 0$, linearized gluons grow as $\Theta(\beta v^{-2})$.)
- **(t3) Group test ($\mathrm{SU}(3)$ and general $\mathrm{SU}(N)$; PROVED):** Check 1556's circle action extends to every $\mathrm{SU}(N)$ ($N \ge 2$) with no reliance on $\dim\mathfrak{su}(2) = 3$. On the full-Haar-measure conjugation-invariant set where $Q_x \in \mathrm{SU}(N)$ has distinct eigenvalues $e^{i\theta_1}, \dots, e^{i\theta_N}$ with $-\pi < \theta_1 < \dots < \theta_N < \pi$, let $P_N(Q_x)$ be the rank-$1$ orthogonal projector onto the $e^{i\theta_N}$-eigenspace and put $a_x(Q_x) := i(I - N P_N(Q_x)) \in \mathfrak{su}(N)$ (and $0$ on the null discriminant locus). Then $a_x$ is gauge-covariant ($Q_x \mapsto g Q_x g^{-1} \Rightarrow P_N \mapsto g P_N g^{-1}$), commutes with all centre flips $C_z$ (since $C_z Q_x = Q_x$), is independent of $1$-links, and satisfies $\exp(\frac{2\pi}{N} a_x) = e^{2\pi i/N} I \exp(-2\pi i P_N) = e^{2\pi i/N} I$ a.e., reaching the centre twist at $s = 2\pi/N$.
- **(t6) Villain $\mathrm{U}(1)$ and finite subgroups:** Villain $\mathrm{U}(1)$ is covered in §2.1 (fails right at $-2$ conditional on periodic $\beta_{\rm eff} > 0$). Finite subgroups ($\mathbb{Z}_2, Q_8, 2I$) admit no continuous circle action $R_s$; in a deep-well $\mathrm{SU}(2)$ perturbation concentrating near $Q_8$ or $2I$, the weak-coupling deconfined phase has $\log(Z^0/Z^{e_1}) \asymp \sigma_{\rm dual} n^2$, forcing $\mathcal{L}_0 \ge c \sigma_{\rm dual} > 0$ (not even $v^{-2}$) by (1.7).

| Test model | Status of Lemma (L) | Exponent / bound | Proof standing |
|---|---|---|---|
| 4D Gaussian Maxwell | **FAILS** | $\frac{\beta}{nv} \le \mathcal{L}_0 \le C \frac{\beta}{v^2}$ | **PROVED** (Theorem B) |
| 4D compact $\mathrm{U}(1)$ (Villain/Wilson), large $\beta$ | **FAILS** | $\mathcal{L}_0 \ge \max\{\frac{\beta_{\rm eff}}{nv},\, \frac{2}{\pi^2 n^2}\log\frac{Z^0}{Z^{e_1}}\}$ | **PROVED** lower bound (Thm C); failure **CONDITIONAL** on periodic $\beta_{\rm eff} \ge c_0 > 0$ |
| 5D $\mathrm{SU}(2)$, weak coupling ($\beta > \beta_c^{\rm 5D} \approx 1.64$, incl. $[2, 3]$) | **FAILS** | $\mathcal{L}_0 \ge \frac{2}{\pi^2 n^3}\log\frac{Z^0}{Z^{e_1}} \asymp \beta_{\rm eff} v^{-2}$ | Lower bound **PROVED** (Thm A); failure **ARGUED** (5D masslessness belief-grade) |
| 4D $\mathrm{SU}(2)$ ($\beta < 2/9$), 5D $\mathrm{SU}(2)$ ($\beta < 1/6$), 4D $\mathrm{U}(1)$ ($\beta < 1/9$), 3D $\mathrm{U}(1)$ ($\beta < 1/6$) | **HOLDS** | $\le \frac{3\beta^2}{(1-q)^2} v q^{v-2}$ uniformly in $(X, Y)$ | **PROVED** unconditionally (Theorem E) |
| 3D compact Villain $\mathrm{U}(1)$, large $\beta$ ($R_s^{\rm const}$) | **HOLDS** (expected) | $O(e^{-m_{\rm GM}(\beta) v})$ for $v \gg m_{\rm GM}^{-1}$ | **ARGUED** (Göpfert–Mack 1982); massless non-compact 3D Maxwell **PROVED** to fail (Thm B) |
| 4D $\mathrm{SU}(2) \times$ neutral massless spectator | **BLIND** (unchanged) | Identical to pure 4D $\mathrm{SU}(2)$ | **PROVED** (Prop. 1.2(1)); excludes (L) $\Rightarrow$ (PUR-io) |
| 4D $\mathrm{SU}(2)$ + adjoint Higgs (Coulomb) / K7 scalar | **FAILS** | $\Theta(v^{-2})$ | **ARGUED** (K7 may still satisfy (L-signed)) |
| 4D $\mathrm{SU}(2)$ at fixed $(n, v)$, $\beta \to \infty$ (Remark STAB) | **FAILS** | $\ge \frac{3}{\pi^2 n^2}\log\beta - O_{n,v}(1) \to \infty$ | **PROVED GIVEN** row 1143 (6) / check 1144 |
| 4D $\mathrm{SU}(N)$ ($N \ge 3$) | **Well-posed** | $a_x = i(I - N P_N(Q_x))$, $R_{2\pi/N} = C_1$ a.e. | **PROVED** (Passes (t3)) |

**Conclusion of the pre-proof tests:** Unlike the algebraic or UV facts of rows 1530, 1532, 1538, and 1549 (checked in 1535, 1543, 1546, 1551), Lemma (L) **genuinely passes test (g3)** (the gapped-twin test): its truth value changes across phase transitions inside fixed $(G, d)$ (holds in strong-coupling 4D $\mathrm{U}(1)$ and 5D $\mathrm{SU}(2)$, fails in weak-coupling 4D $\mathrm{U}(1)$ and 5D $\mathrm{SU}(2)$; holds in gapped 3D compact $\mathrm{U}(1)$, fails in massless 3D Maxwell) and fails as $\beta \to \infty$ at fixed $(n, v)$. Thus Lemma (L) is a genuine non-perturbative dynamical confinement/mixing statement — and for the exact same reason, proving it at $\beta \in [2, 3]$ cannot come from any algebra-, dimension-count-, or UV-only argument.

---

## 3. Three Distinct Attacks on Lemma (L) for 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$

Because Lemma (L) is expected to **HOLD** for 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$ (with exponential decay $O(e^{-m(\beta) v})$, since the bulk is believed to be in a single massive confining phase with correlation length $\xi(\beta) \in [1, 30]$, GUIDE), no refutation is expected at $\beta \in [2, 3]$ (we also verified in §1.2 that the non-smoothness of $a_x$ at $Q_x = \pm 1$ produces no singularity and that $|\mathcal{O}_x^{(1)}| \le \beta$ everywhere). Conversely, by Theorem A(3), proving Lemma (L) at $\beta = 3$ would prove rigorous electric-flux confinement $\lim_{v \to \infty} Z^{e_1}(2v; \beta=3)/Z^0(2v; \beta=3) = 1$, a major open problem (cf. row 792).

We attack Lemma (L) at $\beta \in [2, 3]$ by **three genuinely distinct methods**, proving exact identities and sharp partial theorems in each and pinpointing the exact wall where each stops.

---

### 3.1 Attack 1: Transfer-Operator Spectral Decomposition and Two-Slice Integration by Parts

#### Theorem 1 (Exact Two-Slice Integration-by-Parts Identity; PROVED)

Let $D_1, D_2$ be any two divergence-free (Haar-preserving) first-order differential operators on $G^{\mathcal{E}}$ with bounded coefficients (in particular $D_1 = D_x$, $D_2 = D_y$ of (1.3), or any linear combination $D_f = \sum_{x \in \mathcal{C}_1} f(x_\perp) D_x$). Then for every $\beta > 0$, $n \ge 3$, $v \ge 2$, and $z \in \mathbb{Z}_2^{d-1}$:
$$
\mathbb{E}_{\mu_{z, 2v}}\!\big[(D_1^{(1)} D_2^{(2)} \log K_v)(B, C_z A)\big]
= -\mathbb{E}_{\mu_{z, 2v}}\!\Big[\big((D_1^{(2)} \log K_v)(A, B) + (D_1^{(1)} \log K_v)(B, C_z A)\big)\, (D_2^{(2)} \log K_v)(B, C_z A)\Big]. \tag{3.1}
$$
At $z = 0$ (where $K_v(A, B) = K_v(B, A)$ and $\mathbb{E}_{\mu_{0,2v}}[D_j \log K_v] = 0$), this simplifies to
$$
\mathbb{E}_{\mu_{0, 2v}}\!\big[(D_1^{(1)} D_2^{(2)} \log K_v)(B, A)\big]
= -2 \, \operatorname{Cov}_{\mu_{0, 2v}}\!\big((D_1^{(1)} \log K_v)(B, A),\, (D_2^{(2)} \log K_v)(B, A)\big). \tag{3.2}
$$

*Proof.* First verify skew-adjointness of $D_x$ on $L^2(G^{\mathcal{E}}, dU)$: for fixed links other than $U_{(x, 1)}$, $a_x(U)$ is constant and $R_{\theta e_x}$ is left-multiplication on $U_{(x, 1)}$ by $e^{\theta a_x}$, preserving product Haar measure. For smooth $f, g$ on compact $G^{\mathcal{E}}$, differentiating $\int f(R_{\theta e_x} U) g(R_{\theta e_x} U)\, dU = \int f(U) g(U)\, dU$ at $\theta = 0$ (justified by dominated convergence since $|a_x| \le 1$) gives $\int (D_x f) g\, dU = -\int f (D_x g)\, dU$, with no boundary term and no singularity at $Q_x = \pm 1$ (where $D_x = 0$). Now write $D_1^{(1)} D_2^{(2)} \log K_v = (D_1^{(1)} D_2^{(2)} K_v)/K_v - (D_1^{(1)} \log K_v)(D_2^{(2)} \log K_v)$. Multiplying by $d\mu_{z, 2v}(A, B) = Z^z(2v)^{-1} K_v(A, B) K_v(B, C_z A)\, dA\, dB$, the first term is
$$
\frac{1}{Z^z(2v)} \iint K_v(A, B)\, \big(D_1^{(1)} D_2^{(2)} K_v\big)(B, C_z A)\, dA\, dB
= -\frac{1}{Z^z(2v)} \iint \big(D_1^{(2)} K_v\big)(A, B)\, \big(D_2^{(2)} K_v\big)(B, C_z A)\, dA\, dB
$$
by skew-adjointness of $D_1$ in the variable $B$. Dividing and multiplying by $K_v(A, B) K_v(B, C_z A)$ gives (3.1). At $z = 0$, $K_v(A, B) = K_v(B, A)$ gives $(D_1^{(2)} \log K_v)(A, B) = (D_1^{(1)} \log K_v)(B, A)$, and $\mathbb{E}_{\mu_{0,2v}}[D_1^{(1)}\log K_v] = \frac{1}{2} Z^0(2v)^{-1} \iint D_1^{(1)}(K_v(B, A)^2)\, dA\, dB = 0$, yielding (3.2). $\square$

*(Check: (3.2) is also equivalent to applying the law of total covariance to the identity $0 = \operatorname{Cov}_{\mathbb{T}}(S_1(B), S_2(A))$ for the full-torus link scores $S_1(B) = D_1^{(B)}(-S_{\mathbb{T}})$ and $S_2(A) = D_2^{(A)}(-S_{\mathbb{T}})$, which have zero covariance on $\mathbb{T}$ by Haar IBP since $v \ge 2$.)*

#### Theorem 2 (Exact Spectral–Thermal Upper Bound at $s = t = 0$, $z = 0$; PROVED)

Let $\lambda_0 > \lambda_1 \ge \lambda_2 \ge \dots > 0$ be the eigenvalues of $T = \mathsf{T}_P$ on $\mathcal{H}_{\rm inv}$, $m(\beta, n) := -\log(\lambda_1/\lambda_0) > 0$ the full (all-sector) transfer gap, and $S(t; n^{d-1}) := \sum_{j \ge 1} (\lambda_j/\lambda_0)^t$ the full thermal sum. Then for every $\beta > 0$, $n \ge 3$, $v \ge 4$, every integer $k \ge 0$ with $r := v - 2 - 2k \ge 1$ (so $v - r = 2k + 2$), and every $(X, Y)$:
1. **(Pointwise kernel bound):**
   $$
   \big|(D_x^{(1)} D_y^{(2)} \log K_v)(X, Y)\big| \le 8\beta^2 \lambda_1^r \frac{\sqrt{K_{v-r}(X, X) K_{v-r}(Y, Y)}}{K_v(X, Y)}. \tag{3.3}
   $$
2. **(Integrated bound at $s = t = 0$, $z = 0$):**
   $$
   \sup_{x \in \mathcal{C}_1} \sum_{y \in \mathcal{C}_1} \mathbb{E}_{\mu_{0, 2v}}\!\big|(D_x^{(1)} D_y^{(2)} \log K_v)(B, A)\big| \le 8\beta^2 n^{d-2} \, e^{-r \, m(\beta, n)} \frac{1 + S(v - r;\, n^{d-1})}{\sqrt{1 + S(2v;\, n^{d-1})}}. \tag{3.4}
   $$

*Proof.* Define boundary states in $\mathcal{H}_{\rm inv}$ at slices $1$ and $v - 1$: $\alpha_X(U_1) := A_T(X, U_1)$ and
$$
\dot\alpha_{X, x}(U_1) := e^{-\frac{1}{2}V(X) - \frac{1}{2}V(U_1)} \int_{\mathcal{G}} \mathcal{O}_x^{(1)}(X, g_0, U_1) K_0(X, g_0 \cdot U_1)\, dg_0,
$$
and analogously $\alpha_Y, \dot\alpha_{Y, y}$ at slice $v - 1$. Then $K_v(X, Y) = \langle \alpha_X, T^{v-2} \alpha_Y \rangle$, $|\dot\alpha_{X, x}(U_1)| \le \beta \alpha_X(U_1)$ pointwise, and $|\dot\alpha_{Y, y}(U_{v-1})| \le \beta \alpha_Y(U_{v-1})$ pointwise. Let $\Omega$ be the positive ground state of $T$ (`library/gap-transfer.md` Statement 4), put $\mu_{X, x} := \langle \Omega, \dot\alpha_{X, x} \rangle / \langle \Omega, \alpha_X \rangle$ ($|\mu_{X, x}| \le \beta$) and $\mu_{Y, y} := \langle \Omega, \dot\alpha_{Y, y} \rangle / \langle \Omega, \alpha_Y \rangle$ ($|\mu_{Y, y}| \le \beta$), and set $\hat\alpha_{X, x} := \dot\alpha_{X, x} - \mu_{X, x} \alpha_X$, $\hat\alpha_{Y, y} := \dot\alpha_{Y, y} - \mu_{Y, y} \alpha_Y$. Shifting $\mathcal{O}_x^{(1)} \mapsto \mathcal{O}_x^{(1)} - \mu_{X, x}$ and $\mathcal{O}_y^{(2)} \mapsto \mathcal{O}_y^{(2)} - \mu_{Y, y}$ leaves $\operatorname{Cov}_{\nu_{X,Y}}$ unchanged, while $\langle \Omega, \hat\alpha_{X, x} \rangle = \langle \Omega, \hat\alpha_{Y, y} \rangle = 0$ and $|\hat\alpha_{X, x}| \le 2\beta \alpha_X$, $|\hat\alpha_{Y, y}| \le 2\beta \alpha_Y$ pointwise. Letting $Q_\Omega = I - |\Omega\rangle\langle\Omega|$ and $T_\perp = Q_\Omega T Q_\Omega$ ($\|T_\perp\| = \lambda_1$), the vacuum projector annihilates $\hat\alpha_{X, x}$ and $\hat\alpha_{Y, y}$, so
$$
(D_x^{(1)} D_y^{(2)} \log K_v)(X, Y) = \frac{\langle \hat\alpha_{X, x}, T_\perp^{v-2} \hat\alpha_{Y, y} \rangle}{K_v(X, Y)} - \frac{\langle \hat\alpha_{X, x}, T_\perp^{v-2} \alpha_Y \rangle}{K_v(X, Y)} \cdot \frac{\langle \alpha_X, T^{v-2} \hat\alpha_{Y, y} \rangle}{K_v(X, Y)}. \tag{3.5}
$$
Write $T_\perp^{v-2} = Q_\Omega T^k T_\perp^r T^k Q_\Omega$. Because $T^k$ has a pointwise positive integral kernel $K_k > 0$ and $|\hat\alpha_{X, x}| \le 2\beta \alpha_X$ pointwise, $|(T^k \hat\alpha_{X, x})(U)| \le 2\beta (T^k \alpha_X)(U)$ pointwise, whence
$$
\|Q_\Omega T^k \hat\alpha_{X, x}\|_2 \le \|T^k \hat\alpha_{X, x}\|_2 \le 2\beta \|T^k \alpha_X\|_2 = 2\beta \sqrt{\langle \alpha_X, T^{2k} \alpha_X \rangle} = 2\beta \sqrt{K_{2k+2}(X, X)} = 2\beta \sqrt{K_{v-r}(X, X)}.
$$
Applying Cauchy–Schwarz to the first numerator in (3.5) gives $|\langle \hat\alpha_{X, x}, T_\perp^{v-2} \hat\alpha_{Y, y} \rangle| \le 4\beta^2 \lambda_1^r \sqrt{K_{v-r}(X, X) K_{v-r}(Y, Y)}$. In the second term of (3.5), the second factor equals $\mathbb{E}_{\nu_{X,Y}}[\mathcal{O}_y^{(2)} - \mu_{Y, y}]$, which is bounded in magnitude by $2\beta$, while the first numerator is bounded by $\lambda_1^r \|T^k \hat\alpha_{X, x}\|_2 \|T^k \alpha_Y\|_2 \le 2\beta \lambda_1^r \sqrt{K_{v-r}(X, X) K_{v-r}(Y, Y)}$. Adding the two terms proves (3.3).

For (3.4), integrate (3.3) against $d\mu_{0, 2v}(A, B) = Z^0(2v)^{-1} K_v(B, A)^2 dA dB$. One factor of $K_v(B, A)$ cancels, and Cauchy–Schwarz in $L^2(dA\, dB)$ gives
$$
\begin{aligned}
\frac{1}{Z^0(2v)} \iint K_v(B, A) \sqrt{K_{v-r}(B, B) K_{v-r}(A, A)}\, dA\, dB
&\le \frac{1}{Z^0(2v)} \sqrt{\iint K_v(B, A)^2\, dA\, dB} \sqrt{\iint K_{v-r}(B, B) K_{v-r}(A, A)\, dA\, dB} \\
&= \frac{\sqrt{Z^0(2v)} \, Z^0(v - r)}{Z^0(2v)} = \frac{Z^0(v - r)}{\sqrt{Z^0(2v)}}.
\end{aligned}
$$
Multiplying by $8\beta^2 \lambda_1^r = 8\beta^2 \lambda_0^r e^{-r m(\beta, n)}$, writing $Z^0(t) = \lambda_0^t (1 + S(t; n^{d-1}))$, and summing over the $n^{d-2}$ sites $y \in \mathcal{C}_1$ gives (3.4). $\square$

**Exact failure points of Attack 1 at $\beta \in [2, 3]$:**
1. *(Failure 1a — circularity at $s = t = 0$):* To make (3.4) decay as $C v^{-2-\epsilon}$ at $\beta \in [2, 3]$, one needs **both** a volume-uniform **all-sector** gap $m(\beta, n) \ge m_0(\beta) > 0$ (including all seven centre-charged electric-flux sectors) **and** a sub-exponential bound $S(v-r; n^3) = o(e^{r m_0}/n^2)$ on the full periodic thermal sum at $\beta \in [2, 3]$ — inputs stronger than the open full periodic seed at $\beta \in [2, 3]$. (In 4D $\mathrm{U}(1)$ at weak coupling, $m(\beta, n) \sim (2\beta_{\rm eff} n)^{-1}$, so $r m(\beta, n) = O(1)$ and (3.4) fails to decay.)
2. *(Failure 1b — rough-cut denominator mismatch for $s, t \in (0, \pi)$):* While the spatial action factor $e^{-V(R_s B)/2}$ cancels between $\sqrt{K_{v-r}(R_s B, R_s B)}$ and $K_v(R_s B, R_t C_z A)$ in (3.3), integrating (3.3) at $s, t \in (0, \pi)$ against $d\mu_{z, 2v}(A, B)$ leaves the uncancelled ratio
   $$
   \frac{K_v(B, C_z A)}{K_v(R_s B, R_t C_z A)} \cdot \lambda_0^r \sqrt{K_{v-r}(R_s B, R_s B) K_{v-r}(R_t C_z A, R_t C_z A)}.
   $$
   Controlling its $\mu_{z, 2v}$-expectation requires $L^1(\mu_{z, 2v})$ control of the excited-state ratio $E_v(R_s B, R_t C_z A) = K_v(R_s B, R_t C_z A)/(\lambda_0^v \Omega(R_s B)\Omega(R_t C_z A)) - 1$ on cut-roughened boundaries $R_s B$ that lie outside the typical support of $\Omega^2$. Meanwhile, Theorem 1's IBP identity (3.1)–(3.2) applies only to the *signed* mean at $s = t = 0$, not to the absolute value.

---

### 3.2 Attack 2: Pinned-Cylinder Dobrushin Contraction and Non-Abelian Interior Ward / OpenAI-Style Commutator Deformations

Here we work directly inside the pinned cylinder measure $\nu_{X, Y}$ without assuming a transfer gap.

1. **Dobrushin contraction (Theorem E) and its exact barrier at $\beta \in [2, 3]$:**
   Theorem E proves uniform exponential decay across all $(X, Y)$ for $\beta < 2/9$ in 4D $\mathrm{SU}(2)$. At $\beta \in [2, 3]$, $q = \frac{9}{2}\beta \in [9, 13.5] \gg 1$. Crucially, this is **not** a merely technical artifact of single-link Dobrushin: by **Proposition CA-FAIL** (row 1072, checked rows 1074–1075, via Fröhlich–Simon–Spencer 1976), at every $\beta > 2 W_3 \approx 1.0109$ (in particular every $\beta \in [2, 3]$), **no boundary-uniform mixing / complete analyticity criterion holds** (for a single pinned slab $v = 1$ with $X = Y = I$, the temporal links $g_0$ form an ordered 3D $O(4)$ ferromagnet with spontaneous long-range order). Thus any proof at $\beta \in [2, 3]$ must necessarily average over $\mu_{z, 2v}$ (typical boundaries) and cannot be uniform in $(X, Y)$.

2. **Exact Covariant Ampère / Schwinger–Dyson Transport into the Cylinder Interior (PROVED):**

   **Proposition 4 (PROVED).** For fixed $(X, Y)$ and $x \in \mathcal{C}_1$, define the parallel-transported axis on slice $t = 1$ by $\tilde a_x(1) := g_0(x)^{-1} a_x(X) g_0(x) \in \operatorname{Im}\mathbb{H}$. Then for every $v \ge 3$ and every $y \in \mathcal{C}_1$,
   $$
   \operatorname{Cov}_{\nu_{X, Y}}\!\big(\mathcal{O}_x^{(1)},\, \mathcal{O}_y^{(2)}\big) = \operatorname{Cov}_{\nu_{X, Y}}\!\Big(\mathcal{O}_x^{(1),\, 1 \to 2} + \mathcal{M}_x^{(1),\, 1},\;\; \mathcal{O}_y^{(2)}\Big), \tag{3.6}
   $$
   where $\mathcal{O}_x^{(1),\, 1 \to 2} := \beta \operatorname{Im}\!\big(g_1(x) U(2)_{(x,1)} g_1(x+\hat 1)^{-1} U(1)_{(x,1)}^{-1}\big) \cdot \tilde a_x(1)$ is the next-slab electric field along $\tilde a_x(1)$ and $\mathcal{M}_x^{(1),\, 1} := -\sum_{j \in \{\pm 2, \pm 3\}} \beta \operatorname{Im}\!\big(P_{1j}(x, 1)\big) \cdot \tilde a_x(1)$ is the spatial magnetic-curl force on $U(1)_{(x,1)}$ along $\tilde a_x(1)$ (with each $P_{1j}(x, 1) = U(1)_{(x,1)} U(1)_{(x+\hat 1, j)} U(1)_{(x+\hat j, 1)}^{-1} U(1)_{(x, j)}^{-1}$ based at $x$ starting along $+1$).

   *Proof.* Rotate the single interior link $U(1)_{(x, 1)} \mapsto e^{-\theta \tilde a_x(1)} U(1)_{(x, 1)}$ while holding all other links of $\Phi_{\rm int}$ fixed. Because $\tilde a_x(1)$ depends only on $X$ and $g_0(x)$ (not on $U(1)_{(x,1)}$), this rotation preserves Haar measure $dU(1)_{(x,1)}$. Using $\operatorname{Re}(a q) = \operatorname{Re}(q a) = -\operatorname{Im}(q) \cdot a$ for $a \in \operatorname{Im}\mathbb{H}$, we compute the $\theta$-derivative at $\theta = 0$ of each of the six plaquettes containing $U(1)_{(x,1)}$:
   - On slab $0$, $P_{01}(x, 0) \mapsto e^{-\theta a_x(X)} P_{01}(x, 0)$, giving $-\beta \operatorname{Re}(a_x P_{01}(x,0)) = +\mathcal{O}_x^{(1)}$.
   - On slab $1$, $P_{01}(x, 1) = g_1(x) U(2)_{(x,1)} g_1(x+\hat 1)^{-1} U(1)_{(x,1)}^{-1} \mapsto P_{01}(x, 1) e^{+\theta \tilde a_x(1)}$, giving $+\beta \operatorname{Re}(P_{01}(x, 1) \tilde a_x(1)) = -\mathcal{O}_x^{(1),\, 1 \to 2}$.
   - On each of the four spatial plaquettes $P_{1j}(x, 1)$ ($j \in \{\pm 2, \pm 3\}$), $P_{1j}(x, 1) \mapsto e^{-\theta \tilde a_x(1)} P_{1j}(x, 1)$, giving $-\beta \operatorname{Re}(\tilde a_x(1) P_{1j}(x, 1)) = +\beta \operatorname{Im}(P_{1j}(x, 1)) \cdot \tilde a_x(1)$, whose sum is $-\mathcal{M}_x^{(1),\, 1}$.

   Thus $\left.\frac{\partial}{\partial\theta}\right|_{\theta=0} (-\widetilde{S}) = \mathcal{O}_x^{(1)} - \mathcal{O}_x^{(1),\, 1\to 2} - \mathcal{M}_x^{(1),\, 1}$. Since $\mathcal{O}_y^{(2)}$ does not depend on $U(1)_{(x, 1)}$ for $v \ge 3$, Haar integration by parts gives $\mathbb{E}_{\nu_{X,Y}}[(\mathcal{O}_x^{(1)} - \mathcal{O}_x^{(1), 1 \to 2} - \mathcal{M}_x^{(1), 1}) F] = 0$ for both $F = 1$ and $F = \mathcal{O}_y^{(2)}$, proving (3.6). $\square$

3. **Exact failure points of Attack 2 (Ward / OpenAI-style commutator port) at $\beta \in [2, 3]$:**
   Credit: OpenAI authors ("Exponential decay in two-dimensional classical $O(n)$ models", Sept. 2026; "Sharp mass bounds for the two-dimensional $O(4)$ model", Sept. 2026, read via `library/prior/gap-2don-proofs-read-opus.md`, row 1007).
   - *(Failure 2a — non-cancellation of the magnetic curl in Ampère transport):* When summing (3.6) over $x \in \mathcal{C}_1$ on slice $t$, each spatial $12$-plaquette $P_{12}(x, t)$ meets two cut links, $(x, 1)$ and $(x+\hat 2, 1)$, contributing $-\beta \operatorname{Im}(P_{12}(x, t)) \cdot \big(\tilde a_x(t) - \operatorname{Ad}(U(t)_{(x,2)}) \tilde a_{x+\hat 2}(t)\big)$. In $\mathrm{U}(1)$ with $a_x \equiv i$, $\operatorname{Ad}(U) i = i$ so this difference vanishes identically (exact electric-flux conservation!). In $\mathrm{SU}(2)$, iterating (3.6) across $t = 1, \dots, v-1$ with a linear profile $c_t = 1 - t/v$ leaves an $O(1)$ covariant difference $\Delta_j \tilde a_x(t)$ on every one of the $O(v n^2)$ spatial plaquettes meeting the 3D sheet $\{x_1 = 0\} \times [1, v-1]$. Thus variational / Cauchy–Schwarz upper bounds on the transported operator scale as $O(\beta v n^2)$ (growing with $v$, worse than the un-transported 2D cut bound!).
   - *(Failure 2b — structural obstruction to porting the OpenAI 2D commutator-stiffness proof):* In the OpenAI authors' 2D $O(3)$ proof (Proposition 2.2 & Proposition 3.1, row 1007 B(2)), a multiscale family of local rotations $\exp(F_x)$ ($F_x \in \operatorname{span}(a, b)$) has action cost proportional to the *gradient* $\|dF\|_2^2$ (because constant rotations are an exact global symmetry) while its commutator $[F_x, F_y]$ generates the twist axis $c$ with a $\log N$ gain. In 4D $\mathrm{SU}(2)$ on the pinned cylinder $\nu_{X, Y}$:
     - Interior **gauge** transformations $U_{xy} \mapsto g_x U_{xy} g_y^{-1}$ ($g_x = 1$ on $t = 0, v$) leave the interior action identically invariant, giving $0 = 0$ at every order (no Ward inequality; cf. row 1007 B(5) and row 1553 Step 13(a)).
     - Interior **action-preserving staple rotations** (Lemma MC of row 1016, `library/gap-global-reform-max.md` lines 506–529; Proposition LF of row 1034, `library/gap-sym-reg.md` lines 182–200) have identically zero interior Ward current and leave boundary covariances unchanged.
     - Interior **non-gauge link shifts** $U_e \mapsto \exp(F_e) U_e$ ($F_e \in \mathfrak{su}(2)$) pay the covariant curl energy $\beta \|d_U F\|_2^2$. By the checked adjoint-Laplacian gap bounds of rows 1532/1543 and 1538/1546, typical 4D $\mathrm{SU}(2)$ Wilson fields at $\beta \in [2, 3]$ admit no covariantly constant adjoint sections on scales $r \gg 1$ (lowest adjoint eigenvalue $\ge c ((1+\beta)^2 + \sqrt{\log n})^{-1}$, or Lifshitz bound $c (\log\log n / \log n)^{1/2}$), so low-frequency non-gauge modes pay $\gtrsim (\log n)^{-1/2} \|F\|_2^2$ instead of $r^{-2} \|F\|_2^2$, defeating the scale-invariant $\sum 1/r \sim \log v$ commutator accumulation. Moreover, every interior change of variables fixes the pinned ends $(R_s B, R_t C_z A)$ and cannot remove the boundary defect wall at $s, t \in (0, \pi)$.

---

### 3.3 Attack 3: Centre-Coset ($\mathbb{Z}_2 \times \mathrm{SO}(3)$) Conditioning and In-Law Slab Coupling

Because $R_\pi = C_1$ is a $\mathbb{Z}_2$ centre flip, a third distinct approach is to disintegrate the pinned cylinder $\nu_{X, Y}$ along the Mack–Petkova / Tomboulis $\mathbb{Z}_2 \times \mathrm{SO}(3)$ split, or to couple two copies of $\nu_{X, Y}$ slab-by-slab across $t = 1, \dots, v-1$.

#### Proposition 5 (Exact Centre-Coset and Single-Slab Disintegrations; PROVED)

1. **(Centre-coset decomposition).** Choose a measurable section $V: \mathrm{SO}(3) \to \mathrm{SU}(2)$ and write every interior link as $U_e = z_e V_e$ ($z_e \in \{\pm 1\}$, $e \in \mathcal{I}$). Then $\mathcal{O}_x^{(1)} = (dz)_{p_x} \widetilde{\mathcal{O}}_x^{(1)}(V_{\rm int}; X)$ and $\mathcal{O}_y^{(2)} = (dz)_{p_y} \widetilde{\mathcal{O}}_y^{(2)}(V_{\rm int}; Y)$, where $p_x = (x, 0; 01)$ and $p_y = (y, v-1; 01)$ and $(dz)_{p_x} = z_{g_0(x)} z_{U(1)_{(x,1)}} z_{g_0(x+\hat 1)} \in \{\pm 1\}$. Conditioning on $V_{\rm int}$ gives the exact decomposition
   $$
   \begin{aligned}
   \operatorname{Cov}_{\nu_{X, Y}}(\mathcal{O}_x^{(1)}, \mathcal{O}_y^{(2)})
   &= \underbrace{\mathbb{E}_{\nu_{X, Y}}\!\Big[\widetilde{\mathcal{O}}_x^{(1)} \widetilde{\mathcal{O}}_y^{(2)} \operatorname{Cov}_{\mathbb{Z}_2(\cdot \mid V_{\rm int})}\!\big((dz)_{p_x},\, (dz)_{p_y}\big)\Big]}_{\text{Term I: conditional } \mathbb{Z}_2 \text{ gauge covariance}} \\
   &\quad + \underbrace{\operatorname{Cov}_{\nu_{X, Y}}\!\Big(\widetilde{\mathcal{O}}_x^{(1)} \mathbb{E}[(dz)_{p_x} \mid V_{\rm int}],\; \widetilde{\mathcal{O}}_y^{(2)} \mathbb{E}[(dz)_{p_y} \mid V_{\rm int}]\Big)}_{\text{Term II: } \mathrm{SO}(3) \text{ bulk covariance}},
   \end{aligned} \tag{3.7}
   $$
   where conditional on $V_{\rm int}$, $z \in \{\pm 1\}^{\mathcal{I}}$ follows the 4D $\mathbb{Z}_2$ gauge law $\propto \exp\!\big(\sum_p J_p(V) \eta_p(V) (dz)_p\big)$ with $J_p(V) = \beta |\operatorname{Re} V_p|$ and $\eta_p(V) = \operatorname{sign}(\operatorname{Re} V_p)$ (with boundary $z_e \equiv 1$ on $X, Y$).
2. **(Single-slab Durhuus–Fröhlich boundary observable).** Conditioning $\nu_{X, Y}$ on the spatial slices $(U(1), \dots, U(v-1))$ yields
   $$
   \operatorname{Cov}_{\nu_{X, Y}}(\mathcal{O}_x^{(1)}, \mathcal{O}_y^{(2)}) = \operatorname{Cov}_{\nu_{X, Y}}\!\big(f_1(U(1); X),\, f_2(U(v-1); Y)\big), \tag{3.8}
   $$
   where $f_1(U_1; X) := \mathbb{E}_{\nu_{X, Y}}[\mathcal{O}_x^{(1)} \mid U(1) = U_1]$ is the single-bond expectation of $\mathcal{O}_x^{(1)}$ in the 3D $O(4)$ spin model of temporal links $g_0 \in (S^3)^{\Lambda}$ coupled via the $\mathrm{SO}(4)$ link transport $(X_e, U_{1, e})$: $\propto \exp\!\big(\beta \sum_{(w, i)} g_0(w) \cdot (X_{(w, i)} g_0(w+\hat i) U_{1, (w, i)}^{-1})\big)$.

*Proof.* (1) Since $\operatorname{Im}(-q) = -\operatorname{Im}(q)$, factoring $z_e \in \{\pm 1\}$ out of $P_{01}(x, 0)$ and $W_y^{(v)}$ pulls out $(dz)_{p_x}$ and $(dz)_{p_y}$ linearly, and the law of total covariance conditioned on $V_{\rm int}$ gives (3.7). (2) Conditional on $(U(1), \dots, U(v-1))$, the temporal-link layers $g_0, \dots, g_{v-1}$ are mutually independent; since $v \ge 3$, $g_0$ and $g_{v-1}$ are conditionally independent given $(U(1), U(v-1))$, so the law of total covariance collapses to (3.8). $\square$

**Exact failure points of Attack 3 at $\beta \in [2, 3]$:**
1. *(Failure 3a — $\mathbb{Z}_2$ freezing and random-sign frustration in (3.7)):* At $\beta \in [2, 3]$, typical couplings $J_p(V) = \beta|\operatorname{Re} V_p|$ sit well above the exact self-dual critical coupling $\beta_c^{\mathbb{Z}_2, 4D} = \frac{1}{2}\log(1+\sqrt{2}) \approx 0.4407$ of pure 4D $\mathbb{Z}_2$ gauge theory (GUIDE: $\langle J_p \rangle \approx 1.3$ at $\beta = 2$ to $2.25$ at $\beta = 3$). Meanwhile, check 1556 §(vi) (lines 145–147) proves that frustrated $\mathbb{Z}_2$-monopole cubes occur at positive density $c(\beta) > 0$ uniformly in volume, so the conditional $\mathbb{Z}_2$ gauge system is a **frustrated random-sign 4D $\mathbb{Z}_2$ gauge spin glass** (no FKG/Griffiths positivity for Term I). Even if Term I decays exponentially (as in the gapped ordered phase of pure 4D $\mathbb{Z}_2$), $\mathbb{E}[(dz)_{p_x} \mid V_{\rm int}] \approx \eta_{p_x}(V)$ freezes away from monopoles, pushing the entire long-range correlation problem into **Term II (the 4D $\mathrm{SO}(3)$ bulk covariance at $\beta \in [2, 3]$)** — which has the exact same non-perturbative difficulty (and in 5D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$, $\mathbb{Z}_2$ also freezes while Term II retains the $\Theta(v^{-2})$ massless gluon decay!).
2. *(Failure 3b — slab/block coupling and Durhuus–Fröhlich surface ordering in (3.8)):*
   - In (3.8), $f_1(U_1; X)$ is NOT manifestly local in $U_1$ for cold $(X, U_1)$: at $\beta \in [2, 3] > 2 W_3 \approx 1.0109$, the 3D $O(4)$ model of $g_0$ orders on cold slices (and check 1556 §(vi) line 149 shows its $\mathrm{SO}(4)$ transports cannot be made ferromagnetic on generic backgrounds).
   - Direct global Doeblin contraction of $T$ (`gap-transfer.md` Lemma A3(d)) gives rate $1 - e^{-24\beta n^3}$, useless for $v \asymp n$.
   - Local worst-boundary block Hamming contraction fails for block sides $1$–$10$ at $\beta \ge 2.3$ (row 1511 / check 1514). Any viable **in-law** block coupling / disagreement-percolation proof on the cylinder $[0, v]$ must show that non-contracting ("bad") blocks in 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$ are subcritical for percolation — a property that **fails** at the exact same $\beta \in [2, 3]$ in 5D $\mathrm{SU}(2)$ (under $\beta_c^{\rm 5D} \approx 1.64$, GUIDE). Thus Attack 3 reduces directly to a genuinely 4D-selective order-one in-law block-mixing theorem (of kind (K-II) / R10), which remains open.

---

## 4. Stopping Point, Credits, and Claim-by-Claim Audit

### 4.1 Stopping Point (Rule: Equivalent Is Not Progress)

We neither prove nor refute Lemma (L) for 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$. In accordance with the rule **Equivalent is not progress**, we do **not** propose a disguised restatement of Lemma (L) or (PUR-io) as progress. We stop cleanly at **Lemma (L)** itself — noting its two structurally distinct sub-obligations uncovered by Attacks 1–3:
1. **(Typical-slice bulk decay at $s = t = 0$, $z = 0$):**
   $$
   \sup_{x \in \mathcal{C}_1} \sum_{y \in \mathcal{C}_1} \mathbb{E}_{\mu_{0, 2v}}\!\big|\operatorname{Cov}_{\nu_{B, A}}(\mathcal{O}_x^{(1)}, \mathcal{O}_y^{(2)})\big| \le C v^{-2-\epsilon} \qquad (\beta \in [2, 3]). \tag{L-0}
   $$
   This sub-obligation already separates 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$ from weak-coupling 4D $\mathrm{U}(1)$ (Theorem C), from weak-coupling 5D $\mathrm{SU}(2)$ (including $\beta \in [2, 3]$), and from $\beta \to \infty$ at fixed $(n, v)$, while holding in all strong-coupling gapped twins (Theorem E).
2. **(Rough-cut stability for $s, t \in (0, \pi)$ and general $z \in \mathbb{Z}_2^3$):** Controlling the cut-roughened boundaries $(R_s B, R_t C_z A)$ under $\mu_{z, 2v}$, where $K_v(R_s B, R_t C_z A)$ no longer cancels the sewn-torus weight $K_v(B, C_z A)$ (Failure 1b).

The strictly weaker signed bound **(L-signed)** already suffices for the relative twist weights (1.8)–(1.9) via Theorem A(3) and filters out a confining neutral $0^{++}$ critical scalar (K7), but still encounters the exact same non-perturbative 4D confinement/mixing wall at $\beta \in [2, 3]$. Neither (L) nor (L-signed) implies (PUR-io) (Proposition 1.2).

### 4.2 Credits

- **G. 't Hooft (1978, 1979):** Centre twists and electric/magnetic flux sectors on periodic tori.
- **OpenAI authors (Sept.–Oct. 2026):** Pinned-spin stiffness proof and fourth-order commutator-rotation inequality in 2D classical $O(n)$ models (read via `library/prior/gap-2don-proofs-read-opus.md`, row 1007).
- **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text:** The YM4 release, calibrated trajectory, and transfer/continuum framework referenced in `library/gap-k2-tool-design-fable.md` and `library/gap-transfer.md` (with **T. Balaban** for the underlying ultraviolet renormalization-group method).
- **A. Guth (1980); J. Fröhlich and T. Spencer (1982):** Weak-coupling masslessness and dielectric stiffness of 4D compact $\mathrm{U}(1)$ lattice gauge theory.
- **M. Göpfert and G. Mack (1982):** All-coupling confinement and mass gap of 3D compact Villain $\mathrm{U}(1)$.
- **J. Fröhlich, B. Simon, and T. Spencer (1976); K. Osterwalder and E. Seiler (1978); M. Lüscher (1977); B. Durhuus and J. Fröhlich (1980); G. Mack and V. B. Petkova (1979); E. T. Tomboulis (1981, 2007); R. L. Dobrushin (1970); H. Föllmer (1982); H. Künsch (1982); M. Creutz (1979):** Standard statistical-mechanics and lattice gauge theory results cited above.
- **Lane rows credited:** Check 1556 (gpt-6.2-astra: circle map $R_s$, four-corner identity, Lemma (L)); row 1553 (Claude Fable: tests (g1)–(g6)); row 785 / check 790 (gpt-6-astra / Claude Opus: Theorem V on $S^3$); row 786 / check 794 (gpt-6-astra: periodic 4D Villain $\mathrm{U}(1)$ covariance bound); rows 1016, 1034 (Lemma MC, Proposition LF); row 1072 / checks 1074–1075 (CA-FAIL); row 1143 / check 1144 (fixed-box 4D $\mathrm{SU}(2)$ twist asymptotics); row 1468, check 1527, check 1541, rows 1511/1514, 1530/1535, 1532/1543, 1538/1546.

### 4.3 Summary of Claims by Proof Standing

| Claim | Standing |
|---|---|
| Lemma 1.1 (exact pinned-cylinder connected covariance $\operatorname{Cov}_{\nu_{X,Y}}(\mathcal{O}_x^{(1)}, \mathcal{O}_y^{(2)})$, $|\mathcal{O}| \le \beta$, gauge/centre invariance) | **PROVED** |
| Theorem A (four-corner identity, universal lower bound $\mathcal{L}_0 \ge \mathcal{L}_0^{\rm signed} \ge \frac{2}{\pi^2 n^{d-2}}\log(Z^0/Z^{e_1})$, relative twist weights (1.8)–(1.9) from (L-signed)) | **PROVED** |
| Proposition 1.2 (logical incomparability of (L) and (PUR-io) on reflection-positive transfer data via neutral spectator and check 1541 example) | **PROVED** |
| Theorem B (exact $d$-dimensional Gaussian Maxwell kernel $M_v$, signed sum $\frac{\beta}{nv}$, and two-sided bound $\frac{\beta}{nv} \le \sum_y |M_v| \le 4 B_d^{d/2}(n/v)^{(d-2)/2}\frac{\beta}{v^2}$) | **PROVED** |
| Theorem C (exact interacting $\mathrm{U}(1)$ identity $\mathbb{E}[-g''(0)] = 2\operatorname{Var}(g'(0)) = 2(-F''(0))$ and lower bounds $\mathcal{L}_0^{\mathrm{U}(1), d} \ge \max\{\frac{\beta_{\rm eff, d}}{nv}, \frac{2}{\pi^2 n^{d-2}}\log(Z^0/Z^{e_1})\}$) | **PROVED** |
| Proposition D (exact Villain harmonic–monopole factorization (2.11)) | **PROVED** |
| Failure of Lemma (L) and (L-signed) in 4D compact $\mathrm{U}(1)$ at weak coupling ($\ge \frac{c_0}{1024 v^2}$) | **PROVED GIVEN** periodic-torus $\beta_{\rm eff, 4} \ge c_0 > 0$ |
| Theorem E (strong-coupling exponential decay $\le \frac{3\beta^2}{(1-q)^2} v q^{v-2}$ in 4D $\mathrm{SU}(2)$ $\beta<2/9$, 5D $\mathrm{SU}(2)$ $\beta<1/6$, 4D $\mathrm{U}(1)$ $\beta<1/9$, 3D $\mathrm{U}(1)$ $\beta<1/6$, with $S^{m-1}$ chord-$W_1$ and martingale Dobrushin proofs) | **PROVED** |
| Test (g5) / Remark STAB: $\mathcal{L}_0^{\mathrm{SU}(2), 4}(n, v; \beta) \ge \frac{3}{\pi^2 n^2}\log\beta + O_{n,v}(1) \to \infty$ as $\beta \to \infty$ at fixed $(n, v)$ | **PROVED GIVEN** row 1143 (6) / check 1144 |
| Test (t3): explicit $\mathrm{SU}(N)$ circle map $a_x = i(I - N P_N(Q_x))$ reaching $e^{2\pi i/N} I$ at $s = 2\pi/N$ a.e. | **PROVED** |
| Theorem 1 (exact two-slice IBP identity (3.1)–(3.2)) and Theorem 2 (exact spectral–thermal upper bound (3.3)–(3.4) at $s = t = 0, z = 0$) | **PROVED** |
| Proposition 4 (exact covariant Ampère transport (3.6)) and Proposition 5 (exact $\mathbb{Z}_2 \times \mathrm{SO}(3)$ and Durhuus–Fröhlich slab decompositions (3.7)–(3.8)) | **PROVED** |
| Failure of (L) in 5D weak-coupling $\mathrm{SU}(2)$, 4D adjoint-Higgs Coulomb phase, K7 critical endpoint; holding of (L) in 3D weak-coupling Villain $\mathrm{U}(1)$ | **ARGUED** (conditional on standard/belief-grade phase properties or Göpfert–Mack cylinder extension) |
| Lemma (L), (L-signed), (L-0) for 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$, (PUR-io), and the 4D $\mathrm{SU}(2)$ mass gap | **OPEN** |

RESULT: OPEN — Lemma (L) of check 1556 section (v) is neither proved nor refuted for 4D SU(2) at beta in [2, 3]; we stop at Lemma (L) after three distinct attacks (transfer-operator spectral/IBP, Dobrushin/covariant-Ampere/OpenAI-commutator, and Z_2 x SO(3)/slab-coupling). PROVED unconditionally: exact connected-covariance formula (Lemma 1.1); four-corner universal sandwich and relative twist weights from the weaker signed form (L-signed) (Theorem A); logical incomparability of (L) with (PUR-io) via neutral spectators and transfer counterexamples (Proposition 1.2); exact d-dimensional Gaussian Maxwell two-sided scaling Theta_d(beta v^(-2)) confirming and sharpening the lead's rough count (Theorem B); exact interacting U(1) variance-stiffness identity and universal lower bound L_0 >= beta_eff/(n v) (Theorem C, plus Villain factorization Proposition D, refuting (L) in 4D compact U(1) at weak coupling conditional on uniform positive periodic-torus dielectric stiffness); strong-coupling exponential decay L_z <= 3 beta^2 (1-q)^(-2) v q^(v-2) in all four strong-coupling gapped twins (4D SU(2) beta < 2/9, 5D SU(2) beta < 1/6, 4D U(1) beta < 1/9, 3D U(1) beta < 1/6; Theorem E); fixed-lattice blow-up as beta -> infinity given row 1143/1144 (Remark STAB); SU(N) generalization of R_s; exact two-slice IBP identity (Theorem 1), spectral-thermal upper bound at s = t = 0 (Theorem 2), covariant Ampere transport (Proposition 4), and Z_2 x SO(3)/Durhuus-Frohlich decompositions (Proposition 5). ARGUED: failure at the exact exponent -2 in 5D weak-coupling SU(2) (including beta in [2, 3] under belief-grade masslessness), adjoint-Higgs Coulomb, and K7; holding in 3D weak-coupling Villain U(1) (Gopfert-Mack). Even a full proof of Lemma (L) would yield only relative twist weights Z^z(2v)/Z^0(2v) -> 1 at beta in [2, 3], leaving open both the two-period neutral normalization Z_+(2u)/Z_+(u)^2 and the carry to the calibrated release roots beta_K.
