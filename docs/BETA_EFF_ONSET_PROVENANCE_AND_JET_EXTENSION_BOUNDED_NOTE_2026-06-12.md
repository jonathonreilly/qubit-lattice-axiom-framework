# Beta_eff Onset Provenance and Jet Extension Bounded Note

**Date:** 2026-06-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Exact finite-jet provenance and composition statement:
the beta_eff onset is obtained by local-response jet composition, and the
declared `Delta` coefficients through `d_11` determine the displayed
beta_eff jet through order 11. The witness-pair spread is a diagnostic only.
**Status authority:** independent audit lane only. This source note records
bounded provenance and exact rational jet algebra; it does not set, predict, or
imply any audit status or effective-status change for any claim.
**Primary runner:** [scripts/beta_eff_onset_provenance_jet_extension_2026_06_12.py](../scripts/beta_eff_onset_provenance_jet_extension_2026_06_12.py)
**Runner cache:** [logs/runner-cache/beta_eff_onset_provenance_jet_extension_2026_06_12.txt](../logs/runner-cache/beta_eff_onset_provenance_jet_extension_2026_06_12.txt)

## Scope

This note answers one bounded provenance question: how the displayed
`beta_eff(beta) = beta + beta^5/26244 + O(beta^6)` onset coefficient was derived,
and what the same finite-jet composition gives if the current `Delta` coefficient
rows are consumed as declared inputs.

No external literature value, comparator, new axiom, fitted plaquette value, or
new physical input is used here. The original bridge note is not edited.

## One-hop authorities and declared inputs

- [GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md](GAUGE_VACUUM_PLAQUETTE_MIXED_CUMULANT_AUDIT_NOTE.md)
  supplies the beta^5 provenance lines, the local one-plaquette slope, and the
  formal small-beta reduction-law composition.
- [GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md](GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_NO_GO_THEOREM_NOTE_2026-05-03.md)
  supplies the original witness scale and the finite-beta inverse-response
  firewall.
- [GAUGE_VACUUM_PLAQUETTE_BRIDGE_SUPPORT_NOTE.md](GAUGE_VACUUM_PLAQUETTE_BRIDGE_SUPPORT_NOTE.md)
  and its runner [scripts/frontier_gauge_vacuum_plaquette_bridge_support.py](../scripts/frontier_gauge_vacuum_plaquette_bridge_support.py)
  supply the existing local one-plaquette Bessel response evaluator used for
  the numeric spread diagnostic.

Declared finite-series coefficient inputs, load-bearing for the order-11 jet
but not promoted by this note:

- [BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md](BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md)
  declares `Delta(beta) := P_full(beta) - P_1plaq(beta)` and gives
  `d_6 = 7/5668704`, `d_7 = 5/17006112`.
- [BETA6_PLAQUETTE_D8_COEFFICIENT_AND_SINGLE_PAIR_VERDICT_BOUNDED_NOTE_2026-05-30.md](BETA6_PLAQUETTE_D8_COEFFICIENT_AND_SINGLE_PAIR_VERDICT_BOUNDED_NOTE_2026-05-30.md)
  gives `d_8 = 5/272097792`.
- [BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D9_COEFFICIENT_BOUNDED_NOTE_2026-06-04.md)
  gives `d_9 = -2035/264479053824`.
- [BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D10_COEFFICIENT_AND_RADIUS_EVIDENCE_BOUNDED_NOTE_2026-06-04.md)
  gives `d_10 = -10483/5289581076480`.
- [BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md](BETA6_PLAQUETTE_D11_COEFFICIENT_AND_CONTINUATION_SPREAD_BOUNDED_NOTE_2026-06-04.md)
  gives `d_11 = -13/3967185807360`.

This note assigns no audit standing to those coefficient rows. It uses them
only as declared finite-series inputs for the computation below.

## Provenance Result

Case (a) holds. The beta^5 `P_full - P_1plaq` coefficient is derived by a
direct mixed-cumulant calculation; the beta_eff coefficient is then obtained by
jet composition through the local one-plaquette response map. It is not derived
by an independent beta_eff cumulant or diagram object.

Defining lines from the provenance source:

```text
P_full(beta) = P_1plaq(beta) + beta^5 / 472392 + O(beta^6)

beta_eff(beta) = beta + beta^5 / 26244 + O(beta^6)
```

The operative derivation lines are:

```text
P_1plaq'(0) = 1 / 18

P_full(beta) = P_1plaq(beta_eff(beta))

beta_eff(beta) = beta + (1 / 26244) beta^5 + O(beta^6).
```

So the precedent is finite-jet local-response composition: divide the first
nonlocal `P_full - P_1plaq` coefficient by the one-plaquette slope under the
formal small-beta reduction law.

## Exact Jet Extension

The runner rebuilds the SU(3) one-plaquette response from the Bessel determinant
partition function as an exact rational series. Through order 11:

```text
R_O(beta) =
  beta/18
  + beta^2/216
  - 5 beta^4/93312
  - beta^5/186624
  + 7 beta^6/33592320
  + 59 beta^7/604661760
  + 97 beta^8/14511882240
  - 67 beta^9/87071293440
  - 3839 beta^10/21941965946880
  - 1949 beta^11/329129489203200.
```

With

```text
Delta(beta) = sum_{n=5}^{11} d_n beta^n,
```

and the declared `d_n` inputs listed above, exact triangular solution of

```text
R_O(beta_eff(beta)) = R_O(beta) + Delta(beta) + O(beta^12)
```

gives

| n | beta_eff coefficient a_n |
|---:|---:|
| 5 | `1/26244` |
| 6 | `5/314928` |
| 7 | `5/1889568` |
| 8 | `5/136048896` |
| 9 | `-955/14693280768` |
| 10 | `-4207/528958107648` |
| 11 | `5579/3173748645888` |

Equivalently,

```text
beta_eff(beta) = beta
  + beta^5/26244
  + 5 beta^6/314928
  + 5 beta^7/1889568
  + 5 beta^8/136048896
  - 955 beta^9/14693280768
  - 4207 beta^10/528958107648
  + 5579 beta^11/3173748645888
  + O(beta^12).
```

The runner verifies exactly, with no float atoms in the jet algebra:

```text
R_O(beta_eff(beta)) - R_O(beta) - Delta(beta) = O(beta^12).
```

## Refreshed Witness Pair

The minimal same-scale pair after an order-11 jet is:

```text
c = 10^(-7)

beta_eff^-(beta) = beta + sum_{n=5}^{11} a_n beta^n
beta_eff^+(beta) = beta_eff^-(beta) + c beta^12.
```

At `beta = 6`:

```text
beta_eff^-(6) = 32111/4374 ~= 7.341335162322817
beta_eff^+(6) - beta_eff^-(6) = 17006112/78125 ~= 217.678233600000000
beta_eff^+(6) = 76893405763/341718750 ~= 225.019568762322820
```

The original same-scale order-6 gap was

```text
10^(-7) 6^6 = 729/156250 ~= 0.004665600000000.
```

Thus the exact beta_eff witness gap moves by the factor

```text
6^12 / 6^6 = 46656.
```

Using the existing local one-plaquette Bessel evaluator as a numeric diagnostic,
the original response gap and refreshed response gap are:

```text
original R_O gap   ~= 2.914372116089026e-04
refreshed R_O gap  ~= 4.801069283071555e-01
```

This is a finite witness-pair diagnostic at the same coefficient scale. It is not
a physical tail estimate and does not select the exact nonperturbative
`beta_eff(6)`, `<P>(6)`, a convergence theorem, or a remainder bound.

## Runner

Run:

```bash
python3 scripts/beta_eff_onset_provenance_jet_extension_2026_06_12.py
```

Expected final line:

```text
TOTAL: PASS=12, FAIL=0
```
