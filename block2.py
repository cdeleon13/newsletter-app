from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


block2 = html.Div(
    className="block-2",
    children=[
        dbc.Card(
            style={'background-color': '#153654', 'border': '1px solid white'},
            children=[
                dbc.CardHeader(
                    html.H2(children="Who's active?", className='display-4', style={'color': 'white'})
                ),
                dbc.CardBody(
                    children=[
                        dbc.Container(
                            className="body-section-2-subsection-1",
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="seniors_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="Seniors (55+) Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='senior_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="families_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="Families Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='families_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="tay_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="TAY (18-24) Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='tay_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="veterans_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="Veterans Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='veteran_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        dbc.CardBody(
                            className="body-section-2-subsection-2",
                            children=[
                                html.Div(
                                    className='active-card active-card-center',
                                    children=[
                                            html.Div(className='active-graph', children=[dcc.Graph(id='active_counts_pie')]),
                                            html.Div(className='active-card', id='active-card-center', children=[
                                                html.Div(className='active-card-container', children=[
                                                    html.Div(className='active-card-top', children=[
                                                        html.Div(id="active_count", className="active-metric-1 display-4", style={'color': 'white'}),
                                                        html.Div(className="active-text-1 display-5", children="Active Clients", style={'color': 'white'}),
                                                    ]),
                                                    # html.Div(className='active-card-bottom', children=[
                                                    #     html.Div(className="arrow-up-1", children="", style={'color': 'white'}),
                                                    #     html.Div(className="active-metric-2 display-5", children="4% Last Month", style={'color': 'white'}),
                                                    # ]),
                                                ]),
                                            ]),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            className="w-100",
        ),
    ]
)





# from dash import Dash, html, dcc, Input, Output
# import dash_bootstrap_components as dbc

# block2 = html.Div(
#     className="block-2",
#     children=[
#         html.Div(
#             className="title-section-2",
#             children=[html.H2(children="Who's active")]
#         ),
#         html.Div(
#             className="body-section-2",
#             children=[
#                 html.Div(
#                     className="body-section-2-subsection-1",
#                     children=[
#                         html.Div(
#                             className='top',
#                             children=[
#                                 html.Div(
#                                     className="active-bottom-right",
#                                     children=[
#                                         html.H3(id="seniors_active_count",className="metric"),
#                                         html.H3(children="Seniors (55+) Served"),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='senior_active_race_plot'),
#                                         ),
#                                     ]
#                                 ),
#                                 html.Div(
#                                     className="active-bottom",
#                                     children=[
#                                         html.H3(id="families_active_count", className="metric"),
#                                         html.H3(children="Families Served"),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='families_active_race_plot'),
#                                         ),
#                                     ]
#                                 ),
#                             ]
#                         ),
#                         html.Div(
#                             className='bottom',
#                             children=[    
#                                 html.Div(
#                                     className="active-right",
#                                     children=[
#                                         html.H3(id="tay_active_count", className="metric"),
#                                         html.H3(children="TAY (18-24) Served"),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='tay_active_race_plot'),
#                                         ),
#                                     ]
#                                 ),
#                                 html.Div(
#                                     className="active",
#                                     children=[
#                                         html.H3(id="veterans_active_count", className="metric"),
#                                         html.H3(children="Veterans Served"),
#                                         html.Div(
#                                             className='housed_plots',
#                                             children=dcc.Graph(id='veteran_active_race_plot'),
#                                         ),
#                                     ]
#                                 )
#                             ]
#                         ),                                        
#                     ]
#                 ), 
#                 html.Div(
#                     className="body-section-2-subsection-2",
#                     children = [
#                         dcc.Graph(
#                             id='active_counts_pie'
#                         ),
#                         html.Div(
#                             className='active-card',
#                             children=[
#                                 html.Div(
#                                     className='active-card-top',
#                                     children=[
#                                         html.Div(id="active_count", className="active-metric-1"),
#                                         html.Div(className="active-text-1",children="Active Clients"),
#                                     ]
#                                 ),
#                                 html.Div(
#                                     className='active-card-bottom',
#                                     children=[
#                                         html.Div(className="arrow-up-1", children=""),
#                                         html.Div(className="active-metric-2", children="4% Last Month"),
#                                     ]
#                                 ),
#                             ]
#                         ),
#                     ]
#                 ),                             
#             ]
#         )
#     ]
# )