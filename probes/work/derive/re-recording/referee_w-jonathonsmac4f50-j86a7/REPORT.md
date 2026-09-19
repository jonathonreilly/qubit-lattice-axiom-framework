# Referee report: J:derive:re-recording:a1

- **Author:** w-macbookpro90c72-j5e15 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j86a7 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j5e15__49570efa__20260919T011813Z`.

**Disclosure.** This referee's model family has already refereed other attempts of this problem: `referee_w-jonathonsmac4f50-j50b9`,
`-j4469` and `-jf4b6`. One of them found that a neighbour-only synchronous law factorises over the sublattices on bipartite windows.
`check.py` here is independent code.

## The claim

- **(a) Asynchronous re-recording.** It is the heat bath of the static nearest-neighbour law, reversible for any clock rates.
- **(b) Synchronous 6-stencil re-recording.** It is reversible with respect to `∏_x Z(S_x)`.
  - That law is the marginal of the doubled graph `Γ₆`, whose Laplacian spectrum is `{E, 12 − E}`.
  - The zone corner is a zero mode, whereas the 7-stencil gives `{E, 14 − E}` with an odd corner eigenvalue of 2.
  - On the `2×2×2` cube at `(3,1,2)`, the static and sync all-`+x` probabilities differ.
- **(c) Transfer.** At small `β` the sync symbol is `(6 − E)²`, and the async law transfers the static results.

## Step by step

**Step 1 (async detailed balance): holds.** V1 checks it exhaustively on the Ising 4-cycle at `t = 2`, and on a six-axis 3-site path at
`(3,1,2)`.

**Step 2 (bilinear identity): holds.** V2 checks 200 random pairs on `(Z/4)³`.

**Step 3 (`Γ₆` spectrum): holds.** On `(Z/4)³` (V3):
- `Γ₆` has spectrum `{E, 12 − E}` with exactly **two** zero eigenvalues;
- with the self-loop the spectrum is `{E, 14 − E}` with one zero eigenvalue, and the odd corner eigenvalue is 2.

**Correction.** The second zero mode is not an open "infrared statement about the graph". On even tori `Γ₆` has two connected components.
The sync stencils see only the other sublattice, so `∏_x Z(S_x) = f(s_odd)·g(s_even)`. Under `π` the two sublattices are exactly
independent, and the staggered channel is uncoupled, not merely ungapped. V4 checks this on `L = 2`: the stencils see only the other
sublattice, and `Z_sync` is the product of the two sublattice half-sums.

**Step 4 (cube): the conclusion holds, the comparator is mismatched.**
- **The sync value.** It is `3489597637546254592801/31238481641953905892567296 = 1.117·10⁻⁴`, exactly as stated. It uses the `L = 2` torus,
  where the 6-stencil counts each neighbour twice.
- **The static value.** The attempt's `59049/775835648` is the isolated cube with 12 single bonds. That is not the async stationary law of
  the same doubled stencil.
- **The matched comparator.** The matched law carries `φ²` on each pair and gives `94143178827/29808744616192 = 3.158·10⁻³`.
- **So** "static ≠ sync on this window" holds against the matched law too, but the attempt's witness compares two different graphs.

**Step 5 (small `β`): holds.**
- `log(sinh κ/κ) = κ²/6 − κ⁴/180 + …`.
- The 6-sum's `|S|²` has symbol `(6 − E)²`, checked on three modes of `(Z/4)³`.

**Step 6 (what transfers): holds as a reading.** It is sharpened by the factorisation above: the sync law is two independent sublattice
laws.

## Verdict

**The partial survives, with two corrections.**
- **What re-derives:**
  - async detailed balance;
  - sync reversibility;
  - the `Γ₆` spectrum and the 7-stencil contrast;
  - the small-`β` symbol;
  - the sync cube value.
- **Correction 1.** Step 4's static comparator is the single-bond cube. The matched doubled-stencil static law gives `3.158·10⁻³`, still
  different from sync.
- **Correction 2.** The zone-corner zero mode is the exact sublattice decoupling of the sync law, not an undecided infrared question.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
