1. Build the Docker Image 

`docker build -t toolbox-app .`

2. Configure Authentication

`gcloud auth configure-docker asia-southeast2-docker.pkg.dev`

3. Tag the Image for the Registry

`docker tag toolbox-app asia-southeast2-docker.pkg.dev/eikon-dev-ai-team/toolbox/toolbox:latest`

4. Push the Image

`docker push asia-southeast2-docker.pkg.dev/eikon-dev-ai-team/toolbox/toolbox:latest`

5. Create the Secret (Run this only if you haven't created the secret yet)
`gcloud secrets create tools --data-file=tools.yaml`

6. Deploy the Service to Cloud Run
```
export IMAGE=asia-southeast2-docker.pkg.dev/eikon-dev-ai-team/toolbox/toolbox:latest 

gcloud run deploy toolbox \
--image $IMAGE \
--region asia-southeast2 \
--set-secrets "/app/tools.yaml=tools:latest" \
--args="--tools-file=/app/tools.yaml","--address=0.0.0.0","--port=8080" \
--allow-unauthenticated
```

Ref:
- https://googleapis.github.io/genai-toolbox/getting-started/introduction/

- https://googleapis.github.io/genai-toolbox/how-to/deploy_toolbox/