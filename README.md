# HNGi13 Stage 0 RESTful API — Dynamic Profile Endpoint

This is a simple RESTful API that returns your profile information along with a dynamic cat fact fetched from an external API. Built with **Python** and **FastAPI**, and containerized using **Docker**.

---

## Features

- GET `/me` endpoint
- Returns JSON response with:
  - `status` — always `"success"`
  - `user` — your profile info (`email`, `name`, `stack`)
  - `timestamp` — current UTC time in ISO 8601 format ending with `Z`
  - `fact` — a random cat fact from [Cat Facts API](https://catfact.ninja/fact)
- Dynamic timestamp and cat fact with every request
- Graceful fallback if Cat Facts API fails

---

## Project Structure

