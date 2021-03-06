from select import select
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data as v_data
from dash import Dash, html, dcc, Input, Output, dash_table, State
import dash_bootstrap_components as dbc

alt.data_transformers.disable_max_rows()
data = pd.read_csv("data/processed/athlete_events_2000.csv")
filter_df = data[["NOC", "Medal", "Year"]]
filter_df = filter_df.rename(columns={"NOC": "Team"})
total_medals = (
    filter_df.groupby(["Team", "Year"])
    .count()
    .reset_index()
    .rename(columns={"Medal": "Total Medals Received"})
)
physical_df = data[["NOC", "Age", "Height", "Weight", "Year"]]
physical_df = physical_df.rename(columns={"NOC": "Team"})
df_cols = ["Team", "Age", "Height", "Weight"]
physical_df = (
    physical_df.groupby(["Team", "Year"])
    .mean()
    .round(1)
    .rename(
        columns={
            "Age": "Average Age",
            "Height": "Average Height (cm)",
            "Weight": "Average Weight (kg)",
        }
    )
    .reset_index()
)
agg_df = physical_df["Year"].astype(str)
agg_df = pd.merge(physical_df, total_medals, on=["Team", "Year"]).sort_values(
    by=["Total Medals Received"], ascending=False
)
agg_df["Ranking"] = np.arange(1, len(agg_df) + 1)
logo = "olympics_data_viz.png"

# Setup app layout
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
app.title = "Analyzing the Olympics Over the Years"
server = app.server

dropdown_list = sorted(list(data["Year"].unique()), reverse=True)
season = data["Season"].unique()[0]
background_style = {
    "backgroundColor": "#f7f2dc",
    "height": "100%",
    "display": "fixed",
    "width": "100%",
}
tabs_styles = {"height": "60px", "width": "100%", "backgroundColor": "#1C4E80"}
tab_style = {
    "borderTop": "1px solid #000000",
    "padding": "2px",
    "fontWeight": "bold",
    "marginLeft": "auto",
    "color": "black",
}


tab_selected_style = {
    "borderTop": "1px solid #000000",
    "backgroundColor": "#1C4E80",
    "color": "white",
    "padding": "10px",
    "float": "left",
    "width": "100%",
    "height": "50px",
}

collapse = html.Div(
    [
        dbc.Button(
            "I Need Help",
            id="collapse-button",
            className="mb-3",
            outline=False,
            style={
                "margin-top": "10px",
                "width": "150px",
                "background-color": "white",
                "color": "steelblue",
            },
        ),
    ]
)


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


content = "We developed this dashboard in the hopes of making Olympic Games statistics accessible to the public. Here, users can explore the statistics of Olympic Events from 2000 to 2016. We developed filters to extract data that we found summarized the most important Olympic statistics that users may want to know about. Specifically, our dashboard aims to provide digestible visuals that demonstrate the differences in biological sex, geographic location, and physical characteristics of athletes and how these factors impact performance within the Olympic Games. Our dashboard is a collaborative effort and we look forward to hearing your feedback and integrating any contributions that you wish to make!"
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        children=[
                            html.H3(
                                "Analyzing the Olympics From 2000-2016",
                                style={"color": "white"},
                            )
                        ],
                    ),
                    style={"textalign": "centre"},
                ),
                dbc.Col(
                    [
                        dbc.Collapse(
                            html.P(
                                """
                        Thanks for stopping by! Explore the performances of different teams over the years
                        by using the dropdown menus provided for you. You can select different years, sports,
                        or you can filter by sex as well. You can obtain more information about each country by hovering over your country of 
                        interest. If you want to remove filters, just press the X button for the
                        corresponding filter. Feel free to navigate into the 'Data' tab as well to explore additional statistics
                        about the teams at the Olympics. Happy filtering!""",
                                style={
                                    "color": "white",
                                    "width": "100%",
                                },
                            ),
                            id="collapse",
                        )
                    ]
                ),
                dbc.Col([collapse], align="center", style={"padding-left": "500px"}),
            ],
            style={"backgroundColor": "#4EB593"},
        ),
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        html.Br(),
                        html.Div(
                            [
                                dbc.Row(
                                    [
                                        html.H2(
                                            "Filters",
                                            style={
                                                "flex-grow": "1",
                                                "margin": "0px",
                                                "line-height": "1",
                                                "textAlign": "center",
                                                "color": "white",
                                            },
                                        )
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.P(
                                                    "Year",
                                                    style={
                                                        "textAlign": "center",
                                                        "color": "#000000",
                                                    },
                                                ),
                                                dcc.Dropdown(
                                                    id="year_dropdown",
                                                    options=[
                                                        {"label": i, "value": i}
                                                        for i in dropdown_list
                                                    ],
                                                    value=2016,
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            [
                                                html.P(
                                                    "Sex",
                                                    style={
                                                        "textAlign": "center",
                                                        "color": "#000000",
                                                    },
                                                ),
                                                dcc.Dropdown(
                                                    id="sex_dropdown",
                                                    options=data.Sex.unique().tolist(),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            [
                                                html.P(
                                                    "Sport",
                                                    style={
                                                        "textAlign": "center",
                                                        "color": "#000000",
                                                    },
                                                ),
                                                dcc.Dropdown(
                                                    id="sport_dropdown",
                                                    options=data.Sport.unique().tolist(),
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            style={
                                "width": "100%",
                                "margin-top": "0px",
                                "padding": "25px",
                                "background-color": "#4EB593",
                                "border-radius": "10px",
                            },
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.CardHeader(
                                                    "Number of Medals Received By Each Country",
                                                    style={
                                                        "color": "#000000",
                                                        "textAlign": "center",
                                                    },
                                                ),
                                                dbc.CardBody(
                                                    html.Iframe(
                                                        id="world_map",
                                                        # srcDoc = create_world_plot(data, year=2000, sport="Ice Hockey", sex="Female"),
                                                        style={
                                                            "border-width": "0",
                                                            "width": "100%",
                                                            "height": "750px",
                                                        },
                                                    )
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.CardHeader(
                                                    "Number and Type of Medals Received By Each Sex",
                                                    style={
                                                        "color": "#000000",
                                                        "textAlign": "center",
                                                    },
                                                ),
                                                dbc.CardBody(
                                                    html.Iframe(
                                                        id="gender_medals",  # srcDoc = create_gender_medal_plot(data, year=2000, sport="Ice Hockey", sex="Female"),
                                                        style={
                                                            "width": "100%",
                                                            "height": "400px",
                                                        },
                                                    )
                                                ),
                                            ]
                                        )
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        dbc.Card(
                                            [
                                                dbc.CardHeader(
                                                    "Density of Each Medal Type Received Distributed By Age",
                                                    style={
                                                        "color": "#000000",
                                                        "textAlign": "center",
                                                    },
                                                ),
                                                dbc.CardBody(
                                                    html.Iframe(
                                                        id="age_plot",  # srcDoc = create_age_plot(data, year=2000, sport="Ice Hockey", sex="Female"),
                                                        style={
                                                            "width": "100%",
                                                            "height": "400px",
                                                        },
                                                    )
                                                ),
                                            ]
                                        )
                                    ],
                                    style={"border-style": None},
                                ),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                html.Div(
                                    [
                                        html.P(
                                            [
                                                "What does ",
                                                html.Span(
                                                    "Density",
                                                    id="tooltip-target",
                                                    style={
                                                        "textDecoration": "underline",
                                                        "cursor": "pointer",
                                                    },
                                                ),
                                                " mean?",
                                            ]
                                        ),
                                        dbc.Tooltip(
                                            "Density is just another way of showing a number. It has an arbitrary unit, but the higher the density, the higher the count. For the age density plot, a higher density means a higher number of medals received!",
                                            target="tooltip-target",
                                        ),
                                    ]
                                )
                            ]
                        ),
                        html.Br(),
                        dbc.Alert(
                            [
                                "For more information, visit our ",
                                html.A(
                                    "GitHub repo",
                                    href="https://github.com/UBC-MDS/olympics_data_analysis/",
                                    className="alert-link",
                                ),
                                " or check out the ",
                                html.A(
                                    "sourcecode",
                                    href="https://github.com/UBC-MDS/olympics_data_analysis/blob/main/src/app.py",
                                    className="alert-link",
                                ),
                                " to see how we developed this app",
                            ],
                            color="primary",
                        ),
                    ],
                    label="Analysis",
                    style=tab_style,
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div(
                                            [
                                                html.H2(
                                                    "Explore the Data",
                                                    style={
                                                        "flex-grow": "1",
                                                        "margin": "0px",
                                                        "line-height": "1",
                                                        "textAlign": "center",
                                                        "color": "white",
                                                    },
                                                ),
                                                html.Hr(),
                                                html.P(
                                                    "Select a Year",
                                                    style={
                                                        "textAlign": "center",
                                                        "color": "#000000",
                                                    },
                                                ),
                                                dcc.Dropdown(
                                                    id="year_df_dropdown",
                                                    options=[
                                                        {"label": i, "value": i}
                                                        for i in dropdown_list
                                                    ],
                                                    value=2016,
                                                ),
                                                html.Br(),
                                                html.Br(),
                                                html.P(
                                                    "Select an Olympic Statistic",
                                                    style={
                                                        "textAlign": "center",
                                                        "color": "#000000",
                                                    },
                                                ),
                                                dcc.Dropdown(
                                                    id="df_dropdown",
                                                    options=[
                                                        {"label": col, "value": col}
                                                        for col in agg_df.columns
                                                    ],
                                                    multi=True,
                                                    value=["Team", "Year", "Ranking"],
                                                ),
                                            ],
                                            style={
                                                "width": "70%",
                                                "margin-top": "0px",
                                                "padding": "25px",
                                                "background-color": "#4EB593",
                                                "border-radius": "10px",
                                                "justify-content": "space-around",
                                                "flex-direction": "row",
                                            },
                                        )
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        html.H4(
                                            "Team Statistics and Rankings According to Number of Medals Received by Individual Athletes Each Year",
                                            style={
                                                "textAlign": "center",
                                                "font_size": "15px",
                                            },
                                        ),
                                        html.Br(),
                                        dash_table.DataTable(
                                            id="table",
                                            columns=[
                                                {"name": col, "id": col}
                                                for col in df_cols
                                            ],
                                            data=agg_df.to_dict("records"),
                                            page_size=15,
                                            style_cell={
                                                "padding": "5px",
                                                "color": "#010c17",
                                            },
                                            style_data_conditional=[
                                                {
                                                    "if": {"row_index": "odd"},
                                                    "backgroundColor": "rgb(174, 226, 235)",
                                                }
                                            ],
                                            style_header={
                                                "backgroundColor": "rgb(116, 180, 219)",
                                                "fontWeight": "bold",
                                                "color": "#010c17",
                                            },
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    label="Data",
                    style=tab_style,
                ),
                dbc.Tab(
                    [
                        html.Br(),
                        dbc.Row([html.Div(content)]),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Alert(
                                    [
                                        "I want to ",
                                        html.A(
                                            "contribute",
                                            href="https://github.com/UBC-MDS/olympics_data_analysis#contribute-to-the-cause",
                                            className="alert-link",
                                        ),
                                        " to your project!",
                                    ],
                                    color="primary",
                                ),
                            ]
                        ),
                        html.Br(),
                    ],
                    label="About the project",
                    style=tab_style,
                ),
            ],
        ),
    ],
    style=background_style,
)


@app.callback(
    Output("table", "data"),
    Output("table", "columns"),
    Input("df_dropdown", "value"),
    Input("year_df_dropdown", "value"),
)
def filter_table(cols, year):
    filtered_df = agg_df[agg_df["Year"] == year]
    filtered_df["Ranking"] = np.arange(1, len(filtered_df) + 1)
    columns = [{"name": col, "id": col} for col in cols]
    df = filtered_df[cols].to_dict("records")
    return df, columns


@app.callback(
    Output("world_map", "srcDoc"),
    Input("year_dropdown", "value"),
    Input("sport_dropdown", "value"),
    Input("sex_dropdown", "value"),
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
    data = pd.read_csv("data/processed/athlete_events_2000.csv")
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

    data_2 = (
        data[["NOC", "Medal", "Year", "Sport", "Sex"]]
        .groupby(["NOC", "Year", "Sport", "Sex"])
        .agg("count")
        .reset_index()
        .rename(columns={"Medal": "medals"})
    )

    country_ids = pd.read_csv("data/processed/country-ids.csv")

    noc = pd.read_csv("data/processed/noc_regions.csv")
    noc = noc[["NOC", "region"]]

    noc["region"][noc["region"] == "USA"] = "United States"
    noc["region"][noc["region"] == "Boliva"] = "Bolivia, Plurinational State of"
    noc["region"][noc["region"] == "Brunei"] = "Brunei Darussalam"
    noc["region"][noc["region"] == "Republic of Congo"] = "Congo"
    noc["region"][
        noc["region"] == "Democratic Republic of the Congo"
    ] = "Congo, the Democratic Republic of the"
    noc["region"][noc["region"] == "Ivory Coast"] = """Cote d'Ivoire"""
    noc["region"][noc["region"] == "Iran"] = "Iran, Islamic Republic of"
    noc["region"][
        noc["region"] == "North Korea"
    ] = """Korea, Democratic People's Republic of"""
    noc["region"][noc["region"] == "South Korea"] = "Korea, Republic of"
    noc["region"][noc["region"] == "Moldova"] = "Moldova, Republic of"
    noc["region"][noc["region"] == "Palestine"] = "Palestinian Territory, Occupied"
    noc["region"][noc["region"] == "Russia"] = "Russian Federation"
    noc["region"][noc["region"] == "Syria"] = "Syrian Arab Republic"
    noc["region"][noc["region"] == "Taiwan"] = "Taiwan, Province of China"
    noc["region"][noc["region"] == "Tanzania"] = "Tanzania, United Republic of"
    noc["region"][noc["region"] == "Trinidad"] = "Trinidad and Tobago"
    noc["region"][noc["region"] == "UK"] = "United Kingdom"
    noc["region"][noc["region"] == "Venezuela"] = "Venezuela, Bolivarian Republic of"
    noc["region"][noc["region"] == "Vietnam"] = "Viet Nam"

    country_noc_ids = noc.merge(
        country_ids, how="inner", left_on="region", right_on="name"
    )
    country_noc_ids = country_noc_ids[country_noc_ids["NOC"] != "NFL"]
    country_noc_ids = country_noc_ids[["id", "name", "NOC"]].rename(
        columns={"name": "country"}
    )

    country_noc_medals_ids = country_noc_ids.merge(data_2, how="left", on="NOC")
    country_noc_medals_ids = country_noc_medals_ids[
        ["id", "country", "NOC", "medals", "Year", "Sport", "Sex"]
    ]

    map_click = alt.selection_multi()
    world_map = alt.topo_feature(v_data.world_110m.url, "countries")

    if (year is None) & (sex is None) & (sport is None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
    elif (year is None) & (sex is None) & (sport is not None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Sport" "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
        country_noc_medals_ids = country_noc_medals_ids[
            (country_noc_medals_ids.Sport == sport)
        ]
    elif (year is None) & (sex is not None) & (sport is not None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Sport", "Sex", "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
        country_noc_medals_ids = country_noc_medals_ids[
            (country_noc_medals_ids.Sport == sport)
            & (country_noc_medals_ids.Sex == sex)
        ]
    elif (year is not None) & (sex is None) & (sport is not None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Sport", "Year", "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
        country_noc_medals_ids = country_noc_medals_ids[
            (country_noc_medals_ids.Sport == sport)
            & (country_noc_medals_ids.Year == year)
        ]
    elif (year is not None) & (sex is not None) & (sport is None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Sex", "Year", "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
        country_noc_medals_ids = country_noc_medals_ids[
            (country_noc_medals_ids.Sex == sex) & (country_noc_medals_ids.Year == year)
        ]
    elif (year is not None) & (sex is None) & (sport is None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Year", "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
        country_noc_medals_ids = country_noc_medals_ids[
            (country_noc_medals_ids.Year == year)
        ]
    elif (year is None) & (sex is not None) & (sport is None):
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Sex", "country"])["medals"]
            .agg("sum")
            .reset_index()
        )
        country_noc_medals_ids = country_noc_medals_ids[
            (country_noc_medals_ids.Sex == sex)
        ]
    else:
        country_noc_medals_ids = (
            country_noc_medals_ids.groupby(["id", "Sex", "Sport", "Year", "country"])[
                "medals"
            ]
            .agg("sum")
            .reset_index()
        )

    world_final_map = (
        alt.Chart(world_map)
        .mark_geoshape()
        .transform_lookup(
            lookup="id",
            from_=alt.LookupData(country_noc_medals_ids, "id", ["country", "medals"]),
        )
        .encode(
            tooltip=["country:O", "medals:Q"],
            color="medals:Q",
            opacity=alt.condition(map_click, alt.value(1), alt.value(0.2)),
        )
        .add_selection(map_click)
        .project("equalEarth", scale=200)
        .properties(width=700, height=400)
    )

    background = (
        alt.Chart(world_map)
        .mark_geoshape(fill="lightgray", stroke="white")
        .project("equalEarth", scale=210)
        .properties(width=950, height=700)
    )
    map_display = background + world_final_map

    return map_display.configure_view(strokeWidth=0).to_html()


@app.callback(
    Output("gender_medals", "srcDoc"),
    Input("year_dropdown", "value"),
    Input("sport_dropdown", "value"),
    Input("sex_dropdown", "value"),
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
    data = pd.read_csv("data/processed/athlete_events_2000.csv")

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

    colors = ["#d95f0e", "#fec44f", "silver"]

    bars = (
        alt.Chart(data, title="Medal Distribution by Gender in Olympics after 2000's")
        .encode(
            x=alt.X("Sex:N", title="", axis=alt.Axis(grid=False)),
            y=alt.Y(
                "count(Medal):Q",
                title=f"Olympic Medals won in {year}",
                axis=alt.Axis(grid=False, title=None),
            ),
            color=alt.Color("Medal", scale=alt.Scale(scheme="greenblue")),
        )
        .mark_bar()
    )

    text = bars.mark_text(
        align="center",
        baseline="middle",
        dy=14,  # Nudges text to right so it doesn't appear on top of the bar
        fill="black",
    ).encode(text="count(Medal):Q")

    chart = (
        (bars + text)
        .properties(height=200, width=100)
        .facet(
            facet=alt.Facet("Medal:N", title=None, header=alt.Header(labelExpr="''"))
        )
        .configure_axisX(labelAngle=0)
    )

    return chart.configure_view(strokeWidth=0).to_html()


@app.callback(
    Output("age_plot", "srcDoc"),
    Input("year_dropdown", "value"),
    Input("sport_dropdown", "value"),
    Input("sex_dropdown", "value"),
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
    data = pd.read_csv("data/processed/athlete_events_2000.csv")
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

    hist = (
        (
            alt.Chart(data)
            .transform_density("Age", groupby=["Medal"], as_=["Age", "density"])
            .mark_area(interpolate="monotone", opacity=0.4)
            .encode(
                x=alt.X("Age", title="Age (Years)", axis=alt.Axis(grid=False)),
                y=alt.Y(
                    "density:Q",
                    title="Density",
                    axis=alt.Axis(grid=False),
                ),
                color=alt.Color("Medal:O", scale=alt.Scale(scheme="darkblue")),
            )
        )
        .properties(height=320, width=350)
        .configure_axis(grid=False)
    )
    return hist.configure_view(strokeWidth=0).to_html()


if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
