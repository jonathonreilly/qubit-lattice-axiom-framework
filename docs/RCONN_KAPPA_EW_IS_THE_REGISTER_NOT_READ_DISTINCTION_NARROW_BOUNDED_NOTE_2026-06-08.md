# The EW-Current Matching Rule κ_EW Is the Record Ontology's Register-Not-Read Distinction

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a matching-rule selector via the record ontology, conditional on
one named extension)
**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit verdict. Effective status is pipeline-derived after independent audit and
dependency closure.
**Primary runner:**
[`scripts/frontier_rconn_kappa_ew_register_not_read.py`](../scripts/frontier_rconn_kappa_ew_register_not_read.py)
**Cached log:**
[`logs/runner-cache/frontier_rconn_kappa_ew_register_not_read.txt`](../logs/runner-cache/frontier_rconn_kappa_ew_register_not_read.txt)
(TOTAL: PASS=10 FAIL=0)

## 0. The selector this supplies, and the untried frame

The retained no-go [`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) establishes the exact SU(N_c)
Fierz adjoint fraction `F_adj = (N_c²−1)/N_c²` (`= 8/9` at `N_c=3`) but leaves the **physical
EW-current readout selector `κ_EW` free**:

```text
R_phys(κ_EW) = F_adj + κ_EW·(1 − F_adj),    κ_EW=0 → 8/9 (octet/connected),  κ_EW=1 → 1 (total).
```

The no-go's reopen condition is "a … selector theorem … that fixes `κ_EW = 0` from accepted
primitives." It records that the frames it tried — CMT mean-field scaling and OZI suppression —
do **not** fix `κ_EW` (CMT scales both channels equally; OZI gives a size class, not an exact
coefficient). **One frame was never tried: the framework's *central* principle — the record
ontology (register-not-read; the `I/d` reference is an unregistered reconstruction).** This note
applies it and it selects `κ_EW = 0`.

**The matching rule is the register-not-read distinction.** In the Fierz operator basis the
connected/disconnected split is exactly the content/reference split: the disconnected singlet
channel **is** the `I/d`-trace (reference), the connected octet channel **is** the traceless
(registered) content. Register-not-read discards the reference → registers the octet → `κ_EW=0` →
`R_conn = (N_c²−1)/N_c²`. The crux — whether register-not-read formally governs the color
operator-trace channel — is the single named residual.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| `R_phys = F_adj + κ_EW(1−F_adj)`; `κ_EW` the free selector; CMT/OZI do not fix it | [`RCONN_DERIVED_NOTE`](RCONN_DERIVED_NOTE.md) | `retained_no_go` | the selector this supplies |
| exact Fierz `S+C` channel decomposition; `F_adj=(N_c²−1)/N_c²` (exact group theory) | [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md) | retained (decoration) | the exact structure |
| `N_c = 3` from spatial `d = 3` (`Z³`) | [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md), [`NATIVE_GAUGE_CLOSURE_NOTE`](NATIVE_GAUGE_CLOSURE_NOTE.md) | `retained` | fixes `N_c` |
| register-not-read: the `I/d` reference is an unregistered reconstruction (the realist-slip discipline) | [`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05`](RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md) | `meta` (audit-decided) | the selecting principle |

No PDG value is load-bearing. No new axiom, import, or vocabulary; `8/9` is the exact group-theory
`F_adj`, not a fit.

## 2. The connected/disconnected split is the content/reference split (exact)

For the quark propagator `G`, the q-q̄ two-point function decomposes by the SU(N_c) Fierz
completeness identity (exact, no expansion; runner `FIERZ_*`):

```text
Tr_color[G(x,y) G(y,x)] = (1/N_c)|Tr G|²  +  2 Σ_A |Tr[G t^A]|²  =  S  +  C.
```

In the orthonormal Fierz operator basis `{I/√N_c, √2 t^A}`:

- **`S = (1/N_c)|Tr G|²` is *exactly* the `I/√N_c`-component** — i.e. the color **trace**, the
  **`I/d` reference direction** in the operator algebra (runner `S_is_the_I_over_d_trace_reference`:
  `|⟨G, I/√N_c⟩|² = S`). This is the **singlet / disconnected** channel.
- **`C = 2 Σ_A |Tr[G t^A]|²` is the traceless (octet) content** — every `t^A` is traceless
  (runner `octet_generators_are_traceless_content`). This is the **adjoint / connected** channel.

So the EW-current connected/disconnected distinction is, channel-for-channel, the operator-algebra
content/reference distinction.

## 3. Register-not-read selects κ_EW = 0 → R_conn = (N_c²−1)/N_c²

The framework's record ontology is **register-not-read**: the realized **content** is registered;
the **`I/d` reference** is a *reconstruction*, not the registration (the realist slip is treating
the reference as the reality). Applied to the Fierz operator readout:

- the `I/d`-trace channel `S` is the reference → **not registered**;
- the traceless octet channel `C` is the realized content → **registered**.

The registered observable is therefore the octet (connected) channel only:

```text
κ_EW = 0    ⟹    R_conn = F_adj = (N_c²−1)/N_c²    (= 8/9 at N_c=3).
```

The runner confirms `κ_EW=0 → R_conn=8/9`, `κ_EW=1 → 1`, and that the **content fraction**
`dim(traceless)/dim(all) = (N_c²−1)/N_c²` equals `F_adj` — register-not-read selects exactly the
traceless-content fraction. The selection is **N_c-universal**: it yields `(N_c²−1)/N_c²` at every
`N_c` (runner `FAMILY_*`), so `8/9` is the `N_c=3` value of a structural law, not a coincidence.

This is the selector the no-go's CMT/OZI frames could not supply: CMT scales `S` and `C` equally
(it is reference-blind); register-not-read **distinguishes** them (reference vs content), which is
exactly what selecting `κ_EW` requires.

## 4. Scope — what this establishes, and the one named residual

**Establishes (exact / conditional):**
- The connected/disconnected (octet/singlet) Fierz split is exactly the content/reference
  (traceless/`I/d`-trace) split of the operator algebra.
- Register-not-read (registered content, unregistered `I/d` reference) selects `κ_EW = 0`, hence
  `R_conn = (N_c²−1)/N_c²`, `N_c`-universally.

**The single named residual (the crux, conditional):**
- Whether the framework's register-not-read principle — established for the central-sector / `I/d`
  density-matrix reference — **formally governs the color operator-trace channel `S`**. The
  identification is direct (the Fierz `I/√N_c` *is* the `I/d`-reference direction), and the
  discipline supports it, but the formal extension of register-not-read from sector weights to the
  color operator-trace is not separately proved here. With it, `κ_EW = 0` is a derivation; this note
  is therefore **bounded** on that extension.

**Does NOT establish (separate):**
- It does **not** re-derive the Fierz ratio (cited exact group theory) and does **not** touch the
  separate Route-2 `c_TE = −R_conn` bridge or the `ρ_E` readout.

## 5. Honest verdict

The EW-current matching rule the `RCONN_DERIVED` no-go left free — connected (`8/9`) vs total
(`1`) — is, structurally, the framework's own **register-not-read** distinction: the disconnected
singlet channel is the `I/d`-trace reference (unregistered) and the connected octet channel is the
registered content. Register-not-read therefore selects `κ_EW = 0` and supplies
`R_conn = (N_c²−1)/N_c²` (`= 8/9` at `N_c=3`), `N_c`-universally — the selector CMT/OZI could not
give. This is **bounded** on one named extension (register-not-read governing the color
operator-trace), not unconditional; but it converts "no accepted primitive fixes `κ_EW`" into "the
framework's central principle fixes `κ_EW = 0`, modulo a color-trace extension." It connects a
heavily-load-bearing EW/color wall to the record ontology.

## 6. No-Go Discipline Gate

**Status:** PASS for this bounded matching-rule selector. It does **not** claim an unconditional
derivation; it names the register-not-read color-trace extension as the residual.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| CMT mean-field scaling | RULED OUT (prior no-go) | reference-blind; does not fix `κ_EW` |
| OZI suppression | RULED OUT (prior no-go) | a size class, not an exact coefficient |
| register-not-read (record ontology) | SELECTS | `κ_EW=0 → (N_c²−1)/N_c²`; bounded on the color-trace extension |
| Route-2 `c_TE=−R_conn` bridge / `ρ_E` | OUT OF SCOPE | separate residuals |

**N2 — Wall-independence.** The Fierz ratio (exact), the `κ_EW` selector (this note), the Route-2
bridge, and `ρ_E` are independent; this note supplies only the `κ_EW` selector.

**N3 — Hidden-wall scan.** Uses only the exact Fierz `S=I/√N_c`-component identity, the traceless
octet, and the register-not-read principle; `8/9` is the group-theory `F_adj`, not fitted.

**N4 — Residual matching.** The residual named is exactly the register-not-read color-trace
extension, not a numerical gap.

**N5 — Rhetoric audit.** The claim is a *bounded* selection of `κ_EW=0` via register-not-read,
conditional on one named extension; not an unconditional theorem, not a numerology match.

**N6 — Partial-closure path scan.** The next step is the formal proof that register-not-read governs
the color operator-trace channel (the central-sector/`I/d` discipline extended to color). No new
axiom requested.

**N7 — Steelman.** A reviewer may hold the color-singlet is the *physical* (confined) sector, so it
should be registered (`κ_EW=1`). The split here is of the q-q̄ *correlator operator* (the
disconnected `|Tr G|²` piece), not the physical bound-state propagator; the disconnected/trace
channel is the `I/d`-reference direction, not the confined meson. The steelman correctly identifies
the residual as *which* notion of "singlet" register-not-read applies to — the named extension.

**N8 — Cross-cycle echo.** Consistent with the retained Fierz decomposition, the retained `N_c=3`
closure, and the retained-no-go `RCONN_DERIVED` (which it supplies a frame for, not overruled) — and
with the register-not-read record ontology.

## 7. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained / retained-no-go / meta
  rows plus textbook SU(N_c) Fierz algebra.
- **No PDG/fitted load-bearing input; no new transcendental.** `8/9` is the exact `F_adj`.

## 8. Command

```bash
python3 scripts/frontier_rconn_kappa_ew_register_not_read.py
```

Expected: `TOTAL: PASS=10 FAIL=0`. numpy + stdlib, deterministic, `N_c×N_c` color matrices
(memory-safe). The runner verifies the exact Fierz `S+C` decomposition (`N_c=2..5`), that `S` is the
`I/√N_c`-trace (reference) component and the octet is traceless content, the `κ_EW` algebra, that the
traceless-content fraction equals `F_adj`, and the `N_c`-universal selection
`R_conn=(N_c²−1)/N_c²`.
