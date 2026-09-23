# Numerical and mutation history

All runs are personal floating or exact-integer diagnostics. None is an independent theorem check or a canonical audit cache. The general proposed estimates are derived in the notes. The source hash printed by each successful primary program is checked against its actual current file during focused verification.

| Program | Final successful output | Distinct comparison and practical limit |
| --- | --- | --- |
| block01_temporal_resummation_check.py | BLOCK01_TEMPORAL_RESUMMATION_ATTEMPT1.stdout.txt | Direct Wilson inverse/determinant versus summed temporal runs, trace-log and rectangle sum; finite shapes only |
| block02_physical_curl_hessian_check.py | BLOCK02_CURL_HESSIAN_ATTEMPT1.stdout.txt | Analytic matrix Hessian in another Clifford basis, exact gauge null directions and determinant differences; slice count is fixed, so duration shrinks with delta |
| block03_open_boundary_hamiltonian_check.py | BLOCK03_OPEN_HAMILTONIAN_ATTEMPT1.stdout.txt | Full time-Dirac determinant, Schur/complementary minors, explicit70-state CAR evolution and exterior powers for noncommuting histories |
| block04_dynamical_gauge_join_check.py | BLOCK04_DYNAMICAL_GAUGE_ATTEMPT3.stdout.txt | Actual clock path sum, physical1296-state transfer, separate sparse CAR/electric Hamiltonian and arbitrary-vector generator; a single edge has no magnetic plaquette |
| block05_integer_local_filling_check.py | BLOCK05_INTEGER_FILLING_ATTEMPT2.stdout.txt | Exact integer boundaries, local support, translations, all six spatial contraction orders and physical curl/image phases for120 closed walks |
| block06_third_curl_variation_check.py | BLOCK06_THIRD_VARIATION_ATTEMPT1.stdout.txt | Third matrix derivative versus separately evaluated determinant differences at fixed physical duration0.3, with gauge directions checked |

At mu6,kappa0.5, the sufficient refined Hessian bound is about12186, whereas the measured finite Hessian norm is at most about1.35e-4 in its chosen examples. The loose third bound is about1.07e7, whereas resolved third variations are around5.5e-5 to6.2e-5. These large gaps are reported; finite examples do not optimize or validate the general bound merely by lying beneath it.

The first temporal-run and rectangle comparisons agree near floating precision; the leading constant-field response approaches the derived expression. The Fock one-particle/explicit-CAR continuum amplitudes differ by about3.2e-11 at the declared ODE tolerances. The coupled gauge path sum1.0016056500616617 agrees with the physical transfer1.0016056500616752, difference1.35e-14. Omitting its endpoint multipliers changes that example by about9.56e-4. The third-variation Richardson differences are1.3e-10 to3.4e-10 in the reported directions.

## Preserved coarse-refinement failure

Block04 attempt1 failed the declared requirement that the final error be at least a factor3 smaller than the first error on each joint path. Its slow path had3 and17 time slices, with errors0.0152695768 and0.0064723867. The reduction was about2.36, so the assertion correctly failed. The failed source is block04_dynamical_gauge_join_check.ATTEMPT1.py, SHA2567dc70c8b2ec3c06f780512cb333ee7362294a645b1e7a3838b924755ac33f23a. Its stdout is empty and its actual assertion traceback is preserved.

The separate BLOCK04_REFINEMENT_FAILURE_DIAGNOSTIC stdout records all three paths through N33, invoking the original source's explicit_paths, continuum_hamiltonian and physical_boundary functions. It compared the same parameters mu6,kappa0.5,g0.8,T0.5 and N3,5,9,17,33 with M_t=N^power for powers1,2,3. It was run as a one-off Python stdin command; it is a diagnostic transcript, not a registered standalone runner. The slow path at33 slices has error0.0038088813, satisfying the original factor3 target. No threshold was loosened. Attempt2 adds N33 on that path and preserves the original target; its successful source is separately retained. Attempt3 adds the independent arbitrary-vector generator test after review identified that one boundary amplitude alone could miss a wrong electric energy. Its errors fall from0.00436664 to0.00109407 to0.00027359 as N64,128,256 increase on the specified very-small-time path. Removing the electric energy leaves an error near0.748 and is rejected.

The final coupled boundary errors are0.00380888 for the slow path endpoint N33,0.000494813 for N17 squared, and0.0000257305 for N17 cubed. The diagnostic's farther N33 cubed point has error0.00000298532. Those are finite observations, not a claimed convergence rate for arbitrary graphs.

## Preserved initially equivalent orientation mutation

The first challenge_blocks04_06 run rejected10 changes and failed its own all-rejected assertion because filling_wrong_orientation exited successfully. The original source contracted axes in ascending order. After earlier axes are projected away, every remaining nondegenerate edge has b>a. Consequently replacing the factor "1 if a<b else -1" by1 is equivalent on that exact domain. Its survival is not evidence of an incorrect boundary identity, and the original mutant/output remain preserved.

The follow-up keeps the original primary source as block05_integer_local_filling_check.ATTEMPT1.py and adds the other five permitted spatial contraction orders, keeping time first. These exercise the a>b branch while preserving the same area argument. The same orientation change then violates an exact integer boundary identity. The original failed harness source and stdout/stderr are preserved, and the follow-up writes to a separate directory so it does not overwrite the first evidence.

The final first harness rejects12 formula faults in Blocks01-03. The final second harness rejects11 in Blocks04-06. Their actual mutant sources and streams are in formula_mutations and formula_mutations_followup. They cover missing normalization/pairing, temporal closure, Hessian contacts, fermion parity, endpoint factors, Gauss electric energy, integer orientations, physical time conversion and third-derivative coefficients. Counting those23 final tests does not make them independent audits or establish that all possible faults would be detected.

## Prose and source corrections

The final Block02 rectangle sum includes t=0, correcting a prose lower-limit typo; the program already included it. Physical time was made explicit in the filling paragraph. Block03 and Block02 scope paragraphs now point to the completed companion proposals, replacing stale future-tense descriptions. A working Block04 note initially written in a root notes directory was moved unchanged into this campaign pack before staging. No pre-existing science was displaced.
