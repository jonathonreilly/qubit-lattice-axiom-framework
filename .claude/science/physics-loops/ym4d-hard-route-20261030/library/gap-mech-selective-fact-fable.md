lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-26T08:48Z

# Row 1533: prove one selective fact (gap-mech-selective-fact-fable)

Started 2026-11-25T20:48Z (date -u). Pinned commit 27ac80562. Author run, unchecked. No commit, no push (relay copies the file).

## 0. Plan

1. Read the brief (FINISH row 1533), Proposition NEG (row 1386, `library/gap-mech-direction2-fable.md`) and the
   mechanism programme pointers. Record what NEG covers.
2. List candidate selective facts. Grep each against `library/open-core.md`, `library/gap-*.md`, `parts/gap.md`.
3. Attack one candidate at a time. After each: statement, argument, what failed, what is left.
4. If no fact is proved: state the strongest obstruction for an explicitly quantified family of candidates.
5. End with one RESULT line.

## Status log

- 2026-11-25T20:48Z file created; reading inputs.
- 21:01Z Section 1 written (sweep of candidates, each checked against the folder). Memory free 35 percent by
  memory_pressure: below the 50 percent rule, so no numeric job; all work by hand.

## 1. What the brief asks, and a sweep of candidate facts

**The three properties.** (a) order-one coupling, uniform in the box. (b) not lattice-local, not an identity.
(c) the proof reads d = 4 and the non-abelian group, and the statement or the step fails in 4D compact U(1),
5D SU(2), or 4D SU(2) with an adjoint Higgs field.

**Which unconditional tools give (a) and (b) at all.** I listed every tool I know that gives a statement at one
fixed beta, uniform in the box, about more than a bounded set of links. Each is group-blind and dimension-blind
in its proof. Sources are named; I did not re-read the papers in this session (recalled, unchecked).

| Tool | Non-local statement it gives at every beta | Reads d = 4? | Reads SU(2)? |
|---|---|---|---|
| Reflection positivity, transfer operator T >= 0 (Osterwalder, Seiler) | Z^z <= Z^0; positivity of every flux-sector trace | no | no |
| Perron-Frobenius for T | the vacuum is unique and centre-neutral at each finite box | no | no |
| Chessboard estimates (Froehlich, Israel, Lieb, Simon) | P(all of A excited) <= q^|A| | only in q | only in q |
| Perimeter upper bound on Wilson loops (Simon, Yaffe) | W(C) <= exp(-c |C|) | no | no |
| Centre sandwich (Mack, Petkova; Froehlich) | SU(2) loop <= Z_2 loop in a random background | no | centre only |
| Tomboulis-Yaffe inequality | loop <= power of (1 - twist ratio) | no | centre only |
| 't Hooft duality in exact form | linear relations and positivity among the 64 twisted sums | form only | centre only |
| Variational bounds on levels of T | upper bounds on gaps and tensions | no | no |

The selective statements that are proved at order-one coupling come from one-link or one-cube integrals
(Proposition NEG's class F_loc). So a selective non-local fact needs either a new non-local tool or a way to
pass a local selective number through a blind non-local tool without losing the reading. The second way gives
"selective by a constant" only (a chessboard bound with a 4D SU(2) value of q). I do not offer that as a
selective fact: the statement holds in every comparison model with another constant, so (c) fails.

**Candidates I derived before searching, and where each already sits.** Keyword counts were taken with
`grep -l -i -F` over `library/gap-*.md parts/gap.md`; I opened each cited passage.

| # | Candidate | Verdict | On file at |
|---|---|---|---|
| C1 | Spread a centre twist with fixed left and right multipliers and use Jensen, as for U(1); the mean of a plaquette after the map is a product of four corner cosines, not the cosine of a sum | no better than an area law for SU(2) | Proposition J, `gap-mini-branch-fable.md` L368-412 (row 1179, mine); JEN(ii) in `gap-invent-selective-check-astra.md` L47; field-dependent form row 1177 (33)-(35), `gap-solve17-astra62.md` L403-426 |
| C2 | For compact U(1) a twist equals a uniform flux pi/(n_mu n_nu) per plaquette, and Jensen gives a box-uniform bound in 4D | PROVED on file for U(1); restated in Section 2 at the seed's aspect | (BL-c) of row 1051 as checked at `gap-direction3-check-opus.md` L151; profile of row 1169 |
| C3 | The sum over twists with the sign (-1)^Pf(z) is a trace with a positive kernel (the SO(3)- global form, electric flux = magnetic flux) | identity, centre only; reads d = 4 in its form, not in a bound | idea 33 of row 876, `gap-brainstorm2-max.md` L186, L243 |
| C4 | For a twist with odd Pfaffian no flat SU(2) connection exists and the least action is bounded below uniformly in the box in 4D ('t Hooft's half-integer charge) | a classical statement: it holds at every beta but constrains no typical field, so (b) fails; no hit for "half-instanton", 3 files for "fractional charge" | not attacked |
| C5 | A box-uniform lower bound on the ratio Z^z/Z^0 for a single-plane twist of SU(2) | open; it is the family of (BS) of row 1175; if proved it would also hold for U(1) (C2), so it is not selective against U(1) | rows 1171-1177 |
| C6 | A faster-than-perimeter upper bound on large Wilson loops | selective against 4D U(1) at weak coupling (Guth; Froehlich, Spencer: perimeter lower bound) but it is of confinement strength | `parts/gap.md` test table |
| C7 | Deconfinement of the one-slice trace Tr(C_z T) at beta in [2, 3] | holds for U(1) and in 5D as well; not selective | Borgs-Seiler rows (33 files) |
| C8 | The three comparison models as one family: N_5 layers with coupling beta_5 (beta_5 = 0 is a product of 4D copies; N_5 = 1 is a group-valued adjoint Higgs field) | observation only; no theorem follows without clustering of a layer | "anisotropic" 83 files; I10, I11 of `gap-outside-box-max.md` |

**Reading of the sweep (ARGUED, mine).** The comparison models are softer than the target at long distance.
A lower bound on a long-distance quantity that is true for the target is then true for them too. So a
selective fact must be an upper bound on a long-distance quantity, one that a Coulomb phase violates. Sections 2
and 3 make this exact for one family and then attack the weakest member.

## 2. One family made exact: box-uniform bounds on twist ratios

- 21:04Z Sections 2 to 4 written.

**Setting.** Box n^3 x v, v = rho n, Wilson action, gauge group G = SU(2) or compact U(1) (with the twist -1 in
U(1)). z is a nonzero class in H^2 of the torus with Z_2 coefficients, and r_z = Z^z / Z^0. The seed is built from
the temporal classes: Z_+(v) = (1/8) sum over temporal z of Z^z(v). The family is

  T = { L(z, rho, c): "r_z >= c for every n" } and { U(z, rho, c): "r_z <= c for every large n" }, 0 < c < 1.

Each member meets (a) and (b): it is a statement at one beta, uniform in the box, about the trace of C_z T^v.

**Proposition TW (PROVED; part (i) restates (BL-c) of row 1051 as checked at
`gap-direction3-check-opus.md` L151, at the aspect of the seed; part (ii) is Proposition J of row 1179; part
(iii) is elementary).**

(i) For 4D compact U(1), every beta >= 0 and every box: r_z >= exp(- (pi^2 beta / 2) kappa(z, rho)), where
kappa is the sum, over the coordinate planes that z pairs with, of V / (n_mu n_nu)^2. This is rho for a spatial
plane and 1/rho for a temporal plane. At the seed's aspects, rho = 1/512 and 1/256, a temporal twist in one plane
has r_z >= exp(- 256 pi^2 beta) and exp(- 128 pi^2 beta), for every n. In d dimensions the same proof gives the
exponent (pi^2 beta / 2) n^(d-4) on a cube: uniform exactly at d = 4.

Proof. A twist pi on one stack of (mu, nu)-plaquettes and the uniform 2-cochain eps = pi / (n_mu n_nu) on all
(mu, nu)-plaquettes are both closed and have the same periods on every coordinate 2-torus. Their difference is
exact, so a shift of the link angles maps one twisted action to the other and Z^z = Z(eps). Then
r_z = < exp(beta sum_p [cos(theta_p + eps) - cos theta_p]) >_0, and Jensen gives the exponent
- beta (1 - cos eps) sum_p < cos theta_p > - beta sin eps sum_p < sin theta_p >. The last mean is 0 by the
symmetry theta -> - theta. Use < cos theta_p > <= 1, 1 - cos eps <= eps^2 / 2, and V plaquettes per plane
direction. Several planes add.

(ii) For SU(2) in every dimension, the same method with any fixed left and right multipliers gives no more than
r_z >= exp(- (1 - 2^(-1/2)) beta < w > N_perp), with N_perp the number of planes parallel to the twist, n^(d-2) on
a cube: an area law. The mean of a plaquette after the map is the product of four corner cosines times < w >,
not the cosine of a sum. (Proposition J, `gap-mini-branch-fable.md` L378-387, is stated and proved there for one
stack on a 4D torus. For other dimensions and classes I have only this session's blind argument, unchecked: a
plaquette whose corner product is within 1/50 of z_p has four corner frames aligned up to sign within the angle
pi/14; at a site, signs chosen along chains of at most seven such corners are consistent, so on those plaquettes
z is the coboundary of a link sign; hence z times that coboundary is a closed cochain of the same nonzero class
supported on the other plaquettes, and it meets each of the n^(d-2) parallel coordinate 2-tori that pair with z.
This gives the constant 1/50 in place of 1 - 2^(-1/2).)

(iii) So in T: every lower bound L(z, rho, c) with c <= exp(- (pi^2 beta / 2) kappa) holds for 4D compact U(1) by
proof and is not selective against it. Every upper bound U(z, rho, c) with a temporal z says that the odd electric
flux sectors keep weight at least (1 - c)/2 at time rho n. That is the negation of 't Hooft's flux criterion at
this aspect, so it is false for SU(2) if the target holds, and it is the expected truth in a Coulomb phase.

**Consequence (the obstruction for this family; (i) to (iii) PROVED, the last sentence ARGUED).** A true and
selective member of T for 4D SU(2) is a lower bound L(z, rho, c) with c above the true U(1) value of r_z at the
same beta. It is an upper bound on the weight of the odd flux sectors. No member of T that is weaker than "SU(2)
keeps less odd flux than the U(1) Coulomb phase" is selective. The method that proves the U(1) bound reads
commutativity, and reads it in the wrong direction: it is strong for U(1) at d = 4 and it gives only an area
law for SU(2) at every d. So the family holds a proved contrast between the two groups and between d = 4 and
d = 5, but the contrast favours U(1). This is not a selective fact about SU(2) in the sense of the brief.

**What this does not show.** It covers one family and one method. It does not bound r_z from above for U(1)
(the true Coulomb value is not proved on file at beta in [2, 3]). It says nothing about spatial twists of
SU(2), whose box-uniform lower bound is the open family of (BS), rows 1171 to 1177.

## 3. Attacks of this session that failed, with the point of failure

Each was one attempt at a statement with (a), (b), (c). None is new to the folder as an idea; I record the point
of failure so that the next row does not repeat it.

1. **Jensen spreading for SU(2) with a covariant map.** Tried: gauge transformations on the cover with
   omega(x + n e_1) = i sigma_1 omega(x), omega(x + n e_2) = i sigma_2 omega(x). The image fields obey a
   conjugation-twisted condition with one extra centre sign on the seam links, so the map sends periodic fields
   to periodic fields of the same class. No twist is produced. This is Lemma K4 of row 1051 again.
2. **Conjugation by a slowly varying SO(3) field.** The field needs a Z_2 vortex in each twisted plane (the
   SO(3) bundle with holonomies of angle pi about two axes has no section). The mean cost is the sigma-model
   energy of the field, at least of order n^(d-2) log n. Worse than the thin stack.
3. **Complex translations (McBryan, Spencer) for an upper bound on a Wilson loop or a flux weight.** The
   imaginary shift U -> U exp(a sigma_3) is allowed for entire observables. The first-order change of each
   plaquette is purely imaginary, so the cost is quadratic in the corner differences of a, as for U(1). The
   gain fails: exp(a sigma_3) has the eigenvalues e^a and e^(-a), and the gauge average of the loop keeps both,
   so the loop is not multiplied by a small factor. Same corner structure as Proposition J. On file as a
   recalled tool: `gap-global-reform-max.md` L151, L205, L593.
4. **Odd-Pfaffian twist at order-one coupling.** The classical statement (no flat connection; least action
   bounded below uniformly in the box in 4D, growing with the box in 5D, and zero for a single plane) reads
   both d = 4 and the group. I found no way to carry it to a statement about the Wilson measure at beta in
   [2, 3]: reflection positivity gives Z^(01)+(23) <= min(Z^(01), Z^(23)) only, and no sign for the ratio
   Z^(01)+(23) Z^0 / (Z^(01) Z^(23)). In the 2D Ising model the analogous ratio exceeds 1 at low temperature
   by an entropy factor of the diagonal wall (ARGUED from the wall count 4^n; not proved here), so no general
   inequality is available. Not on file under "half-instanton" (0 files); the classical fact is 't Hooft's.
5. **Positivity of the full Fourier transform of z -> Z^z over all six planes.** True for Z_2 and U(1) by the
   surface expansion. For SU(2) it is proved only for classes whose planes share an axis (a transfer operator
   exists). For the class (01)+(23) the weight is the mean of a sum of products of tanh(beta x_p) over closed
   surfaces under the cosh measure (the marked polynomial (M), `gap-crux-core-max.md` L107), and row 737 holds
   a surface with a negative character term (`gap-means-max.md` L78: negative at small beta when the Euler
   characteristic is odd, for example a projective plane). Not attacked further.
6. **A box-uniform bound on the thermal sum at fixed aspect.** It needs the finite-size correction of the free
   energy to be of order one, not of surface order. That is the gap itself, or conformal control. A free photon
   gas also has a bounded thermal sum at fixed aspect, exp(c / rho^3), so only a bound with a small constant is
   selective. That is the seed's kind (Section 2 reading).

## 4. Outcome

**No selective fact with the three properties is proved here.** What the session established:

- PROVED (assembled from on-file parts; the constants at the seed's aspect are new; the extension of part (ii)
  beyond 4D and one stack is this session's unchecked argument): Proposition TW. In the twist-ratio
  family every lower bound below exp(- (pi^2 beta / 2) kappa) holds for 4D compact U(1), every upper bound
  negates the flux criterion, and the multiplier method is box-uniform for U(1) at d = 4 only and area-law for
  SU(2).
- ARGUED: a selective fact must be an upper bound on a long-distance quantity (odd flux weight, thermal sum,
  loop beyond the perimeter law) that a Coulomb phase violates. Every unconditional non-local tool in the table
  of Section 1 gives lower bounds of this kind, or upper bounds that are blind. This is Proposition NEG's
  content seen from the side of the tools, not a new theorem.
- The one statement on file that meets (c) with content on typical Wilson fields is (6) of row 1530 (shell
  response, holds in check 1535). Its range R <= beta^(1/16)/8 fails (a). I did not improve its range.
- FAILED: the six attacks of Section 3.

**Open.** The seed (PUR-io); the mass gap; (BS); a box-uniform lower bound on any SU(2) twist ratio at
order-one coupling; a proved upper bound on the U(1) twist ratio at beta in [2, 3]; the sign of the
odd-Pfaffian ratio of attack 4.

**Suggested use by the lead (my judgement).** Do not queue another "prove one selective fact" row without a
new non-local tool. The cheapest test of a proposed tool is Section 2: ask whether it bounds the odd flux
weight from above, and where its proof fails for the uniform-flux U(1) computation of Proposition TW (i).

Finished 2026-11-25T21:04Z (date -u). No numeric run (memory free 35 percent, below the 50 percent rule). No subagents. Sources recalled and not re-read in this session are marked in Section 1.

RESULT: Row 1533 (Claude Fable 5.2 medium, Mac mini worker 1; author, checked by no one; no numeric run, no subagents). No selective fact with properties (a), (b), (c) is proved. PROVED, assembled from on-file parts: Proposition TW for the family of box-uniform bounds on twist ratios Z^z/Z^0: (i) for 4D compact U(1) every lower bound below exp(-(pi^2 beta/2) kappa) holds at every beta and box (uniform flux plus Jensen; kappa = 1/rho per temporal plane, so exp(-256 pi^2 beta) at the seed aspect; uniform exactly at d = 4), (ii) the same method gives only an area law for SU(2) (Proposition J of row 1179 in 4D, corner-cosine product; other dimensions and classes by an unchecked argument of this session), (iii) every upper bound in the family negates the flux criterion. So in this family the only selective true statements are upper bounds on the odd flux weight beyond the U(1) Coulomb value, and the proved group and dimension contrast favours U(1). ARGUED: every unconditional non-local tool listed (reflection positivity, Perron-Frobenius, chessboard, perimeter bound, centre sandwich, Tomboulis-Yaffe, exact duality, variational bounds) is blind or selective by a constant only. FAILED: six attacks (covariant spreading, SO(3) conjugation field, complex translations, odd-Pfaffian twist at order-one coupling, full Fourier positivity over six planes, box-uniform thermal sum); every candidate derived blind was already on file, anchors in Section 1. OPEN: (PUR-io), the mass gap, (BS), any box-uniform SU(2) twist-ratio lower bound at order-one coupling, a proved U(1) upper bound at beta in [2, 3], the sign of the odd-Pfaffian ratio.
