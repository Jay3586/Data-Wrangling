import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import urlparse

# send request to the website
url = "https://www.gadgets360.com/tv/tv-finder"

response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

#with open("tabel2.html", "w", encoding = "utf-8") as f:
    #f.write(response.text)


print("\n\n==================Headers below =====================")
my_headers = soup.find_all("h2")
for headers in my_headers:
    print(f"\n{headers}")

print("\n\n================== link below =====================")
# Find all the links on the page with an "href" attribute
my_links = soup.find_all("a", href=True)

# Print out the URLs of the links
for link in my_links:
    print(link['href'])


print("\n\n================== image below  =====================")
# Find all the images on the page
my_images = soup.find_all("img")

# Print out the URLs of the images
for image in my_images:
    src = image.get("src")
    if src:
        print(src)
    else:
        print("Image has no source attribute:", image)


print("---------------- Paragraph Below ------------------")
my_paragraph = soup.find_all("p")
for paragraph in my_paragraph:
    print(f"\n{paragraph}")

print("\n\n==================Item below =====================")
item = soup.find_all("div", {"class": "_flx _lpbwg"})
for item in item:
    print(f"\n{item}")

# ---------------------

# Find the TVs on the page
tv_list = soup.find_all("div", class_="_lpdscn")

# Print the total number of TVs on the page
print(f"Total number of TVs on the page: {len(tv_list)}")

name = (soup.find('h3').text.strip())
Display = (soup.find("td",class_="_vltxt").text.strip())




print("\n\n-------------Mobile Feature----------\n\n")
TVs= {
    'name':name,
    'Display':Display,

    # add more key-value pairs as needed
}
print(TVs)


print("\n\n-------------Mobile Feature----------\n\n")
tv_lists =[]
testlink1 ="https://www.gadgets360.com/oneplus-tv-43-y1s-pro-price-in-india-107390"

r = requests.get(testlink1)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Dimensions"
Dimension_span = div_element3.find_next('span', {'class': '_ttl'}, string='Dimensions')
# Get the next sibling span element with class "_vltxt" and extract its text
Dimension_size = Dimension_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()


div_element5 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Resolution Standard"
Resoultion_standard_span = div_element5.find_next('span', {'class': '_ttl'}, string='Resolution Standard')
# Get the next sibling span element with class "_vltxt" and extract its text
Resoultion_standard_Capacity = Resoultion_standard_span .find_next_sibling('span', {'class': '_vltxt'}).text.strip()


div_element4 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "OS"
OS_span = div_element4.find_next('span', {'class': '_ttl'}, string='OS')
# Get the next sibling span element with class "_vltxt" and extract its text
OS = OS_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()


tvs= {
    'name':name,
    'price':price,
    'display':display_size,

    'Resolution Standard':Resoultion_standard_Capacity,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)

testlink2 ="https://www.gadgets360.com/lg-24-inch-led-full-hd-tv-24mn48-9065"

r = requests.get(testlink2)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Dimensions"
Dimension_span = div_element3.find_next('span', {'class': '_ttl'}, string='Dimensions')
# Get the next sibling span element with class "_vltxt" and extract its text
Dimension_size = Dimension_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()


div_element5 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Resolution Standard"
Resoultion_standard_span = div_element5.find_next('span', {'class': '_ttl'}, string='Resolution Standard')
# Get the next sibling span element with class "_vltxt" and extract its text
Resoultion_standard_Capacity = Resoultion_standard_span .find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Dimensions':Dimension_size,
    'Resolution Standard':Resoultion_standard_Capacity,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)

testlink3 ="https://www.gadgets360.com/samsung-65-inch-qled-ultra-hd-4k-tv-q70rak-qa65q70rakxxl-price-in-india-91837"

r = requests.get(testlink3)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Screen Type'"
Screen_Type_span = div_element3.find_next('span', {'class': '_ttl'}, string='Screen Type')
# Get the next sibling span element with class "_vltxt" and extract its text
Screen_Type_size = Screen_Type_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()


div_element5 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Resolution Standard"
Resoultion_standard_span = div_element5.find_next('span', {'class': '_ttl'}, string='Resolution Standard')
# Get the next sibling span element with class "_vltxt" and extract its text
Resoultion_standard_Capacity = Resoultion_standard_span .find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Screen Type':Screen_Type_size,
    'Resolution Standard':Resoultion_standard_Capacity,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)


testlink4 ="https://www.gadgets360.com/vu-gloled-55-inch-ultra-hd-led-android-smart-tv-55gloled-price-in-india-113017"

r = requests.get(testlink4)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Screen Type'"
Screen_Type_span = div_element3.find_next('span', {'class': '_ttl'}, string='Screen Type')
# Get the next sibling span element with class "_vltxt" and extract its text
Screen_Type_size = Screen_Type_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()


div_element5 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Resolution Standard"
Resoultion_standard_span = div_element5.find_next('span', {'class': '_ttl'}, string='Resolution Standard')
# Get the next sibling span element with class "_vltxt" and extract its text
Resoultion_standard_Capacity = Resoultion_standard_span .find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Screen Type':Screen_Type_size,
    'Resolution Standard':Resoultion_standard_Capacity,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)

testlink5 ="https://www.gadgets360.com/thomson-32-inch-led-hd-ready-tv-r9-32tm3290-price-in-india-92063"

r = requests.get(testlink5)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Screen Type'"
Screen_Type_span = div_element3.find_next('span', {'class': '_ttl'}, string='Screen Type')
# Get the next sibling span element with class "_vltxt" and extract its text
Screen_Type_size = Screen_Type_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Screen Type':Screen_Type_size,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)

testlink6 ="https://www.gadgets360.com/lg-43-inch-led-ultra-hd-4k-tv-43um7300pta-price-in-india-91788"

r = requests.get(testlink6)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Screen Type'"
Screen_Type_span = div_element3.find_next('span', {'class': '_ttl'}, string='Screen Type')
# Get the next sibling span element with class "_vltxt" and extract its text
Screen_Type_size = Screen_Type_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Screen Type':Screen_Type_size,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)


testlink7 ="https://www.gadgets360.com/sony-bravia-x75k-55-inch-smart-android-led-tv-kd-55x75k-price-in-india-108272"

r = requests.get(testlink7)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Screen Type'"
Screen_Type_span = div_element3.find_next('span', {'class': '_ttl'}, string='Screen Type')
# Get the next sibling span element with class "_vltxt" and extract its text
Screen_Type_size = Screen_Type_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Screen Type':Screen_Type_size,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)

testlink8 ="https://www.gadgets360.com/xiaomi-smart-tv-5a-32-inch-price-in-india-108072"

r = requests.get(testlink8)
soup =BeautifulSoup(r.content,'html.parser')
name = (soup.find('h1').text.strip())
price = soup.find('a', class_='_trtprc').text.strip().split('.')[0].replace(',', '').replace('₹','')




# Find the div element with class "_pdsd"
div_element = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Display"
display_span = div_element.find('span', {'class': '_ttl'}, string='Display')
# Get the next sibling span element with class "_vltxt" and extract its text
display_size = float(display_span.find_next_sibling('span', {'class': '_vltxt'}).text.replace('inch','').replace('-','').strip())


div_element2 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Smart TV"
Smart_TV_span = div_element2.find_next('span', {'class': '_ttl'}, string='Smart TV')
# Get the next sibling span element with class "_vltxt" and extract its text
Smart_TV_size = Smart_TV_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()

div_element3 = soup.find('div', {'class': '_pdsd'})
# Find the span element with class "_ttl" that contains the text "Screen Type'"
Screen_Type_span = div_element3.find_next('span', {'class': '_ttl'}, string='Screen Type')
# Get the next sibling span element with class "_vltxt" and extract its text
Screen_Type_size = Screen_Type_span.find_next_sibling('span', {'class': '_vltxt'}).text.strip()




tvs= {
    'name':name,
    'price':price,
    'display':display_size,
    'Screen Type':Screen_Type_size,

    'Smart TV':Smart_TV_size,
}
print(tvs)
tv_lists.append(tvs)

df =pd.DataFrame(tv_lists)
print(df)


# Find all div elements with class '_lpdwgt _flx pdbtlinks'
# Create a dictionary to count the number of TV brands
# Create the scatter plot  of the price versus RAM columns

# Create a bar chart for the 'name' and 'price' columns
plt.bar(df['name'], df['price'])

# Set the labels for the x-axis and y-axis
plt.xlabel('TV Name')
plt.ylabel('Price ($)')

# Set the title for the chart
plt.title('TV Prices')

# Rotate the x-axis labels by 90 degrees
plt.xticks(rotation=90)
# Show the chart
plt.show()


# Create a scatter plot using matplotlib
plt.scatter(df['price'], df['display'])

# Set the title and axis labels for the plot
plt.title('TV Price vs Display Size')
plt.xlabel('Price ($)')
plt.ylabel('Display Size (inches)')

# Show the plot
plt.show()

# Create a pie chart for the 'Screen Type' column
screen_type_counts = df['Screen Type'].value_counts()
plt.pie(screen_type_counts, labels=screen_type_counts.index, autopct='%1.1f%%')

# Set the title for the chart
plt.title('TV Screen Type Distribution')

# Show the chart
plt.show()


# Create a line chart for the 'display' and 'price' columns
plt.plot(df['display'], df['price'], 'bo-')

# Set the labels for the x-axis and y-axis
plt.xlabel('Display Size')
plt.ylabel('Price ($)')

# Set the title for the chart
plt.title('TV Display Size vs. Price')

# Show the chart
plt.show()


def plot1():
    brand_count = {}
    names = df['name']
    for nam in names:
        if nam in brand_count:
            brand_count[nam] += 1
        else:
            brand_count[nam] = 1

    # Plot the bar graph
    plt.bar(range(len(brand_count)), list(brand_count.values()), align='center')
    plt.xticks(range(len(brand_count)), list(brand_count.keys()), rotation=90)
    plt.xlabel('TV Brands')
    plt.ylabel('Count')
    plt.title('TV Brands and their Count')
    plt.show()


plot1()
