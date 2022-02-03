import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from neuralprophet import NeuralProphet
import matplotlib as mpl
import streamlit as st
from sklearn.preprocessing import LabelEncoder
mpl.rcParams['figure.dpi'] = 150
savefig_options = dict(format="png", bbox_inches="tight")
plt.style.use('ggplot')
from neuralprophet import set_random_seed 
import streamlit.components.v1 as components
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="Real Estate in the Dallas Fort Worth Metroplex by County", layout="wide")


image = Image.open(Path("./Data/ReSI-DATA.jpg"))

with st.sidebar:
    option = st.selectbox(
        'Please select an option',
        ('Home', 'Map', 'Graph', 'Forecast'))

if option == 'Home':
    col1, col2, col3 = st.beta_columns([3,3,3])

    with col1:
        st.write("---")

    with col2:
	
        st.image(image)
        

    with col3:
        st.write("---")



    col1, col2, col3 = st.beta_columns([1,10,1])

    with col1:
        st.write("---")

    with col2:
        st.title("Real Estate in the Dallas Fort Worth Metroplex by County") 
        

    with col3:
        st.write("---")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write("RESI-DATA is a real estate analysis service that provides easy-to-grasp analyses of housing data on the county level to help you make the most informed decision on your biggest investment. Whether you are looking to buy a home or invest inproperty, Resi-Data can help you narrow down your search based on previous market trends and high level forecasting.")
    st.write("---")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")	
    st.write("""
    This interactive dashboard is designed to visualize real estate data and market trends in the DFW metroplex. It includes data from the following counties: Collin, Dallas, Denton, Ellis, Johnson, Kaufman, Parker, Rockwall, and Tarrant.
    To explore this app, please click on the sidebar to navigate the different pages
    """)


hide_streamlit_style = """
            <style>
            footer {
	        visibility: hidden;
	            }
            footer:after {
	            content:'developed by Shruti B, Jacob E, Steven L, and Mouhamadou D'; 
	            visibility: visible;
	            display: block;
	            position: relative;
	            #background-color: red;
	            padding: 5px;
	            top: 2px;
                    }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)







if option == 'Map':
    map = st.selectbox(
    'Please select a map to view',
    ('Select', 'Median Price', 'Average Price', 'Total Listings'))    
    if map == 'Median Price':
        html_temp = """<div class='tableauPlaceholder' id='viz1643335350730' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RealEstate-DFW&#47;Sheet1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643335350730');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        median_price = components.html(html_temp, height = 1000)
        agree = st.checkbox('Show Forecast')
        if agree:
            html_data = """<div class='tableauPlaceholder' id='viz1643772012736' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Forecasting-MedianPrice&#47;Sheet43' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643772012736');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
            avg_price_forecast = components.html(html_data, height = 1000)
    elif map == 'Average Price':
        html_temp = """<div class='tableauPlaceholder' id='viz1643335455475' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RealEstate-DFW-AvgPrices&#47;Sheet12' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643335455475');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        avg_price = components.html(html_temp, height = 1000)
        agree = st.checkbox('Show Forecast')
        if agree:
            html_data = """<div class='tableauPlaceholder' id='viz1643771612727' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Forecasting-AveragePrice&#47;Sheet44' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643771612727');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
            avg_price_forecast = components.html(html_data, height = 1000)

    elif map == 'Total Listings':
        html_temp = """<div class='tableauPlaceholder' id='viz1643335597624' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='RealEstate-DFW-TotalListings&#47;Sheet13' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643335597624');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        total_list_map = components.html(html_temp, height = 1000)

if option == 'Graph':
    graph = st.selectbox(
        'Please select a graph to view',
        ('Select', 'Median Price', 'Average Price', 'Percent Change Over Time', 'Sales vs Listings'))    
    if graph == 'Median Price':
        html_temp = """<div class='tableauPlaceholder' id='viz1643338581813' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='MedianPriceoverTime&#47;Sheet4' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643338581813');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        median_time = components.html(html_temp, height = 1000)
    elif graph == 'Average Price':
        html_temp = """<div class='tableauPlaceholder' id='viz1643338627324' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='AveragePriceoverTime&#47;Sheet42' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643338627324');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        avg_time = components.html(html_temp, height = 1000)
    elif graph == 'Sales vs Listings':
        html_temp = """<div class='tableauPlaceholder' id='viz1643766932279' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SalesvsListings_16433385697830&#47;Sheet5' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643766932279');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        list_sale = components.html(html_temp, height = 2000)
    elif graph == 'Percent Change Over Time':
        html_temp = """<div class='tableauPlaceholder' id='viz1643928720286' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PercentChange-MedianPrice&#47;Sheet10' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1643928720286');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        avg_time = components.html(html_temp, height = 400)

if option == 'Forecast':
    st.write(
        """
       Select a county below to view the house price forecast up to January 2023.
        """)    

    st.write('---')   
    null4_0,row4_1, row4_2, row4_3 , row4_5= st.beta_columns((0.17,6,0.1, 1.6, 0.17))


    URL = ("dfw_county_market_tracker.csv")

    @st.cache(allow_output_mutation=True)
    def fetch_data():
        df = pd.read_csv(Path("./Data/dfw_county_market_tracker.csv"), infer_datetime_format=True)
        return df

    price_forecast = fetch_data()

    price_forecast = price_forecast.drop(['city'], axis=1)

    price_forecast = price_forecast.dropna()

    price_forecast = price_forecast[(price_forecast['property_type_id']==-1)]

    price_forecast = price_forecast[['period_begin', 'table_id', 'median_sale_price']]

    price_forecast['period_begin'] = price_forecast['period_begin'].astype('datetime64[ns]')

    price_forecast.rename(columns = {list(price_forecast)[0]: 'ds', list(price_forecast)[2]: 'y', list(price_forecast)[1]: 'region'}, inplace = True)


    with row4_1:
        st.write(
        """
        ### **Median House Price Forecast Per County**
        """) 

    null5_0,row5_1, row5_2, null= st.beta_columns((0.23,6, 4, 0.1))    

    st.write(
        """
        #### **Enter County to Forecast:** 
        """)     

    zipcode_forecast = st.selectbox('Select County', ('Collin County', 'Dallas County', 'Denton County', 'Ellis County', 'Johnson County', 'Kaufman County', 'Parker County', 'Rockwall County', 'Tarrant County' ))

    if zipcode_forecast=='Collin County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2682)]
    elif zipcode_forecast=='Dallas County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2696)]
    elif zipcode_forecast=='Denton County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2700)]
    elif zipcode_forecast=='Ellis County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2709)]
    elif zipcode_forecast=='Johnson County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2765)]
    elif zipcode_forecast=='Kaufman County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2768)]
    elif zipcode_forecast=='Parker County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2823)]
    elif zipcode_forecast=='Rockwall County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2838)]
    elif zipcode_forecast=='Tarrant County':
        zipcode_forecast = price_forecast[(price_forecast['region']==2859)]

    btn = st.button('Get Median House Price Forecast')                                        

    if btn:   
        try:
            # xz = np.array([[zipcode_forecast]])
            # df_new = pd.DataFrame(xz, columns=['region'])
                
            # now let's change datatype from object to float:
            zipcode_forecast['region'] = zipcode_forecast['region'].astype('float64')
            # filter_zippp = df_new['region'].values[0]     
            
            price_forecast = zipcode_forecast

            print(price_forecast)
        
            price_forecast.drop('region', axis=1, inplace=True)
            
            model_final = NeuralProphet(
                                        n_changepoints=40,
                                        changepoints_range=0.90,
                                        num_hidden_layers=2,
                                        #learning_rate=1.0,
                                        seasonality_mode="multiplicative",
                                        #n_lags=14,
                                        #n_forecasts=14,
                                    ) 
            # For reporducibility and to have identical forecast each time, let's set the seed from prophet:
            set_random_seed(0)
            metrics = model_final.fit(price_forecast, freq='MS')
        
            future = model_final.make_future_dataframe(price_forecast, periods=14, 
                                                    n_historic_predictions=len(price_forecast)) #forecast for 14 Months
            forecast = model_final.predict(future) 
        
            
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=forecast['ds'], y=forecast['y'], 
                                        name='Actual Price', opacity=0.7,
                                        line=dict(color='green', width=4)))
            fig1.add_trace(go.Scatter(x=forecast['ds'],y=forecast['yhat1'], 
                                        name = 'Forecast Price',
                                        line=dict(color='firebrick', width=4, dash='dash')))

            fig1.add_vrect(x0="2021-05-01", x1="2022-06-01", 
                            line_width=0, fillcolor="red", opacity=0.2, annotation_text="Forecast  ", annotation_position="inside top left",
                            annotation=dict(font_size=14, font_family="Comic Sans MS"))
            fig1.add_vrect(x0="2021-04-01", x1="2021-04-01", 
                            line_width=8, fillcolor="green", opacity=0.8, annotation_text="Current  ", annotation_position="outside top left",
                            annotation=dict(font_size=14, font_family="Comic Sans MS"))

            fig1.update_xaxes(rangeselector_activecolor="#EBD2B9",
                                rangeslider_visible=True,
                                rangeselector=dict(
                                                    buttons=list([
                                                                dict(count=2, label="2y", step="year", stepmode="backward"),
                                                                dict(count=3, label="3y", step="year", stepmode="backward"),
                                                                dict(count=4, label="4y", step="year", stepmode="backward"),
                                                                dict(count=5, label="5y", step="year", stepmode="backward"),
                                                                dict(step="all")
                                                                ])
                                                    )
                                )               
                # Edit the layout
            fig1.update_layout(title='House Sale Price Actual vs Forecast',
                                xaxis_title='Time', height=600, width=1500,
                                yaxis_title='House Price')
            st.plotly_chart(fig1, use_container_width=False)
        
        except Exception as e:
            row5_1.error(e)
