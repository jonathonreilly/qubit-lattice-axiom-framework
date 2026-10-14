# Recover original reviewed bytes

SOURCE_DISPOSITION_v1.json lists every constituent path and original SHA256.
Direct source_recovery files are byte-identical. For an archival entry decode
its base64 from ARCHIVAL_BYTES_v1.json into a separate empty directory and
verify both byte count and SHA256 before use. Never overwrite an unknown file.
DISPLAY files have patch-compatible whitespace and are explicitly not the
reviewed originals. Canonical code does not import any historical runner.
Primary paper render/text files remain at their listed local recovery paths.
