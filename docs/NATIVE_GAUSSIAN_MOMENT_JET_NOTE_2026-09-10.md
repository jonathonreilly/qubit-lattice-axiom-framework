---
claim_id: native_gaussian_moment_jet_note_2026-09-10
claim_type: bounded_theorem
claim_scope: "Conditional native Gaussian determinant bridge and finite source-degree closure, with certified local moments of orders seven through ten for the supplied P/O defects."
upstream_dependencies:
  - native_correlated_ward_certificates_note_2026-09-10
  - native_finite_moment_ward_note_2026-09-10
runner: scripts/native_gaussian_moment_jet_2026_09_10.py
---

# Gaussian jets and certified local high moments

**Type:** bounded_theorem

Status: conditional mathematical bridge and accepted scalar/high-moment certificates. Independent canonical source review is recorded in the packet. Full pipeline, current-main combined validation, changed-audit readiness and formal audit are UNRUN.

For the supplied dimensionless native Hamiltonian, the negative free spectral projector and the original reference normal-order convention, the accepted computation encloses the P/O impurity moments of orders seven through ten. Both classes meet the fixed full-width pilot target \(10^{-6}\); the largest reported width is about \(1.848\times10^{-19}\). This is a moment certificate. It does not establish a Ward error target, the sign of alpha, or a Gaussian state approximation.

## The conditional Gaussian bridge

Write \(h_0=iK\), \(P=1_{(-\infty,0)}(h_0)\), and \(V=2i(ad^*-da^*)\). Keep the original reference scalar subtraction in \(D\). The relative one-particle operator is

\[
U(t)=e^{t h_0}e^{-t(h_0+V)},\qquad
Z(t)^2=\det\bigl(I+P(U(t)-I)\bigr),\quad Z(0)=1.
\]

Thus \(\log Z=\tfrac12\operatorname{Tr}\log(I+P(U-I))\), and \(m_n=(-1)^n n![t^n]Z(t)\). The factor one half and the reference scalar are essential. Replacing the scalar by the impurity ground-energy shift would change the problem.

The imported infinite-volume proof controls the relative trace-class perturbation and its analytic germ, using bounded free propagation, finite-rank Duhamel terms, strong finite-volume convergence and convergence of the local negative covariance. The supplied free zero set has Haar measure zero; no positive free spectral gap is assumed. The finite determinant identity alone is not the infinite-volume justification. The complete conditional argument and its independent review are retained in the proof packet.

## Why degree ten needs only finite low-degree tables

Set \(U-I=\sum_{n\ge1}A_n t^n\). The exact recurrence is
\[
 nA_n=[h_0,A_{n-1}]-A_{n-1}V,
\]
with the constant identity included at order zero. The one-defect sector is \(L_n=-\operatorname{ad}_{h_0}^{n-1}(V)/n!\). Since \([P,h_0]=0\), its trace vanishes for \(n\ge2\). Remove that trace analytically before asking for a projected matrix entry; retain the one-defect operators in products with other coefficients.

Every remaining cumulant of degree \(n\ge2\) has at least two defect factors. Splitting at those factors bounds intervening free powers by \(n-2\). The sparse coefficient implementation therefore uses ordinary and projected two-source tables only through degree eight for \(m_{10}\), without a Gram inverse. Its scalar Euler recurrence is \(nZ_n=\sum_{j=1}^n j\ell_j Z_{n-j}\). Accepted \(m_0,\ldots,m_6\) determine the lower scalar coefficients and are reused; the new computation evaluates only orders seven through ten.

The P/O source table and its signed negative-band convention remain those of the pinned proof. In the opposite class a neighbor diagonal introduces a two-power radial shift. Hence this degree-ten calculation uses absolute odd moments through \(\omega_9\), and exact even radial moments through order ten. There is no requirement here for \(\omega_{11}\). The separately reviewed multisource and reflected-jet route is future work and is not part of this numerical certificate.

## Accepted suppliers and actual retained evidence

The new omega79 supplier reused the accepted 1742 Gauss nodes, represented by 3484 endpoint oracle evaluations in the original catalog, and made zero new oracle calls. It used the frozen positive-integral identities, low and high tail bounds, and 40-term tails with new exact moments M44/M45. The independent root reconstructed the node/tail/final arithmetic. Both \(\omega_7\) and \(\omega_9\) met their original full-width targets, \(10^{-22}\) and \(10^{-20}\). The complete supplier proof is copied; original node files are recoverable by the exact output hash inventory rather than duplicated here.

The high-moment producer reused the authenticated degree20 lower moments, scalar sources and even-moment records. An independent root reconstructed its A/Q coefficients, logarithm traces and new scalar coefficients from retained data using separate interval arithmetic. The successful packet has six files and 189 events, with eight new P/O moment intervals and both CERTIFIED_PILOT_WIDTH flags. The original lower moments and scalar supplier truth are inherited, explicitly; the root does not claim to have independently recomputed those native quantities.

The high-moment execution took 3.87 seconds externally, with 68,386,816 bytes external RSS and 119,685,120 bytes sampled tree peak, within the fixed 60-second/384-MiB protocol. The omega79 execution took 9.79 seconds within its 30-second/384-MiB protocol. Historical root receipts retain their external-pending field; separate ROOT_ACCEPTANCE files supply the completed external reconciliation. Neither historical receipts nor failed preparations have been relabeled.

## Compact verification and recovery

The supporting checker validates immutable imported bytes, accepted result/source/root identities, resource metadata, class/order census, canonical intervals and width flags. It hashes the retained high-moment events as opaque evidence. It does not replay node integrands, native Wick calculations or event arithmetic. Its small exact half-log fixture and coherent semantic mutants test the compact checker, not the native theorem.

IMPORTS.json maps each local copy to its exact original path and SHA-256. The original runtime freezes retain their full input closures; the local mapping identifies which copies this draft carries. Archive92 is 89025d1e4adb1ac54dc95706f91e8f71dc9e3880. Omega79 preregistration is bf4f60b2e52c9a41d9638eaba1740cb86f07e25e; high-moment preregistration is 0ac1cd2f075c8182358939bec5e01c2c2bc02928. All portable source and accepted high-moment output bytes are recovered by RECOVERY_MAP.json at archive94 commit 932e27f7180f9975456de1ee6874de331afc6b98. These preregistration commits are not asserted to contain later execution outputs.

## Reproduction and dependencies

Run `python3 scripts/native_gaussian_moment_jet_2026_09_10.py` for portable receipt checks and synthetic controls. This does not replay the native computations. See the packet (`outputs/native_gaussian_moment_jet_2026_09_10_inputs/HANDOFF.md`), [finite moment hierarchy](NATIVE_FINITE_MOMENT_WARD_NOTE_2026-09-10.md), and [previous correlated bounds](NATIVE_CORRELATED_WARD_CERTIFICATES_NOTE_2026-09-10.md). The new moments supply a later error-bound calculation; that calculation is outside this block.


## Current compact evidence boundary

The [canonical cache](../logs/runner-cache/native_gaussian_moment_jet_2026_09_10.txt) records only the current compact receipt, identity and synthetic checks. The current capture budget is 30 seconds and 384 MiB with external process-tree supervision. Historical source, results and resource receipts retain their original identities and protocol limits; this compact run does not repeat their numerical calculations. The raw original packet and its input manifests are retained under `outputs/native_gaussian_moment_jet_2026_09_10_inputs/`. Historical review assertions are provenance, not a current review verdict.

## Current claim disposition

Current claims are the constructive identities, valid conditional enclosure bounds, moment-supplier constructions and explicitly finite certificate outcomes described above. Certification of the historical constant-trial/all-q exclusions, zero-dual exclusion and norm-only optimality claim is deferred: the exact-target No-Go Discipline route requirement is unmet. Their original proofs and results remain byte-exact in the input packets as historical conditional evidence. They are not current closed negative claims or premises needed to establish the constructive bounds.

## No-Go Discipline record and limitation

The determinant germ and degree-filtered moment supplier are conditional on the supplied Gaussian model. The finite toy is not the infinite-volume bridge; a Haar-null free zero set is not a positive gap. These results select neither a physical state nor the sign of alpha.

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

Current supporting proofs include the exact `source_draft/proofs/native-gaussian-moment-jet-cold-review-REVIEW.md` and `native-gaussian-moment-jet-parent-synthesis-REVIEW.md` files in the retained Gaussian input packet. Their infinite-volume argument is load-bearing scientific input despite the historical filenames; their old review verdicts are not current authority.

## Recovered scientific input closure

The [scientific recovery manifest](work_history/repo/review_feedback/pr8079-8083-scientific-recovery/manifest.json) binds the relevant catalog geometry and endpoint records, producer and arithmetic-root sources, and saved rho5/omega5/omega79 arithmetic payloads. Existing exact catalog objects are reused from landed archives. Original compact packets retain the degree20 event stream and later trial/Gram/moment records. The manifest is a declared proof-identity input; the compact runner does not read or recompute every recovered numerical payload. Historical execution receipts keep their original dates, source identities and resource scopes.
