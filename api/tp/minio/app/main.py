from fastapi import FastAPI, File, UploadFile
from minio import Minio
from datetime import timedelta

client = Minio("minio:9000", "root", "rootpassword", secure=False)

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

@app.post('/file/upload/')
async def upload_file(file: UploadFile = File(...)):
    result = client.put_object("photo-bucket", file.filename, file.file, length=5000)
    return {'result': result}

@app.get('/file/pregisned_url/')
async def upload_file(name: str):
    get_url= client.get_presigned_url(
    "GET",
    "photo-bucket",
    name,
    expires=timedelta(days=1),
    response_headers={"response-content-type": "application/json"},
)
    return get_url

@app.get('/show_buckets')
async def show_buckets(name_bucket : str):
    objects = client.list_objects(name_bucket, recursive=True)
    list_name= []
    for obj in objects:
        list_name.append(obj.object_name)
    return list_name




