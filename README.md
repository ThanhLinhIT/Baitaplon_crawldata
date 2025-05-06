# Thu thập Dữ liệu Bất động sản
1. Giới thiệu
Đây là đoạn mã Python tự động thu thập dữ liệu bất động sản tại Đà Nẵng từ trang web [batdongsan.so](https://batdongsan.so/). Công cụ được lập trình để chạy vào lúc 6 giờ sáng mỗi ngày, thu thập thông tin về các bất động sản đang được rao bán và lưu trữ dữ liệu vào file CSV.

2. Tính năng chính
- Truy cập vào trang batdongsan.so.
- Tự động chọn khu vực **Đà Nẵng** và loại **Bán biệt thự** , bấm **Tìm kiếm**.
- Crawl dữ liệu từ các bài đăng: **Tiêu đề, Mô tả, Giá, Diện tích, Địa chỉ**.
- Hỗ trợ chuyển trang (next page).
- Lưu dữ liệu vào file: `btl_alonhadat_danang.csv`.
- Tự động chạy hàng ngày lúc **6:00 sáng**.

3. Yêu cầu hệ thống
- Python 3.6 trở lên
- Các thư viện Python được liệt kê trong file requirements.txt
- Trình duyệt Chrome và ChromeDriver

4. Cách sử dụng
- Chạy chương trình: `python btl_crawldata_bds.py`
- Chương trình sẽ tự động chạy vào lúc 6 giờ sáng hàng ngày
- Dữ liệu thu thập được sẽ được lưu vào file `btl_alonhadat_danang.csv`