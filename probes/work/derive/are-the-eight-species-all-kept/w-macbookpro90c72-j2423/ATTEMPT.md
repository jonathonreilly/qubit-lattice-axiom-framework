# J:derive:are-the-eight-species-all-kept:a2: no supplied clause removes a branch, reading the sixteen as one object is the parked decision, and a closed static system with both signs has total ledger zero

**Provenance.**
- Worker `w-macbookpro90c72-j2423`, model `claude-opus-5-5`, one session. Attempt 2 of 3; no prior attempt files exist.
- **Plan, formed before reading.**
  - **(a)** Use the coin algebra's lack of an anticommuting element, and the senses of the species.
  - **(b)** Use block 60 T4's charges with opposite signs and block 71 T3(d)'s positivity criterion.
- **Sources.**
  - Blocks 60 (T1, T4), 70 (T1, T3), 71 (T3, T4) and 58 (T1), on their PR branches.
  - The axioms memo, read in full (`docs/MINIMAL_AXIOMS_2026-06-29.md`: one-site algebra `M₂(ℂ)`; a record locks one local possibility and is read by content alone).
  - Block 77's staggered term, via the task's setting.
- **Not read:** block 82 ("what can gap the walk inside the qubit"), which is later than the task's setting.
- **Comparator, named and ASSUMED.** The fermion-doubling theorem (Nielsen–Ninomiya).
- Nothing is adopted. The parked decisions are not proposed.

## 1. The statement attempted

**(a)(i) A further nearest-neighbour term (PROVED; CHECKED E.gap, E.ops).**
- **Nothing in M₂(ℂ) gaps a species.**
  - No nonzero 2×2 matrix anticommutes with `σ_x, σ_y, σ_z`.
  - Every term of the covariant nearest-neighbour family `a₀ + 2aΣcos k + βσ·sin k` is a scalar at each of the eight species points `k = πn`. So no such term gaps any species; it only shifts its crossing energy (block 77's `1:3:3:1` levels).
- **The staggered term `mε`** is covariant and nearest-neighbour in the rate-timed sense. It couples each species `n` to `n̄ = n + (1,1,1)`, which has the opposite sense (`det D_{n̄} = −det D_n`), and gaps the pair to `±m`.
- **Senses.** The eight senses sum to zero (four of each).
- **Seven is impossible.** By the doubling theorem (ASSUMED), any local Hermitian term removes gapless crossings only in opposite-sense pairs. So gapping exactly seven species is impossible for any local term on `M₂(ℂ)` sites.
- **Gapping all eight** keeps all sixteen branches, now massive; it removes none.
- **What the staggered term does** (exact on the `4³` torus, integer matrices):
  - **Current.** It anticommutes with each one-step momentum `S_a`, so block 63's conserved current is lost. It commutes with each two-step momentum `S_aC_a`, so block 69's survives.
  - **Maps.** `V_nHV_n = s_nH` but `V_nεV_n = ε`, so for the four odd species `H + mε ↦ −H + mε`. The odd maps and block 70's energy reversal no longer carry solutions to solutions.
  - **Force law and covariance.** Clause B's force law holds: the rates multiply the whole generator, and the rest energy is timed (block 77). Proper-rotation covariance holds: `ε` is invariant.
  - **Top speed.** It drops below 1 for every species.

**(a)(ii) Sixteen components on the doubled lattice (PROVED; CHECKED E.map).**
- **The map.** The regrouping `x = 2y + η` (`η ∈ {0,1}³`) followed by the Hadamard transform over `η` (`HHᵀ = 8`) is unitary. It carries each species' plane wave exactly to one taste at every coarse site.
- **The object per coarse site** is `ℂ² ⊗ ℂ⁸`: sixteen components.
- **The honest reading.** As a map this is a relabelling of the same fine lattice. Read as **one object per site**, it makes the coarse site carry a one-site space larger than the Qubit axiom's `M₂(ℂ)`. **That is the parked larger-site-algebra decision in disguise.** Stopped there, as instructed.

**(a)(iii) Records (PROVED; CHECKED E.form).**
- **A formed record's amplitude.** An amplitude localised at a site has `⟨H^k⟩ = 0` for every odd `k`, because the walk is bipartite with no on-site term (CHECKED for `k ≤ 7`). So its spectral measure is symmetric: it weighs both signs of energy equally. It also weighs all eight species equally: every species' plane wave has modulus 1 at every site.
- **What a record reads.** A record reads only its site (Record axiom), and the site density is the same for every species (block 70 T1(d)). So no record can tell species or signs apart.
- **Formation events.** A formation event, a localisation, mixes all species and both signs.
- **The record's energy.** Block 58's `m′` is a supplied rest energy. The record's locked possibility (an element of the one-site domain) carries no energy sign.

**(b) A closed static system with both signs (PROVED; CHECKED E.zero, exact rationals).**
- **Setup.** In block 60's curvature member, take bodies at rest with charges `Q₁ = −Q₂ = Q`.
- **The field.** `χ = 1 + Q(g₁ − g₂)`, with bare energies `m_i = 8KQ_iχ_i` (block 60 T4(a)), and `N` from `(−Δ + Q/χ)N = 0` with `N = 1` on the walls.
- **The ledger.** The walls' ledger is `8K(Q₁ + Q₂) = 0`.
- **Existence.** Positive static rates exist iff the rates' operator is positive definite (block 71 T3(d)).
- **Executed on a `5×3×3` box**, bodies at `(1,1,1)` and `(3,1,1)`, `Q = 1/10`, `K = 1/2`:
  - `χ > 0` everywhere;
  - `m₁ = 248876/609875`, `m₂ = −239024/609875`;
  - all 45 exact LDL pivots of the rates' operator are positive;
  - `N > 0` everywhere;
  - block 60's bond-form ledger is stationary at every site (`∂𝓔/∂u = ∂𝓔/∂λ = 0`, exact).
- **HIT condition met.** There is an exact static solution with total ledger zero.
- **Its meaning.** By block 60 T1 the ledger is the walls' share, so at total zero the solution is also stationary under a change of the unit of rate. With amplitudes of both signs the unit of rate can be a variable.
- **The mass balance.** The positive body is heavier in bare energy: `m₁ + m₂ = 8KQ(χ₁ − χ₂) > 0`.

**(c) What could decide which amplitudes are present.**
- **Nothing local removes a branch:**
  - (a)(i), and the doubling theorem;
  - no rule of finite reach keeps only the positive energies (block 71 T4);
  - records cannot tell species or signs apart (a)(iii);
  - the ledger does not exclude mixed configurations (b).
- **What remains** are global or declared choices: which amplitudes are present (the owner's fork), the exchange sign with a filled-sea reading (block 76's reading, a comparator), or a boundary or initial condition.
- **A larger site algebra**, which would let Wilson-type terms gap species singly, is the parked decision. It is not proposed here.

## 2. Steps

**S1 (PROVED; CHECKED E.gap).**
- **No anticommutor.** The linear system `{M, σ_a} = 0` for `a = 1, 2, 3` has only `M = 0` (sympy).
- **Scalars at the species points.** At `k = πn` every `sin k_a = 0`, so the covariant family is `(a₀ + 2aΣcos πn_a)·1`: one eigenvalue.
- **The staggered pair.** `ε` shifts `k` by `π(1,1,1)`. On the pair `(n, n̄)` at the species point the walk vanishes and the `4×4` block is `m` times the swap, with eigenvalues `±m` (each twice).
- **Senses.** `det D_n = (−1)^{|n|}`, whose sum over the eight species is `1 − 3 + 3 − 1 = 0`.

**S2 (PROVED; CHECKED E.ops).**
- **Commutators.** `ε` flips the sign of every one-step hop and fixes every two-step hop. So `{ε, S_a} = 0`, `[ε, S_aC_a] = 0` and `{ε, H} = 0`.
- **The maps.** `V_n = R_nU_n`, with `U_n = (−1)^{n·x}` and `R_n` the coin's half turn with `R_nσ_aR_n⁻¹ = (s_nD_n)_aσ_a`. `U_n` commutes with `ε`, both being diagonal, and `R_n` acts on the coin only. So `V_nεV_n = ε`, while `V_nHV_n = s_nH` (block 70 T1(b)).
- **CHECKED** with integer matrices on `4³` for `n = (1,0,0), (1,1,1), (1,1,0)`.

**S3 (PROVED; CHECKED E.map).** The Hadamard matrix over `{0,1}³` satisfies `HHᵀ = 8·1`. The species' plane wave `(−1)^{n·x}` restricted to the block `2y + η` is `(−1)^{n·η}`. Its transform is `8δ_{taste, n}` at every coarse site.

**S4 (PROVED; CHECKED E.form).** `H` hops by one site and `ε` anticommutes with it. A walk of odd length cannot return to its start, so the site state's odd moments vanish. Checked for the coin state `(1, 1)` at the origin of `4³`, `k = 1, 3, 5, 7`.

**S5 (PROVED; CHECKED E.zero). The zero-ledger pair.**
- **Construction.** Block 60 T4(a): off the bodies `Δχ = 0`, and `(Δχ)_i = −Q_i`. So `χ = 1 + Σ Q_i g_i` with `g` the Dirichlet inverse of `−Δ`, and `μ_i = Q_iχ_i` gives the bare energies.
- **The rates.** Block 60 T4(b) and block 71 T3(d): `(−Δ + Q/χ)N = 0` with `N = 1` on the walls has a positive solution iff the operator is positive definite. Positive LDL pivots without pivoting are equivalent to that, for a symmetric matrix.
- **Stationarity.** Checked exactly at every site: `e + 8KN(Δχ) = 0` with `e = m w` at the bodies, and `N(Δχ) + χ(ΔN) = 0`.
- **The ledger.** `8K(Q₁ + Q₂) = 0` (block 60 T4(c) proof: the walls' term equals `8KΣQ_i`).

## 3. The first failing step

- **The route "a supplied clause removes branches"** fails at S1. Nothing in `M₂(ℂ)` gaps a single species, and the staggered term works in opposite-sense pairs.
- **The route "one sixteen-component object"** stops at S3, because it is the parked decision.
- **The route "a zero-total closed system is impossible"** fails at S5, because one exists.

## 4. What would finish it

1. **The full family of zero-ledger static pairs.** The range of `Q` and separations for which the rates' operator stays positive definite; it fails once the negative charge's well is deep enough, as in block 71 T3(c).
2. **Whether such a closed system is dynamically stable** under block 60 T5's kinetic term for the lengths.
3. **The owner's fork on which amplitudes are present.** Nothing local decides it.

## 5. Running it

```
python3 probes/work/derive/are-the-eight-species-all-kept/w-macbookpro90c72-j2423/check.py
```

The run takes under a second. It prints five exact checks, then the SUMMARY and HIT lines.
