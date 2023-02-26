import uvicorn

from schedule.schedule_loop import ScheduleEventLoop

from config import Config

Config("../config/config.yaml")

if __name__ == "__main__":
    # event process loop as a thread
    event_loop = ScheduleEventLoop(Config.evt_queue())
    event_loop.start()

    # fast api
    uvicorn.run(
        "api.api_main:fast_api",
        host="0.0.0.0",
        port=9901,
        log_level="info",
        reload=True,
    )