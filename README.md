# FindMyStuff

## Description
FindMyStuff is an Alexa Skill that allows users to have a personal item inventory of their home. There is currently functionality for adding new items to your inventory, finding where you put items, and updating the current count of your item inventory. 

### Prerequisites
This Alexa Skill is a private skill run completely on AWS. Due to the nature of the application, we can run this for little to no cost using the AWS free tier. Lambda allows us to run 1 million times a month for free, and DynamoDB allows for 20GB of free storage on their service. 

- You must create an AWS account, a new Lambda function, and a new DynamoDB table.
    - Your DynamoDB table must have a partition key (__userId__) and a sort key (__item_name__)
- You must create an Alexa Skills Developer account as well. Then create a new Alexa Skill.
- This code references 2 env variables, __DYNAMODB_TABLE__ and __APPICATION_ID__, both of which must be added to your Lambda function's env variables section. 
    - __DYNAMODB_TABLE__ is the name you gave your table
    - __APPLICATION_ID__ can be found on your Alexa Skill's endpoints page
    - You must also link your Alexa Skill to your Lambda function in this endpoints page and on your Lambda function's triggers page.
- The boto3 client is used to interact with our DynamoDB table

### Initiating the skill
I went with "Alexa item finder", but you can choose your own invocation phrase. This is captured in __lambda_function.py__ and then handled in __event_types.py__, when we check for a launch request. 

### Adding new items
This is handled by the PutItem intent. This intent takes 3 slots, __item__, __location__, and __quantity__. These slot values are then passed to the Lambda function and handled by __put_item.py__, which performs a PUT request to our DynamoDB table.

### Getting items
This is handled by the GetItem intent. This intent takes 1 slot, __item__. The value of __item__ is then passed to __get_item.py__ to search our DynamoDB table. 

### Updating items
This is handled by the RemoveItem intent. This intent takes 2 slots, __item__ and __quantity__. These slot values are passed to __remove_item.py__ which does two things. The first, is we search to see if we currently have the item in the inventory. We have two cases to account for:
- If we don't have the item, we tell the user we don't have that item so we cannot update it.
- If we do have the item, we perform a PUT request to update the quantity in our DynamoDB table.

### Exiting the skill
This is handled in __event_types.py__ which also controls the Launch event. We want to gracefully exit by saying goodbye before turning off the skill.