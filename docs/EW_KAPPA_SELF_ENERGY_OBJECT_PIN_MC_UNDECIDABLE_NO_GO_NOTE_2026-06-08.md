# EW kappa_EW Object Identification and Monte-Carlo-Undecidability No-Go Note

**Date:** 2026-06-08
**Claim type:** no_go
**Status:** no-go proposal for independent audit-lane review. Sharpens the
already-landed EW `kappa_EW` no-go family with two new results: (i) `kappa_EW`
is **structurally not Monte-Carlo-decidable**, and (ii) the channel fraction
`R_conn = 8/9` is a **kinematic, `beta`-independent gauge-orbit fraction**, not a
dynamical coupling renormalization. It pins the object `kappa_EW` weights (the
bare connected EW correlator, which computes the full color trace `S + C`) and
keeps the readout weight `kappa_EW` as an external scheme choice. It does **not**
privilege either completion (`kappa_EW = 0` or `kappa_EW = 1`), introduces no new
axiom, selector, or audit verdict.
**Primary runner:**
[`scripts/frontier_ew_kappa_self_energy_object_pin.py`](../scripts/frontier_ew_kappa_self_energy_object_pin.py)
(PASS=20/20, zero PDG/experimental inputs).
**Cached output:**
[`logs/runner-cache/frontier_ew_kappa_self_energy_object_pin.txt`](../logs/runner-cache/frontier_ew_kappa_self_energy_object_pin.txt).

## Cited authority (one-hop, landed)

- [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)
  — `retained_no_go`. Names `kappa_EW`, the parametrization
  `K_EW(kappa_EW) = 1/(F_adj + kappa_EW(1 - F_adj))`, and proves the retained
  Fierz/CMT/OZI packet does not fix it; the physical readout functional (which
  channels the matched coupling retains) is the open gate. CMT scaling is
  color-blind (§2).
- [`EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md`](EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03.md)
  — `retained_no_go`. Writes the connected two-current correlator as
  `<J_EW(x) J_EW(y)>_same line ~ Tr_internal(Q_EW^2) [S + C]`; the singlet
  channel carries weight `Tr_internal(Q_EW^2)`, not `Tr_internal(Q_EW)^2`.
- [`RCONN_DERIVED_NOTE.md`](RCONN_DERIVED_NOTE.md) — `retained_no_go`. The MC
  `R_conn = C/T = 8/9` is a consistency check after choosing the connected-trace
  target; it is not a derivation of `kappa_EW = 0`.

Plain-text context (not load-bearing dependencies of this no-go):
`docs/EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md` (the exact
`F_adj = (N_c^2-1)/N_c^2` ratio), `docs/EW_CURRENT_MATCHING_OZI_SUPPRESSION_THEOREM_NOTE_2026-04-27.md`
(the `O(1/N_c^2)` singlet size class), and `docs/COMPLETE_PREDICTION_CHAIN_2026_04_15.md`
§4.1 (which states the singlet channel is the non-planar, genus `>= 1`,
`1/N_c^2`-suppressed piece and the adjoint channel is planar).

## Background: the named coefficient

The framework's sub-percent EW couplings (`g_1`, `g_2`, `1/alpha_EM`) and its
top mass (`m_t`, `-0.07%`) ride a color projection on the EW gauge coupling and,
reciprocally, on the Yukawa:

```text
g_EW  ->  g_EW * sqrt(K_EW(kappa_EW)),    sqrt(9/8) only at kappa_EW = 0,
y_t   ->  y_t  * sqrt(8/9),               the kappa_Y twin (same I_color insertion).
```

with `K_EW(kappa_EW) = 1/(F_adj + kappa_EW(1 - F_adj))` and `F_adj = 8/9` at
`N_c = 3`. The good numbers are the `kappa_EW = 0` (singlet-subtracted)
specialization; `kappa_EW = 1` (full trace) gives `K_EW = 1` (no projection). The
matching-rule no-go proved both completions are compatible with the retained
packet. This note keeps that symmetry and adds: (a) the object `kappa_EW` weights
is pinned, but the readout weight is external; (b) `kappa_EW` is not
MC-decidable; (c) `R_conn = 8/9` is kinematic and `beta`-independent.

## 1. Headline 1: kappa_EW is structurally not Monte-Carlo-decidable

The lattice ensemble outputs the channel data `{<S>, <C>, <T> = <S> + <C>}`
(runner §E). Of these, only `<T> = <Tr[G G^dag]>` is pointwise gauge-invariant;
the per-configuration `S, C` are gauge-variant, and `<S>, <C>` are their
gauge-orbit (ensemble) averages over the gauge-invariant measure — well-defined
channel diagnostics, not direct gauge-invariant observables. The bare connected
correlator the ensemble computes is the full trace `<T> = <S> + <C>`. But
`kappa_EW` is the **external weight** of `S` in the physical readout functional
`Pi_phys = C + kappa_EW S`:

- `Pi_phys(kappa_EW = 0) = C` (singlet-subtracted) and `Pi_phys(kappa_EW = 1) = T`
  (full trace) are **both** functions of the **same** measured `{S, C, T}`;
- no Monte-Carlo observable is a function of `kappa_EW` alone.

Therefore measuring the correlator to arbitrary precision — including measuring
the gauge-invariant connected object directly — fixes the channel split
(`8/9 : 1/9`) but **not** `kappa_EW`. This is why the MC measurement of `8/9`
(`RCONN_DERIVED_NOTE`) is a consistency check, not a determination: the residual
freedom is the continuum readout functional (which channels the matched physical
coupling retains), an input external to the ensemble. The harder, fully
gauge-invariant object is no more decisive, and the reason is structural.

## 2. Headline 2: R_conn = 8/9 is a kinematic, beta-independent gauge-orbit fraction

The split `<S>/<T>` is not a dynamical coupling renormalization. It is the
fraction of the open bilocal `G(x,y)`'s Hilbert-Schmidt norm carried by the
trace (singlet) direction once the unfixed gauge ensemble averages over the
gauge orbit. The exact statement (runner §C) is a gauge-orbit-average identity
that holds for **any** dressed propagator `M` (an arbitrary complex matrix, not
just unitary), by the Weingarten identity
`<|Tr[Omega(0) M Omega(x)^dag]|^2> = (1/N_c) Tr[M M^dag] = <T>/N_c`:

```text
<S>/<T> = 1/N_c^2     for an ARBITRARY dressed (non-unitary) M averaged over its
                      gauge orbit  M -> Omega(0) M Omega(x)^dag,
```

verified numerically (runner §C) for `N_c = 2,3,4,5`, with the free-propagator
and Haar-random color matrix as two cross-check regimes. So
`R_conn = C/T = (N_c^2 - 1)/N_c^2 = 8/9` at `N_c = 3` independent of the
dressing. Because the result does not depend on `M`, `R_conn = 8/9` is
`beta`-independent: it is the gauge-orbit singlet fraction, not a quantity with a
continuum (`beta -> infinity`) trend. This is consistent with the prediction
chain's `beta`-independence statement (§4.1), here given its kinematic reason. The singlet weight `<S> ~ <T>/N_c^2` is precisely the
non-planar / `O(1/N_c^2)` (OZI) piece of the single connected loop, matching the
OZI size class.

## 3. The object identification (the readout weight is separate)

`K_EW` renormalizes the EW gauge coupling, i.e. it is fixed by the EW
gauge-boson self-energy built from the framework's own color-blind point-split
current `J^mu_x ~ bar(psi)_x Q_EW U_mu(x) psi_{x+mu}`, whose color structure at
the vertex is `I_color` (SU(2) x U(1) is a direct-product factor commuting with
SU(3)). For a color-blind vertex the connected two-current loop factorizes
(runner §B, exact at any gauge configuration):

```text
<J_EW(x) J_EW(y)>_connected = Tr_internal(Q_EW^2) * Tr_color[G(x,y) G(y,x)]
                            = Tr_internal(Q_EW^2) * Tr_color[G G^dag]
                            = Tr_internal(Q_EW^2) * (S + C),
```

using the staggered color reflection and the Fierz/Parseval identity
`Tr[G G^dag] = (1/N_c)|Tr G|^2 + 2 sum_A |Tr[G t^A]|^2 = S + C` (runner §A,
reproven for `N_c = 2,3,4,5`). The reflection is a theory property, not an
assumption: the massive staggered operator obeys `eps`-hermiticity
`D_m^dag = eps D_m eps` (`eps(x) = (-1)^{sum_mu x_mu}`), so
`G = D_m^{-1}` obeys `G^dag = eps G eps`, i.e.
`G(y,x)_color = eps(x) eps(y) G(x,y)_color^dag` (runner §B', verified on a real
random-SU(3) background; this is the same reflection the RCONN MC and the
Fierz/traceless-generator notes use). This connected-correlator expression is the
one the landed traceless-generator no-go records. So the **bare object** the
ensemble computes is the full color trace `S + C`, and `Tr_color[G G^dag]` is
invariant under `G -> Omega(x) G Omega(y)^dag`, so `<T> = <S> + <C>` is a genuine
gauge-invariant number.

**This pins the object but not the readout.** Reading the physical running
coupling off the bare correlator requires a continuum scheme choice:

- `kappa_EW = 1`: retain the full trace `S + C` — the exact connected correlator;
- `kappa_EW = 0`: subtract the `O(1/N_c^2)` color-singlet channel `S` — the
  OZI / planar / leading-`N_c` truncation (equivalently the traceless projection
  `G - (Tr G / N_c) I`, runner §D).

**Neither completion is forced by the color-blindness of the current.** A
multiplicative color-scalar (`Z I_color`) renormalization scales `S` and `C` by
the same `|Z|^2` (runner §D), leaving `R_conn = C/T` invariant — it selects
neither completion. A more general dressed two-current kernel can carry
independent singlet and adjoint projectors, but their coefficients are equally
unfixed by color-blindness alone (color-blindness is agnostic to the channel
weights). This is the same color-blindness the matching-rule no-go §2 identified:
it does **not** fix `kappa_EW`. The singlet channel is also not removable by
tracelessness of the generator: for `Q_EW = T_3`, `M = I_color`, the loop is
entirely singlet (`S = N_c`, `C = 0`) with weight `Tr(T_3^2) = 1/2 != 0`
(runner §B4, the landed counterexample).

`kappa_EW = 0` is an active singlet projection (a non-color-blind operation);
`kappa_EW = 1` is the identity readout (retain the full trace). Selecting which
the physical coupling uses is an external continuum scheme choice either way; the
lattice current and its color-blind renormalization privilege neither. The note
does not select between them.

## 4. Consequence (symmetric; sin^2(theta_W) survives)

- `kappa_EW` is a continuum renormalization-scheme weight (which channels the
  matched physical EW coupling retains), structurally not Monte-Carlo-decidable
  and not fixed by the framework's primitives. Both the full-trace (`kappa_EW = 1`)
  and singlet-subtracted (`kappa_EW = 0`) readouts are admissible scheme choices;
  neither is privileged by any lattice measurement.
- The framework's published `sqrt(9/8)` on `g_1, g_2` and the reciprocal
  `sqrt(8/9)` on `y_t`/`m_t` (the `kappa_Y` twin) are the singlet-subtracted
  (`kappa_EW = 0`) specialization — a legitimate but underived scheme choice,
  exactly the status the four landed no-gos hold. The full-trace (`kappa_EW = 1`)
  alternative gives `K_EW = 1` (no projection), under which the absolute
  `g_1, g_2, alpha_EM` shift by `~5%` and `m_t` by `-0.07% -> +5.5%`, together
  (contextual comparators, not derivation inputs).
- `sin^2(theta_W)` is `kappa_EW`-invariant: both `g_1` and `g_2` carry the same
  `sqrt(K_EW(kappa_EW))`, which cancels in the ratio (runner §F). It survives
  either completion and is **not** at stake.

This note does **not** claim either `kappa_EW` value is forced, nor that the
framework is falsified. It states that the readout weight is an external scheme
choice the lattice does not fix, and that no Monte-Carlo measurement can decide
it. The `O(1/N_c^2)` singlet is the OZI channel: conventional treatments differ
on whether the physical coupling retains it (exact connected correlator) or drops
it (OZI/planar truncation), which is precisely why neither value is privileged.

## 5. What this closes and what it leaves open

**Closed (on the support surface, runner-reproven):**

- The object `kappa_EW` weights is pinned: the bare connected EW correlator
  `= Tr(Q_EW^2)(S + C)`, the full color trace. The readout weight `kappa_EW` is a
  separate, external functional.
- `R_conn = 8/9` is a `beta`-independent gauge-orbit / `O(1/N_c^2)` fraction, not
  a continuum coupling renormalization with a `beta`-trend.
- Color-blindness fixes neither completion; both `kappa_EW = 0` and `kappa_EW = 1`
  are external scheme choices.
- `kappa_EW` is structurally not Monte-Carlo-decidable.

**Left open (the irreducible residual):**

- The continuum renormalization condition that would select whether the matched
  physical coupling retains (`kappa_EW = 1`) or subtracts (`kappa_EW = 0`) the
  color-singlet channel. This is a scheme choice external to the lattice; the
  framework's numbers assume the singlet-subtracted scheme without deriving it,
  and the full-trace scheme is equally available and equally underived.

## 6. No-Go Discipline Gate

Scope of the no-go: Monte-Carlo data from the retained color-blind EW-current
packet do not select the readout coefficient `kappa_EW`. This does not claim
that no future continuum readout theorem, convention, or additional matching
principle could select a value.

- **N1 alternative routes tested.** Direct full-correlator measurement fixes
  `<T>` but not the readout `C + kappa_EW S`; channel-split measurement fixes
  the gauge-orbit fractions but not their physical weight; generator
  tracelessness fails by the retained traceless-generator no-go and the
  `M = I_color` counterexample; OZI/large-`N_c` fixes only the size class; a
  color-scalar renormalization scales `S` and `C` together and selects neither
  completion.
- **N2 wall collapse.** The collapsed wall is one residual: the readout
  functional is not supplied by the ensemble or by the retained current packet.
  The object pin and the `1/N_c^2` gauge-orbit fraction are support facts, not
  separate admissions.
- **N3 hidden-wall scan.** The load-bearing phrases are explicit: "color-blind"
  cites the landed EW-current packet, "external scheme choice" is the residual
  left by the retained no-gos, and "Monte-Carlo" means ensemble data for the
  stated lattice-current object.
- **N4 residual matching.** The cited retained no-gos attack the same residual:
  failure to derive the connected-trace selector `kappa_EW = 0` or any
  framework-native readout coefficient from the retained packet.
- **N5 rhetoric audit.** "Not Monte-Carlo-decidable" is only the
  ensemble-data/readout-coefficient statement above; it is not a claim about
  every possible future continuum matching theorem.
- **N6 partial-closure scan.** A retained theorem supplying the continuum
  readout functional, or an explicitly approved convention fixing it, would
  reopen and could retire this no-go. No currently registered axiom, primitive,
  Record readout baseline, or scale-reference primitive supplies that selector.
- **N7 steelman.** A hostile reviewer could say the physical coupling is defined
  by a continuum renormalization condition, and that condition might naturally
  choose the exact full trace or the OZI/planar subtraction. That is a real
  route, but it is outside the Monte-Carlo-data claim and is listed as the
  reopen condition rather than ruled out here.
- **N8 cross-cycle echo.** The older `RCONN_DERIVED_NOTE`,
  `EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03`, and
  `EW_CURRENT_TRACELESS_GENERATOR_SELECTOR_NO_GO_NOTE_2026-05-03` already caught
  the same overclaim shape: exact color algebra plus MC agreement does not fix
  the physical readout coefficient. This note preserves that boundary while
  pinning the bare object more explicitly.

Gate result: **PASS for the scoped no-go only**.

## 7. Reopen conditions

Promote either `sqrt(9/8)` (`kappa_EW = 0`) or the no-projection (`kappa_EW = 1`)
factor to derived only with a retained-grade theorem that supplies the continuum
readout functional from accepted primitives (a framework-native EW-current
matching whose continuum coupling mechanically retains or subtracts the singlet
channel). Until then, downstream uses of `sqrt(9/8)` and `sqrt(8/9)` are the
conditional `kappa_EW = 0` specialization, and the EW absolute normalization must
be written as scheme-conditional.

## 8. Verification

```bash
python3 scripts/frontier_ew_kappa_self_energy_object_pin.py
```

The runner reproves, with zero PDG inputs: (A) the SU(`N_c`) Fierz identity for
`N_c = 2,3,4,5`; (B) the color-blind connected loop `= Tr(Q^2)(S+C)` (the object)
and the singlet-carries-`Tr(Q^2)` counterexample; (B') the staggered
`eps`-hermiticity reflection `G^dag = eps G eps` on a real random-SU(3)
background; (C) the gauge-orbit-average identity `<S>/<T> = 1/N_c^2` for an
arbitrary dressed `M` (Weingarten), with free+random-gauge and Haar cross-checks
(kinematic, `beta`-independent); (D) color-blindness selects neither completion —
`kappa_EW = 0` (active singlet projection) and `kappa_EW = 1` (identity readout)
are both external scheme choices; (E) the structural MC-undecidability of
`kappa_EW`; (F) `sin^2(theta_W)` `kappa`-invariance. Expected:
`RUNNER STATUS: PASS (PASS=20 FAIL=0)`.

## 9. Safe wording

**Can claim:**
- "The object `kappa_EW` weights is the bare connected EW correlator, which
  computes the full color trace `S + C`; the readout weight is separate."
- "`R_conn = 8/9` is a `beta`-independent gauge-orbit singlet fraction, not a
  continuum coupling renormalization."
- "`kappa_EW` is not Monte-Carlo-decidable; it is a continuum scheme choice, and
  both `kappa_EW = 0` and `kappa_EW = 1` are external to the lattice primitives."
- "The EW absolute normalization is scheme-conditional; `sin^2(theta_W)` is
  `kappa_EW`-invariant and survives."

**Cannot claim:**
- bare `retained` / `promoted`.
- "`kappa_EW = 1` is the standard/natural output" or "`kappa_EW = 0` is
  non-standard / falsified." (Both are admissible scheme choices; neither is
  privileged by the lattice or the MC.)
- "This derives the matching rule" or "this closes the `9/8` factor."
- "The MC settles `kappa_EW`." (It does not — that is the no-go.)
