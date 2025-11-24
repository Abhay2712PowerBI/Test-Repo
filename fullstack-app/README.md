# fullstack-app

This repository contains a minimal scaffold for a fullstack application.

Structure:

- `fullstack-app/client` — React frontend (Vite)
- `fullstack-app/server` — Node + Express backend
- `docker-compose.yml` — example compose file (optional)
- `.github/workflows` — CI/CD workflow examples

Quick local run (PowerShell):

```powershell
# Server
cd fullstack-app\server
npm install
npm test            # run tests
npm start           # start server (port 4000)

# In another terminal: Client
cd fullstack-app\client
npm install
npm run dev         # starts Vite dev server (port 5173)
```

Notes:
- The scaffold includes example tests for the server using Jest + Supertest.
- Dockerfiles are not included in this scaffold. The `docker-compose.yml` is an example only.
- CI workflow `fullstack-ci.yml` builds the client and runs server tests.
