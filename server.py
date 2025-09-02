#!/usr/bin/env python3
"""Web server template for Caminu-generated agents"""

import asyncio
import os
import logging
from typing import Any, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from agent import agent
from agents import Runner

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Holiday Hero Letterwriter (Action-Icon Inspired)",
    description="Users want a fun, personalized Christmas letter that evokes the high-energy, motivational, tongue-in-cheek persona of a famous Austrian-born action icon without directly impersonating or claiming to be that person. The agent should transform a user-provided topic into a festive letter that captures high-level stylistic traits (confidence, gym/motivation vibes, playful action references, warm holiday wishes) while complying with style-transformation and impersonation policies.",
    version="1.0.0"
)

class AgentRequest(BaseModel):
    prompt: str = "Please demonstrate your functionality."

class AgentResponse(BaseModel):
    response: str
    status: str = "success"

@app.get("/")
async def root():
    return {
        "message": "Welcome to Holiday Hero Letterwriter (Action-Icon Inspired)",
        "endpoints": {
            "POST /generate": "Generate a response from a prompt",
            "GET /health": "Health check"
        }
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "holiday-hero-letterwriter-action-icon-inspired"}

@app.post("/generate", response_model=AgentResponse)
async def generate(request: AgentRequest):
    try:
        logger.info(f"Processing request: {request.prompt[:100]}...")
        result = await Runner.run(agent, request.prompt)
        return AgentResponse(
            response=result.final_output,
            status="success"
        )
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )