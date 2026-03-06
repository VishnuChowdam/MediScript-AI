
import urllib

def get_location(location):
    # Taking the location and getting map link
    if location and isinstance(location, dict) and location.get('latitude') and location.get('longitude'):
        latitude=location.get('latitude')
        longitude=location.get('longitude')
        search_query='nearby pharmacies'
        encoded_query=urllib.parse.quote(search_query)
        map_link = f"https://www.google.com/maps/search/{encoded_query}/@{latitude},{longitude},15z"
        return map_link
    return 'Location not provided or permission denied'

