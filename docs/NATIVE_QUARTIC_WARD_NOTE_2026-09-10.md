---
claim_id: native_quartic_ward_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Under the supplied native Ward model and common channel gap, a quartic inverse-square envelope sharpens two unchanged quadratic/constant trial certificates; both sign intervals remain inconclusive."
upstream_dependencies:
  - native_gaussian_moment_jet_note_2026-09-10
  - native_stronger_ward_estimators_note_2026-09-10
runner: scripts/native_quartic_ward_2026_09_10.py
---

# Quartic inverse-square envelopes for unchanged Ward trials

**Type:** bounded_theorem

Status: new saved-data estimator completed and independently reconciled. Both modes remain INDETERMINATE_SIGN. Canonical review is pending; full pipeline, current-main combined validation, changed-audit readiness and formal audit are UNRUN.

The accepted calculation applies a quartic spectral envelope to the original quadratic first polynomial and constant second polynomial. It changes the certified residual estimate while retaining those trials and their nominal. The resulting alpha intervals are approximately

| Original mode | E upper | F upper | Alpha interval |
| --- | ---: | ---: | --- |
| residual | 1.3838 | 66.6052 | [-465.2922, 609.3813] |
| variational | 1.1428 | 66.7061 | [-468.7459, 629.7689] |

Both intervals contain zero. Exact rational endpoints are in the immutable result packet. These intervals are not combined with a better enclosure from an unrelated signed-dual trial family.

## A positive quartic envelope

Use the supplied dimensionless bound \(D\ge\delta I\), with \(\delta=1/4\). For positive rational \(t,u\), define
\[
P(x)=(x-\delta)(x-t)^2(x-u)^2,\quad
B=(\delta t^2u^2)^{-1},\quad
A=B(\delta^{-1}+2/t+2/u).
\]
The constant and linear terms of \(1+P(x)(Ax+B)\) vanish, so
\[
Q_{t,u}(x)=\frac{1+P(x)(Ax+B)}{x^2}
\]
is a polynomial of degree four. For every \(x\ge\delta\),
\[
Q_{t,u}(x)-x^{-2}
=\frac{(x-\delta)(x-t)^2(x-u)^2(Ax+B)}{x^2}\ge0.
\]
Repeated parameters cause no singularity. The final fixed schedule uses all fifteen unordered pairs with repetition from \(\{1,2,4,8,16\}\). It is neither a continuous optimum nor a fitted search. The earlier proof's half-shifted prospective schedule is historical; the identity holds for all positive parameters.

Let \(p\) be the unchanged degree-two first polynomial and \(r=(I-Dp(D))\Omega\). With \(v=(1,-p_0,-p_1,-p_2)\), the seven exact convolution coefficients \(d_k=\sum_{i+j=k}v_i v_j\) give
\[
\rho_j=\langle r,D^jr\rangle=\sum_{k=0}^6d_k m_{k+j},\qquad 0\le j\le4.
\]
The new protocol reuses the accepted \(\rho_0\) and evaluates only \(\rho_1,\ldots,\rho_4\), using accepted moments through order ten. If \(Q=\sum c_jx^j\), the spectral theorem gives \(\|D^{-1}r\|^2\le\sum c_j\rho_j\). Since coefficients may be negative, each interval endpoint is selected by the coefficient sign. Correlations can widen this bound but cannot invalidate it. A negative certified upper is a contradiction and causes refusal; only a lower endpoint can intersect the known nonnegative domain.

The minimum over the fifteen valid upper bounds and the retained same-trial gap alternative is valid. No accepted trial is reoptimized or recomputed. There are two original modes and two P/O classes, hence sixty fixed quartic candidates.

## Coupled second residual and the posterior enclosure

Retain the original constant \(q_A\) and source residual interval \(t_A^2\). For each channel,
\[
F_A\le\delta^{-1}\bigl(\sqrt8 E_A+\sqrt{t_A^2}\bigr).
\]
Combine twelve P channels and three O channels by sums of squares. This step propagates the improved first-residual estimate into the second bound without asking for a new mixed-source kernel.

Let \(a,b\) be accepted upper bounds on the unchanged trial norms. With \(X=4\sqrt{15}\), \(V=32\sqrt{30}\), set \(\chi=\min(X,a+E)\), \(\psi=\min(V,b+F)\). The imported posterior theorem bounds the Ward error by
\[
\mathcal E=6\{E(a+\chi)+\min(Eb+\chi F,E\psi+aF)\}.
\]
Outward roots and arithmetic produce the certified new interval \([(N_- -\mathcal E)/8,(N_+ +\mathcal E)/8]\). Its intersection with the accepted same-trial posterior interval is retained. Empty intersection refuses. This theorem guarantees containment; it does not promise a sign or improvement for every input.

## Same-trial and scalar provenance

The loader authenticates three accepted families: original degree20, its posterior certificate, and the new high-moment pilot. Both later families must bind the exact original degree20 event/result pair. Original 255-event chronology supplies identical lower moments across the two modes, the original \(p,q,\rho_0,t^2\), and nominal. The high supplier's retained lower table must equal the outward fixed-grid mapping of those lower moments. Its new orders seven through ten then complete the same physical moment sequence.

Posterior mode inputs must match the original gate, q and source-norm identity. The unchanged nominal is checked against both accepted results. This is stronger than matching a mode name. The packet carries exact bindings and compact accepted source records; original event and scalar truth is inherited from their accepted calculations rather than claimed as new independent work.

The independent root separately reconstructed the source-to-INPUTS mapping, signed residual sums, closed-form quartic coefficients, all candidate expectations, channel roots and posterior enclosure. It uses separate arithmetic, with original scalar and trial truth explicitly inherited. The new output has 97 events and eight files. All eight output hashes and their membership are checked before and after reconciliation.

## Actual execution and portable verification

The fixed protocol completed once in 1.72 seconds externally, with 54,951,936 bytes external RSS and 101,793,792 bytes sampled tree peak, within 30 seconds and 384 MiB. The immutable root acceptance is separate from its historical external-pending receipt. No original oracle, native moment or trial computation was replayed.

The supporting compact checker verifies copied hashes, accepted root/worker/source identities, source-family linkage, resource fields, exact counts and mode copies. It checks ordered rational interval semantics, intersection, nonnegative error bounds and faithful indeterminate status. It hashes retained events opaquely and does not reconstruct their arithmetic. Six coherent metadata/interval/identity mutants reject; a small rational quartic factor test exercises the mathematical identity without accepted numerical inputs.

IMPORTS.json records exact original-to-copy hash correspondence. Runtime freezes retain the full transitive input inventory. Preregistration95 is 418d2e3c66e8cb6a99d3014149d2834c9e360e64; it is not asserted to contain later outputs. The accepted result is preserved at archive96 commit a5324fc7c7d908ea2cf8c8072db92d4239fd430e. All corrected portable draft files have exact archive97 recovery at commit c96ee19fad05d7739d0762a9e0dc74057ce6c4f7, listed in RECOVERY_MAP.json. Full source proofs and independent reviews are copied alongside the compact evidence. Canonical assembly preserves the original draft and its reviews as separate immutable source records.

## Reproduction and dependency boundary

Run `python3 scripts/native_quartic_ward_2026_09_10.py` for compact receipt checks and synthetic factor controls. It does not replay the saved-data estimator or native calculations. See the packet (`outputs/native_quartic_ward_2026_09_10_inputs/HANDOFF.md`), [higher moments](NATIVE_GAUSSIAN_MOMENT_JET_NOTE_2026-09-10.md) and [prior posterior bounds](NATIVE_STRONGER_WARD_ESTIMATORS_NOTE_2026-09-10.md). A richer linear inner trial requires a new nominal and is outside this block.


## Current compact evidence boundary

The [canonical cache](../logs/runner-cache/native_quartic_ward_2026_09_10.txt) records only the current compact receipt, identity and synthetic checks. The current capture budget is 30 seconds and 384 MiB with external process-tree supervision. Historical source, results and resource receipts retain their original identities and protocol limits; this compact run does not repeat their numerical calculations. The raw original packet and its input manifests are retained under `outputs/native_quartic_ward_2026_09_10_inputs/`. Historical review assertions are provenance, not a current review verdict.

## Current claim disposition

Current claims are the constructive identities, valid conditional enclosure bounds, moment-supplier constructions and explicitly finite certificate outcomes described above. Certification of the historical constant-trial/all-q exclusions, zero-dual exclusion and norm-only optimality claim is deferred: the exact-target No-Go Discipline route requirement is unmet. Their original proofs and results remain byte-exact in the input packets as historical conditional evidence. They are not current closed negative claims or premises needed to establish the constructive bounds.

## No-Go Discipline record and limitation

The quartic certificate concerns fifteen fixed parameter pairs and the unchanged degree20 trials and nominal. An unrelated signed-dual family cannot be substituted. Negative certified norm uppers and empty same-trial intersections refuse; inconclusive intervals are not impossibility theorems.

**N1 — Actual mechanisms and unresolved quota.** The unit records the following five genuinely different historical mechanisms. They are not five failed in-domain attacks against any one negative theorem. The exact-target five-route requirement is not established by this inventory; no No-Go Discipline Gate PASS is asserted for those negative claims. The table preserves actual attempts without inventing additional tests.

| Mechanism | Actual retained outcome | Relation to the original all-q obstruction |
| --- | --- | --- |
| Polynomial inverse approximation with gap-residual error | Degree10 and degree20 certificates remain indeterminate | Only the frozen degree10 first polynomials and original estimator are covered; degree20 lies outside |
| Posterior trial-norm enclosure | Degree10 and degree20 certificates remain indeterminate | A different error functional, outside that obstruction |
| Quadratic spectral-residual envelope | Two fixed degree10 choices remain indeterminate | A different estimator using residual moments |
| Correlated signed-dual correction | Five fixed scales narrow the enclosure but remain indeterminate | A different center and error estimator |
| Quartic spectral envelope with higher Gaussian moments | Two same-degree20 modes remain indeterminate | A new moment mechanism and first polynomials outside the original target |

Changing polynomial degree alone, changing lambda, or supplying the moments does not create an additional mechanism family. No row rules out the full physical alpha problem.

**N2 — Dependencies, not independent obstructions.** The supplied model, reference and CAR/normal-order conventions define the objects; the Ward identity defines the observable; the channel gap controls inverse bounds. Certified numerical moments are downstream conditional data, not independent physical constraints. The determinant germ uses bounded h0, finite-rank perturbation and absence of a zero atom; it does not itself require the impurity gap. The inverse and quartic estimates separately require that gap. No count of independent impossibility arguments is inferred from these dependencies.

**N3 — Exact hypotheses.** The all-q bound retains the frozen first polynomial and original residual error functional, with honest residual bounds for the second trial. The constant-trial statement retains the specified constant choices and scalar inputs. The zero-dual screen retains its original errors. Norm-only sharpness allows abstract error vectors obeying the stated norm bounds and operator premises; extra native correlations can improve the estimate. All numerical conclusions inherit the supplied model and the certified input intervals.

**N4 — Residual-to-claim record.** The paths below identify retained historical negative evidence and finite descriptive outcomes, not current negative certification or new executions.

| Retained record | Exact residual or conclusion | What it does not establish |
| --- | --- | --- |
| Finite-moment `imports/ALL_Q.md` and `ALLQ_RESULT.json` | Neither strict-sign test succeeds for the frozen p and original error estimator | Failure of another p or estimator |
| Finite-moment `imports/DEGREE10.md`, constant section | The specified original constant p/q sign test is inconclusive | Failure of every constant trial or error bound |
| Correlated `source_draft/proofs/sharp.md`, section 2 | Sharp abstract norm-only remainder, with extremizers in the 6 and -3 eigenspaces | Realization by the actual native errors |
| Correlated `source_draft/evidence/zero/RESULT.json` and sharp proof section 1 | The fixed zero-dual lower-endpoint screen does not become strictly positive | Failure of signed-dual corrections |
| Signed-dual and quartic saved results | Particular certified enclosures contain zero | A general physical no-go or alpha equal to zero |

**N5 — Resolution and execution scope.** Per element: exact rational, sign and identity checks apply to the retained finite inputs. Per site: no new sitewise native calculation is executed. Per mode: only the stated saved modes and candidates are compared. Per block: compact receipt checks and synthetic controls cover the declared packet. Lattice wide: infinite-model conclusions rely on their stated analytical proofs and premises; compact checks do not replay the numerical catalog, native moments or an infinite lattice.

**N6 — Missing implication.** Indeterminate certificates leave a sign decision open; they do not require a new axiom. A better first polynomial, a sharper certified residual estimate or additional justified correlations can change the certificate. Those routes require their own compatible nominal, residual and input proofs.

**N7 — Concrete steelman.** A signed-dual route takes y=s(V-tJU) and z=-tU, retains the signed corrections <r,y>+<s,z>, and computes both residual norms from complete Gram data. A successful attack would certify the corrected positive endpoint. The retained lambda=1 attempt narrows the interval but does not prove that endpoint positive. A richer first polynomial with certified higher moments is another concrete route. These escapes change the old obstruction's domain; they preserve its narrow algebra while preventing a universal inference. Scaling lambda scales both trial vectors linearly, not quadratically.

**N8 — Prior-work echo.** The constant-trial limitation led to degree-one/two trials; the original all-q error obstruction led to posterior and spectral estimators; the zero-dual limitation led to signed corrections. These are recorded changes of scope, not proofs of a physical sign and not demands for new axioms. The unresolved exact-target N1 quota remains a packet limitation, separately from validity of the conditional algebra and positive enclosure constructions.

## Recovered scientific input closure

The [scientific recovery manifest](work_history/repo/review_feedback/pr8079-8083-scientific-recovery/manifest.json) binds the relevant catalog geometry and endpoint records, producer and arithmetic-root sources, and saved rho5/omega5/omega79 arithmetic payloads. Existing exact catalog objects are reused from landed archives. Original compact packets retain the degree20 event stream and later trial/Gram/moment records. The manifest is a declared proof-identity input; the compact runner does not read or recompute every recovered numerical payload. Historical execution receipts keep their original dates, source identities and resource scopes.
