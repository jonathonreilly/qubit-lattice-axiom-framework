# The charged-lepton carrier import is TWO bits on the retained tier, ONE only modulo auditing named spin-statistics rows

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** a bit-count audit of the charged-lepton **carrier** import
(the statistics posit and the faithfulness posit). It pins the count on the
strict-retained tier and on the optimistic (collapse-granted) tier, and names
the exact ledger rows whose status flips the count from two to one. It does
**not** re-derive the faithful=>CAR collapse physics (that is
`KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01`), does **not** audit or
promote any row, does **not** touch the separate VALUE bit (the
2-sector/partition `r=1/2` choice), does **not** derive `Q=2/3`, and does
**not** set an audit verdict.
**Primary runner:**
`scripts/frontier_koide_carrier_bit_count_is_two_on_retained_one_modulo_audit.py`
with cache
`logs/runner-cache/frontier_koide_carrier_bit_count_is_two_on_retained_one_modulo_audit.txt`
(SCORECARD PASS=16, including a live `origin/main` ledger read of the five
tier-determining rows).

## The question

The charged-lepton carrier reduces (per
`KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01` and
`KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01`) to two scoped-frame
posits on the matter operator `M`:

- **STAT** — *statistics*: the cross-site frame is fermionic/CAR rather than the
  hard-core boson (the sign of the hopping bilinear `c_x^† c_y`).
- **FAITH** — *faithfulness*: matter sits in the boost-acting faithful Weyl rep
  rather than the trivial scalar `J=K=0`.

The capstone reading fuses these to **one** bit via the conditional collapse
"faithful spin-½ ⟹ CAR" (`KOIDE_P1_COLLAPSES_FRAME_RESIDUALS`: Bose-quantizing
a faithful Dirac mode is unbounded below, so CAR is the unique positive-energy
quantization). This note asks the narrow accounting question the capstone leaves
implicit: **on the strict-retained tier, is the carrier import one admission or
two?**

## Result: TWO on strict-retained; ONE only modulo auditing three named rows

**(1) The collapse direction "faithful ⟹ CAR" is correct physics but is NOT
retained-load-bearing.** Given a faithful spin-½ Weyl rep the Dirac spectrum is
`±E`; a bosonic occupation of the negative-energy mode drives `min H → −∞`,
while CAR is bounded (`H ≥ 0`). That argument is sound and non-circular, but on
the citation graph it is carried by the **plain-text-only** rows

- `axiom_first_spin_statistics_theorem` (effective_status **unaudited**,
  criticality `critical`),
- `free_field_os_wightman_reconstruction` (effective_status **unaudited**),
- `free_sector_spin_statistics_level1` (effective_status **unaudited**),

none of which is a load-bearing dependency edge of any note that performs the
collapse (verified against the live ledger by the runner). So the collapse
exists only **modulo independent audit** of those three rows.

**(2) The retained surface does NOT exclude the hard-core boson — so STAT and
FAITH are independent there.** The only retained statistics authorities are:

| row | effective_status | what it forces | does it exclude the hard-core boson? |
|---|---|---|---|
| `spin_statistics_cardinality_pauli_exclusion` | **retained** | `[a,a†]=I` needs `dim=∞` (`Tr[a,a†]=0≠D`) | **No** — kills only the *free/CCR* boson; `b=σ₊` has `[b,b†]` traceless, evades it |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing` | **retained_no_go** | nothing — it *proves* the baseline does not force fermions | **No** — it is the no-forcing result itself |
| `spin_statistics_berezin_determinant` | **retained_bounded** | `Z_F=det M` + exchange sign **given Grassmann generators** | **No** — Grassmann anticommutation is an explicit *hypothesis* |
| `area_law_majorana_car_fock_equivalence` | **retained** | Clifford-Majorana ⇔ CAR-Fock on `C⁴` **given** `{γ_i,γ_j}=2δ_ij` | **No** — presupposes the anticommuting structure |

On a single site the fermion `c` and the hard-core boson `b` are *literally the
same* matrix `σ₊` (`{c,c†}=I` and `[b,b†]=diag(1,−1)` are both true of it), so
no retained row reaches the cross-site exchange sign. STAT therefore stays a
live, independent posit on the retained tier.

**(3) FAITH is independent of STAT regardless of tier — the scalar is
admitted.** Microcausality / reflection-positivity / positive-energy do **not**
force faithfulness: the trivial scalar `J=K=0` is a healthy free field
(`ω_k>0`, equal-time bracket vanishes spacelike, OS/Källén–Lehmann kernel PSD —
the canonical Glimm–Jaffe RP measure). A constraint whose own 2-point function
is RP cannot exclude the RP scalar. So FAITH never collapses *into* STAT from
the constraint side; the collapse runs the *other* way (FAITH ⟹ STAT), and only
modulo (1).

## The count, pinned

- **Strict-retained tier:** **TWO** independent admissions — `{STAT, FAITH}`.
  The retained inventory excludes only the free/CCR boson and admits the scalar;
  neither posit is derivable from the other on retained-only data.
- **Optimistic (collapse-granted) tier:** **ONE** admission — `{FAITH}` — and
  this count is *exactly* "one **modulo** auditing
  `axiom_first_spin_statistics_theorem`,
  `free_field_os_wightman_reconstruction`, and
  `free_sector_spin_statistics_level1`." The reduction is `FAITH ⟹ STAT`, never
  the reverse, and never to zero (the scalar survives every microcausality/RP
  constraint on a single matter field).

So the honest headline is **two-on-retained, one-modulo-audit** — *not* a clean
single bridge. The collapse is real physics, but until those three rows are
audited it does not contract the retained admission count, and a capstone that
reports "one carrier bit" is reporting the optimistic-tier count and silently
inheriting the three unaudited rows.

## Why this matters strategically (not just bookkeeping)

The two tiers route the next step to different objects:

- If the right count is **two**, the cleanest single move is to **audit the
  spin-statistics / OS-reconstruction step** (ratify
  `axiom_first_spin_statistics_theorem` S2 and close
  `free_field_os_wightman_reconstruction`'s open lattice↔continuum and
  `1+1d → 4D` gates). That one audit converts STAT into a *derived* consequence
  of FAITH and legitimately contracts the count to one.
- The residual that survives **either way** is **FAITH** (faithful-Weyl-over-
  scalar), and the note above shows it is untouched by the same
  microcausality/RP lever that admits the scalar — so FAITH must be pursued
  through `M`'s own spin content / the `so(3,1)` carrier assignment, a different
  front from the statistics audit.

Pinning the count keeps these two fronts from being conflated: "select the
hopping sign" (STAT, dischargeable by an audit) and "select faithful-over-
scalar" (FAITH, the lone irreducible carrier posit) are *different* admissions
on the strict tier, and only the first is retired by auditing the named rows.

## Non-circularity

`Q=2/3` never appears; no fermionic frame and no faithful rep is assumed. The
single-site `σ₊` identities, the cardinality trace obstruction, and the scalar's
RP/positive-energy facts are computed directly (runner). The ledger statuses are
read from the live `origin/main` ledger snapshot, not asserted. No
finite-enumeration / "only route" framing is used: this is a count at a fixed
tier, and auditing the named rows is one open path among others that could
contract it.

## Load-bearing authorities

[KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01.md](KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01.md),
[KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md](KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01.md),
[KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01.md](KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01.md),
[SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md),
and
[STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md).

Named audit targets whose status flips the optimistic count (kept as plain text
/ non-load-bearing, exactly as in the P1 note):
`axiom_first_spin_statistics_theorem`,
`free_field_os_wightman_reconstruction`, and
`free_sector_spin_statistics_level1`.

## Command

```bash
python3 scripts/frontier_koide_carrier_bit_count_is_two_on_retained_one_modulo_audit.py
```

Expected output: `SCORECARD PASS=16` (when run with `origin/main` reachable;
the five ledger checks read the live ledger snapshot).
