def get_table_data(table_name):
    """
    Retrieve data for a specific table
    
    Args:
        table_name (str): Name of the table to retrieve
        
    Returns:
        dict: Table data
    """
    tables = {
        "table1": {
            'Metrics': [1, 2, 3],
            'Data Pedigree': [
                'All key data available with poor accuracy, precision and traceability (e.g scope, boundary conditions, drawings, ...)',
                'All key data known. Significant data with acceptable accuracy, precision and traceability',
                'All key data known with acceptable accuracy, precision and traceability'
            ],
            'Validation': [
                'Expert judgment only\n\nConceptual model addresses problem statement\n\nComparison with measurements from similar systems or applications',
                'Key simulation outputs agree with data from the component/system operating in a representative environment (e.g., rig test)\n\nRCA partly validated by measurement',
                'Key simulation outputs agree with data from the component/system operating in a real environment (e.g. field test) over the full range of operation.\n\nRCA fully validated by measurement'
            ],
            'Code readiness only for in house software': [
                'Expert judgment only\n\nMinimal testing of software elements',
                'Some algorithms are tested to determine if they satisfy requirements\n\nSome features & capabilities are tested with benchmark solutions\n\nSome peer review conducted.',
                'All algorithms are tested to determine if they satisfy requirements\n\nAll features and capabilities are tested with rigorous benchmark solutions\n\nIndependent peer review conducted'
            ],
            'Models': [
                'Empirical models further specialized or calibrated to represent target',
                'Physics-based model for some of most important processes.\n\nRepresentation and geometric fidelity: coarser without significant defeaturing',
                'Established physics-based models\n\nRepresentation and geometric fidelity: High fidelity representation consistent with the "as built", with little to no defeaturing simplification'
            ],
            'Input pedigree': [
                'All key data available with poor accuracy, precision (e.g operational data, ...)',
                'All key data known. Significant data with acceptable accuracy, precision and traceability',
                'All key data known with acceptable accuracy, precision and traceability'
            ],
            'Uncertainty': [
                'Only deterministic analyses are conducted\n\nUncertainties in model results are not addressed',
                'Most sources of uncertainty identified and, at best, qualitatively assessed. Uncertainty is assessed only for most important model results.\n\nMedium/moderate safety factor compensates results uncertainty',
                'Uncertainty of results is provided quantitatively through propagation of the relevant uncertainty sources. High safety factor compensates results uncertainty'
            ],
            'Sensitivity': [
                'Sensitivities of model input are not addressed. No clear identification of the main sources of uncertainty in the model outputs and the model inputs.\n\nQualitative estimates only for sensitivities in modelling and simulations',
                'Sensitivities known for main parameters. Sensitivities of model input addressed. Correlation identified between uncertainty in the model outputs and the most important model inputs.',
                'Sensitivities known for main parameters. Sensitivities of model input addressed. Correlation identified between uncertainty in the model outputs and all the model inputs.\n\nMost key sensitivities identified.'
            ],
            'History': [
                'New model or major changes in model, or major differences in model use.',
                'At most moderate changes in model and most moderate differences in model use.',
                'At most minor changes in model and minor refinement in model use.'
            ],
            'Process development': [
                'Ad hoc simulation only, no simulation guideline available',
                'Calculation process defined',
                'Calculation guideline done and methods understood'
            ]
        },
        "table2": {
            'row_labels': ['4', '3', '2', '1'],
            'col_labels': ['1', '2', '3', '4'],
            'row_title': 'DESIGN SOLUTION',
            'col_title': 'M&S credibility / maturity',
            'data': [
                [2, 3, 4, 4],
                [2, 2, 3, 4],
                [1, 2, 2, 3],
                [1, 1, 2, 2]
            ]
        },
        "table3": {
            'row_labels': ['1', '2', '3', '4'],
            'col_labels': ['1', '2', '3', '4'],
            'row_title': 'DECISION CONSEQUENCE',
            'col_title': 'SIMULATION INFLUENCE',
            'data': [
                ['green', 'green', 'green', 'yellow'],
                ['green', 'green', 'green', 'yellow'],
                ['green', 'yellow', 'yellow', 'red'],
                ['yellow', 'yellow', 'red', 'red']
            ]
        },
        "table4": {
            'categories': ['G', 'Y', 'R'],
            'CC1': [
                '• The risk of virtual validation is acceptable\n• Opportunities for improvement in M&S credibility',
                '• Design solution to be validated by simulation and physical test\n• Improvement in M&S credibility\n• Skip of physical test with approval escalation for risk acceptance',
                '• The risk of virtual validation implementation is not acceptable\n• M&S credibility to be improved'
            ],
            'CC2': [
                '• The risk of virtual validation is acceptable',
                '• Design solution to be validated by simulation and physical test\n• Opportunities for improvement in M&S credibility',
                '• Design solution to be validated by simulations and physical test\n• M&S credibility to be improved'
            ],
            'CC3': [
                '• The risk of virtual validation is acceptable',
                '• The risk of virtual validation is acceptable\n• Opportunities for improvement in M&S credibility',
                '• Skip of physical test with approval escalation for risk acceptance\n• Opportunities for improvement in M&S credibility'
            ]
        }
    }
    
    return tables.get(table_name, {})

def get_all_table_names():
    """Return list of all available table names"""
    return ["table1", "table2", "table3", "table4"]

def get_table_type(table_name):
    """
    Get the type of table for different rendering
    
    Args:
        table_name (str): Name of the table
        
    Returns:
        str: Type of table (detailed, matrix_numeric, matrix_color, matrix_text)
    """
    table_types = {
        "table1": "detailed",
        "table2": "matrix_numeric", 
        "table3": "matrix_color",
        "table4": "matrix_text"
    }
    return table_types.get(table_name, "detailed")