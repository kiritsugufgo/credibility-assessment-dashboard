import streamlit as st

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

def _create_numeric_matrix(table_data, table_id):
    """Create numeric matrix table (Table 2)"""
    row_labels = table_data['row_labels']
    col_labels = table_data['col_labels']
    data = table_data['data']
    row_title = table_data['row_title']
    col_title = table_data['col_title']
    
    # Create container with proper spacing
    st.markdown("<div style='margin: 20px 0;'>", unsafe_allow_html=True)
    
    # Add CSS for better text visibility in buttons
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
                        _toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected)
        
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

def _create_color_matrix(table_data, table_id):
    """Create color matrix table (Table 3)"""
    row_labels = table_data['row_labels']
    col_labels = table_data['col_labels']
    data = table_data['data']
    row_title = table_data['row_title']
    col_title = table_data['col_title']
    
    # Color mapping
    color_styles = {
        'green': 'background-color: #4CAF50; color: white;',
        'yellow': 'background-color: #FFEB3B; color: black;',
        'red': 'background-color: #F44336; color: white;'
    }
    
    # Create the matrix layout
    cols = st.columns([2] + [1.5] * len(col_labels))
    
    # Empty top-left cell and column headers
    with cols[0]:
        st.markdown("")
    
    for col_idx, col_label in enumerate(col_labels):
        with cols[col_idx + 1]:
            st.markdown(f"**{col_label}**")
    
    # Data rows with row labels
    for row_idx, row_label in enumerate(row_labels):
        cols = st.columns([2] + [1.5] * len(col_labels))
        
        # Row label
        with cols[0]:
            st.markdown(f"**{row_label}**")
        
        # Data cells
        for col_idx in range(len(col_labels)):
            with cols[col_idx + 1]:
                cell_color = data[row_idx][col_idx]
                cell_key = f"{table_id}_{row_idx}_{col_idx}"
                
                # Check if this cell is selected
                selected_cell = st.session_state.selected_cells[table_id]['selected_cell']
                is_selected = selected_cell == (row_idx, col_idx)
                
                # Create colored button
                button_style = color_styles.get(cell_color, '')
                if is_selected:
                    button_style += ' border: 3px solid #000000;'
                
                # Use HTML button with custom styling
                button_html = f"""
                <button style='{button_style} padding: 10px; margin: 2px; border: 2px solid #ccc; border-radius: 4px; cursor: pointer; width: 100%;' 
                        onclick='document.querySelector("[data-testid=\\"stButton\\"] button").click()'>
                    &nbsp;
                </button>
                """
                
                if st.button(" ", key=cell_key, help=f"Color: {cell_color}"):
                    _toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected)
    
    # Add axis labels
    st.markdown(f"<div style='text-align: center; margin-top: 10px;'><strong>{col_title}</strong></div>", unsafe_allow_html=True)

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
                display_text = _truncate_text(cell_text.replace('•', '').replace('\n', ' '), 60)
                
                if st.button(display_text, key=cell_key,
                           type="primary" if is_selected else "secondary",
                           help=cell_text):
                    _toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected)

def _toggle_matrix_cell_selection(table_id, row_idx, col_idx, is_selected):
    """Toggle the selection state of a matrix cell"""
    if is_selected:
        st.session_state.selected_cells[table_id]['selected_cell'] = None
    else:
        st.session_state.selected_cells[table_id]['selected_cell'] = (row_idx, col_idx)
    st.rerun()

def _truncate_text(text, max_length):
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