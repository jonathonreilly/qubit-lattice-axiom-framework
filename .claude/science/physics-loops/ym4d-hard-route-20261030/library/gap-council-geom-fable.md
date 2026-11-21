# Gap council, geometry seat (FINISH row 1129)

Seat: geometric analysis of gauge fields. Model: Claude Fable 5.2, max effort, laptop subagent.
Blind to the other council files. This file is written in stages.

## Plan (five steps)

1. Read `library/gap-council-brief.md` in full. State the obstacle of its Section 3 in the terms of geometric analysis: the object, the nearest known theorem, the line where that theorem stops.
2. Propose at most three attacks, ranked. For each: mechanism, exact first statement, the three failure lines of Section 4, nearest item of Section 5, cheapest decisive test.
3. Attempt the first statement of the top attack now. End at a proof, a counterexample, or a named failing line.
4. Only then read `parts/gap.md` (crux, route registry, test table, methods set aside 1 to 34) and the FINISH RESULT lines it cites. Mark each attack new or already tried, with its row.
5. Write one RESULT line.

Status marks used below: PROVED, ARGUED, GUIDE, OPEN.

## Step 1. The obstacle in the terms of geometric analysis

Source read: `library/gap-council-brief.md`, all seven sections. No other lane file was read before step 4.

### 1.1 The object

- By (TM) each periodic cube has a positive transfer operator T = exp(-a H). In my field H is a Schrodinger operator on the orbit space B_L = A_L / G_L of SU(2) connections over the 3-torus of side L:
  H = -(g^2/2) Laplacian_B + (1/(2 g^2)) int |F_A|^2.
  The wall asks for z(L) = L gap(H_L) to be unbounded, flux sectors included, while one Casimir energy stays bounded. ARGUED (this is the continuum reading; the lattice statement is the brief's).
- The flux part is a statement about one topological boundary condition. Let Theta be one centre flip of (TM-c). Put Z = Tr T^L, Z_tw = Tr(T^L Theta), R = Z_tw / Z. Z_tw is the partition function with one 't Hooft twist ('t Hooft 1979). With P_+- = (1 +- Theta)/2 and Z_+- = Tr(T^L P_+-):
  Z_- / Z_+ = (1 - R) / (1 + R). PROVED (two lines: Z = Z_+ + Z_-, Z_tw = Z_+ - Z_-).
  So "the lowest flux gap times L is large" says R(L) is close to 1. The measure must forget a twist.
- The twisted sector has a classical vacuum of zero action. Take U = i sigma_1 on the 1-links of one slice x_1 = 0, U = i sigma_2 on the 2-links of one slice x_2 = 0, and U = 1 elsewhere. Every plaquette is +1 except the plaquettes at (x_1, x_2) = (0, 0), which are -1. PROVED (direct product of four links). Hence Z_tw is the partition function of the same local action with fields periodic up to Ad(i sigma_1), Ad(i sigma_2) ('t Hooft's twist eaters; Gonzalez-Arroyo, van Baal). The twist costs entropy only. This is special to a non-abelian group. For U(1) a half-unit flux costs action of order 1/e^2 at every size.
- Geometric reading. Translations by L act on the orbit space of the torus of side 2L. Their fixed set is the disjoint union of the periodic and the twisted orbit spaces of side L (equivariant connections on a cover are connections on the quotient, one component per twist class). ARGUED (standard for bundles; not written out on the lattice). So R compares the weight of two components of one fixed set.
- The doubling defect sees the same numbers. Let Gamma be the group of the three centre flips that commute with T, and R_k = Z_k / Z for k in Gamma. Then
  Z(2 L_1) <= (1/8) sum_{k in Gamma} Z_k(L_1)^2, so 2 F(L_1) - F(2 L_1) >= log( 8 / sum_k R_k^2 ) >= 0. PROVED (Tr A^2 <= (Tr A)^2 in each of the eight sectors, then Parseval on Gamma).
  A small one-direction doubling defect eps forces 1 - R_k^2 <= 8 eps for every k. So (CAS) contains the flux statement. The converse is the hard direction.

### 1.2 The nearest known theorems and where each stops

(a) Uhlenbeck 1982 (Coulomb gauge, removable singularities, weak compactness). If int_B |F|^2 < eps_0 on a 4-ball, a Coulomb gauge exists with ||A||_{W^{1,2}} <= C ||F||_{L^2}. Balaban's small-field regions are the lattice form of this hypothesis. The theorem stops at the line "int_B |F|^2 < eps_0". At first passage a block violates it with probability of order exp(-c / g^2(L)), and that is not small when g(L) is of order one. This is the same line as the brief's "first passage". ARGUED.

(b) Yang-Mills gradient flow. On the lattice the flow exists for all time and for every configuration, with no small-field condition. In the continuum: Struwe 1994, Waldron 2019 (global existence in 4D), Luscher 2010 and Luscher-Weisz 2011 (flowed observables need no new renormalization, to all orders), Cao-Chatterjee 2021 and 2023 (flow trajectories as a state space in 3D; random distributional data). The flow smooths without a large-field problem. It stops because it is a first-order transport of the measure and no functional of the transported measure is known to be monotone. Hamilton's and Chen-Shen's monotone quantity (T - t)^2 int |F_t|^2 G_{T-t} becomes, under translation invariance, (T - t)^2 <E_t>, and its monotonicity is then only the trivial statement that <E_t> decreases. ARGUED (one line: int G = 1).

(c) Curvature of the orbit space. Singer 1981: by O'Neill's formula the sectional curvature of B is K(X,Y) = 3 <[X,Y]^v, G_A [X,Y]^v> >= 0. It vanishes identically for an abelian group. Bakry-Emery or Lichnerowicz would turn a Ricci bound into a gap. It stops at two lines. The Ricci trace diverges and has no uniform lower bound in units of 1/L. The potential int |F|^2 is not convex; its Hessian d_A^* d_A + ad(F) carries the same bracket with the bad sign. This is the brief's route RF.

(d) Atiyah-Bott 1983, Witten 1991 (2D). The Yang-Mills functional on a surface is equivariantly perfect and the partition function is Migdal's sum over representations. The 2D gap is a Casimir value and holds for U(1) too. So the 2D mechanism is not selective. In 4D there is no localization. Instanton calculus (Atiyah-Hitchin-Singer, Taubes; fractional instantons on twisted tori) is valid only below first passage.

(e) Gribov 1978; Zwanziger 1982-1994; Dell'Antonio-Zwanziger 1991; Semenov-Tyan-Shanskii and Franke 1982; van Baal 1992. The fundamental modular region of the Coulomb or Landau gauge is convex and bounded in every direction for a non-abelian group. For U(1) the Faddeev-Popov operator does not depend on the field and there is no horizon. This is a selective kinematic fact at every coupling. It stops because it bounds gauge-fixed fields, not the spectrum: Payne-Weinberger and Andrews-Clutterbuck need a diameter in the kinetic metric and a convex potential.

(f) Chatterjee 2021 ("A probabilistic mechanism for quark confinement"). For a group with non-trivial centre, exponential decay uniform in the boundary condition gives the area law. So the flux part of z^- follows from mixing that is uniform in boundary conditions. The theorem stops at its hypothesis, which is the wall.

### 1.3 The line where my field stops, in one statement

Every theorem above is of one of two kinds. Kind (i) expands around a classical solution and needs int_block |F|^2 small against eps_0, so g^2(L) small: Uhlenbeck, Taubes, instanton calculus, Balaban. Kind (ii) is kinematic, holds at every coupling and is silent on the measure: existence of the flow, boundedness of the modular region, O'Neill's curvature, twist eaters. The wall is the absence of a statement of kind (ii) that controls a spectral quantity. The three selective facts of kind (ii) (bracket curvature, horizon, zero-action twist) are the material for step 2.

## Step 2. Three attacks, ranked

Notation. r(L) = Z_tw(L) / Z(L) is the twist ratio of step 1.1 on the symmetric torus, rho = (1 - r)/(1 + r) = Z_- / Z_+, F_v = -log r is the vortex free energy. D denotes a Casimir factor log(Tr T^n / lambda_0^n).

A remark that orders the three attacks (ARGUED). The comparison models of Section 4 split by sector. A frozen finite group has a gap in the zero-flux sector and fails only in the flux sectors. A product with a massless factor passes every flux test, because the centre flips read only the SU(2) factor; it fails only in the zero-flux sector. Compact U(1) at weak coupling fails in both. So no statement that reads only flux ratios can fail for the product, and no statement that reads only the zero-flux sector can fail for Q_8. A selective input is therefore two inequalities with different kill sets, or one inequality that couples the sectors. Attack 1 takes the flux half. Attack 2 takes the zero-flux half. Attack 3 is a tool for clause (L3). ERRATUM (added in step 4): the sentence about frozen groups is right for Z_2 and wrong for Q_8 and the binary tetrahedral group; see 4.2.

### Attack 1 (top). TWIST: the flux half as growth of the twist ratio, with twist eaters

Mechanism. For SU(2) the twisted torus has a vacuum of zero action (step 1.1). So F_v(L) is an entropy, not an energy. It is the cost of closing a tube: weaken the sheet S of twisted plaquettes to coupling s beta, 0 <= s <= 1. At s = 0 the sheet is a tube of deleted plaquettes and the twist is invisible, so the ratio is exactly 1. Hence F_v(L) = beta |S| int_0^1 Du_L(s) ds, where Du_L(s) is the difference of the mean sheet plaquette between the periodic and the twisted sector at sheet coupling s beta. This is thermodynamic integration (de Forcrand, D'Elia, Pepe 2001) and the tube is the vortex container of Mack and Petkova 1980. In the plane of the twist, reflection positivity makes r grow under doubling. In the two sheet directions r can fall. The attack is to prove that the gain beats the loss from a seed r_1 that is a moderate number (about 0.2 to 0.5, not exp(-30)), and to carry r from first passage to r_1 through a bounded number of doublings. The carry is a (K-flow) statement: at first passage the account gives r as a one-loop determinant ratio around an isolated vacuum.

First statement (TW-1), in two parts.
(a) For all sizes L_1,...,L_4, all beta > 0 and every twist plane: with time in a direction of the twist plane, rho(2 L_1) <= rho(L_1)^2 exp(2 D_+), where D_+ = log(Z_+(L_1) / lambda_0^{L_1}); with time in a sheet direction, r(2 L_3) >= r(L_3)^2 exp(-2 D_tw), where D_tw = log(Z_tw(L_3) / (lambda_0^tw)^{L_3}).
(b) (TW-GROW, the selective clause.) There are r_1 < 1 and c > 0 such that for every dyadic physical size L between first passage and the first size with r(L) >= r_1: r(2L) >= (1 + c) r(L).

Failure lines. Compact U(1) at weak coupling: (b) fails; the half-flux ratio is a quotient of theta functions of e^2 and does not depend on L, so r(2L) = r(L) up to exponentially small monopole terms. Product with a massless factor: (a) and (b) both hold if they hold for SU(2); the attack fails as a whole at the line "(Z-UNB) includes the zero-flux sector", which it does not touch. This is by design, see the remark above. Frozen Q_8 and the binary tetrahedral group: (b) fails; twist eaters lie in Q_8, so the twisted sector also has zero-action vacua, and r(L) tends to a ratio of two counts of flat connections, a constant below 1. Frozen Z_2: r tends to 0 (no twist eaters, area law for the sheet).

Nearest item of Section 5. Route RG (hierarchical comparison; Tomboulis 2007 claimed (b) by Migdal-Kadanoff interpolation, and Ito and Seiler 2007 showed the gap in it), and Lemma SHEET (row 996). It differs in three ways. It uses no decimation. It is not uniform over plaquette coupling fields: only the one-parameter family s on one sheet appears, and only as an exact identity. The seed r_1 is a moderate number.

Cheapest decisive test. Evaluate the "ideal" doubling map that (a) gives when all Casimir factors are 1, find its threshold, and compare with published twist ratios in the window (Kovacs-Tomboulis 2000; de Forcrand-von Smekal 2002). If the threshold is far above the measured r at every size below the seed size of (Z-SEED), the flux half gives nothing new. If it is reached within one or two doublings of first passage, the flux half of the seed moves down by a large factor. Hand work plus reading; no new run is needed.

### Attack 2. HELIX: the Gribov horizon as a selective kinematic inequality for the zero-flux half

Mechanism. In the minimal Coulomb gauge on a time slice the fundamental modular region is the orbit space B_L in coordinates. At a minimum of the gauge-fixing functional the Faddeev-Popov form is non-negative: for every Lie-algebra-valued omega,
Q_U(omega) = sum_{x,mu} [ (u_0/8) |omega(x) - omega(x+mu)|^2 - (1/4) u . (omega(x) x omega(x+mu)) ] >= 0, where U_mu(x) = u_0 + i u . sigma.
The cross-product term is the bracket. It is absent for U(1). Testing Q_U on one plane wave and taking the Schur complement against all others gives the horizon inequality (Zwanziger 1991-1994): the field amplitudes in B_L are bounded mode by mode. A free massless gluon of strength g^2 violates the bound once (3 g^2 / (16 pi^2)) log(L/a) > 1 (Gribov's 1978 gap equation, read as an inequality). So the massless branch is excluded kinematically beyond an explicit scale, at every coupling. The attack is to turn this into the selective clause of the zero-flux half: a dimension-free Poincare bound on the convex bounded region (Payne-Weinberger 1960 in the log-concave form) applied to block modes at one scale in the band.

First statement (HX-1). For every finite periodic lattice, every U at a local minimum of F_U(g) = sum_{x,mu} (1 - (1/2) tr(g(x) U_mu(x) g(x+mu)^*)) at g = 1, every non-zero lattice momentum k and every orthonormal colour pair (e_1, e_2): with omega_k = e_1 cos(k.x) + e_2 sin(k.x) and P the projector off omega_k and off the constants, Q_U(omega_k) >= <M omega_k, (P M P)^+ M omega_k>, where M is the matrix of Q_U. Second statement (HX-2, the open one): there is a number h > 0 such that the Wilson measure in the band gives the lowest block mode a variance at most (1 - h) times the free massless value, and (1 - h) feeds a Poincare bound.

Failure lines. Compact U(1): the cross product of two vectors in a one-dimensional Lie algebra is zero, so Q_U has no field-dependent term at second order and HX-1 holds trivially with no content; HX-2 is false (the photon has the free variance). Product with a massless factor: HX-1 constrains only the SU(2) coordinates; the Poincare step needs a bounded region in every direction and the photon directions are unbounded; it fails at "diameter finite". Frozen Q_8 and the binary tetrahedral group: there are no infinitesimal gauge rotations, so the Hessian Q_U and the horizon do not exist; the attack fails at its first line. A selective statement of this kind is silent on the flux sectors, which is where these models fail; it needs Attack 1 beside it.

Nearest item of Section 5. Route RF (functional inequalities from small-field convexity). It differs in the source of convexity: the region is convex and bounded at every coupling (Semenov-Tyan-Shanskii and Franke; Dell'Antonio and Zwanziger), and the action is not asked to be convex. The price is the non-convex potential, which Payne-Weinberger does not allow; that is the line where I expect it to stop.

Cheapest decisive test. On a 4^3 or 6^3 slice in the window, fix the minimal Coulomb gauge by repeated relaxation from many starts, and histogram the lowest plane-wave amplitude against (i) the free value and (ii) the horizon bound from HX-1. If the measured variance sits at the free value with the horizon far away, the horizon does not bite in the band and the attack is dead. Memory is a few megabytes. GUIDE only.

### Attack 3. FLOW-PIN: gradient-flowed boundary data to cut clause (L3) to finite dimension

Mechanism. Clause (L3) fails because the space of boundary conditions of a cell has a diameter that grows with the boundary area: a response bound per boundary link, summed along a path between two rough boundary fields, is not small. The Yang-Mills gradient flow of the boundary field for flow time t = (c L)^2 is defined for every configuration. After the flow the boundary field has curvature bounded at the scale of the cell, and Uhlenbeck's gauge theorem then puts it within a fixed distance of the trivial connection on the boundary of a cube, which is simply connected. So flowed boundary data mod gauge form a set of bounded diameter and finite metric entropy at each resolution. The attack is to prove (L3) only for observables and boundary conditions that factor through the flow at scale cL, and to leave the rough part to the account, whose ultraviolet control is exactly a statement that fields below the scale of the cell decouple.

First statement (FP-1). For every cell of side L, every pair of boundary fields U, U' on its boundary and every flow time t >= (c L)^2: there is a gauge transformation g of the boundary with dist(V_t(U)^g, V_t(U')) <= K(c), where V_t is the lattice gradient flow of the boundary action and K(c) does not depend on L, on the lattice spacing or on U, U'. Second statement (FP-2, open): the law of the interior, conditioned on the boundary field, depends on it through V_t(U) up to an error that the account bounds.

Failure lines. Compact U(1): FP-1 holds (heat flow); the attack fails later, at the response bound itself, which has no bracket gain. Product with a massless factor: FP-1 holds for each factor; the response bound reads the SU(2) pin only; fails at (L3) for the photon observables. Frozen Q_8 and the binary tetrahedral group: there is no gradient flow on a finite group; fails at the first line.

Nearest item of Section 5. The pinned-cell criteria (rows 845-896, 1115-1123) and (T-pin) clause (L3). It differs by restricting the class of pins to flowed data, so that the path length in (L3) is bounded by geometry instead of by a uniqueness clause.

Cheapest decisive test. FP-1 is false if the flow has an L-independent supply of non-trivial stable critical points on the boundary 3-sphere at scale L. On the lattice, flow 100 random boundary fields of a 6^4 cell and record the action at t = (L/2)^2. A broad distribution kills FP-1. A few megabytes. GUIDE only.

## Step 3. Attempt on the first statement of Attack 1 (TW-1)

Setting. A periodic lattice of sides L_1,...,L_4. One twist in the plane (1,2). "Plane directions" are 1 and 2. "Sheet directions" are 3 and 4. Inputs: (TM) and (TM-c) from the brief. One more input is used and is only ARGUED here: (TM-tw), the box with a twist in a spatial plane also has a positive trace-class transfer operator. Reason: in the thin-vortex form the twist flips the sign of the coupling on a line of spatial plaquettes; this changes the multiplication operator and not the kinetic kernel.

### 3.1 Part (a) is PROVED

Lemma T1 (plane direction). Let time run in direction 1. Let T >= 0 be the transfer operator of the cross-section, Theta the centre flip of direction 2, Z_+-(n) = Tr(P_+- T^n), lambda_+ the top of the spectrum of T on the even sector, D_+(n) = log(Z_+(n) / lambda_+^n) >= 0. Then rho(2n) <= rho(n)^2 exp(2 D_+(n)).
Proof. T commutes with Theta, so P_- T^n is a positive trace-class operator. For a positive trace-class A, Tr A^2 <= (Tr A)^2. Hence Z_-(2n) <= Z_-(n)^2. Also Z_+(2n) >= lambda_+^{2n}. Divide. PROVED.

Lemma T2 (sheet direction). Let time run in direction 3. Let S and S' be the transfer operators of the periodic and of the twisted spatial torus, mu' the top eigenvalue of S', D_tw(n) = log(Z_tw(n) / mu'^n) >= 0. Then r(2n) >= r(n)^2 exp(-2 D_tw(n)), and r(2n) <= r(n)^2 exp(2 D_per(n)).
Proof. Z(2n) = Tr S^{2n} <= (Tr S^n)^2 and Z_tw(2n) = Tr S'^{2n} >= mu'^{2n}. Divide. The upper bound is the same with the roles exchanged. PROVED, given (TM-tw).

Lemma T3 (exact bookkeeping). For every L, with Phi_4 the doubling defect of the brief and Phi_4^tw the same expression with twisted partition functions:
F_v(2L) = 16 F_v(L) - ( Phi_4(L) - Phi_4^tw(L) ).
For one direction: log r(2 L_mu) = 2 log r(L_mu) + delta_mu^per - delta_mu^tw, where delta = 2 F(n) - F(2n) in each sector.
Proof. Write out log r = F_tw - F at both sizes. PROVED (one line).

Lemma T4 (thermodynamic integration; after de Forcrand, D'Elia and Pepe). Let Z(s) be the periodic partition function with coupling s beta on the plaquettes of the sheet S, and r(s) = Z(-s)/Z(s). Then r(0) = 1, r(1) = r and
F_v = beta |S| int_0^1 Du(s) ds, Du(s) = u_per(s) - u_tw(s),
where u_per(s) and u_tw(s) are the means of (1/2) tr U_p over the sheet in the periodic and in the twisted sector at sheet coupling s beta.
Proof. d/ds log Z(s) = beta sum_{p in S} <(1/2) tr U_p>_s. The measure at -s is the twisted measure at +s after the centre change of variables, with the sign of the sheet plaquettes reversed. PROVED. (That r(s) <= 1 for 0 <= s <= 1 is ARGUED: the weakened slab operator is still positive for s >= 0.)

### 3.2 The ideal map and its threshold

If every Casimir factor is 1, T1 gives rho -> rho^2 in a plane direction, which reads r -> psi(r) = 2r / (1 + r^2), and T2 gives r -> r^2 in a sheet direction. Doubling the two plane directions first and then the two sheet directions gives G(r) = psi(psi(r))^4.

- G(0.1) = 0.0211 < 0.1 and G(0.5) = 0.906 > 0.5. PROVED (hand arithmetic: psi(0.5) = 0.8, psi(0.8) = 0.9756, fourth power 0.906).
- G has a repelling fixed point r* = 0.1991 (GUIDE: bisection, script `ideal_and_counts.py` in the session scratchpad). Above r* the ideal map runs to 1. Below r* it runs to 0.
- So the flux half has a seed that is a moderate number: r(L) above about 0.2, plus Casimir factors close to 1. In the ideal case rho <= 0.67 is enough. Compare the size of the zero-flux seed, z larger than 256 D_0 + 30. ARGUED.
- Limit of the lemmas. With Casimir factors bounded by D_0 > 0 and not tending to 0, T1 and T2 give a fixed point below 1, so a uniform lower bound on the flux gap in units of 1/L, not an unbounded one. Unboundedness still needs the Casimir factors to tend to 1. PROVED (G_D(1) = exp(-6 D) < 1).

### 3.3 The comparison models, computed

- Frozen Q_8 as beta tends to infinity: r tends to the ratio of the numbers of twisted and periodic flat 4-tuples, 96 / 736 = 3/23 = 0.130. PROVED by a finite count (twisted: 24 anticommuting pairs times 4 central pairs; periodic: 16 + 3 (4^4 - 2^4) = 736). The same script confirms it.
- Frozen binary tetrahedral group: 96 / 5856 = 1/61 = 0.016. GUIDE (script count; not redone by hand).
- Both lie below r* = 0.199. Both have Casimir factors far from 1 (degenerate vacua), so the ideal map does not apply to them; their r is constant in L. This is the line where they fail (b).
- Compact U(1) at weak coupling: the half-flux ratio is theta_2-type over theta_3-type in q = exp(-(2 pi)^2 / (2 e^2) x aspect), scale invariant on symmetric boxes. ARGUED (Gaussian sector; monopole corrections are exponentially small). It fails (b) with r(2L) = r(L).
- SU(2) below first passage: the twisted vacuum is isolated and the periodic vacuum has the toron valley, so r is a positive power of g(L) and is small. ARGUED (zero-mode count; the power was not fixed here). So SU(2) starts below r*, like the frozen groups, and must cross it. The frozen groups never do.

### 3.4 Part (b): the named line where the attempt stops

By Lemma T3, (TW-GROW) at size L is the same statement as
Phi_4(L) - Phi_4^tw(L) >= 15 F_v(L) + log(1 + c). (TW-line)
In words: the periodic box must have a larger doubling defect than the twisted box, by 15 vortex free energies. Below first passage this holds for a clear reason: the periodic box has the toron valley and the twisted box does not, so the periodic box has more light states. In the band I have no tool for (TW-line). Reflection positivity gives T1 and T2 and nothing more: T2 loses exactly D_tw, and an upper bound on D_tw relative to D_per is again a comparison of boundary conditions at one scale. The attempt stops at (TW-line). OPEN.

What the attempt does give. (i) PROVED: T1 to T4. (ii) A new form of the flux half: it is a statement about the difference of two doubling defects, the object the lane already studies, and its seed is a moderate number. (iii) A sharp reading of the kill tests: the frozen groups and SU(2) at first passage are on the same side of r*; the selective content of the flux half is the crossing of r* and nothing else.

## Step 4. Comparison with the lane (read only after step 3)

Read now: `parts/gap.md` (Formulation, Hardest open obligation, Routes tried with the methods set aside 19 to 34, Route registry, Test table, The exact price; the Obligations lines that mention twists, vortices, Gribov, flux sectors and Chatterjee), the table of methods 1 to 18 in `library/gap-crux-exercise2-max.md` 6a, and the RESULT lines of FINISH rows 731, 734, 930, 1004, 1018, 1025 and 1032, with ideas B8, B9, B11 of `library/gap-afield-b-max.md`. Not read: the other council files; the body of most cited files.

### 4.1 Marks

| Attack | Mark | Rows | What is the same | What differs |
|---|---|---|---|---|
| 1 TWIST | already tried, in every main part | 731 (flux half; Theorem EV-L, Proposition CL, Theorem S-w), 783 and 930 (twist ratio, odd weight p = (1 - r)/2, frozen ratios), 1004 (Theorem TW-T = (TM-tw); Lemma TW), 1018 ((T-vor), Lemma PAR, Corollary MP after Mack and Petkova; Lemma ADD), 1025 ((TB)_n; Lemma FAC: the line reads one factor), 1127 (sheet sums); methods 4, 13, 17 | the object, the flux half, the container, the one-factor reading, the stop at a comparison of two boundary conditions at one scale | three small items not found by search: the ideal map and its threshold r* = 0.199; the form (TW-line); guide numbers for r on symmetric tori (section 4.3) |
| 2 HELIX | already tried | 1032 (B8: convex modular region and Faddeev-Popov weight, with Payne-Weinberger and Brascamp-Lieb, FAILS; B9: horizon condition, no consumer, FAILS), 1042 (Coulomb frame, Lemma UNIQ), 1063 (Gribov reading CONTESTED) | the source, the consumer (a volume-free Poincare bound), the stop (non-convex Wilson weight; no implication from the horizon to gauge-invariant decay) | HX-1 isolates the cross-product term, which is exactly zero for compact U(1) on the lattice. Lemma FP-U1 of row 1032 (the U(1) gain from the cos(theta) conductances) therefore does not kill HX-1 itself. The verdict "no consumer" of B9 stands unchanged, so this does not reopen the idea. |
| 3 FLOW-PIN | new as a device, not as a mechanism | nearest: 1005 topic F and 1032 B11 (the flow as a monotone: "renames (CAS)"), 1011, 1016 (Lemma CEN+), 1042, 1122, 1123 ((L3)); method 34 | Uhlenbeck's gauge and the flow are on file; (L3) is on file | no row uses flowed boundary data to bound the path length in (L3). But see 4.2: its first statement is expected false in the worst-case form, and the in-law form is method 34. |

### 4.2 Corrections to my own steps after the reading

- ERRATUM to the remark at the head of step 2. The test table says that frozen Q_8 and 2T fail the even-sector statement too in the frozen limit: the frozen transfer operator has at least two centre-even flat states at every box (check 884). My sentence "a frozen finite group has a gap in the zero-flux sector" is right for Z_2 and wrong for Q_8 and 2T. So the split of kill sets holds for Z_2 and for the product only. An even-sector tool is still tested by Q_8 and 2T. My own count agrees: 736 periodic flat 4-tuples for Q_8 give 92 flat states on the 3-torus, far more than the eight centre characters can separate.
- Step 3.1 called (TM-tw) ARGUED. It is Theorem TW-T of row 1004 (`library/gap-transfer-twisted.md`; check 1008, same provider). Lemma T2 rests on it.
- The frozen ratios 3/23 and 1/61 of step 3.3 are on file (rows 783, 930; `library/gap-oddgap-max.md`). My counts were made blind and agree. This is a second derivation, not an independent check of anything else.
- The remark on Hamilton's formula in step 1.2 (b) is idea B11 of row 1032, found again.
- Lemma T3 is the difference of Lemma ADD of row 1018 in the two sectors. Found again in substance.
- (TW-GROW) is a monotone statement along scales with no tool that reads the group. Row 998 9.5 lists this under "what not to do next", and method 4 says each such step is as hard as the seed. My step 3.4 reached the same sentence by another path.
- FP-1 of Attack 3. In the worst-case form ("every pair of boundary fields") it is expected FALSE: a boundary field near an unstable critical point of the boundary action leaves its neighbourhood after a flow time that has no bound. ARGUED, not proved; the test of step 2 would show it. In the form "in the law of the model" it is a criterion of the kind of method 34, and Lemma TS3 (check 1120) and row 1011 (the pin supremum forgets colour coherence) apply. So Attack 3 gives a smaller space of pins and no gain term.

### 4.3 The cheapest test of Attack 1, run as a guide

GUIDE only; no step of a proof uses it. Row 734 found no published twist ratio on a symmetric four-torus. I measured r = Z_tw / Z for one twist plane by Lemma T4: 16 Gauss-Legendre nodes in the sheet coupling s, pure-Python heat bath, one process, a few megabytes (script `twist_ti_pure.py` in the session scratchpad; not committed). Bulk plaquette at beta = 2.3 came out 0.60, against the known 0.602. Results are appended below when the runs end.

First two results (GUIDE; statistical error only, 5000 sweeps per node; the quadrature error was not measured):

| L | beta | F_v | r = Z_tw / Z | against r* = 0.199 |
|---|---|---|---|---|
| 4 | 2.3 | 0.94 +- 0.08 | 0.39 (0.36 to 0.42) | above |
| 4 | 2.5 | 1.78 +- 0.11 | 0.17 (0.15 to 0.19) | just below |

The integrand Du(s) is largest at s = 0, where the sheet is a tube of deleted plaquettes (about 0.066 at beta = 2.3), and is below 0.005 for s above 0.85. So in this guide the vortex free energy is the work of closing a thin tube, as the container picture says.

More results (same method; GUIDE):

| L | beta | F_v | r = Z_tw / Z | against r* = 0.199 |
|---|---|---|---|---|
| 4 | 2.2 | 0.24 +- 0.06 | 0.79 (0.74 to 0.84) | above |
| 4 | 2.4 | 1.54 +- 0.11 | 0.21 (0.19 to 0.24) | at the threshold |
| 6 | 2.5 | 0.92 +- 0.23 | 0.40 (0.31 to 0.50) | above |

Last result: L = 6, beta = 2.3, 2500 sweeps per node: F_v = -0.08 +- 0.17, so r = 1.09 (0.92 to 1.29). The true r is at most 1. The estimate is compatible with r between about 0.8 and 1.

Reading of the test (GUIDE in every line):

- At a fixed coupling r grows with the size, from L = 4 to L = 6: 0.17 to 0.40 at beta = 2.5, and 0.39 to about 1 at beta = 2.3. This is the direction of (TW-GROW).
- On the side-4 torus r falls with beta: 0.79, 0.39, 0.21, 0.17 at beta = 2.2, 2.3, 2.4, 2.5. It crosses r* = 0.199 near beta = 2.4 to 2.5. On the side-6 torus it is already 0.40 at beta = 2.5.
- So the first clause of the test of step 2 comes out on the favourable side: the moderate threshold is met at boxes of four to six lattice spacings in the window. The box of side 4 at beta = 2.3 is about one inverse critical temperature across (the side-4 deconfinement coupling is near 2.30; recalled, not re-read).
- The consequence is limited. Lemmas T1 and T2 lose a factor exp(2 D) at each step, and the Casimir factors D_+ and D_tw were not measured. At boxes this small they are not expected to be near 1. So the guide supports "the flux threshold comes early". It does not support a seed.
- The frozen values 3/23 = 0.130 and 1/61 = 0.016 lie below every measured value. The closest is r(4^4, beta = 2.5): with both walks combined (see the check below) it is 0.169 (0.155 to 0.184), about two and a half standard errors above 0.130. A tool for the flux half must tell SU(2) at such a box from frozen Q_8, and the value of r at one size hardly does.

Check of the sampler (GUIDE). The run at L = 4, beta = 2.5 was repeated with another seed and with the walk in s reversed, from -1 up to +1. The two walks give F_v = 1.780 +- 0.113 and 1.779 +- 0.124. Node by node the largest difference is 2.0 standard errors. So no hysteresis between the periodic and the twisted vacuum is seen at this size. Combined: F_v = 1.78 +- 0.08. This checks the sampler against itself only. It is not an independent method.

Addendum to step 3.2, after the runs (GUIDE: a numeric scan of the map of Lemmas T1 and T2, script `gd_map.py` in the session scratchpad). With every Casimir factor bounded by d, the map G_d(r) = psi_d(psi_d(r))^4 exp(-6 d) has a region with G_d(r) >= r only for d below about 0.088. Examples: d = 0.02 gives r in [0.24, 0.89]; d = 0.05 gives [0.30, 0.74]; d = 0.08 gives [0.40, 0.58]. So Lemmas T1 and T2 keep the twist ratio above a moderate level only when the thermal excess of each sector is below about nine per cent, that is, when the box is already several correlation lengths of that sector across. The flux half does not free itself from the glue half by these lemmas. This agrees with rows 731 and 1025.

## Step 5. Result

Summary of the top attack, five lines.

1. TWIST reads the flux half of the wall as growth of the twist ratio r = Z_tw / Z. For SU(2) the twisted torus has a zero-action vacuum (twist eaters), so -log r is the work of closing a tube of deleted plaquettes (Lemma T4).
2. PROVED here, checked by no one: T1 (rho(2n) <= rho(n)^2 exp(2 D_+) in a plane direction), T2 (r(2n) >= r(n)^2 exp(-2 D_tw) in a sheet direction, given Theorem TW-T of row 1004), T3 (F_v(2L) = 16 F_v(L) - (Phi_4 - Phi_4^tw)), T4.
3. With Casimir factors equal to 1 the doubling map has a repelling fixed point r* = 0.199. Frozen Q_8 (3/23), frozen 2T (1/61), weak compact U(1) and SU(2) at first passage all lie below it. GUIDE runs: r = 0.79, 0.39, 0.21, 0.17 on 4^4 at beta = 2.2, 2.3, 2.4, 2.5, and 0.40 and about 1 on 6^4 at beta = 2.5 and 2.3.
4. The attempt stops at (TW-line): Phi_4(L) - Phi_4^tw(L) >= 15 F_v(L) + log(1 + c) in the band. It is a comparison of two boundary conditions at one scale. Reflection positivity gives no more, and the lemmas work only when every Casimir factor is below about 0.088.
5. After the reading: the attack is already on file in every main part (rows 731, 783, 930, 1004, 1018, 1025). New here are only the threshold, the form (TW-line) and the guide numbers. No mass-gap claim.

RESULT: Row 1129 (Claude Fable 5.2 max, laptop subagent, geometry seat; the other council files were not read; checked by no one; guide runs only, under 10 MB). No attack passes the wall and (W) is unchanged. Obstacle in the terms of the field: its theorems are either small-energy (Uhlenbeck, instanton calculus, Balaban; they stop at int_block |F|^2 < eps_0, which is first passage) or kinematic and silent on the measure (existence of the flow, the modular region, O'Neill's curvature, twist eaters). Attack 1 TWIST (flux half as growth of the twist ratio): ALREADY TRIED in every main part (rows 731, 783, 930, 1004, 1018, 1025; methods 4, 13, 17); PROVED here, unchecked: Lemmas T1, T2 (given Theorem TW-T), T3, T4; stops OPEN at (TW-line), Phi_4 - Phi_4^tw >= 15 F_v + log(1 + c), a monotone statement with no tool that reads the group; small items not found on file: the ideal doubling map with threshold r* = 0.199, the form (TW-line), and GUIDE twist ratios on symmetric tori (4^4: 0.79, 0.39, 0.21, 0.17 at beta 2.2, 2.3, 2.4, 2.5; 6^4: 0.40 at 2.5 and about 1 at 2.3; reverse-walk check at one point), with the limit that the lemmas need Casimir factors below about 0.088. Attack 2 HELIX (Gribov horizon): ALREADY TRIED (row 1032, B8 and B9); the cross-product term is zero for compact U(1) on the lattice, so Lemma FP-U1 does not kill HX-1, but "no consumer" stands. Attack 3 FLOW-PIN (flowed boundary data for (L3)): new as a device only; its first statement is expected false in the worst case (ARGUED) and its in-law form is method 34. One erratum to my own step 2 (frozen Q_8 and 2T fail the even sector too, check 884). The frozen counts 3/23 and 1/61 were re-derived blind and agree with rows 783 and 930. Output `library/gap-council-geom-fable.md`; scripts in the session scratchpad, not committed.
