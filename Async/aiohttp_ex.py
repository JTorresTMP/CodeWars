import aiohttp, asyncio, json


brewery_url = 'https://api.openbrewerydb.org/breweries'

brew_params = {
    'by_postal': '92626'
}

age_url = 'https://api.agify.io'

age_params = {'name': 'Andrea'}

ron = 'https://ron-swanson-quotes.herokuapp.com/v2/quotes'

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(ron + '/4') as resp:
            print(resp.status)
            print(await resp.text())
        await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())