import streamlit as st

from components.matrix_utils import toggle_matrix_cell_selection, truncate_text

def _create_numeric_matrix(table_data, table_id):
    """Create numeric matrix table (Table 2)"""
    row_labels = table_data['row_labels']
    col_labels = table_data['col_labels']
    data = table_data['data']
    row_title = table_data['row_title']
    col_title = table_data['col_title']
    
    # Container with proper spacing
    st.markdown("<div style='margin: 20px 0;'>", unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    /* Make text in secondary buttons dark and bold */
    div[data-testid="stButton"] > button[kind="secondary"] {
        color: #000000 !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        border: 2px solid #cccccc !important;
    }
    
    /* Ensure primary buttons remain visible */
    div[data-testid="stButton"] > button[kind="primary"] {
        color: #ffffff !important;
        font-weight: bold !important;
        height: 100% !important;
        width: 100% !important;
    }
    
    /* Remove gaps between elements */
    .stHorizontalBlock {
        gap: 0rem !important;
    }
    
    # .stVerticalBlock {
    #     gap: 0rem !important;
    # }
    
    .stColumn {
        gap: 0rem !important;
        padding: 0rem !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Create main layout with row title on left
    main_cols = st.columns([1.5, 10])  # Left column for row title, right for matrix
    
    with main_cols[0]:
        # Row title - vertically centered and rotated
        st.markdown(f"""
        <div style='
            height: 200px; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-weight: bold; 
            font-size: 16px;
            background-color: #f0f0f0;
            border-radius: 5px;
            margin-right: 10px;
            color: #000000;
        '>
            {row_title}
        </div>
        """, unsafe_allow_html=True)
    
    with main_cols[1]:
        # Matrix data
        for row_idx, row_label in enumerate(row_labels):
            cols = st.columns([1] + [1.2] * len(col_labels))
            
            # Row label
            with cols[0]:
                st.markdown(f"""
                <div style='
                    background-color: #f0f0f0; 
                    padding: 10px; 
                    text-align: center; 
                    font-weight: bold; 
                    border-radius: 5px; 
                    margin: 2px;
                    height: 35px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: #000000;
                '>
                    {row_label}
                </div>
                """, unsafe_allow_html=True)
            
            # Data cells
            for col_idx in range(len(col_labels)):
                with cols[col_idx + 1]:
                    cell_value = data[row_idx][col_idx]
                    cell_key = f"{table_id}_{row_idx}_{col_idx}"
                    
                    # Check if this cell is selected
                    selected_cell = st.session_state.selected_cells[table_id]['selected_cell']
                    is_selected = selected_cell == (row_idx, col_idx)
                    
                    if st.button(str(cell_value), key=cell_key,
                               type="primary" if is_selected else "secondary"):
                        toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected)
        
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
                    margin: 2px;
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