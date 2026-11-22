lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-22T17:57Z

# Row 1382: the selective facts on the record against (5D) and (AH)

Row `gap-selective-5d-sweep-opus`, Claude Opus 5.5 high, Mac mini worker 2, commit 2df402783, started 2026-11-22T05:57Z (date -u).
Reading and short proofs. No new attack. Checked by no one.

## Plan

Source: `library/gap-mech-direction-fable.md` (row 1380), Section 5, row 2.
For each positive selective statement on the record, read the statement and its proof in its file and say:
(a) does the proof use d = 4 through a scale-free sum (a sum over scales or a log-divergent lattice sum that
is marginal exactly at d = 4)? (b) does the statement hold verbatim for SU(2) in d = 5 at weak coupling
(no mass gap; test (5D))? (c) does it hold verbatim for SU(2) with an adjoint Higgs factor (test (AH))?

Items, in order:
1. Row 1141, items (2) and (8).
2. Lemma NAB, row 1018.
3. Lemma FR, row 1011.
4. Identity CUBE and Lemma SOFT, row 1016.
5. Corollary WN2's rho, row 1013.
6. Proposition LF and Theorem BD, row 1034.
7. M-C, row 1380.
8. Any other selective statement in the registry of `parts/gap.md`.

Decisive outcome: the list of selective facts that survive (5D). Empty list: no selective fact on the record sees
the scale. Non-empty: name the seed.

## Repo search

(written as each item is read)

Searched before judging (grep, this checkout): the row files named in the brief; `parts/gap.md` (registry, via
`git show HEAD:`); `library/open-core.md` and the FINISH rows for "5D", "five dimensions", "adjoint Higgs".
Hits are cited at each item. The test definitions are row 1380's (`gap-mech-direction-fable.md` L152-158):
(5D) SU(2) in five dimensions at weak coupling, massless (belief grade, row 1011 Section 6); (AH) SU(2) with an
adjoint Higgs field in its Coulomb phase, massless (belief grade, item A16 of row 1017).

**Reading of "survives".** A fact survives (5D) when it is false in (5D), or when its proof fails there at a
named line, so that it can tell the gapped theory from a massless one. A fact that holds verbatim in (5D)
(constants allowed to change with the number of plaquettes per link, 2(D-1)) is a lattice-scale fact and does
not survive. The same reading for (AH). Notation: D is the lattice dimension, d a sub-cube dimension.

## Item 1. Row 1141, items (2) and (8) (`library/gap-crux2-astra62.md` L45-133)

**Statements.** (2): in a cube of side R inside a periodic Wilson SU(2) torus, with probability at least
1 - (2+R)^(-k), every adjoint section s has covariant energy at least c/(1 + b + (log(2+R))^(2/d)) |s|^2.
(8): E lambda_x >= 1/(64(1+6b)) for the minimum over a common axis of the forward-plaquette cross products.

**Where the proof uses the dimension.** Only locally: (i) the one-link conditional law is e^(h.q) with
|h| <= 2(D-1) b, so 6b at D = 4 (L55); (ii) the density bound M_b = 4(1 + 2(D-1) b) and the cap estimate (3);
(iii) cells of side three, 6^d of them per rectangle of side m (L96), and the Poincare constant 2 d m^2 on a
rectangle of side m ~ (log R)^(1/d) (L105-117); (iv) a union bound over at most R^d rectangles. There is no sum
over scales and no lattice sum that is marginal at D = 4. The log R is from the union bound, not from a
propagator.

**(5D).** Holds verbatim in D = 5 with 6b replaced by 8b and 6^d, d <= 5, in the constants: every line above is
local and uses only that the two pinning plaquettes have distinct links and a common root (L127). So (2) and (8)
hold in five dimensions at weak coupling, where the theory is believed massless. **Does not survive.** This is
row 1380's own example (L154-158, L287).

**(AH).** With a fixed-length adjoint Higgs field phi (|phi_x| = 1) and hopping kappa phi_x . Ad(U_xy) phi_y,
the one-link conditional density is the Wilson one times a factor in [e^(-kappa), e^(kappa)], so (3) holds with
M_(b,kappa) <= e^(2 kappa) M_b, and (4), (6)-(8), (2) hold with delta_(b,kappa) = e^(-2 kappa) delta_b
(ARGUED in this one line; for a radial Higgs field condition on the moduli and truncate). The constant degrades
as kappa grows: deep in the Higgs/Coulomb phase the plaquettes are near rotations about phi, and the section
s = phi has covariant energy of order |phi|^2/kappa per site, which is mass-like in R but small. So at each
fixed kappa (2) and (8) hold with a smaller constant; they hold in the massless Coulomb phase. **Does not
survive.**

**Selective against (U1)?** Yes (D = 0 for abelian transport, L210). So these are the record's clean example of
a fact that passes (U1) and fails (5D): a statement of ultraviolet roughness.

## Item 2. Lemma NAB, row 1018 (`library/gap-short-step-max.md` L306-321)

**Statement.** Wilson SU(2), every beta > 0, torus with sides >= 3: (i) E(1 - x_p^2) >= xbar/(2 beta);
(ii) E|y_p x y_p'|^2 >= 3 (E[x_p x_p'] + (1/3) E[y_p . y_p'])^2/(218 beta^2) for p = (x;1,2), p' = (x;3,4);
(iii) lambda_x >= e_2(M)/tr M pointwise; so, if xbar >= 3/4, E lambda_x >= 1/(3924 beta^2).

**Where the proof uses the dimension.** Only through the number of plaquettes on a link, 2(D-1) = 6: in
E[X^2] = 6 beta xbar, in E[X^4] <= 108 beta^2 and in the constant 218; and through the existence of two planes
(1,2), (3,4) at x with disjoint links, which needs D >= 4. No scale-free sum. The author says so: Remark (d),
L319, "The lemma is dimension free ... it does not tell four dimensions from five".

**(5D).** Holds in D = 5 with 6 -> 8 (E[X^2] = 8 beta xbar, E[X^4] <= 3 . 8 . 8 beta^2, the constant 218 ->
2 . 192 + 2 = 386) and the same pair of planes; xbar >= 3/4 holds at weak coupling in 5D as in 4D. **Does not
survive.** Row 1018's own table (L342) already says "holds at the bare scale (Lemma NAB)" for five dimensions.

**(AH).** The integrations by parts in (i), (ii) take the full action. With an adjoint Higgs term
kappa phi_x . Ad(U_l) phi_y, X gains the Higgs force on l and D X gains a term bounded by 2 kappa |phi|^2, so (i)
and (ii) hold with kappa-dependent constants at each finite kappa (ARGUED, a one-line change of the two
Schwinger-Dyson identities); (iii) is pointwise. Row 1018's table (L340): "True at the bare scale (Lemma NAB holds
there)". **Does not survive.** Row 1018 marks the cell-scale (FL) as the selective half and false in (AH); that is
an OPEN statement, not a fact on the record (Item 9 below).

## Item 3. Lemma FR, row 1011 (`library/gap-pinned-cell-gauge-max.md` L460-484), with FR+ of row 1018 (L247-255)

**Statement.** For every link configuration omega and every unit-vector site field n,
sum_l |D_l n|^2 >= NA(omega)/6, NA = sum_x lambda_x; FR+ is the same for variable-length fields.

**Where the proof uses the dimension.** Only in "a link lies in at most 6 plaquettes" (2(D-1)). The inequality is
a pointwise telescoping identity around one plaquette; no sum over scales.

**(5D).** Holds verbatim with 6 -> 8 for every configuration. **Does not survive.**

**(AH).** It is a deterministic inequality on link configurations, so it holds verbatim for every configuration of
the adjoint Higgs model. It is consistent with the Coulomb phase: there the Higgs field is a frame with small
defect, and FR then forces NA to be small. **Does not survive.**

**Note on row 1011 Section 3.4.** The shell sum (2 pi/N)^d sum |k|^(-d) = |S^(d-1)| log(K/M) (L202-208) is the
one statement in rows 1011-1018 that uses D = 4 through a scale-free sum: in D = 5 the sum of |k|^(-4) grows like
K and has no logarithm. It is arithmetic about free propagators and is not selective (it is the same for U(1)
and SU(2)); row 1011's test table (L434) says everything else in its Sections 3-4 is dimension free. It is
the place where a selective fact would have to meet the dimension, not such a fact.

## Item 4. Identity CUBE and Lemma SOFT, row 1016 (`library/gap-global-reform-max.md` L857-885)

**Statement.** For the twelve links of one 3-cube under Haar measure, the six class angles have the joint density
r(phi) = (2/pi)^6 prod sin(phi_i) sum_k k^(-4) prod sin(k phi_i), with r(c) = 2/(3 pi^2) and Hessian of log r
equal to -(1 + 12/pi^2) I at phi = (pi/2, ..., pi/2); so the trace map of the cube is a submersion somewhere
(SOFT). For U(1) the six angles satisfy one linear relation.

**Where the proof uses the dimension.** Nowhere: it is a Haar computation on one 3-cube (character expansion and
the gluing rule). The k^(-4) is the power of the six faces glued around one cube (each gluing gives 1/k, the
cube's Euler characteristic gives k^2), not a lattice propagator. No coupling, no sum over scales. The argued
reading after it (orbit dimension 9N against 6N plaquettes) is a count per site; in D = 5 it is 12N against
10N, so the same reading holds there.

**(5D).** Holds verbatim (a 3-cube is a 3-cube in every D >= 3). The author says so (L882: "Five dimensions: the
same structure, no dimension-4 input"). **Does not survive.**

**(AH).** A statement about Haar measure on one cube, with no action: it holds verbatim. With an adjoint Higgs
factor the conditional law of a cube is Haar times a positive continuous density, so SOFT (an open set of regular
points of positive measure) holds for it as well. **Does not survive.**

## Item 5. Corollary WN2 and its rho, row 1013 (`library/gap-invent-selective-max.md` L152-164; check
`library/gap-invent-selective-check-astra.md` items 5, 14, 15)

**Statement.** For a corner field theta whose non-zero corners lie at pairwise distinct free sites,
-W''(0) = sum over corners of theta^2 [beta E x_p - (beta^2/3) E(1 - x_p^2)] = beta rho sum theta^2 on a
common-mean torus, rho = xbar - (beta/3) E(1 - x_p^2) (WN2 HOLDS, astra item 5); WN3: rho = (beta/18) sum over
q != q' on one link of E[y_q . y_q']. rho > 0 is OPEN (astra item 15; sufficient: E(1 - x) < 3/(3 + 2 beta)).

**Where the proof uses the dimension.** WN2: nowhere; it is two Schwinger-Dyson differentiations and a gauge
average at one free site. WN3: only through the 2(D-1) = 6 plaquettes on a link, in the factor 18 = 3 . 6. No
scale-free sum.

**(5D).** WN2 holds verbatim (the setting says Z^4; nothing in the proof uses it). WN3 becomes
rho = (beta/24) sum over q != q' (eight plaquettes on a link: E|sum_q y_q|^2 = 24 xbar/beta, diagonal
8 E(1 - x^2)). The sign of rho is a same-link field-strength correlation, not a long-distance quantity. At weak
coupling the equipartition count gives E(1 - x_p) = 3/(D beta) + O(beta^(-2)) (Gaussian dof 3(D-1) per site,
D(D-1)/2 plaquettes per site; D = 4 gives row 1013's RECALLED 3/(4 beta)), hence
rho = 1 - 3/(D beta) - (2 beta/3)(3/(D beta)) + O(beta^(-1)) = 1 - 2/D + O(1/beta): 1/2 in D = 4 and 3/5 in
D = 5 (ARGUED, leading order; the same order of limits as row 1013's remark). So rho > 0 at weak coupling, if true
in 4D, is true in 5D by the same count. **Does not survive.**

**(AH).** WN2 uses only invariance of the measure under the gauge transformation at one free site; with an adjoint
Higgs factor that transformation also rotates phi_x, and the full measure is invariant, so WN2 holds verbatim
(with "free site" also meaning phi_x integrated). rho is again a same-link correlation; in the Coulomb phase the
massive W directions change its value, not its locality. **Does not survive** (the identity; the sign is open in
both models).

**U(1) for comparison.** Row 1013's table (L192): for U(1) "the twist costs classically", so WN2 is not the place
where U(1) and SU(2) differ in scale either.

## Item 6. Proposition LF and Theorem BD, row 1034 (`library/gap-sym-reg.md` L182-200, L257-287)

**Statements.** LF: with one covariant unit vector per link (rotation of U_l about its staple axis, using a
plaquette q_mu at the tail not containing l), the flow preserves e^A dU, so the current j - d is identically zero,
of range 2, with (REG); its consumer is empty (a measure-preserving flow changes no bound). BD: at a pinned lower
face {x_4 = 0} of a cell, if Psi_V for the boundary rotation (d lambda) n at a face site z is a.s. constant, then
D n = 0 on the three face links into z; so off abelian pins (Lemma FR) the cost of a boundary rotation is not a
curl form in d theta.

**Where the proofs use the dimension.** LF: only that a plaquette at the tail avoids l (D >= 3). BD: only the
three in-face directions i = 1, 2, 3 (D - 1 of them) and the private interior link P_i of the plaquette
(z - e_i; i, 4) (the count of 6.4 with nu = D). Both are one-site arguments; no scale-free sum.

**(5D).** LF holds verbatim. BD holds verbatim with i = 1, ..., 4 and the face {x_5 = 0}. **Neither survives.**

**(AH).** LF fails verbatim: the staple rotation keeps Re(U_l S_l) but not the Higgs hopping
kappa phi_x . Ad(U_l) phi_y, which is non-constant on the orbit unless phi_y is along the rotation axis; so
Psi_theta picks up the Higgs force along n_l (ARGUED, one line). This failure is not a gap mechanism: LF has zero
gain in every model. BD holds with the Higgs force at z added to Psi_V (the Gauss law at z gains the term from
phi_z); the Higgs part does not depend on the private link P_i, which is not at z, so the affine argument and
D_i n = 0 go through (ARGUED). **Neither survives.**

## Item 7. M-C, row 1380 (`library/gap-mech-direction-fable.md` L223-246)

**Statement (LAY-cov, a proposal, not proved).** E|Cov_layer(f_x, h_y | A, A')| <= C exp(-|x - y|/ell(b)) under
the Wilson law of two neighbouring slices; exact part: the mixed second derivative of log K is the layer
covariance of two forces.

**Where it uses the dimension.** Its argued source of decay is the lattice-scale mass of row 1141 (2) (Item 1),
which is local. No scale-free sum.

**(5D).** The author's own verdict (L238-240): true or false together in 4D and 5D. I agree: the argument named for
it is Item 1, which holds in 5D. **Does not survive.**

**(AH).** At fixed kappa the off-diagonal (W) components of the thin links still fluctuate at order b^(-1/2), so
the lattice-scale roughness that M-C's argument uses is present, and the layer's residual rotations about phi
are not a global symmetry of the layer unless the background is abelian; the argued mass is the same lattice-
scale one (ARGUED). **Does not survive.** The exact identity (second derivative of log K = layer covariance) is
model-free.

**Consistency check of the (AH) lines in Items 1-2.** Row 1004, Lemma GG (`library/gap-outside-box-max.md` L147,
L208; PROVED there, unchecked by me): at kappa = infinity the fixed-length adjoint Higgs model is exactly compact
U(1) with the restricted weight. Items 1 and 2 fail for U(1) (D = 0, NA = 0). So their constants must degrade as
kappa grows, which the factor e^(-2 kappa) above does. No (AH) verdict above claims a bound uniform in kappa.

## Item 8. Other selective statements in `parts/gap.md` (read at HEAD with `git show`; registry L223-266,
obligations L105-212)

The route registry lists routes, not facts. The positive statements in `parts/gap.md` and the rows it cites that
pass (U1) (true for SU(2), false or empty for U(1)) are these. Each was read at the cited lines.

**8a. Asymptotic freedom at small coupling** (`parts/gap.md` L45, quoting row 998 6b: "the one selective fact
that is provable today, asymptotic freedom at small coupling, has no engine that carries it across the band").
Supplied by the account of Sussman and Alpoge (with Claude and Codex) on Balaban's renormalization group (CMP 109
and the series), in the small-field region g_k <= gamma; not proved in the lane. One block step of ratio L reads
1/g_(k+1)^2 = L^(D-4)/g_k^2 - b_0 log L + O(g_k^2) only when D = 4; in general the one-loop term is the shell sum
of |k|^(-4), which is (1/(8 pi^2)) log(K/M) per unit volume exactly at D = 4 (row 1011 Section 3.4, L202-208).
- Scale-free sum in D = 4: **yes**, this is its whole content.
- (U1): pure U(1) has b_0 = 0: no running, so it passes.
- (5D): **false**. In D = 5 the tree term L/g_k^2 dominates, the shell sum is a power of the cutoff with no
  logarithm, and g_k decreases under blocking (infrared free, the Coulomb phase). **Survives (5D).**
- (AH): **holds**. A real adjoint scalar changes b_0 from 22/3 to 22/3 - 1/3 = 7 for SU(2) (one-loop count,
  RECALLED, not rebuilt), so the coupling runs up toward the infrared down to the W mass, where the Higgs mechanism
  stops it and the photon is free. **Does not survive (AH).** A mechanism seeded by it needs a clause that reads the
  absence of an adjoint condensate (row 1380 M-D: "(AH): a clause of A must exclude long-range order of an adjoint
  section").

**8b. Theorem A of row 1084 ((GH2_2-MIX) at beta_L = 0)** (`parts/gap.md` L209, check 1086 HOLDS GIVEN OpenAI's
Theorem 3.1). Selective: the U(1) analogue stops where OpenAI's bracket (3.28) vanishes. It is a statement about an
exact two-dimensional model (an O(4) marginal on a subdivided 2D lattice); its proof uses the two-dimensional
scale-free sum of the O(4) paper (Sum |k|^(-2), row 1011 L204), not a four-dimensional one. In D = 5 the same
sublattice construction gives the same 2D sheets (row 1011's remark on Lemma EMB, L434: "sheets exist in every
d >= 3 and are 2D models ... in 5D the bulk is believed massless"). **Holds verbatim in (5D); does not survive.**
(AH) not needed after that.

**8c. Proposition G1 of row 1128** (`library/gap-council-rg-fable.md` L272-298, PROVED there, unchecked). The
one-link sewn stiffness gains Ricci/12 = 1/6 for SU(2), 0 for the circle. A Haar identity for one link; no
dimension at all. **Holds verbatim in (5D) and (AH); does not survive.** Its author notes it is the 2D
marginal mechanism; in 4D gauge theory the marginal sum is the one of 8a.

**8d. Lemmas S and S_n of row 1273** (`library/gap-owner-threeaxis-opus.md` L334-392; Simon's method; check 1279
HOLDS). The reduced constant-mode Hamiltonian with n >= 2 spatial directions has discrete spectrum and a neutral
gap kappa_n g^(2/3)/L; for U(1) none (free rotor g^2/L on the lattice). In D = 5 there are n = 4 spatial
directions and Lemma S_n applies verbatim, with g(L)^2 the dimensionless coupling at L (which goes to zero as
L/a grows at weak coupling in 5D, as it does as L goes to 0 in 4D). With an adjoint Higgs zero mode phi the
potential gains sum_i |y_i x phi|^2 >= 0 and a confining V(|phi|), so (a)-(c) hold (row 1279 also records "the
adjoint-Higgs endpoint is exact in finite volume"). A finite-volume, small-coupling statement.
**Holds in (5D) and (AH); does not survive.**

**8e. Not selective, listed so the sweep is complete.** (A) of rows 1132/1135 at beta <= 1/48 (strong coupling,
Dobrushin; gapped for U(1) and in 5D alike); row 1145's electric strip (spatial coupling at most c/(1+beta):
a strong-coupling zone, gapped for U(1) too); row 1143's weak-coupling end (Gaussian counts; row 1028 gives the
U(1) and 5D analogues, `FINISH.md` row 1028: D = ((d - 1)/2) log(beta n^(d-4)) + O(1), ARGUED there). These are not
selective, so they are outside the sweep. Rows 1145-1177 are equivalent forms of (W) (their own RESULT lines),
not facts.

## Item 9. Open selective statements on the record that would pass (5D) (not facts; listed because Item 2 points here)

- (DEC) of row 1018 (`gap-short-step-max.md` L327-342): Rbar(2l) <= Rbar(l)(1 - c_2 NA_l). OPEN. Row 1018's
  own table: false in five dimensions and in the frozen-slice model (d), "a proof of (DEC) must use the isotropic
  cell in four dimensions"; true and empty in (AH). So (DEC) is selective against (U1) only through NA and passes
  (5D), but it is empty in (AH) and must be joined with (FL).
- (FL) at the cell scale, same table: false in (AH) (the blocked field is abelian beyond the W length), holds at
  the bare scale in 5D. OPEN.
- (BUB) of row 1383 (in progress on worker 1): stated by row 1380 as selective by construction; its (5D) and (AH)
  tests are that row's job.
None of these is proved; none is counted as a survivor below.

## 10. Verdicts

| Statement (row) | Scale-free sum in D = 4? | Holds verbatim in (5D)? | Holds in (AH)? | Survives (5D) |
|---|---|---|---|---|
| 1141 (2): covariant energy >= c/(1+b+(log R)^(2/d)) | no (local; log R from a union bound) | yes, 6b -> 8b | yes at fixed kappa, constant e^(-2 kappa) delta_b (ARGUED) | no |
| 1141 (8): E lambda_x >= 1/(64(1+6b)) | no | yes, 6b -> 8b | yes at fixed kappa (ARGUED) | no |
| Lemma NAB (1018) | no (counts 2(D-1) plaquettes) | yes (218 -> 386; author's Remark (d)) | yes at the bare scale (row 1018 L340; ARGUED here) | no |
| Lemma FR, FR+ (1011, 1018) | no (pointwise) | yes, 6 -> 8 | yes, pointwise | no |
| Identity CUBE, Lemma SOFT (1016) | no (Haar on one 3-cube) | yes (author, L882) | yes | no |
| Corollary WN2 and rho (1013) | no (one-site Schwinger-Dyson) | yes; WN3 with beta/24; weak-coupling rho = 1 - 2/D (ARGUED) | identity yes; sign open in both | no |
| Proposition LF (1034) | no | yes | no (Higgs hopping not kept by the staple flow; ARGUED); zero gain anyway | no |
| Theorem BD (1034) | no (one face site) | yes, i = 1..4 | yes with the Higgs force in Psi_V (ARGUED) | no |
| M-C (1380) | no (its argued source is 1141 (2)) | yes (author's own verdict) | yes (ARGUED) | no |
| Theorem A, (GH2_2-MIX) at beta_L = 0 (1084) | 2D sum, not 4D | yes (2D sheets) | not needed | no |
| Proposition G1 (1128) | no (one link) | yes | yes | no |
| Lemmas S, S_n (1273) | no (finite volume) | yes, n = 4 | yes (row 1279) | no |
| Asymptotic freedom at small coupling (account; row 998) | **yes** (one-loop shell sum, log only at D = 4) | **no** (infrared free in 5D) | yes (b_0 = 7 down to the W mass; RECALLED count) | **yes** |

**Decisive outcome.** Of the selective facts on the record, exactly one survives (5D): asymptotic freedom at small
coupling, the account's one-loop step (Sussman and Alpoge on Balaban), which is not a lane result and which the
record already names as "the one selective fact that is provable today" (row 998 6b, `parts/gap.md` L45). It does
not survive (AH). Every selective fact proved in the lane (rows 1011, 1013, 1016, 1018, 1034, 1084, 1128, 1141,
1273) and M-C of row 1380 holds verbatim in five dimensions at weak coupling: each uses the dimension only through
the number 2(D-1) of plaquettes on a link or the existence of a 3-cube or a pair of planes, and none through a
scale-free sum. So **the lane holds no lane-proved selective fact that sees the scale.**

**Named seed.** The only survivor is asymptotic freedom itself, so the seed of a mechanism that passes (5D) is the
statement the record has had since row 998: carry the one-loop step from first passage through the band, a
(K-flow) statement with dressed moves (M-D of row 1380). This is not a new mechanism. To pass (AH) as well, the
class carried must contain a clause that excludes an adjoint condensate (row 1380 M-D). Lead-level reading
(ARGUED): add (5D) to the selectivity test, as row 1380 proposes; with it, every statement that reads only the
lattice-scale roughness of SU(2) (Items 1-7, 8b-8d) is a constraint, not a mechanism.

**What is not done.** No new attack (by the brief). The (AH) lines marked ARGUED are one-line arguments, not
written proofs; the b_0 = 7 count and the 5D infrared freedom are RECALLED, not rebuilt. No literature search
(row 1379 ran it for the programme). No numeric run. Checked by no one. Same-session time `date -u`: 2026-11-22T06:02Z.

RESULT: Row 1382 (Claude Opus 5.5 high, Mac mini worker 2, reading and short arguments, unchecked): of the selective facts on the record (row 1141 (2), (8); Lemma NAB; Lemma FR/FR+; Identity CUBE and Lemma SOFT; Corollary WN2 and rho; Proposition LF; Theorem BD; M-C; and from parts/gap.md Theorem A of row 1084, Proposition G1, Lemmas S and S_n), every one uses the dimension only through local counts (2(D-1) plaquettes per link, a 3-cube, two disjoint planes), none through a scale-free sum, and every one holds verbatim in five dimensions at weak coupling (and, at fixed kappa with degraded constants, with an adjoint Higgs factor; LF alone fails there, with zero gain anyway), so none survives (5D); the only survivor is asymptotic freedom at small coupling (the account's one-loop step on Balaban's RG, log sum only at D = 4, infrared free in 5D), already on record since row 998, and it does not survive (AH) (b_0 = 7, recalled). The lane holds no lane-proved selective fact that sees the scale; the seed is the (K-flow)/M-D carry of asymptotic freedom with a clause excluding an adjoint condensate. OPEN: (DEC), (FL) at the cell scale, (BUB), and the mass gap; the (AH) lines are ARGUED.
