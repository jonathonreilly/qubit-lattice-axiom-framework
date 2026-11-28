# Band Neutral Sector Attack: Obstructions to Local Replica-Swap Circles, Connected-Group Two-Seam and Two-Cut Interpolations, Selectivity Tests, and Three Attacks

*Author: Gemini 4 Neon (XHigh). Research-stage working document; unchecked by another model; grants no scientific status. All proof steps are by hand; no numeric or Lean run serves as a proof step. No files from rows 1573 or 1574 were read.*

## 0. Setup, Target, and Prior-Work Anchor Map

Fix the release witnesses (odd block factor $b$, calibration level $g_0$) as in check 1453, an admissible spatial side $\ell \in 1024\mathbb{N}$, and at cutoff $K$ put $n = \ell b^K$, $u = n/512$, and $v = u/2 = n/1024 \ge 3$. On the spatial torus $\Sigma = (\mathbb{Z}/n)^3$ with vertex set $V(\Sigma)$ ($|V(\Sigma)| = n^3$) and oriented spatial link set $E(\Sigma)$ ($|E(\Sigma)| = 3n^3$), let $\mathcal{A} = \mathrm{SU}(2)^{E(\Sigma)}$ carry normalized product Haar measure $dA$, let $\mathcal{G} = \mathrm{SU}(2)^{V(\Sigma)}$ act by vertex gauge transformations $(g \cdot A)_{x,i} = g_x A_{x,i} g_{x+\hat i}^{-1}$, and let $C_z$ ($z \in \mathbb{Z}_2^3$) be the centre translations multiplying by $(-1)^{z_i}$ every positive $i$-link with tail at $x_i = 0$.

At coupling $\beta \ge 0$, write the symmetric Wilson transfer operator on the physical gauge-invariant space $\mathcal{H} = L^2(\mathcal{A}/\mathcal{G})$ as
$$
T = M K_\beta M, \qquad M(A) = \exp\!\left(\frac{\beta}{2} \sum_{p \subset \Sigma} \operatorname{Re} A_p\right), \qquad K_\beta(A, B) = \int_{\mathcal{G}} \exp\!\left(\beta \sum_{e=(x,y)\in E(\Sigma)} \operatorname{Re}\bigl(A_e g_y B_e^{-1} g_x^{-1}\bigr)\right) dg,
$$
where $\mathrm{SU}(2)$ is identified with the unit quaternions $S^3 \subset \mathbb{H}$ and $\operatorname{Re} q = \tfrac{1}{2}\operatorname{tr} q$ in the fundamental $2\times 2$ representation. Let $P_0 = \frac{1}{8}\sum_{z\in\mathbb{Z}_2^3} C_z$ project onto the centre-neutral physical subspace $\mathcal{H}_0 = P_0 \mathcal{H}$, and put $T_+ = P_0 T$, $Z^z(w) = \operatorname{Tr}_{\mathcal{H}}(C_z T^w)$, $Z_+(w) = \operatorname{Tr}_{\mathcal{H}_0}(T_+^w) = \frac{1}{8}\sum_z Z^z(w)$, and
$$
P_K = \frac{Z_+(2u)}{Z_+(u)^2}, \qquad s_+(w; n^3; \beta) = \sum_{i \ge 1} \left(\frac{\lambda_i}{\lambda_0}\right)^w,
$$
where $\lambda_0 > \lambda_1 \ge \lambda_2 \ge \cdots \ge 0$ are the eigenvalues of $T_+$ on $\mathcal{H}_0$ (simple strictly positive top eigenvector $\psi_0 > 0$, ON FILE: `library/gap-transfer.md` Lemma A3, check 1539).

**Target seed `(PUR-io)` (ON FILE: `library/gap-k2-tool-design-fable.md` §3.1, rows 1461/1462/1465, `lean/gapchain`):** $P_K \ge 457/625$ at infinitely many $K$ along the calibrated release trajectory $\beta_K$, for one $\ell \in 1024\mathbb{N}$ and one $g_0$. By Fact PUR, $P_K \ge 457/625$ gives $s_+(u; n^3; \beta_K) \le 4/21$, which is the exact neutral seed `(M-io-exists)` consumed by rows 1461/1462/1465 to produce a calibrated continuum limit with mass gap. Check 1527 (`library/gap-agy-seed-approaches-neon-check-astra62.md` §(ii)) shows that any uniform margin $P_K \ge \frac{1}{2} + \varepsilon$ suffices at a changed aspect.

**Where the 2026-11-26 band programme stands:**
- Check 1556 (`library/gap-mech-direction4-check-astra62.md` §(v), gpt-6.2-astra) constructed a deterministic, Haar-preserving, gauge-covariant, centre-commuting circle of link maps $R_s$ on a spatial cut $x_1 = 0$ reaching the centre flip $R_\pi = C_1$ a.e., yielding the four-corner identity $\int_0^\pi\int_0^\pi \partial_s\partial_t \log K_v(R_s X, R_t Y)\,ds\,dt = 2\log(K_v(X, Y)/K_v(X, C_1 Y))$.
- Rows 1565, 1566, 1568 and checks 1570, 1571, 1572 established that the resulting mixed boundary covariance lemma `BC(eps)` controls only electric-flux confinement `(N-flux)` (relative twist weights $Z^z/Z^0$), fails for interacting weak 4D compact Wilson $\mathrm{U}(1)$ (proved, row 1565 / check 1571), sits at the 4D free-field marginal power $v^{-2}$ (while passing 3D free Maxwell with $\epsilon = 1$), and is **blind to neutral sectors**: a neutral spectator leaves it unchanged while destroying purity.
- Row 1529 (`library/gap-mech-attack-fable.md` §3, Claude Fable; checked by check 1539, gpt-6.2-astra) embedded two $\mathrm{SU}(2)$ replicas in $\mathrm{Sp}(2)$ with a unit $5$-vector Higgs field so that the replica swap became conjugation by $J \in \mathrm{Sp}(2)$ on the stabilizer $H = \mathrm{SU}(2)^2$, but the twist symmetry $n \mapsto -n$ remained a discrete $\mathbb{Z}_2$ outside $\mathrm{SO}(5)$ and required sending $\kappa \to \infty$ across an uncontrolled Higgs region.
- Prior neutral replica / affinity / cross-ratio work checked before writing: row 1337 (`library/gap-solve44-astra62.md`: angular heat-flow interpolation of crossed affinity), row 1373 (`library/gap-seed3-astra62.md`: prefix affinity Gram operators), row 1207 (`library/gap-agy-solve2-argon.md` / check 1208: Doob cross-ratio), row 1402 (`library/gap-band-fresh-fable.md`: route COVER and Pin(4)), row 1016 (`library/gap-global-reform-max.md`: Lemma MC), row 1526/1527 (midpoint affinity path energy). None of the results below—Theorems 1.1–1.2, Proposition 1.3, Structures I–II (Theorems 2.1–2.3), the interacting neutral Villain $\mathrm{U}(1)$ refutation (Theorem 3.1), the diagonal Hilbert–Schmidt arc-length reductions, or Theorems 4.1–4.2—were found in `library/open-registry.md`, `parts/gap.md`, or `library/gap-*.md`.

**Credits:** ’t Hooft (electric/magnetic twists), Osterwalder–Seiler and Lüscher (reflection positivity and transfer matrix), Kotecký–Preiss / Dobrushin (strong-coupling mixing), Fröhlich–Spencer and the repository PV note (`docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md`) via row 786/794 and row 1565/1571 (interacting periodic 4D $\mathrm{U}(1)$ lower bounds), Redner–Machta–Chayes / Adhikari–Cao via rows 1099/1118/1565 (replica-exchange disagreement percolation), the OpenAI 2D $\mathrm{O}(n)$ authors (pinned-spin stiffness), and Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (the YM4 release calibration and outline).

---

## 1. Exact Classification and No-Go Theorems for Deterministic Replica-Swap Interpolations

The neutral purity is the replica-swap trace ratio
$$
P_K = \frac{Z_+(2u)}{Z_+(u)^2} = \frac{\operatorname{Tr}_{\mathcal{H}_0 \otimes \mathcal{H}_0}\bigl(\mathbb{S}\,(T_+^u \otimes T_+^u)\bigr)}{\operatorname{Tr}_{\mathcal{H}_0 \otimes \mathcal{H}_0}\bigl(T_+^u \otimes T_+^u\bigr)}, \qquad \mathbb{S}(A, B) = (B, A).
$$
Check 1556 §(v) interpolated $\mathrm{id} \to C_1$ on $\mathcal{A}$ via a local (range $1$), Haar-preserving, $(\mathcal{G} \times \mathbb{Z}_2^3)$-covariant circle action $R_s$ whose only singularities lie on a closed codimension-$3$ null set ($Q_x = \pm 1$). The first question is whether any analogous deterministic map $\Phi_s : \mathcal{A}^2 \to \mathcal{A}^2$ can interpolate $\mathrm{id} \to \mathbb{S}$ (even up to gauge and centre transformations). We prove two sharp no-go theorems showing why a direct analogue does not exist in any local gauge-descending class, and explicitly classify what happens when each hypothesis is relaxed.

### 1.1 Theorem 1.1 (Orientation Obstruction for Single-Link and Abelian Orbit Swaps) — PROVED

Let $G$ be a compact connected Lie group of **odd dimension** (including $G = \mathrm{SU}(2)$, $\dim G = 3$; $G = \mathrm{U}(1)$, $\dim G = 1$; and $G = \mathrm{SU}(2k)$, $\dim G = 4k^2 - 1$).
1. *(Single-link obstruction)* The link swap $\mathbb{S}_e : G \times G \to G \times G$, $\mathbb{S}_e(u, v) = (v, u)$, reverses orientation: $\det D\mathbb{S}_e = (-1)^{\dim G} = -1$. Consequently:
   - No continuous homotopy $\phi_s : G \times G \to G \times G$ ($s \in [0, 1]$) of homeomorphisms (in particular, no continuous circle action or connected-group action on $G \times G$) satisfies $\phi_0 = \mathrm{id}$ and $\phi_1 = \mathbb{S}_e$.
   - More generally, for any closed singular set $N \subset G \times G$ of codimension at least $2$, the complement $\Omega = (G \times G) \setminus N$ is connected and orientable, so no continuous one-parameter family of diffeomorphisms $\phi_s : \Omega \to \Omega$ satisfies $\phi_0 = \mathrm{id}_\Omega$ and $\phi_1 = \mathbb{S}_e|_\Omega$.
2. *(Global orbit-space parity split: $\mathrm{SU}(2)$ vs $\mathrm{U}(1)$)* On $\Sigma = (\mathbb{Z}/n)^3$ with $n \ge 3$ even:
   - For $G = \mathrm{U}(1)$, the gauge-orbit space $\mathcal{M}(\mathrm{U}(1)) = \mathcal{A}/\mathcal{G} \cong \mathrm{U}(1)^{|E(\Sigma)| - |V(\Sigma)| + 1} = \mathrm{U}(1)^{2n^3 + 1}$ is a smooth torus of **odd** dimension $2n^3 + 1$. Thus the global replica swap $\mathbb{S}$ on $\mathcal{M}(\mathrm{U}(1))^2$ is orientation-reversing and does not lie in the identity component of $\operatorname{Homeo}(\mathcal{M}(\mathrm{U}(1))^2)$. (By contrast, $\mathbb{S} \circ (\mathrm{id} \times \mathcal{C})$, where $\mathcal{C}(\theta) = -\theta$ is charge conjugation, has degree $(-1)^{2n^3+1}(-1)^{2n^3+1} = +1$.)
   - For $G = \mathrm{SU}(2)$, the generic gauge stabilizer is the constant centre $\{\pm 1\}$ (dimension $0$), so the smooth irreducible stratum $\mathcal{M}_{\mathrm{reg}}(\mathrm{SU}(2)) = \mathcal{A}_{\mathrm{irr}}/\mathcal{G}$ has **even** dimension $3(|E(\Sigma)| - |V(\Sigma)|) = 6n^3$, and $|E(\Sigma)| = 3n^3$ is even. Thus global orientation does not obstruct a continuous swap on $\mathcal{A}^2$ or $\mathcal{M}_{\mathrm{reg}}(\mathrm{SU}(2))^2$.

*Proof.* On any oriented $d$-manifold $M$, swapping two ordered frames of length $d$ in $T_x M \oplus T_y M$ requires $d^2$ transpositions, giving orientation sign $(-1)^{d^2} = (-1)^d$. A homotopy of homeomorphisms of a closed oriented manifold preserves its fundamental class in $H_{2d}(M \times M; \mathbb{Z}) \cong \mathbb{Z}$, hence its topological degree $+1 \neq -1$. On $\Omega = (G \times G) \setminus N$ with $\operatorname{codim}(N) \ge 2$, $\Omega$ is connected (a smooth path in $G \times G$ can be perturbed off $N$ by transversality) and inherits the orientation of $G \times G$, so the sign of the Jacobian determinant of a continuous path of diffeomorphisms $\phi_s$ on $\Omega$ is locally constant, hence $+1$ for all $s$, contradicting $\det D\mathbb{S}_e = -1$. Part (2) follows by counting dimensions: for $\mathrm{U}(1)$ the constant subgroup $\mathrm{U}(1) \subset \mathcal{G}$ acts trivially, leaving $\dim(\mathcal{A}/\mathcal{G}) = 3n^3 - (n^3 - 1) = 2n^3 + 1$; for $\mathrm{SU}(2)$ the constant centre $\{\pm 1\}$ has dimension $0$, leaving $3(3n^3 - n^3) = 6n^3$. $\blacksquare$

### 1.2 Theorem 1.2 (Exact 1-Form Cohomology Obstruction to Local Gauge-Descending Replica-Swap Interpolations) — PROVED

Although global orientation does not obstruct a swap of $\mathrm{SU}(2)$ replicas on $\Sigma = (\mathbb{Z}/n)^3$, **1-form centre cohomology** obstructs *every* finite-range, gauge-orbit-descending, regular deterministic interpolation between $\mathrm{id}$ and $\mathbb{S}$.

Let $\Sigma = (\mathbb{Z}/n)^3$ and $G = \mathrm{SU}(2)$. Say a map $\Phi : \mathcal{A}^2 \to \mathcal{A}^2$ has **range at most $R$** if for every spatial edge $e = (u, v) \in E(\Sigma)$, the output link pair $\Phi(A, B)_e$ depends only on the input links $(A_{e'}, B_{e'})$ whose endpoints lie in $B_R(u) \cup B_R(v)$ (in $\ell_\infty$ periodic distance on $\Sigma$). Write $\mathcal{G}_+ := \mathcal{G} \times \mathbb{Z}_2^3$ for the group generated by vertex gauge transformations and centre translations on one replica (the exact symmetry group of the neutral transfer kernel $K_v^+$).

**Theorem 1.2 (PROVED).** *Let $R \ge 0$ and $n \ge 2R + 7$. There exists **no** measurable family of maps $\Phi_s = (\Phi_s^{(1)}, \Phi_s^{(2)}) : \mathcal{A}^2 \to \mathcal{A}^2$ ($s \in [0, \pi]$) satisfying all four conditions:*
1. **(Finite range)** *For every $s \in [0, \pi]$, $\Phi_s$ has range at most $R$.*
2. **(Descent under local $\mathbb{Z}_2$ vertex gauge maps)** *For every $s \in [0, \pi]$ and every $\tau \in \{\pm 1\}^{V(\Sigma)} \subset \mathcal{G}$ acting on replica 1, $\Phi_s(\tau \cdot A, B) \in (\mathcal{G}_+ \times \mathcal{G}_+) \cdot \Phi_s(A, B)$ for Haar-almost every $(A, B) \in \mathcal{A}^2$.*
3. **(Haar domination and Hölder continuity in $s$)** *There exists $C < \infty$ such that $(\Phi_s^{(1)})_* \mu_{\mathrm{Haar}}^{\otimes 2} \le C \mu_{\mathrm{Haar}}$ for every $s \in [0, \pi]$ (in particular, Haar preservation holds with $C = 1$), and for Haar-almost every $(A, B) \in \mathcal{A}^2$ the map $s \mapsto \Phi_s^{(1)}(A, B)$ is $\alpha$-Hölder continuous with some exponent $\alpha > 1/10$ (in particular, Lipschitz or $C^1$).*
4. **(Endpoints)** *For Haar-almost every $(A, B) \in \mathcal{A}^2$, $\Phi_0^{(1)}(A, B) \in \mathcal{G}_+ \cdot A$ and $\Phi_\pi^{(1)}(A, B) \in \mathcal{G}_+ \cdot B$. (In particular, arbitrary field-dependent endpoint gauge transformations and centre twists are permitted, and no condition on $\Phi_s^{(2)}$ is needed. If the endpoint centre twists are fixed, it suffices that this holds on any set $E_0 \subset \mathcal{A}^2$ with $\mu_{\mathrm{Haar}}^{\otimes 2}(E_0 \cap (C_{e_1} \times \mathrm{id})^{-1}(E_0)) > 0$, e.g. any set of measure $> 1/2$.)*

*Proof.* Equip $\mathrm{SU}(2) = S^3 \subset \mathbb{H} \cong \mathbb{R}^4$ with the quaternion Euclidean metric $|q - q'|$, and $\mathcal{A}$ with $\operatorname{dist}_{\max}(U, U') = \max_{e \in E(\Sigma)} |U_e - U'_e|$. Define the **locally irreducible stratum** $\mathcal{A}_{\mathrm{irr}} \subset \mathcal{A}$ to be the open set of configurations $U \in \mathcal{A}$ such that at every vertex $x \in V(\Sigma)$, the six spatial plaquettes based at $x$ in the positive and negative octants,
$$
Q_{x, +12},\; Q_{x, +23},\; Q_{x, +31},\; Q_{x, -12},\; Q_{x, -23},\; Q_{x, -31},
$$
do not all commute (equivalently, their six imaginary parts $\operatorname{Im} Q \in \mathbb{R}^3$ are not all collinear). Set $\mathcal{B} := \mathcal{A} \setminus \mathcal{A}_{\mathrm{irr}}$.

**Step 1 (Codimension-$10$ Haar-tube bound on $\mathcal{B}$).** Fix $x \in V(\Sigma)$. Notice that the six "far" edges $(x+\hat 1, x+\hat 1+\hat 2)$, $(x+\hat 2, x+\hat 2+\hat 3)$, $(x+\hat 3, x+\hat 3+\hat 1)$ and $(x-\hat 1, x-\hat 1-\hat 2)$, $(x-\hat 2, x-\hat 2-\hat 3)$, $(x-\hat 3, x-\hat 3-\hat 1)$ are six distinct links, each belonging to exactly one of the six plaquettes above (since $n \ge 3$). Conditioning on all other links of $\mathcal{A}$ and varying these six links by Haar measure shows that the six plaquette holonomies $(q_1, \dots, q_6)$ are independent Haar elements of $\mathrm{SU}(2)$.

Let $\mathcal{C}_6 \subset \mathrm{SU}(2)^6$ be the closed set of $6$-tuples with collinear imaginary parts, and let $\delta > 0$. If $(q_1, \dots, q_6)$ satisfies $\max_a |q_a - q'_a| \le \delta$ for some $(q'_1, \dots, q'_6) \in \mathcal{C}_6$ sharing a unit axis $u \in S^2$, then $v_a := \operatorname{Im} q_a \in \mathbb{R}^3$ ($r_a := |v_a| \le 1$) satisfies $|v_a - (v_a \cdot u)u| \le |v_a - \operatorname{Im} q'_a| \le \delta$ for all $a = 1, \dots, 6$. Let $a_*$ maximize $r_a$.
- If $r_{a_*} \le 2\delta$, then all six $r_a \le 2\delta$. Since the Haar pushforward density of $v_a = \operatorname{Im} q_a$ on the unit $3$-ball is $\pi^{-2}(1 - |v_a|^2)^{-1/2}\,d^3v_a$ (summing the two hemispheres $\operatorname{Re} q_a = \pm\sqrt{1 - |v_a|^2}$), $\mathbb{P}(r_a \le 2\delta) \le C_0 \delta^3$, giving probability $\le (C_0 \delta^3)^6 = C_0^6 \delta^{18}$.
- If $r_{a_*} > 2\delta$, then $\sin\angle(\hat v_{a_*}, u) \le \delta / r_{a_*}$, and the orthogonal projections satisfy $\|P_{\hat v_{a_*}}^\perp - P_u^\perp\|_{\mathrm{op}} = \sin\angle(\hat v_{a_*}, u)$, so for every $b \neq a_*$,
  $$
  \bigl|v_b - (v_b \cdot \hat v_{a_*})\hat v_{a_*}\bigr| \le \bigl|v_b - (v_b \cdot u)u\bigr| + r_b \sin\angle(\hat v_{a_*}, u) \le \delta + r_b \frac{\delta}{r_{a_*}} \le 2\delta.
  $$
  Conditional on $q_{a_*}$, the remaining five $q_b$ are independent Haar, and each falls in the cylinder of radius $2\delta$ around $\mathbb{R}\hat v_{a_*}$ inside the unit $3$-ball. Integrating the Haar density $\pi^{-2}(1 - z^2 - \rho^2)^{-1/2}$ over this cylinder in cylindrical coordinates $(z, \rho)$ gives
  $$
  \frac{1}{\pi^2} \int_{-1}^1 dz \int_0^{\min(2\delta, \sqrt{1-z^2})} \frac{2\pi\rho\,d\rho}{\sqrt{1 - z^2 - \rho^2}}
  = \frac{2}{\pi} \int_{-1}^1 \left(\sqrt{1-z^2} - \sqrt{\max(0, 1 - z^2 - 4\delta^2)}\right) dz \le C_1 \delta^2,
  $$
  where the last inequality splits into $1 - z^2 \le 4\delta^2$ (integral $O(\delta^3)$) and $1 - z^2 > 4\delta^2$ (using $\sqrt{t} - \sqrt{t - 4\delta^2} \le 4\delta^2/\sqrt{t}$ and $\int_0^1 (t(1-t))^{-1/2}\,dt = \pi$). By independence of the five $q_b$ ($b \neq a_*$) and a union bound over the $6$ choices of $a_*$ and $n^3$ vertices $x$,
  $$
  \mu_{\mathrm{Haar}}\bigl(\mathcal{N}_\varepsilon(\mathcal{B})\bigr) \le C_2 n^3 \varepsilon^{10} \qquad (\varepsilon > 0),
  $$
  since each plaquette holonomy is $4$-Lipschitz in $\operatorname{dist}_{\max}$ (taking $\delta = 4\varepsilon$).

**Step 2 (Almost every orbit stays in $\mathcal{A}_{\mathrm{irr}}$ for all $s \in [0, \pi]$).** Let $L(A, B) < \infty$ be the $\alpha$-Hölder constant of $s \mapsto \Phi_s^{(1)}(A, B)$ in $\operatorname{dist}_{\max}$, and put $E_M = \{(A, B) : L(A, B) \le M\}$. For any integer $N \ge 1$ and grid points $s_k = k\pi/N$ ($0 \le k \le N$), if $(A, B) \in E_M$ and $\Phi_s^{(1)}(A, B) \in \mathcal{B}$ for some $s \in [0, \pi]$, then choosing $k$ with $|s - s_k| \le \pi/(2N)$ gives $\Phi_{s_k}^{(1)}(A, B) \in \mathcal{N}_{\varepsilon_N}(\mathcal{B})$ with $\varepsilon_N = M(\pi/(2N))^\alpha$. By hypothesis (3),
$$
\mu_{\mathrm{Haar}}^{\otimes 2}\bigl(\{(A, B) \in E_M : \exists s \in [0, \pi],\; \Phi_s^{(1)}(A, B) \in \mathcal{B}\}\bigr)
\le \sum_{k=0}^N C\,\mu_{\mathrm{Haar}}\bigl(\mathcal{N}_{\varepsilon_N}(\mathcal{B})\bigr)
\le C C_2 n^3 (N+1) M^{10} \left(\frac{\pi}{2N}\right)^{10\alpha}.
$$
Since $\alpha > 1/10$, letting $N \to \infty$ gives measure zero for every $M \ge 1$. Taking $\bigcup_{M=1}^\infty E_M$ yields a full-measure set $\Omega_1 \subset \mathcal{A}^2$ on which $\Phi_s^{(1)}(A, B) \in \mathcal{A}_{\mathrm{irr}}$ for **every** $s \in [0, \pi]$.

**Step 3 (Local gauge equivalence under $C_{e_1}$ at all $s \in [0, \pi]$).** For each vertex $x_0 \in V(\Sigma)$, let $U(x_0) = \{y \in V(\Sigma) : \|y - x_0\|_\infty \le 2\}$ (with all edges having both endpoints in $U(x_0)$). By hypothesis (1), $\Phi_s^{(1)}|_{U(x_0)}$ depends only on input links with both endpoints in $B_{R+2}(x_0)$, whose first coordinates span at most $2R + 5$ consecutive residues modulo $n$. If either $0$ or $1$ is absent from these first coordinates, no $1$-link at $x_1 = 0$ has both endpoints in $B_{R+2}(x_0)$, so $\tau^{(x_0)} \equiv +1$ already satisfies $(\tau^{(x_0)} \cdot A)_e = (C_{e_1} A)_e$ on every link in $B_{R+2}(x_0)$. Otherwise both $0$ and $1$ lie in this span; since $n \ge 2R + 7$, there exist two adjacent slices $c, c+1 \pmod n$ disjoint from $B_{R+2}(x_0)$ (necessarily $c \in \{2, \dots, n - 2\}$), and defining $\tau^{(x_0)} \in \{\pm 1\}^{V(\Sigma)}$ equal to $-1$ on $\{1, \dots, c\}$ and $+1$ on the complement flips only the $1$-links at $x_1 = 0$ and at $x_1 = c$ (the latter disjoint from $B_{R+2}(x_0)$), so again $(\tau^{(x_0)} \cdot A)_e = (C_{e_1} A)_e$ on every link in $B_{R+2}(x_0)$.

Let $Q = ([0, \pi] \cap \mathbb{Q}) \cup \{0, \pi\}$. By hypothesis (2) and countability of $Q \times V(\Sigma)$, there is a full-measure set $\Omega_2 \subset \mathcal{A}^2$ on which, for every $s \in Q$ and every $x_0 \in V(\Sigma)$, $\Phi_s^{(1)}(\tau^{(x_0)} \cdot A, B) \in \mathcal{G}_+ \cdot \Phi_s^{(1)}(A, B)$. On $U(x_0)$ (diameter $4 < n$), any centre twist $C_z$ is itself equal to a $\mathbb{Z}_2$ vertex gauge transformation on $U(x_0)$. Therefore, on $\Omega_2$, for every $s \in Q$ and every $x_0 \in V(\Sigma)$ there exists $h^{(x_0)}(s) \in \mathrm{SU}(2)^{U(x_0)}$ such that
$$
\Phi_s^{(1)}(C_{e_1} A, B)\big|_{U(x_0)} = \Phi_s^{(1)}(\tau^{(x_0)} \cdot A, B)\big|_{U(x_0)} = \bigl(h^{(x_0)}(s) \cdot \Phi_s^{(1)}(A, B)\bigr)\big|_{U(x_0)}. \tag{1.1}
$$
On the full-measure set $\Omega_3 = \Omega_1 \cap (C_{e_1} \times \mathrm{id})^{-1}(\Omega_1) \cap \Omega_2$, both $A^{(s)} := \Phi_s^{(1)}(A, B)$ and $A'^{(s)} := \Phi_s^{(1)}(C_{e_1} A, B)$ are continuous in $s \in [0, \pi]$; by compactness of $\mathrm{SU}(2)^{U(x_0)}$ and density of $Q$ in $[0, \pi]$, (1.1) extends to **every** $s \in [0, \pi]$.

**Step 4 (Local rigidity and constant cohomology class $w_1(s) \in H^1(\Sigma; \mathbb{Z}_2)$).** Fix $(A, B)$ in the full-measure intersection $\Omega_3 \cap E_0 \cap (C_{e_1} \times \mathrm{id})^{-1}(E_0)$ (where $E_0$ is the endpoint set of hypothesis (4); in the fixed-twist case, any point of $\Omega_3 \cap E_0 \cap (C_{e_1} \times \mathrm{id})^{-1}(E_0)$ suffices). For any $s \in [0, \pi]$ and any adjacent vertices $x, y \in V(\Sigma)$, both $B_1(x)$ and $B_1(y)$ lie inside $U(x) \cap U(y)$ (since $\|z - y\|_\infty \le 1 \implies \|z - x\|_\infty \le 2$). On $U(x) \cap U(y)$, the ratio $g = (h^{(x)}(s))^{-1} h^{(y)}(s)$ fixes $A^{(s)}$. In particular, $g_x$ commutes with all six based plaquettes of $A^{(s)}$ at $x$, and $g_y$ with all six at $y$. Because $A^{(s)} \in \mathcal{A}_{\mathrm{irr}}$ and the centralizer of two non-commuting elements of $\mathrm{SU}(2)$ is $\{\pm 1\}$, we obtain $g_x, g_y \in \{\pm 1\}$; the edge equation $g_x A^{(s)}_{x,y} g_y^{-1} = A^{(s)}_{x,y}$ then forces $g_x = g_y =: \sigma_{xy}(s) \in \{\pm 1\}$.

Put $H_x(s) := h^{(x)}(s)(x) \in \mathrm{SU}(2)$. Then $H_y(s) = h^{(y)}(s)(y) = \sigma_{xy}(s)\, h^{(x)}(s)(y)$, so on every directed edge $e = (x, y) \in E(\Sigma)$,
$$
A'^{(s)}_{x,y} = \sigma_{xy}(s)\, H_x(s) A^{(s)}_{x,y} H_y(s)^{-1}. \tag{1.2}
$$
Around any elementary plaquette $p$ based at $x$, all four edges of $p$ lie in $U(x)$, so $\operatorname{Hol}_p(A'^{(s)}) = H_x(s)\operatorname{Hol}_p(A^{(s)}) H_x(s)^{-1}$, while (1.2) multiplies this by $\prod_{e \in \partial p} \sigma_e(s)$. Hence $\prod_{e \in \partial p} \sigma_e(s) = +1$ for every plaquette $p$: $\sigma(s)$ is a closed $\mathbb{Z}_2$ $1$-cocycle on $\Sigma$, defining a cohomology class $w_1(s) \in H^1(\Sigma; \mathbb{Z}_2) \cong \mathbb{Z}_2^3$.

We show $w_1(s)$ is locally constant in $s \in [0, \pi]$. Fix $s_0 \in [0, \pi]$. At each site $x$, because $A^{(s_0)} \in \mathcal{A}_{\mathrm{irr}}$, pick two of its six based plaquettes whose imaginary parts are linearly independent; by continuity in $s$, they stay linearly independent on a common open interval $I \subset [0, \pi]$ containing $s_0$ for all $x \in V(\Sigma)$. Gram–Schmidt orthonormalization of those two plaquettes in $A^{(s)}$ and $A'^{(s)}$ determines $\operatorname{Ad}(H_x(s)) \in \mathrm{SO}(3)$ continuously on $I$. Since $I$ is simply connected, this lifts to a continuous path $\widetilde{H}_x(s) \in \mathrm{SU}(2)$ on $I$, differing from $H_x(s)$ by a vertex sign $\eta_x(s) \in \{\pm 1\}$. Replacing $H_x$ by $\widetilde{H}_x$ modifies $\sigma_{xy}(s)$ only by the coboundary $\eta_x(s)\eta_y(s)$, leaving $w_1(s)$ unchanged, while the modified cocycle
$$
\widetilde{\sigma}_{xy}(s) = \operatorname{Re}\!\left(A'^{(s)}_{x,y}\, \widetilde{H}_y(s) (A^{(s)}_{x,y})^{-1} \widetilde{H}_x(s)^{-1}\right) \in \{+1, -1\}
$$
is continuous on $I$, hence constant on $I$. Thus $w_1(s)$ is locally constant, hence constant on $[0, \pi]$:
$$
w_1(0) = w_1(\pi) \in \mathbb{Z}_2^3. \tag{1.3}
$$

**Step 5 (Endpoint contradiction, including field-dependent endpoint twists).** If the endpoint centre twists $z_0, z_\pi \in \mathbb{Z}_2^3$ are fixed on $E_0$, then on $\Omega_3 \cap E_0 \cap (C_{e_1} \times \mathrm{id})^{-1}(E_0)$ we immediately have $w_1(0) = e_1$ and $w_1(\pi) = 0$, contradicting (1.3).

When arbitrary field-dependent endpoint twists $z_0(A, B), z_\pi(A, B) \in \mathbb{Z}_2^3$ are permitted on the full-measure set $E_0$, we rule out $A$-dependence by single-link induction. Let $e_1, \dots, e_{n^2}$ be the $1$-links on the cut $x_1 = 0$, and let $F_j : \mathcal{A} \to \mathcal{A}$ flip the sign of $e_j$ only (so $C_{e_1} = F_{n^2} \circ \dots \circ F_1$). Because each $F_j \times \mathrm{id}$ preserves Haar measure, the finite intersection
$$
\widetilde{\Omega} := \Omega_3 \cap \bigcap_{S \subset \{1, \dots, n^2\}} \left(\Bigl(\prod_{j \in S} F_j\Bigr) \times \mathrm{id}\right)^{-1}(\Omega_1 \cap E_0)
$$
has full Haar measure. Fix $(A, B) \in \widetilde{\Omega}$ and put $A^{(k)} = F_k \cdots F_1 A$ ($0 \le k \le n^2$). For each $k$, $A^{(k)}$ and $A^{(k-1)}$ differ only on the single link $e_k$, so $\Phi_\pi^{(1)}(A^{(k)}, B)$ and $\Phi_\pi^{(1)}(A^{(k-1)}, B)$ agree on every link having both endpoints outside $B_R(e_k)$. Since $n \ge 2R + 7$, for each coordinate direction $i \in \{1, 2, 3\}$ there is a coordinate winding loop $\gamma_i$ whose $1$-neighborhood $B_1(\gamma_i)$ is disjoint from $B_R(e_k)$ (as $B_R(e_k)$ spans at most $2R + 2$ consecutive sites in each transverse direction, $B_1(\gamma_i)$ spans $3$, and $2R + 5 < n$). Writing $U = \Phi_\pi^{(1)}(A^{(k-1)}, B) \in \mathcal{A}_{\mathrm{irr}}$ (by $\Omega_1$) and $U' = \Phi_\pi^{(1)}(A^{(k)}, B) = C_{\Delta z_k}(h_k \cdot U)$ with $\Delta z_k = z_\pi(A^{(k)}, B) - z_\pi(A^{(k-1)}, B)$, equality $U' = U$ on $B_1(\gamma_i)$ preserves all six based plaquettes at every $x \in \gamma_i$ (as $C_{\Delta z_k}$ is flat), forcing $h_{k, x} \in \{\pm 1\}$ at every vertex $x \in \gamma_i$ by local rigidity of $\mathcal{A}_{\mathrm{irr}}$. Multiplying the edge relations along $\gamma_i$, the vertex signs cancel in pairs, yielding $\operatorname{Hol}_{\gamma_i}(U) = \operatorname{Hol}_{\gamma_i}(U') = (-1)^{(\Delta z_k)_i} \operatorname{Hol}_{\gamma_i}(U)$, so $(\Delta z_k)_i = 0$ for $i = 1, 2, 3$. Inducting over $k = 1, \dots, n^2$ gives $z_\pi(C_{e_1} A, B) = z_\pi(A, B)$, hence $w_1(\pi) = 0$. The identical single-link induction applied to $s = 0$ gives $z_0(C_{e_1} A, B) = z_0(A, B)$, hence $w_1(0) = e_1$ (since $C_{e_1} A$ itself adds $e_1$). Thus $e_1 = w_1(0) = w_1(\pi) = 0$, contradiction. $\blacksquare$

**Corollary 1.2' (Compact $\mathrm{U}(1)$ vs Noncompact Free Maxwell, PROVED).**
- *Compact $\mathrm{U}(1)$:* If $\Phi_s : \mathrm{U}(1)^{E(\Sigma)} \times \mathrm{U}(1)^{E(\Sigma)} \to \mathrm{U}(1)^{E(\Sigma)} \times \mathrm{U}(1)^{E(\Sigma)}$ is continuous in $(s, A, B)$, has range $R$ ($n \ge 2R + 7$), descends to $(\mathcal{G} \times \mathcal{G})$-orbits, and connects $\mathrm{id}$ to $\mathbb{S}$ (or $\mathbb{S} \circ (\mathrm{id} \times \mathcal{C})$), then applying a continuous flat $\mathrm{U}(1)$ cut twist $C_\alpha$ ($\alpha \in \mathbb{R}/2\pi\mathbb{Z}$) to replica 1 induces a continuous family of cohomology maps $\alpha \mapsto w_1(s, \alpha) \in H^1(\Sigma; \mathrm{U}(1)) \cong (S^1)^3$ whose winding degree along the first circle $d_1(s) \in \pi_1(S^1) = \mathbb{Z}$ is continuous in $s$, hence constant; yet $d_1(0) = 1$ while $d_1(\pi) = 0$, contradiction.
- *Noncompact free Maxwell ($G = \mathbb{R}$):* Since $\pi_1(\mathbb{R}) = 0$, the obstruction vanishes, and the link-local ($R = 0$) $\mathrm{SO}(2)$ replica rotation $(A_1, A_2) \mapsto (\cos s\, A_1 + \sin s\, A_2,\; -\sin s\, A_1 + \cos s\, A_2)$ preserves Lebesgue measure, descends to $(\mathcal{G} \times \mathcal{G})$-orbits, and connects $\mathrm{id}$ to $(\mathrm{id} \times \mathcal{C}) \circ \mathbb{S}$ at $s = \pi/2$.
- *Contrast with check 1556's cut rotation $R_s$:* For $R_s : \mathcal{A} \to \mathcal{A}$ (one replica, $\mathrm{id} \to C_1$), the induced action on $C_{e_1}$ stays $w(s) \equiv e_1$ at both $s = 0$ and $s = \pi$, so no cohomology jump occurs.

### 1.3 Escaping Locality Only vs Escaping Continuity Only (Two Dead Ends Recorded)

Theorem 1.2 acts as a structural compass: any interpolation reading $P_K = Z_+(2u)/Z_+(u)^2$ must relax at least one of (1) finite range, (2) $(\mathcal{G}_+ \times \mathcal{G}_+)$-descent at intermediate $s$, (3) staying in $\mathcal{A}_{\mathrm{irr}}$ with a deterministic link map, or (4) continuity in $s$. Before presenting the two viable structures in Section 2, we record why relaxing (1) alone or (4) alone fails analytically.

**Proposition 1.3 (Global Comb-Tree Circle Action $\Phi_s^{\mathrm{tree}}$, PROVED).** *On $\Sigma = (\mathbb{Z}/n)^3$ ($n \ge 4$ even), there exists an explicit deterministic, Haar-preserving, $(\mathcal{G}_+ \times \mathcal{G}_+)$-orbit-descending Borel circle action $\Phi_s^{\mathrm{tree}} : \mathcal{A}^2 \to \mathcal{A}^2$ ($s \in \mathbb{R}/2\pi\mathbb{Z}$) such that $\Phi_0^{\mathrm{tree}} = \mathrm{id}$, $\Phi_s^{\mathrm{tree}}\Phi_t^{\mathrm{tree}} = \Phi_{s+t}^{\mathrm{tree}}$, and $\Phi_\pi^{\mathrm{tree}}(A, B) \in (\mathcal{G}_+ \times \mathcal{G}_+) \cdot (B, A)$ for Haar-almost every $(A, B)$. Consequently, its unitary pullback $U_s$ on $\mathcal{H}_0 \otimes \mathcal{H}_0$ satisfies*
$$
H^{\mathrm{tree}}(s; u) := \operatorname{Tr}_{\mathcal{H}_0 \otimes \mathcal{H}_0}\!\bigl(U_s (T_+^u \otimes T_+^u)\bigr), \qquad H^{\mathrm{tree}}(0; u) = Z_+(u)^2, \qquad H^{\mathrm{tree}}(\pi; u) = Z_+(2u).
$$
*Proof (construction).* Fix the coordinate comb spanning tree $T \subset E(\Sigma)$ rooted at $x_0 = (0, 0, 0)$ (decreasing the highest nonzero coordinate of each vertex; cf. check 1527 §(iii)). On $\mathcal{A}/\mathcal{G}$, represent the centre translations $C_z$ on the wrapping links $x_i = n - 1 \to 0$ (gauge-equivalent to $x_i = 0 \to 1$, and completely disjoint from $T$). For $A \in \mathcal{A}$, let $P_x(A) \in \mathrm{SU}(2)$ be the tree transport from $x_0$ to $x$, and $W_e(A) = P_x(A) A_e P_y(A)^{-1}$ ($e \in E \setminus T$, $|E \setminus T| = 2n^3 + 1$). Under Haar measure $dA$, the $n^3 - 1$ tree links and $2n^3 + 1$ chords $W_e$ are independent Haar. Pick the two non-wrapping plaquette chords $e_1 = ((0,1,0),(1,1,0))$ and $e_2 = ((0,0,1),(0,1,1))$ (whose other three edges lie in $T$) to define a Borel root frame $u_{x_0}(A) \in \mathrm{SU}(2)/\{\pm 1\} = \mathrm{SO}(3)$ via Gram–Schmidt on $(\operatorname{Im} W_{e_1}, \operatorname{Im} W_{e_2})$, leaving three mutually independent gauge-and-centre-invariant angle coordinates $(\theta_1, \theta_2, \phi) \in (0, \pi)^3$ and $2n^3 - 1$ conjugated chords $\widehat{W}_k = u_{x_0}^{-1} W_{e_k} u_{x_0} \in \mathrm{SU}(2)$ that are strictly $\mathcal{G}$-invariant and conditionally independent Haar. Because $C_z$ acts solely on the wrapping chords, in each direction $i \in \{1, 2, 3\}$ fix one reference wrapping chord $\widehat{W}_{*, i}$, let $\sigma_i = \operatorname{sgn}(\operatorname{Re} \widehat{W}_{*, i}) \in \{\pm 1\}$ (a.e.), and replace all $n^2$ direction-$i$ wrapping chords by $\sigma_i \widehat{W}_e$; then each $\widehat{W}_{*, i}$ lies in the open upper hemisphere $H_+ = \{q \in S^3 : \operatorname{Re} q > 0\}$ (Haar-uniform on $H_+$) and all remaining $2n^3 - 4$ chords are strictly $\mathcal{G}_+$-invariant and independent Haar on $S^3$. Thus the open full-measure neutral orbit space $\mathcal{M}_+^{\mathrm{open}} \subset \mathcal{A}_{\mathrm{reg}}/\mathcal{G}_+$ has even dimension $3 + 9 + 3(2n^3 - 4) = 6n^3$ and admits an explicit product measure-preserving smooth diffeomorphism $\eta : \mathcal{M}_+^{\mathrm{open}} \to \mathbb{C}^{3n^3}$ (equipped with standard complex Gaussian measure $\gamma_{\mathbb{C}^{3n^3}}$) constructed factorwise from 1D quantile maps on $(0, \pi)^3$, $H_+^3 \cong (\mathbb{R}^3)^3$, and $(S^3 \setminus \{-1\})^{2n^3 - 4} \cong (\mathbb{R}^3)^{2n^3 - 4}$ paired into $\mathbb{C}^{3n^3}$. On $\mathbb{C}^{3n^3} \times \mathbb{C}^{3n^3}$, define the $\mathrm{U}(2)$ circle action
$$
U_s(z_A, z_B) := \left(\frac{1 + e^{is}}{2}\,z_A + \frac{1 - e^{is}}{2}\,z_B,\;\; \frac{1 - e^{is}}{2}\,z_A + \frac{1 + e^{is}}{2}\,z_B\right),
$$
which preserves $\gamma_{\mathbb{C}^{3n^3}}^{\otimes 2}$, satisfies $U_0 = \mathrm{id}$, $U_s U_t = U_{s+t}$, $U_{2\pi} = \mathrm{id}$, and $U_\pi(z_A, z_B) = (z_B, z_A)$. Pulling $U_s$ back via $\eta$ while keeping the tree links, root frames $u_{x_0}(A), u_{x_0}(B)$, and centre signs $\sigma_i(A), \sigma_i(B)$ fixed defines $\Phi_s^{\mathrm{tree}}$ with all stated properties. $\blacksquare$

*Why Proposition 1.3 is analytically dead (ARGUED):* Because $\Phi_s^{\mathrm{tree}}$ acts through comb-tree transports of length $O(n)$, moving a single coordinate changes spatial plaquettes across the entire slice, producing an $O(\beta n^3)$ spatial wall (worse than check 1556's $O(\beta n^2)$ wall), singularities at the codimension-$1$ hemisphere cut loci $\operatorname{Re} \widehat{W}_{*, i} = 0$ and the collinearity locus $\sin\phi = 0$, and no local Gibbs covariance representation. It is also completely blind to the Lie group and the dimension.

**Remark 1.4 (Breaking continuity in $s$: discrete spatial branched cover / Rényi-2 sweep, ARGUED).** Swapping replicas 1 and 2 across the seam $\tau = u-1 \to 0$ on an expanding slab $\Lambda_k = \{0 \le x_1 < k\}$ ($k = 0, \dots, n$) is strictly $(\mathcal{G} \times \mathcal{G})$-gauge invariant for every $k$: temporal plaquettes straddling $\partial \Lambda_k$ close after two circuits as $8$-link plaquettes around the codimension-$2$ branch planes $\{x_1 = 0, k\} \times \{\tau = u - 1/2\}$. However, for every $1 \le k \le n - 1$, the $2n^2$ branch plaquettes incur an extensive UV entanglement area-law free energy $e^{-c(\beta) n^2}$ that buries the $O(1)$ purity $P_K$ until the two walls annihilate at $k = n$.

---

## 2. Two Exact, Local, Zero-Wall Structures Escaping Theorem 1.2

Theorem 1.2 leaves two clean, local, zero-wall mechanisms that directly read the neutral sector:
- **Structure I** relaxes $(\mathcal{G} \times \mathcal{G})$-invariance *strictly at two antipodal temporal seams* by realizing the replica swap through the connected subgroup $\mathrm{SO}(2) \subset \mathrm{Sp}(2)$ (resolving row 1529's disconnected $\mathbb{Z}_2$ without any Higgs field or extra bulk variables).
- **Structure II** preserves **100% exact $(\mathcal{G} \times \mathbb{Z}_2^3)$ gauge and centre invariance** on a **single replica**, escaping Theorem 1.2 by scaling the temporal coupling of two antipodal layers linearly through $0 \in B^4 \subset \mathbb{H}$.

Both yield **unpinned**, translation-invariant, cubic-symmetric four-corner covariance identities and **exact 1-parameter reflection-positive diagonal Hilbert–Schmidt arc-length bounds**.

### 2.1 Structure I: Connected-Group $\mathrm{SO}(2) \subset \mathrm{Sp}(2)$ Two-Seam Interpolation

Embed two $\mathrm{SU}(2)$ link fields $(U^{(1)}, U^{(2)})$ into the connected compact group $\mathrm{Sp}(2)$ ($2 \times 2$ unitary quaternionic matrices, with normalized real trace $\chi(g) = \operatorname{Re}(g_{11} + g_{22})$) as block-diagonal matrices $\mathbf{U}_b = \operatorname{diag}(U^{(1)}_b, U^{(2)}_b) \in H = \mathrm{SU}(2) \times \mathrm{SU}(2)$. Consider the real $\mathrm{SO}(2)$ circle subgroup inside $\mathrm{Sp}(2)$:
$$
R_s := \begin{pmatrix} \cos s & -\sin s \\ \sin s & \cos s \end{pmatrix} \in \mathrm{SO}(2) \subset \mathrm{Sp}(2), \qquad R_0 = I, \qquad R_{\pi/2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.
$$
Conjugation by $R_s$ preserves $\mathrm{Sp}(2)$ and satisfies
$$
R_s \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix} R_s^{-1}
= \begin{pmatrix} \cos^2 s\, a + \sin^2 s\, b & \sin s \cos s\,(a - b) \\ \sin s \cos s\,(a - b) & \sin^2 s\, a + \cos^2 s\, b \end{pmatrix},
\qquad R_{\pi/2} \operatorname{diag}(a, b) R_{\pi/2}^{-1} = \operatorname{diag}(b, a). \tag{2.1}
$$
Notice that $R_{\pi/2}$ implements the **exact replica swap** inside the identity component of $\mathrm{Sp}(2)$, with no sign flips and no auxiliary Higgs field. Moreover, because conjugation by a constant $R_s$ is a group homomorphism, the spatial plaquette trace $\chi(\operatorname{Hol}_p(R_s \mathbf{X} R_s^{-1})) = \operatorname{Re} X_{1,p} + \operatorname{Re} X_{2,p}$ is identically independent of $s$ (zero spatial wall energy).

**Key algebraic factorization across a diagonal temporal step.** Let $\mathbf{X}_e = \operatorname{diag}(X_{1,e}, X_{2,e})$ sit on slice $\tau = 0$ and let the temporal-plaquette staple $\mathbf{W}_{0,e} = \operatorname{diag}(W_{1,0,e}, W_{2,0,e})$ (with $W_{a,0,e} = V_{a,0,y} (X'_{a,e})^{-1} V_{a,0,x}^{-1} \in \mathrm{SU}(2)$) live in pure $H = \mathrm{SU}(2)^2$. Because $\mathbf{W}_{0,e}$ is block-diagonal, the off-diagonal blocks of $R_s \mathbf{X}_e R_s^{-1}$ drop out identically from $\chi$: putting $\lambda := \sin^2 s \in [0, 1]$,
$$
\beta\,\chi\bigl((R_s \mathbf{X}_e R_s^{-1})\mathbf{W}_{0,e}\bigr)
= (1 - \lambda)\beta\bigl(\operatorname{Re}(X_{1,e} W_{1,0,e}) + \operatorname{Re}(X_{2,e} W_{2,0,e})\bigr)
+ \lambda\beta\bigl(\operatorname{Re}(X_{2,e} W_{1,0,e}) + \operatorname{Re}(X_{1,e} W_{2,0,e})\bigr)
= s_{\mathrm{dir},0,e} + \lambda\,\mathcal{F}_{0,e}, \tag{2.2}
$$
where
$$
\mathcal{F}_{0,e} := \beta \operatorname{Re}\!\Bigl((X_{2,e} - X_{1,e})(W_{1,0,e} - W_{2,0,e})\Bigr), \qquad |\mathcal{F}_{0,e}| \le 4\beta.
$$

**Definition (Two-Seam Partition Function $Z_{\mathrm{2seam}}(\lambda, \mu; u)$).** On two copies of $\Lambda = (\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ ($u = 2v$, $v \ge 3$), keep unmodified decoupled Wilson actions on all spatial slices and all temporal layers $\tau \notin \{0, v\}$; replace the temporal plaquette weights on **Seam 1** ($\tau = 0 \to 1$) by (2.2) with parameter $\lambda \in [0, 1]$, and on **Seam 2** ($\tau = v \to v+1$) by the identical expression with parameter $\mu \in [0, 1]$ and derivative $\mathcal{F}_{v, e'}$. Insert four independent centre twists $(z_1, z_2, z'_1, z'_2) \in (\mathbb{Z}_2^3)^4$ on the interior midpoint layers $\tau = \lfloor v/2 \rfloor \to \lfloor v/2 \rfloor + 1$ (replicas 1, 2) and $\tau = v + \lfloor v/2 \rfloor \to v + \lfloor v/2 \rfloor + 1$ (replicas 1, 2), and average uniformly (weight $8^{-4}$) over all four twists to define $Z_{\mathrm{2seam}}(\lambda, \mu; u)$ and its joint Gibbs probability measure $\mathbb{P}_{\lambda, \mu}$ on $(\mathbb{Z}_2^3)^4 \times \mathrm{SU}(2)^{2|E(\Lambda)|}$.

Define the one-step seam operator $\mathcal{K}_{\mathrm{seam}}(\lambda)$ on $\mathcal{H} \otimes \mathcal{H}$ by averaging the layer-$0$ weight $\exp(\sum_e (s_{\mathrm{dir},0,e} + \lambda \mathcal{F}_{0,e}))$ over independent vertex gauges $(g_1, g_2)$ on slice $0$, $(h_1, h_2)$ on slice $1$, and temporal links $(V_1, V_2)$ on layer $0 \to 1$ and sandwiching with $M(X_1)M(X_2)$ on both sides; set $\mathcal{K}_{\mathrm{seam}}^+(\lambda) := (P_0 \otimes P_0)\mathcal{K}_{\mathrm{seam}}(\lambda)(P_0 \otimes P_0)$ on $\mathcal{H}_0 \otimes \mathcal{H}_0$ and
$$
\widetilde{A}(\lambda) := (T_+ \otimes T_+)^{(v-1)/2}\,\mathcal{K}_{\mathrm{seam}}^+(\lambda)\,(T_+ \otimes T_+)^{(v-1)/2} \qquad (\lambda \in [0, 1]).
$$

**Theorem 2.1 (Unpinned Two-Seam Identity and Hilbert–Schmidt Purity Angle, PROVED).** *For every $\beta \ge 0$, $n \ge 3$, and $u = 2v$ with $v \ge 3$:*
1. *(Exact operator trace and symmetries)* $\mathcal{K}_{\mathrm{seam}}^+(\lambda)$ and $\widetilde{A}(\lambda)$ are self-adjoint on $\mathcal{H}_0 \otimes \mathcal{H}_0$, commute with $\mathbb{S}$, satisfy $\mathbb{S}\mathcal{K}_{\mathrm{seam}}^+(\lambda) = \mathcal{K}_{\mathrm{seam}}^+(1 - \lambda)$ (in particular, $\mathcal{K}_{\mathrm{seam}}^+(1/2)$ annihilates the swap-odd subspace $\Lambda^2 \mathcal{H}_0$), $\mathcal{K}_{\mathrm{seam}}^+(0) = T_+ \otimes T_+$, $\mathcal{K}_{\mathrm{seam}}^+(1) = \mathbb{S}(T_+ \otimes T_+)$, and
   $$
   Z_{\mathrm{2seam}}(\lambda, \mu; u) = \operatorname{Tr}_{\mathcal{H}_0 \otimes \mathcal{H}_0}\!\bigl(\widetilde{A}(\lambda)\,\widetilde{A}(\mu)\bigr) = \langle \widetilde{A}(\lambda),\, \widetilde{A}(\mu) \rangle_{\mathrm{HS}},
   $$
   with $Z_{\mathrm{2seam}}(\lambda, \mu; u) = Z_{\mathrm{2seam}}(\mu, \lambda; u) = Z_{\mathrm{2seam}}(1 - \lambda, 1 - \mu; u)$.
2. *(Exact four-corner identity for the neutral purity $P_K$)*
   $$
   Z_{\mathrm{2seam}}(0, 0; u) = Z_{\mathrm{2seam}}(1, 1; u) = Z_+(u)^2, \qquad Z_{\mathrm{2seam}}(1, 0; u) = Z_{\mathrm{2seam}}(0, 1; u) = Z_+(2u),
   $$
   and hence
   $$
   -2\log P_K = \int_0^1\!\int_0^1 \partial_\lambda\partial_\mu \log Z_{\mathrm{2seam}}(\lambda, \mu; u)\,d\lambda\,d\mu
   = 3n^3 \int_0^1\!\int_0^1 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}_{\lambda, \mu}}\!\bigl(\mathcal{F}_{0, e_0},\; \mathcal{F}_{v, e'}\bigr)\,d\lambda\,d\mu, \tag{2.3}
   $$
   for any fixed link $e_0 \in E(\Sigma)$.
3. *(Exact diagonal reflection positivity and 1-parameter Hilbert–Schmidt arc-length bound)* For every $\lambda \in [0, 1]$,
   $$
   h_{\mathrm{2seam}}(\lambda) := \partial_\lambda\partial_\mu \log Z_{\mathrm{2seam}}(\lambda, \mu; u)\Big|_{\mu=\lambda}
   = 3n^3 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}_{\lambda, \lambda}}\!\bigl(\mathcal{F}_{0, e_0},\; \mathcal{F}_{v, e'}\bigr)
   = \left\|\frac{d}{d\lambda} \frac{\widetilde{A}(\lambda)}{\|\widetilde{A}(\lambda)\|_{\mathrm{HS}}}\right\|_{\mathrm{HS}}^2 \ge 0, \tag{2.4}
   $$
   $P_K = \cos\theta_{\mathrm{HS}}(\widetilde{A}(0), \widetilde{A}(1))$, and
   $$
   \arccos(P_K) \le 2 \int_0^{1/2} \sqrt{h_{\mathrm{2seam}}(\lambda)}\,d\lambda. \tag{2.5}
   $$
4. *(Corner reduction)* At $(\lambda, \mu) = (0, 0)$, vertex gauge invariance kills the cross-replica terms of $\mathcal{F}_{0, e}$ and $\mathcal{F}_{v, e'}$, giving
   $$
   \operatorname{Cov}_{\mathbb{P}_{0, 0}}\!\bigl(\mathcal{F}_{0, e},\; \mathcal{F}_{v, e'}\bigr) = 2\operatorname{Cov}_{\mathbb{P}_u^+}\!\bigl(E_{0, e},\; E_{v, e'}\bigr), \tag{2.6}
   $$
   where $E_{\tau, e} = \beta\operatorname{Re} U_{p(\tau, e)}$ is the ordinary single-replica temporal plaquette energy in the neutral period-$u$ Wilson measure $\mathbb{P}_u^+$.

*Proof.*
(1) Integrating out slices $\{1, \dots, v-1\}$ and $\{v+1, \dots, 2v-1\}$ with the averaged twists at $\lfloor v/2 \rfloor$ and $v + \lfloor v/2 \rfloor$ (which lie strictly inside the $v - 1 \ge 2$ unmodified layers on each arc) produces $(T_+ \otimes T_+)^{v-1} = (P_0 \otimes P_0)(T \otimes T)^{v-1}(P_0 \otimes P_0)$ on each arc, projecting both sides of each seam onto $\mathcal{H}_0 \otimes \mathcal{H}_0$ (and averaging slice-$0$ and slice-$1$ gauge orbits in the bulk path integral automatically produces the gauge-averaged kernel $\mathcal{K}_{\mathrm{seam}}(\lambda)$ on $\mathcal{H} \otimes \mathcal{H}$). Setting $\widetilde{V}_b := V_b h_b$ (absorbing $h_b$ by Haar invariance), the exponent of $\mathcal{K}_{\mathrm{seam}}(\lambda)(X_1, X_2; X'_1, X'_2)$ depends on the four pairings $\operatorname{Re}((g_a \cdot X_{a,e})(\widetilde{V}_b \cdot X'_{b,e})^{-1})$ with weight $(1-\lambda)\beta$ for $a = b$ and $\lambda\beta$ for $a \neq b$. Under the transpose $(X_1, X_2) \leftrightarrow (X'_1, X'_2)$ combined with the Haar-preserving swap $(g_1, g_2) \leftrightarrow (\widetilde{V}_1, \widetilde{V}_2)$ and $\operatorname{Re}(q^{-1}) = \operatorname{Re}(q)$, the $(1,1)$ and $(2,2)$ pairings stay fixed while $(2,1)$ and $(1,2)$ interchange, so $\mathcal{K}_{\mathrm{seam}}(\lambda)$ is symmetric (self-adjoint) on $\mathcal{H} \otimes \mathcal{H}$, and hence $\mathcal{K}_{\mathrm{seam}}^+(\lambda)$ is self-adjoint on $\mathcal{H}_0 \otimes \mathcal{H}_0$. Swapping $(X_1, X_2) \mapsto (X_2, X_1)$ and relabelling $(g_1, g_2) \mapsto (g_2, g_1)$ interchanges $(1-\lambda)$ and $\lambda$, giving $\mathbb{S}\mathcal{K}_{\mathrm{seam}}(\lambda) = \mathcal{K}_{\mathrm{seam}}(1-\lambda)$; since $[\mathbb{S}, P_0 \otimes P_0] = 0$, $\mathbb{S}\mathcal{K}_{\mathrm{seam}}^+(\lambda) = \mathcal{K}_{\mathrm{seam}}^+(1-\lambda)$, and taking adjoints shows $[\mathbb{S}, \mathcal{K}_{\mathrm{seam}}^+(\lambda)] = 0$. At $\lambda = 0$, shifting $\widetilde{V}_a \mapsto g_a \widetilde{V}_a$ recovers $T \otimes T$, so $\mathcal{K}_{\mathrm{seam}}^+(0) = T_+ \otimes T_+$ and $\mathcal{K}_{\mathrm{seam}}^+(1) = \mathbb{S}(T_+ \otimes T_+)$. Since $T_+ \ge 0$, cyclic trace gives $Z_{\mathrm{2seam}}(\lambda, \mu; u) = \operatorname{Tr}_{\mathcal{H}_0^{\otimes 2}}(\widetilde{A}(\lambda)\widetilde{A}(\mu))$, whence symmetry in $(\lambda, \mu)$ and invariance under $(\lambda, \mu) \mapsto (1-\lambda, 1-\mu)$ (using $\widetilde{A}(1-\lambda) = \mathbb{S}\widetilde{A}(\lambda)$ and $\mathbb{S}^2 = 1$) follow immediately.
(2) At $(0,0)$ and $(1,1)$, $\widetilde{A}(0) = T_+^v \otimes T_+^v$ and $\widetilde{A}(1) = \mathbb{S}(T_+^v \otimes T_+^v)$, so $\operatorname{Tr}(\widetilde{A}(0)^2) = \operatorname{Tr}(\widetilde{A}(1)^2) = Z_+(2v)^2 = Z_+(u)^2$ (with independent averaged twists $z_1 + z'_1, z_2 + z'_2$ at $(0,0)$ and $z_1 + z'_2, z_2 + z'_1$ at $(1,1)$). At $(1,0)$ and $(0,1)$, $\operatorname{Tr}(\widetilde{A}(1)\widetilde{A}(0)) = \operatorname{Tr}(\mathbb{S}(T_+^{2v} \otimes T_+^{2v})) = Z_+(4v) = Z_+(2u)$ (total twist $z_1 + z'_1 + z_2 + z'_2$ uniformly averaged). Since $\mathbb{P}_{\lambda, \mu}$ is a positive finite-dimensional Gibbs measure linear in $(\lambda, \mu)$ in the exponent, differentiating $\log Z_{\mathrm{2seam}}$ yields $\partial_\lambda\partial_\mu \log Z_{\mathrm{2seam}}(\lambda, \mu) = \operatorname{Cov}_{\mathbb{P}_{\lambda,\mu}}(\sum_e \mathcal{F}_{0,e}, \sum_{e'} \mathcal{F}_{v,e'})$. Spatial translation and cubic symmetry make $\sum_{e'} \operatorname{Cov}(\mathcal{F}_{0,e}, \mathcal{F}_{v,e'})$ independent of $e \in E(\Sigma)$ ($3n^3$ links). The fundamental theorem of calculus on $[0, 1]^2$ gives (2.3).
(3) Put $B(\lambda) = \partial_\lambda \widetilde{A}(\lambda)$ and $\widehat{A}(\lambda) = \widetilde{A}(\lambda)/\|\widetilde{A}(\lambda)\|_{\mathrm{HS}}$. Direct differentiation of $\log\langle \widetilde{A}(\lambda), \widetilde{A}(\mu)\rangle_{\mathrm{HS}}$ at $\mu = \lambda$ gives
$$
\partial_\lambda\partial_\mu \log\langle \widetilde{A}(\lambda), \widetilde{A}(\mu)\rangle_{\mathrm{HS}}\Big|_{\mu=\lambda}
= \frac{\|B(\lambda)\|_{\mathrm{HS}}^2 \|\widetilde{A}(\lambda)\|_{\mathrm{HS}}^2 - \langle B(\lambda), \widetilde{A}(\lambda)\rangle_{\mathrm{HS}}^2}{\|\widetilde{A}(\lambda)\|_{\mathrm{HS}}^4}
= \left\|\frac{d}{d\lambda}\widehat{A}(\lambda)\right\|_{\mathrm{HS}}^2 \ge 0.
$$
Since $\langle \widehat{A}(0), \widehat{A}(1)\rangle_{\mathrm{HS}} = Z_+(2u)/Z_+(u)^2 = P_K$, the geodesic angle $\theta_{\mathrm{HS}}(\widehat{A}(0), \widehat{A}(1)) = \arccos(P_K)$ on the unit Hilbert–Schmidt sphere is bounded above by the arc length $\int_0^1 \|\widehat{A}'(\lambda)\|_{\mathrm{HS}}\,d\lambda = 2\int_0^{1/2} \sqrt{h_{\mathrm{2seam}}(\lambda)}\,d\lambda$ (using $h_{\mathrm{2seam}}(1-\lambda) = h_{\mathrm{2seam}}(\lambda)$).
(4) At $(\lambda, \mu) = (0, 0)$, $\mathbb{P}_{0,0} = \mathbb{P}_u^+ \otimes \mathbb{P}_u^+$. Write $\mathcal{F}_{0,e} = \beta(\operatorname{Re}(X_{2,e} W_{1,0,e}) + \operatorname{Re}(X_{1,e} W_{2,0,e})) - E_{1,0,e} - E_{2,0,e}$. A vertex gauge transformation $g_1$ supported solely on slice $\tau = 0$ of replica 1 (sending $X_{1,e} \mapsto g_{1,x} X_{1,e} g_{1,y}^{-1}$, $V_{1,0,x} \mapsto g_{1,x} V_{1,0,x}$, and $V_{1,u-1,x} \mapsto V_{1,u-1,x} g_{1,x}^{-1}$) leaves $\mathbb{P}_{0,0}$, $E_{1,0,e}$, $E_{2,0,e}$, and $\mathcal{F}_{v,e'}$ invariant (since $v \ge 3$), while sending $X_{2,e} W_{1,0,e} \mapsto X_{2,e} g_{1,y} W_{1,0,e} g_{1,x}^{-1}$ and $X_{1,e} W_{2,0,e} \mapsto g_{1,x} X_{1,e} g_{1,y}^{-1} W_{2,0,e}$. Since $x \neq y$ ($n \ge 3$) and $\int_{\mathrm{SU}(2)} g\,dg = 0$, averaging over $g_1$ kills the cross-replica part of $\mathcal{F}_{0,e}$ inside $\operatorname{Cov}_{\mathbb{P}_{0,0}}(\mathcal{F}_{0,e}, \mathcal{F}_{v,e'})$, leaving $\operatorname{Cov}_{\mathbb{P}_{0,0}}(-E_{1,0,e}-E_{2,0,e}, \mathcal{F}_{v,e'})$. Repeating the identical slice-$v$ gauge average kills the cross-replica part of $\mathcal{F}_{v,e'}$, leaving $\operatorname{Cov}_{\mathbb{P}_{0,0}}(-E_{1,0,e}-E_{2,0,e}, -E_{1,v,e'}-E_{2,v,e'}) = 2\operatorname{Cov}_{\mathbb{P}_u^+}(E_{0,e}, E_{v,e'})$. $\blacksquare$

**Remark 2.1' (Pinned factorization into the quaternionic ball $B^4 \subset \mathbb{H}$, PROVED).** If instead of integrating over slices $\tau = 0$ and $\tau = v$ one pins boundary slices $\mathbf{X} = (X_1, X_2)$ and $\mathbf{Y} = (Y_1, Y_2)$ across a single half-cylinder of length $v$, then by (2.2) the two replicas decouple completely in the interior for every $(\lambda, \mu) \in [0, 1]^2$:
$$
\widetilde{K}_v^+(\mathbf{X}, \lambda;\, \mathbf{Y}, \mu) = \mathcal{K}_v^+\bigl((1-\lambda)X_1 + \lambda X_2,\; (1-\mu)Y_1 + \mu Y_2\bigr)\,\mathcal{K}_v^+\bigl(\lambda X_1 + (1-\lambda)X_2,\; \mu Y_1 + (1-\mu)Y_2\bigr),
$$
where $\mathcal{K}_v^+(M, N)$ is the single-replica neutral cylinder kernel with quaternionic boundary pins $M_e, N_e \in B^4 = \{q \in \mathbb{H} : |q| \le 1\}$. Because the boundary pin $X_e(\lambda) = (1-\lambda)X_{1,e} + \lambda X_{2,e}$ satisfies $|X_e(\lambda)| \le 1$, it never increases the boundary coupling above $\beta$. Notice, however, that in Structure I the relative gauge transformations between replicas 1 and 2 on the two seam slices $\tau = 0, v$ become local 3D spin variables $(g_x, h_x)$ at intermediate $\lambda \in (0, 1)$ (integrated out inside $\mathcal{K}_{\mathrm{seam}}(\lambda)$). Structure II eliminates even those seam spin variables completely.

### 2.2 Structure II (Primary Structure): Single-Replica, Gauge- and Centre-Invariant Two-Cut Interpolation $Z_{\mathrm{cut}}^+(\lambda, \mu; u)$

Radial scaling $M = \lambda X \in B^4$ ($0 \le \lambda \le 1$) inside the single-replica kernel $\mathcal{K}_v^+$ simply multiplies the temporal plaquette coupling on layer $0 \to 1$ by $\lambda \in [0, 1]$ while preserving **100% exact $(\mathcal{G} \times \mathbb{Z}_2^3)$ gauge and centre invariance** at every $\lambda \in [0, 1]$. Doing this unpinned on two antipodal layers of a **single** torus $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ ($u = 2v$, $v \ge 3$) yields an extraordinarily clean structure.

**Definition (Single-Replica Two-Cut Partition Function $Z_{\mathrm{cut}}^+(\lambda, \mu; u)$).** On a single copy of $\Lambda = (\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ ($u = 2v$, $v \ge 3$), define for $\lambda, \mu \in [0, 1]$ the one-step modified neutral transfer operator on $\mathcal{H}_0$:
$$
T_+(\lambda) := M (P_0 K_{\lambda\beta}) M \ge 0, \qquad T_+(1) = T_+, \qquad T_+(0) = |M\mathbf{1}\rangle\langle M\mathbf{1}|,
$$
where $\mathbf{1}(A) \equiv 1$ is the constant function (strictly gauge- and centre-invariant, so $M\mathbf{1} \in \mathcal{H}_0$). Set
$$
A(\lambda) := T_+^{(v-1)/2}\, T_+(\lambda)\, T_+^{(v-1)/2} \ge 0, \qquad
Z_{\mathrm{cut}}^+(\lambda, \mu; u) := \operatorname{Tr}_{\mathcal{H}_0}\!\bigl(T_+(\lambda) T_+^{v-1} T_+(\mu) T_+^{v-1}\bigr) = \langle A(\lambda),\, A(\mu) \rangle_{\mathrm{HS}}.
$$
Equivalently, $Z_{\mathrm{cut}}^+(\lambda, \mu; u)$ is the single-replica Wilson partition function on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/u)$ with temporal plaquette coupling $\lambda\beta$ on layer $0 \to 1$, $\mu\beta$ on layer $v \to v+1$, unmodified coupling $\beta$ on all spatial plaquettes and all other temporal layers, and a **single** $\mathbb{Z}_2^3$ centre twist $z$ averaged uniformly ($\frac{1}{8}\sum_{z \in \mathbb{Z}_2^3}$) at the midpoint layer $\tau = \lfloor v/2 \rfloor \to \lfloor v/2 \rfloor + 1$. Let $\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \mu}$ denote this probability measure, and let $Z_{\mathrm{cut}}^{(z)}(\lambda, \mu; u)$ and $\mathbb{P}^{\mathrm{cut}, z}_{\lambda, \mu}$ denote the **pure Gibbs measure** at a single fixed twist $z \in \mathbb{Z}_2^3$ (in particular $z = 0$, the untwisted periodic torus with two dialed temporal cuts).

**Theorem 2.2 (Exact Two-Cut Neutral Seed Inequality and Diagonal Arc-Length Bound, PROVED).** *For every $\beta \ge 0$, $n \ge 3$, and $u = 2v$ with $v \ge 3$:*
1. *(Twist invariance of the open cylinders)* Because $C_z (M\mathbf{1}) = M\mathbf{1}$ and $[C_z, T] = 0$, for every $z \in \mathbb{Z}_2^3$ the open-cylinder partition functions $Z_{\mathrm{open}}(w) := \langle M\mathbf{1}, T^{w-1} M\mathbf{1} \rangle = \langle M\mathbf{1}, T_+^{w-1} M\mathbf{1} \rangle$ are independent of $z$. Consequently:
   $$
   Z_{\mathrm{cut}}^{(z)}(1, 1; u) = Z^z(u), \qquad Z_{\mathrm{cut}}^{(z)}(1, 0; u) = Z_{\mathrm{cut}}^{(z)}(0, 1; u) = Z_{\mathrm{open}}(u), \qquad Z_{\mathrm{cut}}^{(z)}(0, 0; u) = Z_{\mathrm{open}}(v)^2,
   $$
   and averaging over $z \in \mathbb{Z}_2^3$ gives $Z_{\mathrm{cut}}^+(1, 1; u) = Z_+(u)$, $Z_{\mathrm{cut}}^+(1, 0; u) = Z_{\mathrm{cut}}^+(0, 1; u) = Z_{\mathrm{open}}(u)$, and $Z_{\mathrm{cut}}^+(0, 0; u) = Z_{\mathrm{open}}(v)^2$.
2. *(Exact cancellation of $\lambda_0$ and $c_0$, and neutral-seed inequality)* With $c_i := \langle M\mathbf{1}, \psi_i \rangle^2 \ge 0$ ($c_0 > 0$) and $r_i := \lambda_i/\lambda_0 \in [0, 1)$ for the neutral eigenbasis of $T_+$,
   $$
   I^{(+)}(u) := \log\frac{Z_+(u)\,Z_{\mathrm{open}}(v)^2}{Z_{\mathrm{open}}(u)^2}
   = \log\bigl(1 + s_+(u)\bigr) + 2\log\frac{1 + \sum_{i \ge 1} \frac{c_i}{c_0} r_i^{v-1}}{1 + \sum_{i \ge 1} \frac{c_i}{c_0} r_i^{2v-1}}
   \;\ge\; \log\bigl(1 + s_+(u)\bigr) \ge 0, \tag{2.7}
   $$
   and simultaneously
   $$
   I^{(+)}(u) = \int_0^1\!\int_0^1 \partial_\lambda\partial_\mu \log Z_{\mathrm{cut}}^+(\lambda, \mu; u)\,d\lambda\,d\mu
   = 3n^3 \int_0^1\!\int_0^1 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \mu}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\,d\lambda\,d\mu, \tag{2.8}
   $$
   where $E_{\tau, e} = \beta\operatorname{Re} U_{p(\tau, e)}$ is a single ordinary temporal plaquette. For the untwisted pure Gibbs measure ($z = 0$), the identical derivation yields
   $$
   I^{(0)}(u) := 3n^3 \int_0^1\!\int_0^1 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\,d\lambda\,d\mu
   = \log\frac{Z^0(u)\,Z_{\mathrm{open}}(v)^2}{Z_{\mathrm{open}}(u)^2}
   \ge \log\bigl(1 + S_{\mathrm{full}}(u)\bigr) \ge \log\bigl(1 + s_+(u)\bigr), \tag{2.9}
   $$
   and the twist-by-twist four-corner integrals $I^{(z)}(u)$ satisfy $\frac{1}{8}\sum_{z \in \mathbb{Z}_2^3} \exp(I^{(z)}(u)) = \exp(I^{(+)}(u))$.
3. *(1-parameter diagonal reflection positivity and Hilbert–Schmidt arc-length bound)* For every $\lambda \in [0, 1]$,
   $$
   h_{\mathrm{cut}}^+(\lambda) := \partial_\lambda\partial_\mu \log Z_{\mathrm{cut}}^+(\lambda, \mu; u)\Big|_{\mu=\lambda}
   = 3n^3 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \lambda}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)
   = \left\|\frac{d}{d\lambda}\frac{A(\lambda)}{\|A(\lambda)\|_{\mathrm{HS}}}\right\|_{\mathrm{HS}}^2 \ge 0. \tag{2.10}
   $$
   Moreover, $I^{(+)}(u) = -2\log\cos\theta_{\mathrm{HS}}(A(1), A(0))$, so if the diagonal arc length $\mathcal{L}_{\mathrm{diag}}^+(u) := \int_0^1 \sqrt{h_{\mathrm{cut}}^+(\lambda)}\,d\lambda < \pi/2$, then
   $$
   \log\bigl(1 + s_+(u)\bigr) \le I^{(+)}(u) \le -2\log\cos\bigl(\mathcal{L}_{\mathrm{diag}}^+(u)\bigr). \tag{2.11}
   $$
   In particular, $\mathcal{L}_{\mathrm{diag}}^+(u) \le \arccos(\sqrt{21}/5) \approx 0.4115$ (or $I^{(+)}(u) \le \log(25/21) \approx 0.17435$) implies $s_+(u) \le 4/21$ (the exact consumer seed `(M-io-exists)`), and $\mathcal{L}_{\mathrm{diag}}^+(u) \le \arccos(457^{1/4}/5) \approx 0.3905$ (or $I^{(+)}(u) \le \frac{1}{2}\log(625/457) \approx 0.15653$) implies $P_K \ge (1 + s_+(u))^{-2} \ge 457/625$. The exact same diagonal bound holds for $I^{(0)}(u)$ and $\log(1 + S_{\mathrm{full}}(u))$ with $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}$.

*Proof.*
(1) At $\lambda = 0$, $K_0(A, B) = \int_{\mathcal{G}} 1\,dg = 1$, so $T_+(0) = |M\mathbf{1}\rangle\langle M\mathbf{1}|$. With a single twist $C_z$ inserted at layer $k = \lfloor v/2 \rfloor$ ($1 \le k \le v - 1$), averaging over $z \in \mathbb{Z}_2^3$ inserts $P_0$; because $[P_0, T(\lambda)] = [P_0, T(\mu)] = [P_0, T] = 0$ and $P_0^2 = P_0$, the single-twist average identically equals $\operatorname{Tr}_{\mathcal{H}_0}(T_+(\lambda) T_+^{v-1} T_+(\mu) T_+^{v-1}) = \langle A(\lambda), A(\mu)\rangle_{\mathrm{HS}}$. At fixed $z$, we have:
- at $(1, 1)$: $\operatorname{Tr}(C_z T^{2v}) = Z^z(u)$;
- at $(1, 0)$: $\operatorname{Tr}(T^k C_z T^{v-k} |M\mathbf{1}\rangle\langle M\mathbf{1}| T^{v-1}) = \langle M\mathbf{1}, T^{v-1+k} C_z T^{v-k} M\mathbf{1}\rangle = \langle M\mathbf{1}, T^{2v-1} M\mathbf{1}\rangle = Z_{\mathrm{open}}(u)$ because $[C_z, T] = 0$ and $C_z(M\mathbf{1}) = M\mathbf{1}$;
- at $(0, 1)$: identically $Z_{\mathrm{open}}(u)$;
- at $(0, 0)$: $\operatorname{Tr}(|M\mathbf{1}\rangle\langle M\mathbf{1}| T^{k-1} C_z T^{v-k} |M\mathbf{1}\rangle\langle M\mathbf{1}| T^{v-1}) = \langle M\mathbf{1}, T^{v-1} M\mathbf{1}\rangle^2 = Z_{\mathrm{open}}(v)^2$.
Because $M\mathbf{1} \in \mathcal{H}_0$, $Z_{\mathrm{open}}(w) = \langle M\mathbf{1}, T_+^{w-1} M\mathbf{1}\rangle$.
(2) Expanding in the neutral eigenbasis gives $Z_+(2v) = \lambda_0^{2v}(1 + s_+(2v))$, $Z_{\mathrm{open}}(v) = \lambda_0^{v-1} c_0 (1 + \sum_{i\ge 1} \frac{c_i}{c_0} r_i^{v-1})$, and $Z_{\mathrm{open}}(2v) = \lambda_0^{2v-1} c_0 (1 + \sum_{i\ge 1} \frac{c_i}{c_0} r_i^{2v-1})$. Both $\lambda_0^{4v-2}$ and $c_0^2$ cancel identically in $Z_+(2v) Z_{\mathrm{open}}(v)^2 / Z_{\mathrm{open}}(2v)^2$. Since $c_i/c_0 \ge 0$ and $r_i^{v-1} \ge r_i^{2v-1} \ge 0$ for $i \ge 1$, the second ratio is $\ge 1$, giving (2.7). Equation (2.8) follows from differentiating $\log Z_{\mathrm{cut}}^+(\lambda, \mu; u)$ under the finite positive integral and applying spatial translation and cubic symmetry. Equation (2.9) is identical using $Z^0(2v) = \lambda_0^{2v}(1 + S_{\mathrm{full}}(2v))$, and $\frac{1}{8}\sum_z e^{I^{(z)}} = \frac{(\frac{1}{8}\sum_z Z^z) Z_{\mathrm{open}}(v)^2}{Z_{\mathrm{open}}(u)^2} = e^{I^{(+)}}$.
(3) Identical to Theorem 2.1(3), using $Z_{\mathrm{cut}}^+(\lambda, \mu; u) = \langle A(\lambda), A(\mu)\rangle_{\mathrm{HS}}$, so $\cos\theta_{\mathrm{HS}}(A(1), A(0)) = \frac{Z_{\mathrm{open}}(u)}{\sqrt{Z_+(u) Z_{\mathrm{open}}(v)^2}} = e^{-I^{(+)}(u)/2}$, hence $I^{(+)}(u) = -2\log\cos\theta_{\mathrm{HS}}(A(1), A(0))$. Finally, $P_K = \frac{1 + s_+(2u)}{(1 + s_+(u))^2} \ge \frac{1}{(1 + s_+(u))^2} \ge e^{-2 I^{(+)}(u)}$. $\blacksquare$

### 2.3 Theorem 2.3 (Exact Free-Field Identity for Structure II in Every Dimension $D \ge 3$) — PROVED

Before testing Structure II on interacting comparison models, we evaluate it **exactly** on a free Gaussian field (scalar or transverse Maxwell field with zero modes removed) on $(\mathbb{Z}/n)^{D-1} \times (\mathbb{Z}/2v)$ ($u = 2v$).

**Theorem 2.3 (PROVED).** *Consider a single real harmonic oscillator mode $q(\tau)$ ($\tau \in \mathbb{Z}/2v$, $v \ge 1$) of dispersion $\omega > 0$ ($\kappa = 2(\cosh\omega - 1) = 4\sinh^2(\omega/2)$), with two-cut action*
$$
S_{\mathrm{mode}}(\lambda, \mu) = -\frac{\beta}{2}\left[\lambda (q_1 - q_0)^2 + \mu(q_{v+1} - q_v)^2 + \sum_{\tau \notin \{0, v\}} (q_{\tau+1} - q_\tau)^2 + \kappa \sum_{\tau=0}^{2v-1} q_\tau^2\right].
$$
*Let $g_0 := \frac{\cosh((v - 1/2)\omega)}{2\sinh(\omega/2)\sinh(v\omega)}$ and $g_v := \frac{\cosh(\omega/2)}{2\sinh(\omega/2)\sinh(v\omega)}$ be the endpoint and end-to-end Green's functions of the $v$-site Neumann chain. Then for every $\lambda, \mu \in [0, 1]$ and $v \ge 1$:*
1. *(Exact two-cut ratio equals $1/P_{\mathrm{mode}}$)*
   $$
   \frac{Z_{\mathrm{cut}}(1, 1; 2v)\, Z_{\mathrm{cut}}(0, 0; 2v)}{Z_{\mathrm{cut}}(1, 0; 2v)^2} = \coth(v\omega) = \frac{1}{\tanh(u\omega/2)} = \frac{1}{P_{\mathrm{mode}}}. \tag{2.12}
   $$
2. *(Exact mixed derivative — pointwise positive and UV-finite)*
   $$
   \partial_\lambda\partial_\mu \log Z_{\mathrm{cut}}(\lambda, \mu; 2v) = \frac{2\,g_v^2}{\bigl((1 + 2\lambda g_0)(1 + 2\mu g_0) - 4\lambda\mu\, g_v^2\bigr)^2} > 0, \tag{2.13}
   $$
   *and along the diagonal $\lambda = \mu$, the exact Hilbert–Schmidt arc length is*
   $$
   \int_0^1 \sqrt{\partial_\lambda\partial_\mu \log Z_{\mathrm{cut}}(\lambda, \mu; 2v)\big|_{\mu=\lambda}}\,d\lambda = \frac{1}{\sqrt{2}}\log\coth\!\left(\frac{v\omega}{2}\right), \tag{2.14}
   $$
   *which matches $\theta_{\mathrm{HS}} = \arccos\sqrt{\tanh(v\omega)} = \sqrt{2}\,e^{-v\omega}(1 + O(e^{-2v\omega}))$ with asymptotically sharp constant $\sqrt{2}$ as $v\omega \to \infty$.*
3. *(Real-space free Maxwell field in every dimension $D \ge 3$)* For the noncompact free Maxwell field on $(\mathbb{Z}/n)^{D-1} \times (\mathbb{Z}/2v)$ (spatial zero modes removed) with quadratic plaquette energies $E_{\tau, e} = -\frac{\beta}{2}(dA)_{\tau, e}^2$, Wick's theorem makes the real-space covariance **pointwise nonnegative**:
   $$
   \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}}_{\lambda, \mu}}\!\bigl(E_{0, e},\; E_{v, e'}\bigr) = \frac{1}{2}\Bigl(\beta \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}}_{\lambda, \mu}}\bigl((dA)_{0, e},\; (dA)_{v, e'}\bigr)\Bigr)^2 \ge 0 \qquad \forall e, e' \in E(\Sigma). \tag{2.15}
   $$
   *Consequently, putting absolute values inside the sum over $e'$ introduces **zero loss** and **zero UV divergence**, and at fixed aspect $n/v = 1024$ the integrated single-link row sum is*
   $$
   \int_0^1\!\int_0^1 \sum_{e' \in E(\Sigma)} \Bigl|\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}}_{\lambda, \mu}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\Bigr|\,d\lambda\,d\mu
   = \frac{D - 2}{(D - 1) n^{D-1}} \sum_{k \in (\frac{2\pi}{n}\mathbb{Z}_n)^{D-1} \setminus \{0\}} \log\coth(v\omega_k)
   = \Theta_D\!\bigl(v^{-(D-1)}\bigr), \tag{2.16}
   $$
   *independent of $\beta > 0$! In particular, in every dimension $D \ge 3$—including $D = 3$, $D = 4$, and $D = 5$—free Maxwell sits **exactly at the marginal power $v^{-(D-1)}$** and fails $C v^{-(D-1)-\epsilon}$ for every $\epsilon > 0$.*

*Proof.*
(1) Write $A_{\mathrm{cut}}(\lambda, \mu)$ for the $2v \times 2v$ quadratic-form matrix of $S_{\mathrm{mode}}$ (without $\beta$). At $\lambda = \mu = 0$, $A_{\mathrm{cut}}(0, 0) = A_{\mathrm{Neum}}(v) \oplus A_{\mathrm{Neum}}(v)$, where $A_{\mathrm{Neum}}(L)$ is the $L \times L$ tridiagonal matrix with diagonal $(1+\kappa, 2+\kappa, \dots, 2+\kappa, 1+\kappa)$ and off-diagonals $-1$. Expanding $\det A_{\mathrm{Neum}}(L)$ via the Dirichlet determinants $D_k = \sinh((k+1)\omega)/\sinh\omega$ (diagonal $2 + \kappa = 2\cosh\omega$) gives
$$
\det A_{\mathrm{Neum}}(L) = D_L - 2 D_{L-1} + D_{L-2} = \frac{\sinh((L+1)\omega) - 2\sinh(L\omega) + \sinh((L-1)\omega)}{\sinh\omega}
= \frac{2(\cosh\omega - 1)\sinh(L\omega)}{\sinh\omega} = 2\tanh(\omega/2)\sinh(L\omega).
$$
Meanwhile $\det A_{\mathrm{cut}}(1, 1) = 4\sinh^2(v\omega)$ (periodic circle of length $2v$) and $\det A_{\mathrm{cut}}(1, 0) = \det A_{\mathrm{Neum}}(2v) = 2\tanh(\omega/2)\sinh(2v\omega)$. Since $Z_{\mathrm{cut}} = (\det A_{\mathrm{cut}})^{-1/2}$ up to a $(\lambda, \mu)$-independent constant,
$$
\frac{Z_{\mathrm{cut}}(1, 1) Z_{\mathrm{cut}}(0, 0)}{Z_{\mathrm{cut}}(1, 0)^2}
= \sqrt{\frac{\det A_{\mathrm{Neum}}(2v)^2}{4\sinh^2(v\omega)\, \det A_{\mathrm{Neum}}(v)^2}}
= \frac{\sinh(2v\omega)}{2\sinh^2(v\omega)} = \coth(v\omega).
$$
(2) Let $e_0 = \delta_0 - \delta_1$ and $e_v = \delta_v - \delta_{v+1}$ in $\mathbb{R}^{2v}$ (where site $0 \equiv 2v$ lies in the second Neumann block $\{v+1, \dots, 2v\}$ and sites $1, v$ lie at the two ends of the first Neumann block $\{1, \dots, v\}$). Then $A_{\mathrm{cut}}(\lambda, \mu) = A_{\mathrm{cut}}(0, 0) + \lambda e_0 e_0^T + \mu e_v e_v^T$. For the Neumann block $A_{\mathrm{Neum}}(v)$, solving $((A_{\mathrm{Neum}}(v))u)_j = \delta_{j, 1}$ gives $u_j = \frac{\cosh((v + 1/2 - j)\omega)}{2\sinh(\omega/2)\sinh(v\omega)}$, so $(A_{\mathrm{Neum}}(v)^{-1})_{1,1} = (A_{\mathrm{Neum}}(v)^{-1})_{v,v} = g_0$ and $(A_{\mathrm{Neum}}(v)^{-1})_{1,v} = g_v$. Hence $e_0^T G^{(0)} e_0 = e_v^T G^{(0)} e_v = 2g_0$ and $e_0^T G^{(0)} e_v = -2g_v$. By the matrix determinant lemma,
$$
D(\lambda, \mu) := \frac{\det A_{\mathrm{cut}}(\lambda, \mu)}{\det A_{\mathrm{cut}}(0, 0)}
= \det\begin{pmatrix} 1 + 2\lambda g_0 & -2\lambda g_v \\ -2\mu g_v & 1 + 2\mu g_0 \end{pmatrix}
= (1 + 2\lambda g_0)(1 + 2\mu g_0) - 4\lambda\mu g_v^2 > 0.
$$
Writing $a = 1 + 2\lambda g_0$ and $b = 1 + 2\mu g_0$, we have $\partial_\lambda D = 2g_0 b - 4\mu g_v^2$, $\partial_\mu D = 2g_0 a - 4\lambda g_v^2$, and $\partial_\lambda\partial_\mu D = 4(g_0^2 - g_v^2)$. Expanding directly gives
$$
(\partial_\lambda D)(\partial_\mu D) - D(\partial_\lambda\partial_\mu D)
= 4g_v^2\bigl(ab - 2\lambda g_0 b - 2\mu g_0 a + 4\lambda\mu g_0^2\bigr)
= 4g_v^2(a - 2\lambda g_0)(b - 2\mu g_0) = 4g_v^2.
$$
Hence $\partial_\lambda\partial_\mu \log Z_{\mathrm{cut}} = -\frac{1}{2}\partial_\lambda\partial_\mu \log D = \frac{1}{2}\frac{4g_v^2}{D^2} = \frac{2g_v^2}{D^2}$, proving (2.13). Along $\lambda = \mu$, $D(\lambda, \lambda) = (1 + 2\lambda(g_0 + g_v))(1 + 2\lambda(g_0 - g_v))$, so partial fractions give
$$
\int_0^1 \frac{\sqrt{2}\,g_v}{D(\lambda, \lambda)}\,d\lambda
= \frac{1}{2\sqrt{2}} \int_0^1 \left(\frac{2(g_0 + g_v)}{1 + 2\lambda(g_0 + g_v)} - \frac{2(g_0 - g_v)}{1 + 2\lambda(g_0 - g_v)}\right) d\lambda
= \frac{1}{2\sqrt{2}}\log\frac{1 + 2(g_0 + g_v)}{1 + 2(g_0 - g_v)}.
$$
Using $\sinh(\omega/2)\sinh(v\omega) + \cosh((v - 1/2)\omega) = \cosh(\omega/2)\cosh(v\omega)$, we get $1 + 2(g_0 \pm g_v) = \coth(\omega/2)\frac{\cosh(v\omega) \pm 1}{\sinh(v\omega)}$, whose ratio is $\frac{\cosh(v\omega) + 1}{\cosh(v\omega) - 1} = \coth^2(v\omega/2)$, proving (2.14).
(3) For centered jointly Gaussian variables $X, Y$, $\operatorname{Cov}(X^2, Y^2) = 2(\operatorname{Cov}(X, Y))^2 \ge 0$, proving (2.15). Summing over $e, e' \in E(\Sigma)$ (there are $(D-1)n^{D-1}$ links on $\Sigma$ and $D - 2$ transverse polarizations per nonzero spatial momentum $k$, with $\omega_k = 2\operatorname{arsinh}(\frac{1}{2}(\sum_{j=1}^{D-1} 4\sin^2(k_j/2))^{1/2})$) gives (2.16). At fixed aspect $n/v = 1024$, the modes with $0 < |k| \le 1/v$ number $\Theta_D((n/v)^{D-1})$ and each contributes $\log\coth(v\omega_k) \ge \log\coth(1) > 0$, while modes with $|k| > 1/v$ sum convergently to $O_D((n/v)^{D-1})$ because $\log\coth(t) \le 3 e^{-2t}$ for $t \ge 1$. Dividing by $(D-1)n^{D-1}$ yields $\Theta_D(v^{-(D-1)})$. $\blacksquare$

---

## 3. Candidate Band Lemmas and Complete Selectivity & Non-Equivalence Audit ((g1)–(g6))

Before attacking any estimate for 4D $\mathrm{SU}(2)$ at $\beta \in [2, 3]$, we state the exact candidate lemmas from Structures II and I and run the full six-test filter of row 1553 §1.5 as corrected by check 1556.

**Candidate Band Lemmas (at fixed $\beta \in [2, 3]$, $n \in 1024\mathbb{N}$, $u = n/512$, $v = u/2 = n/1024 \ge 3$):**
- **Lemma `TC(eps)` (Two-Cut Neutral Covariance):** Uniformly in $\beta \in [2, 3]$ and $n \in 1024\mathbb{N}$,
  $$
  \int_0^1\!\int_0^1 \sum_{e' \in E(\Sigma)} \Bigl|\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \mu}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\Bigr|\,d\lambda\,d\mu \;\le\; C v^{-3 - \epsilon}. \tag{TC($\epsilon$)}
  $$
  Its **1-parameter diagonal** reflection-positive sibling (which already suffices by Theorem 2.2(3)!) is:
  $$
  \mathcal{L}_{\mathrm{diag}}^+(u) := \int_0^1 \sqrt{3n^3 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \lambda}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)}\,d\lambda \;\le\; C v^{-\epsilon}. \tag{TC$_{\mathrm{diag}}(\epsilon)$}
  $$
  Their pure-Gibbs untwisted counterparts (with $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}$ and $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}$) are denoted **`TC_0(eps)`** and **`TC_{diag,0}(eps)`**.
- **Lemma `TS(eps)` (Two-Seam $\mathrm{Sp}(2)$ Neutral Covariance):** Uniformly in $\beta \in [2, 3]$ and $n \in 1024\mathbb{N}$,
  $$
  \int_0^1\!\int_0^1 \sum_{e' \in E(\Sigma)} \Bigl|\operatorname{Cov}_{\mathbb{P}_{\lambda, \mu}}\!\bigl(\mathcal{F}_{0, e_0},\; \mathcal{F}_{v, e'}\bigr)\Bigr|\,d\lambda\,d\mu \;\le\; C v^{-3 - \epsilon} \tag{TS($\epsilon$)}
  $$
  (with diagonal arc-length sibling `TS_{diag}(eps)`: $2\int_0^{1/2}\sqrt{h_{\mathrm{2seam}}(\lambda)}\,d\lambda \le C v^{-\epsilon}$).

In $D$ dimensions ($n = 1024 v$), the test exponent matching the slice volume $(D-1)n^{D-1}$ is $v^{-(D-1)-\epsilon}$ for `TC(eps)` / `TS(eps)`, and $v^{-\epsilon}$ for `TC_{diag}(eps)` / `TS_{diag}(eps)`.

### 3.1 Test `(g1)`: 4D Compact $\mathrm{U}(1)$ at Weak Coupling — PROVED FAILS (Both Free and Interacting!)

The two-cut construction $Z_{\mathrm{cut}}^+(\lambda, \mu; u)$ applies verbatim to 4D compact $\mathrm{U}(1)$ (with the $\mathbb{Z}_2^3$ centre subgroup $\{\pm 1\}^3 \subset \mathrm{U}(1)^3$), and the two-seam construction $Z_{\mathrm{2seam}}(\lambda, \mu; u)$ applies verbatim by embedding $\mathrm{U}(1)^2 \subset \mathrm{U}(2)$ with the same $R_s \in \mathrm{SO}(2) \subset \mathrm{U}(2)$.

1. **Free Maxwell (PROVED, Theorem 2.3(3)):** The integrated row sum equals $\Theta(v^{-3})$, refuting `TC(eps)` for every $\epsilon > 0$; similarly $-\log P_{\mathrm{free}} = \Theta((n/u)^3)$ refutes `TC_{diag}(eps)`, `TS(eps)`, and `TS_{diag}(eps)`.
2. **Interacting 4D Compact Villain $\mathrm{U}(1)$ — Neutral Sector (PROVED GIVEN checked results on file):**

**Theorem 3.1 (Refutation of Neutral Purity and `TC`/`TS` for Interacting 4D Villain $\mathrm{U}(1)$, PROVED GIVEN PV (7.3), row 786/794, row 1368/1370, and Corollary EV).** *For 4D compact Villain $\mathrm{U}(1)$ at every fixed $\beta \ge 2^{14}$ and every admissible box $n \in 1024\mathbb{N}$ with $n \ge 2048$ (so $u = n/512 \ge 4 \ge 3$, covering every $v = n/1024 \ge 3$ of Section 0), the $\mathbb{Z}_2^3$-neutral thermal sum and purity satisfy*
$$
s_+^{\mathrm{Villain}}(u; n^3; \beta) > \frac{4}{21}, \qquad P_K^{\mathrm{Villain}, \mathrm{U}(1)} < \frac{457}{625}. \tag{3.1}
$$
*Consequently, uniformly in $n \in 1024\mathbb{N}$ ($n \ge 3072$, $v = n/1024 \ge 3$),*
$$
I^{(+)}(u) > \log\frac{25}{21}, \qquad \mathcal{L}_{\mathrm{diag}}^+(u) > \arccos\!\left(\frac{\sqrt{21}}{5}\right), \qquad -2\log P_K^{\mathrm{Villain}, \mathrm{U}(1)} > 2\log\frac{625}{457},
$$
*so `TC(eps)`, `TC_{diag}(eps)`, `TS(eps)`, and `TS_{diag}(eps)` (as well as their untwisted versions) all **FAIL** for interacting weak 4D compact Villain $\mathrm{U}(1)$ at every $\epsilon > 0$ (row sum $\ge c v^{-3}$).*

*Proof.* Suppose for contradiction that $s_+^{\mathrm{Villain}}(u; n^3; \beta) \le 4/21$ for some $\beta \ge 2^{14}$ and some $n \in 1024\mathbb{N}$ with $n \ge 2048$ ($u = n/512 \ge 4 \ge 3$). Four-dimensional compact Villain $\mathrm{U}(1)$ satisfies `(TM-tw)`, `(S)`, and `(L)` of `library/gap-flux-exercise.md` (its plaquette weight $\phi_\beta(\theta) \ge e^{-\pi^2\beta/2} > 0$ has strictly positive Fourier weights $e^{-q^2/(2\beta)} > 0$ on $\mathbb{Z}$, giving a strictly positive, self-adjoint, trace-class, reflection-positive, hypercubic-symmetric transfer operator with $Z^k \le Z^0$ and the $\mathbb{Z}_2^3$ centre subgroup $\{\pm 1\}^3 \subset \mathrm{U}(1)^3$).
- By **Theorem 4 and Corollary 5 (row $K = 44$) of row 1368** (checked in check 1370, `library/gap-agy-seed-neon-check-astra.md` lines 67–106; here $4 \mid n$, $u \ge 4 \ge 3$, $n = 512 u \ge 44 u$, and $s_0 = 4/21$), $s_+(u; n^3; \beta) \le 4/21$ directly implies $S_\kappa(N; (2N)^3; \beta) < 1/5041$ at $N = n/2 \ge 1024 \ge 3$.
- By **Corollary EV** of `library/gap-flux-exercise.md` line 515 (checked in `gap-flux-exercise-check.md`), $S_\kappa(N; (2N)^3; \beta) < 1/5041$ implies that **every** local subsequential limit $\nu$ of the periodic symmetric tori $T_M = (\mathbb{Z}/M)^4$ as $M \to \infty$ clusters exponentially at a positive rate $m_0 > 0$ in each of the four coordinate directions separately on all bounded continuous local $\mathbb{Z}_2^3$-even observables.
- The single-plaquette Villain score $s_p(\theta) = \phi'_\beta((d_1\theta)_p)/\phi_\beta((d_1\theta)_p)$ is bounded, continuous, local (width $\le 2$ in each axis), and $\mathbb{Z}_2^3$-even (every plaquette is unchanged by centre translations). Hence $|\operatorname{Cov}_\nu(s_0, s_x)| \le \|s_0\|_\infty^2 \exp(-m_0(|x_\mu| - 2))$ for every $\mu \in \{0, 1, 2, 3\}$; taking the maximum over $\mu$ yields $|\operatorname{Cov}_\nu(s_0, s_x)| \le \|s_0\|_\infty^2 \exp(-m_0(\|x\|_\infty - 2))$, so $x \mapsto \operatorname{Cov}_\nu(s_0, s_x)$ lies in $\ell^1(\mathbb{Z}^4)$.
- This directly contradicts **row 786 §1.3** (checked line by line in check 794, `library/gap-tu-check-opus.md` lines 40–52, built on PV (7.3)), which proves that at every $\beta \ge 2^{14}$ no local subsequential limit of periodic 4D compact Villain $\mathrm{U}(1)$ on $T_M$ has $\ell^1(\mathbb{Z}^4)$ score covariance.

Hence $s_+^{\mathrm{Villain}}(u; n^3; \beta) > 4/21$, and Fact PUR immediately forces $P_K^{\mathrm{Villain}, \mathrm{U}(1)} < 457/625$. Combining (3.1) with Theorems 2.1 and 2.2 refutes `TC(eps)`, `TC_{diag}(eps)`, `TS(eps)`, and `TS_{diag}(eps)` for every $\epsilon > 0$. $\blacksquare$

**Corollary 3.2 (Interacting 4D Compact Wilson Cosine $\mathrm{U}(1)$ — Unprojected Sector, PROVED GIVEN row 1565 / check 1571).** *For 4D compact Wilson cosine $\mathrm{U}(1)$ at every $\beta_W \ge \beta_*$ (the existential threshold of row 1565 (7), checked in check 1571), on every $n \in 1024\mathbb{N}$, $u = n/512$, the odd electric-flux probability at period $u$ satisfies $p_- \ge \eta_{2000} > 0$, hence $S_{\mathrm{full}}(u) \ge \eta_{2000}$ and $\Pi^{\mathrm{Wilson}, \mathrm{U}(1)} = Z^0(2u)/Z^0(u)^2 \le \frac{1 + \eta_{2000}^2}{(1 + \eta_{2000})^2} < 1$. Therefore `TC_0(eps)`, `TC_{diag,0}(eps)`, `TS_0(eps)`, and `TS_{diag,0}(eps)` all **FAIL** rigorously for interacting weak 4D compact Wilson cosine $\mathrm{U}(1)$.* (The neutral-projected Wilson-cosine counterpart remains ARGUED/OPEN because PV's positive current expansion has not been transferred to coexact score covariances of the cosine action; cf. row 786.)

*Proof.* Write $Z^0(u) = Z_{\mathrm{even}}(u) + Z_{\mathrm{odd}}(u)$ where $Z_{\mathrm{odd}}(u) \ge \eta Z^0(u)$ ($\eta = \eta_{2000} \in (0, 1/2]$). Dividing by $\lambda_0^u$ gives $s_{\mathrm{odd}} \ge \frac{\eta}{1-\eta}(1 + s_{\mathrm{even}}) \ge \eta$, so $S_{\mathrm{full}}(u) \ge \eta$. As in Fact PUR, $\Pi \le (1 + \min(S, S^2))/(1 + S)^2$; this bound is $\le 1/2$ for $S \ge 1$ and strictly decreasing on $[0, 1]$, so $\Pi \le (1 + \eta^2)/(1 + \eta)^2 < 1$. Theorems 2.1–2.2 then give $I^{(0)}(u) \ge \log(1 + \eta) > 0$ and $-2\log\Pi \ge 2\log((1+\eta)^2/(1+\eta^2)) > 0$, refuting the $v^{-\epsilon}$ decay. $\blacksquare$

### 3.2 Test `(g2)`: 5D $\mathrm{SU}(2)$ at Weak Coupling — PROVED FAILS (Free Part); BELIEF (Interacting)

- **Free 5D $\mathrm{SU}(2)$ (3 noninteracting photons, PROVED):** By Theorem 2.3(3) with $D = 5$, $n = 1024 v$, the integrated single-link row sum of `TC` is $\Theta(v^{-4})$, refuting `TC(eps)` ($\le C v^{-4-\epsilon}$) for every $\epsilon > 0$; similarly `TC_{diag}`, `TS`, `TS_{diag}` fail with $O(1)$ lower bounds (independent of $n$).
- **Interacting weak 5D $\mathrm{SU}(2)$ (BELIEF):** Under the standard belief that 5D $\mathrm{SU}(2)$ is gapless at weak coupling (with massless gluons, so $s_+(u) \ge c > 0$ and $P_K \le 1 - c'$ at fixed aspect), `TC`, `TC_{diag}`, `TS`, and `TS_{diag}` all fail for every $\epsilon > 0$.

### 3.3 Test `(g3)`: The Gapped Twins — PROVED PASSES Strong Coupling & Genuine 3D Gap Sensitivity!

**Theorem 3.3 (Exponential Decay in All Four Strong-Coupling Gapped Twins, PROVED).** *In $D \in \{3, 4, 5\}$ dimensions, for $G = \mathrm{SU}(2)$ or $G = \mathrm{U}(1)$ Wilson action, put $q := 6(D - 1)\beta$ ($2(D - 1)$ plaquettes per link $\times 3$ neighbours $\times \beta$; explicitly $q < 1$ is $\beta < 1/18$ in $D = 4$, $\beta < 1/24$ in $D = 5$, and $\beta < 1/12$ in $D = 3$). Then uniformly in $(\lambda, \mu) \in [0, 1]^2$ and $n \in 1024\mathbb{N}$ ($u = 2v$, $v \ge 4$):*
1. *(Untwisted Two-Cut `TC_0`)*
   $$
   \sum_{e' \in E(\Sigma)} \Bigl|\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\Bigr| \;\le\; \frac{8(D - 1)\beta^2\, q^{v - 1}}{1 - q}. \tag{3.2}
   $$
2. *(Neutral-Projected Two-Cut `TC`)* With the $\mathbb{Z}_2^3$ twist placed at layer $\tau = \lfloor v/2 \rfloor$,
   $$
   \sum_{e' \in E(\Sigma)} \Bigl|\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \mu}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\Bigr| \;\le\; \frac{8(D - 1)\beta^2\, q^{v - 1}}{1 - q} + \frac{32(D - 1)\beta^2\, n^{D-1}\, q^{2(\lfloor v/2 \rfloor - 1)}}{(1 - q)^2}. \tag{3.3}
   $$
3. *(Two-Seam $\mathrm{Sp}(2)$ `TS` and `TS_0`)* Because on every seam link ($X_{a, e}$, $X'_{a, e}$, and $V_{a, 0, x}$) the direct and swapped temporal couplings sum to $(1 - \lambda)\beta + \lambda\beta = \beta$, the exact same single-link Dobrushin constant $q = 6(D-1)\beta < 1$ applies uniformly in $(\lambda, \mu) \in [0, 1]^2$, yielding exponential decay $\le C_D \beta^2 n^{D-1} q^{v - 3}$ for both `TS_0` and `TS`.

*Proof.* On a $D$-dimensional hypercubic lattice, every link $i$ lies in $2(D-1)$ plaquettes, each containing $3$ other links, giving $6(D-1)$ plaquette neighbours. For Wilson coupling $b_p \in [0, \beta]$ on every plaquette (including $\lambda\beta, \mu\beta \le \beta$ on the dialed cuts, and $(1-\lambda)\beta + \lambda\beta = \beta$ on every seam link type of Structure I: $X_{a, e}$, $X'_{a, e}$, and $V_{a, 0, x}$ each have total temporal-neighbour coupling weight $3\beta$ per incident temporal direction), changing one neighbouring link shifts the conditional log-density of link $i$ by oscillation at most $4b_p$. By interpolation of normalized densities (using Popoviciu's inequality $|\operatorname{Cov}(g, \Delta)| \le \frac{1}{4}\operatorname{osc}(g)\operatorname{osc}(\Delta)$ for $0 \le g \le 1$), the total-variation Dobrushin matrix $C$ has row sums at most $6(D-1) \cdot (\frac{1}{4} \cdot 4\beta) = 6(D-1)\beta = q < 1$ uniformly in $(\lambda, \mu) \in [0, 1]^2$ (identical to row 1565 §1, checked in check 1571).

For (3.2), Dobrushin's covariance inequality (`gap-dob-astra.md` / row 1565 §1) gives
$$
\sum_{e' \in E(\Sigma)} \bigl|\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}}(E_{0, e_0}, E_{v, e'})\bigr|
\le \frac{1}{4} \sum_{i \in \mathrm{supp}(E_{0, e_0})} \delta_i(E_{0, e_0}) \sum_{j} \bigl[(I - C)^{-1}\bigr]_{ij} \sum_{e' \in E(\Sigma)} \delta_j(E_{v, e'}).
$$
Each plaquette $E_{0, e_0}$ depends on $4$ links with single-link oscillation $\delta_i(E_{0, e_0}) \le 2\beta$. For any link $j$, if $j$ is a spatial link on slice $v$ or $v+1$ it belongs to one plaquette $E_{v, e'}$ ($\sum_{e'} \delta_j \le 2\beta$); if $j$ is a temporal link on layer $v \to v+1$ it belongs to $2(D-1)$ plaquettes $E_{v, e'}$ ($\sum_{e'} \delta_j \le 4(D-1)\beta$); otherwise $\sum_{e'} \delta_j = 0$. Every link-plaquette adjacency path from $\mathrm{supp}(E_{0, e_0})$ (time slices $0, 1$) to $\mathrm{supp}(E_{v, e'})$ (time slices $v, v+1$) along either arc of $\mathbb{Z}/2v$ requires at least $v - 1$ steps in $C$, so $\sum_{j \in \mathrm{supp}(\text{layer } v)} [(I - C)^{-1}]_{ij} \le q^{v-1}/(1 - q)$. Multiplying $\frac{1}{4} \cdot (4 \cdot 2\beta) \cdot \frac{q^{v-1}}{1-q} \cdot 4(D-1)\beta$ yields (3.2).

For (3.3), decompose $\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, +}_{\lambda, \mu}}$ by the law of total covariance over $z \in \mathbb{Z}_2^3$: the within-twist average satisfies (3.2), while for the between-twist covariance $\operatorname{Cov}_z(X_z, Y_z) = \frac{1}{2}\mathbb{E}_{z, z'}[(X_z - X_{z'})(Y_z - Y_{z'})]$ ($X_z = \mathbb{E}^{(z)}[E_{0, e_0}]$, $Y_z = \mathbb{E}^{(z)}[E_{v, e'}]$), changing the twist from $z$ to $z'$ on layer $\tau = \lfloor v/2 \rfloor$ alters single-link conditional distributions only at links $k \in S$ (total-variation discrepancy $b_k \le 1$), at graph distance $d \ge \lfloor v/2 \rfloor - 1$ from both layer $0$ and layer $v$. By Dobrushin's comparison theorem, $|X_z - X_{z'}| \le \sum_{i \in \mathrm{supp}(E_{0, e_0})} \delta_i(E_{0, e_0}) \sum_{k \in S} [(I - C)^{-1}]_{ik} \le 8\beta q^d/(1 - q)$, and identically for $|Y_z - Y_{z'}|$. Thus $|\operatorname{Cov}_z(X_z, Y_z)| \le \frac{1}{2}(8\beta q^d/(1 - q))^2 = 32\beta^2 q^{2d}/(1 - q)^2$; summing over $(D-1)n^{D-1}$ links $e'$ yields (3.3). Part (3) follows identically using $|\delta_i(\mathcal{F})| \le 4\beta$ and the midpoint twist layers at $\tau = \lfloor v/2 \rfloor$ and $v + \lfloor v/2 \rfloor$ (with $2(\lfloor v/2 \rfloor - 1) \ge v - 3$). $\blacksquare$

**Crucial 3D $\mathrm{U}(1)$ improvement over check 1556's `BC(eps)`:** In row 1566 / check 1570, check 1556's cut-covariance lemma `BC(eps)` was *already passed by massless 3D free Maxwell* with $\epsilon = 1$, showing that in $D = 3$ `BC(eps)` did not read the gap. By contrast, in **Theorem 2.3(3)** massless 3D free Maxwell **FAILS** `TC(eps)` ($\Theta(v^{-2})$ against $v^{-2-\epsilon}$), while gapped **3D compact $\mathrm{U}(1)$** **PASSES** `TC(eps)` exponentially at small $\beta < 1/12$ (Theorem 3.3) and is expected to pass exponentially at every $\beta > 0$ via the Göpfert–Mack mass gap (ARGUED). Thus `TC` / `TS` genuinely track the gap in **all** dimensions $D \ge 3$, not merely 4D cut-area scaling.

### 3.4 Test `(g4)`: Gapless Members with an $\mathrm{SU}(2)$ Factor and Neutral Spectators — PROVED PASSES!

This is the exact test that killed check 1556's `BC(eps)` as a gap/purity input.
1. **Product with a neutral spectator ($T = T_W \otimes T_m$, $P_0 = P_{0, W} \otimes 1$, PROVED):** When the two-cut dialing $(\lambda, \mu) \in [0, 1]^2$ (or the two-seam replica swap) acts on the **full** theory—dialing both the $\mathrm{SU}(2)$ temporal layer and the spectator temporal layer (so $T_{\mathrm{full}}(\lambda) = T_{+, W}(\lambda) \otimes T_m(\lambda)$ with $T_m(0) = |M_m \mathbf{1}_m\rangle\langle M_m \mathbf{1}_m|$)—the partition functions factor:
   $$
   Z_{\mathrm{cut}}^{\mathrm{full}}(\lambda, \mu; u) = Z_{\mathrm{cut}, W}^+(\lambda, \mu; u)\, Z_{\mathrm{cut}, m}(\lambda, \mu; u), \qquad
   Z_{\mathrm{2seam}}^{\mathrm{full}}(\lambda, \mu; u) = Z_{\mathrm{2seam}, W}(\lambda, \mu; u)\, Z_{\mathrm{2seam}, m}(\lambda, \mu; u).
   $$
   Hence the four-corner integrals are **strictly additive**:
   $$
   I^{\mathrm{full}}(u) = I^{(+)}_W(u) + I_m(u) \ge \log\bigl(1 + s_{+, W}(u)\bigr) + \log\bigl(1 + s_m(u)\bigr), \qquad
   -2\log P_K^{\mathrm{full}} = -2\log P_{K, W} - 2\log P_{K, m}.
   $$
   For **any** seedless neutral spectator (for instance, row 1565's harmonic rotor with $P_m < 1/2$ and $s_m(u) > 1$, or a decoupled massless 4D scalar/photon with $I_m(u) = \Theta(512^3)$), $I^{\mathrm{full}}(u) \ge \log(1 + s_m(u)) \ge c > 0$ and $-2\log P_K^{\mathrm{full}} \ge 2\log 2$, **refuting `TC(eps)`, `TC_{diag}(eps)`, `TS(eps)`, and `TS_{diag}(eps)`**! (Scope check per check 1556 §(iii): if one applies the construction only to the $\mathrm{SU}(2)$ links while leaving an uncoupled spectator untouched, it reads pure $\mathrm{SU}(2)$ only; on the enlarged product class where the full transfer is tested, it detects every spectator.)
2. **Pure-$\mathrm{SU}(2)$ and $\mathrm{SU}(2)$-matter gapless members: K7 and Adjoint-Higgs Coulomb (PROVED given their gapless premises; premises BELIEF):** In the mixed fundamental–adjoint K7 coexistence/critical endpoint (two nearly degenerate neutral vacua $\implies s_+(u) \ge 1 - o(1)$, $P_K \le 1/2 + o(1)$) and in the adjoint-Higgs Coulomb phase (massless neutral photon inside the $\mathrm{SU}(2)$ field $\implies s_+(u) \ge c > 0$, $-\log P_K = \Theta(512^3)$), Theorems 2.1 and 2.2 immediately force $I^{(+)}(u) \ge \log(1 + c) > 0$ and $-2\log P_K \ge c' > 0$, refuting `TC`, `TC_{diag}`, `TS`, and `TS_{diag}` even with no external spectator.

### 3.5 Test `(g5)`: Scale ($\beta \to \infty$ at Fixed Lattice $(n, u)$) — PROVED FAILS!

By row 1215 (5) and check 1527 §(iii) (`library/gap-agy-seed-approaches-neon-check-astra62.md` lines 77–81, PROVED), at any fixed $n, u \ge 3$ and $\beta \to \infty$, the neutral thermal sum of 4D $\mathrm{SU}(2)$ Wilson theory obeys $1 + s_+(u; n^3; \beta) \ge c_{n, u} \beta^{3/2} \log\beta$ and $P_K \asymp_{n, u} \beta^{-3/2}/\log\beta \to 0$. Therefore, by Theorems 2.1–2.2,
$$
I^{(+)}(u) \ge \frac{3}{2}\log\beta + \log\log\beta - O_{n, u}(1) \longrightarrow +\infty, \qquad
-2\log P_K = 3\log\beta + 2\log\log\beta + O_{n, u}(1) \longrightarrow +\infty.
$$
Hence `TC(eps)`, `TC_{diag}(eps)`, `TS(eps)`, and `TS_{diag}(eps)` cannot hold uniformly as $\beta \to \infty$ at fixed $(n, u)$. They also pass the `(t3)` $\mathrm{SU}(3)$ test (every formula uses only the normalized fundamental trace $\frac{1}{N}\operatorname{Re}\operatorname{tr}$, with nothing specific to $\dim\mathfrak{su}(2) = 3$) and `(t6)` Villain test (Theorem 3.1).

### 3.6 Test `(g6)` and the Rule "Equivalent is Not Progress" — PROVED Separation on Transfer Data; Honest Scope on Pure Wilson

We state the exact logical relationship between our band lemmas and `(PUR-io)`:
1. **Fixed coupling $\beta \in [2, 3]$ vs calibrated trajectory $\beta_K$:**
   - Proving `TC(eps)` or `TC_{diag}(eps)` (or `TS(eps)` / `TS_{diag}(eps)`) at fixed $\beta \in [2, 3]$ yields $s_+(u; n^3; \beta) \to 0$ and $P(\beta; n, u) \to 1$ as $n \to \infty$, hence a uniform positive neutral mass gap $m_+(\beta) > 0$ at every $\beta \in [2, 3]$ via row 1368/1370 (and a full gap + confinement via Theorem S for `TC_0(eps)`). It does **not** by itself reach `(PUR-io)` at the release roots $\beta_K$; that still requires the carry from order-one coupling to $\beta_K$ (registry R12, or `(A2)` of Theorem T).
   - **Important calibration fact:** Along the calibrated trajectory $\beta_K$ at a fixed physical side $\ell$, the continuum neutral purity $P_{\mathrm{cont}}(\ell)$ is expected to lie strictly below $1$ (a fixed physical glueball of mass $m_{\mathrm{phys}}$ gives $s_+(u) \to \sum_j e^{-m_j \ell/512} > 0$). Thus the asymptotic power $v^{-\epsilon} \to 0$ is **false** at fixed physical side $\ell$ along $\beta_K$; the trajectory form that implies `(PUR-io)` is the non-asymptotic threshold:
     $$
     \mathcal{L}_{\mathrm{diag}}^+(u; \beta_K) \le \arccos\!\left(\frac{\sqrt{21}}{5}\right) \quad \text{or} \quad
     2\int_0^{1/2}\sqrt{h_{\mathrm{2seam}}(\lambda; \beta_K)}\,d\lambda \le \arccos\!\left(\frac{457}{625}\right)
     \quad \text{at infinitely many } K \text{ for one } \ell, g_0. \tag{TC$_{\mathrm{traj}}$ / TS$_{\mathrm{traj}}$}
     $$
2. **Strict non-equivalence on positive transfer data (PROVED):** Both `TC_{traj}` (and `TC(eps)`) and `TS_{traj}` (and `TS(eps)`) are **sufficient** for the seed `(M-io-exists)` / `(PUR-io)` (Theorem 2.1(3), Theorem 2.2(3)), and are **strictly stronger** than `(PUR-io)` on positive transfer data:
   - *Explicit separation for `TC`:* Consider a $2$-level positive transfer $T_+ = \operatorname{diag}(1, r)$ ($0 < r < 1$) with boundary vector $M\mathbf{1} = (\sqrt{c_0}, \sqrt{c_1})$. Put $r^u = \delta \in (0, 1/100)$ and $c_1/c_0 = \delta^{-3/4}$. Then $s_+(u) = \delta < 4/21$ and $P_K = (1 + \delta^2)/(1 + \delta)^2 \to 1$ as $\delta \downarrow 0$ (passing `(PUR-io)` with arbitrary margin), while at $v = u/2$,
     $$
     I^{(+)}(u) = \log(1 + \delta) + 2\log\frac{1 + \delta^{-1/4}}{1 + \delta^{1/4}} \ge \frac{1}{2}\log(1/\delta) - 2\log 2 \longrightarrow +\infty,
     $$
     so both `TC_{traj}` and `TC_{diag}` fail arbitrarily badly! (Note that in a massive free field, $c_1/c_0$ is $O(1)$ per mode and the second term equals $\sum_k \log(1 + e^{-2v\omega_k}) \approx \log(1 + s(u))$ without explosion; for an interacting $0^{++}$ glueball coupled to a bare open boundary, the open boundary renormalizes to Lüscher–Schaefer open boundary conditions (GUIDE), and at fixed $\beta \in [2, 3]$ even $c_1/c_0 = O(n^3)$ is crushed by $e^{-m(\beta) v}$.)
   - *Explicit separation for `TS`:* On `TS`, putting absolute values inside $\sum_{e'}$ is strictly stronger than the signed integral $-2\log P_K$, and the diagonal arc length $\int_0^1 \|\widehat{\widetilde{A}}'(\lambda)\|_{\mathrm{HS}}\,d\lambda$ can exceed the chord angle $\arccos(P_K)$ whenever the curve $\lambda \mapsto \widehat{\widetilde{A}}(\lambda)$ bends off the geodesic (e.g., for any $3$-state operator family whose midpoint $\widetilde{A}(1/2)$ has an orthogonal component).
3. **Honest status under "Equivalent is not progress":** On general positive transfer data, our sufficient statements are **strictly stronger** than `(PUR-io)`, not equivalent to it. Inside pure 4D $\mathrm{SU}(2)$ Wilson theory along the calibrated trajectory $\beta_K$, we **cannot prove** that `(PUR-io)` does not imply `TC_{traj}` or `TS_{traj}` (strictness inside pure Wilson is OPEN), and we have not proved `TC_{diag}(eps)` at $\beta \in [2, 3]$ or the carry R12 to $\beta_K$. Therefore, under the programme rule, we claim **no progress toward solving `(PUR-io)` itself**—our positive contribution is the exact structural obstruction (Theorems 1.1–1.2), the exact neutral-sector interpolation structures passing all tests `(g1)`–`(g5)` (Theorems 2.1–2.3, 3.1–3.3), and the sharpest reduced band lemma attacked three ways below.

---

## 4. Stopping Lemma and Three Distinct Attacks at $\beta \in [2, 3]$

Because Structure II's diagonal arc-length lemma is **single-replica**, **100% gauge- and centre-invariant**, **zero-wall**, **1-parameter**, and **strictly reflection-positive**, and because its untwisted version `TC_{diag,0}(eps)` lives on a single pure Wilson Gibbs measure $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}$ with no twist mixture at all, we adopt the following single precise stopping lemma in the order-one band:

> **Stopping Lemma `TC_{diag,0}(eps)` (OPEN at $\beta \in [2, 3]$):** There exist $C < \infty$ and $\epsilon > 0$ such that, uniformly in $\beta \in [2, 3]$ and $n \in 1024\mathbb{N}$ ($u = n/512$, $v = u/2 = n/1024 \ge 3$),
> $$
> \int_0^1 \sqrt{3n^3 \sum_{e' \in E(\Sigma)} \operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)}\,d\lambda \;\le\; C v^{-\epsilon}, \tag{TC$_{\mathrm{diag}, 0}(\epsilon)$}
> $$
> where $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}$ is the single-replica untwisted Wilson Gibbs measure on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/2v)$ with temporal plaquette coupling $\lambda\beta$ on layers $0 \to 1$ and $v \to v+1$ and unmodified coupling $\beta$ on all other plaquettes, and $E_{\tau, e} = \beta\operatorname{Re} U_{p(\tau, e)}$.

By Theorem 2.2(3), `TC_{diag,0}(eps)` implies $S_{\mathrm{full}}(u; n^3; \beta) \to 0$ (hence $s_+(u) \to 0$, $P(\beta; n, u) \to 1$, and a full mass gap + confinement via Theorem S at every $\beta \in [2, 3]$). Every step below applies equally to the neutral-projected sibling `TC_{diag}(eps)`.

### Attack 1: Dobrushin Comparison and Anisotropic Midpoint-Polyakov Replica Exchange (Temporal Coupling Kept in $[2, 3]$)

Theorem 3.3 already proves `TC_{diag,0}(eps)` with exponential decay $O(\beta v^{3/2} (18\beta)^{(v-1)/2})$ for all $0 \le \beta < 1/18$. To push the temporal coupling all the way into the band $[2, 3]$ while preserving an exact positive decay theorem, we apply replica-exchange disagreement percolation on the **unpinned periodic torus** by placing the residual Polyakov temporal gauge links at the midpoint of the backward arc.

**Theorem 4.1 (Anisotropic Band-Temporal Decay for Two-Cut Covariance, PROVED).** *Consider the anisotropic 4D $\mathrm{SU}(2)$ Wilson measure $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}(b_t, \kappa)$ on $(\mathbb{Z}/n)^3 \times (\mathbb{Z}/2v)$ ($v \ge 4$) with temporal plaquette coupling $b_t \in [2, 3]$ (scaled to $\lambda b_t, \mu b_t$ on layers $0 \to 1$ and $v \to v+1$) and spatial plaquette coupling $\kappa \ge 0$. Set*
$$
p := 1 - e^{-12}, \qquad a := -\tfrac{1}{2}\log p > 0, \qquad L := \frac{1 + \sqrt{p}}{1 - \sqrt{p}}, \qquad J := 12, \qquad \kappa_* := -\frac{1}{4}\log\!\left(1 - \frac{1}{2 J L}\right) > 0.
$$
*Then for every $b_t \in [2, 3]$, $0 \le \kappa \le \kappa_*$, $(\lambda, \mu) \in [0, 1]^2$, and $e_0, e' \in E(\Sigma)$,*
$$
\Bigl|\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}(b_t, \kappa)}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)\Bigr|
\;\le\; 8 b_t^2 L\, e^{-a(\lfloor v/2 \rfloor - 1)}. \tag{4.1}
$$
*In particular, summing over $3n^3$ links $e'$ gives exponential decay of `TC_0(eps)` and `TC_{diag,0}(eps)` uniformly in $(\lambda, \mu) \in [0, 1]^2$ throughout $b_t \in [2, 3]$, $0 \le \kappa \le \kappa_*$.*

*Proof.* Set $\tau_* := v + \lfloor v/2 \rfloor$ (the midpoint of the backward arc $\{v+1, \dots, 2v-1\}$). By a Haar-preserving gauge change along the open time paths starting from slice $\tau_* + 1$ and running forward through $0, 1, \dots, v, \dots, \tau_*$, set all temporal links $V_{\tau, x} = 1$ for every $\tau \neq \tau_*$, leaving only the Polyakov temporal links $g_x := V_{\tau_*, x} \in \mathrm{SU}(2)$ on the single layer $\tau_* \to \tau_* + 1$. Since $v \ge 4$, the $g$-free region $\mathcal{R} = \{\tau \in \mathbb{Z}/2v : \tau \neq \tau_*, \tau_* + 1\}$ contains both seam layers $0 \to 1$ and $v \to v+1$ strictly in its interior, with vertical distance $\ge \lfloor v/2 \rfloor - 1$ from layer $0 \to 1$ to both layer $v \to v+1$ (forward arc, length $v - 1 \ge \lfloor v/2 \rfloor$) and layer $\tau_* \to \tau_* + 1$ (backward arc, length $\lceil v/2 \rceil - 1 \ge \lfloor v/2 \rfloor - 1$).

Take two independent copies $(U, g)$ and $(U', g')$ from $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}(b_t, \kappa)$. For each plaquette factor $f$ (a temporal bond $(U_{\tau, e}, U_{\tau+1, e})$ for $\tau \neq \tau_*$, a Polyakov plaquette at layer $\tau_*$, or a spatial plaquette on slice $\tau$), let $W_f$ be the product of its two replica weights and $w_{*, f}$ the minimum of $W_f$ over all partial swaps of its incident variable pairs; independently mark $f$ open with probability $1 - w_{*, f}/W_f$. Swapping any union of complete open components of variables preserves the joint distribution (Redner–Machta–Chayes / Adhikari–Cao; cf. row 1565 §2). On the event $\mathcal{E}$ that the union $C := \operatorname{Comp}(0, e_0) \cup \operatorname{Comp}(1, e_0)$ of the open components of $(0, e_0)$ and $(1, e_0)$ fails to reach either slice $v$ or slice $\tau_* + 1$, $C$ lies strictly inside the open arc $\{\tau_* + 2, \dots, 2v - 1, 0, 1, \dots, v - 1\}$; hence swapping $C$ preserves the joint distribution, reverses $E_{0, e_0} - E'_{0, e_0}$ (since both $(0, e_0), (1, e_0) \in C$), and leaves $E_{v, e'} - E'_{v, e'}$ fixed (as $C$ is disjoint from slices $v, v+1$ and from all Polyakov links $g_x$). Since $2\operatorname{Cov}(E_{0, e_0}, E_{v, e'}) = \mathbb{E}[(E_{0, e_0} - E'_{0, e_0})(E_{v, e'} - E'_{v, e'})]$ and $|E - E'| \le 2b_t$,
$$
\bigl|\operatorname{Cov}(E_{0, e_0}, E_{v, e'})\bigr| \le 2 b_t^2\,\mathbb{P}(\mathcal{E}^c).
$$
Inside the $g$-free region, every temporal bond has coupling $\le b_t \le 3$, so $e^{-2b_t} \le w_{*, f} \le W_f \le e^{2b_t}$ and conditional mark probability $\le 1 - e^{-4b_t} \le p$. Every spatial plaquette has conditional mark probability $\le p_s := 1 - e^{-4\kappa}$. On $\mathcal{E}^c$, at least one of the two sites $(0, e_0)$ or $(1, e_0)$ connects via a simple path of marked factors inside the $g$-free region to slice $v$ or slice $\tau_* + 1$ (total vertical displacement $\ge d := \lfloor v/2 \rfloor - 1$). Decomposing any simple path into alternating maximal vertical runs (weight $1 + 2\sum_{\ell \ge 1}(p e^a)^\ell = L$ with exponential tilt $e^{a\ell}$) and spatial plaquette steps ($4$ plaquettes per spatial link $\times 3$ exit links $= 12 = J$ choices, weight $p_s$), and applying the exact simple-path union bound of row 1565 §2 from both endpoints $(0, e_0)$ and $(1, e_0)$ gives
$$
\mathbb{P}(\mathcal{E}^c) \le 2 e^{-a d} \sum_{h \ge 0} L (J p_s L)^h \le 4 L e^{-a d}
$$
whenever $J p_s L \le 1/2$, i.e. $\kappa \le \kappa_*$. Multiplying by $2b_t^2$ yields (4.1). $\blacksquare$

**Exact failure point of Attack 1 at isotropy ($\kappa = b_t \in [2, 3]$):** At $\beta = \kappa = b_t = 2$, the unweighted single-link Dobrushin TV matrix already has bulk row sum $> 18/(10) = 1.8 > 1$ (row 1565 §1, checked in check 1571), and the replica-exchange path factor satisfies $J p_s L \ge 12(1 - e^{-8})(1 + \sqrt{1 - e^{-8}})/(1 - \sqrt{1 - e^{-8}}) > 10^3 \gg 1$, so worst-case mark percolation is deeply supercritical. Moreover, Theorem 4.1 holds identically for compact $\mathrm{U}(1)$ and in $D = 5$ (with $J = 18$), confirming that worst-case percolation contains no 4D non-abelian mechanism.

### Attack 2: Reflection-Positive Hilbert–Schmidt Spectral Analysis of $A(\lambda)$

Attack 2 exploits Theorem 2.2(3), which already eliminated two major obstructions of check 1556's `BC(eps)`: there is no $e^{+c\beta n^2}$ spatial wall excitation, and $h_{\mathrm{cut}}^0(\lambda) = \|A_0'(\lambda) - c(\lambda) A_0(\lambda)\|_{\mathrm{HS}}^2 / \|A_0(\lambda)\|_{\mathrm{HS}}^2$ is strictly nonnegative for every $\lambda \in [0, 1]$ with $A_0(\lambda) = T^{(v-1)/2} T(\lambda) T^{(v-1)/2}$.

Expand $A_0(\lambda)$ and $B_0(\lambda) = \partial_\lambda A_0(\lambda) = T^{(v-1)/2} T'(\lambda) T^{(v-1)/2}$ in the orthonormal eigenbasis $\{\psi_i\}_{i \ge 0}$ of $T$ ($T \psi_i = \lambda_i \psi_i$, $r_i = \lambda_i/\lambda_0$, $\psi_0 > 0$). Put $a_{ij}(\lambda) := \langle \psi_i, T(\lambda)\psi_j\rangle$ and $b_{ij}(\lambda) := \langle \psi_i, T'(\lambda)\psi_j\rangle$. Since $A_0(\lambda)_{ij} = \lambda_0^{v-1} (r_i r_j)^{(v-1)/2} a_{ij}(\lambda)$, subtracting $c_*(\lambda) = b_{00}(\lambda)/a_{00}(\lambda)$ (which minimizes $\|B_0 - c A_0\|_{\mathrm{HS}}^2$ up to higher order) gives the exact upper bound
$$
h_{\mathrm{cut}}^0(\lambda)
\le \frac{\|B_0(\lambda) - c_*(\lambda) A_0(\lambda)\|_{\mathrm{HS}}^2}{A_0(\lambda)_{00}^2}
= \sum_{(i, j) \neq (0, 0)} (r_i r_j)^{v - 1} \left|\frac{b_{ij}(\lambda)}{a_{00}(\lambda)} - \frac{b_{00}(\lambda)}{a_{00}(\lambda)}\frac{a_{ij}(\lambda)}{a_{00}(\lambda)}\right|^2. \tag{4.2}
$$

**Exact failure points of Attack 2 (two independent walls):**
1. *(Circularity at $\lambda = 1$)* At $\lambda = 1$, $T(1) = T$ is diagonal in $\{\psi_i\}$, so $a_{ij}(1) = \lambda_i \delta_{ij}$. Even restricting (4.2) to the diagonal terms $i = j \ge 1$ gives $\sum_{i \ge 1} r_i^{2v} |b_{ii}(1)/\lambda_i - b_{00}(1)/\lambda_0|^2$, which requires controlling the weighted excited thermal sum $\sum_{i \ge 1} r_i^u$—already of seed strength at $\beta \in [2, 3]$! (Worse, the prefactor $|b_{ii}(1)/\lambda_i - b_{00}(1)/\lambda_0|$ is the temporal action-insertion difference between level $i$ and the vacuum, the exact object of `(VIR_K)` / registry R11.)
2. *(Extensive $L^2$ boundary-overlap wall at $\lambda = 0$)* At $\lambda = 0$, $T(0) = |M\mathbf{1}\rangle\langle M\mathbf{1}|$, so $a_{00}(0) = \langle M\mathbf{1}, \psi_0\rangle^2$, while $\|T(0)\|_{\mathrm{op}} = \|M\mathbf{1}\|_2^2$. Since $M(A) = \exp(\frac{\beta}{2}\sum_{p\subset\Sigma} \operatorname{Re} A_p)$ differs from the vacuum density on every plaquette of the 3D slice, the global $L^2$ ratio $\|M\mathbf{1}\|_2^2 / \langle M\mathbf{1}, \psi_0\rangle^2 = \sum_{i \ge 0} c_i/c_0$ grows exponentially in the 3D slice volume $n^3$ (just as in row 1207 / check 1208's Doob penalty!). Bound (4.2) cannot pay $e^{+c(\beta) n^3}$ using $r_1^{v-1} = e^{-m(\beta)(v-1)}$ because $n^3 \gg v = n/1024$. As Theorem 2.3 proved for a massive free field, the actual $h_{\mathrm{cut}}^0(0) = O(n^3 e^{-2mv})$ does **not** suffer this $e^{+c n^3}$ blowup, because the excitations of $M\mathbf{1}$ factorize across modes and cancel logarithmically; global Hilbert–Schmidt spectral bounds cannot see that cluster cancellation.

### Attack 3: Conditional $\mathbb{Z}_2 \times \mathrm{SO}(3)$ Decomposition and Bakry–Émery / Helffer–Sjöstrand Curvature

Attack 3 directly targets the logarithmic Gibbs covariance $\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}}(E_{0, e_0}, E_{v, e'})$ without global $L^2$ spectral norms, via two complementary non-abelian tools.

**3A. Structural blindness of $\mathbb{Z}_2 \times \mathrm{SO}(3)$ centre conditioning (PROVED identity; ARGUED obstruction).** Write $U_b = z_b V_b$ with $z_b \in \{\pm 1\}$ and $V_b \in \mathrm{SU}(2)$ a fixed Borel lift of $\mathrm{Ad}(U_b) \in \mathrm{SO}(3)$. For every plaquette $p$, $E_p = \beta\operatorname{Re} U_p = \beta (dz)_p \eta_p(V) |\operatorname{Re} V_p|$, where $\eta_p(V) = \operatorname{sgn}(\operatorname{Re} V_p)$. By the law of total covariance conditioning on the entire $\mathrm{SO}(3)$ field $V$,
$$
\operatorname{Cov}_{\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \lambda}}\!\bigl(E_{0, e_0},\; E_{v, e'}\bigr)
= \mathbb{E}_V\Bigl[\operatorname{Cov}\bigl(E_{0, e_0},\; E_{v, e'} \mid V\bigr)\Bigr]
+ \operatorname{Cov}_V\Bigl(\mathbb{E}[E_{0, e_0} \mid V],\; \mathbb{E}[E_{v, e'} \mid V]\Bigr). \tag{4.3}
$$
Even in the best-case scenario where the conditional $\mathbb{Z}_2$ gauge model freezes completely onto $(dz)_p = \eta_p(V)$ (eliminating the first term; note check 1556 §(vi) already shows frustrated cubes occur at positive density for finite $\beta$, blocking FKG in the first term anyway), the second term becomes $\operatorname{Cov}_V(\beta|\operatorname{Re} V_{p(0, e_0)}|,\; \beta|\operatorname{Re} V_{p(v, e')}|)$: the full connected correlation of the **centre-neutral $\mathrm{SO}(3)$ adjoint energy density**. Thus centre-coset conditioning leaves the entire neutral glueball channel untouched.

**3B. Bakry–Émery / Helffer–Sjöstrand curvature: small-$\beta$ proof and exact smooth-field paramagnetic instability for all $\beta > 1$ (PROVED).** Equip each $\mathrm{SU}(2)$ link factor with the bi-invariant metric in which the left-invariant vector fields $L_{b, a} f(U) = \frac{d}{dt}\big|_{t=0} f(U_b e^{t e_a/2})$ ($a = 1, 2, 3$, with unit quaternions $e_1 e_2 = e_3$ so $[L_a, L_b] = \varepsilon_{abc} L_c$) form an orthonormal frame. In this normalization (corresponding to the round $3$-sphere of radius $2$, matching check 1527 §(iv) line 88 and Lichnerowicz eigenvalue $\lambda_1(-\Delta) = 3/4$), $\operatorname{Ric}_{\mathrm{SU}(2)}(v, v) = \frac{1}{2}\|v\|^2$ on every link. For the Wilson measure $d\mu \propto e^{S(U)} dU$, the Helffer–Sjöstrand / Witten $1$-form operator on $M = \mathrm{SU}(2)^{E(\Lambda)}$ is
$$
\mathcal{H}_1 = \nabla^*\nabla + \operatorname{Ric} - \operatorname{Hess}\, S = \nabla^*\nabla + \frac{1}{2} I - \operatorname{Hess}\, S.
$$

**Theorem 4.2 (Bakry–Émery Small-$\beta$ Domain and Exact Smooth-Field Instability for All $\beta > 1$, PROVED).**
1. *(Small-$\beta$ uniform positivity)* On any 4D Wilson lattice (including $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}$ for all $\lambda, \mu \in [0, 1]$), $\|\operatorname{Hess}\, S\|_{\mathrm{op}} \le \frac{21}{2}\beta$ pointwise at every configuration $U \in M$. Hence for every $0 \le \beta < 1/21$, $\operatorname{Ric} - \operatorname{Hess}\, S \succeq (\frac{1}{2} - \frac{21}{2}\beta) I > 0$ uniformly on $M$ (supplying a Bakry–Émery / Brascamp–Lieb spectral gap $\ge \frac{1}{2} - \frac{21}{2}\beta$ and Helffer–Sjöstrand exponential covariance decay via finite-range Hessian propagation).
2. *(Exact small-field paramagnetic instability for every $\beta > 1$)* On $\Lambda = (\mathbb{Z}/n)^3 \times (\mathbb{Z}/2v)$ with $n$ even, fix any $\varepsilon \in (0, \pi)$ and consider the smooth configuration $U^{(\varepsilon)}$ defined by
   $$
   U^{(\varepsilon)}_{x, 1} = \begin{cases} e^{\varepsilon e_3/2}, & x_2 \text{ even}, \\ 1, & x_2 \text{ odd}, \end{cases}
   \qquad U^{(\varepsilon)}_{x, 2} = U^{(\varepsilon)}_{x, 3} = U^{(\varepsilon)}_{x, 0} = 1 \quad \forall x \in \Lambda,
   $$
   whose every plaquette satisfies $\operatorname{Re} U^{(\varepsilon)}_p \in \{\cos(\varepsilon/2), 1\}$, and the constant left-invariant tangent vector $v$ with
   $$
   v_{x, 1} = e_1, \qquad v_{x, 2} = (-1)^{x_2 + 1} e_2, \qquad v_{x, 3} = v_{x, 0} = 0 \quad \forall x \in \Lambda.
   $$
   Then for **every** $(\lambda, \mu) \in [0, 1]^2$, the Bakry–Émery curvature tensor of $\mathbb{P}^{\mathrm{cut}, 0}_{\lambda, \mu}$ at $U^{(\varepsilon)}$ satisfies **exactly**
   $$
   \frac{(\operatorname{Ric} - \operatorname{Hess}\, S)(v, v)}{|\Lambda|} = 1 - \beta \sin\!\left(\frac{\varepsilon}{2}\right). \tag{4.4}
   $$
   In particular:
   - At every $\beta > 1$ (covering the entire band $\beta \in [2, 3]$), choosing $\varepsilon \in (2\arcsin(1/\beta), \pi)$ makes $\operatorname{Ric} - \operatorname{Hess}\, S$ strictly negative! (At $\beta = 2$, $\varepsilon = \pi/2$ already has $\operatorname{Re} U_p = \frac{\sqrt{2}}{2} \approx 0.707$ and gives $1 - \sqrt{2} \approx -0.414 < 0$.)
   - At arbitrarily large $\beta$, the instability already occurs at $\varepsilon = 4/\beta \ll \beta^{-1/2}$ (far smoother than typical Wilson fields, which have curvature $\sim \beta^{-1/2}$), giving $1 - \beta\sin(2/\beta) \le 1 - 4\sin(1/2) < -0.9 < 0$ for all $\beta \ge 4$ (and approaching $-1$ as $\beta \to \infty$).

*Proof.*
(1) For a single plaquette $U_p = U_1 U_2 U_3^{-1} U_4^{-1}$ with $U_r(t) = U_r e^{t v_r/2}$ ($v_r = \sum_{a=1}^3 v_{r,a} e_a \in \operatorname{Im}\mathbb{H}$, $\|v_r\|^2 = \sum_a v_{r,a}^2$), transporting all four velocities to the right end of $U_p$ yields signed unit-norm-preserving velocities $\tilde v_1, \tilde v_2, \tilde v_3, \tilde v_4 \in \operatorname{Im}\mathbb{H}$ ($\|\tilde v_r\| = \|v_r\|$) with
$$
U_p(t) = U_p \exp\!\left(\frac{t}{2}\tilde v_1\right)\exp\!\left(\frac{t}{2}\tilde v_2\right)\exp\!\left(\frac{t}{2}\tilde v_3\right)\exp\!\left(\frac{t}{2}\tilde v_4\right)
= U_p\left(1 + \frac{t}{2}\sum_{r=1}^4 \tilde v_r + \frac{t^2}{8}\Bigl(\sum_{r=1}^4 \tilde v_r\Bigr)^2 + \frac{t^2}{8}\sum_{1\le r < s \le 4} [\tilde v_r, \tilde v_s] + O(t^3)\right).
$$
Since $(\sum \tilde v_r)^2 = -\|\sum \tilde v_r\|^2 \in \mathbb{R}$ and $|[\tilde v_r, \tilde v_s]| = 2\|v_r \times v_s\| \le 2\|v_r\|\|v_s\|$, differentiating twice at $t = 0$ and taking $\operatorname{Re}$ gives
$$
\left|\frac{d^2}{dt^2}\Big|_{t=0} \operatorname{Re} U_p(t)\right|
\le \frac{1}{4}\Bigl\|\sum_{r=1}^4 \tilde v_r\Bigr\|^2 + \frac{1}{4}\sum_{1 \le r < s \le 4} 2\|v_r\|\|v_s\|
\le \sum_{r=1}^4 \|v_r\|^2 + \frac{3}{4}\sum_{r=1}^4 \|v_r\|^2 = \frac{7}{4}\sum_{r=1}^4 \|v_r\|^2.
$$
Multiplying by $b_p \le \beta$ and summing over all plaquettes (each link belongs to $6$ plaquettes in $D = 4$) yields $|(\operatorname{Hess}\, S)(v, v)| \le 6 \cdot \frac{7}{4}\beta \|v\|^2 = \frac{21}{2}\beta \|v\|^2$.

(2) Under $U_e(t) = U^{(\varepsilon)}_e e^{t v_e/2}$, check every plaquette orientation on $\Lambda$ ($n$ even ensures $(-1)^{x_2+1}$ is periodic):
- For every $(1, 3)$, $(1, 0)$, $(2, 3)$, $(2, 0)$ plaquette, the two opposite active links share the same $x_2$-coordinate, hence the same $U^{(\varepsilon)}_e$ and the same $v_e$, while the other two links have $U = 1, v = 0$; therefore $U_p(t) \equiv 1$ identically in $t$ (including on the $\lambda, \mu$-dialed temporal layers!). Every $(3, 0)$ plaquette has $v = 0$, so $U_p(t) \equiv 1$.
- For a $(1, 2)$ plaquette based at $x$ with $x_2$ **even**, $U_1 = e^{\varepsilon e_3/2}$, $U_2 = U_3 = U_4 = 1$, $v_1 = v_3 = e_1$, $v_2 = v_4 = -e_2$:
  $$
  U_p(t) = e^{\varepsilon e_3/2} e^{t e_1/2} e^{-t e_2/2} e^{-t e_1/2} e^{t e_2/2}
  = e^{\varepsilon e_3/2} \exp\!\left(-\frac{t^2}{4}[e_1, e_2] + O(t^3)\right)
  = \exp\!\left(\frac{\varepsilon - t^2}{2} e_3 + O(t^3)\right),
  $$
  using $[e_1, e_2] = 2e_3$. Hence $\operatorname{Re} U_p(t) = \cos\bigl(\frac{\varepsilon - t^2}{2}\bigr) + O(t^3) = \cos(\varepsilon/2) + \frac{t^2}{2}\sin(\varepsilon/2) + O(t^3)$, so $\frac{d^2}{dt^2}\big|_{t=0} \operatorname{Re} U_p(t) = +\sin(\varepsilon/2)$.
- For a $(1, 2)$ plaquette based at $x$ with $x_2$ **odd**, $U_3 = e^{\varepsilon e_3/2}$, $U_1 = U_2 = U_4 = 1$, $v_1 = v_3 = e_1$, $v_2 = v_4 = +e_2$:
  $$
  U_p(t) = e^{t e_1/2} e^{t e_2/2} (e^{\varepsilon e_3/2} e^{t e_1/2})^{-1} e^{-t e_2/2}
  = e^{t e_1/2} e^{t e_2/2} e^{-t e_1/2} e^{-\varepsilon e_3/2} e^{-t e_2/2}.
  $$
  Conjugating by $e^{t e_2/2}$ preserves $\operatorname{Re}$ and yields
  $$
  e^{-t e_2/2} e^{t e_1/2} e^{t e_2/2} e^{-t e_1/2} e^{-\varepsilon e_3/2}
  = \exp\!\left(-\frac{t^2}{4}[e_2, e_1] + O(t^3)\right) e^{-\varepsilon e_3/2}
  = \exp\!\left(-\frac{\varepsilon - t^2}{2} e_3 + O(t^3)\right),
  $$
  using $[e_2, e_1] = -2e_3$. Again $\operatorname{Re} U_p(t) = \cos(\varepsilon/2) + \frac{t^2}{2}\sin(\varepsilon/2) + O(t^3)$, so $\frac{d^2}{dt^2}\big|_{t=0} \operatorname{Re} U_p(t) = +\sin(\varepsilon/2)$.
Summing over all $|\Lambda|$ spatial $(1, 2)$ plaquettes gives $(-\operatorname{Hess}\, S)(v, v) = -|\Lambda|\beta\sin(\varepsilon/2)$, while each site has two active links of unit norm, giving $\operatorname{Ric}(v, v) = |\Lambda| \cdot (\frac{1}{2} + \frac{1}{2}) = |\Lambda|$. Adding yields (4.4). $\blacksquare$

**Exact failure point of Attack 3:** Theorem 4.2(2) exhibits the exact lattice Nielsen–Olesen / paramagnetic spin instability: on $\mathcal{A}$, pointwise Bakry–Émery positivity fails throughout $\beta > 1$ even inside the deep small-field regime $\varepsilon \sim 4/\beta \ll \beta^{-1/2}$. Controlling $\mathcal{H}_1^{-1}$ at $\beta \in [2, 3]$ therefore cannot come from pointwise curvature lower bounds; it requires a genuine *in-law* cancellation between the bare positive Ricci curvature, the indefinite spin term, and the kinetic term $\nabla^*\nabla$ (the same non-perturbative wall identified in rows 1011, 1244, 1526/1527).

---

## 5. Summary of Claim Standings

| Claim | Standing | Scope / Anchors |
|---|---|---|
| Theorem 1.1 (orientation obstruction for odd-dim single-link swaps and $\mathcal{M}(\mathrm{U}(1))^2$) | **PROVED** | All odd-dimensional compact connected $G$ ($\mathrm{SU}(2), \mathrm{U}(1), \mathrm{SU}(2k)$); codim $\ge 2$ singular sets. |
| Theorem 1.2 (1-form cohomology obstruction for finite-range gauge-descending replica swaps) & Corollary 1.2' | **PROVED** | 4D $\mathrm{SU}(2)$, $n \ge 2R + 7$, $\alpha > 1/10$ Hölder, Haar domination; compact $\mathrm{U}(1)$ via $\pi_1(S^1) = \mathbb{Z}$; contrasts with free Maxwell ($G = \mathbb{R}$) and check 1556's $R_s$. |
| Proposition 1.3 (global comb-tree circle action $\Phi_s^{\mathrm{tree}}$ on $\mathcal{H}_0 \otimes \mathcal{H}_0$) | **PROVED** | Explicit Haar-preserving circle action; analytic wall / nonlocality defect **ARGUED**. |
| Remark 1.4 (spatial branched-cover Rényi-2 sweep area-law wall) | **ARGUED** | Exact gauge-invariant 8-link branch plaquettes; $O(\beta n^2)$ wall. |
| Theorem 2.1 (connected $\mathrm{SO}(2) \subset \mathrm{Sp}(2)$ two-seam identity, diagonal RP, and Hilbert–Schmidt angle bound for $P_K$) & Remark 2.1' | **PROVED** | Exact for all $\beta \ge 0$, $n \ge 3$, $u = 2v$, $v \ge 3$; zero spatial wall; no Higgs field. |
| Theorem 2.2 (single-replica, 100% gauge- and centre-invariant two-cut neutral seed inequality & diagonal arc-length bound) | **PROVED** | Exact cancellation of $\lambda_0$ and $c_0$; pure-Gibbs untwisted and neutral-projected forms. |
| Theorem 2.3 (exact free-field two-cut identity, Wick positivity, and $\Theta_D(v^{-(D-1)})$ marginal scaling in every $D \ge 3$) | **PROVED** | Exact mode-by-mode equality to $1/P_{\mathrm{mode}}$; asymptotically sharp diagonal arc length; fails for free Maxwell in $D = 3, 4, 5$. |
| Theorem 3.1 (interacting weak 4D compact Villain $\mathrm{U}(1)$ neutral refutation) | **PROVED GIVEN** | Given PV (7.3), row 786/794, row 1368/1370, and Corollary EV: $s_+^{\mathrm{Villain}}(u) > 4/21$ and $P_K^{\mathrm{Villain}, \mathrm{U}(1)} < 457/625$ at all $\beta \ge 2^{14}$ and $n \in 1024\mathbb{N}$. |
| Corollary 3.2 (interacting weak 4D Wilson cosine $\mathrm{U}(1)$ unprojected refutation) | **PROVED GIVEN** | Given row 1565 (7) / check 1571 ($\beta_W \ge \beta_*$). Neutral-projected Wilson cosine remains **OPEN**. |
| Theorem 3.3 (strong-coupling exponential decay in all four gapped twins) | **PROVED** | Uniform in $(\lambda, \mu) \in [0, 1]^2$ for $6(D-1)\beta < 1$ (4D $\beta < 1/18$, 5D $\beta < 1/24$, 3D $\beta < 1/12$). |
| Tests `(g4)` (neutral spectators, K7, adjoint-Higgs) and `(g5)` ($\beta \to \infty$ at fixed lattice) | **PROVED** (spectator additivity & `(g5)` given check 1527 §(iii)); **BELIEF** (K7 / adjoint-Higgs gaplessness) | Passes `(g4)` completely (unlike check 1556's `BC(eps)`). |
| Non-equivalence to `(PUR-io)` | **PROVED** on positive transfer data (strictly stronger); **OPEN** inside pure Wilson on $\beta_K$ | Explicit 2-level counterexample with $P_K \to 1$ and $I^{(+)}(u) \to \infty$; trajectory form requires non-asymptotic threshold `TC_{traj}` / `TS_{traj}` (not $v^{-\epsilon}$). |
| Theorem 4.1 (anisotropic band-temporal decay $b_t \in [2, 3]$, $\kappa \le \kappa_*$) | **PROVED** | Midpoint Polyakov gauge + replica-exchange percolation; fails at isotropy ($J p_s L > 10^3$). |
| Theorem 4.2 (Bakry–Émery small-$\beta < 1/21$ bound & exact smooth-field instability for all $\beta > 1$) | **PROVED** | Explicit witness $U^{(\varepsilon)}$ gives $(\operatorname{Ric} - \operatorname{Hess}\, S)(v, v)/|\Lambda| = 1 - \beta\sin(\varepsilon/2) < 0$ already at $\varepsilon = 4/\beta \ll \beta^{-1/2}$. |
| Stopping Lemma `TC_{diag,0}(eps)` (and `TC_{diag}(eps)`, `TS_{diag}(eps)`) at $\beta \in [2, 3]$, carry R12 to $\beta_K$, `(PUR-io)`, and the 4D $\mathrm{SU}(2)$ mass gap | **OPEN** | Neither proved nor refuted. |

RESULT: Neither (PUR-io) nor the 4D SU(2) mass gap is proved or disproved; PROVED: exact topological/cohomological no-go theorems excluding single-link odd-dimensional replica-swap flows (Theorem 1.1) and every finite-range, regular, Haar-dominated, gauge-and-centre-descending deterministic replica-swap interpolation on 4D SU(2) and compact U(1) (Theorem 1.2, contrasting with check 1556's cut rotation and free Maxwell), an explicit global comb-tree circle action on the neutral orbit space showing why breaking locality alone hits an O(beta n^3) wall (Proposition 1.3), and two local, zero-wall, unpinned neutral-sector structures escaping Theorem 1.2—the connected SO(2) in Sp(2) two-seam interpolation reading -2 log P_K and arccos(P_K) directly without a Higgs field (Theorem 2.1), and the single-replica, 100% gauge- and centre-invariant two-cut interpolation Z_cut^+(lambda, mu; u) reading log(1 + s_+(u)) directly via both a four-corner covariance identity and a 1-parameter reflection-positive diagonal Hilbert-Schmidt arc-length bound (Theorem 2.2) that equals -log P_free exactly in free fields of every dimension D >= 3 (Theorem 2.3); both pass the full row 1553 §1.5 / check 1556 filter—failing for interacting weak 4D compact Villain U(1) even in the neutral sector (Theorem 3.1, proved given PV/row 786/row 1368/Corollary EV), for interacting weak 4D Wilson U(1) unprojected (Corollary 3.2, given row 1565), for free 3D/4D/5D Maxwell at the exact marginal power v^(-(D-1)), for any seedless neutral spectator (g4), and as beta -> infinity at fixed lattice (g5), while passing all four strong-coupling gapped twins exponentially (Theorem 3.3); both are strictly stronger than (PUR-io) on positive transfer data (strictness inside pure Wilson on beta_K is OPEN; fixed-beta lemmas still require carry R12); stopped at the 1-parameter reflection-positive diagonal lemma TC_{diag,0}(eps) at beta in [2, 3], attacked three distinct ways without closure (Dobrushin + midpoint-Polyakov anisotropic replica exchange proved for b_t in [2, 3], kappa <= kappa_* in Theorem 4.1, supercritical at isotropy; Hilbert-Schmidt spectral expansion circular at lambda = 1 and blocked by e^(c n^3) boundary overlap at lambda = 0; Z_2 x SO(3) conditioning blind to the neutral SO(3) channel and Bakry-Emery curvature proved for beta < 1/21 but refuted for all beta > 1 on an explicit smooth small-field paramagnetic witness in Theorem 4.2).
