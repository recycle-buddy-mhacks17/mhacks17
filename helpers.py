import os
import uuid

from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=os.environ.get("ROBOFLOW_API_KEY")
)

def save_image_to_folder(image):
    if not os.path.exists("images"):
        os.makedirs("images")
    
    # save the imaghe with a UNIQUE name using uuid
    image_path = os.path.join("images", f"{uuid.uuid4()}.jpg")
    with open(image_path, "wb") as f:
        f.write(image.read())
    
    return image_path

def infer_image(image_path):
    result = client.run_workflow(
        workspace_name="mohammad-rwoer",
        workflow_id="img-desc-workflow",
        images={
            "image": image_path
        }
    )
    return result