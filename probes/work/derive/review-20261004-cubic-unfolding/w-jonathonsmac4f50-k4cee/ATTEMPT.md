# Attempt: J:derive:review-20261004-cubic-unfolding:a1 (worker: Sonnet 5.5, same family, unrefereed)

Plain-language summary. The supplied four-site model has "nodes", places where the two middle energy bands touch at zero energy.
Near the line node whose charge flips above J = 2, the landed notes show the leading-order picture (one node before the flip,
three after) but say they do not exclude extra nodes. This attempt shows, for each fixed J in the two open intervals and also at
J0 (root of J^3 - 4J - 4 = 0), that the landed local expansion plus the exact node families leave no room for extra nodes in
a small box around the flip. The size of the box is not computed. The argument is a counting argument (the number of
zeros of an analytic map near an isolated zero cannot change), plus one exact fact that makes the scalar part of the effective
Hamiltonian follow the vector part.

I read, in the current main checkout (a77a3449c9...): `docs/MINIMAL_AXIOMS_2026-06-29.md` (all of it; the four axioms are at lines 35-83,
the "complete supplied foundation" sentence at lines 108-112) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (the
three registered primitives, lines 31-130). None of the four axioms and none of the three primitives (`scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`) is used or needed below. The model is a supplied comparator
(flip note lines 18-26 and 121-128, its N3 and N8): a statement about a matrix family, not about the framework.

Source objects: all six sha256 values match at 2868a0c453e667d1267f0e1e7403732a11893d78 (see RECOVERY_STATUS.json).

Labels: PROVED = full argument below (modulo the named cited theorem T and the named supplied inputs); CHECKED = executed by
`check.py` (exact sympy, or mpmath at 40-60 digits, not interval-certified); ASSUMED = premise; READING = interpretation.

## Step 1. Setting and the object counted (ASSUMED, supplied)

H(f) = i M(f), M real hopping on the landed four-site network, couplings Jx = Jy = 1, Jz = J, odd term kappa, u = kappa^2
(flip note line 18-26; network rebuilt in check.py from the network rules). Flip data (landed, flip note lines 35-36): node
f0 = (x, 1-x, 0), cos 2 pi x = c_F = (J-2)(J+1)/(J+2), kappa_f^2 = u_f = J(J+2)/(4A), A = 4 + 2J - J^2, N = J^3 - 4J - 4,
J0 = 2.38298 the root of N in (2,3). Coordinates xi = 2 pi (f - f0), u = xi1 - xi2, v = xi1 + xi2, t = xi3, eps = kappa - kappa_f.
Call a *node* a real f with dim ker H(f) >= 2, that is, a zero-energy double level.
Objects: the 2x2 E=0 Schur complement S = s0 + d.sigma on a fixed frame of ker H(f0, kappa_f), and the box
P_r = {|u|, |v|, |t| < r} (complexified when stated).

## Step 2. The spectrum is even, so middle-band touchings are exactly the zero-energy double levels (CHECKED exact E1; also landed)

The characteristic polynomial of M has no lambda^3 and no lambda^1 term, identically in (z1,z2,z3,J,kappa) (check E1). Hence
spec H(f) = {+-l1, +-l2}, det H = l1^2 l2^2 >= 0, and the middle pair +-l2 can touch only at E = 0, where it is a double zero.
(Landed in the general-couplings and off-plane notes: `docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_THE_LINE_TOUCHINGS_AND_THEIR_CHARGES_ARE_EXACT_FOR_GENERAL_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md:4`.
Not new. Used here only through steps 3 and 6.)

## Step 3. Block elimination and scalar-zero slaving (PROVED from step 2; the numbers are CHECKED N2)

At (f0, kappa_f) the levels are 0, 0, +-4J (flip note line 35 and check N0), so the 2x2 block C = Q^H H Q on the complement
is invertible near the node, with det C < 0 (eigenvalues near -4J and +4J). Write H = [[A,B],[B',C]] in the frame (K,Q).
(a) For real or complex f: ker H and ker S correspond (v_Q = -C^{-1} B' v_K), so dim ker H = dim ker S. (b) det H = det C det S, and for real
f, det S = s0^2 - |d|^2. With det H >= 0 (step 2):

    |d|^2 - s0^2 = det H / |det C| >= 0.

So **|s0| <= |d| near the node**: a real zero of the vector d automatically has s0 = 0, hence S = 0, hence a zero-energy double level.
In the box, nodes = real zeros of d. This closes the "scalar-zero" item for the census: no separate scalar equation is needed.
(The source notes only say the scalar part has strictly higher weighted order: flip note lines 94-97.) CHECKED: N2 shows
max |s0|/|d| ~ 3e-3 at 25 random real points for each of J = 13/6, 5/2, 3.

## Step 4. Supplied jets at fixed J (ASSUMED from the landed exact identities; CHECKED at three J)

For J in (2,J0) or (J0,1+sqrt5), the landed expansion is d = x_u u' + x_v v + x_beta t^3 + (weighted order >= 4), weights (3,3,1),
u' = u - u2 t^2, with x_u, x_v, x_beta mutually orthogonal, positive determinant (flip note lines 37-45 and 90-97; birth note
lines 56-63 give the formulas a^2, b^2, g^2, u2 for J < 2). Consequences used:
(J-a) d(f0,kappa_f) = 0, d_t = 0 there, and d_u, d_v are linearly independent;
(J-b) after solving the x_u and x_v components for (u,v) = (U,V)(t,kappa) by the implicit function theorem, the remaining scalar
function phi(t,kappa) = nu . d(U,V,t,kappa) (nu the unit normal to span(x_u,x_v)) satisfies phi(t,kappa_f) = g t^3 + O(t^4), g != 0.
CHECKED (N1a, N1b) at J = 13/6, 5/2, 3 in 40-digit arithmetic: d_t = 0 to 1e-20, cos(x_u,x_v) ~ 1e-27, and phi/t^3 extrapolates
to the landed value sqrt(J^4 (J+2)/8)/|N| (1.35763 vs 1.35768, 2.88390 vs 2.88462, 0.646819 vs 0.646830), U/t^2 to the landed u2.
Not re-proved exactly here: the identities for every J of the intervals rest on the source runner's function-field computation.

## Step 5. Standard theorem T (cited, not re-proved here; recalled from memory, not re-read in the repository)

T (conservation of multiplicity). Let F_lambda : Omega in C^n -> C^n be holomorphic jointly in (z, lambda), with F_0 having an isolated zero
at 0 of multiplicity m (m = dim O_0/(F_0)). For a small closed polydisc B around 0 there is a neighbourhood Lambda' of lambda = 0 such that for
lambda in Lambda' there is no zero on the boundary of B and the zeros in B have multiplicities summing to m; a zero has multiplicity 1
iff the Jacobian determinant is nonzero. Also (T2) eliminating a variable that has a nonzero linear term preserves the multiplicity, and (T3) two plane germs with orders
p, q and no common tangent have intersection multiplicity p q. (Griffiths-Harris, Principles of Algebraic Geometry, ch. 5 sec. 2; Chirka, Complex Analytic Sets, ch. 1.)
For one variable this is Rouche's theorem. Step 7 needs only that case; steps 10-11 need T and T3.

## Step 6. The exact families are zeros of d, complex points included (CHECKED exact E3, E4)

(a) Line family (z1,z2,z3) = (z,1/z,1), z a root of u z^4 - z^3 + (J^2-2u-2) z^2 - z + u: all 16 entries of adj(M) reduce to 0 modulo this
polynomial (E3a). (b) Plane family (ii) (z1 root of z^2 - 2 a z + 1, a = 1 - J/(4u); z2 = 1/z1; z3 root of z^2 - 2 b z + 1, b = (J+2)/(4u) - (4+J-J^2)/J): all 16
entries of adj(M) reduce to 0 modulo the two quadratics (E3b). So rank M <= 2, dim ker H >= 2, at every point of both families, real or
complex. By step 3(a), S = 0 there, hence d = 0 and s0 = 0 at those family points that lie in the box (complex ones included).
(The real statement is landed; the complex extension is the new ingredient.) Flip algebra, exact (E4): b = 1 and a = c_F at u_f;
q(c_F; u_f) = 0 with dq/dc = 2N/A and disc_c q (u_f) = 4N^2/A^2; so for N != 0 the line root c_F is simple and the
real line node (x,1-x,0) persists, analytic in u, for u near u_f. For u > u_f we have b < 1 (b strictly decreasing in u), giving the real plane pair (x_p, 1-x_p, +-f3), f3 != 0,
and for u < u_f we have b > 1, giving f3 = +-i y with cosh(2 pi y) = b. Exactly E5: u_f lies above the vertex of disc_c(q)(u) = 64u^2 + 16(2-J^2)u + 4 on (2,1+sqrt5), so u_f >= u_*
(the larger root) with equality iff N = 0, and disc is increasing through u_f.

## Step 7. Census at a fixed J in (2,J0) or (J0,1+sqrt5) (PROVED from steps 3-6, conditional on the supplied jets of step 4)

Claim A. Fix such J. There are r > 0 and eps_J > 0 such that, in the box P_r, for 0 < |eps| < eps_J:
for eps < 0 the nodes are exactly one, the line node (x,1-x,0); for eps > 0 exactly three, the line node and the two plane-(ii) nodes
(x_p, 1-x_p, +-f3); at eps = 0 exactly one, the cubic point. All are nondegenerate zeros of d (Jacobian det != 0) when eps != 0.

Proof. By (J-a) and the implicit function theorem, in a complex polydisc P = D_r(u) x D_r(v) x D_delta(t) and for |kappa - kappa_f| < eps_1,
the zeros of d are the points (U(t,kappa), V(t,kappa), t) with phi(t,kappa) = 0; the multiplicity of such a zero of d equals that of the zero of phi (O/(d) is isomorphic to O_t/(phi)).
By (J-b), phi(.,kappa_f) has a zero of order exactly 3 at t = 0 and no other zero in |t| <= delta (shrink delta). By Rouche, shrinking eps_J, for |eps| < eps_J
phi(.,kappa) has exactly 3 zeros in |t| < delta counted with multiplicity. Now:
 - eps > 0: the line node (t = 0) and the plane nodes (t = +-T, T = arccos b(kappa) > 0) are three distinct real zeros of d (step 6), in P once eps is small (continuity of the
   exact formulas), hence three distinct zeros of phi (by uniqueness of (U,V) in P). That is all 3, so these are all the zeros of d in P, real or complex, each simple.
 - eps < 0: the line node (t = 0) is a real zero; the plane points have t = +-i y, y > 0, by step 6 zeros of d; three distinct zeros, multiplicity 3 used up. The only real zero
   of d in P is the line node, simple (multiplicity 1, and its Jacobian sign is +1: CHECKED N3c).
 - eps = 0: multiplicity 3 at t = 0 and no other zero.
Since by step 3 nodes in P_r (r real) are exactly the real zeros of d, Claim A follows. QED (conditional on step 4 and on the existence of eps_J, r without computing them).

CHECKED consistency (N3a-N3c, 40 digits, J = 13/6, 5/2, 3, relative eps about +-3e-4 to 1.5e-3): the winding number of phi on |t| = 0.14
is 3.0 for both signs; the three family points are zeros of d with |d|,|s0| < 1e-25; Jacobian signs (line, pair) = (-1, +1, +1) above and +1 below, sum +1 (degree conserved).

## Step 8. Supplied jets at J = J0 (ASSUMED, landed X12-X14; CHECKED at 60 digits, N4a-N4d)

At (J0, kappa_f(J0)): d = 0, s0 = 0, levels 0, 0, +-4 J0 (N4a). d_u = d_t = 0 to 1e-25 and d_v != 0 (N4b), so the Jacobian has rank 1 (the x_u coefficient is proportional to N, flip note line 54).
In the orthonormal frame e2 = d_v/|d_v|, e1 = d_tt/|d_tt|, e3 = e2 x e1, the second derivatives are d_uu = 2 c_uu e1, d_tt = 2 c_tt e1, d_ut = c_ut e3,
d_kappa = c_eps e1 + (nothing in e2, e3), with c_uu = 0.3238994356 (= J0^2/(4(J0+2)), landed), c_tt = 1/2, c_ut = 1.091553, c_eps = -2.8176, b = |d_v| = 2.2852; every off-pattern entry is below 5e-30 (N4d).
This is the landed normal form F1 = c_uu u^2 + c_tt t^2 + c_eps eps, F2 = b v, F3 = c_ut u t (flip note lines 54-62) re-derived numerically.

## Step 9. The multiplicity at J0 is exactly 4 (PROVED from step 8 and T2, T3; the resultant is CHECKED N4c)

By T2, eliminate v by e2.d = 0 (b != 0): v = V(u,t) = O(2). The reduced germ g = (e1.d, e3.d)(u, V(u,t), t) has zero 1-jet (d_u = d_t = 0 and e1, e3 are orthogonal to d_v)
and 2-jet (Q1, Q3) = (c_uu u^2 + c_tt t^2, c_ut u t), because the correction from V enters only at order 3 (the cross terms d_uv u V and d_vv V^2 are cubic or higher, and the
d_v V term drops out against e1, e3). Their resultant is c_uu c_tt c_ut^2 (nonzero, checked at N4c as Res/scale = 0.136), so the two tangent cones have no common
complex line. By T3 the multiplicity of the germ d(.; J0, kappa_f) at the node is 2 x 2 = 4. (The local degree is 0, matching the landed degree-zero statement, flip note lines 103-109.)

## Step 10. Census at J = J0 (PROVED from steps 3, 6, 9 with T; conditional on step 8)

Claim B. At J = J0 there are r > 0 and eps_0 > 0 such that, in P_r, for 0 < |eps| < eps_0 the nodes are exactly: for eps < 0 none; for eps > 0 four, namely the two line nodes
(x_{1,2}, 1-x_{1,2}, 0) and the two plane-(ii) nodes (x_p, 1-x_p, +-f3); each is a nondegenerate zero. At eps = 0 the node is isolated.

Proof. By T, for small |eps| the zeros of d in a fixed complex polydisc have total multiplicity 4. The four exact family points are pairwise distinct for eps != 0: the line pair
needs disc(u) = 64u^2 + 16(2-J0^2)u + 4 != 0, and disc(u_f) = 0 with disc' (u_f) > 0 (E4, E5); the plane pair needs b != 1, i.e. u != u_f; the plane points have t != 0
while the line points have t = 0. They lie in the polydisc for small eps because the line roots tend to c_F (at N = 0, q and q' both vanish at c_F, so c_F is the double root c_b) and f3 -> 0.
By step 6 they are zeros of d. Four distinct zeros use up the multiplicity: no other zero exists. For eps > 0 all four are real (disc > 0, b < 1): four nodes, simple.
For eps < 0, disc < 0 makes the line points nonreal (c nonreal) and b > 1 makes the plane points nonreal (f3 = +-i y): no real zero, so no node. QED.

CHECKED (N4e, 60 digits, eps/kappa_f = +-1e-6): d and s0 vanish at all four points to 1e-40; separations 2.8e-3; real for eps > 0 with Jacobian signs (-1,-1,+1,+1) (sum 0); nonreal for eps < 0.
A finite sample of 30 random real points at eps < 0 finds no zero (N4f; not part of the proof).

## Step 11. Two-parameter statement near the exceptional point (PROVED as step 10 with lambda = (J - J0, kappa - kappa_f(J0)); conditional on step 8)

Claim B2. There are a neighbourhood W of (J0, kappa_f(J0)) in the (J,kappa) plane and a box such that for (J,kappa) in W off the two curves u = u_*(J) and u = u_f(J),
the nodes in the box are exactly the real points among the four family points (two line, two plane-(ii)), and their number is 0 for u < u_*, 2 for u_* < u < u_f, 4 for u > u_f (E5: u_f >= u_*).
Proof: step 10 with T applied to the family d_lambda: multiplicity 4 is conserved over W; off the two curves the four family points are distinct; each is a zero of d (step 6); they are in the box by continuity.
CHECKED (N5, J = J0 +- 0.004, one coupling in each of the three regimes): u_f > u_*, d = s0 = 0 at all four points, counts of real points 0 / 2 / 4.
Consistency with Claim A: for fixed J != J0 the second line root sits at distance of order |N| from c_F, so it is outside the shrinking box of Claim A; the two claims do not contradict each other.

## Step 12. What is new, what is not

Not new (sources): the families (09-26 note lines 46-50), the line and plane algebra, the jets, orthogonality, degrees, charges, the weighted normal forms, `det H >= 0` and the even spectrum (general-couplings note), the leading-form counts 1/3 and 0/4.
Retrieval and the numerical agreement of N1 with landed values are not new.
New in this attempt (relative to the six sources and to what I found on main at a77a3449c9; searches for "Weierstrass", "Rouche", "slaved" in the composite-site notes found nothing):
 1. The slaving inequality |s0| <= |d| (step 3), which removes the scalar equation from the census.
 2. Rank M <= 2 at complex points of both families (E3), so complex family points count as zeros of d.
 3. The multiplicity-counting census: exactly 1 node for kappa <= kappa_f and exactly 3 for kappa > kappa_f near the flip, for each fixed J (Claim A), and exactly 0/4 at J0 (Claim B) and 0/2/4 in a neighbourhood (Claim B2), in a small box, conditional on the supplied jets.
These are conditional results for the supplied comparator. They are not a physical statement, an audit verdict or a global census.

## Step 13. First unresolved step and remaining work

First unresolved: the radii r, eps_J, eps_0 and W are not computed. Every "small" above comes from the implicit function theorem and Rouche or T and is non-constructive, so nothing here bounds the box or the range of eps, and
nothing is uniform in J (the box must shrink as J -> J0 because x_u is proportional to N, and the behaviour as J -> 2 and J -> 1 + sqrt 5 is not examined). To make Claim A explicit for one rational J (for example 5/2), one needs Cauchy
estimates for the complex-analytic Schur complement on a stated polydisc and a quantitative Rouche inequality for phi; the argument-principle counts in N3a (radius 0.14) are 40-digit numerical evidence, not a bound.
Also not re-proved here: the jets of steps 4 and 8 for every J of the intervals and exactly at J0 (supplied, re-checked numerically only at J = 13/6, 5/2, 3 and J0), the theorem T (cited), and the multiplicity of merged points on the curves u = u_*(J), u = u_f(J).
Not covered: any census outside the box, anisotropic couplings, J < 2, and any physical reading.

No repository file was edited; nothing was committed (the brief gives no repository write access, so the "commit the checker before run_probe.py" step is left to the supervisor).
