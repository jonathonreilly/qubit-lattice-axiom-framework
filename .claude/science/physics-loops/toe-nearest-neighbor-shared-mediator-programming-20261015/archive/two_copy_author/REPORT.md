# Constructive single-pair shared-mediator pilot

The candidate gives a positive ordinary-NN two-qubit construction for the actual fixed pair c=v0=(0,1,1), e=e(v0)=(0,2,1), for any real samples f_j and one chosen Pauli pair Pc,Pe. All original sites, H0+K_X, arbitrary old inputs and references remain. Fresh auxiliaries start in their bare product vacuum and are retained in the comparison. This is a proposed conditional theorem with a complete author proof; it has not had independent review or audit.

The key is two matched shared hopping graphs. Pc drives their source ports with opposite signs; Pe detunes their remote ports with opposite signs; n_j drives both clock ports equally. Direct rank-one inversion gives an exact second-order pair coefficient and cancels n_j Pc and n_j Pe. On N_X=1, cross-clock n_j n_k terms vanish. The global scalar s0 and all clock onsite terms s_j n_j are actually installed. The full-space positive penalty has precisely the bare original-space vacuum kernel, gap at least1/4, and norm2m. A global two-corrector residual retains mixed virtual sectors and noncommuting H0/K_X, yielding

    ||e^(-it K_Delta)J - J e^(-it H_tar)||
        <= F1/sqrt(Delta)+F2/Delta,    0<=t<=T.

The phase-sensitive full-output theorem and explicit constants, scalar, positive reserve, energy, coefficient-error and timing charges are in DERIVATION.md sections1–5. No dressed preparation or discarded output is used.

For the literal v0 pair, section7 supplies both graphs for every permitted L_b,Q,n_old,M: copies of the fixed clock square at z=4 and z=2, with disjoint equal-length tails to four fresh data neighbors. There are 2[M+x_max+L_b+18] auxiliaries. Each original addressed site uses two fresh neighbors independent of M, and the fresh interaction degree is at most4. The original Hamiltonian is unchanged as a summand; added clock counterterms are explicit.

One exact predeclared diagnostic ran once, successfully: L_b=8,Q=3,n_old=2,M=4, 74 original sites, 66 fresh auxiliaries, direct rational33-by33 inverses. It checked actual NN placement and all one-clock/Pauli-sign responses, retained a nonzero two-clock cross term, and detected omitted-mirror and missing-clock-counterterm mutations. It did not simulate the full2^66 auxiliary Hilbert space or independently certify the analytic dynamics. The exact result is SELECTED_RESULT.json; source, plan, hashes and complete streams are preserved under runs/selected_01.

The full autonomous program remains open. The same fresh-port certificate fails at v1=(-1,0,0), whose six neighbors are already original occupied factors. Three separate Pauli-axis copies would also overspend available data ports. These are limits of this construction, not a broad no-go. Independent checking should first target the full-sector inverse/residual and the all-parameter fixed-pair placement. Further full-program work needs a mechanism that handles shared noncommuting axes and saturated old sites.

All requested source identities matched, including autonomous freeze39d2efbb. Source/exposure coverage is in SOURCE_COVERAGE.md. No Git, PR, audit, physical axiom, campaign checkpoint, other chat, or editable prompt was changed. Only the authorized local_clock_shared_mediator_candidate directory was written. FINAL_FREEZE.json binds the final report and complete packet. The pre-execution derivation is separately preserved, and the post-execution changes are scope/notation/geometry-explanation clarifications, coefficient-count bookkeeping, and attribution/evidence notes without a scientific rerun.
