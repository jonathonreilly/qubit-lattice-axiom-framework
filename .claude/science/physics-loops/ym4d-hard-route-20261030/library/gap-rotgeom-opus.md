lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T02:09Z

# Row 963, gap-rotgeom-opus: rotated and diagonal geometry for the seed

Queue row 963 of `FINISH.md` (pinned at commit 3900bfe8b). Owner's question: "could the box
rotate in time as well?" Test item, analysis plus GUIDE. Author: Claude Opus 5.5 max, Mac mini
worker 2. Labels: PROVED (written argument, checkable by hand), CONDITIONAL (proved given a
named hypothesis), GUIDE (a run or heuristic; refutes or guides only), OPEN.

## Plan (at most eight steps; one step per response, each appended here before the next)

1. Sources: FINISH rules; rows 960 (`gap-vargeom-opus.md`), 962 (`gap-constraints-max.md`),
   row 892 section 4.1 (Lemma SPLIT, centre-twist flux sectors); the definition of the seed
   S(a; B); grep `open-core.md` and the FINISH rows for overlap.
2. Item (1): twisted tori. Exact statement of Tr((R T)^a) = Tr(R^a T^a); sector decomposition of
   the seed by characters of the spatial symmetry group; the centre-twist flux sectors as the
   existing analogue.
3. Item (2): sector-wise statements. Which sectors carry the soft modes (free photon, U(1)
   toron, frozen Q_8 / 2T flat vectors); whether momentum or lattice angular momentum gives a
   free-energy margin; whether the trivial sector carries the full order-one difficulty.
4. Item (3a): reflection positivity of the Wilson action across diagonal hyperplanes: literature
   with sources, and a by-hand proof or refutation on the smallest case.
5. Item (3b): what a diagonal transfer operator and its thermal sum give relative to the axis one.
6. Item (4): fact tests (U(1), frozen groups, SMALL-BOX) by hand.
7. GUIDE: sector thermal sums in a solvable model (only if cheap), scripts in `guide/lane963/`.
8. Verdict: does rotated or diagonal geometry buy anything over the static axis tori, and why.
   RESULT line.

## Step log

(Steps are appended below as they finish.)

- 2026-11-14T14:40Z: Steps 1-6 written; Step 7 criteria written; the numeric lock is held by row 968's GUIDE batch
  (lease to 16:32Z), so the run waits for the lock. The "done" times of the step headings were removed: I had
  written estimated clock times that were wrong.
- 2026-11-14T15:33Z: Step 7 run done (lock held 15:32:03Z to 15:33:09Z, memory free 72 percent, peak RSS 0.80 GB,
  66 s). Results and the final RESULT line written at the end of the file.

### Step 1. Repo search and sources (done)

**Repo search (rule 0a).** `grep -i "rotat|diagonal refl|angular mom|point group|cubic irrep|mapping torus|twisted tor"`
over `library/open-core.md`: no line. Over FINISH rows: only rows 962 and 963. So no open lemma of this item is owned
by another row. Prior work that this item must build on, not repeat:

- Row 962 (`gap-constraints-max.md`, Claude Fable 5.2 max, unchecked). A4 sheared tori and Lemma SHIFT; B1 projected
  (momentum, cubic irrep, parity, centre) seeds; Section 7.4 projected doubling and the projected crossing identity
  (the deficit step needs the full sum); A5 Klein gluing Tr(T_b^a R) with R a reflection (not selective: R reverses
  U(1) flux); A6 diagonal reflections (ARGUED, "thresholds are not the obstacle"); B2 twist-summed engine (seed false
  in the confined phase). Theorem 2O (engine without axis exchange). Its finding: no relaxation is a NEW INPUT.
- Row 960 (`gap-vargeom-opus.md`): varying geometry buys nothing (Lemma NO-OP, DEN, OVL).
- Row 892 Section 4.1 (`gap-crux-core-max.md` L265-280): Lemma SPLIT. Setting: T = T_(B,0) on a periodic box B,
  commuting centre flips C_2, C_3, C_4, eight sector projections P_chi, Z_chi(t) = Tr(T^t P_chi) >= 0,
  S_ev = Z_0/lambda_0^t - 1, q_i = Tr(T^t (1 - C_i)/2)/Tr T^t = (1 - Z^(v_1i)/Z^0)/2, Q_0 = max q_i. Then
  (1 + S_ev)/(1 - Q_0) <= 1 + S <= (1 + S_ev)/(1 - 3 Q_0). The twisted partition function Z^(v_1i) = Tr(T^t C_i) is
  the centre-twist analogue of the rotated trace of item (1).
- **Diagonal reflection positivity is already in the repository and in the account.** `library/am1-port.md` Section 3
  (Codex, a port of Sussman-Alpoge YM3_I IV-16-26 and SA 2773-2883): allowed normals e_mu and e_mu +- e_lambda,
  diagonal mirror heights c in Z, adapted tori Gamma = T (+) Z(L n/|n|^2) with T in n-perp; at a diagonal cut "the
  only crossing plaquettes have heights c-1, c, c, c+1, in the (1, 2) plane ... Their weight is k(P_+, P_-), and
  reflection exchanges the paths" (L62), with the positive Gram expansion k(g, h) = e^(-beta) e^(beta s(g).s(h))
  (L50-57). Its Lemma S (Claude, checked by Codex, L6-14): no lattice is adapted to both e_4 and e_1 - e_4. LG1
  Theorem 10 and 13(5) (`library/lg1.md`): every periodic Wilson DLR state is RP at the diagonal lattice mirrors.
  `library/ro1-vs-ca.md` L52 quotes CA-III L79973-79974: "Diagonal reflection positivity holds for the Wilson weight
  on Z^4 and fails on every straight torus", and CA-III Remark 10.1 (L79931-79990). So item (3) is a citation plus
  the transfer-operator question; I do not re-prove the positivity, I restate it with its sources and test it on the
  smallest case.
- Seed: S(a; B) = Tr(T_B^a)/lambda_0^a - 1 (`gap-seed-shape.md`, Theorem SH, checked row 707); engine of row 962
  Section 1.1 (Lemmas K, X, E', Theorem SH; uses (TM) in each direction, the exchange of two axes, a simple top
  eigenvalue).

Next: Step 2, item (1), the twisted-trace identity and the sector decomposition.

### Step 2. Item (1): rotating boxes are twisted tori; sector decomposition (done)

**Setting R.** B a periodic box with sides b_2, b_3, b_4 >= 3, Omega_B = SU(2)^(E(B)) with Haar measure,
H_B = L^2(Omega_B). Input (TM), the lane's items 5-6 (the m = 0 case of (TM-tw), `gap-flux-exercise.md` L115;
used by Lemma SPLIT): T_B is an integral operator with strictly positive continuous kernel K_B, positive, trace
class, Z(a; B) = Tr T_B^a, and K_B is built from the Wilson action and Haar measure (T_B = M' C_E M' in the lane's
notation, L418). Sym(B) = the lattice symmetries of the box (translations, permutations of axes of equal length,
reflections). g in Sym(B) acts on configurations by (g.U)_(g x, g y) = U_(x, y), with U_(y, x) = U_(x, y)^(-1), and
on H_B by (V_g psi)(U) = psi(g^(-1).U). C_2, C_3, C_4 are the lane's centre flips.

**Lemma R1 (symmetries; PROVED given (TM)).** (a) V_g is unitary, maps nonnegative functions to nonnegative
functions, and commutes with T_B. (b) The top eigenvalue lambda_0 of T_B is simple with a strictly positive
eigenfunction Omega_0, and V_g Omega_0 = Omega_0 and C_nu Omega_0 = Omega_0. (c) Tr(V_g T_B^a) > 0 and
Tr(V_g T_B^a) <= Tr T_B^a.
Proof. (a) Haar measure and the Wilson action are invariant under g, so K_B(g.U, g.U') = K_B(U, U'). (b) Simplicity
and positivity are Jentzsch's theorem for a strictly positive continuous kernel on a compact space (the lane's (TM)
states them). V_g Omega_0 is again a top eigenfunction, so V_g Omega_0 = c Omega_0 with |c| = 1; both functions are
positive, so c > 0 and c = 1. The flips are the same (they act by a measure-preserving change of variables).
(c) Tr(V_g T^a) is the integral of the positive kernel of T^a at (g^(-1).U, U). The upper bound is
|Tr(V T^a)| <= Tr T^a for unitary V and positive T^a. QED

**Lemma R2 (a box that rotates in time; PROVED).** For g_1, ..., g_a in Sym(B),
Tr(V_(g_1) T_B V_(g_2) T_B ... V_(g_a) T_B) = Tr(V_h T_B^a), h = g_1 g_2 ... g_a.
In particular Tr((V_R T_B)^a) = Tr(V_R^a T_B^a) = Tr(V_(R^a) T_B^a), and the value depends only on the conjugacy
class of h in Sym(B). So every schedule of rotations, reflections and translations of the box, one per time step,
gives one number per conjugacy class of the total product. A 90-degree rotation R per step with 4 | a gives the
plain torus back.
Proof. V_g commutes with T_B (Lemma R1 (a)); move each V_(g_i) to the left and use V_g V_k = V_(gk). Conjugation:
Tr(V_k V_h V_k^(-1) T^a) = Tr(V_h V_k^(-1) T^a V_k) = Tr(V_h T^a). QED

**Lemma R3 (the twisted torus; PROVED given (TM) in kernel form).** Tr(V_g T_B^a) = Z(a; B; g), the Wilson
partition function on the lattice M_g(a; B) := (Z x B)/((t, x) ~ (t + a, g x)) (the mapping torus of g; it is
non-orientable when g reverses orientation, and the Wilson weight is still defined because Re tr does not see the
orientation). Z(a; B; g) = Z(a; B; g^(-1)) by the time reflection.
Proof. Write the kernel of T_B^a as the a-fold composition of K_B. The kernel of V_g T_B^a at (U, U') is
K_B^(a)(g^(-1).U, U'); the trace sets U' = U, which glues slice a to slice 0 through g. Each factor K_B is the
Wilson weight of one time layer (time links integrated, spatial plaquettes split half and half), so the integrand
is the Wilson weight of M_g(a; B). QED
The centre analogue is (TM-tw): Z^(e)(a; B) = Tr(T_B^a C^e), the 't Hooft twist in the planes (1, nu).

**Lemma R4 (sector decomposition; PROVED).** Let G be a finite group and V a unitary representation of G on H_B
that commutes with T_B (G = Sym(B), the centre flips Z_2^3, or the group they generate on gauge-invariant
states). For an irreducible representation rho (dimension d_rho, character chi_rho) let
P_rho = (d_rho/|G|) sum_g conj(chi_rho(g)) V_g and Z_rho(a) := Tr(T_B^a P_rho) >= 0. Then
(i) Z(a; B) = sum_rho Z_rho(a);
(ii) Tr(V_g T_B^a) = sum_rho (chi_rho(g)/d_rho) Z_rho(a) for every g in G;
(iii) Z_rho(a) = (d_rho/|G|) sum_g conj(chi_rho(g)) Tr(V_g T_B^a).
Proof. (i) sum_rho P_rho = 1. (iii) is the definition. (ii) On the rho-isotypic subspace H_rho = M_rho (x) W_rho,
G acts as 1 (x) rho(g) and T_B as T_rho (x) 1 (Schur), so Tr(V_g T^a P_rho) = chi_rho(g) Tr(T_rho^a) and
Z_rho = d_rho Tr(T_rho^a). Sum over rho. QED
For G = Z_2^3 (the flips) this is the lane's (F1): Z^(e) = sum_chi chi(e) Z_chi.

**Sector seeds.** S_rho(a; B) := Z_rho(a)/lambda_0^a - delta_(rho, 1), 1 the trivial representation. By Lemma
R1 (b) the vacuum is in the trivial sector, so S_rho >= 0 and

S(a; B) = sum_rho S_rho(a; B),   Tr(V_g T_B^a)/lambda_0^a = 1 + sum_rho (chi_rho(g)/d_rho) S_rho(a; B).

So the rotated seed Tr(V_h T^a)/lambda_0^a - 1 is a SIGNED sum of the sector seeds. It is not a thermal sum of a
positive operator.

**Lemma R5 (SPLIT for any finite symmetry group; PROVED).** Let Sigma be a generating set of G with
Sigma = Sigma^(-1). Let kappa(G, Sigma) be the least eigenvalue, over the nontrivial irreducible rho, of the
Hermitian matrix L_rho = sum_(s in Sigma) (1 - rho(s)). Put q_s := (1 - Re Tr(V_s T_B^a)/Tr T_B^a)/2 and
1 + S_1 := Z_1(a)/lambda_0^a. Then

max_(s in Sigma) q_s <= 1 - Z_1/Z <= (2/kappa) sum_(s in Sigma) q_s,

hence (1 + S_1)/(1 - max_s q_s) <= 1 + S <= (1 + S_1)/(1 - (2/kappa) sum_s q_s) when the last denominator is
positive. Also S_1 <= S, 1 + S_1 >= (1 + S)/|G|, and every q_s <= S/(1 + S).
Proof. L_rho >= 0, and L_rho w = 0 forces rho(s) w = w for every generator, so w = 0 for nontrivial irreducible
rho: kappa > 0. On H_rho, sum_s (1 - Re V_s) = sum_s (1 - (V_s + V_s^*)/2) acts as 1 (x) L_rho (Sigma symmetric), so
sum_s (1 - Re V_s) >= kappa (1 - P_1); and 0 <= 1 - Re V_s <= 2 (1 - P_1). Multiply by T^a (commuting, positive),
take traces, divide by Tr T^a. The bound 1 + S_1 >= (1 + S)/|G| is Lemma R4 (iii) for rho = 1 with every
Tr(V_g T^a) > 0 (Lemma R1 (c)). Last: Z_1 >= lambda_0^a. QED
Check against Lemma SPLIT: G = Z_2^3, Sigma = {C_2, C_3, C_4}: L_chi = 2 #{s: chi(s) = -1} >= 2, so kappa = 2 and
(2/kappa) sum q_s = q_2 + q_3 + q_4 <= 3 Q_0: Lemma SPLIT is the case G = Z_2^3 of Lemma R5.

**What item (1) gives (ARGUED from R1-R5).** Rotating the box in time gives nothing beyond the family
{Tr(V_h T^a): h in a conjugacy class}, the Fourier coefficients of the sector seeds. The costs of using it in a
SPLIT-type bound are the Kazhdan constants: kappa = 2 for the centre flips; for the translations Z_b^3 with
Sigma = {tau_i^(+-1)}, kappa = 4 sin^2(pi/b), so (2/kappa) sum q_s = 3 q_tau/sin^2(pi/b), about 3 b^2 q_tau/pi^2; for the
48 point-group elements of a cube, kappa is a pure number. Next: Step 3, which sectors carry the soft modes.

### Step 3. Item (2): which sectors carry the soft modes; is any sector easier? (done)

Group used: G_full = (centre flips Z_2^3) x| Sym(b^3) on gauge-invariant states, Sym(b^3) = translations Z_b^3
x| O_h (48 point-group elements: permutations of the three axes and the three inversions). "Trivial sector" = the
trivial representation of G_full: centre-even, zero momentum, A_1 under O_h.

**3.1 Frozen Q_8 and 2T (PROVED, by hand count).** At beta = infinity the gauge-invariant transfer operator of a
finite group H projects on flat spatial connections, and all its nonzero eigenvalues are equal, with multiplicity
N_flat = |Hom(Z^3, H)/H| (commuting triples up to simultaneous conjugation). G_full permutes the flat classes (a
flip multiplies h_nu by -1; a permutation of axes permutes entries; the inversion of axis nu replaces h_nu by its
inverse; translations act trivially). So the frozen ground space restricted to a sector is a permutation module, and
its trivial part has one vector per G_full-orbit.
- Q_8. Commuting triples: 8 central ones, and for each of x = i, j, k the 4^3 - 8 = 56 triples in <x> with a
  noncentral entry; conjugation by j (or k) maps x to -x, so N_flat = 8 + 3 x 28 = 92. Flip-fixed classes for C_2:
  type (noncentral, central, central), 4 per x, 12 in all, so Z^v/Z = 12/92 = 3/23 and q = 10/23: this reproduces
  the lane's FT-FROZEN number p = 10/23 (row 962, 1.4), an independent check of the count. Flip orbits: 1 central
  orbit, and for each x one orbit per nonempty set S of noncentral positions (the flips act transitively on the
  signs): 1 + 3 x 7 = 22, so S_ev = 21 in the frozen limit. Point group on top: permutations act on S, inversions
  keep S, so the orbits are labelled by |S| in {1, 2, 3}: **1 + 3 x 3 = 10 orbits; S_1 = 9 in the trivial sector**
  (S = 91 in all sectors).
- 2T (order 24). Maximal abelian subgroups: <i>, <j>, <k> (order 4, conjugate under 2T) and four conjugate cyclic
  groups <u> of order 6 (u = (1 + i + j + k)/2), each its own normalizer, with u not conjugate to u^(-1) and not to
  -u. N_flat = 8 + 168/6 + 832/4 = 8 + 28 + 208 = 244; flip-fixed classes for C_2: 4 (type (n, c, c) of the order-4
  family), so Z^v/Z = 1/61 and q = 30/61, again the lane's number. Flip orbits: 1 + 7 + (3 x 2 + 3 x 4 + 8) = 34
  (each noncentral entry of the order-6 family is [u] or [u^(-1)] up to sign). Point group (inversions exchange [u]
  and [u^(-1)] at one position): **1 + 3 + 3 = 7 orbits; S_1 = 6 in the trivial sector** (S = 243).
So the zero-quantum-number sector keeps an exact degeneracy of 10 (Q_8) or 7 (2T) frozen flat vectors. A seed stated
in that sector fails for the frozen groups, as any form must (its consumer, a gap in that sector, is false there).

**3.2 Compact U(1) (Coulomb phase): torons and photons (ARGUED; the counting is PROVED from the stated spectrum).**
Spectrum used (the standard weak-coupling Hamiltonian picture, RECALLED, not derived here): the zero mode is the
torus of flat holonomies theta in T^3; its conjugate is the electric flux e in Z^3 with energy g^2 |e|^2/(2b)
(lattice units, uniform field e/b^2 on b^3 links); the rest are photons, momentum p in (2 pi/b) Z_b^3 \ {0}, two
polarizations, energy omega(p) >= 2 sin(pi/b).
- Torons. A flux state has zero momentum. Under the lane's flips it is odd in direction nu iff e_nu is odd, so the
  odd e fill the flux half Q_0 and the even e != 0 sit in the even sector, in S_ev. Under O_h, e is a polar vector;
  each orbit O_h e carries exactly one A_1 vector. So the trivial sector of G_full keeps one toron state per O_h-orbit
  of (2Z)^3 \ {0}. Count at the seed shape b = 24 a: sum over e in (2Z)^3 of exp(-a g^2 |e|^2/(2b)) =
  (sum_n exp(-g^2 n^2/12))^3, about (12 pi/g^2)^(3/2) = 231/g^3, so the trivial sector holds about 231/(48 g^3), that
  is 4.8/g^3, toron states below energy of order 1/a (GUIDE arithmetic). The projection divides the toron count by
  8 x 48 = 384 and leaves it of order one or more at g <= 1.
- Photons. One-photon states have p != 0 and are centre-even. The trivial sector holds no one-photon state; it
  holds the A_1, zero-total-momentum part of the multi-photon gas (the lightest: two photons at +- p_min, energy
  about 4 pi/b, weight e^(-pi/6) = 0.59 per state at b = 24 a). Lemma R5 gives 1 + S_1 >= (1 + S)/|G_full| with
  |G_full| = 8 x 48 x b^3. At the seed shape the free count of row 962 (1.5) is log(1 + S) about 9.1e3, and at
  a = 30, b = 720: log |G_full| = log(384 x 3.7e8) = 25.7. So log(1 + S_1) >= 9.1e3 - 26: FT-U1 fails in the
  trivial sector by the same extensive margin. Projection removes log |G|, never an extensive amount.

**3.3 Momentum and lattice angular momentum give no free-energy margin (ARGUED, dilute-gas reading; GUIDE in Step 7).**
A margin would be a lower bound on the lowest energy of a nontrivial sector well above the gap, so that the
nontrivial sectors are automatically small. There is none:
- Momentum p != 0: the lowest state is one particle of momentum p, energy sqrt(m^2 + p^2) = m + p^2/(2m) + ..., so
  the margin over the gap is p^2/(2m), about (2 pi/b)^2/(2m); for the photon it is omega(p_min), about 2 pi/b, and
  e^(-a 2 pi/b) = e^(-2 pi/24) = 0.77 at the seed shape. The p != 0 sectors together carry the one-particle count
  b^3 (m/(2 pi a))^(3/2) e^(-m a), the volume factor of the seed.
- Lattice angular momentum at p = 0: two identical scalars at +- q are labelled by the unordered pair {q, -q};
  the inversion fixes each pair (and acts as +1 on the symmetric state), so for generic q the pairs fill the regular
  representation of O_h/{1, -1} (24 elements): every inversion-even irreducible rho gets d_rho^2/24 of the
  two-particle continuum, which starts at 2 sqrt(m^2 + (2 pi/b)^2); the inversion-odd sectors get none from pairs
  of one species and start at three particles or at a particle with spin. (Corrected about 14:40Z; the first text said
  d_rho^2/48 in every sector.) One particle of spin J != 0 at rest is heavier than 0++ (a spectral fact of the
  model, not a bound we have).
- The twisted tori do have a large free-energy deficit (for the free photon, log Z(a; B; R)/lambda_0^a is about
  (1/256) of the untwisted thermal free energy for a quarter turn R, plus a term of order b/a from the axis, because
  away from the axis the mapping torus is locally the torus of time 4a). But that deficit is what spreads a LARGE
  thermal sum evenly over the sectors (S_rho about d_rho^2 S/|G|); it makes no sector small. When S is small (the
  seed regime) Lemma R4 (ii) gives Tr(V_R T^a)/lambda_0^a = 1 + O(S): nothing to exploit.

**3.4 The zero-quantum-number sector carries the full order-one difficulty (ARGUED from 3.1-3.3 and Lemma R5).**
(i) It contains the vacuum, the lightest excitation of the confining theory (0++ at rest, which is centre-even,
p = 0, A_1+), so the gap of T_B on it is the mass gap itself. (ii) [CORRECTED about 14:40Z; the first text kept only
one- and two-particle states and gave thresholds 4.5 and 2.5, which are WRONG.] Dilute reading, one free scalar,
b = 24 a, x = m a, one-particle count s(x) = b^3 x^2 K_2(x)/(2 pi^2 a^3) (exact relativistic one-particle sum;
878 x^1.5 e^(-x) is its leading term). Zero total momentum costs a Gaussian volume (2 pi N sigma^2)^(3/2) per
N-particle term, sigma^2 = x b^2/(2 pi a)^2, so S_0 = e^(-x) sum_N s^(N-1)/(N! N^1.5), which grows like
e^(-x) e^s/s^2.5 once s >> 1: the multi-particle zero-momentum states dominate, not the pairs. Hand values (K_2 from
K_0, K_1 tables and the asymptotic series): s(7) = 19.0, s(7.5) = 12.6, s(8) = 8.3, s(9) = 3.7, s(12) = 0.26;
S_0(7) about 106, S_0(7.5) about 0.37, S_0(8) = 0.0094, S_0(9) = 3.2e-4. For the trivial sector of G_full the
twisted traces with R != 1 are 1 + (sums over a plane, a line or the origin), so S_1 is about S_0/48 when S_0 >> 1.
Thresholds for 0.3: full seed x near 12.0 (s = 0.26); p = 0 sector x near 7.55; trivial sector x near 7.2. So the
sector seeds are easier by about 4.5 to 5 units of m a at this shape (they tolerate a gas of about a dozen
particles, because a zero-momentum constraint costs only a power of s while the gas entropy grows like e^s); the
point group adds only about 0.35. Step 7 checks these numbers. (iii) But no consumer
reads it. The engine needs S (Lemma X uses the full trace in both channels), and by Lemma R5 the step from S_1 to S
costs the deficits q_s, which are the weight of the nontrivial sectors: in the dilute gas almost all of S. And the
target (GAP) is a gap for tr F^2 correlations at separated points, which needs the lowest energy at EVERY momentum
and lattice angular momentum; a trivial-sector gap bounds only the zero-momentum A_1 correlator. On the lattice no
statement E(p) >= E(0) is available before O(4).
For the centre flips that split is useful because the electric flux states are heavy in the confined phase
(Lemma SPLIT, Q_0); for the space group it puts almost all of the seed into the deficit half. (iv) Every sector form
still fails FT-U1 (3.2), FT-FROZEN (3.1) and SMALL-BOX (the small-box 0++ level, of order g^(2/3)/b in Luscher's
small-volume expansion, RECALLED, is in the trivial sector), as it must. Next: Step 4, diagonal reflection positivity.

### Step 4. Item (3a): reflection positivity across diagonal hyperplanes (done)

**4.1 Known results, with sources (READ at 3900bfe8b and in CA-III at 31a47c543775).**
- Wilson weight on Z^4, diagonal mirrors {x_mu +- x_nu = c}, c an integer: reflection positive. CA-III L108556-108560:
  "The Wilson weight has that positivity on Z^4: with theta the reflection in the mirror, the plaquettes crossing
  {x_mu = x_nu} enter it as Re tr(A (theta A)^dagger), where A is the product of the two links on one side of the
  mirror. A diagonal hyperplane, however, does not separate the periodic torus on which the lattice measures of
  Theorem 0 live. This positivity is therefore not asserted for the limits of Theorem 0 and is not used in this
  book." CA-III L79973-79974 (Remark 10.1:rem-diagonal-positivity): "Diagonal reflection positivity holds for the
  Wilson weight on Z^4 and fails on every straight torus". Sussman and Alpoge, with Claude and Codex as authors.
- Our rebuild: `library/am1-port.md` Section 3 (Codex, a port of their YM3_I IV-16-26 with SA 2773-2883): allowed
  normals e_mu and e_mu +- e_lambda; diagonal mirror heights c in Z; adapted tori Gamma = T (+) Z(L n/|n|^2), T in
  n-perp, with two cuts at heights c and c + L/2; the Gram expansion k(g, h) = e^(-beta) e^(beta s(g).s(h)) with
  (1/2) tr(g h^(-1)) = s(g).s(h) for unit quaternions; RP for every bounded half test, gauge-invariant or not.
  Section 5 there (IV-29-40) folds along diagonal tori Gamma_i to prove that every periodic DLR state is diagonally
  RP; `library/lg1.md` Theorem 10 and 13(5) state it (frozen, one Claude gate per `ro1-vs-ca.md` L50). Lemma S
  (`am1-port.md` L6-14, Claude, checked by Codex): no lattice is adapted to both e_4 and e_1 - e_4.
- Older literature (RECALLED, not read, not used): Osterwalder and Seiler (1978) for coordinate site and link
  reflections of the Wilson action; Frohlich, Israel, Lieb and Simon (1978) for the general reflection and chessboard
  machinery. I did not find or read a classical source for diagonal mirrors in lattice gauge theory.

**4.2 Smallest case by hand: the crossing plaquette (PROVED).** Take n = e_1 + e_2, mirror {x_1 + x_2 = 1},
theta(y_1, y_2, y_3, y_4) = (1 - y_2, 1 - y_1, y_3, y_4). A plaquette has corner heights h, h+1, h+1, h+2 (h its
base height), so it meets both open sides iff h = 0: the (1, 2)-plaquette P at base 0 with corners (0,0), (1,0),
(0,1), (1,1) (heights 0, 1, 1, 2). Its two corners at height 1 lie on the mirror and are fixed by theta. Split U_P at
them. The upper path A goes (1,0) -> (1,1) -> (0,1): A = U_((1,0),2) U_((0,1),1)^(-1). The lower path B goes
(1,0) -> (0,0) -> (0,1): B = U_((0,0),1)^(-1) U_((0,0),2). theta maps the link (1,0) -> (1,1) to (1,0) -> (0,0) and the
link (1,1) -> (0,1) to (0,0) -> (0,1), keeping the order of traversal, so theta(A) = B as a function of the links:
the reflected copy of the upper path is exactly the lower path, with no inversion. Then
tr U_P = tr(U_((0,0),1) A U_((0,0),2)^(-1)) = tr(A B^(-1)) = tr(A theta(A)^dagger), and with unit-quaternion
coordinates (1/2) tr(A theta(A)^(-1)) = s(A).s(theta A). So the crossing weight is
exp(beta s(A).s(theta A)) = sum_r (beta^r/r!) sum_(i_1..i_r) F_i(A) F_i(theta A), F_i = prod_j s_(i_j), real: a
positive Gram sum of terms F theta(F). The links in directions 3 and 4 at height 1 are fixed by theta and are the
conditioning variables; every other plaquette lies in a closed half. This is the step that `am1-port.md` L62 states
in four lines; the computation above confirms it, including the orientation (no inverse appears in theta(A)).

**4.3 Straight tori: the diagonal hyperplane does not separate (PROVED, elementary).** Let Lambda = (Z/N)^4 with
N >= 3 and theta(x) = (x_2, x_1, x_3, x_4) (any diagonal swap of a straight torus with N_1 = N_2 = N; if N_1 != N_2
it is not a symmetry at all). Fix(theta) = {x_1 = x_2 mod N}. Claim: the sites off Fix(theta) form ONE connected
set in the nearest-neighbour graph with Fix(theta) removed. Proof: put d = x_1 - x_2 mod N; the level d = k
(k = 1, ..., N - 1) has the sites (x_2 + k, x_2, x_3, x_4). Bonds in directions 3, 4 keep d, so x_3, x_4 move freely
inside a level. A direction-1 bond changes d by +- 1, a direction-2 bond by -+ 1. Inside the level k, go from
(x_2 + k, x_2) to (x_2 + 1 + k, x_2 + 1) through (x_2 + 1 + k, x_2) (level k + 1) if k != N - 1, or through
(x_2 + k, x_2 + 1) (level k - 1) if k != 1; for N >= 3 one of the two is allowed for every k, and repeating the move
runs through all N sites of the level. Levels k and k + 1 (both nonzero) are joined by a direction-1 bond. So the
levels 1, ..., N - 1 form one connected set, and the complement of Fix(theta) is connected. Hence
no split Lambda = Lambda_+ u Lambda_-, theta(Lambda_+) = Lambda_-, Lambda_+ n Lambda_- = Fix(theta), exists in which
every bond and plaquette not meeting Fix(theta) lies in one closed half: a connected complement crosses from one
open half to the other through a bond that avoids the mirror. The positivity argument of 4.2 then has no setting.
This is what CA-III means by "does not separate". (Topologically: on the square 2-torus the swap fixes ONE closed
circle, of length N sqrt 2, and acts on the open annulus around it as a glide; the coordinate reflection fixes two
circles.) I do not claim a negative value of <F theta F> on a straight torus; none is needed and none was sought.

**4.4 Where diagonal RP holds on a torus (PROVED from 4.2 and `am1-port.md` Section 3).** On an adapted torus
Gamma = T (+) Z (L/2) n, n = e_1 + e_2, L even, T a rank-3 lattice in n-perp (for example
T = M Z (e_1 - e_2) (+) N Z e_3 (+) N Z e_4): the mirrors at heights c and c + L/2 bound two slabs exchanged by
theta_c, the crossing plaquettes at both cuts are the diamonds of 4.2, and the Gram argument gives RP. Such a
torus is a straight torus in the rotated frame (n, e_1 - e_2, e_3, e_4); by Lemma S it has no coordinate mirror
normal to e_1 or e_2, so the axis transfer operators in directions 1 and 2 do not exist on it. Next: Step 5, the
diagonal transfer operator and its thermal sum.

### Step 5. Item (3b): the diagonal transfer operator and its thermal sum, against the axis one (done)

Notation: n = e_1 + e_2, n' = e_1 - e_2, height h(x) = x_1 + x_2, mirrors theta_c (c integer). Only integer heights
carry diagonal mirrors: theta_(c + 1/2) does not map Z^4 to itself, so there are no "link" diagonal mirrors.

**Lemma D1 (the diagonal transfer is positive for a step of two heights; PROVED given RP at theta_c and
theta_(c+1)).** theta_(c+1) theta_c = tau_n (translation by n, height + 2). Let nu be a tau_n-invariant state (on Z^4,
or the Wilson measure of an adapted torus), RP at theta_c and theta_(c+1). On the OS space H_c (bounded functions of
the links at heights >= c, form <F, G>_c = nu(theta_c(F) G), null vectors removed) put T_n [F] = [tau_n F]. Then
<F, T_n F>_c >= 0 and T_n is symmetric.
Proof. <F, T_n F>_c = nu(theta_c(F) . theta_(c+1)(theta_c F)) = nu(G theta_(c+1) G) with G = theta_c F, which lives at
heights <= c, inside one closed half of theta_(c+1); RP at theta_(c+1) gives >= 0. Symmetry:
nu(theta_c(tau_n F) G) = nu(tau_(-n)(theta_c F) G) = nu(theta_c(F) tau_n G), because theta_c tau_n = tau_(-n) theta_c and
nu is tau_n-invariant. QED. (That T_n is well defined and a contraction is the standard OS step, RECALLED.) A step of
ONE height is the positive part times a glide reflection of the layer (theta_(c+1) followed by tau_(-e_1)) (ARGUED,
layer bookkeeping not written), so reflection gives it no positivity; the positive diagonal operator is the step n,
of Euclidean length sqrt 2.

**Lemma D2 (every adapted diagonal torus is a sheared axis torus; PROVED).** Let
Gamma = Z (L/2) n (+) Z M n' (+) N Z e_3 (+) N Z e_4, L even, and g = gcd(L/2, M), p = L M/g. Then the (1, 2)-part of
Gamma has the basis (p, 0), (s, g) for some integer s (the Hermite normal form), and

Z(Gamma) = Tr( T_(B')^g tau_1^s ),   B' = (p, N, N) a straight box (sides in directions 1, 3, 4), time along e_2,

with tau_1 the unit translation of B' in direction 1 (Lemma R3 for a translation). For L/2 = M = b: g = b, p = 2b,
s = b, so Z(Gamma) = Tr(T_(B')^b tau_1^b) = Z_even - Z_odd, where Z_even (Z_odd) is the axis thermal trace on the
momenta k in Z_(2b) of direction 1 with k even (odd): tau_1^b acts on momentum k as (-1)^k (Lemma R4 for G = Z_2).
Proof. The (1, 2)-part is {((L/2) j + M k, (L/2) j - M k)}. With L/2 = g u, M = g w, gcd(u, w) = 1: the second
coordinate g (u j - w k) takes every value in g Z; it vanishes iff (j, k) = t (w, u), and then the first coordinate is
2 g u w t = p t. A full-rank sublattice of Z^2 with Lambda n (Z x {0}) = p Z and second coordinates g Z has the basis
(p, 0), (s, g). Gluing the e_2-direction after g steps with a shift s is Tr(T^g tau^s). QED
Reading. The diagonal torus is row 962's sheared family (A4, Lemma SHIFT), not a new geometry. What diagonal RP adds:
on the half-shift torus (L/2 = M) the same number Z_even - Z_odd, a SIGNED axis sum, is also a trace of the positive
diagonal operator T_n (Lemma D1 plus the trace formula on the torus, which I did not write: ARGUED). So the
diagonal channel is a positive channel for a sheared torus, which the axis frame does not have.

**Proposition D3 (fully diagonal tori carry the whole engine; CONDITIONAL).** Put n_1 = e_1 + e_2, n_2 = e_1 - e_2,
n_3 = e_3 + e_4, n_4 = e_3 - e_4 and Gamma_D(alpha) = (+)_i Z alpha_i n_i. Gamma_D is adapted to all four normals n_i
(each n_i-perp contains the other three periods). The lattice symmetries x_2 -> -x_2, x_4 -> -x_4 and
(x_1, x_2) <-> (x_3, x_4) act on the n_i as (12), (34) and (13)(24); they generate the dihedral group of order 8 that
keeps the pairing {n_1, n_2}, {n_3, n_4}, NOT all of S_4 (the map n_2 <-> n_3 fixing n_1, n_4 sends e_1 to
(e_1 + e_2 + e_3 + e_4)/2, not a lattice vector). So n_1 can be exchanged with every n_j, but the exchanges with n_3
and n_4 also swap the other two directions. The engine's three inputs (TM in each direction, exchange of two axes,
simple top eigenvalue) then hold in the frame (n_1, ..., n_4) for boxes whose two spectator sides are equal,
CONDITIONAL on (i) the trace formula Z(Gamma_D) = Tr(T_(n_1)^(alpha_1)) with T_(n_1) positive and trace class on a
slice space, and (ii) a simple top eigenvalue (Jentzsch, if the kernel is strictly positive after the gauge
average). Given (i) and (ii), Lemmas K, X, E' run with W(a, b) = Z(Gamma_D(a, b, c, c)); whether every step of
Theorem SH's recursion keeps the spectators equal, or can be reordered to, I did not check (OPEN, expected yes for
the cube steps). If so, one diagonal seed gives a gap on every larger fully diagonal torus. In a mixed frame (n_1, n_2, e_3, e_4) the exchange n_1 <-> e_3 is not a lattice symmetry
(|n_1|_1 = 2, |e_3|_1 = 1), so the engine there needs two seeds (Theorem 2O of row 962): strictly more input.

**Proposition D4 (the infinite-volume gaps agree within a factor 2 per step; PROVED given LG1 and the two OS
constructions).** Let nu be a periodic Wilson DLR state; by LG1 Theorem 10 it is RP at the coordinate mirrors and at
the diagonal mirrors. Let m_1 be the spectral gap of T_(e_1) on the axis OS space (per step e_1) and m_n that of
T_n on the diagonal OS space (per step n). Then m_1 <= m_n <= 2 m_1; in Euclidean units the two masses agree within
the factor sqrt 2 both ways.
Proof. For local mean-zero F at heights <= c and G at heights >= c, and y in n-perp (translation along n' or e_3,
e_4 commutes with theta_c and preserves heights), nu(F tau_(k n + y) G) = <theta_c F, T_n^k [tau_y G]>_c, so
|nu(F tau_(kn + y) G)| <= C_(F,G) e^(-k m_n). Take k e_1 = (k/2) n + (k/2) n' (k even): decay along e_1 at rate m_n/2
per step for every pair of local observables. The spectral measure of [F] for T_(e_1) then sits in [0, e^(-m_n/2)] on
the vacuum complement, and local F are dense, so m_1 >= m_n/2. The same argument in the axis frame with
k n = k e_1 + k e_2 (tau_(k e_2) commutes with the axis mirror) gives m_n >= m_1. QED
So in infinite volume a diagonal gap and an axis gap are the same statement up to the factor 2: nothing is gained
or lost there. The seed, however, is a finite-volume statement, and the two seeds live on different tori (Lemma S:
no torus has both mirror families in one plane).

**What diagonal geometry gives relative to the axis one (ARGUED from D1-D4).**
(a) No new number: diagonal tori are sheared axis tori (D2); the fully diagonal seed is the thermal sum of a box
rotated by 45 degrees in two planes, the same thermal pressure at the same physical temperature up to lattice
artifacts (the Euclidean step is sqrt 2 per n). FT-U1, FT-FROZEN (the flat classes are Hom(Z^3, H)/H on any 3-torus
slice) and SMALL-BOX come out exactly as for the axis seed.
(b) A rotated copy of the engine (D3), which reaches the account only through a comparison of box shapes: the gap on
large fully diagonal tori gives (by D4) an axis gap for volume-first limits ALONG DIAGONAL TORI; the account's
limits are taken along straight tori. Equality of the two limit states, or a direct comparison of their thermal
sums, is exactly the shape independence that CA-III L79975-79977 says "is not proved". It is a new open obligation,
not a saving.
(c) No exact inequality between an axis seed and a diagonal seed: Lemma S excludes a common torus, so the only
bridge is the bulk free energy, which is the same for every van Hove family; Lemma E' and Proposition B3 compare boxes
within one frame only.
Next: Step 6, the fact tests in one table, then Step 7 (GUIDE).

### Step 6. Item (4): fact tests, all forms in one table (done)

Y = the form fails for the rival, as a sufficient form must; N = the rival passes; "-" = an identity or an engine
(group-blind), not a seed form. K7 is the mixed-action endpoint of row 708 (no seed at any size); identities and
engines are group-blind and do not separate it, as for the axis engine. Sources of each entry are the steps named.

| Form | FT-U1 | FT-FROZEN (Q_8, 2T) | SMALL-BOX | K7 | consumer | label |
|---|---|---|---|---|---|---|
| Rotating box, any schedule: Tr(V_h T^a) (R2, R3) | - | - | - | - | none: a signed sum of sector seeds (R4), at most one positive channel (the rotation axis) | PROVED identity |
| Sector seeds S_rho, any rho (R4) | Y: photons fill p != 0, pairs fill p = 0 (3.2) | Y in the trivial sector (3.1); the other 82 (Q_8) and 236 (2T) frozen vectors fill the rest | Y (3.4 iv) | not tested (see note) | engine needs S; (GAP) needs every momentum (3.4 iii) | PROVED decomposition; ARGUED readings |
| Trivial sector of G_full, S_1 | Y: log(1 + S_1) >= log(1 + S) - 25.7; torons 4.8/g^3 (3.2) | Y: S_1 = 9 (Q_8), 6 (2T) (3.1) | Y | not tested | as above | PROVED counts; GUIDE arithmetic |
| SPLIT for the space group (R5) | - | - | - | - | loses 3 b^2/pi^2 on translations; useful only for the centre (kappa = 2) | PROVED |
| Diagonal seed, fully diagonal torus (D3) | Y: same photon pressure at the same physical temperature (5, (a)) | Y: Hom(Z^3, H)/H on the slice 3-torus, same counts | Y | Y (group-blind engine; K7 has no seed in any frame) | gap on diagonal tori only; needs shape independence (5, (b)) | CONDITIONAL |
| Half-shift identity Z_diag = Z_even - Z_odd (D2) | - | - | - | - | links the diagonal channel to sheared axis sums | PROVED |
| Gap equivalence m_1 <= m_n <= 2 m_1 (D4) | - | - | - | - | infinite volume only | PROVED given LG1 and OS |

Note on K7 in row 2: K7 fails the full seed at every size; S_rho <= S does not make a sector seed fail for K7, so a
sector seed MIGHT hold for K7 in some sector. I did not test it (K7's spectrum is not on disk in a usable form here).
It does not matter for the verdict: no consumer reads a sector seed.

Reading of the table: every seed form that this item produces still fails where it must (U(1), frozen groups,
small boxes), so none is a wrong target; but the only forms that are easier as numbers (the sector seeds, 3.4 ii) have
no consumer, and the forms with a consumer (the diagonal seed, D3) are the same number in another frame.
Next: Step 7, GUIDE run in the free scalar field.

### Step 7. GUIDE: sector thermal sums of a free massive scalar (criteria written before the run, 2026-11-14T14:36Z)

Model: one free real scalar of mass m on the periodic cube of side L = 24 tau (continuum dispersion
omega_k = sqrt(m^2 + (2 pi k/L)^2), k in Z^3, |k_i| <= 60), Euclidean time tau = 1, x = m tau. Exact Fock traces:
Tr(V_R e^(i theta.P) e^(-H)) = 1/det(1 - R e^(i theta.P) e^(-h)) on the one-particle space (vacuum energy 0), so
log Tr = sum_n (1/n) sum_(k: R^n k = k) e^(i theta.(k + Rk + ... + R^(n-1) k)) e^(-n omega_k). The p = 0 projection
is the mean over a 192^3 grid of theta (aliasing only from total momentum in 192 Z^3; with about s particles of
per-component momentum spread sqrt(x) b/(2 pi a), the total spread at x >= 6.5 is at most about 53 units, so the
aliased weight is below e^(-6.6) there; the p = 0 columns at x <= 6 may be aliased and are not used); the
trivial sector of the space group is (1/48) sum over O_h of the R-twisted p = 0 traces (Lemma R4 (iii)), summed by
conjugacy class (Lemma R2). Script `guide/lane963/sector_sums.py`. A run guides; it proves nothing.

Criteria, written first. While writing them I found that the arithmetic of 3.4 (ii) keeps only one- and
two-particle states. With one-particle count s = 878 x^1.5 e^(-x), the p = 0 sum is about
(e^(-x)/s) sum_N s^N/(N! N^1.5), and that is large once s >> 1. So I predict that 3.4 (ii) is WRONG for the
projected sectors.
- C1 (full seed): S <= 0.3 first at x_full in [11, 13]. Fail otherwise.
- C2 (claim of 3.4 ii, p = 0): threshold x_0 in [3.5, 5]. Predicted to FAIL; the corrected estimate is x_0 near 7.3.
- C3 (claim of 3.4 ii, trivial sector): threshold x_1 in [1.5, 3]. Predicted to FAIL; corrected estimate x_1 near 6.9.
- C4 (3.3, quarter turn R about an axis): log Tr(V_R e^(-H)) <= 0.02 log Tr e^(-H) at x = 0.25 (the twisted torus
  keeps under 2 percent of the thermal free energy). Fail otherwise.

(Step 7 results: see "Step 7 results" after Step 5b below.)

### Step 8. Verdict (drafted while the Step 7 run waited; the run changed no conclusion, only confirmed the corrected numbers)

**Does rotated or diagonal geometry buy anything over the static axis tori? No, not for the seed.**

The reason, in three parts. The seed number is fixed by the measure and the physical size (row 962, 8.1). Every
rotated or diagonal object of this item is one of three kinds, and none of them changes that number or gives a
consumer a weaker input:
1. **A box that rotates in time is a twisted torus** (Lemmas R2, R3). Only the total twist h counts, up to
   conjugacy. Its trace Tr(V_h T^a) is a signed sum of the sector seeds (Lemma R4), not the thermal sum of a
   positive operator. The mapping torus of a rotation has at most one positive transfer channel (along the rotation
   axis), so the engine (Lemmas K, X, E', Theorem SH, Theorem 2O) does not run on it.
2. **Sector seeds are weaker, and as numbers easier, but no consumer reads them.** S = sum_rho S_rho (Lemma R4).
   The trivial sector of centre x space group keeps the vacuum, the 0++ at rest, the zero-momentum multi-particle
   continuum, one toron state per orbit (U(1)), and 10 (Q_8) or 7 (2T) frozen flat vectors (3.1, 3.2). So every
   sector form still fails U(1), the frozen groups and SMALL-BOX, as it must. In the dilute free-scalar reading at
   b = 24 a it needs m a near 7.15 in place of 12.0 (3.4 (ii), corrected; Step 7 GUIDE: 7.15 and 7.49 for the
   trivial and the p = 0 sector, 12.0 for the full seed). But the engine needs the
   full trace in both channels, Lemma R5 shows that the step from S_1 back to S costs exactly the weight of the
   other sectors, and the target (GAP) needs the gap at every momentum and angular momentum. Momentum and lattice
   angular momentum give no energy margin (3.3); projection removes the logarithm of the number of populated
   sectors, never an extensive amount.
3. **Diagonal mirrors give the same thermal sum in another frame.** Diagonal reflection positivity holds on Z^4 and
   on adapted tori (CA-III L108556-108560, `am1-port.md` Section 3; smallest case checked by hand in 4.2) and fails
   on every straight torus because the mirror does not separate (4.3, proved). The positive diagonal operator is the
   step n = e_1 + e_2 (Lemma D1). Adapted diagonal tori are sheared axis tori (Lemma D2: on the doubled square,
   Z_diag = Z_even - Z_odd). Fully diagonal tori carry a rotated copy of the engine (Proposition D3, conditional on
   the trace formula), and in infinite volume the diagonal and axis gaps are equivalent within a factor 2 per step
   (Proposition D4). The diagonal seed is the same thermal pressure at the same physical temperature; to reach the
   account's limits along straight tori it needs a box-shape independence that CA-III L79975-79977 says is not
   proved. That is a new obligation, not a saving.

**What would change the verdict.** A consumer for a projected seed: a crossing identity for Tr(T^a P_1) whose
twisted crossed channels are controlled without the full sum (row 962, 7.4, names the same obstacle for momentum), or
a lattice statement that the lowest energy at momentum p and angular momentum rho is at least the trivial-sector
gap. I know neither. Neither is attacked here: both are outside this test item, and row 962 (8.2, ranked item 3) already names the projected engine as a possible lane.

**By-products that stand on their own (PROVED unless marked):**
- Lemma R5: Lemma SPLIT for any finite symmetry group, with the Kazhdan constant of a generating set; Lemma SPLIT is
  its case G = Z_2^3 with kappa = 2. For the translations kappa = 4 sin^2(pi/b), so the space-group split loses
  about 3 b^2/pi^2.
- Frozen counts: N_flat = 92 (Q_8) and 244 (2T), which reproduce the lane's p = 10/23 and 30/61; the trivial sector of
  centre x space group keeps 10 and 7 frozen vectors.
- Lemma D2 and the half-shift identity; Proposition D4 (given LG1 and the OS constructions); Lemma D1.
- 4.3: the straight-torus non-separation, the reason CA-III gives, written as a proof.

### Step 5b (addendum to item (3)). Which hyperplane reflections exist at all; note for row 967

Row 967 (`gap-pca-opus.md` L224-229) leaves reflection positivity across diagonal hyperplanes to this row, and
states that the reflection along v = (1, 1, 1, 1) is not a symmetry of Z^4.

**Lemma M (the lattice mirrors of Z^d; PROVED).** A reflection theta(x) = x - 2 ((n.x - c)/|n|^2) n, n a primitive
integer vector, maps Z^d onto itself iff n = +- e_mu with c in (1/2) Z, or n = +- e_mu +- e_nu (mu != nu) with c in Z.
Proof. The linear part 1 - 2 n n^T/|n|^2 must be an integer matrix. Its diagonal entries give 2 n_i^2/|n|^2 in
{0, 1, 2} for every i. If one n_i^2 equals |n|^2, then n = +- e_i. Otherwise every nonzero n_i^2 equals |n|^2/2, so
exactly two entries are nonzero and equal in absolute value; primitivity gives n = +- e_i +- e_j. The off-diagonal
entries are then integers. The translation part 2c n/|n|^2 must be integral: c in (1/2) Z for |n|^2 = 1, c in Z for
|n|^2 = 2. Conversely these maps are signed permutations followed by integer translations. QED
So the light-cone normal (1, 1, 1, 1) and every normal with three or four nonzero entries are excluded, which
confirms row 967's statement. Every lattice mirror of Z^4 is a coordinate mirror (site or link) or one of the twelve
diagonal families (site mirrors only); `am1-port.md` Section 3 lists the same normals ("Allowed normals are e_mu and
e_mu +- e_lambda") without this proof. The positive transfer steps that reflection positivity can give are
therefore e_mu (axis) and e_mu +- e_nu (Lemma D1). A step of one height in a diagonal frame gets no positivity from
reflection (it is a glide times a positive operator, ARGUED in D1). No light-cone step (along (1, 1, 1, 1)) is positive by reflection.

### Step 7 results (GUIDE; run 2026-11-14T15:32Z-15:33Z under the numeric lock)

Run: `guide/lane963/run_guide.sh` -> `sector_sums.py 192 "0.25,1,...,13"`; log `guide/lane963/sector_sums.log`.
Lock acquired 15:32:03Z (holder rotgeom963-opus) and released 15:33:09Z; memory free 72 percent; 66 s; peak RSS
0.80 GB; BLAS threads 1, nice 10. Model and criteria as written above, before the run. Selected rows (b = 24 a):

| x = m a | S (full seed) | S_0 (p = 0) | S_1 (trivial sector) | hand value of 3.4 (ii), corrected |
|---|---|---|---|---|
| 6.5 | 2.6e12 | 7.8e5 | 1.6e4 | - |
| 7.0 | 1.8e8 | 95.3 | 1.99 | S_0 about 106 |
| 7.25 | 5.4e6 | 3.75 | 0.079 | - |
| 7.5 | 3.0e5 | 0.285 | 0.0065 | S_0 about 0.37 |
| 8.0 | 4.0e3 | 7.9e-3 | 5.1e-4 | S_0 = 9.4e-3 |
| 9.0 | 34.2 | 2.85e-4 | 1.29e-4 | S_0 = 3.2e-4 |
| 11.5 | 0.500 | 1.09e-5 | 1.02e-5 | - |
| 12.0 | 0.297 | 6.4e-6 | 6.2e-6 | s(12) = 0.26 |
| 13.0 | 0.113 | 2.30e-6 | 2.26e-6 | e^(-13) = 2.26e-6 |

Thresholds for 0.3 (log-linear interpolation): full seed x_full = 12.0; p = 0 sector x_0 = 7.49; trivial sector of
centre x space group x_1 = 7.15. Quarter turn: log Tr(V_R e^(-H))/log Tr e^(-H) = 0.0097 at x = 0.25 (0.0008 to
0.0013 at x >= 7). Imaginary parts of the projected sums below 6e-15 relative. Ratio S_0/S_1 = 48.0 at x = 6.5,
as the hand reading "S_1 about S_0/48 when S_0 >> 1" says; for x >= 9 both tend to e^(-x), one particle at rest.

Criteria:
- C1 PASS: x_full = 12.0 in [11, 13].
- C2 FAIL, as predicted before the run: x_0 = 7.49, not in [3.5, 5]. The two-particle arithmetic first written in
  3.4 (ii) was wrong; the corrected hand value 7.55 is within 0.06.
- C3 FAIL, as predicted: x_1 = 7.15, not in [1.5, 3]; corrected hand value 7.2.
- C4 PASS: 0.0097 <= 0.02. The quarter-turn twisted torus keeps under 1 percent of the thermal free energy (bulk part
  1/256 = 0.0039, the rest from the axis).

What the run can establish (GUIDE only): in this model the sector seeds are easier as numbers by about 4.5 to 4.9
units of m a at the shape b = 24 a, and the point group adds only 0.34 of that; the corrected hand formulas of
3.4 (ii) are right to about 25 percent. What it cannot establish: anything about SU(2), a consumer for a sector
seed, or any bound. Row 962's figure "m a of about 6" for a zero-momentum seed (A4) is low by about 1.5 in this
model (7.49), for the same reason as my first figure: multi-particle zero-momentum states.

### Final result

RESULT: Row 963 (Claude Opus 5.5 max, Mac mini worker 2; not checked by another model): rotated and diagonal geometry buy NOTHING for the seed over the static axis tori, because the seed number is fixed by the measure and the box size, and every rotated or diagonal object is a signed recombination of the same sector sums, a sector projection with no consumer, or the same thermal sum in a rotated frame. PROVED: a box rotating in time is a twisted torus, Tr((V_R T)^a) = Tr(V_(R^a) T^a), and only the total twist counts (Lemmas R2, R3); twisted traces are Fourier coefficients of the sector seeds, S = sum_rho S_rho (R4); Lemma SPLIT holds for any finite symmetry group with the Kazhdan constant of its generators (R5; SPLIT is the case Z_2^3, and the space group loses about 3 b^2/pi^2); frozen counts 92 (Q_8) and 244 (2T) reproduce the lane's p = 10/23 and 30/61, and the trivial sector keeps 10 and 7 frozen flat vectors; diagonal reflection positivity (CA-III L108556-108560, `am1-port.md` Section 3) checked by hand on the crossing plaquette; on straight tori the diagonal mirror does not separate (4.3); the lattice mirrors of Z^d have normals e_mu and e_mu +- e_nu only (Lemma M, for row 967); adapted diagonal tori are sheared axis tori (D2, half-shift identity Z_diag = Z_even - Z_odd); the infinite-volume axis and diagonal gaps agree within a factor 2 per step (D4, given LG1). CONDITIONAL: the fully diagonal engine (D3, on the diagonal trace formula). ARGUED, with GUIDE support: sector seeds are easier as numbers (free scalar at b = 24 a: m a = 7.15 in the trivial sector and 7.49 at p = 0, against 12.0; my first two-particle figures 2.5 and 4.5 were wrong), but no consumer reads them: the engine needs the full trace and (GAP) needs every momentum; momentum and lattice angular momentum give no energy margin. OPEN: (LSI-J-seed) and (SEED-FP) unchanged; box-shape independence for diagonal tori; a projected engine (row 962 ranked item 3).
