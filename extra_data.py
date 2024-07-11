from uuid import UUID
from datetime import datetime, time, timedelta

from fastapi import FastAPI, Body

app = FastAPI()


@app.put("/items/{item_id}")
async def read_item(
    item_id: UUID,
    start_date: datetime | None = Body(None),
    end_date: datetime | None = Body(None),
    repeat_at: time | None = Body(None),
    process_after: timedelta | None = Body(None),
):
    start_date = start_date or datetime.now()
    end_date = end_date or datetime.now()
    repeat_at = repeat_at or time(hour=1, minute=1)
    process_after = process_after or timedelta(minutes=10)
    start_process = start_date + process_after
    duration = end_date - start_process
    return {
        "item_id": item_id,
        "start_date": start_date,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
