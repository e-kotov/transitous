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

### License validation (optional)

License compliance is checked using the [REUSE tool](https://reuse.software/).

```bash
# Install (requires Python/pipx)
pipx install reuse

# Check for license compliance
reuse lint
```

### Automated validation with pre-commit (optional)

For contributors who prefer automated local checks, the repository includes a [pre-commit](https://pre-commit.com/) configuration:

```bash
pipx install pre-commit
pre-commit install
```

This will automatically check for license compliance and validate region files before each commit.
