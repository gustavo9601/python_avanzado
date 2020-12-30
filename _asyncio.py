import asyncio

# pip install asyncio

async def slow_operations(future):
    await asyncio.sleep(2)
    future.set_result('Future is donde')

def got_result(future):
    print(future.result())
    loop.stop()


loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operations(future))
future.add_done_callback(got_result)

try:
    loop.run_forever()
finally:
    loop.close()