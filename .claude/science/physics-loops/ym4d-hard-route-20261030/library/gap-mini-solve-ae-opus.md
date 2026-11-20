lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T22:11Z

# gap-mini-solve-ae-opus: mass gap for 4D SU(2) Yang-Mills (queue row 1255)

Started 2026-11-20T10:11Z (date -u) at commit da81f7368 on branch claude/ym4d-hard-route. Research-stage working state; no status, no public claim.

Labels: PROVED (every step written here or in a cited checked note), ARGUED (argument written, a step not fully closed), GUIDE (heuristic or numeric guide only), OPEN.

## Step 0. Reading and plan

Reading done by 2026-11-20T10:15Z (date -u). Read: GOAL.md in full; FINISH.md L1-90 and L299-356 (rules, joining, efficiency);
queue row 1255 in full; the RESULT lines of rows 1161, 1179, 1180, 1183 and 1200-1256; `parts/gap.md` L1-104;
`library/prior/gap-onebound-read-sol.md` L19-218 (row 1218); the screening tables of rows 1189 (`gap-mini-solve-b-fable.md`
2.1), 1194 (`gap-mini-solve-e-fable.md` 2.1) and 1199 (`gap-mini-solve-i-fable.md` 1.2); the sibling row 1251
(`gap-mini-solve-ad-opus.md`, running, Zeng's package) in full.

**What the record fixes (cited; not re-derived).**
- The gap clause on the tr F^2 sector reads one open lattice estimate beside the account's premises: (N-phys)
  (row 1161 L146-148; row 1179 Theorem BP, check 1183 HOLDS AFTER CORRECTION; row 1225 Theorem E-N, check 1232).
  In the notation of row 1218 L33-44: there are L and j_0 such that for every j >= j_0 some integer u_j with
  3 <= u_j <= n_j/K has s_(+,j)(u_j; n_j^3) = Tr_(H_(+,j)) U_j^(u_j) - 1 <= 1/2, where U_j is the vacuum-normalized
  periodic transfer of the spatial cube of side n_j = L/a_j and H_(+,j) its centre-neutral sector.
- Row 1180: (N-phys) holds iff every fine coupling has a finite one-cube seed nu(beta_j) and limsup a_j nu(beta_j) is
  finite. Row 1233 (check 1242: HOLDS AFTER CORRECTION, conditional) pays the second half from the account's
  two-cutoff comparison, given its representatives. Row 1234 (check 1250 HOLDS): a uniform lattice gap alone does not
  give (N-phys).
- About 45 route families are on file with a first failing step (rows 1189, 1190, 1194, 1199 tables; `parts/gap.md`
  methods 19-36; route registry RA-RG). Every one stops at one of: a one-scale number at order-one coupling (K7,
  Proposition V), a selective non-abelian step with no identity fixing its sign (lead rule W2, row 1243), or the
  neutral conversion (SING) with no association (rows 1115, 1194, 1241).

**Plan (written before the attack).** Step 1 decides the attack by asking which statement, if proved, changes what the
lane does, and checks it against the record by grep. Steps 2 onward do the attack, one stage per response, each
appended here with its label. The last step states what stays open and ends with one RESULT line.

## Step 1. How best to attack it (judgement, ARGUED; written 10:26Z by date -u)

**1.1 What a proof must contain (cited).** Beside the T0 chain, the gap clause reads (N-phys) (Step 0). Row 1180 splits
it into (a) a finite neutral seed at every fine coupling and (b) seed size O(1/a_j). The one-cutoff form (ONE-K)
(row 916, check 917) trades this for a seed at one cutoff plus the ultraviolet carry. Row 1233 Proposition 3.7 pays
the carry from the account's chapter 9 comparison; check 1242 (L52-76) keeps it only after a correction: the exact
decomposition is Phi(d) = P_9(d) + Delta H(d) + D(d), with D(d) = Delta log(S_8(d)/S_9(d)) the relative normalisation of
the chapter 8 and chapter 9 representatives, and row 1233 omitted D.

**1.2 My own screening of the infrared seed, grepped before any work (rule 0a).** Each idea is on file or dies at once.

| Idea | Status |
|---|---|
| Seed from strong spatial mixing (Dobrushin-Shlosman, Martinelli-Olivieri) at one coupling | FALSE as an input: mixing uniform over boxes and boundary data fails at every coupling of the window, because pinned slabs order (Proposition CA-FAIL, `gap-bridge-exercise-opus.md` L337, L463; check `gap-bridge-exercise-check-opus.md` L280) |
| Seed in small physical volume with twisted (twist-eater) boundary data, where the account controls the flow | dies at the massless floor: every scale-invariant spectrum gives the same s(L/K; L) at every L, so K must make the free gluon fail, and then small volumes fail too (method 26, row 988 Lemma FLOOR) |
| Degree-one gauge twists on the boundary of a 4-ball as a continuous stiffness (the instanton analogue of the 2D twist) | dies on the lattice: SU(2)^links is connected, every gauge twist of pinned data is removable (row 1013 Lemma TWIST); only centre twists survive (CEN+, row 1016) |
| Lossy mixing length at one weak coupling, as in OpenAI's 2D Proposition 2.1 | on file as the crux in that form (row 1229); a Jensen step with any bounded flow sees screening in one-loop 4D (row 1244) |
| Lower bound on the deconfinement temperature in physical units | it is (N-phys) (row 1199 table, "Thermal form") |
| Strong-coupling expansion of the Kogut-Susskind Hamiltonian in x = 2/g^4 | a (K-one) number at x about 0.7, far outside any hand-provable radius (rows 1229, 1251 1.2) |
| Migdal-Kadanoff or Tomboulis decimation bounds | route RG, retired (`parts/gap.md` L76-78; rows 797-801) |

Verdict (ARGUED): no engine off the record; the infrared seed at one coupling stays OPEN, as in rows 1219-1251.

**1.3 Choice for this row.** Rule 0 asks what changes. The one-cutoff carry (row 1233 Proposition 3.7 as corrected by
check 1242) is the step that turns a seed at one cutoff into (N-phys) along the trajectory. Its remaining open input
named by check 1242 that no row has attacked (grep at da81f7368: "S_8", "relative normalisation" hit only check 1242) is
D(d). Check 1242 L60-66 says what suffices: S_9 = S_8, or D constant on each predecessor chain, or D(d) - D(d_0) <= sigma
with sigma below the seed margin; and it names the likely mechanism: "If the sole difference can be identified as the
same omitted levels on both tori in the same vacuum family, the wrapping estimates above also bound that subseries."
This row does that identification from the account's text and then bounds D by hand. Moves: (ONE-K)'s carry of the
gap clause. Success: Proposition 3.7 holds with sigma explicit and small on large tori, modulo the account premises
check 1242 lists. Failure: the first account statement that the identification needs, by label and line.

## Step 2. What the account says about the two normalisations (READ; started 10:27Z by date -u)

Source: Sussman and Alpoge's complete account at commit 31a47c543775 (`theorem_0_complete_account_raw_I/II/III.tex`,
fetched into a scratch folder outside the repository; credit Ethan Sussman and Levent Alpoge, with Claude and Codex as
authors of their text; their construction uses Balaban's). Line numbers below are of those files.

**2.1 The chapter 9 mass (READ III:11812-11960, III:18136-18310).**
- Runs (III:11814-11818): A has length n and real centre zeta_*^n + u; B has length n+1 and centre
  zeta_*^(n+1) + n_n(u), with n_n the matching map. The flow stops at depth w = w(g); the last lattice T_w has
  N_w = 2L^(m_0 + w) sites per side; the stop level is k = n - w (III:11824-11831).
- Normalisation (III:11849-11860, eq. 9.1:eq-centre-normalisation-a): Z^c(c^c; v) = e^(E^c(v)) Z~^c(v), where Z^c is
  "the sourced integral of the run c at the stop", E^c(v) = sum_j sum_X [e^(j),c(X; c^c + v) - e^(j),c(X; c^c)] and
  Z~^c(v) = sum_h tau_h^c(v)(V_w). At zero residual source E^c(0) = 0, so Z^c(c^c; 0) = Z~^c(0) (III:11906-11907).
  So the chapter 9 mass at zero source, S_9 in check 1242's notation, is the sourced integral of the run at the stop.
- Remark 9.1:rem-centre-normalisation-b (1) (III:18226-18232, proof III:18286-18302): the vacuum constants that do not
  depend on z sit inside tau_h^c and are counted in the total load; "The normalisation admits exactly one free positive
  constant for each run and each centre."
- Corollary 9.1:cor-sourced-integrals (III:18136-18157): |Z~^B - Z~^A| <= eps*_n A at every source of P_IR and at the
  zero residual source, eps*_n <= C*_TC(N_w; g) e_w, with C*_TC independent of n.

**2.2 The bare constant and exactness (READ; written 10:32Z by date -u).**
- Definition 1.1:def-wilson-action (I:447-490): the bare density is rho_0(U) = exp[-g_0^(-2) A(U)], with no constant;
  dU is the product of normalised Haar measures.
- Setting of the correlation theorem, 5.1:eq-torus-floor-b (II:730-741): rho_0^w := exp[-A(x_0 - w, U) - E], where E is
  "a constant, independent of U and of z, entering the exponent of the bare density additively"; Z(z) := int rho_0^w dU.
- Lemma 4.34:lem-sourced-exactness (I:157268-157290): at every level k where the induction holds,
  int rho_k^w dV_k = int rho_0^w dU, with "E the additive constant of the bare density". The correlation theorem
  5.1:thm-correlation-theorem (iii) (II:2949-2953) states the same identity.
- Lemma 4.36:lem-label-energy (a) (I:159123-159150): the energy constant is E := sum_(j=0)^(K-1) E^(j)(T, T), and a label
  carries E_k[S] := E - sum_(j<k) E^(j)(Omega_(j+1), Lambda_(j+1)) at step k; for the never-large label the remainder at
  an intermediate stop k is sum_(j=k)^(K-1) E^(j)(T, T) (I:159423-159426). Here E^(j)(Omega, Lambda) = N^(j)(Omega, Lambda)
  + E^(j+1)(Lambda, 1) + R^(j+1)(Lambda, 1) (I:159110-159113) are Balaban's one-step numbers (CMP 119 (3.15), (3.33)).
- Chapter 8, 8.22:not-partition-sources-cells (II:140876-140926): Z_m(v) = int exp[-x_0 A(U) + O(v)] dU with no
  normalising constant, and "the normalised partition function of the correlation theorem" is
  Z~_m(v) = e^(-E_m - Ecal_m(v)) Z_m(v), E_m = sum_(j<K) E^(j)_vac(T_m, T_m), "Balaban's normalisation constant of the
  bare density rho_0 = exp[-x_0 A(U) - E_m] on T_m"; with |Z~_m(v)| <= e^(E_+^sharp (2L^m)^4) and
  Z~_m(0) >= e^(-C_low (2L^m)^4).
- The last paragraph of the correlation theorem (II:2971-2978): the frozen whole-lattice objects (b_j, zeta_j, the
  families P, E, P^flat, Q, R, the reference sequence x_j and K) "do not depend on the torus"; for levels K' < k <= K+1
  they are built on auxiliary tori whose side is a power of L.
- Chapter 9 (III:21091-21094): "At the depths r < w only numbers attached to the whole lattice, frozen at the stop, are
  carried, in the form in which the correlation theorem states them."
- Chapter 9 (III:18286-18290): "each Z~^c is the correlation theorem's representation at c^c"; and (III:18249-18250,
  18301-18302) "The normalisation admits exactly one free positive constant for each run and each centre."

**2.3 Consequence of the reading (PROVED from the cited identities; one line).** For any run c on a torus T with bare
inverse coupling x_0^c and additive bare constant E^c, Lemma 4.34 at zero source gives
S_9^c := Z^c(c^c; 0) = int rho_k^c dV_k = e^(-E^c) Z^bare_T(x_0^c), where Z^bare_T(x) = int exp[-x A(U)] dU. Chapter 8 has
S_8(d) = e^(-E_m(d)) Z^bare_T(x_0(d)). So whenever the run c represents the datum d (same torus, same bare coupling),
log(S_8(d)/S_9^c) = E^c - E_m(d): **D is exactly the two-torus defect of the difference of the two additive bare
constants.** The free positive constant of III:18249 is e^(-E^c). Check 1242's counterexample (L58) is this freedom.

**2.4 How chapter 9 itself uses the masses (READ III:53470-53560, Lemma 9.8 on derivative closeness).** Chapter 9's
consumer compares h^c(z) = Z~^c(z)/Z~^c(0) for c = A, B (Step 2 of that proof: h^B - h^A = P/P_0 - Q/Q_0), using the
closeness (c) at z and at the zero source and the bounds (b) 1/P_0 <= B, |Q| <= A. A constant common to the two runs
cancels in h^c, and (c) at the zero source fixes only the relative normalisation of A and B. So within the account the
overall constant is a convention, which is why III:18301-18302 can say one free positive constant remains. This is
where check 1242's D comes from.

## Step 3. Removing D from the one-cutoff carry (written 10:35Z by date -u)

Notation as in check 1242 (L22-24, L52-64): physical tori T_m and T_(m+1), r = L^4, Delta f := r f(T_m) - f(T_(m+1)),
Phi(d) := Delta log Z^bare(d) for a first-passage datum d, Z^bare_T(x) := int exp[-x A(U)] dU (normalised Haar, no
constant). A **representative** of d on T is a chapter 9 run of length K(d) at the bare coupling of d, normalised by an
additive bare constant E9(d; T); its zero-source mass is S_9(d; T). It is **consistent** if the same run and the same
E9(d; T) are used on both chain edges at d (as the B-run of (d, pi d) and as the A-run of the edge into d), as check
1242 L60 requires.

**Lemma D0 (PROVED; from Lemma 4.34 at zero source).** For every representative, log S_9(d; T) = log Z^bare_T(d) - E9(d; T).
Hence Phi(d) = Delta log S_9(d) + Delta E9(d) exactly, and, with chapter 8's S_8 = e^(-E_m) Z^bare,
D(d) = Delta log(S_8(d)/S_9(d)) = Delta(E9(d) - E_m(d)).

Proof. Lemma 4.34 (I:157268-157290; also clause (iii) of 5.1:thm-correlation-theorem, II:2949-2953) at w = 0 gives
int rho_k dV_k = int rho_0 dU = e^(-E9) int exp[-x_0 A(U)] dU at the stop level k, and III:11849-11860 with
E^c(0) = 0 identifies the left side with S_9. Take logarithms and apply Delta. QED

**Corollary D1 (PROVED GIVEN the chapter 9 comparison for consistent representatives).** Let d -> pi d -> ... -> d_0 be
a chain satisfying (EDGE) (check 1242 L68), with consistent representatives on both tori, and suppose the zero-source
comparison of 9.1:cor-sourced-integrals holds on each edge with these representatives, so that Lemma 3.5 of row 1233
(HOLDS in check 1242 L28-32) gives |Delta log S_9^B - Delta log S_9^A| <= b_n on the edge of shorter length n. Then

    Phi(d) <= Phi(d_0) + sum_(n=K_0)^(K-1) b_n + Delta E9(d) - Delta E9(d_0)
           <= Phi(d_0) + sum_(n>=K_0) b_n + 2 sup_(d') |Delta E9(d')|.

Proof. By Lemma D0 on each edge, Phi(d) - Phi(pi d) = [Delta log S_9(d) - Delta log S_9(pi d)] + [Delta E9(d) - Delta E9(pi d)].
Consistency makes S_9(pi d) the same number on the edge (d, pi d) and on the edge (pi d, pi^2 d), and likewise for E9, so
the second brackets telescope. The first bracket is at most b on each edge. Sum over the chain. QED

So check 1242's pair (S_8, D) is not needed: the one-cutoff telescope needs only **(V9)**, a uniform bound
sup_d |Delta E9(d)| <= eta_9 on the two-torus defect of the representatives' own bare constants, with
eta_9 <= (phi_* - Phi(d_0) - sum b_n)/2 at the base. Check 1242's form is the case E9 = E_m + c_T.

**Proposition D2 (PROVED GIVEN Lemma 3.6 of row 1233, which HOLDS in check 1242 L34-46 for its stipulated families).**
(a) If E9(d; T) - E_m(d; T) = c_T depends on the torus only, then D(d) = r c_(T_m) - c_(T_(m+1)) is the same number for
every datum, so D(d) - D(d_0) = 0 on every chain: check 1242's sigma is 0.
(b) If E9 = E_m, the energy constant of Lemma 4.36(a) of the run (I:159130-159135) that 8.22 calls Balaban's
normalisation constant of the bare density (II:140916-140922), then D = 0, (V9) is the bound on Delta H, and
eta_9 <= eta_vac(m) + eta_det(m), which tends to 0 faster than every power of L^(-m) (row 1233 Lemma 3.6 sharpened;
check 1242 L34-46).
Proof. (a) Lemma D0. (b) Lemma D0 and Lemma 3.6. QED

**Reading (R): the 9.1 representatives carry the energy constant of their own run (ARGUED; not proved).**
For: II:140916-140922 calls e^(-E_m - Ecal_m) Z_m "the normalised partition function of the correlation theorem";
III:18286-18290 says each chapter 9 Z~^c "is the correlation theorem's representation at c^c"; III:21091-21094 says the
levels below the stop carry "numbers attached to the whole lattice, frozen at the stop, in the form in which the
correlation theorem states them", which is how the never-large label's remainder sum_(j>=k) E^(j)(T, T) of Lemma 4.36
appears (I:159423-159426); III:11973-11975 and III:18295-18296 file the run's vacuum constants as stored slots of the run,
compared slot by slot between A and B. Against: II:730-741 leaves E free in the correlation theorem's setting, and
III:18249-18250, 18301-18302 state that one free positive constant remains per run and centre. No line I read states
(R) for the 9.1 comparison in so many words. Under (R), D = 0 and the corrected Proposition 3.7 holds with sigma = 0.
Without (R), Corollary D1 still holds for whatever normalisation 9.1 is proved for, and the open item is (V9) for that
normalisation; by Proposition D2(a), any choice that differs from E_m by a torus-only constant is enough.

**What this changes (ARGUED).** Check 1242's open item "identifying the chapter 9 representatives with the physical
normalisation (or bounding their relative two-torus defect along the chain)" becomes the reading (R), a question about
the account's text, plus Lemma 3.6, which HOLDS. The other open inputs of the one-cutoff carry are unchanged (check
1242 L72-76): the 9.1 hypotheses (a)-(e), with (e) the outstanding Proposition 9.1:prop-blind-site-expansions;
(EDGE) on every predecessor edge; 8.22's standing hypotheses and torus independence; (DET)'s (S1)-(S3); the infrared
seed at every base datum. The seed stays OPEN.
