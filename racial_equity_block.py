import dash_bootstrap_components as dbc
from dash import html

accordion_block = html.Div(
    children=[
        html.Div(
            className="re-block-1",
            children=[
                dbc.Card(
                    [
                        dbc.CardHeader("Racial Equity Statements for PIT Data", className='display-4'),
                        dbc.CardBody(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Card(
                                                [
                                                    dbc.CardHeader("Sheltered PIT Data", className='display-5'),
                                                    dbc.CardBody(
                                                        children=[
                                                            html.P(id='sheltered_pit_2'),
                                                            html.P(id='sheltered_pit_1'),
                                                            
                                                        ]
                                                    )
                                                ],
                                            ),
                                            width=12, sm=12, md=6, lg=6, xl=6
                                        ),
                                        dbc.Col(
                                            dbc.Card(
                                                [
                                                    dbc.CardHeader("Unsheltered PIT Data", className='display-5'),
                                                    dbc.CardBody(
                                                        children=[
                                                            html.P(id='unsheltered_pit_2'),
                                                            html.P(id='unsheltered_pit_1'),
                                                        ]
                                                    )
                                                ],
                                            ),
                                            width=12, sm=12, md=6, lg=6, xl=6
                                        ),
                                    ],
                                    className="mb-2",  # Add margin-bottom for spacing
                                ),
                            ],
                            style={"height": "100%"}
                        ),
                    ],
                    style={
                        "background-color": "#BED9EC",
                        "border-color": "#36413E",
                        "opacity": "0.9"
                    }
                ),
            ],
            style={"height": "100%"}
        ),
        dbc.Accordion(
            [
                dbc.AccordionItem(
                    [
                        html.P(id="fth_compare_pop_percent"),
                        html.P(id="fth_likely_statement"),
                    ],
                    title="Racial Equity Statements on First Time Homeless in HMIS",
                ),
                dbc.AccordionItem(
                    [
                        html.P(id="active_compare_pop_percent"),
                        html.P(id="active_likely_statement"),
                    ],
                    title="Racial Equity Statements on Active Clients in HMIS",
                ),
                dbc.AccordionItem(
                    [
                        html.P(id="housed_compare_pop_percent"),
                        html.P(id="housed_likely_statement"),
                    ],
                    title="Racial Equity Statements on Housed Clients in HMIS",
                ),
            ],
        ),
    ]
)

