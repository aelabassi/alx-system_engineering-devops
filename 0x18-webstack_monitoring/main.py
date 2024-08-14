from datadog import initialize, api
import os

options = {
    'api_key': os.getenv('DD_API_KEY'),
    'app_key': os.getenv('DD_APP_KEY')
}

initialize(**options)

print(api.Hosts.totals())
