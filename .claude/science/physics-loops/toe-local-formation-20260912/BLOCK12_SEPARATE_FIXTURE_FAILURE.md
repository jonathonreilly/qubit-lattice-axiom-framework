# Preserved first enlarged-table fixture failure

The first native check returned ordered_pairs90, maximum table error12,
maximum signed-kernel error1.25e-14 and maximum trial-norm error3.56e-14.
The self-pair fixture incorrectly used both distinct pair labels A,C for the
same physical vector while leaving some cross-slot table entries unfiltered.
The helper treats A,C as disjoint slots by design. The corrected self fixture
checks every entry on(w_A,a,Ka,d_A,Kd_A); all five disjoint-pair classes still
check every entry on the full eight-field table. No theorem formula, nominal,
norm, tolerance or genuine disjoint-pair table entry was changed. This is a
fixture correction, not evidence of a failed native Ward identity.
