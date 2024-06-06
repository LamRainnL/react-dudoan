document.addEventListener('DOMContentLoaded', function () {
  // Mở modal khi trang web tải
  var myModal = new bootstrap.Modal(document.getElementById('myModal'));
  myModal.show();

  // Ngăn không cho modal tắt nếu chưa nhập thông tin
  var modalElement = document.getElementById('myModal');
  modalElement.addEventListener('hide.bs.modal', function (event) {
    var inputField = document.getElementById('username');
    if (inputField.value.trim() === "") {
      event.preventDefault();
    }
  });

  // Đóng modal khi người dùng nhập thông tin và submit form
  var modalForm = document.getElementById('modalForm');
  modalForm.addEventListener('submit', function (event) {
    var inputField = document.getElementById('username');
    event.preventDefault();
    if (inputField.value.trim() !== "") {
      myModal.hide();
      // Lấy giá trị từ input
      var inputData = document.getElementById('username').value;

      // Hiển thị giá trị trong div kết quả
      document.getElementById('name_user').innerText = 'Xin chào: ' + inputData;
    }
  });



});