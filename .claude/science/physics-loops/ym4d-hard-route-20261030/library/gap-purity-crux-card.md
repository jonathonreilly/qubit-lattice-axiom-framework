lead: anthropic/claude-opus-5-5 laptop lead
written: 2026-11-28 (date -u), pinned at commit cf9b9b280

# The crux card: the Wilson purity bound (PUR-io)

Owner, 2026-11-28: "focus all effort and brainstorming and new math attacks on that one measurement. New being the key here." This card is the shared statement for every lane of that campaign (FINISH rows 1682 on). It states the target, the consumer and the test for "new". It proposes no method.

## 1. The target, exactly (Lean, kernel-checked consumer)

Definitions, verbatim from `lean/gapchain/GapChain/Purity.lean` L25-L29 and `PurIo.lean` L25:

```lean
def purity (Γ : CubicPeriodSublattice) (β : ℝ) (u : ℕ) : ℝ :=
  let T := Γ.transfer μt β
  let P₀ := neutralProj Γ μt
  (tracePW (P₀ * T ^ (2 * u)) / tracePW (P₀ * T ^ u) ^ 2).re

def passingCutoffs (L M : ℕ) (g₀ : ℝ) (ℓ : ℕ) : Set ℕ :=
  {k | ∀ Γ : CubicPeriodSublattice, Γ.side = ℓ * L ^ k →
    457 / 625 ≤ purity Γ (betaAt L M k g₀) (Γ.side / 512)}
```

- `Γ.transfer μt β`: the Wilson SU(2) transfer matrix in the time direction on the spatial periodic cube of side n = `Γ.side` (`lean/gapchain/GapChain/Transfer.lean` L548-L666). It is positive (reflection positivity).
- `neutralProj` (`Stage0.lean` L71): the average of the eight centre (Z_2) translations along the three spatial axes. Its range is the sector with zero electric centre flux.
- `betaAt L M k g₀` (`Stage0.lean` L151): the inverse squared bare coupling that the Sussman-Alpoge release selects at cutoff k (asymptotically free trajectory; spacing L^(-k)).
- With λ_i the eigenvalues of T on the neutral sector, purity = Σ λ_i^(2u) / (Σ λ_i^u)^2. This is the purity tr ρ² of the neutral thermal state ρ ∝ P₀ T^u at lattice time u = n/512.

**(PUR-io):** for one admissible L, the calibrated M and g₀, and one ℓ with 1024 | ℓ, the set `passingCutoffs L M g₀ ℓ` is infinite.

Consumer (KERNEL, author report, row 1679; independent rebuild row 1681 pending): `GapChain.Offset.su2_fixed_observable_gap_of_infinite_passing` (`Offset.lean` L701). Any infinite passing set gives, at the release's fixed-observable witnesses, the full fixed-observable conditions (Osterwalder-Schrader, Euclidean invariance, non-Gaussian), a mass gap (2/ℓ) log(2^18/5041) and a unique vacuum. Axioms: propext, Classical.choice, Quot.sound. The release is the work of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), on Balaban's method.

A second plug-in exists: `ExpClusters L K ν m` (Stage 2). A proof of exponential clustering of the lattice states at one physical rate m, by any route, enters there and needs no cube.

## 2. What the target says in words (ARGUED by the lead; not a proof step)

At infinitely many fine cutoffs, in a periodic box of fixed physical side ℓ, the zero-flux sector of lattice SU(2) Yang-Mills at Euclidean time ℓ/512 is close to a pure state: excited states carry at most about a quarter of the weight. Row 1672 (`library/gap-direction9-fable.md` section 1, GUESSED there) estimates that under the standard picture this needs m ℓ of about 12,000. So it is a deep-infrared statement at every late cutoff. Bare couplings are tiny there: at K ≥ 70 the cube side is at least 2^70 and β lies above 2^2800 (rows 1464, 1467). No finite computation reaches it without a carry in K.

Two facts every attack must respect (ON FILE):
- The same statement is false for weak four-dimensional compact U(1) (free photons are massless), and a correct proof must read the non-abelian structure and the dimension (tests (g1)-(g6) of row 1672's gate).
- Equivalent is not progress. A restatement of (PUR-io), or of the mass gap, in other words moves nothing.

## 3. The test for "new"

The gate of row 1672 (`library/gap-direction9-fable.md` section 4, upheld by check 1675 with the sharpening that the real test is (g1)-(g6)): one proved estimate Λ on the calibrated trajectory, at a fixed physical size above the range of the account, that

1. is an inequality with a sign and a size, uniform in K, about the Wilson law at β_K on a box of fixed physical side (or a law that Lemma TW carries to it exactly);
2. is false or void for weak 4D compact U(1), and its proof reads the dimension;
3. is not equivalent to the seed, and the seed does not follow from it by lattice-local steps alone;
4. has its first estimate written out, not named.

**Campaign filter (added 2026-11-28 after check 1692).** A proposed input to the purity bound must meet the precise form of wish (Y4) in `library/gap-purity-rh-strategy-fable-check-astra62.md` section 4: the box and law fixed before the cutoffs are chosen; a signed estimate with its gain and loss and constants fixed before K, on the same selected cutoffs; the inequality that spends the gain within the budget log(625/457); and the group, dimension, strong-coupling and neutral-spectator tests stated there.

**Twin test (added 2026-11-28 after checks 1698 and 1704).** Twice a step looked SU(2)-specific only because it used an operation that is trivial for U(1) (the adjoint action; a two-routing singlet packet; an orientation sheet). Before calling a step group-reading, build its U(1) twin with the same normalisation (for example a charge +1/-1 packet of the same dimension, the sheet theta -> -theta, the cosine-plaquette test in place of the adjoint test) and check every proved line against it. A step that the twin satisfies verbatim reads the operation, not the law.

A method is **new** for this campaign when it is not one of the method classes on file. The record of what was tried is `library/open-registry.md` (the one registry) and the attack files it cites; the earlier blind brainstorm passes are `library/gap-afield-a-max.md`, `gap-afield-b-max.md`, `gap-brainstorm-max.md`, `gap-brainstorm2-max.md`, `gap-newmath-*.md`, `gap-rh-tools-transfer-*.md`, `gap-kernel-solve-*.md`, and the direction rows `gap-direction*-fable.md`. Row 1672 records that rows 1386 to 1672 used one method (write candidates, then search the folder). This campaign uses different methods: mining how other hard problems fell, reading outside literature, and building tools.

## 4. Lanes of the campaign (owner direction of 2026-11-28)

- Strategy mining: how hard problems fell, mapped to this target (Fable).
- Far-afield new mathematics (gpt-6.2-astra max).
- Literature sweeps, mathematics and mathematical physics, 2015-2026 (gpt-6-luna), then full reads of the papers that may apply (Luna), then an applicability read (Opus).
- A tool: a design, then its first buildable component, proved by hand or checked in Lean. The solution may be a chain of different tools.
