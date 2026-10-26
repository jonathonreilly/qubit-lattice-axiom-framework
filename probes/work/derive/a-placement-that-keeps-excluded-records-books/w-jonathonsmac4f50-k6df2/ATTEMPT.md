# Can any local placement of energy and stress keep the member's books for records under one per site?

Task `J:derive:a-placement-that-keeps-excluded-records-books:a1`. Same-family, unrefereed. Worker: Claude Sonnet 5.5.
Files: `check.py` (35 checks, all PASS, about 58 s, 360 MB), `RECOVERY_STATUS.json`.

## Plain-language summary

Two records that may not share a site lose, in a collision on a square lattice, part of what the member's identity needs: the total flow of energy is not constant. The question is whether we can rescue this by shifting where we say the energy sits (adding a sum of local pieces to the energy's first moment). The answer found here: no, for two antisymmetric excluded records on Z^2, **provided three standard scattering-theory facts hold** (listed as ASSUMED). The reason is short. A shift of that kind can only add a bounded quantity to the energy dipole. A bounded quantity cannot change the long-time limit of the energy flow, before or after a collision. But the collision does change that limit, and the exact structure of the collision (a single-channel phase shift) shows it. So no bounded shift, local or not, restores conservation.

Two side findings. (b) The local operator `[H2, J]` is of order 1 at the lattice corners, not of order kappa^3; the cubic order belongs to the net change over a whole collision (numerical slope 2.98). (c) Three records add a genuinely three-body part to `[H3, J3]` but no new obstruction.

## Reading and sources (stated as required)

Read in full on main `a77a3449c91a753b06ce2a63876cd460b62cb4cf` (detached checkout): `docs/MINIMAL_AXIOMS_2026-06-29.md` (four axioms: Lattice, Qubit, Admissibility, Record), `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (approved primitives: scale reference, kinetic isotropy, realized state; none is used), and the head of `docs/audit/data/axiom_premise_nodes.json`. Landed notes read as landed: block 137 (`..._KEEPS_THE_BOOKS_ONLY_AT_LEADING_ORDER_...`), block 143 (`..._EXACT_BOOKS_NEED_RECORDS_THAT_NEVER_SCATTER_OR_BIND_...`), the 2026-09-26 collision note (`..._A_COLLISION_CHANGES_THE_RECORDS_TWO_STEP_MOMENTUM_ONLY_AT_THIRD_ORDER_...`), and the header and T1-T3 of block 141. Not read: block 121's landed text beyond its use in 137 (its content is used only through 137), blocks 135, 136, 138, 139 (PRs closed; not needed). Hashes in `RECOVERY_STATUS.json`.

Order of work: I read the landed notes and fixed my route (a bounded-G averaging lemma plus the exact rank-one S-matrix) before reading the earlier attempts printed in the probes view. The one prior attempt I then read is for the sibling task `no-local-interaction-keeps-excluded-records-books` (author claude-opus-5-5, referee grok-4.6, "Confirmed no-go"). Overlap is disclosed in "What is new".

## 1. The statement attempted

**Setting (supplied, nothing adopted).** Two records of block 54's walk `H = sigma_x S_x + sigma_y S_y` on Z^2 (qubit coin), exchange-antisymmetric. Block 78's compression `P` removes every state with both records on one site. `H2 = P(H x 1 + 1 x H)P`. Energy dipole `D2 = P(D x 1 + 1 x D)P`, matrix elements `(x_t + x_s)/2 * H_ts` on the moving record. Energy current `J = i[H2, D2]` (block 137). The member's identity with a finite stress forces the first moment of the energy placement to have a conserved current (block 137 T3(a)): `[H2, J'] = 0` for `J' = i[H2, D2 + G]`, where `G` is the first moment of a change `e_u = h + (total differences of local operators)`, i.e. a sum of local operators.

**Claim (a).** There is no bounded `G` (in particular no local, translation-invariant `G`) with `[H2, J + i[H2, G]] = 0` on two antisymmetric excluded records on Z^2, given ASSUMED A1-A5 below.

**Claims (b), (c).** See sections 5 and 6.

## 2. Premises

- ASSUMED A1. Fiber decomposition over total wave vector `K`. For almost every `K` the wave operators `Omega_±(K) = s-lim e^{iH2 t} P e^{-ih0 t}` (from the free pair `h0` on the antisymmetric space to `Ran P`) exist and are complete; they assemble into direct integrals. (Birman-Kuroda: the resolvent difference has rank at most 2, check B1, hence trace class. Direct-integral measurability is not re-proved.)
- ASSUMED A2. Riemann-Lebesgue: for `psi` in the absolutely continuous subspace and a fixed vector `a`, `<a| e^{-iH2 t} psi> -> 0` as `t -> ±infinity`.
- ASSUMED A3. Stationary form of the scattering operator: on each energy shell `S = 1 - 2 pi i T(E + i0)` with `T = |c><c| / G_cc(E + i0)` (landed, 2026-09-26 T2(a)); `G_cc(E+i0)` is finite for almost every `E` (Fatou) with `Im G_cc = pi rho_c`, `rho_c(E) > 0` on an open set of energies.
- ASSUMED A4. `G` is bounded on the two-record space and does not depend on the number of records (it is a sum of local operators of the many-record theory).
- ASSUMED A5. Block 137 T3(a): the member's identity with a local stress needs `[H2, J'] = 0` on finite-support states.
- Landed inputs used as stated: block 143 T1 (the total two-step momentum `g_a = sin K_a cos 2q_a` is constant on no shell component, for almost every `(K, E)`), 2026-09-26 E1 (singlet overlap `(1 - s1 s2 n1.n2)/4`), block 140 T1 (free current = two-step momentum).

## 3. Steps for (a)

**S1. CHECKED (A1-A8).** Exact Gaussian-integer engine, `[H2,J] = (i/16)[H',[H',D']]`.
- Free pair: `[H,J] = 0` on all 676 columns with `|r| <= 6`, both directions (control).
- Excluded pair: `[H2,J]` is nonzero on exactly the 48 columns with `1 <= |r|_1 <= 2` (12 sites x 4 coins), zero elsewhere; translation- and exchange-covariant; both exchange signs nonzero on an adjacent pair (block 137 T1 reproduced).
- Free `J` = `(i/4)(T_+^2 - T_-^2)` per record on the identity coin: the two-step momentum. `J - J_free` is nonzero only on the 48 columns `|r|_1 <= 2`; `J` is hermitian. Hence in each fiber `J_ext - J0` has finite rank, where `J_ext = J (+) 0` on the removed states and `J0` is the free current.

**S2. PROVED (algebra).** `[H2, J'] = [H2, J] + i[H2,[H2, G]]`. So the placement problem is: find `G` with `i[H2,[H2,G]] = -[H2,J]`.

**S3. PROVED. Lemma L1 (the key step).** Let `G` be bounded and `[H2, J'] = 0`, `J' = J + i[H2, G]`. For a vector `psi` write `psi_t = e^{-iH2 t} psi`. Then `<J'>_t = c` is constant, and `<J>_t = c - d<G>_t/dt`. Suppose `<J>_t` has a limit `L_+` as `t -> +infinity`. Then `d<G>_t/dt -> c - L_+`, and since `|<G>_t| <= ||G|| ||psi||^2` is bounded, `c - L_+ = 0`. The same at `-infinity`. So **`L_+ = L_- = c` for every bounded `G`**, whatever its form. Quantitatively, for windows of length `W`: `|avg_1<J> - avg_2<J>| <= 4||G||/W`. This needs no locality of `G`, no decomposition of the current, and no knowledge of `G`: the necessary condition depends on `J` alone.

**S4. PROVED given A1, A2.** Take `psi = Omega_- phi` (`phi` a free antisymmetric state, smooth in `K`). By A1, `psi = Omega_+ psi_+` with `psi_+ = S phi`, `S = Omega_+^† Omega_-`. Write `<J>_t = <psi_t|J0|psi_t> + <psi_t|(J_ext - J0)|psi_t>`. The second term tends to 0 by S1 (finite rank per fiber), A2 and dominated convergence over `K`. `J0` is the scalar `g = (1/2)(sin 2k1 + sin 2k2)` (S1), commuting with `h0`, so by the definition of `Omega_±`, `<psi_t|J0|psi_t> -> <psi_±|J0|psi_±>`. Hence `L_- = <phi|J0|phi>`, `L_+ = <S phi|J0|S phi>`.

**S5. PROVED.** By S3, S4: `<phi|(S^† J0 S - J0)|phi> = 0` for all such `phi`, so `S^† J0 S = J0`, i.e. `[S, J0] = 0` (S unitary). `J0` and `h0` commute, so on each shell `J0` is multiplication by `g(K, q)` and `S = 1 - 2 pi i T_E` with kernel condition `(g(q') - g(q)) t(q', q) = 0` for almost every `(q', q)` on the shell.

**S6. CHECKED + landed.** The kernel is rank one, `t(q', q) = tau(E) a(q') conj(a(q))`, `tau = 1/G_cc(E+i0)` (B1, exact resolvent identity for the compression). `a(q)` is the singlet overlap of the band state, nonzero off a null set (B4 at 144 rational points; landed E1). `tau` is finite and nonzero (A3; `Im G_cc > 0`). `g` is not constant on the shell for almost every `(K, E)` (B5 reproduces the rational minor; landed block 143 T1).

**S7. PROVED given S5, S6.** The product `tau a(q') conj(a(q))` is nonzero for almost every `(q', q)`, and `g(q') != g(q)` on a set of positive measure of the shell (since `g` is not almost-everywhere constant). So the kernel equation fails on a positive-measure set of `(K, E)`. Contradiction. **No bounded `G` exists (A1-A5).** ∎ (conditional)

**S8. CHECKED (B2).** Exact size of the failure: for `S = 1 + lambda |a><a|`, `|1 + lambda| = 1`, `S^† g S - g = lambda |u><a| + conj(lambda)|a><u|` with `u = (1 - |a><a|) g a`, and `2 Re lambda = -|lambda|^2`. It vanishes iff `lambda u = 0`, i.e. iff `a` is an eigenvector of `g` (checked exactly on rational matrices, both cases). With `psi_- = cos(t) a^ + sin(t) u^` the in/out change of the mean two-step momentum is `-|lambda|^2 ||u|| sin t cos t != 0`.

**S9. CHECKED (NUMERIC, float64; E1-E7).** Exact fiber operators on an N x N torus at `K = 2 pi m/N`, built from the exact tables of S1. Spectrum matches `±eps(k1) ± eps(K-k1)` to 1e-14; free current is the scalar two-step momentum; a packet in the antisymmetric sector (residual 1e-16) with no exclusion keeps `<J_x>` constant to 5e-16. With exclusion, one collision changes the window-averaged `<J_x>` by +0.0075 (N = 96, window W = 10) and +0.0070 (N = 128, W = 19). By L1 this forces `||G_K|| >= W |change|/4`: 0.019 and 0.033, growing nearly linearly with the window while the change barely moves. This is a direct test of S3 on the actual operators; it does not use A1-A5, but it is a torus fiber (equal to the infinite-plane dynamics up to finite-speed wrap-around, not proved here) and floating point.

## 4. Where the route stops, and what is not covered

- **First unresolved step: A1-A3.** The scattering imports are named, not re-proved: complete wave operators per fiber assembled over `K`, the stationary form of `S`, and Riemann-Lebesgue. The sibling refereed attempt reaches a no-go for a related class with different imports (spectral theorem, Fatou, Riesz, Paley-Wiener, coarea, Morse) and no wave operators.
- **Symmetric pairs.** The contact is rank 3, not rank one. S5 still gives `(g(q') - g(q)) t(q', q) = 0`, and by continuity `T = 0` (so `S = 1`); I did not finish the contradiction (it needs the determinant argument of the sibling attempt). Not claimed.
- **Z^3**: same argument expected (landed T1 has the 3D witness); not run.
- **Sector-dependent `G`** (a different bounded `G` per record number) is not excluded by L1 alone; A4 assumes a single density.
- **Torus numerics** are finite-size floating-point, not exact.

## 5. (b) Size of the violation for slow records

**CHECKED, exact (C1, C2).** The plane-wave symbol of `[H2, J]` (from the exact table of S1; finite relative range) has a nonzero coin matrix at the exact corners for all 128 corner assignments and both directions: the raw matrix elements are order `kappa^0`, **not** `kappa^3`. At five exact rational on-shell points (Pythagorean directions, band `(+,+)`, total wave vector conserved), band-projected with leading-order spinors: product-state elements are `kappa^0` in all 30 samples; antisymmetrised elements are `kappa^0` (7) or `kappa^2` (23), and only even orders (0, 2, 4) appear up to `kappa^5`. Scope: free plane waves (not scattering states), leading-order band spinors.

**CHECKED, numerical (E7).** The net change of `<J_x>` over one collision for packets of width `3/kappa` near the corner `(0,0)`: -1.8e-3, -1.2e-4, -1.6e-5 at `kappa` = 0.8, 0.4, 0.2: slope 2.98 between 0.4 and 0.2 (3.89 between 0.8 and 0.4, not yet asymptotic). This agrees with the landed cubic kinematics (2026-09-26 T1) and says the cubic order is a property of the integrated collision, not of the commutator's matrix elements.

## 6. (c) Three records on Z^2

- **CHECKED (D1).** A pair plus a distant third record: `[H3, J3]` equals the pair operator exactly; the spectator is inert.
- **CHECKED (D2, D3).** The connected three-body part `[H3,J3] - sum over pairs [H_pair, J_pair]` (each pair excluded alone) is nonzero on 288 of 448 three-record cluster basis states (direction 0) and zero on chains with spacing at least 2: it needs one record within a hop of both others.
- **Reading, via A4.** If `G` is one density valid in every sector, restriction to the two-record sector gives a bounded `G`, excluded by S7, so three records give no new route to a placement. A sector-specific three-record `G` is not covered.

## 7. What is new

- Retrieval or reproduction, not new: block 137 T1 (nonconservation), block 143's conditional no-go for placements, the 2026-09-26 cubic kinematics, the sibling attempt's no-go for finite-range interactions and placements in a related class.
- New (scoped, unrefereed): **L1**, that the necessary condition for any bounded placement change depends on `J` alone (no decomposition of `G`, locality not needed beyond boundedness); the pointwise rank-one form of the failure `(g(q')-g(q)) tau a(q')conj(a(q)) = 0` and the exact in/out formula (S8); the exact table of `[H2,J]` (48 columns, relative range 2) and its order-`kappa^0` symbol (not `kappa^3`); the numerical lower bounds on `||G_K||` growing with window length; the connected three-body part.
- Overlap: for the exclusion-only case with `G` of the sibling's class, (a) is already covered by the sibling's refereed route. This attempt gives a different route with different imports and a larger class (all bounded `G`).

## 8. What would finish it

Prove A1-A3 for this fiber (the rank-one resolvent makes this concrete: wave operators by Birman-Kuroda, `G_cc(E+i0)` boundary values from the van Hove structure of the walk in 2D). Then handle rank 3 (symmetric) through the invariance argument of S5 plus the determinant identity, and run the Z^3 witness.
