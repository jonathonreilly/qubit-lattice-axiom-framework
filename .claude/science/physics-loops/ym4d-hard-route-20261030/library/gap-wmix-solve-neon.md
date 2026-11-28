# Attack on (W-mix) and the 4D SU(2) Mass Gap Seed (PUR-io)

- **Target file:** `library/gap-wmix-solve-neon.md`
- **Status:** Complete — Outcome (c) (Obstruction Theorem)
- **Date:** 2026-11-27

## 0. Scope and Reading Log

Starting survey of the lane records:
- `FINISH.md` (rows 1072, 1115-1123, 1378-1443, 1453, 1468, 1510-1527, 1553, 1566-1598)
- `library/gap-direction6-fable.md` (PZ-why, WB1-WB3)
- `library/gap-band-direction5-fable.md` ((13.4)-(13.6))
- `library/gap-mech-direction2-fable.md` (Prop NEG, K-I / K-II)
- `library/gap-k2-tool-design-fable.md` (section 3.1, (PUR-io))
- `library/gap-agy-seed-approaches-neon-check-astra62.md` (check 1527)
- `library/open-registry.md`

Every claim below will be labeled `PROVED`, `ARGUED`, `GUESSED`, or `ON FILE (row ...)`.

---

## 1. Exact Inventory of On-File Forms of `(W-mix)` and Their Consumers

Every item below is `ON FILE` with its exact row anchor.

| Name / Anchor | Exact Statement of the Mixing Estimate `(W-mix)` | Consumer & Coupling | Proved Range / Known Obstructions |
|---|---|---|---|
| **Bound (2)** (row 1573, check 1579) | $B_K := \frac{1}{2}\int_0^\pi\int_0^\pi \mathbb{E}_\mu |h(s,t;X,Y)|\,ds\,dt \le \log(625/457)$ infinitely often on $\beta_K$, where $h = \partial_s\partial_t \log L(R_s X, R_t Y)$, $L(X,Y) = k_v^+(x_1,y_1)k_v^+(x_2,y_2)$, $d\mu = L^2 dX dY / Z_+(u)^2$ (paired-link circle $R_s$, or thermal clock $V_s$). Signed form: $\mathbb{E}_\mu J = D(p\|m) + D(m\|p) \le \log(625/457)$ (`Lemma JI` substance). | Direct to `(PUR-io)` by Jensen ($-\log P_K \le \mathbb{E}_\mu J \le B_K$) at $\beta_K$ (calibrated trajectory). | Proved at fixed $\beta < 2/9$ (4D SU(2)), $\beta < 1/9$ (4D U(1)), $\beta < 1/6$ (5D SU(2)). Fails for weak 4D compact U(1) ($\mathbb{Z}_2^3$-even) and neutral spectator. Strictly stronger than `(PUR-io)` on abstract positive kernels (check 1579). |
| **`(SW)`** (row 1574, check 1580) | $L_\sigma(v) := \sup_{s,t\in[0,\pi],p} \sum_q \mathbb{E}_\mu |h_{pq}(R_s Y', R_t Y)| \le C v^{-3-\epsilon}$ on $\beta \in [2,3]$ (band form), or $(3\pi^2/4) n^3 L_\sigma(u/2) \le \log(625/457)$ (trajectory form). | Band form $\implies$ full band seed (needs carry R12 for `(PUR-io)`). Trajectory form $\implies$ `(PUR-io)` directly. | Proved for $\beta < 2/9$ (check 1580). Fails weak 4D U(1) and neutral spectator. Strictly stronger than seed on abstract transfer data (check 1580). |
| **`TC(eps)` / `TC_{diag}(eps)` / `TC_{traj}`** & **`TS(eps)` / `TS_{diag}(eps)` / `TS_{traj}`** (row 1576, check 1582) | Two-cut (single-replica, gauge- & centre-invariant) or two-seam ($\mathrm{Sp}(2)$) cross-cylinder covariance in defect Gibbs measures $\mathbb{P}^{\mathrm{cut},+}_{\lambda,\mu}$ or $\mathbb{P}_{\lambda,\mu}$: e.g. `TC_{diag,0}(eps)`: $\int_0^1 \sqrt{3n^3 \sum_{e'} \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut},0}_{\lambda,\lambda}}(E_{0,e_0}, E_{v,e'})}\,d\lambda \le C v^{-\epsilon}$ on $\beta \in [2,3]$; trajectory form $\mathcal{L}_{\mathrm{diag}}^+(u;\beta_K) \le \arccos(\sqrt{21}/5)$. | Band form $\implies$ full/neutral band seed (needs R12). Trajectory form $\implies$ `(M-io-exists)` / `(PUR-io)`. | Proved for $\beta < 1/18$ (isotropic) and $b_t \in [2,3], \kappa \le \kappa_* \approx 1.6 \times 10^{-8}$ (Theorem 4.1). Fails weak 4D Villain U(1) (neutral) and Wilson U(1) (unprojected), 3D/4D/5D free Maxwell, neutral spectator, $\beta \to \infty$ at fixed box. Defect measures carry $\Theta(n^3)$ free-energy defect (check 1582). |
| **`(B)` / `BC(eps)` / `(L)`** (check 1556, rows 1565/1566/1568, checks 1570-1572) | Cut-rotation mixed boundary covariance $\sup_{s,t,x}\sum_y \mathbb{E}|D_x D_y \log K_v(R_s B, R_t C_z A)| \le C v^{-2-\epsilon}$. | Controls `(N-flux)` (electric-flux weights $a_t = Z_+(t)/Z^0(t)$) only; blind to $\Pi = Z^0(2u)/Z^0(u)^2$ and neutral spectators. | Proved for $\beta < 1/18$ (1566), $\beta < 2/9$ (1568). Fails weak 4D compact U(1) (proved, 1565/1571). |
| **`(FL)`** (row 1510, check 1513; Registry R10) | In-law posterior score covariance decay for one $Q_2$ step ($\kappa = \beta$) at $\beta \in [2,3]$: $|\operatorname{Cov}_{\mu^V}(f, S_c)|^2 \le \mathbb{E}_{\mu^V}[\sum_l \gamma_{cl} |\nabla_l f|^2]$ with $\mathbb{E}[\gamma_{cl}] \le C e^{-m\operatorname{dist}(c,l)}$, plus local-to-global theorem. | Carry for weighted Poincaré (`PC` + `REV`, row 1510); still needs coarse gap source (T2) and joint moments. | Open at $\beta \in [2,3]$. Expected to hold for U(1) and 5D too (it is a carry, not selective). |
| **`(CM_k)`** (row 1468 §4.3) | Mixing of the constrained $Q_2$ system for every rule in $\mathrm{Tube}(\Phi_k^*, \rho_k; \eta_k)$ and every coarse field in a regular set, plus large-field bound. | Feeds `(K2-STEP)` $\to$ Theorem K2 $\to$ `(PUR-io)`. | Weak-coupling release floor $> 2^{1600}$; order-one band has no closed class and no method. Uniform mixing over all coarse/boundary fields fails above $\beta_{\mathrm{FSS}} \approx 1.0109$ (`CA-FAIL`, row 1072). |
| **`(L3)` / `(CONV)` / `(H-two)` / `(H-swap)`** (rows 1115-1123; Lemma TS3, Lemma JI, Prop J) | In-law core-ring mixing: `(H-two)` $\mathbb{E}\,d_{\mathrm{TV}}(m_\Omega, m_{\Omega'}) \le \eta$ (within factor 2 of $\beta$-mixing, `TS3`); `(H-two-N1)` single neutral core observable; `(H-swap)` joint swap-defect tails (`CONV-swap`). | `(CONV-swap)` $\implies$ exponential clustering; `(CONV-two)` open. | `(H-swap)` **REFUTED** at $\beta \in [2.3, 2.6]$ for every cell size $l$ (`Proposition J`, `Lemma JI`, check 1121). `(H-ent-local)` refuted by vES coexistence (row 1118). One-sample affine criteria cannot force clustering without uniqueness (`Lemma AFF`, `Example PROD`, row 1122/1123). |
| **`(T-mix)`** (row 1553 §3.3; sharpened row 1584 §2.5) | Proof of `(FL)`, or two-sample mixing at typical ends across a half-cylinder of length $u/2$ at $\beta \in [2,3]$, or covariance decay inside defect measures uniform in layer coupling. | Feeds bound (2) (1573), `TC` (1576), or `PC+REV` (1510). | Open above Dobrushin range ($2/9$); uniform mixing over all boundaries fails above $1.0109$ (row 1072). |

---

## 2. Theorem 1: Exact Equivalence of Bounded Half-Cylinder Mixing (`(H-two)`, $\beta_{\mathrm{mix}}$, Hellinger, Affinity) to `(PUR-io)`

### 2.1 The positive-kernel transfer family $\mathcal{F}_+$

Let $(\mathcal{X}, \mathcal{F}, \mu_0)$ be a $\sigma$-finite measure space. Define the family $\mathcal{F}_+$ to consist of all nonzero self-adjoint, positive semidefinite, trace-class integral operators $A$ on $L^2(\mathcal{X}, \mu_0)$ admitting a measurable, symmetric, nonnegative kernel $k : \mathcal{X} \times \mathcal{X} \to [0, \infty)$ ($k(x, y) = k(y, x) \ge 0$) with
$$
Z := \operatorname{Tr}(A^2) = \iint_{\mathcal{X}^2} k(x, y)^2\,d\mu_0(x)\,d\mu_0(y) \in (0, \infty).
$$
Let $k_2(x, x') := \int_{\mathcal{X}} k(x, y) k(y, x')\,d\mu_0(y)$ be the kernel of $A^2$. Associate to $A \in \mathcal{F}_+$ the two-slice joint density $p$, marginal density $\rho$, product marginal $m$, conditional density $p_x$ (for $x \in \mathcal{X}_+ := \{\rho > 0\}$, which has $\rho$-measure $1$), and spectral purity $P$:
$$
p(x, y) := \frac{k(x, y)^2}{Z}, \qquad \rho(x) := \int_{\mathcal{X}} p(x, y)\,d\mu_0(y) = \frac{k_2(x, x)}{Z}, \qquad m(x, y) := \rho(x)\rho(y),
$$
$$
p_x(y) := \frac{p(x, y)}{\rho(x)} = \frac{k(x, y)^2}{k_2(x, x)}, \qquad P := \frac{\operatorname{Tr}(A^4)}{(\operatorname{Tr}(A^2))^2} \in (0, 1].
$$

**Wilson instantiation (`ON FILE`, rows 1373, 1468, 1527, 1573, 1574).** For 4D $\mathrm{SU}(2)$ Wilson lattice gauge theory on $(\mathbb{Z}/n)^3$ at any coupling $\beta \ge 0$ and any integer $v \ge 1$ ($u = 2v$), take $\mathcal{X} = \mathrm{SU}(2)^{3n^3}$ with normalized Haar measure $\mu_0$ and $A = P_0 T^v$ (where $T$ is the physical gauge-invariant Wilson transfer operator carrying vertex-gauge projection $P_{\mathcal{G}}$, and $P_0 = \frac{1}{8}\sum_{z \in \mathbb{Z}_2^3} C_z$ projects onto the centre-neutral sector; `ON FILE`, check 1527 §(i)). Its kernel $k_v^+(x, y) = \frac{1}{8}\sum_z K_v(x, C_z y)$ is smooth, symmetric, and strictly positive on $\mathcal{X}^2$, with $Z = Z_+(u) = \operatorname{Tr}(P_0 T^u)$, $\operatorname{Tr}(A^4) = Z_+(2u) = \operatorname{Tr}(P_0 T^{2u})$, and $P = Z_+(2u)/Z_+(u)^2 = P_K$. The same holds for the unprojected transfer $A = T^v$ (with $P = \Pi = Z^0(2u)/Z^0(u)^2$), for 4D compact $\mathrm{U}(1)$, for 5D $\mathrm{SU}(2)$, and for massive free scalar fields.

Define the four standard bounded half-cylinder mixing quantities of $A \in \mathcal{F}_+$:
1. Two-sample squared Hellinger distance: $H_{\mathrm{two}}^2 := \mathbb{E}_{x, x' \sim \rho \otimes \rho}[H^2(p_x, p_{x'})] = 1 - \mathbb{E}_{x, x'}[\operatorname{Aff}(p_x, p_{x'})]$, where $\operatorname{Aff}(f, g) := \int \sqrt{fg}\,d\mu_0$ and $H^2(f, g) := 1 - \operatorname{Aff}(f, g)$.
2. Two-sample total variation distance (the cylinder form of `(H-two)` of rows 1118–1120): $d_{\mathrm{TV}}^{\mathrm{two}} := \mathbb{E}_{x, x' \sim \rho \otimes \rho}[d_{\mathrm{TV}}(p_x, p_{x'})]$.
3. Joint-to-product total variation ($\beta$-mixing coefficient across the half-cylinder): $\beta_{\mathrm{mix}} := d_{\mathrm{TV}}(p, m) = \mathbb{E}_{x \sim \rho}[d_{\mathrm{TV}}(p_x, \rho)]$.
4. Joint-to-product squared Hellinger / affinity defect: $H^2(p, m) := 1 - \operatorname{Aff}(p, m) = \mathbb{E}_{x \sim \rho}[H^2(p_x, \rho)]$.

---

### 2.2 Theorem 1A (Exact single-box two-sided equivalence and sharpness on $\mathcal{F}_+$) — `PROVED`

**Theorem 1A (`PROVED`).** *For every $A \in \mathcal{F}_+$:*
1. *(Midpoint affinity identity; `ON FILE` rows 1373, 1526, check 1527 §(i), proved here for all $A \in \mathcal{F}_+$ without strict positivity):*
   $$P = \mathbb{E}_{x, x' \sim \rho \otimes \rho}\!\left[\operatorname{Aff}(p_x, p_{x'})^2\right].$$
2. *(Exact two-sided bounds):*
   $$1 - \sqrt{P} \;\le\; H_{\mathrm{two}}^2 \;\le\; 1 - P, \tag{T1.1}$$
   $$1 - \sqrt{P} \;\le\; d_{\mathrm{TV}}^{\mathrm{two}} \;\le\; \sqrt{1 - P}, \tag{T1.2}$$
   $$1 - P^{1/4} \;\le\; H^2(p, m) \;\le\; H_{\mathrm{two}}^2 \;\le\; 1 - P, \tag{T1.3}$$
   $$1 - P^{1/4} \;\le\; \beta_{\mathrm{mix}} \;\le\; d_{\mathrm{TV}}^{\mathrm{two}} \;\le\; \sqrt{1 - P}. \tag{T1.4}$$
   *In particular, $P \ge (1 - d_{\mathrm{TV}}^{\mathrm{two}})^2$, $P \ge (1 - H_{\mathrm{two}}^2)^2$, $P \ge (1 - H^2(p, m))^4$, and $P \ge (1 - \beta_{\mathrm{mix}})^4$ (strictly sharper for every $\beta_{\mathrm{mix}} \in (0, 1)$ than $(1 - 2\beta_{\mathrm{mix}})_+^2$ from `Lemma TS`).*
3. *(Sharpness on strictly positive, strictly positive definite kernels in $\mathcal{F}_+$):*
   - *The lower bounds $1 - \sqrt{P} \le H_{\mathrm{two}}^2$, $1 - \sqrt{P} \le d_{\mathrm{TV}}^{\mathrm{two}}$, and $1 - P^{1/4} \le H^2(p, m)$ are asymptotically sharp at every $P \in (0, 1)$.*
   - *The upper bound $H_{\mathrm{two}}^2 \le 1 - P$ is asymptotically sharp at every $P \in [1/2, 1)$.*
   - *The exponent $1/2$ in the upper bounds $d_{\mathrm{TV}}^{\mathrm{two}} \le \sqrt{1 - P}$ and $\beta_{\mathrm{mix}} \le \sqrt{1 - P}$ is sharp as $P \uparrow 1$.*

**Proof (`PROVED`).**
*(1)* For $x, x' \in \mathcal{X}_+$,
$$\operatorname{Aff}(p_x, p_{x'}) = \int_{\mathcal{X}} \frac{k(x, y) k(x', y)}{\sqrt{k_2(x, x) k_2(x', x')}}\,d\mu_0(y) = \frac{k_2(x, x')}{\sqrt{k_2(x, x) k_2(x', x')}}.$$
If $x \notin \mathcal{X}_+$, then $k_2(x, x) = \int k(x, y)^2\,d\mu_0(y) = 0$, so by Cauchy–Schwarz $k_2(x, x') = 0$ for all $x'$. Squaring and integrating against $\rho(x)\rho(x')\,d\mu_0(x)\,d\mu_0(x') = Z^{-2} k_2(x, x) k_2(x', x')\,d\mu_0(x)\,d\mu_0(x')$ therefore yields
$$\mathbb{E}_{x, x'}[\operatorname{Aff}(p_x, p_{x'})^2] = \frac{1}{Z^2}\iint_{\mathcal{X}^2} k_2(x, x')^2\,d\mu_0(x)\,d\mu_0(x') = \frac{\operatorname{Tr}(A^4)}{Z^2} = P.$$

*(2)* Write $R := \operatorname{Aff}(p_x, p_{x'}) \in [0, 1]$, so $\mathbb{E}[R^2] = P$ and $\mathbb{E}[R] = 1 - H_{\mathrm{two}}^2$.
- *Proof of (T1.1):* Since $R \in [0, 1]$, $R^2 \le R$, giving $P = \mathbb{E}[R^2] \le \mathbb{E}[R] = 1 - H_{\mathrm{two}}^2$. By Cauchy–Schwarz, $1 - H_{\mathrm{two}}^2 = \mathbb{E}[R] \le \sqrt{\mathbb{E}[R^2]} = \sqrt{P}$. Rearranging gives (T1.1).
- *Proof of (T1.2):* For any two probability densities $f, g$ on $(\mathcal{X}, \mu_0)$,
  $$H^2(f, g) = \frac{1}{2}\int (\sqrt{f} - \sqrt{g})^2\,d\mu_0 \le \frac{1}{2}\int |\sqrt{f} - \sqrt{g}|(\sqrt{f} + \sqrt{g})\,d\mu_0 = d_{\mathrm{TV}}(f, g),$$
  and by Cauchy–Schwarz,
  $$d_{\mathrm{TV}}(f, g)^2 = \frac{1}{4}\left(\int |\sqrt{f} - \sqrt{g}|(\sqrt{f} + \sqrt{g})\,d\mu_0\right)^2 \le \frac{1}{4}(2 - 2\operatorname{Aff}(f, g))(2 + 2\operatorname{Aff}(f, g)) = 1 - \operatorname{Aff}(f, g)^2.$$
  Averaging over $(x, x') \sim \rho \otimes \rho$ and using (T1.1) and Jensen on the concave function $t \mapsto \sqrt{1 - t}$ gives
  $$1 - \sqrt{P} \le H_{\mathrm{two}}^2 \le d_{\mathrm{TV}}^{\mathrm{two}} \le \mathbb{E}\!\left[\sqrt{1 - R^2}\right] \le \sqrt{1 - \mathbb{E}[R^2]} = \sqrt{1 - P}.$$
- *Proof of (T1.3):* Using $p(x, y) = \rho(x) p_x(y)$, write
  $$\operatorname{Aff}(p, m) = \iint_{\mathcal{X}^2} \sqrt{p(x, y)\rho(x)\rho(y)}\,d\mu_0(x)\,d\mu_0(y) = \int_{\mathcal{X}_+} \sqrt{\rho(y)} \left(\int_{\mathcal{X}_+} \rho(x)\sqrt{p_x(y)}\,d\mu_0(x)\right) d\mu_0(y).$$
  Applying Cauchy–Schwarz in $y$ with $\int \rho(y)\,d\mu_0(y) = 1$, followed by Tonelli's theorem for nonnegative functions, gives
  $$\operatorname{Aff}(p, m)^2 \le \int_{\mathcal{X}} \left(\int_{\mathcal{X}_+} \rho(x)\sqrt{p_x(y)}\,d\mu_0(x)\right)^2 d\mu_0(y) = \iint_{\mathcal{X}_+^2} \rho(x)\rho(x')\operatorname{Aff}(p_x, p_{x'})\,d\mu_0(x)\,d\mu_0(x') = 1 - H_{\mathrm{two}}^2 \le \sqrt{P}.$$
  Hence $\operatorname{Aff}(p, m) \le P^{1/4}$, i.e., $1 - P^{1/4} \le H^2(p, m)$. In the opposite direction, concavity of $t \mapsto \sqrt{t}$ and $\rho(y) = \int \rho(x') p_{x'}(y)\,d\mu_0(x')$ give $\sqrt{\rho(y)} \ge \int \rho(x') \sqrt{p_{x'}(y)}\,d\mu_0(x')$. Multiplying by $\rho(x)\sqrt{p_x(y)}$ and integrating over $(x, y)$ gives $\operatorname{Aff}(p, m) \ge \mathbb{E}_{x, x'}[\operatorname{Aff}(p_x, p_{x'})] = 1 - H_{\mathrm{two}}^2$, so $H^2(p, m) \le H_{\mathrm{two}}^2 \le 1 - P$.
- *Proof of (T1.4):* From $H^2(p, m) \le d_{\mathrm{TV}}(p, m) = \beta_{\mathrm{mix}}$ and (T1.3) we get $1 - P^{1/4} \le \beta_{\mathrm{mix}}$. Since $\rho = \mathbb{E}_{x'}[p_{x'}]$ and $q \mapsto d_{\mathrm{TV}}(p_x, q)$ is convex, $\beta_{\mathrm{mix}} = \mathbb{E}_x[d_{\mathrm{TV}}(p_x, \mathbb{E}_{x'}[p_{x'}])] \le \mathbb{E}_{x, x'}[d_{\mathrm{TV}}(p_x, p_{x'})] = d_{\mathrm{TV}}^{\mathrm{two}} \le \sqrt{1 - P}$ (`Lemma TS` of row 1119). Finally, for every $x \in (0, 1)$, $(1 - x)^2 = 1 - 2x + x^2 > (1 - 2x)_+$, so $(1 - x)^4 > (1 - 2x)_+^2$.

*(3) Sharpness witnesses (all strictly positive, strictly positive definite kernels on finite sets with counting measure):*
- *Witness A ($N \times N$ spiked kernel):* Fix $t \in (0, 1)$, set $\alpha := \sqrt{t/(1 - t)} > 0$, and on $\{1, \dots, N\}$ put $k_N(x, y) := \alpha\sqrt{N}\,\delta_{xy} + 1$. Then $k_N = \alpha\sqrt{N} I_N + \mathbf{1}\mathbf{1}^T$ is strictly positive and strictly positive definite, with eigenvalues $\alpha\sqrt{N} + N$ (multiplicity $1$) and $\alpha\sqrt{N}$ (multiplicity $N - 1$). Direct computation gives:
  $$Z_N = (\alpha\sqrt{N} + N)^2 + (N - 1)\alpha^2 N = N^2\bigl(1 + \alpha^2 + O(N^{-1/2})\bigr),$$
  $$\operatorname{Tr}(k_N^4) = (\alpha\sqrt{N} + N)^4 + (N - 1)\alpha^4 N^2 = N^4\bigl(1 + O(N^{-1/2})\bigr),$$
  so $P(k_N) \to (1 + \alpha^2)^{-2} = (1 - t)^2$ as $N \to \infty$. By symmetry $\rho(x) = 1/N$, $p_x(x) = \frac{(\alpha\sqrt{N}+1)^2}{(\alpha\sqrt{N}+1)^2 + N - 1} \to t$, and $p_x(y) = \frac{1}{(\alpha\sqrt{N}+1)^2 + N - 1} \sim \frac{1 - t}{N}$ for $y \neq x$. Hence for $x \neq x'$:
  $$\operatorname{Aff}(p_x, p_{x'}) = 2\sqrt{p_x(x) p_x(x')} + (N - 2) p_x(x') \to 1 - t, \qquad d_{\mathrm{TV}}(p_x, p_{x'}) = p_x(x) - p_x(x') \to t,$$
  giving $H_{\mathrm{two}}^2 \to t = 1 - \sqrt{P}$ and $d_{\mathrm{TV}}^{\mathrm{two}} \to t = 1 - \sqrt{P}$. Likewise
  $$\operatorname{Aff}(p, m) = N\sqrt{\frac{p_x(x)}{N^3}} + N(N - 1)\sqrt{\frac{p_x(x')}{N^3}} \to \sqrt{1 - t} = P^{1/4},$$
  giving $H^2(p, m) \to 1 - P^{1/4}$. Since $t \in (0, 1)$ is arbitrary, $(1 - t)^2$ sweeps all of $(0, 1)$.
- *Witness B (near-diagonal $2 \times 2$ kernel):* Fix $q \in [1/2, 1)$ and let $k_\delta := \operatorname{diag}(\sqrt{q}, \sqrt{1 - q}) + \delta \mathbf{1}\mathbf{1}^T$ ($\delta > 0$). Then $k_\delta \in \mathcal{F}_+$ is strictly positive and strictly PD, and as $\delta \downarrow 0$, $P(k_\delta) \to q^2 + (1 - q)^2 \in [1/2, 1)$ while $H_{\mathrm{two}}^2(k_\delta) \to 2q(1 - q) = 1 - P$.
- *Witness C (weakly perturbed $2 \times 2$ kernel):* For $\varepsilon \in (0, 1)$, let $k_\varepsilon := \begin{pmatrix} 1 & 1 - \varepsilon \\ 1 - \varepsilon & 1 \end{pmatrix} \in \mathcal{F}_+$ (eigenvalues $2 - \varepsilon > \varepsilon > 0$). Then $\rho = (1/2, 1/2)$, $p_1(1) - p_2(1) = \frac{1 - (1 - \varepsilon)^2}{1 + (1 - \varepsilon)^2} = \varepsilon + O(\varepsilon^2)$, so $\beta_{\mathrm{mix}} = d_{\mathrm{TV}}^{\mathrm{two}} = \frac{1}{2}\varepsilon + O(\varepsilon^2)$, while $P = \frac{(2 - \varepsilon)^4 + \varepsilon^4}{((2 - \varepsilon)^2 + \varepsilon^2)^2} = 1 - \frac{1}{2}\varepsilon^2 + O(\varepsilon^3)$. Hence $d_{\mathrm{TV}}^{\mathrm{two}}/\sqrt{1 - P} \to 1/\sqrt{2}$ and $\beta_{\mathrm{mix}}/\sqrt{1 - P} \to 1/\sqrt{2}$ as $\varepsilon \downarrow 0$. $\square$

---

### 2.3 Theorem 1B (Exact logical equivalence to `(PUR-io)` on the calibrated trajectory $\beta_K$) — `PROVED`

Fix the release witnesses of check 1453 (`ON FILE`, row 1453): the odd block factor $b \ge 3$ and calibration level $g_0 \in (0, \delta)$. Note that the calibrated bare inverse coupling $\beta_K = g_K^{-2}$ depends only on $(b, g_0, K)$ and is **independent of the physical spatial side $\ell$** (`ON FILE`, check 1453, row 1468 §3.1). For any $\ell \in \mathbb{N}_{>0}$ and integer $v \ge 1$ dividing $n_K := \ell b^K$, write $d_{\mathrm{TV}}^{\mathrm{two}}(v; \ell, \beta_K)$, $\beta_{\mathrm{mix}}(v; \ell, \beta_K)$, $H_{\mathrm{two}}^2(v; \ell, \beta_K)$, $H^2(p, m)(v; \ell, \beta_K)$, and $P(2v; \ell, \beta_K) := Z_+(4v; n_K^3; \beta_K)/Z_+(2v; n_K^3; \beta_K)^2$ for the quantities of Theorem 1A applied to $A = P_0 T_{n_K, \beta_K}^v$.

**Theorem 1B (`PROVED` given checked rows 705/707 `B3` and `SH`, rows 1368/1370 `Theorem 4`/`Corollary 5`, and check 1527 `Theorem 2` & `Handoff`).** *Fix $(b, g_0)$ as above. The following five statements are logically equivalent (and pass on the exact same infinite set $E \subset \mathbb{N}_{\ge 1}$ of cutoffs $K$, up to replacing $\ell$ by a fixed dyadic multiple $2^{j+8}\ell$ independent of $K$):*

1. **`(PUR-io)`:** *There exist $\ell \in 1024\mathbb{N}_{>0}$ and an infinite set $E \subset \mathbb{N}_{\ge 1}$ such that $P(n_K/512; \ell, \beta_K) \ge 457/625$ for all $K \in E$.*
2. **`(W-mix-TV-512)`:** *There exist $\ell \in 1024\mathbb{N}_{>0}$ and an infinite set $E \subset \mathbb{N}_{\ge 1}$ such that $d_{\mathrm{TV}}^{\mathrm{two}}(n_K/1024; \ell, \beta_K) \le 1 - \frac{\sqrt{457}}{25}$ for all $K \in E$.*
3. **`(W-mix-TV-all)`:** *There exists an infinite set $E \subset \mathbb{N}_{\ge 1}$ such that for **every** $\eta > 0$ there exists $\ell_\eta \in 1024\mathbb{N}_{>0}$ with $d_{\mathrm{TV}}^{\mathrm{two}}(n_K/1024; \ell_\eta, \beta_K) \le \eta$ for all $K \in E$.*
4. **`(W-mix-TV-any)`:** *There exist $\varepsilon \in (0, 1/2)$, an even integer $A \ge 2\lceil \log(10^6)/\log(1 + \sqrt{2\varepsilon})\rceil$, a side $\ell \in 4A\mathbb{N}_{>0}$, and an infinite set $E \subset \mathbb{N}_{\ge 1}$ such that $d_{\mathrm{TV}}^{\mathrm{two}}(n_K/(2A); \ell, \beta_K) \le 1 - \sqrt{\frac{1}{2} + \varepsilon}$ for all $K \in E$.*
5. *The exact counterparts of (2), (3), (4) obtained by replacing $d_{\mathrm{TV}}^{\mathrm{two}}$ with $H_{\mathrm{two}}^2$ (same thresholds), or with $\beta_{\mathrm{mix}}$ or $H^2(p, m)$ (with thresholds $1 - (457/625)^{1/4}$ in (2) and $1 - (\frac{1}{2} + \varepsilon)^{1/4}$ in (4), and arbitrary $\eta > 0$ in (3)).*

**Proof (`PROVED` from the cited checked results).**
We verify `(3) => (2) => (1) => (3)` and `(1) => (4) => (1)` (and the simultaneous equivalences in `(5)`).

- **`(3) => (2)`:** Take $\eta = 1 - \frac{\sqrt{457}}{25} > 0$ (and $\eta = 1 - (457/625)^{1/4} > 0$ for $\beta_{\mathrm{mix}}, H^2(p, m)$).
- **`(2) => (1)`:** Immediate from Theorem 1A (T1.1)–(T1.4): $d_{\mathrm{TV}}^{\mathrm{two}} \le 1 - \frac{\sqrt{457}}{25}$ (or $H_{\mathrm{two}}^2 \le 1 - \frac{\sqrt{457}}{25}$) implies $P \ge (1 - d_{\mathrm{TV}}^{\mathrm{two}})^2 \ge 457/625$; $\beta_{\mathrm{mix}} \le 1 - (457/625)^{1/4}$ (or $H^2(p, m) \le 1 - (457/625)^{1/4}$) implies $P \ge (1 - \beta_{\mathrm{mix}})^4 \ge 457/625$.
- **`(1) => (4)`:** Take $\varepsilon = 457/625 - 1/2 = 289/1250$ (so $\sqrt{2\varepsilon} = 17/25$ and $1 + \sqrt{2\varepsilon} = 42/25$). Since $(42/25)^2 > (3/2)^2 = 9/4 > 2$, we have $(42/25)^{256} > 2^{128} > 10^6$, so $A = 512 \ge 2\lceil \log(10^6)/\log(42/25)\rceil$ is admissible. Applying `(1) => (3)` below with $\eta = 1 - \frac{\sqrt{457}}{25}$ (and $1 - (457/625)^{1/4}$ for $\beta_{\mathrm{mix}}, H^2(p, m)$) produces $\ell_\eta = 2^{j(\eta)+8}\ell$ with $j(\eta) \ge 8$, so $2^{26} \mid \ell_\eta$; in particular $\ell_\eta \in 2048\mathbb{N}_{>0} = 4A\mathbb{N}_{>0}$, giving `(4)` and `(5)`.
- **`(4) => (1)`:** Let $K \in E$, $n_K = \ell b^K$, $u_K = n_K / A$, $v_K = u_K / 2 = n_K / (2A)$. Since $\ell \in 4A\mathbb{N}_{>0}$ and $b \ge 3$, $4 \mid n_K$, $v_K \ge 2 b^K \ge 6$, and $u_K \ge 12 \ge 3$. By Theorem 1A (T1.1)–(T1.4), the hypothesis in `(4)` (or its counterpart in `(5)`) implies $P(u_K; \ell, \beta_K) \ge \frac{1}{2} + \varepsilon$ for all $K \in E$. By check 1527 `Theorem 2(1)–(2)` (`ON FILE`, lines 47–51, invoking checked `Theorem 4` of row 1368/1370 and `Proposition B3` of row 705/707), this yields the Pfaffian excited sum bound
  $$S_\kappa(n_K/2; (2n_K)^3; \beta_K) < \frac{1}{25} \qquad (\forall K \in E). \tag{T1.5}$$
  Now apply the spatial enlargement chain constructed in `(1) => (3)` below with $\eta = 1 - \frac{\sqrt{457}}{25}$ (or any $\eta \in (0, 1 - \frac{\sqrt{457}}{25})$): it produces a fixed integer $j \ge 8$ (independent of $K$) such that on side $N_K = 2^{j+8} n_K = \ell' b^K$ with $\ell' = 2^{j+8}\ell$ (note $2 \mid A \implies 8 \mid \ell \implies 1024 \mid 2^{j+8}\ell$), $P(N_K/512; \ell', \beta_K) \ge 1 - \eta^2 > 457/625$ for all $K \in E$, which is `(PUR-io)` on the same infinite set $E$.
- **`(1) => (3)` (and `(5)`):** Assume `(PUR-io)` holds at $\ell \in 1024\mathbb{N}_{>0}$ for all $K \in E \subset \mathbb{N}_{\ge 1}$. For each $K \in E$, $n_K = \ell b^K$ satisfies $4 \mid n_K$ and $u_K = n_K / 512 = (\ell/512) b^K \ge 6 \ge 3$.
  - *Step 1 (`Fact PUR`, checked in check 1527 `Theorem 2(1)`):* Writing $x_i = (\lambda_i/\lambda_0)^{u_K} \in [0, 1]$ ($i \ge 1$) for the excited spectrum of $P_0 T_{n_K, \beta_K}^{u_K} / \lambda_0^{u_K}$ and $s_+ := \sum_{i \ge 1} x_i$, we have $\sum x_i^2 \le \min(s_+, s_+^2)$. If $s_+ \ge 1$ then $P \le (1 + s_+)^{-1} \le 1/2 < 457/625$, impossible. Thus $s_+ < 1$ and $(1 + s_+^2)/(1 + s_+)^2 \ge 457/625 \iff (21 s_+ - 4)(4 s_+ - 21) \ge 0$, forcing $s_+(u_K; n_K^3; \beta_K) \le 4/21$.
  - *Step 2 (From aspect $512$ to the Pfaffian seed at $r = 4$):* Since $A = 512$ is even and $512 \ge 2\lceil \log(10^6)/\log(42/25)\rceil$ (checked above), check 1527 `Theorem 2(2)` (`ON FILE`, lines 49–51) yields (T1.5): $S_\kappa(n_K/2; (2n_K)^3; \beta_K) < 1/25$ for all $K \in E$.
  - *Step 3 (`Theorem SH` at $r = 4$, `ON FILE`, row 705 `gap-seed-shape.md` line 123, checked row 707 and check 1370 line 104):* Starting from $(a_0, B_0) = (n_K/2, (2n_K)^3)$ with $a_0 \ge 512 \ge 3$, $B_0/a_0 = 4$, and $S_\kappa(a_0; B_0; \beta_K) < 1/25$, iterate $j \ge 2$ steps of `Theorem SH` with $(2, 2, 3)$ and $K_{\mathrm{SH}} = 22.2$. At side $B_j := 2^{j+1} n_K$ and time $a_j := B_j / 4 = 2^{j-1} n_K$,
    $$s_j := S_\kappa(a_j; B_j^3; \beta_K) \le \frac{1}{22.2}\left(\frac{22.2}{25}\right)^{2^j}.$$
  - *Step 4 (`Proposition B3` spatial enlargement at fixed time, `ON FILE`, row 705 line 76, checked row 707 and check 1527 line 53):* Enlarge the spatial cube from $B_j^3$ to $N_K^3 := (128 B_j)^3 = (2^{j+8} n_K)^3$ at the fixed time $U_K := a_j = 2^{j-1} n_K = N_K / 512$, applying `(B3-q)` with $p = q = 1$ and $a = U_K \ge 3$ (clearly $U_K = B_j/4 < B_j$). Here $\beta_i = B_j/(B_j - B_j/4) = 4/3$, $\Pi = (4/3)^3$, and $|H|/|B| = 128^3$, so
    $$\log\!\bigl(1 + S_\kappa(U_K; N_K^3; \beta_K)\bigr) \le \left(\frac{512}{3}\right)^3 \log(1 + s_j) \le \left(\frac{512}{3}\right)^3 s_j =: X_j.$$
    Since $512/3 < 171$, $171^3 = 5{,}000{,}211$, and $22 \cdot 2^{18} = 5{,}767{,}168 > 5{,}000{,}211$, we have $(512/3)^3/22.2 < 2^{18}$. Moreover $22.2/25 = 111/125 < 9/10$ and $(9/10)^7 = 4{,}782{,}969 / 10^7 < 1/2$, so for every $j \ge 2$,
    $$X_j \le 2^{18}\left(\frac{9}{10}\right)^{2^j} \le 2^{18} \cdot 2^{-\lfloor 2^j / 7 \rfloor} \le 2^{18 - (2^j - 6)/7} = 2^{(132 - 2^j)/7}.$$
  - *Step 5 (Explicit $j(\eta)$ and return to mixing):* Given any $\eta \in (0, 1]$, set
    $$j(\eta) := \left\lceil \log_2\!\bigl(146 + 14\lceil \log_2(1/\eta)\rceil\bigr) \right\rceil \ge 8, \qquad \ell_\eta := 2^{j(\eta)+8}\ell \in 1024\mathbb{N}_{>0}.$$
    Then $(132 - 2^{j(\eta)})/7 \le -2 - 2\lceil \log_2(1/\eta)\rceil \le \log_2(\eta^2/4)$, so $X_{j(\eta)} \le \eta^2 / 4 \le 1/4$. Since $e^x - 1 \le 2x$ on $[0, 1/4]$ and $s_+(U_K; N_K^3; \beta_K) \le S_\kappa(U_K; N_K^3; \beta_K)$ (neutral sector is contained in the Pfaffian transfer with the same simple top eigenvalue; `ON FILE`, check 1370 line 102), we obtain
    $$s_+(U_K; N_K^3; \beta_K) \le e^{X_{j(\eta)}} - 1 \le 2 X_{j(\eta)} \le \frac{\eta^2}{2} \qquad (\forall K \in E).$$
    Since $(1 + s)^{-2} \ge 1 - 2s$ for all $s \ge 0$ (as $(1 - 2s)(1 + s)^2 = 1 - 3s^2 - 2s^3 \le 1$),
    $$P(U_K; \ell_\eta, \beta_K) \ge \frac{1}{(1 + s_+)^2} \ge 1 - 2 s_+ \ge 1 - \eta^2 \qquad (\forall K \in E).$$
    Finally, note $V_K := U_K / 2 = 2^{j(\eta)-2} n_K = N_K / 1024 \in \mathbb{N}_{>0}$. Applying Theorem 1A (T1.1)–(T1.4) yields, for all $K \in E$:
    $$d_{\mathrm{TV}}^{\mathrm{two}}(V_K; \ell_\eta, \beta_K) \le \eta, \qquad \beta_{\mathrm{mix}}(V_K; \ell_\eta, \beta_K) \le \eta, \qquad H_{\mathrm{two}}^2(V_K; \ell_\eta, \beta_K) \le \eta^2 \le \eta, \qquad H^2(p, m)(V_K; \ell_\eta, \beta_K) \le \eta^2 \le \eta.$$
    Note that $\ell_\eta$ is independent of $K$, and every implication passes on the exact same infinite set $E$. $\square$

**Obstruction reading (`PROVED`).** By the lane's rule (*"Equivalent is not progress"*), **no bounded total-variation, $\beta$-mixing, Hellinger, or affinity formulation of `(W-mix)` across the half-cylinder is strictly weaker than `(PUR-io)`**: proving any one of them at any admissible aspect and threshold on $\beta_K$ is logically equivalent to proving `(PUR-io)` itself, and conversely `(PUR-io)` already forces all four quantities below any $\eta > 0$ at one fixed rescaled side $\ell_\eta$.

---

## 3. Theorem 2: Complete $f$-Divergence Trichotomy on $\mathcal{F}_+$ and Sharper Mutual-Information Consumer

Let $f : (0, \infty) \to \mathbb{R}$ be convex with $f(1) = 0$. Pick any subgradient $c \in \partial f(1)$ and set $\tilde{f}(t) := f(t) - c(t - 1) \ge 0$ for $t > 0$, with boundary limits
$$
M_0(f) := \tilde{f}(0) := \lim_{t \downarrow 0} \tilde{f}(t) \in [0, \infty], \qquad M_\infty(f) := \lim_{t \to \infty} \frac{\tilde{f}(t)}{t} \in [0, \infty], \qquad M(f) := M_0(f) + M_\infty(f) \in [0, \infty].
$$
(Both limits exist in $[0, \infty]$ by convexity of $\tilde{f}$ and $\tilde{f}(1) = 0$.) Assume $f$ is **non-degenerate at $1$**, i.e., $f$ is not affine on any open interval containing $1$. Define the modulus
$$
\phi_f(\delta) := \tilde{f}(1 + \delta) + \tilde{f}(1 - \delta) \qquad (\delta \in [0, 1]).
$$
For any two probability measures $P, Q$ with common dominating measure $\nu$ and densities $p, q$, recall the Csiszár $f$-divergence $D_f(P \| Q) := \int q\,\tilde{f}(p/q)\,d\nu \in [0, \infty]$ (with standard conventions $0 \cdot \tilde{f}(0/0) = 0$ and $0 \cdot \tilde{f}(a/0) = a M_\infty(f)$ for $a > 0$, independent of $c \in \partial f(1)$). For $A \in \mathcal{F}_+$, put
$$
D_f^{\mathrm{two}}(A) := \mathbb{E}_{x, x' \sim \rho \otimes \rho}\!\left[D_f(p_x \| p_{x'})\right], \qquad D_f^{\mathrm{joint}}(A) := D_f(p \| m).
$$

**Theorem 2 (Complete $f$-divergence trichotomy on $\mathcal{F}_+$; `PROVED`).** *Let $f : (0, \infty) \to \mathbb{R}$ be convex with $f(1) = 0$ and non-degenerate at $1$.*

1. *(Universal sufficiency via $\phi_f$):* *The modulus $\phi_f : [0, 1] \to [0, \infty]$ is convex, strictly increasing, with $\phi_f(0) = 0$ and $\phi_f(\delta) > 0$ for all $\delta \in (0, 1]$. For every pair of probability measures $P, Q$, $D_f(P \| Q) \ge \phi_f(d_{\mathrm{TV}}(P, Q))$. Consequently, for every $A \in \mathcal{F}_+$:*
   $$D_f^{\mathrm{two}}(A) \;\ge\; \phi_f\!\bigl(d_{\mathrm{TV}}^{\mathrm{two}}(A)\bigr) \;\ge\; \phi_f\!\bigl(1 - \sqrt{P}\bigr), \qquad D_f^{\mathrm{joint}}(A) \;\ge\; \phi_f\!\bigl(\beta_{\mathrm{mix}}(A)\bigr) \;\ge\; \phi_f\!\bigl(1 - P^{1/4}\bigr). \tag{T2.1}$$
2. *(Bounded $f$-divergences, $M(f) < \infty$ — **exact equivalence to `(PUR-io)`**):* *If $M(f) < \infty$ (including total variation, squared Hellinger, Jensen–Shannon with $M = \log 2$, triangular discrimination with $M = 2$, and Hellinger-$\alpha$ divergences for $\alpha \in (0, 1)$), then for every $P, Q$, $D_f(P \| Q) \le M(f)\,d_{\mathrm{TV}}(P, Q)$. Consequently, for every $A \in \mathcal{F}_+$:*
   $$\phi_f\!\bigl(1 - \sqrt{P}\bigr) \;\le\; D_f^{\mathrm{two}}(A) \;\le\; M(f)\sqrt{1 - P}, \qquad \phi_f\!\bigl(1 - P^{1/4}\bigr) \;\le\; D_f^{\mathrm{joint}}(A) \;\le\; M(f)\sqrt{1 - P}. \tag{T2.2}$$
   *Therefore, on the calibrated trajectory $\beta_K$, every bounded $f$-divergence cylinder mixing criterion ($D_f^{\mathrm{two}} \le \tau$ or $D_f^{\mathrm{joint}} \le \tau$ for any $\tau$ forcing $P > 1/2$ at the corresponding aspect, or for all $\eta > 0$ at rescaled sides $\ell_\eta$) is **logically equivalent to `(PUR-io)`**.*
3. *(Unbounded $f$-divergences, $M(f) = \infty$ — **strictly stronger than $P$ on $\mathcal{F}_+$**):* *If $M(f) = \infty$ (including Shannon mutual information $I(X; Y) = D_{\mathrm{KL}}(p \| m)$, Lautum information $L(X; Y) = D_{\mathrm{KL}}(m \| p)$, the symmetric exchange cost $I + L$ of `Lemma JI` / row 1573 (3), $\chi^2$-divergence, and Rényi-$\alpha$ divergences for $\alpha > 1$), then there exists a sequence of strictly positive, strictly positive definite finite-dimensional kernels $A_r \in \mathcal{F}_+$ such that*
   $$P(A_r) \longrightarrow 1, \qquad D_f^{\mathrm{joint}}(A_r) \longrightarrow +\infty, \qquad \text{and} \qquad D_f^{\mathrm{two}}(A_r) \longrightarrow +\infty \qquad (r \to \infty). \tag{T2.3}$$
4. *(Sharper mutual-information consumer dropping Lautum $L$):* *For every $A \in \mathcal{F}_+$ with mutual information $I(X; Y) := D_{\mathrm{KL}}(p \| m)$ and Lautum information $L(X; Y) := D_{\mathrm{KL}}(m \| p)$,*
   $$-\log P \;\le\; 2\min\bigl(I(X; Y),\; L(X; Y)\bigr) \;\le\; I(X; Y) + L(X; Y). \tag{T2.4}$$
   *This strictly improves row 1573 identity (3) ($-\log P \le I + L$): on the strictly positive PD family $k_c = \begin{pmatrix} 1 & \delta(c) \\ \delta(c) & c \end{pmatrix}$ with $0 < \delta(c) = c e^{-1/c^3} \ll c \downarrow 0$, we have $P \to 1$ and $I(X; Y) \to 0$ while $L(X; Y) \to +\infty$ (hence $I + L \to +\infty$). Thus on $\mathcal{F}_+$, $I(X; Y)$ is strictly weaker than $I + L$ yet still strictly stronger than $P$.*

**Proof (`PROVED`).**
*(1)* Since $\tilde{f} \ge 0$ is convex with $\tilde{f}(1) = 0$, $\phi_f(\delta) = \tilde{f}(1 + \delta) + \tilde{f}(1 - \delta)$ is convex on $[0, 1]$ with $\phi_f(0) = 0$. If $\phi_f(\delta) = 0$ for some $\delta > 0$, then $\tilde{f}(1 + \delta) = \tilde{f}(1 - \delta) = 0$, and convexity forces $\tilde{f} \equiv 0$ on $[1 - \delta, 1 + \delta]$, contradicting non-degeneracy of $f$ at $1$. Hence $\phi_f(\delta) > 0$ for all $\delta \in (0, 1]$; by convexity and $\phi_f(0) = 0$, for $0 \le \delta_1 < \delta_2 \le 1$ we have $\phi_f(\delta_1) \le \frac{\delta_1}{\delta_2}\phi_f(\delta_2) < \phi_f(\delta_2)$, so $\phi_f$ is strictly increasing.

Now let $P, Q$ have densities $p, q$ with respect to $\nu$, put $E := \{p > q\}$, $a := P(E)$, $b := Q(E)$, and $\delta := d_{\mathrm{TV}}(P, Q) = a - b \in [0, 1]$ (so $b \in [0, 1 - \delta]$). By the data-processing inequality (Jensen's inequality on the two-cell partition $\{E, E^c\}$),
$$D_f(P \| Q) \ge b\,\tilde{f}\!\left(1 + \frac{\delta}{b}\right) + (1 - b)\,\tilde{f}\!\left(1 - \frac{\delta}{1 - b}\right).$$
For $b \in (0, 1]$, writing $1 + \delta = b(1 + \delta/b) + (1 - b)\cdot 1$ and applying convexity of $\tilde{f}$ with $\tilde{f}(1) = 0$ gives $\tilde{f}(1 + \delta) \le b\,\tilde{f}(1 + \delta/b)$; at $b = 0$, the left term is $\delta M_\infty(f) \ge \tilde{f}(1 + \delta)$ because $s \mapsto \tilde{f}(1 + s)/s$ is nondecreasing on $(0, \infty)$. Symmetrically, for $1 - b \in (0, 1]$, $1 - \delta = (1 - b)(1 - \delta/(1 - b)) + b \cdot 1$ gives $\tilde{f}(1 - \delta) \le (1 - b)\,\tilde{f}(1 - \delta/(1 - b))$ (and at $1 - b = \delta$, $\delta\tilde{f}(0) \ge \tilde{f}(1 - \delta)$). Adding the two bounds gives $D_f(P \| Q) \ge \tilde{f}(1 + \delta) + \tilde{f}(1 - \delta) = \phi_f(\delta)$. Applying this to $(p_x, p_{x'})$ and $(p, m)$, using Jensen on convex increasing $\phi_f$, and invoking Theorem 1A (T1.2), (T1.4) yields (T2.1).

*(2)* Suppose $M(f) = \tilde{f}(0) + M_\infty(f) < \infty$. For $t \in [0, 1]$, convexity and $\tilde{f}(1) = 0$ give $\tilde{f}(t) \le (1 - t)\tilde{f}(0) = M_0(f)(1 - t)_+$. For $t \ge 1$, monotonicity of $s \mapsto \tilde{f}(1 + s)/s$ gives $\tilde{f}(t) \le M_\infty(f)(t - 1)_+$. Hence pointwise (including on $\{q = 0\}$, where $0 \cdot \tilde{f}(p/0) = M_\infty(f) p = M_\infty(f)(p - q)_+$),
$$q\,\tilde{f}\!\left(\frac{p}{q}\right) \le M_0(f)(q - p)_+ + M_\infty(f)(p - q)_+.$$
Integrating against $\nu$ and using $\int (q - p)_+\,d\nu = \int (p - q)_+\,d\nu = d_{\mathrm{TV}}(P, Q)$ gives $D_f(P \| Q) \le M(f)\,d_{\mathrm{TV}}(P, Q)$. Combining with (T2.1) and Theorem 1A gives (T2.2), and the calibrated-trajectory equivalence to `(PUR-io)` follows immediately from Theorem 1B (with $\eta$ replaced by $\eta / M(f)$ in `(3)` and $\phi_f^{-1}(\tau)$ in `(2)` and `(4)`).

*(3)* Since $M(f) = M_0(f) + M_\infty(f) = \infty$, at least one of $M_0(f) = \infty$ or $M_\infty(f) = \infty$ holds.

- *Case A ($M_0(f) = \tilde{f}(0) = \infty$):* For $0 < \delta < c < 1/2$, define the $2 \times 2$ kernel on $\{1, 2\}$ (counting measure)
  $$k_{c, \delta} := \begin{pmatrix} 1 & \delta \\ \delta & c \end{pmatrix}.$$
  Since $\det k_{c, \delta} = c - \delta^2 > c - c^2 > 0$ and $\operatorname{tr} k_{c, \delta} = 1 + c > 0$, $k_{c, \delta}$ is strictly positive and strictly positive definite ($k_{c, \delta} \in \mathcal{F}_+$). Here $Z = 1 + 2\delta^2 + c^2 \in (1, 1 + 3c^2) \subset (1, 2)$, $\rho_1 = (1 + \delta^2)/Z \ge 1/2$, $\rho_2 = (\delta^2 + c^2)/Z \in [c^2/2, 2c^2]$, and
  $$P(k_{c, \delta}) \ge \frac{k_2(1, 1)^2}{Z^2} = \frac{(1 + \delta^2)^2}{(1 + 2\delta^2 + c^2)^2} \ge \frac{1}{(1 + 3c^2)^2} \longrightarrow 1 \qquad (c \downarrow 0).$$
  Meanwhile $p_{12} = \delta^2 / Z$, $m_{12} = \rho_1 \rho_2 \ge c^2 / 4$, and
  $$\frac{p_{12}}{m_{12}} = \frac{\delta^2 Z}{(1 + \delta^2)(\delta^2 + c^2)} \le \frac{2\delta^2}{c^2} < 1 \qquad \text{for } \delta < \frac{c}{2}.$$
  Similarly, $p_2(2) = c^2/(\delta^2 + c^2) \ge 1/2$ and $p_1(2)/p_2(2) = \frac{\delta^2(\delta^2 + c^2)}{c^2(1 + \delta^2)} \le 2\delta^2 \le \frac{2\delta^2}{c^2}$. Since $\tilde{f} \ge 0$ is nonincreasing on $(0, 1]$, keeping only $(1, 2)$ and $(2, 1)$ in $D_f(p \| m)$, and only $(x, x') = (1, 2)$ at $y = 2$ in $D_f^{\mathrm{two}}$, yields
  $$D_f^{\mathrm{joint}}(k_{c, \delta}) \ge 2 m_{12}\,\tilde{f}\!\left(\frac{p_{12}}{m_{12}}\right) \ge \frac{c^2}{2}\,\tilde{f}\!\left(\frac{2\delta^2}{c^2}\right), \qquad D_f^{\mathrm{two}}(k_{c, \delta}) \ge \rho_1\rho_2\,p_2(2)\,\tilde{f}\!\left(\frac{p_1(2)}{p_2(2)}\right) \ge \frac{c^2}{8}\,\tilde{f}\!\left(\frac{2\delta^2}{c^2}\right).$$
  Because $\lim_{t \downarrow 0} \tilde{f}(t) = \infty$, for each $c_r = 1/(2r + 2)$ choose $\delta_r \in (0, c_r/2)$ with $\tilde{f}(2\delta_r^2/c_r^2) \ge 8/c_r^3$. Then $P \to 1$ while $D_f^{\mathrm{joint}} \ge 4/c_r \to \infty$ and $D_f^{\mathrm{two}} \ge 1/c_r \to \infty$.

- *Case B ($M_\infty(f) = \infty$):* For $\delta \in (0, 1/4)$, integer $M \ge 3$, and $0 < \varepsilon \le \frac{\delta}{8 M (M + 1)^2}$, define the $(M + 1) \times (M + 1)$ kernel on $\{0, 1, \dots, M\}$ (counting measure)
  $$k_{\delta, M, \varepsilon} := \operatorname{diag}\!\left(\sqrt{1 - \delta},\; \sqrt{\frac{\delta}{M}},\; \dots,\; \sqrt{\frac{\delta}{M}}\right) + \varepsilon \mathbf{1}\mathbf{1}^T.$$
  It is strictly positive and strictly positive definite ($k_{\delta, M, \varepsilon} \in \mathcal{F}_+$). Bounding the perturbation terms using $3(M + 1)\varepsilon + M(M + 1)\varepsilon^2 \le \frac{\delta}{2M} \le \frac{1}{8}$ gives $1 \le Z \le \frac{9}{8}$, $\rho_0 \ge \frac{1 - \delta}{9/8} \ge \frac{2}{3}$, and for every $i \in \{1, \dots, M\}$:
  $$p_{ii} = \frac{(\sqrt{\delta/M} + \varepsilon)^2}{Z} \ge \frac{8\delta}{9M}, \qquad \frac{8\delta}{9M} \le \rho_i \le \frac{\delta}{M} + 4\varepsilon \le \frac{3\delta}{2M}.$$
  Hence $P \ge \frac{k_2(0, 0)^2}{Z^2} \ge \frac{(1 - \delta)^2}{(1 + \delta/(2M))^2} \ge (1 - 2\delta)^2 \to 1$ as $\delta \downarrow 0$. Meanwhile, for each $i \in \{1, \dots, M\}$:
  $$\frac{p_{ii}}{m_{ii}} = \frac{p_{ii}}{\rho_i^2} \ge \frac{8\delta/(9M)}{9\delta^2/(4M^2)} = \frac{32 M}{81\delta} \ge \frac{M}{3\delta} > 1,$$
  and $p_i(i) = p_{ii}/\rho_i \ge \frac{16}{27} > \frac{1}{2}$, $p_0(i) = \varepsilon^2/(Z\rho_0) \le \frac{3}{2}\varepsilon^2$, so $\frac{p_i(i)}{p_0(i)} \ge \frac{1}{3\varepsilon^2} \ge \frac{M}{3\delta}$. Since $\tilde{f} \ge 0$ and $t \mapsto \tilde{f}(t)/t$ is nondecreasing on $[1, \infty)$ (for $1 \le t_1 < t_2$, $\frac{\tilde{f}(t_1)}{t_1} = \frac{t_1 - 1}{t_1}\frac{\tilde{f}(t_1)}{t_1 - 1} \le \frac{t_2 - 1}{t_2}\frac{\tilde{f}(t_2)}{t_2 - 1} = \frac{\tilde{f}(t_2)}{t_2}$), keeping only the $M$ diagonal terms $i = 1, \dots, M$ in $D_f^{\mathrm{joint}}$ and the $M$ pairs $(x, x') = (i, 0)$ at $y = i$ in $D_f^{\mathrm{two}}$ gives
  $$D_f^{\mathrm{joint}} \ge \sum_{i=1}^M p_{ii}\,\frac{\tilde{f}(p_{ii}/m_{ii})}{p_{ii}/m_{ii}} \ge \frac{8\delta}{9}\,\frac{\tilde{f}(M/(3\delta))}{M/(3\delta)}, \qquad D_f^{\mathrm{two}} \ge \sum_{i=1}^M \rho_i\rho_0\,p_i(i)\,\frac{\tilde{f}(p_i(i)/p_0(i))}{p_i(i)/p_0(i)} \ge \frac{8\delta}{27}\,\frac{\tilde{f}(M/(3\delta))}{M/(3\delta)}.$$
  Because $M_\infty(f) = \infty$, for $\delta_r = 1/(4r + 4)$ choose $M_r \ge 3$ with $\frac{\tilde{f}(M_r/(3\delta_r))}{M_r/(3\delta_r)} \ge \frac{4}{\delta_r^2}$ and $\varepsilon_r = \frac{\delta_r}{8 M_r(M_r + 1)^2}$. Then $P \to 1$ while $D_f^{\mathrm{joint}} \to \infty$ and $D_f^{\mathrm{two}} \to \infty$.

*(4)* By Theorem 1A (T1.3), $P \ge \operatorname{Aff}(p, m)^4$, so $-\log P \le -4\log \operatorname{Aff}(p, m)$. If $I(X; Y) < \infty$, then $p \ll m$, and Jensen's inequality for the convex function $t \mapsto e^{-t/2}$ yields
$$\operatorname{Aff}(p, m) = \int_{\{p > 0\}} p\,\exp\!\left(-\frac{1}{2}\log\frac{p}{m}\right) d(\mu_0 \otimes \mu_0) \ge \exp\!\left(-\frac{1}{2}\int_{\{p > 0\}} p\log\frac{p}{m}\right) = e^{-I(X; Y)/2}.$$
Symmetrically, if $L(X; Y) < \infty$, then $m \ll p$ and $\operatorname{Aff}(p, m) = \mathbb{E}_m[\exp(-\frac{1}{2}\log(m/p))] \ge e^{-L(X; Y)/2}$. Taking $-4\log$ gives $-\log P \le 2\min(I(X; Y), L(X; Y)) \le I(X; Y) + L(X; Y)$ (since $2\min(a, b) \le a + b$).

For the strict separation of $I$ from $I + L$, evaluate on $k_{c, \delta}$ of Case A with $\delta = c e^{-1/c^3}$ ($c \in (0, 1/4)$):
- $p_{11}/m_{11} = Z/(1 + \delta^2)^2 \le 1 + c^2$, so $p_{11}\log(p_{11}/m_{11}) \le c^2$;
- $p_{12}/m_{12} < 1$, so $2 p_{12}\log(p_{12}/m_{12}) < 0$;
- $p_{22} \le c^2$ and $p_{22}/m_{22} \le c^2 Z / c^4 \le 2/c^2$, so $p_{22}\log(p_{22}/m_{22}) \le c^2\log(2/c^2)$.
Thus $0 \le I(X; Y) \le c^2(1 + \log(2/c^2)) \to 0$ as $c \downarrow 0$, whereas by Case A (for $\tilde{f}(t) = -\log t + t - 1$), $L(X; Y) \ge \frac{c^2}{2}\log\frac{c^2}{2\delta^2} - \frac{c^2}{2} = \frac{1}{c} - \frac{c^2}{2}(1 + \log 2) \to +\infty$. $\square$

**Contrast with the infinite-cylinder Doob chain (`ON FILE`, row 839 `gap-compress-opus.md` Identity I1 and Proposition K, checked in `gap-compress-check-astra.md`).** Row 839 proved that for two slices $(X_0, X_v)$ of the *infinite-cylinder* Doob chain (with ground-state marginal $\pi(dx) = \Omega(x)^2 dx$), Shannon mutual information $I^{\mathrm{Doob}}(X_0; X_v)$ does **not** control the thermal sum $S(2v)$ (Proposition K: a rare slow mode has tiny ground-state weight $\varepsilon$, making $I^{\mathrm{Doob}} \to 0$ while $S(2v) = \mu^{2v}$ stays $O(1)$), whereas $I_{\chi^2}^{\mathrm{Doob}}(X_0; X_v) = S(2v)$ exactly. Theorem 2 reveals the exact reversal on the **periodic-torus** two-slice law $p(x, y) = k_v^+(x, y)^2/Z_+(2v)$ where `(W-mix)` lives: because the torus marginal $\rho(x) = k_{2v}^+(x, x)/Z_+(2v)$ is *thermal* rather than ground-state, every slow excited mode receives full weight in $\rho$, so even bounded $f$-divergences (TV, Hellinger) control $P$ and are equivalent to `(PUR-io)`, while Shannon $I(X; Y)$ becomes **strictly stronger** than `(PUR-io)` on $\mathcal{F}_+$.

---

## 4. Theorem 3: Breakdown of One-Observable Weakening (`(H-two-N1)` / `Lemma TS3`) and Incomparability of $\rho_{\max}$

Because bounded $f$-divergence mixing in law (`(H-two)`, $\beta_{\mathrm{mix}}$) is equivalent to `(PUR-io)` (Theorems 1–2), a natural escape attempt — recorded on file as `(H-two-N1)` in check 1120 (`library/gap-resp-in-law-sheet-check-opus.md` §5.3, `ON FILE` row 1120) — is to weaken the supremum over events inside $\mathbb{E}_{x, x'} d_{\mathrm{TV}}(p_x, p_{x'})$ by pulling the supremum over bounded observables *outside* the expectation, or by replacing $d_{\mathrm{TV}}^{\mathrm{two}}$ with the maximal correlation $\rho_{\max}(p)$. Theorem 3 proves that this weakening fails completely: `(H-two-N1)` implies **no** positive lower bound on $P_K$, even inside local reflection-positive 4D lattice field theories.

For $A \in \mathcal{F}_+$ with two-slice law $p(x, y) = k(x, y)^2/Z$, marginal $\rho$, and Markov conditional expectation operator $(Q f)(x) := \mathbb{E}_{p_x}[f]$ on $L^2(\rho)$, define:
$$
\alpha_{\mathrm{N1}}^{\mathrm{two}}(A) := \sup_{\|f\|_\infty \le 1} \mathbb{E}_{x, x' \sim \rho \otimes \rho}\!\left|\mathbb{E}_{p_x}[f] - \mathbb{E}_{p_{x'}}[f]\right|, \qquad \alpha_{\mathrm{N1}}(A) := \sup_{\|f\|_\infty \le 1} \mathbb{E}_{x \sim \rho}\!\left|\mathbb{E}_{p_x}[f] - \mathbb{E}_\rho[f]\right|,
$$
$$
\rho_{\max}(A) := \sup\left\{\operatorname{Corr}_p(f(X), g(Y)) : f, g \in L^2(\rho),\; \operatorname{Var}_\rho(f) > 0,\; \operatorname{Var}_\rho(g) > 0\right\} = \|Q|_{\mathbf{1}^\perp}\|_{L^2(\rho) \to L^2(\rho)}.
$$

**Theorem 3 (`PROVED`).**
1. *(Universal upper bounds on $\mathcal{F}_+$):* For every $A \in \mathcal{F}_+$,
   $$\alpha_{\mathrm{N1}}(A) \;\le\; \alpha_{\mathrm{N1}}^{\mathrm{two}}(A) \;\le\; \min\!\left(2\alpha_{\mathrm{N1}}(A),\; 2 d_{\mathrm{TV}}^{\mathrm{two}}(A)\right), \qquad \alpha_{\mathrm{N1}}(A) \;\le\; \rho_{\max}(A), \qquad \alpha_{\mathrm{N1}}^{\mathrm{two}}(A) \;\le\; \min\!\left(2\rho_{\max}(A),\; 2\sqrt{1 - P(A)}\right). \tag{T3.1}$$
2. *(Strict insufficiency of `(H-two-N1)` and $\rho_{\max}$ on $\mathcal{F}_+$):* For every $\varepsilon \in (0, 1)$ and $\delta \in (0, 1)$, there exists a strictly positive, strictly positive definite finite-dimensional product kernel $A \in \mathcal{F}_+$ with
   $$\alpha_{\mathrm{N1}}^{\mathrm{two}}(A) \le 2\rho_{\max}(A) \le \delta \qquad \text{and} \qquad P(A) \le \varepsilon.$$
3. *(Realization inside 4D local reflection-positive lattice field theory):* Consider the 4D Euclidean massive free scalar field on the periodic lattice $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ ($u = 2v \ge 2$ even, $n = A u$ with integer aspect $A \ge 66$). Given any target $\varepsilon \in (0, 1)$, set $C := 108 e \log(1/\varepsilon) > 0$. For every $A \ge \max(66, \lceil C^{1/3}\rceil + 1)$ and every even $u \ge 2$, choosing the positive lattice mass $m := 2\sinh\!\bigl(\frac{3\log A - \log C}{2u}\bigr) > 0$ yields a local reflection-positive transfer operator $T^v \in \mathcal{F}_+$ satisfying
   $$\alpha_{\mathrm{N1}}^{\mathrm{two}}(T^v) \;\le\; 2\rho_{\max}(T^v) \;\le\; 4\sqrt{C}\,A^{-3/2} \longrightarrow 0 \quad (A \to \infty) \qquad \text{while} \qquad P(T^v) \;\le\; \varepsilon. \tag{T3.2}$$
4. *(Strict incomparability of $\rho_{\max}$ and $P$ on $\mathcal{F}_+$):* Conversely, on the $2 \times 2$ strictly positive PD family $k_c = \begin{pmatrix} 1 & c^2 \\ c^2 & c \end{pmatrix}$ ($0 < c < 1$), as $c \downarrow 0$ we have $P(k_c) \to 1$ (and $\alpha_{\mathrm{N1}}^{\mathrm{two}}(k_c) \to 0$) while $\rho_{\max}(k_c) = \frac{1}{1 + c^2} - \frac{c^4}{1 + c^4} \to 1$.

**Proof (`PROVED`).**
*(1)* For any measurable $f$ with $\|f\|_\infty \le 1$:
- Triangle inequality gives $|\mathbb{E}_{p_x}[f] - \mathbb{E}_{p_{x'}}[f]| \le |\mathbb{E}_{p_x}[f] - \mathbb{E}_\rho[f]| + |\mathbb{E}_{p_{x'}}[f] - \mathbb{E}_\rho[f]|$, so $\alpha_{\mathrm{N1}}^{\mathrm{two}} \le 2\alpha_{\mathrm{N1}}$.
- Jensen in $x'$ gives $|\mathbb{E}_{p_x}[f] - \mathbb{E}_\rho[f]| = |\mathbb{E}_{x'}[\mathbb{E}_{p_x}[f] - \mathbb{E}_{p_{x'}}[f]]| \le \mathbb{E}_{x'}|\mathbb{E}_{p_x}[f] - \mathbb{E}_{p_{x'}}[f]|$, so $\alpha_{\mathrm{N1}} \le \alpha_{\mathrm{N1}}^{\mathrm{two}}$.
- Since $|\mathbb{E}_{p_x}[f] - \mathbb{E}_{p_{x'}}[f]| \le 2 d_{\mathrm{TV}}(p_x, p_{x'})$, taking $\mathbb{E}_{x, x'}$ and then $\sup_{\|f\|_\infty \le 1}$ gives $\alpha_{\mathrm{N1}}^{\mathrm{two}} \le 2 d_{\mathrm{TV}}^{\mathrm{two}} \le 2\sqrt{1 - P}$ by Theorem 1A (T1.2).
- Put $\tilde{f} := f - \mathbb{E}_\rho[f] \in \mathbf{1}^\perp$. Then $\|\tilde{f}\|_{L^2(\rho)}^2 = \operatorname{Var}_\rho(f) \le \mathbb{E}_\rho[f^2] \le 1$. Since $p(x, y) = p(y, x)$, $Q$ is self-adjoint on $L^2(\rho)$ with $Q\mathbf{1} = \mathbf{1}$ and $\|Q|_{\mathbf{1}^\perp}\|_{2\to 2} = \rho_{\max}(A)$. By Cauchy–Schwarz,
  $$\mathbb{E}_{x \sim \rho}\!\left|\mathbb{E}_{p_x}[f] - \mathbb{E}_\rho[f]\right| = \|Q\tilde{f}\|_{L^1(\rho)} \le \|Q\tilde{f}\|_{L^2(\rho)} \le \rho_{\max}(A)\|\tilde{f}\|_{L^2(\rho)} \le \rho_{\max}(A).$$
  Taking $\sup_{\|f\|_\infty \le 1}$ gives $\alpha_{\mathrm{N1}} \le \rho_{\max}$, hence $\alpha_{\mathrm{N1}}^{\mathrm{two}} \le 2\rho_{\max}$.

*(2)* Fix $c := \sqrt{2\log(1/\varepsilon)} > 0$ and an integer $M \ge \max(\lceil c^2 \rceil + 1,\; \lceil 16 c^2 / \delta^2 \rceil)$. Set $r := c/\sqrt{M} \in (0, 1)$, and define on $\{0, 1\}$ (counting measure) the $2 \times 2$ kernel
$$k_1 := \frac{1}{2}\begin{pmatrix} 1 + r & 1 - r \\ 1 - r & 1 + r \end{pmatrix}.$$
Its eigenvalues are $1$ and $r > 0$, so $k_1 \in \mathcal{F}_+$ is strictly positive and strictly PD, with $Z_1 = 1 + r^2$, $\operatorname{Tr}(k_1^4) = 1 + r^4$, and
$$P(k_1) = \frac{1 + r^4}{(1 + r^2)^2} = 1 - \frac{2r^2}{(1 + r^2)^2} \le \exp\!\left(-\frac{2r^2}{(1 + r^2)^2}\right) \le e^{-r^2/2} = e^{-c^2/(2M)}.$$
Its two-slice conditional operator $Q_1$ has $\rho_1 = (1/2, 1/2)$ and eigenvalues $1$ and $\lambda := p_0(0) - p_0(1) = \frac{(1 + r)^2 - (1 - r)^2}{(1 + r)^2 + (1 - r)^2} = \frac{2r}{1 + r^2}$. Now take the $M$-fold tensor product $A := k_1^{\otimes M} \in \mathcal{F}_+$ on $\{0, 1\}^M$. Then $Q = Q_1^{\otimes M}$ is diagonal in the Walsh basis with eigenvalues $\lambda^{|S|}$ ($S \subseteq \{1, \dots, M\}$), so its largest nontrivial eigenvalue is $\rho_{\max}(A) = \lambda = \frac{2r}{1 + r^2} \le \frac{2c}{\sqrt{M}} \le \frac{\delta}{2}$, giving $\alpha_{\mathrm{N1}}^{\mathrm{two}}(A) \le 2\rho_{\max}(A) \le \delta$. Meanwhile $P(A) = P(k_1)^M \le e^{-c^2/2} = \varepsilon$.

*(3)* For the 4D massive free scalar field on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ with action $S(\phi) = \frac{1}{2}\sum_{x, \mu}(\phi_{x + e_\mu} - \phi_x)^2 + \frac{m^2}{2}\sum_x \phi_x^2$, transforming to $n^3$ real orthonormal spatial Fourier modes indexed by $k = \frac{2\pi}{n} j$ ($j \in \{-\lfloor (n-1)/2\rfloor, \dots, \lfloor n/2\rfloor\}^3$) decouples $T^v = \bigotimes_k T_k^v$, where each $T_k^v$ is a strictly positive-definite Mehler integral operator on $L^2(\mathbb{R})$ with dispersion
$$E_k = 2\operatorname{arsinh}\!\left(\frac{\mu_k}{2}\right) > 0, \qquad \mu_k^2 := m^2 + 4\sum_{i=1}^3 \sin^2\!\left(\frac{k_i}{2}\right), \qquad q_k := e^{-u E_k} \in (0, 1).$$
For each mode $k$, the periodic two-slice law of $(X_k, Y_k)$ at separation $v = u/2$ is centered bivariate Gaussian with correlation $\rho_k = \frac{2\sqrt{q_k}}{1 + q_k}$ and mode purity $P_k = \frac{1 - q_k}{1 + q_k}$ (`ON FILE`, check 1527 §(i) line 41). Let $\{H_a\}_{a \ge 0}$ be the orthonormal Hermite polynomials of $\mathcal{N}(0, 1)$, with generating function $\sum_{a \ge 0} \frac{s^a}{\sqrt{a!}} H_a(x) = e^{s x - s^2/2}$. For standard bivariate Gaussian $(X, Y)$ with correlation $\rho_k$,
$$\sum_{a, b \ge 0} \frac{s^a t^b}{\sqrt{a!\,b!}}\mathbb{E}[H_a(X) H_b(Y)] = \mathbb{E}\!\left[e^{s X - s^2/2 + t Y - t^2/2}\right] = e^{\rho_k s t} = \sum_{a \ge 0} \frac{(st)^a}{a!}\rho_k^a,$$
so $\mathbb{E}[H_a(X) H_b(Y)] = \delta_{ab} \rho_k^a$. Therefore $Q = \bigotimes_k Q_k$ is diagonal in the orthonormal tensor-product Hermite basis $\prod_k H_{a_k}(x_k)$ of $L^2(\rho)$ with eigenvalues $\prod_k \rho_k^{a_k}$. Since $E_k \ge E_0 = 2\operatorname{arsinh}(m/2)$ for all $k$ and $q \mapsto \frac{2\sqrt{q}}{1 + q}$ increases on $[0, 1]$,
$$\rho_{\max}(T^v) = \max_k \rho_k = \rho_0 = \frac{2\sqrt{q_0}}{1 + q_0} \le 2 e^{-u E_0/2}.$$
With our choice $m = 2\sinh\!\bigl(\frac{3\log A - \log C}{2u}\bigr) > 0$, we have $u E_0 = 3\log A - \log C$, so $e^{-u E_0} = C A^{-3}$ and
$$\alpha_{\mathrm{N1}}^{\mathrm{two}}(T^v) \le 2\rho_{\max}(T^v) \le 4 e^{-u E_0/2} = 4\sqrt{C}\,A^{-3/2}.$$
For the purity upper bound, note $\log\frac{1 - q}{1 + q} = -2\sum_{r=0}^\infty \frac{q^{2r+1}}{2r+1} \le -2q$ for $q \in [0, 1)$, so $P(T^v) = \prod_k \frac{1 - q_k}{1 + q_k} \le \exp(-2\sum_k q_k)$. Set $R := \lfloor A / (2\sqrt{3}\pi)\rfloor$. Since $12\pi^2 < 12 \cdot 9.87 = 118.44 < 121 = 11^2$, we have $2\sqrt{3}\pi < 11$, so for $A \ge 66$:
$$2R + 1 \ge 2\lfloor A/11\rfloor + 1 > \frac{2A}{11} - 1 \ge \frac{A}{6}, \qquad \text{and} \qquad R \le \frac{A}{10} < \frac{A u}{2} = \frac{n}{2}.$$
Thus all $(2R + 1)^3 \ge A^3 / 216$ integer triples $j \in \{-R, \dots, R\}^3$ yield distinct lattice momenta $k = \frac{2\pi}{n} j$. On this cube, $4\sum_{i=1}^3 \sin^2(k_i/2) \le \sum_{i=1}^3 k_i^2 \le \frac{12\pi^2 R^2}{n^2}$, so $\frac{\mu_k}{2} \le \frac{m}{2} + \frac{\sqrt{3}\pi R}{n}$. Since $\operatorname{arsinh}'(z) = (1 + z^2)^{-1/2} \le 1$ on $[0, \infty)$,
$$u E_k = 2u\operatorname{arsinh}\!\left(\frac{\mu_k}{2}\right) \le u E_0 + \frac{2\sqrt{3}\pi R}{A} \le u E_0 + 1 \implies q_k = e^{-u E_k} \ge e^{-1} e^{-u E_0} = \frac{C}{e A^3}.$$
Summing over the $(2R + 1)^3$ modes gives $\sum_k q_k \ge \frac{A^3}{216}\cdot \frac{C}{e A^3} = \frac{C}{216 e}$, whence $P(T^v) \le \exp\!\bigl(-\frac{C}{108 e}\bigr) = \varepsilon$.

*(4)* For $k_c = \begin{pmatrix} 1 & c^2 \\ c^2 & c \end{pmatrix}$ ($0 < c < 1$), $\det k_c = c(1 - c^3) > 0$, so $k_c \in \mathcal{F}_+$. By Theorem 2(3) Case A (with $\delta = c^2$), $P(k_c) \ge (1 + 3c^2)^{-2} \to 1$ as $c \downarrow 0$, hence $\alpha_{\mathrm{N1}}^{\mathrm{two}}(k_c) \le 2\sqrt{1 - P(k_c)} \to 0$. Meanwhile $Q$ is the $2 \times 2$ stochastic matrix with diagonal entries $p_1(1) = \frac{1}{1 + c^4}$ and $p_2(2) = \frac{c^2}{c^2 + c^4} = \frac{1}{1 + c^2}$, whose nontrivial eigenvalue is $\rho_{\max}(k_c) = \operatorname{tr}(Q) - 1 = p_1(1) + p_2(2) - 1 = \frac{1}{1 + c^2} - \frac{c^4}{1 + c^4} \to 1$ as $c \downarrow 0$. $\square$

---

## 5. Theorem 4: Obstructions for Swap-Circle, Absolute-Row `(SW)`, `(H-swap)`, and Uniform Mixing Forms

We now establish three explicit obstructions targeting the concrete stronger forms of `(W-mix)` built on file: the paired-link circle `Lemma CORNER` and Attack 2 of row 1574 (Proposition 4.1), the absolute-row trajectory bound `(SW)` of row 1574 (Proposition 4.2), and `(H-swap)` / uniform mixing along the calibrated trajectory $\beta_K$ (Proposition 4.3).

### 5.1 Proposition 4.1 (Exact vanishing of $P_{\mathcal{G}\times\mathcal{G}} D_p P_{\mathcal{G}\times\mathcal{G}}$ and `Lemma CORNER` for 4D $\mathrm{SU}(2)$ and $\mathrm{U}(1)$ Wilson) — `PROVED`

Let $n \ge 4$ be even, $\beta \ge 0$, $v \ge 1$, and $G \in \{\mathrm{SU}(2), \mathrm{U}(1)\}$ on $(\mathbb{Z}/n)^3$. Let $R_s = \prod_p R_s^p$ be the paired-link circle action of row 1574 `Proposition ROT` (or equivalently row 1573 `Lemma 1` for $\mathrm{SU}(2)$, and the square-contour pair rotation of row 1574 lines 173–176 for $\mathrm{U}(1)$), where each dimer $p = (e_1, e_2)$ consists of two consecutive spatial links $e_1 = (x, y)$, $e_2 = (y, z)$ along a coordinate line, with generator $D_p$ on the regular set $U$. Let $P_{\mathcal{G}\times\mathcal{G}}$ be the orthogonal projection onto separately gauge-invariant functions on $\mathcal{X} \times \mathcal{X}$ ($F(A^{g_A}, B^{g_B}) = F(A, B)$ for all $(g_A, g_B) \in \mathcal{G} \times \mathcal{G}$), and let $M_v \in \{T^v, P_0 T^v\}$ with doubled kernel $L(Y', Y) = k_v(A', A) k_v(B', B)$, sewing measure $d\mu = L^2 dY' dY / Z_1$, and mixed derivatives $h_{pq}(Y', Y) = D_p^{(1)} D_q^{(2)} \log L(Y', Y)$ (`ON FILE`, row 1574 Step 4).

**Proposition 4.1 (`PROVED`).** *For every even $n \ge 4$, every $\beta \ge 0$, every $v \ge 1$, and both $G = \mathrm{SU}(2)$ and $G = \mathrm{U}(1)$:*
1. *For every dimer $p$ and every smooth $(\mathcal{G}\times\mathcal{G})$-invariant function $F$ on $\mathcal{X} \times \mathcal{X}$, $(P_{\mathcal{G}\times\mathcal{G}} D_p F)(A, B) = 0$ identically at every $(A, B) \in \mathcal{X} \times \mathcal{X}$. Hence*
   $$P_{\mathcal{G}\times\mathcal{G}}\, D_p\, P_{\mathcal{G}\times\mathcal{G}} = 0 \qquad \text{and} \qquad (M_v \otimes M_v)\, D_p\, (M_v \otimes M_v) = 0. \tag{T4.1}$$
2. *In `Lemma CORNER` (row 1574 lines 224–234, check 1580 line 60) with $MM = M_v \otimes M_v$ and $G_{\mathrm{rot}} = -i\sum_p D_p$, every physical matrix element $\langle a, G_{\mathrm{rot}} b \rangle$ between eigenstates $a, b$ of $MM$ vanishes identically, so*
   $$\operatorname{Tr}(G_{\mathrm{rot}}\, MM\, G_{\mathrm{rot}}\, MM) = 0 \qquad \text{and} \qquad \mathbb{E}[jk] = 0 \qquad \text{identically.}$$
   *(Thus row 1574's necessary test $\mathbb{E}[jk] \le N_p L_\sigma/2$ and Attack 2's spectral bound at the unrotated corner reduce identically to $0 \le N_p L_\sigma/2$ and $0 = 0$.)*
3. *For every pair of dimers $(p, q)$ and every $(s, t)$ on the entire boundary $\partial([0, \pi]^2) = \{s \in \{0, \pi\}\} \cup \{t \in \{0, \pi\}\}$,*
   $$\mathbb{E}_\mu\!\left[h_{pq}(R_s Y', R_t Y)\right] = 0 \qquad \text{identically.} \tag{T4.2}$$
   *Consequently, $100\%$ of the positive exchange information $\mathbb{E}_\mu J = I(X; Y) + L(X; Y) = \frac{1}{2}\int_0^\pi\int_0^\pi \sum_{p, q} \mathbb{E}_\mu[h_{pq}(R_s Y', R_t Y)]\,ds\,dt$ in row 1573 (1) and row 1574 `Theorem SW` arises strictly from interior heated angles $(s, t) \in (0, \pi)^2$, where $R_s$ breaks $\mathcal{G}\times\mathcal{G}$-alignment and $D_p$ maps physical states into $(\mathcal{H} \otimes \mathcal{H})^\perp$.*

**Proof (`PROVED`).**
*(1)* Fix a dimer $p = (e_1, e_2)$ with $e_1 = (x, y)$, $e_2 = (y, z)$. Because $n \ge 4$ is even, the three vertices $x, y, z \in (\mathbb{Z}/n)^3$ are **pairwise distinct**. Let $F \in C^\infty(\mathcal{X} \times \mathcal{X})$ be $(\mathcal{G}\times\mathcal{G})$-invariant. For any $(g_A, g_B) \in \mathcal{G}\times\mathcal{G}$, set $u := g_A^{-1} g_B \in \mathcal{G}$. Because $R_s^p$ commutes with diagonal gauge transformations $(g_A, g_A)$ (`ON FILE`, row 1574 `Proposition ROT (iv)`, row 1573 `Lemma 1`) and $F$ is $(\mathcal{G}\times\mathcal{G})$-invariant,
$$F\!\left(R_s^p(A^{g_A}, B^{g_B})\right) = F\!\left((R_s^p(A, B^u))^{(g_A, g_A)}\right) = F\!\left(R_s^p(A, B^u)\right) = F\!\left((R_s^p(A, B^u))^{(1, u^{-1})}\right).$$
Differentiating at $s = 0$ and integrating over $(g_A, g_B) \in \mathcal{G}\times\mathcal{G}$ (with $u = g_A^{-1} g_B$ Haar-distributed on $\mathcal{G}$) gives
$$(P_{\mathcal{G}\times\mathcal{G}} D_p F)(A, B) = \int_{\mathcal{G}} \left.\frac{d}{ds}\right|_{s=0} F\!\bigl(\hat{A}(s; u), \hat{B}(s; u)\bigr)\,du,$$
where $(\hat{A}(s; u), \hat{B}(s; u)) := (R_s^p(A, B^u))^{(1, u^{-1})}$ starts at the **fixed** configuration $(\hat{A}(0; u), \hat{B}(0; u)) = (A, B)$ independent of $u$, and moves only the four links $(a_1, b_1, a_2, b_2)$ on $e_1, e_2$. By the chain rule at the fixed point $(A, B)$,
$$\left.\frac{d}{ds}\right|_{s=0} F\!\bigl(\hat{A}(s; u), \hat{B}(s; u)\bigr) = \sum_{i=1}^2 \Bigl(\langle \nabla_{a_i} F(A, B),\, \dot{\hat{a}}_i(u)\rangle + \langle \nabla_{b_i} F(A, B),\, \dot{\hat{b}}_i(u)\rangle\Bigr),$$
with uniformly bounded velocities ($\le 1$ for $\mathrm{SU}(2)$, $\le 2$ for $\mathrm{U}(1)$; `ON FILE`, check 1580 lines 24, 28), so Fubini applies.

- *Case $G = \mathrm{SU}(2)$ (row 1574 `Proposition ROT`):* On $(A, B^u)$, $\tilde{b}_1 = u_x b_1 u_y^{-1}$, $\tilde{b}_2 = u_y b_2 u_z^{-1}$, so
  $$\tilde{c}_1 = a_1^{-1} u_x b_1 u_y^{-1} = e^{\tilde{\theta}_1 \tilde{n}_1}, \quad \tilde{m}_1 = a_1 e^{\tilde{\theta}_1 \tilde{n}_1/2}, \qquad \tilde{c}_2 = u_y b_2 u_z^{-1} a_2^{-1} = e^{\tilde{\theta}_2 \tilde{n}_2}, \quad \tilde{m}_2 = e^{\tilde{\theta}_2 \tilde{n}_2/2} a_2,$$
  and $\tilde{k}_p = (\tilde{n}_1 \times \tilde{n}_2)/|\tilde{n}_1 \times \tilde{n}_2|$ a.e. From row 1574 lines 150–151, pulling back $\tilde{b}_1(s), \tilde{b}_2(s)$ by $u^{-1}$ and differentiating at $s = 0$ yields the exact pullback velocities:
  $$\dot{\hat{a}}_1(u) = \frac{1}{2}(\tilde{m}_1 \tilde{k}_p \tilde{m}_1^{-1}) a_1 - \frac{1}{2} a_1 \tilde{k}_p, \qquad \dot{\hat{b}}_1(u) = \frac{1}{2}(u_x^{-1} \tilde{m}_1 \tilde{k}_p \tilde{m}_1^{-1} u_x) b_1 - \frac{1}{2} b_1(u_y^{-1} \tilde{k}_p u_y),$$
  $$\dot{\hat{a}}_2(u) = \frac{1}{2} \tilde{k}_p a_2 - \frac{1}{2} a_2 (\tilde{m}_2^{-1} \tilde{k}_p \tilde{m}_2), \qquad \dot{\hat{b}}_2(u) = \frac{1}{2}(u_y^{-1} \tilde{k}_p u_y) b_2 - \frac{1}{2} b_2 (u_z^{-1} \tilde{m}_2^{-1} \tilde{k}_p \tilde{m}_2 u_z).$$
  Because $x, y, z$ are distinct, $u_x, u_y, u_z \in \mathrm{SU}(2)$ are independent Haar variables.
  - *Integrate $\dot{\hat{a}}_1, \dot{\hat{b}}_1$ over $u_z$ at fixed $(u_x, u_y)$:* Neither $\tilde{c}_1$, $\tilde{m}_1$, $u_x$, nor $u_y$ depends on $u_z$, whereas $u_z \mapsto \tilde{c}_2 = u_y b_2 u_z^{-1} a_2^{-1}$ pushes Haar measure on $\mathrm{SU}(2)$ to Haar measure on $\mathrm{SU}(2)$. The Haar-preserving involution $\tilde{c}_2 \mapsto \tilde{c}_2^{-1}$ (explicitly $u_z \mapsto a_2^{-1} u_y b_2 u_z^{-1} a_2^{-1} u_y b_2$) sends $(\tilde{\theta}_2, \tilde{n}_2) \mapsto (\tilde{\theta}_2, -\tilde{n}_2)$ and therefore negates $\tilde{k}_p \mapsto -\tilde{k}_p$ while fixing every other factor in $\dot{\hat{a}}_1, \dot{\hat{b}}_1$. Hence $\int \dot{\hat{a}}_1\,du_z = \int \dot{\hat{b}}_1\,du_z = 0$.
  - *Integrate $\dot{\hat{a}}_2, \dot{\hat{b}}_2$ over $u_x$ at fixed $(u_y, u_z)$:* Neither $\tilde{c}_2$, $\tilde{m}_2$, $u_y$, nor $u_z$ depends on $u_x$, whereas $u_x \mapsto \tilde{c}_1 = a_1^{-1} u_x b_1 u_y^{-1}$ is Haar. The Haar-preserving involution $\tilde{c}_1 \mapsto \tilde{c}_1^{-1}$ sends $\tilde{n}_1 \mapsto -\tilde{n}_1$, hence $\tilde{k}_p \mapsto -\tilde{k}_p$, while fixing every other factor in $\dot{\hat{a}}_2, \dot{\hat{b}}_2$. Hence $\int \dot{\hat{a}}_2\,du_x = \int \dot{\hat{b}}_2\,du_x = 0$.
  (The identical calculation holds for row 1573 `Lemma 1`, which replaces $\tilde{c}_2$ by $\tilde{c}_2^{-1}$.)
- *Case $G = \mathrm{U}(1)$ (row 1574 square-contour rotation):* Here $\tilde{\phi}_1 = b_1 - a_1 + u_x - u_y$ and $\tilde{\phi}_2 = b_2 - a_2 + u_y - u_z \pmod{2\pi}$ in $(-\pi, \pi)$. On the open edges of $\max(|\tilde{\phi}_1|, |\tilde{\phi}_2|) = \rho$, $(\dot{\hat{a}}_1, \dot{\hat{b}}_1)$ equals $(+2\rho/\pi, -2\rho/\pi)\operatorname{sgn}(\tilde{\phi}_2)\mathbf{1}_{|\tilde{\phi}_1| < |\tilde{\phi}_2|}$, which is odd under the Haar-preserving involution $\tilde{\phi}_2 \mapsto -\tilde{\phi}_2$ (via $u_z$ at fixed $u_x, u_y$); symmetrically, $(\dot{\hat{a}}_2, \dot{\hat{b}}_2)$ is odd under $\tilde{\phi}_1 \mapsto -\tilde{\phi}_1$ (via $u_x$ at fixed $u_y, u_z$). Again all four integrals vanish.

Thus $(P_{\mathcal{G}\times\mathcal{G}} D_p F)(A, B) = 0$ identically. Since smooth $(\mathcal{G}\times\mathcal{G})$-invariant functions are dense in $\operatorname{Ran}(P_{\mathcal{G}\times\mathcal{G}})$ and $MM = P_{\mathcal{G}\times\mathcal{G}} MM P_{\mathcal{G}\times\mathcal{G}}$ has smooth kernel, (T4.1) follows.

*(2)* Every eigenstate $a, b$ of $MM$ with nonzero eigenvalue is smooth and $(\mathcal{G}\times\mathcal{G})$-invariant (`ON FILE`, check 1580 line 60), so $\langle a, G_{\mathrm{rot}} b \rangle = -i\sum_p \langle a, P_{\mathcal{G}\times\mathcal{G}} D_p P_{\mathcal{G}\times\mathcal{G}} b \rangle = 0$. Hence $\operatorname{Tr}(G_{\mathrm{rot}} MM G_{\mathrm{rot}} MM) = \sum_{a, b} \Lambda_a \Lambda_b |\langle a, G_{\mathrm{rot}} b \rangle|^2 = 0$, and by `Lemma CORNER` (row 1574 line 226), $\mathbb{E}[jk] = 0$.

*(3)* Fix $t \in [0, \pi]$ and $Y \in U$, and set $F_{t, Y}(Y') := (D_q^{(2)} \log L)(Y', R_t Y)$. Because $L(Y', Z) = k_v(A', Z_1) k_v(B', Z_2)$ is smooth and $(\mathcal{G}\times\mathcal{G})$-invariant in its first argument $Y'$ for every $Z$, differentiating in $Z$ preserves $(\mathcal{G}\times\mathcal{G})$-invariance in $Y'$. Hence $F_{t, Y}$ is smooth and $(\mathcal{G}\times\mathcal{G})$-invariant in $Y'$, and $h_{pq}(Y', R_t Y) = (D_p^{(1)} F_{t, Y})(Y')$. Since $d\mu(Y', Y) = L(Y', Y)^2 dY' dY / Z_1$ is $(\mathcal{G}\times\mathcal{G})$-invariant in $Y'$ at fixed $Y$, averaging $Y'$ over $\mathcal{G}\times\mathcal{G}$ and applying part *(1)* yields
$$\mathbb{E}_\mu\!\left[h_{pq}(Y', R_t Y)\right] = \mathbb{E}_\mu\!\left[(P_{\mathcal{G}\times\mathcal{G}} D_p^{(1)} F_{t, Y})(Y')\right] = 0 \qquad (\forall t \in [0, \pi]).$$
Since $R_\pi = \sigma$ preserves $\mu$ and commutes with $R_s$, and $L(Y', Y) = L(Y, Y')$, the identical vanishing holds at $s = \pi$ (for all $t \in [0, \pi]$) and at $t \in \{0, \pi\}$ (for all $s \in [0, \pi]$). $\square$

---

### 5.2 Proposition 4.2 (Exact $\Omega(n^2) \to +\infty$ failure of row 1574's `(SW)` trajectory form on every 4D massive free scalar continuum trajectory) — `PROVED`

Consider the 4D Euclidean massive free scalar field on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ at fixed physical mass $m > 0$, fixed physical spatial side $\ell > 0$, and fixed even aspect $K_{\mathrm{asp}} \ge 2$ (e.g. $K_{\mathrm{asp}} = 512$), so lattice spacing $a = \ell/n$, lattice mass $m_0 := m\ell/n$, $u = n / K_{\mathrm{asp}}$, and $v = u/2 = n / (2 K_{\mathrm{asp}}) \ge 2$. By check 1527 `Proposition 1.2(1)–(2)` (`ON FILE`), as $n \to \infty$ the purity converges to $P_{\mathrm{cont}}(m\ell, K_{\mathrm{asp}}) \in (0, 1)$, with $1 - P_{\mathrm{cont}} \le C(1 + (m\ell/K_{\mathrm{asp}})^{3/2}) e^{-m\ell/K_{\mathrm{asp}}}$ (so $P_{\mathrm{cont}}$ can be made arbitrarily close to $1$, in particular $> 457/625$, by choosing $m\ell$ large).

On two copies $Y = (\phi, \psi) \in \mathbb{R}^{n^3} \times \mathbb{R}^{n^3}$, write $\bar{\phi}_x = (\phi_x + \psi_x)/2$, $\delta\phi_x = (\phi_x - \psi_x)/2$. Partition $(\mathbb{Z}/n)^3$ into $N_p = n^3 / 2$ adjacent dimers $p = (a_p, b_p)$ along axis $1$ ($a_p = (2j_1, j_2, j_3)$, $b_p = (2j_1 + 1, j_2, j_3)$), and define the smooth Lebesgue-preserving Euclidean dimer circle $R_s = \prod_p R_s^p$ fixing $\bar{\phi}$ and rotating $(\delta\phi_{a_p}, \delta\phi_{b_p})$ by angle $s$:
$$\delta\phi_{a_p}(s) = \cos s\,\delta\phi_{a_p} - \sin s\,\delta\phi_{b_p}, \qquad \delta\phi_{b_p}(s) = \sin s\,\delta\phi_{a_p} + \cos s\,\delta\phi_{b_p}.$$
Then $R_0 = \mathrm{id}$, $R_\pi = \sigma$ (exact replica swap), and `Theorem SW` (row 1574) holds verbatim with $L_\sigma(v) := \sup_{s, t \in [0, \pi],\, p} \sum_q \mathbb{E}_\mu |h_{pq}(R_s Y', R_t Y)|$ and $h_{pq} = D_p^{(1)} D_q^{(2)} \log L$.

**Proposition 4.2 (`PROVED`).** *In the 4D massive free scalar field at **every** fixed physical mass $m > 0$, physical side $\ell > 0$, and even aspect $K_{\mathrm{asp}} \ge 2$, for every $n \in 2 K_{\mathrm{asp}} \mathbb{N}$ with $v = n/(2 K_{\mathrm{asp}}) \ge 2$:*
1. *(Quadratic Gaussian 4th-moment lemma):* For every real quadratic form $Q = \sum_{j=1}^d \lambda_j G_j^2$ in i.i.d. $\mathcal{N}(0, 1)$ variables $G_1, \dots, G_d$,
   $$\mathbb{E}[Q^4] \;\le\; 17\,(\mathbb{E}[Q^2])^2, \qquad \text{and hence} \qquad \mathbb{E}|Q| \;\ge\; \frac{1}{\sqrt{17}}\sqrt{\mathbb{E}[Q^2]}. \tag{T4.3}$$
2. *(Failure of row 1574's inner-absolute-value `(SW)` bound):*
   $$L_\sigma(v) \;\ge\; \frac{1}{\sqrt{17}\bigl(16 + (m\ell/n)^2\bigr)}\,\frac{m\ell}{\sinh\!\bigl(m\ell/(2 K_{\mathrm{asp}})\bigr)}\,\frac{1}{n},$$
   $$\frac{\pi^2}{2} N_p L_\sigma(v) \;\ge\; \frac{\pi^2}{4\sqrt{17}\bigl(16 + (m\ell/n)^2\bigr)}\,\frac{m\ell}{\sinh\!\bigl(m\ell/(2 K_{\mathrm{asp}})\bigr)}\,n^2 \;\longrightarrow\; +\infty \qquad (n \to \infty). \tag{T4.4}$$
3. *(Exact contrast with signed and outer-absolute-value sums):* Along the exact same continuum trajectory, the signed exchange cost $I(X; Y) + L(X; Y) = \sum_k \frac{4 q_k}{(1 - q_k)^2}$ and the outer-absolute-value integrand at $s = t = \pi/2$ satisfy
   $$\mathbb{E}_\mu\!\left|\sum_{p, q} h_{pq}(R_{\pi/2} Y', R_{\pi/2} Y)\right| \;\le\; \sqrt{\left(\sum_k \frac{2 q_k}{(1 - q_k)^2}\right)^2 + \sum_k \frac{q_k(1 + q_k)^2 + 4 q_k^2}{(1 - q_k)^4}} \;=\; O_{m\ell, K_{\mathrm{asp}}}(1), \tag{T4.5}$$
   *which remains bounded uniformly in $n$ and tends to $0$ exponentially as $m\ell \to \infty$. Thus pulling the absolute value inside the dimer sum $\sum_q$ in row 1574's $L_\sigma(v)$ destroys continuum scaling by two powers of $n$ even in a gapped free 4D field with $P_{\mathrm{cont}} \to 1$.*

**Proof (`PROVED`).**
*(1)* Let $s_r := \sum_{j=1}^d \lambda_j^r$ ($r = 1, 2, 3, 4$). Using $\mathbb{E}[G_j^2] = 1$, $\mathbb{E}[G_j^4] = 3$, $\mathbb{E}[G_j^6] = 15$, $\mathbb{E}[G_j^8] = 105$ and independence of $G_j$:
$$\mathbb{E}[Q^2] = 3 s_2 + (s_1^2 - s_2) = s_1^2 + 2 s_2.$$
Expanding $\mathbb{E}[Q^4] = \sum_{i, j, k, l} \lambda_i\lambda_j\lambda_k\lambda_l \mathbb{E}[G_i^2 G_j^2 G_k^2 G_l^2]$ by index-equality partitions gives:
- $(4)$: $105 s_4$;
- $(3, 1)$: $4 \cdot 15 (s_3 s_1 - s_4) = 60(s_3 s_1 - s_4)$;
- $(2, 2)$: $3 \cdot 9 (s_2^2 - s_4) = 27(s_2^2 - s_4)$;
- $(2, 1, 1)$: $6 \cdot 3 (s_2 s_1^2 - s_2^2 - 2 s_3 s_1 + 2 s_4) = 18(s_2 s_1^2 - s_2^2 - 2 s_3 s_1 + 2 s_4)$;
- $(1, 1, 1, 1)$: $s_1^4 - 6 s_2 s_1^2 + 3 s_2^2 + 8 s_3 s_1 - 6 s_4$.

Summing the five terms gives the exact identity
$$\mathbb{E}[Q^4] = s_1^4 + 12 s_1^2 s_2 + 12 s_2^2 + 32 s_1 s_3 + 48 s_4.$$
Since $s_4 \le s_2^2$ and $|s_3| \le (\max_j |\lambda_j|) s_2 \le s_2^{3/2}$, AM–GM yields $32 |s_1 s_3| \le 32 |s_1| s_2^{3/2} = 16(2|s_1| s_2^{1/2}) s_2 \le 32 s_1^2 s_2 + 8 s_2^2$. Hence
$$\mathbb{E}[Q^4] \le s_1^4 + 44 s_1^2 s_2 + 68 s_2^2 \le 17(s_1^2 + 2 s_2)^2 = 17(\mathbb{E}[Q^2])^2.$$
Applying Hölder's inequality $\mathbb{E}[Q^2] = \mathbb{E}[|Q|^{2/3} |Q|^{4/3}] \le (\mathbb{E}|Q|)^{2/3} (\mathbb{E}[Q^4])^{1/3}$ gives $\mathbb{E}|Q| \ge (\mathbb{E}[Q^2])^{3/2}/(\mathbb{E}[Q^4])^{1/2} \ge \frac{1}{\sqrt{17}}\sqrt{\mathbb{E}[Q^2]}$.

*(2)* Integrating out the interior slices $t = 1, \dots, v - 1$ of the pinned free-scalar cylinder gives
$$\log k_v(\phi', \phi) = \text{(single-end terms)} + \langle \phi', M_v \phi \rangle,$$
where $M_v(x, y) = G_{\mathrm{int}}((x, 1), (y, v - 1))$ is the Green function of $H_{\mathrm{int}} = -\Delta_{\mathrm{int}} + m_0^2$ on $(\mathbb{Z}/n)^3 \times \{1, \dots, v - 1\}$ with Dirichlet boundary conditions at $t = 0, v$. Writing $H_{\mathrm{int}} = (8 + m_0^2) I - A_{\mathrm{int}}$ with nonnegative adjacency matrix $A_{\mathrm{int}}$ ($\|A_{\mathrm{int}}\| \le 8 < 8 + m_0^2$), the Neumann series $H_{\mathrm{int}}^{-1} = \sum_{r=0}^\infty (8 + m_0^2)^{-(r+1)} A_{\mathrm{int}}^r$ proves $M_v(x, y) > 0$ for all $x, y$. In spatial Fourier mode $k$, the 1D Dirichlet Green function satisfies $\widehat{M}_v(k) = \frac{\sinh E_k}{\sinh(v E_k)}$, so $\sum_{y \in (\mathbb{Z}/n)^3} M_v(x, y) = \widehat{M}_v(0) = \frac{\sinh E_0}{\sinh(v E_0)}$.

For two replicas $Y' = (\phi', \psi')$ and $Y = (\phi, \psi)$, the cross-end term of $\log L(Y', Y)$ is $\langle \phi', M_v \phi \rangle + \langle \psi', M_v \psi \rangle = 2\langle \bar{\phi}', M_v \bar{\phi}\rangle + 2\langle \delta\phi', M_v \delta\phi\rangle$. Differentiating along $R_s^p$ and $R_t^q$ gives
$$h_{pq}(R_s Y', R_t Y) = 2\sum_{x \in p,\, y \in q} M_v(x, y)\,\bigl(\partial_s \delta\phi'_x(s)\bigr)\bigl(\partial_t \delta\phi_y(t)\bigr).$$
At $s = t = \pi/2$, we have $\partial_s \delta\phi'_x(\pi/2) = -\delta\phi'_x$ and $\partial_t \delta\phi_y(\pi/2) = -\delta\phi_y$ for both sites of each dimer, so
$$Q_{pq} := h_{pq}(R_{\pi/2} Y', R_{\pi/2} Y) = 2\sum_{x \in p,\, y \in q} M_v(x, y)\,\delta\phi'_x\,\delta\phi_y.$$
Under $\mu$, the two replicas are independent copies of the periodic free scalar on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ ($u = 2v$), so $(\delta\phi', \delta\phi)$ is jointly centered Gaussian with $\mathbb{E}_\mu[\delta\phi'_x \delta\phi'_{x'}] = \mathbb{E}_\mu[\delta\phi_x \delta\phi_{x'}] = \frac{1}{2} C_0(x - x')$ and $\mathbb{E}_\mu[\delta\phi'_x \delta\phi_y] = \frac{1}{2} C_v(x - y)$, where $C_t(z) = G_{\mathrm{per}}((0, 0), (z, t)) > 0$ is the periodic torus Green function (again strictly positive by Neumann series). By Wick's theorem,
$$\mathbb{E}_\mu[Q_{pq}^2] = \sum_{x, x' \in p}\sum_{y, y' \in q} M_v(x, y) M_v(x', y')\Bigl[C_v(x - y) C_v(x' - y') + C_0(x - x') C_0(y - y') + C_v(x - y') C_v(x' - y)\Bigr].$$
Every summand is strictly positive; keeping only the diagonal terms $x = x', y = y'$ of the middle term and applying Cauchy–Schwarz to the $4$ pairs in $p \times q$ gives
$$\mathbb{E}_\mu[Q_{pq}^2] \ge C_0(0)^2 \sum_{x \in p,\, y \in q} M_v(x, y)^2 \implies \sqrt{\mathbb{E}_\mu[Q_{pq}^2]} \ge \frac{C_0(0)}{2}\sum_{x \in p,\, y \in q} M_v(x, y).$$
Since $Q_{pq}$ is a real quadratic form in the jointly centered Gaussian vector $(\delta\phi'_p, \delta\phi_q)$ (hence orthogonally diagonalizable as $\sum \lambda_j G_j^2$ in i.i.d. $\mathcal{N}(0, 1)$ variables), part *(1)* gives $\mathbb{E}_\mu|Q_{pq}| \ge \frac{C_0(0)}{2\sqrt{17}}\sum_{x \in p, y \in q} M_v(x, y)$. Summing over all $N_p = n^3/2$ dimers $q$ (which partition $(\mathbb{Z}/n)^3$) at fixed $p$ ($|p| = 2$) gives
$$L_\sigma(v) \ge \sum_q \mathbb{E}_\mu|Q_{pq}| \ge \frac{C_0(0)}{2\sqrt{17}}\cdot 2\sum_{y \in (\mathbb{Z}/n)^3} M_v(a_p, y) = \frac{C_0(0)}{\sqrt{17}}\,\frac{\sinh E_0}{\sinh(v E_0)}.$$
Finally:
- Every 4D lattice Laplacian eigenvalue lies in $[0, 16]$, so $C_0(0) = \frac{1}{n^3 u}\sum_{k, \omega} (\hat{k}^2 + \hat{\omega}^2 + m_0^2)^{-1} \ge \frac{1}{16 + m_0^2}$;
- $\sinh E_0 = 2\sinh(E_0/2)\cosh(E_0/2) = m_0\sqrt{1 + m_0^2/4} \ge m_0 = m\ell/n$;
- $E_0 = 2\operatorname{arsinh}(m_0/2) \le m_0$, so $v E_0 \le v m_0 = m\ell/(2 K_{\mathrm{asp}})$ and $\sinh(v E_0) \le \sinh(m\ell/(2 K_{\mathrm{asp}}))$.

Substituting these three elementary bounds and multiplying by $\frac{\pi^2}{2} N_p = \frac{\pi^2}{4} n^3$ yields (T4.4).

*(3)* For a single standard bivariate Gaussian with correlation $\rho_k = \frac{2\sqrt{q_k}}{1 + q_k}$, direct Gaussian integration gives $I(X_k; Y_k) = -\frac{1}{2}\log(1 - \rho_k^2)$ and $L(X_k; Y_k) = \frac{1}{2}\log(1 - \rho_k^2) + \frac{\rho_k^2}{1 - \rho_k^2}$, so $I(X; Y) + L(X; Y) = \sum_k \frac{\rho_k^2}{1 - \rho_k^2} = \sum_k \frac{4 q_k}{(1 - q_k)^2}$. For the outer-absolute-value sum $H(\pi/2, \pi/2) = \sum_{p, q} Q_{pq} = 2\langle \delta\phi', M_v \delta\phi\rangle$, Wick's theorem gives
$$\mathbb{E}_\mu[H(\pi/2, \pi/2)^2] = \bigl(\operatorname{Tr}(M_v C_v)\bigr)^2 + \operatorname{Tr}(M_v C_0 M_v C_0) + \operatorname{Tr}(M_v C_v M_v C_v).$$
In spatial Fourier space, $\widehat{C}_0(k) = \frac{\cosh(v E_k)}{2\sinh E_k \sinh(v E_k)}$ and $\widehat{C}_v(k) = \frac{1}{2\sinh E_k \sinh(v E_k)}$, so $\widehat{M}_v(k)\widehat{C}_v(k) = \frac{1}{2\sinh^2(v E_k)} = \frac{2 q_k}{(1 - q_k)^2}$ and $\widehat{M}_v(k)\widehat{C}_0(k) = \frac{\cosh(v E_k)}{2\sinh^2(v E_k)} = \frac{\sqrt{q_k}(1 + q_k)}{(1 - q_k)^2}$. Cauchy–Schwarz ($\mathbb{E}|H| \le \sqrt{\mathbb{E}[H^2]}$) gives (T4.5); the uniform $O_{m\ell, K_{\mathrm{asp}}}(1)$ summability and exponential decay as $m\ell \to \infty$ follow directly from check 1527 `Proposition 1.2(1)–(2)` (`ON FILE`). $\square$

---

### 5.3 Proposition 4.3 (Unconditional failure of `(H-swap)` and uniform-boundary mixing on the calibrated trajectory $\beta_K$) — `PROVED`

**Proposition 4.3 (`PROVED` given checked row 1121 `Proposition J`, row 1072 `CA-FAIL`, and row 1453 `BND-1`/`BND-2`).** *Fix the release witnesses $(b, g_0)$ of check 1453 and let $\beta_K$ be the calibrated bare inverse coupling trajectory.*

1. *(Elementary uniform plaquette lower bound at all $\beta \ge 1$):* For 4D $\mathrm{SU}(2)$ Wilson lattice gauge theory on any periodic hypercubic torus $(\mathbb{Z}/L)^4$ ($L \ge 2$) and every $\beta \ge 1$, the mean plaquette $\bar{P}(\beta) := \mathbb{E}_\beta[\frac{1}{2}\operatorname{tr} U_p]$ satisfies
   $$\bar{P}(\beta) \;\ge\; 1 - \frac{3 + \log(8\beta)}{\beta}. \tag{T4.6}$$
   *In particular, $\lim_{K \to \infty} \bar{P}(\beta_K) = 1$ uniformly in $L \ge 2$.*
2. *(Calibrated-trajectory refutation of `(H-swap)` of row 1118 for every cell size $l \ge 2$):* Let $p_c$ be the cell swap-defect probability of `(H-swap)` (row 1118 (4.3)–(4.5), check 1121 §8.1), whose threshold in four dimensions is $\varepsilon_0(4) = 1/1250$. By check 1453 (`BND-1`, `BND-2`), $\beta_K \to +\infty$, so there exists $K_1$ with $\beta_K \ge 2.3$ for all $K \ge K_1$. For every fixed cell size $l \ge 2$, on any torus of side $L \ge 5l$ divisible by $l$ (or in any local limit of torus states),
   $$\mathbb{E}_{\rho_K \otimes \rho_K}[p_c] \;\ge\; 0.010 \;>\; \frac{1}{1250} \quad (\forall K \ge K_1,\; L \ge 20), \qquad \text{and} \qquad \liminf_{K \to \infty} \mathbb{E}_{\rho_K \otimes \rho_K}[p_c] \;\ge\; \frac{1}{2} \;\gg\; \frac{1}{1250}. \tag{T4.7}$$
   *Hence `(H-swap)` (4.4) and its path-moment weakening (4.5) fail unconditionally for every cell size $l \ge 2$ on the entire tail $K \ge K_1$ of the calibrated trajectory $\beta_K$, already on a one-cell chain $\{c\}$.*
3. *(Calibrated-trajectory failure of boundary-uniform mixing):* Because $\beta_K \to +\infty$, eventually $\beta_K > \beta_{\mathrm{FSS}} \approx 1.0109$, so by `Proposition CA-FAIL` (`ON FILE`, row 1072 `library/gap-bridge-exercise-opus.md`), uniform-over-boundaries mixing fails on every large box along $\beta_K$. In particular, no boundary-uniform Dobrushin/Wasserstein contraction (the mechanism of rows 1566, 1568, 1573, 1574, 1576) and no uniform-over-all-coarse-fields version of `(CM_k)` (row 1468 §4.3) holds on the tail of $\beta_K$.

**Proof (`PROVED`).**
*(1)* Let $V = L^4$ be the number of sites on $(\mathbb{Z}/L)^4$ (with $4V$ links and $6V$ plaquettes) and $Z_L(\beta) = \int \exp(\beta \sum_p t_p)\,dU$, where $t_p = \frac{1}{2}\operatorname{tr} U_p \in [-1, 1]$. Since $\log Z_L(\beta)$ is convex in $\beta$ with $\log Z_L(0) = 0$ and all $6V$ plaquettes have the same expectation by lattice symmetry (`ON FILE`, check 1121 §8.3),
$$6V\bar{P}(\beta) = \frac{d}{d\beta}\log Z_L(\beta) \ge \frac{\log Z_L(\beta)}{\beta} \implies \bar{P}(\beta) \ge \frac{\log Z_L(\beta)}{6\beta V}.$$
For any $\delta \in (0, \pi/8]$, restrict every link $U_e = e^{\theta_e n_e} \in \mathrm{SU}(2)$ to the geodesic ball $B_\delta := \{U : \theta \in [0, \delta]\}$. By bi-invariance of the geodesic distance $d(I, U) = \theta$ and the triangle inequality, every plaquette holonomy satisfies $d(I, U_p) \le 4\delta \le \pi/2$, hence $t_p = \cos(d(I, U_p)) \ge \cos(4\delta) \ge 1 - 8\delta^2$. Using $\sin\theta \ge \frac{2}{\pi}\theta$ on $[0, \pi/2]$ and $3\pi^3 < 3(3.142)^3 < 93.1 < 96 = 12 \cdot 8$, the normalized Haar volume of $B_\delta$ obeys
$$\operatorname{Haar}(B_\delta) = \frac{2}{\pi}\int_0^\delta \sin^2\theta\,d\theta \ge \frac{8}{\pi^3}\int_0^\delta \theta^2\,d\theta = \frac{8\delta^3}{3\pi^3} \ge \frac{\delta^3}{12}.$$
Integrating over $B_\delta^{4V}$ therefore gives $Z_L(\beta) \ge \exp(6\beta V(1 - 8\delta^2))(\delta^3/12)^{4V}$, so
$$\bar{P}(\beta) \ge 1 - 8\delta^2 - \frac{2\log(1/\delta)}{\beta} - \frac{2\log 12}{3\beta}.$$
For $\beta \ge 1$, set $\delta := (8\beta)^{-1/2} \le 8^{-1/2} < 0.354 < 0.392 < \pi/8$. Then $8\delta^2 = 1/\beta$, $2\log(1/\delta)/\beta = \log(8\beta)/\beta$, and $\frac{2}{3}\log 12 < \frac{2}{3}(2.5) < 2$, yielding (T4.6). Since $\beta_K \to +\infty$ by check 1453 (`BND-1`, `BND-2`), $\bar{P}(\beta_K) \to 1$ uniformly in $L \ge 2$.

*(2)* By check 1121 `Proposition J(a)` (`ON FILE`, lines 134–150), for every $l \ge 2$ and every torus of side $L \ge 5l$ divisible by $l$ (and local limits), $\mathbb{E}[p_c] \ge \frac{1}{2}(1 - e^{-3\beta l})\bar{P}(\beta)$. For $\beta_K \ge 2.3$ and $L \ge 20$, check 1121 `Proposition J(c)` gives $\mathbb{E}[p_c] \ge 0.010 > 1/1250$. As $K \to \infty$, $\beta_K \to +\infty$ gives $1 - e^{-3\beta_K l} \to 1$ and $\bar{P}(\beta_K) \to 1$ by part *(1)*, yielding $\liminf_{K \to \infty} \mathbb{E}[p_c] \ge 1/2$.

*(3)* Direct combination of check 1453 (`BND-1`: $\beta_K \to +\infty$) and row 1072 `Proposition CA-FAIL` (`ON FILE`). $\square$

---

## 6. Synthesis: Family Covered, Open Frontier, Selectivity, and Claim Audit

### 6.1 Summary table: the complete `(W-mix)` obstruction landscape

| On-file form of `(W-mix)` | Relation to `(PUR-io)` / Calibrated-trajectory status | Exact anchor here | Status |
|---|---|---|---|
| `(H-two)` ($d_{\mathrm{TV}}^{\mathrm{two}}$), $\beta_{\mathrm{mix}}$, $H_{\mathrm{two}}^2$, $H^2(p, m)$ on half-cylinder | **Logically equivalent to `(PUR-io)`** on $\beta_K$ (exact two-sided bounds on $\mathcal{F}_+$, sharp exponents) | Theorems 1A, 1B | `PROVED` (1B uses checked 705/707, 1368/1370, 1527) |
| Any bounded $f$-divergence ($M(f) < \infty$, non-degenerate at $1$: JS, Triangular, Hellinger-$\alpha$ for $\alpha \in (0, 1)$) | **Logically equivalent to `(PUR-io)`** on $\beta_K$ via $\phi_f(1 - \sqrt{P}) \le D_f^{\mathrm{two}} \le M(f)\sqrt{1 - P}$ | Theorem 2(1)–(2) | `PROVED` |
| Any unbounded $f$-divergence ($M(f) = \infty$: $I(X; Y)$, $L(X; Y)$, `Lemma JI` $I + L$, $\chi^2$, Rényi-$\alpha$ for $\alpha > 1$) | **Strictly stronger than $P$ on $\mathcal{F}_+$**; sharpened consumer $-\log P \le 2\min(I, L) \le I + L$ drops Lautum $L$ | Theorem 2(3)–(4) | `PROVED` |
| `(H-two-N1)` ($\alpha_{\mathrm{N1}}^{\mathrm{two}}$, check 1120 §5.3) and $\rho_{\max}(p)$ | **Strictly weaker / insufficient** ($\alpha_{\mathrm{N1}}^{\mathrm{two}} \to 0$ with $P \le \varepsilon$ on product kernels & 4D massive free scalars); $\rho_{\max}$ incomparable with $P$ | Theorem 3 | `PROVED` |
| Row 1574 `Lemma CORNER` & Attack 2 ($\operatorname{Tr}(G MM G MM)$, $\mathbb{E}[jk]$, boundary $\mathbb{E}_\mu[h_{pq}]$) | **Identically zero** ($P_{\mathcal{G}\times\mathcal{G}} D_p P_{\mathcal{G}\times\mathcal{G}} = 0$, $\mathbb{E}_\mu[h_{pq}] = 0$ on $\partial([0, \pi]^2)$) for 4D $\mathrm{SU}(2)$ & $\mathrm{U}(1)$ Wilson at all $\beta \ge 0$, even $n \ge 4$ | Proposition 4.1 | `PROVED` |
| Row 1574 `(SW)` inner-absolute-value trajectory bound $\frac{\pi^2}{2} N_p L_\sigma(v)$ | **Diverges as $\Omega(n^2) \to +\infty$** on every 4D massive free scalar continuum trajectory (even when $P_{\mathrm{cont}} \to 1$ and outer-absolute-value $B_K \to 0$) | Proposition 4.2 | `PROVED` |
| `(H-swap)` (row 1118) and uniform-boundary mixing (`CA-FAIL`, row 1072) | **Fail unconditionally on the tail of $\beta_K$**: $\liminf_{K \to \infty} \mathbb{E}[p_c] \ge 1/2 \gg 1/1250$ for every $l \ge 2$; uniform mixing fails for $\beta_K > 1.0109$ | Proposition 4.3 | `PROVED` (uses checked 1072, 1121, 1453) |

### 6.2 Family covered and what remains open

**Family covered by this obstruction theorem (`PROVED`).**
1. Every bounded $f$-divergence half-cylinder mixing criterion (two-sample $D_f^{\mathrm{two}}$ or joint-to-product $D_f(p \| m)$) on the full positive-kernel transfer family $\mathcal{F}_+$, and hence on the calibrated trajectory $\beta_K$ of 4D $\mathrm{SU}(2)$ Wilson lattice gauge theory (exact logical equivalence to `(PUR-io)`).
2. Every unbounded $f$-divergence half-cylinder mixing criterion on $\mathcal{F}_+$ (strict strength over $P$ on $\mathcal{F}_+$, plus the sharper consumer $-\log P \le 2\min(I, L) \le I + L$).
3. One-observable weakenings `(H-two-N1)` and maximal correlation $\rho_{\max}(p)$ on $\mathcal{F}_+$ and in 4D local reflection-positive massive free scalar fields (strict insufficiency / incomparability).
4. The paired-link circle `Lemma CORNER` and boundary-angle responses of rows 1573–1574 for 4D $\mathrm{SU}(2)$ and $\mathrm{U}(1)$ Wilson (exact gauge-projection vanishing); row 1574's inner-absolute-value `(SW)` bound on 4D continuum massive free scalar trajectories ($\Omega(n^2)$ blowup); and `(H-swap)` / boundary-uniform mixing on the calibrated trajectory $\beta_K$ (unconditional refutation).

**What remains open (not excluded by Theorems 1–4).**
1. *Strictness or failure inside pure 4D $\mathrm{SU}(2)$ Wilson along $\beta_K$* for the **unbounded / exterior-modulus / defect-measure** half-cylinder forms: $I(X; Y)$, $I + L$, row 1573's outer-absolute-value $B_K$, row 1574's $N_p L_\sigma(v)$ (Proposition 4.2 refutes its continuum scaling in 4D massive free scalars, not yet inside interacting 4D $\mathrm{SU}(2)$ Wilson), and row 1576's defect-measure covariance bounds (`TC_{diag}`, `TC_{traj}`, `TS_{diag}`, `TS_{traj}`).
2. *Single-step renormalization mixing* rather than half-cylinder mixing: `(FL)` (row 1510, lattice-scale-$2$ posterior score covariance at $\beta \in [2, 3]$) and regular-set `(CM_k)` (row 1468 §4.3, restricted to a regular set of coarse fields rather than worst-case boundaries excluded by `CA-FAIL`).
3. *Coupling/scale carries* (`R11`, `R12`, `TWO-PER`, `(T-carry)`) and *non-`(W-mix)` mechanisms* of row 1386 (`(K-I)` signed typical-field stiffness carry, `(K-II)` order-one RG step).
4. `(PUR-io)` and the 4D $\mathrm{SU}(2)$ Yang–Mills mass gap itself.

### 6.3 Selectivity and gapped-twin checks for the equivalence class

- **4D compact $\mathrm{U}(1)$ at weak coupling (`PROVED` given checked row 1573 lines 131–150 / check 1580 line 92):** In the $\mathbb{Z}_2^3$-even sector, $P_{\mathrm{even}} \le (1 + 2d^4)^{-1} < 1$ uniformly at aspect $512$ (Villain $\beta \ge 2000$ and Wilson $\beta_W \ge \beta_*$, `ON FILE` check 1580 line 92). By Theorem 1A (T1.1)–(T1.4), $d_{\mathrm{TV}}^{\mathrm{two}}, H_{\mathrm{two}}^2 \ge 1 - (1 + 2d^4)^{-1/2} > 0$ and $\beta_{\mathrm{mix}}, H^2(p, m) \ge 1 - (1 + 2d^4)^{-1/4} > 0$ uniformly, so `(W-mix-TV-all)` (and every bounded $D_f$-form via $\phi_f$) **fails**.
- **5D $\mathrm{SU}(2)$ at weak coupling (`ARGUED` / belief-grade, `ON FILE` check 1580 line 109):** Under the belief of a massless weak-coupling phase with persistent thermal weight at fixed aspect, $P$ stays bounded away from $1$, so `(W-mix-TV-all)` fails.
- **Gapped twin 4D $\mathrm{SU}(2)$ at fixed $\beta < 2/9$ (`PROVED` given checked row 1568 / check 1580 line 97):** By check 1580 line 97, $-\log P_K \le O(n^3 v q^{v-2}) \to 0$ exponentially with $q = 9\beta/2 < 1$, so by Theorem 1A and Theorem 2(2), $d_{\mathrm{TV}}^{\mathrm{two}}, \beta_{\mathrm{mix}}, D_f^{\mathrm{two}}, D_f^{\mathrm{joint}} \le M(f)\sqrt{1 - P_K} \to 0$ exponentially.

### 6.4 Claim-by-claim label audit

- **Section 1 (Inventory table):** `ON FILE` (exact row anchors cited per row).
- **Theorem 1A (single-box bounds & sharpness on $\mathcal{F}_+$):** `PROVED` (midpoint affinity identity `ON FILE` rows 1373/1526/1527, extended here without strict positivity; all inequalities and sharpness witnesses `PROVED` in full).
- **Theorem 1B (calibrated-trajectory equivalence to `(PUR-io)`):** `PROVED` from checked `ON FILE` inputs (rows 705/707 `B3`/`SH`, 1368/1370 `Theorem 4`/`Corollary 5`, 1453, 1527 `Theorem 2`).
- **Theorem 2 ($f$-divergence trichotomy & $-\log P \le 2\min(I, L)$):** `PROVED` in full (contrasted with `ON FILE` row 839 Proposition K).
- **Theorem 3 (insufficiency of `(H-two-N1)` & incomparability of $\rho_{\max}$):** `PROVED` in full (including the 4D massive free scalar witness).
- **Proposition 4.1 ($P_{\mathcal{G}\times\mathcal{G}} D_p P_{\mathcal{G}\times\mathcal{G}} = 0$, vanishing of `Lemma CORNER` and $\partial([0, \pi]^2)$):** `PROVED` in full.
- **Proposition 4.2 ($\Omega(n^2)$ blowup of `(SW)` $N_p L_\sigma(v)$ in 4D massive free scalars vs $O(1)$ outer-modulus $B_K$):** `PROVED` in full.
- **Proposition 4.3 (calibrated-trajectory failure of `(H-swap)` and uniform-boundary mixing):** `PROVED` from checked `ON FILE` inputs (rows 1072, 1121, 1453) plus self-contained proof of $\bar{P}(\beta) \ge 1 - (3 + \log(8\beta))/\beta$.
- **5D $\mathrm{SU}(2)$ weak-coupling failure:** `ARGUED` (conditional on belief-grade masslessness). No claim is `GUESSED`. No proof step uses Monte Carlo or floating-point arithmetic.

---

## 7. RESULT

**Outcome (c) — Obstruction theorem for `(W-mix)`.** Four quantified theorems delimit the on-file half-cylinder `(W-mix)` family (`PROVED`; 1B/4.3 use checked rows 705/707, 1072, 1121, 1368/1370, 1453, 1527):
(1) **Theorems 1A–1B:** on $\mathcal{F}_+$, $1-\sqrt{P}\le H_{\mathrm{two}}^2\le d_{\mathrm{TV}}^{\mathrm{two}}\le\sqrt{1-P}$ and $1-P^{1/4}\le H^2(p,m)\le\beta_{\mathrm{mix}}\le\sqrt{1-P}$ (sharp); on $\beta_K$, every half-cylinder TV (`(H-two)`), $\beta_{\mathrm{mix}}$, Hellinger, or affinity criterion is **equivalent to `(PUR-io)`**.
(2) **Theorem 2:** complete $f$-divergence trichotomy on $\mathcal{F}_+$—bounded $f$-divergences ($M(f)<\infty$) are equivalent to `(PUR-io)` on $\beta_K$, unbounded ones ($I,L,I+L,\chi^2$) are strictly stronger on $\mathcal{F}_+$, and $-\log P\le 2\min(I,L)\le I+L$ strictly sharpens row 1573 (3).
(3) **Theorem 3:** `(H-two-N1)` implies no positive lower bound on $P$ (even in 4D massive free scalars: $\alpha_{\mathrm{N1}}^{\mathrm{two}}\le 4\sqrt{C}A^{-3/2}\to 0$ with $P\le\varepsilon$), and $\rho_{\max}$ is incomparable with $P$.
(4) **Theorem 4:** for 4D $\mathrm{SU}(2)/\mathrm{U}(1)$ Wilson (all $\beta\ge 0$, even $n\ge 4$), $P_{\mathcal{G}\times\mathcal{G}}D_p P_{\mathcal{G}\times\mathcal{G}}=0$, so row 1574's `Lemma CORNER` and boundary $\mathbb{E}_\mu[h_{pq}]$ vanish identically; row 1574's `(SW)` bound $N_p L_\sigma(v)$ diverges as $\Omega(n^2)$ on every 4D massive free scalar continuum trajectory even when $P_{\mathrm{cont}}\to 1$ and $B_K\to 0$; and `(H-swap)` plus uniform-boundary mixing fail unconditionally on $\beta_K$ ($\liminf\mathbb{E}[p_c]\ge 1/2\gg 1/1250$).
**Left open:** pure-Wilson strictness on $\beta_K$ of $I,B_K,N_p L_\sigma,\mathrm{TC}/\mathrm{TS}$, single-step RG mixing (`(FL)`, regular-set `(CM_k)`), coupling carries (`R11`/`R12`), and `(PUR-io)`.
