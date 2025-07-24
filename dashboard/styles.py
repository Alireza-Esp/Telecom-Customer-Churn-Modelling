import streamlit as st
import plotly.express as px

css_styles = """
<style>
        [data-testid="stMainBlockContainer"] {
            padding-top: 80px;
            padding-bottom: 80px;
            padding-left: 0px;
            padding-right: 0px;
            margin-top: 0px;
            margin-bottom: 0px;
            margin-left: 0px;
            margin-right: 0px;
            max-width: 85%;
        }
        [data-testid="stVerticalBlock"] {
            gap: 0px;
        }
        # [data-testid="stMarkdownContainer"] {
        #     text-align: justify;
        # }
        .maplibregl-canvas {
            border-radius: 10px
        }
        .maplibregl-ctrl-attrib-inner {
            font-size: 8px
        }
</style>
"""

plotly_color_palettes = [
    px.colors.qualitative.Set1,
    px.colors.qualitative.Set2,
    px.colors.qualitative.Set3,
    ]

color_scales = [
    "blues",
    "greens", 
    "purples"
    ]


# plotly_color_palettes2 = [px.colors.qualitative.Alphabet,
#     px.colors.qualitative.Antique,
#     px.colors.qualitative.Bold,
#     px.colors.qualitative.D3,
#     px.colors.qualitative.Dark2,
#     px.colors.qualitative.Dark24,
#     px.colors.qualitative.G10,
#     px.colors.qualitative.Light24,
#     px.colors.qualitative.Pastel,
#     px.colors.qualitative.Pastel1,
#     px.colors.qualitative.Pastel2,
#     px.colors.qualitative.Plotly,
#     px.colors.qualitative.Prism,
#     px.colors.qualitative.Safe,
#     px.colors.qualitative.Set1,
#     px.colors.qualitative.Set2,
#     px.colors.qualitative.Set3,
#     px.colors.qualitative.T10,
#     px.colors.qualitative.Vivid
#     ]