# job_searcher
Web scraper that aggregates IT job offers in one place.
Project is composed of four parts and lives in four separate docker containers.
1. Crawler, that scrapes all major polish websites witch post job offers and saves that info into database
2. MongoDB database
3. REST API that makes querying database possible
4. Frontend that consumes job offers API and makes visualising them easy


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
can find REST API for IT related job offers.

## Things to do:
- [x] ~~Create first iteration of REST API~~ [27.01.2020]
- [x] ~~Add NoFluffJobs support~~ [01.02.2020]
- [] Add BulldogJob support
- [x] ~~Migrate to MongoDB~~ [30.01.2020]
- [] Find a way to crawl multiple pages in parallel
- [x] Create front that consumes api [16.02.2020]
- [x] ~~Create Dockerfile for each program part~~ [13.02.2020]
- [x] ~~Create docker-compose.yaml~~ [13.02.2020]

