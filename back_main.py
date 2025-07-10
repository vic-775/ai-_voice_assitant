from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from livekit import agents
from run_agent import entrypoint
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  # ← make sure environment variables are loaded

app = FastAPI()

# Serve frontend files from /frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

@app.on_event("startup")
async def start_worker():
    opts = agents.WorkerOptions(
        entrypoint_fnc=entrypoint,
    )
    worker = agents.Worker(opts)
    asyncio.create_task(worker.run())

