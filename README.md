## Project Vision:
Our original project vision recognized that in any large-scale industry, a product must go through various
manufacturing stages before it is launched to the market. The path a product takes to reach its destination
depends on factors like quality, requirements, and cost. To find the best way, we need a smart algorithm.
This helps reduce costs, improve efficiency, and maintain product quality. Our project aims to create such
an algorithm using SQL. Therefore, our objective for our final product included the following features:

1. Return 5 shortest paths for a given source and destination ordered by cost.
2. Exclude devices that are faulted or in use by another path currently running.
3. Ability to work with divergent and convergent devices to handle transporting from one source to
multiple locations and vice versa.
4. Ability to reasonably scale up to larger sites with more devices.

As we progressed towards the end of our project, our initial vision remained largely consistent, with only
a few minor adjustments to our requirements. These changes included considering the inclusion of loops
in our systems and addressing costs associated with both the path and devices. This was made possible
by our thorough examination of the project outline and the formulation of essential questions for the
client, which provided us with a clearer project vision.

For more detailed documentation please check /Documentation/FinalReport.pdf

## How to run?

To see a step by step guide please check 

Open SSMS

1. Run the query inside filename "createDatabase.sql"
2. Run queries inside the file "createTables.sql"


The database is now created named "factory"
Tables named "device" and "path" have also been created.
NOTE: MAKE SURE THAT YOU HAVE THE FACTORY DATABASE SELECTED WHEN RUNNING QUERRIES.

Now we need to create some stored procedures (functions)

To create these stored procedures run all queries listed accordingly:
1. insertDevice.sql
2. insertDeviceForced.sql
3. insertPath.sql
4. addDevices.sql

Now execute all the remaining stored procedures.

READY TO GO.
Simply run the "runSearch.sql" with relevant parameters to get the desired output.

You can find some simple test querries in the filename: testCaseQueries.sql
The commands for the provided dataset is in filename "givenDataSet.sql" so you can simply copy and paste and run the queries to insert the database inside the created "factory" database.
  
### Step by Step Video tutorial:
https://www.youtube.com/watch?v=W8MEEJmMUzo
