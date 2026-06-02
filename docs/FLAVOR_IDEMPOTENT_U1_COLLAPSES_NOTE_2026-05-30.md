# Flavor — the flavor-U(1)-on-idempotents route collapses; C³=I no-go is narrower than stated; the ordering has no native indexing parameter

**Date:** 2026-05-30
**Claim type:** bounded negative (route collapses) + one refinement (no-go narrowed) + one honest negative (ordering not natively indexed).
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_idempotent_u1_collapses_2026_05_30.py` (SCORECARD PASS=4).
**Source:** 6-agent build `wf_561034c7` (map → 4 tests → adjudication).

## Question
A candidate route tested here: a derived continuous **flavor/horizontal U(1) on the singlet⊕doublet idempotent split**
(`P_s=J/3, P_d=I−J/3`) — *not* a rephasing of the generator `C`, so potentially dodging `C³=I` — that
orients `J_cs` (→ det_C → Q=2/3) **and** reproduces the ordering `r = 0.50(lep) < 0.60(down) < 0.77(up)`.

## Result — collapses three ways
The idempotent U(1) `U(φ,ψ)=e^{iφ}P_s+e^{iψ}P_d` is native (a polynomial in `C`) and is `diag(e^{iφ},e^{iψ},e^{iψ})`
in the C₃-Fourier basis — *same* phase on both doublet modes (vs a Hermitian b-rephasing, which needs
*opposite* phases). So it **commutes with `C`** and **genuinely dodges `C³=I`**. But:
1. **Inert by conjugation:** `[U,C]=0` ⇒ `U H U† = H` exactly (verified) for any circulant H — `b`, `r` unchanged. It pins nothing.
2. **The only nontrivial action is the one-sided chiral `H → H U†`**, which **breaks Hermiticity** (complex
   eigenvalues, killing the signed Brannen readout the closure rests on) with value set by the **free** angle
   ψ — and that chiral split **is exactly the grading blocked by retained `koide_z3_equivariant_anticommuting_no_go`** (the same generation-chirality import).
3. **The gauge-charge det_C route collapses to the forbidden move:** gluing the doublet into one charged
   complex field requires *opposite* charge on the `ω, ω̄` modes = a rephasing of `C` = the `C³=I`-forbidden
   operation. Equal charge (the genuine idempotent U(1)) selects nothing.

## The one refinement (worth recording)
**The `C³=I` obstruction is narrower than its blanket phrasing.** Step-4b reads as "no continuous doublet
U(1)"; precisely, it forbids *rephasing the generator `C`* (or, equivalently, the opposite-phase mode gluing).
A *distinct* U(1) — the idempotent one, which commutes with `C` — does dodge it. The obstruction is real but
specific; it is not a blanket ban on all doublet U(1)s.

## The honest negative on the ordering
The ladder `r = 0.500(lep) < 0.597(down) < 0.773(up) < 1.0(rank-1)` is **real and native** — it is a function
of the mass spectrum alone, scale-invariant, with no CKM/QCD contamination (CKM does not enter a
diagonal-mass Koide readout; only ratios matter). **But it has no native indexing parameter:**
- `|Q_em|` = `(1, 1/3, 2/3)` — **non-monotone** with r (leptons have the *largest* |charge| but the *smallest* r).
- color = `(1, 3, 3)` — **non-monotone** (down = up).
- Only "mass-dominance" tracks r, which is **tautological** with Q.

So the ordering does *not* hand us a new handle: there is no charge/color/Yukawa quantity *inside* the
generation C₃ algebra to index which sector gets which `r`. **The generation C₃ algebra is pure flavor** — the
charge/color/Yukawa structure lives on the spinor/color/Higgs factors, which are generation-blind. This is the
sharp, recurring reason: nothing internal to the generation factor can place the sectors on the ladder.

## Honest verdict
The flavor-U(1)-on-idempotents route — this symmetry-side candidate — **collapses** (inert-by-conjugation,
or the already-blocked chiral grading, or the `C³=I`-forbidden charge gluing). The `C³=I` no-go is *narrowed*
(useful), and the ordering is *real but unindexed* (honest negative). The two gates are unchanged and now
maximally sharp:
1. **`r=1/2` fixing** — the det_C-vs-det_R measure on the doublet (`J_cs` forced, orientation/measure free).
2. **the sector-selector** — what connects the (pure-flavor, generation-blind-decoupled) generation algebra to
   the charge/color/Yukawa factors so that each sector lands at its observed `r`.

Both require a *cross-factor* coupling between the generation algebra and the charge/scale factors — exactly
the connection the framework keeps showing is absent (generation-blindness). That is the precise, structural
statement of what the charged-lepton (and full charged-fermion) mass value is waiting on.

## Stale-citation flags
- Anchors: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded — the chiral grading the chiral action
  reduces to), `koide_c3_generator_rephasing_obstruction` (retained — now seen as *narrow*: forbids C-rephasing,
  not the idempotent U(1)), `three_generation_observable` (retained — the idempotents are native).
