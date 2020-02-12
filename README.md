# job_searcher
Web scraper that aggregates IT job offers in one place.
Project is composed of three parts:
1. Crawler, that scrapes all major polish websites witch post job offers and saves that info into database
2. REST API that makes querying database possible
3. Simple frontend that consumes job offers API and makes visualising them easy


## Installation
Installation is simple, but requires Docker installed. First, clone the repository:
```
git clone https://github.com/psobczak/job_searcher.git
cd job_searcher
```
Then just type:
```
docker-compose up
```
Wait for a few seconds for build to finish, and... that's it. Now go to ```http://localhost:5000/offers``` where you 
cant find IT related job offers REST api.

## Things to do:
- [x] ~~Create first iteration of REST API~~ [27.01.2020]
- [x] ~~Add NoFluffJobs support~~ [01.02.2020]
- [] Add BulldogJob support
- [x] ~~Migrate to MongoDB~~ [30.01.2020]
- [] Find a way to crawl multiple pages in parallel
- [] Create front that consumes api
- [x] ~~Create Dockerfile for each program part~~ [13.02.2020]
- [x] ~~Create docker-compose.yaml~~ [13.02.2020]

