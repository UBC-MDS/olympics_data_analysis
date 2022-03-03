import pandas as pd
import numpy as np
import altair as alt

data = pd.read_csv("../data/processed/athlete_events_2000.csv")
# World map 

def create_world_plot(data, year=None, sport=None, sex=None, season=None):
    """
    Filters for selected features and creates the 'country' vs 'medals won' plot.
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
        the plot showing the medals received distributed by country, filtered for the selected features
    Examples
    --------
    >>> create_world_plot(data, year=2014, sport="Ice Hockey", sex="Male", season="Winter")
    >>> create_world_plot(data, year=2014, season="Summer")
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
        
    data_2 = data[['NOC', 'Medal', 'Year', 'Sport', 'Season', 'Sex']].groupby(
    ['NOC', 'Year', 'Sport', 'Season', 'Sex']).agg(
    'count').reset_index().rename(columns = {'Medal': 'medals'})
    
    country_ids = pd.read_csv('../data/processed/country-ids.csv')
    
    noc = pd.read_csv("../data/processed/noc_regions.csv")
    noc = noc[['NOC', 'region']]
    
    country_noc_ids = noc.merge(country_ids, how='inner', left_on='region', right_on='name')
    country_noc_ids = country_noc_ids[country_noc_ids["NOC"]!="NFL"]
    country_noc_ids = country_noc_ids[['id', 'name', 'NOC']].rename(columns = {'name': 'country'})
    
    country_noc_medals_ids = country_noc_ids.merge(data_2, how='left', on='NOC')
    country_noc_medals_ids = country_noc_medals_ids[['id', 'country', 'NOC', 'medals', 'Year', 'Sport', 'Season', 'Sex']]
    
    map_click = alt.selection_multi()

    world_final_map = (alt.Chart(world_map, title="Number of medals received distributed by country").mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(country_noc_medals_ids, 'id', ['country', 'medals']))
     .encode(tooltip=['country:O', 'medals:Q'], 
             color='medals:Q', 
             opacity=alt.condition(map_click, alt.value(1), alt.value(0.2)))
     .add_selection(map_click)
     .project('equalEarth', scale=90).properties(
        width=700,
        height=400
    ))
    
    background = alt.Chart(world_map).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project('equalEarth', scale=90).properties(
        width=700,
        height=400
    )
    map_display = background + world_final_map
    
    return map_display

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