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
st.title("📊 Child Population Projections: Clarifying the Numbers")
st.markdown("**Comparing Mid-Year Estimates with GLA 2024-based Population Projection Variants**")

# Executive Summary Box
st.info("""
### 🎯 Quick Answer for Children's Services

**For 2025 population aged 0-19:** The most reliable estimate is approximately **34,700–34,900 persons**

**For 2025 population aged 0-15:** The most reliable estimate is approximately **25,500–25,700 persons**

These figures come from the GLA's 2024-based population projections (research outputs). The 2025 Mid-Year Estimates 
will not be published until mid-2026, so these projections are currently the best available evidence.

**Why the confusion?** Different teams may be referencing:
- Different age bands (0-15 vs 0-19)
- Different projection variants (5yr, 10yr, 15yr migration assumptions)
- Older projection rounds or planning documents
""")

st.markdown("---")

# Methodology explanation
with st.expander("📋 About These Projections - Click to Read More"):
    st.markdown("""
    ### Methodology
    
    These projections are from the **GLA 2024-based trend-based population projections (research outputs)**, 
    published in November 2024. They are interim "research outputs" pending final publication in early 2026.
    
    **How GLA Created These Projections:**
    
    The GLA used the **2024 Mid-Year Estimates as the base year** (published July 2024 by ONS). From this starting point,
    they projected forward using assumptions about future fertility, mortality, and migration patterns.
    
    **Key Technical Details:**
    - **Base data**: 2024 Mid-Year Estimates for Westminster
    - **Fertility assumption**: Principal (central) fertility rates - held constant
    - **Life expectancy assumption**: Principal (central) life expectancy - held constant
    - **Migration variants**: THREE scenarios based on different historical periods:
        - **5-year migration**: Average of 2019-2024 migration patterns
        - **10-year migration** ⭐ **(RECOMMENDED CORE PROJECTION)**: Average of 2014-2024 migration patterns
        - **15-year migration**: Average of 2009-2024 migration patterns
    
    ### Why Only Migration Variants?
    
    **For this analysis, I focused exclusively on migration variants** whilst keeping fertility and life expectancy constant at their
    principal (central) assumptions. This is because:
    
    ✅ **Migration is the most volatile demographic component** for Westminster  
    ✅ **Westminster is a highly mobile borough** with significant population turnover  
    ✅ **Migration changes can have immediate, substantial impacts** on child populations  
    ✅ **Migration is harder to predict** than fertility or mortality, making it the key source of uncertainty  
    
    **I have not yet analysed the other GLA variants** that combine different fertility and life expectancy assumptions:
    
    **Core projections:**
    - 2024_ppt_10yr - Principal fertility, principal life expectancy, 10 years past migration ⭐
    - 2024_hht_15yr - High fertility, high life expectancy, 15 years past migration
    - 2024_llt_5yr - Low fertility, low life expectancy, 5 years past migration
    
    **Additional variants:**
    - 2024_hht_10yr - High fertility, high life expectancy, 10 years past migration
    - 2024_llt_10yr - Low fertility, low life expectancy, 10 years past migration
    - 2024_ppt_5yr - Principal fertility, principal life expectancy, 5 years past migration
    - 2024_ppt_15yr - Principal fertility, principal life expectancy, 15 years past migration
    
    These additional variants may provide a wider range of scenarios, but for Westminster's specific context,
    migration assumptions drive the most significant variation.
    
    ### The 10-Year Migration Variant (Core Projection)
    
    **The recommended core projection is the 10-year migration variant** (coded as 2024_ppt_10yr in GLA outputs).
    
    **What this means:**
    - Takes the **average migration rates from 2014-2024** (10 years of data)
    - Assumes these average rates will continue into the future
    - Balances recent trends (which may be anomalous) with longer-term patterns
    - Provides a "middle ground" between very recent volatility and longer historical trends
    
    **Why 10 years?**
    - Long enough to smooth out short-term fluctuations
    - Short enough to capture relatively recent migration dynamics
    - Recommended by GLA as the central scenario
    - Widely used for planning across London boroughs
    
    ### Range of Projections
    
    The difference between the migration variants shows the range of plausible outcomes:
    
    **Ages 0-19:**
    - Population range: 34,705 to 34,897 = **192 persons**
    - Decrease from 2024 ranges from −720 (15yr variant) to −912 (10yr variant)
    - 10yr variant gives the largest decrease (most conservative)
    
    **Ages 0-15:**
    - Population range: 25,516 to 25,668 = **152 persons**
    - Decrease from 2024 ranges from −552 (15yr variant) to −704 (10yr variant)
    - 10yr variant gives the largest decrease (most conservative)
    
    This relatively narrow range suggests **high confidence** in the projections for 2025.
    
    ### Why Use GLA Projections?
    
    **Strengths:**
    ✅ Most recent data available (based on 2024 MYEs)  
    ✅ Incorporates latest migration trends  
    ✅ Provides range of scenarios showing uncertainty  
    ✅ Widely used for planning across London boroughs  
    ✅ Transparent methodology  
    
    **Limitations:**
    ⚠️ Labelled as "research outputs" - not yet quality assured  
    ⚠️ Cannot yet produce housing-led projections (awaiting 2023/24 small area estimates)  
    ⚠️ Projections are inherently uncertain - actual 2025 MYE may differ  
    ⚠️ Migration is highly volatile and difficult to predict  
    ⚠️ This analysis only examines migration variants, not fertility/life expectancy variants  
    
    **Source:** [GLA 2024-based population projections – research outputs](https://data.london.gov.uk/blog/gla-2024-based-population-projections-research-outputs/)
    """)

# Data
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
st.sidebar.header("⚙️ Display Options")
show_gender = st.sidebar.checkbox("Show gender breakdown", value=False)
age_group_filter = st.sidebar.multiselect(
    "Select age groups to display",
    options=df['Age Group'].unique(),
    default=df['Age Group'].unique()
)

highlight_core = st.sidebar.checkbox("Highlight core 10yr projection", value=True)

# Filter data
df_filtered = df[df['Age Group'].isin(age_group_filter)]

def create_projection_chart(data, age_group, column='Persons', highlight_core=False):
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
        hovertemplate='<b>MYEs</b><br>Year: %{x}<br>Population: %{y:,.0f}<extra></extra>'
    ))
    
    # GLA Projections
    colors = {'GLA RO 5yr Migration': '#0066cc', 
              'GLA RO 10yr Migration': '#00a86b', 
              'GLA RO 15yr Migration': '#cc6600'}
    
    for dataset, color in colors.items():
        df_proj = df_age[df_age['Dataset'] == dataset]
        is_core = dataset == 'GLA RO 10yr Migration'
        
        fig.add_trace(go.Scatter(
            x=df_proj['Year'],
            y=df_proj[column],
            mode='lines+markers',
            name=dataset.replace('GLA RO ', '').replace(' Migration', '') + (' ⭐ (Core)' if is_core and highlight_core else ''),
            line=dict(color=color, width=3 if (is_core and highlight_core) else 2, dash='dash'),
            marker=dict(size=7 if (is_core and highlight_core) else 6),
            hovertemplate=f'<b>{dataset}</b><br>Year: %{{x}}<br>Population: %{{y:,.0f}}<extra></extra>'
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
    fig.add_vline(x=2024.5, line_dash="dot", line_color="grey", 
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
    
    # Get specific projection values
    proj_5yr = df_age[(df_age['Dataset'] == 'GLA RO 5yr Migration') & (df_age['Year'] == 2025)]['Persons'].values[0]
    proj_10yr = df_age[(df_age['Dataset'] == 'GLA RO 10yr Migration') & (df_age['Year'] == 2025)]['Persons'].values[0]
    proj_15yr = df_age[(df_age['Dataset'] == 'GLA RO 15yr Migration') & (df_age['Year'] == 2025)]['Persons'].values[0]
    
    # Changes (showing decreases)
    change_5yr = mye_2024 - proj_5yr
    change_10yr = mye_2024 - proj_10yr
    change_15yr = mye_2024 - proj_15yr
    
    return {
        'mye_2024': mye_2024,
        'proj_min': proj_min,
        'proj_max': proj_max,
        'proj_5yr': proj_5yr,
        'proj_10yr': proj_10yr,
        'proj_15yr': proj_15yr,
        'change_5yr': change_5yr,
        'change_10yr': change_10yr,
        'change_15yr': change_15yr,
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
                    chart = create_projection_chart(df_filtered, age_group, column, highlight_core)
                    for trace in chart.data:
                        trace.showlegend = (idx == 1)  # Only show legend for first chart
                        fig.add_trace(trace, row=1, col=idx)
                
                fig.update_layout(height=500, title_text=f"Population Projections - Ages {age_group}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig = create_projection_chart(df_filtered, age_group, highlight_core=highlight_core)
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Statistics
            stats = calculate_statistics(df_filtered, age_group)
            
            st.metric(
                label="2024 MYE (Actual)",
                value=f"{stats['mye_2024']:,.0f}"
            )
            
            st.metric(
                label="2025 Projection Range",
                value=f"{stats['proj_min']:,.0f} – {stats['proj_max']:,.0f}",
                delta=f"Range: {stats['range']:,.0f}",
                delta_color="off"
            )
            
            st.metric(
                label="⭐ Core 10yr Projection (2025)",
                value=f"{stats['proj_10yr']:,.0f}",
                delta=f"−{stats['change_10yr']:,.0f} from 2024",
                delta_color="inverse"
            )
            
            # Additional info
            st.info(f"""
            **Projected Change (2024→2025):**
            - 5yr variant: −{stats['change_5yr']:,.0f}
            - 10yr variant: −{stats['change_10yr']:,.0f}
            - 15yr variant: −{stats['change_15yr']:,.0f}
            
            **Which gives min/max:**
            - Minimum: 10yr variant ({stats['proj_min']:,.0f})
            - Maximum: 15yr variant ({stats['proj_max']:,.0f})
            - Variance: {(stats['range']/stats['mye_2024']*100):.2f}% of 2024 population
            """)
        
        st.markdown("---")
    
    # Summary table
    with st.expander("📋 View Full Data Table"):
        # Create comparison table for 2025
        comparison_data = []
        for age_group in age_group_filter:
            stats = calculate_statistics(df_filtered, age_group)
            comparison_data.append({
                'Age Group': age_group,
                '2024 MYE': f"{stats['mye_2024']:,.0f}",
                '2025 (5yr)': f"{stats['proj_5yr']:,.0f}",
                '2025 (10yr) ⭐': f"{stats['proj_10yr']:,.0f}",
                '2025 (15yr)': f"{stats['proj_15yr']:,.0f}",
                'Change from 2024 (10yr)': f"−{stats['change_10yr']:,.0f}",
                'Range (10yr-15yr)': f"{stats['range']:,.0f}"
            })
        
        comparison_df = pd.DataFrame(comparison_data)
        st.dataframe(comparison_df, use_container_width=True)
    
    # Final recommendation box
    st.success("""
    ### 📌 Recommendation for Children's Services
    
    **Use the 10-year migration variant (core projection) for planning purposes:**
    - Ages 0-19: **34,705 persons** for 2025
    - Ages 0-15: **25,516 persons** for 2025
    
    These figures represent the GLA's recommended "central" scenario and are based on the most recent 
    2024 Mid-Year Estimates. The actual 2025 MYE will be published in mid-2026, allowing verification 
    of projection accuracy.
    
    **Note:** All projections show a declining child population from 2024 to 2025, continuing the trend 
    observed since 2023. The 10-year variant shows the largest decrease, making it the most conservative projection.
    """)
    
else:
    st.warning("Please select at least one age group from the sidebar.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: grey; font-size: 12px;'>
    Data source: GLA 2024-based Population Projections (Research Outputs) | ONS Mid-Year Estimates<br>
    Created for Westminster City Council Children's Services | Last updated: December 2024
</div>
""", unsafe_allow_html=True)
