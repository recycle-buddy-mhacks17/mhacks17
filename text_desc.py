from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="ROBOFLOW_KEY"
)

result = client.run_workflow(
    workspace_name="ROBOFLOW_WORKSPACE",
    workflow_id="img-desc-workflow",
    images={
        "image": "20240928_170043.jpg"
    }
)

print(result)