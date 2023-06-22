from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

block1 = html.Div(
    className="block-1",
    children=[
        dbc.Card(
            [
                dbc.CardHeader("What's new?", className='display-4'),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        id='first_card',
                                        className="card card-container",
                                        children=[
                                            html.Div(className="plots", children=[dcc.Graph(id='fth_race_plot', className='race_plot')]),
                                            html.H3(children="First Time Homeless", className='display-5', style={"text-align": "center", "position": "absolute", "top": "45%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                            html.H3(id="fth_count", className="metric", style={"text-align": "center", "position": "absolute", "top": "55%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                        ],
                                        style={"position": "relative", "height": "100%"}
                                    ),
                                    width=12, sm=12, md=6, lg=6, xl=3
                                ),
                                dbc.Col(
                                    html.Div(
                                        className="card card-container",
                                        children=[
                                            html.Div(className="plots", children=[dcc.Graph(id='housed_race_plot', className='race_plot')]),
                                            html.H3(children="Persons Housed", className='display-5', style={"text-align": "center", "position": "absolute", "top": "45%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                            html.H3(id="housed_count", className="metric", style={"text-align": "center", "position": "absolute", "top": "55%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                        ],
                                        style={"position": "relative", "height": "100%"}
                                    ),
                                    width=12, sm=12, md=6, lg=6, xl=3
                                ),
                                dbc.Col(
                                    html.Div(
                                        className="card card-container",
                                        children=[
                                            html.Div(className="plots", children=[dcc.Graph(id='new_entries_race_plot', className='race_plot')]),
                                            html.H3(children="New Program Entries", className='display-5', style={"text-align": "center", "position": "absolute", "top": "45%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                            html.H3(id="new_entries_count",className="metric", style={"text-align": "center", "position": "absolute", "top": "55%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                        ],
                                        style={"position": "relative", "height": "100%"}
                                    ),
                                    width=12, sm=12, md=6, lg=6, xl=3
                                ),
                                dbc.Col(
                                    html.Div(
                                        className="card card-container",
                                        children=[
                                            html.Div(className="plots", children=[dcc.Graph(id='new_referrals_race_plot', className='race_plot')]),
                                            html.H3(children="New Referrals to Housing Queue", className='display-5', style={"text-align": "center", "position": "absolute", "top": "45%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                            html.H3(id="new_referrals_count", className="metric", style={"text-align": "center", "position": "absolute", "top": "55%", "left": "50%", "transform": "translate(-50%, -50%)"}),
                                        ],
                                        style={"position": "relative", "height": "100%"}
                                    ),
                                    width=12, sm=12, md=6, lg=6, xl=3
                                ),
                            ],
                            align="center",
                            justify="around",
                            style={"display": "flex", 'align-items':'stretch', "flex-direction": "row", "height": "100%"} # set the parent container to
                        ),
                    ],
                    style={"height": "100%"} # set the height of the card body container to 100%
                ),
            ],
            style={"background-color": "#ADC48B", "border-color": "#36413E", "opacity": "0.9"} # set the card background color and outline color
        ),
    ],
    style={"height": "100%"} # set the height of the main container to 100%
)


# from dash import Dash, html, dcc, Input, Output
# import dash_bootstrap_components as dbc

# block1 = html.Div(
#     className="block-1",
#     children=[
#         html.Div(
#             className="title-section-1",
#             children=[html.H2(children="What's new?")]
#         ),
#         html.Div(
#             className="body-section-1",
#             children=[
#                 html.Div(
#                     id='first_card',
#                     className="card",
#                     children=[
#                         html.H3(id="fth_count", className="metric"),
#                         html.H3(children="First Time Homeless"),
#                         html.Div(className="plots", children=[dcc.Graph(id='fth_race_plot', className='race_plot')]),
#                     ]
#                 ),
#                 html.Div(
#                     className="card",
#                     children=[
#                         html.H3(id="housed_count", className="metric"),
#                         html.H3(children="Persons Housed"),
#                         html.Div(className="plots", children=[dcc.Graph(id='housed_race_plot', className='race_plot')]),
#                     ]
#                 ),
#                 html.Div(
#                     className="card",
#                     children=[
#                         html.H3(id="new_entries_count",className="metric"),
#                         html.H3(children="New Program Entries"),
#                         html.Div(className="plots", children=[dcc.Graph(id='new_entries_race_plot', className='race_plot')]),
#                     ]
#                 ),
#                 html.Div(
#                     className="card",
#                     children=[
#                         html.H3(id="new_referrals_count", className="metric"),
#                         html.H3(children="New Referrals to Housing Queue"),
#                         html.Div(className="plots", children=[dcc.Graph(id='new_referrals_race_plot', className='race_plot')]),
#                     ]
#                 )
#             ]
#         )
#     ]
# )