## APIs Details
Base URL for all API endpoints : `http://127.0.0.1:8000/` <br />

**Linkedin Scraper API:**

Following API endpoints available in linkedin_scraper app.
 
**1) refresh-linkedin-employees**<br />
 This API will scrap the data of linkedin profiles and upsert to the database. This API will be accessed by 
 administrator/super users only. <br />
 To hit this API, first login to admin area: 
 `http://127.0.0.1:8000/admin/`

- Methods: GET, HEAD, OPTIONS
- Endpoint: `linkedin_scraper/api/v1/refresh/`
- Response: <br />
  code: `200 OK` <br />
  data: None

**2) employee-list**<br />
This API will return list of all scraped linkedin employee profiles from database.
- Methods: GET, HEAD, OPTIONS
- Endpoint: `linkedin_scraper/api/v1/`
- Response: <br />
  code: `200 OK` <br />
  data: 
  ```
  [{
      "company": "Mambu",
      "name": "gargi",
      "email": "gargi@mambu.com",
      "designation": "IT admin",
      "employed_date": "2017-11-26"
    },
    .
    .
    ] 

**3) employee-detail**<br />
This API will return employee detail when employee id is passed to endpoint.
- Methods: GET, HEAD, OPTIONS 
- Endpoint: `linkedin_scraper/api/v1/<int:pk>/` <br />
  Required: int: id
- Success Response: <br/>
  code: `200 OK` <br />
  data: 
  ```{
      "company": "Mambu",
      "name": "gargi",
      "email": "gargi@mambu.com",
      "designation": "IT admin",
      "employed_date": "2017-11-26"
    }
-  Failure Response: <br />
   code: `404 not found` <br />
   data: None
  

**Tracxn Scraper API:**

Following API endpoints available in tracxn_scraper app.
 
**1) company-list**<br />
This API will return list of all scraped tracxn companies from database.
- Methods: GET, HEAD, OPTIONS
- Endpoint: `tracxn_scraper/api/v1/`
- Response: It will return employees list with status code- `200 OK` 

**2) company-detail**<br />
This API will return company detail when company id is passed.
- Methods: GET, HEAD, OPTIONS 
- Endpoint: `tracxn_scraper/api/v1/<int:pk>/` <br />
  Required: id
- Success Response: <br />
  code: `200 OK` <br />
  data: 
  ```{
        "id": 1, 
        "name": "Mambu",
        "short_description": "company1",
        "description": "company1", 
        "founded_year": 2020,
        "location": "mumbai",
        "total_funding": "112.00", 
        "stage": "unfunded",
        "investor": [
            { 
                "id": 1,
                "name": "default investor",
                "is_angel": false 
            }, 
            { 
                "id": 3,
                "name": "default investor3", 
                "is_angel": false 
            } 
        ], 
        "category": [ 
            { 
                "id": 2,
                "name": "CRM"
            } 
        ] 
  } 
-  Failure Response: <br />
   code: `404 not found` <br />
   data: None