# Referee report: J:derive:formation-order-independence:a2

- **Author:** w-macbookpro90c72-je352 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jc19a (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-je352__01cd5ffc__20260919T013701Z`.

**Disclosure.** This referee's model family has already refereed three other attempts of this problem:

| Attempt | Referee directory | Outcome |
|---|---|---|
| a1 | `referee_w-jonathonsmac4f50-j40d0` | confirmed, with corrections |
| a4 | `referee_w-jonathonsmac4f50-jacb3` | confirmed |
| a3 | `referee_w-jonathonsmac4f50-j6e70` | failed at step 2, on the same "smallest example" claim as here |

`check.py` is independent code, with exact Fractions over full joint laws.

## The claim

1. **The DAG statement.** On a DAG with finite predecessor sets, every topological formation order gives `∏ K(v_x | v_pred(x))`.
2. **The example.** The smallest violating example is the V `A → C ← B`, with `P(C=1|a,b) = (2a+b+1)/7`. `P(1,0,1)` is `3/28` legally and
   `1/8` when `C` is formed first.
3. **Z³.** A monotone corner order on `Z³` is not a linear extension of `x ↦ {x−e_j}`.

## Step by step

**Step 1 (product formula): holds.** S1 tests 30 random DAGs with 3–5 sites, 122 linear extensions in all, with random kernels. Each DAG has
one joint law.

**Step 2 (two topological orders agree): holds.** S2 confirms that `ABC` and `BAC` give the same law.

**Step 3 (violating order changes the law): the V's numbers hold. The "smallest" claim and the order count fail.**

- **The V's numbers.** `P(1,0,1)` is `3/28` legally and `1/8` with `C` first. Exactly the orders `ABC` and `BAC` give the legal law.

- **The V is not the smallest example.** The attempt's V uses a directed reading: sources never condition on `C`, and `C` without both
  parents uses the empty kernel `1/2`. In that reading, the two-site edge `a → b` formed child-first already changes the law (S3):
  - `TV = 1/4` with the attempt's own one-parent kernel from E0 (`p = 3/4` if equal, `q = 1/4`);
  - `TV = 3/14` with the V's kernel at `B = 0`.
- **Why the attempt missed it.** Its own E0–E1 tested the two-site edge only in the undirected reading, where the later site conditions on
  the earlier. With the symmetric Ising kernel that gives `TV = 0`, and the attempt concluded that three sites were needed. The two
  readings are mixed:
  - in the V's directed reading, two sites suffice;
  - in the undirected reading, a non-symmetric one-parent kernel also violates at two sites, with `TV = 1/8`.
- **The order count.** The text says the four violating orders "place C before both predecessors". Only two do (`CAB` and `CBA`). The other
  two (`ACB` and `BCA`) place `C` between its parents. The attempt's code gives those two the empty kernel for `C`, ignoring the parent
  already recorded. That convention is not stated.

**Step 4 (Z³): the conclusion holds, the stated reason is off for one corner.** "A monotone corner order is … not a linear extension of
`x ↦ {x−e_j}`" is false for the `(1,1,1)` corner. S4, on the `2×2×2` cube with the binary product kernel `[[2,1],[1,2]]`, finds:
- the `(1,1,1)` corner order is a linear extension, and read undirected it gives exactly the DAG law;
- the other seven corner orders are not linear extensions, and each gives a different law.

**Scope.** The task also asks for the comparison with the formation-rate and formation-unit clauses (blocks 14 and 15). The attempt does not
address them.

## Verdict

**Fails at step 3.** The V is not the smallest violating example. In the attempt's own reading the two-site edge formed child-first changes
the law: `TV = 1/4` with its own kernel.

Two further corrections:
- the violating-order count is two, not four;
- the `(1,1,1)` corner is a linear extension.

What survives:
- step 1;
- the V's numbers `3/28` and `1/8`;
- the Z³ conclusion.

`check.py` prints `SUMMARY: fails at step 3 - ...` with no HIT line.
