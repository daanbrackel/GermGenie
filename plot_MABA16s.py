import argparse
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def plot_stacked_bar(input_csv, output_html):
    # Read input CSV
    df = pd.read_csv(input_csv)

    # Calculate percentage of reads for each species in each barcode
    df['Total_reads'] = df.groupby('Barcode')['num_reads'].transform('sum')
    df['Percentage'] = (df['num_reads'] / df['Total_reads']) * 100

    # Create a dictionary to map species to colors
    species_colors = {}
    species_list = df['blast_hit'].unique()
    color_palette = px.colors.qualitative.Plotly
    for i, species in enumerate(species_list):
        species_colors[species] = color_palette[i % len(color_palette)]

    # Create traces for each species
    traces = []
    for species in df['blast_hit'].unique():
        species_df = df[df['blast_hit'] == species]
        traces.append(go.Bar(x=species_df['Barcode'], y=species_df['Percentage'], name=species, marker_color=species_colors[species]))

    # Create layout
    layout = go.Layout(title='Stacked Bar Plot of Species Percentage per Barcode',
                       xaxis_title='Barcode',
                       yaxis_title='Percentage of Reads',
                       barmode='stack')

    # Create figure
    fig = go.Figure(data=traces, layout=layout)

    # Save the plot as HTML
    fig.write_html(output_html)

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Plot stacked bar plot of species percentage per barcode")
    parser.add_argument("input_csv", type=str, help="Path to input CSV file (your merged CSV file)")
    parser.add_argument("output_html", type=str, help="Path to output HTML file for the plot")
    args = parser.parse_args()

    # Call plot_stacked_bar function with provided arguments
    plot_stacked_bar(args.input_csv, args.output_html)
