"""skifer-snowflake — Skifer connector for Snowflake.

A connector implements the three Skifer core contracts and nothing else:

- **execution**: submit SQL, read a bounded result;
- **catalog**: resolve and describe relations;
- **publication**: create or replace a table or a view, with the platform's
  atomicity and permission rules stated explicitly.

It never carries business logic: the pipeline YAML is compiled once by the
Skifer core, rendered for this platform's SQL dialect, and handed over here.
"""

__version__ = "0.1.0.dev0"

__all__ = ["__version__"]
