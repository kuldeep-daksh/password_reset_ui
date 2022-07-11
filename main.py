import requests
from fastapi import FastAPI, Request, File, Form, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

url = " http://127.0.0.1:8001/change_password/"
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
from pydantic import BaseModel


class userDataPasswordReset(BaseModel):
    username: str
    password: str
    newPassword: str
    confirmPassword: str


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # import pdb;
    # pdb.set_trace()
    return templates.TemplateResponse("item.html", {"request": request, })


@app.post("/password_change")
def password_change(username: str = Form(), password: str = Form(),
                    newPassword: str = Form(), confirmPassword: str = Form()):
    # import pdb; pdb.set_trace()
    # print(type(username))
    print(f"username is ==== ===   == {username}")
    print(f"password is ==== ===   == {password}")
    print(f"new_password is ==== ===   == {newPassword}")
    print(f"confirm_password is ==== ===   == {confirmPassword}")
    data = json.dumps({"name": username, "password": password, "new_password": newPassword,
                       "confirm_password": confirmPassword})
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("An Http Error occurred:" + repr(errh))
    except requests.exceptions.ConnectionError as errc:
        print("An Error Connecting to the API occurred:" + repr(errc))
    except requests.exceptions.Timeout as errt:
        print("A Timeout Error occurred:" + repr(errt))
    except requests.exceptions.RequestException as err:
        print("An Unknown Error occurred" + repr(err))
    else:
        print(response.status_code)
        print(response.json())


@app.post("/password_reset", response_class=HTMLResponse)
async def password_reset(request: Request, adminname: str = Form(), password: str = Form(), username: str = Form(),
                         new_password: str = Form(), confirm_password: str = Form()):
    print(f"username is ==== ===   == {Form}")
    print(f"password is ==== ===   == {password}")
    print(f"new_password is ==== ===   == {new_password}")
    print(f"confirm_password is ==== ===   == {confirm_password}")
    return json.dumps({"adminname": adminname, "username": username, "password": password, "new_password": new_password,
                       "confirm_passwod": confirm_password})
