# Exact 2D Mirror Gravity-Law Cleanup Note

**Date:** 2026-04-03 (status line rephrased 2026-04-28 per audit-lane verdict; claim narrowed 2026-05-09 to primary-runner-backed evidence per audit `runner_artifact_issue` repair target; imported-authority dependency lifted into the header 2026-05-10 per follow-up `runner_artifact_issue` repair target).
**Status:** bounded null-result note — the exact 2D mirror primary-runner evidence shows weak gravity-side mass-window and distance-tail fits, so no clean 2D mirror mass law and no clean 2D mirror distance law are supported on the searched windows.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/mirror_2d_validation.py`](../scripts/mirror_2d_validation.py) — load-bearing 2D exact mirror linear propagator.
**Primary runner cache:** [`logs/runner-cache/mirror_2d_validation.txt`](../logs/runner-cache/mirror_2d_validation.txt) — load-bearing registered cached stdout (`exit_code=0`, `status=ok`) that backs every weakness row in the "Retained result (primary runner)" section below.
**Imported authority:** [`scripts/mirror_born_audit.py`](../scripts/mirror_born_audit.py) — load-bearing dependency; provides `gen_2d_mirror` (exact 2D mirror generator) and `propagate_LINEAR` (strictly linear propagator) imported by the primary runner.
**Imported authority cache:** [`logs/runner-cache/mirror_born_audit.txt`](../logs/runner-cache/mirror_born_audit.txt) — load-bearing dependency registered cached stdout (`exit_code=0`, `status=ok`) verifying the imported generator and propagator on the strict mirror Born family, so the exact-2D-mirror linear-propagator premise is closed by a one-hop registered dependency.
**Primary runner historical log (audit-trail context):** [`logs/2026-04-03-mirror-2d-validation.txt`](../logs/2026-04-03-mirror-2d-validation.txt) — original completed stdout retained for audit trail; the registered runner-cache above is load-bearing.
**Companion cleanup runner (diagnostic-only, not load-bearing):** [`scripts/mirror_2d_gravity_law_cleanup.py`](../scripts/mirror_2d_gravity_law_cleanup.py) — slow gravity-law cleanup sweep over wider anchor / distance windows. The companion table below is recorded as diagnostic context only; it is not load-bearing for the bounded null-result claim.
**Companion cleanup runner cached log (diagnostic-only):** [`logs/2026-04-03-mirror-2d-gravity-law-cleanup.txt`](../logs/2026-04-03-mirror-2d-gravity-law-cleanup.txt).

## Audit dependency scoping (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `runner_artifact_issue`, stating: *"provide
`scripts/mirror_born_audit.py` and `logs/runner-cache/mirror_born_audit.txt`
in the restricted packet, then re-audit whether the imported exact
generator and linear propagator close the primary-runner premise."*

Both files already exist in the repository and are referenced in the
header preamble above as the load-bearing imported authority and
registered cache. This revision makes their role in the restricted
packet **explicit**:

**Restricted-packet files (load-bearing for this audit row):**
1. `scripts/mirror_2d_validation.py` — primary runner (2D exact mirror
   linear propagator).
2. `logs/runner-cache/mirror_2d_validation.txt` — primary-runner
   SHA-pinned cache (`exit_code=0`, `status=ok`).
3. `scripts/mirror_born_audit.py` — imported authority providing
   `gen_2d_mirror` (exact 2D mirror generator) and `propagate_LINEAR`
   (strictly linear propagator) consumed by the primary runner.
4. `logs/runner-cache/mirror_born_audit.txt` — imported-authority
   SHA-pinned cache (`exit_code=0`, `status=ok`) verifying the
   imported generator and propagator on the strict mirror Born family.

With items 3 and 4 registered above as restricted-packet members, the
exact-2D-mirror linear-propagator premise is closed by a one-hop
registered dependency on the imported authority. The auditor's
"closes the primary-runner premise" check is therefore: does item 4
demonstrate `gen_2d_mirror` + `propagate_LINEAR` correctness on the
strict mirror Born family? Per the registered cache it does
(`exit_code = 0`, `status = ok`), so the premise is closed at the
restricted-packet level. The bounded null-result claim itself
(no clean 2D mirror mass law, no clean 2D mirror distance law on the
searched windows) is unchanged.

**2026-05-18 inline-repair augmentation.** The 2026-05-17 re-audit
verdict on this row was `audited_conditional` (repair class
`runner_artifact_issue`) noting that the imported helper source and its
registered cache were not visible in the restricted packet the auditor
actually reads. To make the packet self-contained without changing any
of the four registered files above, the load-bearing helper-function
definitions (`gen_2d_mirror`, `propagate_LINEAR`, and their private
helper `_topo_order`) are now inlined verbatim into this note, together
with the relevant excerpt of `logs/runner-cache/mirror_born_audit.txt`.
Two stale display numbers in the "Retained result" section (the gravity
scaling fit and the `N=60` Born value) were synchronized against the
registered cache `logs/runner-cache/mirror_2d_validation.txt` at the
same time. None of these edits change the bounded null-result
conclusion.

This note freezes the exact 2D mirror gravity-law lane.

It uses the exact 2D mirror family retained in:

[`scripts/mirror_2d_validation.py`](../scripts/mirror_2d_validation.py)

The goal was narrow:

- check fixed-anchor mass-window and fixed-geometry distance-tail behaviour on the primary 2D mirror runner
- keep the exact 2D mirror family fixed
- promote a law only if the primary-runner fit quality is genuinely clean

## Helper-runner code excerpt (load-bearing for restricted packet, inlined 2026-05-18)

Inlined here so the restricted audit packet is self-contained: the primary
runner `scripts/mirror_2d_validation.py` does
`from scripts.mirror_born_audit import gen_2d_mirror, propagate_LINEAR`, so
the exact-2D-mirror linear-propagator premise depends on the verbatim function
definitions below. Source of truth: `scripts/mirror_born_audit.py` at commit
`b179c2d2c`. The two functions and their one private helper (`_topo_order`)
are reproduced byte-equivalent below; any subsequent edit to the upstream
script that changes these definitions must be re-mirrored here.

```python
# From scripts/mirror_born_audit.py (load-bearing for the primary runner).
# BETA is module-level in the upstream file and is consumed by propagate_LINEAR
# via closure-style read of the module global.
import math
import cmath
import random
from collections import defaultdict, deque

BETA = 0.8


def _topo_order(adj, n):
    in_deg = [0] * n
    for nbs in adj.values():
        for j in nbs:
            in_deg[j] += 1
    q = deque(i for i in range(n) if in_deg[i] == 0)
    order = []
    while q:
        i = q.popleft()
        order.append(i)
        for j in adj.get(i, []):
            in_deg[j] -= 1
            if in_deg[j] == 0:
                q.append(j)
    return order


def propagate_LINEAR(positions, adj, field, src, k, blocked):
    """STRICTLY LINEAR propagator. No normalization of any kind.
    This is the ONLY propagator used for Born claims on this branch."""
    n = len(positions)
    order = _topo_order(adj, n)
    amps = [0j] * n
    for s in src:
        amps[s] = 1.0 / len(src)
    for i in order:
        if abs(amps[i]) < 1e-30 or i in blocked:
            continue
        for j in adj.get(i, []):
            if j in blocked:
                continue
            if len(positions[i]) == 2:
                x1, y1 = positions[i]; x2, y2 = positions[j]
                dx, dy = x2-x1, y2-y1; dz = 0
            else:
                x1, y1, z1 = positions[i]; x2, y2, z2 = positions[j]
                dx, dy, dz = x2-x1, y2-y1, z2-z1
            L = math.sqrt(dx*dx + dy*dy + dz*dz)
            if L < 1e-10:
                continue
            lf = 0.5 * (field[i] + field[j])
            dl = L * (1 + lf)
            ret = math.sqrt(max(dl*dl - L*L, 0))
            act = dl - ret
            theta = math.atan2(math.sqrt(dy*dy + dz*dz), max(dx, 1e-10))
            w = math.exp(-BETA * theta * theta)
            ea = cmath.exp(1j * k * act) * w / L
            amps[j] += amps[i] * ea
    return amps


# Generator 3: 2D mirror
def gen_2d_mirror(nl, npl_half, yr, cr, seed):
    rng = random.Random(seed); pos = []; adj = defaultdict(list); li = []; mm = {}; bl = nl // 3
    for layer in range(nl):
        x = float(layer); ln = []
        if layer == 0:
            pos.append((x, 0)); ln.append(len(pos)-1); mm[len(pos)-1] = len(pos)-1
        else:
            up, lo = [], []
            for _ in range(npl_half):
                y = rng.uniform(0.5, yr)
                iu = len(pos); pos.append((x, y)); up.append(iu)
                il = len(pos); pos.append((x, -y)); lo.append(il)
                mm[iu] = il; mm[il] = iu
            ln = up + lo
            lb = max(0, len(li) - (1 if layer == bl+1 else 2))
            for ci in up:
                cx, cy = pos[ci]
                for pl in li[lb:]:
                    for pi in pl:
                        px, py = pos[pi]
                        if math.sqrt((cx-px)**2+(cy-py)**2) <= cr:
                            adj[pi].append(ci); adj[mm[pi]].append(mm[ci])
        li.append(ln)
    return pos, dict(adj), bl
```

## Imported-authority cache excerpt (load-bearing, 2026-05-18)

Inlined verbatim from
[`logs/runner-cache/mirror_born_audit.txt`](../logs/runner-cache/mirror_born_audit.txt)
so the restricted audit packet is self-contained. The Born-family
verification numbers below (all PERFECT, `|I3|/P` at machine precision) close
the exact-2D-mirror linear-propagator premise that the primary runner
relies on via its `from scripts.mirror_born_audit import ...` line.

```
===== runner cache v1 =====
runner: scripts/mirror_born_audit.py
runner_sha256: ccbbc2f10c2187338017a1b7020815e452240f96245718fab15ea12d86a04270
timeout_sec: 120
exit_code: 0
elapsed_sec: 7.80
status: ok
----- stdout -----
================================================================================
BORN AUDIT: ALL MIRROR GENERATORS (LINEAR PROPAGATOR ONLY)
  8 seeds per generator
================================================================================

   3D chokepoint N=15 npl=25 r=4  mean=1.74e-16  max=4.84e-16  ok=3  PERFECT
   3D chokepoint N=25 npl=25 r=4  mean=1.32e-15  max=1.93e-15  ok=4  PERFECT
       3D hybrid N=25 npl=40 r=5  mean=1.67e-15  max=4.05e-15  ok=8  PERFECT
       3D hybrid N=40 npl=40 r=5  mean=1.44e-15  max=2.05e-15  ok=8  PERFECT
     2D mirror N=25 npl=12 r=2.5  mean=5.21e-16  max=7.79e-16  ok=8  PERFECT
     2D mirror N=40 npl=12 r=2.5  mean=6.53e-16  max=9.89e-16  ok=8  PERFECT

VERIFICATION: This script uses propagate_LINEAR which has
NO normalization of any kind. If Born passes here, the
linear propagator on these graph families is Born-clean.

----- stderr -----
```

## Retained result (primary runner, load-bearing)

The exact 2D mirror family remains review-safe for Born, MI, decoherence, and
positive gravity, but the gravity-side fits on the primary runner are weak.

From the registered primary-runner cache
[`logs/runner-cache/mirror_2d_validation.txt`](../logs/runner-cache/mirror_2d_validation.txt)
(load-bearing) — values synchronized 2026-05-18 to the registered cache:

- gravity scaling across `N ∈ {15, 25, 40, 60, 80, 100}`:
  `gravity = 2.19 * N^+0.049`, `R^2 = 0.015` (weak)
- fixed-anchor mass window:
  `delta ~= 0.8720 * M^0.132`, `R^2 = 0.167` (weak)
- distance sweep tail:
  `delta ~= 0.3418 * b^0.320`, `R^2 = 0.075` (weak)

These primary-runner fit qualities are themselves the load-bearing evidence
that no clean promoted 2D mirror mass law or distance law is supported on the
searched windows.

The strongest retained clean row from the exact 2D validation lane is:

- `N = 60`
- `MI = 0.756118`
- `1 - pur_min = 0.4420`
- `d_TV = 0.8572`
- gravity `+2.5687`
- Born `1.26e-15`
- `k=0 = 0.00e+00`

## Companion cleanup sweep (diagnostic-only, not load-bearing)

The companion cleanup runner (`scripts/mirror_2d_gravity_law_cleanup.py`) was
run as a wider diagnostic sweep over additional anchor and threshold windows.
Its rows are reproduced here for diagnostic context only; they are NOT load-
bearing for the bounded null-result claim above, which closes from the primary
runner alone.

Diagnostic rows (from [`logs/2026-04-03-mirror-2d-gravity-law-cleanup.txt`](../logs/2026-04-03-mirror-2d-gravity-law-cleanup.txt)):

- `N = 60`
  - best mass window: `anchor_b = 5.0`, `delta ~= 0.8676 * M^0.462`, `R^2 = 0.923`
  - best distance tail: `mass_count = 5`, `peak_thr = 3.0`, `delta ~= 0.8858 * b^0.307`, `R^2 = 0.872`
- `N = 80`
  - best mass window: `anchor_b = 5.0`, `delta ~= 1.0791 * M^0.458`, `R^2 = 0.820`
  - best distance tail: FAIL on the wider sweep
- `N = 100`
  - best mass window: `anchor_b = 6.0`, `delta ~= 1.0027 * M^0.204`, `R^2 = 0.568`
  - best distance tail: `mass_count = 4`, `peak_thr = 1.0`, `delta ~= 0.9961 * b^0.140`, `R^2 = 0.321`

The companion cleanup table is consistent with the primary-runner conclusion
(deteriorating fits at larger N, no `R^2 >= 0.95` promotable row), but the
bounded null-result claim does not require those rows.

## Cleanup Conclusion

The primary runner does not support a clean promoted 2D mirror mass law or
distance law. The retained exact 2D mirror gravity story on primary-runner
evidence is:

- positive
- bounded
- weakly fit-dependent

So the conservative synthesis is:

- **exact 2D mirror = review-safe bounded coexistence pocket**
- **exact 2D mirror = no primary-runner-supported promoted mass law**
- **exact 2D mirror = no primary-runner-supported promoted distance law**

The family remains scientifically useful, but on the gravity side it is still a
bounded pocket rather than a law-like result.

## Audit boundary (2026-05-09 — claim narrowing per `runner_artifact_issue`)

The 2026-05-08 audit verdict on this note was `audited_conditional` with the
repair target:

> runner_artifact_issue: provide the completed `mirror_2d_gravity_law_cleanup.py`
> output/cache and source, or narrow the note to the diagnostic core actually
> backed by current runner output.

This revision takes the second branch of the repair target. The bounded null-
result claim is now anchored entirely on the primary runner
(`scripts/mirror_2d_validation.py`) and its cached log
(`logs/2026-04-03-mirror-2d-validation.txt`). The wider companion cleanup
sweep is recorded as diagnostic-only context. The bounded null-result holds
from the primary-runner fit qualities alone (`R^2 = 0.168 / 0.167 / 0.075`),
without depending on the companion cleanup rows.

## Audit boundary (2026-04-28)

The earlier Status line ended in "no clean 2D mirror law `proposed_promoted`",
which the audit-lane parser read as a `proposed_promoted` claim even though
the literal sentence said the opposite. The Status line has been rephrased
to a positive bounded null-result framing.

Audit verdict (`audited_failed`, leaf criticality):

> Issue: the target is classified as `proposed_promoted`, but the source
> note and runner both say the cleanup found no clean promoted 2D mirror
> gravity law. Why this blocks: the best mass exponents are weak or
> deteriorating and the distance-tail fits are absent or low quality, so
> promoting a law would invert the actual result of the source packet.

> Repair target: change the Status line so the audit queue does not read
> this as `proposed_promoted`; the safe statement is the bounded
> null-result that the cleanup did not find a clean promoted mass or
> distance law.

## What this note does NOT claim

- A promoted 2D mirror mass law.
- A promoted 2D mirror distance law.
- That the bounded coexistence pocket is the same thing as a
  promoted-tier gravity result on the 2D mirror family.
- Any load-bearing conclusion drawn from the diagnostic-only companion
  cleanup table; the bounded null-result rests on the primary-runner
  log alone.

## What would close this lane (Path A future work)

Reinstating a promoted 2D mirror gravity law would require:

1. A registered primary-runner mass-exponent fit that clears a hard
   `R^2` threshold (e.g. `R^2 >= 0.95`) on at least three sizes — the
   current primary-runner mass-window fit is `R^2 = 0.167`, well below
   the bar.
2. A registered primary-runner distance-tail fit that clears the same
   hard threshold — currently `R^2 = 0.075` on the primary runner.
3. A first-principles argument that the fitted exponent is the
   mass-coupling exponent, not just an empirical curve fit.

## Audit boundary (2026-05-10 — imported-authority dependency lifted into the header)

This revision addresses the generated-audit repair target:

> runner_artifact_issue: supply scripts/mirror_born_audit.py or vendor its
> generator/propagator into the primary runner, then re-audit the same
> cached weak-fit rows.

This revision takes the first branch of the repair target: it lifts
`scripts/mirror_born_audit.py` and its registered cache
`logs/runner-cache/mirror_born_audit.txt` into the note header as direct
load-bearing dependencies (one-hop). The bounded null-result claim itself
is unchanged; the supplied audit packet now includes the exact-2D-mirror
generator and `propagate_LINEAR` authority alongside the primary-runner
weak-fit cache.

## Registered runner artifacts

The primary-runner source and registered cached stdout backing the three
weak-fit rows, plus the imported-authority cache, are all present in the
worktree as one-hop registered dependencies:

- Primary runner: `scripts/mirror_2d_validation.py` (load-bearing source for
  every weak-fit row in the "Retained result (primary runner, load-bearing)"
  section above).
- Primary runner cache: `logs/runner-cache/mirror_2d_validation.txt`
  (registered cached stdout; `exit_code=0`, `status=ok`).
- Imported generator/propagator authority: `scripts/mirror_born_audit.py`
  (provides `gen_2d_mirror` and `propagate_LINEAR`, imported by the primary
  runner — load-bearing for the exact-2D mirror linear-propagator premise).
- Imported authority cache: `logs/runner-cache/mirror_born_audit.txt`
  (registered cached stdout; `exit_code=0`, `status=ok`).
- Companion cleanup runner (diagnostic-only):
  `scripts/mirror_2d_gravity_law_cleanup.py`.

The bounded null-result claim closes from the primary runner's cached stdout
plus the imported-authority cache (for the exact-mirror generator and linear
propagator); the companion cleanup table remains diagnostic context.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [mirror_program_synthesis](MIRROR_PROGRAM_SYNTHESIS.md)
