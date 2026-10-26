# Record birth cost of an explicit site-local instrument, apparatus ledger, and a pointer-information criterion

Task `J:derive:review-20260929-record-birth-cost-and-observability:a1`. Same-family (Claude Sonnet 5.5), unrefereed.
Checker: `check.py` in this directory (`TOTAL: PASS=57 FAIL=0`, about 20 s).

## Plain-language summary

The source note prices a "record" as a sharp lock of one lattice site in the walker's sea and finds about 1.19 or 2.39
hop energies. I took the actual instrument apart. In the sea's half-filled state, I can write the energy cost of *any*
instrument acting on one site in one formula. That gives three things.

1. Among all sharp, parity-respecting, non-trivial one-site instruments, 1.19 is the exact minimum (a lock of one coin mode
   or any other binary yes/no question about the site). The complete rank-one lock of the site costs exactly twice that.
2. 1.19 is not the minimum over record laws. Weak (partial) instruments cost any amount from 0 up. A reliable copy of
   one bit still costs nearly the full 1.19, and the weak-limit price per bit is `ln 2` times 1.19, about 0.83.
3. Counting the apparatus: with a pointer qubit coupled impulsively the work is exactly
   `1.19 (1 - cos th) + (pointer gap) x (1/2) sin^2 th`. A finite-time coupling pays a little less, and also reads out less.

The "monotone count is impossible" result is a statement about a fixed Hamiltonian. An explicit open (Lindblad) law has an exactly
non-decreasing record count. Heat budgets bound a rate only under stated assumptions, and a cosmological density needs
dilution accounting.

## Reading performed

- Axioms: `docs/MINIMAL_AXIOMS_2026-06-29.md` (read in full, current main `3e1a2dd253`). Lines 33-83 are the four axioms
  (Record: lines 75-83). Lines 85-95 and 108-112: no dynamics, formation rate, Hamiltonian or measurement rule is supplied;
  lines 173-190 list the formation rules as open.
- Primitives: `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` lines 21-130: `scale_reference_primitive`,
  `kinetic_isotropy_primitive`, `realized_state_primitive`. None supplies a Hamiltonian, instrument, noise model or cosmology.
  I use none of them as a premise; `t = hbar c / a` below is a units reading of the walker cone.
- Source branch `claude/toe-viability-probes-20260927` at `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`: all 28 named objects exist
  and their sha256 equal the values in `SOURCE_MAP.json` (list in `RECOVERY_STATUS.json`, all `verified: true`).
  Read in full: the record-cost note (T1-T7: lines 88-336 of the git blob), the count note (T1-T3, N1-N8), the viability map
  (record-cost items, lines 79, 150-185, 590-720, 825-885).
- The record-cost note is not on current main (`git ls-tree` of `docs` finds no such file). The related landed notes I found are
  `docs/NATIVE_INFORMATIVE_EDGE_RECORD_AND_DISTURBANCE_BOUNDED_THEOREM_NOTE_2026-09-13.md` (a binary effect, its information and
  disturbance, in a different carrier: the native edge/CAR carrier; Section 5, line 251) and
  `docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md` (pointer conservation
  with a controlled copy, qubit toy). I found no landed note on the walker sea instrument cost.
- Earlier attempts read: `probes/work/derive/deferred-20260926-quantum-record-codes-and-pointers/` (a different "pointer": positivity
  of a depolarised classical pointer generator, not this obligation) and `a-formation-price-from-local-data/` (kept-ledger price
  of a record in a box, a different object). No active attempt on this obligation found. No open PR search succeeded beyond local grep.
- Known review corrections (SOURCE_MAP `known_review_boundaries`, RECORD_COST entries) are background: no "site occupation is the
  most expensive question" claim (I use the corrected one-mode rule), the 96 percent is a finite fixed-lock number, and the
  physical mass/readout conversion is not claimed.

## What is supplied, and what is proved here

Supplied (ASSUMED, none adopted by the axioms): (P1) the sites carry a quantum state and a record is formed by an instrument
(Kraus operators `K_y` on the site); (P2) the walker comparator `H = sum_ij h_ij c_i^+ c_j`, number conserving, hop `t = 1`,
half-filled Slater ground state, with no zero modes; (P3) the comparator's site is the two-mode Fock space (4 dimensional), not
the axiom's `M_2(C)`; (P4) fermion superselection: instruments are *even*, i.e. every Kraus operator commutes with the site's
fermion parity; (P5) the sea is "inversion paired" (antiperiodic torus with even side, or the infinite lattice), so the site
block of `<c^+ c>` is `1/2` times the identity. The axioms do not entail P1-P5.

`lam := <|s(k)|>_BZ` (`|h|` at one site). `lam = 1` exactly on the two-site antiperiodic ring, `1/sqrt 2` on the 4-ring, `1.194945`
on the `8^3` torus, `1.1938` in the infinite lattice (the note's `2.387602/2`).

## Steps

**S1 (ASSUMED).** P1-P5 above. T1 of the source (for a finite system, `Delta E = Tr rho (Phi*(h_x) - h_x)`) is used as given;
it is old and re-derived in one line by S5.

**S2 (CHECKED, exact).** The exact model: antiperiodic two-site ring, 4 modes, 16 dimensional Fock space, sympy arithmetic. Its
spectrum lies in `{-2,..,2}`, the level `-2` is nondegenerate, `E0 = -2 = -N lam`, the site block of `<c^+ c>` is `I/2`,
all `<c c>` vanish, and `sum_m h_am <c_b^+ c_m> = -(lam/2) delta_ab` (check A1-A6).

**S3 (PROVED). Lemma (K).** Under P2 with no on-site term `h_ab = 0` (a,b in the site `x`) and `(P_-)_xx = I/2`, `(|h|)_xx = lam I`:
`sum_m h_am <c_b^+ c_m> = (h P_-)_ab = ((h - |h|)/2)_ab = -(lam/2) delta_ab`, because `P_- = (1 - sgn h)/2`
and `<c_i^+ c_j> = (P_-)_ji`. (Verified exactly in S2 and numerically on `8^3`, check F2.)

**S4 (PROVED). Lemma (Wick).** Write the four site Majorana operators `gamma_k` and let `X` be any operator odd under the
site parity. Then `X = X^(1) + X^(3)` with `X^(1)` in the span of the `gamma_k` and `X^(3)` in the span of the products of three
distinct `gamma`'s (these 8 operators are Hilbert-Schmidt orthogonal and span all odd operators of the two-mode algebra). In the
state of P2/P5 all two-point functions among site Majoranas equal `delta_ij` (no antisymmetric part: `<c^+ c> = I/2`,
`<c c> = 0`). So for any linear `B = sum_m b_m c_m` of outside modes, Wick gives `<X^(3) B> = 0`: each term contracts two
distinct site Majoranas, which vanishes. Therefore `<X B> = <X^(1) B>`. This is where P5 matters: for odd side with generic
twist the site block is not `I/2` (the source's `L = 3` sol counterexample) and S4 fails.

**S5 (PROVED). Result 1: the cost of any even one-site instrument.** Let `Phi*(X) = sum_y K_y^+ X K_y` with every `K_y` even and
`sum K_y^+ K_y = 1`. Define the `2 x 2` matrix `A_ab = Tr[c_b Phi*(c_a^+)]/2` (trace over the 4-dim site Fock space). Then the mean
energy change of forming the record is
`Delta E = lam (2 - Re Tr A)`.
Proof. By locality only terms touching `x` change: `H_x = sum_a (c_a^+ B_a + h.c.)`, `B_a = sum_{m not in x} h_am c_m`. Even Kraus
operators commute with `c_m`, so `Delta E = sum_a 2 Re <(Phi*(c_a^+) - c_a^+) B_a>`. By S4 keep only the Majorana-linear part of
`Phi*(c_a^+)`, which is `sum_b A_ab c_b^+ + A'_ab c_b`. `<c_b B_a> = 0` (no anomalous correlator), and `<c_b^+ B_a> = -(lam/2) delta_ab`
by S3. Hence `Delta E = sum_a 2 Re[(A_aa - 1)(-lam/2)] = lam sum_a (1 - Re A_aa)`. Q.E.D.
CHECKED: exact rational (Q(i)) agreement for 10 instruments on the 2-ring (B1-B9); agreement to `1e-14` on full Fock-space exact
diagonalisation of the 4-ring and 6-ring for 16 random even Kraus instruments (E4.2, E6.2); agreement to `9e-16` on the `8^3` torus
with Gaussian three-mode reductions (F3). In all cases `Delta E >= 0`, as it must for a ground state.

**S6 (PROVED + CHECKED). Result 2: the sharp floor.** For a projective instrument `{P_i}` with each `P_i` commuting with the site parity
(rank pattern `(r_e^i, r_o^i)` in the even block `{|00>,|11>}` and odd block `{|01>,|10>}`, `sum_i r_e^i = sum_i r_o^i = 2`), the
Majorana identity `sum_k gamma_k M gamma_k = (-1)^d (4 - 2d) M` on monomials of degree `d` (CHECKED exactly, D4) gives
`Re Tr A = (1/2) sum_k R_kk = (1/2) sum_i r_e^i r_o^i`, with `R_lk = Tr[gamma_l Phi*(gamma_k)]/4` (checked D5, and `Re A_aa = (R_11+R_22)/2`).
Therefore `Delta E = lam (4 - sum_i r_e^i r_o^i)/2`.
Combinatorial bound (PROVED): for a partition with at least two nonempty parts, `sum_i r_e^i r_o^i <= 2`. If some part has
`r_e = 2`, the other parts have `r_e = 0`, and that part has `r_o <= 1` (else the others are empty), so the sum is `<= 2`; if all `r_e^i <= 1`
then `sum r_e^i r_o^i <= sum r_o^i = 2`. Exhaustive enumeration (D1-D2): the possible sums are `{0, 1, 2}`, trivial instrument 4.
So every non-trivial sharp parity-respecting site instrument costs `>= lam`, with equality exactly when the sum is 2: any binary
question of rank pattern `(1,1)`, `(1,0)`, `(0,1)`, `(1,2)`, `(2,1)` (all costs equal, whatever the superposition angles; CHECKED on `8^3`,
F4, minimum over 40 random partitions `1.194945`). The complete rank-one lock and the parity record have sum 0, cost `2 lam`.
Per outcome entropy: `Delta E >= lam H(outcomes)` bits for every sharp partition (CHECKED, D3). So *among sharp site instruments in this sea* 1.19
is an exact minimum, attained by one-mode records, and the source's 2.39 lock is the expensive end.

**S7 (PROVED). Not a minimum over record laws.** Take Kraus operators diagonal in the occupation of a coin mode `f`:
`K_y = alpha_y (1 - n_f) + beta_y n_f`. Then `A_ff = c := sum_y conj(beta_y) alpha_y` and `A_gg = 1` for the other mode,
so `Delta E = lam (1 - Re c)`. Exact example: `alpha = (3/5, 4/5)`, `beta = (4/5, 3/5)` gives `c = 24/25` and cost `lam/25` (B8).
So a non-sharp instrument is not required to cost `lam`: the cost goes continuously to 0 with the disturbance. Also, a mode of long wavelength has `E_+ - E_-` of order `|k|`, so that the source's T4(h) one-mode rule gives
cost of order `|k|`, far below lam, for a collective mode (suggested, from T4(h), not checked here).
Consequence for the claim "1.19 is what a record costs": it is the price of a **sharp** site-local binary record in this sea, and only that.

**S8 (PROVED). Result 3: classical-information criterion for the QND class.** Prior: `<n_f> = 1/2` (exact, C1), so the two classical
inputs are equiprobable. A readout `y` of the instrument has conditional distributions `P_0(y) = |alpha_y|^2`, `P_1(y) = |beta_y|^2`.
(a) `|c| <= BC := sum_y sqrt(P_0 P_1)` by Cauchy-Schwarz, so `Delta E >= lam (1 - BC)`.
(b) `I(n_f; y) <= 1 - h(BC)`, `h(beta) := H_2((1 + sqrt(1 - beta^2))/2)`. Proof: with posterior `q_y`, weights `w_y`, and
`beta_y = 2 sqrt(q_y(1 - q_y))` one has `I = 1 - sum_y w_y h(beta_y)` and `BC = sum_y w_y beta_y`. `h` is convex on (0,1):
`h'(beta) = beta artanh(u)/u` (nats, `u = sqrt(1 - beta^2)`) and `h''(beta) = sum_{m>=0} u^{2m}/(2m+3) = (artanh u - u)/u^3 > 0`
(the series coefficient is `1/(2m+1) - 2(m+1)/(2m+3) + 2m/(2m+1) = 1/(2m+3)`; CHECKED symbolically and numerically, G1-G3). Jensen gives
`sum w h(beta_y) >= h(BC)`.
(c) Attained: a pure pointer qubit with overlap `gamma = cos th` read in the optimal basis is the symmetric binary channel with error
`(1 - sin th)/2` (CHECKED against a scan over readouts, G6), `BC = cos th`, and system cost `lam (1 - cos th)`.
So for every QND instrument with information `I` bits about the occupation,
`Delta E >= lam (1 - sqrt(1 - eps(I)^2))`, `I = 1 - H_2((1 - eps)/2)`.
Values (units of `lam`): I = 0.1, 0.5, 0.9, 0.99, 0.999 cost at least 0.070, 0.374, 0.774, 0.941, 0.984 (H2). The ratio
cost/(lam I) rises from `ln 2` at `I -> 0` to 1 at `I = 1` (CHECKED, H1): `Delta E >= ln2 lam I`, and a sharp bit is the most
expensive way per bit by a factor `1/ln 2`.
**Verdict on the "observable pointer" question.** *Refuted*: an observable pointer needs a sharp lock. Any `I > 0` is available at
cost `~ ln2 lam I`. *Proved*: a **reliable** pointer for one coin-mode bit (`I >= 1 - delta`) cannot be cheap; its cost tends to
`lam = 1.19 t` as `delta -> 0`. Scope: the QND class; other sea modes, interactions and non-QND instruments are not covered (S14).

**S9 (PROVED + CHECKED, exact). Apparatus ledger.** System `S` plus a pointer qubit `A` with `H_A = omega |1><1|`, initially `|0>`, joined by
the impulsive controlled rotation `U = (1 - n_f) x 1 + n_f x (cos th - i sin th sigma_y)`; the pointer states have overlap `cos th`.
The agent's work is `W = Tr[(H_S + H_A)(U rho U^+ - rho)]`. Because `H_S` terms see only the S-reduced state, whose coherences between
`n_f = 0, 1` are multiplied by `cos th`, and `H_A` sees only the diagonal part:
`W = (1 - cos th) lam + omega <n_f> sin^2 th`, with `<n_f> = 1/2`. EXACT check with `cos th = 5/13`, `omega = 1/3` (C2, C3): `W = 128/169`;
the split is system `8/13` and apparatus `1/3 * 1/2 * 144/169`. The `omega` term is energy stored in the apparatus; the
system term is energy deposited in the lattice (stored in a defect if the mode is held, released if not, S10). For `omega = 0` and
`th = pi/2` (a perfect copy) the work is exactly the source's one-mode cost `lam`: a bond-free ancilla copy pays the same
`Delta E` as a lock (the note's T7 statement), and nothing less.

**S10 (CHECKED). Stored versus released.** If the recorded mode is then held (frozen, decoupled), the sea cannot relax below the
ground energy of the remaining modes in the same particle number. On `8^3`: stored `1.1585` of `1.1949` (97 %, the same for both
outcomes), released at most `0.0365`; for the complete site lock `2.3170` of `2.3899` (0.97; the source quotes 0.96 at `12^3`). If the
mode is not held (an ancilla copy), no lock keeps the defect and the full deposited energy is free to spread (READING; the
energy is not measured to leave in this checker).

**S11 (CHECKED). Coherent back-action at finite coupling.** 4-ring Fock space plus pointer qubit; coupling `g n_f sigma_y` switched on for
`tau = th/g`, with `H_S` running during the pulse (so `n_f` is not conserved). (I1) the work done equals `-g <n_f sigma_y>` at the
end of the pulse (exact bookkeeping `dE/dt = <dH/dt>`). (I2) the work converges monotonically to the impulsive ledger of S9 as `g` grows
(`theta = pi/2, omega = 0`: `g = 1, 3, 10, 30` give W = 0.4508, 0.6740, 0.7041, 0.7068, ideal 0.7071). (I3) The system-side energy
stays above the QND frontier of S8 evaluated at the measured reproducibility information `I_rep` (the information between the
pointer and a sharp `n_f` measurement just after the pulse): excess about `3e-5` to `1e-3`. In 16 cases there is no violation. This is a numerical
observation, not a proof (S14).

**S12 (PROVED + CHECKED). Open law versus the monotone-count theorem.** The unitary note's T1 (a count that never falls under fixed
Hermitian `H` never rises) is a statement about fixed-`H` unitary dynamics. Take a record counter `N = 1 - P_empty` on a pointer qutrit
`{empty, 0, 1}`, jump operators `J_0 = sqrt(k) |0><empty| x (1 - n_f)`, `J_1 = sqrt(k) |1><empty| x n_f` on any Hamiltonian `H_S` of
the system. Then `[H_S, N] = 0` and exactly `L*(N) = k P_empty >= 0` for every state (J1, J2 exact, rational `k = 7/5`), so the count is
non-decreasing and rises as `1 - exp(-k t)` (J4), the pointer value equals `n_f` (a classical copy), and the energy injected over the
whole formation is the S5 cost: `L*(H_S) = k P_empty x (Phi*(H_S) - H_S)` (J3 exact), the total equals `Tr rho(Phi*(H) - H)` from a stationary
state and its exponentially time-averaged value otherwise (J5). So a non-decreasing count *with* a record content is not excluded by the
monotone-count theorem once the law is open. It is a toy: it does not say how the Lindbladian arises from the axioms, and it pays
energy from a reservoir the model does not include (READING).

**S13 (PROVED + CHECKED). Additivity and rate bounds.** Records at graph distance `>= 2` have disjoint terms, so the costs add
(proof: the support of `Phi*_x'(h_x')` excludes `x`); CHECKED exactly on the 6-ring (sites 0 and 3: `1.333333 = 2 x 0.666667`, E6.4). Adjacent records that
share a hop are strictly sub-additive (`1.0` against `1.3333`, E6.5). Heat-budget rate bound (a stated-assumption statement):
if every record costs `>= lam hbar c/a` and *all* of it thermalises in the budgeted mass within the budget time, the number of records per kg per s is
at most `P/(lam hbar c/a)`; with `a = 1e-19 m`, `P = 7e-12 W/kg`: `1.85e-5` (K3, reference constants, same as the viability map's `2e-5`).
A held mode record releases only 3 %, so the *heat* bound loosens by about 33, but the 97 % is stored as rest mass, which needs its own
budget. For QND records the same budget bounds the information rate: bits per kg per s `<= P/(ln2 lam hbar c/a) = 2.7e-5` (K4), under the extra
assumption that fresh sites `>= 2` apart are used (S13 additivity).

**S14 (UNRESOLVED, first failing step).** The cost-information lower bound `Delta E >= lam (1 - BC*(I))` is proved for the QND class only. For general
even site instruments (Kraus operators not diagonal in `n_f`, or coherent finite-time couplings) S5 gives the exact cost, but no
information-disturbance inequality is proved; S11 shows no violation in 16 numerical cases. The same-family native-edge note proves a contrast-disturbance relation for
a different carrier; I did not adapt it.

**S15 (UNRESOLVED).** The pointer's own reading is not priced. In S9 the pointer is a bond-free qubit, so locking its reading is free (T1: no terms touch it). A
pointer that is a lattice site in the same sea pays `lam` or `2 lam` for its own lock (S5, S6); in an aligned product region the source's T3 gives
cost 0. The regress (what holds the pointer's record) is not closed.

**S16-S18 (UNRESOLVED / READING).** Interacting, gapped, bosonic and non-inversion-paired vacua are outside S3-S4. Whether the axioms' Record is a
Lueders or rank-one lock is the source's supplied reading (P1), not derived. For cosmological accumulation I only checked the scalings: a constant
proper-volume injection rate `r` in a matter-dominated era (`a ~ t^{2/3}`) leaves a present density fraction `3/11` (radiation-like) or `1/3` (rest
mass) of the undiluted `r t_0` (K1, exact), and energy injected at redshift `z` counts with `(1+z)^{-4}` or `(1+z)^{-3}`, so a bound of the form
"critical density x age / cost" is not a bound on early-universe births, and it ignores loss channels (READING). No injection history was fitted.

## What is new, and what is not

Not new: the one-site cost identity (T1), the numbers 1.19 and 2.39, the 96-97 % stored share, the heat-budget arithmetic, the monotone-count
theorem T1, and the general information-disturbance tradeoff (established mathematics; a parity-effect version exists in the native-edge
note, different carrier). New (same-family, unrefereed, scoped to P1-P5): the closed formula `Delta E = lam (2 - Re Tr A)` for every even one-site
instrument and its proof (S3-S5); the exact sharp floor and the cost formula `lam (4 - sum r_e r_o)/2`, whose nontrivial values are `lam`, `3 lam/2`, `2 lam` (S6); the
weak-QND cost and the proved frontier with its convexity step (S7-S8); the exact apparatus ledger and finite-pulse bookkeeping (S9, S11); the open-law
example (S12).

## Files

- `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/attempts/review-20260929-record-birth-cost-and-observability/ATTEMPT.md`
- `.../check.py`, `.../RECOVERY_STATUS.json` in the same directory.
