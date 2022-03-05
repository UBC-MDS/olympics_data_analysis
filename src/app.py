from select import select
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data as v_data
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

data = pd.read_csv("/app/data/processed/athlete_events_2000.csv")

# Setup app layout.
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

dropdown_list = sorted(list(data['Year'].unique()), reverse=True)
season = data['Season'].unique()[0]

tabs_styles = {
    'height': '60px',
    'width': '100%',
    'backgroundColor': '#1C4E80'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '2px',
    'fontWeight': 'bold',
    "marginLeft": "auto"
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'color': 'white',
    'padding': '10px',
    'float': 'left',
    'width': '100%',
    'height': '50px'
}

content = "An interactive dashboard demonstrating statistics regarding the Summer and Winter Olympic Games from 2002 to 2016.This app will provide a dashboard that summarizes a few of the key statistics that we have extracted from this data. Specifically, our dashboard aims to provide accessible visuals that demonstrate the differences in biological sex, geographic location, and physical characteristics of athletes and how these factors impact performance within the Olympic Games."
app.layout = dbc.Container([
    dbc.Row(
                dbc.Col(html.Div(style=tab_selected_style, children=[
                    html.H2("Olympics Data Visualization")]
                ), width="auto")
            ),
    html.Br(),
    dbc.Tabs([
        dbc.Tab([
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.P("Year", style={'textAlign': 'center'}),
                    dcc.Dropdown(
                        id="year_dropdown",
                        options=[{'label': i, 'value': i} for i in dropdown_list],
                        value=2016
                    )
                ]),
                dbc.Col([
                    html.P("Gender", style={'textAlign': 'center'}),
                    dcc.Dropdown(
                        id="sex_dropdown",
                        options=data.Sex.unique().tolist()
                    )
                ]),
                dbc.Col([
                    html.P("Sport", style={'textAlign': 'center'}),
                    dcc.Dropdown(
                        id="sport_dropdown",
                        options=data.Sport.unique().tolist()
                    )
                ])
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(
                html.Iframe(
                    id='world_map',
                    #srcDoc = create_world_plot(data, year=2000, sport="Ice Hockey", sex="Female"),
                    style={'border-width': '0', 'width': '100%', 'height': '750px'})
                )
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    html.Iframe(
                        id="gender_medals",
                        #srcDoc = create_gender_medal_plot(data, year=2000, sport="Ice Hockey", sex="Female"),
                        style={
                            "width": "100%",
                            "height": "400px"
                        }
                    )
                ]),

                dbc.Col([
                    html.Iframe(
                        id="age_plot",
                        #srcDoc = create_age_plot(data, year=2000, sport="Ice Hockey", sex="Female"),
                        style={
                            "width": "100%",
                            "height": "400px"
                        }
                    )
                ], style={'border-style': None})
            ]),
            html.Br(),
            dbc.Alert(
            [
                "Checkout the ",
                html.A("GitHub repo", href="https://github.com/UBC-MDS/olympics_data_analysis/tree/main", className="alert-link"),
                " for the sourcecode."
            ],
            color="primary",
        ),
        ], label="Analysis", style=tab_style),
        dbc.Tab(content, label='About the project', style=tab_style)
    ]),
], style=tabs_styles)    


@app.callback(
    Output("world_map", "srcDoc"),
    Input("year_dropdown", "value"),
    Input("sport_dropdown", "value"),
    Input("sex_dropdown", "value")
)
# World map 
def create_world_plot(year=None, sport=None, sex=None):
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
    
    Returns
    -------
    alt.Chart
        the plot showing the medals received distributed by country, filtered for the selected features
    Examples
    --------
    >>> create_world_plot(year=2014, sport="Ice Hockey", sex="Male")
    >>> create_world_plot(year=2014)
    """
    data = pd.read_csv("/app/data/processed/athlete_events_2000.csv")
    if not isinstance(year, int) and year is not None:
        raise TypeError("year should be of type 'int'")
    if not isinstance(sport, str) and sport is not None:
        raise TypeError("sport should be of type 'str'")
    if not isinstance(sex, str) and sex is not None:
        raise TypeError("sex should be of type 'str'")
    
    if year is not None:
        data = data[data["Year"] == year]
    if sport is not None:
        data = data[data["Sport"] == sport]
    if sex is not None:
        data = data[data["Sex"] == sex]
        
    data_2 = data[['NOC', 'Medal', 'Year', 'Sport', 'Sex']].groupby(
    ['NOC', 'Year', 'Sport', 'Sex']).agg(
    'count').reset_index().rename(columns = {'Medal': 'medals'})
    
    country_ids = pd.read_csv('/app/data/processed/country-ids.csv')
    
    noc = pd.read_csv("/app/data/processed/noc_regions.csv")
    noc = noc[['NOC', 'region']]
    
    country_noc_ids = noc.merge(country_ids, how='inner', left_on='region', right_on='name')
    country_noc_ids = country_noc_ids[country_noc_ids["NOC"]!="NFL"]
    country_noc_ids = country_noc_ids[['id', 'name', 'NOC']].rename(columns = {'name': 'country'})
    
    country_noc_medals_ids = country_noc_ids.merge(data_2, how='left', on='NOC')
    country_noc_medals_ids = country_noc_medals_ids[['id', 'country', 'NOC', 'medals', 'Year', 'Sport', 'Sex']]
    
    map_click = alt.selection_multi()
    world_map = alt.topo_feature(v_data.world_110m.url, 'countries')
    
    world_final_map = (alt.Chart(world_map, title="Number of medals received by country").mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(country_noc_medals_ids, 'id', ['country', 'medals']))
     .encode(tooltip=['country:O', 'medals:Q'], 
             color='medals:Q', 
             opacity=alt.condition(map_click, alt.value(1), alt.value(0.2)))
     .add_selection(map_click)
     .project('equalEarth', scale=300).properties(
        width=700,
        height=400
    ))
    
    background = alt.Chart(world_map).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project('equalEarth', scale=200).properties(
        width=950,
        height=700
    )
    map_display = background + world_final_map
    
    return map_display.to_html()



@app.callback(
    Output("gender_medals", "srcDoc"),
    Input("year_dropdown", "value"),
    Input("sport_dropdown", "value"),
    Input("sex_dropdown", "value")
)
# Gender/medal plot
def create_gender_medal_plot(year=None, sport=None, sex=None):
    """
    Filters for selected features and creates the 'gender' vs 'medals count' distribution.
    Parameters
    ----------
    year : int
        the year to filter the data by
    sport: str
        the sport to filter the data by
    sex: str
        the biological sex to filter the data by
    
    Returns
    -------
    alt.Chart
        the plot showing the medals received distributed by gender, filtered for the selected features
    Examples
    --------
    >>> create_gender_medal_plot(year=2014, sport="Ice Hockey", sex="Male")
    >>> create_gender_medal_plot(year=2014)
    """
    data = pd.read_csv("/app/data/processed/athlete_events_2000.csv")
   
    if not isinstance(year, int) and year is not None:
            raise TypeError("year should be of type 'int'")
    if not isinstance(sport, str) and sport is not None:
        raise TypeError("sport should be of type 'str'")
    if not isinstance(sex, str) and sex is not None:
        raise TypeError("sex should be of type 'str'")

    if year is not None:
        data = data[data["Year"] == year]
    if sport is not None:
        data = data[data["Sport"] == sport]
    
    colors = ['#d95f0e', '#fec44f', 'silver']

    bars = alt.Chart(data, title="Medal Distribution by Gender in Olympics after 2000's").encode(x=alt.X('Sex:N', title=''),
                                 y=alt.Y('count(Medal):Q', title=f'Olympic Medals won in {year}'),
                                 color = alt.Color('Medal', scale=alt.Scale(scheme='greenblue'))).mark_bar()

    text = bars.mark_text(
    align='center',
    baseline='middle',
    dy=14, # Nudges text to right so it doesn't appear on top of the bar
    fill='black'
    ).encode(
        text='count(Medal):Q'
    )

    chart = (bars+text).properties(height=200, width=100).facet(facet=alt.Facet('Medal:N', title=None, header=alt.Header(labelExpr="''"))).configure_axisX(labelAngle=0)  

    return chart.to_html()

@app.callback(
    Output("age_plot", "srcDoc"),
    Input("year_dropdown", "value"),
    Input("sport_dropdown", "value"),
    Input("sex_dropdown", "value")
)
# Age plot
def create_age_plot(year=None, sport=None, sex=None):
    """
    Filters for selected features and creates the 'age' vs 'medals received' bar chart.
    Parameters
    ----------
    year : int
        the year to filter the data by
    sport: str
        the sport to filter the data by
    sex: str
        the biological sex to filter the data by
    
    Returns
    -------
    alt.Chart
        the plot showing the medals received distributed by age, filtered for the selected features
    Examples
    --------
    >>> create_age_plot(year=2014, sport="Ice Hockey", sex="Male")
    >>> create_age_plot(year=2014)
    """
    data = pd.read_csv("/app/data/processed/athlete_events_2000.csv")
    if not isinstance(year, int) and year is not None:
        raise TypeError("year should be of type 'int'")
    if not isinstance(sport, str) and sport is not None:
        raise TypeError("sport should be of type 'str'")
    if not isinstance(sex, str) and sex is not None:
        raise TypeError("sex should be of type 'str'")
    
    if year is not None:
        data = data[data["Year"] == year]
    if sport is not None:
        data = data[data["Sport"] == sport]
    if sex is not None:
        data = data[data["Sex"] == sex]
        
    hist = (alt.Chart(data, title="Number of medals received distributed by age").mark_bar(size=6.5).encode(
        x=alt.X("Age:Q", title="Age (Years)", axis=alt.Axis(grid=False)),
        y=alt.Y("count():Q", title="Number of medals received", axis=alt.Axis(grid=False))
    )).configure_axis(grid=False).configure_view(
    strokeWidth=0
)
    return hist.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)