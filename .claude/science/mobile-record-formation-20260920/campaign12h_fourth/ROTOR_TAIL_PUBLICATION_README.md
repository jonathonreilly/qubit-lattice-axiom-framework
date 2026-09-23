# Long-time behavior of the rotor second-formation clock

The exact eight-site rotor clock has rare long waits that its limiting
exponential mixture does not capture in higher moments. For a single
circulation input and a=eta-4delta nonzero, its survival satisfies

    S(t) ~ t^(-3/2)/(32 |a| sqrt(2 pi kappa)).

Its mean is 3/(8 kappa), while its second moment and variance are infinite.
This holds for both specified first-formation instruments. It is compatible
with uniform absolute convergence to the exponential mixture as eta grows;
that convergence does not justify exchanging the limit with moment integration.
At a=0 the clock instead has survival exp(-4 kappa t).

The [author argument](second_event_tail_author/ROTOR_CLOCK_LONG_TIME_TAIL_AND_MOMENTS.md)
derives the tail coefficient, its continuous-density qualification, and an
exact second-moment integral. A normalizable input is not enough to infer an
identical tail for every field density. The positive coefficient and density
hypotheses are part of the statement.

The [independent reconstruction](second_event_tail_independent/REPORT.md)
additionally obtains an exact Laplace law, positive-moment integrability
criteria, finite-variance field examples and an instrument-dependent
cancellation example. These are separately authored extensions. The
[source-bound comparison](second_event_tail_independent/COMPARISON.md)
confirms the original author's narrower formulas and every saved control
without importing the author builder. Both pre-comparison snapshots remain
unchanged. Frozen statements that comparison was pending are historical;
the completed comparison records current selective-check status.

The proof uses exact two-state Lyapunov equations and controlled small-frequency
integration. Matrix exponentials, angular excision and separately folded
frequency quadratures corroborate the proof. They are not certified numerical
tail bounds. [Root coverage](ROOT_TAIL_PUBLICATION_REVIEW.json) records the
complete arguments and controls read and the source identities authenticated.

This is the supplied unit-rotor target at fixed graph and nonzero fixed a.
No microscopic long-time approximation, joint finite-spin field limit,
volume limit or formal retained/audit status is asserted. The positive
finite-variance examples prevent a universal infinite-variance interpretation.

The [manifest](PUBLICATION_UNIT_ROTOR_TAIL.json) selects 30 byte-identical
source artifacts. From the repository root, verify the content identities with:

```sh
python3 .claude/science/mobile-record-formation-20260920/campaign12h_fourth/verify_rotor_tail_publication.py
```

This read-only verifier authenticates files and portable dependency bindings;
it does not rerun or replace the scientific derivations. Reproduce runners in
a fresh copied packet because the saved evidence is intentionally immutable.
