import streamlit as st
import pandas as pd
from data.table_data import get_table_data, get_table_type
from components.selectable_table import create_selectable_table
from components.summary_table import create_summary_table
from components.matrix_table import create_matrix_table, display_matrix_selected_values

def run_dashboard():
    """Main function to run the Streamlit dashboard"""
    st.set_page_config(page_title="Credibility Assessment Dashboard", layout="wide")
    
    st.title("Credibility Assessment Dashboard")
    st.markdown("---")
    
    # Initialize session state for selected cells if not exists
    if 'selected_cells' not in st.session_state:
        st.session_state.selected_cells = {}
    
    # Table 1: Detailed Credibility Assessment Criteria
    st.subheader("Table 1: Credibility Assessment Criteria")
    st.markdown("*Click on cells to select them (one per column)*")
    
    table1_data = get_table_data("table1")
    df = pd.DataFrame(table1_data)
    create_selectable_table(df, "table1")
    update_summary_tables_from_selections(df, "table1")  # Update summary tables based on selections
    #display_selected_values(df, "table1")
    
    create_summary_table(df, "summary_table1")
    
    # Calculate button
    st.markdown("---")
    if st.button("🧮 Calculate Credibility Assessment", type="primary"):
        st.info("Calculate function will be implemented in the next step!")
    
    st.markdown("---")
    
    # Table 2: Design Solution vs M&S Credibility Matrix
    st.subheader("Table 2: Design Solution vs M&S Credibility Matrix")
    st.markdown("*Click on a cell to select it*")
    
    table2_data = get_table_data("table2")
    create_matrix_table(table2_data, "table2", "matrix_numeric")
    
    st.markdown("### Selected Values:")
    display_matrix_selected_values(table2_data, "table2", "matrix_numeric")
    
    st.markdown("---")
    
    # Table 3: Decision Consequence vs Simulation Influence Matrix
    st.subheader("Table 3: Decision Consequence vs Simulation Influence Matrix")
    st.markdown("*Click on a cell to select it*")
    
    table3_data = get_table_data("table3")
    create_matrix_table(table3_data, "table3", "matrix_color")
    
    st.markdown("### Selected Values:")
    display_matrix_selected_values(table3_data, "table3", "matrix_color")
    
    st.markdown("---")
    
    # Table 4: Risk Assessment Matrix
    st.subheader("Table 4: Risk Assessment Categories")
    st.markdown("*Click on a cell to select it*")
    
    table4_data = get_table_data("table4")
    create_matrix_table(table4_data, "table4", "matrix_text")
    
    st.markdown("### Selected Values:")
    display_matrix_selected_values(table4_data, "table4", "matrix_text")
    

def display_selected_values(df, table_id):
    """Display the currently selected values for Table 1"""
    st.markdown("### Selected Values:")
    if st.session_state.selected_cells.get(table_id):
        for col, row_idx in st.session_state.selected_cells[table_id].items():
            if row_idx is not None:
                value = df.iloc[row_idx][col]
                metric_value = df.iloc[row_idx]['Metrics']
                display_text = f"**{col}**: Row {metric_value} - {value[:50]}..." if len(str(value)) > 50 else f"**{col}**: Row {metric_value} - {value}"
                st.write(display_text)
    else:
        st.write("No cells selected yet.")

def update_summary_tables_from_selections(df, table_id):
    """Update summary tables based on selected cells in the selectable table"""
    if table_id not in st.session_state.selected_cells:
        return
    
    # Initialize summary data in session state if not exists
    if 'summary_data' not in st.session_state:
        st.session_state.summary_data = {
            'development': {'Data Pedigree': '', 'Validation': '', 'Code Readiness': '', 'Models': ''},
            'use': {'Input Pedigree': '', 'Uncertainty': '', 'Sensitivity': ''},
            'support': {'History': '', 'Process': ''}
        }
    
    # Column mapping from selectable table to summary tables
    column_mapping = {
        'Data Pedigree': ('development', 'Data Pedigree'),
        'Validation': ('development', 'Validation'),
        'Code readiness only for in house software': ('development', 'Code Readiness'),
        'Models': ('development', 'Models'),
        'Input pedigree': ('use', 'Input Pedigree'),
        'Uncertainty': ('use', 'Uncertainty'),
        'Sensitivity': ('use', 'Sensitivity'),
        'History': ('support', 'History'),
        'Process development': ('support', 'Process')
    }
    
    # Update summary data based on selections
    selections = st.session_state.selected_cells[table_id]
    for col, row_idx in selections.items():
        if row_idx is not None and col in column_mapping:
            table_name, summary_col = column_mapping[col]
            # Get the actual metric value from the dataframe
            metric_value = df.iloc[row_idx]['Metrics']
            st.session_state.summary_data[table_name][summary_col] = str(metric_value)