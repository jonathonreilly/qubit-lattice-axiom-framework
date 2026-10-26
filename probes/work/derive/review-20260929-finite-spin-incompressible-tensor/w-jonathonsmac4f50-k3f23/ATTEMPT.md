# A finite-spin incompressible tensor channel: necessary conditions, not a state

Task `J:derive:review-20260929-finite-spin-incompressible-tensor:a1`. Worker: Claude Sonnet 5.5 (same family as the source authors; unrefereed). No agents were spawned. Nothing outside the output directory was written.

## Verdict (plain language)

**PARTIAL.** I did not build a state with an inelastic TT susceptibility of order q^2 and a linear lowest weighted mode, and I did not refute that one exists. What I proved instead is a list of exact conditions that any such state must meet. They rule out whole families of candidates (harmonic/Gaussian, flat, short-range-correlated, and any candidate whose ground-state bookkeeping removes only the mean). The route stops at the many-body step: nothing here supplies a state with the required power-law correlations.

Reading statement. I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` (current main, `a77a3449c91`) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, including the three approved primitives (`scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`). None of them is used below.

## What the axioms say, what the lane supplied, what is proved here

| Layer | Content |
|---|---|
| Axioms (`MINIMAL_AXIOMS_2026-06-29.md:37-82`) | Cubic lattice Z^3. One qubit-algebra M_2(C) of possibilities per site. A nearest-neighbour rule fixes a distribution. Records form, are one per site, permanent, and are the only readable content. Lines 85-90: further structure needs a retained derivation or an approved primitive. |
| Supplied by the lane (not axioms) | Six tensor-electric slots per cell (not one qubit per site); an integer stencil G; slot values read as electric fields; Hamiltonians of local terms that each preserve G E = b; a ground state and a probe O_q. Moves that change several slot contents at once conflict with record permanence (the lane's own admission, probe-10 note, "Records"). Nothing below uses the records reading. |
| Proved here | Steps S4 to S9 below, under premises P1 to P7. They are statements about the supplied model, not about the axioms. |

## Sources and provenance

- Source branch `claude/toe-viability-probes-20260927`, frozen head `fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`. All 33 source objects were extracted from that commit and their sha256 matched `probes/work/review-science-20260929/SOURCE_MAP.json` (`RECOVERY_STATUS.json`). PR #9363 is CLOSED, unmerged.
- None of the six parent notes in the task list is on current main (`ls docs` finds no match). What is on main: the stencil G (`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_..._2026-09-14.md:96-97`), the moment proof (same note, 225-243) with its own caveat "not a no-go for qubits" (213-217), the moment chain (`RING_MODEL_ENERGY_ONLY_BOUNDS_..._2026-09-25.md:26-32`), and `FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_..._2026-09-30.md` (canonical-bracket obstruction; a different question, not used).
- Overlap search: no `ai/probes` attempt exists for this problem or the three nearby ones I looked at (`deferred-20260926-cubic-couplings-and-gauss-screens`, `deferred-20260926-local-rk-preparation`; the review-science README has no completed attempt). `gh pr list` searches on "incompressible", "susceptibility tensor", "graviton qubit" return nothing relevant.
- Read in full: probe-10 note (the q^4 sum rule), the Gauss-law note, the swapped-assignment note, the SUMMARY, ROUTES, ASSUMPTIONS rows S4 and C (`ASSUMPTIONS.md:28,47`) and kill round 1 (`agents/kill1_price_strong.md:10-19`).

## Premises (all ASSUMED)

- **P1 Slots.** Six slot types per cell (jj at doubled position 2x, ij at 2x+e_i+e_j). Each slot is finite-dimensional, with commuting diagonal electric operators E_s on a unit-step spectrum (spin 1/2: E = +-1/2).
- **P2 Rule.** The stencil (G p)_j(x) = p_jj(x+e_j) - p_jj(x) + sum_{i!=j}[p_ij(x) - p_ij(x-e_i)] (main, 09-14 note:96-97), sector G E = 0.
- **P3 Hamiltonian.** Translation-invariant, H = sum_x sum_a T_(a,x), fixed finite range, volume-independent norms. Each term splits into electric-change components T_(a,x,m) with E_s T_m = T_m (E_s + m_s). Each term preserves the sector, so only active m (G m = 0) occur (m = 0, i.e. diagonal terms, is allowed and does not contribute to double commutators).
- **P4 Probe.** O_q = N^{-1/2} sum_s e^{i q.r_s} eps_{c(s)} E_s with a real polarization eps in slot space (TT directions in ker G(q); basis independent after summing).
- **P5 Thermodynamic limit.** For statements about q -> 0 along a ray I use infinite-volume objects: spectral measures of O_q in a translation-invariant ground state exist for a continuum of small q, and the finite-volume sum rules of S4 pass to them (they are identities in local expectation values).
- **P6 For Theorem B only.** At the q considered the ground state has no elastic weight, S_el(q) = 0. Example: a unique translation-invariant ground state and q != 0 (momentum conservation gives <0|O_q|0> = 0 and P0 O_q|0> = 0).
- **P7** Same-family, unrefereed.

## Definitions: the whole ground eigenspace is removed

Let P0 be the projector on the E0-eigenspace of the ground state |0> (the whole eigenspace, not a rank-one projector), Q = 1 - P0. For a probe O put

- mu_O = sum_{n in Q} |<n|O|0>|^2 delta(omega - (E_n - E_0)),
- m_j(O) = integral of omega^j dmu_O,
- S_in = m_0, chi_in = 2 m_{-1} (the source's convention),
- omega_min = infimum of the support of mu_O (the lowest weighted mode outside P0),
- S_el = <0|O^dag P0 O|0> >= |<0|O|0>|^2, S_tot = S_in + S_el.

Subtracting only the mean <0|O|0> leaves S_el - |<O>|^2 (and its zero-energy denominators) inside the "inelastic" moments.

## Steps

**S1 (ASSUMED).** P1 to P7.

**S2 (CHECKED; re-verification, not new).** The stencil rebuilt from its formula has an exact rational kernel (dimension 15 on a 3^3 box, 66 on 4^3) in which every basis vector has vanishing zeroth and first moments for each slot type, at the declared doubled positions. This is the landed lemma (09-14 note:225-243), here by exact nullspace over Q instead of the polynomial-gauge argument. `check.py` S2.

**S3 (CHECKED).** A +-1 (qubit) kernel move found by scipy MILP in the 4^3 box has support 20 (optimal in that box), G m = 0 at every row of an enlarged window, zero zeroth/first moments, and nonzero TT quadrupole along x and y (cross polarization, M = -2; zero along z for this one move). For its two TT polarizations the exact series gives w(t q-hat) = -(M/2) t^2 + O(t^3). So for H = -J sum(T + T^dag) over this move's translates, K(q) <= 2J|w|^2 = (J M^2/2) q^4 and kappa c^2 <= J M^2 = 4J along x (cross). The 20-slot minimum is the lane's already-reported value; I only reproduce it. This is the premise-non-vacuity check.

**S4 (PROVED, supporting facts CHECKED).** For an eigenstate and moments over Q:

1. *f-sum.* <0|[O^dag,[H,O]]|0> = <0|O^dag(H-E0)O|0> + <0|O(H-E0)O^dag|0> = m_1(O) + m_1(O^dag). Expand [O^dag,[H,O]] = O^dag H O - O^dag O H - H O O^dag + O H O^dag. The E0 terms combine. In the eigenbasis, H - E0 vanishes on P0, so the sum is over Q. This holds for any state in a degenerate ground eigenspace.
2. *Chain.* omega_min m_{-1} <= m_0 <= m_1/omega_min (support bound), m_0^2 <= m_{-1} m_1 (Cauchy-Schwarz), hence omega_min <= m_0/m_{-1} <= sqrt(m_1/m_{-1}) <= m_1/m_0, and m_{-1} <= m_1/omega_min^2.
3. *Sum rule.* For an active component, [E_s, T_m] = m_s T_m gives [O,T_m] = w(m) T_m, [O^dag,[T_m,O]] = -|w|^2 T_m with w = N^{-1/2} sum_s e^{iq.r_s} eps_c m_s. This is exact for any slot dimension and E-dependent prefactors (`check.py` S4, sympy, spin 1/2 and spin 1, complex prefactors). Summing the N translates gives sum_x |w_x|^2 = |m-hat(q)|^2 (phases cancel). By the zero zeroth/first moments, |m-hat(q)| <= mu_2(m) |q|^2/2. Hence **K(q) := <[O^dag,[H,O]]> = -sum_(a,m) |m-hat_(a,m)(q)|^2 t_(a,m)** with t_(a,m) = <T_(a,0,m)> per cell, and |K(q)| <= C_H |q|^4, C_H = (1/4) sum ||T_(a,m)|| mu_2(m)^2. For a ground state m_1(O^dag) >= 0, so **m_1(O) <= K(q) <= C_H q^4**. This is probe-10's T3; it is cited, and re-proved here only to carry the whole-eigenspace definition.
4. Numerical check (ring of 8 sites, qubit dipole-conserving move (1,-1,-1,1), diagonal NN and NNN couplings, Q=0 sector, ground eigenspace of dimension 2 found by tolerance): the f-sum identity, K <= 2J|m-hat|^2 at all four ring momenta, and the whole chain hold with P0 removed (`check.py` S5; floating point).

**S5 (CHECKED exactly; PROVED lemma).** *Mean-only subtraction breaks the source's own bound.* Lemma: for E-diagonal O, P0 O|0> receives contributions only from ground states sharing E-support with |0>. For a stoquastic H in one connected fragment the ground state is unique and S_el = |<O>|^2. The difference arises for a state that is a superposition across degenerate fragments (a translation-invariant "cat" over spectator configurations). Exact example in `check.py`: sites 0-3 carry the move (1,-1,-1,1), sites 4,5 are spectators, H = -(T + T^dag). Ground energy -1 has multiplicity 4. Take |0> = psi_+ (x) uniform over spectators and a generic rational f. Then:

- S_Q = 316969/705600 = m_1/omega_min with omega_min = 2 (the f-sum sees exactly the Q weight);
- S_mean-only = 483569/705600 > m_1/omega_min, and the elastic weight is 17/72 while the mean squared is 0.

So "S <= m_1/omega_min" (the step behind probe-10's S <= C_H q^3/c) fails for the mean-only structure factor and holds for S_in. The ring example in S4(4) has a degenerate ground eigenspace but zero elastic weight (translation partners with disjoint E-support): the degeneracy alone is harmless for diagonal probes; a cat across fragments is what matters. **Scope: this is a bookkeeping correction, not a physical result.**

**S6 (PROVED). Theorem A (window).** Assume P1 to P5 and, along a ray q = t q-hat, t in (0,t0): (H1) chi_in(q) >= kappa t^2, (H2) omega_min(q) >= c t, with kappa, c > 0. Then, with C_H from S4(3) and k(q-hat) := -(1/4) sum_(a,m) |M_(a,m)(q-hat)|^2 t_(a,m), where M_(a,m)(q-hat) = sum_s (q-hat.r_s)^2 eps_c m_s:

- (a) S_in >= c kappa t^3/2.
- (b) m_1(O) >= c^2 kappa t^4/2.
- (c) S_in <= C_H t^3/c.
- (d) chi_in <= 2 C_H t^2/c^2.
- (e) k(q-hat) >= c^2 kappa/2, i.e. -sum |M_(a,m)|^2 t_(a,m) >= 2 c^2 kappa. In particular kappa c^2 <= 2 C_H.

*Proof.* (a) chi = 2 m_{-1} <= 2 m_0/omega_min, so m_0 >= omega_min chi/2 >= c kappa t^3/2. (b) m_1 >= omega_min m_0 and (a). (c) m_0 <= m_1/omega_min <= C_H t^4/(c t). (d) m_{-1} <= m_1/omega_min^2 <= C_H t^4/(c^2 t^2). (e) With the zero zeroth/first moments, |m-hat(tq-hat)|^2 = t^4 |M|^2/4 + O(t^5) for each of finitely many move types; checked in S3 (series). So K(t q-hat) = t^4 k(q-hat) + O(t^5). By S4(3), K >= m_1(O) >= c^2 kappa t^4/2. Divide by t^4 and let t -> 0. QED.

(c) and (d) are probe-10's T4 (source `ONE_QUBIT_PER_SLOT...:186-204`). **(a), (b) and (e) are not in the sources.** (e) says the state must have measurable local kinetic energy: the expectations t_(a,m) of the moves, weighted by the squared TT quadrupole of each move, must be negative enough. A product state or a sign-random state has t_(a,m) near 0 and fails (b); a state with S_in = Theta(1) fails (c).

`check.py` S9 verifies (a) to (d) on 2000 exact rational spectral measures and shows the window is non-empty at the moment level: a single mode omega = c q with weight kappa c q^3/2 has chi = kappa q^2, S = kappa c q^3/2, m_1 = kappa c^2 q^4/2, consistent with m_1 <= C q^4 iff kappa c^2 <= 2C. So Theorem A alone excludes nothing; the exclusions below come from the structure of S_in.

**S7 (PROVED). Theorem B (no short-range Born statistics).** Assume P6 and (H1), (H2) for all t in (0,t0). Then the connected Born correlations of the TT electric pattern cannot satisfy sum_Delta |Delta|^3 |C(Delta)| < infinity.

*Proof.*
1. All E_s commute, so S_in = S_tot is the structure factor of the classical probability distribution |<E|0>|^2 (P6). For q != 0 only connected correlations contribute (a translation-invariant mean sums to zero).
2. With real eps and translation invariance, C_ab(Delta) = C_ba(-Delta), so f(t) := S_in(t q-hat) = sum_Delta c(Delta) cos(t q-hat.Delta) with c(Delta) real and summed over slot-type pairs and displacements (half-integer displacements included).
3. Assume sum |c||Delta|^3 < infinity (hence sum |c| < infinity, since all displacements except Delta = 0 have |Delta| >= 1/2). By Theorem A (a),(c), c kappa t^3/2 <= f(t) <= C_H t^3/c.
4. f(t) = O(t^3), so f(0+) = 0 = sum c, by dominated convergence. Then the t^2 coefficient: sum c (q-hat.Delta)^2 = 0.
5. Hence f(t) = sum c [cos(t q-hat.Delta) - 1 + (t q-hat.Delta)^2/2], and |cos x - 1 + x^2/2| <= min(|x|^3/6, x^4/24). So |f(t)|/t^3 <= sum |c||Delta|^3 rho(t q-hat.Delta) with rho(x) = min(1/6, |x|/24) -> 0. Dominated convergence gives f(t) = o(t^3), contradicting f >= c kappa t^3/2. QED.

Corollary. In 3D a pointwise bound |C(Delta)| <= A |Delta|^{-6-delta}, delta > 0, is excluded (the sum is then convergent). A state meeting (H1), (H2) needs Born correlations of the TT electric pattern decaying like |Delta|^{-6} or slower along the ray (log-borderline; in 3D, |q|^3 is the Fourier transform of |Delta|^{-6}). `check.py` S6 confirms exactly the two sides in one dimension: with a finite-support correlation obeying sum c = 0 and sum c Delta^2 = 0, S = 16 sin^4(q/2) = q^4 + ...; a tail c ~ r^{-4} gives the closed form sum cos(qr)/r^4 = pi^4/90 - pi^2 q^2/12 + pi q^3/12 - q^4/48 (error < 1e-25) with an odd cubic term, S/q^3 -> pi/6, and a divergent third moment (log growth); an exponentially decaying c with S(0) = S''(0) = 0 imposed has S/q^3 -> 0.

*Scope.* Conditional on P5 and P6. Not a statement that no such state exists: it says it must be a critical, power-law-correlated state (S_in ~ |q|^3). When there is elastic weight (cat or degenerate ground eigenspace sharing E-support), S_tot = S_in + S_el and the argument applies only if the correlation hypothesis is placed on S_in itself.

**S8 (PROVED). Which candidates the conditions remove.**

1. *Harmonic/Gaussian.* In a quadratic comparator H = (1/2) E.U.E + (1/2) theta.K.theta with U a finite-range local quadratic form on ker G(q), chi = eps^T U(q)^{-1} eps >= 1/||U(q)|| >= 1/R, R a row-sum bound independent of q (`check.py` S8: oscillator chi = 1/U exactly in sympy; norm bound on 200 random stencils, numerical). Theorem A (d) needs chi_in <= 2 C q^2/c^2 for a linear mode, which fails as q -> 0. So a linear lowest weighted mode is excluded for every Gaussian state; the comparator's omega = sqrt(UK) q^2 is the consistent value. This is the exact sense in which "beyond harmonic comparators" is forced; it restates the source's remark that chi stays bounded in every comparator examined.
2. *Flat inelastic weight* (an RK-type structure factor S_in >= s0 > 0): contradicts Theorem A (c).
3. *Short-range-correlated states with a lowest linear mode of order q^3 weight:* Theorem B.
4. *A state with no local kinetic expectation:* contradicts Theorem A (e).

**S9 (PROVED + CHECKED). Exact termwise Gauss preservation is not harmonic shift invariance.**

- For the linear Gauss operator G_x = sum g_s E_s, [G_x, T_m] = (g.m) T_m, so exact preservation is the grading condition G m = 0 (`check.py` S7). It says nothing about quadratic potentials.
- For a diagonal quadratic potential Q = sum_{s<t} a_st E_s E_t on spin-1/2 slots and a product-flip move T_m (m_s = +-1 on its support): on every active configuration, Q(E+m) - Q(E) = sum_{t not in supp} E_t (sum_{s in supp} a_st m_s). So [Q,T_m] = 0 iff sum_{s in supp} a_st m_s = 0 for every outside slot t. The squares E_s^2 = 1/4 are constants and play no role.
- Harmonic shift invariance X m = 0 (X symmetric with free diagonal d_s) gives the same outside-slot rows; its support rows only fix d_s, which is always solvable because m_s = +-1.
- If the squares are dropped as constants (d = 0), the harmonic condition is strictly stronger. Exact dimensions in `check.py` S7 on a 6-slot example: 13 (commuting cross terms) = 13 (projection of the harmonic solution space) > 9 (harmonic with d = 0).
- So the cross terms of a Fierz-Pauli-type form are not constants at spin 1/2 and are constrained by exactly the outside rows; harmonic shift invariance is sufficient but not necessary for exact commutation. This is scope cleanup (the swapped note's claim for the metric-diagonal assignment is consistent with it), not a new result.

**S10 (READING).** In the sector G E = 0 on a contractible region, E should be a second derivative of an integer-valued potential Q (the kernel of G being the image of a discrete incompatibility operator). I have not verified exactness of that complex over Z[x^{+-1}]. If it holds, the requirement S_in ~ |q|^3, chi ~ q^2, omega ~ q reads: the potential Q must have free-massless-field equal-time statistics (S_Q ~ 1/|q|) with a linear mode, i.e. the stored electric field is the double derivative of the graviton-like field. This matches the lane's "composite" language (kill 1, `agents/kill1_price_strong.md:19`). It is an interpretation, not used above.

## What is new relative to the sources

- **Not new.** S2 (landed lemma), S3's 20-slot minimum (reported by the lane), S4 (probe-10 T3/T4 and the main-note chain), the oscillator chi = 1/U (textbook), the statement that a linear mode needs chi = O(q^2) (probe-10, kill 1).
- **New, scoped (same-family, unrefereed).**
  1. Theorem A (a), (b), (e): the lower bound S_in >= c kappa q^3/2, the saturation of the f-sum at order q^4 and the local kinetic-quadrupole condition.
  2. Theorem B and its corollary: the state must have non-summable cubic Born correlations (|Delta|^{-6}-type tail), so no short-range-correlated state qualifies.
  3. The exact mean-only counterexample (S5).
  4. The spin-1/2 exact-commutation versus harmonic-invariance dimension count (S9) is a clarification.

## First unresolved step, and remaining obligations

**First unresolved step: S11 (not reached).** Exhibit, or refute, a translation-invariant ground state in the exact-rule finite-spin class (qubit slots, P1 to P3) for which all of the following hold with volume-independent constants, with the whole ground eigenspace removed:

1. S_in(q) = Theta(|q|^3) with Born correlations of the TT electric pattern decaying as |Delta|^{-6} (Theorem B);
2. omega_min(q) >= c|q| on the lowest weighted mode;
3. the local kinetic expectations satisfy -sum |M_(a,m)|^2 t_(a,m) >= 2 c^2 kappa (Theorem A (e)).

Nothing in the sources or here supplies a state with property 1. A finite box cannot decide it (exponent fits need many q; an exploratory (not in check.py) enumeration of the one-dimensional analogue found 160-state fragments among 12870 states at 16 sites, which also warns that a thermodynamic phase is not accessible by small exact diagonalization). A finite-box MILP support count, a commutator identity or an RK sampler does not establish it either.

Remaining obligations:
- **O1.** Passage from finite-volume sum rules to the infinite-volume objects used in Theorem A and B (P5), including uniform tail control.
- **O2.** Independent confirmation of the proofs (same-family, unrefereed here); N1 to N8 would be required before any negative statement is promoted. None is promoted: Theorems A and B are conditional necessary conditions, not a no-go for a state.
- **O3.** Exactness of the integer complex behind S10.
- **O4.** A non-Gaussian, non-short-range construction or a proof that the kinetic-quadrupole condition cannot be met together with property 1 (for example in the 3D qubit move family).

## Files

- `check.py` (29 checks, about 10 to 35 s, under 300 MB), `check_output.txt` (its last run), `RECOVERY_STATUS.json`, and `src/` (the 33 verified source objects, read-only copies).
