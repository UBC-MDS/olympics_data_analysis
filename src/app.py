import pandas as pd
import numpy as np
import altair as alt

data = pd.read_csv("../data/processed/athlete_events_2000.csv")
# World map 



















# Gender/medal plot





























# Age plot

def create_age_plot(data, year=None, sport=None, sex=None, season=None):
    """
    Filters for selected features and creates the 'age' vs 'medals received' bar chart.
    Parameters
    ----------
    data : pd.DataFrame
        pandas dataframe containing the olympics data
    year : int
        the year to filter the data by
    sport: str
        the sport to filter the data by
    sex: str
        the biological sex to filter the data by
    season: str
        the olympic season to filter the data by (Summer or Winter)
    
    Returns
    -------
    alt.Chart
        the plot showing the medals received distributed by age, filtered for the selected features
    Examples
    --------
    >>> create_age_plot(data, year=2014, sport="Ice Hockey", sex="Male", season="Winter")
    >>> create_age_plot(data, year=2014, season="Summer")
    """
    
    
    if not isinstance(year, int) and year is not None:
        raise TypeError("year should be of type 'int'")
    if not isinstance(sport, str) and sport is not None:
        raise TypeError("sport should be of type 'str'")
    if not isinstance(sex, str) and sex is not None:
        raise TypeError("sex should be of type 'str'")
    if not isinstance(season, str) and season is not None:
        raise TypeError("season should be of type 'str'")
    
    if year is not None:
        data = data[data["Year"] == year]
    if sport is not None:
        data = data[data["Sport"] == sport]
    if sex is not None:
        data = data[data["Sex"] == sex]
    if season is not None:
        data = data[data["Season"] == season]
        
    hist = (alt.Chart(data, title="Number of medals received distributed by age").mark_bar(size=6.5).encode(
        x=alt.X("Age", title="Age (Years)"),
        y=alt.Y("count()", title="Number of medals received")
    )).configure_axis(grid=False).configure_view(
    strokeWidth=0
)
    return hist