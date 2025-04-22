from fastapi import FastAPI
from kubernetes import client, config
import uuid
import os

app = FastAPI()

# Try to load in-cluster config first, fall back to local config
try:
    config.load_incluster_config()
except:
    config.load_kube_config()

@app.post("/start-workspace")
def start_workspace(repo_url: str = "https://github.com/octocat/Hello-World.git"):
    pod_name = f"workspace-{uuid.uuid4().hex[:6]}"
    pod = client.V1Pod(
        metadata=client.V1ObjectMeta(name=pod_name),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name="worker",
                    image="workspace-image:latest",
                    image_pull_policy="Never",
                    env=[client.V1EnvVar(name="REPO_URL", value=repo_url)],
                )
            ],
            restart_policy="Never"
        )
    )
    api = client.CoreV1Api()
    api.create_namespaced_pod(namespace="default", body=pod)
    return {"status": "started", "pod_name": pod_name}
