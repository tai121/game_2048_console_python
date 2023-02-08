# Làm game 2048 đơn giản với Python
## 1. Giới thiệu về game 2048

2048 chơi trên một lưới vuông 4×4. Mỗi lần di chuyển là một lượt, người chơi sử dụng các phím mũi tên và các khối vuông sẽ trượt theo một trong bốn hướng tương ứng (lên, xuống, trái, phải). Mỗi lượt có một khối có giá trị 2 hoặc 4 sẽ xuất hiện ngẫu nhiên ở một ô trống trên lưới.

## 2. Tạo file lưu các hằng
Ta tạo file **constant.py** để lưu danh sách các hằng được sử dụng trong project. Mục đích của việc này là giúp chúng ta dễ quản lý các hằng hơn đặc biệt là khi thay đổi giá trị sẽ không phải tìm tất cả các file có chứa hằng đó để sửa.
```python 
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
LENGTH_OF_SQUARE = 4
```
Ở đây ta dùng <kbd>w</kbd>, <kbd>s</kbd>, <kbd>a</kbd>, <kbd>d</kbd> tương ứng với các hành động lên, xuống, trái, phải. Trong bài viết này mình sẽ sử dụng lưới ô vuông 4×4, các bạn có thể thay đổi tùy ý.
## 3. Tạo class game
![Example Image](https://drive.google.com/uc?id=1gIhqYU8EY5ex2xxOdWZeFRInyzJUEsTe)
* board: đây là lưới lưu giá trị của các ô vuông
* max_value: là giá trị ô lớn nhất trong lưới, nếu giá trị này bằng 2048 thì người chơi sẽ thắng
* score
