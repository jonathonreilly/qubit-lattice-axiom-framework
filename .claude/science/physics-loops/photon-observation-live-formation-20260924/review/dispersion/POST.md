# Released-source POST: photon observation Part I only

Part I is mathematically consistent with the preserved independent PRE and selects the correct observational conventions and published benchmarks. No material derivation or conversion error was found. One narrow wording correction is recommended: the three-energy timing ratios agree **at leading quadratic order**, rather than exactly at finite spacing. The explicit printed-number discrepancy identified in PRE remains preserved below.

This is a released-source comparison, not another blind derivation or an audit verdict. The complete Part I, its imports, and the shared closing remarks relevant to its observation gap were read. The Part II body, graph-control implementations and graph result rows were excluded from scientific review. Shared document/result hashes bind their identity; they do not constitute a verdict on Part II or import another checker's work.

## Exact reviewed and preserved sources

The root directory is `/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/photon-observation-personal`. The frozen identities are:

| File | SHA256 |
|---|---|
| `PHOTON_OBSERVATION_AND_LIVE_BIRTH_ROOT_DERIVATION.md` | `15c48725d54c95abe43de50de23b62fbf9d983029ee2152c125f361a9ca316ba` |
| `SOURCE_PINS.json` | `b9b16f37c7236ec8f9886bcf448805be9b744f2e61a5fba14cf5ef6a64e63a23` |
| `AUTHOR_CONTROL_SEAL.json` | `2ee41b61dd03f9e20eacd257469cd03bb54c9b96951bc06c0d58e535e0394f05` |
| `photon_birth_controls.py` | `b00520addc22448ae3fed5981964b4907a92ebe093a0bee326c5c17b7e0d8bbc` |
| `PHOTON_BIRTH_CONTROL_RESULTS.json` and complete stdout | `5fb7eeea0583f4f59795bb00273dc243bd07fe6c50dae9da571cb87e7a296c76` |
| `CONTROL_EXECUTION.json` | `27d3802370b8a5f3dc6adf2f07a88c20694b6a1190bf0cd196f4872a60852ced` |

The reviewed argument is original lines 1–122. Lines 252–270 were read for the shared qualifications concerning Part I, without endorsing their Part II calculations. The independent anchors remain PRE `19e92bfd9575efdaaeb1ad8b1a7a189de6ec900cfab8862ce465222642de8789` and PRE seal `a83ce23e6d3e27a0a4bccd4ec2170441123e6b49c0cf09b3d2670eea00a1e6e4`. All 37 PRE members match their seal. The root seal and all 11 members match as bytes, including the retained failed harness attempt. Its authorship seal is dated 18:28:05 UTC, before the independent PRE seal at 18:46:45 UTC.

The three Part I Git sources match the PRE snapshots exactly at `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`: weak-field note `651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf`, electric parent `eb5e31ae7e76f80383c454bf3e01ec98df2f503e93f04159b1cc11545d9996b4`, and ring parent `d5c5b7119cde0679ddd023904bb26d08adf31b3f6a201d877f95d604fa7b99d4`. Their exact finite-box, prepared-state, dressing, moment and ordered-limit hypotheses are reused, not independently recertified or waived.

## Mathematical comparison

Equations (1)–(2) agree with PRE: differentiating the harmonic frequency gives `v_i/c=sin(k_i)/sqrt(D(k))`; the weighted-cosine identity proves `|v|<=c`; the two transverse eigenfrequencies coincide. The latter is harmonic absence of polarization splitting, not global rotational invariance or a microscopic signal-speed theorem. The fourth-order phase coefficient `A6/720-A4^2/1152` is correct. The radial and speed corrections are `-A4 x^2/8`, the leading transverse term is `-(x^2/6)(n^3-A4 n)`, and changing from wavevector to ray direction affects the stated order-four remainder.

The complete explicit-bound proof in lines 45–60 is sound. In its notation `b=sum n_i sin(x n_i)/x`, one has `5/6<=b<=1` for `0<x<=1`. Its inverse-square-root Taylor remainder satisfies the proposed `u^2/2` bound on `[-1/12,0]`; this yields the stated `7 x^4/1440` bound. To make the multiplication step explicit, write

```
b = 1-A4 x^2/6+r_b,
d^(-1/2) = 1+A4 x^2/24+e,
|e| <= 7 x^4/1440.
```

Then the radial residual is

```
-A4^2 x^4/144 + r_b(1+A4 x^2/24) + b e.
```

The second term is at most `25 x^4/2880 < x^4/110`, and `b<=1` controls the last one. This justifies the candidate's sum, which is below `x^4/40`; no omitted cross term spoils it.

For the transverse bound, project `sin(x n)/x = n-x^2 n^3/6+rho`, with `|rho|<=x^4/120`. Since `d^(-1/2)<=12/11`, its transverse component is at most `(x^2/6+x^4/120)12/11 <=21 x^2/110`. The positive radial lower bound gives

```
|v|/c-(n dot v)/c <= (3/5)(21/110)^2 x^4.
```

Adding `x^4/40` stays below `x^4/20`. Thus Eq. (3) is supported uniformly in direction. The candidate correctly avoids claiming the same constants survive the energy-coordinate conversion unchanged. PRE supplies separate energy/ray and packet-remainder refinements; they are not silently attributed to the earlier root candidate.

Equations (4)–(6) have the right sign, power and factor of three. Identifying `E=ℏω` and the observed low-energy speed gives

```
E_QG,2 = sqrt(12) hbar c/[a sqrt(A4)],
Delta t = (L/c) a^2 A4 (E_h^2-E_l^2)/(8 hbar^2 c^2)
```

at leading order, for the stated fixed-path assumptions. The direction factor is not averaged away. The positive quadratic coefficient selects the subluminal quadratic row; a linear or superluminal limit cannot be substituted. The conversion uses `ℏ`, including `2 pi`, and the units and orientation-independent necessary bound are correct.

The cosmological paragraph explicitly supplies constant proper spacing/orientation, ordinary redshift and an FLRW transport law before borrowing the quadratic kernel. This agrees with PRE's distinction between constant proper and constant comoving spacing. It does not claim that the finite static construction selected a cosmology. The source-emission and photon/clock/detector gaps remain explicit, as does the absence of parameter selection or empirical confirmation.

## Narrow correction and preserved numerical qualification

**Minor precision edit, original lines 79–80.** The phrase “would give equal” can be read as exact equality for three energies. Equation (6) is introduced as a leading delay, so this is a wording qualification rather than a material failure of the proof. Suggested replacement:

> To leading quadratic order, three energies yield the same ratio Delta t/(E_h^2-E_l^2), up to the quartic dispersion remainder and packet, emission and other propagation errors.

No source was edited during this review. For nearly coincident energies, the PRE's absolute two-energy remainder should not be described as a uniform relative error in that ratio.

**Printed LHAASO values, preserved PRE finding.** The selected v2 ML/MINOS table states `E_QG,2>6.9e11 GeV`; its displayed `eta2` upper endpoint is `0.32`. Combining that endpoint with the paper's approximate `E_Pl=1.22e19 GeV` instead gives `6.8200073e11 GeV`, about 1.17% lower. Conversely `6.9e11` maps to `eta2=0.3126234...`. The candidate uses the printed energy-scale benchmark and does not assert exact inversion of the rounded displayed endpoint, so its conversion is unaffected. If both values are later displayed together, retain the discrepancy rather than claiming exact numerical identity or inventing an explanation for the paper's internal precision.

## Primary-source wording and evidence

The source inferences agree with the versioned PDFs preserved in PRE: [MAGIC arXiv:1709.00346v1](https://arxiv.org/pdf/1709.00346v1), PDF SHA `7b01528216cb47bad4f59ac8e8c63be66de01a917b5f03c1d40a36877b4b0ba8`, and [LHAASO arXiv:2402.06009v2](https://arxiv.org/pdf/2402.06009v2), PDF SHA `ee06a3a04a9306b0c0c1382e1675dd7df5514777fc13c569a64db7e35bcfcad9`.

MAGIC's `5.9e10 GeV` is the quadratic subluminal Table 6 value including its studied systematic uncertainties. Those uncertainties do not cover arbitrary intrinsic pulse-position drifts. LHAASO v2's selected `6.9e11 GeV` is ML/MINOS; the candidate correctly distinguishes `7.2e11` for the calibrated method and `4.7e11` for CCF. Its references to the evolving afterglow, response/background, EBL and cosmological assumptions are warranted. No current-best-limit claim, raw-data refit or new confidence-coverage result is made. This review does not turn either paper's statistical model into an assumption-free source-emission bound.

The complete `dispersion_controls` function and all 30 dispersion rows were read, including the previously truncated middle rows in a separate complete read. Its 70-digit arithmetic evaluates the intended symbol and remainder expressions. The maximal recorded radial and speed residuals divided by `x^4` are both about `0.00260417`, below the asserted `1/40` and `1/20`. Eight points overlap the independent PRE grid; their `A4`, radial and speed residuals equal the PRE output at its retained numeric precision. The 70-digit `ℏc` string and both length conversions also agree:

| Benchmark | `a sqrt(A4)` bound | Necessary orientation-independent `a` bound |
|---|---:|---:|
| MAGIC with studied systematics | `1.15857747749e-26 m` | `2.00671505552e-26 m` |
| LHAASO v2 ML/MINOS table scale | `9.90667698144e-28 m` | `1.71588678660e-27 m` |

These digits document arithmetic identity, not the precision of the observational inputs. The current root execution record has exit 0, wrapper time about 0.528 seconds, empty stderr, matching script hash, and complete stdout byte-identical to its result JSON. The earlier harness failure remains preserved in the root seal; no dispersion result is attributed to that failed attempt. No unchanged control or primary was rerun.

`POST_SOURCE_PINS.json`, `POST_VERIFICATION.json`, the scoped source/result extracts and the read-only bookkeeping script/logs bind this comparison. All PRE members remain unchanged. Part II and its separate review remain outside this verdict. The disposition is supported conditional Part I with the narrow leading-order wording edit above; no publication, retained status or audit state was changed.
