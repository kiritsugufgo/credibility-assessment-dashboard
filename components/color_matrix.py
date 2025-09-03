import streamlit as st

from components.matrix_utils import toggle_matrix_cell_selection, truncate_text

def _create_color_matrix(table_data, table_id):
    """Create color matrix table (Table 3)"""
    row_labels = table_data['row_labels']
    col_labels = table_data['col_labels']
    data = table_data['data']
    row_title = table_data['row_title']
    col_title = table_data['col_title']
    
    # Color mapping
    color_map = {
        'green': '#4CAF50',
        'yellow': '#FFEB3B', 
        'red': '#F44336'
    }
    
    # Container with proper spacing
    st.markdown("<div style='margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Create main layout with row title on left
    main_cols = st.columns([1.5, 10])
    
    with main_cols[0]:
        # Row title - vertically centered
        st.markdown(f"""
        <div style='
            height: 25em;
            width: 2.5em; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-weight: bold; 
            font-size: 16px;
            background-color: #f0f0f0;
            border-radius: 5px;
            margin-right: 10px;
            color: #000000;
            writing-mode: vertical-lr;
            text-orientation: mixed;
        '>
            {row_title}
        </div>
        """, unsafe_allow_html=True)
    
    with main_cols[1]:
        # Matrix data with colored backgrounds
        for row_idx, row_label in enumerate(row_labels):
            cols = st.columns([1] + [1.2] * len(col_labels))
            
            # Row label
            with cols[0]:
                st.markdown(f"""
                <div style='
                    background-color: #f0f0f0; 
                    padding: 15px; 
                    text-align: center; 
                    font-weight: bold; 
                    border-radius: 5px; 
                    margin: 1px;
                    height: 50px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: #000000;
                '>
                    {row_label}
                </div>
                """, unsafe_allow_html=True)
            
            # Data cells with colored backgrounds
            for col_idx in range(len(col_labels)):
                with cols[col_idx + 1]:
                    cell_color = data[row_idx][col_idx]
                    cell_key = f"color_{table_id}_{row_idx}_{col_idx}"
                    
                    # Check if this cell is selected
                    selected_cell = st.session_state.selected_cells[table_id]['selected_cell']
                    is_selected = selected_cell == (row_idx, col_idx)
                    
                    bg_color = color_map.get(cell_color, '#ccc')
                    border_style = "3px solid #000000" if is_selected else "1px solid #333"
                    
                    # Create colored background container with transparent button
                    st.markdown(f"""
                    <div style='
                        background-color: {bg_color};
                        border: {border_style};
                        border-radius: 5px;
                        margin: 1px;
                        height: 50px;
                        position: relative;
                    '>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Overlay transparent button
                    if st.button(
                        label="",
                        key=cell_key,
                        help=f"Color: {cell_color}",
                        use_container_width=True
                    ):
                        toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected)
                    
                    # Style the button to be transparent and overlay on the colored background
                    st.markdown(f"""
                    <style>
                    div[data-testid="stButton"] > button[data-key="{cell_key}"] {{
                        background-color: transparent !important;
                        border: none !important;
                        height: 100% !important;
                        width: 100% !important;
                        position: absolute !important;
                        top: -55px !important;
                        left: 0 !important;
                        margin: 0 !important;
                        padding: 0 !important;
                        z-index: 10 !important;
                    }}
                    div[data-testid="stButton"] > button[data-key="{cell_key}"]:hover {{
                        background-color: rgba(255,255,255,0.2) !important;
                    }}
                    </style>
                    """, unsafe_allow_html=True)
        
        # Column labels row
        st.markdown("<div style='margin-top: 10px;'>", unsafe_allow_html=True)
        cols = st.columns([1] + [1.2] * len(col_labels))
        
        # Empty cell under row labels
        with cols[0]:
            st.markdown("")
        
        # Column labels
        for col_idx, col_label in enumerate(col_labels):
            with cols[col_idx + 1]:
                st.markdown(f"""
                <div style='
                    background-color: #f0f0f0; 
                    padding: 10px; 
                    text-align: center; 
                    font-weight: bold; 
                    border-radius: 5px; 
                    margin: 1px;
                    color: #000000;
                '>
                    {col_label}
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Column title at bottom
        st.markdown(f"""
        <div style='
            text-align: center; 
            margin-top: 15px; 
            font-weight: bold; 
            font-size: 16px;
            color: #000000;
        '>
            {col_title}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)