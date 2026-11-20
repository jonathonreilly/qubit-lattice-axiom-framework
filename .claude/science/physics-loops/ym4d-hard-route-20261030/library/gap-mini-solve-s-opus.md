lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T18:20Z

# gap-mini-solve-s-opus: the SU(2) mass gap, attack s (Opus 5.5 max, Mac mini worker 2)

Queue row 1228 of `FINISH.md`. Pinned at commit b34979e9a on branch `claude/ym4d-hard-route`.
Started 2026-11-20T06:20Z (date -u).

Labels: PROVED (written argument, checkable by hand), ARGUED (argument with a named gap), GUIDE (heuristic or numeric orientation, never a proof step), OPEN.

## Status

Step 0: file created. Reading the brief, FINISH.md rules, `parts/gap.md`, the RESULT lines of the earlier gap rows and `library/prior/gap-onebound-read-sol.md`.

## Step 0. Where the lane stands (record, not evidence; written 06:24Z)

Read: `GOAL.md`; `FINISH.md` L1-84, L299-360 and row 1228; RESULT lines of rows 1188-1225 (mini-solve a-r) and of
rows 1222, 1227, 1230; `library/gap-mini-branch-fable.md` L296-360 ((N-phys) and Theorem BP); `parts/gap.md` L1-60;
`library/gap-mini-solve-i-fable.md` L1-80 (screening table 1.2); `library/gap-mini-solve-p-fable.md` L250-300.

1. By Theorem BP (row 1179, check 1183) the only open lattice input of the Jaffe-Witten gap clause on the account's
   tr F^2 sector is (N-phys): at one physical side L, for every cutoff index j, the periodic centre-neutral excited
   trace of the cube n_j^3 at some time u_j <= n_j/K is at most 1/2. The other input is the continuum datum of the
   T0 chain (row 1225 Theorem E-N, unchecked composition).
2. In thermal words (rows 1180, 1184): the periodic box of side L at temperature K/L is on the confined side with a
   dilute neutral gas. Physically true for L large against the inverse glueball mass; false for small L.
3. Eighteen plain-brief rows (a-r) screened about fifty route families; every one is on the lane's map with a named
   failing step. Row 1224 (q) 8.4 recommends one precise question per row instead of a further screening.
4. Consequence for this row: no new screening. One precise question is chosen in Step 1, grepped against the record,
   and attacked to a proof or a counterexample.

## Step 1. How best to attack it (06:50Z)

**Judgement (ARGUED).** Every route on file ends at one kind of step: a selective inequality carried through the
band, where the running coupling is of order one. The only selective multiscale monotone in the literature is the
pinned-cell stiffness flow of OpenAI's 2D O(4) paper (row 1007 7.3; rows 1009-1016 read and port it). It works because
its twist is a global symmetry, so it acts on every pin, rough or not, and its direct cost is classical (row 1011
(M2)-(M3)). In 4D pure gauge theory the port fails at exactly that point: a twist applied to a rough pin has a
pin supremum that forgets colour coherence (row 1011 Proposition B, B'; row 1016 Theorem BH), there is no hidden
symmetry (Lemma CEN+), and any colour frame costs the non-abelian part of the pin (Lemma FR).

**The precise question of this row.** Proposition B concerns twists applied to the rough pins themselves. A cell of
a tiling has rough pins on its faces, but the twist need not live there. Put it on one face that is smooth: the
bottom face of a slab-shaped cell, pinned to a fixed abelian (here trivial) configuration, as in the
Schrodinger functional of Luscher, Narayanan, Weisz and Wolff. All other faces carry arbitrary pins. Then:

(Q-SF) Is the class of such cells closed under conditioning on the cell boundaries of a tiling, and does its
stiffness for a constant bottom twist have the two properties the 2D flow needs: a twist that is locally a
symmetry, and a start bound by dropping the covariance that is classical and uniform over the other pins?

Grep before work (06:45Z): `one smooth face`, `abelian bottom`, `smooth bottom`, `other faces arbitrary`,
`twist on one face`, `remaining faces` over `library/gap-*.md`: no hit on this class. Nearest on file: row 1011 4.7 (ii)
(all-abelian pins, not closed under conditioning); row 1195 (S1') (all-abelian pins); row 1202 (slab between two
trivially pinned plates, no tiling); row 1016 Lemma GT (Jacobian-one transports along curves). `library/open-core.md`
has no gap-lane entry for it.

Why either answer helps. If (Q-SF) holds, the 2D flow has a 4D gauge form with a class closed under conditioning,
and the next step is the variance gain (row 1011 (N3)). If it fails, the failure shows whether the obstruction is
the location of the twist (pins) or the interior non-abelian field, which sharpens row 1011 (N1)-(N3).

## Step 2. The plate class: what holds and where it fails

Notation of row 1011 3.1 (quaternions, t = Re, s = Im, w_p the tiling weights, strengths |beta_p| <= b). A cell is
c = {0, ..., R}^4 with coordinates (x_0; x_1, x_2, x_3). Its **plate** is the bottom face F_0 = {x_0 = 0}; its
**junction** is the edge set E = F_0 meet (union of the six side faces), a 2-dimensional surface. The class
**P_b** consists of all cells with the plate pinned to the trivial field (C_l = 1 for every link of F_0), and every
other boundary link pinned to arbitrary data omega. For x in F_0 put q_x = U_0(x), the link from (x, 0) to (x, e_0):
an integrated link ("plate spin") when x is not in E, a pin of a side face ("junction pin") when x is in E.

**Lemma P1 (rigid group of the plate; PROVED).** For g in SU(2) let omega^(g) be omega with every junction pin
q_x, x in E, replaced by g q_x. Then Z_c(1, omega^(g)) = Z_c(1, omega).
Proof. Let G = g on the sites of F_0 and 1 elsewhere. The plate field is fixed: g 1 g^(-1) = 1. Junction pins go to
g q_x, and the other pins are unchanged: a side-face link other than a junction pin has no end on F_0, or lies
in F_0. Change variables on the interior links with an end on F_0 (fixed left translations keep the Haar
measure); every plaquette trace is invariant. QED

**Lemma P2 (the twist and its cost; PROVED).** Let a be a unit imaginary quaternion, u a real function on the
sites of F_0, and T_eps omega the pin with q_x replaced by e^(eps u(x) a) q_x for x in E. Put
F(eps) = - log Z_c(1, T_eps omega) and H_c(u) = F''(0). Then for every real extension u~ of u to all sites of F_0:

  H_c(u) = sum_p beta_p w_p E[t_p] (Delta_p u~)^2 - Var(X),   X = sum_p beta_p w_p (Delta_p u~) a . s_p,

where p runs over the plate plaquettes p = (x; j, 0) (x, x + e_j in F_0, j spatial), Delta_p u~ = u~(x + e_j) - u~(x),
and s_p is the imaginary part of the holonomy q_(x + e_j) U_j(x + e_0)^(-1) q_x^(-1). Consequently:
(i) H_c(u) depends on u only through its values on the junction E;
(ii) H_c(u) <= b D_3(u), uniformly over all pins omega and all strength fields with |beta_p| <= b, where D_3(u) is
the minimum over extensions u~ of sum_p w_p (Delta_p u~)^2, the three-dimensional Dirichlet energy on the plate of
the harmonic extension of u|E;
(iii) a constant u costs nothing (Lemma P1).
Proof. Change variables q_x -> e^(eps u~(x) a) q_x on the plate spins (x not in E); Haar measure is kept. The plate
spins occur only in the plate plaquettes, with trace t(q_(x+e_j) W q_x^(-1)), W = U_j(x + e_0)^(-1), because the plate
link of p is 1. After the change the trace is t(e^(eps u~(x+e_j) a) M e^(-eps u~(x) a)) with M the old holonomy, which is
t(e^(eps Delta_p u~ a) M) since both factors are rotations about the same axis a. With t(e^(delta a) M) = cos(delta) t(M) -
sin(delta) a . s(M), F'' = - E[A''] - Var(A') gives the formula (signs of X do not matter in the variance). (i): two
extensions differ on plate spins only, which is a change of variables. (ii): drop the variance and use |t_p| <= 1.
QED

**Lemma P3 (closure and the exact Hessian; PROVED).** Tile c into cells c' of side R' dividing R and condition on
the links of the cell boundaries. The cells that meet F_0 are cells of P_b: their plate is F_0 meet c' (trivial),
their junction pins are the ring links q_x on the walls inside F_0 and the junction pins of c. With u~ any
extension of u to F_0, the law of total variance gives

  H_c(u) = E[ sum over c' meeting F_0 of H_(c')(u~ restricted to the junction of c') ] - Var( sum over c' of J_(c') ),

where J_(c') is the first derivative of the free energy of c' given its ring pins. Cells away from F_0 do not
enter. Proof: Markov property of the Wilson measure across pinned cell boundaries, Lemma P2 for each c'. QED

**What P1-P3 give.** The class P_b has the three properties that row 1016 6.2 asks for and that row 1016 found in
no candidate: (R-a) a rigid group acting by field-independent maps (Lemma P1); (R-b) charged pins in a class
closed under the conditioning used, here for the cells that carry the twist (Lemma P3; the junction pins are
charged because the side faces and the plate are one connected pinned component, Lemma REM); (R-c) the response
is a derivative of the Wilson free energy in a direction that changes the gauge orbit of the pin. It also has the
2D engine's free start bound (M3) in the form (ii), and the bracket (M6): plate spins are quaternion spins under
left multiplication, so Proposition W of row 1011 applies to rotations of the ring plate spins about a second
axis. This adds a candidate to row 1016 8.2 item 1 and 8.7 ("(R-a), (R-b), (R-c) together: no candidate", stated
there as "not found in the ten families"). It also narrows row 1202's table line 41 ("a class of pins that is closed
under conditioning carries no rigid group"): that holds if every cell of the tiling must lie in the class; P_b needs
only the cells that carry the twist, and the cells away from the plate are not in P_b.

**Where P_b fails (ARGUED; the scaling is a computation, not a theorem).** The 2D engine needs the twist cost to be
additive over the tiling and scale invariant: in 2D the cell Dirichlet energies of a smooth twist add up to the
square's, and a twist of angle theta costs order theta^2 at every side. In P_b neither holds for any normalisation.

1. The free bound (ii) is a three-dimensional Dirichlet energy on the plate. A twist whose junction values vary by
   theta has D_3 of order theta^2 R. So the bound grows with R. In this normalisation Gaussian U(1) also has a
   small stiffness ratio, H_c / (b D_3) <= C (1 + log R)/R (Proposition P5 (a) below), so a small ratio is not
   selective and cannot feed the 2D engine's step (M8) from small stiffness to decay.
2. The true response sees only the junction (Lemma P2 (i)), a 2-dimensional surface of codimension 2 in the cell.
   For Gaussian U(1) the gauge-invariant change of the pin is a boundary flux d_E u on the strip of side-face
   plaquettes along E, and the minimal Maxwell action with that boundary flux is of order b theta^2 log R
   (a strip source of lattice width on a face of side R; Fourier estimate, int dk_perp / |k| over |k_par| < 1/R).
3. Under the tiling of Lemma P3 into L^4 cells of side R' = R/L, the L^3 cells on the plate have junctions that
   include the walls inside F_0, which are not junctions of c. A smooth twist varies by about theta/L across each
   small plate, so their responses sum to about L^3 b (theta/L)^2 log R' = L b theta^2 log R', against
   b theta^2 log R for c. The variance in Lemma P3 must cancel all but a fraction 1/L of the cell sum. The 2D engine's
   gain is a variance lower bound with relative error of order B^(-N) against a gain delta of order (log L)/pi
   (row 1009 Step 3, (3.50)-(3.51)); here the same gain is a fraction delta/(h L) of the cancelled amount. A bound of
   Brascamp-Lieb type cannot resolve it.

So the plate supplies the rigid group, the charged pins and the bracket, and the induction fails at the geometry:
the gauge-invariant content of a plate twist lives on a junction of codimension 2, and a tiling creates new
junctions. Taken with row 1016 4.4 (a Dirichlet form of a link field is not scale invariant in d = 4) this is one
dimension count, stated here as a reading, not a theorem: a twist of a rigid q-form symmetry costs a Dirichlet
energy of a q-form, which is scale invariant when d = 2(q + 1); a bracket needs a non-abelian group, and
continuous symmetries of form degree q >= 1 are abelian (generalized global symmetries, Gaiotto, Kapustin,
Seiberg and Willett 2015; RECALLED). So in d = 4 the scale-invariant twist (q = 1, the U(1) one-form symmetry) has
no bracket, and the non-abelian twists (q = 0, or the plate group of P1) are not scale invariant. This is the
lane's sentence "U(1) has the twist with zero gain, SU(2) has the bracket with no twist" (row 1011) in counting form.

**Status of Step 2.** PROVED: Lemmas P1, P2, P3 (by hand, unchecked). ARGUED: the failure 1-3. The answer to (Q-SF):
closed under conditioning YES (for the twisted cells), twist locally a symmetry YES, free classical start bound YES
in the plate normalisation, but that normalisation is not scale invariant, and the scale-invariant response is
not additive. The 2D engine has no 4D form in P_b. (W), (N-phys) and the gap are not moved.

## Step 3. The non-additivity is exact in the comparison model (07:04Z)

This step turns failure points 2-3 of Step 2 into a theorem for Gaussian (non-compact) U(1), the model the
lane uses to test selectivity. Its free energy is quadratic in the pins, so the response is classical.

Setting. Cell c = {0, ..., R}^4, plate F_0, junction E, as in Step 2; tiling of c into L^4 cells c' of side R' = R/L.
The twist is the U(1) rotation of the junction pins by e^(i eps u(x)) with u(x) = theta x_1/R on E. In additive
notation A for the U(1) potential, the Gaussian weight is exp(-(b/2) sum_p w_p (dA)_p^2). For pin data p_0 put
E_c(p_0) = min over interior A of sum_p w_p (dA)_p^2. Then F_c(eps) = (b/2) E_c(eps-shifted pins) + const, so
H_c(u) = b E_c(shift data of u), where the shift data are u(x) on the junction temporal links and 0 on all other
boundary links. (Write the interior field as the minimiser plus a fluctuation; the cross term vanishes.)

**Proposition P5 (PROVED, Gaussian U(1)).** There is an absolute constant C such that for every R >= 2 and every
L >= 2 dividing R:
(a) H_c(u) <= C b theta^2 (1 + log R);
(b) for the tiling and the extension u~(x) = theta x_1/R on all of F_0, the bottom cells of Lemma P3 satisfy
    sum over c' meeting F_0 of H_(c')(u~ on the junction of c') >= (L - 1) b theta^2;
(c) hence, in Lemma P3, Var(sum of J_(c')) = sum E[H_(c')] - H_c >= (L - 1) b theta^2 - C b theta^2 (1 + log R).

Proof. (b) The fully pinned plaquettes of a cell enter E_(c') with their fixed values, so E_(c') is at least their
weighted sum. On a wall {x_2 = j R'} inside c (1 <= j <= L - 1) the plaquettes (x; 1, 0) with x_0 = 0 have the links:
plate link (shift 0), junction pins of the two cells at x and x + e_1 (shifts u~(x), u~(x + e_1)), the link at height 1
(a ring link, shift 0). Each is fully pinned in both cells beside the wall, with weight 1/2 in each, and its shift
flux is u~(x + e_1) - u~(x) = theta/R. There are at least R^2 of them per wall (x_1 in 0..R-1, x_3 in 0..R), and L - 1
walls in direction 2 (the same again in direction 3, not needed). Sum: at least (L - 1) R^2 (theta/R)^2.
(a) Gauge-transform the shift data by lambda = -u~ on the sites of F_0 and 0 elsewhere (A_l -> A_l + lambda(tail) -
lambda(head); a change of the interior variables; E_c is gauge invariant). The junction shifts cancel, and the new data
are theta/R on every 1-link of F_0, junction 1-links included, and 0 on every other boundary link. Competitor:
A_(x,1) = (theta/R) phi(x_0, x_2, x_3) on every 1-link, all other interior
links 0, with phi = 1 on x_0 = 0, phi = 0 at x_0 >= 1 on the side faces x_2 in {0, R} or x_3 in {0, R}, and on the top.
Then (dA)_p is non-zero only for p = (x; 1, m), m in {0, 2, 3}, where it is (theta/R) times a lattice difference of phi,
so E_c <= (theta/R)^2 R D(phi), with D the 3D lattice Dirichlet energy of phi on {0..R}^3. Take
phi = psi(x_0, d_2) psi(x_0, d_3) (1 - x_0/R), with d_i the lattice distance to the nearer i-face and
psi(t, s) = (2/pi) arctan(s/t) for t >= 1, psi(0, s) = 1. On the quarter-plane lattice {0 <= t, s <= R} the angular
function has |grad psi| <= C'/(1 + t + s) away from the corner link, so its Dirichlet sum is at most C''(1 + log R);
each psi(., d_i) is constant along one more coordinate (length R) and is used on two faces; |psi| <= 1 gives
|grad(fg)|^2 <= 2(|grad f|^2 + |grad g|^2); the factor (1 - x_0/R) adds at most C R. So D(phi) <= C R (1 + log R) and
E_c <= C theta^2 (1 + log R). (c) is Lemma P3 with (a), (b). QED

**What P5 says.** With the twist normalised by its scale-invariant size (the U(1) response, of order b theta^2
up to log R), the cells of a tiling carry at least (L - 1)/(C (1 + log R)) times the response of the whole cell.
The excess sits on the plate walls that the tiling creates (codimension 1 in the plate, like the true junction),
and the variance must remove it. In the 2D engine the matching excess is the ring bonds, a fraction O(1/R) of the
twist energy. So an induction of the 2D form in P_b must bound a variance of order L b theta^2 from below to an
accuracy finer than its gain delta theta^2, a relative accuracy delta/(b L); the 2D engine works with relative
errors B^(-N) against delta/h and needs L >= B^(10J) (row 1009, (3.50)-(3.53)). That this cannot be met is ARGUED,
not proved: P5 proves the size of the cancellation, not the absence of another inequality.

For SU(2) the same fully pinned wall plaquettes enter H_(c') with the factor t_p of the ring field, so the excess is
there whenever the ring plaquettes are near 1 (weak coupling). It is not a lower bound on H_(c') for SU(2): the
interior part of an SU(2) cell response has no sign.

## Step 4. The plate obstruction does not depend on the dimension (07:10Z)

A check of Step 2's dimension count. I first expected the plate class to be additive in d = 3 (the plate is then
2-dimensional, and its free bound (ii) is a scale-invariant 2D Dirichlet energy). It is not. ARGUED below by the
classical (tree-level) count; the 4D case is the theorem P5.

**Squeezing (ARGUED, classical U(1) count, every d >= 2).** Let the plate twist change the holonomy across a cell of
side R by theta, with the top of the cell pinned. The response field is an electric field of size theta/R^2 over the
whole height, with energy b theta^2 R^(d-4). After a tiling into cells of side R' = R/L, a bottom cell has its top on a
ring at height R', pinned inside the cell, and a holonomy change theta/L across it. Its field is
(theta/L)/R'^2 = L theta/R^2, L times stronger, over a layer that is 1/L of the height. The L^(d-1) bottom cells
together carry L^(d-3) b theta^2 R'^(d-4) = L b theta^2 R^(d-4): L times the response of the whole cell, in every d.
In the 2D engine no squeezing occurs: the twist rotates every spin, ring spins included, so each cell sees the
local gradient and the cell energies add up.

**The dichotomy (ARGUED).** To avoid squeezing, the extension of the twist must rotate the rings above the plate
consistently. The only rigid maps there are gauge transformations G = e^(u~ a) applied at all heights. They make the
top and bottom of each bottom cell consistent, but they rotate the side rings of the cells by a non-constant G,
which is the twist of rough pins of Proposition B (row 1011), with its mass-like cost. So a plate twist is either
squeezed (non-additive by a factor L, Proposition P5 for 4D U(1)) or applied to rough pins (Proposition B). The 2D
engine needs a rigid group that acts on all integrated variables, and pure lattice gauge theory has none in any
dimension (Lemma CEN+ of row 1016).

Correction to Step 2. The remark there on the dimension count of form symmetries stands as a reading about bulk
symmetries. It does not single out d = 4 for the plate class: the plate class fails in every dimension, by the
squeezing above, and in 4D by P5.

