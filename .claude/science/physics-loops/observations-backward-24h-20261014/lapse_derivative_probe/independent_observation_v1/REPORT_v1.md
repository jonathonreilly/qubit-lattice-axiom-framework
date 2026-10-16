# Blind observational-input assessment for a possible M17 extension

Independent reviewer: `/root/launch_check`. Root's new theory, code and outputs have not been read. The starting M17 note is the published-commit source `9a19c88e254a4d0eed3d4f4ed76ffa5e0082b6db`, SHA-256 `7393fe28d957358c22fdc1915eeca7c6564ad3b83f3f1355ea2628722fc94fda`.

**Conclusion:** a spatial-curvature/lapse/first-lapse-gradient input package is physically distinct from a four-curvature input package and may support a new conditional comparison. It is not automatically supplied by finite clock and ranging measurements. Nothing in this blind assessment proves the unread environmental inequality or retires its premises.

With the static physical spherical metric, independently calibrated areal radius, stationary outward endpoints, standard clock ratios and ideal vacuum roundtrip ranging,

```text
f=N/N0, g=tau', B=4/(f^2 g^2),
R3=2(1-B)/r^2 + (4B/r)(f'/f+g'/g),
|grad_h ln N|=2|f'|/(f^2 g).
```

Thus this pointwise reconstruction avoids explicit `f''` but still requires `g'=tau''`. The full derivation gives conservative positive-metric, curvature and gradient interval/error enclosures. It also gives the coordinate conversion when the observed radial label is not already the physical areal radius: that conversion needs the radius map's derivatives, including a second derivative for `g'`.

A useful weaker supplier is also available: `[r(1-B)]'=r^2 R3/2`. Integration by parts therefore encloses a specified signed weighted curvature functional from `B` values, fixed weights and boundary terms without estimating `g'` pointwise. It does not bound `(R3)_+` or supply an arbitrary spatial-volume functional. The eventual theorem must match the available functional; the pointwise derivative limitation is not a universal obstruction to weak measurement routes.

Four qualifications are essential:

1. Uniform function and slope enclosures must cover the intended domain. Finite samples with value errors do not certify derivative errors. A smooth metric can agree at all finitely sampled nodes while its three-curvature has arbitrarily large excursions between them. Additional regularity, resolution/window calibration or an independently validated weaker functional is needed. The displayed counterexample is kinematic, not a full candidate solution or universal measurement no-go.
2. A whole ball needs a controlled regular center limit; an annulus instead needs its inner boundary. Exterior links do not automatically constrain the interior. The field boundary required by an environmental theorem is an additional supplier, not a metric observable supplied here.
3. `R3` belongs to the orthogonal static physical slices. Staticity, spherical symmetry, physical-clock/metric identification and independent areal-radius calibration are substantive assumptions. Stationarity with a shift, moving reflectors, material propagation and finite turnaround delays need a different calibrated map.
4. `R4=R3-2 Delta_h N/N`. Bounded `R3` and a small first lapse gradient do not by themselves bound `R4` pointwise. A new theorem must genuinely eliminate the lapse-divergence term or control it weakly. Integration by parts can use first derivatives, but its boundary terms and weights must be accounted for. This is a concrete possible route, not a claimed theorem about root's unread proposal.

The source comparison reuses exact prior primary scopes. [Philipp et al., 1702.08412v2](https://arxiv.org/pdf/1702.08412v2), complete PDF pp. 4–6, Section III A–C, supports the stationary clock/lapse convention; it does not supply the spatial metric, a radial calibration or real instrument errors. [Faber and Visser, astro-ph/0512213v2](https://arxiv.org/pdf/astro-ph/0512213v2), PDF pp. 1–7, Sections 1–9, supplies a concrete static weak-field comparison of distinct dynamical and lensing metric information. Its GR density/pressure interpretation is not imported as a scalar-theory curvature law. The earlier Salgado and Kaiser readings remain action/frame background only; the Khoury–Weltman example remains a competing boundary-matching construction, not an ambient-state supplier. No new literature-priority or current experimental-feasibility claim is made.

Exact reused versions, PDF/text hashes, previous reading scope, equation-page checks and extraction warnings remain bound by the M17 source record, copied by reference in the new identity receipt. All 41 files in the final M17 reviewer freeze were checked unchanged before beginning. No new paper acquisition, raw data, fit, author implementation, numerical science run, formal audit, Git mutation, PR action or other-chat message occurred.

The full independent derivation is `DERIVATION_v1.md`. This report is ready to be frozen and then compared with root's proposed extension. That later exposure must have its own report; the present conclusions and counterexamples remain immutable.
