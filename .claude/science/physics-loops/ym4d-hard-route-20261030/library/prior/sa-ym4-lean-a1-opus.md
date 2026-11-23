lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-24T10:26Z

# Row 1454: does the Lean renormalisation flow fire trigger R3?

Started 2026-11-23T22:26Z (date -u). Worker: Claude Opus 5.5, high effort, Mac mini worker 2, pinned at commit 67debf644.
Source read (read only, never built or run): Ethan Sussman and Levent Alpoge, public `YM4 Lean` release at commit 3932084a9b82 (`~/ym4d-papers/sa-ym4-lean-full`). All declarations quoted below are theirs; credit to the authors.

## Plan

1. Read FINISH.md rules (efficiency, build on published work), row 1442 (trigger R3), check 1443, row 1451 and its output `library/prior/sa-ym4-lean-trajectory-opus.md`, and Theorem T of row 1332 (`library/gap-shrink-box-fable.md` section 4.4), to pin the exact form of (A0)-(A3) and R3.
2. Read the Lean flow declarations row 1451 used (bare_root_with_window_data, runDomain, NoEscapingLevel, HasLinearDescent, abs_flow_step_le, FlowPassage, IsFirstPassageDatum) and what they rest on.
3. Answer (a)-(d) with file:line quotes.
4. Next two rows.

## Repo search

`grep` of this folder for the declaration names of the row: hits only in FINISH rows 1449-1454, `library/prior/sa-ym4-lean-inputs-opus.md` (row 1449) and `library/prior/sa-ym4-lean-trajectory-opus.md` (row 1451). Trigger R3 is defined in row 1442 (`library/gap-mech-direction3-fable.md`) and sharpened by check 1443 (`library/gap-mech-direction3-check-astra62.md`). The rate-form programme for (UNIV-K) is rows 1391-1406 (`library/gap-univk-*.md`).

## Step 1. The target statements, as on file

**Theorem T** (row 1332, `library/gap-shrink-box-fable.md` L152-176, Claude Fable 5.2; author only). For the account's data g, odd L >= 25, B_sharp, the torus family, phi_* < (L/2) log(13/10):

- (A0) kappa > 0 with g^-2 + B_sharp <= beta <= g^-2 + (K+1) kappa for every first-passage datum (K, beta) at g (L154);
- (A1) C_U > 0, 0 < q < 1 such that for every admissible ell = 2 L^m and every K_0, (UNIV-K) holds on T_ell and T_(L ell) with eps_K <= C_U ell^4 q^K (L155);
- (A2) infrared carry in rate form, seed size N(beta) <= C_1 exp(c (beta - beta_w)) (L156);
- (A3) c < (log L)/kappa + log(1/q)/(4 kappa) (L157);

then (KER)(beta_w; n_w, (2 n_w)^3; log(1 + q_0/5041)) gives (SEED-FP).

**(UNIV-K), exact form** (row 916, `library/gap-chain-ce-opus.md` L293-296, Claude Opus 5.5; check 917). Fix K_0. A predecessor map pi sends each first-passage datum d of cutoff K > K_0 to a datum pi(d) of cutoff K-1. There are eps_K >= 0 with sum_(K > K_0) eps_K finite and one real c_d per d with

  |F_d(T) - F_(pi d)(T) - c_d vol(T)| <= eps_K for T = T_ell and T = T_(L ell),

F_d(T) = log Z_(K,T,beta) (unnormalized Wilson partition function at bare coupling beta, mesh L^-K, physical torus T). The scalar of Theorem T is Phi(d) = L^4 F_d(T_ell) - F_d(T_(L ell)) (L289-290), and Lemma ONE-K gives |Phi(d) - Phi(pi d)| <= (L^4 + 1) eps_K.

So (A1) is a statement about **unnormalized log partition functions** (n = 0 mass), up to one extensive constant per datum, at two adjacent cutoffs, on two fixed physical tori, with error C_U ell^4 q^K. Row 916 L339: the account statement that would supply it is the n = 0 form of (U2) (CA L94364-94381), which the account does not state (scalar vacuum factors CA L94473-94474; large-field histories CA L94505-94512).

**R3** (row 1442; check 1443 sharpening): R3 fires when (A1) is proved in rate form. Check 1443: rate-form (A1) compares adjacent cutoffs of **one** family; it does not identify two bare actions.

**What Lean has to supply for R3.** A statement, for the Lean trajectory or for all first-passage data at g, of the form above: a bound on log Z (or on Phi) differences between cutoffs K and K-1, with a summable rate. A bound on effective couplings x_K alone is not (A1): (A1) needs the full log partition function modulo one volume term.


## Step 2. The Lean flow and its free-energy statements (read 2026-11-23T22:28Z)

Source paths are relative to the release root (`~/ym4d-papers/sa-ym4-lean-full`, git HEAD 3932084a9b82fc79466b4a2faad9ec032b637445). Everything quoted is by Sussman and Alpoge (release written with OpenAI Codex assistance).

**2.1 Lean's flow quantity.** `YangMills/Construction/WindowOfTheParameters/FlowOfTheTotalDensities.lean` L9-27:
- `logRatio D n V = log D(n,V) - log D(n, trivialField n)` (L9-10);
- `HasNextCoupling L D x'`: D positive near the trivial field, and `HasSlopeCoefficient (sideFilter L) (logRatio D) (-x')` (L13-14), `sideFilter L` = sides 2 L^q, q to infinity (L8);
- `flowData p β 0 = (β, wilsonWeight β)`, `flowData p β (t+1) = (nextCoupling ..., kernelImage p x_t D_t)` (L22-26); `coupling p β k = (flowData p β k).1` (L27).
So Lean's x_k is one real number per level: the large-torus slope coefficient of the log of the exactly blocked torus density D_k, read **relative to its value at the trivial field**. The vacuum (field-independent) part of log D_k is divided out by construction. The density itself is carried along (the second component), so x_k is a reading of D_k, not of a truncated action.

**2.2 Lean's first-passage data.** `.../WindowOfTheParameters/FirstPassageOfASequenceForm.lean` L5-12: threshold `g^-2 + B`; `IsFirstPassageIndex B g x K` = `x K ≤ threshold ∧ ∀ k < K, threshold < x k` (L7-8); `passageWindow` adds `threshold ≤ β` (L9-10); `definedPassageWindow` adds the flow-defined predicate (L11-12). `IsFirstPassageDatum ℓ Bs g K β` is membership of β in that window for `TotalDensityFlow.coupling` (`.../TotalDensitiesGiveASystem/TopStatementDefs.lean` L20-21). K is the least crossing index, so **K is a function of β** (for fixed ℓ, Bs, g).

**2.3 Free-energy statements in Lean** (`YangMills/Construction/FreeEnergiesOfTheFlow/`). Notation: `torusPartition p β t n = wilsonPartition β (fineSide p.side t n)` (FreeEnergyDefs.lean L11-12), the unnormalized Wilson partition function at bare β on the fine torus that t block steps map to the block torus of side n; `flowFunctionalAtTrivial p β t n` = the level-t flow functional at the trivial field (L13-14).
- `flowFunctionalIntegral` (MassOfTheFlow.lean L7-12): the level-t flow functional is measurable, positive, bounded, and **its Haar integral on the side-n block torus equals torusPartition p β t n**. (Lean counterpart of SA L17285 as read in row 916: the integral of rho_K is Z exactly.)
- `freeEnergyUpperBound` (FreeEnergyFromAbove.lean L6-12): above the floor, log Z ≤ log D_t(trivial) + (log 2 + 2E) n^4.
- `freeEnergyLowerBound` (FreeEnergyFromBelow.lean L6-11; also `HullTrees.freeEnergyLowerBoundStatement`, HullsInEveryVolume/FreeEnergyBeforeTheFloor.lean L6-13): log D_t(trivial) - (C + 6 log x_t) n^4 ≤ log Z.
- `freeEnergyVolumeScaling` (GrowthOfTheFreeEnergy.lean L6-15): for block sides n ≤ n' with n ≥ nS x_t^(1/100), |log Z(n') - (n'/n)^4 log Z(n)| ≤ C (1 + log x_t) n'^4. `partitionPowerBound` (PowerOfThePartitionFunction.lean L6-14) is the one-sided exponential form.
- These are Props; their proofs are `freeEnergyUpperBound_of_flow`, `freeEnergyLowerBound_of_flow`, `freeEnergyVolumeScaling_of_bounds` (the *Proof.lean files, L13, L22, L14), each from named hypotheses (`flowFunctionalIntegral`, `expansionAlongFlow`, the two bounds).

**Reading.** Every Lean statement on log Z found so far is at **one** bare β and one level t, and its error is of order n^4 (the volume) times (1 + log x_t). None compares log Z at two cutoffs, or at two bare couplings, and none has an error that is small against the volume. For Phi = L^4 F(T_ell) - F(T_(L ell)), `freeEnergyVolumeScaling` gives only |Phi| ≤ C (1 + log x_t) (L ell)^4 in block units, with no smallness. So these are not (A1), and not near it: (A1) asks for an error C_U ell^4 q^K after removing one extensive term, that is, exponentially small in K at fixed ell.

**2.4 (A0) in Lean (ARGUED from the quoted statements; elementary).** `FlowPassage.passes` (TopStatementDefs.lean L32-34): for every β ≥ threshold there is K with `IsFirstPassageDatum ℓ Bs g K β`, (β - g^-2)/Bs - 1 ≤ K and K ≤ 1 + (β - g^-2 - Bs + c₅)/lam. The first inequality is β ≤ g^-2 + (K+1) Bs. By 2.2, K is unique for β. So for every Lean first-passage datum (K, β) at g with FlowPassage at g:

  g^-2 + Bs ≤ β ≤ g^-2 + (K + 1) Bs,

which is (A0) of Theorem T with kappa = Bs **for Lean's flow**. Also λ-side: K ≤ 1 + (β - g^-2 - Bs + c₅)/lam. Which g carry FlowPassage is checked in Step 3 (row 1451 reads it from `bare_root_with_window_data`, clause for all g ∈ (0, γ]).

Status: Step 2 partly done. Next: search Lean for any statement comparing two flows (two bare couplings or two cutoffs): universality, Lipschitz dependence on the initial weight, the tuned branch, the kernel along the coupling.
