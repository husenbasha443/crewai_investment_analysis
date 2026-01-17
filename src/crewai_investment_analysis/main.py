from crewai_investment_analysis.crew import CrewaiInvestmentAnalysis

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': "Gold ETF for conservative investors"
    }

    try:
        CrewaiInvestmentAnalysis().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")