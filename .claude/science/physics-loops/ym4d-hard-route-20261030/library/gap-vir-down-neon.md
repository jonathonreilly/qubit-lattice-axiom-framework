# Attack on `(VIR-down)` on the Order-One Band

**Target:** `(VIR-down)` on the order-one band, in the form accepted by Theorem TR-down with `(HOT)` (row 1610, check 1613).
**Author:** Gemini 4 Neon (XHigh), independent author run. Unchecked by another provider. No Lean run (Lean/Lake are not installed on this machine). One small Python floating-point sanity check was run outside the repository (recorded as GUIDE in §6.4; no proof step uses it).
**Labels used:** `PROVED` (complete hand proof in this file, noting any `ON FILE` premises), `ARGUED`, `GUESSED`, `ON FILE (row ...)`, `GUIDE`.

---

## 0. Reading Log, Duplicate Check, and Target Statement

### 0.1 Sources Read and Process Compliance
- **Required readings (read in full or relevant sections):** `library/gap-direction7-fable.md` (row 1610, in full); `library/gap-direction7-fable-check-astra62.md` (check 1613, in full); `library/gap-mid-max.md` (row 708: Theorem TR, `(VIR_K)`, Lemma 4.1–4.2, §4.4–4.5); `library/gap-vir-sc.md` (row 710: Lemma J, Lemma C, Theorem U, Proposition EL, Theorem B1, §8); `library/gap-thermdi-astra.md` (row 905: spectral ratio `(R)`, §6.2–6.3); `library/gap-twoperiod-solve-fable-check-astra62.md` (check 1521, in full); `library/gap-twoperiod-solve-fable.md` (row 1520, §§1–3); `library/gap-mech-direction4-fable.md` (row 1553: Lemma ALG, tests (g1)–(g6)); `library/gap-r11-tool-design-fable.md` (row 1517: Lemma CONJ, Proposition VOL, TR2) and check 1519; `library/gap-r11-thermal-solve-fable.md` (row 1522: CB1, HI, SQ) and check 1523; `library/gap-mech-direction2-fable.md` (row 1386: Proposition NEG, Remark STAB, Remark PAIR); `library/gap-k2-tool-design-fable.md` (row 1468, §3.1); `library/sa-ym4-lean-trajectory-check-astra62.md` (check 1453: `BND`, `BND-1`, `BND-2`); `library/gap-crux-direction-astra62.md` (row 1461: displays (1)–(2)) and check 1465 summary; `library/gap-solve-astra62.md` (row 1143: (1)–(17), check 1144 summary); `library/gap-solve23-astra62.md` (row 1215: (1)–(5), check 1221 summary); `library/gap-phys-seed.md` (row 720, §3.2 `(MONO-Delta)`); `library/gap-direction-max.md` (row 931, `(ANOM)`); `library/gap-mini-solve-h-fable.md` (row 1198); `library/gap-vacsub-max.md` (row 934, §1); `library/gap-band-neutral-astra62.md` (row 1573) and check 1579; `parts/gap.md` (§1–2); `FINISH.md` RESULT summaries for cited rows.
- **Isolation rule:** No file whose name begins with `gap-vir-down` (other than this file) was opened or read.
- **Duplicate check:** Safe greps over `library/*.md` (excluding `gap-vir-down*`) for `LEV-down`, `anisotropic split`, `spatial-action deficit`, `2 tanh`, `compact Gaussian`, `Poisson integral`, `high-spin` found no prior proof of Theorems 1–4 or Propositions 5–6 below. Row 1610 L188 gives an `ARGUED` momentum-level heuristic against `(LEV-down)` (no proof); Row 1517 Lemma CONJ and Check 1519 §(iv) study the ascending operator form inequality (not descending `(VIR-down)`); Row 1522 Proposition HI localizes ascending `(VIR_K)` for $\beta \le 2$ (not descending `(VIR-down)` for all $\beta > 0$); Row 1143 (13) treats symmetric tori against bulk $f_\beta$ (not the neutral trace $Z_+(t)$ against fixed-box $\lambda_0(\beta)^t$).

### 0.2 Notation and Exact Consumer Target (`ON FILE`, rows 1453, 1461, 1468, 1610, check 1613)
Fix the release witnesses (odd block factor $b > 1$ and calibration level $g_0 \in (0, \delta)$ as in check 1453), and a physical side $\ell \in 1024\mathbb{N}_{>0}$. At cutoff $K$, put $n = n_K = \ell b^K$ and $u = u_K = n_K / 512$ (even, $u \ge 2 b^K \ge 6$). Let $\beta_K = g_K^{-2}$ be the calibrated bare inverse-coupling root. On the spatial torus $B = (\mathbb{Z}/n)^3$ ($|B| = n^3$, set of spatial links $E$ with $|E| = 3|B|$), let $T_\beta$ be the Wilson transfer operator in the shifted action convention $1 - \frac{1}{2}\operatorname{tr} U_p$, $P_0 = \frac{1}{8}\sum_{z \in \mathbb{Z}_2^3} C_z$ the projection onto centre-neutral gauge-invariant states $H_0 = P_0 H_{\mathrm{inv}} \subset L^2(\mathrm{SU}(2)^E, \mathrm{Haar})$, and $R_\beta = P_0 T_\beta$ its neutral restriction:
$$R_\beta = P_0 M_\beta C_\beta M_\beta P_0, \qquad M_\beta = e^{-\frac{\beta}{2} V_1}, \qquad V_1(U) = \sum_{p \text{ spatial}} \left(1 - \tfrac{1}{2}\operatorname{tr} U_p\right) \in [0, 6|B|],$$
where $C_\beta$ is linkwise convolution by $c_\beta(g) = \exp(-\beta(1 - \frac{1}{2}\operatorname{tr} g))$. By check 1613 (and rows 667, 710, 1521; `ON FILE`), for every $\beta > 0$:
- $R_\beta$ is positive semidefinite, injective on $H_0$, trace class, and real-analytic in trace norm on $(0, \infty)$; its top eigenvalue $\lambda_0(\beta) > 0$ is simple with strictly positive unit eigenfunction $\psi_0(\beta) \in H_0$.
- Write the ordered eigenvalues of $R_\beta$ on $H_0$ with multiplicity as $\lambda_0(\beta) > \lambda_1(\beta) \ge \lambda_2(\beta) \ge \dots > 0$, ratios $r_i(\beta) = \lambda_i(\beta)/\lambda_0(\beta) \in (0, 1]$, and energies $m_i(\beta) = -\log r_i(\beta) \in (0, \infty)$ ($m_0 = 0$). Put $\widehat{R}_\beta := R_\beta / \lambda_0(\beta)$.
- For real $t \ge 1$, the neutral thermal sum is $G(t; \beta) = \sum_{i \ge 1} r_i(\beta)^t = \sum_{i \ge 1} e^{-t m_i(\beta)}$. By check 1613 ("Regularity `(R)`", L66–75; `ON FILE`), $G$ is jointly $C^1$ in $(t, \beta) \in [1, \infty) \times (0, \infty)$ with
  $$\partial_\beta G(t; \beta) = t \operatorname{Tr}_{H_0}\!\left(\widehat{R}_\beta^{t-1} \widehat{R}_\beta'\right), \qquad -t \partial_t G(t; \beta) = t \operatorname{Tr}_{H_0}\!\left(\widehat{R}_\beta^{t-1} \Phi(\widehat{R}_\beta)\right) = (1 + G(t; \beta))\, t \bar{E}_t(\beta),$$
  where $\Phi(x) := -x \log x$ on $[0, 1]$ and $\bar{E}_t(\beta) := (1 + G(t; \beta))^{-1} \sum_{i \ge 1} m_i(\beta) r_i(\beta)^t$.
- At integer $t \ge 1$, $1 + G(t; \beta) = Z_+(t; \beta)/\lambda_0(\beta)^t$, and by Lemma D1 (row 1610, check 1613; `ON FILE`):
  $$\partial_\beta \log(1 + G(t; \beta)) = t a_0(\beta) - A_t(\beta),$$
  where $A_t(\beta) = (\sum_z Z^z(t) \mathbb{E}_t^z[S_t^z])/(\sum_z Z^z(t))$ is the mean shifted Wilson action of the neutral torus of period $t$, and $a_0(\beta) = -\frac{d}{d\beta}\log \lambda_0(\beta) = \lim_{v \to \infty} A_v(\beta)/v \ge 0$.
- Define the **thermal coupling-rate ratio** (row 905 `(R)` for the neutral trace):
  $$\mathcal{R}(t; \beta) := \frac{\partial_\beta G(t; \beta)}{-t \partial_t G(t; \beta)} = \frac{\partial_\beta \log(1 + G(t; \beta))}{-t \partial_t \log(1 + G(t; \beta))},$$
  which at integer $t \ge 1$ equals $(t a_0(\beta) - A_t(\beta)) / (t \bar{E}_t(\beta))$.

**Consumer target `(T-down)` (row 1610 §2.3, check 1613; `ON FILE`):** For one $\ell \in 1024\mathbb{N}_{>0}$, one $g_0 \in (0, \delta)$, and infinitely many $K$, there exist $\beta_h > \beta_K$, a continuous $\kappa \ge 0$ on $[\beta_K, \beta_h]$, and $t(\beta) = u \exp\!\left(\int_{\beta_K}^\beta \kappa(s)\,ds\right)$ with $t_h = t(\beta_h)$ such that:
- **`(HOT)`:** $G(t_h; \beta_h) \le 4/21$;
- **`(VIR-down)`:** $\partial_\beta G(t(\beta); \beta) \ge -\kappa(\beta)\, t(\beta)\, \partial_t G(t(\beta); \beta)$ (equivalently $\mathcal{R}(t(\beta); \beta) \ge \kappa(\beta)$) for all $\beta \in [\beta_K, \beta_h]$.

By Theorem TR-down and check 1613, `(T-down)` implies $G(u; \beta_K) \le 4/21$ and (by enlargement) `(PUR-io)`, hence a calibrated continuum limit with a mass gap.

---

## 1. All-$\beta$ Bessel Bounds and High-Spin Collapse: Refutation of `(LEV-down)` and All-State Operator Form Bounds

Row 710 (`gap-vir-sc.md`, checked by row 715) established Lemma J, Lemma C, and Theorem U on the strong-coupling interval $0 < \beta < 4$. Because `(VIR-down)` operates at late bare couplings $\beta \ge \beta_K \sim \frac{11 \log b}{3\pi^2} K \to \infty$, we first extend the Bessel and single-eigenstate bounds to **all $\beta > 0$**. This immediately produces an unconditional refutation of both the levelwise form `(LEV-down)` (row 1610 §3.3) and every all-state operator conjugation / form inequality on $H_0^\perp$ (the descending counterpart of row 1517 Lemma CONJ).

### 1.1 Lemma 1 (All-$\beta$ Bessel ratio and link-weight bounds). `PROVED` (elementary, self-contained; extends row 710 Lemma J from $0 < \beta \le 4$ to all $\beta > 0$)

For every integer $n \ge 0$ and every $\beta > 0$, let $I_n(\beta) := \sum_{k=0}^\infty \frac{(\beta/2)^{n+2k}}{k!(n+k)!}$ (called $J_n$ in row 710), $r_n(\beta) := I_{n+1}(\beta)/I_n(\beta)$, and for $j \in \frac{1}{2}\mathbb{N}_0$ let $c_j(\beta) = \frac{2e^{-\beta}}{\beta} I_{2j+1}(\beta)$ and $\eta_j(\beta) = -\log c_j(\beta)$ (`ON FILE`, row 710 Lemma J(d)). Then:
1. **(Poisson integral identity)** With $(-1)!! := 1$,
   $$I_n(\beta) = \frac{\beta^n}{\pi (2n-1)!!} \int_{-1}^{1} (1 - t^2)^{n - 1/2} e^{\beta t}\,dt.$$
2. **(Strict ratio bound at all couplings)** $0 < r_n(\beta) < 1$ for every $n \ge 0$ and every $\beta > 0$.
3. **(Two-sided link-weight and derivative bounds at all couplings)** For every $j \in \frac{1}{2}\mathbb{N}_0$ and every $\beta > 0$:
   $$e^{-\beta} \frac{(\beta/2)^{2j}}{(2j+1)!} \le c_j(\beta) \le e^{-\beta + \beta^2/4} \frac{(\beta/2)^{2j}}{(2j+1)!},$$
   $$2j - \beta < -\beta \eta_j'(\beta) = 2j - \beta(1 - r_{2j+1}(\beta)) < 2j.$$

**Proof.**
*(1)* Since $n - 1/2 \ge -1/2 > -1$, $(1 - t^2)^{n-1/2} \in L^1(-1, 1)$ is nonnegative and $e^{\beta t} = \sum_{m=0}^\infty \frac{\beta^m t^m}{m!}$ converges uniformly on $[-1, 1]$. Termwise integration eliminates odd $m$ by symmetry. For $m = 2k$, substituting $t = \cos\theta$ gives
$$\int_{-1}^1 (1 - t^2)^{n-1/2} t^{2k}\,dt = 2 \int_0^{\pi/2} \sin^{2n}\theta \cos^{2k}\theta\,d\theta =: 2 W(n, k).$$
Integrating by parts for $k \ge 1$ with $u = \cos^{2k-1}\theta$ and $dv = \sin^{2n}\theta \cos\theta\,d\theta$ yields
$$W(n, k) = \frac{2k-1}{2n+1} \int_0^{\pi/2} \sin^{2n+2}\theta \cos^{2k-2}\theta\,d\theta = \frac{2k-1}{2n+1}\bigl(W(n, k-1) - W(n, k)\bigr),$$
hence $W(n, k) = \frac{2k-1}{2(n+k)} W(n, k-1)$. By symmetry $W(n, 0) = \frac{2n-1}{2n} W(n-1, 0)$ with $W(0, 0) = \pi/2$, induction gives $W(n, k) = \frac{\pi}{2} \frac{(2n-1)!!(2k-1)!!}{2^{n+k}(n+k)!}$. Using $(2k)! = 2^k k! (2k-1)!!$,
$$\frac{\beta^n}{\pi (2n-1)!!} \sum_{k=0}^\infty \frac{\beta^{2k}}{(2k)!} \cdot 2 W(n, k) = \sum_{k=0}^\infty \frac{(\beta/2)^{n+2k}}{k!(n+k)!} = I_n(\beta).$$

*(2)* Since every term in the series for $I_{n+1}(\beta)$ is positive, $r_n(\beta) > 0$. Applying (1) to $I_{n+1}(\beta)$, note that $u(t) := (1 - t^2)^{n+1/2}$ satisfies $u(\pm 1) = 0$ (as $n + 1/2 \ge 1/2 > 0$) and $u'(t) = -(2n+1) t (1 - t^2)^{n-1/2} \in L^1(-1, 1)$. Integrating by parts on $[-1+\varepsilon, 1-\varepsilon]$ and letting $\varepsilon \downarrow 0$ by dominated convergence gives
$$I_{n+1}(\beta) = \frac{\beta^{n+1}}{\pi (2n+1)!!} \cdot \frac{2n+1}{\beta} \int_{-1}^1 t (1 - t^2)^{n-1/2} e^{\beta t}\,dt = \frac{\beta^n}{\pi (2n-1)!!} \int_{-1}^1 t (1 - t^2)^{n-1/2} e^{\beta t}\,dt.$$
Subtracting from (1):
$$I_n(\beta) - I_{n+1}(\beta) = \frac{\beta^n}{\pi (2n-1)!!} \int_{-1}^1 (1 - t)(1 - t^2)^{n-1/2} e^{\beta t}\,dt > 0,$$
since the integrand is strictly positive on $(-1, 1)$. Thus $0 < r_n(\beta) < 1$.

*(3)* From $c_j(\beta) = e^{-\beta} \sum_{k=0}^\infty \frac{(\beta/2)^{2j+2k}}{k!(2j+1+k)!}$, keeping $k = 0$ gives the lower bound. Since $(2j+1+k)! \ge (2j+1)!\, k!$ for all integers $2j+1 \ge 1$ and $k \ge 0$,
$$c_j(\beta) \le e^{-\beta} \frac{(\beta/2)^{2j}}{(2j+1)!} \sum_{k=0}^\infty \frac{(\beta^2/4)^k}{(k!)^2} \le e^{-\beta} \frac{(\beta/2)^{2j}}{(2j+1)!} \sum_{k=0}^\infty \frac{(\beta^2/4)^k}{k!} = e^{-\beta + \beta^2/4} \frac{(\beta/2)^{2j}}{(2j+1)!}.$$
The identity $-\beta \eta_j'(\beta) = 2j - \beta(1 - r_{2j+1}(\beta))$ is row 710 Lemma J(e) (`ON FILE`; follows for all $\beta > 0$ from $\beta I_n' = n I_n + \beta I_{n+1}$), and $0 < 1 - r_{2j+1}(\beta) < 1$ by (2). $\blacksquare$

### 1.2 Theorem 1 (All-$\beta$ single-eigenstate bounds and high-spin collapse of the coupling rate). `PROVED` (given Lemma C of row 710 and the transfer-operator properties of §0.2)

Fix a spatial box $B = (\mathbb{Z}/n)^3$ ($n \ge 3$), put $m := 3|B| = 3n^3$, and let $\beta > 0$. For any unit eigenvector $\psi \in H_0$ of $R_\beta$ with eigenvalue $\lambda > 0$, define $q_\psi(\mathbf{j}) := \|\Pi_{\mathbf{j}} M_\beta \psi\|^2$, $w_\psi(\mathbf{j}) := c_{\mathbf{j}}(\beta) q_\psi(\mathbf{j})/\lambda$, $N(\mathbf{j}) := \sum_{\ell \in E} 2j_\ell$, $R(\mathbf{j}) := \sum_{\ell \in E} (1 - r_{2j_\ell+1}(\beta))$, and $D(\psi; \beta) := \langle \psi, R_\beta' \psi \rangle / \lambda$. Write $D_i(\beta) := D(\psi_i; \beta)$ for any orthonormal eigenbasis $\{\psi_i\}_{i \ge 0}$ of $R_\beta$ on $H_0$. Then:
1. **(All-$\beta$ exact identity and bounds)** For every $\beta > 0$ and every unit eigenvector $\psi \in H_0$ with eigenvalue $\lambda > 0$:
   $$\beta D(\psi; \beta) = \langle N \rangle_{w_\psi} - \beta \langle R \rangle_{w_\psi} - \beta \langle \psi, V_1 \psi \rangle, \qquad -9|B| \le D(\psi; \beta) \le \frac{\langle N \rangle_{w_\psi}}{\beta},$$
   $$-\log \lambda \ge \langle N \rangle_{w_\psi} \log\!\frac{\langle N \rangle_{w_\psi}}{e m \beta / 2} + m\left(\beta - \frac{\beta^2}{4}\right)$$
   (with $0 \log 0 := 0$). Moreover, $0 \le -\log \lambda_0(\beta) \le 9\beta|B|$ and $0 \le a_0(\beta) = -D_0(\beta) \le 9|B|$.
2. **(Infinite rank and pointwise high-spin collapse)** $H_0$ is infinite-dimensional, $m_i(\beta) \to +\infty$ as $i \to \infty$, and for every $\beta > 0$ (uniformly over all choices of orthonormal eigenbasis in degenerate eigenspaces):
   $$\lim_{i \to \infty} \frac{D_i(\beta) - D_0(\beta)}{m_i(\beta)} = 0.$$
3. **(Two-coupling high-spin ratio)** For every $0 < \beta_1 < \beta_2$:
   $$\lim_{i \to \infty} \frac{m_i(\beta_1)}{m_i(\beta_2)} = 1.$$

**Proof.**
*(1)* As in §0.2, each $\Pi_{\mathbf{j}}$ and $M_\beta$ commute with $P$ and every centre flip $C_z$, hence with $P_0$. Thus $\lambda = \langle \psi, R_\beta \psi \rangle = \langle M_\beta \psi, C_\beta M_\beta \psi \rangle = \sum_{\mathbf{j}} c_{\mathbf{j}} q_\psi(\mathbf{j})$ by Lemma C of row 710 (`ON FILE`), so $w_\psi$ is a probability weight on $(\frac{1}{2}\mathbb{N}_0)^E$ and $\sum_{\mathbf{j}} q_\psi(\mathbf{j}) = \|M_\beta \psi\|^2 \le 1$. Differentiating $R_\beta = P_0 M_\beta C_\beta M_\beta P_0$ as in row 710 Theorem U(ii) (`ON FILE`; valid for all $\beta > 0$) gives
$$\beta D(\psi; \beta) = \sum_{\mathbf{j}} w_\psi(\mathbf{j}) \sum_{\ell \in E} \bigl(-\beta \eta_{j_\ell}'(\beta)\bigr) - \beta \langle \psi, V_1 \psi \rangle = \langle N \rangle_{w_\psi} - \beta \langle R \rangle_{w_\psi} - \beta \langle \psi, V_1 \psi \rangle.$$
By Lemma 1(2), $0 < R(\mathbf{j}) < 3|B|$, and $0 \le V_1 \le 6|B|$ with $N(\mathbf{j}) \ge 0$. Hence $-9|B| \le D(\psi; \beta) \le \langle N \rangle_{w_\psi}/\beta$.

For the energy lower bound, Theorem U(iii) of row 710 (`ON FILE`, valid for all $\beta > 0$ via $\sum q_\psi \le 1$ and the log-sum inequality) gives $-\log \lambda = \langle \eta \rangle_{w_\psi} + \sum_{\mathbf{j}} w_\psi(\mathbf{j}) \log(w_\psi(\mathbf{j})/q_\psi(\mathbf{j})) \ge \langle \eta \rangle_{w_\psi}$. Using $(2j+1)! \ge (2j)! \ge (2j/e)^{2j}$ (from $e^k \ge k^k/k!$ for all integers $k \ge 0$) in Lemma 1(3),
$$\eta_j(\beta) = -\log c_j(\beta) \ge 2j \log\!\frac{2j}{e\beta/2} + \beta - \frac{\beta^2}{4}.$$
Summing over the $m = 3|B|$ links and applying Jensen's inequality twice to the convex function $x \mapsto x \log x$ on $[0, \infty)$ (first over the uniform average on the $m$ links, then over $w_\psi$):
$$\eta(\mathbf{j}; \beta) \ge N(\mathbf{j}) \log\!\frac{N(\mathbf{j})}{e m \beta / 2} + m\left(\beta - \frac{\beta^2}{4}\right) \implies -\log \lambda \ge \langle N \rangle_{w_\psi} \log\!\frac{\langle N \rangle_{w_\psi}}{e m \beta / 2} + m\left(\beta - \frac{\beta^2}{4}\right).$$
For the vacuum bounds: $0 < M_\beta \le 1$ and $\|C_\beta\| = c_0(\beta)^m \le 1$ give $\lambda_0(\beta) \le 1$, while testing the constant unit vector $\mathbf{1} \in H_0$ gives $\lambda_0(\beta) \ge \langle \mathbf{1}, M_\beta C_\beta M_\beta \mathbf{1} \rangle \ge e^{-6\beta|B|} c_0(\beta)^{3|B|} \ge e^{-9\beta|B|}$ (using $c_0(\beta) \ge e^{-\beta}$ from Lemma 1(3)). Finally, $a_0(\beta) = -D_0(\beta) = \lim_{v \to \infty} A_v(\beta)/v \ge 0$ (check 1613, Lemma D1), and $-D_0(\beta) \le 9|B|$ by the bound just proved.

*(2)* Fix one spatial plaquette $p_0$. Choosing one edge $e_0$ of $p_0$ and holding the other three fixed, Haar invariance implies that $U \mapsto U_{p_0}$ pushes product Haar measure forward to normalized Haar measure on $\mathrm{SU}(2)$. Each $f_j(U) := \chi_j(U_{p_0})$ ($j \in \mathbb{N}_0$) is gauge-invariant and centre-neutral (every $C_z$ preserves $U_{p_0}$), so $\{f_j\}_{j \in \mathbb{N}_0}$ is an infinite orthonormal set in $H_0$. Thus $\dim H_0 = \infty$. Because $R_\beta$ is compact, positive, and injective on $H_0$, its ordered eigenvalues satisfy $\lambda_i(\beta) \downarrow 0$ and $m_i(\beta) = -\log(\lambda_i/\lambda_0) \to +\infty$.

Put $C := e m \beta / 2 > 0$ and $X_i := \langle N \rangle_{w_{\psi_i}} \ge 0$. Fix any $\alpha > 0$. If $X_i \ge C e^\alpha$, then $\log(X_i / C) \ge \alpha$, so (1) and $-\log\lambda_0 \le 9\beta|B|$ give
$$\alpha X_i \le X_i \log\!\frac{X_i}{C} \le -\log \lambda_i + \frac{m \beta^2}{4} \le m_i(\beta) + 9\beta|B| + \frac{3|B|\beta^2}{4}.$$
Whether $X_i \ge C e^\alpha$ or $X_i < C e^\alpha$, we obtain
$$X_i \le \frac{m_i(\beta) + 9\beta|B| + \frac{3}{4}|B|\beta^2}{\alpha} + C e^\alpha.$$
Since $D_0(\beta) \in [-9|B|, 0]$, part (1) yields $-9|B| \le D_i(\beta) - D_0(\beta) \le X_i/\beta + 9|B|$. Dividing by $m_i(\beta)$:
$$-\frac{9|B|}{m_i(\beta)} \le \frac{D_i(\beta) - D_0(\beta)}{m_i(\beta)} \le \frac{1}{\alpha \beta} + \frac{1}{m_i(\beta)}\left(\frac{9|B| + \frac{3}{4}|B|\beta}{\alpha} + \frac{3 e |B| e^\alpha}{2} + 9|B|\right).$$
Letting $i \to \infty$ gives $0 \le \liminf_{i \to \infty} \frac{D_i - D_0}{m_i} \le \limsup_{i \to \infty} \frac{D_i - D_0}{m_i} \le \frac{1}{\alpha \beta}$. Sending $\alpha \to \infty$ proves (2).

*(3)* Let $\mu_0(\beta) \ge \mu_1(\beta) \ge \dots > 0$ be the ordered eigenvalues of $P_0 C_\beta P_0$ on $H_0$. Because $M_\beta$ is a bounded invertible linear bijection of $H_0$ satisfying $e^{-6\beta|B|} \|\phi\|^2 \le \|M_\beta \phi\|^2 \le \|\phi\|^2$, the Courant–Fischer min–max theorem gives
$$e^{-6\beta|B|} \mu_i(\beta) \le \lambda_i(\beta) \le \mu_i(\beta) \qquad (\forall i \ge 0,\ \forall \beta > 0). \tag{1.1}$$
Now fix $0 < \beta_1 < \beta_2$. By Lemma 1(3), for every $j \in \frac{1}{2}\mathbb{N}_0$,
$$c_j(\beta_1) \le e^{\beta_2 - \beta_1 + \beta_1^2/4} c_j(\beta_2), \qquad c_j(\beta_2) \le e^{\beta_1 - \beta_2 + \beta_2^2/4} \left(\frac{\beta_2}{\beta_1}\right)^{2j} c_j(\beta_1).$$
The first inequality gives $P_0 C_{\beta_1} P_0 \le e^{m(\beta_2 - \beta_1 + \beta_1^2/4)} P_0 C_{\beta_2} P_0$, hence $\mu_i(\beta_1) \le e^{m(\beta_2 - \beta_1 + \beta_1^2/4)} \mu_i(\beta_2)$ for all $i \ge 0$. For the reverse direction, fix any $\varepsilon > 0$ and choose $N_0 \ge 1$ such that $\log\frac{N_0}{e m \beta_2 / 2} \ge \frac{1}{\varepsilon} \log\frac{\beta_2}{\beta_1}$. For every $\mathbf{j}$ with $N(\mathbf{j}) \ge N_0$, combining the second inequality with the bound on $\eta(\mathbf{j}; \beta_2)$ from (1):
$$\log\!\frac{c_{\mathbf{j}}(\beta_2)}{c_{\mathbf{j}}(\beta_1)} \le N(\mathbf{j}) \log\!\frac{\beta_2}{\beta_1} + m\left(\beta_1 - \beta_2 + \frac{\beta_2^2}{4}\right) \le \varepsilon \left(-\log c_{\mathbf{j}}(\beta_2)\right) + K_1,$$
where $K_1 := m\bigl(\beta_1 - \beta_2 + \frac{\beta_2^2}{4} + \varepsilon |\beta_2 - \frac{\beta_2^2}{4}|\bigr)$. Thus $c_{\mathbf{j}}(\beta_1) \ge e^{-K_1} c_{\mathbf{j}}(\beta_2)^{1+\varepsilon}$ for all $N(\mathbf{j}) \ge N_0$. Since $\{ \mathbf{j} : N(\mathbf{j}) < N_0 \}$ is finite and $c_{\mathbf{j}}(\beta_2) \le 1$, putting $\tilde{c}(\varepsilon) := \min\bigl(e^{-K_1}, \min_{N(\mathbf{j}) < N_0} c_{\mathbf{j}}(\beta_1)\bigr) > 0$ yields
$$c_{\mathbf{j}}(\beta_1) \ge \tilde{c}(\varepsilon)\, c_{\mathbf{j}}(\beta_2)^{1+\varepsilon} \qquad \text{for every } \mathbf{j} \in \bigl(\tfrac{1}{2}\mathbb{N}_0\bigr)^E.$$
Because $P_0 C_{\beta_1} P_0$ and $P_0 C_{\beta_2} P_0$ are simultaneously diagonal in the $\Pi_{\mathbf{j}}$ decomposition of $H_0$, this implies $P_0 C_{\beta_1} P_0 \ge \tilde{c}(\varepsilon) (P_0 C_{\beta_2} P_0)^{1+\varepsilon}$ on all of $H_0$, and hence $\mu_i(\beta_1) \ge \tilde{c}(\varepsilon) \mu_i(\beta_2)^{1+\varepsilon}$ for all $i \ge 0$. Taking $-\log$ and inserting (1.1) with $0 \le -\log\lambda_0(\beta) \le 9\beta|B|$ gives constants $C_1(\varepsilon), C_2$ (independent of $i$) such that
$$m_i(\beta_2) - C_2 \le m_i(\beta_1) \le (1 + \varepsilon) m_i(\beta_2) + C_1(\varepsilon) \qquad (\forall i \ge 1).$$
Dividing by $m_i(\beta_2) \to +\infty$, sending $i \to \infty$, and then sending $\varepsilon \downarrow 0$ proves (3). $\blacksquare$

### 1.3 Three Unconditional Corollaries (`PROVED` from Theorem 1)

- **Corollary 1A (Unconditional refutation of `(LEV-down)` of row 1610 §3.3).** On every finite spatial box $B = (\mathbb{Z}/n)^3$ ($n \ge 3$), for every $0 < \beta_1 < \beta_2$ and every $E > 1$, the hypothesis `(LEV-down)` ($m_i(\beta_1) \ge E m_i(\beta_2)$ for all $i \ge 1$) of Theorem TR-down (level form) is **FALSE**.
  *Proof.* Divide $m_i(\beta_1) \ge E m_i(\beta_2)$ by $m_i(\beta_2) > 0$ and let $i \to \infty$; Theorem 1(3) gives $1 \ge E$, contradiction. $\blacksquare$
  *(Note: Row 1610 L188 warned that `(LEV-down)` was heuristically too strong due to high-momentum states; Corollary 1A turns this into an unconditional refutation on every finite Wilson box via high-spin link representations, without any continuum or dispersion assumption.)*

- **Corollary 1B (Unconditional refutation of every all-state operator form bound on $H_0^\perp$).** On every finite box $B = (\mathbb{Z}/n)^3$ ($n \ge 3$), for every $\beta > 0$, every $\kappa > 0$, and every linear operator $A$ on $H_0$ whose domain contains an orthonormal eigenbasis $\{\psi_i\}_{i \ge 1}$ of $R_\beta|_{H_0^\perp}$ (in particular every bounded operator $A$, and every finite-rank skew-adjoint block generator $A_K$ of the Sussman–Alpoge GL12 class highlighted in check 1519 §(iv)), the descending form inequality
  $$\operatorname{Re}\langle \phi, (\widehat{R}_\beta' - [A, \widehat{R}_\beta]) \phi \rangle \ge \kappa \langle \phi, \Phi(\widehat{R}_\beta) \phi \rangle \qquad (\forall \phi \in H_0^\perp \cap \operatorname{Dom}(A))$$
  is **FALSE**.
  *Proof.* Take $\phi = \psi_i$ ($i \ge 1$). Because $\widehat{R}_\beta$ is self-adjoint with $\widehat{R}_\beta \psi_i = r_i \psi_i$, $\langle \psi_i, (A \widehat{R}_\beta - \widehat{R}_\beta A)\psi_i \rangle = r_i \langle \psi_i, A \psi_i \rangle - \langle \widehat{R}_\beta \psi_i, A \psi_i \rangle = 0$. Meanwhile $\langle \psi_i, \widehat{R}_\beta' \psi_i \rangle = r_i (D_i(\beta) - D_0(\beta))$ and $\langle \psi_i, \Phi(\widehat{R}_\beta) \psi_i \rangle = r_i m_i(\beta)$. Dividing by $r_i m_i(\beta) > 0$ gives $(D_i(\beta) - D_0(\beta))/m_i(\beta) \ge \kappa$ for all $i \ge 1$. Sending $i \to \infty$ contradicts Theorem 1(2). $\blacksquare$
  *(Structural asymmetry with ascending `(VIR_K)` of row 1517 Lemma CONJ: for ascending `(VIR_K)` the inequality points the other way ($\le K$), which is consistent with $\lim_{i \to \infty} (D_i - D_0)/m_i = 0 \le K$. Reversing the direction for `(VIR-down)` unconditionally eliminates every all-state operator conjugation method, including the adiabatic generator and GL12 block generators.)*

- **Corollary 1C (Small-time collapse).** For every finite box $B = (\mathbb{Z}/n)^3$ ($n \ge 3$) and every $\beta > 0$, the series $\sum_{i \ge 1} r_i(\beta)^t$ and $\sum_{i \ge 1} m_i(\beta) r_i(\beta)^t$ converge for every real $t > 0$. Defining the basis-independent spectral ratio $\mathcal{R}_{\mathrm{spec}}(t; \beta) := \bigl(\sum_{i \ge 1} (D_i(\beta) - D_0(\beta)) r_i(\beta)^t\bigr) / \bigl(\sum_{i \ge 1} m_i(\beta) r_i(\beta)^t\bigr)$ (which equals $\mathcal{R}(t; \beta) = \partial_\beta G / (-t \partial_t G)$ for all $t \ge 1$ by check 1613),
  $$\lim_{t \downarrow 0} \mathcal{R}_{\mathrm{spec}}(t; \beta) = 0.$$
  *Proof.* By (1.1), $\sum_{i \ge 0} \lambda_i(\beta)^t \le \sum_{i \ge 0} \mu_i(\beta)^t \le \bigl(\sum_{j \in \frac{1}{2}\mathbb{N}_0} (2j+1)^2 c_j(\beta)^t\bigr)^m < \infty$ for every $t > 0$ by Lemma 1(3) (super-exponential decay in $j$). Similarly $\sum_{i \ge 1} m_i r_i^t < \infty$ (since $x \log(1/x) \le C x^{1/2}$). Given $\varepsilon > 0$, Theorem 1(2) gives $I_\varepsilon$ such that $|D_i - D_0| \le \varepsilon m_i$ for all $i > I_\varepsilon$. Then
  $$|\mathcal{R}_{\mathrm{spec}}(t; \beta)| \le \frac{\sum_{i=1}^{I_\varepsilon} |D_i - D_0|}{\sum_{i \ge 1} m_i r_i^t} + \varepsilon.$$
  As $t \downarrow 0$, monotone convergence gives $\sum_{i \ge 1} m_i r_i^t \uparrow \sum_{i \ge 1} m_i = +\infty$. Thus $\limsup_{t \downarrow 0} |\mathcal{R}_{\mathrm{spec}}(t; \beta)| \le \varepsilon$ for every $\varepsilon > 0$. $\blacksquare$

---

## 2. Exact Cold-Torus `(VIR-down)` in 4D Compact Gaussian $U(1)$ with $P_0$: Under-Specification of Row 1610's Trigger

Row 1610 §4 proposed as a reopen trigger for `(T-down)`: *"a lower bound for $t a_0 - A_t$ against $\kappa t \bar{E}_t$ on cold neutral tori at late bare couplings, with a method that fails for the free photon."* Row 1610 L137 also argued (without proof) that in weak 4D compact $U(1)$ with the literal three $\mathbb{Z}_2$ half-turns $P_0$, the cold rate is zero to leading order. Check 1613 L110 noted that this photon-rate claim did not follow.

We now **disprove** Row 1610 L137's argued rate claim in the exact zero-monopole compact $U(1)$ model (4D compact Gaussian $U(1)$ with $P_0$) and **prove** that every cold neutral torus at $\beta \ge 4$ obeys `(VIR-down)` with $\kappa(\beta) = \frac{9}{10\beta} > 0$, even though `(T-down)` and `(PUR-io)` fail at every $\beta_1 \ge 1$.

### 2.1 Definition of the Model (`ON FILE` components from row 929 / check 1613)
Fix $n \ge 4$ and $\beta > 0$. On $(\mathbb{Z}/n)^3$, the zero-monopole sector of 4D Villain $U(1)$ projected by the literal three $\mathbb{Z}_2$ half-turns $P_0$ has the vacuum-normalized positive trace-class transfer operator
$$R_\beta^{\mathrm{cG}} := R_\beta^{\mathrm{flux}} \otimes R^{\mathrm{phot}},$$
where:
- $R_\beta^{\mathrm{flux}}$ acts diagonally on $\ell^2((2\mathbb{Z})^3)$ with eigenvalues $\exp\!\left(-\frac{\|Q\|_2^2}{2\beta n}\right)$ for $Q \in (2\mathbb{Z})^3$ (the three compact flat holonomy modes $\Phi_1, \Phi_2, \Phi_3 \in \mathbb{R}/2\pi\mathbb{Z}$ with inertia $\beta n$, restricted to even electric flux by $P_0$);
- $R^{\mathrm{phot}}$ is the tensor product over all nonzero spatial lattice momenta $k \in \Lambda_n^* := \bigl\{\frac{2\pi}{n} m : m \in \mathbb{Z}^3 \setminus \{0\},\ -\frac{n}{2} < m_j \le \frac{n}{2}\bigr\}$ of two transverse harmonic-oscillator transfer operators with vacuum-normalized eigenvalues $e^{-r \omega(k)}$ ($r \in \mathbb{N}_0$), where $\omega(k) := 2\operatorname{arsinh}\!\left(\sqrt{\sum_{j=1}^3 \sin^2(k_j/2)}\right)$ (the exact free lattice photon dispersion of row 929 and check 1613).

For every real $t > 0$ and $\beta > 0$, $R_\beta^{\mathrm{cG}}$ satisfies (S1) and (R) of row 1610, with
$$1 + G^{\mathrm{cG}}(t; \beta) = \bigl(1 + G_{\mathrm{flux}}(t; \beta)\bigr)\bigl(1 + G_{\mathrm{phot}}(t)\bigr),$$
$$1 + G_{\mathrm{flux}}(t; \beta) = \sum_{Q \in (2\mathbb{Z})^3} e^{-\frac{t \|Q\|_2^2}{2\beta n}}, \qquad \log\bigl(1 + G_{\mathrm{phot}}(t)\bigr) = -2 \sum_{k \in \Lambda_n^*} \log\bigl(1 - e^{-t \omega(k)}\bigr).$$

### 2.2 Theorem 2 (Cold-torus `(VIR-down)` holds in gapless 4D compact Gaussian $U(1)$ with $P_0$, while `(T-down)` fails). `PROVED`

For every integer $n \ge 4$:
1. **(Global sandwich)** For all $\beta > 0$ and all real $t > 0$,
   $$0 < \mathcal{R}^{\mathrm{cG}}(t; \beta) := \frac{\partial_\beta G^{\mathrm{cG}}(t; \beta)}{-t \partial_t G^{\mathrm{cG}}(t; \beta)} < \frac{1}{\beta}.$$
2. **(Cold-torus lower bound)** For every $\beta \ge 2$ and every real $t > 0$ satisfying the cold condition $G^{\mathrm{cG}}(t; \beta) \le 4/21$:
   $$t > 1.7\, \beta n \qquad \text{and} \qquad \mathcal{R}^{\mathrm{cG}}(t; \beta) \ge \frac{1}{\beta \bigl(1 + 280 \beta e^{-2.5\beta}\bigr)}.$$
   In particular, for every $\beta \ge 4$, every $n \ge 4$, and every cold neutral torus ($G^{\mathrm{cG}}(t; \beta) \le 4/21$),
   $$\partial_\beta G^{\mathrm{cG}}(t; \beta) > -\frac{9}{10\beta}\, t\, \partial_t G^{\mathrm{cG}}(t; \beta).$$
3. **(Failure of `(T-down)` and `(PUR-io)`)** For every $n \ge 4$ (with $u = n/512$), every $\beta_1 \ge 1$, every $\beta_h > \beta_1$, and every continuous $\kappa \ge 0$ on $[\beta_1, \beta_h]$:
   - $G^{\mathrm{cG}}(u; \beta_1) > 5 > 4/21$, so the thermal seed fails;
   - If `(VIR-down)` holds along $t(\beta) = u \exp(\int_{\beta_1}^\beta \kappa)$ throughout $[\beta_1, \beta_h]$, then $\kappa(\beta) < 1/\beta$ everywhere, $t_h < u \beta_h / \beta_1$, and $G^{\mathrm{cG}}(t_h; \beta_h) > 5 > 4/21$, so `(HOT)` fails.

**Proof.**
*(1)* Put $E_{\mathrm{flux}} := -t \partial_t \log(1 + G_{\mathrm{flux}}) > 0$ and $E_{\mathrm{phot}} := -t \partial_t \log(1 + G_{\mathrm{phot}}) > 0$. Since $G_{\mathrm{flux}}(t; \beta)$ depends on $(t, \beta)$ only through $t/\beta$, $\beta \partial_\beta \log(1 + G_{\mathrm{flux}}) = E_{\mathrm{flux}}$, while $\partial_\beta \log(1 + G_{\mathrm{phot}}) = 0$. Therefore
$$\mathcal{R}^{\mathrm{cG}}(t; \beta) = \frac{\partial_\beta \log(1 + G^{\mathrm{cG}})}{-t \partial_t \log(1 + G^{\mathrm{cG}})} = \frac{1}{\beta} \cdot \frac{E_{\mathrm{flux}}}{E_{\mathrm{flux}} + E_{\mathrm{phot}}} \in \left(0, \frac{1}{\beta}\right).$$

*(2)* Suppose $\beta \ge 2$ and $G^{\mathrm{cG}}(t; \beta) \le 4/21$. Then $G_{\mathrm{flux}}(t; \beta) \le G^{\mathrm{cG}}(t; \beta) \le 4/21$. Retaining only the six states $Q \in \{(\pm 2, 0, 0), (0, \pm 2, 0), (0, 0, \pm 2)\}$ (each having $\|Q\|_2^2 = 4$) gives $6 e^{-\frac{2t}{\beta n}} \le 4/21$, so $\frac{2t}{\beta n} \ge \log(63/2)$. Since $1.65^2 = 2.7225 > e$, $e^3 < 1.65^6 = (4.492125)^2 < 20.25$, and $e^{0.4} < 1 + 0.4 + 0.08 + \frac{0.064}{6}\cdot\frac{1}{1 - 0.1} < 1.5$, we have $e^{3.4} < 30.375 < 31.5 = 63/2$. Thus $\frac{2t}{\beta n} > 3.4$, i.e. $t > 1.7 \beta n$.

Keeping the same six terms in $E_{\mathrm{flux}}$ gives
$$E_{\mathrm{flux}} = \frac{\sum_{Q \in (2\mathbb{Z})^3 \setminus \{0\}} \frac{t \|Q\|_2^2}{2\beta n} e^{-\frac{t \|Q\|_2^2}{2\beta n}}}{1 + G_{\mathrm{flux}}} \ge \frac{6}{1 + 4/21} \cdot \frac{2t}{\beta n} e^{-\frac{2t}{\beta n}} = \frac{126}{25} \cdot \frac{2t}{\beta n} e^{-\frac{2t}{\beta n}} > 5 \cdot \frac{2t}{\beta n} e^{-\frac{2t}{\beta n}}.$$
For $E_{\mathrm{phot}} = \sum_{k \in \Lambda_n^*} \frac{2 t \omega(k)}{e^{t \omega(k)} - 1}$, write $k = \frac{2\pi}{n} m$ ($m \in \mathbb{Z}^3 \setminus \{0\}$, $|m_j| \le n/2$) and $s(k) := \sqrt{\sum_{j=1}^3 \sin^2(\pi m_j / n)}$. By $\frac{2}{\pi} x \le \sin x \le x$ on $[0, \pi/2]$, we have $\frac{2\|m\|_2}{n} \le s(k) \le \frac{\pi \|m\|_2}{n}$ and $s(k) \le \sqrt{3}$. By concavity of $\operatorname{arsinh}$ on $[0, \infty)$, $\frac{\operatorname{arsinh}(\sqrt{3})}{\sqrt{3}} s \le \operatorname{arsinh}(s) \le s$ on $[0, \sqrt{3}]$. Since $e < 2.72 \implies e^{1.1} = e \cdot e^{0.1} < 2.72 \cdot 1.11 < 3.02$ and $e^{-1.1} > 1/3.02 > 0.33$, we have $\sinh(1.1) < (3.02 - 0.33)/2 = 1.345 < 1.73 < \sqrt{3}$, so $\operatorname{arsinh}(\sqrt{3}) > 1.1$ and $\frac{4\operatorname{arsinh}(\sqrt{3})}{\sqrt{3}} > \frac{4.4}{1.74} > 2.5$. Hence
$$\frac{2.5 \|m\|_2}{n} \le \omega(k) \le \frac{2\pi \|m\|_2}{n} \qquad (\forall k \in \Lambda_n^*).$$
For $\beta \ge 2$ and $\|m\|_2 \ge 1$, this implies $2.5 \|m\|_2 - \frac{2}{\beta} \ge 2.5 \|m\|_2 - 1 \ge 1.5 \|m\|_2$, so
$$t \omega(k) \ge \frac{2t}{\beta n} + \frac{1.5 t}{n} \|m\|_2.$$
Moreover $t \omega(k) \ge 2.5 \cdot 1.7 \cdot 2 = 8.5 > \log 2$, so $e^{t \omega(k)} - 1 \ge \frac{1}{2} e^{t \omega(k)}$. Setting $\alpha := \frac{1.5 t}{n} > 1.5 \cdot 1.7 \beta = 2.55\beta > 2.5\beta \ge 5$,
$$E_{\mathrm{phot}} \le 4 \sum_{k \in \Lambda_n^*} t \omega(k) e^{-t \omega(k)} \le \left(\frac{2t}{\beta n} e^{-\frac{2t}{\beta n}}\right) \cdot 4\pi \beta \sum_{m \in \mathbb{Z}^3 \setminus \{0\}} \|m\|_2 \, e^{-\alpha \|m\|_2}.$$
Grouping by $r = \|m\|_\infty \ge 1$, there are $(2r+1)^3 - (2r-1)^3 = 24 r^2 + 2 \le 26 r^2$ vectors with $\|m\|_\infty = r$, each satisfying $r \le \|m\|_2 \le \sqrt{3} r < 2r$. For all integers $r \ge 1$, $r^3 \le e^{3(r-1)}$ (checked for $r = 1$: $1 = 1$; $r = 2$: $8 < 20 < e^3$; and for $r \ge 2$, $(1+1/r)^3 \le 27/8 < e^3$). Since $\alpha \ge 5$,
$$\sum_{m \in \mathbb{Z}^3 \setminus \{0\}} \|m\|_2 e^{-\alpha \|m\|_2} \le 52 e^{-\alpha} \sum_{r=1}^\infty r^3 e^{-\alpha(r-1)} \le 52 e^{-\alpha} \sum_{r=1}^\infty e^{-2(r-1)} = \frac{52 e^{-\alpha}}{1 - e^{-2}} < 52 \cdot \frac{7}{6} e^{-\alpha} < 104 e^{-2.5\beta}.$$
With $4\pi \cdot 104 < 4 \cdot 3.15 \cdot 104 = 1310.4 < 1400$, we obtain $E_{\mathrm{phot}} / E_{\mathrm{flux}} \le (1400/5) \beta e^{-2.5\beta} = 280 \beta e^{-2.5\beta}$. On $\beta \ge 4$, $280 \beta e^{-2.5\beta}$ is strictly decreasing and at $\beta = 4$ is $1120 e^{-10} < 1120 / 21800 < 1/10$ (using $e > 2.718 \implies e^2 > 7.38 \implies e^4 > 54.4 \implies e^8 > 2959 \implies e^{10} > 21800$). Hence $\mathcal{R}^{\mathrm{cG}} = \frac{1}{\beta(1 + E_{\mathrm{phot}}/E_{\mathrm{flux}})} > \frac{10}{11\beta} > \frac{9}{10\beta}$.

*(3)* By (1), if `(VIR-down)` holds everywhere on $[\beta_1, \beta_h]$, then $\kappa(\beta) \le \mathcal{R}^{\mathrm{cG}}(t(\beta); \beta) < 1/\beta$, so $t_h = u \exp(\int_{\beta_1}^{\beta_h} \kappa) < u \beta_h / \beta_1$. Hence at both $(\beta_1, u)$ and $(\beta_h, t_h)$,
$$G^{\mathrm{cG}}(t_h; \beta_h) \ge G_{\mathrm{flux}}(t_h; \beta_h) \ge 6 e^{-\frac{2 t_h}{\beta_h n}} > 6 e^{-\frac{2 u}{\beta_1 n}} = 6 e^{-\frac{1}{256 \beta_1}} \ge 6 e^{-1/256} > 5 > \frac{4}{21}. \quad \blacksquare$$

**Consequence for Row 1610's Trigger (`PROVED` from Theorem 2).** A cold-torus inequality $t a_0 - A_t \ge \kappa(\beta) t \bar{E}_t$ at late bare couplings with $\kappa(\beta) \le \frac{9}{10\beta}$ fails for the non-compact free photon ($\mathcal{R} \equiv 0$) yet **holds** on every cold neutral torus of the gapless 4D compact Gaussian $U(1)$ model with $P_0$. Thus Row 1610 §4's trigger is **under-specified**: distinguishing `(VIR-down)` from gapless compact $U(1)$ requires not merely a positive rate that fails for the free photon, but a rate exceeding the $O(1/\beta)$ ceiling and meeting the consumer's integrated budget — which Section 3 makes exact on the calibrated trajectory.

---

## 3. Calibrated-Trajectory Necessary Budget and Obstructions to $o(1)$, $O(1/\beta)$, and $L^1$ Rates

Check 1613 (L88–99) showed that for the **literal existential** $\beta_h > \beta_K$ of row 1610, `(T-down)` at cutoff $K$ can be witnessed on an arbitrarily short interval $[\beta_K, \beta_K + \varepsilon]$ with $\kappa \equiv 0$ whenever $G(u; \beta_K) < 4/21$ and $\partial_\beta G(u; \beta_K) > 0$, without ever reaching a weak small box. To actually use `(T-down)` as a downward transport from a genuinely hot (weak-coupling) small box, $\beta_h$ must reach a regime where the spatial box is hot at time $u$. The next theorem quantifies the exact necessary rate budget on the calibrated trajectory and rules out all $o(1)$ and $O(1/\beta)$ rates on fixed-physical-ratio windows, as well as all $L^1[\beta_K, \infty)$ rates for arbitrarily large $\beta_h$.

### 3.1 Theorem 3 (Necessary budget and calibrated-trajectory rate obstructions). `PROVED` (given check 1453 `BND-1`, row 1461 (1)–(2) checked by 1465, and row 1215 (5) checked by 1221)

Fix the release witnesses $(b, g_0)$, $\ell \in 1024\mathbb{N}_{>0}$, $n_K = \ell b^K$, $u_K = n_K / 512$, and the calibrated roots $\beta_K = \beta_K(r(g_0))$. Let $s := \frac{11 \log b}{3\pi^2} > 0$, and let $(H, \lambda, c_r, C_I, K_I, c, Q)$ be the constants of check 1453 (`BND-1`) and row 1461 (displays (1)–(2)) for a closed interval $I \subset (0, r(\delta))$ containing $r(g_0)$.

1. **(Exact necessary budget)** If `(T-down)` holds at cutoff $K$ on $[\beta_K, \beta_h]$ with continuous $\kappa \ge 0$ and `(HOT)`: $G(t_h; \beta_h) \le 4/21$, where $t_h = u_K \exp\!\left(\int_{\beta_K}^{\beta_h} \kappa(\beta)\,d\beta\right)$, then
   $$\int_{\beta_K}^{\beta_h} \kappa(\beta)\,d\beta \ge \log\!\frac{512 \log(21/4)}{n_K m_1(\beta_h)} > \log\!\frac{844}{n_K m_1(\beta_h)}. \tag{3.1}$$
2. **(Bounded bare width of fixed-physical-ratio windows)** For every fixed integer $r \ge 1$ (shifting the physical box side from $\ell$ to the UV side $L_{\mathrm{uv}} = \ell b^{-r}$, since $n_K = \ell b^K = (\ell b^{-r}) b^{K+r}$), all $K \ge K_I$ satisfy
   $$\bigl|(\beta_{K+r} - \beta_K) - s r\bigr| \le W(r) := 2 C_I + 2 c + \frac{2 Q}{s}\bigl(1 + \log r\bigr). \tag{3.2}$$
   Consequently, on any sequence of windows $[\beta_K, \beta_h(K)]$ of bounded bare width $0 < \beta_h(K) - \beta_K \le \Delta$ (in particular $\beta_h(K) = \beta_{K+r}$ with $s r > W(r)$ and $\Delta = s r + W(r)$):
   - Every sequence of schedules with $\sup_{\beta \in [\beta_K, \beta_h(K)]} \kappa_K(\beta) \to 0$ as $K \to \infty$ — and in particular every $O(1/\beta)$ rate $\kappa_K(\beta) \le C/\beta$ — obeys $\int_{\beta_K}^{\beta_h(K)} \kappa_K \to 0$ and $t_h(K) / u_K \to 1$. Hence `(T-down)` **FAILS** at all sufficiently large $K$ whenever either $\limsup_{K \to \infty} n_K m_1(\beta_h(K)) < 512 \log(21/4)$ (for instance, $< 844$) or $\liminf_{K \to \infty} G(u_K(1 + \delta); \beta_h(K)) > 4/21$ for some $\delta > 0$.
   - Conversely, if $n_K m_1(\beta_h(K)) \le \Gamma_h < 512 \log(21/4)$ on an infinite set of $K$, then every `(T-down)` witness on $[\beta_K, \beta_h(K)]$ must satisfy
     $$\sup_{\beta \in [\beta_K, \beta_h(K)]} \kappa_K(\beta) \ge \frac{1}{\Delta} \log\!\frac{512 \log(21/4)}{\Gamma_h} = \Omega(1) \qquad (\text{uniformly in } K).$$
3. **(Arbitrarily large $\beta_h$: $L^1$ and $c/\beta$ obstructions)**
   - For every fixed cutoff $K$ and every finite budget $M > 0$, there exists $\beta_*(K, M) > \beta_K$ such that no schedule with $\int_{\beta_K}^{\beta_h} \kappa \le M$ can witness `(T-down)` for any $\beta_h \ge \beta_*(K, M)$. In particular, no $\kappa \in L^1[\beta_K, \infty)$ can witness `(T-down)` for arbitrarily large $\beta_h$ at fixed $K$.
   - For any sequence $\beta_h(K) > \beta_K$ (growing arbitrarily fast with $K$) and any schedule $\kappa_K(\beta) \le c/\beta$ on $[\beta_K, \beta_h(K)]$ ($c > 0$), `(T-down)` **FAILS** at cutoff $K$ whenever $n_K m_1(\beta_h(K)) < 512 \log(21/4)\, (\beta_K/\beta_h(K))^c$. In particular, for the toron rate $c = 1/3$, if $n_K m_1(\beta_h(K)) \le C_0 \beta_h(K)^{-1/3}$ along an infinite set of $K$, then $t_h(K) m_1(\beta_h(K)) \le \frac{C_0}{512} \beta_K^{-1/3} \to 0$, contradicting `(HOT)` at all sufficiently large $K$ in that set.

**Proof.**
*(1)* Retaining only the first excited neutral level in `(HOT)` gives $e^{-t_h m_1(\beta_h)} \le G(t_h; \beta_h) \le 4/21$, hence $t_h m_1(\beta_h) \ge \log(21/4)$. Substituting $t_h = (n_K/512)\exp(\int_{\beta_K}^{\beta_h} \kappa)$ yields the first inequality of (3.1). For the numerical bound: $e < 2.7183$ and $e^{0.65} < 1 + 0.65 + 0.21125 + 0.04578 + 0.00744 + 0.00097 + 0.00011 = 1.91555$, so $e^{1.65} < 2.7183 \cdot 1.91555 < 5.21 < 5.25 = 21/4$. Thus $\log(21/4) > 1.65$ and $512 \log(21/4) > 844.8 > 844$.

*(2)* By row 1461 displays (1)–(2) (`gap-crux-direction-astra62.md` L56–89, checked in 1462 and 1465; `ON FILE`), for all $K \ge K_I$:
$$B_K = \sum_{i=0}^{K-1} a_i + \frac{1}{s} \sum_{i=0}^{K-1} \frac{q_i}{K - i}, \qquad |\beta_K - B_K| \le C_I, \qquad \left|\sum_{i=K}^{K+r-1} a_i - s r\right| \le 2c, \qquad |q_i| \le Q.$$
Taking the difference $B_{K+r} - B_K$:
$$B_{K+r} - B_K = \sum_{i=K}^{K+r-1} a_i + \frac{1}{s} \sum_{i=K}^{K+r-1} \frac{q_i}{K + r - i} + \frac{1}{s} \sum_{i=0}^{K-1} q_i \left(\frac{1}{K + r - i} - \frac{1}{K - i}\right).$$
The second sum has magnitude at most $\frac{Q}{s} \sum_{m=1}^r \frac{1}{m}$. In the third sum, substituting $m = K - i$ gives
$$\sum_{m=1}^{K} \left(\frac{1}{m} - \frac{1}{m + r}\right) = \sum_{m=1}^r \frac{1}{m} - \sum_{m=K+1}^{K+r} \frac{1}{m} \le \sum_{m=1}^r \frac{1}{m} \le 1 + \int_1^r \frac{dx}{x} = 1 + \log r.$$
By the triangle inequality and $|\beta_K - B_K|, |\beta_{K+r} - B_{K+r}| \le C_I$, we obtain (3.2).

Now let $0 < \beta_h(K) - \beta_K \le \Delta$. If $\kappa_K(\beta) \le C/\beta$, then by check 1453 (`BND-1`: $\beta_K \ge H + \lambda K - c_r \to \infty$ with $\lambda > 0$), $\sup_{[\beta_K, \beta_h(K)]} \kappa_K \le C/\beta_K \to 0$. Whenever $\sup_{[\beta_K, \beta_h(K)]} \kappa_K \to 0$, we have $\int_{\beta_K}^{\beta_h(K)} \kappa_K \le \Delta \sup \kappa_K \to 0$, so $t_h(K)/u_K \to 1$. Under $\limsup n_K m_1(\beta_h(K)) < 512\log(21/4)$, the right side of (3.1) has a strictly positive $\liminf$, contradicting $\int \kappa_K \to 0$. Under $\liminf G(u_K(1 + \delta); \beta_h(K)) > 4/21$, eventually $t_h(K) \le u_K(1 + \delta)$, and decrease of $G$ in time gives $G(t_h(K); \beta_h(K)) \ge G(u_K(1+\delta); \beta_h(K)) > 4/21$, contradicting `(HOT)`. The $\Omega(1)$ supremum bound is immediate from $\Delta \sup \kappa_K \ge \int_{\beta_K}^{\beta_h(K)} \kappa_K$ and (3.1).

*(3)* At fixed $K$, row 1215 equation (5) (`gap-solve23-astra62.md` L90–96, checked by row 1221; `ON FILE`) proves $\lim_{\beta \to \infty} m_1(\beta; n_K) = 0$. Hence the right side of (3.1) tends to $+\infty$ as $\beta_h \to \infty$, yielding the first claim. For $\kappa_K(\beta) \le c/\beta$, integration gives $\int_{\beta_K}^{\beta_h(K)} \kappa_K \le c \log(\beta_h(K)/\beta_K)$, so $t_h(K) \le u_K (\beta_h(K)/\beta_K)^c$; comparing with (3.1) gives the second claim and the $c = 1/3$ cancellation $t_h(K) m_1(\beta_h(K)) \le \frac{C_0}{512}\beta_K^{-1/3} \to 0$. $\blacksquare$

---

## 4. Exact Anisotropic Spatial-Action Split and the Magnetic-Suppression Dichotomy

Theorem 3 shows that carrying `(T-down)` across any fixed-physical-ratio window $[\beta_K, \beta_{K+r}]$ from a hot UV box requires an $\Omega(1)$ rate $\kappa(\beta)$ at late bare couplings $\beta_K \sim s K \to \infty$. We now prove an exact finite-lattice identity explaining **where** an $\Omega(1)$ rate must live inside the Wilson action, and why it is sharply separated from both the free lattice photon and compact Gaussian $U(1)$.

### 4.1 Theorem 4 (Exact anisotropic spatial-action split and dichotomy). `PROVED`

Fix $B = (\mathbb{Z}/n)^3$ ($n \ge 3$), $\beta > 0$, and an integer $t \ge 1$. For $(\beta_\tau, \beta_\sigma) \in (0, \infty)^2$, define the anisotropic neutral Wilson transfer operator
$$R(\beta_\tau, \beta_\sigma) := P_0 M_{\beta_\sigma} C_{\beta_\tau} M_{\beta_\sigma} P_0$$
on $H_0$, with simple top eigenvalue $\lambda_0(\beta_\tau, \beta_\sigma) > 0$, neutral trace $Z_+(t; \beta_\tau, \beta_\sigma) = \operatorname{Tr}_{H_0}(R(\beta_\tau, \beta_\sigma)^t)$, and thermal sum $1 + G(t; \beta_\tau, \beta_\sigma) = Z_+(t; \beta_\tau, \beta_\sigma)/\lambda_0(\beta_\tau, \beta_\sigma)^t$. Let $A_t^\sigma(\beta) := \mathbb{E}_{+,\beta,t}[S_\sigma]$ be the neutral thermal mean of the purely spatial shifted Wilson action $S_\sigma = \sum_{p \text{ spatial}} (1 - \frac{1}{2}\operatorname{tr} U_p)$ on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/t)$ (note the temporal twists $z \in \mathbb{Z}_2^3$ act only on temporal plaquettes, so $S_\sigma$ is independent of $z$), and put $a_0^\sigma(\beta) := -\left.\partial_{\beta_\sigma} \log \lambda_0(\beta_\tau, \beta_\sigma)\right|_{(\beta,\beta)} = \lim_{v \to \infty} A_v^\sigma(\beta)/v$.

1. **(Exact split)** Along the anisotropy curve $(\beta_\tau(\xi), \beta_\sigma(\xi)) = (\xi \beta, \xi^{-1} \beta)$ through $\xi = 1$:
   $$t a_0(\beta) - A_t(\beta) = \frac{1}{\beta} \left.\frac{\partial}{\partial \xi} \log\bigl(1 + G(t; \xi\beta, \xi^{-1}\beta)\bigr)\right|_{\xi=1} + 2\bigl(t a_0^\sigma(\beta) - A_t^\sigma(\beta)\bigr), \tag{4.1}$$
   where the purely spatial action deficit has the spectral representation
   $$t a_0^\sigma(\beta) - A_t^\sigma(\beta) = \frac{t}{1 + G(t; \beta)} \sum_{i \ge 1} \bigl(\langle \psi_0, V_1 \psi_0 \rangle - \langle \psi_i, V_1 \psi_i \rangle\bigr) e^{-t m_i(\beta)}. \tag{4.2}$$
2. **(Dichotomy for `(VIR-down)`)** Suppose `(VIR-down)` holds at $(t, \beta)$ with rate $\kappa > 0$. Then for every $C > 0$, at least one of the following holds:
   - **(i) Spatial (magnetic) action suppression:**
     $$t a_0^\sigma(\beta) - A_t^\sigma(\beta) \ge \frac{1}{2}\left(\kappa - \frac{C}{\beta}\right) t \bar{E}_t(\beta)$$
     (strictly positive whenever $\kappa > C/\beta$, meaning the thermal neutral torus holds strictly **less** spatial plaquette action than $t$ vacuum slabs); or
   - **(ii) Super-classical anisotropy response:**
     $$\left.\frac{\partial}{\partial \xi} \log\bigl(1 + G(t; \xi\beta, \xi^{-1}\beta)\bigr)\right|_{\xi=1} > C\, t \bar{E}_t(\beta).$$
3. **(Exact sign reversal in the free lattice photon and compact Gaussian $U(1)$ with $P_0$)** In both the anisotropic free lattice photon ($\beta_\tau = \xi\beta, \beta_\sigma = \xi^{-1}\beta$, with dispersion $\omega(k; \xi) = 2\operatorname{arsinh}(\frac{\sqrt{\ell(k)}}{2\xi})$, $\ell(k) = 4\sum_{j=1}^3 \sin^2(k_j/2)$) and the anisotropic 4D compact Gaussian $U(1)$ model with $P_0$ ($m_Q(\beta_\tau, \beta_\sigma) = \frac{\|Q\|_2^2}{2\beta_\tau n}$), for every $n \ge 4$, every $\beta > 0$, and every real $t > 0$:
   $$0 < \left.\frac{\partial}{\partial \xi} \log\bigl(1 + G(t; \xi\beta, \xi^{-1}\beta)\bigr)\right|_{\xi=1} < t \bar{E}_t(\beta), \qquad t a_0^\sigma(\beta) - A_t^\sigma(\beta) < 0. \tag{4.3}$$
   In particular, for every $\kappa > 1/\beta$ and $C = 1$, **both** alternatives (i) and (ii) of part (2) fail identically on every finite lattice in both models.

**Proof.**
*(1)* By the same analyticity argument as Lemma D1 (check 1613 L49, L68–72), $(\beta_\tau, \beta_\sigma) \mapsto R(\beta_\tau, \beta_\sigma)$ is jointly real-analytic in trace norm on $(0, \infty)^2$ with simple isolated top eigenvalue $\lambda_0(\beta_\tau, \beta_\sigma) > 0$. Differentiating the finite compact-group integrals $Z^z(t; \beta_\tau, \beta_\sigma) = \int \exp(-\beta_\tau S_\tau^z - \beta_\sigma S_\sigma)\,dU$ gives $\partial_{\beta_\tau}\log Z_+ = -A_t^\tau$ and $\partial_{\beta_\sigma}\log Z_+ = -A_t^\sigma$, while $-\partial_{\beta_\tau}\log\lambda_0 = a_0^\tau$ and $-\partial_{\beta_\sigma}\log\lambda_0 = a_0^\sigma$, with $A_t = A_t^\tau + A_t^\sigma$ and $a_0 = a_0^\tau + a_0^\sigma$. By the chain rule at $\xi = 1$:
$$\left.\partial_\xi \log(1 + G(t; \xi\beta, \xi^{-1}\beta))\right|_{\xi=1} = \beta(t a_0^\tau - A_t^\tau) - \beta(t a_0^\sigma - A_t^\sigma).$$
Subtracting this from $\beta(t a_0 - A_t) = \beta(t a_0^\tau - A_t^\tau) + \beta(t a_0^\sigma - A_t^\sigma)$ yields $2\beta(t a_0^\sigma - A_t^\sigma)$; dividing by $\beta$ gives (4.1). For (4.2), differentiating $R(\beta, \beta_\sigma) = P_0 M_{\beta_\sigma} C_\beta M_{\beta_\sigma} P_0$ in $\beta_\sigma$ gives $\partial_{\beta_\sigma} R = -\frac{1}{2} P_0 (V_1 R + R V_1) P_0$ (since $V_1$ commutes with $P_0$), so in any orthonormal eigenbasis $\{\psi_i\}$ of $R_\beta$ on $H_0$, $\langle \psi_i, (\partial_{\beta_\sigma} R)\psi_i \rangle = -\lambda_i \langle \psi_i, V_1 \psi_i \rangle$. Applying $\partial_{\beta_\sigma} \operatorname{Tr}(R^t) = t \operatorname{Tr}(R^{t-1} \partial_{\beta_\sigma} R)$ and subtracting $t \partial_{\beta_\sigma}\log\lambda_0 = -t\langle \psi_0, V_1 \psi_0 \rangle$ gives (4.2).

*(2)* Direct algebra from (4.1): if (ii) fails, then $2(t a_0^\sigma - A_t^\sigma) = (t a_0 - A_t) - \frac{1}{\beta}\partial_\xi \log(1+G)|_{\xi=1} \ge (\kappa - C/\beta) t \bar{E}_t$.

*(3)* For each nonzero photon mode $k \in \Lambda_n^*$, write $x = \omega(k)/2 > 0$, so $\sinh x = \sqrt{\ell(k)}/2$ and $\cosh x = \sqrt{1 + \ell(k)/4}$. Differentiating $\omega(k; \xi) = 2\operatorname{arsinh}(\sqrt{\ell(k)}/(2\xi))$ at $\xi = 1$ gives
$$-\left.\partial_\xi \omega(k; \xi)\right|_{\xi=1} = \frac{\sqrt{\ell(k)}}{\sqrt{1 + \ell(k)/4}} = 2 \tanh\!\left(\frac{\omega(k)}{2}\right).$$
Since $\tanh x < x$ for all $x > 0$ (as $(\tanh x)' = \operatorname{sech}^2 x < 1$ on $(0, \infty)$ and $\tanh 0 = 0$), we have $0 < 2\tanh(\omega(k)/2) < \omega(k)$ for every $k \in \Lambda_n^*$. Summing over the positively weighted photon modes gives $0 < \partial_\xi \log(1 + G_{\mathrm{phot}})|_{\xi=1} < E_{\mathrm{phot}}$. Since $t a_0^{\mathrm{phot}} - A_t^{\mathrm{phot}} \equiv 0$, (4.1) gives $t a_0^{\sigma, \mathrm{phot}} - A_t^{\sigma, \mathrm{phot}} = -\frac{1}{2\beta} \partial_\xi \log(1 + G_{\mathrm{phot}})|_{\xi=1} < 0$. In the compact Gaussian $U(1)$ model, $G_{\mathrm{flux}}(t; \beta_\tau)$ is independent of $\beta_\sigma$ and has $\partial_\xi \log(1 + G_{\mathrm{flux}})|_{\xi=1} = E_{\mathrm{flux}}$ (exact equality), while $t a_0^{\sigma, \mathrm{flux}} - A_t^{\sigma, \mathrm{flux}} = 0$. Adding the photon and flux pieces gives $0 < \partial_\xi \log(1 + G^{\mathrm{cG}})|_{\xi=1} = E_{\mathrm{flux}} + \partial_\xi \log(1 + G_{\mathrm{phot}})|_{\xi=1} < E_{\mathrm{flux}} + E_{\mathrm{phot}} = t \bar{E}_t^{\mathrm{cG}}$ and $t a_0^{\sigma, \mathrm{cG}} - A_t^{\sigma, \mathrm{cG}} = t a_0^{\sigma, \mathrm{phot}} - A_t^{\sigma, \mathrm{phot}} < 0$. $\blacksquare$

**Remark 4.1 (Comparison with the Schwinger–Dyson force identity and weak-coupling SU(2) torons).**
- *Schwinger–Dyson (`ON FILE` in substance, row 913 Lemma F / row 934 L117):* Integrating $\Delta_\ell S - \beta |\nabla_\ell S|^2$ over Haar measure gives $t a_0(\beta) - A_t(\beta) = \frac{\beta}{3}(Q_t - t q_\infty)$ for $\mathrm{SU}(2)$ (and $\frac{\beta}{4}(Q_t - t q_\infty)$ for compact Wilson $U(1)$, versus $0$ for the non-compact free photon). This identity reflects only compactness of the link group (shared by compact $U(1)$ and 5D $\mathrm{SU}(2)$) and leaves the same extensive-subtraction problem $Q_t - t q_\infty$.
- *Weak-coupling $\mathrm{SU}(2)$ torons (`ARGUED`):* In the anisotropic small-box toron Hamiltonian $H_{\mathrm{eff}} \sim \frac{1}{2\beta_\tau n}(-\nabla_\Phi^2) + \frac{2\beta_\sigma}{n}\sum_{i<j}|\Phi_i \times \Phi_j|^2$, rescaling $\Phi = (\beta_\tau \beta_\sigma)^{-1/6} Y$ gives $m_{\mathrm{toron}}(\beta_\tau, \beta_\sigma) \propto n^{-1} \beta_\tau^{-2/3} \beta_\sigma^{1/3} = \xi^{-1} n^{-1} \beta^{-1/3}$, so $\partial_\xi \log(1+G)|_{\xi=1} = t \bar{E}_t$ and $t a_0^\sigma - A_t^\sigma = -\frac{1}{3\beta} t \bar{E}_t < 0$ — again **strictly negative**! By contrast, in the 4D $\mathrm{SU}(2)$ scaling/confining regime (`GUIDE`, Michael–Rothe sum rules, row 710 §8), $\partial_\xi \log(1+G)|_{\xi=1} \approx t \bar{E}_t$ while $t a_0 - A_t \approx \frac{3\pi^2}{11} t \bar{E}_t$, forcing $t a_0^\sigma - A_t^\sigma \approx +\frac{1}{2}(\frac{3\pi^2}{11} - \frac{1}{\beta}) t \bar{E}_t > 0$: thermal neutral excitations must suppress spatial magnetic fluctuations relative to the vacuum (the lattice trace anomaly).

**Remark 4.2 (Product with a neutral massless scalar — test `(g4)` of row 1553; `PROVED` given row 1573).**
Tensor $R_\beta$ with an independent $\beta$-independent neutral lattice scalar $R^{\mathrm{scal}}$ on $(\mathbb{Z}/n)^3$ with lattice mass $m_K = b^{-2K}$ (as in row 1573, checked by check 1579 item 8; `ON FILE`). Then $1 + G^{\mathrm{prod}}(t; \beta) = (1 + G^{\mathrm{SU(2)}}(t; \beta))(1 + G^{\mathrm{scal}}(t))$. At $t = u_K = n_K/512$, the lowest nonzero scalar mode has $\omega_1^{\mathrm{scal}} = 2\operatorname{arsinh}(\frac{1}{2}\sqrt{m_K^2 + 4\sin^2(\pi/n_K)})$, so $u_K \omega_1^{\mathrm{scal}} \to 2\pi/512$ and $G^{\mathrm{prod}}(u_K; \beta_K) \ge G^{\mathrm{scal}}(u_K) \ge e^{-u_K \omega_1^{\mathrm{scal}}} \to e^{-2\pi/512} > 4/21$. By check 1613's mean-value-theorem obstruction, `(T-down)` fails at all sufficiently large $K$, despite the intact 4D $\mathrm{SU}(2)$ factor.

---

## 5. Fixed-Box Weak-Coupling Limit and All-$\beta$ Low-Energy Window Localization

We record two exact complementary results: Proposition 5 determines the exact fixed-box $\beta \to \infty$ limit of $\beta(t a_0 - A_t)$ (establishing why fixed-lattice weak-coupling positivity is hot and non-selective), and Proposition 6 builds the first structural component of C4 — an all-$\beta$ low-energy window localization for `(VIR-down)` that removes the high-spin tail identified in Theorem 1.

### 5.1 Proposition 5 (Exact fixed-box weak-coupling limit of $\beta(t a_0 - A_t)$). `PROVED` (given row 1143 (1)–(3), (11) checked by 1144, and row 1215 (4) checked by 1221)

For every fixed spatial side $n \ge 3$ and every fixed integer period $t \ge 3$, 4D Wilson $\mathrm{SU}(2)$ satisfies
$$\lim_{\beta \to \infty} \beta \bigl(t a_0(\beta) - A_t(\beta)\bigr) = \frac{3}{2}. \tag{5.1}$$

**Proof.**
*Step 1 (Uniform $O(s^{-9/2})$ bound for all seven nonzero temporal twists $z \in \mathbb{Z}_2^3 \setminus \{0\}$).* Let $V = t n^3$, $M = 3V - 3$, $Q = \max(t n, n^2)$. By row 1143 equation (1) (`ON FILE`), for every temporal twist $z \in \mathbb{Z}_2^3 \setminus \{0\}$ (which sets $\epsilon_{0i} = (-1)^{z_i}$ and $\epsilon_{ij} = +1$ for $1 \le i < j \le 3$),
$$Z^z(t; \beta) \le I(\beta/2)^M J_z(\beta/(2Q)), \qquad J_z(s) = \int_{\mathrm{SU}(2)^4} e^{-s A_z(h)}\,dh,$$
where $A_z(h) = \sum_{0 \le \mu < \nu \le 3} a(\epsilon_{\mu\nu}[h_\mu, h_\nu])$. Write $h_\mu = (x_\mu, u_\mu) \in S^3 \subset \mathbb{R} \times \mathbb{R}^3$ ($x_\mu^2 + |u_\mu|^2 = 1$). By row 1143 §2 (`ON FILE`), $a([h, k]) = 2|u \times v|^2$ and $a(-[h, k]) = 2(1 - |u \times v|^2)$. Permuting spatial axes, assume $z_1 = 1$, so $\epsilon_{01} = -1$. The zero locus $\{A_z = 0\}$ is characterized by $x_0 = x_1 = 0$, $u_0 \perp u_1$ (unit vectors), and for each $j \in \{2, 3\}$: $u_j = 0$ if $z_j = 0$, whereas $x_j = 0$ and $u_j = \pm u_1$ if $z_j = 1$ (which automatically makes $u_2 \times u_3 = 0$).

Define the open neighborhood $U_z$ of $\{A_z = 0\}$ by $|x_0|, |x_1| < 1/4$, $|y| < 1/2$ (with $y := \frac{u_0 \cdot u_1}{|u_0||u_1|}$), and for each $j \in \{2, 3\}$: $|u_j| < 1/4$ if $z_j = 0$, or $|x_j| < 1/4$ and $|u_1 \times u_j| < 1/4$ if $z_j = 1$. On the compact complement $\mathrm{SU}(2)^4 \setminus U_z$, $A_z \ge c_0 > 0$, contributing at most $e^{-c_0 s}$ to $J_z(s)$. On $U_z$:
- By row 1143 L77–78 (`ON FILE`), $\frac{1}{2} a(-[h_0, h_1]) = x_0^2 + x_1^2 - x_0^2 x_1^2 + (1 - x_0^2)(1 - x_1^2) y^2 \ge \frac{1}{2}(x_0^2 + x_1^2 + y^2)$, and $|u_0|^2, |u_1|^2 \ge 15/16$.
- For $j \in \{2, 3\}$ with $z_j = 0$: $(\hat{u}_0 \cdot u_j)^2 + (\hat{u}_1 \cdot u_j)^2 \le (1 + |y|)|u_j|^2 \le \frac{3}{2}|u_j|^2$, so $a([h_0, h_j]) + a([h_1, h_j]) = 2|u_0 \times u_j|^2 + 2|u_1 \times u_j|^2 \ge \frac{15}{8}(2 - \frac{3}{2})|u_j|^2 = \frac{15}{16}|u_j|^2$. The marginal density of $u_j$ on $\{|u_j| < 1/4\}$ is $\frac{2}{\pi^2\sqrt{1 - |u_j|^2}} d^3 u_j \le C d^3 u_j$, so integrating over $h_j$ at fixed $(h_0, h_1)$ gives at most $C s^{-3/2}$.
- For $j \in \{2, 3\}$ with $z_j = 1$: write $u_j = \alpha_j \hat{u}_1 + w_j$ with $w_j \perp \hat{u}_1$ ($w_j \in \mathbb{R}^2$). Then $|u_1 \times u_j|^2 = |u_1|^2 |w_j|^2 \ge \frac{15}{16}|w_j|^2$, and $1 - |u_0 \times u_j|^2 \ge 1 - |u_0|^2 |u_j|^2 \ge 1 - |u_j|^2 = x_j^2$, hence
  $$a(-[h_0, h_j]) + a([h_1, h_j]) \ge 2 x_j^2 + \frac{15}{8} |w_j|^2.$$
  On $U_z$, $|x_j| < 1/4$ and $|w_j|^2 \le \frac{16}{15}\cdot\frac{1}{16} = \frac{1}{15}$, so $|\alpha_j| = \sqrt{1 - x_j^2 - |w_j|^2} \ge \sqrt{1 - \frac{1}{16} - \frac{1}{15}} > \frac{4}{5}$. Summing the two sign branches of $\alpha_j$, Haar measure on $h_j$ is $\frac{2}{\pi^2 |\alpha_j|} dx_j\,d^2 w_j \le \frac{5}{2\pi^2} dx_j\,d^2 w_j$, so integrating over $h_j$ at fixed $(h_0, h_1)$ again gives at most $C s^{-3/2}$.
- Finally, integrating $(h_0, h_1)$ over $|x_0|, |x_1| < 1/4, |y| < 1/2$ (and compact $S^2 \times S^1$ directions) against $e^{-s(x_0^2 + x_1^2 + y^2)/2}$ gives at most $C s^{-3/2}$.

Combining the three factors yields $J_z(s) \le C'(1 + s)^{-9/2}$ for every $z \in \mathbb{Z}_2^3 \setminus \{0\}$. Using $I(s) \asymp (1 + s)^{-3/2}$ (row 1143 L92), we get $Z^z(t; \beta) = O_{n,t}(\beta^{-9V/2})$ for every $z \ne 0$.

*Step 2 (Asymptotics and convexity secant sandwich).* By row 1143 equation (11) (`ON FILE`), $Z^0(t; \beta) \sim c_{n,t} \beta^{-(9V-3)/2} \log \beta$ with $c_{n,t} > 0$. By Step 1, all seven twisted terms are $O_{n,t}(\beta^{-3/2}/\log\beta)$ relative to $Z^0$, so
$$f_1(\beta) := \log Z_+(t; \beta) = -\frac{9 t n^3 - 3}{2} \log \beta + \log \log \beta + \log\!\frac{c_{n,t}}{8} + o(1) \qquad (\beta \to \infty).$$
By row 1215 equation (4) (`gap-solve23-astra62.md` L75, checked by row 1221; `ON FILE`), $\lambda_0(\beta) = I_\beta^{3 n^3} \lambda_0(F_{\beta, 0})$ with $I_\beta = (2\pi^2)^{-1}(2\pi/\beta)^{3/2}(1 + o(1))$ and $\lim_{\beta \to \infty} \lambda_0(F_{\beta,0}) = e^{-3 S_n(0)} > 0$. Hence
$$f_2(\beta) := \log \lambda_0(\beta) = -\frac{9 n^3}{2} \log \beta + c_n + o(1) \qquad (\beta \to \infty).$$
Both $f_1$ and $f_2$ are smooth and convex on $(0, \infty)$ (row 708 Lemma 4.2, check 1613). For any smooth convex $f$ with $f(\beta) = -p \log\beta + q \log\log\beta + c + o(1)$ and any fixed $b > 1$, convexity gives
$$\frac{f(\beta) - f(\beta/b)}{1 - 1/b} \le \beta f'(\beta) \le \frac{f(b\beta) - f(\beta)}{b - 1}.$$
Letting $\beta \to \infty$ (where $\log\log(b\beta) - \log\log\beta \to 0$) and then $b \downarrow 1$ gives $\lim_{\beta \to \infty} \beta f'(\beta) = -p$. Applying this to $f_1$ ($p_1 = (9 t n^3 - 3)/2$) and $f_2$ ($p_2 = 9 n^3 / 2$) yields
$$\lim_{\beta \to \infty} \beta(t a_0(\beta) - A_t(\beta)) = \lim_{\beta \to \infty} \beta\bigl(f_1'(\beta) - t f_2'(\beta)\bigr) = -\frac{9 t n^3 - 3}{2} + t \cdot \frac{9 n^3}{2} = \frac{3}{2}. \quad \blacksquare$$

*(Scope note: Proposition 5 holds at fixed $(n, t)$ in the **hot** limit $1 + G(t; \beta) \asymp \beta^{3/2} \log\beta \to \infty$, not on cold tori, and yields the exact same constant $3/2$ as 4D compact Gaussian $U(1)$ with $P_0$, where $1 + G_{\mathrm{flux}}(t; \beta) \asymp (\beta n / t)^{3/2}$ gives $\beta(t a_0 - A_t) \to 3/2$. Thus fixed-lattice weak-coupling positivity is non-selective.)*

### 5.2 Proposition 6 (All-$\beta$ low-energy window localization for `(VIR-down)` — first structural component of C4). `PROVED` (given Theorem 1 and check 1613 regularity `(R)`)

Fix $B = (\mathbb{Z}/n)^3$ ($n \ge 3$), $\beta > 0$, real $t \ge 2$, $\kappa_1 > \kappa \ge 0$, and $M_0 > 0$ such that $G(t/2; \beta) \le M_0$. Let $\Lambda > m_1(\beta)$ satisfy $\Lambda \ge 2/t$ and
$$e^{-t(\Lambda/2 - m_1(\beta))} \cdot \frac{(9|B| + \kappa \Lambda) M_0}{(\kappa_1 - \kappa) m_1(\beta)} \le 1. \tag{5.2}$$
Assume that the low-energy window $\{i \ge 1 : m_i(\beta) < \Lambda\}$ satisfies
$$\sum_{0 < m_i(\beta) < \Lambda} \bigl((D_i(\beta) - D_0(\beta)) - \kappa m_i(\beta)\bigr) e^{-t m_i(\beta)} \ge (\kappa_1 - \kappa) m_1(\beta) e^{-t m_1(\beta)} \tag{5.3}$$
(which holds in particular if $D_i(\beta) - D_0(\beta) \ge \kappa_1 m_i(\beta)$ for every $i \ge 1$ with $m_i(\beta) < \Lambda$). Then `(VIR-down)` holds at $(t, \beta)$ with rate $\kappa$:
$$\partial_\beta G(t; \beta) \ge -\kappa\, t\, \partial_t G(t; \beta).$$

**Proof.**
By check 1613 (regularity `(R)`, L66–75), for every real $t \ge 1$ and $\beta > 0$, $\partial_\beta G(t; \beta) + \kappa t \partial_t G(t; \beta) = t \sum_{i \ge 1} \bigl((D_i - D_0) - \kappa m_i\bigr) e^{-t m_i}$ in any orthonormal eigenbasis of $R_\beta$ on $H_0$. Split the sum at $\Lambda$. By Theorem 1(1), $D_i(\beta) \ge -9|B|$ and $-D_0(\beta) = a_0(\beta) \ge 0$, so $D_i(\beta) - D_0(\beta) \ge -9|B|$ for every $i \ge 1$ and every $\beta > 0$. (In contrast to ascending `(VIR_K)` in row 1522 Proposition HI, the vacuum action $a_0 \ge 0$ enters with the favourable sign, and no upper restriction $\beta < 4$ is needed.)

For $x \ge \Lambda \ge 2/t$, the function $x \mapsto x e^{-tx/2}$ is non-increasing (its derivative $(1 - tx/2)e^{-tx/2} \le 0$), so $m_i e^{-t m_i/2} \le \Lambda e^{-t\Lambda/2}$ and $e^{-t m_i/2} \le e^{-t\Lambda/2}$ for all $m_i \ge \Lambda$. Hence
$$\sum_{m_i \ge \Lambda} \bigl((D_i - D_0) - \kappa m_i\bigr) e^{-t m_i} \ge -\sum_{m_i \ge \Lambda} (9|B| + \kappa m_i) e^{-t m_i/2} e^{-t m_i/2} \ge -(9|B| + \kappa \Lambda) e^{-t\Lambda/2} G(t/2; \beta) \ge -(9|B| + \kappa \Lambda) M_0 e^{-t\Lambda/2}.$$
Adding (5.3) and applying (5.2) yields $\sum_{i \ge 1} ((D_i - D_0) - \kappa m_i) e^{-t m_i} \ge 0$. $\blacksquare$

**Scope and limits of Proposition 6 (`ARGUED`):** On a cold box ($G(t; \beta) \le 4/21 \implies m_1 \ge \frac{\log(21/4)}{t}$) with $G(t/2; \beta) \le 1$, $\kappa_1 = 2\kappa$, $\kappa = O(1)$, and $t = u = n/512$, (5.2) is satisfied by $\Lambda = 2 m_1 + O\!\left(\frac{\log n}{n}\right)$. Thus the high-spin collapse of Theorem 1 does not obstruct thermal `(VIR-down)` once $G(t/2)$ is controlled. However, Proposition 6 (i) requires the additional half-time bound $G(t/2; \beta) \le M_0$, (ii) does not supply the low-energy bound (5.3) on the band, and (iii) holds verbatim for compact Wilson $U(1)$ and 5D $\mathrm{SU}(2)$ (so it is a structural localization, not a selective input).

---

## 6. Selectivity, Lemma ALG, Equivalence to `(PUR-io)`, Labels, and Open Boundary

### 6.1 Where Each Argument Fails for the Free Photon and Weak 4D Compact $U(1)$, and Lemma ALG Audit (row 1553)

| Statement | Free photon | Weak 4D compact $U(1)$ | 5D $\mathrm{SU}(2)$ weak / twins (g3) / products (g4) | Reads law vs algebra/dim (Lemma ALG, row 1553)? |
|---|---|---|---|---|
| **Lemma 1 & Theorem 1** (high-spin collapse; refutes `(LEV-down)` & all-state form bounds) | Non-compact link space (no spin $j$); vacuously $\mathcal{R} \equiv 0$, so `(LEV-down)` and form bounds fail trivially | Holds verbatim for compact Wilson $U(1)$ (replace $I_{2j+1}$ by $I_{|n|}$ as in row 1522 §5.1) | Holds verbatim in 5D $\mathrm{SU}(2)$ and all gapped twins (g3) | Reads only compact-group link convolution (**not** a selective input for `(PUR-io)`, and not claimed as one; it is a proof-method obstruction) |
| **Theorem 2** (cold-torus `(VIR-down)` in compact Gaussian $U(1)$ with $P_0$) | Fails: $\mathcal{R} \equiv 0$ (no compact flat holonomies) | **Holds** on cold tori in zero-monopole compact Gaussian $U(1)$ with $P_0$ ($\frac{9}{10\beta} < \mathcal{R} < \frac{1}{\beta}$ for $\beta \ge 4$), while `(T-down)` fails everywhere; for interacting Wilson $U(1)$ with $P_0$, `(T-down)` fails by check 1613 given row 1565/1571 | Shows that beating the free photon via $O(1/\beta)$ rates reads only compact $U(1)^3$ holonomy topology (NOT a gap) | Explicitly diagnoses **algebraic/topological non-selectivity** in row 1610's trigger: $O(1/\beta)$ cold-torus rates fail the gapless $U(1)$ test |
| **Theorem 3** (necessary $\Omega(1)$ budget on $[\beta_K, \beta_{K+r}]$; refutes $o(1)$, $O(1/\beta)$, $L^1$ rates) | Fails budget (3.1): $\mathcal{R} \equiv 0$ while $n m_1 \le 2\pi < 844$ (`PROVED`) | Fails budget (3.1) for compact Gaussian $U(1)$ with $P_0$ ($\mathcal{R} < 1/\beta$, $n m_1 = 2/\beta$; `PROVED`), and fails `(T-down)` for weak Wilson/Villain $U(1)$ with $P_0$ (check 1613; `ON FILE`); full $U(1)^3$ projection open for interacting Wilson | 5D $\mathrm{SU}(2)$ weak: conditional on $n m_1 \le C(\beta n)^{-1/3}$ and $\kappa \le 1/(3\beta)$ (check 1613 L111). Products (g4): fails by Remark 4.2 (`PROVED`) | The budget condition $\int \kappa \ge \log(512\log(21/4)/(n m_1(\beta_h)))$ with $\kappa = \Omega(1)$ on $[\beta_K, \beta_{K+r}]$ reads the **law** (P-law and P-scale of row 1553), not algebra or dimension |
| **Theorem 4** (anisotropic split & dichotomy: magnetic suppression $t a_0^\sigma - A_t^\sigma \ge \frac{1}{2}(\kappa - C/\beta) t \bar{E}_t$ vs $\partial_\xi \log(1+G) > C t \bar{E}_t$) | Both alternatives fail for every $\kappa > 1/\beta, C = 1$: $0 < \partial_\xi \log(1+G) < t\bar{E}_t$ and $t a_0^\sigma - A_t^\sigma < 0$ (`PROVED`, exact on every finite lattice) | Both alternatives fail identically on every finite lattice in compact Gaussian $U(1)$ with $P_0$ for $\kappa > 1/\beta, C=1$ (`PROVED`); in interacting Villain/Wilson $U(1)$ with full $U(1)^3$ projection, monopole shift is `ARGUED` $O(e^{-c\beta})$ | Weak 5D $\mathrm{SU}(2)$ & 4D $\mathrm{SU}(2)$ torons: $t a_0^\sigma - A_t^\sigma < 0$ (`ARGUED`). 1-plaquette $\mathrm{SU}(2)$ Wilson (same algebra & weight!): $t a_0^\sigma - A_t^\sigma < 0$ at $\beta = 0.5, 2, 4, 8$ (`GUIDE`, §6.4). Product with massless scalar (g4): fails (`PROVED`). Strong-coupling $U(1)$ twin (g3): electric term $\frac{1}{\beta}\partial_\xi \log(1+G)$ dominates, not magnetic suppression (`ARGUED`) | The identity (4.1) is universal. The **forced band clause** $t a_0^\sigma - A_t^\sigma \ge c_0 t \bar{E}_t > 0$ at late $\beta_K$ reads a non-perturbative property of the **4D $\mathrm{SU}(2)$ scaling law** (passes Lemma ALG, (g1)–(g5)); it is **OPEN** |
| **Proposition 5** ($\beta(t a_0 - A_t) \to 3/2$ at fixed $n, t$) | Fails ($\equiv 0$) | Same limit $3/2$ in compact Gaussian $U(1)$ with $P_0$ | $9/4$ in 5D $\mathrm{SU}(2)$ (`ARGUED`); hot regime ($G \to \infty$) | Reads flat-holonomy dimension count only (non-selective, hot) |
| **Proposition 6** (low-energy window localization) | N/A (non-compact) | Holds verbatim for compact Wilson $U(1)$ | Holds verbatim in 5D $\mathrm{SU}(2)$ and twins (g3) | Structural reduction only; **not** a selective input (Lemma ALG) |

### 6.2 Equivalence to `(PUR-io)`
- **No equivalent restatement is proposed as progress.**
- For `(T-down)` itself (`ON FILE`, check 1613): on calibrated Wilson boxes, `(T-down)` implies `(PUR-io)` over allowed sides by enlargement, while the converse and strictness are open; at fixed $K$, the literal existential `(T-down)` is equivalent to $G(u; \beta_K) \le 4/21$ plus right-neighborhood non-decrease of $G(u; \cdot)$ at $\beta_K$.
- **None of Theorems 1–4 or Propositions 5–6 is equivalent to `(PUR-io)`:** Theorems 1, 2, 3, 4(1)–(3) and Proposition 5 are unconditional theorems (holding independently of whether `(PUR-io)` is true or false), and Proposition 6 is a one-way spectral localization at a single $(t, \beta)$ that neither implies `(PUR-io)` (lacking `(HOT)` and a band supplier) nor follows from `(PUR-io)`.

### 6.3 Summary of Why `(VIR-down)` on the Band Remains Open (Five Approaches Tried and Where Each Stopped)
1. **All-level / operator conjugation / GL12 generator bounds (`PROVED` dead):** Killed unconditionally on every finite Wilson box at every $\beta > 0$ by Theorem 1 + Corollaries 1A–1B.
2. **Convexity / secant bounds on $\log Z_+ - t \log \lambda_0$ (`ARGUED` dead):** Both $\log Z_+$ and $\log \lambda_0$ are convex; expanding at $\beta + h$ yields a lower bound $G'(\beta) \ge \frac{G(\beta+h) - G(\beta)}{h} - \frac{h}{2} M_F$, which requires knowing $G(\beta+h) > G(\beta)$ beforehand (circular).
3. **Schwinger–Dyson force identity (`ON FILE` / `ARGUED` insufficient):** $t a_0 - A_t = \frac{\beta}{3}(Q_t - t q_\infty)$ holds in compact $U(1)$ (with factor $\beta/4$) and 5D $\mathrm{SU}(2)$ and leaves the identical extensive subtraction $Q_t - t q_\infty$.
4. **Weak-coupling / $O(1/\beta)$ / toron / fixed-box expansions (`PROVED` insufficient):** Killed on fixed-physical-ratio windows $[\beta_K, \beta_{K+r}]$ by Theorem 3(2) (and non-selective against compact Gaussian $U(1)$ with $P_0$ by Theorem 2).
5. **Anisotropic / electric–magnetic decomposition (`PROVED` dichotomy, open core):** Theorem 4 isolates the exact non-perturbative obligation on the band at late bare couplings $\beta_K \to \infty$: either macroscopic spatial (magnetic) action suppression in cold thermal neutral states, $t a_0^\sigma - A_t^\sigma \ge \frac{1}{2}(\kappa - C/\beta) t \bar{E}_t > 0$ with $\kappa = \Omega(1)$ (opposite in sign to the free photon, compact Gaussian $U(1)$, and small-box torons), or super-classical anisotropy response $\partial_\xi \log(1+G)|_{\xi=1} > C t \bar{E}_t$. No method on file proves either on the band; this is the lattice trace-anomaly obstruction in exact downward form.

### 6.4 Guide Check Record (Floating Point, Outside Repository; Never a Proof Step)
One small Python script was run in the session scratch directory outside the repository (`<appDataDir>/brain/.../scratch/guide_check.py`, one process, < 50 MB RAM, < 2 s) solely to sanity-check signs and arithmetic:
- Verified Lemma 1(2)–(3) for $\beta \in \{0.1, 1, 4, 10, 20\}$ and $2j \le 15$ (0 violations).
- Verified Theorem 2 on $n \in \{4, 8, 12\}$, $\beta \in \{2, 4, 10\}$, $t/t_{\mathrm{cold}} \in \{1.02, 2, 5\}$: at $\beta = 4, n = 12, t/t_{\mathrm{cold}} = 1.02$, $G = 0.1885 \le 4/21$, $\beta \mathcal{R}^{\mathrm{cG}} = 1.00000000$, and $E_{\mathrm{phot}}/E_{\mathrm{flux}} = 1.46 \times 10^{-16} \le 5.085 \times 10^{-2}$.
- Verified Theorem 4(1) on the 1-plaquette $\mathrm{SU}(2)$ transfer matrix (truncation $2j \le 17$, $t = 2$, $\beta \in \{0.5, 2, 4, 8\}$): identity (4.1) matched to $10^{-13}$; moreover, at $\beta = 4.0, 8.0$ (cold: $G \approx 1.5 \times 10^{-3}, 1.1 \times 10^{-3}$), both $\partial_\beta \log(1+G) < 0$ and $t a_0^\sigma - A_t^\sigma < 0$.

### 6.5 Complete Label Table

| Item | Label | Anchor / Dependencies |
|---|---|---|
| Lemma 1 (all-$\beta$ Poisson integral, $0 < r_n < 1$, $c_j$ & $-\beta\eta_j'$ bounds) | `PROVED` | §1.1 (self-contained; extends row 710 Lemma J) |
| Theorem 1(1)–(3) (all-$\beta$ Theorem U bounds, $\lim (D_i - D_0)/m_i = 0$, $\lim m_i(\beta_1)/m_i(\beta_2) = 1$) | `PROVED` | §1.2 (given row 710 Lemma C and §0.2) |
| Corollaries 1A, 1B, 1C (failure of `(LEV-down)`, all-state form bounds on $H_0^\perp$, small-time collapse) | `PROVED` | §1.3 (from Theorem 1; check 1613 for $t \ge 1$) |
| Theorem 2 (4D compact Gaussian $U(1)$ with $P_0$: $\frac{9}{10\beta} < \mathcal{R}^{\mathrm{cG}} < \frac{1}{\beta}$ on cold tori at $\beta \ge 4$; `(T-down)` fails; trigger under-specified) | `PROVED` | §2.2 (self-contained) |
| Theorem 3(1)–(3) (necessary budget (3.1), window width (3.2), $o(1)/O(1/\beta)/L^1$ calibrated obstructions) | `PROVED` | §3.1 (given check 1453 `BND-1`, row 1461 (1)–(2)/check 1465, row 1215 (5)/check 1221) |
| Theorem 4(1)–(3) (anisotropic split (4.1), spectral form (4.2), dichotomy, exact sign reversal (4.3) in free photon & compact Gaussian $U(1)$) | `PROVED` | §4.1 (given Lemma D1 / check 1613) |
| Remark 4.2 (failure of `(T-down)` in product with neutral massless scalar, test `(g4)`) | `PROVED` | §4.1 (given row 1573 / check 1579, check 1613) |
| Proposition 5 ($\lim_{\beta \to \infty} \beta(t a_0 - A_t) = 3/2$ at fixed $n, t \ge 3$, including all 7 twists) | `PROVED` | §5.1 (given row 1143 (1)–(3), (11)/check 1144, row 1215 (4)/check 1221) |
| Proposition 6 (all-$\beta$ low-energy window localization for `(VIR-down)`) | `PROVED` | §5.2 (given Theorem 1 and check 1613 `(R)`) |
| Weak-coupling $\mathrm{SU}(2)$ toron spatial-action sign; Schwinger–Dyson insufficiency; convexity circularity | `ARGUED` | §§4.1, 6.3 |
| 1-plaquette $\mathrm{SU}(2)$ values and Python sanity checks | `GUIDE` | §6.4 (outside repo; never a proof step) |
| `(VIR-down)` on the band C4; `(HOT)` C2; `(PUR-io)`; mass gap | **OPEN** | untouched |

---

RESULT: Outcome (c) (scoped obstructions with quantifiers) plus (d) only as a non-selective localization (Prop. 6);
(a), (b) are not reached, and (VIR-down) on the band, (PUR-io) and the gap stay OPEN. Hand proofs (unchecked, no Lean):
(1) Lemma 1, Theorem 1 & Corollaries 1A-1C: all-beta Bessel/Theorem-U bounds, lim (D_i-D_0)/m_i = 0 and
lim m_i(b1)/m_i(b2) = 1, unconditionally refuting (LEV-down) (E>1), every all-state operator form bound on H_0^perp
(incl. bounded & GL12 generators), and small-time lower bounds on every finite Wilson box at every beta > 0.
(2) Theorem 2: gapless 4D compact Gaussian U(1) with P_0 satisfies 9/(10 beta) < R < 1/beta on every cold torus
(G<=4/21, n>=4, beta>=4) while (T-down) fails everywhere—refuting row 1610 L137 and showing §4's trigger is weak.
(3) Theorem 3: exact budget int kappa >= log(512 log(21/4)/(n_K m_1(beta_h))) and width |beta_{K+r}-beta_K-sr| <= W(r)
(given 1461/1465), ruling out o(1)/O(1/beta) rates on hot-UV windows and L^1 schedules at large beta_h (given 1215/1221).
(4) Theorem 4, Remark 4.2, Props. 5-6: split t a_0-A_t = beta^-1 d_xi log(1+G)|_{xi=1} + 2(t a_0^sigma-A_t^sigma) forcing
magnetic suppression or super-classical anisotropy (both fail for free photon & compact Gaussian U(1)); SU(2)xscalar fails;
fixed-box hot limit beta(t a_0-A_t)->3/2 (given 1143/1215); all-beta window localization. None is equivalent to (PUR-io).
