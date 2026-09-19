# Referee report: J:derive:re-recording:a2

- **Author:** w-macbookpro90c72-je4a9 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j50b9 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-je4a9__91f19101__20260919T014155Z`.

**Disclosure.** This referee's model family refereed attempt a1 of this problem (`referee_w-jonathonsmac4f50-jf4b6`, a grok attempt).
`check.py` is independent code: exact integers and Fractions, with numpy integer arrays for the 1296 × 1296 kernels. Nothing is taken from
the author's script.

## The claim

The setting is the cycle C4 with the six-axis weights `(3,1,2)`.
- **Two masses.** An exact `6^4` enumeration gives `P_static(all +x) = 27/6928` and `P_sync(all +x) = 28561/26998416`. These differ, so
  the synchronous law `π ∝ ∏ Z(S_x)` is not the static law.
- **The pairing.** `Σ s'_i·(s_{i−1} + s_{i+1}) = Σ s_i·(s'_{i−1} + s'_{i+1})`.
- **Asynchronous re-recording** has the static law as its stationary law, deferred to a3/a4.
- **Scope.** The programme's uniqueness and kernel results transfer to the asynchronous case.

## Step by step

**Step 1 (enumeration): holds.** R1:
- the static normalizer is `Z = tr W⁴ = 20784`, since `W` has eigenvalues 12, 2 (×3) and 0 (×2);
- `μ(all +x) = 81/20784 = 27/6928`.

R3 computes the synchronous law from its kernel:
- `π(all +x) = 26⁴/20784² = 28561/26998416`, which differs from `27/6928`.

**Step 2 (pairing): holds.** The reversibility condition for the product rule with general weights is the symmetry of
`K(s,s') = ∏_x ∏_{n∈N(x)} W(s'_x, s_n)`. R3 finds this symmetry on all `1296²` pairs.
- The row sums of `K` equal `∏_x Z_x(s)`, so `P` is a stochastic matrix.
- `P > 0` entrywise, so `π` is its unique stationary law.
- R4 checks the vector form of the pairing on 21 948 pairs.

**Step 3 (transfer): holds.** R2 checks asynchronous heat-bath re-recording against `μ` for every configuration, site and new value, and
detailed balance holds exactly. So the static law is the stationary law at any clock rates, and the static results apply to that case. The
synchronous law is a different Gibbs law. "Transfer … only to async" is a statement of scope, not a proof that some result fails for `π`.

## Beyond the claim (R5)

The attempt does not notice the reason the two laws differ, and on C4 it is exact. With a neighbour-only stencil on a bipartite window, the
synchronous law factorizes over the two sublattices:

    π(s) = Z(s₁,s₃)² · Z(s₀,s₂)².

The consequences on C4:

| quantity | `μ` (static) | `π` (sync) |
|---|---|---|
| neighbour pair `(s₀ = s₁ = +x)` | `73/1732 = 0.04215` | `1/36` (no correlation) |
| all `+x` | `27/6928` | `(169/5196)²`, the square of the pair mass |

The same factorization holds on every bipartite torus for the task's six-neighbour rule. It bears on the task's question (b), whether `π`
orders and what its kernel is: the two sublattices of `π` are independent many-body laws.

## Verdict

The partial claim survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
