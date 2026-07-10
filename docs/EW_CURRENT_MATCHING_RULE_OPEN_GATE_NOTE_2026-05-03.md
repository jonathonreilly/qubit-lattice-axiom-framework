# EW Current Matching Rule Kappa_EW Parametrization Note

**Date:** 2026-05-03
**Claim type:** bounded_theorem
**Status:** proposed bounded recut; independent audit required
**Claim scope:** on the explicitly supplied channel-weight/readout surface,
for every `kappa_EW != 1 - N_c^2`, the note proves
`K_EW(kappa_EW) = T/(C + kappa_EW S) =
1/(F_adj + kappa_EW(1-F_adj))`. At `N_c=3` this is
`1/(8/9+kappa_EW/9)`. The `kappa_EW=0` and `kappa_EW=1` cases are exhibits,
not selector derivations.
**Primary runner:** `scripts/frontier_ew_current_matching_rule_no_go.py`

## Authorities And Supplied Premises

- [Fierz channel note](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  supplies the exact `SU(N_c)` representation-dimension fraction
  `F_adj=(N_c^2-1)/N_c^2`. It does not turn that dimension fraction into a
  correlator contribution or physical readout weight.
- [YT EW M-residual note](YT_EW_M_RESIDUAL_NOTE_2026-05-02.md) supplies the
  narrow common-CMT-scaling statement used below: on its declared two-link
  channel model, singlet and adjoint pieces acquire the same nonzero `u_0^2`
  factor.

This note has two explicit supplied premises:

```text
Supplied channel-weight map:
C/T = F_adj = (N_c^2 - 1)/N_c^2,
S/T = 1 - F_adj = 1/N_c^2.

KAPPA-EW:
the physical disconnected-current readout coefficient kappa_EW is supplied;
the connected-trace specialization is kappa_EW = 0.
```

The channel-weight map is a count-to-contribution assumption, not a consequence of
the Fierz identity. `KAPPA-EW` is an extra matching premise. Neither premise is
an axiom or a registered primitive.

## Exact Parametrization

Normalize the declared channel weights by `T=C+S=1`. Define

```text
Pi_EW^phys(kappa_EW) = C + kappa_EW S.
```

Then, whenever the denominator is nonzero,

```text
K_EW(kappa_EW)
  = T / Pi_EW^phys(kappa_EW)
  = 1 / (F_adj + kappa_EW(1 - F_adj))
  = N_c^2 / (N_c^2 - 1 + kappa_EW).                 (1)
```

The excluded pole is

```text
kappa_EW = 1 - N_c^2.
```

At `N_c=3`, equation (1) becomes

```text
K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9) = 9/(8+kappa_EW),
kappa_EW != -8.
```

Two exact exhibits are

```text
Completion A: kappa_EW = 0,  K_EW = 9/8.
Completion B: kappa_EW = 1,  K_EW = 1.
```

They show that the supplied selector changes the normalization. They do not
select which completion is physical.

## Why Fierz Dimensions Do Not Fix Channel Contributions

The Fierz authority fixes the decomposition

```text
N_c tensor anti-N_c = 1 + adj,
dim(1)=1,
dim(adj)=N_c^2-1.
```

This note does not infer general correlator weights from those representation
dimensions. At `N_c=3`, a color matrix proportional to the identity has zero
adjoint contribution, while `diag(1,-1,0)` has zero singlet contribution.
The channel-weight map is therefore kept as a separate supplied premise here.

## Common CMT Scaling

On the cited declared two-link model, take a common nonzero factor

```text
C(U)=u_0^2 C(V),
S(U)=u_0^2 S(V),
T(U)=u_0^2 T(V).
```

The factor cancels from equation (1):

```text
T(U)/(C(U)+kappa_EW S(U))
  = T(V)/(C(V)+kappa_EW S(V)).
```

No `kappa_EW` selection is claimed from this cancellation.

## OZI-Scaling Boundary

For fixed `kappa_EW`, or for a family uniformly bounded as
`kappa_EW=O(1)` while `N_c` grows,

```text
kappa_EW S/C = kappa_EW/(N_c^2-1) = O(1/N_c^2).
```

The qualifier is load-bearing. A family such as `kappa_EW=N_c^2` gives a
ratio tending to one and is not OZI-suppressed. OZI scaling therefore supplies
only a bounded asymptotic class; no `kappa_EW=0` derivation is claimed.

## Open Repair Targets

Two premise-discharge targets remain separate:

1. derive the count-to-contribution weighting from the physical
   current/correlator; and
2. derive the physical `kappa_EW` readout coefficient.

This note makes no no-go claim about either target and prunes no candidate
route.

## Citation Contract

Citation is audit-gated. This note may be cited only for equation (1), its pole,
the common-scaling cancellation, the uniformly bounded OZI class, and the two
computed exhibits under the named supplied premises.

Forbidden uses:

- citing `C/T=F_adj` as a Fierz-derived correlator weight;
- citing `kappa_EW=0` or `K_EW=9/8` as unconditionally derived;
- citing the OZI statement without the fixed/uniformly-bounded qualifier;
- using empirical agreement after choosing `kappa_EW=0` to fit or ratify the
  coefficient; or
- citing this note as a no-go against future selector derivations.

Safe downstream wording:

> On the declared channel-weight surface, the EW normalization is
> `K_EW(kappa_EW)=1/(8/9+kappa_EW/9)` away from `kappa_EW=-8`.
> The familiar `9/8` factor is the supplied connected-trace specialization,
> not an unconditional retained theorem.

Unsafe downstream wording:

> The framework derives the exact `9/8` EW color-projection correction.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_ew_current_matching_rule_no_go.py
```

The runner checks the rational family, excluded pole, common-scaling
cancellation, fixed/uniformly-bounded OZI condition, count-to-contribution
counterexamples, exhibits, dependency links, and downstream wording guards.

## Repair Provenance

- **2026-07-08:** narrowed the former no-go framing to the algebraic
  `kappa_EW` family.
- **2026-07-09:** exposed `CHANNEL-WEIGHT` as a supplied premise, excluded the
  pole, restricted the asymptotic, and removed the untested no-go route
  inventory. Independent audit owns the verdict and effective status.
