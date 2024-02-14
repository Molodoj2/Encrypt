function sendData() {
    var method = document.getElementById("method").value;
    var inputText = document.getElementById("input_text").value;
    var encryptionKey = document.getElementById("encryption_key").value;
    var action = document.querySelector('input[name="action"]:checked').value; // Получаем значение выбранной радиокнопки "action"

    // Создаем объект FormData для передачи данных формы
    var formData = new FormData();
    formData.append('method', method);
    formData.append('input_for_encrypt', inputText);
    formData.append('encryption_key', encryptionKey);
    formData.append('action', action);

    // Отправляем данные на сервер с помощью fetch API
    fetch("{% url 'test_front' %}", {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text(); // Можете возвращать другой тип данных в зависимости от того, что вам нужно
    })
    .then(data => {
        console.log(data); // Выводим ответ сервера в консоль
        // Делаем что-то с ответом от сервера, если это необходимо
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}
