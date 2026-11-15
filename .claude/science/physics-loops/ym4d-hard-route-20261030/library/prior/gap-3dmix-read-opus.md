lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-15T13:45Z

# gap-3dmix-read-opus (FINISH row 992): literature search for a volume-free 3D SU(2) mixing / LSI / susceptibility bound

Pinned commit d0d88c388, branch claude/ym4d-hard-route. Started 2026-11-15 01:45Z (date -u). Literature reading only;
no numeric job planned.

## Plan (at most eight steps; one step per response, appended before the next)

1. Read row 992, Route 2 (i) / Identity G of `library/gap-unit-max.md`, and grep the lane (open-core, FINISH rows,
   prior reading files) for earlier 3D mixing / LSI literature searches, so this search runs on a new path.
2. Sussman-Alpoge repository: YM3 subfolder (YM3_I and later parts) and any 3D statements in the complete account;
   statement, coupling range, volume-free or not.
3. Balaban's 3D papers (CMP 1984-1989 series on 3D lattice gauge theory, the UV-stability papers) and Dimock's
   revisits: what they bound (effective actions, partition function), whether any mixing/susceptibility statement.
4. Recent stochastic-analysis results: Shen-Zhu-Zhu (Langevin/Bakry-Emery for lattice YM, strong coupling),
   Chatterjee, Cao-Nissim-Sheffield, Adhikari, Chevyrev-Chandra-Hairer-Shen (3D YMH / 2D-3D Langevin), Bauerschmidt-
   Bodineau-Dagallier (LSI by Polchinski flow), Forsstrom, Gross-King-Sengupta (3D YM measure, small time), etc.
5. Arxiv full-text search (fetched into /tmp scratch) for any remaining hit: "three-dimensional" lattice gauge
   theory + "log-Sobolev" / "spectral gap" / "mixing" / "mass gap" at weak coupling.
6. Table: hit, statement, coupling range, volume-free?, short quote with citation.
7. Verdict on Route 2 (i) (Identity G anchored at zero temporal coupling): does any hit supply it?
8. RESULT line.

## Status log
- 2026-11-15 01:45Z: file created with plan.

## Step 1. Target, duplicate check, earlier searches (done 2026-11-15 01:46Z)

**Target (row 992, from `library/gap-unit-max.md` Route 2, L197-229, row 988).** Identity G: at temporal coupling
beta_t = 0 the time slices of B x t decouple, S(t; B) = 0, and X(t; B) is an integral over the temporal coupling s in
[0, beta_t] of the gap between mean temporal plaquette actions. Route 2 (i) needs a seed in the time direction for small s,
uniform in the box. One link of a slice changes the next slice's density by a factor in [e^(-4s), e^(4s)], but the changed
law can move all links through the correlations of nu_0, the slice law. nu_0 is three-dimensional SU(2) Wilson theory at the
unit (window) spatial coupling. A volume-free rate needs "s times a susceptibility of nu_0 below one". So the input searched
for is: a volume-free bound on a susceptibility, a mixing time, a spectral gap or a log-Sobolev constant of 3D SU(2) lattice
gauge theory (Wilson or a nearby action) at weak or order-one coupling, i.e. outside the strong-coupling regime.

**Duplicate check (rule 0a).** This is a reading row, not an attack on an open lemma. `library/open-core.md` and the FINISH
rows: row 992 is the only row on this search (grep "gap-3dmix" hits only line 1070). No lemma is attacked here.

**Earlier lane searches that already hold related hits (read by grep only; this run does not repeat them):**
- Shen-Zhu-Zhu arXiv:2204.12737 (LSI / Bakry-Emery for lattice YM, strong coupling only: `prior/gap-lit-bridge-lsi.md` L55,
  `prior/gap-lit-grok.md` L99, "|beta| < 1/48" for d = 4 in their normalisation).
- Piazza-Shen arXiv:2610.35286 (2D all coupling; `prior/gap-lit-bridge-lsi.md` L56; row 957 `gap-ps-disint-max.md`).
- Bauerschmidt-Bodineau-Dagallier arXiv:2307.07619 (LSI by Polchinski flow; spin systems; row 968).
- 3D U(1): Goepfert-Mack CMP 82 (confinement / gap, all couplings, Villain; `prior/gap-crux-lit-nonab.md` L139).
- 3D with central U(1): Chatterjee / Adhikari-Cao arXiv:2602.00436 (`prior/gap-crux-lit-nonab.md` L147,
  `prior/gap-lit-arealaw.md` L28).
- Nair arXiv:2608.10133 (3D SU(N) Hamiltonian, `prior/gap-crux-lit-nonab.md` L197); Cherrington arXiv:0908.1893
  (`prior/gap-crux-lit-2.md` L239).
- Sussman-Alpoge YM3_I and Aronow-Lopatto 3D SU(2) torus: located for the large-field question only
  (`lit-large-field.md` L103-136); never read for a correlation, mixing or gap statement.

**New path for this run.** (a) the 3D manuscripts of the Sussman-Alpoge repository (YM3_I, YM3_II, YM3_main) and the
Aronow-Lopatto 3D SU(2) papers, read for what they prove about correlations, clustering or a gap at weak coupling;
(b) Balaban's 3D gauge papers and Dimock's QED_3, same question; (c) recent stochastic-analysis work on 3D gauge theory
(Chandra-Chevyrev-Hairer-Shen 3D YMH, Cao-Chatterjee 3D state space, Shen-Zhu-Zhu YMH Langevin, finite-group weak-coupling
decay of Adhikari-Cao / Forsstrom, any 2025-2026 LSI or spectral-gap paper for d = 3) by a fresh arXiv listing search.

## Step 2. Sussman-Alpoge 3D manuscripts (YM3) (done 2026-11-15 01:47Z)

**Source and version.** Repository `ethanwsussman/Yang--Mills-LLM-experiment`, fetched by raw URL at main
`c7fef8b21b58` into `/tmp/gap3dmix-sa/`. The four YM3 `.tex` files have the same byte sizes at our pin `31a47c543775`
(GitHub tree API), and the last commit touching `YM3/YM3_II.tex` is `5b90577cd6cd` (2026-11-01, a rename). Line numbers
below are of these files. Authors: Ethan Sussman and Levent Alpoge, text written with Claude and Codex (README L8-21).
Term counts (grep -c -i), YM3_I / YM3_II / YM3_main: "log-Sobolev" 0 / 14 / 0; "mixing" 0 / 6 / 0; "susceptib" 0 / 0 / 0;
"Dobrushin" 0 / 2 / 0; "mass gap" 2 / 2 / 1; "strong coupling" 0 / 1 / 0.

**What YM3 claims, by its own scope lines.** Continuum SU(2) YM in d = 3 on tori and growing-torus limits, observable the
plaquette-energy density; Osterwalder-Schrader axioms for tr F^2 (README L21). It states it does not prove a gap:
- YM3_I L660-669: "fixed-torus estimate retains a power of the volume and does not give uniqueness of these infinite-volume
  limits ... asserts no mass gap." YM3_I L89138: "it does not prove non-Gaussianity or a mass gap."
- YM3_main L325: "The result leaves contact terms, uniqueness of the cutoff limit and a mass gap open."
- YM3_II L2334: "no mass gap, uniqueness of the vacuum or clustering is used."

**Hit 2a. YM3_II Theorem C-367-2 "Nontrivial Markov limits and mixing" (L22346-22400), Section "Continuum limits of the
lattice Langevin dynamics" (L22250).** Under the setting (E) (a calibrated weak-coupling first-passage family, L33705-33755),
on a FIXED torus of side ell, the Wilson Langevin processes have subsequential continuum limits. (A4) gives a WEAK Poincare
inequality with a defect: Var_mu(H) <= C_n E(H) + r_n osc(H)^2, and L^2 relaxation
||P_t H - mu(H)||^2 <= (r_n + (1/4) e^(-2t/C_n)) osc(H)^2. (A5) is a weak entropy relaxation. Coupling range: the
continuum (fine lattice, weak bare coupling, superrenormalizable 3D) at a fixed physical torus.
Volume-free: NO. The section preamble (L22259-22261): "Their constants may depend on the fixed torus". Subsection
"Uniformity and the order of limits" (L25077): "The inequalities of (A4), (A5) and (B2)(c) carry a defect, and their
constants depend on ell". Also a weak inequality with a defect r_n > 0 is not a spectral gap.

**Hit 2b. YM3_II Lemma C-367-7 (iv) "Conditional laws along the renormalisation chain" (L22681-22700, proof SKETCH).** On the
small-field part sigma^K of the measure (lost mass at most R_n), the law p_W of the fine field in a gauge chart, given the
block field W one scale up, is e^(-Psi_W) dB with (1/4) gamma_r <= D^2 Psi_W <= Lambda_+, so Bakry-Emery gives
Var and (1/2) Ent of g o V_W at most C_P (a_d^2 / b) times the Dirichlet form, "with C_P = 4 C_ch / gamma_r, which depends
only on the constants of the construction, and not on K, k, W, ell or b". Volume-free: YES, but it is a CONDITIONAL
(fibre) inequality: fine scales given the coarse block field, on the small-field cut. L25077 confirms that the only
volume-free constants of the mixing theorem "are those of the fine field given a block field". Coupling range: weak
coupling at every scale of the chain (the small-field region of the RG of a superrenormalizable theory).

**Hit 2c. YM3_II Lemma sf-plat (a), (d) (L35324-35330, proof sketch).** Under (H), for limits at coupling g:
|rho(A(X tau_v Y)) - rho(E[A(X)|I] E[A(Y)|I])| <= C(X) C(Y) R/|v|, with I the translation-invariant sigma-field; the proof
says this is "the power |v|^(-1) that positivity gives without a mass gap" (reflection positivity and nested cubes).
Volume-free: yes as a bound, but a rate |v|^(-1) is not summable in d = 3 (the sum over a box of side ell grows like
ell^2), so it gives no susceptibility bound and no mixing rate.

**Hit 2d. `YM3/YM3_supplement.tex` (same commit; 50,022 lines) repeats Theorem C-367-2 (L32450) and says plainly (L32443-32446):
"The constants C_n may depend on the physical torus. This proves the stated mixing without supplying a spectral gap uniform
in volume."** Same verdict as 2a. `YM3_alt.tex` has no hit for any search term except three "exponential decay" lines (not read).

**Hit 2e. YM3_supplement Proposition C-378-379-1-13 (L47038).** Exponential clustering and a hyperboloid spectrum
"suppose that m = liminf m_lat(nu_j)/a_j > 0". This is an implication FROM a lattice gap, so it supplies nothing here.

**Hit 2f. YM3_supplement Section "A finite-size criterion for confinement", Sketch C-361-3 (L35807-35870), labelled a
SKETCH by its authors.** With e(l) = 2 log Z(l,2l,2l; beta) - log Z(2l,2l,2l; beta) (periodic 3D Wilson boxes): if
e(l_K) <= x_0 <= 0.069 at one physical side ell_0 for every large cutoff, then theta = 12.9 x_0 < 1, the Gibbs and continuum
limits and the vacuum are unique, and the gap is m_* = 2 log(1/theta)/ell_0; the engine is the doubling
"e(2l) <= 12.9 e(l)^2". The text says it "isolates the remaining quantitative confinement problem in one explicit
inequality". So in 3D the hypothesis (a small free-energy defect at one scale) is OPEN, and the criterion has the same
shape as this lane's own seed-plus-doubling (Theorem S and the seed of `gap-crux-restate.md`; (U2) of row 988). It moves the
3D input of Route 2 (i) to a 3D seed, one dimension down; it does not supply it.

**Relevance to Route 2 (i).** Route 2 (i) needs a volume-free susceptibility of nu_0, the three-dimensional slice law at the
order-one unit coupling, on a box of side up to e^(c/g^2) unit cells. That is the infrared (coarse) end. YM3 gives the
opposite end: a volume-free conditional LSI of fine scales given the block field (2b), and at the coarse end only
ell-dependent weak inequalities (2a) and a non-summable 1/|v| (2c). In the superrenormalizable 3D theory the dimensionless
coupling at the torus scale is g^2 ell, so a volume-free top-scale inequality is the 3D mass-gap problem, which YM3 states
is open. Verdict for Step 2: NO supplier. YM3_supplement and YM3_alt were grepped (2d-2f): no unconditional volume-free statement.

## Step 3. Aronow-Lopatto (3D SU(2) on a torus) and Balaban's 3D papers (part A written 2026-11-15T01:48Z)

**Hit 3a. P. M. Aronow and P. Lopatto, "The continuum limit of three-dimensional SU(2) lattice Yang-Mills theory on a
torus"** (machine-written with supervision, per its README). Read: GitHub `pmaronow/3d-ym-torus` at `93ebd0dfeb38`
(README says it is "dated"; the current five-part version is on hexagonmath.org 2610.00506-2610.00512, which returned a
sign-in page, so I stopped there). Fetched to `/tmp/gap3dmix-al/`. Statement (abstract): Wilson SU(2) on a FIXED periodic
3D torus, bare coupling g^2 = g_3^2 a; joint laws of finitely many Wilson-flowed loops converge as a -> 0 along sides
n M^k; small-field complement controlled "using reflection positivity and chessboard estimates". Coupling range: every
fixed g_3 on a fixed torus, i.e. weak lattice coupling at the cutoff. Its own scope (`s01_introduction.tex` L70): "The torus
is fixed: we do not take the infinite-volume limit, and we prove nothing about a mass gap or confinement." Its LSI
statements are conditional, fine given coarse: the "conditional fluctuation kernel" has density proportional to
1_Omega e^(-V) with "D_w^2 V >= I/2" (`s16_ch13.tex` L31, `s03_overview.tex` L53), whence an LSI with constant 4 on
products of balls (`s32_ch29.tex` L238). Grep counts over all 36 section files: "susceptib" 0, "Dobrushin" 0, "spectral
gap" 2 (both finite-dimensional tools in `s05_ch02.tex`). Volume-free top-scale statement: NONE. Same structure as YM3_II
Lemma C-367-7 (iv): volume-free only for the fibre law of one RG step.

**Hit 3b. T. Balaban, "Ultraviolet stability of three-dimensional lattice pure gauge field theories", CMP 102 (1985)
255-275, DOI 10.1007/BF01229380 (Crossref).** Open copy: Deep Blue hdl 2027.42/46460 answered with a Cloudflare page
("Just a moment"), Springer returned no abstract to curl; I stopped there (rules). Not in `~/ym4d-papers` (it holds 102b
only, per its README and `library/b109.md` L113). Statement as quoted by Sussman-Alpoge YM3_I L89012-89019 (secondary):
Theorem 1 and (5)-(6) give "upper and lower bounds on the renormalized densities and, after stopping at a fixed coarse
scale, cutoff-uniform bounds on the normalized partition function ... These bounds control the size of the functional
integral; they do not by themselves assert convergence of the correlations". Coupling range: 3D pure gauge, small bare
coupling at the cutoff, fixed physical torus. Volume-free mixing: NO. The bounds are of the size of the functional
integral, e^(+-c |Lambda|) in the physical volume; no correlation, mixing or susceptibility statement.

**Hit 3c. The rest of Balaban's gauge series** (CMP 95, 96, 98, 99a, 99b, 102b, 109, 116, 119, 122a, 122b) is the
multiscale small-field / large-field RG on a fixed torus, mostly in d = 4 with d = 3 cases in the propagator papers. The
lane has read these for the UV chain (`library/lit-balaban.md`, `library/b109.md`, `library/b119.md`). None of them states an
infrared statement: no mass gap, clustering at the torus scale, or volume-free mixing. Balaban states his results on a
torus of fixed physical size. Grep check (2026-11-15 01:50Z) over `lit-balaban.md`, `b109.md`, `b119.md` and the OCR of
CMP 96, 98, 99a, 99b, 102b, 122a, 122b in `~/ym4d-papers`: "mixing" 0 and "mass gap" 0 in every file; "cluster" (0-4 per
file) is the cluster expansion of effective actions; "decay" (0-17) is the decay of the block propagators at the block
scale, which comes from the averaging operator, not a physical gap. CMP 95, 109, 116, 119 were not grepped (not on disk).
This is a negative statement by grep and from the lane's records, not a fresh re-read of each paper.

**Hit 3d. Dimock, QED_3 series** (arXiv 1512.04373, 1712.10029, 2009.01156; `library/lit-large-field.md` L90-100):
abelian, ultraviolet stability on a fixed torus. Not SU(2), not infrared. NO.

**Step 3 verdict.** The Balaban-school 3D work (Balaban, Dimock, Sussman-Alpoge YM3, Aronow-Lopatto) is ultraviolet:
fixed physical torus, weak coupling at the cutoff, and every volume-free inequality in it is a conditional (fibre) inequality
for one RG step given the coarse field. None reaches the order-one coupling at the coarse end, which is where nu_0 lives.
