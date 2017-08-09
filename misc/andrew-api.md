### Quick, unfinished thoughts on a REST API<br />for updating iMIS records
<br>

```PUT /api/v1/andrew/accounts/{aoa_id}```
###### Example request - Edit last name
```
  [
    "last_name": "Clark-Seaborn"
  ]
```

<br>
<br>
```POST /api/v1/andrew/accounts/{aoa_id}```
###### Example request - Add business address
```
  [
    "email": "",
    "business_addr_1": "4830 Highway 260",
    "business_addr_2": "Suite 103",
    "city": "Globe",
    "state": "AZ",
    "business_phone": "9284258151",
  ]
```
