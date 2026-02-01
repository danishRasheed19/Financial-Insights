import json
from fastapi import FastAPI
from contextlib import asynccontextmanager
import data.personality_questions.questions_data as qdata
from routers.personality import router as PersonalityRouter
from routers.auth import router as auth
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup section
    with open("data/personality_questions/questions.json", "r", encoding="utf-8") as f:
        qdata.QUESTIONS.clear()           # keep the reference
        qdata.QUESTIONS.extend(json.load(f))
    qdata.QUESTION_MAP.clear()
    qdata.QUESTION_MAP.update({q["id"]: q["trait"] for q in qdata.QUESTIONS})
    print(f"✅ Loaded {len(qdata.QUESTIONS)} questions")

    yield  # <-- Application runs here

    # Shutdown section (optional)
    print("👋 App shutting down...")

# Create app with lifespan
app = FastAPI(lifespan=lifespan)
app.include_router(PersonalityRouter)
app.include_router(auth)

origins = [
    "http://localhost:3000",  # Next.js dev
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # allows cookies, auth headers
    allow_methods=["*"],      # allow all HTTP methods
    allow_headers=["*"],      # allow all headers
)


