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
- 2026-11-24T13:14Z Phase 2 written (Section 2): the wall named; Phase 1 attack ORB is the lane's (VIR_K), not progress. Phase 3 turns to the Lean flow.
- 2026-11-24T13:25Z Phase 3 written (Section 3): attack LD on the Lean block map; Lemma LD-1, Lemma SE, Theorem LOSS proved by hand; LD reduces to K-I. Section 4: next two rows. Re-read of the PROVED items is next.
- 2026-11-24T13:27Z Re-read of every PROVED item done (LD-1, LD-2, SE (a)-(d), LOSS, RANGE re-derived line by line; `axisPath` checked in the release; one number corrected: epsilon at most 2.53e-6). RESULT line written. Finished.

## 1. Phase 1: from the target and published work only

Written before any lane row after 1142 was read. The only post-1142 text read is the row itself and the target
statement (M-neutral-all), `library/sa-ym4-lean-trajectory-check-astra62.md` L96-112 (the statement and the lines
around it). Limit of the blindness: my navigation notes from earlier rows of this lane were in context from the
start. They name Theorem T (row 1332), (N-phys), the filter of row 1386 and the verdict of row 1442 in one line
each. So Phase 1 is independent of the row files and RESULT lines after 1142, not of those one-line pointers.

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

## 2. Phase 2: the record, the common wall, and my Phase 1 attack against it

Read: `parts/gap.md` L4-104 (state of attack); the RESULT parts of rows 1143, 1161, 1177, 1283, 1315, 1323, 1326,
1330-1332, 1335, 1339, 1340, 1342, 1356, 1363, 1377, 1380, 1381, 1383, 1385-1389, 1402, 1418, 1421, 1425, 1430,
1434, 1436, 1438-1443, 1445, 1449, 1451, 1454, 1456, 1457; `gap-mech-direction2-fable.md` 4.4. Not read: the other
solve rows and the row files (RESULT lines only), so the statements below about "all solve rows" rest on this
sample of about 45 rows and on the lane's own digests.

### 2.1 The common wall

In the lane's words (`parts/gap.md` L31-33, L43-45): "on each doubling of the box, between the last small box and
the first good box, a certain free energy shrinks by a fixed factor"; "every engine found is blind, so its seed
sits in the band; the one selective fact that is provable today, asymptotic freedom at small coupling, has no
engine that carries it across the band".

In the sample, every solve row follows one pattern: an exact rewriting of the neutral thermal trace (a comparison
integral, a cut, a noise factor, a cover, a pin, a predictor), a proof that the rewriting is exact or loses
$o(1)$, and then a stop at a comparison that needs order-one accuracy at a physical size (rows 1323 (30), 1330
(30), 1339, 1377: "the whole-face term at physical time"). The mechanism rows 1380-1439 each closed a class by
showing that it holds for U(1), for 5D, or for Villain U(1), or that it is an exact re-encoding with zero gain
(row 1438 (12)). Row 1386 names the missing input: **K-I** (an exact carry with a sign for a typical-field
stiffness), **K-II** (a renormalization step at order-one effective coupling), **K-III** (a verified computation,
priced out by rows 1326 and 1418).

This is statement (NS) of 1.2. My Phase 1 analysis found nothing that the lane does not have:

| Phase 1 item | Already on file |
|---|---|
| (F2) thermal reading | row 1402 Phase 1; row 1363 ("energy density at least three times the pressure") |
| (S3)/(NS), the three sources | (K-one)/(K-flow), `parts/gap.md` L46-49; K-I, K-II, K-III, `gap-mech-direction2-fable.md` L339-348 |
| table of stalled models | U(1), frozen groups, K7, products: `parts/gap.md` L27-29; five dimensions and the N-test: `gap-assume-opus.md` L145; a published-theorem version of K7: Proposition V with van Enter-Shlosman, `gap-crux-fp.md` L264, L287 |
| (Q) qualitative band | Theorem T, `gap-shrink-box-fable.md` (row 1332, check 1335); (SEED-L) with ONE-K |
| (VIR-H) | (VIR_K), Theorem TR, (VIR-log), `gap-mid-max.md` L52-58, L120, L172 (row 708); idea 46 / G8 (NOCRIT-HF), `gap-brainstorm-max.md` L334, L484, L619 ("no tool") |
| attack ORB | method 31 of `parts/gap.md` (rows 957, 968); `gap-mini-solve-d-fable.md` L83 ("no consumer above beta about 1/8") |
| local inequality + exact transport + certified recursion | row 1025 (Tomboulis), rows 1418-1432 (signed tensor steps), row 1326 |

**Verdict on Phase 1.** Attack ORB with first lemma (VIR-H) is the lane's (VIR_K) in Hamiltonian words. It is
equivalent to a closed line and is not progress. One sharpening is worth keeping, because it sorts the record:

**Remark PATH (ARGUED, from on-file tests).** Attacks split by the path along which they carry a seed.
- *Coupling paths* (transport in the bare $\beta$ at a fixed lattice: (VIR_K), (NOCRIT), (A2) of Theorem T,
  Tomboulis, continuity methods). The conclusion of such a carry is false at a coexistence point. Proposition V
  (a theorem, given van Enter-Shlosman) and the N-test (a belief: Wilson SU(N), N at least 5) show that
  coexistence occurs for weights with every structural property of the Wilson SU(2) weight. So a coupling-path
  proof must read the Wilson SU(2) weight through a number. No structural proof exists.
- *Scale paths* (transport in the scale at a late cutoff, from first-passage data: K-I, K-II). No model with the
  same local structure is known to stall, because all such weights have one continuum limit. The only tests are
  changes of group, dimension or content. This is the only kind where a structural proof is not excluded.

The Lean release works on a scale path with an exact block map. No attack row has used its flow objects: rows
1449-1458 are port readings, and the mechanism rows 1380-1439 predate them. Row 1383 left open "an exact
statement for an averaging map at finite coupling" and check 1385 recorded that the level form "is a candidate
statistic only". The Lean flow is such a map with a statement. Phase 3 takes this as the attack.

## 3. Phase 3: attack LD (carry the band on the Lean release's own block map)

**Attack LD.** The Lean release blocks the Wilson density exactly, by a soft kernel, and controls the result
above a floor. Continue that exact flow below the floor to a strong-coupling end class (the consumer is
Proposition CH of row 1332). **First lemma (LD-loc):** below the floor the block step still returns a local
density whose local stiffness is comparable to its readout.

Not on file: `kernelImage` and `contourMean` occur only in the port readings (rows 1451, 1454, 1456); no attack
row uses them (grep of `library/`, `library/prior/`; row 1456 L21 records the same search of FINISH.md and
`open-core.md`). Thin-line self-energy as a fact is on file (Simon-Yaffe one-link randomization, rows 1132-1138;
`gap-mini-dualstep2-fable.md` L421); its use on the Lean kernel is not.

Source read (read only, release 3932084a9b82): `YangMills/Construction/ClusterExpansionOfAStep/LumpsOnATorus.lean`
L52-79 (`partitionFn`, `bondKernel`, `averagedKernel`, `kernelImage`);
`HoleBesideASecondHole/CutsLumpsBasesAndContours.lean` L76-104 (`IsBaseChoice`, `contourPath`, `allContours`,
`usedContours`, `contourMean`); `HoleBesideASecondHole/BlocksOfTheLevels.lean` L210-215 (`axisPath_eq_flows`: an axis
path is one straight run per axis, in the order $\pi(0),\dots,\pi(3)$); `TotalDensitiesGiveASystem/TopStatementDefs.lean` L12-18
(`IsUnitMeshStepParameters`: coupling = 1, side odd, **side at least 2^40**, threshold in (0,1)). Credit for every
object in this section: Sussman and Alpoge (with Claude and Codex), YM4 Lean release.

### 3.1 The objects

A fine field $W$ on the torus of side $mL$, a coarse field $V$ on the torus of side $m$, $L$ the block side.
For a coarse bond $c=(y,\mu)$ and a base choice $b$, a contour $e=(\xi,\pi)$, $\xi$ in the centred cube of side
$L$, $\pi\in S_4$, is the lattice path: axis path (axes in the order $\pi$) from $b(y)$ to centre$(y)+\xi$, then
$L$ steps in direction $\mu$, then the reverse axis path from centre$(y+\hat\mu)+\xi$ to $b(y+\hat\mu)$. The contour
mean is $\bar W_b(c)=|E|^{-1}\sum_{e\in E}\mathrm{hol}_W(e)\in\mathbb H$, $E$ the used contours. The kernel is

$$
K_b(W,V)=\prod_c\frac{\exp\big(x\,\mathrm{Re}(\bar W_b(c)V(c)^{-1})\big)}{\mathcal Z(x\|\bar W_b(c)\|)},\qquad
\mathcal Z(s)=\int_{SU(2)}e^{s\,\mathrm{Re}\,g}dg,\qquad
D'(V)=\int D(W)\,\frac1{|\mathcal B(W)|}\sum_{b\in\mathcal B(W)}K_b(W,V)\,dW .
$$

The **plain kernel** $K^{pl}$ is the case of one base choice (all bases at cell centres) and all $N=24L^4$
contours. It equals the release's kernel wherever no hot lump is near (my reading of `usedContours` and
`IsBaseChoice`; not checked beyond the quoted lines). The results below are proved for the plain kernel.

### 3.2 Lemma LD-1 (exact step identity). PROVED

Let $D\ge0$ be integrable, $x>0$, $D'(V)>0$, $X$ a map from coarse bonds to $\mathrm{Im}\,\mathbb H$, and
$V_\varepsilon(c)=e^{\varepsilon X(c)}V(c)$. Let "post" be the law of $(W,b)$ with density proportional to
$D(W)|\mathcal B(W)|^{-1}K_b(W,V)$. Put $q_b(c)=\bar W_b(c)V(c)^{-1}$, $\xi_b(c)=\mathrm{Im}\,q_b(c)$,
$m_V(c)=\mathbb E_{post}\mathrm{Re}\,q_b(c)$. Then

$$
-\frac{d^2}{d\varepsilon^2}\Big|_0\log D'(V_\varepsilon)
= x\sum_c|X(c)|^2\,m_V(c)\;-\;x^2\,\mathrm{Var}_{post}\Big(\sum_c\langle\xi_b(c),X(c)\rangle\Big).\qquad\text{(LD-1)}
$$

*Proof.* Only the numerators depend on $V$. For a quaternion $q$ and imaginary $X$:
$\frac d{d\varepsilon}\mathrm{Re}(qe^{-\varepsilon X})|_0=-\mathrm{Re}(qX)=\langle\mathrm{Im}\,q,X\rangle$ and
$\frac{d^2}{d\varepsilon^2}\mathrm{Re}(qe^{-\varepsilon X})|_0=\mathrm{Re}(qX^2)=-|X|^2\mathrm{Re}\,q$. So
$\ell_b(\varepsilon)=\log K_b(W,V_\varepsilon)$ has $\ell_b'(0)=x\sum_c\langle\xi_b(c),X(c)\rangle$ and
$\ell_b''(0)=-x\sum_c|X(c)|^2\mathrm{Re}\,q_b(c)$. For a mixture, $(\log\int e^{\ell})''=\mathbb E_{post}[\ell'']
+\mathrm{Var}_{post}(\ell')$; differentiation under the integral is allowed because the domain is compact and
$|\ell'|\le x\sum_c|X(c)|$. $\square$

**Corollary LD-2 (the kernel caps the local stiffness). PROVED.** For every $D\ge0$, every coupling, every $V$:

$$
-\frac{d^2}{d\varepsilon^2}\Big|_0\log D'(V_\varepsilon)\le x\sum_c|X(c)|^2\,\mathbb E_{post}\|\bar W_b(c)\| .
$$

**Remark LD-3 (the readout; SKETCHED, the Lean statement of `nextCoupling` was read only through row 1456
L50).** At $V=\mathbf 1$ the off-diagonal Hessian kernel of $\log D'$ is $x^2\mathrm{Cov}_{post}(\xi(c),\xi(c'))$,
so the readout is $x'=(x^2/2)\sum_z z_0^2\,\mathrm{Cov}_{post}(\xi^a(0,e_1),\xi^a(z,e_1))$: the next coupling is a
second moment of the posterior covariance of the block means given a trivial coarse field. This has the form of
Proposition LIFT of row 1383 (a mean minus a conditional variance), now for an averaging map. It is blind to the group; a sign for it at order-one coupling is K-I.

### 3.3 Lemma SE (self-energy of two thin lines). PROVED

Let $t$ have the density proportional to $e^{\kappa t}(1-t^2)^{1/2}$ on $[-1,1]$ and $A(\kappa)=\mathbb E\,t$.

(a) $A(\kappa)\le1-\dfrac3{2\kappa+3}$ and $A$ is increasing. *Proof.* $\frac d{dt}(1-t^2)^{3/2}=-3t(1-t^2)^{1/2}$,
so by parts $\mathbb E\,t=\frac\kappa3\mathbb E(1-t^2)\le\frac{2\kappa}3\mathbb E(1-t)$, hence
$\mathbb E\,t\le\frac{2\kappa}{2\kappa+3}$. $A'=\mathrm{Var}(t)\ge0$. $\square$

(b) Under the Wilson law at $\beta$ (any torus, any twist of signs on plaquettes), let a closed lattice word,
after free reduction, contain a set $S$ of links, each exactly once, no two of them in a common plaquette. Then
$|\mathbb E\,\mathrm{Re}\,\mathrm{hol}|\le A(6\beta)^{|S|}\le\exp\!\big(-|S|/(4\beta+1)\big)$.
*Proof.* Given all links outside $S$, the links of $S$ are independent, and $U_\ell$ has the density proportional to
$\exp(\beta\,\mathrm{Re}(U_\ell M_\ell))$ with $M_\ell$ the sum of the six staples, $\|M_\ell\|\le6$. Its mean is
$A(\beta\|M_\ell\|)$ times a unit quaternion. The holonomy is multilinear in the links of $S$, so its conditional
mean is the same product with each $U_\ell$ replaced by its mean; the quaternion norm is multiplicative. $\square$

(c) **Plain contour mean.** For every coarse bond $c$, $\;\mathbb E_\beta\|\bar W^{pl}(c)\|^2\le\dfrac7L+e^{-2L/(4\beta+1)}$.
*Proof.* $\|\bar W\|^2=N^{-2}\sum_{e,e'}\mathrm{Re}(\mathrm{hol}(e)\overline{\mathrm{hol}(e')})$. Call a pair
generic if all components of $\xi,\xi'$ transverse to $\mu$ are non-zero and $|\xi_i-\xi'_i|\ge2$ for one
transverse $i$. The non-generic fraction is at most $6/L+27/L^3\le7/L$ (for $L\ge6$). For a generic pair the reduced loop
contains $L$ links of the line through $\xi_\perp$ and $L$ links of the line through $\xi'_\perp$, each once:
the straight segment, or, when $\mu$ is last in $\pi$, the segment from offset 0 to offset $L$ after the leg's
backtracking cancels. A leg moves in direction $\mu$ at a transverse position whose components are 0 or those of
its own $\xi$; it meets a generic line only in the case just described. Collinear links share no plaquette, and
lines at transverse distance at least 2 share none. Apply (b) with $|S|=2L$. $\square$

(d) **Posterior version.** Let post be the law of $W$ proportional to $w_\beta(W)K^{pl}_x(W,V)$, any $V$. Then
$\mathbb E_{post}\|\bar W^{pl}(c)\|^2\le\dfrac7L+e^{-2L/(4\beta+1)}+e^{\eta}-1$, $\;\eta=256\,x/L^3$.
*Proof.* Fix a generic pair and its set $S$ (two lines). A contour of any bond meets a given generic line only
if its three coordinates transverse to $\mu$ equal the line's (as a straight segment, or as a leg with $\mu$
last): a fraction at most $L^{-3}$ per line, so at most $4L^{-3}$ is a safe count for the two lines. At most 16 bonds have contours in the two cells of $S$. So a change
of the links of $S$ moves each $\bar W(c')$ by at most $8L^{-3}$ in norm, each numerator exponent by at most
$8xL^{-3}$ and each $\log\mathcal Z$ by at most $8xL^{-3}$ ($|(\log\mathcal Z)'|\le1$): in total the kernel
changes by a factor in $[e^{-\eta},e^{\eta}]$. Given the links outside $S$, the posterior law of the links of $S$
has a density in $[e^{-\eta},e^{\eta}]$ against the Wilson conditional law, so a function bounded by 1 has a
mean within $e^\eta-1$ of its Wilson conditional mean. Sum as in (c). $\square$

### 3.4 Theorem LOSS (the plain Lean step loses the coarse field below $x\approx\sqrt L$). PROVED

Let $D_1^{pl}(V)=\int w_\beta(W)K^{pl}_x(W,V)dW$ on any torus, and
$\epsilon^2:=7/L+e^{-2L/(4\beta+1)}+e^{256x/L^3}-1$. Then for every $V$ and $X$:

$$
-\frac{d^2}{d\varepsilon^2}\Big|_0\log D_1^{pl}(V_\varepsilon)\le x\,\epsilon\sum_c|X(c)|^2 .
$$

*Proof.* Corollary LD-2, Jensen, Lemma SE (d). $\square$

Numbers at the release's smallest side $L=2^{40}$, for $\beta\le10^9$ and $x\le10^9$:
$\epsilon\le2.53\cdot10^{-6}$ ($7/L=6.37\cdot10^{-12}$; the other two terms are below $10^{-24}$). So for $x=\beta\le3.9\cdot10^5$ the blocked action $-\log D_1^{pl}$ has Hessian at
most the identity at **every** coarse field. A Wilson density at inverse coupling $x'$ has single-bond Hessian
$6x'$ at the trivial field.

**Corollary RANGE (PROVED given its hypothesis).** Let the Hessian form of $-\log D_1^{pl}$ at $V=\mathbf 1$ have
the symbol $\hat Q_{11}(k_0,0,0,0)\ge x'k_0^2-Mk_0^4$ at some torus momentum with $k_0^2=x'/(2M)$. Then
$M\ge x'^2/(4x\epsilon)$. *Proof.* LOSS gives $\hat Q_{11}\le x\epsilon$ at every momentum; evaluate. $\square$
So if the readout continued the asymptotic-freedom line $x'\approx x-c_0$ at $x\le3.9\cdot10^5$, the blocked
action would have a squared range $M/x'\ge1/(4\epsilon)\approx10^5$ in coarse units: it is not a local action at
the coarse scale with order-one constants.

**What this decides.**

1. (LD-loc) is **REFUTED for the plain kernel at the first step** in the range $x=\beta\le\sqrt L/3$: the step
   returns local stiffness at most 1, at couplings where the physical coupling at scale $L$ is still weak
   ($\beta-c_0$ with $c_0=\tfrac{11}{3\pi^2}\log L\approx10.3$). The cause is the linear self-energy of thin
   transporters of length $L$, the same for U(1). It is not disorder of the theory.
2. For the release's adapted kernel (hot lumps, moved bases, filtered contours) and for later levels the same
   statement is SKETCHED only: the adaptation removes contours and does not thicken them; at later levels the
   one-link conditional law is no longer explicit.
3. Consequence for the lane's plan: the Lean flow cannot be the vehicle of the band, in any form. Its block side
   is at least $2^{40}$ by hypothesis, so one step spans the whole band, and below $x\approx\sqrt L$ its output is
   not a carrier of the coupling. Theorem T's transfer to the Lean datum (row 1456) stays valid as a statement on
   the first-passage set; a band step (K-II) needs a different map, with transporter self-energy bounded: block
   side at most of order $x$, so side 2 or 3 at order-one coupling. GUESSED: the release's floor is at least of
   order $\sqrt L$; not read in the release.
4. With a small-block soft map, LD-1 still holds and Remark LD-3 gives the step as a posterior second moment.
   The first lemma then reads: $(x^2/2)\sum_z z_0^2\mathrm{Cov}_{post}\le x-c$ at order-one $x$. That is K-I. So
   **attack LD reduces to the common wall.** It is not progress on (M-neutral-all).

### 3.5 Verdict of the row

- No attack was found that avoids the common wall. My Phase 1 attack (ORB) is the lane's (VIR_K). My Phase 3
  attack (LD) is new as an object, its first lemma is refuted for the release's map in a stated range, and with
  a repaired map it is K-I.
- What is proved here: Lemma LD-1, Corollary LD-2, Lemma SE (a)-(d), Theorem LOSS, Corollary RANGE. All by
  hand, unchecked. No numeric run: memory free was 39 percent (`memory_pressure`, 13:22Z), below the 50 percent
  rule.
- What is argued: Remark PATH (2.1): a coupling-path proof must read the Wilson SU(2) weight through a number;
  only scale-path attacks at a late cutoff are not excluded structurally. This is not a proof that every attack
  hits the wall.
- Open, unchanged: K-I or K-II for a small-block map; (A1); (M-neutral-all); the gap.

## 4. Next two rows

1. **`gap-crux-direction-fable-check-astra62`** (cross-provider check, read only). Check Theorem LOSS first:
   Lemma SE (c) (the genericity count and the claim that legs do not meet a generic line), Lemma SE (d) (the
   count of contours through a line and the factor 256), LD-1. Then read `usedContours`, `IsBaseChoice` and
   `hotLumps` in the release and decide whether LOSS holds for the release's kernel on cold configurations.
   Decisive outcome: HOLDS, or the first failing line. If SE (c) fails for the release's kernel, item 3 of 3.4
   falls back to "not shown".
2. **`lean-step-side-read-opus`** (read only, no proof). In the release, list every lemma of
   `ClusterExpansionOfAStep` and `TotalDensitiesGiveASystem` that consumes `side_ge` or `side_gt`, with the
   inequality each one needs, and the place where the coupling ceiling of the calibration is chosen after the
   side. Decisive outcome, one of two: (a) an explicit floor $H(L)$ and the smallest admissible side, so that
   the band $[\,\text{order one},H\,]$ has numbers for the first time (row 1326 found "the datum has no numbers")
   and the sizing of K-III can be redone on them; or (b) the side bound is structural (lump geometry) and the
   release gives no small-block step, so K-II must be built from Balaban's averaging map. Either result fixes
   which map a K-II row may use. No attack row on the band is proposed: none found here passes the filter of
   row 1386, and row 1442's reopen triggers (R1)-(R3) stand.

## 5. Result

Finished 2026-11-24T13:27Z (`date -u`). Author only, checked by no one. No numeric run (memory free 39 percent, below the rule).

RESULT: Row 1460 (Claude Fable 5.2 high, Mac mini worker 1; author only, unchecked; hand proofs, no numeric run, release read only). No attack was found that avoids the common wall; (M-neutral-all) is not moved. Phase 1 (before reading rows after 1142): the target as a thermal statement; any proof must supply a no-stalling statement (NS) on a compact band of order-one couplings, from an exact non-abelian inequality, a signed identity or a verified computation; named attack ORB with first lemma (VIR-H) (an excitation lowers the magnetic term by at most kappa/2 times its energy). Phase 2: every Phase 1 item is on file ((K-one)/(K-flow), K-I to K-III, Theorem T, Proposition V); (VIR-H) is (VIR_K) of row 708, so ORB is equivalent to a closed line. Remark PATH (ARGUED): coupling-path carries must read the Wilson SU(2) weight through a number (Proposition V, N-test); only scale-path attacks at a late cutoff are not excluded structurally. Phase 3, attack LD (carry the band on the Lean release's own exact block map; not on file): PROVED by hand, Lemma LD-1 (the blocked log-Hessian is x times the posterior mean of Re(contour mean) minus x^2 times a posterior variance), Corollary LD-2 (the kernel caps the local stiffness), Lemma SE (the squared plain contour mean has Wilson and posterior mean at most 7/L + exp(-2L/(4 beta+1)) + exp(256x/L^3) - 1, from the self-energy of thin transporters), Theorem LOSS (for the plain kernel at the first step the blocked action has Hessian at most x epsilon at every coarse field; at L = 2^40 at most the identity for x = beta up to 3.9e5), Corollary RANGE. So the first lemma (LD-loc) is refuted for the plain kernel in that range, the Lean flow is not a vehicle for the band (block side at least 2^40 by hypothesis), and with a small-block map LD is K-I: it reduces to the common wall. SKETCHED only: the same for the release's adapted kernel and for later levels. Open: K-I or K-II for a small-block map, (A1), the seed, the mass gap. Next rows: (1) cross-provider check, Theorem LOSS first, and whether it holds for the adapted kernel on cold configurations; (2) `lean-step-side-read-opus`, a read-only list of what consumes the side bound and where the coupling ceiling is chosen: either an explicit floor H(L) (numbers for the band) or "the side bound is structural". Credit: Balaban; Sussman and Alpoge with Claude and Codex (every Lean object used); Simon and Yaffe for one-link randomization.
