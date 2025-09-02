import streamlit as st
import pandas as pd

def create_summary_table(df, table_id):
    """
    Create 4 summary tables that update based on se    support_evidence_data = {
        'Credibility': ['Factor Ranking'],
        'Peer Review': [support_peer_review],
        'Acceptance': [support_acceptance],
        'Overall Score': [support_overall_score],
        'Ranking Level': [get_ranking_level(support_overall_score, "support_evidence")]
    }s from the main table
    """
    
    # Credibility ranges for determining ranking levels
    credibility_ranges_with_code = {
        "development": [
            {"range": (0.00, 0.09), "category": "Insufficient", "level": 4},
            {"range": (0.09, 0.29), "category": "Poor", "level": 3},
            {"range": (0.29, 0.43), "category": "Acceptable", "level": 2},
            {"range": (0.44, 1.00), "category": "Advanced", "level": 1}
        ],
        "use": [
            {"range": (0.00, 0.05), "category": "Insufficient", "level": 4},
            {"range": (0.06, 0.29), "category": "Poor", "level": 3},
            {"range": (0.29, 0.43), "category": "Acceptable", "level": 2},
            {"range": (0.43, 1.00), "category": "Advanced", "level": 1}
        ],
        "support_evidence": [
            {"range": (0.00, 0.32), "category": "Insufficient", "level": 4},
            {"range": (0.32, 0.43), "category": "Poor", "level": 3},
            {"range": (0.43, 0.665), "category": "Acceptable", "level": 2},
            {"range": (0.665, 1.00), "category": "Advanced", "level": 1}
        ],
        "overall_credibility": [
            {"range": (0.0000, 0.09), "category": "Highly credible results", "level": 1},
            {"range": (0.09, 0.139), "category": "Credible results", "level": 2},
            {"range": (0.14, 0.28), "category": "Slightly credible results", "level": 3},
            {"range": (0.28, 1.00), "category": "Not credible results", "level": 4}
        ]
    }
    
    credibility_ranges_no_code = {
        "development": [
            {"range": (0.0000, 0.14), "category": "Insufficient", "level": 4},
            {"range": (0.14, 0.29), "category": "Poor", "level": 3},
            {"range": (0.29, 0.43), "category": "Acceptable", "level": 2},
            {"range": (0.43, 1.00), "category": "Advanced", "level": 1}
        ],
        "use": [
            {"range": (0.00, 0.14), "category": "Insufficient", "level": 4},
            {"range": (0.14, 0.29), "category": "Poor", "level": 3},
            {"range": (0.29, 0.43), "category": "Acceptable", "level": 2},
            {"range": (0.43, 1.00), "category": "Advanced", "level": 1}
        ],
        "support_evidence": [
            {"range": (0.00, 0.32), "category": "Insufficient", "level": 4},
            {"range": (0.32, 0.43), "category": "Poor", "level": 3},
            {"range": (0.43, 0.665), "category": "Acceptable", "level": 2},
            {"range": (0.665, 1.00), "category": "Advanced", "level": 1}
        ],
        "overall_credibility": [
            {"range": (0.00, 0.089), "category": "Highly credible results", "level": 1},
            {"range": (0.09, 0.139), "category": "Credible results", "level": 2},
            {"range": (0.14, 0.279), "category": "Slightly credible results", "level": 3},
            {"range": (0.28, 1.00), "category": "Not credible results", "level": 4}
        ]
    }
    
    def get_ranking_level(score, table_type):
        """Determine ranking level based on score and table type"""
        if not score or score == '':
            return ''
        
        try:
            score_float = float(score)
            ranges_dict = credibility_ranges_with_code if has_code_readiness else credibility_ranges_no_code
            ranges = ranges_dict.get(table_type, [])
            
            for range_info in ranges:
                min_val, max_val = range_info["range"]
                if min_val <= score_float <= max_val:
                    return f"{range_info['level']} ({range_info['category']})"
            return ''
        except (ValueError, TypeError):
            return ''
    
    def extract_level_number(ranking_level):
        """Extract the numeric level from ranking level string like '1 (Advanced)'"""
        if not ranking_level or ranking_level == '':
            return None
        try:
            return int(ranking_level.split(' ')[0])
        except (ValueError, IndexError):
            return None
        
    def calculate_score(*values, divisor):
        if not all(values) or any(val == '' for val in values):
            return ''
        try:
            product = 1
            for val in values:
                product *= int(val)
            score = product / divisor
            return score
        except (ValueError, ZeroDivisionError):
            return ''
    
    def calculate_weighted_score(dev_level, use_level, support_level, divisor=64):
        """Calculate weighted score from ranking levels"""
        levels = [extract_level_number(level) for level in [dev_level, use_level, support_level]]
        if all(level is not None for level in levels):
            try:
                score = (levels[0] * levels[1] * levels[2]) / divisor
                return f"{score:.4f}"
            except ZeroDivisionError:
                return ''
        return ''
    
    # Initialize summary data in session state if not exists
    if 'summary_data' not in st.session_state:
        st.session_state.summary_data = {
            'development': {'Data Pedigree': '', 'Validation': '', 'Code Readiness': '', 'Models': ''},
            'use': {'Input Pedigree': '', 'Uncertainty': '', 'Sensitivity': ''},
            'support': {'History': '', 'Process': ''}
        }
    
    # Get summary data from session state or use defaults
    summary_data = getattr(st.session_state, 'summary_data', {
        'development': {'Data Pedigree': '', 'Validation': '', 'Code Readiness': '', 'Models': ''},
        'use': {'Input Pedigree': '', 'Uncertainty': '', 'Sensitivity': ''},
        'support': {'History': '', 'Process': ''}
    })
    
    #------------------------------------------------------------------------
    
    # Table 1: Development (1 row x 7 columns)
    st.subheader("Development")
    
    # Calculate Overall Score for Development
    dev_data_pedigree = summary_data['development'].get('Data Pedigree', '')
    dev_validation = summary_data['development'].get('Validation', '')
    dev_code_readiness = summary_data['development'].get('Code Readiness', '')
    dev_models = summary_data['development'].get('Models', '')

    has_code_readiness = bool(dev_code_readiness and dev_code_readiness != '')

    dev_overall_score = ''
    dev_ranking_level = ''
    
    if has_code_readiness:
        dev_overall_score = calculate_score(dev_data_pedigree, dev_validation, dev_code_readiness, dev_models, divisor=81)
    else:
        dev_overall_score = calculate_score(dev_data_pedigree, dev_validation, dev_models, divisor=27)
    
    dev_ranking_level = get_ranking_level(dev_overall_score, "development")
    
    development_data = {
        'Credibility': ['Factor Ranking'],
        'Data Pedigree': [dev_data_pedigree],
        'Validation': [dev_validation],
        'Code Readiness': [dev_code_readiness],
        'Models': [dev_models],
        'Overall Score': [dev_overall_score],
        'Ranking Level': [dev_ranking_level]
    }
    development_df = pd.DataFrame(development_data)
    st.dataframe(development_df, hide_index=True, use_container_width=True)
    
    #------------------------------------------------------------------------
    
    # Table 2: Use (1 row x 6 columns)
    st.subheader("Use")
    
    # Calculate Overall Score for Use
    use_input_pedigree = summary_data['use'].get('Input Pedigree', '')
    use_uncertainty = summary_data['use'].get('Uncertainty', '')
    use_sensitivity = summary_data['use'].get('Sensitivity', '')
    
    has_code_readiness = bool(dev_code_readiness and dev_code_readiness != '')
    
    use_overall_score = ''
    use_ranking_level = ''
    if has_code_readiness:
        use_overall_score = calculate_score(use_input_pedigree, use_uncertainty, use_sensitivity, divisor=27)
    else:
        use_overall_score = calculate_score(use_input_pedigree, use_uncertainty, use_sensitivity,divisor=27)
    use_ranking_level = get_ranking_level(use_overall_score, 'use')
    
    use_data = {
        'Credibility': ['Factor Ranking'],
        'Input Pedigree': [use_input_pedigree],
        'Uncertainty': [use_uncertainty],
        'Sensitivity': [use_sensitivity],
        'Overall Score': [use_overall_score],
        'Ranking Level': [use_ranking_level]
    }
    use_df = pd.DataFrame(use_data)
    st.dataframe(use_df, hide_index=True, use_container_width=True)
    
    #------------------------------------------------------------------------
    
    # Table 3: Support Evidence (1 row x 5 columns)
    st.subheader("Support Evidence")
    
    # Calculate Overall Score for Support Evidence
    support_history = summary_data['support'].get('History', '')
    support_process = summary_data['support'].get('Process', '')
    
    support_overall_score = ''
    support_ranking_level = ''
    if all([support_history, support_process]):
        try:
            support_overall_score = calculate_score(support_history, support_process, divisor=9)
        except (ValueError, ZeroDivisionError):
            support_overall_score = ''
    support_ranking_level = get_ranking_level(support_overall_score, "support_evidence")
    
    support_data = {
        'Credibility': ['Factor Ranking'],
        'History': [support_history],
        'Process Development': [support_process],
        'Overall Score': [support_overall_score],
        'Ranking Level': [support_ranking_level]
    }
    support_df = pd.DataFrame(support_data)
    st.dataframe(support_df, hide_index=True, use_container_width=True)
    
    #------------------------------------------------------------------------
    
    # Table 4: Credibility assessment (3 rows x 6 columns)Over
    st.subheader("Credibility assessment")
    
    # Calculate scores for all three rows using ranking levels
    dev_level_num = extract_level_number(dev_ranking_level)
    use_level_num = extract_level_number(use_ranking_level)
    support_level_num = extract_level_number(support_ranking_level)
    weighted_support_ranking_level = support_level_num * 0.5 if support_level_num is not None else ''
    
    not_weighted_score = calculate_score(dev_level_num, use_level_num, support_level_num, divisor=64)
    not_weighted_ranking_level = get_ranking_level(not_weighted_score, "overall_credibility") if not_weighted_score else ''
    weighted_score = not_weighted_score * 0.5 if not_weighted_score else ''
    weighted_ranking_level = get_ranking_level(weighted_score, "overall_credibility") if weighted_score else ''
    
    credibility_data = {
        'Phase': ['Not Weighted', 'Weight', 'Weighted'],
        'Development': [dev_ranking_level, 1, dev_level_num],
        'Use': [use_ranking_level, 1, use_level_num],
        'Support': [support_ranking_level, 0.5, weighted_support_ranking_level],
        'Overall Score': [not_weighted_score, '', weighted_score],
        'Credibility Level': [not_weighted_ranking_level, '', weighted_ranking_level]
    }
    
    credibility_df = pd.DataFrame(credibility_data)
    st.dataframe(credibility_df, hide_index=True, use_container_width=True)