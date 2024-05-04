This project is a chatbot implemented using AWS services, particularly API Gateway, AWS Lambda, Bedrock, Knowledge Base, and S3. It leverages the Bedrock Agent Runtime to facilitate natural language processing and generation.

# Chatbot description
The Chatbot project queries a knowledge base and utilizes this information to invoke a Large Language Model (LLM) to generate responses. It enables users to interact with the system through a frontend interface and receives responses generated based on the provided inputs and pre-existing knowledge base.


## Architecture
![Chatbot Architecture](media/architecture.svg)

## Chatbot-demo
<video src="media/chatbot_demo.mp4" controls></video>

# Chatbot-Setup

## AWS-setup
 1. Setup S3 bucket and add files.
 2. Set up knowledgebase and add the previously created S3 bucket.
 3. Set up a lambda function with a API Gateway as trigger
 4. Change the following parameters in the lambda function: `API_GATEWAY_URL`, `KNOWLEDGEBASE_ID` & `INSTRUCTIONS FOR THE CHATBOT`

### Lambda function
```python
import json
import boto3

# Initialize the Bedrock Agent Runtime client
boto3_session = boto3.session.Session()
region = boto3_session.region_name
client = boto3.client('bedrock-runtime', region_name=region)
client_ret = boto3.client('bedrock-agent-runtime', region_name=region)

def retrieve(query, kbId, numberOfResults=5):
    return client_ret.retrieve(
        retrievalQuery= {
            'text': query 
        },
        knowledgeBaseId=kbId,
        retrievalConfiguration= {
            'vectorSearchConfiguration': {
                'numberOfResults': numberOfResults
            }
        }
    )
    
def get_contexts(retrievalResults):
    contexts = ""
    for retrievedResult in retrievalResults: 
        contexts += retrievedResult['content']['text'] + "\n"
    return contexts

def lambda_handler(event, context):

    # declare model id for calling RetrieveAndGenerate API
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    model_arn = f'arn:aws:bedrock:{region}::foundation-model/{model_id}'

    # Check if the request body is present
    request_body = event.get('body')
    if request_body:
        input_data = json.loads(request_body)
        user_input = input_data.get('input')

        # Send the request to the Bedrock Agent Runtime AP
        try:
            response_text = retrieve(user_input, 'KNOWLEDGEBASE_ID')
            retrievalResults = response_text['retrievalResults']
            contexts = get_contexts(retrievalResults)
            
            prompt = f"""Objective: INSTRUCTIONS FOR THE CHATBOT
            
            
            <context>
            {contexts}
            </context>
            
            <question>
            {user_input}
            </question>
            
            The response should be specific and use statistics or numbers when possible.
            Assistant:"""

            messages=[{ "role":'user', "content":[{'type':'text','text': prompt.format(contexts, user_input)}]}]
                    
            kwargs = {
                    "modelId": "anthropic.claude-3-sonnet-20240229-v1:0",
                    "contentType": "application/json",
                    "accept": "application/json",
                    "body": json.dumps({
                        "anthropic_version": "bedrock-2023-05-31",
                        "max_tokens": 4096,
                        "messages": messages
                    })
                    }
            
            response = client.invoke_model(**kwargs)
            response_body = json.loads(response.get('body').read())
            response_text = response_body.get('content')[0]['text']
            
            return {
                'statusCode': 200,
                'body': json.dumps({'response': response_text})
            }

        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f"Internal Server Error: {str(e)}"})
            }
    else:
        # Return an error if no input data is provided
        return {
            'statusCode': 400,
            'body': json.dumps('No input data provided')
        }

```

# LocalHost-setup
1. Creat a url.py file which has the variablename ```API_GATEWAY_URL``` with the URL string for the API Gateway created previously.
2. Open the terminal and run `streamlit run chatbot.py`