import cv2
from ultralytics import YOLO
from pathlib import Path

# ─── CONFIG ───────────────────────────────────────────────────────────────────
MODEL_PATH = "best.pt"   # ← change this to your best.pt path
CONF_THRESHOLD = 0.4
# ──────────────────────────────────────────────────────────────────────────────

def main():
    # Load model
    model = YOLO(MODEL_PATH)
    print(f"✅ Model loaded: {Path(MODEL_PATH).name}")
    print(f"📦 Classes ({len(model.names)}): {model.names}\n")

    # Open camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    print("🎥 Camera open — press Q to quit\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to grab frame")
            break

        # Run inference
        results = model(frame, conf=CONF_THRESHOLD, verbose=False)[0]

        # Draw boxes
        annotated = results.plot()

        # Show FPS + class count in corner
        n_det = len(results.boxes)
        cv2.putText(annotated, f"Detections: {n_det}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("YOLO Camera Test — press Q to quit", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Done")

if __name__ == "__main__":
    main()