import streamlit as st
import random
import time

# Danh sách màu sắc để áp dụng cho văn bản
text_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Danh sách các thông điệp
messages = [
    "HÉP PI BỚT ĐÂY CHỊ 🐼",  # Đổi thông điệp ở đây
    "CHÚC CHỊ 8386! 💖",
    "VẠN SỰ NHƯ MƠ! 🌸",
    "MÃI ĐỈNH MÃI ĐỈNH! 💪",
]

# Danh sách các hình ảnh bóng bay (hoặc emoji bóng bay)
balloon_emoji = "🎈"  # Hoặc thay thế bằng URL của ảnh bóng bay nếu muốn sử dụng hình ảnh thật

# Kích thước màn hình điện thoại
screen_width = 375  # Chiều rộng màn hình điện thoại
screen_height = 667  # Chiều cao màn hình điện thoại

# Tiêu đề ứng dụng đã sửa đổi
st.title("HACKER ẤN VÀO MẤT NICK 👾🐼")

# Hàm để tạo hiệu ứng dích dắc cho thông điệp
def display_random_effect():
    message_height = 40  # Chiều cao của mỗi thông điệp (để điều chỉnh khoảng cách giữa các thông điệp)
    num_messages = 10  # Số lượng thông điệp xuất hiện tại cùng một thời điểm (tùy chỉnh số lượng)
    
    # Vị trí y cố định ở phần trên màn hình
    max_y_position = screen_height // 3  # Các thông điệp chỉ xuất hiện ở phần trên màn hình (1/3 trên của màn hình)
    
    for _ in range(num_messages):  # Hiển thị một số lượng thông điệp có trật tự
        # Chọn màu ngẫu nhiên từ danh sách
        chosen_color = random.choice(text_colors)
        # Chọn thông điệp ngẫu nhiên từ danh sách
        message = random.choice(messages)
        
        # Điều chỉnh vị trí y của thông điệp để các thông điệp xuất hiện ở phần trên màn hình
        y_position_message = random.randint(0, max_y_position - message_height)
        
        # Vị trí x được điều chỉnh để thông điệp không bị chồng lên nhau
        x_position_message = random.randint(0, screen_width - 150)
        
        # Hiển thị lời chúc tại vị trí ngẫu nhiên với màu sắc ngẫu nhiên, sử dụng hiệu ứng di chuyển dích dắc
        st.markdown(
            f'<style>'
            f'@keyframes moveX{{'
            f'0% {{ transform: translateX(0px); }}'
            f'50% {{ transform: translateX(30px); }}'
            f'100% {{ transform: translateX(0px); }}'  # Di chuyển dích dắc trái phải
            f'}}'
            f'</style>'
            f'<span style="font-size: 20px; color: {chosen_color}; background-color: pink; '
            f'padding: 10px; border-radius: 10px; position: absolute; top: {y_position_message}px; left: {x_position_message}px; '
            f'animation: moveX 2s ease-in-out infinite;">'  # Thêm hiệu ứng di chuyển dích dắc
            f'{message}</span>',
            unsafe_allow_html=True
        )
        
        # Hiển thị bóng bay ở vị trí ngẫu nhiên (ở trên màn hình) với hiệu ứng di chuyển lên xuống
        x_position_balloon = random.randint(0, screen_width - 50)
        y_position_balloon = random.randint(0, max_y_position)  # Để bóng bay xuất hiện phần trên màn hình
        
        st.markdown(
            f'<style>'
            f'@keyframes moveBalloon{{'
            f'0% {{ transform: translateY(0px); }}'
            f'50% {{ transform: translateY(-30px); }}'
            f'100% {{ transform: translateY(0px); }}'  # Di chuyển bóng bay lên xuống
            f'}}'
            f'</style>'
            f'<span style="font-size: 30px; position: absolute; top: {y_position_balloon}px; left: {x_position_balloon}px; '
            f'animation: moveBalloon 3s ease-in-out infinite;">'
            f'{balloon_emoji}</span>',
            unsafe_allow_html=True
        )
        
        time.sleep(0.5)  # Thời gian giữa mỗi lần hiển thị, giảm để hiệu ứng xuất hiện nhanh hơn

# Tạo nút để bắt đầu hiệu ứng
if st.button("Nhấn vào đây để nhận 🎁"):
    display_random_effect()

# Footer
st.write("")
