# Mutation Plan

Stage A mutations must independently trigger at least:

1. four rather than five trail colours;
2. acceptance of two next-colour neighbours;
3. omission of torus wrap edges;
4. deduplication of width-two parallel darts;
5. omission of a reachable Block 220 ancestry stack;
6. retuning after held-width inspection;
7. treating an anchor as a permanent Record;
8. allowing commit beside an anchor;
9. hidden root identity or coordinate data;
10. an undeclared extra normal-direction state.

Later stages add false-commit, opposite-commit, rollback, ABA, lost-dart,
fair-MEC, covariance, projector-completeness and projective-phase mutations.
The independent consumer must use a distinct implementation and nonidentical
mutation hooks.
