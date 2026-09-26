# Execution history

The first checker attempt was interrupted with SIGINT after more than six minutes because SymPy expanded a redundant six-variable linear cancellation before grouping the coefficients. Its source SHA-256 was `1ca8aa162584d9c4118ef15ea1cf28d5e621e9fc48f134300b2c6065425e0a04`. The full interrupt traceback is preserved in INTERRUPTED_SYMBOLIC_ATTEMPT.log. Earlier symbolic identities had completed without an assertion failure. The correction groups the coefficient matrix before multiplying arbitrary derivative symbols; it changes neither the identity nor the model. A results read attempted while this process was still running found no RESULTS.json; no partial output was treated as verification.

The final complete run is preserved separately in RUN.log and RESULTS.json.
