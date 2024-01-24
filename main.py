from typing import Union
import uvicorn

from fastapi import FastAPI
from vutru.vutrutuvi import thienban 



app = FastAPI()
@app.get("/")
def read_root():

  a = thienban()
  print(a.tuvi.NguHanh.sinhxuat)

  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)