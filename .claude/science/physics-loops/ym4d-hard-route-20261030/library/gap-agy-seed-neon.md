lead: google/gemini-4-neon-xhigh/agy laptop

# Row 1368 (`gap-agy-seed-neon`): Neutral Seed for 4D SU(2) Wilson Lattice Yang–Mills

Started: 2026-11-21T20:59Z (laptop `agy` CLI, `google/gemini-4-neon-xhigh`, third provider; plain brief, strictly independent of row 1367).

---

## 0. Executive Summary, Repo Search, Credits, and Top-Line Verdict

### 0.1 Top-line verdict

- **Status of `(M-neutral)` / `(N-phys)` / mass gap (`OPEN`).** The neutral rank-one test `(M-neutral)` at tolerance $2/5$ (equivalently $s(2w) \le 4/21$ uniformly at late cutoffs on the Wilson trajectory in the coupling band $\beta_0 \le \beta_j \le B_0 \log(L/a_j)$ of `library/gap-phys-seed.md`), the neutral seed `(N-phys)`, and the Jaffe–Witten mass gap are **not proved** and **not disproved** here.
- **Status of the checked chain (`PROVED` / no step disproved).** Every link of the checked chain `(M-neutral)` (row 1356, checked row 1359) $\Rightarrow$ `(N-phys)` (row 1353, checked row 1355) $\Rightarrow$ one-cube neutral consumer to Pfaffian seed $S_\kappa$ / `(G_ev-phys)` (row 1161, checked row 1162; row 731, checked row 732; row 705, checked row 707) $\Rightarrow$ matched continuum gap clause (row 1179, checked row 1183; row 1342, checked row 1349) was audited and **no step is disproved**.
- **What this work adds (`PROVED` — all new, exact, hand-checkable, zero floating point in proofs):**
  1. **Exact Frame-1 sector-cancellation identities and universal sector bounds (Theorem 1).** Six exact nonnegative Frame-1 combinations **(ID1)**–**(ID3-mag1)** whose Frame-1 channels are all misaligned, plus two universal $S_4$ identities on every symmetric $n^4$ torus ($4 \mid n$ or even $n \ge 4$, all $\beta \ge 0$): the *exact misaligned-electric identity* $\sum_{q \text{ mis. at } e_1} X_{e_1, q}(n) = X_{0, e_1}(n) - X_{0, e_{123}}(n) \ge 0$ (hence $X_{0, e_1}(n) \ge X_{0, e_{123}}(n)$ universally) and the *universal magnetic ceiling* $X_{e_1, e_1}(n) \le \frac{2}{3}(1 + s(n))$.
  2. **Factor-of-2 sharpened aligned tail bound (Lemma 2).** Improves row 1161 eq. (4)'s aligned tail bound from $2 d^{v/u}$ to $d^{v/u}$ for every integer $v \ge 2u$ (no divisibility $u \mid v$ needed).
  3. **Four exact optimal LP-dual certificates (Lemma 3) and the derivative-free one-cube neutral consumer (Theorem 4 & Corollary 5).** Replaces row 1161's finite-difference one-cube consumer — which required $n \ge 2^{70} \approx 1.18 \times 10^{21}$, aspect ratio $K = 512$, and suffered $O(\sqrt{h})$ error — by a purely algebraic, derivative-free consumer that:
     - **completely eliminates the $n \ge 2^{70}$ floor** (holds for every $4 \mid n$, every integer $u \ge 3$ with $n \ge K u$, e.g. $n \ge 104$ for `(M-neutral)` and $n \ge 180$ for `(N-phys)`);
     - improves the error rate from $O(\sqrt{h})$ to the **exact optimal linear rate** $14\, d^{v/u} + O(d^K)$ simultaneously for every integer $v \in [n/2, n]$;
     - combined with the already-checked two-time Proposition B3 ($t = n/2, t' = 3n/4, H = (2n)^3$) and Theorem SH line $r = 4$ (threshold $1/25$, row 705 checked row 707; still requiring only $4 \mid n$), slashes the required aspect ratio from **$K = 512$** down to:
       - **`(M-neutral)` ($s_0 = 4/21$, $u = 2w$):** **$K = 34$** ($w \le n/68$, $n \ge 104$) via Proposition B3 ($r = 4$); or directly at $v = n/2$ without enlargement, **$K = 40$** (for $S_\kappa(n/2; n^3) < 1/1650$) and **$K = 44$** (for $S_\kappa(n/2; n^3) < 1/5041$).
       - **`(N-phys)` ($s_0 = 1/2$):** **$K = 60$** ($u \le n/60$, $n \ge 180$) via Proposition B3 ($r = 4$); or directly at $v = n/2$, **$K = 70$** ($< 1/1650$) and **$K = 78$** ($< 1/5041$).
     - preserves and tightens the Alternative I / Alternative II dichotomy and transverse selection bound ($\mathbb{P}_n(m \neq 0) \le 1.67 \times 10^{-5}$ at $K = 34$ in Alt II, vs row 1161's $1/1000$ at $K = 512$).
     - *(GUIDE)* Physically, shrinking $K$ from $512$ to $34$ reduces the required neutral seed cube side from $L \approx 11{,}000\,\xi$ (row 1180) to $L \approx 466\,\xi$, a **$23\times$ reduction in box side** and **$> 3 \times 10^5\times$ reduction in physical 4-volume $L^4$**.
  4. **Exact sharpness of the leading constant $14$ (Proposition 6).** Explicit two-line primal families in both Alt I and Alt II, realized by finite positive spectra with even misaligned multiplicities and $s(v) \equiv 0$, satisfying all Frame-1 and diamagnetic inequalities for every $v \ge 1$ and attaining $S_\kappa(n/2) = S_{\mathrm{per}}(n/2) = 14 t$ (Alt I) and $S_\kappa(n/2) = S_{\mathrm{full}}(n/2) = 14 t$ (Alt II) *exactly*.
  5. **Exact all-integer-period spectral obstruction to `(EV-STEP)` at aspect $K = 2$ (Theorem 7).** Explicit closed-form rational-eigenvalue positive-spectrum family (even multiplicity in all 42 misaligned sectors) with $s(k n/2) = 0$ for every integer $k \ge 1$, all 64 Frame-1 traces $H_{1, c, q_{\mathrm{new}}}(k n/2) \ge 0$ and $0 \le I(k n/2, B) \le I(k n/2, 0)$ for every integer $k \ge 1$, exact $S_4$ symmetry across all 11 $S_4$-orbits of $B$ at $k = 2$ ($v = n$), yet $S_\kappa(n/2) = 7$ (the literal algebraic maximum). We also show via Jensen's entropy inequality why non-integer times $v \in (n/2, n)$ break `(ID1)` at $r = 1^+$, explaining structurally why aspect $K > 2$ (or dynamical input beyond integer-period Frame-1 positivity) is indispensable.
  6. **Coupling-band diagnosis and audit of `(M-neutral)` (Section 4, `ARGUED` / `GUIDE` / `OPEN`).** Clarifies the role of the lead-note range $\beta_0 \le \beta_j \le B_0 \log(L/a_j)$ (explaining why `(M-neutral)` cannot hold for arbitrary $B_0$ above the asymptotic-freedom coefficient $11/(3\pi^2)$, and why along the physical trajectory the remaining wall is a single in-law bound at order-one effective coupling).

### 0.2 Repo search and independence record (`GUIDE`)

Files read in this worktree (strictly $\le$ row 1366; row 1367 was never read or inspected):
- `GOAL.md`, `parts/gap.md`, `FINISH.md` (rows 1175–1366 RESULT lines).
- `library/gap-phys-seed.md` (including Theorem ZD-c and both 2026-11-21 lead notes), `library/gap-seed-shape.md` (Lemma E2, Proposition B3, Theorem SH), `library/gap-flux-exercise.md` (§§3, 8, Pfaffian seed $W_\kappa$ and Theorem S-w).
- `library/gap-solve9-astra62.md` (row 1161) and `library/gap-solve9-check-opus.md` (row 1162).
- `library/gap-mini-branch-fable.md` (row 1179), `library/gap-mini-neutral-fable.md` (row 1180), `library/gap-mini-neutral2-fable.md` (row 1184), `library/gap-solve35-astra62.md` (row 1315), `library/gap-agy-argon-check-opus.md` (row 1206).
- Recent chain and checks: `library/gap-seed-audit-fable.md` (row 1342), `library/gap-seed-audit-check-astra.md` (row 1349), `library/gap-mini-neutral-step-fable.md` (row 1353), `library/gap-mini-neutral-step-check-astra.md` (row 1355), `library/gap-mini-mneutral-fable.md` (row 1356), `library/gap-mini-mneutral-check-astra.md` (row 1359), `library/gap-mini-seed-fable.md` (row 1363), `library/gap-mini-seed2-fable.md` (row 1364), `library/gap-mini-seed-check-astra.md` (row 1365), `library/gap-mini-seed2-check-astra.md` (row 1366).

Targeted grep across `library/gap-*.md` confirmed that no prior file removes row 1161's $n \ge 2^{70}$ floor or reduces its one-cube aspect ratio $K = 512$, nor contains the derivative-free Frame-1 certificates (Lemma 3), the sharpness constant $14$ (Proposition 6), or the all-integer-period $K = 2$ obstruction (Theorem 7).

### 0.3 Credits and statement labels (`GUIDE`)

- **Primary literature:** K. G. Wilson (lattice action); K. Osterwalder & E. Seiler (reflection positivity, transfer operator); M. Lüscher (transfer matrix, small-volume spectrum); G. 't Hooft (twisted boundary conditions, electric/magnetic duality, compensated translations); G. Mack & V. B. Petkova (center vortices and twist ratios); T. Bałaban (ultraviolet renormalization group); E. Sussman & L. Alpoge (with Claude and Codex as authors of their text, Theorem 0 ultraviolet reconstruction chain).
- **Lane rows:** `claude-fable-5-2` (Theorem S, Proposition B3, Theorem SH in rows 697, 705; Theorem ZD-c in row 720; Pfaffian seed $W_\kappa$ and Theorem S-w in row 731; branch consumer in row 1179; Lemma N1 in row 1184; seed audit in row 1342; `(N-phys)` step in row 1353; Lemma M1, Corollary M2, `(M-neutral)` in row 1356; seed attempts in rows 1363, 1364); `gpt-6.2-astra` / `gpt-6-astra` (one-cube consumer and compensated-translation multiplicity in row 1161; checks in rows 699, 1349, 1355, 1359, 1365, 1366); `claude-opus-5-5` (checks in rows 698, 707, 732, 1162, 1206).
- **Labels:** Every statement below is labeled `PROVED` (complete self-contained proof by hand with exact rational arithmetic, unchecked by another model), `PROVED GIVEN (...)` (depends explicitly on named checked lane theorems), `ARGUED`, `GUIDE` (heuristic/physical estimate, used in no proof step), or `OPEN`. No unchecked floating-point arithmetic is used in any proof step.

---

## 1. Exact Frame-1 Sector-Cancellation Identities and Universal Bounds

### 1.1 Setting and exact coordinate conventions (`PROVED`, matching row 1161)

Work on a periodic four-dimensional lattice torus $Q_v = (v, n, n, n)$ with spacetime axes $(0, 1, 2, 3)$, where $n \ge 4$ is even and $v \ge 3$ is an integer, with the four-dimensional $SU(2)$ Wilson action at arbitrary coupling $\beta \ge 0$. Represent a $\mathbb{Z}_2$ center twist by an alternating $4 \times 4$ matrix $B = (B_{\mu\nu}) \in \Lambda^2 \mathbb{F}_2^4$.

In **Frame 0** (time = axis $0$, length $v$; spatial cube $n^3$ along axes $(1, 2, 3)$), write $B = (m, e)$ with
$$m = (B_{23}, B_{13}, B_{12}) \in \mathbb{F}_2^3, \qquad e = (B_{01}, B_{02}, B_{03}) \in \mathbb{F}_2^3, \qquad \operatorname{Pf}(B) = m \cdot e \pmod 2.$$
Let $F_m = F_{m; n^3} \ge 0$ be the positive trace-class Wilson transfer operator in static magnetic twist $m$ on $n^3$, $\lambda_0 := \|F_0\| > 0$ its simple Perron–Frobenius ground-state eigenvalue, and for each electric character $q \in \mathbb{F}_2^3$ define
$$X_{m, q}(v) := \operatorname{Tr}_q\!\left(\frac{F_m}{\lambda_0}\right)^{\!v} \ge 0, \qquad s(v) := X_{0, 0}(v) - 1 \ge 0, \qquad b_{m, q} := \frac{\|F_m|_q\|}{\lambda_0} \in [0, 1],$$
with $b_{m, q} = 0$ if sector $(m, q)$ vanishes. The normalized twisted partition functions are
$$I(v, m, e) := \frac{Z_{(m, e)}(v, n, n, n)}{\lambda_0^v} = \sum_{q \in \mathbb{F}_2^3} (-1)^{q \cdot e}\, X_{m, q}(v) \ge 0.$$
By spatial $S_3$ cubic symmetry of $n^3$, $X_{m, q}(v)$ depends only on the simultaneous $S_3$-orbit of $(m, q)$ under coordinate permutations of $\{1, 2, 3\}$. Denote the standard basis of $\mathbb{F}_2^3$ by $e_1 = (1,0,0)$, $e_2 = (0,1,0)$, $e_3 = (0,0,1)$, and write $e_{123} = (1,1,1)$. There are exactly **20** $S_3$-orbits of the 64 sectors $(m, q)$:
- **10 aligned orbits** ($m = 0$, $q = 0$, or $q = m$; 22 sectors): $(0,0)$ [1], $(0, e_1)$ [3], $(0, e_1+e_2)$ [3], $(0, e_{123})$ [1], $(e_1, 0)$ [3], $(e_1, e_1)$ [3], $(e_1+e_2, 0)$ [3], $(e_1+e_2, e_1+e_2)$ [3], $(e_{123}, 0)$ [1], $(e_{123}, e_{123})$ [1].
- **10 misaligned orbits** ($m \neq 0$ and $q \notin \{0, m\}$, equivalently $M q \neq 0$; 42 sectors): $(e_1, e_2)$ [6], $(e_1, e_1+e_2)$ [6], $(e_1, e_2+e_3)$ [3], $(e_1, e_{123})$ [3], $(e_1+e_2, e_1)$ [6], $(e_1+e_2, e_3)$ [3], $(e_1+e_2, e_1+e_3)$ [6], $(e_1+e_2, e_{123})$ [3], $(e_{123}, e_1)$ [3], $(e_{123}, e_1+e_2)$ [3].

Three facts from row 1161 (checked row 1162) hold for every even $n \ge 4$ and integer $u \ge 3$:
- **(E-mult)** In every misaligned sector ($M q \neq 0$), every positive eigenvalue of $F_m|_q$ has even real multiplicity (row 1161 L46).
- **(Dom)** $0 \le X_{m, q}(u) \le X_{m, 0}(u) \le X_{0, 0}(u) = 1 + s(u)$ and hence $b_{m, q} \le b_{m, 0} \le 1$ (row 1161 eq. (3)).
- **(N1)** $s(v) \le s(u)^{v/u}$ for every integer $v \ge u$ (row 1184 Lemma N1: if $r_i \in [0, 1]$ and $\sum r_i^u = s$, then $\sum r_i^v \le (\max r_i)^{v - u} s \le s^{(v-u)/u} s = s^{v/u}$).

In **Frame 1** (time = axis $1$, length $n$; spatial box along axes $(0, 2, 3)$ of sides $(v, n, n)$), the static spatial magnetic vector is $c = (c_0, c_1, c_2) := (B_{23}, B_{03}, B_{02}) \in \mathbb{F}_2^3$ (dual to axes $(0, 2, 3)$ in the skew matrix on $(0, 2, 3)$), and the temporal twist vector along axis $1$ is $\alpha = (\alpha_0, \alpha_2, \alpha_3) := (B_{01}, B_{12}, B_{13}) \in \mathbb{F}_2^3$. Reversing the map gives Frame-0 coordinates $m = (c_0, \alpha_3, \alpha_2)$ and $e = (\alpha_0, c_2, c_1)$. For every $(c, q_{\mathrm{new}}) \in \mathbb{F}_2^3 \times \mathbb{F}_2^3$ with $q_{\mathrm{new}} = (q_0, q_2, q_3)$, Fourier inversion in Frame 1 defines the normalized Frame-1 sector trace
$$H_{1, c, q_{\mathrm{new}}}(v) := \frac{1}{8} \sum_{\alpha_0, \alpha_2, \alpha_3 \in \mathbb{F}_2} (-1)^{q_0 \alpha_0 + q_2 \alpha_2 + q_3 \alpha_3}\, I\!\big(v,\, (c_0, \alpha_3, \alpha_2),\, (\alpha_0, c_2, c_1)\big) = \frac{\operatorname{Tr}_{q_{\mathrm{new}}}\!\big(F_{c; (v, n, n)}^n\big)}{\lambda_0(n^3)^v} \ge 0. \tag{1.1}$$
Crucially:
1. $H_{1, c, q_{\mathrm{new}}}(v) \ge 0$ holds for **every** integer $v \ge 3$ and **every** $(c, q_{\mathrm{new}})$.
2. At $v = n$, the Frame-1 spatial box $(v, n, n)$ is the cube $n^3$ itself, so $H_{1, c, q_{\mathrm{new}}}(n) = X_{c, q_{\mathrm{new}}}(n)$; in particular, whenever $q_{\mathrm{new}}$ is **misaligned** with $c$ ($c \neq 0$ and $q_{\mathrm{new}} \notin \{0, c\}$), $H_{1, c, q_{\mathrm{new}}}(n)$ is a misaligned $n^3$-sector trace!

We also define the three excited sums (and their non-neutral parts $S_*^{\neq 0} := S_* - s$) at any time $v \ge 3$:
$$\begin{aligned}
S_\kappa(v; n^3) &:= \frac{W_\kappa(v, n^3)}{\lambda_0^v} - 1 = s(v) + \underbrace{3 X_{e_1, e_1}(v) + 3 X_{e_1+e_2, e_1+e_2}(v) + X_{e_{123}, e_{123}}(v)}_{S_\kappa^{\neq 0}(v)}, \\
S_{\mathrm{per}}(v; n^3) &:= \frac{Z_0(v, n^3)}{\lambda_0^v} - 1 = s(v) + \underbrace{3 X_{0, e_1}(v) + 3 X_{0, e_1+e_2}(v) + X_{0, e_{123}}(v)}_{S_{\mathrm{per}}^{\neq 0}(v)}, \\
S_{\mathrm{full}}(v; n^3) &:= s(v) + \underbrace{3 X_{e_1, 0}(v) + 3 X_{e_1+e_2, 0}(v) + X_{e_{123}, 0}(v)}_{S_{\mathrm{full}}^{\neq 0}(v)}.
\end{aligned}$$

---

### 1.2 Theorem 1 (Exact Frame-1 sector-cancellation identities and universal bounds — `PROVED`)

**Theorem 1 (`PROVED`).** *Let $n \ge 4$ be even, $v \ge 3$ an integer, and $\beta \ge 0$ arbitrary.*

*(a) **(Six exact Frame-1 misaligned-channel identities).** Every Frame-1 channel appearing on the left-hand sides below is misaligned ($c \neq 0$, $q_{\mathrm{new}} \notin \{0, c\}$). Using $S_3$ symmetry of $n^3$, the following identities hold identically:*
$$\begin{aligned}
R_1(v) &:= 2\big(H_{1, (0,0,1), (0,1,0)}(v) + H_{1, (0,0,1), (0,1,1)}(v)\big) \\
       &\phantom{:}= X_{0,0}(v) - X_{0, e_1+e_2}(v) - X_{e_1, 0}(v) - X_{e_1, e_1}(v) + X_{e_1, e_2}(v) + X_{e_1, e_1+e_2}(v) \ge 0, \tag{ID1} \\[4pt]
R_2(v) &:= 2\big(H_{1, (0,1,1), (0,1,0)}(v) + H_{1, (0,1,1), (0,0,1)}(v)\big) \\
       &\phantom{:}= X_{0,0}(v) - 2 X_{0, e_1}(v) + X_{0, e_1+e_2}(v) - X_{e_1+e_2, 0}(v) - X_{e_1+e_2, e_1+e_2}(v) + 2 X_{e_1+e_2, e_1}(v) \ge 0, \tag{ID2-elec} \\[4pt]
M_{2,0}(v) &:= 2\big(H_{1, (1,0,0), (0,1,0)}(v) + H_{1, (1,0,0), (0,1,1)}(v)\big) \\
       &\phantom{:}= X_{e_1, 0}(v) + 2 X_{e_1, e_2}(v) + X_{e_1, e_2+e_3}(v) - X_{e_1+e_2, 0}(v) \\
       &\qquad\quad - X_{e_1+e_2, e_1}(v) - X_{e_1+e_2, e_3}(v) - X_{e_1+e_2, e_1+e_3}(v) \ge 0, \tag{ID2-mag0} \\[4pt]
M_{3,0}(v) &:= 2\big(H_{1, (1,0,0), (0,1,0)}(v) + H_{1, (1,0,0), (0,0,1)}(v)\big) \\
       &\phantom{:}= X_{e_1, 0}(v) + 2 X_{e_1, e_2}(v) + X_{e_1, e_2+e_3}(v) - X_{e_{123}, 0}(v) - 2 X_{e_{123}, e_1}(v) - X_{e_{123}, e_1+e_2}(v) \ge 0, \tag{ID3-mag0} \\[4pt]
M_{2,1}(v) &:= 2\big(H_{1, (1,0,0), (1,1,0)}(v) + H_{1, (1,0,0), (1,1,1)}(v)\big) \\
       &\phantom{:}= X_{e_1, e_1}(v) + 2 X_{e_1, e_1+e_2}(v) + X_{e_1, e_{123}}(v) - X_{e_1+e_2, e_1+e_2}(v) \\
       &\qquad\quad - X_{e_1+e_2, e_1}(v) - X_{e_1+e_2, e_1+e_3}(v) - X_{e_1+e_2, e_{123}}(v) \ge 0, \tag{ID2-mag1} \\[4pt]
M_{3,1}(v) &:= 2\big(H_{1, (1,0,0), (1,1,0)}(v) + H_{1, (1,0,0), (1,0,1)}(v)\big) \\
       &\phantom{:}= X_{e_1, e_1}(v) + 2 X_{e_1, e_1+e_2}(v) + X_{e_1, e_{123}}(v) - X_{e_{123}, e_{123}}(v) - 2 X_{e_{123}, e_1+e_2}(v) - X_{e_{123}, e_1}(v) \ge 0. \tag{ID3-mag1}
\end{aligned}$$
*In particular, dropping the nonpositive misaligned terms in (ID2-mag0) yields*
$$X_{e_1+e_2, 0}(v) \le X_{e_1, 0}(v) + 2 X_{e_1, e_2}(v) + X_{e_1, e_2+e_3}(v). \tag{1.2}$$

*(b) **(Exact $S_4$ misaligned-electric identity and universal magnetic ceiling at $v = n$).** On the symmetric 4-torus $n^4$,*
$$X_{e_1, e_2}(n) + X_{e_1, e_1+e_2}(n) + X_{e_1, e_2+e_3}(n) + X_{e_1, e_{123}}(n) = X_{0, e_1}(n) - X_{0, e_{123}}(n) \ge 0, \tag{1.3}$$
*so $X_{0, e_1}(n) \ge X_{0, e_{123}}(n)$ universally; and*
$$X_{e_1, e_1}(n) \le \frac{2}{3}\big(1 + s(n)\big). \tag{1.4}$$

*Proof.*
**(a)** Expand (1.1) directly using $\sum_{\alpha_0 \in \mathbb{F}_2} (-1)^{q_0 \alpha_0} (-1)^{q_1 \alpha_0} = 2\,\mathbf{1}_{q_1 = q_0}$. For **(ID1)**, take $c = (0,0,1)$, so $m = (0, \alpha_3, \alpha_2)$ and $e = (\alpha_0, 1, 0)$, hence $(-1)^{q \cdot e} = (-1)^{q_1 \alpha_0 + q_2}$. Summing over $q_{\mathrm{new}} \in \{(0,1,0), (0,1,1)\}$ multiplies $(-1)^{\alpha_2}$ by $1 + (-1)^{\alpha_3} = 2\,\mathbf{1}_{\alpha_3 = 0}$ and selects $q_1 = q_0 = 0$. Thus
$$R_1(v) = \frac{1}{2} \sum_{\alpha_2 \in \mathbb{F}_2} (-1)^{\alpha_2} \sum_{q_2, q_3 \in \mathbb{F}_2} (-1)^{q_2} X_{(0, 0, \alpha_2), (0, q_2, q_3)}(v).$$
Evaluating the eight terms gives $(X_{0,0} + X_{0, e_3} - X_{0, e_2} - X_{0, e_2+e_3}) - (X_{e_3, 0} + X_{e_3, e_3} - X_{e_3, e_2} - X_{e_3, e_2+e_3})$. By $S_3$ symmetry, $X_{0, e_3} = X_{0, e_2}$ cancels identically, $X_{0, e_2+e_3} = X_{0, e_1+e_2}$, $X_{e_3, 0} = X_{e_1, 0}$, $X_{e_3, e_3} = X_{e_1, e_1}$, $X_{e_3, e_2} = X_{e_1, e_2}$, and $X_{e_3, e_2+e_3} = X_{e_1, e_1+e_2}$ (via permutation $(13)$). This yields **(ID1)**.

For **(ID2-elec)**, $c = (0,1,1)$ gives $e = (\alpha_0, 1, 1)$ and $(-1)^{q \cdot e} = (-1)^{q_1 \alpha_0 + q_2 + q_3}$. Summing over $q_{\mathrm{new}} \in \{(0,1,0), (0,0,1)\}$ produces $(-1)^{\alpha_2} + (-1)^{\alpha_3} = 2(-1)^{\alpha_2} \mathbf{1}_{\alpha_2 = \alpha_3}$ and selects $q_1 = 0$, leaving $m \in \{(0,0,0), (0,1,1)\}$:
$$R_2(v) = \big(X_{0,0} - X_{0, e_2} - X_{0, e_3} + X_{0, e_2+e_3}\big) - \big(X_{e_2+e_3, 0} - X_{e_2+e_3, e_2} - X_{e_2+e_3, e_3} + X_{e_2+e_3, e_2+e_3}\big).$$
Applying $S_3$ orbit identification gives **(ID2-elec)**.

For **(ID2-mag0)**–**(ID3-mag1)**, $c = (1,0,0)$ gives $m = (1, \alpha_3, \alpha_2)$ and $e = (\alpha_0, 0, 0)$, so $(-1)^{q \cdot e} = (-1)^{q_1 \alpha_0}$. Selecting $q_0 = 0$ fixes $q_1 = 0$, while $q_0 = 1$ fixes $q_1 = 1$. Summing $(q_2, q_3) \in \{(1,0), (1,1)\}$ forces $\alpha_3 = 0$ with sign $(-1)^{\alpha_2}$, contrasting $m = (1,0,0)$ against $m = (1,0,1)$ (giving **(ID2-mag0)** and **(ID2-mag1)**). Summing $(q_2, q_3) \in \{(1,0), (0,1)\}$ forces $\alpha_2 = \alpha_3$ with sign $(-1)^{\alpha_2}$, contrasting $m = (1,0,0)$ against $m = (1,1,1)$ (giving **(ID3-mag0)** and **(ID3-mag1)**). Misalignment of every $(c, q_{\mathrm{new}})$ is immediate by inspection.

**(b)** At $v = n$, $S_4$ symmetry gives $I(n, (e_1, 0)) = I(n, (0, e_1))$ (both rank 2 with one nonzero entry: $B_{23} = 1$ vs $B_{01} = 1$) and $I(n, (e_1, e_2)) = I(n, (0, e_1+e_2))$ (both rank 2 with two entries sharing an axis: $B_{23} = B_{02} = 1$ vs $B_{01} = B_{02} = 1$). Expanding by $S_3$ symmetry:
$$\begin{aligned}
I(n, (e_1, 0)) &= X_{e_1, 0} + X_{e_1, e_1} + 2 X_{e_1, e_2} + 2 X_{e_1, e_1+e_2} + X_{e_1, e_2+e_3} + X_{e_1, e_{123}}, \\
I(n, (e_1, e_2)) &= X_{e_1, 0} + X_{e_1, e_1} - X_{e_1, e_2+e_3} - X_{e_1, e_{123}}, \\
I(n, (0, e_1)) &= X_{0, 0} + X_{0, e_1} - X_{0, e_1+e_2} - X_{0, e_{123}}, \\
I(n, (0, e_1+e_2)) &= X_{0, 0} - X_{0, e_1} - X_{0, e_1+e_2} + X_{0, e_{123}}.
\end{aligned}$$
Subtracting the second from the first and equating to the third minus the fourth gives $2(X_{e_1, e_2} + X_{e_1, e_1+e_2} + X_{e_1, e_2+e_3} + X_{e_1, e_{123}}) = 2(X_{0, e_1} - X_{0, e_{123}})$, which is (1.3). For (1.4), note that $I(n, (0, e_{123})) = X_{0,0} - 3 X_{0, e_1} + 3 X_{0, e_1+e_2} - X_{0, e_{123}} \ge 0$, so
$$3 I(n, (e_1, 0)) = 3 I(n, (0, e_1)) \le 3 I(n, (0, e_1)) + I(n, (0, e_{123})) = 4 X_{0,0}(n) - 4 X_{0, e_{123}}(n) \le 4(1 + s(n)).$$
Since $X_{e_1, e_1}(n) \le X_{e_1, 0}(n)$ by **(Dom)** and all sector traces are nonnegative, $2 X_{e_1, e_1}(n) \le X_{e_1, 0}(n) + X_{e_1, e_1}(n) \le I(n, (e_1, 0)) \le \frac{4}{3}(1 + s(n))$, proving (1.4). $\blacksquare$

---

### 1.3 Lemma 2 (Factor-of-2 sharpened aligned tail bound — `PROVED`)

**Lemma 2 (`PROVED`).** *Let $n \ge 4$ be even, $u \ge 3$ an integer, and suppose $s(u; n^3) \le s_0 < 1$. Put $d := (1 + s_0)/2 \in [1/2, 1)$. Then:*
1. *For every integer $v \ge u$ and every misaligned sector $(m, q)$ ($M q \neq 0$):*
   $$0 \le X_{m, q}(v) \le 2\, d^{v/u}. \tag{1.5}$$
2. *For every integer $v \ge 2u$ (no divisibility $u \mid v$ required) and every sector $(m, q)$:*
   $$0 \le X_{m, q}(v) - b_{m, q}^v \le d^{v/u}. \tag{1.6}$$
3. *For every integer $v \ge u$: $0 \le s(v) \le s_0^{v/u}$.*

*Proof.* Let $1 \ge \mu_0 \ge \mu_1 \ge \dots \ge 0$ be the eigenvalues of $F_m / \lambda_0$ in sector $(m, q)$, and set $y_i := \mu_i^u \in [0, 1]$ and $p := v/u \ge 1$. By **(Dom)**, $\sum_{i \ge 0} y_i = X_{m, q}(u) \le 1 + s_0 = 2 d$.
1. When $M q \neq 0$, **(E-mult)** gives $y_0 = y_1$, so $2 y_0 \le \sum_{i \ge 0} y_i \le 2 d$, hence $y_0 \le d$. Thus $X_{m, q}(v) = \sum_{i \ge 0} y_i^p \le y_0^{p - 1} \sum_{i \ge 0} y_i \le d^{p - 1} (2 d) = 2 d^p$.
2. In any sector, $y_0 + y_1 \le 2 d$ and $y_1 \le y_0$ imply $y_1 \le d$. Write $y_1 = \alpha d$ with $\alpha \in [0, 1]$, and let $S := \sum_{i \ge 1} y_i$. Since $y_0 \ge y_1$, we have $S = \sum_{i \ge 0} y_i - y_0 \le 2 d - y_1 = (2 - \alpha) d$. For $p = v/u \ge 2$:
   $$X_{m, q}(v) - b_{m, q}^v = \sum_{i \ge 1} y_i^p \le y_1^{p - 1} S \le (\alpha d)^{p - 1} (2 - \alpha) d = d^p\, \alpha^{p - 1}(2 - \alpha) \le d^p\, \alpha(2 - \alpha) \le d^p,$$
   since $\alpha \in [0, 1]$ gives $\alpha^{p-1} \le \alpha$ for $p \ge 2$ and $\alpha(2 - \alpha) = 1 - (1 - \alpha)^2 \le 1$.
3. Item 3 is **(N1)** (row 1184 Lemma N1). $\blacksquare$

*(Remark: Row 1161 eq. (4) bounds $X_{m, q}(v) - b_{m, q}^v \le (1 + s_0) d^{v/u - 1} = 2 d^{v/u}$; Lemma 2 sharpens the aligned tail by an exact factor of $2$ for all $v \ge 2u$.)*

---

## 2. Four Exact Optimal Certificates and the Derivative-Free One-Cube Neutral Consumer

### 2.1 Lemma 3 (Four exact optimal LP-dual certificates — `PROVED`)

**Lemma 3 (`PROVED`).** *For every even $n \ge 4$, every integer $v \ge 3$, and every coupling $\beta \ge 0$, the following four exact linear combinations of nonnegative Frame-1 traces $H_{1, c, q_{\mathrm{new}}}(v) \ge 0$ (each with integer weights summing to $32$) yield, after $S_3$ orbit identification:*

1. **Certificate 1 ($S_\kappa^{\neq 0}$ in Alternative I).** *From*
   $$\begin{aligned}
   0 \le &\; 7 H_{1,(0,0,0),(0,0,1)} + 8 H_{1,(0,0,1),(0,1,0)} + 6 H_{1,(0,0,1),(0,1,1)} + 7 H_{1,(0,1,1),(0,0,1)} \\
         &+ H_{1,(1,0,0),(1,0,1)} + H_{1,(1,0,1),(1,0,0)} + H_{1,(1,0,1),(1,1,1)} + H_{1,(1,1,1),(1,0,1)},
   \end{aligned}$$
   *we obtain*
   $$S_\kappa^{\neq 0}(v) \le 7 X_{0, 0}(v) - 3 X_{e_1, 0}(v) - 4 X_{e_1+e_2, 0}(v) + 4 X_{e_1, e_2}(v) + 3 X_{e_1, e_1+e_2}(v). \tag{Cert 1}$$

2. **Certificate 2 ($S_\kappa^{\neq 0}$ in Alternative II).** *From*
   $$\begin{aligned}
   0 \le &\; 6 H_{1,(0,0,1),(0,0,0)} + 7 H_{1,(0,0,1),(0,1,0)} + 7 H_{1,(0,0,1),(0,1,1)} + H_{1,(0,1,1),(0,0,0)} \\
         &+ 7 H_{1,(0,1,1),(0,0,1)} + 2 H_{1,(1,0,1),(1,1,1)} + 2 H_{1,(1,1,1),(1,0,1)},
   \end{aligned}$$
   *we obtain*
   $$S_\kappa^{\neq 0}(v) \le 7 X_{0, 0}(v) - 4 X_{0, e_1}(v) - 3 X_{0, e_1+e_2}(v) + 3 X_{e_1, e_2}(v) + 2 X_{e_1+e_2, e_1}(v) + X_{e_1+e_2, e_{123}}(v) + X_{e_{123}, e_1+e_2}(v). \tag{Cert 2}$$

3. **Certificate 3 ($S_{\mathrm{per}}^{\neq 0}$ in Alternative I).** *From*
   $$\begin{aligned}
   0 \le &\; 7 H_{1,(0,0,1),(0,0,1)} + 7 H_{1,(0,0,1),(0,1,0)} + 6 H_{1,(0,0,1),(0,1,1)} + H_{1,(0,0,1),(1,0,0)} \\
         &+ 2 H_{1,(0,0,1),(1,1,0)} + H_{1,(0,0,1),(1,1,1)} + 8 H_{1,(0,1,1),(0,0,1)},
   \end{aligned}$$
   *we obtain*
   $$S_{\mathrm{per}}^{\neq 0}(v) \le 7 X_{0, 0}(v) - 3 X_{e_1, 0}(v) - 4 X_{e_1+e_2, 0}(v) + 2 X_{e_1, e_1+e_2}(v) + X_{e_1, e_2+e_3}(v) + 4 X_{e_1+e_2, e_1}(v). \tag{Cert 3}$$

4. **Certificate 4 ($S_{\mathrm{full}}^{\neq 0}$ in Alternative II).** *From*
   $$\begin{aligned}
   0 \le &\; 6 H_{1,(0,0,1),(0,0,1)} + 7 H_{1,(0,0,1),(0,1,0)} + 7 H_{1,(0,0,1),(0,1,1)} + 7 H_{1,(0,1,1),(0,0,1)} \\
         &+ H_{1,(0,1,1),(0,1,1)} + 2 H_{1,(1,0,1),(0,1,0)} + 2 H_{1,(1,1,1),(0,0,1)},
   \end{aligned}$$
   *we obtain*
   $$S_{\mathrm{full}}^{\neq 0}(v) \le 7 X_{0, 0}(v) - 4 X_{0, e_1}(v) - 3 X_{0, e_1+e_2}(v) + 3 X_{e_1, e_1+e_2}(v) + 2 X_{e_1+e_2, e_1}(v) + X_{e_1+e_2, e_3}(v) + X_{e_{123}, e_1}(v). \tag{Cert 4}$$

*Notice that in all four certificates, the sum of the misaligned coefficients on the right-hand side is **exactly $7$** (and there are zero negative misaligned terms).*

*Proof.* Each certificate is a finite exact linear identity in the 64 variables $\{X_{m, q}(v)\}$ obtained by substituting (1.1),
$$8 H_{1, c, q_{\mathrm{new}}} = 2\,\mathbf{1}_{q_1 = q_0} \sum_{\alpha_2, \alpha_3 \in \mathbb{F}_2} (-1)^{q_2' \alpha_2 + q_3' \alpha_3} \sum_{q_2, q_3 \in \mathbb{F}_2} (-1)^{q_2 c_2 + q_3 c_1} X_{(c_0, \alpha_3, \alpha_2), (q_0, q_2, q_3)}$$
(writing $q_{\mathrm{new}} = (q_0, q_2', q_3')$), and summing coefficients within each of the 20 $S_3$-orbits. We illustrate the exact cancellation on **(Cert 1)**; the other three follow identically:
- **The $c_0 = 1$ block** ($q_0 = 1$, hence $m_1 = q_1 = 1$): the four unit-weight terms $H_{1,(1,0,0),(1,0,1)} + H_{1,(1,0,1),(1,0,0)} + H_{1,(1,0,1),(1,1,1)} + H_{1,(1,1,1),(1,0,1)}$ have $(c_2, c_1) \in \{(0,0), (1,0), (1,0), (1,1)\}$ and $(q_2', q_3') \in \{(0,1), (0,0), (1,1), (0,1)\}$. Summing the four products $(-1)^{q_2' \alpha_2 + q_3' \alpha_3 + q_2 c_2 + q_3 c_1}$ over all $16$ choices of $(\alpha_2, \alpha_3, q_2, q_3)$ gives $+4$ at $(0,0,0,0)$ (sector $(e_1, e_1)$), $-4$ at $(1,1,1,1)$ (sector $(e_{123}, e_{123})$), and $S_3$-orbit sum $0$ on every other orbit, yielding $+X_{e_1, e_1} - X_{e_{123}, e_{123}}$.
- **The $c_0 = 0$ block** ($q_0 = 0$, hence $m_1 = q_1 = 0$): the four terms $7 H_{1,(0,0,0),(0,0,1)} + 8 H_{1,(0,0,1),(0,1,0)} + 6 H_{1,(0,0,1),(0,1,1)} + 7 H_{1,(0,1,1),(0,0,1)}$ have $(c_2, c_1) \in \{(0,0), (1,0), (1,0), (1,1)\}$ and $(q_2', q_3') \in \{(0,1), (1,0), (1,1), (0,1)\}$. Grouping their $16$ entries by $S_3$-orbits gives exact orbit sums $7$ on $(0,0)$, $-3$ on $(e_1, 0)$, $-4$ on $(e_1, e_1)$, $+4$ on $(e_1, e_2)$, $+3$ on $(e_1, e_1+e_2)$, $-4$ on $(e_1+e_2, 0)$, $-3$ on $(e_1+e_2, e_1+e_2)$, and $0$ on every remaining orbit.
- Adding the two blocks yields $7 X_{0,0} - 3 X_{e_1, 0} - 4 X_{e_1+e_2, 0} - 3 X_{e_1, e_1} - 3 X_{e_1+e_2, e_1+e_2} - X_{e_{123}, e_{123}} + 4 X_{e_1, e_2} + 3 X_{e_1, e_1+e_2} \ge 0$, which is **(Cert 1)**.

All 20 orbit coefficients for all four certificates **(Cert 1)**–**(Cert 4)** were independently verified to exact rational equality over all $64$ sectors. $\blacksquare$

---

### 2.2 Theorem 4 (Derivative-free optimal one-cube neutral consumer — `PROVED`)

**Theorem 4 (`PROVED`).** *Let $n$ satisfy $4 \mid n$, let $u \ge 3$ be an integer, and let $K \ge 4$ be a real number with $n \ge K u$. Suppose that at coupling $\beta \ge 0$,*
$$s(u; n^3) \le s_0 < 1, \qquad d := \frac{1 + s_0}{2} \in \left[\frac{1}{2}, 1\right).$$
*Set $t := d^{n/(2u)} \le d^{K/2}$, $s_{1/2} := s(n/2; n^3) \le s_0^{n/(2u)} \le s_0^{K/2}$, and define recursively*
$$\begin{aligned}
\Delta_1 &:= s_{1/2} + 4 t + 11 t^2, & \tau_1 &:= \frac{\Delta_1}{1 - 2\Delta_1}, \\
\Delta_2 &:= s_{1/2} + \tau_1 + 5 t + 12 t^2, & \tau_2 &:= \frac{\Delta_2}{1 - 2\Delta_2}, & \tau_{2, B} &:= \frac{\Delta_2 / 2}{1 - \Delta_2}, \\
\varepsilon_{A_1} &:= 11 t^2 + 2\tau_1^2, & \varepsilon_{A_2} &:= 12 t^2 + 2\tau_{2, B}^2 + \tau_2^2, \\
\varepsilon_{B_2} &:= 11 t^2 + 2\tau_1^2, & \varepsilon_{B_1} &:= \frac{1}{2}\Big(\varepsilon_{B_2} + 12 t^2 + 2(\tau_1 + 7t)^2\Big).
\end{aligned}$$
*Assume the mild regime conditions*
$$\Delta_2 < \frac{1}{4}, \qquad s_{1/2} + \tau_1 + 5t + 2\tau_2 < 1, \qquad 1 - 12 t^2 > 2\tau_{2, B}^2 + 2\tau_2^2 \tag{2.1}$$
*(which automatically imply $\Delta_1 < \frac{1}{4}$, $s_{1/2} + 4t + 2\tau_1 < 1$, $1 - 11 t^2 > 3\tau_1^2$, and $1 + s_{1/2} + \tau_1 + 5t < 2(1 - \tau_{2, B})$). Then **exactly one of the following two alternatives** holds at $\beta$, and for **every** integer $v \in [n/2, n]$ simultaneously:*

- **Alternative I (electric-confined / magnetic-light phase):**
  $$b_{e_1, 0}^n \ge 1 - \varepsilon_{A_1}, \qquad b_{e_1+e_2, 0}^n \ge 1 - \varepsilon_{A_2},$$
  $$\max\!\big(S_\kappa(v; n^3),\, S_{\mathrm{per}}(v; n^3)\big) \le 8\, s_0^{v/u} + 14\, d^{v/u} + 3\varepsilon_{A_1} + 4\varepsilon_{A_2}. \tag{2.2}$$

- **Alternative II (electric-light / magnetic-heavy phase):**
  $$b_{0, e_1}^n \ge 1 - \varepsilon_{B_1}, \qquad b_{0, e_1+e_2}^n \ge 1 - \varepsilon_{B_2},$$
  $$\max\!\big(S_\kappa(v; n^3),\, S_{\mathrm{full}}(v; n^3)\big) \le 8\, s_0^{v/u} + 14\, d^{v/u} + 4\varepsilon_{B_1} + 3\varepsilon_{B_2}. \tag{2.3}$$
  *Moreover, in Alternative II, the probability of a nonzero spatial-magnetic twist ($m \neq 0$, i.e., any of the 56 twists with $(B_{23}, B_{13}, B_{12}) \neq 0$) in the all-twist mixture on $(v, n^3)$ satisfies*
  $$\mathbb{P}_v(m \neq 0) := \frac{\sum_{m \neq 0,\, e \in \mathbb{F}_2^3} Z_{(m, e)}(v, n^3)}{\sum_{m, e \in \mathbb{F}_2^3} Z_{(m, e)}(v, n^3)} \le S_{\mathrm{full}}^{\neq 0}(v) \le 7\, s_0^{v/u} + 14\, d^{v/u} + 4\varepsilon_{B_1} + 3\varepsilon_{B_2}. \tag{2.4}$$

*In particular, regardless of which alternative occurs, for every integer $v \in [n/2, n]$:*
$$S_\kappa(v; n^3) \le 8\, s_0^{v/u} + 14\, d^{v/u} + \max\!\big(3\varepsilon_{A_1} + 4\varepsilon_{A_2},\; 4\varepsilon_{B_1} + 3\varepsilon_{B_2}\big). \tag{2.5}$$

*Proof.* Since $n \ge K u \ge 4 u$, we have $n/2 \ge 2 u$, so Lemma 2 applies at every integer $v \in [n/2, n]$: aligned tails satisfy $0 \le X_{m, q}(v) - b_{m, q}^v \le d^{v/u}$, misaligned sectors satisfy $0 \le X_{m, q}(v) \le 2 d^{v/u}$, and $s(v) \le s_0^{v/u}$. Write the leading eigenvalues at time $n/2$ as
$$A_1 := b_{e_1, 0}^{n/2}, \quad C_1 := b_{e_1, e_1}^{n/2}, \quad A_2 := b_{e_1+e_2, 0}^{n/2}, \quad C_2 := b_{e_1+e_2, e_1+e_2}^{n/2}, \quad B_1 := b_{0, e_1}^{n/2}, \quad B_2 := b_{0, e_1+e_2}^{n/2},$$
all in $[0, 1]$, with $C_1 \le A_1$ and $C_2 \le A_2$ by **(Dom)**.

**Step 1 (Elementary quadratic dichotomy).** If $x \in [0, 1]$ and $x(1 - x) \le D < 1/4$, then either $x \le \tau(D)$ or $x \ge 1 - \tau(D)$ where $\tau(D) := \frac{D}{1 - 2D}$. Indeed, the smaller root of $x(1 - x) = D$ is
$$\frac{1 - \sqrt{1 - 4D}}{2} = \frac{2D}{1 + \sqrt{1 - 4D}} \le \frac{2D}{1 + (1 - 4D)} = \frac{D}{1 - 2D},$$
using $\sqrt{1 - 4D} \ge 1 - 4D$ on $[0, 1]$.

**Step 2 (First dichotomy from (ID1) at $v = n/2$ and $v = n$).** Evaluating **(ID1)** of Theorem 1 at $v = n/2$ gives $0 \le R_1(n/2) \le (1 + s_{1/2}) - B_2 - A_1 - C_1 + 4 t$, hence
$$B_2 + A_1 + C_1 \le 1 + s_{1/2} + 4 t. \tag{2.6}$$
At $v = n$, Frame 1 has spatial box $n^3$, and both channels $((0,0,1), (0,1,0))$ and $((0,0,1), (0,1,1))$ in $R_1(n)$ are misaligned in Frame 1, so Lemma 2 in Frame 1 gives $R_1(n) \le 2(2t^2 + 2t^2) = 8 t^2$. Meanwhile $X_{0,0}(n) \ge 1$, the misaligned terms are $\ge 0$, and each of the three subtracted aligned traces is bounded above by $b^n + t^2$ by Lemma 2, so
$$1 - (B_2^2 + A_1^2 + C_1^2) - 3 t^2 \le R_1(n) \le 8 t^2 \implies B_2^2 + A_1^2 + C_1^2 \ge 1 - 11 t^2. \tag{2.7}$$
Subtracting (2.7) from (2.6) gives
$$B_2(1 - B_2) + A_1(1 - A_1) + C_1(1 - C_1) \le s_{1/2} + 4 t + 11 t^2 = \Delta_1.$$
Since each summand is nonnegative, Step 1 places every member of $\{B_2, A_1, C_1\}$ in $[0, \tau_1] \cup [1 - \tau_1, 1]$. By (2.1), $1 + s_{1/2} + 4t < 2(1 - \tau_1)$ so at most one member can lie in $[1 - \tau_1, 1]$, and $1 - 11 t^2 > 3\tau_1^2$ so at least one must lie there. Since $C_1 \le A_1$, $C_1$ cannot be the unique large member. Thus either **(Alt I)** $A_1 \ge 1 - \tau_1$ and $B_2, C_1 \le \tau_1$, or **(Alt II)** $B_2 \ge 1 - \tau_1$ and $A_1, C_1 \le \tau_1$. (The two cases are mutually exclusive since $\tau_1 < 1/2$.)

**Step 3 (Quadratic bootstrap in Alternative I).** From (2.7), $A_1^2 \ge 1 - 11 t^2 - B_2^2 - C_1^2 \ge 1 - 11 t^2 - 2\tau_1^2 = 1 - \varepsilon_{A_1}$. Now apply **(ID2-elec)** at $v = n/2$ and $v = n$. At $v = n/2$, $X_{0, e_1+e_2}(n/2) \le B_2 + t \le \tau_1 + t$ and $2 X_{e_1+e_2, e_1}(n/2) \le 4 t$, so $R_2(n/2) \ge 0$ gives
$$2 B_1 + A_2 + C_2 \le 1 + s_{1/2} + \tau_1 + 5 t. \tag{2.8}$$
At $v = n$, both Frame-1 channels in $R_2(n)$ are misaligned, so $R_2(n) \le 8 t^2$. Using $X_{0,0}(n) \ge 1$, $X_{0, e_1+e_2}(n) \ge 0$, $2 X_{e_1+e_2, e_1}(n) \ge 0$, and Lemma 2 on the four subtracted aligned traces gives
$$1 - (2 B_1^2 + A_2^2 + C_2^2) - 4 t^2 \le R_2(n) \le 8 t^2 \implies 2 B_1^2 + A_2^2 + C_2^2 \ge 1 - 12 t^2. \tag{2.9}$$
Subtracting (2.9) from (2.8) gives
$$2 B_1(1 - B_1) + A_2(1 - A_2) + C_2(1 - C_2) \le s_{1/2} + \tau_1 + 5 t + 12 t^2 = \Delta_2.$$
In particular $B_1(1 - B_1) \le \Delta_2 / 2$, so by Step 1 either $B_1 \le \tau_{2, B}$ or $B_1 \ge 1 - \tau_{2, B}$; the latter contradicts (2.8) since $1 + s_{1/2} + \tau_1 + 5t < 2(1 - \tau_2) \le 2(1 - \tau_{2, B})$ by (2.1). Hence $B_1 \le \tau_{2, B}$. Then $A_2^2 + C_2^2 \ge 1 - 12 t^2 - 2\tau_{2, B}^2 > 2\tau_2^2$ by (2.1), while $A_2 + C_2 < 2(1 - \tau_2)$ and $C_2 \le A_2$, forcing $A_2 \ge 1 - \tau_2$ and $C_2 \le \tau_2$. Plugging back into (2.9) gives $A_2^2 \ge 1 - 12 t^2 - 2\tau_{2, B}^2 - \tau_2^2 = 1 - \varepsilon_{A_2}$.

Finally, let $v \in [n/2, n]$ be any integer. Since $b_{m, q} \in [0, 1]$ and $v \le n$, we have $X_{e_1, 0}(v) \ge b_{e_1, 0}^v \ge b_{e_1, 0}^n = A_1^2 \ge 1 - \varepsilon_{A_1}$ and $X_{e_1+e_2, 0}(v) \ge A_2^2 \ge 1 - \varepsilon_{A_2}$. Applying **(Cert 1)** and **(Cert 3)** of Lemma 3 at time $v$, bounding each of the $7$ positive misaligned terms by $2 d^{v/u}$ (Lemma 2), and adding $s(v) \le s_0^{v/u}$ yields (2.2):
$$\max\!\big(S_\kappa(v),\, S_{\mathrm{per}}(v)\big) \le s(v) + 7(1 + s(v)) - 3(1 - \varepsilon_{A_1}) - 4(1 - \varepsilon_{A_2}) + 14 d^{v/u} \le 8 s_0^{v/u} + 14 d^{v/u} + 3\varepsilon_{A_1} + 4\varepsilon_{A_2}.$$

**Step 4 (Quadratic bootstrap in Alternative II).** From (2.7), $B_2^2 \ge 1 - 11 t^2 - A_1^2 - C_1^2 \ge 1 - 11 t^2 - 2\tau_1^2 = 1 - \varepsilon_{B_2}$. From (1.2) of Theorem 1 at $v = n/2$ and Lemma 2:
$$C_2 \le A_2 \le X_{e_1+e_2, 0}(n/2) \le X_{e_1, 0}(n/2) + 2 X_{e_1, e_2}(n/2) + X_{e_1, e_2+e_3}(n/2) \le (A_1 + t) + 6 t \le \tau_1 + 7 t.$$
Substituting $X_{0, e_1+e_2}(n) \ge B_2^2 \ge 1 - \varepsilon_{B_2}$ and $A_2, C_2 \le \tau_1 + 7t$ into $R_2(n) \le 8 t^2$ gives
$$1 + (1 - \varepsilon_{B_2}) - \big(2 B_1^2 + A_2^2 + C_2^2 + 4 t^2\big) \le 8 t^2 \implies 2(1 - B_1^2) \le \varepsilon_{B_2} + 12 t^2 + 2(\tau_1 + 7t)^2 = 2\varepsilon_{B_1},$$
so $b_{0, e_1}^n = B_1^2 \ge 1 - \varepsilon_{B_1}$. For every integer $v \in [n/2, n]$, $X_{0, e_1}(v) \ge 1 - \varepsilon_{B_1}$ and $X_{0, e_1+e_2}(v) \ge 1 - \varepsilon_{B_2}$. Applying **(Cert 2)** and **(Cert 4)** at time $v$ and adding $s(v)$ yields (2.3). For (2.4), Fourier inversion over $e \in \mathbb{F}_2^3$ gives $\sum_{e} I(v, m, e) = 8 X_{m, 0}(v)$, so
$$\mathbb{P}_v(m \neq 0) = \frac{8 \sum_{m \neq 0} X_{m, 0}(v)}{8 \sum_{m} X_{m, 0}(v)} = \frac{S_{\mathrm{full}}^{\neq 0}(v)}{1 + s(v) + S_{\mathrm{full}}^{\neq 0}(v)} \le S_{\mathrm{full}}^{\neq 0}(v),$$
which is bounded by **(Cert 4)** without the extra $s(v)$, giving (2.4). $\blacksquare$

---

### 2.3 Corollary 5 (Explicit aspect ratios $K = 34 / 40 / 44$ for `(M-neutral)` and $K = 60 / 70 / 78$ for `(N-phys)` — `PROVED GIVEN` Proposition B3 & Theorem SH [row 705/707], Theorem S-w [row 731/732])

The crucial structural bonus of Theorem 4 is that **a single $(n/2, n)$ dichotomy simultaneously bounds $S_\kappa(v; n^3)$ at both $v = n/2$ and $v = 3n/4$** (using only $4 \mid n$, the exact same divisibility as row 1161!). Feeding $(t, t') = (n/2, 3n/4)$ into Proposition B3 of `library/gap-seed-shape.md` (§1.3, checked row 707) enlarges $n^3 \to (2n)^3$ directly into Theorem SH's $r = 4$ threshold $1/25$, slashing the required aspect ratio further than any single-time $v = n/2$ test.

**Corollary 5 (`PROVED GIVEN` Proposition B3 & Theorem SH of row 705 [checked row 707], Theorem S-w of row 731 [checked row 732], and the checked continuum chain of rows 1179/1183, 1342/1349, 1353/1355, 1356/1359).** *Let $4 \mid n$, let $u \ge 3$ be an integer, and let $n \ge K u$ (so $n \ge 3K \ge 102$ and $n/4 \ge 25 \ge 3$).*

| Hypothesis | $s_0$ | $d = (1+s_0)/2$ | Route (all require only $4 \mid n$) | Aspect $K$ | Min $n$ ($u \ge 3$) | Certified exact rational bound | Seed threshold beaten |
|---|---|---|---|---:|---:|---|---|
| `(M-neutral)` ($u = 2w$) | $4/21$ | $25/42$ | Two-time Prop. B3 ($t=\tfrac{n}{2}, t'=\tfrac{3n}{4}$) $\to$ Thm. SH ($r=4$) | **$34$** ($w \le n/68$) | $104$ | $S_\kappa(\tfrac{n}{2}; (2n)^3) < 0.0324$ | $< 1/25 = 0.04$ |
| `(M-neutral)` ($u = 2w$) | $4/21$ | $25/42$ | Direct $v = n/2$ $\to$ Thm. SH two-stage ($r=2$) | **$40$** ($w \le n/80$) | $120$ | $S_\kappa(\tfrac{n}{2}; n^3) < 4.49 \times 10^{-4}$ | $< 1/1650 \approx 6.06 \times 10^{-4}$ |
| `(M-neutral)` ($u = 2w$) | $4/21$ | $25/42$ | Direct $v = n/2$ $\to$ Thm. S-w ($r=2$) | **$44$** ($w \le n/88$) | $132$ | $S_\kappa(\tfrac{n}{2}; n^3) < 1.69 \times 10^{-4}$ | $< 1/5041 \approx 1.98 \times 10^{-4}$ |
| `(N-phys)` | $1/2$ | $3/4$ | Two-time Prop. B3 ($t=\tfrac{n}{2}, t'=\tfrac{3n}{4}$) $\to$ Thm. SH ($r=4$) | **$60$** | $180$ | $S_\kappa(\tfrac{n}{2}; (2n)^3) < 0.03998$ | $< 1/25 = 0.04$ |
| `(N-phys)` | $1/2$ | $3/4$ | Two-time Prop. B3 ($t=\tfrac{n}{2}, t'=\tfrac{3n}{4}$) $\to$ Thm. SH ($r=4$) | **$62$** | $188$ | $S_\kappa(\tfrac{n}{2}; (2n)^3) < 0.0276$ | $< 1/25 = 0.04$ |
| `(N-phys)` | $1/2$ | $3/4$ | Direct $v = n/2$ $\to$ Thm. SH two-stage ($r=2$) | **$70$** | $212$ | $S_\kappa(\tfrac{n}{2}; n^3) < 6.04 \times 10^{-4}$ | $< 1/1650 \approx 6.06 \times 10^{-4}$ |
| `(N-phys)` | $1/2$ | $3/4$ | Direct $v = n/2$ $\to$ Thm. S-w ($r=2$) | **$78$** | $236$ | $S_\kappa(\tfrac{n}{2}; n^3) < 1.97 \times 10^{-4}$ | $< 1/5041 \approx 1.98 \times 10^{-4}$ |

*In every row of the table, $s(u; n^3) \le s_0$ implies:*
1. *(Single coupling $\beta$)* Theorem SH / Theorem S-w propagates $S_\kappa$ to all dyadic scales, giving a strictly positive uniform even-sector mass gap $\liminf_{L \to \infty} m_{\mathrm{ev}}(L^3) \ge c_K / n > 0$ (explicitly, in the $r = 4$ rows, $\frac{2}{n} \log\!\big(1 / (22.2\, S_\kappa(n/2; (2n)^3))\big) > 0$), as well as the standard $r = 2$ Pfaffian seed $S_\kappa(2^k n; (2^{k+1} n)^3) < 1/5041$ at $k = 4$.
2. *(Transverse selection for the periodic wall)* In Alternative II, on the symmetric 4-torus $n^4$, $\mathbb{P}_n(m \neq 0)$ is bounded above by $1.67 \times 10^{-5}$ (`(M-neutral)`, $K=34$), $7.55 \times 10^{-7}$ (`(M-neutral)`, $K=40$), $2.36 \times 10^{-5}$ (`(N-phys)`, $K=60$), and $1.37 \times 10^{-6}$ (`(N-phys)`, $K=70$). If $\mathbb{P}_n(m \neq 0)$ strictly exceeds that bound, then Alternative I holds, and $S_{\mathrm{per}}$ satisfies the identical seed bound in place of $S_\kappa$ (yielding the full periodic wall `(W)`).
3. *(Continuum chain, uniform along a trajectory $(a_j, \beta_j)$)* If `(M-neutral)` holds at fixed physical time $w$ on a cube of physical side $L \ge 68 w$ (or `(N-phys)` at physical time $u$ on $L \ge 60 u$) along late cutoffs with $4 \mid (L/a_j)$ and $u_j \ge 3$ (no $n_j \ge 2^{70}$ restriction!), then `(G_ev-phys)` holds and, via rows 1179/1183 and 1342/1349, the matched continuum datum satisfies its mass-gap clause.

*Proof (complete hand-verifiable exact rational arithmetic; zero floating point).*

**Step A (Two-time Proposition B3 reduction to $r = 4$).** The Pfaffian partition function $W_\kappa(n_0, n_1, n_2, n_3) = \frac{1}{8} \sum_B (-1)^{\operatorname{Pf}(B)} Z_B$ is $S_4$-symmetric with positive trace-class transfer operator $T_{\kappa, B} = \bigoplus_m F_{m; B}|_{q=m}$ whose top eigenvalue equals $\lambda_0(B)$ (by **(Dom)**). Applying Proposition B3 (`gap-seed-shape.md` §1.3, checked row 707) to $W_\kappa$ with $B = n^3$, $H = (2n)^3$, $a = n/4 \ge 3$, $p = 2$, $q = 3$ (so $pa = n/2$, $qa = 3n/4 < n$, $\beta_i = \frac{n}{n - 3n/4} = 4$, $\Pi = 64$, $\frac{p}{q}(\Pi - 1) = 42$, $|H|/|B| = 8$) gives
$$g_\kappa\!\left(\frac{n}{2}; (2n)^3\right) \le 8\, g_\kappa\!\left(\frac{n}{2}; n^3\right) + 336\, g_\kappa\!\left(\frac{3n}{4}; n^3\right) \le 8\, S_\kappa\!\left(\frac{n}{2}; n^3\right) + 336\, S_\kappa\!\left(\frac{3n}{4}; n^3\right) =: U, \tag{2.10}$$
using $\log(1 + x) \le x$. For $0 \le U < 2$, $k! \ge 2^{k-1}$ for all $k \ge 1$ gives the exact rational bound
$$S_\kappa\!\left(\frac{n}{2}; (2n)^3\right) = e^{g_\kappa(n/2; (2n)^3)} - 1 \le e^U - 1 = \sum_{k=1}^\infty \frac{U^k}{k!} \le \sum_{k=1}^\infty \frac{U^k}{2^{k-1}} = \frac{U}{1 - U/2}. \tag{2.11}$$
When $\frac{U}{1 - U/2} < \frac{1}{25}$ (equivalently $U < \frac{2}{51}$), $S_\kappa(n/2; (2n)^3) < 1/25$, so $T_{\kappa, (2n)^3}$ has a strictly simple top eigenvalue and Theorem SH line $r = 4$ (`gap-seed-shape.md` §1.5, checked row 707) applies verbatim to $(a_{\mathrm{SH}}, B_{\mathrm{SH}}) = (n/2, (2n)^3)$.

**Step B (Exact rational power chains for $d = 25/42$, $s_0 = 4/21$).** Every inequality below is verified by one integer multiplication:
- $d^2 = \frac{625}{1764} < \frac{50}{141}$ ($625 \times 141 = 88{,}125 < 88{,}200 = 50 \times 1764$);
- $d^4 < \left(\frac{50}{141}\right)^2 = \frac{2500}{19881} < \frac{20}{159}$ ($2500 \times 159 = 397{,}500 < 397{,}620 = 20 \times 19881$);
- $d^8 < \left(\frac{20}{159}\right)^2 = \frac{400}{25281} < \frac{5}{316}$ ($400 \times 316 = 126{,}400 < 126{,}405 = 5 \times 25281$);
- $d^{16} < \left(\frac{5}{316}\right)^2 = \frac{25}{99856} < \frac{251}{10^6}$ ($25 \times 10^6 < 25{,}063{,}856 = 251 \times 99856$);
- $d^{17} = d^{16} \cdot \frac{25}{42} < \frac{251 \times 25}{42 \times 10^6} = \frac{6275}{42 \times 10^6} < \frac{15}{10^5}$ ($6275 < 6300 = 150 \times 42$);
- $d^{20} = d^{16} d^4 < \frac{251 \times 20}{159 \times 10^6} = \frac{5020}{159 \times 10^6} < \frac{32}{10^6}$ ($5020 < 5088 = 32 \times 159$);
- $d^{22} = d^{20} d^2 < \frac{32 \times 50}{141 \times 10^6} = \frac{1600}{141 \times 10^6} < \frac{12}{10^6}$ ($1600 < 1692 = 12 \times 141$);
- $d^{24} = d^{16} d^8 < \frac{251 \times 5}{316 \times 10^6} = \frac{1255}{316 \times 10^6} < \frac{4}{10^6}$ ($1255 < 1264 = 4 \times 316$), and $d^3 = \frac{15625}{74088} < \frac{1}{4}$ ($62{,}500 < 74{,}088$), so $d^{3/2} < \frac{1}{2}$ and $d^{51/2} = d^{24} d^{3/2} < \frac{2}{10^6}$;
- $s_0 = \frac{4}{21} < \frac{1}{5}$ ($20 < 21$), so $s_0^{17} < 5^{-17} < 10^{-11}$, $s_0^{20} < 5^{-20} < 10^{-13}$, $s_0^{22} < 5^{-22} < 10^{-15}$, and $s_0^{51/2} < s_0^{25} < 5^{-25} < 10^{-17}$.

**Step C (Exact rational power chains for $d = 3/4$, $s_0 = 1/2$).**
- $d^5 = \frac{243}{1024}$, $d^{15} = \frac{14{,}348{,}907}{1{,}073{,}741{,}824} < \frac{133{,}635}{10^7}$ ($14{,}348{,}907 \times 10^7 < 143{,}489{,}488{,}699{,}392 = 133{,}635 \times 2^{30}$);
- $d^{30} = (d^{15})^2 < \left(\frac{133{,}635}{10^7}\right)^2 < \frac{1786}{10^7}$ ($133{,}635^2 = 17{,}858{,}313{,}225 < 17{,}860{,}000{,}000$);
- $d^{45} = (d^{15})^3 < \left(\frac{133{,}635}{10^7}\right)^3 < \frac{239}{10^8}$ ($133{,}635^3 < 2.387 \times 10^{15} < 2.39 \times 10^{15}$);
- $d^{31} = d^{30} \cdot \frac{3}{4} < \frac{1786 \times 3}{4 \times 10^7} < \frac{135}{10^6}$ ($5358 < 5400$), and $d^3 = \frac{27}{64} < \frac{4}{9}$ ($243 < 256$) gives $d^{3/2} < \frac{2}{3}$, so $d^{93/2} = d^{45} d^{3/2} < \frac{239 \times 2}{3 \times 10^8} < \frac{16}{10^7}$ ($478 < 480$);
- $d^{35} = d^{30} d^5 < \frac{1786 \times 243}{1024 \times 10^7} < \frac{43}{10^6}$ ($433{,}998 < 440{,}320 = 430 \times 1024$);
- $d^{39} = d^{35} d^4 < \frac{43 \times 81}{256 \times 10^6} < \frac{14}{10^6}$ ($3483 < 3584 = 14 \times 256$);
- $s_0^{30} = 2^{-30} < 10^{-9}$, $s_0^{35} < 10^{-10}$, $s_0^{39} < 10^{-11}$, $s_0^{45} < 10^{-13}$.

**Step D (Exact evaluation of Theorem 4's monotone rational formulas).** Since $\Delta_1, \tau_1, \Delta_2, \tau_2, \tau_{2, B}, \varepsilon_{A_1}, \varepsilon_{A_2}, \varepsilon_{B_1}, \varepsilon_{B_2}$ are strictly increasing rational functions of $(t, s_{1/2})$ on the domain (2.1), substituting the exact rational caps of Steps B–C yields (every line verified in exact rational arithmetic):
- **`(M-neutral)`, $K = 34$** ($t \le 15/10^5$, $s_{1/2} \le 10^{-11}$, $d^{51/2} \le 2/10^6$, $s_0^{51/2} \le 10^{-17}$): $\Delta_1 < 6.01 \times 10^{-4}$, $\tau_1 < 6.02 \times 10^{-4}$, $\Delta_2 < 1.36 \times 10^{-3}$ (regime (2.1) holds with vast margin), $\max(3\varepsilon_{A_1} + 4\varepsilon_{A_2},\, 4\varepsilon_{B_1} + 3\varepsilon_{B_2}) < 1.63 \times 10^{-5}$. Thus $S_\kappa(n/2; n^3) < 2.1163 \times 10^{-3}$, $S_\kappa(3n/4; n^3) < 4.4293 \times 10^{-5}$, $U < 0.031813$, and $\frac{U}{1 - U/2} < 0.032327 < \frac{1}{25}$.
- **`(M-neutral)`, $K = 40$** ($t \le 32/10^6$, $s_{1/2} \le 10^{-13}$): error term $< 7.41 \times 10^{-7}$, so $S_\kappa(n/2; n^3) < 14(32 \times 10^{-6}) + 7.41 \times 10^{-7} + 8 \times 10^{-13} < 4.4875 \times 10^{-4} < \frac{1}{1650}$.
- **`(M-neutral)`, $K = 44$** ($t \le 12/10^6$, $s_{1/2} \le 10^{-15}$): error term $< 1.05 \times 10^{-7}$, so $S_\kappa(n/2; n^3) < 1.6811 \times 10^{-4} < \frac{1}{5041}$.
- **`(N-phys)`, $K = 60$** ($t \le 1786/10^7$, $s_{1/2} \le 10^{-9}$, $d^{45} \le 239/10^8$, $s_0^{45} \le 10^{-13}$): error term $< 2.311 \times 10^{-5}$, $S_\kappa(n/2; n^3) < 2.5236 \times 10^{-3}$, $S_\kappa(3n/4; n^3) < 5.6565 \times 10^{-5}$, $U < 0.039194$, and $\frac{U}{1 - U/2} < 0.039977 < \frac{1}{25}$.
- **`(N-phys)`, $K = 62$** ($t \le 135/10^6$, $s_{1/2} \le 10^{-9}$, $d^{93/2} \le 16/10^7$, $s_0^{93/2} \le 10^{-13}$): $U < 0.027186$ and $\frac{U}{1 - U/2} < 0.027560 < \frac{1}{25}$.
- **`(N-phys)`, $K = 70$** ($t \le 43/10^6$, $s_{1/2} \le 10^{-10}$): error term $< 1.338 \times 10^{-6}$, so $S_\kappa(n/2; n^3) < 6.0334 \times 10^{-4} < \frac{1}{1650}$.
- **`(N-phys)`, $K = 78$** ($t \le 14/10^6$, $s_{1/2} \le 10^{-11}$): error term $< 1.418 \times 10^{-7}$, so $S_\kappa(n/2; n^3) < 1.9615 \times 10^{-4} < \frac{1}{5041}$.

Transverse bounds in Alt II follow by plugging the identical exact rational error caps into (2.4) at $v = n$. $\blacksquare$

### 2.4 Physical box-size comparison (`GUIDE` — not used in any proof)

Following row 1180 (`library/gap-mini-neutral-fable.md` lines 128–132), for a glueball of mass $m = 1/\xi$ in a periodic cube $L^3$ at temperature $K / L$, the one-particle thermal excess is roughly $\log(1 + s) \approx K^3 (x / 2\pi)^{3/2} e^{-x}$ with $x = m L / K$:
- Row 1161 ($K = 512$, $s_0 = 1/2$): $x \approx 21.5$, giving $L / \xi \approx 11{,}000$ ($L\sqrt{\sigma} \approx 2900$ at $m/\sqrt{\sigma} \approx 3.8$), plus the artificial lattice-size requirement $n = L/a \ge 2^{70}$.
- Corollary 5 (`(N-phys)`, $K = 60$, $s_0 = 1/2$): $x \approx 14.4$, giving $L / \xi \approx 864$ ($L\sqrt{\sigma} \approx 227$), a **$12.7\times$ reduction in side** and **$2.6 \times 10^4\times$ reduction in 4-volume $L^4$**, with $n \ge 180$.
- Corollary 5 (`(M-neutral)`, $K = 34$, $s_0 = 4/21$): $x \approx 13.7$, giving $L / \xi \approx 466$ ($L\sqrt{\sigma} \approx 123$), a **$23.6\times$ reduction in side** and **$3.1 \times 10^5\times$ reduction in 4-volume $L^4$**, with $n \ge 104$.

---

## 3. Sharpness of the Constant $14$ and the Aspect $K = 2$ Spectral Obstruction

### 3.1 Proposition 6 (Exact sharpness of the leading constant $14$ — `PROVED`)

**Proposition 6 (`PROVED`).** *Let $t \in [0, 1/2]$ and $\varepsilon := 2t \in [0, 1]$. Both of the following exact sector-trace assignments are realized by finite positive transfer spectra with $s(v) \equiv 0$, even multiplicity in every misaligned sector ($M q \neq 0$), and $0 \le X_{m, q}(v) \le X_{m, 0}(v) \le 1$, and satisfy $H_{1, c, q_{\mathrm{new}}}(v) \ge 0$ and $0 \le I(v, B) \le I(v, 0)$ for **every** $(c, q_{\mathrm{new}})$, **every** $B \in \Lambda^2 \mathbb{F}_2^4$, and **every** real $v \ge n/2$:*

1. **Alt I extremal family:** *Set $X_{m, 0}(v) = 1$ (one eigenvalue $1$) for all $m \in \mathbb{F}_2^3$, and $X_{m, q}(v) = 2 t^{2v/n}$ (two equal eigenvalues $t^{2/n}$) for all $m \in \mathbb{F}_2^3$, $q \neq 0$. At $v = n/2$,*
   $$S_\kappa(n/2) = S_{\mathrm{per}}(n/2) = 7\varepsilon = \mathbf{14\, t}.$$
2. **Alt II extremal family:** *Set $X_{0, q}(v) = 1$ (one eigenvalue $1$) for all $q \in \mathbb{F}_2^3$, and $X_{m, q}(v) = 2 t^{2v/n}$ (two equal eigenvalues $t^{2/n}$) for all $m \neq 0$, $q \in \mathbb{F}_2^3$. At $v = n/2$,*
   $$S_\kappa(n/2) = S_{\mathrm{full}}(n/2) = 7\varepsilon = \mathbf{14\, t}.$$

*Consequently, the leading linear coefficient $14$ in Lemma 3 and Theorem 4 is the exact optimum of the Frame-1 positivity cone in both alternatives.*

*Proof.* Put $\varepsilon_v := 2 t^{2v/n} \in [0, 1]$ for $v \ge n/2$.
1. **Alt I family:** For every $m \in \mathbb{F}_2^3$, $I(v, m, 0) = 1 + 7\varepsilon_v$ and $I(v, m, e) = 1 - \varepsilon_v \ge 0$ for all $e \neq 0$ (since $\sum_{q \neq 0} (-1)^{q \cdot e} = -1$). Because $I(v, m, e)$ is independent of $m = (c_0, \alpha_3, \alpha_2)$, summing over $(\alpha_2, \alpha_3)$ in (1.1) annihilates $H_{1, c, q_{\mathrm{new}}}(v)$ unless $(q_2, q_3) = (0, 0)$. When $(q_2, q_3) = (0, 0)$:
   - if $(c_2, c_1) \neq (0, 0)$, then $e = (\alpha_0, c_2, c_1) \neq 0$ for both $\alpha_0$, giving $H_1 = \frac{1 - \varepsilon_v}{2} \ge 0$ ($q_0 = 0$) and $H_1 = 0$ ($q_0 = 1$);
   - if $(c_2, c_1) = (0, 0)$, then $H_1 = \frac{1}{2}\big((1 + 7\varepsilon_v) + (-1)^{q_0}(1 - \varepsilon_v)\big)$, which equals $1 + 3\varepsilon_v \ge 0$ ($q_0 = 0$) and $4\varepsilon_v \ge 0$ ($q_0 = 1$).
2. **Alt II family:** Here $I(v, 0, 0) = 8$, $I(v, m, 0) = 8\varepsilon_v$ ($m \neq 0$), and $I(v, m, e) = 0$ for all $e \neq 0$. Hence only terms with $\alpha_0 = c_1 = c_2 = 0$ survive in (1.1):
   - if $(c_1, c_2) \neq (0, 0)$, then $H_1 = 0$;
   - if $c = (1, 0, 0)$, then all four $(\alpha_2, \alpha_3)$ have $m \neq 0$, giving $H_1 = 4\varepsilon_v \ge 0$ when $(q_2, q_3) = (0, 0)$ and $0$ otherwise;
   - if $c = (0, 0, 0)$, then $(\alpha_2, \alpha_3) = (0, 0)$ contributes $8$ and the other three contribute $8\varepsilon_v$, giving $H_1 = 1 + 3\varepsilon_v \ge 0$ for $(q_2, q_3) = (0, 0)$ and $H_1 = 1 - \varepsilon_v \ge 0$ for $(q_2, q_3) \neq (0, 0)$.

At $v = n/2$, $\varepsilon_{n/2} = 2t$, so $S_\kappa = S_{\mathrm{per}} = 7(2t) = 14t$ (Alt I) and $S_\kappa = S_{\mathrm{full}} = 7(2t) = 14t$ (Alt II). $\blacksquare$

---

### 3.2 Theorem 7 (Exact all-integer-period spectral obstruction to `(EV-STEP)` at aspect $K = 2$ — `PROVED`)

Can one drop the aspect ratio all the way to $K = 2$ (deducing small $S_\kappa(n/2)$ from $s(n/2)$ alone, i.e., `(EV-STEP)` without a shorter time $u < n/2$) using Frame-1 positivity, $S_4$ symmetry on $n^4$, diamagnetic dominance, and even misaligned multiplicities? **No:** even when $s(k n/2) = 0$ identically for *every* integer $k \ge 1$, the Pfaffian thermal sum $S_\kappa(n/2)$ can still hit its literal algebraic maximum $7$.

**Theorem 7 (`PROVED`).** *Define a 64-sector family of finite positive transfer spectra on $n^3$ (listing eigenvalues raised to the power $n/2$) as follows:*
- *Neutral sector $(0, 0)$:* *$\Lambda_{0, 0} = \{1\}$ (so $X_{0, 0}(k n/2) = 1$ and $s(k n/2) = 0$ for all $k \ge 1$).*
- *The $9$ weight-1 aligned sectors $(0, e_i), (e_i, 0), (e_i, e_i)$ ($i = 1, 2, 3$):*
  $$\Lambda_a := \left\{\frac{6}{13},\; \frac{5}{13},\; \frac{2}{13}\right\}, \qquad a_k := \left(\frac{6}{13}\right)^k + \left(\frac{5}{13}\right)^k + \left(\frac{2}{13}\right)^k.$$
- *All $54$ remaining sectors (all weight-2 and weight-3 sectors, plus all $42$ misaligned sectors):*
  $$\Lambda_b := \left\{\frac{6}{52}\;[\times 2],\; \frac{5}{52}\;[\times 4],\; \frac{2}{52}\;[\times 8],\; \frac{1}{52}\;[\times 4]\right\}, \qquad b_k := 2\!\left(\frac{6}{52}\right)^k + 4\!\left(\frac{5}{52}\right)^k + 8\!\left(\frac{2}{52}\right)^k + 4\!\left(\frac{1}{52}\right)^k.$$

*Then this family satisfies **all** of the following simultaneously:*
1. *Every sector has a finite positive spectrum in $(0, 1]$, and every misaligned sector has strictly **even** multiplicities ($2, 4, 8, 4$).*
2. *$s(k n/2) = 0$ for every integer $k \ge 1$ (zero neutral excited states).*
3. *$0 \le X_{m, q}(k n/2) \le X_{m, 0}(k n/2) \le 1$ and $0 \le I(k n/2, B) \le I(k n/2, 0)$ for every $B \in \Lambda^2 \mathbb{F}_2^4$ and every integer $k \ge 1$.*
4. *All $64$ Frame-1 sector traces satisfy $H_{1, c, q_{\mathrm{new}}}(k n/2) \ge 0$ for **every integer $k \ge 1$**.*
5. *At $k = 2$ ($v = n$), $I(n, B)$ is **exactly $S_4$-invariant** across all $11$ $S_4$-orbits of $\Lambda^2 \mathbb{F}_2^4$.*
6. *Yet at $k = 1$ ($v = n/2$), $S_\kappa(n/2) = 3(1) + 3(1) + 1 = \mathbf{7}$ (and $S_{\mathrm{per}}(n/2) = S_{\mathrm{full}}(n/2) = 7$).*

*Proof.*
**Direct arithmetic at $k = 1, 2$:**
$$a_1 = \frac{6 + 5 + 2}{13} = 1, \qquad a_2 = \frac{36 + 25 + 4}{169} = \frac{65}{169} = \frac{5}{13},$$
$$b_1 = \frac{12 + 20 + 16 + 4}{52} = 1, \qquad b_2 = \frac{72 + 100 + 32 + 4}{2704} = \frac{208}{2704} = \frac{1}{13}.$$

**Comparison $0 < b_k \le a_k \le 1$ for all $k \ge 1$:** For every $k \ge 1$, every base of $\Lambda_b$ is $\le \frac{6}{52} = \frac{3}{26}$ while every base of $\Lambda_a$ is $\ge \frac{2}{13} = \frac{4}{26}$, so
$$b_k \le \left(\frac{3}{26}\right)^{k-1} b_1 = \left(\frac{3}{26}\right)^{k-1} \le \left(\frac{4}{26}\right)^{k-1} a_1 \le a_k \le a_1 = 1.$$
This immediately proves $0 \le X_{m, q}(k n/2) \le X_{m, 0}(k n/2) \le 1$ for all $k \ge 1$.

**Twisted partition functions $I(k, m, e)$ and exact $S_4$ symmetry at $k = 2$:** View each $B \in \Lambda^2 \mathbb{F}_2^4$ as an undirected graph on vertices $\{0, 1, 2, 3\}$ (with an edge $\{\mu, \nu\}$ iff $B_{\mu\nu} = 1$). The $64$ matrices partition into **11** $S_4$-orbits. Direct evaluation of $I(m, e) = \sum_q (-1)^{q \cdot e} X_{m, q}$ for the $(1, a, b)$ assignment across all 11 orbits yields:

| $S_4$-orbit graph type [size] | $\operatorname{Pf}$ | $S_3$-suborbits of $(m, e)$ [count] and formula in $(1, a, b)$ | Value at $k = 2$ ($a = \tfrac{5}{13}, b = \tfrac{1}{13}$) |
|---|---:|---|---:|
| Empty [1] | $0$ | $(0, 0)$ [1]: $1 + 3a + 4b$ | $32/13$ |
| 1 edge [6] | $0$ | $(0, e_1)$ [3]: $1 + a - 2b$;\; $(e_1, 0)$ [3]: $2a + 6b$ | $16/13$ |
| 2-edge path [12] | $0$ | $(0, e_1+e_2)$ [3]: $1 - a$;\; $(e_1, e_2)$ [6]: $2a - 2b$;\; $(e_1+e_2, 0)$ [3]: $8b$ | $8/13$ |
| 3-edge star [4] | $0$ | $(0, e_{123})$ [1]: $1 - 3a + 2b$;\; $(e_1+e_2, e_3)$ [3]: $0$ | $0$ |
| 3-edge triangle [4] | $0$ | $(e_1, e_2+e_3)$ [3]: $2a - 2b$;\; $(e_{123}, 0)$ [1]: $8b$ | $8/13$ |
| 4-cycle [3] & 5 edges [6] | $0$ | $(e_1+e_2, e_1+e_2)$ [3], $(e_1+e_2, e_{123})$ [6] ($m$ wt $\ge 2$, $e \neq 0$): $0$ | $0$ |
| All 4 rank-4 orbits [3, 12, 12, 1] | $1$ | $(e_1, e_1), (e_1, e_1+e_2), (e_1, e_{123})$ ($a - a + 3b - 3b = 0$) and $m$ wt $\ge 2$, $e \neq 0$ ($4b - 4b = 0$): $0$ | $0$ |

Thus exact $S_4$ invariance holds across all 11 orbits at $k = 2$. Moreover, for every integer $k \ge 1$:
- $I(k, (0, e_{123})) = 1 - 3 a_k + 2 b_k$: equals $0$ at $k = 1$ and $k = 2$, and for $k \ge 3$ we have $a_k \le \frac{6}{13} a_2 = \frac{30}{169} < \frac{1}{3}$, so $1 - 3 a_k + 2 b_k > 0$.
- Every other $I(k, B)$ is manifestly $\ge 0$ (since $0 < b_k \le a_k \le 1$) and $\le 1 + 3 a_k + 4 b_k = I(k, 0)$.

**All 64 Frame-1 traces for every integer $k \ge 1$:** Substituting the $(1, a, b)$ values into (1.1) collapses all 64 Frame-1 traces $H_{1, c, q_{\mathrm{new}}}(k n/2)$ to **just five distinct algebraic expressions**:
$$\frac{a_k - b_k}{4}, \qquad \frac{a_k + 15 b_k}{4}, \qquad \frac{1 + 2 a_k - 3 b_k}{4}, \qquad \frac{1 + 6 a_k + 9 b_k}{4}, \qquad \frac{1 - 2 a_k + b_k}{4}.$$
The first four are $\ge 0$ for every real $k \ge 1$ (since $0 < b_k \le a_k \le 1$, and $1 + 2a_k - 3b_k = (1 - b_k) + 2(a_k - b_k) \ge 0$). For the fifth expression, $\frac{1 - 2 a_k + b_k}{4}$:
- at $k = 1$: $\frac{1 - 2 + 1}{4} = 0 \ge 0$;
- for every integer $k \ge 2$ (indeed every real $k \ge 2$): since $a_k \le a_2 = \frac{5}{13} < \frac{1}{2}$, we have $1 - 2 a_k + b_k > 1 - \frac{10}{13} = \frac{3}{13} > 0$.

This establishes properties 1–6 completely. $\blacksquare$

**Structural remark (`PROVED`):** Why does this obstruction vanish once one uses aspect $K > 2$ (or intermediate times $v \in (n/2, n)$)? Observe that the fifth Frame-1 expression $\frac{1 - 2a(r) + b(r)}{4}$ is precisely $\frac{1}{4} R_1(r n/2)$ from **(ID1)**! At $r = 1$ it vanishes, and its derivative at $r = 1^+$ is $\frac{1}{4}(-2 a'(1) + b'(1))$. For any probability spectrum with $b(2) = 1/13$, Jensen's inequality gives $-b'(1) \ge \log 13 \approx 2.565$, whereas for $\Lambda_a$, $-2 a'(1) \approx 2.02 < 2.565$, so $R_1(r n/2)$ turns negative just above $r = 1$. Thus **Theorem 7 shows that integer-period ($v = k n/2$) Frame-1 positivity + $S_4$ symmetry at $n^4$ + diamagnetic dominance + even misaligned multiplicities cannot rule out $S_\kappa(n/2) = 7$ even when $s(k n/2) \equiv 0$**; breaking this obstruction requires either aspect $K > 2$ (as in Theorem 4 and Corollary 5, which need only $K = 34$) or extra dynamical input beyond these symmetries.

---

## 4. Direct Analysis of `(M-neutral)` in the Coupling Band $\beta_0 \le \beta_j \le B_0 \log(L/a_j)$ and Chain Audit

### 4.1 Audit of the checked chain (`PROVED` / `OPEN`)

We audited each link of the chain leading from `(M-neutral)` to the Jaffe–Witten mass gap:
1. **`(M-neutral)` at tolerance $2/5$ $\iff s(2w) \le 4/21$ $\implies$ `(N-phys)` (row 1356 Lemma M1 & Corollary M2, checked row 1359):** Sound. With $P = \lambda_0^{-1} \Omega^{-1} (P_0 T) \Omega$, $\|P^w - \Pi_1\|_{\mathrm{HS}}^2 = s(2w)$ and $\|P^w\|_{\mathrm{HS}}^2 = 1 + s(2w)$, so $\|P^w - \Pi_1\|_{\mathrm{HS}} / \|P^w\|_{\mathrm{HS}} \le \delta \iff s(2w) \le \delta^2 / (1 - \delta^2)$, giving $4/21$ at $\delta = 2/5$.
2. **`(M-neutral)` / `(N-phys)` $\implies$ Pfaffian seed $S_\kappa$ and `(G_ev-phys)` (row 1161/1162, row 705/707, row 731/732):** Sound — and **strictly strengthened by Theorem 4 and Corollary 5 above**, which eliminate $n \ge 2^{70}$ and drop $K$ from $512$ to $34$ (for `(M-neutral)`) or $60$ (for `(N-phys)`).
3. **`(G_ev-phys)` $\implies$ matched continuum gap clause (row 1179/1183, row 1342/1349, second lead note after Theorem ZD-c):** Sound. Neither branch I nor branch II blocks `(G_ev-phys)`, and the even/centre-blind gap carries through the continuum match without requiring the full periodic wall `(W)`.

No step of the chain is disproved.

### 4.2 Role of the coupling band $\beta_0 \le \beta_j \le B_0 \log(L/a_j)$ (`ARGUED` / `GUIDE`)

The first lead note after Theorem ZD-c (`library/gap-phys-seed.md` line 322) specifies $\beta_0 \le \beta_j \le B_0 \log(L/a_j)$ as the domain of validity of the ultraviolet estimates used in rows 1325, 1330, and 1334 (noting that an asymptotic-freedom trajectory satisfies it). It is important to distinguish two quantifiers (`ARGUED` / `GUIDE`):

- **Why `(M-neutral)` cannot hold *uniformly over arbitrary $B_0$* in $\beta_0 \le \beta_j \le B_0 \log(L/a_j)$ (`GUIDE`):** For 4D $SU(2)$ Wilson Yang–Mills, one-loop asymptotic freedom gives $\beta(a) = 4/g^2(a) \sim \frac{11}{3\pi^2} \log(1/(\Lambda a)) \approx 0.3715 \log(1/(\Lambda a))$. If a trajectory grows faster than asymptotic freedom, $\beta_j = B_0 \log(L/a_j)$ with $B_0 > \frac{11}{3\pi^2}$, then the effective physical scale $\Lambda L \sim (L/a_j)^{1 - \frac{3\pi^2}{11} B_0} \to 0$ collapses into Lüscher's small-volume perturbative regime, where the lowest neutral toron/glueball energy scales as $O(g_j^{2/3}/L)$ (or $O(1/L)$), so $e^{-2w E_1} \to 1$ at fixed $w/L \le 1/(2K)$ and $s(2w) \le 4/21$ fails. Thus any proof of `(M-neutral)` on the Wilson trajectory must use **how $\beta_j$ is tied to the physical scale $a_j$** (the renormalization/asymptotic-freedom trajectory), not merely the bare upper envelope $\beta_j \le B_0 \log(L/a_j)$ with arbitrary $B_0$.
- **Why every known direct route to `(M-neutral)` along the Wilson trajectory stops at order-one effective coupling (`ARGUED`):** Even after our $23\times$ reduction of the box side from $L \approx 11{,}000\,\xi$ to $L \approx 466\,\xi$, `(M-neutral)` still asks for a single-cube thermal/spectral contraction of $P_0 T^w$ at physical size $L \gg \xi$, where the effective coupling at scale $L$ is of order one. As already established across rows 1180, 1353, 1356, 1363, and 1364:
  - One-step convexity / Bakry–Émery / Dobrushin / one-link coupling methods die at bare coupling $\beta \sim O(1)$ (above $\beta = \pi^2/4$ for Bakry–Émery, row 1180 Lemma R7; above $\beta \sim 1$–$2$ for local convexity/Dobrushin, row 1356 §7.6).
  - Operator-order / minorization / jump-form comparisons fail for discrete-time Wilson transfers because removing boundary terms shifts $\lambda_0$ extensively (row 1180 Lemma R4) and minorization controls only the spectral gap $\mu_1$, not the excited trace $s(2w) = \sum_{j \ge 1} \mu_j^{2w}$ (row 1356 Lemma JF).
  - Any proof must therefore separate 4D $SU(2)$ Wilson from 4D compact $U(1)$ (gapless photon), 5D $SU(2)$ (deconfined weak coupling), first-order coexistence weights $w_p$, and decoupled neutral spectators — and supply either a vacuum regularity / gluing contraction (`(REG-vac)`, row 1356), a uniform Casimir/gap crossing (`(Z-SEED)` / `(Z-UNB)` + `(BDD-Delta)`, row 720), or a renormalization-group carry across effective coupling $g_{\mathrm{eff}} \sim 1$ (`(EXIT)`).

---

## 5. Summary Table, Open Obligations, and Verification Record

| Statement | Label | Depends on |
|---|---|---|
| **Theorem 1:** Six exact Frame-1 misaligned identities (ID1)–(ID3-mag1); exact $S_4$ misaligned-electric identity (1.3); universal magnetic ceiling $X_{e_1,e_1}(n) \le \frac{2}{3}(1+s(n))$ (1.4) | `PROVED` | `(TM-tw)`, $S_3$/$S_4$ symmetry, `(Dom)` (row 1161/1162) |
| **Lemma 2:** Factor-of-2 sharpened aligned tail bound $X_{m,q}(v) - b_{m,q}^v \le d^{v/u}$ for all integers $v \ge 2u$ | `PROVED` | `(E-mult)`, `(Dom)`, `(N1)` (rows 1161/1162, 1184) |
| **Lemma 3:** Four exact optimal LP-dual integer certificates (Cert 1–4), misaligned weight sum $= 7$ | `PROVED` | Frame-1 positivity (1.1), $S_3$ symmetry |
| **Theorem 4:** Derivative-free optimal one-cube neutral consumer (eliminates $n \ge 2^{70}$; exact linear $14 d^{v/u} + O(d^K)$ simultaneously for all $v \in [n/2, n]$; Alt I/II dichotomy & transverse bound) | `PROVED` | Theorem 1, Lemma 2, Lemma 3 |
| **Corollary 5:** Explicit hand-verified aspect ratios $K = 34, 40, 44$ for `(M-neutral)` and $K = 60, 62, 70, 78$ for `(N-phys)` (all $4 \mid n$, $u \ge 3$, $n \ge K u$) | `PROVED GIVEN` | Theorem 4; Prop. B3 & Thm. SH (row 705/707); Thm. S-w (row 731/732); continuum chain (rows 1179/1183, 1342/1349, 1353/1355, 1356/1359) |
| **Proposition 6:** Exact sharpness of the leading constant $14$ in both Alt I and Alt II (all $v \ge n/2$) | `PROVED` | Elementary algebra |
| **Theorem 7:** Exact all-integer-period ($v = k n/2, k \ge 1$) rational-eigenvalue obstruction to `(EV-STEP)` at $K = 2$ ($s \equiv 0$, $S_\kappa(n/2) = 7$, exact $S_4$ at $k = 2$, even misaligned mult.) | `PROVED` | Elementary algebra |
| Physical box reduction $L \approx 11{,}000\,\xi \to 466\,\xi$ ($> 3 \times 10^5\times$ 4-volume drop) | `GUIDE` | One-particle estimate of row 1180 |
| `(M-neutral)` / `(N-phys)` on the 4D $SU(2)$ Wilson trajectory; `(REG-vac)`; `(Z-UNB)`; `(EXIT)`; Jaffe–Witten mass gap | `OPEN` | Order-one effective coupling wall |

**Optional Lean formalization (`OPEN`, not required for the hand proofs above):** Every identity in Theorem 1, Lemma 3, Proposition 6, Theorem 7, and every rational inequality in Corollary 5 is a finite exact identity/inequality over $\mathbb{Q}$ (at most $64$ terms or $30$-digit integers), directly verifiable in Lean 4 by `norm_num` / `decide` in under 1 second of kernel time.

RESULT: Row 1368 (google/gemini-4-neon-xhigh/agy laptop; author only, unchecked, strictly independent of row 1367; 2026-11-21). NOT solved: (M-neutral), (N-phys), and the Jaffe-Witten mass gap remain OPEN, and no step of the checked chain (rows 1356/1359, 1353/1355, 1161/1162, 705/707, 731/732, 1179/1183, 1342/1349) is disproved. PROVED (by hand with exact rational arithmetic, unchecked): Theorem 1 (six exact Frame-1 misaligned sector-cancellation identities (ID1)-(ID3-mag1), exact S_4 misaligned-electric identity sum_{q mis at e_1} X_{e_1,q}(n) = X_{0,e_1}(n) - X_{0,e_{123}}(n) >= 0, and universal magnetic ceiling X_{e_1,e_1}(n) <= (2/3)(1+s(n)) at all couplings and even n >= 4); Lemma 2 (factor-of-2 sharpened aligned tail bound X_{m,q}(v) - b_{m,q}^v <= d^{v/u} for all integers v >= 2u); Lemma 3 (four exact optimal LP-dual integer certificates Cert 1-4 with misaligned weight sum 7); Theorem 4 (derivative-free optimal one-cube neutral consumer completely eliminating row 1161's n >= 2^{70} floor and improving its O(sqrt(h)) bound to the exact optimal linear rate 14 d^{v/u} + O(d^K) simultaneously for every integer v in [n/2, n], with Alt I/II dichotomy and Alt II transverse bound); Corollary 5 (PROVED GIVEN Prop. B3 & Thm. SH [row 705/707] and Thm. S-w [row 731/732]: slashes required aspect ratio from K = 512 to K = 34 [w <= n/68, n >= 104] for (M-neutral) and K = 60 [u <= n/60, n >= 180] for (N-phys) via two-time Prop. B3 at (n/2, 3n/4) -> Thm. SH r = 4, or directly at v = n/2 to K = 40/44 for (M-neutral) and K = 70/78 for (N-phys) for 1/1650 and 1/5041, all requiring only 4 | n and u >= 3); Proposition 6 (exact sharpness of the leading constant 14 in both Alt I and Alt II); Theorem 7 (exact closed-form rational-eigenvalue all-integer-period obstruction to (EV-STEP) at aspect K = 2 with s(k n/2) = 0, even misaligned multiplicities, all 64 Frame-1 traces >= 0 for every integer k >= 1, exact S_4 symmetry at k = 2, and S_kappa(n/2) = 7). GUIDE: reduces the required neutral seed cube side from about 11,000 xi (K = 512) to about 466 xi (K = 34, > 3 x 10^5-fold 4-volume reduction), and explains why (M-neutral) cannot hold uniformly over arbitrary B_0 > 11/(3 pi^2) in beta_0 <= beta_j <= B_0 log(L/a_j). OPEN: (M-neutral), (N-phys), (REG-vac), (Z-UNB), (EXIT), and the Jaffe-Witten mass gap. Output library/gap-agy-seed-neon.md.
