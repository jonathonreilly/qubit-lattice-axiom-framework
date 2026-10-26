# a-clause-for-one-light-cone, attempt 1: what forces alpha = K/4, and what does not

Worker: Claude Sonnet 5.5 (`claude-sonnet-5-5`), unit `J:derive:a-clause-for-one-light-cone:a1`. Same model family as the notes it builds on; unrefereed.
Checker: `check.py` in this directory. Result: `TOTAL: PASS=30 FAIL=0`, about 3 s, about 150 MB.

**Plain language first.** The field's waves travel at `sqrt(K/(4 alpha))` times the walker's top speed. Call the square of that number `rho = K/(4 alpha)`; "one light cone" means `rho = 1`. I find three things.

1. Asking that the walker's content feed the field consistently (the "source link") does not by itself say `alpha = K/4`. It says `rho` equals the square of the walker's own speed. The value `alpha = K/4` follows only if the walker's speed is one edge per tick. The registered `kinetic_isotropy_primitive` supplies that for matter, in a reading. So the clause that finishes it is the source link plus that reading, and neither is an axiom.
2. Asking that the walker not radiate field quanta gives only `alpha <= K/4`, and that bound is sharp. Asking that field quanta not break up into walker pairs pushes the other way. No single stability clause picks `rho = 1`.
3. Exact equality of the two cones at finite wavelength is impossible for every `rho`. Only the long-wavelength speeds can agree.

## 0. What was read

- `docs/MINIMAL_AXIOMS_2026-06-29.md` lines 1-233, in full. Relevant: lines 114-130 ("Admissibility is not a dynamics axiom"; it does not choose a Hamiltonian, supply weights, or "define a time metric"); lines 85-90 (further structure needs a retained derivation or approved-primitive registration).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` lines 1-130, in full. Approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive` (lines 58-96), `realized_state_primitive`. I also read `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` lines 13-76 and its registry entry (`docs/audit/data/axiom_premise_nodes.json:35`).
- Main: all notes below were read as landed on `origin/main` at `a77a3449c91a753b06ce2a63876cd460b62cb4cf`. **Source mismatch:** the task text lists blocks 112, 124, 126-130 as open PRs. Blocks 112, 124 and 129 are landed on main, and so are blocks 134, 135, 136, 139, 144 and 149 (the "iff alpha = K/4" and cone-kinematics notes). I used the landed text. I did not read PR branches. Blocks 126-128 and 130 were not needed.
  - Block 60/129: `docs/ADMISSIBILITY_RULE_BLOCK_60S_DECLARED_NUMBERS_...2026-09-24.md:152` (nothing fixes K or alpha/K), `:80` (`c_k = 12 alpha + 36 beta`).
  - Block 62: `docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_...2026-09-21.md:67-73` (T4, `X = K wbar^2 p^2/(4 alpha)`; "nothing here forces that value").
  - Block 112: `docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_...2026-09-24.md:31` (T1 closure iff `beta = -alpha`), `:39` and `:89-93` (T3, `e'' = -(K wbar^2/(4 alpha)) p.Theta.p`).
  - Block 135: `docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_...2026-09-25.md:51` and `:86` (T1 operator identity), `:136` (T4), `:73-80` (definitions).
  - Block 149: `docs/ADMISSIBILITY_RULE_A_FREE_WALKER_NEVER_EMITS_...2026-09-25.md:27` (restricted TT action), `:31` (T1), `:55` (T5).
  - Block "every clock profile": `docs/ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_...2026-09-25.md:50` (T5: the walker's own clock bracket matches the member's with `K/(4 alpha) = 1` only for a uniform lapse; general pairs fail at third order).
- Probes view, read after fixing my plan: `one-cone-for-field-and-walker` a1 (Opus 5.5): the clauses of blocks <= 64 leave `K/alpha` free. `the-walker-against-the-members-cone` (Opus 5.5): kinematics at `alpha = K/4` only. `the-walkers-side-of-the-clocks-algebra` and `the-dewitt-ratio-and-local-conservation`: the walker's bracket and the identity. None treats general `rho` kinematics or the `v`-family below.

## 1. The statement attempted

Decide whether any clause in the lane's vocabulary (blocks 53-65, 112, 124) forces `alpha = K/4`, by testing:
- (a) a content whose energy current equals its momentum density sourcing the member consistently;
- (b) a shared causal structure (the member's characteristics equal the walker's);
- (c) whether every such demand is an added clause.

Notation. `rho = K/(4 alpha)` with `wbar = 1`. Member modes: `omega_m(q)^2 = rho |p(q)|^2`, `p_j = 2 sin(q_j/2)`. Walker: `H = sum sigma_a S_a`, `E = +-|s(k)|`, `s_j = sin k_j`. `alpha = K/4` is `rho = 1`.

## 2. Premises, by origin

- **Axioms:** nothing here is derived from them. They contain no walk, member, kinetic term or time metric (`MINIMAL_AXIOMS...:114-130`).
- **Supplied by the lane (ASSUMED, as landed):** the walk (block 54); the member and kinetic family `alpha tr(hdot^2) + beta (tr hdot)^2`, `K` (blocks 60, 62, 101, 124); the closing ratio `beta = -alpha` (block 112 T1); block 135's definitions of the averaged energy `e' = C1 C2 C3 e`, the two-step momentum `P_j = S_j C_j`, the bond current `K_a^j`, and the stress `Theta_ij = phi_j^T K_i^j`.
- **Approved primitive:** `kinetic_isotropy_primitive`, `c_t = c_s` for "the matter kinetic normalization" (`...PRIMITIVE_NOTE:15-25`). Its declared scope is matter. It disclaims dimensionless dynamical content (`:69-71`).
- **Supplied for the kinematics (ASSUMED):** a member quantum of energy `sqrt(rho)|p(q)|` with lattice-momentum conservation (as in block 149's premises); for the pair channel, a filled lower walker band.

## 3. Steps

1. **CHECKED (S1), quoted from blocks 62/149.** The restricted TT action `alpha adot^2 - K p^2 a^2/4` gives `omega^2 = rho p^2`.
2. **CHECKED (S2-S5) and PROVED by inspection.** Every lane condition I can state involves `K/alpha` only through positivity. Sign: `c_k = 12 alpha + 36 beta = -24 alpha < 0` at `beta = -alpha`. Closure: `beta/(alpha + 3 beta) = 1/2` iff `beta = -alpha`. Modes: `K > 0`, `alpha > 0`. `rho` is a ratio of two squared speeds and is invariant under a common rescaling of time. So for every `rho > 0` the lane's clauses, taken one at a time, hold. This restates block 60 `:152`, block 62 and the probes attempt `one-cone-for-field-and-walker` a1. Not new.
3. **CHECKED (C1-C5) plus PROVED scaling: the source link fixes `rho = v^2`.**
   - I re-ran block 135 T1, `-[H,[H,e']] = sum_ij nabla_i nabla_j Theta_ij`, with independent code on a `5^3` torus (integer-valued complex matrices, exact residual `0`). Opposite sign gives constant `-1`. Three mutants (unaveraged energy; stress without the transverse average; stress without `phi_j`) leave a nonzero residual for any constant, as block 135 T3 says.
   - For a walker with hop coefficient `v` (`H_v = vH`, energy `v e'`, bond current `v K` since `K_a^j` contains the bond's hop term), the same identity holds with constant exactly `v^2`: checked for `v = 1, 2, 3` (constants `1, 4, 9`, residual `0`, both sides nonzero). Scaling proof: `e'_v = v e'`, time derivative scales by `v`, so `e''_v = v^3 e'' = v^2 nabla nabla (vTheta)`.
   - The member demands `e'' = rho nabla nabla Theta` (block 112 T3; block 135 T4(a)). So the source link gives `rho = v^2`, that is `alpha = K wbar^2/(4 v^2)`.
   - **Consequence for (a):** content with energy current equal to momentum density sources the member consistently only if `alpha` is tied to the walker's speed. It is not a free-standing derivation of the number `1/4`.
4. **READING.** In the lane the walker has `v = wbar`, one edge per tick. The registered `kinetic_isotropy_primitive` (`c_t = c_s` for matter) is the statement that makes the walker's hop coefficient one edge per tick. Under that reading, step 3 gives `rho = 1`: **source link + this reading of the primitive give `alpha = K/4`.** The source link is the lane's supplied clause (block 135 premises), not an axiom or primitive. The reading is an interpretation: the walk's hop coefficient is a convention of block 54, and the primitive's text does not mention it.
5. **PROVED + CHECKED (A1-A7): (b), the stability half is one-sided.** Take the free massless walker in one fixed-sign band, momenta continuous mod `2 pi`, and the supplied quantum energy `sqrt(rho)|p(q)|`.
   - *Claim:* a same-band emission or absorption `E(k) -> E(k-q)` with `|E(k) - E(k-q)| = sqrt(rho)|p(q)|` and `q != 0` exists iff `rho < 1`.
   - *No emission for `rho >= 1`.* Identity (A1): `|p|^2 - |s(k) - s(k-q)|^2 = sum_j 4 sin^2(q_j/2) sin^2(k_j - q_j/2) >= 0`. By the reverse triangle inequality, `||s(k)| - |s(k-q)|| <= |p(q)|`. Equality in both steps would need `sin(k_j - q_j/2) = 0` for every `j` with `q_j` not zero mod `2 pi`. Then `s_j(k-q) = -s_j(k) != 0` there, so the vectors `s(k)` and `s(k-q)` are antiparallel in that component. They cannot be non-negative multiples of each other, so the reverse-triangle step is strict. Hence the difference is `< |p(q)| <= sqrt(rho)|p(q)|`. (This is block 149 T1 at `rho = 1`. Exact sweep A2: 5997 rational points, including zero-sine components, all strict.)
   - *Emission for `rho < 1`.* Let `a = arccos sqrt(rho) in (0, pi/2)`. Take `k = 3a/2` and `q = a` along an axis. Then `k - q = a/2 > 0`, both energies are positive, and `sin(3a/2) - sin(a/2) = 2 cos a sin(a/2) = sqrt(rho)|p(q)|` (A5; A7 for `rho = (n/40)^2`). For general axis `k` in `(a, 2a)`, `q = 2(k - a)` (A3). Exact rational witnesses: A4, 95 witnesses, `rho` from `49/625` to `1600/1681`.
   - The supremum of `||s(k)| - |s(k-q)|| / |p(q)|` is 1 and is not attained (A6).
   - **So stability of the walker against single-quantum emission is exactly `alpha <= K/4`.** `alpha = K/4` is the boundary of the stable region, not forced by it.
6. **PROVED (IVT) + CHECKED (B1-B6): the other side is unstable in the opposite direction.** Pair creation by a member quantum, particle at `k+q` in the upper band and hole at `k` in the filled lower band, has energy `F(k,q) = |s(k)| + |s(k+q)|`.
   - `F >= |s(q)|` (B2, sweep; proof: `s_j(q) = sin(k_j+q_j) cos k_j - cos(k_j+q_j) sin k_j`, so `s(q)` is a sum of `s(k+q)` and `s(k)` each scaled componentwise by factors of modulus at most 1, and the triangle inequality gives `|s(q)| <= |s(k+q)| + |s(k)|`).
   - For `rho < 1` the channel is closed when every `cos^2(q_j/2) > rho`, since then `rho|p|^2 < |s(q)|^2` (B1, B3).
   - For `rho >= 1` take `q` on an axis with `sin^2(q/2) <= 3/(1+rho)` (B4b). Then `|s(q)| <= sqrt(rho)|p(q)| <= F(k*, q) = 2|cos(q/2)|` at `k* = pi/2 - q/2` (B4, exact endpoint inequalities for `rho in {1, 5/4, 4, 25, 400}`). `F` is continuous in `k`, so there is a resonant `k` (intermediate value theorem). At `rho = 1` the symmetric pair `(-q/2, +q/2)` is exactly resonant for every `q` (B5; this is block 149 T5).
   - **Joint statement (B6):** for no `rho` are both processes closed at small momentum. This is kinematics only: no matrix element, rate, quantization or coupling is derived, and it uses the supplied one-quantum energy and the filled-band reading.
   - **For (b):** a shared causal structure cannot be obtained from "neither process happens". The only available inequality from stability is `alpha <= K/4`. The opposite inequality `alpha >= K/4` ("no member signal outruns the walker's top speed") is a separate causality-type clause, not in the lane's vocabulary or the axioms. I have only the statement that it would be needed; I did not search for a derivation of it.
7. **CHECKED (D2, D3): the strongest reading of (b) fails.** The two full lattice dispersions differ at finite wave number for every `rho`: `omega_m^2 - omega_w^2 = sum_j 4 sin^2(q_j/2)(rho - cos^2(q_j/2))`; at `rho = 1` it is `sum_j 4 sin^4(q_j/2) >= 0`. The cones agree in speed only at long wavelength. Together with the walker's own clock bracket failing at third order for general lapse pairs (block "every clock profile" `:50`), no exact lattice-wide "one cone" statement is available at any `rho`. "One light cone" can only mean equal long-wavelength speeds.
8. **READING (D1): the primitive extended to the member.** In the TT sector the Euclidean action has coefficients `alpha` (time) and `K/4` (space). Exchange of time and space is a symmetry iff `alpha = K/4`. That is nearly a restatement of `rho = 1`; its force depends entirely on whether `kinetic_isotropy_primitive` covers the member's kinetic form. Its text says "the matter kinetic normalization" and also "equivalently the Euclidean regulator block ... is hypercubic-symmetric" (`:17-25`). Whether the second wording extends to a non-matter field is not decided by the text. It also does not settle the other sectors of the member (the lapse and the shift), where hypercubic symmetry alone does not fix the relative coefficients (block 124 `gamma` term, block 62 T4(c)).

## 4. Conclusion on (a), (b), (c)

- **(a)** Forces `rho = v^2`. With `v = 1` (the primitive, in the reading of step 4) it gives `alpha = K/4`. This needs the source-link clause, which is added.
- **(b)** Stability gives only `alpha <= K/4` (sharp). No stability clause gives equality (step 6). Exact cone equality is impossible (step 7). The causality half is an added inequality.
- **(c)** Yes, for every demand I tested: each one is an added clause (source link; no-radiation plus a no-outrunning inequality; extension of the primitive). The lane's vocabulary without them leaves `rho in (0, infinity)`.

## 5. What is new relative to the sources

- New (CHECKED/PROVED): the exact one-sided threshold in step 5 (block 149 had `rho = 1` only); the pair-channel opening for all `rho >= 1` and its closure for `rho < 1` at small momentum, and the joint statement (step 6); the `v`-family and `rho = v^2` (step 3); the exact statement of what the primitive would have to cover (steps 4 and 8).
- Not new: the independence of `K/alpha` from the clauses (block 60, 62; probes `one-cone-for-field-and-walker` a1); block 135 T1 itself (re-run independently, same result); block 149 T1 and T5 at `rho = 1`; the long-wavelength gap of the dispersions at `rho = 1` (`sin^4` identity, in `one-cone-for-field-and-walker` a1).
- Searched, not found: I grepped `docs/ADMISSIBILITY_RULE_*` and `probes/work` for Cherenkov-type conditions on the ratio. I found classical-source Cherenkov conditions for a moving source (`a-delay-for-the-rate-field` attempts), but no quantum same-band threshold in `rho`.

## 6. The first step that does not close

Step 4, then step 6's missing half. Whether the source link and the primitive reading are admitted is a decision outside the supplied notes: the first is a lane clause, the second an interpretation of a registered primitive's scope. Without them the route stops at step 3 (`rho = v^2`) and step 5 (`alpha <= K/4`).

## 7. What would finish it

1. An owner decision on whether `kinetic_isotropy_primitive` covers every kinetic form (then step 8 gives `alpha = K/4` in the TT sector with no source link; the sectors with lapse and shift still need their own statement), or whether the walker's hop coefficient `v = wbar` is the registered content (then step 3 plus the source link gives it).
2. Or a derivation of a no-signal-outruns-the-walker clause, which together with step 5 gives equality.
3. Open in the sources, not touched here: the transverse sector of block 135, nonuniform rates, and a referee from another model family.

## 8. Limits of this attempt

- Continuum momenta: a finite torus need not contain the witness momenta.
- The member's quantum energy and the filled band are supplied. A classical wave's energy is not fixed by its frequency.
- Kinematics only, no rates. Two-body and interband processes are outside step 5. Interband emission is block 149 T3.
- The torus identity is checked on `L = 5` only, and the hop-coefficient family on `v = 1, 2, 3`. I take block 135 T2's symbol argument for all tori.
- D1 is close to a restatement of the coefficient ratio.
- No claim of status is made. Nothing here is adopted.
