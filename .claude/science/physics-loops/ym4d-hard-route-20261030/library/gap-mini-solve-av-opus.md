lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:47Z

# gap-mini-solve-av-opus: mass gap for four-dimensional SU(2) Yang-Mills

Queue row 1296 of `FINISH.md`, pinned at commit 88cfc357c on branch `claude/ym4d-hard-route`.
Started 2026-11-20T15:47Z (date -u).

Labels: PROVED (written argument checkable by hand), ARGUED (argument with a named gap), GUIDE (heuristic or numeric, never a proof step), OPEN.

## Step 0: record read (2026-11-20T16:05Z by date -u)

Read: `GOAL.md` in full; `FINISH.md` L1-84, L299-349 and row 1296 (this item); the RESULT lines of rows 1244-1293
(the Opus mini-solve series aa-as); rows 1284-1295 (in-flight items); `parts/gap.md` L1-104 and L223-330 (state,
route registry, test table, exact price); `library/prior/gap-onebound-read-sol.md` L1-260 (row 1218);
`library/gap-mini-solve-aq-opus.md` Steps 0-1 (row 1284, in flight).

What the record fixes (statements about the record, not evidence; each is cited there):

1. Modulo the ultraviolet carry, the gap reads one lattice input, (N-phys) of row 1161: at one physical side L,
   uniformly in the cutoff, the periodic centre-neutral excited trace of the spatial cube at one time
   u <= n/K (K = 512) is at most 1/2. Equivalent forms on file: (W), (PHYS-SEED), (SEED) at one coupling of the
   window 2.3-2.6 with a carry, (SL) of row 1258.
2. Row 1218's published sources (credited to their authors there): A (Bhattacharjee, Bhattacharya, Lockwood,
   Romanov, Sessford, Singha Roy) proves the ascent from a thermal window bound (A-B*) to a gap, conditional on
   that seed and on (W); B (Bhattacharjee, Bhattacharya, Lockwood, Romanov) Corollary 166 proves BP(n, 1/2) for the
   straight-path block law at b = 2^k, beta_W <= k+2, torus side R <= exp(2^k/(17k)); B's own Remark 155 and row
   1219 call it non-selective. Zeng's routes are conditional.
3. Route registry (row 998): no route near closure; RA, RB, RC, RF blocked-equivalent; RE blocked-local; RG retired;
   RD (dichotomy) survives only as a weaker statement. Theorem-grade tests for any tool: compact U(1), the free
   photon, the product with a massless factor, Theorem D2 (supremum over tilts false), Lemma SHEET (uniform over
   coupling fields false), Proposition CA-FAIL (pinned-slice classes contain ordered members).
4. In-flight at this pin: aq (row 1284: (U-dom), H2' connectedness), as (row 1293, done: (PE)), at (row 1294, just
   started), au (row 1295, queued), owner tiling rows 1285-1287, Codex rows 1288, 1290.

## Step 1: how best to attack it (written 2026-11-20T16:35Z by date -u; judgement, ARGUED)

**The crux.** Modulo the ultraviolet carry, the Jaffe-Witten gap reads one lattice input, (N-phys), equivalently a
seed at one coupling in the window (a uniform cube gap plus the count (TR) of row 1259). Every proof of it must
contain a selective step at order-one coupling: a step that fails for compact U(1), the free photon, products with a
massless factor and frozen finite groups (parts/gap.md test table), and that is not a supremum over pins, tilts or
coupling fields (Theorem D2, Lemma SHEET, Proposition CA-FAIL).

**Screen (rule 0a).** Before reading the tables I re-derived the routes below; each has a match on file with its
first failing step, so none is attacked here.

| Route I re-derived | Match on file | First failing step there |
|---|---|---|
| Sharpness of the transition (OSSS, Aizenman-Barsky-Fernandez) | rows on FKG-NO, HF (row 1084) | no monotone (FKG) structure for SU(2) Wilson |
| Bourgain-Gamburd / Lubotzky-Phillips-Sarnak spectral gap of Hecke operators on SU(2) | `gap-brainstorm-max.md` item 12, `gap-brainstorm2-max.md` item 13; commutator line rows 778-795 | the commutator contraction and density flattening hold for the binary icosahedral group too (row 789 binding test); transport test (TR-F) open |
| Orbit-space curvature (Singer, Feynman), Bakry-Emery, Witten Laplacian | rows 1229, 1237 (Proposition UNI), 1251 (Zeng) | a coupling-uniform curvature makes the limit trivial; (TUN) is the gap |
| Small-volume valley confinement (Simon's x^2 y^2, Luscher's zero modes) and tilings | rows 1273, 1279, 1285-1287 | tiling carries free energies, not gaps; L m = kappa g^(2/3) is small at weak coupling |
| Migdal-Kadanoff decimation inequalities (Tomboulis 2007) | rows 799, 800, 1025, 1029 | one open inequality (TB)_n; gives the flux half only (Lemma FAC), off the path of (W) |
| Semiclassical confinement on R^3 x S^1 (Unsal and others), Polyakov mechanism, Gopfert-Mack | rows 1237, `gap-afield-*`, `gap-global-reform-max.md` | different theory; adiabatic continuity not a theorem |
| Spin-network / electric basis with 6j recoupling | rows 1076, 1081, `gap-descent-sign*.md` | recalled coefficient formula, GUIDE only; no sign at order one |
| Third law (no residual entropy) from a uniform gap, i.e. "uniform gap implies (TR)" | row 1259 Step 2 point 4, row 1291 | OPEN with no counterexample; needs a light-state count that no blind tool gives |
| 2D O(N) pinned-cell engine ported to 4D | rows 1007-1016, 1228, 1229 | fails in the class of all pins (B, B'), and at a trivially pinned plate (P5) |

Verdict (ARGUED): no route to the seed off the record, in agreement with rows 998, 1219, 1278, 1284. A further
screen is waste by row 998 9.5.

**What I work instead.** The rule "only closures count" points to an unowned open input whose closure is decidable
with sources on hand. Check 1288 (gpt-6.2-astra, `gap-uv-batch7-check-astra.md` Section 7) lists what the one-cutoff
carry still needs: (1) the seed and count; (2) the Section 9.1 inputs, including the blind-site expansion (needs
Balaban CMP 116, paywalled: stop by FINISH Rules); (3) a consistent physical normalization and its two-torus price
(reading N2 of row 1275 FAILS there); (4) the across-frame comparison (rows 1278, 1280, 1284 hold its parts); (5)
scope. Item 3 needs no CMP 116 and, by grep of FINISH.md and `library/open-core.md` for "physical normalization",
"N2", "V9" and "normalisation identity", is held by no row at this pin (hits: rows 1275, 1288 and row 1291's RESULT,
which names it as missing and does not take it).

Moves: the one-cutoff carry's item 3 (check 1288 7.3). Success: (V9) holds on its strong reading, so the physical
two-torus price is bounded by summable edge terms, and the carry's list loses item 3. Failure: the exact place where
the account's Section 9.1 representatives cannot be the physical bare constants, which then is a correction to the
carry route. It does not touch the seed; nobody should count it as progress on the crux.

**Plan.** Step 2: read the account's normalization passages that check 1288 cites (CA-II L140873-140926,
CA-III L11832-12058, L17396-17447, L18136-18302) and rows 1255, 1275 (Proposition V9). Step 3: prove the identity
that attaches Section 9.1's arrays to the physical bare densities, or find where it fails. Step 4: labels, RESULT.
If row 1294 or 1295 claims the same item first, I switch to the check of A's thermal ascent (Theorem F).

Duplicate check at 16:45Z: rows 1294 (`gap-mini-solve-at-opus.md`, Step 0 only) and 1295 (no file) name no item yet.

## Step 2: what the account fixes about the chapter-9 normalisation (READ; written 2026-11-20T17:20Z by date -u)

Source: Sussman and Alpoge's complete account at 31a47c543775 (CA-I, CA-II, CA-III; with Claude and Codex as
authors of its text; after Balaban), fetched by raw URL into a scratch folder outside the repository. Line numbers
are grep anchors in those files. Statements R1-R9 are quotations or close paraphrases, not evidence of correctness.

- **R1 (free bare constant, conservation).** rho_0^w = exp[-A(x_0 - w, U) - E] with "E a constant, independent of
  U and of z, entering the exponent of the bare density additively" (II:730-741); int rho_k^w dV_k = int rho_0^w dU
  at every level (5.1:eq-correlation-theorem-c, II:2933-2935).
- **R2 (tuned family).** (J1): the step data "do not depend on the torus" (III:1309-1318). (J4): "the sourced
  integral factors as Z = e^Ecal Z~ ... |Z~| <= A, Z~(0) >= 1/B", A, B "the constants of the setting of clause (v)"
  (III:1343-1366).
- **R3 (the pair at the stop).** Run A has length n, run B length n+1; "The flow stops at the depth w = w(g)"; the
  last lattice has N_w = 2L^(m_0 + w) sites per side; k := n - w is the stop level; Z~^c(v) = sum_h tau_h^c(v)(V_w),
  tau_h^c = chi T^w e^(A^w - Ecal^c), "A^w the effective action at the stop" (9.1:not-centre-normalisation,
  III:11804-11880).
- **R4.** "the label h carries, besides the constant of Balaban's construction, the term ..." (III:11905-11909);
  "There is one normalisation per run and centre: nothing that depends on h or on the source is rescaled"
  (III:11923-11924).
- **R5 (stored units).** tau_h^c = P_h[x^c], "one assembly formula P_h, carrying no run index"; the entries of x^c
  are uses (j, k', .) of stored units at levels k' in [j, k], and include "the pieces that do not depend on z but
  depend on the run, namely the vacuum constants" (III:11961-11977; again III:59795-59803).
- **R6 (loads).** The loads (9.1:eq-centre-normalisation-d, III:12045-12058) are S^+_i[E], S^+_i[R], the boundary
  loads y_j, y'_j, and g_j [z#_j + sum L^(-(j-i)/2) b_i] with z_i, b_i the suprema of the zeta- and b-differences
  (III:12009-12015); every index i is at most the stop level k.
- **R7.** "The normalisation admits exactly one free positive constant for each run and each centre"
  (9.1 Remark, III:18249-18250; again III:18301-18302); "The vacuum constants that do not depend on z occupy slots of
  the entries z" (III:18295-18296).
- **R8 (Theorem 4.36:thm-never-large-exponent, I:159272-159470, under its (h1), (h2), (h4)).** With the energy
  constant E := sum_(j<K) E^(j)(T, T) (4.36:eq-label-energy-a, I:159155-159160), where
  E^(j)(T, T) = N^(j)(T, T) + E^(j+1)(T, 1) + R^(j+1)(T, 1) and N^(j) is the one-step normalisation number built from
  log g_j, log z_j and SU(N) constants times cell counts (I:159370-159390): the never-large label's energy at
  level k is Efrak_k = E_k[empty] = sum_(j=k)^(K-1) E^(j)(T, T) = -l_k + r_k, |r_k| <= C_r |T|_k, and
  (1/2)(d-1)D (1 - L^(-d)) log x_k |T|_k <= l_k <= (1/2)(d-1)D (log x_k + Bbar gamma^2/(L^d - 1)) |T|_k
  (4.36:eq-never-large-exponent-b).
- **R9 (Lemma 8.22:lem-vacuum-energy-density, II:141276-141520).** Under (a) the itemisation of Balaban's constant
  "less the Gaussian normalisers" into three parts (normalisation numbers times lattice counts; sums of E-terms at
  U = 1; sums of R-terms at U = 1), (b) Balaban's format at zero source with constants E_0, K_*, kappa, and (c)
  torus-independent running constants and matching of non-wrapping terms under lifts, the density difference of
  two tori is at most delta_vac-bar. The proof is level by level: the first part is exactly extensive; the second
  and third parts differ by at most 2(E_0 + 1) K_* e^(-(kappa/2) D_j) per site of level j+1, with D_j one quarter
  of the smaller torus's side in units of M L^(j+1-K), less two. The Gaussian normalisers, one torus-wide number per
  level, are excluded and "compared by the determinant lemma" (II:141420-141428).

**Reading (ARGUED; about the text, with the lines above).** The stored source-free pieces (R5) are the run's own
constants of the levels it performs (j <= k), and no load of R6 bounds a number built from levels beyond the stop.
If a run's bare constant is Balaban's full constant through first passage, E = sum_(j<K) E^(j), as in 8.22 and R8,
then at the stop the run carries the leftover Efrak_k of R8, a global number built from the levels k <= j < K that
the stopped run does not perform. The two-run difference Efrak_k^B - Efrak_k^A has the a priori size
(1/2)(d-1)D sum_(j=k)^(K-1) (L^d - 1)|T|_(j+1) |log x_j^B - log x_j^A| + |r_k^B - r_k^A|, and nothing in R6 bounds it.
So the printed proof of 9.1:thm-last-lattice-comparison is complete for normalisations whose leftover constants
agree across the pair, for instance both zero, and needs one more input otherwise. This names the term behind row
1275 3.2 (b) and Proposition N1. It also places check 1288's counterexample to reading N2 (scalars 1 and
(1+d)^(-1) chosen before assembly): those scalars are leftovers whose difference log(1+d) is exactly such an
unloaded mark.

## Step 3: a consistent physical normalisation at the stop (written 2026-11-20T17:30Z by date -u)

**Setting.** The pin route of the one-cutoff carry (row 1233 Proposition 3.7 as corrected by checks 1242, 1263,
1266 and 1288; rows 1255, 1256, 1275). Two tori T_s, T_b with side ratio L, r := L^4, Delta f := r f(T_s) - f(T_b).
For a pin datum d and a torus T, run(d; T) is the chapter-9 run at the exact pin (centre 0, zero residual source).
It has length n(d), stop level k = n(d) - w, and its last lattice has N := N_w(T_s) sites per side on T_s and LN on
T_b (same stop depth, same spacing). E^(j) below is R8's itemisation N^(j) + E^(j+1) + R^(j+1) at U = 1. In the split
convention of R9 a step carries in addition a torus-wide Gaussian normaliser G^(j); it is then included once.

**Definition PN (the partial normalisation).** For c = run(d; T) put E^c_(<k) := sum_(j<k) E^(j)(T) (plus
sum_(j<k) G^(j)(T) in the split convention), give the run the bare density rho_0 = exp[-x_0 A(U) - E^c_(<k)], and put
S_9(d; T) := Z~^c(0) = sum_h tau_h^c(0)(V_w) and E_9(d; T) := E^c_(<k).

**Lemma CONS (the representative is attached to the bare density; PROVED from R1 and R3).**
S_9(d; T) = e^(-E_9(d; T)) Z_bare(d; T), where Z_bare = int exp[-x_0 A(U)] dU has no constant.
*Proof.* Ecal^c(0) = 0 (R3), so Z~^c(0) = Z^c(c; 0) = int rho_k dV_k = int rho_0 dU (R1). QED.
So E_9 is one number per datum and torus. At an exact pin the run is the same object on the two edges
(d, pi d) and (pi d, pi^2 d) that contain it (row 1256 Proposition PIN; row 1275 3.4 (i)), so S_9(pi d; T) is one
number on both edges. With leftover zero for every run, no run-dependent global constant enters the terms.

**Lemma TB' (torus bound in the partial normalisation; PROVED GIVEN (J4) in Balaban's full normalisation and R8 for
the run).** Let Z~^full be the run's representation with bare constant E = sum_(j<K) E^(j) and bounds A, B (R2), and
Z~^part the one of Definition PN. Then Z~^part = e^(Efrak_k) Z~^full, hence
    |Z~^part(v)| <= A' := A e^(C_r |T|_k),    Z~^part(0) >= 1/B',
    B' := B exp[ ((1/2)(d-1)D (log x_k + Bbar gamma^2/(L^d - 1)) + C_r) |T|_k ],
with |T|_k = N^4 on T_s and (LN)^4 on T_b.
*Proof.* E_full - E_part = sum_(j=k)^(K-1) E^(j) = Efrak_k. The constant enters additively in the exponent of
rho_0 (R1), and the steps act linearly on the density, so the two expansions differ by the factor e^(Efrak_k)
term by term. By R8, Efrak_k = -l_k + r_k with l_k >= 0 and |r_k| <= C_r |T|_k; use the upper bound on l_k for B'.
QED. (In the split convention one more factor, exp(sum_(j>=k) G^(j)), enters, and a bound of the same form on it
is GIVEN.) A', B' depend on g (through x_k) and N only.

**Lemma PV (two-torus defect of the partial constant; PROVED GIVEN hypotheses (a)-(c) of
8.22:lem-vacuum-energy-density read at the levels j < k of run(d; T_s) and run(d; T_b)).** Let N >= 2 L^11 M (the
torus floor of R9 at the stop). Then, uniformly in the datum d (that is, in the cutoff),
    |Delta E^(<k)_vac| <= eta_vac(N) := (LN)^4 * 2(E_0 + 1) K_* * sum_(u>=0) L^(4u) exp[-(kappa/2)(N L^u/(4M) - 2)],
where E^(<k)_vac is E_(<k) without the torus-wide Gaussian normalisers (all of E_(<k) in R8's convention).
*Proof.* Level j+1 (j < k) has N L^(k-j-1) sites per side on T_s and LN L^(k-j-1) on T_b, so
nu_(j+1)(T) = nu_k(T) L^(4(k-j-1)) and nu_k(T_b) = r nu_k(T_s). Run the proof of R9 with K replaced by k and the
smaller side 2L^min(m,m') replaced by N: the first part is exactly extensive (the counts are proportional, and the
numbers built from log g_j, log z_j are the same on both tori by (J1) and (c)); the second and third parts differ by
at most 2(E_0 + 1) K_* e^(-(kappa/2) D_j) per site of level j+1, with D_j := N L^(k-j-1)/(4M) - 2 by the wrapping
threshold of (c). Per site of level k this gives |E(T_s)/nu_k(T_s) - E(T_b)/nu_k(T_b)| <= sum_(u=0)^(k-1) L^(4u)
2(E_0+1)K_* e^(-(kappa/2)(N L^u/(4M) - 2)) with u = k-1-j. Finally Delta E = nu_k(T_b) [E(T_s)/nu_k(T_s) -
E(T_b)/nu_k(T_b)] because r = nu_k(T_b)/nu_k(T_s). QED.
The series converges and does not depend on k, n or g_0. Since N/(4M) >= L^11/2, the u = 0 term is at most
(LN)^4 2(E_0+1)K_* e^(kappa) e^(-kappa N/(8M)), and (LN)^4 e^(-kappa N/(8M)) decreases in N once N >= 32M/kappa;
so eta_vac(N) -> 0 as N grows and is at its largest at the torus floor.

**Proposition PN (check 1288, item 3; PROVED GIVEN Lemmas CONS, TB', PV, the determinant lemma (DET) for the
torus-wide Gaussian normalisers of the steps j < k in the split convention, 9.1:thm-last-lattice-comparison with its
hypotheses (a)-(e) read in the partial normalisation with A', B', and the Reading of Step 2).** Along the pin chain
d_0, pi d_0, pi^2 d_0, ... with E_9 and S_9 of Definition PN:
- (i) consistency: one representative per datum and torus, the same on both edges that contain it (CONS);
- (ii) edge bound: |Delta log S_9(d) - Delta log S_9(pi d)| <= b'_n := eps*_n (r A'_s B'_s + A'_b B'_b), with n the
  shorter length of the edge (9.1:cor-sourced-integrals at the zero source, |log x - log y| <= |x - y|/min(x, y), and
  the floor S_9 >= 1/B' of TB'; this is row 1275 3.4 (ii) with A', B');
- (iii) |Delta E_9(d)| <= eta_9 := eta_vac(N) + eta_det(k) for every d, eta_det(k) := 0 in R8's convention;
- (iv) with Phi(d) := Delta log Z_bare(d) = Delta log S_9(d) + Delta E_9(d) (CONS),
  Phi(d) <= Phi(d_0) + sum_(n >= n(d_0)) b'_n + 2 eta_9.
*Proof.* (i) CONS. (ii) as stated. (iii) PV, plus (DET) for the split part. (iv) telescope the edge bounds of (ii)
from d_0 to d and add (iii) at both ends; this is row 1255's Corollary D1 with E_9 in place of E_m. QED.

**What this changes.** Check 1288 item 3 asked to "Fix E_9(d;T) once per datum, centre and torus, and establish the
edge comparisons for those choices. Supply a bound on Delta E_9(d) - Delta E_9(d_0) within the seed margin."
Definition PN fixes E_9; CONS attaches the representative to the bare density by conservation alone, so check 1288's
counterexample to N2 cannot occur (its leftovers differ); PV bounds the defect by 2 eta_9, uniformly in the cutoff.
No identification with chapter 8's full constant E_m is needed, and D := Delta(E_9 - E_m) is never used. The
Gaussian is included once (Definition PN). What stays as input: (DET) in the split convention; hypotheses (a)-(c) of
8.22 at the levels below the stop; 9.1's hypotheses, including the account's outstanding blind-site expansion
(part (e)); and the Reading (ARGUED). If the Reading is wrong and the printed 9.1 proof uses another bare constant,
the needed extra input is the bound on |Efrak_k^B - Efrak_k^A| displayed in Step 2, a statement about the couplings
x_j between the stop and first passage.

**A correction to the account's text (for the lead; not posted).** 9.1 Remark item (1), "The normalisation admits
exactly one free positive constant for each run and each centre" (III:18249-18250), is true of the three
normalisation conditions, as its proof says (III:18299-18302). Theorem 9.1's comparison, however, holds for at most
one relative normalisation of the pair, up to the factor 1 +- 2 eps* A B (row 1275 Proposition N1), and its printed
proof covers normalisations with equal leftovers (Step 2). The partial normalisation of Definition PN is one such
choice, and in it the zero-source comparison compares e^(-E_(<k)) Z_bare of the two runs.

**Margin note (ARGUED).** A' B' grows like exp[C (1 + log g^(-2)) (LN)^4], so (iv) is useful only once the base pin
is deep enough that the tail sum_(n >= n(d_0)) eps*_n A'B' is small; eps*_n decays like rho^(n-w) + Pi_n (row 1233
Lemma 3.5). This depth condition is the carry's existing base-placement condition (check 1288 Section 7 item 2); it
is not new.
