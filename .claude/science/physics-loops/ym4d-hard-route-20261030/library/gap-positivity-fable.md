lead: anthropic/claude-fable-5-2/max laptop-subagent

# gap-positivity-fable (FINISH row 1303)

Status of this file: finished 2026-11-20T17:18Z (date -u); started 16:15Z. Each step appended its result. Labels used:
PROVED, ARGUED, GUIDE, OPEN (with RECALLED for a known result used from memory, and GIVEN for a named input).

## Step 0. File created

Target: four-dimensional SU(2) Yang-Mills mass gap in the sense of Jaffe and
Witten. Working question (owner hint, 2026-11-20): is there a hidden
sign-definite object for the centre-neutral sector of the Wilson measure that
gives the missing neutral inequality, or can one prove that no object of a
named class can?


## Step 1. What was read, the owner's hint, and the plan (written 2026-11-20, first response)

Provenance: Claude Fable 5.2, max effort, laptop subagent, one session. Author only. Checked by no one.
Labels: PROVED (every step is written here, by hand), ARGUED (a step is missing or rests on a named input),
GUIDE (numeric or heuristic, never a proof step), OPEN.

### 1.1 Sources read (statements about the record, not evidence)

- `parts/gap.md` L1-104 and the first words of each obligation line.
- FINISH rows 737, 744, 1193, 1209, 1213, 1241, 1247, 1258, 1265, 1303 (the row lines).
- `library/gap-mini-solve-n-fable.md` (row 1213) in full. `library/gap-mini-solve-e-fable.md` (row 1194) in full.
- `library/gap-solve-def-check-astra.md` items on row 1194 (L110-129). `library/gap-solve-batch4-check-astra.md` L181-200 and L478-488.
- `library/prior/gap-o4-pinned-cell-read-opus.md` L100-215 (the digest of the posted O(4) proof, Sections 3.3-3.12).
- `library/gap-means-max.md` L74-96 (Proposition NS, the surface S_0, Corollary NS0).
- The remark of L. Alpoge (https://alpo.ge/remark.pdf, 4 pages, unrefereed), fetched into a new empty folder outside the repository and read with Python run with `-I`. Not committed.

### 1.2 Where the problem stands (cited, not re-derived)

The lane reduces the Jaffe-Witten gap clause to the account's continuum datum and one lattice statement, (N-phys)
(row 1161; Theorem BP of row 1179, check 1183). (N-phys) is a bound, uniform in the cutoff, on the centre-neutral
excited trace s(u; n) of the vacuum-normalised periodic transfer operator on a spatial cube of fixed physical side:
s(u; n) <= 1/2 for some 3 <= u <= n/512. Every route on file stops at one estimate at one physical scale that is false
for a massless comparison model (rows 998, 1219). The mass gap is OPEN. This file does not prove it.

### 1.3 The hint, in the terms of this problem (ARGUED; a reading, no claim about the remark's correctness)

The remark is a timeline, not a proof text. Its mechanism, as far as it can be read: a quantity with a definite sign
is written in two ways. One way is a count, or a positivity of the Weil functional on a test function, realised
through determinants. The other way is a main term plus a remainder that is bounded by repeated Parseval steps.
Because the sign is known, no cancellation between inverse roots has to be proved. In the remark's words:
"opposite signs meaning no cancellation of inverse roots" (Alpoge, remark, footnote 3). Multiplicity in the sense of
Stepanov is supplied there by a chain of theta lifts. I use only this shape. I use no statement of the remark as an input.

The same shape for the neutral transfer operator T on the cube n^3 (T is positive and trace class by reflection
positivity; credit Osterwalder and Seiler, Luscher):

| Number theory (function field form) | Neutral sector of lattice SU(2) |
|---|---|
| Frobenius, its powers | T, its powers |
| point counts N_k | periods p_k = Tr T^k = the neutral partition function of the torus n^3 x k |
| zeta = exp(sum N_k z^k / k) | zeta_T(z) = exp(sum p_k z^k / k) = 1/det(1 - zT) |
| trivial root q | the vacuum eigenvalue lambda_0 |
| inverse roots, square-root bound | lambda_i/lambda_0 for i >= 1; the gap is lambda_i/lambda_0 <= e^(-m) |
| explicit formula: zeros against primes | Tr f(T) against the character (surface) expansion of the torus partition functions |
| Weil positivity (Rosati, Hodge index) | the spectral measure of T is positive: every Hankel matrix [p_(i+j+1)] is positive semidefinite |
| the decisive one-sided inequality | an upper bound on the positive number s(u; n) = p_u / lambda_0^u - 1 |

Two readings follow at once. Both are on the record in other words.

(R1) The explicit-formula positivity exists here and is free: it is reflection positivity. It gives the wrong
direction for (N-phys): s >= 0, log-convexity of k -> p_k, positivity of all Hankel and Newton determinants of
periods. It is not selective: compact U(1) has it too, and compact U(1) at weak coupling is massless (RECALLED: Guth;
Frohlich and Spencer). So no inequality that follows from the positivity of the spectral measure alone gives the gap.

(R2) In the number-theory shape the geometric side is a count, so it has a sign term by term. Here the geometric
side is the sum over supports of the character expansion (surfaces that wrap the period). For abelian groups its
terms are non-negative (Ginibre). For SU(2) the lane already has: negative terms from spin 1/2 on a non-orientable
closed surface (Corollary NS0 of row 737, check 744; Theorem EP-NO; Lemma FKG-NO of row 1213), and three failed
absolute or positive sums (method 35 of `parts/gap.md`). What was left open on file is the centre-blind form: row
1213 Section 4 asks whether every Haar moment of adjoint plaquette characters is non-negative, finds no negative
value, and check 1247 writes "The sign of general adjoint Haar moments remains open." That is exactly the owner's
question in its simplest precise form: is the centre-neutral sector, written in centre-blind variables, free of signs?

### 1.4 Plan

1. Settle the open sign question of row 1213 for centre-blind plaquette characters (Step 2).
2. State the sign rule behind it, for every spin, and what it closes (Step 3).
3. State exactly what a sign-definite object would have to be to give (N-phys), in period and determinant form, and
   test the candidates named in the row (determinant, Gram or period matrix, explicit-formula identity, auxiliary
   construction with multiplicity) (later steps).

## Step 2. Lemma ADJ-NEG: a negative Haar moment of adjoint plaquette characters (PROVED by hand, given the incidence facts of S_0 checked in row 744)

### 2.1 Statement

Notation. chi_1(U) = (tr U)^2 - 1 is the adjoint character of SU(2). For a finite set P of plaquettes of Z^4,
I(P) is the mean of the product over p in P of chi_1(U_p) under product Haar measure on the links.

S_0 is the lattice projective plane of row 737 (`library/gap-means-max.md` L88-94; 92 plaquettes; coordinates
(x, y, z, t); its parts are M in the slice t = 0, A = c x [0, 1] in the direction t, and C in the slice t = 1).
R is the rectangle [0, 3] x [0, 2] of the plane z = 0, t = 0, and gamma is its boundary, a closed curve of 10 links.
D_0 is the following set of 16 plaquettes: the ten plaquettes l x [-1, 0] in the direction t, for l a link of gamma
(the collar), and the six plaquettes of R translated to t = -1 (the bottom). P_0 = S_0 + D_0. It has 108 plaquettes
and lies in a box of 3 x 3 x 4 x 2 cells.

**Lemma ADJ-NEG.** I(P_0) = -3^(-106) < 0.

So the answer to the open question of row 1213 Section 4 is no: Haar moments of adjoint plaquette characters are
not all non-negative in four dimensions.

### 2.2 Facts used

(F1) Gluing. For a, b in SU(2): the integral over U of chi_1(aU) chi_1(U^(-1) b) is chi_1(ab)/3 (Schur
orthogonality). chi_1 is a class function and chi_1(g) = chi_1(g^(-1)).

(F2) For Haar g: the mean of chi_1(g^2) chi_1(g) is -1. Proof: let g have eigenvalues e^(i phi), e^(-i phi). Then
chi_1(g) = e^(2i phi) + 1 + e^(-2i phi), chi_1(g^2) = e^(4i phi) + 1 + e^(-4i phi), and chi_2(g) = e^(4i phi) +
e^(2i phi) + 1 + e^(-2i phi) + e^(-4i phi). So chi_1(g^2) = chi_2(g) - chi_1(g) + 1, and the characters are
orthonormal. (Second proof by the class density (1/pi)(1 - cos theta) on [0, pi] for the rotation angle theta:
the mean of (1 + 2 cos theta)(1 + 2 cos 2 theta) = 1 + 4 cos theta + 2 cos 2 theta + 2 cos 3 theta is 1 + 4(-1/2) = -1.)
The representation-theory content: chi_1(g^2) is the character of the symmetric square minus that of the
antisymmetric square, and the adjoint representation sits in its own antisymmetric square, through the Lie bracket
(the tensor epsilon).

(F3) Incidence facts of S_0 (checked by gpt-6-astra in row 744): 92 plaquettes, 184 links, 93 sites; every link lies
in exactly two plaquettes; the plaquettes around every site form one cycle.

(F4) New incidence facts, each read from the description of row 737 (and confirmed by a bookkeeping script, GUIDE):
 (a) Every link of gamma lies in exactly two plaquettes of S_0, both in M. For the nine links other than
 b = [(1,0),(2,0)] they are the wall plaquettes above and below the link. For b they are the two floor plaquettes
 [1,2] x [-1,0] and [1,2] x [0,1]. No link of gamma is on the boundary curve c of M, and A and C do not touch gamma's links.
 (b) The plaquettes of S_0 are connected through links that are not on gamma. Proof: neighbours in the upper wall
 (z in [0,1]) share a vertical link; so do neighbours in the lower wall. The upper wall end at (1,0) joins the quarter
 plaquette x = 1, (y,z) in [-1,0] x [0,1]; this joins the floor plaquette [1,2] x [-1,0] through the link x = 1,
 y in [-1,0]; this joins the quarter plaquette x = 2, (y,z) in [-1,0] x [-1,0] through the link x = 2, y in [-1,0];
 this joins the lower wall end at (2,0). In the same way the lower wall end at (1,0) joins the upper wall end at
 (2,0) through the quarter plaquette x = 1, (y,z) in [0,1] x [-1,0], the floor plaquette [1,2] x [0,1] and the quarter
 plaquette x = 2, (y,z) in [0,1] x [0,1]. None of the links used is on gamma. A is joined to M along c, and C to A
 along c + e_t.
 (c) D_0 has 16 plaquettes, 37 links and 22 sites. Its links are: the 10 links of gamma (each in one plaquette of
 D_0), the 10 links in the direction t below the sites of gamma (each in two collar plaquettes), and the 17 links of
 R - e_t (the 10 boundary ones in one bottom and one collar plaquette, the 7 inner ones in two bottom plaquettes).
 Its plaquettes are connected through links not on gamma.
 (d) No plaquette of D_0 is in S_0, and the only links that D_0 shares with S_0 are the links of gamma: S_0 lies in
 0 <= t <= 1, and every other link and every plaquette of D_0 has a point with t < 0.
 So in P_0 the links of gamma lie in exactly three plaquettes and all other links in exactly two.

### 2.3 Lemma GLUE (PROVED)

Let Q be a finite set of plaquettes and Gamma a simple closed curve of links. Assume: (i) every link of Q that is not
on Gamma lies in exactly two plaquettes of Q; (ii) every link of Gamma lies in exactly m plaquettes of Q, m = 1 or 2;
(iii) the plaquettes of Q are connected through links not on Gamma; (iv) at a site off Gamma the plaquettes of Q
form one cycle; at a site on Gamma they form one fan (a path) from one link of Gamma to the other if m = 1, and one
cycle if m = 2; (v) E - (|Q| - 1) = V, with E and V the numbers of links and sites of Q. Then the integral of the
product over p in Q of chi_1(U_p), over all links not on Gamma, equals 3^(-(|Q| - 1)) chi_1(g^m), where g is the
ordered product of the link variables around Gamma.

Proof. Choose a spanning tree of the graph of (iii): its nodes are the plaquettes, its edges are links off Gamma.
Integrate its |Q| - 1 links one at a time. At each step the link lies in two different merged groups, once in the
boundary word of each, and after an inversion of one word (F1) applies. The result is 3^(-(|Q| - 1)) chi_1(W). W is
a closed walk. It passes every link of Gamma m times and every other remaining link twice. Let H be the graph of the
remaining links. H is connected, because W runs through all of it. H contains every site: at a site off Gamma, if
no link were left, the tree would contain the cycle of plaquettes around the site; a site on Gamma lies on a link
of Gamma, and the links of Gamma are never integrated. H has E - (|Q| - 1) = V links on V sites, so it has exactly
one cycle. Gamma is a cycle in H. So H is Gamma with trees attached.

Corners. At a site v, the remaining links at v cut the cycle (or fan) of plaquettes around v into arcs. The plaquettes
of one arc are merged. So each passage of W through v goes from one remaining link at v to the next one in the
order around v. At a site of degree one in H the single passage enters and leaves by the same link u, so W contains
u u^(-1), and this pair cancels inside chi_1. A link of a tree is a bridge of H and W passes it exactly twice, so W
makes one excursion into each subtree and returns by the same link. Remove the trees leaf by leaf. At a site v of
Gamma let c, c' be its two links of Gamma. In the order around v the remaining links are c, u_1, ..., u_a, c' and,
if m = 2, further u_(a+1), ..., u_r back to c. A passage that enters by c leaves by u_1, returns by u_1, leaves by
u_2, and so on, and at last leaves by c'. After the cancellations it is one passage from c to c' (or from c' to c).
For m = 2 the other arc gives a second passage between c and c'. So the reduced walk on Gamma never turns back. It
passes every link of Gamma m times. So it is g^m, up to a cyclic shift and an inversion, and chi_1 does not see
these. The cancelled links no longer occur, so their integrals are 1. QED

The argument for m = 2 is the argument of Proposition NS of row 737 (as corrected in check 744), with the dual tree
chosen off Gamma so that the unique cycle is Gamma.

### 2.4 Proof of Lemma ADJ-NEG

Apply Lemma GLUE to Q = S_0, Gamma = gamma, m = 2: (i) and (iv) are (F3), (ii) is (F4)(a), (iii) is (F4)(b), and
(v) is 184 - 91 = 93. The integral over the links of S_0 off gamma is 3^(-91) chi_1(g^2).

Apply it to Q = D_0, Gamma = gamma, m = 1: (i)-(iv) are (F4)(c) (an interior site of D_0 is one of the 12 sites of
R - e_t; at a site of R - e_t that is inside R the four bottom plaquettes form a cycle; at a site on its boundary
the bottom and collar plaquettes form a cycle; at a site of gamma the two collar plaquettes form a fan between
the two links of gamma), and (v) is 37 - 15 = 22. The integral over the links of D_0 off gamma is 3^(-15) chi_1(g).

By (F4)(d) the two sets of integrated links are disjoint and neither meets the other set of plaquettes. So
I(P_0) = 3^(-106) times the mean of chi_1(g^2) chi_1(g) over the ten links of gamma. g is a product of ten
independent Haar variables, so g is Haar distributed, and (F2) gives I(P_0) = -3^(-106). QED

### 2.5 Guide checks (GUIDE; no proof step)

- Bookkeeping script, run outside the repository with `python3 -E -P`: it rebuilds S_0 from the description of row
 737 and finds (F, E, V) = (92, 184, 93), every link in two plaquettes, one cycle at every site; gamma: 10 links,
 each in two plaquettes of S_0; S_0 connected through links off gamma; D_0: (16, 37, 22), boundary gamma; P_0: 108
 plaquettes, 211 links, 105 sites, ten links in three plaquettes (the links of gamma) and 201 in two.
- Monte Carlo on a small abstract complex with the same shape, prediction written first. The hemicube (the cube
 surface modulo the antipodal map: three squares on the graph K_4, a projective plane) plus one triangle glued on a
 one-sided 3-cycle. Lemma GLUE predicts the adjoint moment -3^(2 - 4) = -1/9 = -0.1111. Run: 4 x 10^7 Haar samples,
 seed 20261120, BLAS threads 1, under 1 GB: -0.11138 +- 0.00017 for the triangle (a, b, d) and -0.11130 +- 0.00017
 for (a, b, c). Controls in the same run: adjoint hemicube alone +0.11126 +- 0.00017 (prediction +1/9); fundamental
 hemicube alone -0.25027 +- 0.00016 (prediction -1/4, the value of row 737).

## Step 3. What Lemma ADJ-NEG gives: the sign rule, and three closures (second response)

### 3.1 Proposition SIGN (all spins on S_0 and P_0; PROVED, same proof)

For a spin j in {1/2, 1, 3/2, ...} let d_j = 2j + 1 and let I_j(P) be the Haar mean of the product over p in P of
chi_j(U_p). Then

 (a) I_j(S_0) = (-1)^(2j) d_j^(-91);
 (b) I_j(P_0) = (-1)^j d_j^(-106) for integer j, and I_j(P_0) = 0 for half-integer j.

So for every spin that is not an even integer there is an explicit plaquette set with a negative Haar moment:
S_0 for the half-integers (this is NS0 of row 737 for j = 1/2), P_0 for the odd integers.

Proof. Lemma GLUE holds for chi_j with 3 replaced by d_j: the gluing integral of chi_j(aU) chi_j(U^(-1) b) is
chi_j(ab)/d_j, and every character of SU(2) is real, so chi_j(g) = chi_j(g^(-1)). The last integral is the mean of
chi_j(g^2) for S_0 and of chi_j(g^2) chi_j(g) for P_0. With eigenvalues e^(i phi), e^(-i phi) of g and
chi_J(g) = sum over M = -J, ..., J of e^(2iM phi):

 chi_j(g^2) = sum over J = 0, 1, ..., 2j of (-1)^(2j - J) chi_J(g).   (1)

Check of (1): the left side is the sum of e^(2iK phi) over K = -2j, -2j + 2, ..., 2j. On the right the coefficient of
e^(2iM phi), M an integer with |M| <= 2j, is the alternating sum over J from |M| to 2j, which is 1 if 2j - |M| is
even and 0 if it is odd. By (1) and orthonormality, the mean of chi_j(g^2) is (-1)^(2j) (the Frobenius-Schur
indicator), and the mean of chi_j(g^2) chi_j(g) is (-1)^j if j is an integer and 0 if not. QED

Reading of (1). chi_j(g^2) is the character of the symmetric square of D^j minus that of the antisymmetric square.
D^J lies in the symmetric square if 2j - J is even and in the antisymmetric square if it is odd. For j = 1/2 the
trivial representation is antisymmetric (the invariant form is symplectic): this is the crosscap sign. For j = 1 the
adjoint representation is antisymmetric (the invariant three-tensor is epsilon, the Lie bracket): this is the new sign.
It does not need pseudoreality. It needs three sheets along a closed curve, two of them exchanged after one turn.

Even integer spins. On S_0 and P_0 the moments of chi_2, chi_4, ... are positive. Spin 2 is settled in Step 5B by a
different mechanism (a 6j symbol, already in three dimensions). A remark on a second route, ARGUED: the
same computation gives: the mean of chi_2(g^3) chi_2(g) is -1 (chi_2(g^3) = chi_6 - chi_5 + chi_3 - chi_2 + chi_0).
So a complex in which one sheet's boundary runs three times around a curve and a disc runs once would be negative for
spin 2. I did not build such a complex in Z^4.

### 3.2 Remark BR (the general sign for branch circles; ARGUED, the surface-with-boundary gluing rule is RECALLED from Migdal and Witten)

Let P be a plaquette set in which every link lies in two or three plaquettes, the three-valent links form disjoint
simple closed curves, and the pieces of P cut along these curves are compact surfaces F with boundary. Then
I(P) = (-1)^t times the product over the pieces F of 3^(chi(F) - |F|), where t is the number of branch curves along
which exactly two of the three sheets are exchanged after one turn. Reason: each piece integrates to
3^(chi(F) - |F|) times the product of chi_1 of its boundary holonomies; at a branch curve the three boundary runs
give the mean of chi_1(g)^3 = 1 (no exchange), of chi_1(g^2) chi_1(g) = -1 (one exchange), or of chi_1(g^3) = 1
(a cyclic exchange). This agrees with Lemma PAR of row 1213 (a parity of local networks) and with its values
3^(-8) and 3^(-15)/2 only where the hypotheses overlap (the first). Only the case P_0 is PROVED in this file.

Dimension. A three-sheet junction with one exchange does not embed in three dimensions (ARGUED: the two exchanged
sheets form a Moebius band around the curve; in the normal plane of the curve their common line turns by an odd
multiple of pi, the direction of the third sheet turns by a multiple of 2 pi, so the two must coincide somewhere).
So, like the crosscap sign of row 737, this sign is a four-dimensional effect. Step 5B treats Z^3: there the
adjoint moments are non-negative for link valence at most three (Proposition P3), and spin 2 is negative (Proposition Y).

### 3.3 Corollary TERM (no positive character expansion in the centre-blind class, at any coupling; PROVED)

Let e^(beta x) = sum over j of c_j(beta) chi_j(U) be the character expansion of the Wilson weight, x = (1/2) tr U;
c_j(beta) > 0 for every j and every beta > 0 (RECALLED: modified Bessel functions). On every periodic lattice with
sides at least 4, 4, 5, 3 that contains P_0, the partition function is the sum over spin assignments j_p of
(product of c_(j_p)) times (Haar mean of the product of chi_(j_p)(U_p)). The term with j_p = 1 on P_0 and j_p = 0
elsewhere is c_1^108 c_0^(N - 108) (-3^(-106)) < 0, at every beta > 0. So the sum has negative terms also among the
assignments with integer spins only. With NS0 (spin 1/2 on S_0) this gives: the character (surface, spin-foam)
expansion of four-dimensional Wilson SU(2) has negative terms in both centre classes, at every coupling. The same
holds for the SO(3) theory with any plaquette weight whose adjoint coefficient is positive.

In the words of Step 1: the geometric side of the explicit formula is not a count, in either centre class. An
inequality for the neutral sector cannot be read off term by term. It would have to hold after a sum over supports,
and by method 35 of `parts/gap.md` not after a sum of absolute values.

### 3.4 Corollary ADJ-FKG (the centre-blind plaquette field is not associated at small coupling; PROVED)

Let y_p = chi_1(U_p) = 4 x_p^2 - 1 in [-1, 3]. Put F = product over p in D_0 of x_p^2 and G = product over p in S_0
of x_p^2. Both have values in [0, 1] and are non-decreasing in every y_p (and in every |x_p|).

(a) Under Haar measure Cov(F, G) = -4^(-108) 3^(-106) < 0.
(b) Under the Wilson measure with plaquette couplings 0 <= beta_p <= 2^(-400) (weight exp(sum beta_p x_p)), and in
its centre-even state, and under the SO(3) Wilson measure exp(sum b_p chi_1(U_p)) with 0 <= b_p <= 2^(-401):
Cov(F, G) < 0.
(c) The same holds if "non-decreasing" is replaced by "non-decreasing in e_p y_p", for any choice of a sign e_p that
depends only on the orientation class (one of six) of p, with the factors x_p^2 replaced by 1 - x_p^2 where e_p = -1.

So the field (y_p), the field (|x_p|) and the field (x_p^2) are not associated in this range, in any of the 64
translation-invariant orders. This is the centre-blind form of Lemma FKG-NO of row 1213.

Proof. (a) x_p^2 = (1 + y_p)/4. Expand the products. The Haar mean of the product of y_p over a set T is 0 if some
link lies in exactly one plaquette of T, because the integral of D^1(U) is 0. T inside D_0, T not empty: if T is not
D_0, then by (F4)(c) some p in T and p' in D_0 outside T share a link off gamma, and this link lies in no other
plaquette of P_0; if T = D_0, a link of gamma lies in one plaquette of T. So the mean of F is 4^(-16). T inside S_0:
if T is not empty and not S_0, two neighbours through a link off gamma, one in T and one outside, exist by (F4)(b),
and that link lies in no other plaquette of P_0. So the mean of G is 4^(-92)(1 + I(S_0)) = 4^(-92)(1 + 3^(-91)).
T = T_D + T_S inside P_0: the same two arguments leave only T empty, T = S_0 and T = P_0 (for T_D = D_0 and
T_S empty a link of gamma lies in one plaquette). So the mean of FG is 4^(-108)(1 + 3^(-91) - 3^(-106)), and the
covariance is -4^(-108) 3^(-106).
(b) The 211 links of P_0 lie in at most 6 x 211 = 1266 plaquettes. Given all other links, the density of these links
with respect to Haar measure has logarithmic oscillation at most u = 2532 beta_max (Wilson) or 5064 b_max (SO(3),
chi_1 has range 4). So each of the three means differs from its Haar value by at most delta = e^u - 1 <= 2u, and
the covariance by at most 3 delta (for numbers in [0, 1], |ab - a'b'| <= |a - a'| + |b - b'|; this is the step of
check 1247 for FKG-NO). 3^106 < 2^169, so |Cov_0| > 2^(-385), and 3 delta <= 6u < 2^(-385) in the stated ranges. The
centre-even state is a mixture of Wilson measures with couplings of both signs and the same absolute values
(EP-NO (c), as used in check 1247), the bound uses only absolute values, and the three bounds on the means pass to
mixtures.
(c) Replace x_p^2 = (1 + y_p)/4 by (3 - y_p)/4 = 1 - x_p^2 where e_p = -1. The three surviving terms become
(product of constants), e(S_0) 3^(-91) (constants), and -e(P_0) 3^(-106), with e(T) the product of e_p over T. In a
closed lattice surface the number of plaquettes of each orientation class is even (its projection to a coordinate
plane is a 2-cycle modulo 2 of the plane, so it is zero). D_0 has 6 plaquettes of class xt, 4 of class yt and 6 of
class xy. So e(S_0) = e(P_0) = 1 and the covariance is -4^(-108) 3^(-106) again. QED

### 3.5 Corollary ADJ-GKS (no first Griffiths inequality for adjoint plaquette characters; PROVED)

Under the Wilson measure with 0 <= beta_p <= 2^(-353), and under the SO(3) Wilson measure with 0 <= b_p <= 2^(-354),
the mean of the product over p in P_0 of chi_1(U_p) is negative. Proof: the product is bounded by 3^108 and its Haar
mean is -3^(-106); 3^214 < 2^340; as in 3.4 (b) the mean moves by at most 3^108 delta. QED

For compact U(1) every such mean of products of cos(n theta_p) is non-negative at every coupling (Ginibre). So
this is a place where SU(2) differs from U(1) by a sign, and the cause is the bracket.

### 3.6 What this closes on the record

Row 1213 Section 5 left (POS-N) with three ways. Way 1 (fundamental traces) FAILS (EP-NO, FKG-NO, on file). Way 2
(Hopf coordinates) FAILS (Lemma HF of row 1188, on file). Way 3 (adjoint plaquette characters) was "OPEN, with no
consumer": no negative moment was known. Now way 3 FAILS in its two natural forms, by a counterexample: the cone of
positive-type centre-blind class functions (it contains chi_1; 3.5), and the cone of functions that are monotone in
the centre-blind plaquette variable (3.4). Not closed: other cones of centre-blind functions that do not contain
chi_1 or a monotone function (for example the cone generated by chi_2 alone, which does not generate the neutral
algebra); association at couplings that are not small. Three dimensions are treated in Step 5B.

### 3.7 Remark CL (the class of coupling fields; PROVED, it is the proof of 3.4 (b) read again)

The proof of 3.4 (b) uses only the couplings of the at most 1266 plaquettes that contain a link of P_0. So for every
b > 0 and every coupling field with values in [0, b] that is at most 2^(-400) on those plaquettes, Cov(F, G) < 0. The
same reading holds for Lemma FKG-NO of row 1213 (its bound uses the plaquettes at the links of S_0 only). So:
association of plaquette variables, in the fundamental or in the centre-blind form, is false on the class of all
coupling fields 0 <= beta_p <= b, for every b > 0. The neutral step of the posted two-dimensional proof is stated
on such a class (its (3.67) holds "for every set of couplings 0 <= b_e <= b, including all intermediate bond
weakenings", as read in `library/prior/gap-o4-pinned-cell-read-opus.md` L182-184, and its (3.70) integrates the
coupling from 0). So a port of that step to plaquette variables has no true statement to prove on the class, in
either centre class. This is the same lesson as Theorem D2 and Lemma SHEET for other class-uniform forms.

Scale of the effect (ARGUED). For the homogeneous Wilson measure the negative sign of 3.4 is visible only at
couplings far below any coupling of interest: a positive term of lower order takes over. Example: the unit cube with
x in [1,2], y in [0,1], t in [-1,0] has two faces in D_0 (the bottom plaquette and the collar plaquette over b) and
one face in S_0 (the floor plaquette [1,2] x [0,1] of M); its three other faces can carry spin 1 from the Wilson
weight, with a factor (c_1/c_0)^3, about beta^6/512 at small beta. That term of the covariance is positive, about
4^(-108) 3^(-4) beta^6/512, and it exceeds the negative term 4^(-108) 3^(-106) once beta is above about 2 x 10^(-8). So 3.4 is a statement about classes and about term-by-term structure. It is not a
statement about the Wilson measure at beta = 2.3. Whether the centre-blind plaquette field is associated at one
fixed coupling of order one is OPEN, and I know no consumer for it.

## Step 4. The candidates named in the row, one by one (third response)

### 4.1 Proposition PER (periods, determinants, Gram form; PROVED, classical; on file in other words)

Let T be a positive trace-class operator on a real L^2 space with a continuous real symmetric kernel, with
eigenvalues lambda_0 > lambda_1 >= lambda_2 >= ... >= 0 (lambda_0 simple). Put x_i = lambda_i/lambda_0,
p_k = Tr T^k, s(u) = sum over i >= 1 of x_i^u, and

 delta_u = (p_u^2 - p_(2u))/p_(2u) = 2 Tr(Lambda^2 T^u)/Tr(T^(2u)),

where Lambda^2 is the antisymmetric square. p_u^2 - p_(2u) is the 2 x 2 Newton determinant of the periods.

(a) s(u) <= delta_u <= 2 s(u) + s(u)^2. So (N-phys), s(u) <= 1/2, follows from delta_u <= 1/2 and implies
delta_u <= 5/4.
(b) For even u = 2v let K_v be the kernel of T^v and k_U = K_v(U, .). Then
p_u^2 - p_(2u) = double integral over U, V of [ |k_U|^2 |k_V|^2 - <k_U, k_V>^2 ], and the integrand is the Gram
determinant of the two half-period boundary states, so it is non-negative pointwise.
(c) Multiplicity: s(mu) <= s(u)^m for every integer m >= 1.
(d) Every inequality between finitely many periods that holds for all such T (every consequence of the positivity
of the spectral measure: all Hankel and Newton determinant inequalities) holds for operators with s(u) as large as
one likes. So no such inequality implies (N-phys).

Proof. (a) p_u = lambda_0^u (1 + s(u)), so p_u^2/p_(2u) = (1 + s(u))^2/(1 + s(2u)). And
0 <= s(2u) <= x_1^u s(u) <= s(u). So 1 + s(u) <= p_u^2/p_(2u) <= (1 + s(u))^2. (b) The kernel of T^u is
K_u(U, V) = <k_U, k_V>; Tr T^u is the integral of K_u(U, U) (Mercer) and Tr T^(2u) is the double integral of
K_u(U, V)^2. (c) A sum of m-th powers of non-negative numbers is at most the m-th power of the sum. (d) Add to T a
direct summand with many eigenvalues close to lambda_0; all positivity inequalities still hold. QED

Reading. (b) is the mean form of the four-point cross-ratio of the slab kernel, Lemma WS' and Proposition RR of
row 1258 (check 1265). (a) is the periodic doubling criterion of the lane in the time direction. So the "determinant
of periods" and the "Gram matrix" of the row exist, are sign-definite, and are on file. The sign is the wrong one:
positivity says delta_u >= 0. (N-phys) is an upper bound on a sign-definite determinant. Positivity of the same kind
cannot give it, by (d), and compact U(1) at weak coupling shows that no property shared with U(1) can.

### 4.2 Verdicts

| Candidate | Does the sign-definite object exist for Wilson SU(2)? | Verdict for the neutral inequality |
|---|---|---|
| Determinants of periods (Hankel, Newton) | Yes: reflection positivity (4.1) | Wrong direction; not selective; PROVED not sufficient (4.1 (d)) |
| Gram matrix of boundary states | Yes (4.1 (b)); it is RR of row 1258 | (N-phys) is its upper bound; a restatement, OPEN as before |
| Explicit-formula identity with a sign-definite geometric side | No. Negative terms in both centre classes at every coupling: NS0 (row 737) and Corollary TERM (3.3, new) | FAILS term by term. After the sum over supports: OPEN, no mechanism; absolute sums fail (method 35) |
| Association or a Griffiths cone in plaquette variables | No on every class [0, b] of coupling fields: EP-NO, FKG-NO (on file); ADJ-FKG, ADJ-GKS, Remark CL (3.4-3.7, new) | FAILS as the class statement that the posted 2D step uses |
| Conditional abelian ferromagnets (Hopf, maximal torus) | No: Lemma HF (row 1188), D2 (row 1194), on file | FAILS, on file |
| Auxiliary construction with multiplicity | Multiplicity exists as the power u (4.1 (c)) and, in the posted 2D charged half, as the number of frequencies in the variance bound | In four dimensions the class induction has no statement (rows 1011, 1016); nothing new here |
| Objects special to SU(2): the bracket squared | Yes, pointwise (4.3) | Selective (zero for abelian groups); no consumer found; OPEN |

### 4.3 Remark FR (a sign-definite object that reads the bracket; PROVED identity, classical, credit Fricke and Vogt; no consumer)

Write g = g_0 + i g.sigma for g in SU(2), with a real vector part g in R^3. For three holonomies a, b, c with a
common base point: (1/4)[tr(abc) - tr(acb)] = det[a, b, c], the triple product of the vector parts. So

 ( (1/4)[tr(abc) - tr(acb)] )^2 = det[ x_i x_j - x_ij ] >= 0,  x_i = (1/2) tr g_i,  x_ij = (1/2) tr(g_i g_j),

the Gram determinant of the three vector parts. Proof: (a.sigma)(b.sigma) = a.b + i (a x b).sigma gives
(1/2) tr(ab) = a_0 b_0 - a.b and (abc)_0 - (acb)_0 = (a x b).c - (a x c).b = 2 det[a, b, c]. QED
It vanishes for commuting holonomies, so it vanishes identically for an abelian group. It is the simplest
gauge-invariant sign-definite quantity that reads the Lie bracket; the continuum forms are det(E + B), det(E - B)
and the Gram matrices of F + F~ and F - F~ (3 x 3, because the Lie algebra and the space of self-dual two-forms
both have dimension three). I found no inequality for the neutral trace that uses it. The record's two other
selective sign-definite objects are the Ricci term of SU(2) with the O'Neill term of the orbit space (cancelled to
all orders, row 1194 Step 2.1) and the variance gain of the bracket term (the posted 2D charged half; no class
statement in 4D, row 1011).

## Step 5. Lemma ADJ-NEG2: the adjoint sign does not need a non-orientable closed set (PROVED by hand; fourth response)

Why this step. P_0 contains the projective plane S_0. `library/gap-loop-eq-opus.md` L139 left open "restricted
cones (sources whose union contains no closed non-orientable plaquette set)". So one can ask whether the adjoint sign
is only the crosscap of row 737 seen again. It is not.

### 5.1 The complex X_2 and the statement

All parts refer to row 737's description of M (24 plaquettes, slice t = 0, boundary curve c of 28 links, core curve
gamma = boundary of R) and of the disc C (40 plaquettes, there in the slice t = 1 with boundary c + e_t).
- D' (26 plaquettes): the twenty plaquettes l x [-1, 0] and l x [-2, -1] in the direction t, for l a link of gamma,
 and the six plaquettes of R translated to t = -2. (A deeper cup than D_0, so that it stays clear of the next part.)
- N: the disc C translated to the slice t = 0, without its roof plaquette q = [0,1] x [0,1] x {z = 2}. N has 39
 plaquettes. N is not a part of X_2; it is the base of the next part.
- G (142 plaquettes): the boundary of N x [-1, 1] in the direction t. That is: N + e_t and N - e_t (39 each), the 56
 plaquettes l x [0, 1] and l x [-1, 0] for l a link of c, and the 8 plaquettes l x [0, 1] and l x [-1, 0] for l a
 link of the boundary of q.
- X_2 = D' + M + G, 192 plaquettes, in a box of 3 x 3 x 4 x 3 cells.

**Lemma ADJ-NEG2.** (a) I(X_2) = -3^(-191) < 0. (b) The only non-empty subset of X_2 in which every link lies in no
plaquette or in exactly two is G, and G is a torus (it has a coherent orientation). So X_2 contains no closed
non-orientable plaquette set, and the Haar moment of its adjoint characters is negative.

### 5.2 Two more gluing lemmas (PROVED)

(F1') For a, b in SU(2): the integral over U of chi_1(a U b U^(-1)) is chi_1(a) chi_1(b)/3 (Schur orthogonality).

**Lemma GLUE-A (a piece with two boundary curves).** Let Q be a finite plaquette set and Gamma_1, Gamma_2 two
simple closed curves of links with no common site. Assume (i) every link of Q off the curves lies in exactly two plaquettes of
Q; (ii) every link of Gamma_i lies in exactly m_i plaquettes of Q, m_i = 1 or 2; (iii) Q is connected through links
off the curves; (iv) at a site off the curves the plaquettes of Q form one cycle, at a site of Gamma_i one fan
between the two links of Gamma_i if m_i = 1 and one cycle if m_i = 2; (v) E - (|Q| - 1) = V + 1. Then the integral
of the product of chi_1(U_p), p in Q, over all links off the curves is 3^(-|Q|) chi_1(g_1^(m_1)) chi_1(g_2^(m_2)),
with g_i the holonomy of Gamma_i.

Proof. As in Lemma GLUE, integrate a spanning tree of links off the curves: 3^(-(|Q| - 1)) chi_1(W), W a closed
walk through the graph H of remaining links. H is connected, has all V sites and V + 1 links, and contains the two
disjoint cycles. Remove the trees as in Lemma GLUE. What is left is connected, has no site of degree one, has one
link more than sites, and contains two disjoint cycles. A graph of that kind with one site of degree four is two
cycles through one site; with two sites of degree three it is three paths between them, or two disjoint cycles
joined by a path. Only the last has two disjoint cycles. So what is left is Gamma_1, Gamma_2 and a path pi from a
site v_1 of Gamma_1 to a site v_2 of Gamma_2. By the corner rule of Lemma GLUE (a passage joins two remaining links
that are neighbours in the order around the site): at an inner site of pi there are two passages along pi; at a site
of Gamma_i other than v_i there are m_i straight passages; at v_i with links c, c' of Gamma_i and the link p of pi
the passages are (c, p), (p, c') and, if m_i = 2, also (c', c). W uses every passage once. Follow W from v_1 along
pi: it reaches v_2, must run around Gamma_2 exactly m_2 times in one direction before it can leave (if it left
earlier, the remaining passage (c', c) and the second run of the links of Gamma_2 could not be reached again, because
both runs of pi are then used), returns along pi, and runs around Gamma_1 exactly m_1 times in one direction. So
W = g_1^(m_1) pi g_2^(+-m_2) pi^(-1), up to a cyclic shift. Apply (F1') to the first link of pi; the other links of
pi then cancel by conjugation. QED

**Lemma GLUE-T (a torus cut along a curve).** Let Q be a finite plaquette set and Gamma a simple closed curve of
links. Assume (i) every link of Q lies in exactly two plaquettes of Q; (ii) Q is connected through links off Gamma;
(iii) at every site the plaquettes of Q form one cycle; (iv) E - (|Q| - 1) = V + 1; (v) the plaquettes of Q can be
oriented so that every link is run in opposite directions by its two plaquettes. Then the integral of the product of
chi_1(U_p), p in Q, over all links off Gamma is 3^(-|Q|) chi_1(g)^2, g the holonomy of Gamma.

Proof. Integrate a spanning tree of links off Gamma. By (v) no word has to be inverted when two words are merged,
so the closed walk W runs every remaining link once in each direction. Remove the trees. What is left is connected,
without sites of degree one, with one link more than sites, and it contains Gamma. Three cases.
Two disjoint cycles joined by a path: by the corner rule, a walk that enters a cycle from the path can leave it
only after two runs in the same direction (the argument of Lemma GLUE-A with m = 2). This contradicts (v). Excluded.
Gamma and a closed path x through one site v of Gamma, with the four links c, c' (of Gamma) and x, x' at v. If c and
c' are neighbours in the order around v, the passages are (c, c'), (c', x), (x, x'), (x', c): a walk that leaves by c
returns by c' and then either runs Gamma again in the same direction, against (v), or goes on to x, returns by x'
and then either runs x again in the same direction, against (v), or closes after one run of every link, against
the count. Excluded. So the order is c, x, c', x', the passages are
(c, x), (x, c'), (c', x'), (x', c), and W = g x g^(-1) x^(-1) up to a cyclic shift and an inversion.
Three paths e_1, e_2, e_3 from a site v to a site v' (Gamma is two of them). W is a cyclic sequence of six runs,
alternately from v to v' and back. Each path is run once in each direction, so it occurs at two places of opposite
parity; two runs in a row use different paths, and the three passages at v' use three different pairs, and so do
those at v. The only such sequence is e_1 e_2 e_3 e_1 e_2 e_3. So W = e_1 e_2^(-1) e_3 e_1^(-1) e_2 e_3^(-1). If
Gamma = e_1 e_2^(-1) = g, then W = g e_3 (e_2^(-1) e_1)^(-1) e_3^(-1), and e_2^(-1) e_1 is conjugate to g; the other
two choices of Gamma differ by a cyclic shift.
In the last two cases (F1'), applied to the first link of x or of e_3, gives chi_1(g) chi_1(g^(-1))/3 = chi_1(g)^2/3. QED

### 5.3 Incidence facts of X_2 (each read from the description; all confirmed by a bookkeeping script, GUIDE)

(X1) M: 24 plaquettes, 62 links, 38 sites. Its links are the 10 of gamma (two plaquettes each), the 28 of c (one
each) and 24 others (two each). Its sites are the 10 of gamma (one cycle each: four wall plaquettes at a site other
than (1,0) and (2,0); at those two, two wall plaquettes, the two floor plaquettes and two quarter plaquettes) and the
28 of c (one fan each). M is connected through links off gamma and c (the chain of (F4)(b)). 62 - 23 = 38 + 1.
(X2) D': 26 plaquettes, 57 links, 32 sites; the facts of (F4)(c) with one more layer of collar; 57 - 25 = 32.
(X3) C is a disc with boundary c: every link of C off c lies in two plaquettes of C, the plaquettes at a site off c
form one cycle and at a site of c one fan. This is contained in (F3), because A meets C only along c + e_t. The four
links of q are each shared with one other plaquette of C (two walls with z in [1,2], two roof plaquettes), and no
link of q is on c. So every inner link of N lies in two plaquettes, and the boundary of N is c together with the boundary of q; at
the four sites of q the plaquettes of N form a fan (of two plaquettes at (0,0,2), of three at the other sites). N
is connected through inner links, because C is, and the four fans join the four neighbours of q to each other.
(X4) G = boundary of N x [-1, 1]: a link of N + e_t or N - e_t that is inner lies in two plaquettes; one over the
boundary of N lies in one plaquette of N +- e_t and one wall; a link in the direction t over a boundary site of N lies
in two walls; a link of c or of the boundary of q at t = 0 lies in the two walls above and below it. At every site
the plaquettes form one cycle. With N oriented, N + e_t with this orientation, N - e_t with the opposite one and the
walls with the product orientation give (v) of Lemma GLUE-T. Counts: 142 plaquettes, 284 links, 142 sites, so
284 - 141 = 142 + 1. G is connected through links off c: N + e_t and N - e_t are connected; each wall over c is joined to
N + e_t or to N - e_t through its link at t = 1 or t = -1; the walls over the boundary of q join N + e_t to N - e_t
through the links of the boundary of q at t = 0, which are not on c.
(X5) D' meets M only in the links of gamma; M meets G only in the links of c; D' and G share no link. (M lies in
t = 0; D' has no plaquette in t = 0 and its links at t = 0 are those of gamma; the links of G at t = 0 are those of
c and of the boundary of q, which lies at z = 2; at t = -1 the links of D' lie over gamma and those of G lie in
N - e_t or over c and q, and N - e_t has no link of gamma - e_t.)
The last clause of (X5) and the fan and cycle counts of (X3)-(X4) are the places where a reader should look hardest.

### 5.4 Proof of Lemma ADJ-NEG2

(a) Lemma GLUE for D' (m = 1): 3^(-25) chi_1(g). Lemma GLUE-A for M with Gamma_1 = gamma, m_1 = 2, Gamma_2 = c,
m_2 = 1: 3^(-24) chi_1(g^2) chi_1(h). Lemma GLUE-T for G with Gamma = c: 3^(-142) chi_1(h)^2. By (X5) the three
integrations use disjoint sets of links. g and h are products of independent Haar variables on disjoint sets of
links, so they are independent and Haar distributed. The mean of chi_1(g) chi_1(g^2) is -1 by (F2), and the mean of
chi_1(h)^3 is 1 (the multiplicity of the trivial representation in the third tensor power of the adjoint). So
I(X_2) = -3^(-191).
(b) Let T be such a subset. If T contains some but not all plaquettes of D', an inner link of D' lies in one
plaquette of T. If T contains D', then at a link of gamma T needs exactly one of the two plaquettes of M; but M is
connected through links off gamma and c that lie in two plaquettes of M and in no other, so T contains all of M or
none of it, a contradiction. So T misses D'. Then T contains all of M or none; if all, a link of c needs exactly one
of its two plaquettes of G, and G is connected through links off c, a contradiction. So T misses M, and T is G or
empty. G has a coherent orientation by (X4), and 142 - 284 + 142 = 0. QED

### 5.5 Guide check (GUIDE)

Monte Carlo of the same shape with three abstract cells (a disc with boundary g; an annulus with boundary word
g g p h p^(-1); a torus cell with word h k h^(-1) k^(-1)), prediction written first: -3^(-2) = -0.1111. Run: 2 x 10^7
Haar samples, seed 1120: -0.11113 +- 0.00030. Control with the annulus word g p h p^(-1) (no exchange): prediction
+0.1111, run +0.11133 +- 0.00030. The bookkeeping script finds for X_2: 192 distinct plaquettes; 327 links in two
plaquettes and 38 in three (the links of gamma and of c); the counts and the cycle and fan types of (X1)-(X4); the
sharing pattern of (X5).

### 5.6 What it adds

The sign of Step 2 comes from one branch curve with an exchange of two sheets, and from nothing else: all closed
subsets of X_2 are orientable. So in the centre-blind class there is no restricted cone of the kind asked for in
`library/gap-loop-eq-opus.md` L139 (PROVED for adjoint sources; the question there, for fundamental sources, stays
OPEN, since a link in three fundamental plaquettes gives the mean zero). The corollaries of Step 3 hold with X_2 in
place of P_0 and the split D' against M + G, with other exponents (ARGUED, not written: it needs the Haar moment of
M + G, which is 3^(-166) by the gluing rule for a Moebius band).

### 5.7 Second derivation of both moments, through Lemma PAR of row 1213 (PROVED for P_0 by hand; exact script for both, GUIDE)

Lemma PAR (row 1213, 4.1 (f); HOLDS in check 1247) is a different route: it factorizes over sites, not over
surfaces. If every link lies in two or three plaquettes, I(P) = 3^(-E_2) 6^(-E_3) times the product over sites of
the local networks A_v (delta at a two-valent link, epsilon at a three-valent link in a fixed order of its three
plaquettes, one index per plaquette corner).

P_0 by hand. E_2 = 201, E_3 = 10. At each of the 95 sites off gamma the plaquettes form one cycle through two-valent
links, so A_v = 3. At a site of gamma the two links l, l' of gamma carry epsilon, and three strands join them: the
fan of D_0, and the two arcs of the cycle of S_0. Order the plaquettes of every link of gamma as (the plaquette of
D_0, A, B), with A the wall plaquette above the link and B the one below, and for the link b with A the floor
plaquette on the side y < 0 and B the one on the side y > 0. If the arcs join A to A and B to B, then A_v = +6; if
they join A to B and B to A, then A_v = -6. At the eight sites other than (1,0) and (2,0) the arcs run through the
vertical links above and below the site: +6. At (1,0) the cycle of S_0 is: upper wall, quarter plaquette x = 1 with
(y,z) in [-1,0] x [0,1], floor y < 0, floor y > 0, quarter plaquette x = 1 with (y,z) in [0,1] x [-1,0], lower wall;
so A joins A and B joins B: +6. At (2,0) the cycle is: floor y < 0, quarter plaquette x = 2 with (y,z) in
[-1,0] x [-1,0], lower wall, upper wall, quarter plaquette x = 2 with (y,z) in [0,1] x [0,1], floor y > 0; so A
joins B: -6. This is the half twist of M. So I(P_0) = 3^(-201) 6^(-10) 3^95 (-6^10) = -3^(-106), as in Step 2.

Exact script (GUIDE; rational arithmetic, `python3 -E -P`, outside the repository). It evaluates the formula of
Lemma PAR by summing every local network over its index values, with the plaquettes of each link in sorted order.
Results: S_0: 93 local values 3, I = 3^(-91). P_0: local values 3 (95 times), +6 (9 times), -6 (once),
I = -3^(-106) exactly. X_2: E_2 = 327, E_3 = 38; local values 3 (134 times), 9 (once, a site where D' and G touch
without a common link), +6 (35 times), -6 (3 times), I = -3^(-191) exactly. So each of the two lemmas has two
derivations that agree: gluing along surfaces (Lemmas GLUE, GLUE-A, GLUE-T) and factorization over sites (Lemma PAR).

## Step 5B. Three dimensions: spin 2 is negative, spin 1 is not (sixth response)

Row 737 wrote of its sign: "It says nothing in three dimensions", and a guide run there found no negative
three-plane integral. Step 3.2 argued that the exchange sign of Step 2 is also a four-dimensional effect. This step
settles what three dimensions do in the centre-blind class.

### 5B.1 Lemma PAR-j (PROVED; it is the proof of Lemma PAR of row 1213 with the spin changed)

Let j >= 1 be an integer, D = D^j in its real orthogonal form, d = 2j + 1, and t a non-zero invariant three-tensor of
D. t is unique up to a factor; it is symmetric if j is even and antisymmetric if j is odd. Put n = <t, t>. If every
link of P lies in two or three plaquettes, then I_j(P) = d^(-E_2) n^(-E_3) times the product over sites of the local
networks A_v: delta at a two-valent link, t at a three-valent link (in one fixed order of its three plaquettes, the
same at both ends), one index per plaquette corner.
Proof. The Haar integral of D (x) D is delta delta / d, and that of D (x) D (x) D is the projection on the
one-dimensional invariant subspace, t (x) t / n. The rest is the proof of Lemma PAR. QED
Local values: a cycle of two-valent links gives d; two three-valent links joined by three strands (a theta) give n
when j is even; four three-valent links joined in all six pairs (a tetrahedron) give T_j = n^2 w_j for even j, where
w_j is the 6j symbol with all six spins equal to j (RECALLED: this contraction of normalised invariant tensors is
the definition of the 6j symbol; for integer spins the phase conventions drop out).

### 5B.2 Proposition Y (a negative spin-2 moment on 32 plaquettes of Z^3; PROVED GIVEN the value w_2 = -3/70)

Y is the following set of 32 plaquettes of Z^3: the 24 plaquettes of the surface of the box [0,2]^3; the four
plaquettes of the plane z = 1 inside the box; the two plaquettes of the plane y = 1 with z in [1,2]; the two
plaquettes of the plane x = 1 with z in [0,1]. (A floor through the middle, a wall above it along x, a wall below it
along y.)

Then I_2(Y) = 5^(-22) w_2^5 = -3^5 / (2^5 7^5 5^27) < 0, about -6.06 x 10^(-23). More generally
I_j(Y) = d^(-22) w_j^5 for every even j.

Proof. Links: 20 lie in three plaquettes (the 8 links of the square where the floor meets the box; for each wall
its two links on the floor, its two links on the top or bottom face, and its two vertical links on the side faces);
the other 34 lie in two. Sites, 27 in all. The 8 corners of the box, the 4 mid-points of the box edges
(1,0,2), (1,2,2), (0,1,0), (2,1,0): one cycle each, value d. Thetas, 10 sites: the 4 mid-points (0,0,1), (2,0,1),
(0,2,1), (2,2,1) of the vertical edges; (0,1,2), (2,1,2) and (1,1,2) on the top edge of the upper wall;
(1,0,0), (1,2,0) and (1,1,0) on the bottom edge of the lower wall. Tetrahedra, 5 sites: the centre (1,1,1), where
the floor carries the four links +-x, +-y, the upper wall joins +x and -x through +z, and the lower wall joins +y
and -y through -z; and the four sites (0,1,1), (2,1,1), (1,0,1), (1,2,1) where a wall ends on the square. (At
(1,0,1): the links +-x lie in two face plaquettes and one floor plaquette, the link -z in two face plaquettes and
the lower wall, the link +y in two floor plaquettes and the lower wall, the link +z in two face plaquettes; the six
pairs of the four three-valent links are joined by the corners (x,-z), (-x,-z), (x,y), (-x,y), (y,-z) and, through
+z, (x,-x).) Each three-valent link ends at two of these 15 sites: 10 x 2 + 5 x 4 = 2 x 20. So by Lemma PAR-j
I_j(Y) = d^(-34) n^(-20) d^12 n^10 (n^2 w_j)^5 = d^(-22) w_j^5.
The value w_2, by Racah's formula, by hand: the triangle coefficient squared is (2!)^3/7! = 1/630; the sum runs
over k = 6, 7, 8 with terms +7!/(2!)^3 = 630, -8! = -40320, +9!/(2!)^4 = 22680; so w_2 = -17010/630^2 = -3/70. QED

Guide checks (GUIDE). A numeric evaluation of the local networks of Y for spin 2 gives 12 values 5, 10 values
2.916667 and 5 values -0.364583. An exact rational script (the projector on traceless symmetric matrices) gives
n = 35/12 and T_2 = -35/96, so T_2/n^2 = -3/70. The same code reproduces 5^(-4) for the cube surface and 5^(-8) for
the 2 x 1 x 1 box with its wall. A census of the 465 sets "surface of [0,2]^3 plus a subset of its 12 inner
plaquettes, every link in two or three plaquettes": the spin-2 moment is negative for 102 of them (each has five
tetrahedra), zero for 24, positive for 339; the smallest negative one found has 31 plaquettes.
An independent Monte Carlo check of the tetrahedral value with its sign, prediction written first: for one
abstract cell with boundary word a a b b a b^(-1) on two loops a, b (its six corners join the four link ends in all
six pairs) the site factorization predicts the Haar mean of chi_2 to be w_2 = -0.042857; run with 4 x 10^7 samples,
seed 31120: -0.04288 +- 0.00014. (The same run gives -0.16674 +- 0.00014 for chi_1, that is -1/6: this abstract
cell is not a lattice set of Z^3, and Proposition P3 below does not apply to it.)
Exact Racah values (script): w_1 = 1/6, w_2 = -3/70, w_3 = -1/14, w_4 = -467/18018; the sign of w_j for
j = 5, ..., 20 is + + + - - - + + + - - + + + - -. So I_j(Y) < 0 for j = 2, 4, 8, 10, 14, 20 in this range.

### 5B.3 Corollary TERM-3 (PROVED GIVEN w_2 = -3/70)

On every periodic lattice Z_L^3 with L >= 3, and on every four-dimensional lattice that contains a translate of Y,
the character expansion of the Wilson SU(2) partition function has a negative term at every beta > 0: the term with
spin 2 on Y and spin 0 elsewhere, c_2^32 c_0^(N - 32) I_2(Y). So three dimensions are not free of signs either. The
first sign there is at spin 2, through a 6j symbol, on a set that a person can draw.

### 5B.4 Proposition P3 (in three dimensions adjoint moments are non-negative when no link lies in more than three plaquettes; PROVED GIVEN Penrose's theorem, RECALLED)

Let P be a finite plaquette set in Z^3 with every link in at most three plaquettes. Then I_1(P) >= 0.
Proof. If a link lies in one plaquette, I_1(P) = 0. Otherwise use Lemma PAR. Around a site v draw a small sphere.
The links at v are points of the sphere, the plaquette corners at v are arcs between them, and the arcs do not
cross. Remove the two-valent points. What is left is a planar graph G_v with all degrees three, and some closed
curves (a factor 3 each). Penrose's theorem (RECALLED): if epsilon is put on every vertex of a planar cubic graph
with V vertices, in the anticlockwise order of its three edges, the contraction is (-1)^(V/2) times the number of
proper colourings of the edges with three colours. Now fix the order of the three plaquettes of every three-valent
link as the right-handed order around the link, directed along its positive coordinate direction. Seen from outside
the sphere at the tail of the link this order is anticlockwise; at the head it is clockwise, which costs one sign.
So A_v = (-1)^(V_v/2) (-1)^(h_v) (number of colourings of G_v) 3^(number of closed curves), with h_v the number of
three-valent links that end at v with their head. The sum of the V_v/2 is E_3, and the sum of the h_v is E_3. So the
product of the signs is +1. QED
Guide (GUIDE): in the census of 5B.2 the adjoint moment is positive for 441 sets and zero for 24, never negative.
Not covered: links in four plaquettes (two crossing planes), where spin 2 enters the link integral.

### 5B.5 The picture after Steps 2, 3, 5 and 5B

| Spin on the plaquettes | Z^3 | Z^4 |
|---|---|---|
| 1/2 (and every half-integer) | no closed non-orientable surface; no negative value known (row 737, guide) | negative: crosscap, S_0 (row 737; here for all half-integers) |
| 1 | non-negative for link valence at most 3 (P3) | negative: exchange of two sheets on a branch curve, P_0 and X_2 (new) |
| 2 | negative: five tetrahedral vertices, Y (new) | negative (Y lies in Z^4) |
| even j >= 4 | negative on Y when w_j < 0 (j = 4, 8, 10, 14, 20, ...); otherwise OPEN | the same |
| odd j >= 3 | not examined | negative on P_0 (Proposition SIGN) |

## Step 6. State at the end (2026-11-20, sixth response)

### 6.1 What was attacked, what failed, what is left

The row's question: is there a hidden sign-definite object for the centre-neutral sector that gives the missing
neutral inequality, or a proof that no object of a named class can?

Attack. The neutral inequality (N-phys) is an upper bound on a quantity that is already sign-definite (4.1). In the
shape of the owner's hint, a one-sided bound of this kind comes for free when the other side of an exact identity is
a count. So the first thing to settle was whether the centre-neutral sector, written in centre-blind variables, has
a geometric side with a sign. That was an open item of the record (row 1213 Section 4; check 1247).

What failed. No sign-definite object that gives (N-phys) was found. The mass gap is not proved. For each candidate
named in the row the first failing step is in the table of 4.2.

What was proved instead (new against the record, as far as my greps of `library/` show):
1. Lemma ADJ-NEG: the Haar moment of adjoint plaquette characters over the explicit 108-plaquette set P_0 is
 -3^(-106). Two derivations.
2. Proposition SIGN: on S_0 and P_0 every spin that is not an even integer has a negative Haar moment; the sign is
 the parity of the symmetric or antisymmetric square.
3. Corollary TERM: the character expansion of Wilson SU(2) in four dimensions has negative terms among the
 integer-spin assignments, at every coupling. With NS0: in both centre classes.
4. Corollaries ADJ-FKG, ADJ-GKS and Remark CL: association and the first Griffiths inequality fail for centre-blind
 plaquette variables at small couplings, in all 64 translation-invariant orders, hence on every class [0, b] of
 coupling fields.
5. Lemma ADJ-NEG2: the same sign on a 192-plaquette set whose only closed subset is a torus; value -3^(-191). Two
 derivations.
6. Proposition PER and Remark FR: classical; they fix what "determinant of periods", "Gram matrix" and "an object
 that reads the bracket" mean here, and that the first two are on file (rows 1258, 1265).
7. Three dimensions (Step 5B). Proposition Y: the spin-2 Haar moment of an explicit 32-plaquette set of Z^3 is
 5^(-22) (-3/70)^5 < 0, so the character expansion has negative terms in three dimensions too (Corollary TERM-3).
 Proposition P3: adjoint moments in Z^3 are non-negative when no link lies in more than three plaquettes.

What is left OPEN.
- (N-phys), the continuum datum, the Jaffe-Witten mass gap. Not moved.
- A neutral inequality after the sum over supports. No mechanism is known. By 3.3 and method 35 it cannot be a
 term-by-term bound and cannot be a bound on absolute values.
- Association of the centre-blind plaquette field at one fixed coupling of order one (no consumer known).
- Haar moments of chi_j for the even integers j with a positive regular 6j symbol (j = 6, 12, 16, 18, ...).
- In three dimensions: adjoint moments with a link in four plaquettes; half-integer spins.
- Coordinates other than plaquette or loop traces: gauge-fixed link coordinates were not treated here; the Hopf
 form is closed on file (Lemma HF).
- A consumer for the bracket-squared objects of Remark FR.

### 6.2 Marks

| Statement | Mark |
|---|---|
| Four-dimensional SU(2) Yang-Mills has a mass gap (Jaffe and Witten); (N-phys) | OPEN. Not proved here |
| 1.3 dictionary; readings (R1), (R2) | ARGUED (a reading; (R1) uses the RECALLED massless phase of compact U(1)) |
| Lemma GLUE | PROVED |
| Lemma ADJ-NEG, I(P_0) = -3^(-106) | PROVED by hand, given (F3) (checked in row 744) and (F4) (read from row 737's description); second derivation 5.7 given Lemma PAR (check 1247) |
| Proposition SIGN (a), (b) | PROVED (same inputs) |
| Spin 2 and the even spins with w_j < 0 | Step 5B; the other even spins OPEN |
| Lemma PAR-j | PROVED (the proof of Lemma PAR, row 1213, check 1247) |
| Proposition Y, Corollary TERM-3 | PROVED GIVEN the tetrahedral value T_2/n^2 = w_2 = -3/70 (the identification with the 6j symbol is RECALLED; Racah's sum is done by hand; an exact script agrees, GUIDE) |
| Proposition P3 | PROVED GIVEN Penrose's theorem (RECALLED) and Lemma PAR |
| Racah signs for j up to 20; the census of 465 sets | GUIDE |
| Remark BR; the statement that the exchange junction does not embed in three dimensions | ARGUED |
| Corollary TERM | PROVED (given the positivity of the character coefficients, RECALLED) |
| Corollary ADJ-FKG (a), (b), (c); Corollary ADJ-GKS; Remark CL first paragraph | PROVED |
| Remark CL, scale of the effect | ARGUED |
| Proposition PER; Remark FR | PROVED (classical) |
| Table 4.2 | verdicts as marked in its rows |
| Lemmas GLUE-A, GLUE-T | PROVED |
| Lemma ADJ-NEG2 (a), (b) | PROVED by hand, given (X1)-(X5) (read from the description; confirmed by script, GUIDE) |
| Monte Carlo runs (2.5, 5.5); bookkeeping and exact scripts (2.5, 5.5, 5.7) | GUIDE |

### 6.3 For the lead (ARGUED, short)

1. Check request, in this order: (F4) and Lemma GLUE with Lemma ADJ-NEG; the hand form of 5.7 (it is the shortest
 full check of the value: ten local networks and one count); Proposition Y (27 sites of a 2 x 2 x 2 box and one
 6j value; the shortest of all); Corollaries TERM, ADJ-FKG, ADJ-GKS; Proposition P3 (the orientation count); then
 (X1)-(X5), Lemmas GLUE-A and GLUE-T, Lemma ADJ-NEG2. The scripts are not in the repository; the complexes are fully described
 in 2.1 and 5.1, and a checker can rebuild them in a few lines.
2. If the check holds, `parts/gap.md` method 35 can gain one sentence: integer-spin terms are negative too, through a
 branch curve where two of three sheets are exchanged (the bracket), with or without a non-orientable closed set,
 and, already in three dimensions, through tetrahedral vertices at spin 2 (a 6j symbol).
 And (POS-N) of row 1213 loses way 3 by a counterexample, not by "no consumer".
3. For the owner's direction: in this problem the sign-definite objects that exist are of the reflection-positivity
 kind, and they give the wrong direction. The geometric side has signs in both centre classes, and the cause in
 the centre-blind class is the same bracket that gives asymptotic freedom. So a proof in the shape of the hint
 would need an exact identity whose other side is positive after a resummation that uses the bracket. I found no
 candidate. The one place on record where the bracket enters with a definite sign is the variance gain of the
 posted two-dimensional charged half.
4. The nearest thing on file to the hint's determinants, in a form that could be formalized, is a finite
 positivity certificate for a one-scale criterion (the certificate form of row 1050; loop equations with reflection
 positivity need loops of the seed size, Proposition VB of `library/gap-loop-eq-opus.md`). I did not attempt one,
 and Steps 2-5B say only that its positive part cannot be a term-by-term expansion.
5. No literature search was run in this session. Signs of spin-network evaluations are classical (Penrose; Ponzano
 and Regge; Wigner for the symmetry of the 3j symbol). "New" in this file means new against the lane's record only.

### 6.4 Credits

Jaffe and Witten (the problem). L. Alpoge and Claude (the remark: only its shape is used, as a reading, and one short
quotation). Stepanov (auxiliary functions with multiplicity). Weil (positivity and the explicit formula). Guinand.
Balaban; Sussman and Alpoge, with Claude and Codex as authors of their text (the account that the lane's chain reads;
no step here uses it). Osterwalder and Seiler; Luscher (reflection positivity, the transfer operator). Griffiths;
Ginibre; Fortuin, Kasteleyn and Ginibre (the inequalities that fail here). Frobenius and Schur (the indicator). Wigner
(the symmetry of the invariant three-tensor; the 6j symbol). Racah (the formula for it). Penrose (epsilon networks
and the colouring theorem used in Proposition P3). Ponzano and Regge (signs of 6j symbols). Migdal; Witten (gluing; two-dimensional
gauge theory on surfaces). Fricke; Vogt (trace identities). Guth; Frohlich and Spencer (compact U(1) at weak
coupling). OpenAI (the posted O(4) and O(3) proofs, as read in rows 1007 and 1009); Ding, Huang and Yang. Mack and
Petkova; Tomboulis (named in the reading). In this lane: Claude Fable 5.2 (row 737: Proposition NS, the surface S_0
and its Moebius band M, on which both complexes here are built; rows 1193, 1194); Claude Opus 5.5 (Theorem EP-NO;
row 1213: Lemma FKG-NO, Lemma PAR and the open question answered here; row 1258); gpt-6-astra and gpt-6.2-astra (the
checks of rows 744, 1209, 1247, 1265, and the sentence that named the open sign).

RESULT: Row 1303 `gap-positivity-fable` (Claude Fable 5.2 max, laptop subagent, 2026-11-20 16:15Z-17:18Z; author only, checked by no one; small guide runs only). The mass gap is NOT proved and nothing in the chain is disproved; (N-phys), the continuum datum and the gap stay OPEN. On the owner's question (a hidden sign-definite object for the centre-neutral sector): none that gives the neutral inequality was found; the sign-definite objects that exist (determinants of periods, the Gram determinant of half-period boundary states) are reflection positivity and give the wrong direction (Proposition PER, classical; the Gram form is RR of row 1258). PROVED by hand, two derivations each (surface gluing; the site factorization of Lemma PAR, row 1213): Lemma ADJ-NEG, the Haar moment of adjoint plaquette characters over an explicit 108-plaquette set P_0 = S_0 + D_0 of Z^4 (row 737's projective plane plus a 16-plaquette disc on the core of its Moebius band) is -3^(-106), which answers the open sign question of row 1213 and check 1247 in the negative; Lemma ADJ-NEG2, the same sign, -3^(-191), on a 192-plaquette set whose only closed subset is a torus, so the cause is one branch curve where two of three sheets are exchanged (the antisymmetric square of the adjoint, the Lie bracket), not the crosscap. PROVED GIVEN the 6j value {2 2 2; 2 2 2} = -3/70: Proposition Y, the spin-2 Haar moment of an explicit 32-plaquette set of Z^3 (a 2 x 2 x 2 box with a floor and two half walls) is 5^(-22) (-3/70)^5 < 0, so three dimensions have negative terms too. PROVED GIVEN Penrose's theorem: in Z^3 adjoint moments are non-negative when no link lies in more than three plaquettes. Consequences PROVED: the character expansion of Wilson SU(2) has negative terms among integer-spin assignments at every coupling, in four dimensions (spin 1) and in three (spin 2), and with NS0 in both centre classes; association and the first Griffiths inequality fail for centre-blind plaquette variables at small couplings in all 64 translation-invariant orders, hence on every class [0, b] of coupling fields, so the association step of the posted 2D proof has no true class statement in plaquette variables; way 3 of (POS-N) of row 1213 FAILS. OPEN: a neutral inequality after the sum over supports (no mechanism); even spins with a positive regular 6j symbol; association at one fixed coupling of order one. Output library/gap-positivity-fable.md.
