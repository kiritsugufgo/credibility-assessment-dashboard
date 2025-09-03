import streamlit as st

from components.matrix_utils import toggle_matrix_cell_selection, truncate_text

def _create_text_matrix(table_data, table_id):
    """Create text matrix table (Table 4)"""
    categories = table_data['categories']
    
    # Create columns for CC1, CC2, CC3
    cols = st.columns([1, 3, 3, 3])
    
    # Headers
    with cols[0]:
        st.markdown("**RISK ASSESSMENT**")
    with cols[1]:
        st.markdown("**CC1**")
    with cols[2]:
        st.markdown("**CC2**") 
    with cols[3]:
        st.markdown("**CC3**")
    
    # Data rows
    for row_idx, category in enumerate(categories):
        cols = st.columns([1, 3, 3, 3])
        
        # Category label (G, Y, R)
        with cols[0]:
            color_map = {'G': '#4CAF50', 'Y': '#FFEB3B', 'R': '#F44336'}
            text_color = 'white' if category in ['G', 'R'] else 'black'
            st.markdown(f"<div style='background-color: {color_map.get(category, '#ccc')}; color: {text_color}; padding: 10px; text-align: center; font-weight: bold; border-radius: 4px;'>{category}</div>", unsafe_allow_html=True)
        
        # Text cells for each column
        for col_idx, col_name in enumerate(['CC1', 'CC2', 'CC3']):
            with cols[col_idx + 1]:
                cell_text = table_data[col_name][row_idx]
                cell_key = f"{table_id}_{row_idx}_{col_idx}"
                
                # Check if this cell is selected
                selected_cell = st.session_state.selected_cells[table_id]['selected_cell']
                is_selected = selected_cell == (row_idx, col_idx)
                
                # Truncate text for button display
                display_text = truncate_text(cell_text.replace('•', '').replace('\n', ' '), 60)
                
                if st.button(display_text, key=cell_key,
                           type="primary" if is_selected else "secondary",
                           help=cell_text):
                    toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected)
