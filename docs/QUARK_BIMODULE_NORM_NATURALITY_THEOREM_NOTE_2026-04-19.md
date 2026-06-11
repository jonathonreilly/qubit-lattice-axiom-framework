# Quark Bimodule NORM-Naturality Theorem

**Date:** 2026-04-19  
**Type:** bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)
**Admitted context inputs:** staggered-Dirac realization derivation target (canonical parent: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`).
**Lane:** Quark up-amplitude / bimodule LO closure  
**Status:** support - structural or confirmatory support note
bimodule structural conditions (complementarity, endpoint normalization,
affine naturality) above the previously retained quark packet and shows that
BICAC is the unique normalized affine extension of the LO split law under
those three conditions. The three conditions are named explicitly in §0
below and are not themselves derived on this branch — they are the cost of
this particular strengthening. **After the same-day
JTS-affine-physical-carrier theorem
(`docs/QUARK_JTS_AFFINE_PHYSICAL_CARRIER_THEOREM_NOTE_2026-04-19.md`) and
ISSR1 forcing, NORM-Naturality is no longer load-bearing for the Quark
closure** — it is a structurally stronger follow-on statement about the
full ownership interval, not a required input for BICAC-LO at the physical
point.  
**Primary runner:** `scripts/frontier_quark_bimodule_norm_naturality_theorem.py`

---

## 0. Executive summary

The same-day NORM-existence theorem shows that the exact bridge family already
lifts to actual complementary bimodule maps on the one-real imaginary channel
`I = R * Im(p)`. That answers the binary existence question with **yes**, but
still leaves a family of candidate split laws.

This note identifies the exact extra structure that collapses that family.

Let `a in [0,1]` denote a generic scalar ownership parameter and let

```text
D_a, U_a : I -> I
```

be the down-sector and up-sector split maps.

Assume three conditions:

1. **Complementarity**

   ```text
   D_a + U_a = Id_I.
   ```

2. **Endpoint normalization**

   ```text
   D_0 = 0,
   D_1 = Id_I.
   ```

3. **Affine naturality in the ownership parameter**

   ```text
   D_{t a + (1-t) b} = t D_a + (1-t) D_b.
   ```

Because `I` is one-real-dimensional, every endomorphism of `I` is scalar
multiplication. Using

```text
a = a * 1 + (1-a) * 0,
```

affine naturality immediately gives

```text
D_a = a D_1 + (1-a) D_0 = a Id_I,
U_a = (1-a) Id_I.
```

At the physical retained point `a = rho = Re(r)`, this is exactly

```text
a_u = U_rho(Im(p)) = Im(p) * (1-rho),
```

so

```text
a_u + rho * Im(p) = Im(p),
```

i.e. BICAC / STRC-LO.

So the quark gap is now sharper:

> the remaining question is no longer "is BICAC just a random endpoint?"

It is:

> can normalized affine NORM naturality itself be derived from retained
> quark-side physics, rather than added as extra bimodule structure?

---

## 1. Setup

Retained quark channel:

```text
I = R * Im(p),
Im(p) = sin_d = sqrt(5/6),
rho = Re(r) = 1 / sqrt(42).
```

From the NORM-existence theorem, the support, target, and BICAC profiles are
all real complementary split laws at the physical point `a = rho`.

But only one of them can extend to a normalized full-interval ownership law on
all `a in [0,1]`.

---

## 2. The theorem

### Formal statement

> **Theorem (NORM naturality uniquely yields BICAC).** Let
> `I = R * Im(p)` be the one-real imaginary channel on the retained CKM ray.
> Suppose a family of real-linear split maps
>
> ```text
> D_a, U_a : I -> I,   a in [0,1],
> ```
>
> satisfies:
>
> 1. `D_a + U_a = Id_I` for all `a`;
> 2. `D_0 = 0` and `D_1 = Id_I`;
> 3. `D_{t a + (1-t) b} = t D_a + (1-t) D_b` for all `a, b, t in [0,1]`.
>
> Then necessarily
>
> ```text
> D_a = a Id_I,
> U_a = (1-a) Id_I.
> ```
>
> In particular, at the retained physical point `a = rho`,
>
> ```text
> U_rho(Im(p)) = Im(p) * (1-rho),
> ```
>
> hence
>
> ```text
> a_u + rho * Im(p) = Im(p),
> ```
>
> which is BICAC / STRC-LO.

### Proof

Because `I` is one-real-dimensional, `End_R(I) = R * Id_I`.

Now write

```text
a = a * 1 + (1-a) * 0.
```

Applying affine naturality with `b = 0` and `t = a`,

```text
D_a = D_{a * 1 + (1-a) * 0}
    = a D_1 + (1-a) D_0
    = a Id_I + (1-a) * 0
    = a Id_I.
```

Then complementarity gives

```text
U_a = Id_I - D_a = (1-a) Id_I.
```

Evaluating at `a = rho` and `Im(p) = sin_d` gives

```text
U_rho(Im(p)) = sin_d * (1-rho),
```

so

```text
U_rho(Im(p)) + rho Im(p) = sin_d.
```

That is exactly BICAC / STRC-LO. QED.

---

## 3. Why the support and target profiles fail this theorem

The two non-BICAC constant-`kappa` bridge profiles extend naturally to

```text
D_a^(kappa) = kappa a Id_I.
```

These are still affine in `a`, but endpoint normalization fails unless
`kappa = 1`:

```text
D_1^(kappa) = kappa Id_I.
```

So:

- support profile gives `D_1 = sqrt(6/7) Id_I != Id_I`;
- target profile gives `D_1 = (48/49) Id_I != Id_I`;
- only BICAC gives `D_1 = Id_I`.

That is the clean mathematical reason BICAC is the unique normalized affine
extension.

---

## 4. Scientific consequence

This theorem does **not** claim reviewer-grade closure. The added content is
still a bimodule-level naturality principle, not a derivation from already
retained quark observables alone.

But it materially improves the quark status:

1. the branch no longer stops at "BICAC is a postulate";
2. BICAC is now identified as the unique normalized affine extension of the LO
   split law on the full ownership interval;
3. the remaining caveat is therefore narrower:

   ```text
   derive NORM normalization / naturality from retained quark-side physics.
   ```

That is a materially sharper and more defensible target than the earlier vague
"derive BICAC somehow."

---

## 5. Relation to the rest of the quark packet

After the same-day quark sequence, the current status is:

1. **NORM existence:** yes  
   `docs/QUARK_BIMODULE_NORM_EXISTENCE_THEOREM_NOTE_2026-04-19.md`

2. **Unique normalized affine extension:** yes  
   this note

3. **Pure retained-packet endpoint derivation:** no  
   `docs/QUARK_BICAC_ENDPOINT_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md`

4. **Quark target closure on bimodule footing:** yes  
   `docs/STRC_LO_COLLINEARITY_THEOREM_NOTE_2026-04-19.md` and
   `docs/QUARK_UP_AMPLITUDE_RPSR_CONDITIONAL_THEOREM_NOTE_2026-04-19.md`

So the branch now brackets the quark science very tightly:

- existence is settled;
- natural normalized extension is settled;
- reviewer-bar caveat is isolated to deriving that naturality from the retained
  physics packet.

---

## 6. Runner summary

The companion runner verifies:

- complementarity of the canonical family;
- endpoint normalization;
- affine naturality on a sample grid;
- exact derivation `D_a = a Id_I`;
- exact BICAC / STRC-LO at the physical point `a = rho`;
- failure of endpoint normalization for the support and target profiles;
- uniqueness of the BICAC profile among constant-`kappa` extensions.

Expected runner status:

```text
PASS=8
FAIL=0
```


## Hypothesis set used (axiom-reset 2026-05-03)

Per `MINIMAL_AXIOMS_2026-05-03.md`, this note depends on the **staggered-Dirac realization derivation target**, which is currently an open gate. The note's load-bearing claim defines or relies on fermion fields, fermion-number operators, fermion correlators, fermion bilinears, the staggered Dirac action, the BZ-corner doubler structure, the `hw=1` triplet, charged-lepton sector content, neutrino sector content, quark / hadron content, the Koide / PMNS / CKM observable surfaces, or the Grassmann CAR boundary structure — all of which depend on the staggered-Dirac realization derivation target listed in `MINIMAL_AXIOMS_2026-05-03.md`.

Canonical parent note: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (`claim_type: open_gate`). In-flight supporting work (see `MINIMAL_AXIOMS_2026-05-03.md`):

- `PHYSICAL_LATTICE_NECESSITY_NOTE.md`
- `THREE_GENERATION_STRUCTURE_NOTE.md`
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`
- `scripts/frontier_generation_rooting_undefined.py`
- `GENERATION_AXIOM_BOUNDARY_NOTE.md` (preserved)

Therefore `claim_type: bounded_theorem` until that gate closes. When that gate closes, the lane becomes eligible for independent audit/governance retagging as `positive_theorem`; the audit pipeline recomputes `effective_status`, but it does not silently invent a new `claim_type`. The substantive science content of this note is unchanged by this retag.

## Registered Tier-A routing (2026-06-11; audit-requested repair)

The recorded conditional-audit repair target for this row is
`dependency_not_retained` on the staggered-Dirac realization gate. This
section takes the precedented registered-routing form of that repair
(per `PMNS_TWISTED_FLUX_TRANSFER_HOLONOMY_BOUNDARY_NOTE.md` and
`YT_WARD_IDENTITY_DEPENDENCIES_REGISTERED_BOUND_NARROW_THEOREM_NOTE_2026-06-05.md`,
plain-text precedent pointers): the carrier admission is routed
explicitly into the **registered Tier-A derivation target**, so the
citation graph carries a registered admission rather than an
unregistered conditional blocker.

1. **The algebra is standalone.** The NORM-naturality uniqueness is pure bimodule structural algebra:
under the three named structural conditions (complementarity, endpoint
normalization, affine naturality) the normalized affine extension of
the LO split law is unique; no carrier input enters the uniqueness
proof.
2. **What the carrier admission carries.** Only the identification of the bimodule structure and the physical LO
point with the staggered-Dirac quark sector consumes the realization
(the three structural conditions themselves remain premises exactly as
stated in this note).
   That naming is the admitted context input this row declares.
3. **The admission is a registered Tier-A target.** The canonical
   parent `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` is the
   registered Tier-A derivation target `AC_phi_lambda` (display
   `AC_φλ`) in the admission registry
   (`docs/audit/data/tier_a_admissions.json`). This note
   routes the carrier naming **into** that registered target; it does
   **not** close the gate. Under the published chain rule
   (`docs/audit/scripts/compute_effective_status.py`), a clean
   `bounded_theorem` row whose only non-retained, non-axiom one-hop
   dependency is a registered Tier-A derivation target is a candidate
   for the Tier-A-bounded class rather than an unregistered
   conditional blocker.
4. **No status assertion.** This section makes the narrow re-audit
   case only. The audit lane is the sole authority for audit status and
   effective status; this note asserts no `effective_status` and
   predicts no audit outcome.


## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
