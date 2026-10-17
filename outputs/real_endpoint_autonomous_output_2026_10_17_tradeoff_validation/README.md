# T30 refinement evidence

This supplements the original PR9668 validation without replacing its history.
Canonical execution passed 179 scoped arithmetic checks and the 49-input integrity check, exit 0, 0.08790898323059082 seconds inside the runner wrapper. Full scientific stdout (49,849 bytes) is preserved in CANONICAL_RESULT.json and the canonical runner cache; outer wrapper stdout is only its receipt. Thirteen new mathematical mutations each failed at their intended check under Python -O after input integrity passed. Previous 25 mathematical and four integrity mutations remain historical evidence, not newly rerun results.

The prelaunch records bind the runtime binary/version, runner, helper, wrapper and inputs. CPU limit 10 seconds, file limit 16 MiB; canonical inner/outer wall limits 30/45 seconds and mutation wall limits 10 seconds. No memory cap. No large matrix, spectral integral or apparatus dynamics was executed. Scalar checks corroborate constants and fixtures; separate source reviews address the analytical arguments, with their stated same-model/source-exposed limitations. No retained audit or combined-main pipeline is claimed.

Historical executable sources have .py.txt suffixes and are provenance, not runtime helpers. Scratch copies are excluded; complete mutation streams and receipts are included. The integration review pins the note before the final execution-evidence paragraph was appended; that later paragraph changes reporting only.
