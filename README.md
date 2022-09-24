# covid19-dashboard

## Dashboard

Dashboard link: https://sn-datawizard.github.io/

Dashboard refreshed at 6am (GMT+2) on daily schedule.

## API

API used: https://github.com/marlon360/rki-covid-api

API provides daily refreshed data.

## Python script Deployment (Docker, GCP Container Registry, GCP Compute Engine)

App-1 fetches data from API and uploads response to Google Cloud Storage.

App-2 imports data which is stored in Cloud Storage to Google Cloud MySQL.

![image](https://user-images.githubusercontent.com/77932366/192109211-c5112c9e-1b4c-4bfb-9bc2-7acc81a3d19b.png)