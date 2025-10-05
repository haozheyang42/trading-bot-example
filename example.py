from huqt_oracle_pysdk import OracleClient, Side, Tif
import asyncio
haorzhe = OracleClient()

async def trade_handler():
    print("\n\033[1;32m-------- Below are the logs for user algorithm --------\033[0m")
    print(haorzhe.get_self_positions())
    await haorzhe.place_limit_order("110", Side.Buy, 200, 1, Tif.Gtc)

async def main():
    ## change these lines for only the markets you want
    await haorzhe.start_client(
        account="",
        api_key="",
        domain="Oracle"
    )

    await haorzhe.subscribe_market("110")

    ## DO NOT CHANGE BELOW THIS LINE
    task = asyncio.create_task(trade_handler())
    try:
        # CTRL-C to stop
        await asyncio.Event().wait()
    except:
        pass
    finally:
        task.cancel()
        await haorzhe.stop_client()
        print("\033[1;31mOracleClient stopped. See ya next time...\033[0m\n")

if __name__ == "__main__":
    asyncio.run(main())