from fastapi import FastAPI, File, UploadFile,Response
import time
timestr =time.strftime("%Y%m%d-%H%M%S")
from fastapi.responses import JSONResponse
import uvicorn
import json
import requests
from fastapi import Request, FastAPI
from fastapi.responses import HTMLResponse
from typing import List
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
from typing import List
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
import plotly.graph_objs as go
import base64
import plotly.express as px
from bs4 import BeautifulSoup
from pydantic import BaseModel


app = FastAPI()

@app.get("/home", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Startup Objectives</title>
        </head>
        <body>
            <div style="background-color: #f5d742; padding: 10px;">
                <h1 style="color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">John Doe</h1>
                <p style="color: #000; font-family: 'Roboto', sans-serif;">Objective: To create a sustainable energy solution for rural communities.</p>
            </div>
            <div style="background-color: #ff6f69; padding: 10px;">
                <h1 style="color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Jane Smith</h1>
                <p style="color: #000; font-family: 'Roboto', sans-serif;">Objective: To develop a platform that simplifies the process of making investments in real estate.</p>
            </div>
            <div style="background-color: #70c1b3; padding: 10px;">
                <h1 style="color: #fff; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">Mark Johnson</h1>
                <p style="color: #000; font-family: 'Roboto', sans-serif;">Objective: To build a product that helps small businesses increase their online visibility.</p>
            </div>
        </body>
    </html>
    """
@app.get("/back", response_class=HTMLResponse)
async def read_root():
    return """
        <html>
            <head>
                <title>Startup Objectives</title>
            </head>
            <body>
                <h1 style="background-color: #FCE205; color: #223843; font-family: Arial, sans-serif; padding: 20px; text-align: center;">Startup Objectives</h1>
                <p style="background-color: #F7F7F7; color: #223843; font-family: Arial, sans-serif; padding: 10px;">Person 1<br>
                Full Name: John Doe<br>
                Objective: To create a sustainable energy solution for rural communities.</p>
                <p style="background-color: #F7F7F7; color: #223843; font-family: Arial, sans-serif; padding: 10px;">Person 2<br>
                Full Name: Jane Smith<br>
                Objective: To develop a platform that simplifies the process of making investments in real estate.</p>
                <p style="background-color: #F7F7F7; color: #223843; font-family: Arial, sans-serif; padding: 10px;">Person 3<br>
                Full Name: Mark Johnson<br>
                Objective: To build a product that helps small businesses increase their online visibility.</p>
            </body>
        </html>
    """
@app.get("/", response_class=HTMLResponse)
async def read_item():
    return """
    <html>
        <head>
            <style>
                body {
                    background-color: #E6E6FA;
                    color: #333333;
                    font-family: Arial, sans-serif;
                    font-size: 16px;
                    line-height: 1.5;
                    padding: 30px;
                }
                h1 {
                    font-size: 36px;
                    font-weight: bold;
                    margin-top: 0;
                }
                h3 {
                    font-size: 24px;
                    font-weight: bold;
                    margin-top: 30px;
                }
                p {
                    margin-top: 0;
                }
            </style>
        </head>
        <body>
            <center><h1>Electronics Startup</h1>
            <hr>
            <h3>Co-founders</h3>
            <h2>Harsh Sanjay Shah</h2>
            <p>Objective: "Developing and implementing effective sales and marketing strategies to increase mobile phone sales and improve customer retention, while leveraging data insights to optimize revenue and profits."</p>
            <p> Work,Position - Innovation and Development,Chief Executive Officer(CEO)</p>
            <h2>Jay R Patel</h2>
            <p>Objective: "Creating and executing successful marketing plans to boost TV sales and customer loyalty, utilizing data analysis to maximize revenue and profitability."</p>
            <p> Work,position -Technical Department,  Chief Technology Officer(CTO)
            <h2>Mark Johnson</h2>
            <p>To build a product that helps small businesses increase their online visibility.</p></center>
        </body>
    </html>
    """





with open("/Users/jaypatel/Downloads/Data Wrangling/mobiles_dataa.json") as f:
    mobiledata = json.load(f)

# Endpoint to retrieve all products
@app.get('/products1')
async def get_products():
    return mobiledata
# Endpoint to retrieve products by brand
@app.get('/products1/{brand1}')
async def get_products_by_brand(mobiledata: str):
    products = [product for product in data if product['Brand'].lower() == brand.lower()]
    if len(products) == 0:
        return {'message': 'No products found'}
    return products

# Endpoint to retrieve a specific product by brand and model
@app.get('/products1/{brand1}/{model1}')
async def get_product(brand: str, model: str):
    for product in mobiledata:
        if product['Brand'].lower() == brand.lower() and product['Model'].lower() == model.lower():
            return product
    return {'message': 'Product not found'}








# Define the endpoint for the report
@app.get("/mobile-report", response_class=HTMLResponse)
async def generate_mobile_report():


    # Calculate the total price and average price of all mobiles
    total_price = sum(mobile["Price_in_India"] for mobile in mobiledata)
    avg_price = total_price / len(data)

    # Generate HTML for individual mobiles
    mobile_template = """
    <div class="mobile">
      <img src="{Picture_URL}" alt="{Brand} {Model}">
      <h2>{Brand} {Model}</h2>
      <p><strong>Price:</strong> {Price_in_India}</p>
      <p><strong>Total Ratings:</strong> {Total_Ratings}</p>
      <p><strong>Battery_capacity(mAh):</strong> {Battery_capacity(mAh)} </p>
      <p><strong>RAM:</strong> {RAM}</p>
      <p><strong>Internal_storage:</strong> {Internal_storage}</p>
      <p><strong>Processor:</strong> {Processor}</p>
      <p><strong>Operating_system:</strong> {Operating_system} kg</p>
      <p><strong>Screen_size(inches):</strong> {Screen_size(inches)} Hz</p>
    </div>
    """
    mobiles_html = ""
    for mobile in mobiledata:
        mobiles_html += mobile_template.format(**mobile)

    # Define an HTML template for the report
    report_template = """
    <!DOCTYPE html>
    <html>
    <head>
      <center><title>Mobile Data Report</title></center>
      <style>
        .mobile-container {{
          overflow: auto;
        }}
        .mobile {{
          border: 1px solid black;
          padding: 20px;
          margin: 20px;
          float: left;
          width: 300px;
          height: 550px;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <h1>Mobile Data Report</h1>
      <p><strong>Total Price: {total_price}</strong>  </p>
      <p><strong>Average Price: {avg_price:.2f}</strong>  </p>
      <div class="mobile-container">
        {mobile_html}
      </div>
    </body>
    </html>
    """

    # Generate HTML for the report
    html = report_template.format(total_price=total_price, avg_price=avg_price, mobile_html=mobiles_html)

    # Return the HTML as a response
    return html


@app.get("/battery_capacity_vs_price")
def battery_capacity_vs_price():
    # Define data for the scatter plot
    x_data = [d['Price_in_India'] for d in mobiledata]
    y_data = [d['Battery_capacity(mAh)'] for d in mobiledata]
    text_data = [f"{d['Brand']} {d['Product_Name']} ({d['Total_Ratings']} reviews)" for d in mobiledata]

    # Define the scatter plot layout
    layout = go.Layout(title='Mobile Battery Capacity vs. Price in India', title_font=dict(size=20),
                       xaxis=dict(title='Price in India', title_font=dict(size=16)),
                       yaxis=dict(title='Battery Capacity (mAh)', title_font=dict(size=16)))

    # Create the scatter plot
    fig = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='markers',
                                     marker=dict(color='#00C9FF', size=10),
                                     text=text_data, hoverinfo='text')], layout=layout)

    # Embed the plot in an HTML page
    plot_div = fig.to_html(full_html=False)
    html_content = f"""
    <html>
        <head>
            <title>Mobile Battery Capacity vs. Price in India</title>
        </head>
        <body>
            <h1>Mobile Battery Capacity vs. Price in India</h1>
            <div>{plot_div}</div>
        </body>
    </html>
    """

    # Return the HTML page with the embedded plot
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/price_screen_size")
async def plot_price_screen_size():
    # Create a list of dictionaries for each phone's price and screen size
    price_screen_size = []
    for dat in mobiledata:
        price = dat['Price_in_India']
        screen_size = dat['Screen_size(inches)']
        if price != "" and screen_size != "":
            price_screen_size.append({'Price': int(price), 'Screen Size': float(screen_size)})
    # Create a scatter plot of price vs. screen size
    fig = px.scatter(price_screen_size, x='Screen Size', y='Price', title='Price vs. Screen Size')
    fig.update_layout(height=500, width=1000)
    # Return the plot as an HTMLResponse
    return HTMLResponse(content=fig.to_html(), status_code=200)

# Define data for the bar plot
totals = {}
counts = {}
# Iterate over the data and update the totals and counts for each brand
for item in mobiledata:
    brand = item['Brand']
    price = item['Price_in_India']
    if brand in totals:
        totals[brand] += price
        counts[brand] += 1
    else:
        totals[brand] = price
        counts[brand] = 1
# Calculate the average prices for each brand
averages = {brand: totals[brand]/counts[brand] for brand in totals}
# Sort the brands by average price in descending order
sorted_brands = sorted(averages, key=averages.get, reverse=True)
# Get the average prices and brand names in separate lists
avg_prices = [averages[brand] for brand in sorted_brands]
brand_names = [brand for brand in sorted_brands]

# Create a bar plot of the average prices for each brand
fig, ax = plt.subplots(figsize=(12,6))
ax.bar(np.arange(len(avg_prices)), avg_prices)
ax.set_xticks(np.arange(len(avg_prices)))
ax.set_xticklabels(brand_names, rotation=90)
ax.set_xlabel('Brand')
ax.set_ylabel('Average price')
ax.set_title('Average prices for each brand')

# Convert the plot to a PNG image
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

# Convert the PNG image to a base64-encoded string
image_base64 = base64.b64encode(image_png).decode()

# Define the route to display the plot
@app.get("/brand-ratings")
async def display_brand_ratings():
    # Create a dictionary to store the total rating for each brand
    brand_rating = {}
    # Calculate the total rating for each brand
    for row in mobiledata:
        brand = row['Brand']
        rating = row['Total_Ratings']
        if brand in brand_rating:
            brand_rating[brand] += rating
        else:
            brand_rating[brand] = rating
    # Sort the brand_rating dictionary by value in ascending order
    brand_rating_sorted = sorted(brand_rating.items(), key=lambda x: x[1],reverse=True)
    # Extract the sorted brands and ratings
    brands = [item[0] for item in brand_rating_sorted]
    ratings = [item[1] for item in brand_rating_sorted]
    # Create a bar plot of total rating versus brand in ascending order
    fig, ax = plt.subplots(figsize=(15,6))
    ax.bar(brands, ratings)
    # Set the x- and y-axis labels and the plot title
    ax.set_xlabel('Brand')
    ax.set_ylabel('Higher Rating')
    plt.title('Total Rating by Brands')
    # Rotate the x-axis tick labels
    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')
    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Return the plot image as a response
    return Response(content=buf.getvalue(), media_type='image/png')

# Define an HTML template for the response
html_template = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Mobile Price Report</title>
</head>
<body>
  <h1>Mobile Price Report</h1>
  <img src="data:image/png;base64,{image_base64}" alt="Mobile Price Report">
</body>
</html>
"""

# Define a route for the HTML response
@app.get("/avg_price_and_brand", response_class=HTMLResponse)
async def get_avg_price_and_brand():
    return html_template


@app.get("/")
def my_main_page():
    return{"message":"welcome to the to new website"}

with open("/Users/jaypatel/Downloads/Data Wrangling/presentation/Tvdata.json") as f:
    data = json.load(f)

# Endpoint to retrieve all products
@app.get('/products')
async def get_products():
    return data
# Endpoint to retrieve products by brand
@app.get('/products/{brand}')
async def get_products_by_brand(brand: str):
    products = [product for product in data if product['Brand'].lower() == brand.lower()]
    if len(products) == 0:
        return {'message': 'No products found'}
    return products

# Endpoint to retrieve a specific product by brand and model
@app.get('/products/{brand}/{model}')
async def get_product(brand: str, model: str):
    for product in data:
        if product['Brand'].lower() == brand.lower() and product['Model'].lower() == model.lower():
            return product
    return {'message': 'Product not found'}

@app.get("/wordcloud", response_class=HTMLResponse)
async def generate_wordcloud():
    brands = [item['Brand'] for item in data]
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(' '.join(brands))
    plt.figure(figsize=(12,8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig("wordcloud.png", bbox_inches='tight')
    plt.close()
    with open("wordcloud.png", "rb") as image_file:
        encoded_image = io.BytesIO(image_file.read())
    return Response(content=encoded_image.getvalue(), media_type="image/png")




# Define an HTML template for displaying a single TV
tv_template = """
<div class="tv">
  <img src="{PictureURL}" alt="{Brand} {Model}">
  <h2>{Brand} {ProductName} {Model}</h2>
  <p><strong>Price:</strong> ₹{price_in_india}</p>
  <p><strong>Display Size:</strong> {display_size} inch</p>
  <p><strong>Resolution:</strong> {resolution_standard} {resolution_pixels}</p>
  <p><strong>USB Ports:</strong> {no_of_usb_port}</p>
  <p><strong>HDMI Ports:</strong> {no_of_hdmi_port}</p>
  <p><strong>Smart TV:</strong> {smart_tv}</p>
  <p><strong>Weight:</strong> {weight_without_stand} kg</p>
  <p><strong>Refresh Rate:</strong> {refresh_rate_hz} Hz</p>
</div>
"""

# Generate HTML for individual TVs
tv_html = ""
for tv in data:
    tv_html += tv_template.format(**tv)

# Define an HTML template for the report
report_template = """
<!DOCTYPE html>
<html>
<head>
  <title>TV Data Report</title>
  <style>
    .tv-container {{
      overflow: auto;
    }}
    .tv {{
      border: 1px solid black;
      padding: 20px;
      margin: 20px;
      float: left;
      width: 300px;
      height: 670px;
      text-align: center;
    }}
  </style>
</head>
<body>
  <h1>TV Data Report</h1>
  <p><strong>Total Price:</strong> ₹{total_price}</p>
  <p><strong>Average Price:</strong> ₹{avg_price:.2f}</p>
  <div class="tv-container">
    {tv_html}
  </div>
</body>
</html>
"""

# Define the endpoint for the report
@app.get("/report", response_class=HTMLResponse)
async def generate_report():
    # Calculate total price and average price
    total_price = sum(tv['price_in_india'] for tv in data)
    avg_price = total_price / len(data)

    # Generate HTML for the report
    html = report_template.format(total_price=total_price, avg_price=avg_price, tv_html=tv_html)

    # Return the HTML response
    return html

@app.get("/tv_brands")
async def get_tv_brands():
    types_tv = [item['Brand'] for item in data]
    # Count the number of occurrences of each unique TV brand
    brand_counts = {}
    for brand in types_tv:
        if brand in brand_counts:
            brand_counts[brand] += 1
        else:
            brand_counts[brand] = 1

    # Sort the brand counts in descending order
    sorted_counts = sorted(brand_counts.items(), key=lambda x: x[1], reverse=True)

    # Create a histogram of the prices
    fig, ax = plt.subplots(figsize=(20,6))
    plt.xticks(rotation=90)
    plt.bar([x[0] for x in sorted_counts], [x[1] for x in sorted_counts])
    plt.title('Count of different TV brands')
    plt.xlabel('Brand')
    plt.ylabel('Count')

    # Save the figure as a PNG and return it as a response
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")

@app.get("/brand_vs_price_plot")
async def brand_vs_price_plot():
    # Compute average prices by brand
    brand_prices = {}
    for item in data:
        brand = item['Brand']
        price_str = item['price_in_india']
        price = float(price_str)  # convert to float

        if brand in brand_prices:
            brand_prices[brand].append(price)
        else:
            brand_prices[brand] = [price]

    brand_avg_prices = {}
    for brand, prices in brand_prices.items():
        avg_price = np.mean(prices)
        brand_avg_prices[brand] = avg_price

    # Generate plot
    sorted_brands = sorted(brand_avg_prices.items(), key=lambda x: x[1], reverse=True)
    sorted_brands_names = [x[0] for x in sorted_brands]
    sorted_brands_prices = [x[1] for x in sorted_brands]

    fig, ax = plt.subplots(figsize=(20,6))
    ax.bar(sorted_brands_names, sorted_brands_prices)
    ax.set_xlabel('Brand')
    ax.set_ylabel('Average Price')
    ax.set_title('Brand vs Average Price')
    plt.xticks(rotation=90)

    # Convert plot to PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Return PNG image as response
    return StreamingResponse(buffer, media_type='image/png')


@app.get("/sonytvs")
async def getsonytvs():
    sonytvs = """
    <!DOCTYPE html>

    <html>
    <body>
    <center><h1 style="background-color:White;">Sony tv top model</h1></center>
    <input type= "text" placeholder="search">
    <div>
    <h1 style="background-color:Sony BRAVIA KD-55X74K 55 inch (139 cm) LED 4K TV;">Sony BRAVIA KD-55X74K 55 inch (139 cm) LED 4K TV</h1>
    <img src="https://www.91-img.com/pictures/television/sony/sony-bravia-kd-55x74k-151034-large-1.jpg?w=0&h=901&q=80&c=1" style="aline:top; width=20%; height=20%;">
    <p style="float: right; text-align: justify; font-size: 15px;margin-left: 10px;margin-right:auto; width: 70%;">
     <strong style="font-size:20px;">Price Rs. 59,990</strong>

    </br>
    <strong>
    KEY SPECS
    </strong>
    </br>
    <strong>
    Display
    </strong>
    </br>
    55 Inch (139.7 cm), LED
    </br>
    4K, 3840x2160
    </br>
    60 Hz
    </br>
    This is Sony BRAVIA 55 inch LED 4K tvs and this product avilable in ours website in discounted price for more information check website and others featurs like 2 usb ports, 3 hdmi sports,apps and games and many more.





    </p>
    </div>
    <div>
    <h1 style="background-color:Sony BRAVIA KD-50X74K 50 inch (127 cm) LED 4K TV;">Sony BRAVIA KD-50X74K 50 inch (127 cm) LED 4K TV</h1 style="aline:bottm; width=20%; height=20%;">
    <img src="https://www.91-img.com/pictures/television/sony/sony-bravia-kd-50x74k-151036-large-1.jpg?w=0&h=901&q=80&c=1">
    <p style="float: right; text-align: justify; font-size: 15px;margin-left: 10px;margin-right:auto; width: 70%;">
    <strong style="font-size:20px;">Price Rs. 51,990</strong>
    </br>
    <strong>KEY SPECS</strong>
    </br>
    <strong>
    Display
    </strong>
    </br>
    50 Inch (127 cm), LED
    </br>
    4K, 3840x2160
    </br>
    60 Hz
    </br>
    This is Sony BRAVIA 55 inch LED 4K tvs and this product avilable in ours website in discounted price for more information check website and others featurs like 2 usb ports, 3 hdmi sports,apps and games and many more.


    </p>


    </div>
    </body> 

    </html>

    """

    return HTMLResponse(content=sonytvs)




# Define a route for the pie chart
@app.get('/piechart')
async def piechart():
    # Get the screen type counts
    screen_type_counts = {}
    for item in data:
        screen_type = item['screen_type']
        if screen_type in screen_type_counts:
            screen_type_counts[screen_type] += 1
        else:
            screen_type_counts[screen_type] = 1

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=list(screen_type_counts.keys()), values=list(screen_type_counts.values()))])

    # Set the title for the chart
    fig.update_layout(title='TV Screen Type Distribution')

    # Convert the chart to HTML and return as a response
    chart_html = fig.to_html(full_html=False, default_height=500, default_width=700)
    return HTMLResponse(content=chart_html, status_code=200)



# Define an HTML template for displaying a single TV
tv_template = """
<div class="tv">
  <img src="{PictureURL}" alt="{Brand} {Model}">
  <h2>{Brand} {ProductName} {Model}</h2>
  <p><strong>Price:</strong> ₹{price_in_india}</p>
  <p><strong>Display Size:</strong> {display_size} inch</p>
  <p><strong>Resolution:</strong> {resolution_standard} {resolution_pixels}</p>
  <p><strong>USB Ports:</strong> {no_of_usb_port}</p>
  <p><strong>HDMI Ports:</strong> {no_of_hdmi_port}</p>
  <p><strong>Smart TV:</strong> {smart_tv}</p>
  <p><strong>Weight:</strong> {weight_without_stand} kg</p>
  <p><strong>Refresh Rate:</strong> {refresh_rate_hz} Hz</p>
</div>
"""

# Define an HTML template for the report
report_template = """
<!DOCTYPE html>
<html>
<head>
  <title>TV Data Report</title>
  <style>
    .tv-container {{
      overflow: auto;
    }}
    .tv {{
      border: 1px solid black;
      padding: 20px;
      margin: 20px;
      float: left;
      width: 300px;
      height: 670px;
      text-align: center;
    }}
  </style>
</head>
<body>
  <h1>Top 10 TV</h1>
  <div class="tv-container">
    {tv_html}
  </div>
</body>
</html>
"""



@app.get("/top_tvs", response_class=HTMLResponse)
def get_top_tvs():
    # Sort the TV data based on price and display size
    sorted_tvs = sorted(data, key=lambda tv: (tv['price_in_india'], tv['display_size']), reverse=True)
    top_tvs = sorted_tvs[:10]

    # Build the HTML response for the top 10 TVs
    tv_html = ""
    for tv in top_tvs:
        tv_html += tv_template.format(**tv)

    # Build the HTML response for the report
    report_html = report_template.format(tv_html=tv_html)

    return report_html


@app.get("/oneplustvs")
async def oneplustvs():
    oneplustvs = """
    <!DOCTYPE html>

    <html>
    <body>
    <center><h1 style="background-color:White;">OnePlus tv top model</h1></center>
    <input type= "text" placeholder="search">
    <div>
    <h1 style="OnePlus Y1S Pro 43 inch (109 cm) LED 4K TV;">OnePlus Y1S Pro 43 inch (109 cm) LED 4K TV</h1>
    <img src="https://www.91-img.com/pictures/television/oneplus/oneplus-y1s-pro-150165-large-1.jpg?tr=q-80" style="aline:top; width=20%; height=20%;">
    <p style="float: right; text-align: justify; font-size: 15px;margin-left: 10px;margin-right:auto; width: 70%;">
     <strong style="font-size:20px;">Price Rs. 29,990</strong>

    </br>
    <strong>
    KEY SPECS
    </strong>
    </br>
    <strong>
    Display
    </strong>
    </br>
   	43 Inch (109.22 cm), LED
    </br>
    4K, 3840x2160
    </br>
    60 Hz
    </br>
    This is OnePlus  Model	Y1S Pro 43 inch (109 cm) LED 4K TVand this product avilable in ours website in discounted price for more information check website and others featurs like 2 usb ports, 3 hdmi sports,apps and games and many more.
    </p>
    </div>
    <div>
    <h1 style="background-color:OnePlus Y1S 32 inch (81 cm) LED HD-Ready TV;">OnePlus Y1S 32 inch (81 cm) LED HD-Ready TV</h1 style="aline:bottm; width=20%; height=20%;">
    <img src="https://www.91-img.com/pictures/television/oneplus/oneplus-y1s-149493-large-1.jpg?tr=q-80">
    <p style="float: right; text-align: justify; font-size: 15px;margin-left: 10px;margin-right:auto; width: 70%;">
    <strong style="font-size:20px;">Price Rs. 13,999</strong>
    </br>
    <strong>KEY SPECS</strong>
    </br>
    <strong>
    Display
    </strong>
    </br>
    32 Inch (81.28 cm), LED
    </br>
    HD-Ready, 1366x768
    </br>
    60 Hz
    </br>
    This is OnePlus Y1S 32 inch (81 cm) LED HD-Ready TV and this product avilable in ours website in discounted price for more information check website and others featurs like 2 usb ports, 3 hdmi sports,apps and games and many more.


    </p>


    </div>
    <div>
    <h1 style="background-color:OnePlus Y1S 43 inch (109 cm) LED Full HD TV;">OnePlus Y1S 43 inch (109 cm) LED Full HD TV</h1 style="aline:bottm; width=20%; height=20%;">
    <img src="https://www.91-img.com/pictures/television/oneplus/oneplus-y1s-43-inch-led-full-hd-tv-149512-large-1.jpg?tr=q-80">
    <p style="float: right; text-align: justify; font-size: 15px;margin-left: 10px;margin-right:auto; width: 70%;">
    <strong style="font-size:20px;">Price Rs. Rs. 23,999</strong>
    </br>
    <strong>KEY SPECS</strong>
    </br>
    <strong>
    Display
    </strong>
    </br>
    43 Inch (109.22 cm), LED
    </br>
    Full HD, 1920x1080
    </br>

    This is OnePlus Y1S 43 inch (109 cm) LED Full HD TV and this product avilable in ours website in discounted price for more information check website and others featurs like 2 usb ports, 3 hdmi sports,apps and games and many more.


    </p>


    </body> 

    </html>

    """

    return HTMLResponse(content=oneplustvs)

app = FastAPI()


@app.get("/mobiles")
async def getsonytvs():
    mobiles = """

<!DOCTYPE html>
<html>
<head>
  <title>TV Data Dashboard</title>
  <style>
    /* Style for the navigation bar */
    .navbar {
      overflow: hidden;
      background-color: #333;
      font-family: Arial;
    }

    .navbar a {
      float: left;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
    }

    .navbar a:hover {
      background-color: #ddd;
      color: black;
    }

    /* Style for the page content */
    .content {
      padding: 20px;
      font-family: Arial;
    }
  </style>
</head>
<body>
  <!-- Navigation bar -->
  <div class="navbar">
    <a href="/mobileplot">Mobile Plot</a>
    <a href="/mobile-report">Mobile Report</a>
    
  </div>

  <!-- Page content goes here -->
  <div class="content">
    <h1>Welcome to the TV Data Dashboard</h1>
    <p>Select a link from the navigation bar above to view different sections of the dashboard.</p>
  </div>
</body>
</html>
"""

    return HTMLResponse(content=mobiles)


@app.get("/mobileplot")
async def mobileplot():
    mobileplot = """

<!DOCTYPE html>
<html>
<head>
	<title>TV Data Navigation Bar</title>
	<style>
		.nav {
			background-color: #333;
			overflow: hidden;
		}

		.nav a {
			float: left;
			color: white;
			text-align: center;
			padding: 14px 16px;
			text-decoration: none;
			font-size: 17px;
		}

		.nav a:hover {
			background-color: #ddd;
			color: black;
		}

		.active {
			background-color: #4CAF50;
			color: white;
		}
	</style>
</head>
<body>
	<div class="nav">
		<a class="active" href="/report">Plot</a>

		<a href="/battery_capacity_vs_price">Mobile Brands Distribution Pie Chart</a>
		<a href="/price_screen_size">Brand vs Screen size Plot</a>
		<a href="/brand-ratings">mobile Brands Ratings</a>
		<a href="/avg_price_and_brand">Price vs Brand</a>
	</div>
</body>
</html>

"""

    return HTMLResponse(content=mobileplot)

@app.get("/battery_capacity_vs_price")
def battery_capacity_vs_price():
    # Define data for the scatter plot
    x_data = [d['Price_in_India'] for d in mobiledata]
    y_data = [d['Battery_capacity(mAh)'] for d in mobiledata]
    text_data = [f"{d['Brand']} {d['Product_Name']} ({d['Total_Ratings']} reviews)" for d in mobiledata]

    # Define the scatter plot layout
    layout = go.Layout(title='Mobile Battery Capacity vs. Price in India', title_font=dict(size=20),
                       xaxis=dict(title='Price in India', title_font=dict(size=16)),
                       yaxis=dict(title='Battery Capacity (mAh)', title_font=dict(size=16)))

    # Create the scatter plot
    fig = go.Figure(data=[go.Scatter(x=x_data, y=y_data, mode='markers',
                                     marker=dict(color='#00C9FF', size=10),
                                     text=text_data, hoverinfo='text')], layout=layout)

    # Embed the plot in an HTML page
    plot_div = fig.to_html(full_html=False)
    html_content = f"""
    <html>
        <head>
            <title>Mobile Battery Capacity vs. Price in India</title>
        </head>
        <body>
            <h1>Mobile Battery Capacity vs. Price in India</h1>
            <div>{plot_div}</div>
        </body>
    </html>
    """

    # Return the HTML page with the embedded plot
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/price_screen_size")
async def plot_price_screen_size():
    # Create a list of dictionaries for each phone's price and screen size
    price_screen_size = []
    for dat in mobiledata:
        price = dat['Price_in_India']
        screen_size = dat['Screen_size(inches)']
        if price != "" and screen_size != "":
            price_screen_size.append({'Price': int(price), 'Screen Size': float(screen_size)})
    # Create a scatter plot of price vs. screen size
    fig = px.scatter(price_screen_size, x='Screen Size', y='Price', title='Price vs. Screen Size')
    fig.update_layout(height=500, width=1000)
    # Return the plot as an HTMLResponse
    return HTMLResponse(content=fig.to_html(), status_code=200)

# Define data for the bar plot
totals = {}
counts = {}
# Iterate over the data and update the totals and counts for each brand
for item in mobiledata:
    brand = item['Brand']
    price = item['Price_in_India']
    if brand in totals:
        totals[brand] += price
        counts[brand] += 1
    else:
        totals[brand] = price
        counts[brand] = 1
# Calculate the average prices for each brand
averages = {brand: totals[brand]/counts[brand] for brand in totals}
# Sort the brands by average price in descending order
sorted_brands = sorted(averages, key=averages.get, reverse=True)
# Get the average prices and brand names in separate lists
avg_prices = [averages[brand] for brand in sorted_brands]
brand_names = [brand for brand in sorted_brands]

# Create a bar plot of the average prices for each brand
fig, ax = plt.subplots(figsize=(12,6))
ax.bar(np.arange(len(avg_prices)), avg_prices)
ax.set_xticks(np.arange(len(avg_prices)))
ax.set_xticklabels(brand_names, rotation=90)
ax.set_xlabel('Brand')
ax.set_ylabel('Average price')
ax.set_title('Average prices for each brand')

# Convert the plot to a PNG image
buffer = io.BytesIO()
plt.savefig(buffer, format='png')
buffer.seek(0)
image_png = buffer.getvalue()
buffer.close()

# Convert the PNG image to a base64-encoded string
image_base64 = base64.b64encode(image_png).decode()

# Define the route to display the plot
@app.get("/brand-ratings")
async def display_brand_ratings():
    # Create a dictionary to store the total rating for each brand
    brand_rating = {}
    # Calculate the total rating for each brand
    for row in mobiledata:
        brand = row['Brand']
        rating = row['Total_Ratings']
        if brand in brand_rating:
            brand_rating[brand] += rating
        else:
            brand_rating[brand] = rating
    # Sort the brand_rating dictionary by value in ascending order
    brand_rating_sorted = sorted(brand_rating.items(), key=lambda x: x[1],reverse=True)
    # Extract the sorted brands and ratings
    brands = [item[0] for item in brand_rating_sorted]
    ratings = [item[1] for item in brand_rating_sorted]
    # Create a bar plot of total rating versus brand in ascending order
    fig, ax = plt.subplots(figsize=(15,6))
    ax.bar(brands, ratings)
    # Set the x- and y-axis labels and the plot title
    ax.set_xlabel('Brand')
    ax.set_ylabel('Higher Rating')
    plt.title('Total Rating by Brands')
    # Rotate the x-axis tick labels
    plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')
    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Return the plot image as a response
    return Response(content=buf.getvalue(), media_type='image/png')

# Define an HTML template for the response
html_template = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Mobile Price Report</title>
</head>
<body>
  <h1>Mobile Price Report</h1>
  <img src="data:image/png;base64,{image_base64}" alt="Mobile Price Report">
</body>
</html>
"""

# Define a route for the HTML response
@app.get("/avg_price_and_brand", response_class=HTMLResponse)
async def get_avg_price_and_brand():
    return html_template

@app.get("/mobilereport")
async def getreport():
    mobilereport = """

<!DOCTYPE html>
<html>
<head>
	<title>TV Data Navigation Bar</title>
	<style>
		.nav {
			background-color: #333;
			overflow: hidden;
		}

		.nav a {
			float: left;
			color: white;
			text-align: center;
			padding: 14px 16px;
			text-decoration: none;
			font-size: 17px;
		}

		.nav a:hover {
			background-color: #ddd;
			color: black;
		}

		.active {
			background-color: #4CAF50;
			color: white;
		}
	</style>
</head>
<body>
	<div class="nav">
		<a class="active" href="/report">mobilereport</a>

		<a href="/mobile-report">Mobile</a>

	</div>
</body>
</html>

"""

    return HTMLResponse(content=mobilereport)

# Define the endpoint for the report
@app.get("/mobile-report", response_class=HTMLResponse)
async def generate_mobile_report():


    # Calculate the total price and average price of all mobiles
    total_price = sum(mobile["Price_in_India"] for mobile in mobiledata)
    avg_price = total_price / len(data)

    # Generate HTML for individual mobiles
    mobile_template = """
    <div class="mobile">
      <img src="{Picture_URL}" alt="{Brand} {Model}">
      <h2>{Brand} {Model}</h2>
      <p><strong>Price:</strong> {Price_in_India}</p>
      <p><strong>Total Ratings:</strong> {Total_Ratings}</p>
      <p><strong>Battery_capacity(mAh):</strong> {Battery_capacity(mAh)} </p>
      <p><strong>RAM:</strong> {RAM}</p>
      <p><strong>Internal_storage:</strong> {Internal_storage}</p>
      <p><strong>Processor:</strong> {Processor}</p>
      <p><strong>Operating_system:</strong> {Operating_system} kg</p>
      <p><strong>Screen_size(inches):</strong> {Screen_size(inches)} Hz</p>
    </div>
    """
    mobiles_html = ""
    for mobile in mobiledata:
        mobiles_html += mobile_template.format(**mobile)

    # Define an HTML template for the report
    report_template = """
    <!DOCTYPE html>
    <html>
    <head>
      <center><title>Mobile Data Report</title></center>
      <style>
        .mobile-container {{
          overflow: auto;
        }}
        .mobile {{
          border: 1px solid black;
          padding: 20px;
          margin: 20px;
          float: left;
          width: 300px;
          height: 550px;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <h1>Mobile Data Report</h1>
      <p><strong>Total Price: {total_price}</strong>  </p>
      <p><strong>Average Price: {avg_price:.2f}</strong>  </p>
      <div class="mobile-container">
        {mobile_html}
      </div>
    </body>
    </html>
    """

    # Generate HTML for the report
    html = report_template.format(total_price=total_price, avg_price=avg_price, mobile_html=mobiles_html)

    # Return the HTML as a response
    return html


app = FastAPI()

# define the endpoint for the report
@app.get("/mobile-report", response_class=HTMLResponse)
async def generate_mobile_report(brand: str = None):
    # filter mobile data based on brand name if provided
    if brand:
        mobiledata_filtered = [mobile for mobile in mobiledata if mobile["Brand"] == brand]
    else:
        mobiledata_filtered = mobiledata

    # Calculate the total price and average price of all mobiles
    total_price = sum(mobile["Price_in_India"] for mobile in mobiledata_filtered)
    avg_price = total_price / len(mobiledata_filtered)

    # Generate HTML for individual mobiles
    mobile_template = """
    <div class="mobile">
      <img src="{Picture_URL}" alt="{Brand} {Model}">
      <h2>{Brand} {Model}</h2>
      <p><strong>Price:</strong> {Price_in_India}</p>
      <p><strong>Total Ratings:</strong> {Total_Ratings}</p>
      <p><strong>Battery_capacity(mAh):</strong> {Battery_capacity(mAh)} </p>
      <p><strong>RAM:</strong> {RAM}</p>
      <p><strong>Internal_storage:</strong> {Internal_storage}</p>
      <p><strong>Processor:</strong> {Processor}</p>
      <p><strong>Operating_system:</strong> {Operating_system} kg</p>
      <p><strong>Screen_size(inches):</strong> {Screen_size(inches)} Hz</p>
    </div>
    """
    mobiles_html = ""
    for mobile in mobiledata_filtered:
        mobiles_html += mobile_template.format(**mobile)

    # Define an HTML template for the report
    report_template = """
    <!DOCTYPE html>
    <html>
    <head>
      <center><title>Mobile Data Report</title></center>
      <style>
        .mobile-container {{
          overflow: auto;
        }}
        .mobile {{
          border: 1px solid black;
          padding: 20px;
          margin: 20px;
          float: left;
          width: 300px;
          height: 550px;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <h1>Mobile Data Report</h1>
      <form action="/mobile-report" method="get">
        <label for="brand">Search by brand:</label>
        <input type="text" id="brand" name="brand">
        <button type="submit">Search</button>
      </form>
      <p><strong>Total Price: {total_price}</strong>  </p>
      <p><strong>Average Price: {avg_price:.2f}</strong>  </p>
      <div class="mobile-container">
        {mobile_html}
      </div>
    </body>
    </html>
    """

    # Generate HTML for the report
    html = report_template.format(total_price=total_price, avg_price=avg_price, mobile_html=mobiles_html)

    # Return the HTML as a response
    return html


app = FastAPI()

class Wearable(BaseModel):
    price: float = 0.0
    battery_life: float = 0.0
    brand: str = "Unknown"

# Objective 1: Plot the distribution of prices
@app.get("/prices")
def get_prices() -> List[float]:
    prices = [wearable.price for wearable in data]
    return prices

# Objective 2: Plot the distribution of battery life
@app.get("/battery-life")
def get_battery_life() -> List[float]:
    battery_life = [wearable.battery_life for wearable in data]
    return battery_life

# Objective 3: Plot the number of wearables by brand
@app.get("/brands")
def get_brands() -> dict:
    brands = {}
    for wearable in data:
        brand = wearable.brand
        brands[brand] = brands.get(brand, 0) + 1
    return brands
@app.get("/scrape")
def scrape_data() -> List[Dict]:
    url = "https://www.gadgets360.com/wearables/smartwatch-finder"
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    request = requests.get(url, headers=headers)

    soup = BeautifulSoup(request.content, 'html.parser')
    productlist = soup.find_all('div', class_='_lpdwgt _flx pdbtlinks')

    product_links = []
    product_name = []
    smartwatch_lists = []

    for item in productlist:
        for link in item.find_all('a', href=True):
            product_links.append(url + link['href'])
        for name in item.find_all('a', title=True):
            product_name.append(name['title'])

    for link in product_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        name = soup.find('h1').text.strip()
        price_elements = soup.find_all('a', class_='_trtprc')
        price = int(price_elements[0].text.replace('₹', '').replace(',', '').strip())

        div_element = soup.find('div', {'class': '_pdsd'})
        spec_titles = div_element.find_all('span', {'class': '_ttl'})
        spec_values = div_element.find_all('span', {'class': '_vltxt'})
        specifications = {}

        for title, value in zip(spec_titles, spec_values):
            specifications[title.text.strip()] = value.text.strip()

        smartwatch = {
            'Model': name,
            'Price in India': price,
            'Water Resistant': specifications.get('Water Resistant', 'N/A'),
            'Battery Life': specifications.get('Battery Life', 'N/A'),
            'Compatible Operating System': specifications.get('Compatible Operating System', 'N/A'),
            'Bluetooth': specifications.get('Bluetooth', 'N/A'),
            'Wi-Fi': specifications.get('Wi-Fi', 'N/A'),
            'Ram': specifications.get('Ram', 'N/A')
        }
        smartwatch_lists.append(smartwatch)

    return smartwatch_lists