#Import libraries
import json
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from wordcloud import WordCloud
from io import BytesIO
import base64
import plotly.graph_objects as go

#Load movies.json as Python dictionary
with open("Tvdata.json") as f:
  tv_data = json.load(f)



# Print the brand of each TV
for obj in tv_data:
    print(obj['Brand'])

# Define a list of features to report on
features_to_report = [
    "Brand",
    "Model",
    "price_in_india",
    "display_size",
    "resolution_standard",
    "no_of_usb_port",
    "no_of_hdmi_port",
    "smart_tv",
    "built_in_wifi",
    "refresh_rate_hz",
    "launch_year"
]

# Calculate the average price of all TVs
total_price = sum(int(str(tv["price_in_india"]).strip()) for tv in tv_data)
average_price = total_price / len(tv_data)
# Generate the report
print("TV Data Report\n")
print(f"Total number of TVs: {len(tv_data)}")
print(f"Average price of TVs: Rs. {average_price:.2f}\n")

for feature in features_to_report:
    feature_values = set(tv[feature] for tv in tv_data)
    feature_values_str = ", ".join(str(value) for value in feature_values)
    print(f"{feature}: {feature_values_str}\n")

total_price = sum(int(str(tv["price_in_india"]).strip()) for tv in tv_data)
avg_price = total_price / len(tv_data)


# Define an HTML template for displaying a single TV
tv_template = """
<div class="tv">
  <img src="{PictureURL}" alt="{Brand} {Model}">
  <h2>{Brand} {Model}</h2>
  <p><strong>Price:</strong> {PriceinIndia}</p>
  <p><strong>Display Size:</strong> {DisplaySize(inch)}</p>
  <p><strong>Resolution:</strong> {ResolutionStandard} {Resolution(pixels)}</p>
  <p><strong>USB Ports:</strong> {NoofUSBPort}</p>
  <p><strong>HDMI Ports:</strong> {NoofHDMIPort}</p>
  <p><strong>Smart TV:</strong> {SmartTV}</p>
  <p><strong>Weight:</strong> {Weight(without stand)} kg</p>
  <p><strong>Refresh Rate:</strong> {RefreshRate(Hz)} Hz</p>
</div>
"""

# Define an HTML template for displaying a single TV
tv_template = """
<div class="tv">
  <img src="{PictureURL}" alt="{Brand} {Model}">
  <h2>{Brand} {ProductName} {Model}</h2>
  <p><strong>Price:</strong> {price_in_india}</p>
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
for tv in tv_data:
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

# Generate HTML for the report
html = report_template.format(total_price=total_price, avg_price=avg_price, tv_html=tv_html)

# Write the HTML to a file
with open("tv_report5.html", "w") as f:
     f.write(html)

brands = [item['Brand'] for item in tv_data]
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(' '.join(brands))
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

for obj in tv_data:
    print(obj['Brand'])

print(type(obj))
print(obj.keys())

types_tv = [item['Brand'] for item in tv_data]



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
plt.show()


brand_prices = {}
for item in tv_data:
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

sorted_brands = sorted(brand_avg_prices.items(), key=lambda x: x[1], reverse=True)
sorted_brands_names = [x[0] for x in sorted_brands]
sorted_brands_prices = [x[1] for x in sorted_brands]

fig, ax = plt.subplots(figsize=(20, 6))
ax.bar(sorted_brands_names, sorted_brands_prices)
ax.set_xlabel('Brand')
ax.set_ylabel('Average Price')
ax.set_title('Brand vs Average Price')
plt.xticks(rotation=90)
plt.show()

col1 = [row['1_stars'] for row in tv_data]
col2 = [row['2_stars'] for row in tv_data]
col3 = [row['3_stars'] for row in tv_data]
col4 = [row['4_stars'] for row in tv_data]
col5 = [row['5_stars'] for row in tv_data]

# Create a 2D array with the column data
data_array = np.array([col1, col2, col3, col4, col5])

# Calculate the correlation matrix
corr_matrix = np.corrcoef(data_array)

# Create a heatmap using Matplotlib
fig, ax = plt.subplots()
im = ax.imshow(corr_matrix, cmap='Spectral')

# Add a color bar
cbar = ax.figure.colorbar(im, ax=ax)

# Set the x- and y-axis tick labels and the plot title
ax.set_xticks(np.arange(len(data_array)))
ax.set_yticks(np.arange(len(data_array)))
ax.set_xticklabels(['1_stars', '2_stars', '3_stars', '4_stars', '5_stars'])
ax.set_yticklabels(['1_stars', '2_stars', '3_stars', '4_stars', '5_stars'])
plt.title('Correlation Plot of 5 Stars Columns')

# Rotate the x-axis tick labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Loop over data dimensions and add annotations
for i in range(len(data_array)):
    for j in range(len(data_array)):
        text = ax.text(j, i, round(corr_matrix[i, j], 2), ha='center', va='center', color='w')

# Display the plot
plt.show()

# Sort the TVs by their average rating in descending order
sorted_tvs = sorted(tv_data, key=lambda x: ((x['5_stars'] + x['4_stars'])/(x['1_stars'] + x['2_stars'] + x['3_stars'] + x['4_stars'] + x['5_stars'])) if (x['1_stars'] + x['2_stars'] + x['3_stars'] + x['4_stars'] + x['5_stars']) != 0 else 0, reverse=True)

# Print the top ten TVs with score and number of reviews
for i, tv in enumerate(sorted_tvs[:10]):
    total_reviews = tv['1_stars'] + tv['2_stars'] + tv['3_stars'] + tv['4_stars'] + tv['5_stars']
    avg_rating = (tv['5_stars'] + tv['4_stars']) / total_reviews
    print(f"{i+1}. {tv['Brand']} {tv['ProductName']} {tv['model_name']} ({avg_rating:.2f} out of 5, based on {total_reviews} reviews)")

# Create lists of feature values
usb_ports = [int(d['no_of_usb_port']) for d in tv_data]
speakers = [int(''.join(filter(str.isdigit, str(d['number_of_speakers'])))) for d in tv_data]
hdmi_ports = [int(d['no_of_hdmi_port']) for d in tv_data]

# Create bar plot
plt.figure(figsize=(8, 6))
plt.bar(['USB Ports', 'Speakers', 'HDMI Ports'], [sum(usb_ports)/len(usb_ports), sum(speakers)/len(speakers), sum(hdmi_ports)/len(hdmi_ports)])
plt.title('Average Number of USB Ports, Speakers, and HDMI Ports in TVs')
plt.ylabel('Average Number')
plt.xlabel('TV Features')
plt.text(0, sum(usb_ports)/len(usb_ports), f"{sum(usb_ports)/len(usb_ports):.2f}", ha='center', fontsize=12)
plt.text(1, sum(speakers)/len(speakers), f"{sum(speakers)/len(speakers):.2f}", ha='center', fontsize=12)
plt.text(2, sum(hdmi_ports)/len(hdmi_ports), f"{sum(hdmi_ports)/len(hdmi_ports):.2f}", ha='center', fontsize=12)

plt.show()

# Extract the number of USB ports for each TV
usb_ports = [tv['no_of_usb_port'] for tv in tv_data]

# Create a histogram of the number of USB ports
plt.hist(usb_ports, bins=range(min(usb_ports), max(usb_ports) + 2, 1), rwidth=0.8)
plt.xlabel('Number of USB ports')
plt.ylabel('Frequency')
plt.title('Distribution of USB Ports in TV Data')
plt.show()

# Extract the number of HDMI ports for each TV and convert to integers
hdmi_ports = [int(tv['no_of_hdmi_port']) for tv in tv_data]

# Create a histogram of the number of HDMI ports
plt.hist(hdmi_ports, bins=range(min(hdmi_ports), max(hdmi_ports) + 2, 1), rwidth=0.8)
plt.xlabel('Number of HDMI ports')
plt.ylabel('Frequency')
plt.title('Distribution of HDMI Ports in TV Data')
plt.show()

# Define the attributes to plot
attributes = [ 'no_of_usb_port', 'number_of_speakers','no_of_hdmi_port']

# Create a string with HTML code for the plots
html_output = ''

for attr in attributes:
    # Get the data for the attribute
    data = [tv[attr] for tv in tv_data]

    # Create a histogram of the data
    fig, ax = plt.subplots()
    ax.hist(data, bins=10)

    # Add the size and x-axis label in vertical orientation
    ax.tick_params(axis='both', labelrotation=90)
    ax.set_xlabel(attr)
    ax.set_ylabel('Frequency')

    # Save the plot as a PNG image
    img_data = BytesIO()
    fig.savefig(img_data, format='png')
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.getvalue()).decode()

    # Add the plot to the HTML output
    html_output += f'<h2>{attr}</h2>'
    html_output += f'<img src="data:image/png;base64,{img_base64}"/>'

# Create a string with HTML code for the whole page
html_page = f'<html><head><title>TV Data</title></head><body>{html_output}</body></html>'

# Save the HTML page to a file
with open('tv_dataplot.html', 'w') as f:
    f.write(html_page)

