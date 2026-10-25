# ATTEMPT: J:derive:review-20261016-strain-path-and-retuning:a1

Resolve the physical strain path and the interacting retuning obligation (review-science-20261016).

- Verdict: PARTIAL. The route stops at Step 10(iii), see section 5. Two scoped sub-results are new (N1-N4 below).
- Worker: Claude Sonnet 5.5, same model family as the packet's workers and referees. Unrefereed. No cross-family confirmation was run.
- Scope: owner-requested research work. It adopts no premise, applies no audit verdict, creates no PR.
- Read before choosing premises: `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 130 lines), at main `a77a3449c91a`.
- Sources: the eight objects named in the task, read in full from commit `6afb06951a13ca861b50f47a8faf5d5c06594109` of `claude/strain-hot-matter-twins-20261013`. All eight sha256 values match (`RECOVERY_STATUS.json`; `check.py` P0.1 re-hashes the copies in `./src`). Local line numbers below (`F1:n` and so on) refer to those copies. Where the packet cites its own scripts, I did not have them and did not use them.
- Disjointness: `check.py` imports and re-runs no packet script. Its exact model is my own construction, so it is a comparator and not a recomputation of the root.

## 0. Plain words

The packet found one specific strained-Dirac one-loop law (F1) whose "rest-mass response to shear" is large and positive. It then found (F3, F4) that the same registered data admit other laws where the response is smaller, zero, or negative. The task asks which law the registered premises pick.

**Answer: none of them.** The four axioms and three approved primitives contain no Hamiltonian, no strain, no photon and no minimal coupling. The lane's own registered strain data (free bands, first-order generator, Ward identity, cubic covariance, hermiticity, locality) are satisfied by the literal deformed symbol, by every Hamiltonian dressing, and by positive local loop ensembles. They differ exactly in the quantity of interest. So the F1 value is one point of a family, and neither "SF-Hazard" nor "SF-Safe" follows from the registered premises.

What I add, all exact except where stated:
1. A proof that positive local loop ensembles realise a whole ray of covariance multipliers, with an extremal bound. On the packet's root numbers the zero needs a hop-cell traversed at least 25 times, and 23 or fewer traversals never reach it.
2. An exact one-loop model, my own, in which the dressing, the ensemble covariance and a bare-mass retune all act on one affine pole-mass response. They move three different observables. No setting keeps all three observables at their strain-free values and also flattens the pole mass. The model is a structure test and not a copy of the root: its covariance slope has the opposite sign to the root's, its Psym response changes sign when the momentum quadrature is changed from 8 to 16 nodes, and its ensemble zero needs only 3 traversals where the root numbers need 25.

## 1. What is new, and what is not

Not new (known from the sources; restated only to fix the scope):
- The F1 value `+2.4240e-2 e^2` and the OPEN reading (F1 referee, `F1v:3,17`).
- Dressing makes the Hessian affine in `a`, with `a* = 0.0141` and a non-Hermitian literal branch (F3:33, 41-44, 78-86; F3 referee items 1-2).
- Path families shift the Hessian by 0.4% to 6.9%, the seagull carries the shift, and mixtures reach zero at `lambda* ≈ -273` (F4:29-30, 109, 133; F4 referee item 6).
- The referee's claim that positive repeated-detour ensembles multiply the Psym covariance by `c_n = 2n^2+2n+1` and reach `c* = 273.998` with `n = 11, 12` (F4 referee item 6). That sentence is the only source statement of the positive-ensemble family.
- The retune P-R19-34a, its knock-on `+1.6894e-2 e_s^2` per field, and RULE-PARTIAL (F5:158; F5 referee items 3, 6).

New in this attempt (labels as in the steps below):
- N1. Step 4: a complete proof of the covariance-scaling lemma for concatenations of iid Psym draws, with the exact check. The referee's family is the special case of one draw forward `n+1` times and one reversed `n` times. The lemma gives every odd-integer multiplier, and every real `c >= 1` by mixing.
- N2. Steps 5 and 9: the extremal bound `c <= (T^2+1)/2` in terms of cell traversals `T`, and its consequence on the packet's numbers.
- N3. Steps 6-7: the exact one-loop comparator, in which all three freedoms act on one affine pole-mass response, with Ward, gauge-parameter, evenness and finite-t controls.
- N4. Step 8: the trade-off statement (no free lunch) with explicit observables, exact in the comparator and conditional for the root.

## 2. Setting and premises

S1. ASSUMED (scope): one loop, U(1), Euclidean, external `P = 0`, `E_g` strain `h = diag(1,-1,0)`, SF units. These are the packet's own (F1:99-105). No T2g, no multiplicative channel, no two loops.

S2. PROVED by inspection (premise audit). What the foundation says:
- The four axioms fix `Z^3` with cubic symmetry, a one-site `M_2(C)` domain, a nearest-neighbour rule giving a probability distribution, and records (`MINIMAL_AXIOMS:33-83`).
- Admissibility "does not choose a Hamiltonian or transfer operator" (`:119-121`).
- "Axioms and approved primitives are the complete supplied foundation" (`:108-110`).
- The three approved primitives are a unit scale, kinetic-form isotropy `c_t = c_s`, and a pointwise realized state (`PRIMITIVE_REGISTRY:31-129`). Each states what it does not supply: no dimensionless dynamical content for the first two, no state-contingent content for the third.
- Nothing in the foundation supplies a strain flow, a Dirac symbol with a Wilson term, a frame photon, a minimal-coupling rule or a gauge-path rule. Under the registry rule at `PRIMITIVE_REGISTRY:17-19` any such ingredient is an unapproved comparator.
- The Lattice and Admissibility axioms are stated cubic-rotation covariant (`:37-38`, `:57-58`). A strained law adds a rotation-breaking background by hand (READING).
- Consequence: every ingredient below is lane-supplied. This includes the F1 law itself.

S3. ASSUMED (lane data `R`, from F1:113-137, F1:30, F1:185-190): the class of one-loop laws I call `R` is
- (R1) free band energies `E∘Φ_t` for the Dirac field and `ω∘Φ^γ_t` for the photon, with the flows of `v = (t/2) h ∇(E²/2)`;
- (R2) first-order generator UD;
- (R3) the Ward identity `Σ_j d_j V_j = D_t(q) − D_t(0)` at every t, and the longitudinal two-photon identity;
- (R4) cubic covariance, hermiticity, locality (vertices continuous on the torus), `xi`-independence of the `P = 0` mass;
- (R5) critical mass fixed at `t = 0`.

Everything in `R` is a statement about the free spectrum, the longitudinal part of the vertices, and symmetries.

## 3. Steps

**1. PROVED (algebra), CHECKED (`check.py` D.1-D.4).** Hamiltonian dressing versus literal conjugation.
- Take `H = γ0 D` and a unitary `V = exp(iεG)`.
- `H' = V H V†` is Hermitian and isospectral for every `V`.
- Literal conjugation `D' = V D V†` gives `H'_L = γ0 V γ0 H V†`. If `{G, γ0} = 0` then `γ0 V γ0 = V†`, so `H'_L − H'_L† = −2iε{G, H} + O(ε²)`.
- In the toy `{G, H} = 2(c1 f2 − c2 f1)·1`. So the band energies pick up a common imaginary shift `2iε(c2 f1 − c1 f2)` unless `c ∥ f`.
- Known: F3 referee item 1. Not new.
- Toy degeneracy: for `f = c` (the toy's `G1`) the shift is 0. The toy therefore uses `G2`-type `f` for this step.
- The dressed operator stays in Dirac form with `δM = −2ε f·c` (D.2).

**2. PROVED, restating F4 Lemma 1 (not new).** What `R` fixes.
- The Ward identity fixes only `Σ_j d_j V_j` and `Σ_jl d_j d_l W_jl`.
- The difference of two laws in `R` is therefore a transverse (field-strength) coupling.
- `CHECKED` exactly in the comparator for every `a, a2, c` (B.1-B.3): Ward at both vertices through O(t²); the longitudinal two-photon identity for `c = 0, 1, 3, 7/2` and symbolic `c`; the gauge-parameter bracket of the self-energy equals `(D(Q) − D(−Q))/2`, whose mass part is 0.

**3. PROVED. The one-loop `P = 0` mass depends on a gauge-path measure only through `(J̄, Cov)`.**
- For a measure `μ` on paths `γ: 0 → n`, write `X_j(γ; q)` for the orientation-signed lattice sum of `e^{iq·x}` over the `j`-steps.
- `U_n = E_μ e^{ieX}`. To `O(e²)` it equals `1 + ie J̄·A − (e²/2)(J̄J̄* + Cov)` with `J̄ = E X` and `Cov = E|X|² − |E X|²`.
- At one loop each hop appears at most twice, so nothing else of `μ` enters.
- The exchange diagram and the Ward identity see only `J̄`; the seagull is affine in `Cov`.

**4. PROVED (new, N1).** Composite loop ensembles. Let `γ_1..γ_r` be iid Psym draws. Take integers `s_1..s_r` with `Σ s_i = 1`. Form the concatenation that traverses `γ_i` forward `f_i` times and reversed `r_i` times, with `s_i = f_i − r_i`, alternating forward and reversed pieces.
- The result is a lattice path `0 → n` inside the cell `[0,n]`, with `X = Σ s_i X(γ_i)`.
- Its mean is unchanged: `E X = (Σ s_i) E X_Psym = E X_Psym`.
- Its second moment is `E[X X*] = Σ_i s_i² E|X|² + Σ_{i≠i'} s_i s_i' |E X|² = |E X|² + c (E|X|² − |E X|²)` with `c = Σ s_i²`. This uses independence for `i ≠ i'`.
- So the one-photon vertex, the Ward data and the exchange diagram are exactly Psym's. The seagull has its covariance part multiplied by `c`.
- Mixtures of such measures are measures and realise every real `c >= 1`.
- The ensemble is positive, local (inside the cell), cubic and reversal-symmetric (A.5).
- Positivity of the covariance matrix: A.6.
- CHECKED exactly (A.1-A.4): 3D hop (1,1,1) with `c = 1, 3, 5, 11`; 2D hops (2,-1) and (1,1), including a label used in both directions. Equality is of Laurent polynomials in `e^{iq}`, so it holds for all q.
- Relation to the referee's `c_n = (n+1)² + n²`: it is the pattern "one draw forward `n+1` times, one reversed `n` times", a special case. The extremal bound of Step 5 shows it is optimal.

**5. PROVED, CHECKED (C.1) (new, N2).** For `T = P + N` traversals (`P − N = 1`), `c = Σ_labels (f − r)²` satisfies
- `c` is odd;
- `c <= P² + N² = (T²+1)/2`;
- equality only for one label used `P` times forward and one used `N` times reversed;
- `c = T` is always attainable.

  Proof: let `S+ = Σ_{s>0} s <= P` and `S− = Σ_{s<0}|s| <= N`. Then `S+ − S− = 1` and `Σ s² <= S+² + S−² <= P² + N²`. Parity: `c ≡ Σ s = 1 (mod 2)`.

**6. CHECKED (toy; exact integrand level, multilinear reconstruction) (new, N3).** The comparator, defined in `check.py`:
- 2 spatial dimensions plus continuum Euclidean time, 2-component spinors, a Wilson-Dirac symbol `D = iσ·sin k + Σ(1 − cos k_j)`, the SF-type `E_g` flow from `v = (t/2)diag(1,−1)∇(E²/2)`, and a frame photon with symbol `sin q_j` and its own flow.
- Psym generalized-link vertices from corner values, evaluated on 8 rational-trigonometric momentum nodes `(±a,±b)`, `(±b,±a)` with `sin a = 4/5`, `cos a = 3/5`, `b = π/2`; the set is symmetric under every reflection and the swap.
- All claims about the nodes are identities of the integrand, so they hold for any quadrature rule.
- The pole-mass response is `½ tr Σ(0)`. Its t² coefficient is `h(a, a2, c)`. The dressings are `G1 = −Σγ_j sin k_j` and `G2 = −Σγ_j sin k_j cos k_l`.
- Result (B.5-B.8): `h` is exactly multilinear, found from the 8 corners of `(a,a2,c)` in `{0,1}^3` and confirmed at two off-corner exact points to 1e-45. Its monomials are `{1, c, a, a2, a2·c}`. There is no `a·c` term for `G1`, and an `a2·c` term for `G2`.
- Values (60-digit evaluation of exact algebraic sums): `h = −0.175510 + 0.075120 c − 10.13180 a − 2.59925 a2 − 8.32406 a2·c`. The Psym value is `h = −0.100390`, i.e. a Hessian of `−0.2008` in the packet's convention (Hessian = 2h).
- Controls (B.1-B.6): Ward, longitudinal two-photon identity, `xi`-bracket, `t⁰` independence of `a, a2, c`, evenness in `t`, cancellation of the non-identity parts of `Σ(0)`.
- Disjoint finite-t check (B.9): true flows by ODE, true matrix exponential for the dressing, and scipy quadrature reproduce `h` at six parameter points, including off-corner ones; worst difference `1.3e-8`.
- Quadrature dependence (B.16): with 16 nodes in place of 8, the Psym response changes sign (`+0.224`) and `c*` moves from `2.34` to `0.665`, while `dh/dc` stays positive. So the model fixes structure, not signs or magnitudes.

**7. CHECKED (toy) (new, N3-N4).** Observables (B.10-B.12).
- The vacuum (free-band) energy slope per unit bare-mass retune is `−5.9029` (nonzero).
- The transverse one-photon vertex at O(t²) depends on the dressing and not on `c` or the retune.
- The transverse two-photon contact depends on `c` (and on the dressing).
- The dressing leaves the free spectrum unchanged exactly (D.1), and `c` does not enter the free vacuum.

**8. CHECKED in the comparator (algebra on the Step 6-7 numbers, B.13-B.17). The retuning bridge.**
- Let the bare-mass counterterm be `μ2 t²`. The pole response is `R(μ2, a, c) = μ2 + h(a, 0, c)`, which is affine.
- It has three different zeros, in the toy `μ2* = +0.100390` (moves the vacuum row), `a* = −0.0099085` (moves the transverse vertex), `c* = 2.33641` (moves the two-photon contact). Exact on the toy; B.13.
- Knock-on map: the vacuum row is touched only by `μ2`; the transverse vertex only by the dressing; the two-photon contact by `c` and the dressing.
- The origin `(μ2, a, c − 1) = (0, 0, 0)` is the only point where all three knock-on observables are at their strain-free values, and `R(0, 0, 1) = h(Psym) = −0.100390 ≠ 0` (B.14).
- So every pole-flat law changes at least one named observable. A retune is not a no-effect move.
- Sign: in the toy `dh/dc > 0`, but the packet's root numbers give `dH/dc < 0`. The sign of the covariance slope is not fixed by structure (B.15).
- In the toy the ensemble zero `c* = 2.336` lies in the realisable range: a mixture with weight `0.668` on the 3-traversal composite and `0.332` on Psym gives zero (B.17).
- For the root, the corresponding statement is conditional on lane numbers (Step 9) and on the assumption, not computed, that the root's three knock-on observables are nonzero.

**9. CHECKED (arithmetic on lane-supplied root numbers; not recomputed) (new, N2).** The packet gives `H_P = +2.4240125e-2` (344 nodes) and `H_J − H_P = +8.879e-5` (F4:108-109). The referee's 130-node run gives `H_P = 0.0242470`, `H_J − H_P = 8.88369e-5` (F4 referee item 3). Using `H(c) = H_J − c(H_J − H_P)`:
- `c* = 274.0` (344-node) and `273.95` (referee); the referee quotes `273.998`.
- By Step 5 the zero needs a path that traverses the hop's cell `T >= 25` times. With `T <= 23` the Hessian stays above `+7.9e-4`.
- The SF-Hazard threshold of F1 (`>= 1e-3`) fails already at `T = 23`.
- An explicit positive local ensemble with `H = 0`: weight 0.875 on a 25-traversal member (`c = 313`) and 0.125 on Psym.
- Scope: this is within the integer-signed Psym class. It is not a statement about every positive local ensemble.

**10. READING. Which path follows from registered premises.**
- (i) From the axioms and approved primitives: none (S2).
- (ii) From `R`: the literal deformed symbol with Psym (`U = 1`), the Hamiltonian dressings for every `a`, and the positive loop ensembles for every `c >= 1` are all members. `R` does not discriminate among them, and they differ in the Hessian (Steps 6-9, with the root slopes from F3 and F4).
- (iii) So "the Hessian" is a function on the space of laws in `R`. The F1 value is its value at `(U = 1, Psym)`. Any universal SF-Hazard or SF-Safe statement needs an added selection principle for the transverse and covariance data.

**11. READING. The retune argument is local.**
- The implicit-function argument (F5:66) gives a unique `m_c(h)` only where `∂m_pole/∂m_0 ≠ 0`.
- In the one-loop truncation the counterterm is exactly linear (Step 8). Nothing here shows a global failure, and I do not claim one.
- Beyond one loop nothing is computed. The order-`e²` vacuum-bubble dependence on `a` and `c` is also not computed, so Step 8's "no free lunch" is a statement about the observables listed, not about all observables.

**12. First unresolved step: see section 5.**

## 4. Controls, as printed by `check.py`

Each line of `check.py` output is PASS or FAIL. Groups:
- P0: source hashes; axiom and registry text needles.
- A: exact path-moment algebra (A.1-A.6).
- C: integer classification, extremal bound, root-number arithmetic (C.1-C.5).
- D: dressing algebra (D.1-D.4).
- B: the exact one-loop comparator (B.1-B.17).

Last full run (`check_output.txt`): 35 PASS, 0 FAIL, 148 s wall under a machine load average of about 150 (46 s CPU), 148 MB peak. It prints a HIT line, scoped as stated in Section 1. The HIT overlaps the F4 referee's positive-ensemble remark; the new content is N1-N4, not any root number.

## 5. First unresolved step

Step 10(iii): **a registered selection principle for the transverse and second-order data of the strained hop.** Specifically for:
- the Hamiltonian-dressing coefficients `a`,
- the loop-ensemble covariance multiplier `c`,
- the path family.

No registered premise supplies one. Until one is supplied the strained-pole-mass Hessian is an affine functional of free data, and no universal Hessian follows.

Also open (not attempted or not possible with the available tools):
- an analytic (non-numerical) evaluation of the root slopes `L` (dressing) and `C` (covariance);
- whether the root's transverse-vertex and two-photon-contact knock-on observables are nonzero (assumed in Step 8's root statement, computed only in the toy);
- the order-`e²` vacuum row's dependence on `a` and `c`;
- the T2g channel, where the packet's frame photon is singular (F5:107-114);
- two loops.

## 6. What this does not show

- It does not recompute any root number. All root numbers are quoted from the packet (F1, F3, F4, F5 and their referees) and used only in arithmetic.
- The toy is not the root. Its covariance slope has the opposite sign, its dressing zero `a* = −0.0099` has no relation to the root's `+0.0141`, and its Psym sign flips with the quadrature rule (B.16).
- It does not show that positive ensembles with `T = 25` are physically natural. Naturalness is not a registered criterion.
- It is same-family and unrefereed.

## 7. Related work and overlap

- Related task `J:derive:review-20261014-flavour-strain-scope:a1` concerns the chirality-grid X2 residual-symmetry classification. It shares only the word "strain" and no object.
- No landed note on main (`a77a3449c91a`) and no open PR (200 listed; title and branch search for strain, Hessian, dressing, Psym) concerns SF strain Hessians. Three open candidate-law PRs (#9907, #9940, #9952) concern a different walk model's link dressing and "minimal strain".
- Overlap with the F4 referee: the positive-ensemble idea (Step 4 relation). Everything else here is absent from the packet.

## 8. Files

- `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/attempts/review-20261016-strain-path-and-retuning/ATTEMPT.md`
- In the same directory: `check.py`, `RECOVERY_STATUS.json`, `check_output.txt` (the last full run of `check.py`), and `src/` (the eight hash-verified source copies).
