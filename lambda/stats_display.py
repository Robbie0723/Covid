def stats():
    true = True
    return {
    "type": "APL",
    "version": "1.1",
    "settings": {},
    "theme": "dark",
    "import": [
        {
            "name": "alexa-layouts",
            "version": "1.0.0"
        }
    ],
    "resources": [
        {
            "description": "Stock color for the light theme",
            "colors": {
                "colorTextPrimary": "#151920"
            }
        },
        {
            "description": "Stock color for the dark theme",
            "when": "${viewport.theme == 'dark'}",
            "colors": {
                "colorTextPrimary": "#f0f1ef"
            }
        },
        {
            "description": "Standard font sizes",
            "dimensions": {
                "textSizeSecondary": 30,
                "textSizeDetails": 40
            }
        },
        {
            "description": "Common spacing values",
            "dimensions": {
                "spacingThin": 6,
                "spacingSmall": 12,
                "spacingMedium": 24,
                "spacingLarge": 48,
                "spacingExtraLarge": 72
            }
        },
        {
            "description": "Common margins and padding",
            "dimensions": {
                "marginTop": 10,
                "marginLeft": 10,
                "marginRight": 10,
                "marginBottom": 10
            }
        }
    ],
    "styles": {
        "textStyleBase": {
            "description": "Base font description; set color",
            "values": [
                {
                    "color": "@colorTextPrimary"
                }
            ]
        },
        "textStyleBase0": {
            "description": "Thin version of basic font",
            "extend": "textStyleBase",
            "values": {
                "fontWeight": "100"
            }
        },
        "textStyleBase1": {
            "description": "Light version of basic font",
            "extend": "textStyleBase",
            "values": {
                "fontWeight": "300"
            }
        },
        "textStyleBase2": {
            "description": "Regular version of basic font",
            "extend": "textStyleBase",
            "values": {
                "fontWeight": "500"
            }
        },
        "mixinBody": {
            "values": {
                "fontSize": "@textSizeBody"
            }
        },
        "mixinPrimary": {
            "values": {
                "fontSize": "@textSizePrimary"
            }
        },
        "mixinDetails": {
            "values": {
                "fontSize": "@textSizeDetails"
            }
        },
        "mixinSecondary": {
            "values": {
                "fontSize": "@textSizeSecondary"
            }
        },
        "textStylePrimary": {
            "extend": [
                "textStyleBase1",
                "mixinPrimary"
            ]
        },
        "textStyleSecondary": {
            "extend": [
                "textStyleBase0",
                "mixinSecondary"
            ]
        },
        "textStyleBody": {
            "extend": [
                "textStyleBase1",
                "mixinBody"
            ]
        },
        "textStyleSecondaryHint": {
            "values": {
                "fontFamily": "Bookerly",
                "fontStyle": "italic",
                "fontSize": "@textSizeSecondaryHint",
                "color": "@colorTextPrimary"
            }
        },
        "textStyleDetails": {
            "extend": [
                "textStyleBase2",
                "mixinDetails"
            ]
        }
    },
    "onMount": [],
    "graphics": {},
    "commands": {},
    "layouts": {
        "FullHorizontalListItem": {
            "parameters": [
                "listLength"
            ],
            "item": [
                {
                    "type": "Container",
                    "height": "100vh",
                    "width": "100vw",
                    "alignItems": "center",
                    "justifyContent": "end",
                    "items": [
                        {
                            "type": "Image",
                            "position": "absolute",
                            "height": "100vh",
                            "width": "100vw",
                            "overlayColor": "rgba(0, 0, 0, 0.6)",
                            "source": "${data.image.sources[0].url}",
                            "scale": "best-fill"
                        },
                        {
                            "type": "AlexaHeader",
                            "headerTitle": "${title}",
                            "headerAttributionImage": "${logo}",
                            "grow": 1
                        },
                        {
                            "type": "Text",
                            "text": "${data.textContent.primaryText.text}",
                            "style": "textStyleBody",
                            "maxLines": 1
                        },
                        {
                            "type": "Text",
                            "text": "${data.textContent.secondaryText.text}",
                            "style": "textStyleDetails"
                        },
                        {
                            "type": "Text",
                            "text": "${ordinal} | ${listLength}",
                            "paddingBottom": "20dp",
                            "color": "white",
                            "spacing": "5dp"
                        }
                    ]
                }
            ]
        },
        "HorizontalListItem": {
            "item": [
                {
                    "type": "Container",
                    "maxWidth": 300,
                    "minWidth": 300,
                    "paddingLeft": 10,
                    "paddingRight": 10,
                    "height": "100%",
                    "items": [
                        {
                            "type": "Image",
                            "source": "${data.image.sources[0].url}",
                            "height": "40vh",
                            "width": "40vh"
                        },
                        {
                            "type": "Text",
                            "text": "${data.textContent.primaryText.text}",
                            "style": "textStyleSecondary",
                            "maxLines": 1,
                            "spacing": 12
                        },
                        {
                            "type": "Text",
                            "text": "${data.textContent.secondaryText.text}",
                            "style": "textStyleDetails",
                            "spacing": 4
                        }
                    ]
                }
            ]
        },
        "ListTemplate2": {
            "parameters": [
                "backgroundImage",
                "title",
                "logo",
                "hintText",
                "listData"
            ],
            "items": [
                {
                    "when": "${viewport.shape == 'round'}",
                    "type": "Container",
                    "height": "100%",
                    "width": "100%",
                    "items": [
                        {
                            "type": "Sequence",
                            "scrollDirection": "horizontal",
                            "data": "${listData}",
                            "height": "100%",
                            "width": "100%",
                            "item": [
                                {
                                    "type": "FullHorizontalListItem",
                                    "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "Container",
                    "height": "100vh",
                    "width": "100vw",
                    "items": [
                        {
                            "type": "Image",
                            "source": "${backgroundImage}",
                            "scale": "best-fill",
                            "width": "100vw",
                            "height": "100vh",
                            "position": "absolute"
                        },
                        {
                            "type": "AlexaHeader",
                            "headerTitle": "${title}",
                            "headerAttributionImage": "${logo}"
                        },
                        {
                            "type": "Sequence",
                            "scrollDirection": "horizontal",
                            "paddingLeft": "@marginLeft",
                            "paddingRight": "@marginRight",
                            "data": "${listData}",
                            "height": "70vh",
                            "width": "100%",
                            "numbered": true,
                            "item": [
                                {
                                    "type": "HorizontalListItem"
                                }
                            ]
                        },
                        {
                            "type": "AlexaFooter",
                            "footerHint": "${payload.listTemplate2ListData.hintText}",
                            "position": "absolute",
                            "top": "85vh"
                        }
                    ]
                }
            ]
        }
    },
    "mainTemplate": {
        "parameters": [
            "payload"
        ],
        "item": [
            {
                "type": "ListTemplate2",
                "backgroundImage": "${payload.listTemplate2Metadata.backgroundImage.sources[0].url}",
                "title": "${payload.listTemplate2Metadata.title}",
                "hintText": "${payload.listTemplate2Metadata.hintText}",
                "logo": "${payload.listTemplate2Metadata.logoUrl}",
                "listData": "${payload.listTemplate2ListData.listPage.listItems}"
            }
        ]
    }
}







def stats_datasource(location, cases, active, recovered, deaths):
    return {
    "listTemplate2Metadata": {
        "type": "object",
        "objectId": "lt1Metadata",
        "title": location,
        "logoUrl": "https://?????????????.s3.amazonaws.com/coronavirus_iicon.png"
    },
    "listTemplate2ListData": {
        "type": "list",
        "listId": "lt2Sample",
        "totalNumberOfItems": 10,
        "hintText": "",
        "listPage": {
            "listItems": [
                {
                    "listItemIdentifier": "Total Cases",
                    "ordinalNumber": 1,
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Total reported cases:"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": cases
                        }
                    },
                    "image": {
                        "sources": [
                            {
                                "url": "https://?????????????.s3.amazonaws.com/total_cases_faces.png",
                                "size": "small",
                                "widthPixels": 0,
                                "heightPixels": 0
                            },
                            {
                                "url": "https://?????????????.s3.amazonaws.com/total_cases_faces.png",
                                "size": "large",
                                "widthPixels": 0,
                                "heightPixels": 0
                            }
                        ]
                    },
                    "token": "cases"
                },
                {
                    "listItemIdentifier": "Active",
                    "ordinalNumber": 2,
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Active cases:"
                        },
                        "secondaryText": {
                            "type": "RichText",
                            "text": active
                        }
                    },
                    "image": {
                        "sources": [
                            {
                                "url": "https://?????????????.s3.amazonaws.com/active_face.png",
                                "size": "small",
                                "widthPixels": 0,
                                "heightPixels": 0
                            },
                            {
                                "url": "https://?????????????.s3.amazonaws.com/active_face.png",
                                "size": "large",
                                "widthPixels": 0,
                                "heightPixels": 0
                            }
                        ]
                    },
                    "token": "active"
                },
                {
                    "listItemIdentifier": "Recovered",
                    "ordinalNumber": 3,
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Recovered:"
                        },
                        "secondaryText": {
                            "type": "RichText",
                            "text": recovered
                        }
                    },
                    "image": {
                        "sources": [
                            {
                                "url": "https://?????????????.s3.amazonaws.com/recovered_faces.png",
                                "size": "small",
                                "widthPixels": 0,
                                "heightPixels": 0
                            },
                            {
                                "url": "https://?????????????.s3.amazonaws.com/recovered_faces.png",
                                "size": "large",
                                "widthPixels": 0,
                                "heightPixels": 0
                            }
                        ]
                    },
                    "token": "recovered"
                },
                {
                    "listItemIdentifier": "Deaths",
                    "ordinalNumber": 1,
                    "textContent": {
                        "primaryText": {
                            "type": "PlainText",
                            "text": "Reported deaths:"
                        },
                        "secondaryText": {
                            "type": "PlainText",
                            "text": deaths
                        }
                    },
                    "image": {
                        "sources": [
                            {
                                "url": "https://?????????????.s3.amazonaws.com/blackribbon.png",
                                "size": "small",
                                "widthPixels": 0,
                                "heightPixels": 0
                            },
                            {
                                "url": "https://?????????????.s3.amazonaws.com/blackribbon.png",
                                "size": "large",
                                "widthPixels": 0,
                                "heightPixels": 0
                            }
                        ]
                    },
                     "token": "deaths"
                }
            ]
        }
    }
}