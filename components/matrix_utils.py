import streamlit as st

def toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected):
    """Toggle the selection state of a matrix cell"""
    if is_selected:
        st.session_state.selected_cells[table_id]['selected_cell'] = None
    else:
        st.session_state.selected_cells[table_id]['selected_cell'] = (row_idx, col_idx)
    st.rerun()

def truncate_text(text, max_length):
    """Truncate text if it exceeds max_length"""
    return text[:max_length] + "..." if len(text) > max_length else text

def display_matrix_selected_values(table_data, table_id, table_type):
    """Display the currently selected values for matrix tables"""
    selected_cell = st.session_state.selected_cells[table_id].get('selected_cell')
    
    if selected_cell:
        row_idx, col_idx = selected_cell
        
        if table_type == "matrix_numeric":
            row_label = table_data['row_labels'][row_idx]
            col_label = table_data['col_labels'][col_idx]
            value = table_data['data'][row_idx][col_idx]
            st.write(f"**Selected**: Row {row_label}, Column {col_label} - Value: {value}")
            
        elif table_type == "matrix_color":
            row_label = table_data['row_labels'][row_idx]
            col_label = table_data['col_labels'][col_idx]
            color = table_data['data'][row_idx][col_idx]
            st.write(f"**Selected**: Row {row_label}, Column {col_label} - Color: {color}")
            
        elif table_type == "matrix_text":
            category = table_data['categories'][row_idx]
            col_names = ['CC1', 'CC2', 'CC3']
            col_name = col_names[col_idx]
            text = table_data[col_name][row_idx]
            st.write(f"**Selected**: {category} - {col_name}")
            st.write(text)
    else:
        st.write("No cell selected yet.")
        
