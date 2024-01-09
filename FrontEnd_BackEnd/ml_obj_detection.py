from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image

def detect(file):
    image = Image.open(file)

    # Check if the image has only two dimensions
    if len(image.size) == 2:
        # Convert grayscale image to RGB (3 channels)
        image = image.convert("RGB")


    # you can specify the revision tag if you don't want the timm dependency
    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
    model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # convert outputs (bounding boxes and class logits) to COCO API
    # let's only keep detections with score > 0.9
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]



    out_response = []

    for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
        box = [round(i, 2) for i in box.tolist()]
        print(
                f"Detected {model.config.id2label[label.item()]} with confidence "
                f"{round(score.item(), 3)} at location {box}"
        )

        out_response.append((model.config.id2label[label.item()],round(score.item(), 3)))


    return out_response