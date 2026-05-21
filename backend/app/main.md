# backend/app/main.py

## Purpose

This file defines the FastAPI application entry point for the EUDI Relying Party Integration Bus.

## Responsibilities

- Create the FastAPI application instance.
- Define global application metadata.
- Provide a basic health check endpoint.

## Current Endpoints

### GET /health

Returns a simple status response to confirm that the backend is running.

Example response:

```json
{
  "status": "ok"
}