Use
=====
Calculates the number of bulk download requests needed in order
to download all of regulations.gov data.
Does this by iterating throught every year and summing
the number of agencies that have a docket in that year.

Number of Requests
=====
Sends a small amount of requests. For the year 2023 it will
send 18 requests (2006 to 2023).

Setup
=====
regulations.gov API key needs to be put in the 'key'
parameter in a .env file.
