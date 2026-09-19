# Referee report: J:derive:two-source-interaction:a3

- **Author:** w-macbookpro90c72-j165b (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jbb31 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j165b__70e61cf3__20260919T012103Z`.

**Disclosure.** This referee's model family has already refereed four other attempts of this problem:

| Attempt | Referee directory | Outcome |
|---|---|---|
| a1 | `referee_w-jonathonsmac4f50-j714a` | — |
| a2 | `referee_w-jonathonsmac4f50-jc66e` | the snapshot-versus-persistent-pin issue |
| a4 | `referee_w-jonathonsmac4f50-jf286` | — |
| a5 | `referee_w-jonathonsmac4f50-jf209` | — |

`check.py` here is independent code: exact big-integer cylinder sums.

## The claim

1. **Reversibility.** The 7-point level automaton is reversible with respect to `π ∝ ∏_x Z(S_x)`, by the pairing identity. Its
   fluctuation–response relation is not the linear AR one.
2. **Cylinder masses.** On the six-axis `L = 2` torus at `e^β = 3`, exact enumeration gives like/unlike two-pin ratios for the
   nearest-neighbour and body-diagonal pairs. Both are above 1 and they differ.
3. **Further statements.** The one-site marginal is uniform, and the pair energy is not a pairwise superposition. `L = 2` can show no `1/r`.

## Step by step

**Step 1 (pairing): holds.** V1 checks 1000 random pairs on `L = 2`, where each axis partner counts twice, and 1000 on `L = 3`.

**Step 2 (Gibbs law ≠ AR): holds** as a statement that the two are different chains.

**Step 3 (two-pin masses): holds exactly.** V2 computes, over the six free sites (`6⁶` configurations each), with integer weights
`3⁷ Z = Σ_u 3^{u·S+7}`:

| Pair | `P(+z,+z)/P(+z,−z)` | Value |
|---|---|---|
| nearest neighbour | `17179558853813045157374427641784866348978652410041 / 47238316419587431650245082317077879359070521` | ≈ 363678.5 |
| body diagonal | `17179504273441154976879226752962922871304575139833 / 46811863452737032502816928474601790785699833` | ≈ 366990.4 |

Both are exactly the stated rationals.

For context, the face diagonal gives about 500045.9. So on `L = 2` the ratio is not monotone in distance, which is consistent with "no
isotropic `1/r` on `L = 2`".

**Step 4 (mass, additivity): holds** as stated. `log Z(|S|)` is a many-body star term. V3 confirms the one-site marginal is uniform, since
`P(+z) = P(+x)` exactly.

## Scope

- **Snapshot, not persistent pins.** These are equal-time two-site marginals of `π`, not sources pinned at every level. The task's "change
  in −log(stationary weight)" for persistent sources is a different object, as in a2.
- **Too small for `1/r`.** On `L = 2` nothing about a `1/r` coefficient can be read off, and the attempt says so.

## Verdict

**The finite `L = 2` partial survives, re-derived exactly:**
- the pairing identity;
- both stated two-pin ratios;
- the uniform marginal.

It is a snapshot statement on a degenerate torus.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
