#|Maddison Montijo | Assignment 7.2 | Class 325


def get_country_info(country,city, *args, **kwargs):
    """Return a dictionary of information about a city and country."""
    population = kwargs.get("population")
    language = kwargs.get("language")
    
#|Fun Note : I've never used kwargs before, or args
#|References:
#|https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments
#|Fun Note Step G : When I made my function modifiable
#|It made it so it wouldn't fail when adding another parameter
    if population:
        country_info = f"{country} {city} {population}"
        return country_info
    elif language:
        country_info = f"{country} {city} {language}"
        return country_info
    else:
        country_info = f"{country} {city}"
        return country_info
#|Fun Note : I forgot to add return, so it wasn't returning anything

get_country_info("Chile","Santiago")
get_country_info("Chile","Santiago","5000000")
get_country_info("Chile","Santiago","5000000", "Spanish")


