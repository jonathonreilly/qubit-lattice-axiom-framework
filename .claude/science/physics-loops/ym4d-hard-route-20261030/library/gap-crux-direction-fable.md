lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T00:49Z

# Crux direction pass (queue row 1460, `gap-crux-direction-fable`)

Research-stage working state. It grants no status; nothing here is a public claim. Unchecked when written.
Pinned at commit c36a03a16 of `claude/ym4d-hard-route`. Twin: row 1461 (Astra), not read.

Credit: T. Balaban (CMP 95-122, the renormalization group for lattice gauge fields); Ethan Sussman and Levent
Alpoge with Claude and Codex (the YM4 outline, the complete account, and the YM4 Lean release 3932084a9b82, which
proves the subsequential 4D SU(2) Wilson continuum limit this row's target sits on).

## 0. Plan and status log

Plan (written first, per the save protocol):

1. Read the rule sections of FINISH.md (lines 1-84, 299-360) and the row. Done at the first log line below.
2. Phase 1: from the target and published work only (lane rows up to 1142 allowed, none after): what any proof
   of a cutoff-uniform gap at a fixed physical scale must supply that no published method supplies; pick the attack.
3. Phase 2: read the RESULT parts of the solve rows (1143-1343) and mechanism rows (1380-1439), direction rows
   1442-1447, closing rows 1434, 1438, 1439; name the common wall; say whether the Phase 1 attack meets it.
4. Phase 3: first lemma of the attack; prove, refute or reduce.
5. Next two rows with decisive outcomes; RESULT line.

Every step below is marked PROVED (argument written here), SKETCHED, or GUESSED.

Status log (times from `date -u` in the same command):

- 2026-11-24T12:49Z file created, row and GOAL.md read.
- 2026-11-24T13:06Z Phase 1 written (Section 1), before reading any lane row after 1142.

## 1. Phase 1: from the target and published work only

Written before any lane row after 1142 was read. The only post-1142 text read is the row itself and the target
statement (M-neutral-all), `library/sa-ym4-lean-trajectory-check-astra62.md` L101-107.

### 1.1 The target in three equal forms

Notation: $T$ is the Wilson transfer operator on the $n^3$ slice at $\beta$, $P_0$ the neutral projection,
$\lambda_0>\lambda_1\ge\dots$ the eigenvalues of $P_0T$, $E_i=-\log\lambda_i$. Take $\phi$ the vacuum and $c=\lambda_0^w$.

- **(F1) Trace form. PROVED (one line).** $\|c^{-1}P_0T^w-|\phi\rangle\langle\phi|\|_{HS}^2=\sum_{i\ge1}(\lambda_i/\lambda_0)^{2w}=:R(\beta;w,n)$.
  So the target is $R(\beta_K;w_K,n_K)\le 4/25$ with $2w_K\le n_K/512$.
- **(F2) Thermal form. PROVED given (F1).** $1+R=\operatorname{Tr}(P_0T^{2w})/\lambda_0^{2w}$ is the neutral partition
  function of the torus $2w\times n^3$ over the vacuum term. The target says: at temperature $512/\ell$ (physical
  units) in the volume $\ell^3$, the thermal excess of the neutral sector is below $\log(29/25)$. For a gas of
  particles of mass $m$ this needs about $512^3 e^{-m\ell/512}\lesssim 0.15$, so $m\ell\gtrsim 1.1\cdot10^4$. For free
  gluons the excess per volume is of Stefan-Boltzmann size, about $10^9$ times too large. SKETCHED (the sizes).
- **(F3) Rate form. SKETCHED.** The conclusion is a gap $\ge 7.9/\ell$ in physical units, so
  $\xi(\beta_K)\le n_K/7.9$ in lattice units for all late $K$: an upper bound on the correlation length along the
  trajectory with the asymptotic-freedom exponent. The Lean trajectory bound $\beta_K\le B_0\log n_K$,
  $B_0>11/(3\pi^2)$, is the matching statement from the ultraviolet side.

### 1.2 What any proof must supply

**(S1) Ultraviolet carry.** Uniformly in $K$, the theory at a fixed physical scale $l_0$ is a lattice theory with
a small effective coupling $\varepsilon_0$. Published supply: Balaban's series; the Sussman-Alpoge account and
Lean release. This part has a small parameter at every step.

**(S2) Infrared carry.** From a seed on one box to every larger box and to the gap. Published supply:
reflection positivity and chessboard estimates (Froehlich-Simon-Spencer; Froehlich-Israel-Lieb-Simon), finite-size
criteria of Dobrushin-Shlosman type. The lane's Theorem S is of this kind. It is blind to the gauge group.

**(S3) The band. This is what no published method supplies.** Between the scale $l_0$ where the effective
coupling is $\varepsilon_0$ and the scale $\ell$ where a seed can hold, the renormalised coupling runs over a
compact interval $[u_0,u_1]$ of order-one values. On it neither the weak-coupling expansion nor the
strong-coupling expansion converges. Any proof contains a proof of:

> **(NS) No stalling.** Along the flow from $l_0$ to $\ell$ the disorder (any coupling that the seed reads)
> increases by a definite amount at each doubling. There is no fixed point and no phase transition in the band.

Why (NS) cannot be had from structure alone (SKETCHED, by tests; not a theorem): each structural property a
proof could use is shared by a model whose band stalls.

| Property | Model that has it and stalls |
|---|---|
| reflection positivity, gauge invariance, compact group | U(1) in 4D at weak coupling (Guth; Froehlich-Spencer: massless) |
| the same, non-abelian group, local action | SU(2) in 5D (no asymptotic freedom); mixed fundamental-adjoint SU(2) at its critical endpoint (Bhanot-Creutz; numerical, the lane's K7) |
| asymptotic freedom at short scales, reflection positivity of the gauge marginal | SU(2) with enough massless matter (Banks-Zaks window; the gauge marginal is non-local) |
| exact inequalities blind to the group (chessboard, convexity in $\beta$, sub-additivity) | all of the above |

So (NS) needs **quantitative** information on pure local SU(2) at every coupling of the band. There are three
sources and no more: (a) an exact inequality that is true for SU(2) and false for U(1) at order-one coupling;
(b) an exact identity (Schwinger-Dyson, loop equation, Ward identity) with a sign; (c) a computation with
proved error bounds. GUESSED: the list is complete (I see no fourth source).

**Where SU(2) and U(1) differ exactly, not perturbatively** (the places where (a) or (b) can come from):

1. Fusion: $\chi_1\chi_1\ni\chi_1$. Electric flux is conserved only modulo the centre. U(1) has a continuous
   one-form symmetry and the photon is its Goldstone mode; SU(2) has only $\mathbb Z_2$. A proof cannot use the
   *absence* of a symmetry directly.
2. Volume: the class-angle density $\sin^2\theta$, the positive curvature of the group and of the orbit space
   (Singer; O'Neill). In 2+1 dimensions Karabali-Kim-Nair locate the gap in the volume measure of the orbit
   space. In the 2D O(N) model the curvature of the sphere drives the flow.
3. Bianchi: the cube constraint on plaquette holonomies is non-abelian, so no dual formulation exists.

**Published non-perturbative methods and where each stops** (all unchecked here, from memory of the sources):

| Method | Source | Stops at |
|---|---|---|
| cluster expansion | Osterwalder-Seiler 1978 | $\beta\ll1$ |
| Bakry-Emery / Langevin | Shen-Zhu-Zhu 2023; Cao-Nissim-Sheffield 2025 | $\beta\lesssim$ const (curvature of the group beats the Hessian) |
| decimation bounds | Tomboulis 0707.2179; Ito-Seiler 0711.4930, 0803.3019 | one unproved inequality on the twisted ratio (T (5.22)); the flow is blind to the group |
| slice comparison | Durhuus-Froehlich 1980 | needs decay of a 3D O(4) model, false at weak coupling |
| centre-vortex bounds | Mack-Petkova 1979; Tomboulis-Yaffe 1985 | give confinement from a vortex free energy, not the free energy itself |
| 2D O(N), every $\beta$ | OpenAI 2026-10; Ding-Huang-Yang 2611.04908 | uses a continuous non-abelian global symmetry (lane rows 1011, 1016: no gauge analogue found) |
| loop-equation bootstrap | Anderson-Kruczenski 2017; Kazakov-Zheng 2022, 2024 | rigorous bounds on short loops at any $\beta$; says nothing on a spectral gap or on $\beta_K\to\infty$ |
| thin twisted tori, semiclassics | Gonzalez-Arroyo et al.; Tanizaki-Unsal 2022 | weak coupling and a gap, but only while two sides stay small; continuity in the side is (NS) again |
| small volume | Luescher 1983; Koller-van Baal 1988 | accurate to $m\ell\approx5$, not rigorous, a seed needs $m\ell\gg5$ |

### 1.3 Two reductions that hold on the way

**(Q) The band problem is qualitative. SKETCHED.** A seed is an open condition on the action (finitely many
box integrals, strict inequality). If the effective actions at scale $l_0$ converge along the sequence, the
target follows from: the *one* limit lattice theory at coupling $\varepsilon_0$ has a positive gap, of any size.
No rate in $\varepsilon_0$ is needed. Rates matter only for a proof by computation.

**(HF) Differential form at a fixed lattice. PROVED below for the Hamiltonian form.** Let
$H=\lambda K+V/\lambda$ on gauge-invariant $L^2$ of the spatial links, $\lambda=g^2$, $K=-\tfrac12\Delta$,
$V\ge0$ the magnetic term. Let $\Omega=e^{-\varphi}$ be the ground state, $\mu=\Omega^2$, and $f\Omega$ a
normalised excited eigenvector with gap $\Delta E=\tfrac\lambda2\mathbb E_\mu|\nabla f|^2$. Hellmann-Feynman
gives $\lambda^2\partial_\lambda\Delta E=\lambda^2\Delta K-\Delta V$ with $\Delta V=\operatorname{Cov}_\mu(f^2,V)$
and $\lambda\Delta K=\Delta E-\Delta V/\lambda$. Hence, for a constant $\kappa>\lambda$,

$$
\frac{d\log\Delta E}{d(1/\lambda)}\ge-\kappa
\iff -\operatorname{Cov}_\mu(f^2,V)\le\frac{\kappa-\lambda}{2}\,\Delta E=\frac{\lambda(\kappa-\lambda)}4\,\mathbb E_\mu|\nabla f|^2 .\qquad\text{(VIR-H)}
$$

In words: an excitation lowers the magnetic term by at most $\kappa/2$ times its energy. A harmonic system has
$\operatorname{Cov}_\mu(f^2,V)=+\lambda\Delta E/2$, so U(1) at weak coupling passes with room; exact
asymptotic-freedom scaling is equality with $\kappa=24\pi^2/11$. (VIR-H) for all $\lambda$ and all sizes, with one
$\kappa$, is "no transition and at most exponential growth of $\xi$". I expect this to be the lane's (VIR_K)
(row 708) in other words; to be checked in Phase 2.

### 1.4 The attack I would name, before reading the record

Ranking by "how many unproved ideas are missing" and "can the first lemma be decided":

1. **Computation across the band** has no missing idea but no feasible form: a direct seed at $\beta\approx2.3$
   already needs an integral over about $10^8$ links, and the band's lower end is set by the constants of the
   ultraviolet construction, which are not of order one. Only small exact computations are feasible (a few links,
   character coefficients, a finite-dimensional recursion).
2. So the only feasible architecture with computation is: **a local inequality, exact transport, a
   finite-dimensional certified recursion.** This is Tomboulis's architecture. Its missing inequality must be
   non-abelian (it must fail for U(1)), so it must come from source 1, 2 or 3 above.
3. Of the three sources only **source 2 (volume, curvature) has a sign**. My Phase 1 attack is therefore:

> **Attack ORB.** Work in the transfer-operator (or Hamiltonian) picture on the slice, where the neutral gap is
> the Poincare constant of the time-zero law $\mu$ on the orbit space. Use the orbit-space volume as the
> non-abelian input to prove the one-scale inequality (VIR-H) with a $\kappa$ independent of the size, and
> integrate it in $1/\lambda$ from a strong-coupling seed.
> First lemma: (VIR-H) for the lowest neutral excitation at one size, or a decisive obstruction to it.

Honest prior: I expect Phase 2 to show that (VIR-H) is on file and that ORB meets the lane's wall.
