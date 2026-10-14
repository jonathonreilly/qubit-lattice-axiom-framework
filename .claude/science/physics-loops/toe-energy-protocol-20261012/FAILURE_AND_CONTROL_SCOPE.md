# Failure and control scope

The proposed driver fails on source/package membership or byte drift, changed
root review coverage, wrong HEAD/branch or stack-parent head, an unclean or
partially installed checkout, parent/procedure changes, unexpected graph nodes
or edges, altered old graph objects, broken local links, vocabulary findings,
unclassified whitespace, unexpected corruption-error reasons, stale caches,
or staged blob/footprint drift. It does not silently retry or repair sources.

Every launched command records argv, cwd, timeout, actual exit code, full
stdout/stderr and timestamps. Cache API calls retain raw inner/outer returns,
the complete available merged child stream and the exact written cache.
On failure the driver saves a traceback and evidence manifest without rolling
back partial installation or rewriting accepted sources. Root inspects the
failure and plans any recovery separately; a second prepare refuses to
overwrite partial work. Immutable packages are revised under new identities.

Byte-corruption controls are isolated and follow successful canonical
baselines. Exact expected failures concern archive bytes, published bytes,
publication metadata and parent bytes. No mathematical negation or scientific
failure follows from them. At preparation freeze none had been run.
