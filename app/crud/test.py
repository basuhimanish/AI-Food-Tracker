from pyzbar import pyzbar
import cv2

def scan_barcode_live():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            barcode_data = barcode.data.decode("utf-8")
            cap.release()
            cv2.destroyAllWindows()
            print(barcode_data)
            return barcode_data  # Return the first barcode data found

        cv2.imshow('Barcode Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the loop
            break

    cap.release()
    cv2.destroyAllWindows()

    return None  # In case no barcode is scanned and loop is exited


scan_barcode_live()