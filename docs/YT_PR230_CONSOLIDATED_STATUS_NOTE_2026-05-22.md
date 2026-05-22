# PR230 Minimal Y_T Source-Action Support Packet

**Status:** exact support / narrowed blocker; not retained; not proposed_retained.

This packet replaces the large PR230 physics-loop history with the minimum
correct science content needed for review.  It does not claim a measured or
derived value of `y_t`.  It records one useful reduction:

```text
source-coupled site-diagonal local action
  <-> external compositional one-site product RN source semantics
```

The result is support only.  The equivalent source/action gate is not yet
accepted as current neutral EW/Higgs authority.

## Exact Support Result

Let the primitive signed record at site `x` be `epsilon_x in {-1, +1}`.  An
external one-site source profile `h` defines the Radon-Nikodym family

```text
R_h(epsilon) = exp(sum_x h_x epsilon_x) / Z(h).
```

This family has two useful properties:

1. Source profiles compose by addition:

```text
normalize(R_h R_k) = R_{h+k}.
```

2. The source generator at `h = 0` is the primitive one-site signed record:

```text
d log R_h / d h_x |_{h=0} = epsilon_x.
```

A source-coupled site-diagonal local action

```text
S_h(epsilon) = S_0(epsilon) - sum_x h_x epsilon_x
```

produces the same RN source family relative to `S_0`.  Conversely, a product
RN source with the primitive one-site generator can be read as this
site-diagonal source coupling.  Thus the source-side mathematics has been
reduced to a single authority question: may this source/action gate be
accepted as the neutral EW/Higgs same-surface source/action?

## What This Does Not Close

This packet does not derive the physical top Yukawa coupling.  It does not
authorize `proposed_retained` wording.

The following gates remain open:

1. Accept or derive the equivalent source/action gate as current same-surface
   neutral EW/Higgs authority.
2. Derive canonical `O_H` and scalar LSZ normalization on that accepted
   surface.
3. Produce strict `C_ss/C_sH/C_HH` source-Higgs pole rows, or a strict
   same-source W/Z physical-response bypass.
4. Only after physical input exists, run matching/running and retained-proposal
   gates.

## Firewalls

This packet does not use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed
top/Yukawa targets, `alpha_LM`, plaquette/u0, package-v, Planck, alpha_s, or a
fitted selector as load-bearing input.

It also does not treat LSP/projective measurement rules as source selection.
Those rules may clarify measurement instrumentation, but the source/action
authority remains a separate open gate.

## Verification

```text
python3 scripts/frontier_yt_pr230_consolidated_status.py
```

Expected result:

```text
SUMMARY: PASS=10 FAIL=0
```

The green result means the support packet is internally consistent and still
rejects retained Y_T closure.  It does not mean Y_T is closed.
