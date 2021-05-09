# CAW_Studios_Assignment-
AWS Project using Lambda, elastic search , API Gateway, Dynamodb servies. 


**Challenge**
● Sign up for AWS free tier.
● Create a table in DynamoDB called “Student” with a single column "Name".
● Create an AWS Elasticsearch Instance (t2.small.elasticsearch)
● Create a DynamoDB stream that automatically inserts a record in the ES index when data is
inserted in the Student table
● Store a bunch of names of your friends in the Student table and check if the ES instance is
populated using the streams
● Create two APIs using AWS Lambda + API Gateway
● /students: Takes the name of the student and inserts it in the Student table. The name should get
inserted in the ES instance automatically using the streams.
● /students?query=: Should search the ES index with the query and return the results.

**Deliverables**
1. Decide appropriate verbs for the two APIs.
2. Commit the Lambdas in Github private repository and share with Github username -
caw-studios-career
3. Add careers@cawstudios.com to the AWS account and give it access to the DynamoDB and ES
instances.
