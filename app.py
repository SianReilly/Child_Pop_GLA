import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Population Projections vs MYEs",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📊 Population Projections Comparison: MYEs vs GLA Research Outputs")
st.markdown("**Comparing actual Mid-Year Estimates with GLA 2024-based projection variants**")
st.markdown("---")

# Default data
default_data = {
    'Dataset': ['MYEs', 'GLA RO 5yr Migration', 'GLA RO 10yr Migration', 'GLA RO 15yr Migration',
                'MYEs', 'GLA RO 5yr Migration', 'GLA RO 10yr Migration', 'GLA RO 15yr Migration',
                'GLA RO 5yr Migration', 'GLA RO 10yr Migration', 'GLA RO 15yr Migration',
                'MYEs', 'GLA RO 5yr Migration', 'GLA RO 10yr Migration', 'GLA RO 15yr Migration',
                'MYEs', 'GLA RO 5yr Migration', 'GLA RO 10yr Migration', 'GLA RO 15yr Migration',
                'GLA RO 5yr Migration', 'GLA RO 10yr Migration', 'GLA RO 15yr Migration'],
    'Year': [2023, 2023, 2023, 2023,
             2024, 2024, 2024, 2024,
             2025, 2025, 2025,
             2023, 2023, 2023, 2023,
             2024, 2024, 2024, 2024,
             2025, 2025, 2025],
    'Age Group': ['0 to 15', '0 to 15', '0 to 15', '0 to 15',
                  '0 to 15', '0 to 15', '0 to 15', '0 to 15',
                  '0 to 15', '0 to 15', '0 to 15',
                  '0 to 19', '0 to 19', '0 to 19', '0 to 19',
                  '0 to 19', '0 to 19', '0 to 19', '0 to 19',
                  '0 to 19', '0 to 19', '0 to 19'],
    'Persons': [26597, 26597, 26597, 26597,
                26220, 26220, 26220, 26220,
                25630, 25516, 25668,
                36000, 36000, 36000, 36000,
                35617, 35617, 35617, 35617,
                34771, 34705, 34897],
    'Male': [13775, 13775, 13775, 13775,
             13483, 13483, 13483, 13483,
             13184, 13127, 13202,
             18449, 18449, 18449, 18449,
             18224, 18224, 18224, 18224,
             17825, 17872, 17997],
    'Female': [12822, 12822, 12822, 12822,
               12737, 12737, 12737, 12737,
               12446, 12388, 12466,
               17551, 17551, 17551, 17551,
               17393, 17393, 17393, 17393,
               16946, 16833, 16899]
}

df = pd.DataFrame(default_data)

# Sidebar for options
st.sidebar.header("⚙️ Options")
show_gender = st.sidebar.checkbox("Show gender breakdown", value=False)
age_group_filter = st.sidebar.multiselect(
    "Select age groups to display",
    options=df['Age Group'].unique(),
    default=df['Age Group'].unique()
)

# Filter data
df_filtered = df[df['Age Group'].isin(age_group_filter)]

def create_projection_chart(data, age_group, column='Persons'):
    """Create an interactive Plotly chart for a specific age group"""
    
    df_age = data[data['Age Group'] == age_group].copy()
    
    fig = go.Figure()
    
    # MYEs (actual data)
    df_mye = df_age[df_age['Dataset'] == 'MYEs']
    fig.add_trace(go.Scatter(
        x=df_mye['Year'],
        y=df_mye[column],
        mode='lines+markers',
        name='MYEs (Actual)',
        line=dict(color='#1a1a1a', width=3),
        marker=dict(size=8),
        hovertemplate='<b>MYEs</b><br>Year: %{x}<br>Population: %{y:,}<extra></extra>'
    ))
    
    # GLA Projections
    colors = {'GLA RO 5yr Migration': '#0066cc', 
              'GLA RO 10yr Migration': '#00a86b', 
              'GLA RO 15yr Migration': '#cc6600'}
    
    for dataset, color in colors.items():
        df_proj = df_age[df_age['Dataset'] == dataset]
        fig.add_trace(go.Scatter(
            x=df_proj['Year'],
            y=df_proj[column],
            mode='lines+markers',
            name=dataset.replace('GLA RO ', '').replace(' Migration', ''),
            line=dict(color=color, width=2, dash='dash'),
            marker=dict(size=6),
            hovertemplate=f'<b>{dataset}</b><br>Year: %{{x}}<br>Population: %{{y:,}}<extra></extra>'
        ))
    
    # Update layout
    fig.update_layout(
        title=f"Population Projections - Ages {age_group}",
        xaxis_title="Year",
        yaxis_title=f"Population ({column})",
        hovermode='x unified',
        height=500,
        template='plotly_white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    # Add vertical line to mark projection start
    fig.add_vline(x=2024.5, line_dash="dot", line_color="gray", 
                  annotation_text="Projections start", 
                  annotation_position="top")
    
    return fig

def calculate_statistics(data, age_group):
    """Calculate key statistics for a specific age group"""
    
    df_age = data[data['Age Group'] == age_group].copy()
    
    # 2024 MYE (actual)
    mye_2024 = df_age[(df_age['Dataset'] == 'MYEs') & (df_age['Year'] == 2024)]['Persons'].values[0]
    
    # 2025 projections
    proj_2025 = df_age[df_age['Year'] == 2025]['Persons'].values
    proj_min = proj_2025.min()
    proj_max = proj_2025.max()
    
    # Changes
    change_min = proj_min - mye_2024
    change_max = proj_max - mye_2024
    
    return {
        'mye_2024': mye_2024,
        'proj_min': proj_min,
        'proj_max': proj_max,
        'change_min': change_min,
        'change_max': change_max,
        'range': proj_max - proj_min
    }

# Main content
if len(age_group_filter) > 0:
    for age_group in age_group_filter:
        st.subheader(f"Ages {age_group}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Main chart
            if show_gender:
                # Create subplot with gender breakdown
                fig = make_subplots(
                    rows=1, cols=3,
                    subplot_titles=('Total', 'Male', 'Female'),
                    horizontal_spacing=0.1
                )
                
                for idx, column in enumerate(['Persons', 'Male', 'Female'], 1):
                    chart = create_projection_chart(df_filtered, age_group, column)
                    for trace in chart.data:
                        trace.showlegend = (idx == 1)  # Only show legend for first chart
                        fig.add_trace(trace, row=1, col=idx)
                
                fig.update_layout(height=500, title_text=f"Population Projections - Ages {age_group}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = create_projection_chart(df_filtered, age_group)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Statistics
            stats = calculate_statistics(df_filtered, age_group)
            
            st.metric(
                label="2024 MYE (Actual)",
                value=f"{stats['mye_2024']:,}"
            )
            
            st.metric(
                label="2025 Projection Range",
                value=f"{stats['proj_min']:,} - {stats['proj_max']:,}",
                delta=f"Range: {stats['range']:,}"
            )
            
            st.metric(
                label="Projected Change (2024→2025)",
                value=f"{stats['change_min']:,} to {stats['change_max']:,}",
                delta=f"Average: {(stats['change_min'] + stats['change_max'])/2:.0f}"
            )
            
            # Additional info
            st.info(f"""
            **Projection Variance:**
            - Difference between variants: {stats['range']:,}
            - As % of 2024 population: {(stats['range']/stats['mye_2024']*100):.2f}%
            """)
        
        st.markdown("---")
    
    # Summary table
    with st.expander("📋 View Data Table"):
        st.dataframe(df_filtered, use_container_width=True)
    
    # Information box
    st.info("""
    **📌 Note:** 
    - **MYEs (Mid-Year Estimates)** represent actual observed population data published by ONS
    - **GLA Projections** for 2025 show three variants based on different migration assumptions:
        - **5yr**: Uses average migration rates from the past 5 years
        - **10yr**: Uses average migration rates from the past 10 years  
        - **15yr**: Uses average migration rates from the past 15 years
    - The 2025 MYE will be published in **mid-2026**, allowing comparison of projection accuracy
    - All projections match MYEs exactly for 2023-2024 as they use MYEs as their base year
    """)
    
else:
    st.warning("Please select at least one age group from the sidebar.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Data source: GLA 2024-based Population Projections (Research Outputs) | Created with Streamlit
</div>
""", unsafe_allow_html=True)
