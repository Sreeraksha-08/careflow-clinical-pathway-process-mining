# CareFlow Process Mining Module

## Owner

Sree Raksha D S

## Role

Member 3 — Process Mining Engine Lead (PM4Py) and Team Lead

## Purpose

This module analyzes simulated Emergency Room event logs to discover patient-flow patterns and identify operational bottlenecks.

## Main Responsibilities

- Load and validate standardized event logs.
- Discover patient-flow processes using PM4Py.
- Generate a Directly-Follows Graph.
- Analyze process variants and bottlenecks.
- Perform conformance checking against an ideal patient journey.
- Evaluate the discovered process.

## Expected Event Log Fields

- "case_id"
- "activity_name"
- "timestamp"
- "resource"
- "department"
- "age_group"

## Technology

- Python
- PM4Py
- pandas
- Graphviz
- pytest

## Data Privacy

Only simulated hospital data will be used. Do not commit real patient records, passwords, API keys, or cloud credentials.