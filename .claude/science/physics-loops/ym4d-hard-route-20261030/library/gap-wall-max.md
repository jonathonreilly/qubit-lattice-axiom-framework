# FINISH row 894, gap-wall-max, Claude Fable 5.2 max

(file seeded by the lead; the author writes below)

Clone commit: de5181bd72f54e89fd7411085e39524f751c384c (branch claude/ym4d-hard-route, /Users/jonreilly/ym4d-lead/clone, read-only).
Author: Claude Fable 5.2, max effort. FINISH row 894. Date 2026-11-13.
Marks: PROVED (mine, by hand), READ (path and line), ARGUED, GUIDE (numeric, never discharges), OPEN.

## Target

(WALL)_40 of D/library/gap-crux-core-max.md (row 892, unchecked):
Var(g^2) >= min( 1 , (a/40) E[g^4] (1 - theta^2) ),
for the flux ground function g at one Theorem SH box.
Task: prove it, or the strongest order-one form with explicit constants, or show it fails.

## Plan (one step per response; each step is appended here before the next starts)

1. Read row 892 (gap-crux-core-max.md): exact statement of (WALL)_40, Lemma R, Proposition W, and Step 7 (the three failed tries). Record the objects and normalisations.
2. Read rows 876 and 886 (gap-brainstorm2-max.md, gap-kurt-max.md) and checks 883, 889: g, kappa, theta, a, b, the moment hierarchy, the hidden-bit picture.
3. Say what (WALL) means physically. Reduce it to an abstract statement about a reversible Markov or transfer operator and its ground function. Decide which hypotheses the statement really uses.
4. Test the abstract statement for failure: build the smallest model (two-state, three-state, birth-death chain) with the right profile and compute Var(g^2), E[g^4], theta. Find the true extremal constant or a counterexample.
5. Attack A: spectral argument for g^2 under the transfer operator (g^2 as a test vector in the even sector; Poincare and reverse Poincare).
6. Attack B: hidden-bit picture and reflection positivity across the flux; what the fused state gives beyond connectedness.
7. Fact tests on every step that survived: U(1) Coulomb, Z_2 at beta 5/2, frozen 2T; Q_8.
8. Assemble: the strongest proved statement with explicit constants, what stays OPEN, and the RESULT line.

## Log

## Step 1. Row 892, read (D/library/gap-crux-core-max.md L327-479)

Objects (READ L384-386, L475-477).
- T: transfer operator of the periodic cube b^3 (time direction 1). Nonnegative for Wilson. Omega its vacuum, lambda_0 its top eigenvalue.
- P: the ground-state transform of T. A reversible Markov operator. Its stationary law nu is the vacuum measure of one time slice.
- Centre flips C_i (i = 1,2,3 spatial): group Z_2^3; seven nonzero characters chi.
- g = Psi_chi/Omega: the flux ground function. P g = theta g, E g^2 = 1, kappa = E g^4. theta = lambda_chi/lambda_0. Var(g^2) = kappa - 1.
- rho = lambda_1^+/lambda_0: top eigenvalue of P on flip-invariant mean-zero functions. h = g^2 - 1 is flip-invariant, mean 0, norm squared kappa - 1.
- a: the time extent (lattice steps). The SH box is a x b^3, b >= 24 a, a >= 82, a even.
- S_ev(a; b^3): the even thermal sum at time a. GLUE: S_ev(a) <= 160^(-16), S_ev(a/2) <= 1. S_ev(a) >= rho^a.

Statements (READ).
- Lemma SQ identity (L384, check 883 HOLDS): <g^2, P^t g^2> >= theta^(2t) kappa.
- Theorem SQ (L384): <g^2, P^t g^2> <= 1 + (kappa - 1) rho^t.
- Lemma R (L391): rho >= 1 - kappa (1 - theta^2)/(kappa - 1).
- (WALL)_M (L397): if kappa <= 2 then kappa - 1 >= (a/M) kappa (1 - theta^2). The one-line form (L477) is (WALL)_40.
- Proposition K (L388): kappa >= 1 + eta for the seven sectors, GLUE at level 160^(-8(1+eta)/eta), a >= log(160) 8 (1+eta)/eta give Q_0 <= 1/20.
- Proposition W (L401): (WALL)_40 + GLUE at 160^(-16) + a >= 82 + b >= 24 a give kappa > 2, then (CORE).
- Step 7 limits (L411-415). Way 1: connectedness alone fails (a double well is connected, kappa near 1, even sector gapped). Way 2: no one-step sign flips gives only M of order a (ARGUED there). Way 3: other even trial vectors give nothing.
- Fact tests of (WALL) (L404-408): fails for Z_2 above its transition and frozen Q_8, 2T (thin membrane in one step). U(1): kappa >= 3/2, passes (WALL), fails GLUE.

First reading (mine, to be made exact in Step 3).
- T, g, kappa, theta do not depend on a. The letter a enters (WALL) only as a clock unit. With a = b/24, (WALL)_40 reads: kappa <= 2 implies 1 - theta^2 <= (960/b) (kappa - 1)/kappa.
- Two regimes. If 1 - theta^2 >= 40/a, (WALL)_40 is the bare statement kappa >= 2. If 1 - theta^2 < 40/a it is a lower bound on the wall measure by (a/40) times the flip rate.
- Under GLUE, Lemma R caps the wall: kappa - 1 <= kappa (1 - theta^2)/(1 - rho), and 1 - rho > 40/a. So under GLUE, (WALL)_40 can hold only with kappa > 2. Under GLUE, (WALL)_40 and (KURT)_1 (kappa > 2) are the same statement. To be proved in Step 3.

## Step 2a. Row 886, read (D/library/gap-kurt-max.md L1-598, whole file)

What row 886 already has (READ; all "PROVED there, unchecked" unless marked). I do not redo any of it.
- Theorem 4.1 (L205): moment hierarchy theta^(pt) M_(2p) <= M_p^2 + rho^t (M_(2p) - M_p^2).
- Theorem 4.3 (L234): with lambda_bar = <h,(1-P)h>/||h||^2 and V = P g^2 - theta^2 g^2: (kappa - 1)(lambda_bar - (1 - theta^2)) = -Cov(g^2, V); lambda_bar (kappa - 1) <= kappa (1 - theta^2).
- Theorem 4.4 (L250): diffusion form, exact: kappa = 3r/(3r - 2), r = lambda_bar/(2E). (KURT)_c0 <=> lambda_bar <= (4/3)(1 + 1/c0) E.
- Theorem 4.5 (L272): kappa >= 1/c^2 with c = E|g|; kappa - 1 >= 2(1 - c); kappa - 1 <= eta gives a sign bit s = sign g with theta(1 - eta) <= <s, P s> <= theta.
- Proposition 4.6 (L288): for a diffusion, Int psi(g) Gamma(g) = E Int Psi(g) g; (KURT) follows from a reverse Holder bound on Gamma(g).
- Theorems 5.1, 5.2 (L303, L321): a circle of symmetries through the flip gives kappa >= 3/2 (U(1)); a transitive multiplet of dimension d gives kappa >= 3d/(d+2).
- Examples 6.1, 6.2 (L361, L373): product chain and a Z_2 gauge theory with frozen space-like plaquettes: kappa = 1 exactly, theta any value, S_ev = 0. Scope note L399: the Z_2 example is anisotropic; an isotropic counterexample to "light or kappa >= 1 + c0" is OPEN there.
- 7.2 (L428): Cheeger form. 7.3 (L444): GUIDE run; in discrete time kappa - 1 can be far below E/m (jumps across the nodal set).
- 7.5 (L484): (HB): a box with a hidden bit (kappa - 1 <= eta_0) has an even excitation with m a <= M_0. OPEN. Why plausible (ARGUED there): the flat connections of a connected group form a connected valley that contains U and zU.
- 7.6 (L502): (FUSE-E): theta <= rho^g suffices for the consumer and is strictly weaker than (KURT).
- 3.6 (L165, ARGUED there): SU(2) below the centre crossover (small box) has kappa -> 1. So no size-free bound kappa >= 1 + c0 exists.
- 8.5 (L580): advice: do not treat (KURT) as a regularity statement; the target is (HB) or (FUSE-E).

Row 892 then made (HB) exact as (WALL)_M (Lemma R is the step from (WALL)_M to "an even mode of rate at most M/a").

Notes for my Steps 3 to 6 (mine; nothing proved yet).
N1. Under GLUE the wall branch of (WALL)_40 is empty (Step 1, last bullet). I must check this by a proof with numbers.
N2. The discrete "way 2" of row 892 was only ARGUED. An exact identity is available: expand E[(g_1 - g_0)^4]. To be proved in Step 5.
N3. kappa = 2 is the value for a sum of two independent bits, and for one free SU(2) character (Haar: E chi^4 = 2). kappa >= 3 - 2/n for n independent equal parts. So (KURT)_1 is the statement "g splits into at least two independent parts". To be made exact.
N4. Partial centre flips (flip only the links of the cut plane that lie in a region Sigma of the transverse torus) give an exact splitting g = g_L + g_R. They are not symmetries; the defect is an equal-time 't Hooft loop on the boundary of Sigma. To be examined in Step 6.

## Step 2b. Row 876, read (D/library/gap-brainstorm2-max.md L353-452)

- 4c Step 9 (L418-421): three attempts on (KURT). (a) Chapman-Robbins with a plaquette sum gives order 1/a. (b) Half-box conditioning: g_R = E[g | right half], g_L its mirror; RP gives Int g_R^2 g_L^2 >= (Int g_R^2)^2; if g = g_R + g_L up to a small remainder then kappa >= 2 - small; stops at (HC). (c) Dynamics: no even observable sees the flips except g^2.
- 4d Lemma RPF (L430): for a half-box odd O, mirror O', Phi = O O', C = <Phi>, f(t) the propagator of O: <phi, (L/lambda_0)^t phi> >= f(t)^2 - C^2. PROVED there.
- 4d Stage 3 (L441): either E >= m/2 or the winding lines have long-range order across the box. Needs (HC): an odd half-box operator creates the flux ground state with amplitude at least a^(-p). OPEN there.
- 4d Stage 4 (L449): ||P_R g||^2 + ||P_L g||^2 >= 2 - E/gamma with gamma a worst-exterior gap. Not usable.
So my note N3 (kappa >= 2 from two independent halves) is row 876's attempt (b). My note N4 (partial centre flips) is a different, exact splitting; row 876 used conditional expectations. I keep N4 and drop N3 as known.

Checks 883 and 889: I rely on row 892's reading of check 883 (Lemma SQ HOLDS; Theorem SQ HOLDS AFTER CORRECTION; the SQ-F display HOLDS). Check 889 had no RESULT at row 892's commit (READ row 892 L469). I look at both files in Step 3 only if a step needs them.

Check 889 (READ D/library/gap-kurt-check-astra.md L508, RESULT line, Codex gpt-6-astra xhigh): row 886's moment hierarchy, discrete energy identity and symmetry theorems HOLD; the diffusion, sign, energy-density and counterexample statements HOLD AFTER corrections; the hidden-bit converse (4.5 "exactly when"), discrete "KURT implies FUSE-E" and the unqualified consumer sufficiency FAIL. I use only items that HOLD.

## Step 3. What (WALL) says, and the decision under GLUE

Standing assumptions (S+): row 886's (S) (READ gap-kurt-max.md L193-200) with P >= 0. So P is a Markov operator, self-adjoint and nonnegative on L^2(nu); g is real, in the sector chi, P g = theta g, E g^2 = 1; theta is the top of P on the sector, 0 < theta < 1 (theta < 1 because the kernel is strictly positive, so 1 is a simple eigenvalue and g is orthogonal to 1); rho is the top of P on flip-invariant functions orthogonal to 1; kappa = E g^4; h = g^2 - 1.

I read (WALL)_M in the one-line form of row 892 L477:  kappa - 1 >= min{ 1, (a/M) kappa (1 - theta^2) }.

**3.1 Physical reading (ARGUED).**
- s = sign g is a centre bit of the time slice. kappa - 1 = E (1 - g^2)^2 measures how far g is from a bit. (1 - theta)/2 is the flip rate of the bit weighted by |g| (READ row 886 Theorem 4.2).
- W := (kappa - 1)/(kappa (1 - theta^2)) is a time, in lattice steps: the mean wall occupancy divided by the flip rate. It is the duration of one flip. (WALL)_M says: W >= a/M, or kappa >= 2.
- Lemma R says the opposite inequality with the even relaxation time: W <= 1/(1 - rho). A flip cannot last longer than the slowest even mode lives, because the wall h = g^2 - 1 is itself an even excitation.
- In four dimensions the flip of the bit of direction i is a centre vortex sheet that spans the two transverse directions (area b^2). W is the thickness of that sheet in the time direction. (WALL)_M with the wall branch active says: the sheet is thicker in time than a/M.
- kappa >= 2 is the kurtosis of a sum of two independent equal parts, each of which may be a bit. kappa >= 3 - 2/n holds for n independent equal parts (each part has kurtosis at least 1). So the branch "kappa >= 2" says: the flux function is not one coherent bit; it is at least as spread as two independent pieces. In a confined box g is a sum of many tube positions and kappa is near 3 (ARGUED in rows 876, 886).

**3.2 Proposition D (under GLUE the wall branch is empty; PROVED).** Assume (S+). Let M > 0 and a > 0 with a (1 - rho) > M. Then (WALL)_M holds if and only if kappa >= 2.
Proof. If kappa >= 2 the left side is at least 1 and (WALL)_M holds. Let kappa < 2. Then kappa - 1 < 1, so (WALL)_M would need kappa - 1 >= (a/M) kappa (1 - theta^2). Lemma R (READ row 892 L391; one line: <h, P h> <= rho (kappa - 1) and <h, P h> = <g^2, P g^2> - 1 >= theta^2 kappa - 1) gives kappa (1 - theta^2) >= (kappa - 1)(1 - rho). So kappa - 1 >= (a (1 - rho)/M)(kappa - 1). If kappa > 1 this says a (1 - rho) <= M, which is excluded. If kappa = 1 it says 0 >= (a/M)(1 - theta^2), which fails because theta < 1. QED

**3.3 Corollary D1 (numbers; PROVED).** Assume GLUE at the level of Proposition W: S_ev(a) <= 160^(-16), a >= 82. Then a (1 - rho) >= 51.5 > 40, and (WALL)_40 for a sector is the same statement as kappa >= 2 for that sector.
Proof. rho^a <= S_ev(a) (READ row 892 L402: the operator is nonnegative), so rho <= e^(-c/a), c = 16 log 160 = 81.20. The function a (1 - e^(-c/a)) is increasing in a (its derivative is 1 - (1 + x) e^(-x) >= 0 at x = c/a). At a = 82 it is 82 (1 - e^(-0.9903)) = 82 x 0.6285 = 51.5. QED
The same holds for every M < 51.5. For large a it holds for every M < 81.2.

**3.4 Corollary D2 (the only alternative to the flux gap is a near-bit; PROVED).** Assume GLUE as in 3.3. If theta^a >= t_0 then (kappa - 1)/kappa <= 2 log(1/t_0)/51.5. For t_0 = 1/20: kappa <= 1.132. For t_0 = 1/80: kappa <= 1.205.
Proof. 1 - theta^2 <= 1 - t_0^(2/a) <= (2/a) log(1/t_0). Lemma R: (kappa - 1)/kappa <= (1 - theta^2)/(1 - rho) <= 2 log(1/t_0)/(a (1 - rho)). Use 3.3. QED

**3.5 Decision (follows from 3.2 to 3.4).**
(i) At an SH box that satisfies GLUE, (WALL)_40 has no wall content. It is exactly (KURT)_1: kappa >= 2 for the seven sectors. No near-bit can satisfy it. A proof of "(WALL)_40" in the regime where the lane uses it is a proof that the flux function is not a near-bit.
(ii) The picture "a near-bit flips slowly, at a rate below 40/a" is never realised at such a box. There the flip of a near-bit lasts at most 1/(1 - rho) <= a/51.5 steps. So the mechanism "thick in time" cannot be what a proof establishes at the SH box. It can only be the route to a contradiction: a structural reason for W >= a/40 that does not use GLUE.
(iii) Without GLUE the wall branch is real. In a weakly coupled small box the flip runs along the toron valley and W is of order b/g (ARGUED, rows 886, 892). There (WALL)_M can hold with kappa near 1.
(iv) What the consumer needs from this node is less: (KURT)_eta for one eta > 0, with GLUE at the level 160^(-8(1+eta)/eta) (READ Proposition K). By 3.4 the scenario to exclude under GLUE is: a centre bit with kappa <= 1.13 to 1.21 whose flips are instanton events shorter than a/51 steps. In field-theory words: a gapped phase in which the one-form centre symmetry is broken at the scale of the box (a Z_2 topological order). (WALL)_40 at the SH box is the statement that pure SU(2) has no such phase at the coupling considered.

## Step 4. Exact models: where (WALL)_M holds, where it fails, and how sharp the threshold is

**4.1 Two-dimensional gauge theory, any compact group G in SU(2) (PROVED).** Space is a ring of b links, time is direction 1, the weight of a time-like plaquette is k(V) proportional to e^(beta chi(V)/2), chi = tr. In temporal gauge the one-step kernel on G^b is the product of k(U_e^(-1) U'_e). There is no space-like plaquette. So Omega = 1, lambda_0 = 1, P = T, and nu is Haar measure on G^b.
(a) Gauge-invariant functions are class functions F(H) of the holonomy H = U_1 ... U_b, and P F = F * k^(*b) (b-fold convolution).
Proof. (P f)(U) = Int prod k(V_e) f(U_1 V_1, ..., U_b V_b) dV. For f = F(H): U_1 V_1 U_2 V_2 ... U_b V_b = H V'_1 ... V'_b with V'_e a conjugate of V_e. k is a class function, so the V'_e are again independent with law k. QED
(b) So the eigenfunctions are the irreducible characters chi_r of G, with eigenvalues c_r^b, c_r = Int k chi_r/dim r. The law of H under nu is Haar measure on G.
(c) For G = SU(2) with the Wilson weight: c_j = I_(2j+1)(beta)/I_1(beta), decreasing in j. The odd sector is half-integer j. Its top is j = 1/2: g = chi(H), theta = (I_2/I_1)^b, rho = (I_3/I_1)^b. And
  kappa = Int chi^4 dHaar = 2 exactly, for every beta and every b
(the number of singlets in four spin-1/2 factors). So Var(g^2) = 1: (WALL)_M holds for every M and a, with equality in its threshold.
(d) Other groups, same computation, kappa = E_G chi^4 (when chi restricted to G is the top odd character):
  Z_2: 1.   U(1) (g = sqrt2 cos): 3/2.   SU(2): 2.   2T (24 elements): 2.   2O (48 elements): 2.   Q_8: 4.
(2T: chi takes the values 2, -2, 0, 1, -1 on 1, 1, 6, 8, 8 elements; E chi^2 = 1, E chi^4 = 48/24 = 2. Q_8: chi = +-2 on +-1 and 0 on the other six; E chi^4 = 4. This is the READ fact "Haar moments of Q_8 and 2T first differ from SU(2) at degrees 4 and 6" in the form that matters here.)
Consequences.
- The threshold 1 of (WALL)_M cannot be raised: SU(2) in two dimensions has Var(g^2) = 1 exactly. A proof of the strict form "kappa > 2" must use more than one tube position. Proposition W works with kappa >= 2 (Proposition K with eta = 1).
- (WALL)_40 is not necessary for the consumer. Two-dimensional U(1) has kappa = 3/2 and 1 - theta^2 = 1 - (I_1/I_0)^(2b), so (WALL)_40 fails there as soon as 1 - theta^2 > 40/(3a), that is in every large box. Yet its flux is heavy and its even sum is small ((KURT)_(1/2) and Proposition K apply). A failure of (WALL)_40 alone refutes nothing.
- In two dimensions 2T and 2O pass with the same value as SU(2). The fourth moment of one tube does not separate SU(2) from 2T. Whatever separates them at order one in four dimensions is not the Haar value of kappa.

**4.2 n independent tube positions (PROVED).** Let P = P_Y x ... x P_Y (n factors) on Y^n with the product law, w the top odd function of one factor, E w^2 = 1, kurtosis kappa_1 >= 1, eigenvalue theta_Y. The function g = n^(-1/2) sum_k w(y_k) is an eigenfunction of P with eigenvalue theta_Y in the sector that is odd under the simultaneous flip, and
  kappa(g) = 3 - (3 - kappa_1)/n.
Proof. P w(y_k) = theta_Y w(y_k) because the other factors act on 1. Expand E (sum w_k)^4 = n kappa_1 + 3 n (n - 1). QED
So kappa >= 2 holds for n >= 2 whatever the parts are (even exact bits: two independent bits give kappa = 2), and for n = 1 only if kappa_1 >= 2. ARGUED: at leading order of the strong-coupling expansion in four dimensions g is the normalised sum of the N = b^2 characters of the winding lines and nu is Haar, so kappa = 3 - 1/N.

**4.3 Where (WALL)_M fails although the state space is connected (PROVED; this is row 892's "way 1" made explicit in the class (S+)).** On SU(2) with Haar measure put s(U) = sign tr U and P(U, dV) = [1 + (1 - 2p) s(U) s(V) + r phi(U) phi(V)] dV, with 0 < p < 1/2, phi a bounded continuous class function, even, Int phi = 0, Int phi^2 = 1, orthogonal to nothing else needed, and r > 0 so small that the density is positive. Then P is Markov, symmetric, nonnegative, with strictly positive kernel; its spectrum is {1, 1 - 2p, r, 0}; g = s, theta = 1 - 2p, kappa = 1, rho = r. So W = 0 and (WALL)_M fails for every M and a; GLUE-type smallness of rho holds; the bit is exact. (The kernel is discontinuous on tr = 0; smoothing s on a thin collar makes it continuous and moves kappa to 1 + small.)
Reading. Nothing in (S+), nor connectedness of the group, forces a wall. The wall must come from the dynamics of the gauge field: which configurations a flip passes through, and how long it stays there.

**4.4 What the examples fix (summary).**
| model | kappa | wall time W | (WALL)_40 at a large box | flux heavy? |
|---|---|---|---|---|
| 2D SU(2), 2T, 2O | 2 exactly | n/a | holds, with equality | yes |
| 2D U(1) | 3/2 | (1/3)/(1 - theta^2), about 1/3 step | fails | yes |
| 2D Z_2, product chain with a bit, 4.3 | 1 | 0 | fails | any value |
| n >= 2 independent parts | 3 - (3 - kappa_1)/n >= 2 | n/a | holds | any value |
| 4D Z_2 deep in its ordered phase | near 1 (ARGUED, row 892) | below 1 step (ARGUED: a tilted thin sheet has more area) | fails | no |
So (WALL)_40 is neither necessary (2D U(1)) nor a class property (4.3). It holds exactly at the boundary for one free SU(2) tube and with room for two or more independent tubes.

## Step 5. Attack A: the spectral form of the wall. Exact identities, and why no Poincare-type inequality can give it

Notation. (X_t) is the stationary chain of P. Delta_n := g(X_n) - g(X_0). lambda_bar_n := <h, (1 - P^n) h>/||h||^2 for kappa > 1. By (S+): 1 - rho^n <= lambda_bar_n <= 1.

**Theorem A1 (increment identity; PROVED).** For every n >= 1:
  <h, (1 - P^n) h> = (4/3) kappa (1 - theta^n) - (1/6) E[Delta_n^4].
Proof. Expand E (g_n - g_0)^4 = 2 kappa - 4 E[g_n^3 g_0] - 4 E[g_n g_0^3] + 6 E[g_n^2 g_0^2]. By reversibility E[g_n^3 g_0] = E[g_0^3 g_n] = <g^3, P^n g> = theta^n kappa. And E[g_n^2 g_0^2] = <g^2, P^n g^2> = 1 + <h, P^n h>. So E Delta_n^4 = 8 kappa (1 - theta^n) - 6 (kappa - 1 - <h, P^n h>). QED
This is row 886's (KE) written with increments (there: with V = P g^2 - theta^2 g^2). The new content is the reading below. Check: two-state chain, flip probability p: Delta = +-2 with probability p, E Delta^4 = 16 p, theta = 1 - 2p, kappa = 1: right side (4/3)(2p) - (16/6) p = 0. Diffusion limit: E Delta^4 = o(1 - theta) and the identity becomes row 886's Theorem 4.4.

**Corollary A2 (the jump fraction; PROVED).** Put J_n := E[Delta_n^4]/(8 kappa (1 - theta^n)). Then
(a) 0 <= J_n <= 1 - (3/4)(1 - rho^n)(kappa - 1)/(kappa (1 - theta^n)) <= 1, and J_n = 1 if and only if kappa = 1.
(b) kappa - 1 = (4/3) kappa (1 - theta^n)(1 - J_n)/lambda_bar_n >= (4/3) kappa (1 - theta^n)(1 - J_n).
(c) The wall time W = (kappa - 1)/(kappa (1 - theta^2)) satisfies, for every n,
  W = (4/3) [(1 - theta^n)/(1 - theta^2)] (1 - J_n)/lambda_bar_n,
  so  (4/3) c_n (1 - J_n) <= W <= (4/3) c_n (1 - J_n)/(1 - rho^n),   c_n := (1 - theta^n)/(1 - theta^2), and n theta^(n-1)/2 <= c_n <= n/(1 + theta).
Proof. (a) <h,(1 - P^n)h> >= (1 - rho^n)(kappa - 1) >= 0 in A1. If J_n = 1 then <h,(1-P^n)h> = 0, and rho < 1 forces h = 0. (b), (c): A1 divided by ||h||^2 = kappa - 1, and 0 <= lambda_bar_n <= 1. QED
Reading. A completed flip inside the window [0, n] makes Delta_n = +-2. For an exact bit Delta_n^4 = 16 with probability (1 - theta^n)/2, so J_n = 1. J_n is the share of the fourth moment of the n-step increment that a pure jump process would have. 1 - J_n is the share of flips still in progress.
So the wall branch of (WALL)_M has three equivalent faces (PROVED, from (c) and row 886 Theorem 4.3):
  (W1) wall time: W >= a/M;
  (W2) reverse Poincare for the single vector h = g^2 - 1: <h,(1 - P)h> <= (4 (1 - J_1)/(3 (1 + theta))) (M/a) ||h||^2 (in the diffusion limit: (2/3)(M/a));
  (W3) L^4 continuity of g along the vacuum process: 1 - J_n >= (3/4) lambda_bar_n (1 - theta^2) a/(M (1 - theta^n)) for every n; for n <= a/M and small rates this reads 1 - J_n >= about (3/2) lambda_bar_n a/(M n): flips do not complete inside a/M steps.

**Corollary A3 (a sufficient criterion with explicit constants; PROVED).** If for one n >= 1 and one eps in (0, 1]: E[(g(X_n) - g(X_0))^4] <= (1 - eps) 8 kappa (1 - theta^n), then W >= (2/3) eps n theta^(n-1), and (WALL)_M holds with M = 3 a/(2 eps n theta^(n-1)).
For (WALL)_40 it is enough to have this at n = a/8 with eps = 1/2 when theta^(n-1) >= 0.6 (then M = 3a/(2 x 0.5 x (a/8) x 0.6) = 40).

**Why this face cannot be reached by an inequality of Poincare type (PROVED limits).**
(L1) A Poincare inequality bounds <h,(1-P)h> from below by (1 - rho)||h||^2. (W2) needs it from above. For one given vector an upper bound on its Dirichlet form is a smoothness statement about that vector.
(L2) The standard source of smoothness is the eigen-equation, g = theta^(-n) P^n g. It gives nothing for h, because (P^n g)^2 <= P^n g^2 (Jensen) goes the wrong way: g^2 is rougher than the smoothing of g^2. In the increment form: E Delta_n^4 <= 8 kappa (1 - theta^n) is all that (S+) gives (A2 (a) with rho = 1), and it is attained by the bit.
(L3) Under GLUE no proof can deliver (W1) to (W3) for a near-bit: they contradict Lemma R (Proposition D). A reverse Poincare inequality with constant below 1 - rho is false for every even vector orthogonal to 1.
(L4) Hypercontractivity bounds E Delta_n^4 by 16 kappa and kappa from above (READ row 886 L130, L521). Row 886's 3.1 stands: every general tool bounds kappa from above.
So Attack A ends in an exact dictionary, not a proof. The dictionary says what a proof of the wall branch would have to be: a continuity estimate, in L^4 and at the scale a/M, for the flux function along the vacuum process. By (L3) such an estimate can hold only where the even sector is slow.

## Step 6a. Attack B: the hidden bit, partial centre flips, and what SU(2) adds to connectedness

Setting. Wilson SU(2) on the cube b^3, T = z^|E| K^(1/2) B K^(1/2) (READ row 892 L356). N is the set of the b^2 links of direction i that cross one cut plane x_i = const. For Sigma in N let C^Sigma multiply the links of Sigma by -1 and (V_Sigma f)(U) = f(C^Sigma U).

**B1 (partial centre flips; PROVED, elementary).**
(1) V_Sigma is unitary on L^2(dU), V_Sigma V_Sigma' = V_(Sigma xor Sigma'), V_N = C_i. V_Sigma commutes with K (a product of convolutions by class functions) and with gauge transformations.
(2) V_Sigma B V_Sigma = B D_dSigma, D_dSigma = exp(-2 beta sum over p in dSigma of x_p), where dSigma is the set of space-like plaquettes that contain exactly one link of Sigma and one link of N outside Sigma. So T_Sigma := V_Sigma T V_Sigma = z^|E| K^(1/2) B D_dSigma K^(1/2), and e^(-2 beta |dSigma|) T <= T_Sigma <= e^(2 beta |dSigma|) T as operators. The defect of a partial flip is an equal-time 't Hooft loop on the boundary of Sigma. It is a perimeter term.
(3) (Bochner.) For every unit vector Phi, Sigma -> <Phi, V_Sigma Phi> is positive definite on the group of subsets, so <Phi, V_Sigma Phi> = sum over A of mu_Phi(A) (-1)^|A and Sigma|, with mu_Phi(A) = ||Pi_A Phi||^2 a probability on subsets A of N. A is the set of cut links on which the vector is odd (half-integer spin in the Peter-Weyl basis): the points where electric flux of odd N-ality crosses the cut plane. For Phi in a sector with chi(C_i) = -1, mu_Phi lives on odd |A|; for the vacuum on even |A|.
(4) g = g_L + g_R exactly, for every split N = L + R: g_L := (g - g o C^L)/2 is odd under C^L and even under C^R, g_R := (g + g o C^L)/2 the reverse.
Proof. (1), (2): the plaquette x_p changes sign under C^Sigma exactly when it contains an odd number of links of Sigma; a space-like plaquette in a plane (i, j) contains two links of N or none. (3): the V_Sigma are commuting unitaries with square 1; Pi_A = 2^(-|N|) sum_Sigma (-1)^|A and Sigma| V_Sigma are their joint spectral projections. (4): g o C^R = g o C^L o C_i = -g o C^L. QED
Where it stops. If nu were invariant under the partial flips, (4) and (3) would give an orthogonal splitting of g in L^2(nu) into tube positions and, for single-tube states (mu on singletons), kappa >= 3 - 2 max-share. nu is not invariant. The non-invariance is exactly D_dSigma, of size e^(+-2 beta |dSigma|) with |dSigma| >= 2b for a half. So this splitting is exact and useless at order one: the correction is the thin 't Hooft loop, a perimeter law with rate of order beta. This is the same loss as in row 892's VAR1 and in row 876's (HC). It does not depend on the group: (1) to (4) hold for Z_2, Q_8, 2T verbatim.

**B2 (what SU(2) adds; the statement is PROVED, its use is ARGUED).**
For one link and an angle phi in [0, 2 pi] let K_phi be convolution with the normalised invariant measure of the conjugacy class of rotation angle phi (tr = 2 cos(phi/2)). PROVED (Peter-Weyl): K_phi is self-adjoint, a contraction, commutes with every other class convolution, acts on spin j as sin((2j+1) phi/2)/((2j+1) sin(phi/2)), K_0 = 1, and K_(2 pi) is the centre flip of that link. The Wilson kernel of the link is a positive mixture of the K_phi.
So for SU(2) the flip C_i = product over N of K_(2 pi) is the end of a continuous path of kinetic moves. For Q_8 the path has the stops {0, pi, 2 pi}, for 2T the stops {0, 2 pi/3, pi, 4 pi/3, 2 pi}, for Z_2 only {0, 2 pi}. For U(1) the path is a path of symmetries (row 886 Theorem 5.1). This is the thing SU(2) has and the frozen groups lack.
What it buys (ARGUED; an action count, not a bound). Spread a flip over n time steps and over d cut planes along direction i, with a common rotation axis field. Kinetic cost: about pi^2 beta b^2/(2 d n). Magnetic cost: the rotated links meet transverse links whose colour directions are not parallel to the axis; per plaquette and step about kf (2 pi s/d)^2, s the progress, kf of order one (it is beta times the squared curvature of the transverse plaquettes); in total about (4 pi^2/3) kf b^2 n/d. The sum is least at n = sqrt(3 beta/(8 kf)) and equals about 2 pi^2 sqrt(2 beta kf/3) b^2/d.
Three readings. (i) Thickness in time alone (d = 1) leaves an area law; it only replaces 2 beta u by a number of the same size. (ii) The optimal duration is of order sqrt(beta) lattice steps for every d. An abelian-profile flip is never as long as a/40. This agrees with Proposition D: at a GLUE box no flip is that long. (iii) At d = b the cost is of order sqrt(beta) b: a perimeter law, the scaling of VAR1 (row 892 L359). An order-one flux weight needs more: the vacuum's own disorder must screen the axis field (the non-abelian thick vortex). That is (S1)/(VF) of row 892. So the two stops of row 892 are one stop, and the wall form adds no easier face.

**B3 (reflection positivity across the flux).** I add nothing proved to row 876's Lemma RPF and its dichotomy (READ L430-444). Under GLUE, Corollary D2 sharpens its second branch: a sector that is not heavy is a near-bit with kappa <= 1.13 to 1.21, so the long-range order of the lines is the order of one coherent sign.

**Stop of Attack B.** For a hidden bit to be excluded by a wall argument, the wall would have to outlast the even relaxation time; no flip of the kinds I can construct does. For it to be excluded directly, one needs a lower bound on a non-perturbative vortex weight. Neither follows from (S+), connectedness, B1 or B2.

## Step 6b. GUIDE run: the smallest lattice with a toron valley and a wall (a run can refute or guide; it proves nothing)

Script: /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane894/scripts/toron_guide.py (numpy only, about 10 seconds, under 100 MB). Outputs: toron_guide_out16.txt and toron_guide_out_su2.txt in the lane894 directory. Criteria were written in the script header before the run.
Model. Wilson theory in 2+1 dimensions on a 1 x 1 spatial torus: two links U1, U2, one space-like plaquette x_P = (1/2) tr(U1 U2 U1^-1 U2^-1) = 1 - 2 sin^2(alpha_1) sin^2(alpha_2) sin^2(gamma), one time-like plaquette per link. T = K^(1/2) B K^(1/2) on conjugation-invariant functions. Flux sector: odd under U1 -> -U1. For SU(2) I use the orthonormal basis f_(j1,J)(alpha_1) f_(j2,J)(alpha_2) P_J(cos gamma) (K is diagonal there), truncated at jmax, with Gauss quadrature. For 2T and Q_8 the model is finite and exact. This is the lattice form of row 892's suggestion (L477): a model where both the wall (trace-zero holonomy) and the flip rate are computable.
Criteria. C0 (norms of both ground vectors on the grid equal 1 to 1e-15): met. C1 (beta -> 0): SU(2) kappa 1.990, 2T 1.9994, Q_8 3.88 at beta 0.25, tending to 2, 2, 4: met. C2 (Lemma R, r_W <= 1): met in every row. C3 ((KE-ineq), i.e. lam_bar W <= 1): met in every row. C4 (jmax against jmax - 1): all digits shown agree.

SU(2) (r_W = W (1 - rho); J_1 = jump fraction of Corollary A2; last column (1 - rho)/(1 - theta)):
| beta | kappa | theta | rho | W (steps) | r_W | lam_bar | J_1 | even rate / flux rate |
|---|---|---|---|---|---|---|---|---|
| 0.25 | 1.9900 | 0.0661 | 0.0028 | 0.500 | 0.498 | 0.997 | 0.60 | 1.07 |
| 1.0 | 1.8612 | 0.2927 | 0.0508 | 0.506 | 0.480 | 0.953 | 0.53 | 1.34 |
| 1.5 | 1.7317 | 0.4453 | 0.1149 | 0.527 | 0.467 | 0.895 | 0.49 | 1.60 |
| 2.3 | 1.5305 | 0.6493 | 0.2443 | 0.599 | 0.453 | 0.778 | 0.42 | 2.15 |
| 2.6 | 1.4665 | 0.7082 | 0.2928 | 0.638 | 0.451 | 0.732 | 0.40 | 2.42 |
| 4.0 | 1.2518 | 0.8746 | 0.4662 | 0.856 | 0.457 | 0.565 | 0.32 | 4.26 |
| 8.0 | 1.0329 | 0.98534 | 0.5972 | 1.094 | 0.441 | 0.444 | 0.28 | 27.5 |
| 12.0 | 1.0038 | 0.998009 | 0.5921 | 0.959 | 0.391 | 0.478 | 0.31 | 205 |
| 16.0 | 1.0005 | 0.999679 | 0.5819 | 0.822 | 0.344 | 0.528 | 0.35 | 1302 |
2T: kappa 1.999, 1.954, 1.858, 1.675 (beta 2.3), 1.633 (2.6), 1.606 (3), 1.622 (4), 1.715 (6), 1.766 (8); W 0.50, 0.54, 0.60, 0.80, 0.94, 1.18, 2.17, 6.5, 18.1 steps; r_W between 0.487 and 0.579 in every row.
Q_8: kappa 3.88, 2.95, 2.48, 2.12 (2.3), 2.05 (2.6), 2.005 (3), 1.956 (4), 1.939 (6), 1.938 (8); r_W from 0.74 down to 0.48.

What the run says (GUIDE).
(G1) One tube of Wilson SU(2) is below the threshold at every coupling: kappa < 2 for every beta > 0 in the table, 1.53 at beta 2.3 and 1.47 at beta 2.6, and W is between 0.5 and 1.1 lattice steps. So (WALL)_40 fails in this model for every a >= 82, at every coupling tested. The model has a connected group, the Wilson action, gauge invariance, exact centre symmetry and a positive transfer operator. It is not an SH box (b = 1). Reading: nothing in the one-tube structure gives (WALL)_40; at an SH box it can only come from the transverse extent (at least two nearly independent tube positions, Step 4.2: kappa = 3 - (3 - kappa_1)/n, and kappa_1 about 1.5 gives 2.25 at n = 2 and 2.6 at n = 4).
(G2) The wall is never thick on the even clock: r_W = W (1 - rho) stays between 0.34 and 0.50 for SU(2), and between 0.48 and 0.74 for the frozen groups. A flip lasts about half an even relaxation time, in the hidden-bit regime (beta 8 to 16, kappa - 1 from 0.03 to 0.0005) as much as at strong coupling. Lemma R (r_W <= 1) is within a factor 2 to 3 of sharp. With r_W about 0.45 the wall branch of (WALL)_M can hold only when a (1 - rho) <= 0.45 M, that is 18 for M = 40.
(G3) The hidden bit of the connected group forms with the even gap open: at beta 16, kappa - 1 = 5e-4 and 1 - theta = 3.2e-4 while 1 - rho = 0.42. The even sector does not slow down with the bit in lattice units (the toron scale is beta^(-1/3) per step, 0.4 here). So the abstract form of (HB), "a hidden bit forces an even mode as slow as the bit", is false for SU(2) in this model. What survives is only the geometric form: in a box of side b the toron and gluon levels are of order 1/b, so m a = m b/24 is small. (HB) at an SH box is a statement about the scaling with b, not about the bit.
(G4) The frozen groups behave the other way round on this lattice: no near-bit forms (kappa stays above 1.6 for 2T and above 1.93 for Q_8), and their flips are long in lattice steps (W = 18 steps for 2T at beta 8) because every move is a rare hop. So on one tube the profile "SU(2) passes, 2T fails" is not present at all; it is a property of large boxes.
(G5) Jump fraction: J_1 is between 0.28 and 0.60. One-step increments of g are far from pure jumps and far from diffusive.
Limits. One plaquette, 2+1 dimensions, no transverse extent. Nothing here is evidence about an SH box at order one. The run refutes two general expectations (a flip that is long on the even clock; an even sector that slows with the bit) and guides the reading of (WALL)_40 as a statement about the number of independent tubes.

## Step 6c. Beyond g^2: fusing two different flux levels. One light level per flux sector (PROVED)

Row 892's way 3 looked for an even trial vector other than g^2 - 1 and found none with a usable sign. There is one: the product of two orthogonal eigenfunctions of the same flux sector. Its vacuum component is exactly zero.

**Lemma B4 (fusion of two flux levels; PROVED).** Assume (S+). Let g, f be real, in the same sector chi, P g = theta g, P f = theta_2 f, E g^2 = E f^2 = 1, E g f = 0, with finite fourth moments kappa_g, kappa_f. Then
 (a) (theta + theta_2 - rho - 1/2) <g^2, f^2> <= (1/2) <f^2, P g^2>;
 (b) [(1 - rho) - (1 - theta) - (1 - theta_2)] <g^2, f^2> <= (1/2) sqrt(kappa_g kappa_f (1 - theta^2)(1 - theta_2^2)), and <g^2, f^2> >= 1 - sqrt((kappa_g - 1)(kappa_f - 1)).
Proof. e := g f is flip-invariant (chi^2 = 1) and E e = E g f = 0. So <e, P e> <= rho ||e||^2 = rho <g^2, f^2>. Next, g_0 g_1 = (g_0^2 + g_1^2)/2 - (g_1 - g_0)^2/2, so <e, P e> = E[g_0 g_1 f_0 f_1] = theta_2 <g^2, f^2> - (1/2) E[(g_1 - g_0)^2 f_0 f_1], using E[g_0^2 f_0 f_1] = <g^2 f, P f> = theta_2 <g^2, f^2> and reversibility for the term with g_1^2. Also |E[(g_1 - g_0)^2 f_0 f_1]| <= E[(g_1 - g_0)^2 (f_0^2 + f_1^2)/2] = E[(g_1 - g_0)^2 f_0^2] = <f^2, P g^2 - 2 theta g^2 + g^2>. Combine: (a). For (b): <f^2, P g^2> = <f^2, g^2> - <h_f, (1 - P) h_g> with h_f = f^2 - 1, h_g = g^2 - 1, and by Cauchy-Schwarz for the nonnegative form 1 - P, then (KE-ineq) for each of f and g (it uses only Jensen, so it holds for every eigenfunction): |<h_f, (1 - P) h_g>| <= sqrt(kappa_f (1 - theta_2^2) kappa_g (1 - theta^2)). The last inequality is Cauchy-Schwarz. QED

**Corollary B4' (an exact bit makes the flux sector a copy of the even sector; PROVED).** If g^2 = 1 almost surely, then multiplication by g is a unitary map of L^2(nu) that carries the even sector onto the sector chi and 1 onto g, and g P g = P - 2 F, where F has the kernel P(x, dy) 1[g(x) != g(y)], row sums (1 - theta)/2 and norm at most (1 - theta)/2. So the ordered eigenvalues satisfy |theta_k - rho_(k-1)| <= 1 - theta for every k (theta_1 = theta, rho_0 = 1, rho_1 = rho). In particular theta_2 <= rho + (1 - theta).
Proof. g^2 = 1 makes the multiplication unitary and an involution. g(x) P(x, dy) g(y) = P(x, dy)(1 - 2 1[g(x) != g(y)]). P g = theta g gives the row sum: 1 - 2 q(x) = theta. A symmetric kernel with nonnegative entries and row sums r has norm at most r (Schur). Weyl's inequality gives the eigenvalue statement. QED
Reading. This is the exact sense of "hidden": with a bit, the flux sector has no state of its own. Every flux level is an even level carried by the bit.

**Proposition B5 (at most one light level per flux sector; PROVED).** Assume (S+). For an eigenfunction in a flux sector put x := (1 - theta^2)/(1 - rho). Two orthogonal eigenfunctions of the same sector cannot both have x < 0.30. More precisely, with x <= x_2 < 1 and c := sqrt(x x_2/((1 - x)(1 - x_2))) < 1: (1 - x - x_2)(1 - c) <= c/2.
Proof. Lemma R holds for every eigenfunction of the sector (Jensen and the bound rho on h_f): (kappa - 1)/kappa <= x, so kappa <= 1/(1 - x) and kappa - 1 <= x/(1 - x). Then sqrt((kappa_g - 1)(kappa_f - 1)) <= c and sqrt(kappa_g kappa_f (1 - theta^2)(1 - theta_2^2)) <= (1 - rho) c. Also 1 - theta <= 1 - theta^2 = x (1 - rho). Insert in B4 (b) and divide by 1 - rho. At x = x_2 = t the inequality reads (1 - 2t)^2 <= t/2, which fails for t < 0.3048; its left side decreases and its right side increases in each of x, x_2, so it fails whenever both are below 0.3048. QED

**Corollary B6 (the flux sectors at a GLUE box; PROVED).** Assume GLUE as in Corollary D1 (a (1 - rho) >= 51.5). Then in each of the seven sectors at most one eigenvalue of P has theta_k^a > e^(-7.85) = 1/2560. If the top one has theta^a >= 1/20, every other eigenfunction f of the sector has, by B4 (b) with kappa_g <= 1.132, theta_2^a <= e^(-a (1 - theta_2)) with 1 - theta_2 >= about (1 - rho)(1 - x - sqrt(x x_2 ...)): its level lies at the even gap up to the factor shown.
Proof of the first sentence. theta_k^a > t_0 gives 1 - theta_k^2 <= (2/a) log(1/t_0), so x_k <= 2 log(1/t_0)/51.5, which is below 0.3048 when log(1/t_0) < 7.85. Apply B5. QED
Reading. Under GLUE the scenario left open by Corollary D2 is now exact in three points: (1) the light flux level is a near-bit, kappa <= 1.13; (2) it is the only light level of its sector; (3) every other flux level sits near an even level (B4', B4). That is a Z_2 topological order: eight vacua, one per sector, and nothing else below the gap. This is what (WALL)_40, equivalently (KURT)_1, must exclude at the SH box.
A possible use (ARGUED). The scenario dies if the flux sector has a second state of its own below the even gap: a unit vector Phi in the sector, orthogonal to Psi_chi, with <Phi, (1 - T/lambda_0) Phi> < 0.3 (1 - rho)/2 or so. In a confined box the candidates are the tube at non-zero transverse momentum; but there E is far above m and the criterion is not needed. In the scenario itself I have no candidate: the half-flip partner V_Sigma Psi_chi of B1 is exactly orthogonal to Psi_chi (PROVED: translate by half the box, V_(Sigma^c) = C_i V_Sigma) but costs the thin 't Hooft loop, <V Psi, T V Psi> >= e^(-2 beta |dSigma|) lambda_chi, a perimeter factor again.

Correction to Step 6c (labels). Corollary B6: only its first sentence is PROVED (at most one eigenvalue with theta_k^a > 1/2560 per sector). Its second sentence is loose; read it as Proposition B5 applied to the pair (top level, any other level). In "A possible use" the exact criterion is: a unit vector phi in the sector, orthogonal to g, with 1 - <phi, P phi>^2 < 0.3048 (1 - rho), contradicts x < 0.3048 for the top level (PROVED: <g, P phi> = theta <g, phi> = 0, so by min-max the second eigenvalue of the sector is at least min(theta, <phi, P phi>); then B5).

## Step 6d. GUIDE check of the identities on random chains

Script: /private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane894/scripts/ident_guide.py (numpy, seconds). 600 random reversible chains with a positive, positive-definite kernel and an involution, 6 to 16 states, 286 of them near-bits (kappa < 1.2). Criteria written first. Result: Theorem A1 holds to 5e-15 for n = 1, 2, 3; no violation of Lemma R, Corollary A2 (a), (KE-ineq), Lemma B4 (a) and (b) (top level against the second and the third), Proposition B5 (no chain has two levels with x < 0.3048), Proposition D (random a, M). A run of this kind can only refute. It did not.

## Step 7. Fact tests

**7.1 The statement (WALL)_40 itself.**
| rival | GLUE at an SH box | kappa | (WALL)_40 | what the chain concludes |
|---|---|---|---|---|
| U(1) Coulomb, 4D | fails (even sum not small) | 3/2 for the pure cosine (READ row 886) | holds by the wall branch: W = (1/3)/(1 - theta^2), r_W = 2/3 for Gaussian flux (m = 4E), and a (1 - rho) is of order e^2/12 (ARGUED with row 892's sizes) | nothing; GLUE fails |
| Z_2 at beta 5/2, 4D | holds (ARGUED: ordered, gapped) | near 1 (ARGUED) | fails: by Proposition D it would need kappa >= 2 | nothing; and (CORE) is false there, as it must be |
| frozen 2T, Q_8, 4D, in their ordered phases | holds (ARGUED) | near 1 (ARGUED) | fails, same reason | nothing |
| SU(2), one plaquette (GUIDE, 6b) | n/a (b = 1) | 1.53 at beta 2.3, below 2 for every beta | fails for every a >= 82 | not an SH box |
| SU(2), 2D (PROVED, 4.1) | holds in large boxes | 2 exactly | holds with equality | flux heavy, true |
| U(1), 2D (PROVED, 4.1) | holds | 3/2 | fails in large boxes | flux heavy all the same: (WALL)_40 is not necessary |
The profile row 892 asked for is confirmed, and sharpened by Proposition D: wherever GLUE holds, "(WALL)_40 fails" means exactly "kappa < 2".

**7.2 Each proved step.**
| step | U(1) Coulomb | Z_2 at beta 5/2 | frozen 2T, Q_8 | verdict |
|---|---|---|---|---|
| Proposition D, Corollaries D1, D2 | hypothesis a (1 - rho) > M fails; empty | apply: (WALL)_40 <=> kappa >= 2, false there; D2 describes the ordered phase (near-bit) | same | group-blind; no claim that could be false in a rival |
| Theorem A1, Corollaries A2, A3 | identities | identities; J_n near 1 at once (thin sheet) | same | group-blind dictionary |
| 4.1 (2D values) | kappa = 3/2 | kappa = 1 | 2T: 2, Q_8: 4 | exact; shows the threshold 1 is the one-tube SU(2) value and that 2T shares it |
| B1 (partial flips) | holds | holds | holds | group-blind; stops at the thin loop for every group |
| B2 (class-angle path) | the path is a path of symmetries | two stops only | three and five stops | the one SU(2)-specific item; PROVED as a statement, ARGUED in its use |
| Lemma B4, B4', B5, B6 | B5 on the degenerate pair (cos, sin) of flux one gives 1 - theta^2 >= 0.30 (1 - rho), i.e. m <= 6.6 E; the truth is m <= 4E (READ row 886 L339): consistent | describe the ordered phase: one light level per sector, the flux sector a copy of the even one | same | group-blind; they sharpen the scenario, they do not exclude it |
| 6b (GUIDE) | not run | not run (2D Z_2 value is 1) | run: no near-bit on one tube | guide only |
No step uses a worst-case, single-site, vertex-block, background-uniform or annealed quantity. Every statement is about one function under the true vacuum measure.

**7.3 What a proof of the open statement must look like (ARGUED from 7.1, 7.2, Step 6).**
- It must fail for Z_2 at beta 5/2 and for frozen 2T: so it cannot be an identity of the class (S+), cannot use only Haar moments up to degree 5 (2T agrees with SU(2) there, and has kappa = 2 on one tube as SU(2) does), and cannot be a perimeter-loss argument (B1, VAR1, (HC) all lose a thin loop for every group).
- It cannot be a wall argument at the SH box (Proposition D).
- It is not a one-tube property (6b: one SU(2) tube has kappa < 2 at every coupling). It must use the transverse extent: at least two nearly independent tube positions, kappa = 3 - (3 - kappa_1)/n.
- A further rival, not in the lane's list (ARGUED, recalled physics, decides nothing): SU(2) with two adjoint Higgs fields has a phase with unbroken gauge group Z_2, a gap, and a deconfined centre. A proof of (KURT)_1 that used only connectedness, positivity and reflection positivity would apply to that model with the Higgs fields integrated out as a non-local positive weight. So a proof must use the locality of the pure plaquette action as well.

## Step 7b. A sharper consumer bound: the threshold 2 can be lowered at the same GLUE level (PROVED from READ inputs)

READ (D/library/gap-brainstorm2-max.md L490-492, item 2 and the first line of the proof of Theorem SQ-F; the trace bound is Corollary 6.3 of gap-loop-eq-opus.md, row 754, checked by row 756, re-derived in row 876; check 883: the SQ-F display HOLDS): for a even, a/2 >= 3 and chi nonzero, p_chi(a) <= (1 + S_ev(a/2)) theta_chi^(a/2).

**Corollary K' (PROVED from that line and Lemma R).** Put A := a (1 - rho). Then
  p_chi(a) <= (1 + S_ev(a/2)) exp( - A (kappa_chi - 1)/(4 kappa_chi) ).
Proof. theta^(a/2) <= exp(-(a/2)(1 - theta)); 1 - theta >= (1 - theta^2)/2; Lemma R: 1 - theta^2 >= (1 - rho)(kappa - 1)/kappa. QED
With GLUE as in Proposition W (S_ev(a/2) <= 1, A >= 51.5 by Corollary D1): p_chi(a) <= 2 exp(-12.875 (kappa - 1)/kappa). This is at most 1/80 as soon as (kappa - 1)/kappa >= log(160)/12.875 = 0.3942, that is
  kappa_chi >= 1.66.
So Proposition W's conclusion Q_0 <= 1/20 (four terms, each at most 1/80; READ row 892 L389) needs only Var(g^2) >= 0.66 for the seven sectors, not Var(g^2) >= 1. In general the needed bound is Var(g^2) >= 4 log 160/(A - 4 log 160): 0.113 at A = 200, 0.021 at A = 1000. Against Theorem SQ-F's exponent (kappa - 1)/(8 kappa) on S_ev(a) this gains a factor 2 in the exponent and replaces log(1/S_ev(a)) by a (1 - rho).
Reading with 4.2 and 6b (GUIDE): two independent tubes with one-tube value 1.5 give kappa = 2.25, above 1.66. One tube at beta 2.3 (1.53) is below it.

## Step 8. Assembly

**8.1 Errata (found on my re-read of each step).**
- Step 3.2 uses theta < 1 and rho < 1; both follow from the strictly positive kernel (1 is a simple eigenvalue). I use the one-line (min) form of (WALL)_M. In the "if kappa <= 2 then" form of row 892 L397 the two forms differ only at kappa = 2 exactly (2D SU(2) sits there).
- Step 4.1 (d): for 2T, 2O the claim that chi is the top odd character under the Wilson weight is checked for 2T (the two other spinor characters have smaller coefficient because the order-6 classes enter with -1/2 each); for 2O I did not check it (the value E chi^4 = 2 is exact either way).
- Step 4.2, last sentence, and the 4D Z_2 row of 4.4 are ARGUED.
- Step 5: two constants were corrected in place ((W2) and the bounds on c_n).
- Step 6c: see the correction placed before Step 6d.
- Step 6a B2: the action count is an estimate with an unknown constant kf. It carries no proof weight.
- Step 6b: C3 was printed only for the rows of the first run; for the others lam_bar W <= 1 can be read off the table.
- Steps 3.5 (iii), 7.1 (U(1) row, Z_2 and frozen rows), 7.3: ARGUED.

- Step 6b, output files. The first output file (toron_guide_out16.txt) has two SU(2) rows printed as nan (beta 0.25 and 1.0 at 2 jmax = 16): a numerically negative Bessel ratio at high order. The script was fixed (clip at 0) before the second run; the SU(2) table in 6b is from the second file (toron_guide_out_su2.txt). The 2T and Q_8 rows are from the first file and are not affected.
- Step 6b, a check by hand of both codes (leading order in beta; ARGUED, not a proof). With c_(1/2) = beta/4, c_1 = beta^2/24, c_(3/2) = beta^3/192 and E_(U2)[x_P] = (1 + chi_1(U1))/4: Psi = chi + eps chi_(3/2)(U1), Omega = 1 + eps' (chi_1(U1) + chi_1(U2)), eps = beta^2/(4 sqrt 48), eps' = beta^2/(4 sqrt 24), so kappa = 2 + 4 eps E[chi^3 chi_(3/2)] - 2 eps' E[chi^4 chi_1] = 2 + (4 x 0.0361 x 1 - 2 x 0.0510 x 3) beta^2 = 2 - 0.162 beta^2 for SU(2). The run gives (2 - kappa)/beta^2 = 0.160 at beta 0.25 and 0.155 at 0.5. For 2T the spin-3/2 character splits into two irreducible characters, each with coefficient beta^3/96, and E[chi^3 chi_(3/2)] = 2, E[chi^4 chi_3] = 4: kappa = 2 + (4 x 0.0510 x 2 - 2 x 0.0510 x 4) beta^2 = 2 + 0 beta^2. The run gives 2 - kappa = 6e-4 at beta 0.25. Also theta = c_(1/2)(1 + beta/4) = 0.0662 at beta 0.25 against 0.0661 in the run. So one tube of SU(2) leaves the value 2 downward at order beta^2, and 2T first differs from SU(2) exactly here, through its degree-6 moments.

**8.2 Answers to the brief.**
Q1. What does (WALL) say physically? W = Var(g^2)/(E g^4 (1 - theta^2)) is the duration of one flip of the centre bit, in lattice steps: the thickness in time of the centre vortex sheet that carries the flip. (WALL)_M says W >= a/M, or else g is at least as spread as two independent pieces (kappa >= 2). Lemma R is the opposite bound W <= 1/(1 - rho).
Q2. Is it a statement about the wall at the box where the lane uses it? No (PROVED, Proposition D, Corollary D1). Wherever a (1 - rho) > M, in particular under the GLUE hypothesis of Proposition W, (WALL)_M is the bare statement kappa >= 2, that is (KURT)_1 of rows 876 and 886. The hypothesis under which Proposition W uses (WALL)_M is exactly the hypothesis under which (WALL)_M has no wall content. So Proposition W is Proposition K with eta = 1; the passage through the wall and Lemma R adds no easier target. The node "(HB) = (WALL)_M" of row 892's table is the node (KURT)_1.
Q3. Can it fail in a model with the right fact-test profile? In the class, yes: Example 4.3 (connected SU(2), positive kernel, exact bit, PROVED); one Wilson SU(2) tube at every coupling tested (GUIDE: kappa = 1.53 at beta 2.3, W below 1.1 steps); 2D U(1) (PROVED: fails, harmlessly). At an SH box of 4D Wilson SU(2) it is not decided. There it is expected to hold through kappa near 3 (ARGUED in rows 876, 886), and by Proposition D it holds exactly when the box has no near-bit.
Q4. Spectral, Poincare and reverse-Poincare arguments. The wall branch is equivalent to a reverse Poincare inequality for the one vector g^2 - 1 and to an L^4 continuity bound for g along the vacuum process (Theorem A1, Corollaries A2, A3: exact, with constants). No inequality of Poincare, Jensen or hypercontractive type gives it; under GLUE it is false for every near-bit (limits L1 to L4).
Q5. The hidden-bit picture. Under GLUE the alternative to a heavy flux is now exact (PROVED: Corollary D2, Lemma B4, Corollary B4', Proposition B5, Corollary B6): a near-bit with kappa <= 1.13 (for theta^a >= 1/20), the only level of its sector above 1/2560 at time a, the rest of the sector a copy of the even sector. This is a Z_2 topological order of the box.
Q6. Reflection positivity across the flux, and partial flips. Exact structure (B1), no bound at order one: every splitting of g into tube positions costs a thin equal-time 't Hooft loop, for every group.
Q7. What SU(2) has that Q_8, 2T lack: the continuous path of class convolutions K_phi from 1 to the flip (B2, PROVED as a statement). Its use is the non-abelian thick vortex, which is row 892's (S1)/(VF). I found no way to use it short of that.

**8.3 Status.**
PROVED here (by hand; each proof re-read once by me; checked by no one; identities also run on 600 random chains, GUIDE):
1. Proposition D and Corollary D1: if a (1 - rho) > M then (WALL)_M <=> kappa >= 2; under GLUE at 160^(-16), a >= 82: a (1 - rho) >= 51.5, so (WALL)_40 <=> (KURT)_1.
2. Corollary D2: under that GLUE, theta^a >= t_0 forces (kappa - 1)/kappa <= 2 log(1/t_0)/51.5 (kappa <= 1.132 at t_0 = 1/20).
3. Theorem A1: <h,(1 - P^n)h> = (4/3) kappa (1 - theta^n) - (1/6) E[(g(X_n) - g(X_0))^4]. Corollaries A2, A3: the jump fraction J_n; W = (4/3) c_n (1 - J_n)/lambda_bar_n; (WALL)_M from E Delta_n^4 <= (1 - eps) 8 kappa (1 - theta^n) with M = 3a/(2 eps n theta^(n-1)).
4. Section 4.1: in two dimensions kappa = E_G chi^4 exactly: SU(2) 2, 2T 2, 2O 2, Q_8 4, U(1) 3/2, Z_2 1, at every coupling and size; (WALL)_M holds with equality for SU(2) and fails for U(1) in large boxes. Section 4.2: kappa = 3 - (3 - kappa_1)/n for n independent parts. Section 4.3: an exact bit on connected SU(2) inside the class.
5. B1: partial centre flips, their defect D_dSigma, the Bochner measure of flux crossings, the exact splitting g = g_L + g_R, the exact orthogonality of the half-flip partner.
6. B2 (statement only): the class convolutions K_phi interpolate between 1 and the centre flip.
7. Lemma B4, Corollary B4', Proposition B5, Corollary B6 (first sentence): fusion of two flux levels; an exact bit makes the flux sector a copy of the even sector within 1 - theta; two orthogonal levels of one flux sector cannot both have 1 - theta^2 < 0.30 (1 - rho); under GLUE at most one level per sector has theta_k^a > 1/2560.
8. Corollary K': p_chi(a) <= (1 + S_ev(a/2)) exp(-a (1 - rho)(kappa - 1)/(4 kappa)); under Proposition W's GLUE the needed bound is kappa >= 1.66, not 2.
GUIDE: Step 6b (one-plaquette model for SU(2), 2T, Q_8) and Step 6d (identities on random chains).
ARGUED: the physical readings of Step 3; kappa = 3 - 1/N at leading strong coupling; the 4D rival rows of 7.1; the action count of B2; 7.3.
NOT PROVED: (WALL)_40, equivalently kappa >= 2 (or the weaker kappa >= 1.66), for any sector of 4D SU(2) at an SH box at any coupling in the band. Nothing at order one is proved for the 4D theory. No mass gap. The statement is not refuted either.
OPEN, in its sharpest form after this note: at one SH box with GLUE, Var(g^2) >= 0.66 for the seven flux ground functions. By D2, B5, B6 this is the exclusion of a Z_2 topological order of the box (eight near-degenerate vacua, kappa <= 1.13). By 6b and 4.2 it is a statement about transverse extent: at least two nearly independent tube positions. Three equivalent-in-difficulty faces are on record: the vortex weight ((S1)/(VF), row 892), a creation operator in half the box ((HC), row 876), and a second light flux level of the sector's own (B5: a unit vector in the sector, orthogonal to g, with 1 - <phi, P phi>^2 < 0.30 (1 - rho), kills the scenario; the half-flip partner is such a vector up to a thin-loop factor). I do not claim any of these is the route that closes.

**8.4 Limits of this note.**
- Rows 886 and 892 are the base; row 892 is unchecked (its check is row 893). I used from it only Lemma R, the statements of Propositions K and W, and S_ev(a) >= rho^a, each of which I re-derived in one line or READ with its line number. Corollary K' rests on the READ trace bound p_chi(a) <= (1 + S_ev(a/2)) theta^(a/2) (row 754, checked by row 756; I did not re-open that row).
- The GUIDE model has one plaquette in 2+1 dimensions. It says nothing quantitative about an SH box.
- I opened no paper and no Sussman-Alpoge source in this run. Statements about the account are READ from lane files that cite it (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text). Balaban's estimates are not used here. The first-passage action was not opened; Steps 3, 5, 6c, 7b use only (S+), which holds for any action with a strictly positive, positive-definite transfer kernel and exact centre symmetry.
- Recalled physics (toron valley, vortex thickness, the adjoint Higgs rival) is ARGUED and carries no proof weight.

RESULT: Row 894 (Claude Fable 5.2 max, unchecked): (WALL)_40 is NOT proved and NOT refuted for 4D SU(2) at an SH box; it is decided as a statement: PROVED that wherever a(1 - rho) > 40, in particular under the GLUE hypothesis of Proposition W (a(1 - rho) >= 51.5), (WALL)_40 has no wall content and is exactly kappa >= 2, i.e. (KURT)_1, so the wall route of row 892 is Proposition K with eta = 1 and "(HB) = (WALL)" is not an easier node; PROVED the exact dictionary of the wall branch (increment identity <h,(1-P^n)h> = (4/3)kappa(1-theta^n) - (1/6)E[Delta_n^4], jump fraction, reverse-Poincare and L^4-continuity faces, with constants) and that no Poincare/Jensen-type inequality gives it; PROVED the exact shape of the scenario to exclude under GLUE (a near-bit with kappa <= 1.13, the only light level of its sector: two orthogonal levels of one flux sector cannot both have 1 - theta^2 < 0.30(1 - rho); an exact bit makes the flux sector a copy of the even sector), i.e. a Z_2 topological order of the box; PROVED exact rival values in two dimensions (SU(2), 2T, 2O: kappa = 2 exactly, so the threshold is attained; U(1): 3/2, (WALL)_40 fails there harmlessly; Z_2: 1) and an in-class connected counterexample; PROVED that the consumer needs only kappa >= 1.66 at the same GLUE level (p_chi(a) <= (1 + S_ev(a/2)) exp(-a(1-rho)(kappa-1)/(4 kappa))); GUIDE: one Wilson SU(2) tube has kappa < 2 at every coupling (1.53 at beta 2.3) and a flip lasting about 0.45 even relaxation times, so (WALL)_40 can hold at an SH box only through transverse extent (two or more nearly independent tubes); OPEN: Var(g^2) >= 0.66 for the seven flux ground functions at one SH box, equivalently no Z_2 topological order there, which needs a non-perturbative vortex weight ((S1)/(VF)), a half-box creation bound ((HC)) or a second light flux level (B5), none of which is supplied here.
