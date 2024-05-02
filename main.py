from get_response import get_response
from recognition import record, recognize
from speech import speak
import asyncio

async def main():
    record()
    query = recognize()
    response = get_response(query)
    print(response)
    await speak(response)


if __name__ == '__main__':
    asyncio.run(main())
