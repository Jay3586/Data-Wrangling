#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json
# Load the citylots.json data
with open('citylots.json') as f:
    data = json.load(f)


# In[7]:


pip install folium


# In[8]:


import folium


# In[10]:


# Create a Folium map centered on the city of San Francisco
m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Loop through the features in the data and add them as GeoJSON layers to the map
for feature in data['features']:
    folium.GeoJson(feature).add_to(m)


# In[12]:


# Create a folium map centered on San Francisco
m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

# Add the GeoJSON data as a layer on the map
folium.GeoJson(data).add_to(m)

# Create a second folium map centered on Oakland
m2 = folium.Map(location=[37.8044, -122.2711], zoom_start=12)

# Add a marker to the map indicating the location of the Oakland Airport
folium.Marker(location=[37.7212, -122.2206], popup='Oakland Airport').add_to(m2)

# Save the maps as HTML files in the current working directory
m.save('sf_map.html')
m2.save('oak_map.html')


# In[13]:


# Create a folium map centered on Union City
m = folium.Map(location=[37.5934, -122.0438], zoom_start=14)

# Add a marker to the map indicating the location of Union City
folium.Marker(location=[37.5934, -122.0438], popup='Union City').add_to(m)

# Save the map as an HTML file in the current working directory
m.save('union_city_map.html')


# In[ ]:




