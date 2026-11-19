import sys
from datetime import datetime

# Đảm bảo hiển thị tiếng Việt có dấu trên Windows terminal
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("Xin chào! Môi trường của tôi đã sẵn sàng cho khóa học AI Agent 101!")
print(f"Thời gian hiện tại: {now}")
