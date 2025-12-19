# File: config.py
# This file holds project-wide configuration

class Config:
    BASE_URL = "https://www.saucedemo.com"
    # Credentials for the demo site
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    # Browser configuration (chrome, firefox, edge)
    BROWSER = "chrome"
    IMPLICIT_WAIT = 10  # Seconds to wait for elements