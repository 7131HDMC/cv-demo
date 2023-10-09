import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

def summary_section():
    container = st.container()
    col1, col2 = container.columns(2)
    col1.markdown("""
    # Hari Dasa Fiuza

    ❤️ I am a passionate problem solver with over three years of professional experience working on different technologies. As an engineer, my expertise lies in the development of multiplatform systems and data modeling. 
    
    I am thrilled to create innovative and efficient data-driven solutions while facing new challenges.

    """)

    # col1.download_button(
    #         label="Download CV",
    #         data=file,
    #         file_name="resume.pdf",
    #         mime="image/png"
    #       )

    col1.markdown("""
    
    ###### :sleuth_or_spy: Please feel free to contact me anytime:
- [💻LinkedIn](https://www.linkedin.com/in/hari-dasa/)
- 📫 [haridasafiuza@gmail.com](mailto:haridasafiuza@gmail.com)
    """)

    radar = radar_chart({
        "points":  [4, 5, 4, 3, 4],
        "features": ["Data Visualization", "Problem-Solving", "Statistical Analysis", "Machine Learning", "Communication"]
    })
    col2.plotly_chart(radar)

def portfolio_section():
    """ List a group of projects for skill demostration """
    container = st.container()
    container.title("Projects")

    col1, col2, col3 = container.columns(3)
    
    col1.markdown("[Portfolio Optimization](https://github.com/7131HDMC/portfolio-optimization)")
    
    col2.markdown("[Stock Monitor](https://github.com/7131HDMC/stock_monitor)")

    col3.markdown("[Credit Analysis](https://github.com/7131HDMC/loan_risk)")

def radar_chart(skills):
    """ Generate radar chart from given skillset """
    fig = go.Figure(
        data=go.Scatterpolar(
            r=skills["points"],
            theta=skills['features'],
            visible=True,
            fill='toself'
        )
    )

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True
        ),
    ),
    showlegend=False
    )

    return fig

def main():
    """App"""
    summary_section()
    st.divider()
    portfolio_section()
if __name__ == "__main__":
    main()