import folium
import json
import os
import pandas as pd



THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

countries = os.path.join(THIS_FOLDER,'countries.geo.json')
claims = os.path.join(THIS_FOLDER, 'claims.csv')
claim = pd.read_csv(claims)

m = folium.Map(
    location = [30, 00],
    tiles = 'Mapbox Control Room', 
    zoom_start = 2.5)

##for i in range(len(claim.NAME)):
##    if claim.NAME[i][0] == 'A' or claim.NAME[i][0] == 'B' or claim.NAME[i][0] == 'C' :
##        claim.replace(claim.Value[i], 1)
##    elif claim.NAME[i][0] == 'D' or claim.NAME[i][0] == 'E' or claim.NAME[i][0] == 'F' :
##        claim.replace(claim.Value[i], 2)
##    elif claim.NAME[i][0] == 'G' or claim.NAME[i][0] == 'H' or claim.NAME[i][0] == 'I' :
##        claim.replace(claim.Value[i], 3)
##    elif claim.NAME[i][0] == 'J' or claim.NAME[i][0] == 'K' or claim.NAME[i][0] == 'L' :
##        claim.replace(claim.Value[i], 4)
##    elif claim.NAME[i][0] == 'M' or claim.NAME[i][0] == 'N' or claim.NAME[i][0] == 'O' :
##        claim.replace(claim.Value[i], 5)
##    elif claim.NAME[i][0] == 'P' or claim.NAME[i][0] == 'Q' or claim.NAME[i][0] == 'R' :
##        claim.replace(claim.Value[i], 6)
##    elif claim.NAME[i][0] == 'S' or claim.NAME[i][0] == 'T' or claim.NAME[i][0] == 'U' :
##        claim.replace(claim.Value[i], 7)
##    elif claim.NAME[i][0] == 'V' or claim.NAME[i][0] == 'W' or claim.NAME[i][0] == 'X' :
##        claim.replace(claim.Value[i], 8)
##    elif claim.NAME[i][0] == 'Y' or claim.NAME[i][0] == 'Z':
##        claim.replace(claim.Value[i], 9)

print (claim.Value[1])        
claim.replace(claim.Value[0], 9)
print (claim.Value[1])

folium.Choropleth(
    geo_data = countries,
    name = 'RISK',
    data = claim,
    columns = ['ID', 'Value'],
    key_on = 'feature.id',
    fill_color = 'Paired',
    fill_opacity = 1,
    line_opacity = 0.2,
    legend_name  = "CLAIMS"
    ).add_to(m)

##if claim['Value'] == 1:
##    folium.Choropleth.fill_color ='BuGn'
    
folium.LayerControl().add_to(m)
m.save('map.html')
