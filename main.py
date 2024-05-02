import json

def lambda_handler(event, context):
    # TODO implement
    prompt ="prompt"

    kwargs = {
                "modelId": "anthropic.claude-3-sonnet-20240229-v1:0",
                "contentType": "application/json",
                "accept": "application/json",
                "body": {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 1000,
                    "messages": [
                    {
                        "role": "user",
                        "content": [
                        {
                            "type": "image",
                            "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": "iVBORw..."
                            }
                        },
                        {
                            "type": "text",
                            "text": f"{prompt}?"
                        }
                        ]
                    }
                    ]
                }
                }
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
