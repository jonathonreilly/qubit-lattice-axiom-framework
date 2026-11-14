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

### Step 1. Repo search and sources (done 2026-11-14T14:25Z)

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

### Step 2. Item (1): rotating boxes are twisted tori; sector decomposition (done 2026-11-14T14:50Z)

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
