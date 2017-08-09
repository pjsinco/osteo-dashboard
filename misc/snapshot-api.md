### Rough first thoughts on a Snapshot REST API

<br />
#####Certifications endpoint
```GET  /api/v1/snapshot/certifications/{aoa_id}```
###### Example response
```
{
  "data": {
    "certifications": [
      {
        "description": "Pediatrics",
        "code": "P",
        "status": "A",
        "expires": "12/31/2018",
        "parent": null,
        [...]
      },
      {
        "description": "Pediatric Neurology",
        "code": "PDN",
        "status": "A",
        "expires": "12/31/2021",
        "parent": "P",
        [...]
      },
    ],
  },
  "errors": []
}
```

<div style="page-break-after: always"></div>
<br />
<br />
#####CME credits endpoint
```GET  /api/v1/snapshot/cme_credits/{aoa_id}```
###### Example response
```
{
  "data": {
    "total_earned": 78.5,
    "total_recommended": 120,
    "cat_1a_earned": null,
    "cat_1a_recommmended": null,
    "certifications": [
      {
        "description": "Pediatrics",
        "code": "P",
        "specialty_earned": 24,
        "specialty_recommended": 50,
        [...],
        "subspecialties": [
          {
            "description": "Pediatric Neurology",
            "code": "PDN"
            "specialty_earned": 15,
            "specialty_recommended": 13,
            [...]
          }
        ] 
      }      
    ],
    [...]
  },
  "errors": []
}
```

<br>
<br>
<div style="page-break-after: always"></div>
#####Membership endpoint
```GET  /api/v1/snapshot/accounts/{aoa_id}```
###### Example response
```
{
  "data": {
    "type": "DO-M",
    "status": "A",
    "paid_thru": "5/31/2018",
    [...]
  },
  "errors": []
}
```

<br>
<br>
#####Whole enchilada endpoint
```GET  /api/v1/snapshot/{aoa_id}```
