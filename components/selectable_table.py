import streamlit as st

def create_selectable_table(df, table_id):
    """
    Create a selectable table where user can select one cell per column
    
    Args:
        df (pandas.DataFrame): Data to display
        table_id (str): Unique identifier for the table
    """
    
    # Initialize table selection in session state
    if table_id not in st.session_state.selected_cells:
        st.session_state.selected_cells[table_id] = {}
    
    # Create columns for the table layout
    cols = st.columns([1] + [3] * (len(df.columns) - 1))  # First column narrower for metrics
    
    # Header row
    for idx, col_name in enumerate(df.columns):
        with cols[idx]:
            st.markdown(f"**{col_name}**")
    
    # Data rows
    for row_idx in range(len(df)):
        cols = st.columns([1] + [3] * (len(df.columns) - 1))
        
        for col_idx, col_name in enumerate(df.columns):
            with cols[col_idx]:
                cell_value = df.iloc[row_idx, col_idx]
                
                # Create unique key for each cell
                cell_key = f"{table_id}_{col_name}_{row_idx}"
                
                # Check if this cell is selected
                is_selected = st.session_state.selected_cells[table_id].get(col_name) == row_idx
                
                # Create button with different styling based on selection
                if col_name == 'Metrics':
                    # For metrics column, just display the number
                    if st.button(str(cell_value), key=cell_key, 
                               type="primary" if is_selected else "secondary"):
                        _toggle_cell_selection(table_id, col_name, row_idx, is_selected)
                else:
                    # For other columns, show truncated text
                    display_text = _truncate_text(str(cell_value), 80)
                    
                    if st.button(display_text, key=cell_key,
                               type="primary" if is_selected else "secondary",
                               help=str(cell_value)):  # Show full text on hover
                        _toggle_cell_selection(table_id, col_name, row_idx, is_selected)

def _toggle_cell_selection(table_id, col_name, row_idx, is_selected):
    """Toggle the selection state of a cell"""
    if is_selected:
        st.session_state.selected_cells[table_id][col_name] = None
    else:
        st.session_state.selected_cells[table_id][col_name] = row_idx
    st.rerun()

def _truncate_text(text, max_length):
    """Truncate text if it exceeds max_length"""
    return text[:max_length] + "..." if len(text) > max_length else text