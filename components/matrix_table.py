import streamlit as st

from components.color_matrix import _create_color_matrix
from components.numeric_matrix import _create_numeric_matrix
from components.text_matrix import _create_text_matrix

def create_matrix_table(table_data, table_id, table_type):
    """
    Create a matrix-style selectable table
    
    Args:
        table_data (dict): Table data
        table_id (str): Unique identifier for the table
        table_type (str): Type of matrix table (matrix_numeric, matrix_color, matrix_text)
    """
    
    # Initialize table selection in session state
    if table_id not in st.session_state.selected_cells:
        st.session_state.selected_cells[table_id] = {}
        st.session_state.selected_cells[table_id]['selected_cell'] = None
    
    if table_type == "matrix_numeric":
        _create_numeric_matrix(table_data, table_id)
    elif table_type == "matrix_color":
        _create_color_matrix(table_data, table_id)
    elif table_type == "matrix_text":
        _create_text_matrix(table_data, table_id)
