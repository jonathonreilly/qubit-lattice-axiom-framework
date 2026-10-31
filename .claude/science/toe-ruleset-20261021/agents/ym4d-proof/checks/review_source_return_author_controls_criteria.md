# Frozen-author mutation diagnostics, declared before execution

Six exact, independently saved mutants of source_return_exact.py at 0ea4e56c4c:
parametrix sign, Neumann product order, missing collar, common logdet half-factor,
omitted marked-right contribution, and reversed contour-side orientation.
Their expected scientific identities are independently derived in the review.
The first, second, third, and sixth should be rejected by the native checker.
The common half-factor is anticipated to survive because both author paths
share it; independent normalization is needed, and this survival is not hidden.
Whether the finite incidence example rejects a missing marked-right term is
an open sensitivity question; the independent star control separates the two
bounds mathematically. Save every output, status, and failure; do not repair
mutants to force rejection. The original exact baseline was already reproduced
by the coordinator and is not rerun here merely for bookkeeping.
