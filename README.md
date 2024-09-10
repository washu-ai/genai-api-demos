# Summary
Researchers, faculty, and staff can now call API endpoints on Open AI endpoints. These endpoints are secure and hosted in WashU’s Azure tenant. Further, users can track their token usage and budget in real-time.

# Key Features
* Access to several OpenAI models in WashU secure environment
* Ability to preset a fixed budget for usage
* Programmatic access to APIs
* Access is limited to WashU networks and VPN
* Usage Instructions
* To request access to the APIs, please submit a request via ServiceNow. (Coming soon.)

# Credentials
To access the API endpoints, you’ll have to be on the WashU network OR you will need to VPN to the WashU network. (VPN instructions can be found at it.wustl.edu/items/connect)

The API endpoints use Microsoft OAuth 2.0 token. A token must be retrieved before an API call can be made.

The following information is needed to retrieve a token:

* **Send a POST to the token URL:** https://login.microsoftonline.com/4ccca3b5-71cd-4e6d-974b-4d9beb96c6d6/oauth2/v2.0/token
* **Client ID:** This is provided to you with these instructions. The Client ID is unique for your research group.
* **Client Secret:** This is the password that will be sent to you when you receive your Client ID. It is essential that only authorized users have access to this password per the WashU Information Security Password Policy.
Once the token is retrieved, you can then make a call to the API endpoint. To call the API endpoint, you’ll need to specify the Scope and the API endpoint that you want to call.

The Scope that you will need to use for the production environment is: api://bbeee386-60d6-4ba4-b9a7-631763f66065/.default

If you are testing another environment, WashU IT or the DI2 Accelerator will notify you if your scope needs to be changed.

Here are API endpoints you may use:
 
## Completions:

https://api.openai.wustl.edu/base-gpt-4-8k/v1/chat/completions

https://api-test.openai.wustl.edu/base-gpt-4o-128k/v1/chat/completions

## Embeddings:

https://api.openai.wustl.edu/base-text-embedding-3-small/v1/embeddings

Details on the input and outputs of this API can be referenced here: https://learn.microsoft.com/en-us/azure/ai-services/openai/reference

Example Python code can be found in the source code of this repository. 