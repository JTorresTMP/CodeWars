import aiohttp
import asyncio, time, json

client_api_key = '251_5btkfzb0v8084w08c08gkgcc4cgcccwkog0840cckkw0wgscog'
client_secret = '3d6iixzstz40g8oos8cck0gw8oo8ws4ccc8kcsc8wcccos4ksk'

request_token_url = 'https://api.rewardify.ca/oauth/v2/token'
retrieve_customer_info_url = 'https://api.rewardify.ca/customer'

token_request_params = {
    'grant_type': 'client_credentials',
    'client_id': client_api_key,
    'client_secret': client_secret
}

params = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'}








# async def main():
#     async with aiohttp.ClientSession() as session:
#         # token = json['access_token']
#         # token = await get_token()
#         print(json)

# #async with session.get(url, params = params) as resp:
# def get_token():
#     token_request = session.post(request_token_url, params = token_request_params)
#     json = token_request.json()   
#     return json['access_token']


# async def fetch(session, url, params):
#     async with session.get(url, params) as response:
#         print(response.status)
#         return await response.text()



# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())


#To Make an HTTP POST request we use session.post(url, data = b'data')
