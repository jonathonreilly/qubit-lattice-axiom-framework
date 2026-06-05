# Fourth-Axiom Scoping — Self-Consistency / Gap-Equation Dynamics for the Generation Yukawa Moduli

**Date:** 2026-06-05
**Claim type:** meta (scoping exploration; no theorem promotion, no axiom adoption)
**Status authority:** independent audit lane only; effective status is pipeline-derived.
**Source-note proposal disclaimer:** this is a source-note proposal; audit
verdict and downstream status are set only by the independent audit lane.
**Owner authorization:** explicit owner-authorized *exploration* of a candidate
4th axiom (self-consistency / dynamical mass generation). This note **scopes**
the candidate; it does **not** adopt it, and adopting any new axiom or import
requires separate explicit owner approval.
**Primary runner:** [`scripts/cl3_fourth_axiom_self_consistency_2026_06_05.py`](../scripts/cl3_fourth_axiom_self_consistency_2026_06_05.py) (16/16 PASS)
**Cached output:** [`logs/runner-cache/cl3_fourth_axiom_self_consistency_2026_06_05.txt`](../logs/runner-cache/cl3_fourth_axiom_self_consistency_2026_06_05.txt)

## Question

A1/A2/A3 carry **no dynamics**. The per-sector generation Yukawa is the
C₃-equivariant Hermitian circulant on the hw=1 generation triplet

```
Y = a I + b C + conj(b) C²,   C = cyclic shift, C³ = I,   (3 real dof: a, |b|, δ=arg b)
```

with the single flavor **modulus** `r = |b|²/a²` and `Q = 1/3 + (2/3) r`
(retained: L6 of [CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md),
via the κ / block-Frobenius isotype split). `r` is a free input on the current
surface. **Candidate 4th axiom:** a self-consistency condition (NJL gap
equation / Schwinger-Dyson / fixed point of a mass-generation map) on the qubit
lattice, à la dynamical chiral symmetry breaking, that fixes `Y` dynamically.

**The honest question.** Gap equations break a symmetry and generate a **scale**
from a coupling (dynamical transmutation). Do they fix the **ratio** `r`, or
only `|Y|`? Two honesty bars are enforced:
- **BAR 1 (generic values).** Does the self-consistent solution reproduce the
  *observed* moduli (`r_lep≈0.500`, `r_down≈0.597`, `r_up≈0.772`, `r_ν<0.5` —
  observational comparison only), or only special values? (`r=1/2` is not forced.)
- **BAR 2 (relocation).** Does the gap equation carry a coupling (an input)?
  Count inputs vs outputs.

## What `r` is (and why it matters for a gap equation)

`r` is the **Frobenius power-balance ratio between the two C₃ isotype blocks** of
the circulant algebra (verified in runner Part 0):

```
singlet block  R⟨I⟩            : ‖a I‖²_F          = 3 a²
doublet block  R⟨C+C²⟩, R⟨i(C-C²)⟩ : ‖b C + conj(b) C²‖²_F = 6 |b|²
=>  (doublet power)/(singlet power) = 2 r        =>  Q = 1/3 + (1/3)·(doublet/singlet).
```

So `r` is a **ratio of magnitudes across two isotypes**, not an overall scale.
It is **degree-0 homogeneous** in `(a,b)` (and in the Fourier eigenvalues):
scaling `(a,b) → κ(a,b)` leaves `r` invariant. A dynamics that fixes only the
overall magnitude `|Y|` therefore *cannot* fix `r` — proven symbolically (Parts
0, 6).

## The spine: C₃ equivariance diagonalizes the gap equation per mode

Diagonalize `C` (eigenvalues `1, ω, ω²`, `ω=e^{2πi/3}`). A C₃-equivariant `Y` is
simultaneously diagonal with Fourier eigenvalues
`λ₀=a+2Re b`, `λ₁=a+2Re(bω)`, `λ₂=a+2Re(bω²)`. A C₃-equivariant self-energy
`Σ = a_Σ I + b_Σ C + conj(b_Σ) C²` obeys a gap equation that, **by equivariance,
is diagonal in the same Fourier basis** (verified symbolically, runner Part 1):

```
λ_k = G · g(λ_k ; mode-data of channel k),   k = 0, 1, 2.
```

Three **decoupled scalar gap equations**, one per Fourier mode. `r` is a function
only of the *spread* of `{λ_k}`. This is the decisive structural fact.

## Results (runner)

**Mode-blind dynamics (genuinely C₃-symmetric kernel — same `g`, same `G` for
every mode).** The three scalar gap equations are identical, so
`λ₀=λ₁=λ₂ ⇒ b=0 ⇒ r=0 ⇒` spectrum `[1,1,1]`, `Q=1/3`. Using the canonical 3+1
NJL gap equation `1 = G·I(λ)` (Hatsuda–Kunihiro form, hard cutoff `Λ`), the
runner confirms a nontrivial **scale** is generated and tracks the coupling
(`G=50 → λ*=0.285`; `G=80 → λ*=0.640`; `G=120 → λ*=0.945`) — textbook dynamical
transmutation — while `r` stays exactly `0` for **every** `G`. This matches the
retained endpoint fact (L8): `r=0 → [1,1,1]` degenerate. **FIXES-SCALE-NOT-MODULUS.**

**Mode-dependent dynamics (per-channel coupling `G_k`).** The runner reaches
**any** target `r` — including each observed value — by tuning a single extra
dial `G₁=G₂≠G₀`:

| sector | target `r` | tuned `G₁=G₂` (`G₀=60`) | self-consistent `r` |
|--------|-----------|--------------------------|---------------------|
| lep    | 0.500     | 40.119                   | 0.5000              |
| down   | 0.597     | 39.859                   | 0.5970              |
| up     | 0.772     | 39.590                   | 0.7720              |
| ν      | 0.300     | 41.157                   | 0.3000              |

Each independent `G_k` is a **new input**. The per-mode coupling pattern carries
exactly 3 dials `(G₀,G₁,G₂) ↔ {scale, |b|, δ}` — as many as the flavor dof
produced. **RELOCATION**, not derivation.

**BAR 1 (a natural, un-tuned kernel?).** The most principled non-tuned mode
weighting that adds no per-mode coupling is the isotype **real-dimension `(1,2)`**
weight on `(singlet, doublet)` — the same `(1,2)` count the free-Gaussian measure
analysis already pins (Probe 25/28 lineage). It yields a **coupling-dependent**
`r` (`r(G=60)=0.050` vs `r(G=120)=0.022`), i.e. not a pure number, and one fixed
weighting gives one `r` — it cannot be the three distinct observed sector moduli.
**No natural un-tuned kernel reproduces the generic observed moduli.**

**Decisive identity (Part 6).** Modeling the homogeneous transmutation as
`λ_k = G_k·c`: the overall scale `s=(λ₀λ₁λ₂)^{1/3}` absorbs a common coupling
rescaling, leaving every ratio `x_k=λ_k/s` — and hence `r` — **invariant**
(symbolic). The overall coupling fixes `|Y|`; `r` is set purely by the coupling
**spread** across modes, which is the new flavor input.

## Verdict

**FIXES-SCALE-NOT-MODULUS** (mode-blind) **/ RELOCATES-to-coupling**
(mode-dependent).

A 4th self-consistency axiom of NJL / gap-equation type supplies the missing
mass **scale** (dynamical transmutation) but does **not**, on its own, fix the
generation flavor **modulus** `r`. The modulus stays free under dynamical mass
generation unless a **new per-mode (flavor) input** is adjoined. This is fully
consistent with the retained no-go that the singlet:doublet isotype ratio is free
([KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md), retained_no_go),
and with the existing NJL-style `V_eff` finding that chiral SSB generates a
condensate scale `σ`, not a ratio
([V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md](V_EFF_TOTAL_NJL_STYLE_BOUNDED_THEOREM_NOTE_2026-05-10.md)).

This **does not close** the modulus question. The residual is sharpened: the gap
equation is **orthogonal** to the `r`-selection problem — it supplies the scale
the `r=1/2` bridge candidates (L9: equipartition / max-entropy / records-flow
separatrix on the two isotype blocks) leave open, and leaves open the ratio they
address. A 4th axiom that fixes the modulus must act on the **doublet/singlet
power balance** (the coupling spread), not on the overall magnitude — a
fundamentally different object than dynamical mass generation provides.

## Scope / non-claims
- Scoping only. No axiom is adopted; no import is taken. No PDG value is a
  derivation input (observed moduli appear only as end comparisons).
- Does not promote, retag, or set status for any row. Does not load-bear on any
  retained theorem; it *reinforces* an existing retained no-go from a new angle.
- The NJL kernel used is an illustrative toy (single four-fermion channel, hard
  cutoff); the structural conclusions (per-mode diagonalization, degree-0
  homogeneity of `r`, input=output count) are kernel-independent and proven
  symbolically — they hold for any C₃-equivariant self-consistency map.
