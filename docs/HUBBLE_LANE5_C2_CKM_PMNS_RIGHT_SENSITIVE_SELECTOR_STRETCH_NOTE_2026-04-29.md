# Lane 5 C2 supplied two-world sign countermodel

**Date:** 2026-04-29; correction 2026-10-21
**Type:** bounded_theorem
**Status:** conditional algebraic countermodel; physical realization remains open.
**Primary runner:** `scripts/frontier_hubble_lane5_c2_ckm_pmns_right_sensitive_selector_stretch.py`

Supply independent real numbers delta,q,a with delta nonzero and a>0, and a
fixed sign k in {-1,+1}. Define the even-data tuple

```
E(delta,q,a) = (delta^2+q^2, delta^2 q^2, a).
```

Consider two supplied worlds whose observable inputs are `(k,E)` and whose
targets are respectively `+a` and `-a`. Replacing delta by -delta leaves E
unchanged. Thus a single-valued function of `(k,E)` must give the same output
on both worlds and cannot recover both distinct targets. This is an exact
nonidentifiability result for the specified data map, with no physical model
required for the proof.

If one additionally supplies the rule `target=k*a`, exactly one of the two
worlds satisfies it. That rule restricts the supplied domain; it is not derived
from the even-data tuple. Independence of k and the target sign is a premise
of this countermodel, not a theorem about the CKM and PMNS sectors.

The previous runner's even-data function was explicitly a stand-in. It did
not reconstruct physical charged-sector matrices or demonstrate admissibility
of both worlds under all framework axioms. Hard-coding that a coupling law is
absent cannot prove its absence from the repository or from physics. Those
claims and the hard-coded status checks are withdrawn.

The physical obligations remain: construct actual admissible opposite-sheet
sources with the same measured inputs, establish the relevant response map,
and determine whether a cross-sector or right-frame law restricts them.
No H_0, Omega_Lambda, baryon asymmetry, physical selector impossibility, or
necessity of any particular new law follows here.

The [minimal A13 construction](DM_LEPTOGENESIS_PMNS_MINIMAL_A13_SHEET_SELECTOR_THEOREM_NOTE_2026-04-16.md)
and [CP-sheet bank note](DM_LEPTOGENESIS_PMNS_SELECTOR_BANK_CP_SHEET_BLINDNESS_THEOREM_NOTE_2026-04-16.md)
are historical motivation for this abstraction, not premises proving its
physical realization. Original source is recoverable at
`f24d17d97d372df977476e4a69674577f31af575` under the same paths.

The runner checks exact rational fixtures; the polynomial sign identity above
is the general proof. Failure returns nonzero. No source text or status label
is used as evidence of the mathematical conclusion.
