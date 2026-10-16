# CareFlow Dashboard — Static Sample Layout

**Day:** 3  
**Purpose:** Draft a static dashboard layout using dummy data.  
**BI Tool:** Power BI (Primary), Looker Studio (Fallback)

> **Note:** All values below are illustrative dummy data for layout demonstration only. They are not actual patient results.

## 1. Overview

### KPI Cards — Dummy Data

| KPI | Sample Value |
|---|---:|
| Total Patient Cases | 120 |
| Total Recorded Events | 840 |
| Average Case Duration | 4.5 hours |
| Average Waiting Time | 35 minutes |
| Loop-back Rate | 12% |
| Conformance Rate | 88% |

### Suggested Visuals
- KPI cards for the six metrics above.
- Bar chart comparing case counts by department.
- Before vs After comparison chart.
- Filters for Department and Age Group.

## 2. Process Map

### Sample Patient Journey

Registration → Triage → X-Ray → Treatment → Discharge

### Suggested Visuals
- Process map showing activity transitions.
- Activity frequency chart.
- Transition count chart.
- Department and Age Group filters.

## 3. Bottlenecks

### Sample Waiting-Time Data

| Transition | Dummy Average Waiting Time |
|---|---:|
| Registration → Triage | 10 minutes |
| Triage → X-Ray | 25 minutes |
| X-Ray → Treatment | 40 minutes |
| Treatment → Discharge | 15 minutes |

### Suggested Visuals
- Bar chart of average waiting time by transition.
- Highlight the transition with the longest sample wait.
- Display X-Ray → Triage loop-back rate.
- Show possible loop-back reasons when data is available.

## 4. Conformance

### Sample Conformance Data

| Measure | Dummy Value |
|---|---:|
| Total Cases | 120 |
| Compliant Cases | 106 |
| Non-compliant Cases | 14 |
| Conformance Rate | 88.3% |

### Suggested Visuals
- Compliant vs Non-compliant cases.
- Conformance percentage card.
- Table of deviations from the ideal clinical pathway.

## 5. Layout and Filters

- Top section: dashboard title and filters.
- First row: KPI cards.
- Middle section: process map and activity charts.
- Bottom section: bottleneck analysis and conformance summary.
- Filters: Department, Age Group, and Before/After period.

## 6. Data and Validation Notes

- Dummy values are used only to demonstrate the layout.
- Replace dummy values with validated project data when available.
- Confirm KPI calculations with the team before publishing final results.
- This document describes a proposed static layout; it is not a live dashboard.