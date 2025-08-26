# Credibility Assessment Dashboard

A Streamlit-based dashboard for conducting credibility assessment and simulation risk assessment. This interactive tool helps evaluate the credibility of modeling and simulation (M&S) results through a systematic assessment framework.

## Features

- **Credibility Assessment Criteria**: Interactive table for selecting assessment factors across multiple categories (Data Pedigree, Validation, Code Readiness, Models, etc.)
- **Matrix-based Risk Assessment**: Visual matrices for evaluating design solutions vs M&S credibility and decision consequences vs simulation influence
- **Automated Calculations**: Real-time calculation of overall scores and ranking levels based on user selections
- **Summary Tables**: Dynamic summary tables that update based on user inputs, showing Development, Use, Support Evidence, and overall Credibility assessment

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- Pandas

### Installation

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirement.txt
   ```

### Running the Dashboard

To start the dashboard, run the following command in your terminal:

```bash
streamlit run main.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## Usage

1. Navigate through the different assessment tables
2. Click on cells to make selections (one per column for detailed tables, single cell for matrix tables)
3. View real-time updates in the summary tables
4. Review the calculated credibility levels and risk assessments
