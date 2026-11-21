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

All eight steps done by 2026-11-20T10:12Z (date -u). Started 09:50Z.

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

## Step 2. Positive claim A: cyclicity of spatial plaquette histories (done 10:04Z)

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
beta > 0, psi is cyclic for H_+ under T and the spatial plaquette multipliers. The
statement is qualitative. It says nothing about depth, norms or uniformity in n or beta
(the author says so at L191).

## Step 3. Positive claim B: fixed-depth slab and the detector D_* (done 10:06Z)

Claim B (L280, L306-311): a depth m_*, independent of n >= 4 and beta > 0, such that
bounded functions of (spatial plaquette traces on m_*+1 slices, one temporal mean per cut)
prepare a dense subspace of H_+ from psi. Then D_*(t) > 0, D_*(t)^{1/t} -> r_+ and
D_*(t+l)/D_*(t) -> r_+^l.

**L282 HOLDS.** T T = DC D^2 CD, so adjacent half weights give the full interior weight.
Products are separately weakly continuous, so L_i L_j is in L_{i+j}. Inserting
D^{-1}(X_0) D^{-1}(X_1) exp((gamma-beta) 3n^3 wbar) (bounded at fixed n) times a scalar
gives C_gamma exactly in L_1. Its eigenvalues prod c_d(gamma) -> 1 and it is a
contraction, so C_gamma -> I strongly and I is in L_1.

**(18) (L284-292) HOLDS.** The kernel of M_{e^{-i sqrt(gamma) F}} C_gamma M_{e^{i sqrt(gamma) F}}
is K_gamma(X,Y) e^{i sqrt(gamma)(F(Y)-F(X))}. Write Y_e = exp(xi_e/sqrt(gamma)) X_e, with
xi_e independent and symmetric, |xi_e| = sqrt(gamma) theta_e. The radial law
r^2 e^{-r^2/2} gives xi_e -> N(0, I_3). The curve exp(t n) X has unit speed, so
sqrt(gamma)(F(Y)-F(X)) = sum_e xi_e . grad_e F + O(|xi|^2/sqrt(gamma)) uniformly at fixed n.
The limit is E exp(i sum xi_e . grad_e F) = exp(-Gamma(F,F)/2). The depth is
d + 1 + d = 2d+1.

**(19) (L294-302) HOLDS.** Gamma(F,F) = sum_{i,j} a_i a_j Gamma(f_i,f_j). For a simple loop,
Gamma(f_i,f_i) = p_i(1-f_i^2), from the cyclic-rotation gradient. Multiplying by the
diagonal correction (depth d) gives depth 3d+1. Conflict count for an edge (i,j): at most
2(Delta-1) edges share an endpoint, and at most 2 Delta^2 edges touch a neighbour of i or j.
So 2 Delta(Delta+1)+1 colours suffice, and each class is an induced matching. On one
matching with a_i = 1, a_j = -h_ij, the cross terms between unmatched vertices of the
matching vanish: the matching is induced, so those loops share no link and their Gamma is
0. Exponentials of linear forms span a unital, conjugation-closed, point-separating
algebra. Uniform limits, then bounded pointwise limits (strong convergence of
multipliers), stay in the weakly closed space L_{d'}.

**L304 HOLDS.** First pass: Delta = 12 (4 edges x 3 other spatial faces), S <= 313,
d' = 313. The fused traces are w(P)w(Q) + Gamma(w(P),w(Q)): a single shared edge, by (2)
with the orientation that cancels it. Second pass: at most 4 faces and 48 fused loops use a
link, every member has length <= 6, so Delta <= 306 <= 312. S <= 195,313 and
m_* <= 313 + 195,313 x 940 = 183,594,533. The bound is finite, absolute, and independent
of n and beta. The second pass contains Gamma(w(AB), w(C)) = 2(w(ABC) - w(AB)w(C)), so all
octant data of S12 are Borel functions of the tuple. S12 then puts every bounded
invariant multiplier in L_{m_*}. Mazur (weak closure of a subspace = norm closure) gives
norm density of the finite slab preparations.

**S21 (L306-311) HOLDS.** The combined kernel is a Gaussian kernel in all readings
(spatial bandwidth sigma, temporal-mean bandwidth (n^{-3}/m_*)^{1/2}). Its Fourier
measure G is a nondegenerate Gaussian with full support, so
D_*(t) = int <v_s^perp, U^t v_s^perp> dG(s) with ||v_s|| <= 1. A top excited vector
orthogonal to v_s for G-a.e. s is orthogonal for all s (continuity in s). Then it is
orthogonal for every bounded function of the readings (Stone-Weierstrass on the compact
reading cube, then dominated convergence), so it is 0 by the density just proved. Hence
c r_+^t <= D_*(t) <= r_+^t. U is compact on H_+, so the next eigenvalue is < r_+, and
D_*(t+l)/D_*(t) -> r_+^l. The temporal factor lies in [e^{-2/n^3}, 1], so each
expectation moves by at most 2n^{-3} and the difference by at most 4n^{-3}. The term-by-term
comparison of (12) is uniform in m, so it applies to the single m_* term.

**S22 (L313) HOLDS.** p_gamma/p_beta = e^{-(gamma-beta)(1-cos theta)} z_beta/z_gamma <= z_beta/z_gamma,
with equality at theta = 0, and z_b is of order b^{-3/2} by the two quadratic bounds on
1-cos.

**Verdict on claim B: HOLDS.** The depth is uniform. The norms are not (S22, and the factors
D^{-1} of size up to e^{3 beta n^3/2}). The author states both, so the claim is not
overstated. "Detects the exact spectral edge" is a finite-(n, beta) statement. Its
physical slab width m_* a -> 0, with m_* about 1.8 x 10^8 by the stated bounds.

## Step 4. Every other statement (done 10:08Z)

**S13 (L123) HOLDS.** The cited text says this. Outline L326-327: sources
O_i = sum_p f_i(x_p) a_p at barycentres. Outline L1688: centre x + a c_P, with
c_P = (e_mu + e_nu)/2. CA-I L429-431 and L462-466: weight c(x(p)) at the barycentre.
I read these at 31a47c543775, fetched into a scratch folder. Distinct barycentres are at
distance >= a/sqrt 2 > a/2, so a bump of radius < a/4 sees one face.

**S14 (L125-146), (6)-(7) HOLDS.** k_m is the characteristic function of
N(0, sigma_m^2 I). The reflected slab has the same insertion operator (T is real
symmetric), so E[conj F_s(X) F_s(Y)] = <v_s, U^t v_s>, with ||v_s|| <= ||psi|| = 1.
The independent copy gives int |<psi, v_s>|^2 dG, exactly the vacuum part. Nonnegativity
and D(t) <= r_+^t follow from U <= r_+ on psi-perp in H_+. The lower bound c r_+^t
follows from the cyclicity S9 (continuity in s, then Stone-Weierstrass on the reading
cube). r_+ lies in (0,1): U is compact, positive and injective (C has eigenvalues
c_d > 0), with a simple top. (The t = 0 value equals the total mass of the spectral
measure, by the Markov property at the shared slice; this is used at L217.)

**S16 (L197-229), (12)-(14) HOLDS given row 1231 (2)-(5).** Row 1235 checked those
inputs: HOLDS. I re-read row 1231 (2)-(5), lines 21-65. With xi = beta(1-w) and
sigma_m^2 = s beta^2/d_m, k_m = exp(-sS/2). Per colour, Z_{p,c} ~ N(0, v_n), so
Var(|Z_p|^2/2) = 3v_n^2/2 and Cov(|Z_p|^2/2, |Z_q|^2/2) = 3P(p,q)^2/2. The mirror partner
of slice -l sits at distance t+2l, which gives both Gaussian means of S. The four-reading
comparison holds: clip at A log beta (sup (A log beta)^4, Lipschitz O((log beta)^{7/2})).
Row 1231 (2) with b = beta^gamma then errs by O((log beta)^4 beta^{-gamma/2}), so
gamma > 2 eta suffices, and exponential moments remove the clip. Var_W S <= Var_G S +
O(beta^{-eta}) <= C/n^3 + O(beta^{-eta}). The second-order Taylor bound with
e^{-xi} <= 1 for S >= 0 gives (s^2/8) Var S. (13): from row 1231 (4),
k_n(t) = n^{-3} sum_{q != 0} (qhat_1^2 + qhat_2^2) e^{-t omega}/(2 sinh omega) >= 0 and
<= C n^{-4} sum_l l^3 e^{-ctl/n} <= C t^{-4}, also for t > n since e^{-c lambda} <=
C lambda^{-4}. v_n -> 1/2: trace 3 over six planes. (14): the angular average of
k_1^2+k_2^2 is 2|k|^2/3, and int r^3 e^{-rt} dr = 6/t^4 gives t^4 k -> 1/pi^2. So
t^8 D -> e^{-3s/8} (3s/(2 pi^4)) sum_m 2^{-m} = e^{-3s/8} 3s/(2 pi^4). The remainder
beta^{-eta} + n^{-3} = o(t^{-8}) needs eta > 8 delta and n >= e^{beta/B_0}. Both hold.

**S17 (L231-237), (15) HOLDS** under the same inputs. D(n) >= e^{-aA n} nu([0, aA]) and
na = L. The monotone ratio is log-convexity of t -> int lambda^t d mu (Cauchy-Schwarz).

**S18 (L243-274), (16)-(17) HOLDS.** Y has plaquette angle 1/b^2 on 12-faces and 0
elsewhere. A b x b square in a rising run carries flux b^2 (1/b^2) = 1. About V/4 such
squares fit, and each edge lies on <= 2b of them. Contractible squares are flip
invariant. The telescoped triangle inequality gives 1 <= sum theta; Cauchy-Schwarz on 4bu
terms and the multiplicity give (17). The numerator: integrate the final gauges from the
leaves of a spanning tree (z^{V-1}, independent of X_{u-1}), then the slices backwards
(z^{3V} each). The diagonal: temporal angles <= 3/sqrt(beta), interior plaquette angles
<= 4/sqrt(beta) + 1/b^2, cap volume >= c beta^{-3/2} per variable, z_{beta/2} <=
C beta^{-3/2}. With b = floor(kappa sqrt(beta)/u): beta/(b^2 u) >= u/kappa^2 and
beta/b^4 <= 16u^4/(kappa^4 beta) -> 0. The exponent is <= -uV(c_1/(2 kappa^2) - C_3 -
o(1)) + (3/2) log beta + log 8. V >= e^{3 beta/B_0} absorbs the log. kappa is absolute.

**S19 (L276) HOLDS.** c_- g g <= K <= c_+ g g forces c_-/c_+ <= z. On the scaled 2 x 2
block [[1,z],[z,1]], d/d eps log((z+e^eps)/(1+z e^eps)) at 0 is (1-z)/(1+z). The
passage to the continuous kernel by narrow bumps is brief but standard (continuity of
the kernel on a compact space).

**S23 (L319-336), (20)-(22) HOLDS given row 1161 (19).** Row 1161 L265-271 states
(19): beta >= 1, M >= c n^3, at least (1/2) binom(M,k) neutral excited levels with
-log(lambda_i/lambda_0) <= Ck. Row 1162 checked it: HOLDS, with energies independent of
beta. (21): (1/2) e^{-Clu} >= (2e^C)^{-lu}. (22): g = sqrt(K(X,X)) has ||g||^2 = Tr_+ U^u
(continuous positive-definite kernel on a compact space). K >= z_u g (x) g pointwise and
<g, U^u g> <= ||g||^2, so z_u <= 1/Tr. Tr_+ U^u >= binom(M,l) Lambda^{-lu} for every
0 <= l <= M, so (1+Lambda^{-u})^M <= (M+1) Tr_+ U^u.

**S24 (L340-344), (23) HOLDS; typo.** lambda chi = D^2 C chi. The log D^2 Hessian is
>= -16 beta sum|v_e|^2: at most 4 edges per face, at most 4 faces per link, then
Cauchy-Schwarz. The log C chi Hessian is mean plus variance, so >= -beta sum|v_e|^2. The
paired increments +-v give cosh >= 1, and the cap probability is >= c. Typo: L344 ends
"Independence proves (21)"; it means (23).

**S25 (L348-354), (24) HOLDS; one line supplied.** "(23) gives R psi <= L_J psi" needs
C_J C_Jbar chi = C_Jbar C_J chi >= c^{|J|} C_Jbar chi. This holds because C_J and
C_Jbar commute and C_Jbar preserves positivity. Then
R psi = lambda^{-1} D C_Jbar chi <= c^{-|J|} lambda^{-1} D C chi = c^{-|J|} psi. The
weighted Schur bound is as stated. R commutes with J-multipliers.

**S26 (L356-362), (25) HOLDS.** V_gamma is one step with the insertion
exp((gamma-beta) |J| wbar_J) times a scalar. It tends strongly to R, so R lies in L_1(J).
The phases on J commute with D and C_Jbar, and the outer R^d commute with them. So each
stage carries R^{d'}, and the degree bounds 12 and 312 are unchanged. Faces, fused loops
and trihedra at vertices of B lie in J. A rectangular box has H^1 = 0, so closed signs
are coboundaries.

**S27 (L364-373), (26) HOLDS.** U <= R and U >= tau on ran P_tau give
<w, R^{-1} w> <= ||w||^2/tau by the variational formula. With y = (1-x/L)^b:
1-(1-y)^{m_*} <= m_* y, and x(1-x/L)^{2b} <= L/(2b+1). Monomials of degree j >= m_*
lie in L_{m_*}(J) L_{j-m_*}(J). L371: finite rank plus Mazur in a finite direct sum.
L373: m_* a^{(delta-alpha)/2} e^{aA/2} -> 0 and m_* a^{1-delta} -> 0.

**S28 (L377) HOLDS.** K is continuous and >= k_0 > 0 on the compact neutral quotient.
So u(X)v(Y)/K(X,Y) is bounded and is an L^2 limit of finite sums of products; multiplying
by K keeps Hilbert-Schmidt convergence. Finite rank operators are weakly dense, and
L_{2m_*+1} is a weakly closed linear space.

**S30 (L388-400) HOLDS** as an implication from (27) and the stated matching hypothesis.
On psi-perp, U^{s+l b} <= r_+^{lb} U^s. The spectral contradiction for A < -log q/h is
correct. Totality then kills 1_{[0,A]}(H) on the vacuum complement.

**S29 (L379-386, L402) OPEN, consistent with the body.** The innermost limit in (27) is
r_+^{b_j} by S21. No statement of the file proves (27), and none claims to.

## Step 5. Cited earlier rows; is the main comparison a restatement? (done 10:10Z)

**Cited rows, read where a step depends on them.**

- Row 1231 (2)-(5) (`gap-solve26-astra62.md` L21-65), the input of S16-S17. Read.
  Its check, row 1235, gives HOLDS. The use in (12) matches the statements. The
  four-reading clip is shown in Step 4.
- Row 1161 (19) (`gap-solve9-astra62.md` L265-271), the input of S23. Read. Its check,
  row 1162, gives HOLDS ("energies Ck independent of beta"). (20) restates it with
  k -> l.
- Row 1236 (6)-(10) (L96-134), cited at L34 for the marked multiplier and "the ordering of
  the marked ratios". Credit precision: row 1236 (6) has the marked kernel
  (w - p_beta) dC_beta and c'_d >= 0 (from row 1149 (16)), which gives v_d >= v_1 = p_beta.
  It does not have the strict order v_{d+1} > v_d in d that S3 needs. Row 1246 proves
  that order itself at L34. No step depends on the citation.
- Row 1171 (`gap-solve14-astra62.md` L23): "contractible loop words of length at most
  18" is accurate. The centre-cochain step at L115 is reproved in the file.
- Row 1178 (`gap-solve18-astra62.md` L124-140): the L121 description is accurate
  (traces of based products of two or three incident plaquettes, length <= 12, n >= 5;
  strict loss for single-time individual plaquette traces). The file reproves the
  null-set step for its smaller selection (S12).
- Lemma F2 of `gap-target-max.md` (L253) is the two-face identity, as L94 says.
- Row 1207 Theorem 4.2, cited at L15 as computing "the electric double commutator for a
  sum of magnetic terms". Credit precision: check row 1208 found that exact display
  (4.8) FAILS by a sign, (1/2)[[-Delta,S],S] = -sum|N|^2. The citation should carry that
  correction. Row 1246's own double commutator (S5) has the correct sign
  (+2 Gamma for [[e^{h Delta}, M_f], M_g]/h), and no step depends on row 1207.
- Row 1151 L174 and L352 (one-step extensive cross ratio for a frustrated endpoint), cited at
  L241. (16) extends it to u = o(beta^{1/4}) steps and vanishing action.
- Not opened (GUIDE only, no step depends on them): the PR files at L3, and the external
  proposals of row 1218 at L7.

**Is the main comparison a restatement?** I read "main comparison" as the comparison of
the Wilson law with the free Gaussian, (12)-(15), as in row 1235's use of the phrase.

- **(12)-(15): a restatement in substance of row 1231 (3)-(6), not a new estimate.** It
  uses the same covariance law Cov_W(X_p, X_q) = (3/2) P_cyl(p,q)^2 + O(beta^{-eta})
  (row 1231 (3)), the same kernel (row 1231 (4)) and the same limit 1/pi^2 (row 1231 (5)).
  It puts them into a Gaussian kernel of the readings. The leading term of D(t) is
  s e^{-3s/8} times the slab average of row 1231's single-plaquette transform. Row 1231 (6)
  gives t^8 int e^{-t E} d mu -> 3/(2 pi^4) and puts the spectral weight at lattice
  energies of order 1/t. Hence the weight on bounded physical energies vanishes, which is
  (15). The file says as much at L229 ("It agrees with the free two-curvature threshold
  seen by a single bare plaquette") and credits row 1231 at L207. What is new is the
  statistic: (6) sees every neutral eigenspace at finite cutoff (S14, S21). The
  weak-coupling evaluation of that statistic adds no Wilson estimate.
- **(16) and (22): extensions, not restatements.** That a Birkhoff/Hopf endpoint
  contraction is not volume-uniform is already on file as a reading:
  `gap-crux-skeleton-max.md` Lemma B2 (an upper bound kappa <= e^{4 beta N_b});
  `gap-fr-opus.md` L99; `gap-mini-free-fable.md` L222 and L379 ("found again; diameter
  grows with the volume", 21 files). Row 1151 L352 proves an extensive log cross ratio at
  one step for a frustrated endpoint. New in row 1246: the lower bound (16) at u steps
  between two vanishing-action fields, and (22) at physical block time,
  z_u <= (Tr_+ U^u)^{-1}. The trace lower bound inside (22) restates row 1161 L308
  (log(1+s(u)) >= c' M e^{-Cu}). The step z_u <= 1/Tr is elementary and new here. The
  reading at L276 (S19) is the known obstruction.
- **(4), cyclicity of plaquette histories: not a restatement.** No match in
  `library/open-core.md` (grep "cyclic", "histor"), and none in the FINISH rows besides
  1246 and 1253. The library has no earlier "is cyclic" or "cyclic vector" claim for
  plaquette histories. Rows 1171 and 1178 reconstruct the slice from single-time Wilson
  loops of length <= 18 and <= 12. Row 1178 shows that single-time individual plaquette
  traces lose part of H_+. Row 1246 replaces the longer loops by time histories, through
  the double commutator with T. The fixed-depth form (S20) is new too. Consistency with
  Sussman-Alpoge: outline L581-586 and L31858-31869 say that the action-density field
  reconstructs only its own cyclic sector, in the continuum. Row 1246 shows the
  finite-cutoff cyclic space is all of H_+. This does not contradict them: at a fixed
  smooth source the single-face isolation of S13 is lost, and (4) carries no uniformity
  (L123, L191).

## Step 6. Published-work credits; guide run (done 10:12Z)

**Credits present and accurate.**
- Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, are
  credited at L5, L17, L123 and L207. I read the cited lines at 31a47c543775: outline
  L326-337, L581-599, L1688-1693 and L31858-31882; CA-I L423-431 and L448-466. They say
  what the file says.
- Osterwalder-Seiler and Luscher for the transfer (L17). Sourav Chatterjee through row
  1231 (L207). Gemini Argon (row 1207). The row 1218 authors (L7, GUIDE).

**Credit corrections (no mathematics changes).**
1. L15: row 1207 Theorem 4.2's double-commutator display (4.8) FAILS by a sign in check
   row 1208. The citation should say so. Row 1246's own sign (S5) is right.
2. L34: row 1236 (6)-(10) does not contain the order v_{d+1} > v_d. It has
   c'_d >= 0, an order in beta. The file proves the order in d itself on the same line.
3. L276: the volume growth of the Birkhoff/Hopf projective diameter is already on file:
   `gap-crux-skeleton-max.md` Lemma B2; `gap-fr-opus.md` L99; `gap-mini-free-fable.md`
   L222 and L379. Cite it. The new content is the lower bounds (16) and (22).
4. Suggested, recalled and not opened in this run, so not a verdict: the idea that Wilson
   loop traces fix the gauge orbit is classical (R. Giles, Phys. Rev. D 24 (1981) 2160).
   So are trace coordinates for SU(2)-characters of a free group (Fricke-Vogt; Procesi).
   The file proves what it uses, so these are credits only.

**Guide run (no step rests on it).** Pure Python, under the numeric lock, memory free 57%,
in a scratch folder. Over 200 random configurations, finite differences agree with
(2), (3), the triple-trace formula and the equal (AB, C) contributions on x and z, to
2e-10. v_d increases in d at beta = 0.3, 1, 4, 20. 2 beta (1-c_d)/(d^2-1) is
0.995, 0.970, 0.937 at beta = 50 and 0.999, 0.993, 0.984 at beta = 200 for d = 2, 3, 4,
consistent with (5). The radial constant equals 1/pi^2.

## Step 7. Verdicts

| Statement | Lines | Verdict |
|---|---|---|
| S1 transfer, positive simple top vector | L21 | HOLDS |
| S2 algebra and cyclic space | L23 | HOLDS |
| S3 joint eigenvalues (1), v_d increasing | L25-34 | HOLDS (credit correction 2) |
| S4 projections, S_{e,h} | L36 | HOLDS |
| S5 double commutator -> 2 Gamma_e | L38 | HOLDS |
| S6 identity (2), corner orbit | L42-56 | HOLDS |
| S7 extension (3), open box | L58-72 | HOLDS |
| S8 seams | L76-82 | HOLDS |
| S9 (4) with marked generators | L84-90 | HOLDS |
| S10 (5), countable exceptional set | L96-101 | HOLDS |
| S11 global temporal-sum reading | L103 | HOLDS |
| S12 octant reconstruction; (4) spatial-only off E | L105-117 | HOLDS |
| S13 barycentre isolation | L123 | HOLDS |
| S14 (6)-(7) statistic and exact rate | L125-146 | HOLDS |
| S15 (8)-(11); (4) spatial-only at every beta | L152-191 | HOLDS (wording at L175: continuous cutoff) |
| S16 (12)-(14) | L197-229 | HOLDS given row 1231 (2)-(5) (checked HOLDS, row 1235) |
| S17 (15) | L231-237 | HOLDS given the same |
| S18 (16)-(17) | L243-274 | HOLDS |
| S19 endpoint-comparison obstruction | L276 | HOLDS (credit correction 3) |
| S20 fixed depth m_* (18)-(19) | L280-304 | HOLDS |
| S21 D_* exact rate | L306-311 | HOLDS |
| S22 reweighting cost | L313 | HOLDS |
| S23 (20)-(22) | L319-336 | HOLDS given row 1161 (19) (checked HOLDS, row 1162) |
| S24 (23) | L340-344 | HOLDS (typo L344: "(21)" means (23)) |
| S25 (24) | L348-354 | HOLDS (one line supplied: C_J and C_Jbar commute) |
| S26 (25) | L356-362 | HOLDS |
| S27 (26), scaling | L364-373 | HOLDS |
| S28 all bounded operators at depth 2m_*+1 | L377 | HOLDS |
| S29 (27), matching, the gap | L379-386, L402 | OPEN, as labelled |
| S30 (27) plus matching gives a gap | L388-400 | HOLDS as an implication |
| GUIDE citation of row 1207 | L15 | HOLDS AFTER CORRECTION (credit only, correction 1) |

Totals: 29 numbered statements HOLD (three given checked earlier rows, one as an
implication). S29 is OPEN as labelled. 0 FAILS. The corrections are credit only
(L15, L34, L276), plus one wording repair (L175), one typo (L344) and one supplied line
(L354).

**Scope.** Claims A and B hold at each fixed n >= 4 and beta > 0. Neither is uniform. The
depth m_* is uniform, but the norms of the preparations are not (S22, and D^{-1} up to
e^{3 beta n^3/2}). The detector's physical slab width m_* a tends to 0. (27) and the
continuum matching stay open. So does the Jaffe-Witten gap. This check grants no status.
It is one cross-provider reading, not an audit.

## Step 8. Result (done 10:12Z)

RESULT: row 1246 HOLDS AFTER CORRECTION (credit only). Claude Opus 5.5 max (Mac mini worker 3, 09:50Z-10:12Z) checked it line by line by hand. This is a cross-provider check of gpt-6.2-astra and grants no status. 29 numbered statements HOLD and 0 FAIL; S29 is OPEN as labelled. Claim A HOLDS: at every n >= 4 and beta > 0, words in T and the spatial plaquette multipliers are cyclic for the centre-neutral space H_+ (one wording repair, L175). Claim B HOLDS: one slab of fixed depth m_* <= 1.84e8, independent of n and beta, with a temporal mean on each cut, prepares a dense subspace, and D_* has exact rate r_+. The norms are not uniform. Credit corrections: L15 (row 1207 (4.8) failed by a sign in row 1208), L34 (row 1236 lacks the order in d), L276 (the Birkhoff/Hopf obstruction is on file). The main comparison (12)-(15) restates in substance row 1231 (3)-(6), through a kernel statistic. (16) and (22) extend rows 1151 and 1161, and (4) is new. A guide run agrees. OPEN: (27), continuum matching, the Jaffe-Witten mass gap.
