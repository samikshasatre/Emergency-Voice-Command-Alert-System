import geocoder

def get_location():
    g = geocoder.ip('me')
    if g.ok:
        print(f"📍 Location: {g.latlng}")
        return g.latlng
    return [0.0, 0.0]
