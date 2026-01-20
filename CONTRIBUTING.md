<!--
SPDX-License-Identifier: CC0-1.0
SPDX-FileCopyrightText: none
-->

# Contributing to Transitous

Thank you for your interest in contributing!

For detailed instructions on adding a region, see the [Project Documentation](https://transitous.org/doc/#adding-a-region).

## Validation

Feed files are automatically validated against a JSON schema in CI via GitHub Actions.
No local setup is required—errors will be caught when you open a pull request.

### Local validation (optional)

For faster feedback before pushing, you can validate files locally using [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema):

```bash
# Install (requires Python/pipx)
pipx install check-jsonschema

# Validate a single file
check-jsonschema --schemafile schemas/transitous-region-feed.json feeds/<region>.json

# Validate all feed files
check-jsonschema --schemafile schemas/transitous-region-feed.json feeds/*.json
```

### Pre-commit hook (optional)

For automated validation before each commit:

```bash
pipx install pre-commit
pre-commit install
```

This will automatically validate region files when you run `git commit`.
