# Historical evidence

source_evidence.tar.gz preserves the original byte sequences listed in INDEX.json. It contains root and focused independent derivations, source snapshots, attempted runs, reading scopes, corrections and failures. Its paths are relative to the original campaign pack. These historical scripts and stdout are provenance; they are not canonical runner caches or new empirical observations.

To inspect, decompress the archive into an empty temporary directory with Python tarfile using filter="data", then check each extracted byte hash against INDEX.json. The complete current calculation is reproduced independently of this archive by scripts/scalar_metric_inverse.py and its ten imported helpers. The original numerical matrix-index failure, boolean serialization failure, mixed-Subs comparison failure and canonical note's superseded local-kernel wording remain visible. Historical absolute paths identify execution locations and are not required by the current primary.
