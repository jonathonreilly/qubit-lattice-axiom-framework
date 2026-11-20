lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T21:50Z

# Check of row 1246 (`library/gap-solve28-astra62.md`), queue row 1253

Checker: Claude Opus 5.5, max effort, Mac mini worker 3, started 2026-11-20T09:50Z
(date -u). Repository commit fd73d8c6a on branch `claude/ym4d-hard-route`.
Cross-provider check: the author of row 1246 is gpt-6.2-astra (max), Codex runner.
This check is by hand; no numeric run is a step of any verdict.

## Plan (at most eight steps)

1. Read FINISH.md rules (queue row 1253, efficiency, build-on-published-work) and
   the whole of `library/gap-solve28-astra62.md`; list its statements with labels and lines.
2. Check positive claim A: cyclicity of spatial plaquette histories for the
   finite-cutoff centre-neutral sector (statement, proof, cited rows).
3. Check positive claim B: the fixed-depth slab with a temporal mean on each cut
   detects the exact spectral edge (statement, proof, cited rows).
4. Check every remaining statement of the file, line by line.
5. Read the earlier rows the steps depend on (cited statements and their proofs);
   decide whether the main comparison is a restatement of an earlier row
   (grep `library/open-core.md`, FINISH rows, earlier `gap-solve*` files).
6. Check the published-work credits (`library/prior/gap-onebound-read-sol.md`,
   Sussman-Alpoge account) where the file relies on them.
7. Verdict table: HOLDS / HOLDS AFTER CORRECTION / FAILS per statement, with line.
8. RESULT line.

## Status

Step 1 in progress.

## Step 1. Inventory of the file under check (done 2026-11-20T10:02Z)

Rules read: FINISH.md queue row 1253, "Working efficiently", "Rules", "How we work"
items 2, 4, 7. The file `library/gap-solve28-astra62.md` (404 lines, commit fd73d8c6a)
was read in full. Labels are the author's. Statement numbers S1-S30 are mine.

| # | Lines | Author label | Statement |
|---|---|---|---|
| S1 | 21 | PROVED | Transfer T=DCD on vertex-gauge-invariant space; top vector psi > 0, simple, symmetric |
| S2 | 23 | PROVED | vN algebra A of T, spatial M_{w_p}, marked T_e; words and strong closure give the same cyclic space |
| S3 | 25-34 | PROVED | D, D^{-1}, C, C^[e] in A; joint eigenvalues (1); v_{d+1} > v_d |
| S4 | 36 | PROVED | spectral projection onto rep d on edge e; S_{e,h}=exp(h Delta_e) in A |
| S5 | 38 | PROVED | h^{-1}[[S_{e,h},M_f],M_g] -> 2 M_{Gamma_e(f,g)} strongly |
| S6 | 42-56 | PROVED | tree gauge; identity (2); seven traces fix the corner orbit |
| S7 | 58-72 | PROVED | extension step (3); all invariant multipliers on an open rectangular box |
| S8 | 76-82 | PROVED | the three periodic seams, up to global centre flips |
| S9 | 84-90 | PROVED | (4): words in T, M_{w_p}, T_e applied to psi are dense in H_+ |
| S10 | 96-101 | PROVED | (5); off a countable set E, C generates the common heat semigroup |
| S11 | 103 | PROVED | global temporal-sum reading gives the common heat semigroup at every beta |
| S12 | 105-117 | PROVED | octant data (length 4 and 6 loops, trihedral) fix the configuration up to gauge and flips; (4) with T and spatial M_{w_p} only, beta not in E |
| S13 | 123 | PROVED | a cutoff-dependent bump isolates one face |
| S14 | 125-146 | PROVED | statistic D(t) of (6); (7): 0 < D(t) <= r_+^t, D(t)^{1/t} -> r_+ |
| S15 | 152-191 | PROVED | (8)-(11): (4) with only T and spatial M_{w_p}, every beta > 0 |
| S16 | 197-229 | PROVED conditional on row 1231 | (12), (13), (14) weak-coupling evaluation of D(t) |
| S17 | 231-237 | PROVED under those inputs | (15): weight of D on bounded physical energies -> 0 |
| S18 | 243-274 | PROVED | (16), (17): u-step kernel ratio <= e^{-cuV} between two vanishing-action fields |
| S19 | 276 | PROVED | endpoint comparison constants >= e^{cuV}; Birkhoff-type contraction near 1 |
| S20 | 280-304 | PROVED | fixed depth m_*: spatial readings on m_*+1 slices plus one temporal mean per cut prepare a dense subspace of H_+; (18), (19) |
| S21 | 306-311 | PROVED | D_*(t) > 0, D_*(t)^{1/t} -> r_+, D_*(t+l)/D_*(t) -> r_+^l |
| S22 | 313 | PROVED | cost (z_beta/z_gamma)^{3n^3} of the cut reweighting |
| S23 | 319-336 | PROVED using row 1161 (19) | (20)-(22): z_u <= (Tr_+ U^u)^{-1} <= (M+1)(1+Lambda^{-u})^{-M} |
| S24 | 340-344 | PROVED | (23): C_J chi >= c^{|J|} chi |
| S25 | 348-354 | PROVED | (24): U <= R, 0 <= R <= L_J |
| S26 | 356-362 | PROVED | (25): local fixed-depth version in a box with collar |
| S27 | 364-373 | PROVED | (26) and its scaling example |
| S28 | 377 | PROVED | B(H_+) lies in the weak closure of (2m_*+1)-step insertions with global temporal means |
| S29 | 379-386, 402 | OPEN | (27), continuum matching, the gap |
| S30 | 388-400 | PROVED conditional on (27) and matching | (27) plus matching gives a gap >= -log q / h |

GUIDE paragraphs (lines 1-17, 94, 121, 148, 195, 241, 317, 346) carry no verdict;
their factual claims about earlier rows are checked in Step 5.

Positive claim A (queue row) = S9 with S12 and S15. Positive claim B = S20 with S21.

## Step 2. Positive claim A: cyclicity of spatial plaquette histories (done 10:20Z)

Claim A, as the RESULT line states it: at every n >= 4 and beta > 0, the closed span of
the words in T and the spatial M_{w_p} applied to psi is H_+ (L 117, L 191). The proof
runs S1-S9 (with the marked T_e), then removes the marks by S10-S12 (beta off a
countable set) or by S15 (every beta). Each step below was redone by hand.

**S1 (L21) HOLDS.** The kernel D(X) prod_e K(X_e Y_e^{-1}) D(Y) is continuous and
strictly positive; Jentzsch gives a simple positive top vector. Gauge maps and flips
commute with T, so psi is invariant.

**S2 (L23) HOLDS.** The closed span K of words on psi contains psi. It is invariant
under each self-adjoint generator, so its projection lies in the commutant and the
von Neumann algebra maps psi into K.

**S3 (L25-34) HOLDS.** Recomputed: with Haar density (2/pi) sin^2 theta and
int_0^pi e^{beta cos theta} cos(k theta) d theta = pi I_k(beta),
int e^{beta w} chi_d/d = (I_{d-1}-I_{d+1})/d = (2/beta) I_d, so c_d = I_d/I_1 > 0.
The marked edge factor is d/dbeta log(c_d Z_1) = p_beta + d/dbeta log c_d, and
p_beta = I_1'/I_1 - 1/beta = I_0/I_1 - 2/beta = I_2/I_1 by the two Bessel recurrences.
The law claim follows from (beta^{-nu} I_nu)' = beta^{-nu} I_{nu+1} and the Poisson
integral, so I_{d+1}/I_d is a mean with derivative a positive variance. Hence
v_{d+1} > v_d. A different positive scalar normalization of T_e only rescales t.

**S4 (L36) HOLDS.** The left derivatives along unit imaginary quaternions are unit-speed
great circles on the unit S^3, so -Delta_e = l(l+2) = d^2-1 on degree l = d-1.
S_{e,h} = sum_d e^{-h(d^2-1)} P_{e,d} lies in A.

**S5 (L38) HOLDS.** The double commutator has kernel
p_h(X,Y)(f(Y)-f(X))(g(Y)-g(X)); its h -> 0 limit on smooth vectors is
L(fgv) - fL(gv) - gL(fv) + fgLv = 2 Gamma_e(f,g) v. Since the semigroup acts on degree-one
coordinates by e^{-3h}, E|Y_e - X_e|^2 = 2(1-e^{-3h}) <= 6h. The Schur bound then gives
norm <= 6 Lip_f Lip_g. Gamma_e(f,g) is gauge invariant because the sum over an
orthonormal frame is rotation invariant.

**S6 (L42-56) HOLDS.** (2): for Q = bQ', d/dt Re(e^{ta}Q) = Re(aQ) = -a.Im Q; for
P = P'b^{-1}, d/dt Re(Pe^{-ta}) = a.Im P. The sum over a gives -Im P.Im Q, and
Re(PQ) = Re P Re Q - Im P.Im Q. The triple-trace formula was expanded and agrees. The
corner graph has 9 edges and 7 vertices (cycle rank 3), and the stated tree leaves one
private chord per face. Gram data plus signed volume fix the triple up to SO(3), which is
quaternion conjugation.

**S7 (L58-72) HOLDS.** (3): both words start with b, so the two gradients are -Im H_i and
-Im(bR); their contraction is +Im H_i.Im(bR), and adding w(H_i)w(bR) gives the R^4 dot
product. {1, L_1, L_2, L_1L_2} is a basis when Im L_1, Im L_2 are nonparallel, because
Im(L_1L_2) has the component Im L_1 x Im L_2 normal to both. The two chord variables are
independent Haar in a tree gauge of H-b, and left multiplication by bD_0 is orthogonal.
Every face in the cube and layer schedule has a new path with fresh interior vertices,
or is a single new edge, and has an old edge b on a cycle of a graph of rank >= 3.
I checked the opposite face z=1, the last face x=1, the tree squares and the non-tree
squares.

**S8 (L76-82) HOLDS.** c_ij B_ij^{-1} is the inverse crossing plaquette started at c_ij,
so (3) applies with old edge c_ij. Telescoping gives B_gamma = A_{i0} b_gamma A_{i0}^{-1}.
Two non-commuting unit quaternions have centralizer {1,-1} in SU(2). The x-seam step uses
only plaquettes whose transverse edge lies in the open (y,z) grid. So no plaquette that
crosses two seams is needed.

**S9 (L84-90), (4) HOLDS** for the marked generators. Each step adds four bounded readings
whose joint law with the old orbit fixes the new orbit off a null set. A Borel inverse
exists (the explicit frame of L70, or Lusin-Souslin on the standard Borel orbit space).
So the abelian algebra of multipliers in A contains all bounded gauge- and
flip-invariant functions. Truncating u/psi and using dominated convergence gives density
in H_+. Every generator preserves H_+.

**S10 (L96-101) HOLDS.** (5) was recomputed: under the law proportional to
sin^2 theta e^{-beta(1-cos theta)}, the rescaled angle sqrt(beta) theta tends to a
chi-3 law with second moment 3, and chi_d/d = 1 - (d^2-1) theta^2/6 + O(theta^4). Then
log s_d = -k_d/(2 beta) + o(1/beta). Two real-analytic functions on (0,inf) that differ
near infinity coincide on a discrete set. The union over countably many pairs of
multisets (entries 1 contribute c_1 = 1, k = 0) is countable. F(C) with F = e^{-hk} on
eigenvalues and 0 elsewhere is a Borel calculus.

**S11 (L103) HOLDS.** c_d(gamma)^{floor(2h gamma)} -> e^{-h(d^2-1)} by (5). The operators
are contractions, so the convergence is strong.

**S12 (L105-117) HOLDS.** The double commutator with the common heat semigroup gives the
total Gamma = sum_e Gamma_e, with Schur constant O(N h) at fixed volume. Two faces at x
that share a ray share exactly one edge. For P = AB (a simple hexagon after cancelling y)
and Q = C, the shared edges are x and z. I recomputed both contributions: each is
-Im(AB).Im C = w(ABC) - w(AB)w(C). So w(ABC) = w(AB)w(C) + Gamma/2. Left and right
derivatives give the same contraction. Each of the 12 faces at x has two private
non-root edges (n >= 3), so the Q_ij are i.i.d. Haar given the root edges. The
octant-gluing system has rows |u||v|(cos phi, sin phi); it is singular only if the
planar angle of e falls on one value mod pi, a null event. Two configurations with the
same data differ by a closed Z_2 cochain, and H^1(T^3; Z_2) = Z_2^3 is the three flips.

**S15 (L152-191) HOLDS, one wording repair.** (8) is correct: (beta/2)^d/d! <= I_d <=
(beta/2)^d e^{beta^2/4}/d!, and Stirling gives h_beta(d) = d log d + O_beta(d). (10) was
expanded and agrees. The resolvent argument is standard and correct. H_k -> sqrt x
uniformly on bounded sets, |H_k| <= C(1+x), and the tail bound
4||Q^2 v||^2/R^2 holds. Repair (wording, L175): "after truncation at R" must use a
continuous cutoff chi_R (1 on [0,R], 0 beyond 2R). Strong resolvent convergence passes
only continuous functions vanishing at infinity, and an indicator is not one. With
chi_R the step is complete, since A_b is bounded and the tail is uniform in k. L182:
(1+G_f)v ranges over a dense set because 1+G_f is bounded and invertible, and v in the
domain of B_k gives the contraction identity. (11): on a simple contour,
|grad_e w(P)| = sqrt(1-w(P)^2) on every edge (cyclic rotation). The common-edge value
is the same on both shared edges of (AB, C), as computed under S12, and
G - (p-l)a - (q-l)b = l sqrt(a^2+b^2+2d) >= 0 inverts. So every vertex datum of S12 lies
in A_s, with each new function a polynomial in the links, hence smooth for the next use
of (9).

**Verdict on claim A: HOLDS** (one wording repair at L175). At fixed n >= 4 and every
beta > 0, ψ is cyclic for H_+ under T and the spatial plaquette multipliers. The
statement is qualitative. It says nothing about depth, norms or uniformity in n or beta
(the author says so at L191).
