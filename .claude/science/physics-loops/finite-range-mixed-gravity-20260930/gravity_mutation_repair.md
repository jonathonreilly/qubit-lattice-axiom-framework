The initial cochain commutator mutation was not detected because the fixture
used I=E00,J=E11 on a directed cycle, so J d I=0 and changing its sign made
no mathematical change. Preserved original mutation results/logs in
`gravity-milestone-mutations-initial-nondetecting`. Strengthened the fixture to
J=E11+E44, where both products are nonzero. This is a test-fixture repair,
not a theorem/source-proof change. All eight mutations are rerun against the
new source; only that final evidence can claim complete mutation coverage.
The earlier expanded-versus-factored scalar assertion failure is preserved in
`gravity_candidate_control.log`, with corrected successful control log separate.
