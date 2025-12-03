# Docker Flask Mood App

Simple Flask app that provides mood responses. Fully containerized with Docker, CI/CD via GitHub Actions, and deployed on Render. Easy to extend and scale.

---

## Project Focus

This project is primarily created to demonstrate **CI/CD, DevOps, and Docker workflows**.  
It is **not intended as a full-featured application**, but rather as a hands-on example of:

- Automating builds and deployments with GitHub Actions  
- Containerizing applications with Docker  
- Deploying services to a cloud platform (Render)  
- Setting up a simple, reproducible DevOps pipeline



## Tech Stack
- **Backend:** Python 3.13, Flask  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions → Docker Hub → Render.com  
- **Hosting:** Render (free plan supported)  

---

## Features
- Simple REST endpoints (`/`, `/mood`)  
- Containerized for portability  
- Automatic deployment via CI/CD pipeline  
- Ready for further development  

---

## Project Structure

docker_flask_mood_app/
│
├─ app.py
├─ Dockerfile
├─ requirements.txt
├─ compose.yaml
│
├─ templates/
│   └─ index.html
│
├─ tests/
│   ├─ __init__.py
│   └─ test_app.py
│
└─ .github/
    └─ workflows/
        └─ python-app.yml



---

## Run Locally

Clone repo and build/run Docker container:

```bash
git clone https://github.com/RhayemSaidi/docker_flask_mood_app.git
cd docker_flask_mood_app
docker build -t docker_flask_mood_app .
docker run -p 8000:8000 docker_flask_mood_app
```

## Deployment

- Push to `main` branch on GitHub.
- GitHub Actions builds Docker image.
- Image is pushed to Docker Hub.
- Render automatically pulls the image and deploys the service.
- Live URL: [https://docker-flask-mood-app.onrender.com](https://docker-flask-mood-app.onrender.com)

## CI/CD Pipeline (DevOps Focus)

**Trigger:** Push to `main` branch  

**Actions:**
- Build Docker image
- Push image to Docker Hub
- Deploy to Render automatically

**Benefits:** Fully automated deployment, easy updates, portable environment

## Notes

- Exposed port: `8000`
- Currently uses Flask development server; switch to production WSGI server (e.g., Gunicorn) for scaling
- Lightweight, easy to extend with new endpoints or features

