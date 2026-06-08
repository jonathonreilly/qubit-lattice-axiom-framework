# Route Portfolio

1. Run full H=0.25 `true_kubo` replay.
   Result: avoided; the exact-edge factorization replays the same fine-H values without the full expensive truth harness.

2. Stream the H=0.25 edge coefficients.
   Result: implemented. It verifies exact-edge replay, monopole cancellation, finite support, and controls.

3. Prove exact dipole asymptotics.
   Result: not supported by fine-H data. The H=0.25 signed large-b slope is about `-2.36`, so the exact order remains open.
