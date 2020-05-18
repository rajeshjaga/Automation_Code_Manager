# import asyncio

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')


# asyncio.run(main())






import os 
try:
    os.system('hello')
except OSError as error:
    print (error)